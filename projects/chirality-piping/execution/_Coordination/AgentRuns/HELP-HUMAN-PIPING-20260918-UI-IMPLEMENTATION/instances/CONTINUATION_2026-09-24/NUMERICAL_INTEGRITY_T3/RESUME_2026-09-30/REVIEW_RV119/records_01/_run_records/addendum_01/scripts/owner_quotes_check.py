#!/usr/bin/env python3
"""RV119: every double-quoted owner phrase in WG's "Owner decisions in force" block occurs verbatim in RR at H
(inside the owner-decision sections), and the 2026-10-08 sections' owner quotes are reported.
Usage: owner_quotes_check.py <RR file> <WG file>"""
import re, sys
rr = open(sys.argv[1], encoding="utf-8").read(); wg = open(sys.argv[2], encoding="utf-8").read().split("\n")
s = next(i for i, l in enumerate(wg) if l.startswith("**Owner decisions in force**"))
e = next(i for i in range(s + 1, len(wg)) if wg[i].startswith("**Assignment IDs."))
q = re.compile(r"\(\"([^\"]+)\"|; \"([^\"]+)\"\)|\"([^\"]{12,})\"")
n = ok = 0
for i in range(s, e):
    for m in re.finditer(r"\"([^\"]+)\"", wg[i]):
        t = m.group(1); n += 1; hit = t in rr; ok += hit
        print(f"WG:{i+1}\t{'VERBATIM-IN-RR' if hit else 'NOT FOUND'}\t{t[:110]}")
print(f"quoted phrases {n}; verbatim in RR {ok}")
for h in ("## Owner decision: development jobs may use up to 64 GiB", "## Owner clarification: 64 GiB is T3's own allocation"):
    j = rr.index(h); seg = rr[j:j + 2500]
    m = re.search(r"\*\*The owner(?:'s direction)?, quoted:\*\* \"([^\"]+)\"", seg)
    print(f"{h[3:60]}...: owner quote = {len(m.group(1)) if m else 0} chars")
