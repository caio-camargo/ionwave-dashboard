#!/usr/bin/env python3
"""
Enrich manifest.json with danilo_tup, danilo_cluster, and passet fields
by cross-referencing crosswalk.json file_to_tup mappings.
"""

import json
import os

BASE = r"G:\Meu Drive\IonWave Bootstrap"

manifest_path = os.path.join(BASE, "data", "manifest.json")
crosswalk_path = os.path.join(BASE, "data", "crosswalk.json")

# Read both files
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(crosswalk_path, "r", encoding="utf-8") as f:
    crosswalk = json.load(f)

file_to_tup = crosswalk.get("file_to_tup", {})

updated = 0
missing = 0

for file_key, file_entry in manifest["files"].items():
    mapping = file_to_tup.get(file_key)

    if mapping:
        file_entry["danilo_tup"] = mapping.get("primary_tup")       # string or null
        file_entry["danilo_cluster"] = mapping.get("cluster")        # string or null
    else:
        # File not in crosswalk — set fields to null
        file_entry["danilo_tup"] = None
        file_entry["danilo_cluster"] = None
        missing += 1

    # All files are Imagination Passet
    file_entry["passet"] = "imagination"
    updated += 1

# Write back with same indent style (2-space)
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
    f.write("\n")  # trailing newline

print(f"Done. Updated {updated} file entries ({missing} had no crosswalk mapping).")
print(f"Manifest written to: {manifest_path}")
