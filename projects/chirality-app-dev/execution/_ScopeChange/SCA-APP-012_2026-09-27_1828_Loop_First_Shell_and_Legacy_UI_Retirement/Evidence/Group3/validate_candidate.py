#!/usr/bin/env python3
"""SCA-APP-012 group-3 candidate validation (read-only on scope files).

Run from the repository root of this checkout:

    validate_candidate.py --accepted-commit C2 [--head REV] [--integrated]
                          [--code-record PREFIX ...]

C2 is the commit that recorded the accepted group-2 snapshot. REV (default
HEAD) is the candidate revision; the working tree must hold REV's content.
Without --integrated the candidate is the scope text alone; with it, REV also
carries the code change of Propagation_Plan.md section 4, and the code checks
(7) become requirements. --code-record adds a repository-relative path prefix
that the code change may write for its records (run receipt folder, tranche
manifest); the fixed code-record categories are listed in CODE_PATHS.

Every git call runs with all GIT_* variables removed from the environment and
must succeed; before any git call the script refuses unless the current
directory is the top level of a git work tree, and refuses on any git error.

It writes only its report, Evidence/Group3/CANDIDATE_VALIDATION.md:

  1. every file in PREIMAGE_POSTIMAGE.csv has its recorded candidate hash;
  2. every non-conditional edit's `new` text is present and its `old` text is
     absent (unless `old` is contained in `new`); E26 is withheld (its `old`
     text is present) and no `{APPLICATION_DATE}` literal is in any file;
  3. write containment between C2 and REV: the scope-text paths changed are
     exactly the 12 files of the accepted write boundary; every other changed
     path is in the SCA folder or in a code-change category; no protected path
     changed (_STATUS.md, Dependencies.csv, _DEPENDENCIES.md, _LATEST.md, the
     companion register, the Task Management register, the frozen
     electron/renderer-window-policy.ts, the Electron probe, the packaged
     security proof and the contract pins);
  4. tools/scope_of_work/validate_scope_of_work.py passes on each written Scope
     of Work;
  5. the retired-item sweep of Evidence/Group2/validate_postimage.py, on the
     current bytes: no uncovered unit across every deliverable ScopeOfWork.md
     and _CONTEXT.md, the decomposition, PRD, SPEC, PLAN, DIRECTIVE and TYPES;
  6. table rows written by edits keep the column count of the rows they
     replace;
  7. code alignment: every live file the scope text cites exists (with
     --integrated, including the new role-picker test); every module the code
     specification deletes is absent (with --integrated) or still present
     (scope-text-only candidate, expected); the frozen renderer-window-policy.ts
     keeps its pinned hash; both kept page routes exist.
"""
from __future__ import annotations

import argparse
import csv
import glob
import hashlib
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.dirname(os.path.dirname(HERE))
G2 = os.path.join(SNAP, "Evidence", "Group2")
REPORT = os.path.join(HERE, "CANDIDATE_VALIDATION.md")
SLOT = "{APPLICATION_DATE}"
APP = "projects/chirality-app-dev/"
FE = APP + "frontend/"
CLEAN_ENV = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
FROZEN = {FE + "electron/renderer-window-policy.ts":
          "e2d63d32423d1ef6b0a03259235676ac9cefadde00e4f067be4f13e5ed2cc3ed"}
# Live files the written scope text cites; they must exist (NEW ones only after the code change).
CITED_LIVE = [
    "src/__tests__/components/loop-tertiary-routes.test.ts",
    "src/__tests__/components/woven-dialogue-route.test.tsx",
    "src/__tests__/lib/guarded-session-selection.test.ts",
    "src/__tests__/lib/persona-resolution.test.ts",
    "src/__tests__/lib/pkg08-compatibility-boundaries.test.ts",
    "src/__tests__/lib/pipeline-dispatch-contract.test.ts",
    "src/__tests__/api/harness/routes.test.ts",
    "src/__tests__/components/woven-dialogue-shell.test.tsx",
    "src/__tests__/components/woven-dialogue-navigator.test.tsx",
    "src/__tests__/components/woven-dialogue-controls.test.tsx",
    "src/__tests__/components/chat-panel-folder-binding.test.tsx",
    "src/components/shell/chat-panel.tsx",
    "src/lib/shell/persona-resolution.ts",
    "src/lib/workspace/task-scope.ts",
    "src/lib/woven-dialogue/guarded-session-selection.ts",
    "src/components/woven-dialogue/method-library-view.tsx",
    "src/app/api/project/deliverables/route.ts",
    "src/app/workbench/page.tsx",
    "src/app/pipeline/page.tsx",
]
CITED_NEW = ["src/__tests__/components/chat-panel-role-picker-guard.test.tsx"]
# Propagation_Plan.md section 4, "Delete".
DELETED = [
    "src/components/shell/loop-shell.tsx", "src/components/shell/portal-loop-shell.tsx",
    "src/components/shell/loop-tertiary-shell.tsx", "src/components/shell/sidebar-right-loop-layout.tsx",
    "src/components/shell/tertiary-sidebar-tabs.tsx", "src/components/portal/agent-matrix.tsx",
    "src/__tests__/components/agent-matrix-panel.test.ts", "src/lib/portal/agent-matrix-cells.ts",
    "src/lib/portal/agent-matrix-launch.ts", "src/__tests__/lib/agent-matrix-launch.test.ts",
    "src/__tests__/lib/agent-matrix-cells.test.ts", "src/components/workspace/deliverables-provider.tsx",
    "src/app/api/working-root/scope/route.ts", "src/components/woven-dialogue/workflows-view.tsx",
    "src/components/woven-dialogue/workflow-detail.tsx", "src/__tests__/components/woven-workflows.test.tsx",
    "src/app/api/working-root/workflow/route.ts", "src/app/api/working-root/workflow/workflow-store.ts",
    "src/app/api/working-root/workflow/workflow-read-contract.ts",
    "src/__tests__/api/working-root-workflow.test.ts",
]
CODE_PATHS = [
    re.escape(FE) + r"src/.*",
    re.escape(APP) + r"execution/PKG-02_[^/]+/1_Working/DEL-02-0[123]_[^/]+/MEMORY\.md",
    re.escape(APP) + r"execution/PKG-08_[^/]+/1_Working/DEL-08-02_[^/]+/MEMORY\.md",
    re.escape(APP) + r"loop/LOOP_RECEIPTS\.md",
    r"exports/chirality-app/.*",
]
PROTECTED = re.compile(r"(/_STATUS\.md|/Dependencies\.csv|/_DEPENDENCIES\.md|_ScopeChange/_LATEST\.md|"
                       r"contract_invariant_coverage_register\.csv|_TaskManagement/REGISTER\.csv|"
                       r"frontend/electron/renderer-window-policy\.ts|frontend/electron/main\.ts|"
                       r"frontend/scripts/run-packaged-security-proof\.mjs|"
                       r"frontend/src/__tests__/contract-pins\.manifest\.ts)$")


def git(*args: str) -> str:
    p = subprocess.run(["git", *args], capture_output=True, text=True, env=CLEAN_ENV)
    if p.returncode != 0:
        raise SystemExit(f"refused: git {' '.join(args)} failed ({p.returncode}): {p.stderr.strip()}")
    return p.stdout


def require_repo_top() -> None:
    top = git("rev-parse", "--show-toplevel").strip()
    if os.path.realpath(top) != os.path.realpath(os.getcwd()):
        raise SystemExit(f"refused: run from the top of the work tree ({top})")


def sha(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def pipes(line: str) -> int:
    return line.count("|") - line.count("\\|")


def load(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--accepted-commit", required=True)
    ap.add_argument("--head", default="HEAD")
    ap.add_argument("--integrated", action="store_true")
    ap.add_argument("--code-record", action="append", default=[])
    args = ap.parse_args()
    require_repo_top()
    c2 = git("rev-parse", "--verify", args.accepted_commit + "^{commit}").strip()
    rev = git("rev-parse", "--verify", args.head + "^{commit}").strip()
    edits = load("amendment_edits", os.path.join(G2, "amendment_edits.py")).EDITS
    sweep = load("validate_postimage", os.path.join(G2, "validate_postimage.py"))
    rows = list(csv.DictReader(open(os.path.join(G2, "PREIMAGE_POSTIMAGE.csv"), newline="", encoding="utf-8")))
    files = [r["File"] for r in rows]
    failures: list[str] = []
    mode = "integrated scope text and code" if args.integrated else "scope text only (code change not yet integrated)"
    out = ["# SCA-APP-012 group-3 candidate validation\n\n",
           f"Accepted group-2 commit `{c2[:9]}`; candidate revision `{rev[:9]}` ({mode}). Git ran with every "
           "`GIT_*` variable removed. The script modifies no scope file and writes only this report.\n\n"]

    # 1. candidate hashes
    ok = sum(sha(r["File"]) == r["CandidateSHA256"] for r in rows)
    failures += [f"candidate hash mismatch: {r['File']}" for r in rows if sha(r["File"]) != r["CandidateSHA256"]]
    out.append(f"1. Candidate hashes: {ok}/{len(rows)} files match `PREIMAGE_POSTIMAGE.csv`.\n")

    # 2. edits present, E26 withheld, no slot literal
    present = 0
    cond = [e for e in edits if e.get("conditional")]
    for e in edits:
        text = open(e["file"], encoding="utf-8").read()
        if e.get("conditional"):
            if e["old"] not in text:
                failures.append(f"{e['id']}: acceptance-conditional old text is not present (applied early?)")
            continue
        if e["new"] in text and (e["old"] in e["new"] or e["old"] not in text):
            present += 1
        else:
            failures.append(f"{e['id']}: new text absent or old text still present in {e['file']}")
    slot_files = [f for f in files if SLOT in open(f, encoding="utf-8").read()]
    failures += [f"{SLOT} literal in {f}" for f in slot_files]
    out.append(f"2. Non-conditional edits present: {present}/{len(edits) - len(cond)}; acceptance-conditional edits "
               f"withheld: {', '.join(e['id'] for e in cond)}; files carrying a `{SLOT}` literal: {len(slot_files)}.\n")

    # 3. write containment
    changed = git("diff", "--name-only", c2, rev).split()
    scope_rx = re.compile(re.escape(APP) + r"(docs/[^/]+\.md|execution/_Decomposition/.*|"
                          r"execution/PKG-[^/]+/[^/]+/DEL-[^/]+/(ScopeOfWork|_CONTEXT)\.md)$")
    snap_rel = os.path.relpath(SNAP)
    allowed = [re.compile("^" + p + "$") for p in CODE_PATHS]
    allowed.append(re.compile("^" + re.escape(snap_rel) + "/.*$"))
    allowed += [re.compile("^" + re.escape(p) + ".*$") for p in args.code_record]
    scope_changed = [p for p in changed if scope_rx.match(p)]
    extra = sorted(set(scope_changed) - set(files))
    missing = sorted(set(files) - set(scope_changed))
    protected = sorted(p for p in changed if PROTECTED.search(p))
    other = sorted(p for p in changed if not scope_rx.match(p) and not any(a.match(p) for a in allowed))
    code = [p for p in changed if not scope_rx.match(p) and any(a.match(p) for a in allowed[:len(CODE_PATHS)])]
    code += [p for p in changed if args.code_record and any(p.startswith(c) for c in args.code_record)]
    failures += [f"scope text outside write boundary: {p}" for p in extra]
    failures += [f"not written: {p}" for p in missing]
    failures += [f"protected path changed: {p}" for p in protected]
    failures += [f"path in no permitted category: {p}" for p in other]
    if not args.integrated and code:
        failures += [f"code path changed in a scope-text-only candidate: {p}" for p in code]
    out.append(f"3. Write containment (`{c2[:9]}..{rev[:9]}`): {len(changed)} paths changed; scope-text paths "
               f"{len(scope_changed)} (outside the accepted boundary: {len(extra)}; boundary files not written: "
               f"{len(missing)}); code-change paths {len(code)}; SCA-folder paths "
               f"{sum(p.startswith(snap_rel + '/') for p in changed)}; protected paths changed: {len(protected)}; "
               f"paths in no permitted category: {len(other)}.\n")

    # 4. SOW validator
    out.append("4. `validate_scope_of_work.py` on each written Scope of Work:\n\n| Deliverable folder | Exit |\n|---|---|\n")
    for f in files:
        if f.endswith("ScopeOfWork.md"):
            p = subprocess.run([sys.executable, "tools/scope_of_work/validate_scope_of_work.py", os.path.dirname(f)],
                               capture_output=True, text=True)
            out.append(f"| `{os.path.basename(os.path.dirname(f))}` | {p.returncode} |\n")
            if p.returncode != 0:
                failures.append(f"SOW validator {f}: {p.stdout[-300:]}{p.stderr[-300:]}")
    out.append("\n")

    # 5. retired-item sweep on the current bytes (the group-2 validator's patterns and history list)
    pattern = APP + "execution/PKG-*/1_Working/DEL-*/"
    targets = sorted(glob.glob(pattern + "ScopeOfWork.md") + glob.glob(pattern + "_CONTEXT.md"))
    targets += [APP + "execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"]
    targets += [APP + f"docs/{n}.md" for n in ("PRD", "SPEC", "PLAN", "DIRECTIVE", "TYPES")]
    uncovered, hist = [], 0
    for path in targets:
        text = open(path, encoding="utf-8").read()
        inside = "\n".join(sweep.controlling_blocks(text))
        for n, u in sweep.units(text):
            if not (sweep.RETIRED.search(u) or sweep.OBLIGATION.search(u)) or sweep.MARK in u or u in inside:
                continue
            if any(h[0] == path and h[1] in u for h in sweep.HISTORICAL):
                hist += 1
            else:
                uncovered.append(f"{path}:{n}")
    failures += [f"uncovered retired item {u}" for u in uncovered]
    out.append(f"5. Retired-item sweep: {len(targets)} files; uncovered units: {len(uncovered)}; listed historical "
               f"passages: {hist}.\n")

    # 6. table column counts
    checked = 0
    for e in edits:
        old_rows = [ln for ln in e["old"].split("\n") if ln.lstrip("> ").startswith("|")]
        new_rows = [ln for ln in e["new"].split("\n") if ln.lstrip("> ").startswith("|")]
        if old_rows and new_rows:
            for ln in new_rows:
                checked += 1
                if pipes(ln) != pipes(old_rows[0]):
                    failures.append(f"{e['id']}: table row column count changed")
    out.append(f"6. Table rows written by edits checked for column count: {checked}.\n")

    # 7. code alignment
    live_missing = [p for p in CITED_LIVE if not os.path.isfile(FE + p)]
    new_missing = [p for p in CITED_NEW if not os.path.isfile(FE + p)]
    still = [p for p in DELETED if os.path.exists(FE + p)]
    frozen_bad = [p for p, h in FROZEN.items() if not os.path.isfile(p) or sha(p) != h]
    failures += [f"cited live file missing: {p}" for p in live_missing]
    failures += [f"frozen file changed: {p}" for p in frozen_bad]
    if args.integrated:
        failures += [f"cited new file missing: {p}" for p in new_missing]
        failures += [f"deleted module still present: {p}" for p in still]
    out.append(f"7. Code alignment: cited live files present {len(CITED_LIVE) - len(live_missing)}/{len(CITED_LIVE)}; "
               f"new cited test present {len(CITED_NEW) - len(new_missing)}/{len(CITED_NEW)}"
               f"{'' if args.integrated else ' (expected 0 before the code change)'}; section-4 deletions still "
               f"present {len(still)}/{len(DELETED)}{'' if args.integrated else ' (expected before the code change)'}; "
               f"frozen `renderer-window-policy.ts` at its pinned hash: {'yes' if not frozen_bad else 'NO'}.\n")

    out.append(f"\nResult: {'PASS' if not failures else 'FAIL'}\n")
    out += [f"- {f}\n" for f in failures]
    open(REPORT, "w", encoding="utf-8").write("".join(out))
    print("PASS" if not failures else "FAIL", os.path.relpath(REPORT))
    for f in failures:
        print(" ", f)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
