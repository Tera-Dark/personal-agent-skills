#!/usr/bin/env python3
"""Read-only estimate for tag shard compaction. Does NOT change live lookup URLs."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def analyze(root=ROOT, max_bucket_bytes=48000):
    base = root / "bundle/tag-index"
    manifest = json.loads((base / "manifest.json").read_text(encoding="utf-8"))
    meta = manifest.get("groups", {}).get("artists", {})
    artist_dir = base / "artists"
    shards = [p for p in artist_dir.glob("*.json") if p.name != "manifest.json"]
    if not shards:
        raise ValueError("no artist shards")
    coarse = {}
    for p in shards:
        prefix = p.stem
        key = "_special" if prefix == "_special" else prefix[:2]
        coarse.setdefault(key, []).append(p.stat().st_size)
    projected = sum(1 if sum(sizes) <= max_bucket_bytes else len(sizes)
                    for sizes in coarse.values())
    if len(shards) != meta.get("shard_count"):
        raise ValueError("artist shard count disagrees with root manifest")
    if manifest.get("source", {}).get("license") != "GPL-3.0":
        raise ValueError("tag-index license metadata differs from upstream notice")
    if not (base / "NOTICE.md").is_file():
        raise ValueError("third-party licensing/provenance NOTICE missing")
    return {
        "schema": manifest.get("schema_version"),
        "current_shards": len(shards),
        "coarse_prefixes": len(coarse),
        "estimated_adaptive_shards": projected,
        "estimated_file_reduction": len(shards) - projected,
        "largest_existing_shard_bytes": max(p.stat().st_size for p in shards),
        "coarse_max_bucket_bytes": max_bucket_bytes,
        "status": "DRY-RUN ONLY - no output rewrite"
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--max-bucket-bytes", type=int, default=48000)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = analyze(args.root, args.max_bucket_bytes)
        if args.check and report["estimated_adaptive_shards"] > report["current_shards"]:
            raise ValueError("proposed sharding would increase file count")
        print(json.dumps(report, indent=2, ensure_ascii=False))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"tag audit failure: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
