"""RV120: the PY mutant table from each run's junit report: failed tests, and whether each failure is an assertion
(AssertionError, or pytest.raises' "DID NOT RAISE"). Usage: python3 mutant_table_py.py <runs dir> <manifest.json>... <out.json>"""
import json
import os
import sys
import xml.etree.ElementTree as ET

runs, *rest = sys.argv[1:]
out = rest[-1]
manifest = []
for m in rest[:-1]:
    manifest += json.load(open(m))
rows = []
for m in [{"id": "NONE", "item": "control", "description": "RV113_MUT unset"}] + manifest:
    p = os.path.join(runs, m["id"], "pytest.xml")
    if not os.path.exists(p):
        continue
    row = dict(m)
    root = ET.parse(p).getroot()
    tot = fail = 0
    failed = []
    for tc in root.iter("testcase"):
        tot += 1
        for child in tc:
            if child.tag in ("failure", "error"):
                fail += 1
                msg = (child.get("message") or "")[:140]
                text = (child.text or "")
                kind = "assertion" if ("AssertionError" in text or "DID NOT RAISE" in text or msg.startswith("assert")) else "other"
                failed.append({"test": f'{tc.get("classname")}::{tc.get("name")}', "kind": kind, "message": msg})
    row.update({"tests_run": tot, "failed": fail, "failed_tests": failed,
                "result": "control" if m["id"] == "NONE" else ("killed (assertion)" if any(f["kind"] == "assertion" for f in failed) else ("failed, no assertion" if failed else "survives"))})
    rows.append(row)
json.dump(rows, open(out, "w"), indent=1)
for r in rows:
    print(r["id"], r["result"], r["tests_run"], r["failed"], "|", "; ".join(f'{f["test"].split("::")[-1][:60]} ({f["kind"]})' for f in r["failed_tests"][:4]))
