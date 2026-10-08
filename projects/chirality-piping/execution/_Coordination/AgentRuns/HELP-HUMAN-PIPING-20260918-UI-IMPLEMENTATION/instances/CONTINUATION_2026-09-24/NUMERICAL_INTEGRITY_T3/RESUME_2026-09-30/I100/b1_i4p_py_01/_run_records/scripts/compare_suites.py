"""I100: two pytest junit reports, test by test. Usage: compare_suites.py <base.xml> <head.xml> <out.json>
A test is (classname, name); its outcome is passed, failed, error or skipped."""
import json
import sys
import xml.etree.ElementTree as ET


def outcomes(path):
    out = {}
    for case in ET.parse(path).getroot().iter("testcase"):
        key = f'{case.get("classname")}::{case.get("name")}'
        kind = "passed"
        for child in case:
            if child.tag in ("failure", "error", "skipped"):
                kind = {"failure": "failed"}.get(child.tag, child.tag)
        assert key not in out, key
        out[key] = kind
    return out


def tally(o):
    t = {}
    for v in o.values():
        t[v] = t.get(v, 0) + 1
    return t


a, b = outcomes(sys.argv[1]), outcomes(sys.argv[2])
res = {"base": tally(a), "head": tally(b), "added": sorted(k for k in b if k not in a), "removed": sorted(k for k in a if k not in b),
       "changed": sorted({"test": k, "base": a[k], "head": b[k]} for k in a if k in b and a[k] != b[k]) if False else [{"test": k, "base": a[k], "head": b[k]} for k in sorted(a) if k in b and a[k] != b[k]],
       "added_outcomes": {k: b[k] for k in sorted(b) if k not in a}}
json.dump(res, open(sys.argv[3], "w"), indent=1)
print(json.dumps({"base": res["base"], "head": res["head"], "added": len(res["added"]), "removed": len(res["removed"]), "changed": len(res["changed"]),
                  "added_list": res["added_outcomes"]}, indent=1))
