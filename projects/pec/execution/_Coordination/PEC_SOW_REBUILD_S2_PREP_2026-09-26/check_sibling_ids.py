#!/usr/bin/env python3
"""Cross-candidate ID check for the S2 (provisional D-PEC-100) candidates.

Every qualified citation `DEL-XX-YY/PFX-NNN` in one candidate that names ANOTHER
S2 deliverable must resolve to an ID defined in that sibling's candidate (a
definition is `**PFX-NNN**` at a list item or table cell start). A candidate's
qualified citation of its OWN ID (a retired ID, or its ID as another record
quotes it) is listed as INFO with whether it is still defined; it is not a
failure. Read-only; stdlib only.
Usage: check_sibling_ids.py <prep dir>
"""
import re, sys
from pathlib import Path
prep = Path(sys.argv[1])
S2 = ["DEL-01-01", "DEL-01-06", "DEL-02-03", "DEL-02-04", "DEL-02-05", "DEL-02-06", "DEL-02-07"]
text, defs = {}, {}
for d in S2:
    f = sorted(prep.glob(f"candidates/projects/pec/execution/PKG-*/1_Working/{d}_*/ScopeOfWork.md"))[0]
    text[d] = f.read_text(encoding="utf-8")
    defs[d] = set(re.findall(r"(?m)^(?:\s*[-|]\s*|\|\s*)\*\*([A-Z]{2,4}-\d{3})\*\*", text[d]))
bad = n = 0
for d in S2:
    for m in sorted(set(re.findall(r"(DEL-\d\d-\d\d)/([A-Z]{2,4}-\d{3})", text[d]))):
        tgt, i = m
        if tgt not in S2: continue
        if tgt == d:
            print(f"INFO {d} cites its own {i} ({'defined' if i in defs[d] else 'not defined: retired'})")
            continue
        n += 1
        if True:
            ok = i in defs[tgt]; kind = "sibling"
        if not ok: bad += 1
        print(("PASS " if ok else "FAIL ") + f"{d} cites {tgt}/{i} [{kind}]")
print(f"RESULT {'PASS' if not bad else 'FAIL'} {n-bad}/{n}")
sys.exit(1 if bad else 0)
