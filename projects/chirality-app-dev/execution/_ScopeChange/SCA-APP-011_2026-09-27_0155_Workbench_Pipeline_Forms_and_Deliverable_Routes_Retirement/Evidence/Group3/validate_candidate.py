#!/usr/bin/env python3
"""SCA-APP-011 group-3 candidate validation (read-only).

Run from the repository root:

    python3 <SCA folder>/Evidence/Group3/validate_candidate.py --accepted-commit C2 [--head REV]

C2 is the commit that recorded the accepted group-2 snapshot; REV (default
HEAD) is the integrated candidate revision (scope text plus the code change).
The script checks the working tree, which must hold REV's content. It modifies
no scope file and writes only its report, Evidence/Group3/CANDIDATE_VALIDATION.md:

  1. every file in PREIMAGE_POSTIMAGE.csv has its expected group-3 candidate
     hash (group3_corrections.py: the group-2 candidate hash, a basis-refreshed
     hash, or a corrected hash); each basis refresh is re-derived by applying
     the accepted edits to the file at the refresh's basis commit;
  2. every non-conditional edit's `new` text (with any group-3 correction
     applied) is present and its `old` text is absent (unless `old` is contained
     in `new`); E47 is not applied and no `{APPLICATION_DATE}` literal is in any
     written file;
  3. write containment against the integrated revision: among scope-text paths
     (App docs, the decomposition, every ScopeOfWork.md and _CONTEXT.md), the
     paths changed between C2 and REV are exactly the 16 files of the accepted
     write boundary; every other changed path belongs to the code-change
     categories of Propagation_Plan.md section 4 or to the SCA folder; no
     _STATUS.md, Dependencies.csv, _LATEST.md or companion register changed;
  4. tools/scope_of_work/validate_scope_of_work.py passes on each written
     Scope of Work;
  5. across every deliverable ScopeOfWork.md and _CONTEXT.md, no line names a
     retired route or scaffold-route obligation without an SCA-APP-011 marker
     or an SCA-APP-011 section that states it controls;
  6. table rows written by an edit keep the column count of the rows they
     replace.
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
OBLIGATION = re.compile(r"/api/working-root/deliverable/(status|dependencies)|/api/harness/scaffold|"
                        r"scaffoldHarnessExecutionRoot|deliverable-api\.ts|scaffold-route\.test|"
                        r"deliverable-contracts\.test\.ts|scaffold, and contract APIs|"
                        r"dependency API route|status API route|scaffold (operation|composition)")
CONTROLS = re.compile(r"SCA-APP-011[^\n]*\n(?:[^\n]*\n){0,12}?[^\n]*this section controls", re.I)


def sha(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def pipes(line: str) -> int:
    return line.count("|") - line.count("\\|")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--accepted-commit", required=True)
    ap.add_argument("--head", default="HEAD")
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location("amendment_edits", os.path.join(G2, "amendment_edits.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    edits = mod.EDITS
    spec3 = importlib.util.spec_from_file_location("group3_corrections", os.path.join(HERE, "group3_corrections.py"))
    g3 = importlib.util.module_from_spec(spec3)
    spec3.loader.exec_module(g3)
    _, expected = g3.expected_hashes()
    rows = list(csv.DictReader(open(os.path.join(G2, "PREIMAGE_POSTIMAGE.csv"), newline="", encoding="utf-8")))
    files = [r["File"] for r in rows]
    failures: list[str] = []
    out = ["# SCA-APP-011 group-3 candidate validation\n\n",
           f"Accepted group-2 commit `{args.accepted_commit}`; integrated candidate revision `{args.head}`. "
           "The script modifies no scope file and writes only this report.\n\n"]

    # 1. candidate hashes
    ok = 0
    for r in rows:
        if sha(r["File"]) == expected[r["File"]]:
            ok += 1
        else:
            failures.append(f"candidate hash mismatch: {r['File']}")
    spec_b = importlib.util.spec_from_file_location("build_amendment_preview", os.path.join(G2, "build_amendment_preview.py"))
    b = importlib.util.module_from_spec(spec_b)
    spec_b.loader.exec_module(b)
    rederived = 0
    for rf in g3.BASIS_REFRESH:
        base = subprocess.run(["git", "show", f"{rf['basis_commit']}:{rf['file']}"], capture_output=True,
                              check=True).stdout.decode("utf-8")
        errs: list = []
        fixed = [e for e in edits if e["file"] == rf["file"] and not e.get("conditional")]
        cand, _ = b.apply_edits(base, fixed, None, errs, rf["file"], base)
        good = (not errs and hashlib.sha256(base.encode()).hexdigest() == rf["basis_preimage_sha256"]
                and hashlib.sha256(cand.encode()).hexdigest() == rf["group3_candidate_sha256"])
        rederived += good
        if not good:
            failures.append(f"{rf['id']}: accepted edits do not re-derive the refreshed candidate for {rf['file']}")
    out.append(f"1. Candidate hashes: {ok}/{len(rows)} files match their expected group-3 candidate hash "
               f"({len(rows) - len(g3.BASIS_REFRESH) - len(g3.CORRECTIONS)} group-2 hash, "
               f"{len(g3.BASIS_REFRESH)} basis refresh, {len(g3.CORRECTIONS)} correction); basis refreshes "
               f"re-derived from their basis commit with the accepted edits: {rederived}/{len(g3.BASIS_REFRESH)}.\n")

    # 2. edits present, E47 withheld, no slot literal
    present = 0
    for e in edits:
        text = open(e["file"], encoding="utf-8").read()
        if e.get("conditional"):
            if e["old"] not in text:
                failures.append(f"{e['id']}: acceptance-conditional old text is not present (applied early?)")
            continue
        new = e["new"]
        for c in g3.CORRECTIONS:
            if c["file"] == e["file"] and c["old"] in new:
                new = new.replace(c["old"], c["new"], 1)
        if new in text and (e["old"] in new or e["old"] not in text):
            present += 1
        else:
            failures.append(f"{e['id']}: new text absent or old text still present in {e['file']}")
    slot_files = [f for f in files if SLOT in open(f, encoding="utf-8").read()]
    failures += [f"{SLOT} literal in {f}" for f in slot_files]
    cond = [e["id"] for e in edits if e.get("conditional")]
    out.append(f"2. Non-conditional edits present: {present}/{len(edits) - len(cond)}; acceptance-conditional "
               f"edits withheld: {', '.join(cond)}; files carrying a `{SLOT}` literal: {len(slot_files)}.\n")

    # 3. write containment against the integrated revision
    changed = subprocess.run(["git", "diff", "--name-only", args.accepted_commit, args.head],
                             capture_output=True, text=True, check=True).stdout.split()
    app = "projects/chirality-app-dev/"
    scope_rx = re.compile(re.escape(app) + r"(docs/[^/]+\.md|execution/_Decomposition/.*|"
                          r"execution/PKG-[^/]+/[^/]+/DEL-[^/]+/(ScopeOfWork|_CONTEXT)\.md)$")
    code_rx = re.compile(r"^(" + re.escape(app) + r"frontend/src/.*|"
                         + re.escape(app) + r"execution/PKG-[^/]+/[^/]+/DEL-[^/]+/MEMORY\.md|"
                         + re.escape(app) + r"execution/PKG-03_[^/]+/1_Working/DEL-03-03_[^/]+/RouteAdapterTestIndex\.md|"
                         + re.escape(app) + r"execution/_Coordination/AgentRuns/APP-REMOVE-LEGACY-FORMS-2026-09-27/.*|"
                         + re.escape(app) + r"execution/_Coordination/AgentRuns/APP-TRANSITION-FORMS-2026-09-26/RECEIPT\.md|"
                         + re.escape(app) + r"execution/_Coordination/WorkGraphs/app-lifecycle-deps-2026-09-26/WORK_GRAPH\.md|"
                         + re.escape(app) + r"loop/LOOP_RECEIPTS\.md|"
                         r"docs/governance_harness/tranche_manifests/APP-REMOVE-LEGACY-FORMS-20260927\.yaml|"
                         r"exports/chirality-app/.*|"
                         + re.escape(os.path.relpath(SNAP)) + r"/.*)$")
    protected_rx = re.compile(r"(/_STATUS\.md|/Dependencies\.csv|_ScopeChange/_LATEST\.md|"
                              r"contract_invariant_coverage_register\.csv)$")
    scope_changed = [p for p in changed if scope_rx.match(p)]
    extra = sorted(set(scope_changed) - set(files))
    missing = sorted(set(files) - set(scope_changed))
    protected = sorted(p for p in changed if protected_rx.search(p))
    other = sorted(p for p in changed if not scope_rx.match(p) and not code_rx.match(p))
    failures += [f"scope text outside write boundary: {p}" for p in extra]
    failures += [f"not written: {p}" for p in missing]
    failures += [f"protected path changed: {p}" for p in protected]
    failures += [f"path outside the code-change categories: {p}" for p in other]
    n_code = len([p for p in changed if code_rx.match(p)])
    out.append(f"3. Write containment (`{args.accepted_commit}..{args.head}`): {len(changed)} paths changed; scope-text "
               f"paths {len(scope_changed)} (outside the accepted boundary: {len(extra)}; boundary files not written: "
               f"{len(missing)}); code-change and SCA-folder paths {n_code}; protected paths changed: {len(protected)}; "
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

    # 5. sweep
    pattern = "projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/"
    swept, uncovered = 0, []
    for path in sorted(glob.glob(pattern + "ScopeOfWork.md") + glob.glob(pattern + "_CONTEXT.md")):
        swept += 1
        text = open(path, encoding="utf-8").read()
        if CONTROLS.search(text) or ("this section controls" in text and "SCA-APP-011" in text):
            continue
        for n, ln in enumerate(text.split("\n"), 1):
            if OBLIGATION.search(ln) and "SCA-APP-011" not in ln:
                uncovered.append(f"{path}:{n}")
    failures += [f"uncovered retired obligation {u}" for u in uncovered]
    out.append(f"5. Deliverable contracts and contexts swept: {swept}; uncovered lines naming a retired route or "
               f"scaffold-route obligation: {len(uncovered)}.\n")

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

    out.append(f"\nResult: {'PASS' if not failures else 'FAIL'}\n")
    out += [f"- {f}\n" for f in failures]
    open(REPORT, "w", encoding="utf-8").write("".join(out))
    print("PASS" if not failures else "FAIL", os.path.relpath(REPORT))
    for f in failures:
        print(" ", f)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
