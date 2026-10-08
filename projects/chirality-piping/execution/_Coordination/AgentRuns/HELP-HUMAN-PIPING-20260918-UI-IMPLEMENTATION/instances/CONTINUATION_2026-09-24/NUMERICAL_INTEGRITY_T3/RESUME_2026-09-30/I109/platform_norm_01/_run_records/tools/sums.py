#!/usr/bin/env python3
"""I109: write SHA256SUMS for a record folder (every file except SHA256SUMS, sorted, relative paths),
and refuse placeholder violations (absolute home, private or worktree-name paths) and symlinks.
Usage: sums.py <record folder>"""
import hashlib
import os
import re
import sys

root = sys.argv[1]
bad = re.compile(b"|".join([b"/Us" + b"ers/", b"/priv" + b"ate/", b"~" + b"/", b"chirality" + b"-t3", b"claude" + b"-worktrees"]))
lines, problems = [], []
for dp, dns, fns in os.walk(root):
    dns.sort()
    if "build" in dns:
        problems.append(f"folder named build under {os.path.relpath(dp, root)}")
    for fn in sorted(fns):
        p = os.path.join(dp, fn)
        rel = os.path.relpath(p, root)
        if rel == "SHA256SUMS":
            continue
        if os.path.islink(p):
            problems.append(f"symlink {rel}")
            continue
        data = open(p, "rb").read()
        if bad.search(data):
            problems.append(f"non-placeholder path in {rel}: {bad.search(data).group(0)!r}")
        lines.append(f"{hashlib.sha256(data).hexdigest()}  {rel}")
if problems:
    print("\n".join(problems))
    sys.exit(1)
open(os.path.join(root, "SHA256SUMS"), "w").write("\n".join(sorted(lines, key=lambda l: l.split("  ", 1)[1])) + "\n")
print(f"{len(lines)} files")
