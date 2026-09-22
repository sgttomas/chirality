#!/usr/bin/env python3
"""Evidence pack item 1: TOUCHED_PATHS.csv (CONVENTIONS §9).

Usage: touched_paths.py --frozen <frozen-tree> --out <TOUCHED_PATHS.csv>

Read-only git against the frozen tree only:
  git -C <frozen> show --name-only --format= <commit>          (per post-release commit)
  git -C <frozen> blame --line-porcelain 00115c719 -- <path>   (per touched path that exists)
For each path, one row per maximal run of consecutive frozen-basis lines blamed to that commit.
A touched path absent at the frozen basis gets one row with StartLine = EndLine = 0.
A touched path that exists but has no line blamed to the commit (e.g. a later commit overwrote
every line, or a binary/rename-only change) gets no row. Sort: Path, StartLine (then Commit).
"""
import argparse
import csv
import io
import subprocess

COMMITS = ["da95ec194", "cb08dbe2f", "9ecbdecdf", "ccb95e06a"]
BASE = "00115c719"


def git(frozen, *args):
    return subprocess.run(["git", "-C", frozen, *args], check=True, capture_output=True,
                          text=True, errors="replace").stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    full = {c: git(a.frozen, "rev-parse", c).strip() for c in COMMITS}
    touched = {}
    for c in COMMITS:
        for p in git(a.frozen, "show", "--name-only", "--format=", c).splitlines():
            if p.strip():
                touched.setdefault(p.strip(), []).append(c)
    rows = []
    for path in sorted(touched):
        exists = subprocess.run(["git", "-C", a.frozen, "cat-file", "-e", f"{BASE}:{path}"],
                                capture_output=True).returncode == 0
        if not exists:
            for c in touched[path]:
                rows.append((path, c, 0, 0))
            continue
        out = git(a.frozen, "blame", "--line-porcelain", BASE, "--", path)
        lines = []  # (final_line, sha)
        for ln in out.splitlines():
            parts = ln.split(" ")
            if len(parts) >= 3 and len(parts[0]) == 40 and all(ch in "0123456789abcdef" for ch in parts[0]):
                lines.append((int(parts[2]), parts[0]))
        for c in touched[path]:
            nums = sorted(n for n, s in lines if s == full[c])
            start = prev = None
            for n in nums:
                if start is None:
                    start = prev = n
                elif n == prev + 1:
                    prev = n
                else:
                    rows.append((path, c, start, prev))
                    start = prev = n
            if start is not None:
                rows.append((path, c, start, prev))
    rows.sort(key=lambda r: (r[0], r[2], r[1]))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["Path", "Commit", "StartLine", "EndLine"])
    w.writerows(rows)
    buf.write("#END\n")
    open(a.out, "w", encoding="utf-8", newline="").write(buf.getvalue())


if __name__ == "__main__":
    main()
