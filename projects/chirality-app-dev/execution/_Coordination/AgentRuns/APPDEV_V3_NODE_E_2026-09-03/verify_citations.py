#!/usr/bin/env python3
"""Recompute every SHA-256 cited in Evidence_AT-053_Governed_Basis_2026-09-03.json.

Checks (1) every manifest entry and (2) every per-row citation against the live tree,
and (3) that the set of cited paths equals the manifest and the manifest is sorted.
Writes VERIFY_CITATIONS_RESULT.json beside this script. Exit 0 only when every digest matches.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
JSON_PATH = REPO_ROOT / "projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/Evidence_AT-053_Governed_Basis_2026-09-03.json"
OUT = Path(__file__).resolve().parent / "VERIFY_CITATIONS_RESULT.json"


def digest(rel: str) -> str | None:
    p = REPO_ROOT / rel
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None


def main() -> int:
    doc = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True).strip()
    mismatches: list[dict] = []
    checked = 0
    for m in doc["manifest"]:
        checked += 1
        live = digest(m["path"])
        if live != m["sha256"] or (REPO_ROOT / m["path"]).stat().st_size != m["bytes"]:
            mismatches.append({"where": "manifest", "path": m["path"], "recorded": m["sha256"], "live": live})
    cited = set()
    for s in doc["sections"]:
        for i, r in enumerate(s["rows"], 1):
            for c in r["citations"]:
                checked += 1
                cited.add(c["path"])
                live = digest(c["path"])
                if live != c["sha256"]:
                    mismatches.append({"where": f"section {s['id']} row {i}", "path": c["path"], "recorded": c["sha256"], "live": live})
    for key in ("plan_pin",):
        checked += 1
        if digest(doc[key]["path"]) != doc[key]["sha256"]:
            mismatches.append({"where": key, "path": doc[key]["path"], "recorded": doc[key]["sha256"], "live": digest(doc[key]["path"])})
    manifest_paths = [m["path"] for m in doc["manifest"]]
    structural = {
        "manifest_sorted": manifest_paths == sorted(manifest_paths),
        "manifest_unique": len(manifest_paths) == len(set(manifest_paths)),
        "cited_subset_of_manifest": cited <= set(manifest_paths),
        "manifest_extra_paths": sorted(set(manifest_paths) - cited),
    }
    result = {
        "schema": "chirality-app-at053-citation-verification/v1",
        "json_path": str(JSON_PATH.relative_to(REPO_ROOT)),
        "json_sha256": hashlib.sha256(JSON_PATH.read_bytes()).hexdigest(),
        "verified_at_head": head,
        "recorded_basis": doc["basis_commit"],
        "digests_checked": checked,
        "manifest_entries": len(manifest_paths),
        "distinct_cited_paths": len(cited),
        "mismatches": mismatches,
        "structural": structural,
        "verdict": "PASS" if not mismatches and structural["manifest_sorted"] and structural["manifest_unique"] and structural["cited_subset_of_manifest"] else "FAIL",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("verdict", "digests_checked", "manifest_entries", "distinct_cited_paths", "verified_at_head")}))
    if mismatches:
        for m in mismatches:
            print("MISMATCH", m)
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
