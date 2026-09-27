#!/usr/bin/env python3
"""SCA-APP-012 group-3 post-change coverage for the candidate (read-only on its inputs).

Run from the repository root on a committed tree (the builder compares the
App tree with HEAD):

    build_post_change_coverage.py --pre-refresh
        On the tree before the candidate is written (the group-2 snapshot
        commit). Writes Evidence/Group3/PRE_CHANGE_REFRESH.json: the accepted
        pre-change baseline recomputed at the current basis, so that basis
        movement since the group-1 basis (G1B-01) is separated from the effect
        of the amendment.

    build_post_change_coverage.py
        On the committed candidate. Writes Post_Change_Coverage.json and
        Evidence/Group3/PRE_POST_COMPARISON.md, comparing the candidate with
        both the accepted Pre_Change_Coverage.json and the refresh.

Both modes run the accepted group-1 builder Evidence/Group1/build_pre_change_baseline.py
unchanged in logic, with three substitutions made in memory: the output file,
the run label, and BASIS_COMMIT set to HEAD. Every GIT_* variable is removed
from the environment first, so git answers for this checkout only, and HEAD is
resolved with a git call that must succeed. The group-1 builder file and
Pre_Change_Coverage.json are not modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import types

for _k in [k for k in os.environ if k.startswith("GIT_")]:
    del os.environ[_k]

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.dirname(os.path.dirname(HERE))
BUILDER = os.path.join(SNAP, "Evidence", "Group1", "build_pre_change_baseline.py")
PRE = os.path.join(SNAP, "Pre_Change_Coverage.json")
REFRESH = os.path.join(HERE, "PRE_CHANGE_REFRESH.json")
POST = os.path.join(SNAP, "Post_Change_Coverage.json")
REPORT = os.path.join(HERE, "PRE_POST_COMPARISON.md")
OLD_BASIS = 'BASIS_COMMIT = "adc8bdae18b2e1e48dcf01a304cc055d2cbf84e0"'
OLD_OUT = 'out = os.path.join(SNAP_REL, "Pre_Change_Coverage.json")'
OLD_LABEL = '"run_label": "SCA_APP_012_GROUP1_PRECHANGE"'
COMPARE = [
    "repository_topology", "ledger_distribution", "forward_coverage", "reverse_coverage",
    "scope_items_without_deliverable", "objectives_without_deliverable", "lifecycle_distribution",
    "issued_deliverables", "checking_deliverables", "affected_deliverables", "affected_scope_items",
    "objective_active_supporters", "dependency_rows", "frontend_reachability", "frontend_references",
    "legacy_css_tokens", "dead_css_candidates", "decomposition_sha256", "companion_register_sha256",
    "scope_change_pointer_sha256",
]


def sha(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def head() -> str:
    p = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
    return p.stdout.strip()


def run_builder(out_rel: str, label: str, basis: str) -> dict:
    src = open(BUILDER, encoding="utf-8").read()
    for a, b in ((OLD_BASIS, f'BASIS_COMMIT = "{basis}"'),
                 (OLD_OUT, f'out = {out_rel!r}'),
                 (OLD_LABEL, f'"run_label": "{label}"')):
        if src.count(a) != 1:
            raise SystemExit(f"substitution anchor not found once: {a}")
        src = src.replace(a, b)
    mod = types.ModuleType("group3_builder")
    exec(compile(src, BUILDER + " (group-3 substitutions)", "exec"), mod.__dict__)
    rc = mod.main()
    if rc:
        raise SystemExit(rc)
    return json.load(open(out_rel, encoding="utf-8"))


def tools_view(d: dict) -> dict:
    t = d["tools"]
    a, c, v = t["audit_structure"], t["analyze_dep_closure"], t["validate_decomposition_registers"]
    return {
        "audit_structure.run_status": a["run_status"],
        "audit_structure.subject_status": a["subject_status"],
        "audit_structure.summary": a["summary"],
        "audit_structure.issues": a["issues"],
        "analyze_dep_closure.graph (nodes, edges, SCCs)": {k: c.get(k) for k in ("graph_nodes", "graph_edges", "scc_count")},
        "analyze_dep_closure (all fields)": c,
        "validate_decomposition_registers.findings_by_code": v["findings_by_code"],
        "validate_decomposition_registers.exit": v["exit"],
    }


def text_hit_counts(d: dict) -> dict:
    counts: dict = {}
    for hits in d["scope_text_hits"].values():
        for h in hits:
            for tag in h["tags"]:
                counts[tag] = counts.get(tag, 0) + 1
    return dict(sorted(counts.items()))


def cell(x) -> str:
    s = json.dumps(x, sort_keys=True)
    return "`" + (s if len(s) <= 120 else s[:117] + "...") + "`"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pre-refresh", action="store_true")
    args = ap.parse_args()
    basis = head()
    rel = lambda p: os.path.relpath(p)
    if args.pre_refresh:
        d = run_builder(rel(REFRESH), "SCA_APP_012_GROUP3_PRECHANGE_REFRESH", basis)
        d["refresh"] = {"purpose": "Accepted pre-change baseline recomputed at the group-3 basis (before the candidate)",
                        "builder_sha256": sha(BUILDER), "wrapper_sha256": sha(os.path.abspath(__file__)),
                        "accepted_pre_change_coverage_sha256": sha(PRE)}
        with open(REFRESH, "w", encoding="utf-8") as fh:
            json.dump(d, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(rel(REFRESH))
        return 0

    post = run_builder(rel(POST), "SCA_APP_012_GROUP3_POSTCHANGE_CANDIDATE", basis)
    pre = json.load(open(PRE, encoding="utf-8"))
    ref = json.load(open(REFRESH, encoding="utf-8"))
    post["method"] = ("Deterministic post-change baseline for the group-3 CANDIDATE, produced by the accepted group-1 "
                      "builder (Evidence/Group1/build_pre_change_baseline.py) with only the output name, run label and "
                      "basis commit substituted (Evidence/Group3/build_post_change_coverage.py). A full audit-decomp "
                      "TASK run was not dispatched from this bounded session; the same registered tools as the "
                      "pre-change baseline were run on the candidate.")
    post["candidate"] = {
        "state": "CANDIDATE (not accepted; _LATEST.md unchanged)",
        "builder_sha256": sha(BUILDER),
        "wrapper_sha256": sha(os.path.abspath(__file__)),
        "pre_change_coverage_sha256": sha(PRE),
        "pre_change_refresh_sha256": sha(REFRESH),
        "acceptance_conditional_withheld": ["E26"],
    }
    comp = {}
    views = [(k, pre.get(k), ref.get(k), post.get(k)) for k in COMPARE]
    tp, tr, tq = tools_view(pre), tools_view(ref), tools_view(post)
    views += [(k, tp[k], tr[k], tq[k]) for k in tp]
    views.append(("scope_text_hits (hit lines per tag)", text_hit_counts(pre), text_hit_counts(ref), text_hit_counts(post)))
    for k, a, b, c in views:
        comp[k] = {"pre_accepted": a, "pre_refresh": b, "post": c,
                   "refresh_equals_accepted": a == b, "post_equals_refresh": b == c}
    post["comparison_to_pre_change"] = comp
    with open(POST, "w", encoding="utf-8") as fh:
        json.dump(post, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    lines = ["# SCA-APP-012 pre/post coverage comparison (group-3 candidate)\n\n",
             f"- Pre (accepted): `Pre_Change_Coverage.json`, basis `{pre['basis_commit'][:9]}`.\n",
             f"- Pre (refresh): `Evidence/Group3/PRE_CHANGE_REFRESH.json`, basis `{ref['basis_commit'][:9]}` "
             "(the group-2 snapshot commit, before the candidate).\n",
             f"- Post: `Post_Change_Coverage.json`, basis `{post['basis_commit'][:9]}` (the committed candidate).\n\n",
             "\"Basis moved\" compares the refresh with the accepted baseline (main's changes, G1B-01). "
             "\"Amendment effect\" compares the candidate with the refresh.\n\n",
             "| Field | Basis moved | Amendment effect | Pre (accepted) | Pre (refresh) | Post |\n|---|---|---|---|---|---|\n"]
    for k, v in comp.items():
        lines.append(f"| {k} | {'no' if v['refresh_equals_accepted'] else '**yes**'} | "
                     f"{'none' if v['post_equals_refresh'] else '**changed**'} | {cell(v['pre_accepted'])} | "
                     f"{cell(v['pre_refresh'])} | {cell(v['post'])} |\n")
    open(REPORT, "w", encoding="utf-8").write("".join(lines))
    print(rel(POST))
    print(rel(REPORT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
