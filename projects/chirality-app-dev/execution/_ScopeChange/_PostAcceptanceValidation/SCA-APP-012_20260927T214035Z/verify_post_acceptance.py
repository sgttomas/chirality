#!/usr/bin/env python3
"""SCA-APP-012 post-acceptance validation (append-only record; read-only on inputs).

Run from the repository root after the acceptance-conditional edits are applied
and committed:

    python3 projects/chirality-app-dev/execution/_ScopeChange/_PostAcceptanceValidation/SCA-APP-012_20260927T214035Z/verify_post_acceptance.py

It compares the applied bytes with the acceptance-conditional list
(Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv) and its templates, checks
that the group-3 manifest binds the accepted revision, reruns the registered
tools on the applied state through the accepted group-1 coverage builder (with
the group-3 wrapper's substitutions; output redirected into this folder),
reruns the supersession --check-map, and writes POST_ACCEPTANCE_VALIDATION.md
and POST_ACCEPTANCE_COVERAGE.json here. Every git call runs with all GIT_*
variables removed and must succeed. It does not modify the candidate evidence
reviewed at group 3.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import types

CLEAN_ENV = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
for _k in [k for k in os.environ if k.startswith("GIT_")]:
    del os.environ[_k]

HERE = os.path.dirname(os.path.abspath(__file__))
REL_HERE = os.path.relpath(HERE)
SC = "projects/chirality-app-dev/execution/_ScopeChange/"
SNAP = SC + "SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/"
G2 = SNAP + "Evidence/Group2/"
G3 = SNAP + "Evidence/Group3/"
DATE = "2026-09-27"
ACT = "I accept SCA-APP-012 checkpoint group 3"
UTC = os.path.basename(HERE).split("_", 1)[1]
DECOMP = "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
ACCEPTED_REV = "ac67109d931eb5a4609bc5ad7c656ac938f6f15b"


def sha_b(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha(p: str) -> str:
    return sha_b(open(p, "rb").read())


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git(*args) -> bytes:
    p = subprocess.run(["git", *args], capture_output=True, env=CLEAN_ENV)
    if p.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed: {p.stderr.decode(errors='replace').strip()}")
    return p.stdout


def main() -> int:
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    fin = load("group3_finalize", G3 + "group3_finalize.py")
    b = load("build_amendment_preview", G2 + "build_amendment_preview.py")
    rows = list(csv.DictReader(open(G2 + "PREIMAGE_POSTIMAGE.csv", newline="", encoding="utf-8")))
    cand_hash = {r["File"]: r["CandidateSHA256"] for r in rows}

    # 1. Group-3 decision folder and manifest
    dec = SC + f"checkpoint_snapshots/SCA-APP-012_GROUP-3_{DATE}/DECISION.md"
    text = open(dec, encoding="utf-8").read()
    first = next(ln.strip() for ln in text.split("\n") if ln.strip())
    check("1. decision folder heading and verbatim act", first.startswith(fin.HEADING) and f"> {ACT}" in text.split("\n"), dec)
    committed = git("ls-files", "--", dec).decode().strip() == dec and subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", dec], env=CLEAN_ENV).returncode == 0
    check("1. decision folder committed and unchanged", committed)
    man = SC + f"checkpoint_snapshots/SCA-APP-012_GROUP-3_{DATE}/ACCEPTED_MANIFEST.csv"
    bound = list(csv.DictReader(open(man, encoding="utf-8")))
    mism = []
    for r in bound:
        if r["SHA256"].startswith("git-tree:"):
            got = "git-tree:" + git("rev-parse", f"{ACCEPTED_REV}:{r['Path'].rstrip('/')}").decode().strip()
        else:
            got = sha_b(git("show", f"{ACCEPTED_REV}:{r['Path']}"))
        if got != r["SHA256"]:
            mism.append(r["Path"])
    check("1. group-3 manifest binds the accepted revision", not mism, f"{len(bound)} entries; mismatches {len(mism)}")

    # 2. E26 and the other 11 files
    edits, _ = b.load_edits()
    cond = [e for e in edits if e.get("conditional")]
    cand = git("show", f"{ACCEPTED_REV}:{DECOMP}").decode("utf-8")
    errs: list = []
    final, _ = b.apply_edits(cand, cond, DATE, errs, DECOMP)
    check("2. candidate decomposition at the accepted revision has its candidate hash",
          sha_b(cand.encode("utf-8")) == cand_hash[DECOMP], cand_hash[DECOMP])
    check("2. E26 applied exactly (candidate + E26 with the date)", not errs and sha(DECOMP) == sha_b(final.encode("utf-8")),
          sha(DECOMP))
    others = [p for p in cand_hash if p != DECOMP]
    same = [p for p in others if sha(p) == cand_hash[p]]
    check("2. other 11 files keep their accepted candidate hash", len(same) == len(others) == 11, f"{len(same)}/{len(others)}")

    # 3. _LATEST.md
    tpl = open(G3 + "LATEST_POSTIMAGE.md", encoding="utf-8").read()
    check("3. _LATEST.md equals the filled template", open(SC + "_LATEST.md", encoding="utf-8").read()
          == fin.fill(tpl, DATE), sha(SC + "_LATEST.md"))

    # 4-6. Status records
    brief = open(SNAP + "Brief.md", encoding="utf-8").read().split("\n")
    dlog = open(SNAP + "Decision_Log.md", encoding="utf-8").read().split("\n")
    check("4. Brief.md status line", brief[2] == fin.fill(fin.BRIEF_AFTER, DATE, ACT))
    check("5. Decision_Log.md G3 row", fin.fill(fin.G3_AFTER, DATE, ACT) in dlog
          and not any(ln.startswith(fin.G3_BEFORE_PREFIX) for ln in dlog))
    hs = fin.fill(open(G3 + "HANDOFF_STATE_POSTIMAGE.md", encoding="utf-8").read(), DATE, ACT, UTC)
    check("6. Handoff_State.md equals the filled template", open(SNAP + "Handoff_State.md", encoding="utf-8").read() == hs,
          sha(SNAP + "Handoff_State.md"))

    # 7. Registered tools on the applied state (group-1 builder with the group-3 wrapper's substitutions)
    w = load("build_post_change_coverage", G3 + "build_post_change_coverage.py")
    head = git("rev-parse", "HEAD").decode().strip()
    builder = SNAP + "Evidence/Group1/build_pre_change_baseline.py"
    src = open(builder, encoding="utf-8").read()
    out_rel = os.path.join(REL_HERE, "POST_ACCEPTANCE_COVERAGE.json")
    subs = [(w.OLD_BASIS, f'BASIS_COMMIT = "{head}"'),
            (w.OLD_OUT, f"out = {out_rel!r}"),
            (w.OLD_LABEL, '"run_label": "SCA_APP_012_POST_ACCEPTANCE"'),
            (w.OLD_TOKENS, w.NEW_TOKENS),
            ('"active_snapshot": "execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/"',
             '"active_snapshot": "execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/"')]
    for a, c in subs:
        assert src.count(a) == 1, a
        src = src.replace(a, c)
    mod = types.ModuleType("post_acceptance_builder")
    mod.__dict__["PRE_LEGACY_TOKENS"] = sorted(json.load(open(SNAP + "Pre_Change_Coverage.json", encoding="utf-8"))["legacy_css_tokens"])
    exec(compile(src, builder + " (post-acceptance substitutions)", "exec"), mod.__dict__)
    rc = mod.main()
    post = json.load(open(out_rel, encoding="utf-8"))
    cj = json.load(open(SNAP + "Post_Change_Coverage.json", encoding="utf-8"))
    keys = ["repository_topology", "ledger_distribution", "forward_coverage", "reverse_coverage",
            "scope_items_without_deliverable", "objectives_without_deliverable", "lifecycle_distribution",
            "issued_deliverables", "checking_deliverables", "affected_deliverables", "affected_scope_items",
            "objective_active_supporters", "dependency_rows", "frontend_reachability", "frontend_references",
            "legacy_css_tokens", "dead_css_candidates", "companion_register_sha256"]
    diff = [k for k in keys if post.get(k) != cj.get(k)]
    topo = post["repository_topology"]
    check("7. coverage and topology equal the reviewed candidate", rc == 0 and not diff,
          f"differing: {diff}; packages {topo['packages']}, deliverables {topo['deliverables']}, scope items "
          f"{topo['scope_items']}, objectives {topo['objectives']}")
    tp, tc = post["tools"], cj["tools"]
    tool_same = (tp["audit_structure"]["summary"] == tc["audit_structure"]["summary"]
                 and tp["audit_structure"]["issues"] == tc["audit_structure"]["issues"]
                 and tp["analyze_dep_closure"] == tc["analyze_dep_closure"]
                 and tp["validate_decomposition_registers"]["findings_by_code"] == tc["validate_decomposition_registers"]["findings_by_code"])
    c = tp["analyze_dep_closure"]
    check("7. registered tools unchanged (audit_structure, analyze_dep_closure, validate_decomposition_registers)", tool_same,
          f"nodes {c.get('graph_nodes')}, edges {c.get('graph_edges')}, SCC {c.get('scc_count')}, "
          f"register findings {tp['validate_decomposition_registers']['findings_by_code']}")
    check("7. decomposition hash moved only by E26", post["decomposition_sha256"] == sha(DECOMP)
          and cj["decomposition_sha256"] == cand_hash[DECOMP])
    check("7. scope-change pointer is the applied _LATEST.md", post["scope_change_pointer_sha256"] == sha(SC + "_LATEST.md"))

    # 8. Supersession --check-map
    tmp = os.path.join(HERE, ".map.tmp.csv")
    p = subprocess.run([sys.executable, "tools/coordination/accumulate_supersession_map.py",
                        "--prior-map", SC + "SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/Supersession_Map.csv",
                        "--delta", SNAP + "Supersession_Delta.csv", "--output-map", tmp,
                        "--check-map", SNAP + "Supersession_Map.csv"], capture_output=True, text=True, env=CLEAN_ENV)
    if os.path.exists(tmp):
        os.remove(tmp)
    check("8. supersession --check-map", p.returncode == 0 and "Findings: 0 total" in p.stdout, p.stdout.strip().split("\n")[-1])

    ok = all(c[1] for c in checks)
    out = ["# SCA-APP-012 post-acceptance validation\n\n",
           f"Owner act: \"{ACT}\" ({DATE}; `checkpoint_snapshots/SCA-APP-012_GROUP-3_{DATE}/`). Accepted revision "
           f"`{ACCEPTED_REV[:9]}`. Applied state `{head[:9]}`. Record `{UTC}`. Written by `verify_post_acceptance.py`; "
           "candidate evidence reviewed at group 3 is not modified.\n\n",
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
