#!/usr/bin/env python3
"""Gate 5 input-shim for chirality-app-dev.

tools/decomp/build_gate5_coverage.py is data-driven and REUSABLE-AS-IS, but it
reads a `Gate2_Source_Unit_Register.csv` with specific columns. app-dev instead has
`Source_Decomp_Prefix_Map.csv` (different column names). This shim generates the
register the tool expects, one row per source unit, pointing SkeletonPath at the
Gate-1.5 reviewed skeletons.

Note: the tool must be run with --repo-root . (monorepo root) — app-dev skeletons
store ABSOLUTE md_path values (repo_root-independent), and repo_root is only used to
locate tools/decomp/render_source_html.py and as the SkeletonPath base. SkeletonPath
is emitted monorepo-relative so it resolves under repo_root=".".

Usage:  python3 _adapter/gate5_make_source_register.py
Run with cwd = MONOREPO_ROOT (chirality/). Prints a JSON summary.
"""
from __future__ import annotations
import csv, json, os
from pathlib import Path

MONO = Path.cwd()
PACK_REL = "domains/chirality-app-dev"
DEC = MONO / PACK_REL / "_Decomposition"
PREFIX = DEC / "Source_Decomp_Prefix_Map.csv"
OUT = DEC / "Gate2_Source_Unit_Register.csv"

FIELDS = ["Gate2SourceSeq", "BatchID", "SourceDocID", "SourcePrefix", "SourceName",
          "RepoRelPath", "SourceGroup", "Grouping", "SkeletonPath",
          "AssetManifestPath", "PackMarkdownPath"]


def main():
    rows = list(csv.DictReader(open(PREFIX, encoding="utf-8")))
    # only include source units that actually have atoms in the Gate-4 ledger;
    # 4 EGOV parent-dir containers are header-only (content lives in dated subfolder
    # units that ARE in the ledger) -> exclude so the tool's source-set match passes.
    ledger_docs = {r["SourceDoc"] for r in csv.DictReader(
        open(DEC / "Domain_Ledger_Gate4_KTY_Draft.csv", encoding="utf-8"))}
    rows = [r for r in rows if r["SourceUnitID"] in ledger_docs]
    out_rows = []
    missing = []
    excluded = []
    for i, r in enumerate(rows, 1):
        uid = r["SourceUnitID"]
        repo_rel = r.get("RepoRelPathOrGlob", "")
        # reviewed skeleton, monorepo-relative (resolves under repo_root=".")
        sk_pack = r["SkeletonPath"].replace("_skeleton.json", "_skeleton.reviewed.json")
        sk_rel = f"{PACK_REL}/{sk_pack}" if not sk_pack.startswith(PACK_REL) else sk_pack
        if not (MONO / sk_rel).exists():
            missing.append((uid, sk_rel))
        out_rows.append({
            "Gate2SourceSeq": str(i),
            "BatchID": "ATOMIZED",
            "SourceDocID": uid,
            "SourcePrefix": r["SourcePrefix"],
            "SourceName": os.path.basename(repo_rel) or uid,
            "RepoRelPath": repo_rel,
            "SourceGroup": r["SourceGroup"],
            "Grouping": r.get("Grouping", ""),
            "SkeletonPath": sk_rel,
            "AssetManifestPath": f"{PACK_REL}/{r.get('AssetManifestPath','')}",
            "PackMarkdownPath": (f"{PACK_REL}/{r['PackMarkdownPath']}" if r.get("PackMarkdownPath") else ""),
        })
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(out_rows)
    print(json.dumps({"source_units": len(out_rows), "missing_reviewed_skeletons": missing,
                      "output": str(OUT.relative_to(MONO))}, indent=2))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
