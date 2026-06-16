#!/usr/bin/env python3
"""Gate 1.5-S machine-assisted skeleton review for chirality-app-dev.

Computes out-of-scope SectionIDs per the accepted scope-trim rules, then re-runs
build_source_skeleton.py with --back-matter-overrides to produce, for every
source unit, a `*_skeleton.reviewed.json` and a reviewed dispatch plan that
excludes out-of-scope sections.

Trim rules (machine-assisted pre-pass; reported for human confirmation):
  R2 GROUPED units: the generated "# Source Pack" boilerplate header is OUT
     (worker/review substrate, not source content).
  R3 GOVERNANCE units: `_LATEST.md` pointer files are OUT (navigation pointers).

Note: the deliverable knowledge-type-doc trim is now handled at SOURCE ADMISSION
(Gate 1, suffix-match) — only KT-suffix docs are admitted — so 1.5-S keeps all
admitted deliverable components. Per-file sources (docs, root, frontend prose)
and the frontend-src unit keep all content (R2 applies only to the grouped
boilerplate header).
"""
from __future__ import annotations
import csv
import json
import subprocess
import sys
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[2]
MONOREPO_ROOT = PACK_ROOT.parents[1]
REPO_ROOT = (PACK_ROOT / "../../projects/chirality-app-dev").resolve()
DECOMP = PACK_ROOT / "_Decomposition"
PACK_REL = "domains/chirality-app-dev"

KEEP_DELIVERABLE = {"Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"}
REVIEW_FIELDS = ["SourceUnitID", "SourcePrefix", "SourceGroup", "Grouping",
                 "ComponentsKept", "ComponentsDropped", "SectionsTotal",
                 "SectionsOut", "SectionsIn", "DispatchUnitsReviewed", "Notes"]


def read_csv(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def load_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def run_tool(cmd):
    proc = subprocess.run(cmd, cwd=MONOREPO_ROOT, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return proc.returncode, proc.stdout, proc.stderr


def component_for_section(line_start, comp_bounds):
    """comp_bounds: sorted list of (heading_line, gen_end, repo_rel_path).
    Return repo_rel_path of the component owning this section, or None (pack preamble)."""
    owner = None
    for hl, ge, rel in comp_bounds:
        if line_start >= hl:
            owner = rel
        else:
            break
    return owner


def main():
    prefix_rows = read_csv(DECOMP / "Source_Decomp_Prefix_Map.csv")
    review_rows = []
    failures = []
    tot_sections = tot_out = tot_units = 0

    for r in prefix_rows:
        uid = r["SourceUnitID"]
        group = r["SourceGroup"]
        grouping = r["Grouping"]
        prefix = r["SourcePrefix"]
        skeleton = PACK_ROOT / r["SkeletonPath"]
        asset = PACK_ROOT / r["AssetManifestPath"]
        reviewed_skel = skeleton.with_name(skeleton.name.replace("_skeleton.json", "_skeleton.reviewed.json"))
        dispatch = PACK_ROOT / r["DispatchPlanPath"]
        man = load_json(asset)
        skel = load_json(skeleton)
        sections = skel["sections"]
        grouped = grouping != "PER_FILE"
        md = (PACK_ROOT / r["PackMarkdownPath"]) if r.get("PackMarkdownPath") else (REPO_ROOT / man["repo_rel_path"])

        out_ids = []
        kept, dropped = [], []
        if grouped:
            comps = sorted(man.get("source_components", []), key=lambda c: c["generated_line_start"])
            bounds = [(c["generated_line_start"] - 2, c["generated_line_end"], c["repo_rel_path"]) for c in comps]
            # decide OUT components
            out_components = set()
            for c in comps:
                base = Path(c["repo_rel_path"]).name
                if group == "EXECUTION_GOVERNANCE" and base == "_LATEST.md":
                    out_components.add(c["repo_rel_path"]); dropped.append(c["repo_rel_path"])
                else:  # deliverable (admission already trimmed) / governance / frontend-src
                    kept.append(c["repo_rel_path"])
            for s in sections:
                # R2: pack boilerplate header
                if s["depth"] == 1 and s["title"].startswith("Source Pack"):
                    out_ids.append(s["section_id"]); continue
                owner = component_for_section(s["line_start"], bounds)
                if owner is None:
                    # pack preamble / Component heading boundary -> keep unless its component is OUT
                    continue
                if owner in out_components:
                    out_ids.append(s["section_id"])
        # per-file: no overrides (keep all)

        # re-run build_source_skeleton with overrides -> reviewed skeleton + reviewed dispatch
        cmd = [sys.executable, "tools/decomp/build_source_skeleton.py",
               "--md", str(md), "--asset-manifest", str(asset),
               "--output-skeleton", str(reviewed_skel),
               "--output-dispatch-plan", str(dispatch),
               "--source-prefix", prefix,
               "--budget-tokens", "15000", "--section-split-threshold", "25000"]
        if out_ids:
            cmd += ["--back-matter-overrides", json.dumps(out_ids)]
        rc, out, err = run_tool(cmd)
        if rc != 0:
            failures.append((uid, err.strip() or out.strip()))
            continue
        rskel = load_json(reviewed_skel)
        rplan = load_json(dispatch)
        n_total = len(rskel["sections"])
        n_in = sum(1 for s in rskel["sections"] if s["in_scope_default"])
        n_out = n_total - n_in
        n_units = len(rplan["units"])
        tot_sections += n_total; tot_out += n_out; tot_units += n_units
        review_rows.append({
            "SourceUnitID": uid, "SourcePrefix": prefix, "SourceGroup": group,
            "Grouping": grouping, "ComponentsKept": len(kept),
            "ComponentsDropped": len(dropped), "SectionsTotal": n_total,
            "SectionsOut": n_out, "SectionsIn": n_in, "DispatchUnitsReviewed": n_units,
            "Notes": ("dropped: " + ";".join(sorted(Path(d).name for d in dropped)[:6])) if dropped else "",
        })

    out_csv = DECOMP / "Gate1.5_Skeleton_Review.csv"
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=REVIEW_FIELDS); w.writeheader(); w.writerows(review_rows)

    from collections import Counter, defaultdict
    g = defaultdict(lambda: [0, 0, 0, 0])
    for r in review_rows:
        k = r["SourceGroup"]; g[k][0] += 1
        g[k][1] += r["SectionsTotal"]; g[k][2] += r["SectionsIn"]; g[k][3] += r["DispatchUnitsReviewed"]
    summary = {
        "units_reviewed": len(review_rows), "failures": len(failures),
        "sections_total": tot_sections, "sections_in_scope": tot_sections - tot_out,
        "sections_out": tot_out, "reviewed_dispatch_units": tot_units,
        "by_group": {k: {"units": v[0], "sections_total": v[1], "sections_in": v[2],
                         "dispatch_units": v[3]} for k, v in sorted(g.items())},
        "failures_detail": [{"unit": f[0], "err": f[1][:200]} for f in failures],
    }
    (DECOMP / "Gate1.5_Review_Telemetry.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
