#!/usr/bin/env python3
"""Whitespace check for the D-PEC-95 act branch (read-only; run from the repository root).

Runs `git diff --check <base>...HEAD` twice: once excluding this run root
(the 119 product paths and the two Task Management registers), once over the
whole diff. Prints exit codes and the notice count per file.
Usage: python3 diffcheck.py <base ref>
"""
import collections
import subprocess
import sys

RR = "projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25"


def run(args):
    p = subprocess.run(["git", "diff", "--check", f"{sys.argv[1]}...HEAD", "--", *args],
                       capture_output=True, text=True)
    notices = collections.Counter()
    for line in p.stdout.splitlines():
        if not line.startswith("+") and ": " in line:
            path, _, rest = line.partition(":")
            notices[(path, rest.split(": ", 1)[-1])] += 1
    return p.returncode, notices


def main():
    rc, n = run([".", f":(exclude){RR}"])
    print(f"outside run root: exit={rc} notices={sum(n.values())}")
    for (path, kind), c in sorted(n.items()):
        print(f"  {c}\t{kind}\t{path}")
    rc, n = run(["."])
    print(f"whole diff: exit={rc} notices={sum(n.values())}")
    for (path, kind), c in sorted(n.items()):
        print(f"  {c}\t{kind}\t{path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
