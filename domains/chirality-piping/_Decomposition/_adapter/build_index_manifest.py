#!/usr/bin/env python3
"""Derive the local retrieval-index manifest for the source-database build.

The canonical _Sources/Source_Manifest.csv admits code and schema files with
IncludeInIndex=YES (two-tier admission: retrieval-tier intent). But the v1
source-database builder (tools/source_catalog/build_source_database.py) can only
chunk MARKDOWN raw sources; non-markdown IncludeInIndex=YES rows are rejected.

Code and schema atoms are still represented in the retrieval index through
LEDGER_ATOM chunks built from Atomic_Domain_Ledger.csv, so dropping their RAW
source chunks does not remove them from retrieval/ratification — it only mirrors
the app-dev snapshot composition (markdown raw sources + ledger atoms).

This emits a DERIVED, local, rebuildable manifest where every non-.md row is
flipped to IncludeInIndex=NO. The canonical manifest is NOT modified.

Usage:  python3 _adapter/build_index_manifest.py    (cwd = MONOREPO_ROOT)
Output: _Sources/Source_Manifest.index.csv
"""
from __future__ import annotations
import csv
from pathlib import Path

MONO = Path.cwd()
SRC = MONO / "domains/chirality-piping/_Sources"
IN = SRC / "Source_Manifest.csv"
OUT = SRC / "Source_Manifest.index.csv"


def main():
    rows = list(csv.DictReader(open(IN, encoding="utf-8")))
    cols = list(rows[0].keys())
    flipped = 0
    for r in rows:
        if not r["RepoRelPath"].endswith(".md") and r["IncludeInIndex"] == "YES":
            r["IncludeInIndex"] = "NO"
            flipped += 1
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader(); w.writerows(rows)
    md_yes = sum(1 for r in rows if r["IncludeInIndex"] == "YES")
    print(f"wrote {OUT.relative_to(MONO)}: {len(rows)} rows, "
          f"{flipped} non-md flipped to NO, {md_yes} markdown IncludeInIndex=YES")


if __name__ == "__main__":
    raise SystemExit(main())
