#!/usr/bin/env python3
"""Phase-2 group brief generator for chirality-app-dev.

Generates per-dispatch-unit atomization briefs for all source units in a given
SourceGroup, into a batch folder. Uses the pack-local alias map
(_adapter/brief_source_ref_map.csv) so build_atomization_brief.py can resolve
SOURCE_REF_BASE / ReviewHtmlPath by our SourceUnitID (the shared tool keys on
SourceDocID/SourceName, not SourceUnitID).

Usage:
  python3 _adapter/phase2_run.py <BATCH_NAME> <SOURCE_GROUP>
    SOURCE_GROUP ∈ {EXECUTION_DELIVERABLE, EXECUTION_GOVERNANCE, FRONTEND_SRC,
                    PRODUCT_DOCS, FRONTEND_DOCS, ROOT_DOCS}

Run with cwd = MONOREPO_ROOT (chirality/). Prints a JSON manifest of dispatch
units (uid, unit_id, brief_path, mode) to stdout.
"""
from __future__ import annotations
import csv, json, subprocess, sys
from pathlib import Path

MONO = Path.cwd()
PACK = MONO / "domains/chirality-app-dev"
DECOMP = PACK / "_Decomposition"
REPO_ROOT = (PACK / "../../projects/chirality-app-dev").resolve()
ALIAS = DECOMP / "_adapter" / "brief_source_ref_map.csv"


def main():
    batch, group = sys.argv[1], sys.argv[2]
    pmap = list(csv.DictReader(open(DECOMP / "Source_Decomp_Prefix_Map.csv", encoding="utf-8")))
    units = [r for r in pmap if r["SourceGroup"] == group and r["AtomizeInV1"] == "YES"]
    manifest = []
    for r in units:
        uid = r["SourceUnitID"]
        reviewed = PACK / r["SkeletonPath"].replace("_skeleton.json", "_skeleton.reviewed.json")
        skel = reviewed if reviewed.exists() else PACK / r["SkeletonPath"]
        dispatch = PACK / r["DispatchPlanPath"]
        asset = PACK / r["AssetManifestPath"]
        grouped = r["Grouping"] != "PER_FILE"
        md = (PACK / r["PackMarkdownPath"]) if grouped and r.get("PackMarkdownPath") else (REPO_ROOT / r["RepoRelPathOrGlob"])
        plan = json.loads(dispatch.read_text())
        bdir = DECOMP / "dispatch_briefs" / batch / uid
        odir = DECOMP / "dispatch_outputs" / batch / uid
        bdir.mkdir(parents=True, exist_ok=True)
        odir.mkdir(parents=True, exist_ok=True)
        for u in plan["units"]:
            uidd = u["unit_id"]
            cmd = [sys.executable, "tools/decomp/build_atomization_brief.py",
                   "--dispatch-plan", str(dispatch), "--unit-id", uidd,
                   "--md", str(md), "--skeleton", str(skel), "--asset-manifest", str(asset),
                   "--output-ledger-path", str(odir / f"{uidd}_atoms.csv"),
                   "--output-vocab-seed-path", str(odir / f"{uidd}_vocab.csv"),
                   "--scope-path", str(odir), "--source-prefix-map", str(ALIAS)]
            res = subprocess.run(cmd, cwd=MONO, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"FAIL {uid} {uidd}: {res.stderr.strip()}", file=sys.stderr)
                sys.exit(1)
            brief_path = bdir / f"{uidd}.md"
            brief_path.write_text(res.stdout)
            mode = "COMPONENT_MAP" if "SOURCE_REF_MODE: COMPONENT_MAP" in res.stdout else "REPO_LINE"
            manifest.append({"uid": uid, "unit_id": uidd,
                             "brief_path": str(brief_path.relative_to(PACK)), "mode": mode})
    print(json.dumps({"batch": batch, "group": group, "source_units": len(units),
                      "dispatch_units": len(manifest), "units": manifest}, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
