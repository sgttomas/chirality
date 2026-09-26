#!/usr/bin/env python3
"""Containment check for the D-PEC-95 act branch (read-only; run from the repository root).

Classifies every path in `git diff --name-status <base>...HEAD` as one of the
119 granted product paths (MODIFY), a Task Management register (MODIFY, T1),
a run-root file, or the brief-authorized return file. Anything else fails.
Usage: python3 containment.py <base ref>
"""
import collections
import subprocess
import sys

RR = "projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/"
REPORT = RR + "gen_d95_report.tsv"
TM = {"projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv",
      "projects/pec/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv"}
RETURN = "projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/U1_D95_CURRENCY_ACT.md"


def main():
    grant = {ln.split("\t")[1] for ln in open(REPORT, encoding="utf-8").read().splitlines()
             if ln.startswith("WRITE\t")}
    out = subprocess.run(["git", "diff", "--name-status", f"{sys.argv[1]}...HEAD"],
                         capture_output=True, text=True, check=True).stdout
    counts = collections.Counter()
    bad = []
    seen = set()
    for line in out.splitlines():
        status, path = line.split("\t", 1)
        seen.add(path)
        if path in grant and status == "M":
            counts["product MODIFY"] += 1
        elif path in TM and status == "M":
            counts["Task Management MODIFY (T1)"] += 1
        elif path.startswith(RR) and status == "A":
            counts["run root ADD"] += 1
        elif path == RETURN and status == "A":
            counts["return ADD"] += 1
        else:
            bad.append(line)
    for k in sorted(counts):
        print(f"{counts[k]}\t{k}")
    missing = sorted(grant - seen)
    print(f"granted paths not changed: {len(missing)}")
    for m in missing:
        print(f"  {m}")
    print(f"outside the boundary: {len(bad)}")
    for b in bad:
        print(f"  {b}")
    ok = not bad and not missing and counts["product MODIFY"] == 119
    print("RESULT\t" + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
