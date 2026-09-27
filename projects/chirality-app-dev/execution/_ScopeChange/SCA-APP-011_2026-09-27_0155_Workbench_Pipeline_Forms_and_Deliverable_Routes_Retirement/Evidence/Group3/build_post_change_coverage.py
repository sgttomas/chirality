#!/usr/bin/env python3
"""SCA-APP-011 group-3 post-change coverage for the candidate (read-only on inputs).

Run from the repository root, on the committed candidate:

    python3 <SCA folder>/Evidence/Group3/build_post_change_coverage.py

It runs the accepted group-1 builder `Evidence/Group1/build_pre_change_baseline.py`
unchanged in logic, with three substitutions made in memory:
  - the output file is `Post_Change_Coverage.json`;
  - the run label is `SCA_APP_011_GROUP3_POSTCHANGE_CANDIDATE`;
  - DEL-07-01 (register row 29) is added to the affected-lifecycle list.
It then adds candidate identity and a field-by-field comparison with the
accepted `Pre_Change_Coverage.json`, and writes `Evidence/Group3/PRE_POST_COMPARISON.md`.
The group-1 builder file and `Pre_Change_Coverage.json` are not modified.
"""
from __future__ import annotations

import hashlib
import json
import os
import types

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.dirname(os.path.dirname(HERE))
BUILDER = os.path.join(SNAP, "Evidence", "Group1", "build_pre_change_baseline.py")
PRE = os.path.join(SNAP, "Pre_Change_Coverage.json")
POST = os.path.join(SNAP, "Post_Change_Coverage.json")
REPORT = os.path.join(HERE, "PRE_POST_COMPARISON.md")
SUBS = [
    ('os.path.join(SNAP_REL, "Pre_Change_Coverage.json")', 'os.path.join(SNAP_REL, "Post_Change_Coverage.json")'),
    ('"run_label": "SCA_APP_011_GROUP1_PRECHANGE"', '"run_label": "SCA_APP_011_GROUP3_POSTCHANGE_CANDIDATE"'),
    ('"DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-03-03", "DEL-05-01", "DEL-07-02",',
     '"DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-03-03", "DEL-05-01", "DEL-07-01", "DEL-07-02",'),
]
COMPARE = [
    "repository_topology", "ledger_distribution", "context_envelopes", "forward_coverage", "reverse_coverage",
    "scope_items_without_deliverable", "objectives_without_deliverable", "lifecycle_distribution",
    "issued_deliverables", "affected_lifecycle",
]


def sha(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def tools_view(d: dict) -> dict:
    t = d["tools"]
    a = t["audit_structure"]
    return {
        "audit_structure.run_status": a["run_status"],
        "audit_structure.subject_status": a["subject_status"],
        "audit_structure.summary": a["summary"],
        "audit_structure.issue_count": len(a["issues"]),
        "audit_structure.target_unit": a["target_unit"],
        "analyze_dep_closure": {k: v for k, v in t["analyze_dep_closure"].items()},
        "validate_decomposition_registers.findings_by_code": t["validate_decomposition_registers"]["findings_by_code"],
        "validate_decomposition_registers.error_count": t["validate_decomposition_registers"]["error_count"],
        "validate_decomposition_registers.exit": t["validate_decomposition_registers"]["exit"],
    }


def main() -> int:
    src = open(BUILDER, encoding="utf-8").read()
    for a, b in SUBS:
        if src.count(a) != 1:
            raise SystemExit(f"substitution anchor not found once: {a}")
        src = src.replace(a, b)
    mod = types.ModuleType("post_change_builder")
    exec(compile(src, BUILDER + " (group-3 substitutions)", "exec"), mod.__dict__)
    rc = mod.main()
    if rc:
        return rc

    pre = json.load(open(PRE, encoding="utf-8"))
    post = json.load(open(POST, encoding="utf-8"))
    post["method"] = ("Synthesized deterministic post-change baseline for the group-3 CANDIDATE, produced by the accepted "
                      "group-1 builder (Evidence/Group1/build_pre_change_baseline.py) with only the output name, run label "
                      "and DEL-07-01 substituted (Evidence/Group3/build_post_change_coverage.py). A full audit-decomp TASK "
                      "run was not dispatched from this bounded session; the same registered tools as the pre-change "
                      "baseline were run on the candidate.")
    post["prior_full_audit"]["reuse"] = ("Not reused: the candidate decomposition differs from the prior audit's input. "
                                         "Listed for provenance only.")
    post["candidate"] = {
        "state": "CANDIDATE (not accepted; _LATEST.md unchanged)",
        "builder_sha256": sha(BUILDER),
        "wrapper_sha256": sha(os.path.abspath(__file__)),
        "pre_change_coverage_sha256": sha(PRE),
        "acceptance_conditional_withheld": ["E47"],
    }
    comparison = {}
    for k in COMPARE:
        comparison[k] = {"pre": pre.get(k), "post": post.get(k), "equal": pre.get(k) == post.get(k)}
    tp, tq = tools_view(pre), tools_view(post)
    for k in tp:
        comparison[k] = {"pre": tp[k], "post": tq[k], "equal": tp[k] == tq[k]}
    comparison["decomposition_sha256"] = {"pre": pre["decomposition_sha256"], "post": post["decomposition_sha256"],
                                          "equal": pre["decomposition_sha256"] == post["decomposition_sha256"]}
    comparison["companion_register_sha256"] = {"pre": pre["companion_register_sha256"],
                                               "post": post["companion_register_sha256"],
                                               "equal": pre["companion_register_sha256"] == post["companion_register_sha256"]}
    comparison["scope_change_pointer_sha256"] = {"pre": pre["scope_change_pointer_sha256"],
                                                 "post": post["scope_change_pointer_sha256"],
                                                 "equal": pre["scope_change_pointer_sha256"] == post["scope_change_pointer_sha256"]}
    post["comparison_to_pre_change"] = comparison
    with open(POST, "w", encoding="utf-8") as fh:
        json.dump(post, fh, indent=2, sort_keys=False)
        fh.write("\n")

    lines = ["# SCA-APP-011 pre/post coverage comparison (group-3 candidate)\n\n",
             f"Pre: `Pre_Change_Coverage.json` (accepted group-1 baseline, basis `{pre['basis_commit'][:9]}`). "
             f"Post: `Post_Change_Coverage.json` (candidate, basis `{post['basis_commit'][:9]}`).\n\n",
             "| Field | Equal | Pre | Post |\n|---|---|---|---|\n"]
    for k, v in comparison.items():
        def cell(x):
            s = json.dumps(x, sort_keys=True)
            return "`" + (s if len(s) <= 160 else s[:157] + "...") + "`"
        lines.append(f"| {k} | {'yes' if v['equal'] else '**no**'} | {cell(v['pre'])} | {cell(v['post'])} |\n")
    open(REPORT, "w", encoding="utf-8").write("".join(lines))
    print(os.path.relpath(POST))
    print(os.path.relpath(REPORT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
