#!/usr/bin/env python3
"""Check the pinned sharded Danbooru snapshot offline; no upstream fetch."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "bundle" / "tag-index"

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    root = load("manifest.json")
    sha = root["source"]["sha256"]
    assert len(sha) == 64 and root["schema_version"] == 1
    assert root["lookup"]["group_isolation"] is True
    for group, cfg in root["groups"].items():
        meta = load(f"{cfg['path_group']}/manifest.json")
        assert meta["source_sha256"] == sha
        assert meta["group"] == group
        assert meta["tag_count"] == cfg["tag_count"]
        assert meta["prefix_length"] == cfg["prefix_length"]
    samples = [
        ("general", "1g", "1girl"),
        ("general", "wh", "white_background"),
        ("characters", "37", "37_(reverse:1999)"),
        ("artists", "sta", "@starshadowmagician"),
    ]
    for group, prefix, candidate in samples:
        shard = load(f"{group}/{prefix}.json")
        assert shard["_meta"]["source_sha256"] == sha
        assert shard["_meta"]["group"] == group
        assert candidate in shard["exact"], (group, candidate)
    assert "sta" in load("artists/manifests/s.json")["prefixes"]
    print("Pinned Danbooru snapshot: PASS (offline metadata and canonical samples)")

if __name__ == "__main__":
    main()
