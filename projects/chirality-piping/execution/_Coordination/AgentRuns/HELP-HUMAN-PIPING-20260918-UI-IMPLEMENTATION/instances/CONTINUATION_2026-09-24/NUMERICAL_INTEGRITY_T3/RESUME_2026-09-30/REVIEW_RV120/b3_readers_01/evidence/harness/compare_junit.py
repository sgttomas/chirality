"""RV120: two pytest junit reports, test by test (classname::name -> passed/failed/error/skipped).
Usage: python3 compare_junit.py <i4.xml> <head.xml> <out.json>"""
import json
import sys
import xml.etree.ElementTree as ET


def tests(path):
    out = {}
    for tc in ET.parse(path).getroot().iter("testcase"):
        k = f'{tc.get("classname")}::{tc.get("name")}'
        st = "passed"
        for child in tc:
            if child.tag in ("failure", "error", "skipped"):
                st = child.tag
        out[k] = st
    return out


a, b = tests(sys.argv[1]), tests(sys.argv[2])
tally = lambda r: {s: sum(1 for v in r.values() if v == s) for s in sorted(set(r.values()))}
diff = [{"test": k, "i4": a.get(k), "head": b.get(k)} for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)]
json.dump({"i4": tally(a), "head": tally(b), "differences": diff}, open(sys.argv[3], "w"), indent=1)
print(json.dumps({"i4": tally(a), "head": tally(b), "differences": len(diff)}))
for x in diff:
    print("  ", json.dumps(x))
