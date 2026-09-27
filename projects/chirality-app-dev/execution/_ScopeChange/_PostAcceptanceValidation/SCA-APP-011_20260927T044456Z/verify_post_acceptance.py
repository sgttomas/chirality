#!/usr/bin/env python3
"""SCA-APP-011 post-acceptance validation (append-only record; read-only on inputs).

Run from the repository root after the acceptance-conditional edits are applied:

    python3 projects/chirality-app-dev/execution/_ScopeChange/_PostAcceptanceValidation/SCA-APP-011_20260927T044456Z/verify_post_acceptance.py

It compares the applied bytes with the acceptance-conditional list
(Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv), reruns the registered tools
on the applied state through the accepted group-1 coverage builder (output
redirected into this folder; DEL-07-01 added to the affected list, as in the
group-3 post-change wrapper), reruns the supersession --check-map, and writes
POST_ACCEPTANCE_VALIDATION.md and POST_ACCEPTANCE_COVERAGE.json here. It does
not modify the candidate evidence reviewed at group 3.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
REL_HERE = os.path.relpath(HERE)
SC = "projects/chirality-app-dev/execution/_ScopeChange/"
SNAP = SC + "SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/"
G2 = SNAP + "Evidence/Group2/"
G3 = SNAP + "Evidence/Group3/"
DATE = "2026-09-27"
ACT = "I accept SCA-APP-011 checkpoint group 3"
UTC = os.path.basename(HERE).split("_", 1)[1]
DECOMP = "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
NOTICE = f"projects/chirality-runtime/execution/_Coordination/NOTICE_{DATE}_APP_SCA-APP-011_SCAFFOLD_API.md"
ACCEPTED_REV = "d48c785c5cb116a1614bf70784b2a116eca7f814"


def sha_b(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha(p: str) -> str:
    return sha_b(open(p, "rb").read())


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git_show(rev, path) -> str:
    return subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")


def main() -> int:
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    g3 = load("group3_corrections", G3 + "group3_corrections.py")
    b = load("build_amendment_preview", G2 + "build_amendment_preview.py")
    _, expected = g3.expected_hashes()

    # 1. Group-3 decision folder
    dec = SC + f"checkpoint_snapshots/SCA-APP-011_GROUP-3_{DATE}/DECISION.md"
    first = next(ln.strip() for ln in open(dec, encoding="utf-8") if ln.strip())
    check("1. decision folder heading", b.GROUP3_HEADING.match(first + " ") and ACT in open(dec, encoding="utf-8").read(), dec)
    man = SC + f"checkpoint_snapshots/SCA-APP-011_GROUP-3_{DATE}/ACCEPTED_MANIFEST.csv"
    bound = list(csv.DictReader(open(man, encoding="utf-8")))
    mism = []
    for r in bound:
        at_rev = sha_b(subprocess.run(["git", "show", f"{ACCEPTED_REV}:{r['Path']}"], capture_output=True,
                                      check=True).stdout)
        if at_rev != r["SHA256"]:
            mism.append(r["Path"])
    check("1. group-3 manifest binds the accepted revision", not mism, f"{len(bound)} entries; mismatches {len(mism)}")

    # 2. E47 and the other 15 files
    edits, _ = b.load_edits()
    cond = [e for e in edits if e.get("conditional")]
    cand = git_show(ACCEPTED_REV, DECOMP)
    errs: list = []
    final, _ = b.apply_edits(cand, cond, DATE, errs, DECOMP)
    check("2. E47 applied exactly (candidate + E47 with the date)", not errs and sha(DECOMP) == sha_b(final.encode("utf-8")),
          sha(DECOMP))
    others = [p for p in expected if p != DECOMP]
    same = [p for p in others if sha(p) == expected[p]]
    check("2. other 15 files keep their accepted candidate hash", len(same) == len(others) == 15, f"{len(same)}/{len(others)}")

    # 3. _LATEST.md
    tpl = open(G3 + "LATEST_POSTIMAGE.md", encoding="utf-8").read()
    check("3. _LATEST.md equals the filled template", open(SC + "_LATEST.md", encoding="utf-8").read()
          == tpl.replace("{APPLICATION_DATE}", DATE), sha(SC + "_LATEST.md"))

    # 4. Runtime notice
    tpl = open(G3 + "RUNTIME_NOTICE_POSTIMAGE.md", encoding="utf-8").read()
    check("4. Runtime notice equals the filled template", os.path.isfile(NOTICE)
          and open(NOTICE, encoding="utf-8").read() == tpl.replace("{APPLICATION_DATE}", DATE), NOTICE)

    # 5. Status records
    st = open(G3 + "STATUS_RECORDS_POSTIMAGE.md", encoding="utf-8").read()
    afters = re.findall(r"After \(exact line\):\n\n```text\n(.*?)\n```", st, re.S)
    fill = lambda t: t.replace("{APPLICATION_DATE}", DATE).replace("{OWNER_ACT_VERBATIM}", ACT).replace("{UTC}", UTC)
    brief = open(SNAP + "Brief.md", encoding="utf-8").read().split("\n")
    dlog = open(SNAP + "Decision_Log.md", encoding="utf-8").read().split("\n")
    check("5. Brief.md status line", brief[2] == fill(afters[0]))
    check("5. Decision_Log.md G3 row", fill(afters[1]) in dlog)
    hs = fill(open(G3 + "HANDOFF_STATE_POSTIMAGE.md", encoding="utf-8").read())
    check("5. Handoff_State.md equals the filled template", open(SNAP + "Handoff_State.md", encoding="utf-8").read() == hs,
          sha(SNAP + "Handoff_State.md"))

    # 6. Registered tools on the applied state (group-1 builder, output redirected here)
    builder = SNAP + "Evidence/Group1/build_pre_change_baseline.py"
    src = open(builder, encoding="utf-8").read()
    subs = [('os.path.join(SNAP_REL, "Pre_Change_Coverage.json")', f'os.path.join({REL_HERE!r}, "POST_ACCEPTANCE_COVERAGE.json")'),
            ('"run_label": "SCA_APP_011_GROUP1_PRECHANGE"', '"run_label": "SCA_APP_011_POST_ACCEPTANCE"'),
            ('"DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-03-03", "DEL-05-01", "DEL-07-02",',
             '"DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-03-03", "DEL-05-01", "DEL-07-01", "DEL-07-02",'),
            ('"active_snapshot": "execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/"',
             '"active_snapshot": "execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/"')]
    for a, c in subs:
        assert src.count(a) == 1, a
        src = src.replace(a, c)
    mod = types.ModuleType("post_acceptance_builder")
    exec(compile(src, builder + " (post-acceptance substitutions)", "exec"), mod.__dict__)
    rc = mod.main()
    post = json.load(open(os.path.join(HERE, "POST_ACCEPTANCE_COVERAGE.json"), encoding="utf-8"))
    cand = json.load(open(SNAP + "Post_Change_Coverage.json", encoding="utf-8"))
    keys = ["repository_topology", "ledger_distribution", "context_envelopes", "forward_coverage", "reverse_coverage",
            "scope_items_without_deliverable", "objectives_without_deliverable", "lifecycle_distribution",
            "issued_deliverables", "affected_lifecycle", "companion_register_sha256"]
    diff = [k for k in keys if post.get(k) != cand.get(k)]
    check("6. coverage and topology equal the reviewed candidate", rc == 0 and not diff, f"differing: {diff}")
    tp, tc = post["tools"], cand["tools"]
    tool_same = (tp["audit_structure"]["summary"] == tc["audit_structure"]["summary"]
                 and tp["audit_structure"]["issues"] == tc["audit_structure"]["issues"]
                 and {k: v for k, v in tp["analyze_dep_closure"].items()} == {k: v for k, v in tc["analyze_dep_closure"].items()}
                 and tp["validate_decomposition_registers"]["findings_by_code"] == tc["validate_decomposition_registers"]["findings_by_code"])
    check("6. registered tools unchanged (audit_structure, analyze_dep_closure, validate_decomposition_registers)", tool_same,
          f"nodes {tp['analyze_dep_closure'].get('graph_nodes')}, edges {tp['analyze_dep_closure'].get('graph_edges')}, "
          f"SCC {tp['analyze_dep_closure'].get('scc_count')}, register findings {tp['validate_decomposition_registers']['findings_by_code']}")
    check("6. decomposition hash moved only by E47", post["decomposition_sha256"] == sha(DECOMP)
          and cand["decomposition_sha256"] == expected[DECOMP])
    check("6. scope-change pointer is the applied _LATEST.md", post["scope_change_pointer_sha256"] == sha(SC + "_LATEST.md"))

    # 7. Supersession --check-map
    p = subprocess.run([sys.executable, "tools/coordination/accumulate_supersession_map.py",
                        "--prior-map", SC + "SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Supersession_Map.csv",
                        "--delta", SNAP + "Supersession_Delta.csv", "--output-map", os.path.join(HERE, ".map.tmp.csv"),
                        "--check-map", SNAP + "Supersession_Map.csv"], capture_output=True, text=True)
    os.remove(os.path.join(HERE, ".map.tmp.csv"))
    check("7. supersession --check-map", p.returncode == 0 and "Findings: 0 total" in p.stdout, p.stdout.strip().split("\n")[-1])

    ok = all(c[1] for c in checks)
    out = ["# SCA-APP-011 post-acceptance validation\n\n",
           f"Owner act: \"{ACT}\" ({DATE}; `checkpoint_snapshots/SCA-APP-011_GROUP-3_{DATE}/`). Accepted revision "
           f"`{ACCEPTED_REV[:9]}`. Record `{UTC}`. Written by `verify_post_acceptance.py`; candidate evidence reviewed at "
           "group 3 is not modified.\n\n",
           "| Check | Result | Detail |\n|---|---|---|\n"]
    for name, good, detail in checks:
        out.append(f"| {name} | {'PASS' if good else 'FAIL'} | {detail} |\n")
    out.append(f"\nResult: {'PASS' if ok else 'FAIL'}\n")
    open(os.path.join(HERE, "POST_ACCEPTANCE_VALIDATION.md"), "w", encoding="utf-8").write("".join(out))
    print("PASS" if ok else "FAIL")
    for name, good, detail in checks:
        print(("  ok   " if good else "  FAIL ") + name, detail)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
