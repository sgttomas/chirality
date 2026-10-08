"""I100: the mutant table from the junit reports. A kill counts only for a failing test whose failure is an
assertion: an AssertionError, or pytest.raises' own "DID NOT RAISE". Any other exception is an error, not a kill.
Usage: mutant_table.py <MUTANTS.json> <runs dir> <out.json>"""
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

mutants = {m["id"]: m for m in json.load(open(sys.argv[1]))}
runs = Path(sys.argv[2])
rows = []
for d in sorted(runs.iterdir()):
    root = ET.parse(d / "junit.xml").getroot()
    total, fails = 0, []
    for case in root.iter("testcase"):
        total += 1
        for child in case:
            if child.tag in ("failure", "error"):
                msg = (child.get("message") or "").strip()
                kind = "assertion" if child.tag == "failure" and (msg.startswith("AssertionError") or msg.startswith("assert ") or msg.startswith("Failed: DID NOT RAISE")) else "error"
                fails.append({"test": f'{case.get("classname").rsplit(".", 1)[-1]}::{case.get("name")}', "kind": kind, "message": msg[:160]})
    killed = any(f["kind"] == "assertion" for f in fails)
    rows.append({"id": d.name, "edit": mutants.get(d.name, {}).get("edit", "control" if d.name == "NONE" else "the head's tests on I4's reader"),
                 "tests": total, "failed": len(fails), "killed_by_assertion": killed, "errors": [f for f in fails if f["kind"] == "error"], "failures": fails})
json.dump(rows, open(sys.argv[3], "w"), indent=1)
for r in rows:
    print(r["id"], r["tests"], "failed", r["failed"], "killed" if r["killed_by_assertion"] else "NOT KILLED", "errors", len(r["errors"]), [f["test"] for f in r["failures"]][:6])
