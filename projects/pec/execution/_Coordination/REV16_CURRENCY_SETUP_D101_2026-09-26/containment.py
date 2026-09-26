#!/usr/bin/env python3
"""Containment of the D-PEC-101 act branch (run from the repository root).

Usage: python3 containment.py <proposal.md> <base-ref> [--with-v]
Reads `git diff --name-status <base-ref>...HEAD` and classifies each path as a granted
product path (the proposal's 161, with the tabled act: M for modified, A for created),
the run root, the brief-authorized AgentRuns brief/return copies, (with --with-v) the
COV_D101_POSTSETUP_* audit folder and DecompCoverage/_LATEST.md, or OUTSIDE. Exit 0 when
every granted path appears with its act and nothing is OUTSIDE.
"""
import re, subprocess, sys
prop, base = sys.argv[1], sys.argv[2]
with_v = "--with-v" in sys.argv
EX = "projects/pec/execution/"
grant, sec = {}, None
for line in open(prop, encoding="utf-8"):
    if line.startswith("### Part K4"): sec = "k4"
    elif line.startswith("### Part K1"): sec = "k1"
    elif line.startswith("### ") or line.startswith("## "): sec = None
    if sec and line.startswith("| ") and "`PKG-" in line:
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        grant[EX + c[1].strip("`")] = "A" if c[0] == "CREATE" else "M"
RR = EX + "_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/"
AR = EX + "_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/"
admin = re.compile(r"^" + re.escape(AR) + r"(briefs/K14A_D101_ACT\.md|returns/K14A_D101_ACT\.md)$")
audit = re.compile(r"^" + re.escape(EX) + r"_Evaluation/DecompCoverage/(COV_D101_POSTSETUP_\d{4}-\d\d-\d\d_\d{4}/[^/]+|_LATEST\.md)$")
out = subprocess.run(["git", "diff", "--name-status", "--no-renames", f"{base}...HEAD"], capture_output=True, text=True, check=True).stdout
seen, counts, outside = {}, {"product": 0, "run_root": 0, "agentruns": 0, "audit": 0}, []
for ln in out.splitlines():
    st, p = ln.split("\t", 1)
    if p in grant: seen[p] = st; counts["product"] += 1
    elif p.startswith(RR): counts["run_root"] += 1
    elif admin.match(p): counts["agentruns"] += 1; print("ADMIN", st, p)
    elif with_v and audit.match(p): counts["audit"] += 1; print("AUDIT", st, p)
    else: outside.append(ln)
wrong = [p for p, a in grant.items() if seen.get(p) != a]
print("COUNTS", counts)
print("granted paths present with their tabled act:", len(grant) - len(wrong), "/", len(grant))
for p in wrong: print("MISSING_OR_WRONG_ACT", seen.get(p), grant[p], p)
for o in outside: print("OUTSIDE", o)
ok = not wrong and not outside
print("RESULT", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
