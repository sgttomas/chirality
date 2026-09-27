#!/usr/bin/env python3
"""Show that the K4 verifier's single containment FAIL on the combined tree is exactly K1.

Usage: python3 check_k4_extras.py <pre_root> <post_root> <proposal.md>
Lists every file under projects/ that differs between the two trees, splits it into
the proposal's K4 paths, K1 MODIFY paths, K1 CREATE paths and anything else, and
exits 0 only when changed-existing = K4 (129) + K1 MODIFY (20), added = K1 CREATE (12),
removed = 0 and other = 0.
"""
import os, re, sys
pre, post, prop = sys.argv[1:4]
EX = "projects/pec/execution/"
k4, k1m, k1c, sec = set(), set(), set(), None
for line in open(prop, encoding="utf-8"):
    if line.startswith("### Part K4"): sec = "k4"
    elif line.startswith("### Part K1"): sec = "k1"
    elif line.startswith("### ") or line.startswith("## "): sec = None
    if sec and line.startswith("| ") and "`PKG-" in line:
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        p = EX + c[1].strip("`")
        (k4 if sec == "k4" else (k1m if c[0] == "MODIFY" else k1c)).add(p)
def walk(r):
    out = {}
    for d, _, fs in os.walk(os.path.join(r, "projects")):
        for f in fs:
            p = os.path.join(d, f); out[os.path.relpath(p, r)] = p
    return out
A, B = walk(pre), walk(post)
changed = {k for k in A if k in B and open(A[k], "rb").read() != open(B[k], "rb").read()}
added, removed = set(B) - set(A), set(A) - set(B)
extra = changed - k4
print(f"changed existing files: {len(changed)}; of which K4 paths {len(changed & k4)}; K1 MODIFY {len(changed & k1m)}; other {len(changed - k4 - k1m)}")
print(f"K4 verifier 'extra' (changed minus K4): {len(extra)}; equals K1 MODIFY set: {extra == k1m}")
for p in sorted(extra): print("  EXTRA", p)
print(f"added files: {len(added)}; equals K1 CREATE set: {added == k1c}")
print(f"removed files: {len(removed)}")
ok = changed == (k4 | k1m) and added == k1c and not removed
print("RESULT", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
