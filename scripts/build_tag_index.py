#!/usr/bin/env python3
"""Build compact web-first tag lookup shards from the Good Anima upstream index.

The full upstream JSON is downloaded only by CI. Runtime web models fetch a
small root manifest, relevant group manifests, and only the needed tag shards.
"""
import argparse
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from collections import defaultdict

SOURCE_URL = "https://raw.githubusercontent.com/ShiroEirin/comfyui-good-anima/main/danbooru-tags/tags_index.json"
SOURCE_REPO = "https://github.com/ShiroEirin/comfyui-good-anima"
SCHEMA_VERSION = 1
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_DIR = os.path.join(ROOT, "bundle", "tag-index")


def fetch_source():
    request = urllib.request.Request(
        SOURCE_URL,
        headers={"User-Agent": "Tera-Dark-personal-agent-skills tag-index builder", "Accept": "application/json"},
    )
    last_error = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                raw = response.read()
            payload = json.loads(raw.decode("utf-8"))
            if not isinstance(payload, dict) or not payload:
                raise ValueError("upstream tag index is not a non-empty JSON object")
            if any(not isinstance(group, str) or not isinstance(rows, list) for group, rows in payload.items()):
                raise ValueError("upstream tag index has an unexpected group schema")
            return payload, hashlib.sha256(raw).hexdigest()
        except (OSError, urllib.error.URLError, json.JSONDecodeError, ValueError) as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise SystemExit(f"Unable to retrieve/validate upstream tag index after 3 attempts: {last_error}")


def safe_group(group):
    safe = re.sub(r"[^a-z0-9_-]", "_", group.lower())
    if not safe:
        raise ValueError(f"unsafe empty group name: {group!r}")
    return safe


def lookup_name(tag, group):
    """Return a location-only name; never use this value for identity comparison."""
    value = tag.lower()
    if group.lower() == "artists":
        if value.startswith("artist:"):
            value = value[len("artist:"):]
        elif value.startswith("@"):
            value = value[1:]
    return value


def prefix_for(tag, group):
    value = lookup_name(tag, group)
    if not value or not re.match(r"^[a-z0-9]", value):
        return "_special"
    # Artist data is more alias-dense than other groups; use a 3-character route key.
    width = 3 if group.lower() == "artists" else 2
    return re.sub(r"[^a-z0-9_]", "_", value[:width])


def generate_outputs(source, source_sha):
    outputs = {}
    group_meta = {}
    for group in sorted(source):
        by_prefix = defaultdict(lambda: {"exact": {}, "aliases": {}})
        rows = source[group]
        valid_count = 0
        for row in rows:
            if not isinstance(row, list) or len(row) < 3 or not isinstance(row[0], str):
                raise ValueError(f"invalid row in upstream group {group!r}: {row!r}")
            canonical = row[0]
            count = row[1] if isinstance(row[1], int) else None
            aliases_text = row[2] if isinstance(row[2], str) else ""
            valid_count += 1
            by_prefix[prefix_for(canonical, group)]["exact"][canonical] = {
                "canonical": canonical,
                "count": count,
            }
            for alias in aliases_text.split(","):
                alias = alias.strip()
                if not alias:
                    continue
                hits = by_prefix[prefix_for(alias, group)]["aliases"].setdefault(alias, [])
                hit = {"canonical": canonical, "count": count, "origin": "source_alias"}
                if hit not in hits:
                    hits.append(hit)

            # Explicit namespace bridge: an upstream @name artist may be queried
            # through the Harness's NAI5 artist:name namespace. This is identity-
            # exact only; no fuzzy matching or punctuation normalization occurs.
            if group.lower() == "artists" and canonical.startswith("@") and len(canonical) > 1:
                bridge = "artist:" + canonical[1:]
                bridge_hits = by_prefix[prefix_for(bridge, group)]["aliases"].setdefault(bridge, [])
                bridge_hit = {"canonical": canonical, "count": count, "origin": "namespace_bridge:artist_to_at"}
                if bridge_hit not in bridge_hits:
                    bridge_hits.append(bridge_hit)

        safe = safe_group(group)
        prefixes = sorted(by_prefix)
        group_manifest_path = f"bundle/tag-index/{safe}/manifest.json"
        group_meta[group] = {
            "path_group": safe,
            "tag_count": valid_count,
            "shard_count": len(prefixes),
            "prefix_length": 3 if group.lower() == "artists" else 2,
            "manifest": group_manifest_path,
        }
        group_manifest = {
            "schema_version": SCHEMA_VERSION,
            "source_sha256": source_sha,
            "group": group,
            "tag_count": valid_count,
            "prefix_length": 3 if group.lower() == "artists" else 2,
            "prefixes": prefixes,
        }
        outputs[group_manifest_path] = json.dumps(
            group_manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ) + "\n"

        for prefix in prefixes:
            shard = by_prefix[prefix]
            shard["aliases"] = {
                alias: sorted(hits, key=lambda item: (item["canonical"], item["origin"]))
                for alias, hits in sorted(shard["aliases"].items())
            }
            payload = {
                "_meta": {
                    "schema_version": SCHEMA_VERSION,
                    "source_sha256": source_sha,
                    "source_url": SOURCE_URL,
                    "group": group,
                    "prefix": prefix,
                },
                "exact": dict(sorted(shard["exact"].items())),
                "aliases": shard["aliases"],
            }
            rel = f"bundle/tag-index/{safe}/{prefix}.json"
            outputs[rel] = json.dumps(
                payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
            ) + "\n"

    root_manifest = {
        "schema_version": SCHEMA_VERSION,
        "source": {
            "repository": SOURCE_REPO,
            "url": SOURCE_URL,
            "sha256": source_sha,
            "license": "GPL-3.0",
        },
        "lookup": {
            "group_isolation": True,
            "prefix_length_by_group": {"artists": 3, "default": 2},
            "prefix_rule": "For file routing only: lowercase the candidate; in group artists, strip a leading artist: or @ before selecting three characters; in other groups select two. If the resulting first character is not ASCII a-z or 0-9 use _special; replace non-[a-z0-9_] characters within the selected prefix with _. Never alter the candidate used for exact identity matching.",
            "lookup_order": ["exact", "alias"],
            "ambiguous_alias": "not promoted; treat as missing",
        },
        "groups": group_meta,
    }
    outputs["bundle/tag-index/manifest.json"] = json.dumps(
        root_manifest, ensure_ascii=False, sort_keys=True, indent=2
    ) + "\n"
    outputs["bundle/tag-index/NOTICE.md"] = (
        "# Third-party tag-index notice\n\n"
        "Generated lookup shards are derived from the Good Anima tag index.\n\n"
        f"- Source repository: {SOURCE_REPO}\n"
        f"- Source file: {SOURCE_URL}\n"
        "- Data license: GPL-3.0 (see the upstream repository's license).\n"
        "- This derived dataset has separate provenance/licensing from the Harness source code; the root MIT license does not relicense this dataset.\n"
        f"- Source SHA-256: {source_sha}\n"
    )
    return outputs


def run_self_tests():
    cases = [
        ("1girl", "general", "1g"),
        ("37_(reverse:1999)", "characters", "37"),
        ("white_background", "general", "wh"),
        ("artist:starshadowmagician", "artists", "sta"),
        ("@starshadowmagician", "artists", "sta"),
        ("(special_tag)", "general", "_special"),
        (":smile:", "general", "_special"),
    ]
    for tag, group, expected in cases:
        actual = prefix_for(tag, group)
        if actual != expected:
            raise SystemExit(
                f"self-test failed: prefix_for({tag!r}, {group!r})={actual!r}, expected {expected!r}"
            )
    sample = generate_outputs(
        {"general": [["long_hair", 12, "long-hair,logn_hair"], ["smile", 7, ":)"]],
         "artists": [["@starshadowmagician", 8, "@star_shadow_magician"]]},
        "test-sha",
    )
    alias_shard = json.loads(sample["bundle/tag-index/general/lo.json"])
    if alias_shard["aliases"].get("long-hair", [{}])[0].get("canonical") != "long_hair":
        raise SystemExit("self-test failed: exact alias did not resolve to canonical tag")
    if "long_hair" not in alias_shard["exact"]:
        raise SystemExit("self-test failed: canonical tag missing from exact map")
    artist_manifest = json.loads(sample["bundle/tag-index/artists/manifest.json"])
    if artist_manifest["prefixes"] != ["sta"] or artist_manifest["prefix_length"] != 3:
        raise SystemExit(f"self-test failed: artist prefixes incorrectly generated: {artist_manifest!r}")
    artist_shard = json.loads(sample["bundle/tag-index/artists/sta.json"])
    if "@starshadowmagician" not in artist_shard["exact"]:
        raise SystemExit("self-test failed: artist source canonical identity was altered")
    bridge = artist_shard["aliases"].get("artist:starshadowmagician", [{}])[0]
    if bridge.get("canonical") != "@starshadowmagician" or bridge.get("origin") != "namespace_bridge:artist_to_at":
        raise SystemExit("self-test failed: NAI5-to-Anima artist namespace bridge missing or mislabelled")


def apply_outputs(expected, check_only):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    expected_paths = set(expected)
    existing_paths = set()
    for dirpath, _, filenames in os.walk(OUTPUT_DIR):
        for filename in filenames:
            if filename.endswith(".json") or filename == "NOTICE.md":
                path = os.path.join(dirpath, filename)
                existing_paths.add(os.path.relpath(path, ROOT).replace(os.sep, "/"))
    stale = sorted(existing_paths - expected_paths)
    mismatches = []
    for rel, content in expected.items():
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            mismatches.append(f"missing: {rel}")
        elif open(path, encoding="utf-8").read() != content:
            mismatches.append(f"out-of-date: {rel}")
    if check_only:
        if stale or mismatches:
            for item in mismatches:
                print(item)
            for item in stale:
                print(f"orphan: {item}")
            raise SystemExit("Tag-index shards are stale; regenerate and commit bundle/tag-index.")
        print(f"Tag-index shards are current ({len(expected)} generated files).")
        return
    for rel in stale:
        os.remove(os.path.join(ROOT, rel))
    for rel, content in expected.items():
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
    shard_paths = [p for p in expected if p.endswith(".json") and not p.endswith("/manifest.json")]
    largest = max((len(expected[p].encode("utf-8")) for p in shard_paths), default=0)
    manifest = json.loads(expected["bundle/tag-index/manifest.json"])
    print(f"Generated {len(shard_paths)} shards; largest shard {largest:,} bytes; source SHA-256 {manifest['source']['sha256']}.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="compare committed shards with current upstream data")
    parser.add_argument("--self-test", action="store_true", help="run local tests without network access")
    args = parser.parse_args()
    run_self_tests()
    if args.self_test:
        print("Tag-index shard self-tests passed.")
        return
    source, source_sha = fetch_source()
    apply_outputs(generate_outputs(source, source_sha), args.check)


if __name__ == "__main__":
    main()
