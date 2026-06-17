#!/usr/bin/env python3
"""Detect which atomized source units are stale after a source-repo change.

Use after an out-of-band source refresh (e.g. the dependency / DAG refresh):
recompute SHA-256 for every admitted component file and compare it to the
`ComponentSha256` recorded at atomization time in Source_Unit_Component_Map.csv.
Any CHANGED or MISSING component flags its owning SourceUnitID for
re-atomization; the affected units are grouped by SourceGroup so the operator
knows exactly which phase2_run / phase2_merge groups to re-run for the next
batch (e.g. V2).

This does NOT detect brand-new admitted files (files added to the repo that now
match an admission rule). For that, re-run build_manifest.py and diff the
manifest row set. Renumbered DAG ids / rewritten prerequisite lines are content
changes and ARE caught here via the hash.

Read-only. Writes nothing. Prints a JSON worklist to stdout.
"""
from __future__ import annotations
import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[2]
DECOMP = PACK_ROOT / "_Decomposition"
REPO_ROOT = (PACK_ROOT / "../../projects/chirality-piping").resolve()


def read_csv(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    comp_rows = read_csv(DECOMP / "Source_Unit_Component_Map.csv")
    prefix_rows = read_csv(DECOMP / "Source_Decomp_Prefix_Map.csv")
    unit_group = {r["SourceUnitID"]: r["SourceGroup"] for r in prefix_rows}

    changed, missing = [], []
    for r in comp_rows:
        rel = r["ComponentRepoRelPath"]
        expected = r["ComponentSha256"]
        f = REPO_ROOT / rel
        if not f.exists():
            missing.append((r["SourceUnitID"], rel))
            continue
        if expected and sha256_file(f) != expected:
            changed.append((r["SourceUnitID"], rel))

    affected_units = sorted({u for u, _ in changed} | {u for u, _ in missing})
    by_group = defaultdict(list)
    for u in affected_units:
        by_group[unit_group.get(u, "UNKNOWN")].append(u)

    out = {
        "repo_root": str(REPO_ROOT),
        "components_checked": len(comp_rows),
        "changed_components": [{"unit": u, "path": p} for u, p in changed],
        "missing_components": [{"unit": u, "path": p} for u, p in missing],
        "affected_source_units": affected_units,
        "affected_groups": {g: sorted(us) for g, us in sorted(by_group.items())},
        "reatomize_worklist": [
            f"phase2_run.py <BATCH> {g}  +  re-dispatch only units {us}  +  phase2_merge.py <BATCH> {g}"
            for g, us in sorted(by_group.items())
        ],
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
