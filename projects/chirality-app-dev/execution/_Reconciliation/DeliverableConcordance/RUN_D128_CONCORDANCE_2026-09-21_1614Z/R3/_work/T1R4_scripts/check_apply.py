#!/usr/bin/env python3
"""T1 (R4 step 1): checks after applying the owner-check answers. Prints one line per check."""
import os, sys, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
from r3lib import *
from dump_rows import oc_rows
PRE = os.path.join(RUN, "R4", "_work", "pre_owner_check")
listed = {k for _, _, k in oc_rows()}
dec = read_csv(os.path.join(WORK, "DEC_OWNERCHECK.csv"))[1]
fields = collections.defaultdict(set)
for d in dec:
    fields[d["ClaimKey"]].add("Notes" if d["Field"] == "Notes+" else d["Field"])
# 1 prefix
old = open(os.path.join(PRE, "REMAP_LOG.csv"), "rb").read()
assert old.endswith(b"#END\n")
new = open(os.path.join(R3, "REMAP_LOG.csv"), "rb").read()
pre = old[:-len(b"#END\n")]
print("C1 REMAP_LOG prefix byte-identical:", "PASS" if new.startswith(pre) else "FAIL", len(pre), "bytes")
# 2 appended lines all OWNER_CHECK
ol = read_csv(os.path.join(PRE, "REMAP_LOG.csv"))[1]
nl = read_csv(os.path.join(R3, "REMAP_LOG.csv"))[1]
app = nl[len(ol):]
print("C2 appended lines all Source OWNER_CHECK:", "PASS" if nl[:len(ol)] == ol and app and all(l["Source"] == "OWNER_CHECK" for l in app) else "FAIL", len(app), "lines")
# 3 concordance diffs
bad = []
changed = collections.Counter()
for f in ("CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"):
    h0, a = read_csv(os.path.join(PRE, f)); h1, b = read_csv(os.path.join(R3, f))
    if h0 != h1 or [r["ClaimKey"] for r in a] != [r["ClaimKey"] for r in b]:
        bad.append(f + " header/keys"); continue
    for x, y in zip(a, b):
        diff = {c for c in h0 if x[c] != y[c]}
        if not diff: continue
        changed[f] += 1
        k = x["ClaimKey"]
        if k not in listed or not diff <= fields[k] | {"RemapSources"}:
            bad.append((k, sorted(diff)))
print("C3 concordance diffs only in listed rows/decided fields:", "PASS" if not bad else "FAIL", dict(changed), bad[:5])
print("C4 REVERSE_CONCORDANCE byte-identical:", "PASS" if open(os.path.join(PRE, "REVERSE_CONCORDANCE.csv"), "rb").read() == open(os.path.join(R3, "REVERSE_CONCORDANCE.csv"), "rb").read() else "FAIL")
print("listed rows", len(listed), "rows changed", sum(changed.values()))
