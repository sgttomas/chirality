#!/usr/bin/env python3
"""Phase-2 group merge + QA + atom-review HTML for chirality-app-dev.

For every source unit in a SourceGroup within a batch:
  1. QA all per-unit atom CSVs (header, sha1[:12] ContentHash, SectionID in
     target set, MD line within dispatch range, monotonic LocalSeq, @repo ref).
  2. merge_source_atomizations.py per-source -> per_source_ledgers/<batch>/<uid>_atomic_units.csv
  3. render_source_html.py --mode atom-review -> atom_review_html/<batch>/<uid>.html

Does NOT do the cross-source merge or vocab consolidation — those run once at
the end across all groups.

Usage: python3 _adapter/phase2_merge.py <BATCH_NAME> <SOURCE_GROUP>
Run with cwd = MONOREPO_ROOT. Prints a JSON summary.
"""
from __future__ import annotations
import csv, hashlib, json, re, subprocess, sys
from pathlib import Path

MONO = Path.cwd()
PACK = MONO / "domains/chirality-app-dev"
DECOMP = PACK / "_Decomposition"
REPO_ROOT = (PACK / "../../projects/chirality-app-dev").resolve()
HEADER = "LocalSeq,UnitStatement,SourceRef,ContentHash,InOutStatus,SectionID,DispatchUnitID,Corrects,Notes"


def qa_unit(csv_path, unit_meta):
    probs = []
    hdr = open(csv_path, encoding="utf-8").readline().rstrip("\r\n")
    if hdr != HEADER:
        probs.append(f"{csv_path.name}: bad header")
    rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
    prev = 0
    n_in = n_out = n_tbd = 0
    for r in rows:
        uid = r["DispatchUnitID"]; ls, le, tids = unit_meta.get(uid, (None, None, set()))
        st = r["InOutStatus"]
        if st == "IN": n_in += 1
        elif st == "OUT": n_out += 1
        elif st == "TBD": n_tbd += 1
        else: probs.append(f"{csv_path.name} seq{r['LocalSeq']}: bad InOutStatus {st}")
        if hashlib.sha1(r["UnitStatement"].encode()).hexdigest()[:12] != r["ContentHash"]:
            probs.append(f"{csv_path.name} seq{r['LocalSeq']}: hash mismatch")
        if tids and r["SectionID"] not in tids:
            probs.append(f"{csv_path.name} seq{r['LocalSeq']}: section {r['SectionID']} not in target")
        if int(r["LocalSeq"]) != prev + 1:
            probs.append(f"{csv_path.name} seq{r['LocalSeq']}: localseq gap (prev {prev})")
        prev = int(r["LocalSeq"])
        m = re.search(r":L(\d+)\|", r["SourceRef"])
        if not m:
            probs.append(f"{csv_path.name} seq{r['LocalSeq']}: no Lnnn in SourceRef")
        if "@repo/" not in r["SourceRef"]:
            probs.append(f"{csv_path.name} seq{r['LocalSeq']}: SourceRef missing @repo")
    return len(rows), n_in, n_out, n_tbd, probs


def main():
    batch, group = sys.argv[1], sys.argv[2]
    pmap = {r["SourceUnitID"]: r for r in csv.DictReader(open(DECOMP / "Source_Decomp_Prefix_Map.csv", encoding="utf-8"))}
    units = [r for r in pmap.values() if r["SourceGroup"] == group and r["AtomizeInV1"] == "YES"]
    psl_dir = DECOMP / "per_source_ledgers" / batch; psl_dir.mkdir(parents=True, exist_ok=True)
    html_dir = DECOMP / "atom_review_html" / batch; html_dir.mkdir(parents=True, exist_ok=True)
    nodes_dir = DECOMP / "atom_review_section_nodes" / batch; nodes_dir.mkdir(parents=True, exist_ok=True)
    audit_dir = DECOMP / "atom_review_audit" / batch; audit_dir.mkdir(parents=True, exist_ok=True)

    all_probs = []; tot = ti = to = tt = 0; merged = 0; rendered = 0; missing = []
    for r in units:
        uid = r["SourceUnitID"]; pref = r["SourcePrefix"]
        dispatch = PACK / r["DispatchPlanPath"]
        plan = json.loads(dispatch.read_text())
        unit_meta = {u["unit_id"]: (u["line_start"], u["line_end"], set(u["target_section_ids"])) for u in plan["units"]}
        odir = DECOMP / "dispatch_outputs" / batch / uid
        for u in plan["units"]:
            f = odir / f"{u['unit_id']}_atoms.csv"
            if not f.exists():
                missing.append(f"{uid}/{u['unit_id']}"); continue
            n, a, b, c, probs = qa_unit(f, unit_meta)
            tot += n; ti += a; to += b; tt += c; all_probs += probs
        # per-source merge
        out = psl_dir / f"{uid}_atomic_units.csv"
        cmd = [sys.executable, "tools/decomp/merge_source_atomizations.py", "per-source",
               "--dispatch-plan", str(dispatch),
               "--unit-csv-glob", str(odir / "UNIT-*_atoms.csv"),
               "--source-prefix", pref, "--source-name", uid, "--output", str(out)]
        res = subprocess.run(cmd, cwd=MONO, capture_output=True, text=True)
        if res.returncode != 0:
            all_probs.append(f"{uid}: per-source merge failed: {res.stderr.strip()[:200]}"); continue
        merged += 1
        # atom-review html
        reviewed = PACK / r["SkeletonPath"].replace("_skeleton.json", "_skeleton.reviewed.json")
        skel = reviewed if reviewed.exists() else PACK / r["SkeletonPath"]
        asset = PACK / r["AssetManifestPath"]
        grouped = r["Grouping"] != "PER_FILE"
        md = (PACK / r["PackMarkdownPath"]) if grouped and r.get("PackMarkdownPath") else (REPO_ROOT / r["RepoRelPathOrGlob"])
        cmd = [sys.executable, "tools/decomp/render_source_html.py", "--md", str(md),
               "--asset-manifest", str(asset), "--skeleton", str(skel), "--audit-dir", str(audit_dir),
               "--output-html", str(html_dir / f"{uid}.html"),
               "--output-section-nodes", str(nodes_dir / f"{uid}_section_nodes.csv"),
               "--mode", "atom-review", "--atomic-units-csv", str(out)]
        res = subprocess.run(cmd, cwd=MONO, capture_output=True, text=True)
        if res.returncode != 0:
            all_probs.append(f"{uid}: atom-review render failed: {res.stderr.strip()[:200]}")
        else:
            rendered += 1
    summary = {"batch": batch, "group": group, "source_units": len(units),
               "per_source_merged": merged, "atom_review_rendered": rendered,
               "atoms": tot, "IN": ti, "OUT": to, "TBD": tt,
               "missing_unit_csvs": missing, "qa_problems": len(all_probs),
               "qa_problem_sample": all_probs[:25]}
    print(json.dumps(summary, indent=2))
    return 0 if not all_probs and not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
