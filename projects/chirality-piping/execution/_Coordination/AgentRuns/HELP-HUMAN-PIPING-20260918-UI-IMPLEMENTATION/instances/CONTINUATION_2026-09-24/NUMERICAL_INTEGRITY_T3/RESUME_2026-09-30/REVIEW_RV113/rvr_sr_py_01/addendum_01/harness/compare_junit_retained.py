"""RV113 (RV-R): the two retained test files, test by test, between two pytest junit reports (plain or .gz).
Usage: compare_junit_retained.py <before.xml[.gz]> <after.xml[.gz]> <out.json>"""
import gzip
import json
import sys
import xml.etree.ElementTree as ET

FILES = ("tests.test_retained_precision_contract", "tests.test_retained_precision_carriers")


def outcomes(path):
    data = (gzip.open if path.endswith(".gz") else open)(path, "rb").read()
    out = {}
    for tc in ET.fromstring(data).iter("testcase"):
        if tc.get("classname") not in FILES:
            continue
        key = f'{tc.get("classname")}::{tc.get("name")}'
        kind = "passed"
        for child in tc:
            if child.tag in ("failure", "error", "skipped"):
                kind = child.tag
        assert key not in out, key
        out[key] = kind
    return out


a, b = outcomes(sys.argv[1]), outcomes(sys.argv[2])
tally = lambda r: {k: sum(1 for v in r.values() if v == k) for k in sorted(set(r.values()))}
res = {"before": tally(a), "after": tally(b),
       "added": sorted([k, b[k]] for k in set(b) - set(a)), "removed": sorted([k, a[k]] for k in set(a) - set(b)),
       "changed": sorted([k, a[k], b[k]] for k in set(a) & set(b) if a[k] != b[k])}
json.dump(res, open(sys.argv[3], "w"), indent=1)
print(json.dumps({k: (v if isinstance(v, dict) else len(v)) for k, v in res.items()}))
for k in res["added"]: print("  +", k)
for k in res["removed"] + res["changed"]: print("  !", k)
