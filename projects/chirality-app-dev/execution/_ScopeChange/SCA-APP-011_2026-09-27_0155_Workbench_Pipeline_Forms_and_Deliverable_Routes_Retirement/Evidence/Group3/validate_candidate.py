#!/usr/bin/env python3
"""SCA-APP-011 group-3 candidate validation (read-only).

Run from the repository root:

    python3 <SCA folder>/Evidence/Group3/validate_candidate.py --accepted-commit C2 --candidate-commit C3

C2 is the commit that recorded the accepted group-2 snapshot; C3 is the commit
that wrote the candidate scope text. The script checks the tree as it stands
(which must be C3's scope text) and writes Evidence/Group3/CANDIDATE_VALIDATION.md:

  1. every file in PREIMAGE_POSTIMAGE.csv has its recorded candidate hash;
  2. every non-conditional edit's `new` text is present and its `old` text is
     absent (unless `old` is contained in `new`); E47 is not applied and no
     `{APPLICATION_DATE}` literal is in any written file;
  3. write containment: the files changed between C2 and C3 are exactly the 16
     files of the accepted write boundary;
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
    ap.add_argument("--candidate-commit", required=True)
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location("amendment_edits", os.path.join(G2, "amendment_edits.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    edits = mod.EDITS
    rows = list(csv.DictReader(open(os.path.join(G2, "PREIMAGE_POSTIMAGE.csv"), newline="", encoding="utf-8")))
    files = [r["File"] for r in rows]
    failures: list[str] = []
    out = ["# SCA-APP-011 group-3 candidate validation\n\n",
           f"Accepted group-2 commit `{args.accepted_commit}`; candidate commit `{args.candidate_commit}`. "
           "Read-only; the tree is not modified.\n\n"]

    # 1. candidate hashes
    ok = 0
    for r in rows:
        if sha(r["File"]) == r["CandidateSHA256"]:
            ok += 1
        else:
            failures.append(f"candidate hash mismatch: {r['File']}")
    out.append(f"1. Candidate hashes: {ok}/{len(rows)} files match `PREIMAGE_POSTIMAGE.csv`.\n")

    # 2. edits present, E47 withheld, no slot literal
    present = 0
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
    cond = [e["id"] for e in edits if e.get("conditional")]
    out.append(f"2. Non-conditional edits present: {present}/{len(edits) - len(cond)}; acceptance-conditional "
               f"edits withheld: {', '.join(cond)}; files carrying a `{SLOT}` literal: {len(slot_files)}.\n")

    # 3. write containment
    changed = subprocess.run(["git", "diff", "--name-only", args.accepted_commit, args.candidate_commit],
                             capture_output=True, text=True, check=True).stdout.split()
    extra = sorted(set(changed) - set(files))
    missing = sorted(set(files) - set(changed))
    failures += [f"outside write boundary: {p}" for p in extra] + [f"not written: {p}" for p in missing]
    out.append(f"3. Write containment: {len(changed)} files changed between the commits; outside the accepted "
               f"write boundary: {len(extra)}; boundary files not written: {len(missing)}.\n")

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
