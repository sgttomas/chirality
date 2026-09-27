#!/usr/bin/env python3
"""Cross-candidate ID check for the S4 (provisional D-PEC-102) candidates.

Every qualified citation `DEL-XX-YY/PFX-NNN` (or `` `DEL-XX-YY`/PFX-NNN ``) in one candidate that names ANOTHER
S4 deliverable must resolve to an ID defined in that sibling's candidate (a
definition is `**PFX-NNN**` at a list item or table cell start). A candidate's
qualified citation of its OWN ID (a retired ID, or its ID as another record
quotes it) is listed as INFO with whether it is still defined; it is not a
failure. With a second argument (an export root), every qualified citation of
an S4 ID in a ScopeOfWork.md OUTSIDE the S4 set is also checked against the
candidates ("external"): a cited ID must stay defined. Read-only; stdlib only.
Usage: check_sibling_ids.py <prep dir> [<export root>]
"""
import re, sys
from pathlib import Path
prep = Path(sys.argv[1])
S4 = ["DEL-04-01", "DEL-04-02", "DEL-08-01", "DEL-08-03", "DEL-08-04", "DEL-04-03", "DEL-03-04", "DEL-10-03"]
text, defs = {}, {}
for d in S4:
    f = sorted(prep.glob(f"candidates/projects/pec/execution/PKG-*/1_Working/{d}_*/ScopeOfWork.md"))[0]
    text[d] = f.read_text(encoding="utf-8")
    defs[d] = set(re.findall(r"(?m)^(?:\s*[-|]\s*|\|\s*)\*\*([A-Z]{2,4}-\d{3})\*\*", text[d]))
bad = n = 0
for d in S4:
    for m in sorted(set(re.findall(r"(DEL-\d\d-\d\d)`?/([A-Z]{2,4}-\d{3})", text[d]))):
        tgt, i = m
        if tgt not in S4: continue
        if tgt == d:
            print(f"INFO {d} cites its own {i} ({'defined' if i in defs[d] else 'not defined: retired'})")
            continue
        n += 1
        if True:
            ok = i in defs[tgt]; kind = "sibling"
        if not ok: bad += 1
        print(("PASS " if ok else "FAIL ") + f"{d} cites {tgt}/{i} [{kind}]")
if len(sys.argv) > 2:
    tree = Path(sys.argv[2])
    for f in sorted(tree.glob("projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md")):
        own = f.parent.name[:9]
        if own in S4: continue
        for tgt, i in sorted(set(re.findall(r"(DEL-\d\d-\d\d)`?/([A-Z]{2,4}-\d{3})", f.read_text(encoding="utf-8")))):
            if tgt not in S4: continue
            n += 1; ok = i in defs[tgt]
            if not ok: bad += 1
            print(("PASS " if ok else "FAIL ") + f"{own} cites {tgt}/{i} [external]")
print(f"RESULT {'PASS' if not bad else 'FAIL'} {n-bad}/{n}")
sys.exit(1 if bad else 0)
