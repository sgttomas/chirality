#!/usr/bin/env python3
"""Check working-tree bytes of the D-PEC-101 grant against the ruled proposal tables.

Usage (from the repository root):
  python3 check_hashes.py <proposal.md> pre      # K4 and K1 preimages (K1 CREATE targets absent)
  python3 check_hashes.py <proposal.md> k1-post  # K1 postimages ({D} = 2026-09-26 column)
  python3 check_hashes.py <proposal.md> k4c-post # K4 postimages, A+C column where given, else A
Also prints the proposal's aggregate conventions (bytewise-sorted projects/pec/... paths;
SHA-256 over concatenated bytes; path list = SHA-256 of each path followed by LF).
Exit 0 when every path matches; 1 otherwise.
"""
import hashlib, os, re, sys
prop, mode = sys.argv[1], sys.argv[2]
EX = "projects/pec/execution/"
H = re.compile(r"`([0-9a-f]{64})`")
k4, k1 = [], []
section = None
for line in open(prop, encoding="utf-8"):
    if line.startswith("### Part K4"): section = "k4"
    elif line.startswith("### Part K1"): section = "k1"
    elif line.startswith("### ") or line.startswith("## "): section = None
    if section and line.startswith("| ") and "`PKG-" in line:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        path = cells[1].strip("`")
        hs = [H.search(c).group(1) if H.search(c) else None for c in cells[2:]]
        (k4 if section == "k4" else k1).append((cells[0], path, hs))
assert len(k4) == 129 and len(k1) == 32, (len(k4), len(k1))
def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.isfile(p) else "absent"
rows = []
if mode == "pre":
    rows = [(EX + p, hs[0]) for _, p, hs in k4] + [(EX + p, hs[0] or "absent") for _, p, hs in k1]
elif mode == "k1-post":
    rows = [(EX + p, hs[1]) for _, p, hs in k1]
elif mode == "k4c-post":
    rows = [(EX + p, hs[2] or hs[1]) for _, p, hs in k4]
else:
    sys.exit("unknown mode")
bad = 0
for p, want in rows:
    got = sha(p)
    ok = got == want
    bad += not ok
    print(f"{'OK' if ok else 'MISMATCH'}\t{p}\t{want}\t{got}")
def agg(paths):
    paths = sorted(paths, key=lambda s: s.encode())
    pl = hashlib.sha256("".join(p + "\n" for p in paths).encode()).hexdigest()
    h = hashlib.sha256()
    for p in paths:
        if os.path.isfile(p): h.update(open(p, "rb").read())
    return len(paths), pl, h.hexdigest()
n, pl, a = agg([p for p, _ in rows])
print(f"AGGREGATE\t{mode}\tfiles={n}\tpathlist_sha256={pl}\tbytes_sha256={a}")
if mode == "k1-post":
    for label, sel in (("modified_K1", "MODIFY"), ("created_K1", "CREATE")):
        print("AGGREGATE\t%s\tfiles=%d\tpathlist_sha256=%s\tbytes_sha256=%s" % ((label,) + agg([EX + p for a_, p, _ in k1 if a_ == sel])))
if mode == "pre":
    print("AGGREGATE\tpre_K4\tfiles=%d\tpathlist_sha256=%s\tbytes_sha256=%s" % agg([EX + p for _, p, _ in k4]))
    print("AGGREGATE\tpre_modified_K1\tfiles=%d\tpathlist_sha256=%s\tbytes_sha256=%s" % agg([EX + p for a_, p, _ in k1 if a_ == "MODIFY"]))
print(f"SUMMARY\t{mode}\t{len(rows) - bad}/{len(rows)} OK")
sys.exit(1 if bad else 0)
