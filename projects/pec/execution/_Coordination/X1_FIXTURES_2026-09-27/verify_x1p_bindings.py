#!/usr/bin/env python3
"""Check that every REQ/AC/VER/CON/TBD binding in the X1 fixture candidates names an ID
defined in the named contract at <commit> (a line starting '- **<ID>** ').
Usage: verify_x1p_bindings.py <repo> <commit> <candidates dir>"""
import json, re, subprocess, sys, ast
from pathlib import Path
repo, commit, cand = sys.argv[1], sys.argv[2], Path(sys.argv[3])
W = "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/"
FOLDERS = {"DEL-02-03": "DEL-02-03_Receipts_ledger_parser_per_loop_grammars",
           "DEL-02-08": "DEL-02-08_Work_graph_parser", "DEL-02-09": "DEL-02-09_MEMORY_run_index_parser"}
defined = {}
for d, f in FOLDERS.items():
    text = subprocess.run(["git", "-C", repo, "show", f"{commit}:{W}{f}/ScopeOfWork.md"], capture_output=True, check=True).stdout.decode()
    defined[d] = set(re.findall(r"^- \*\*((?:REQ|AC|VER|CON|TBD|OUT|CLM|AX)-\d{3})\*\* ", text, re.M))
F = cand / "projects/pec/v2/tests/parsers"
binds = []
for p in sorted((F / "fixtures").rglob("*.json")):
    def walk(o, where):
        if isinstance(o, dict):
            if "binds" in o: binds.extend((f"{p.relative_to(F)}:{o.get('id')}", b) for b in o["binds"])
            for v in o.values(): walk(v, where)
        elif isinstance(o, list):
            for v in o: walk(v, where)
    walk(json.loads(p.read_text()), p)
tree = ast.parse((F / "test_parser_fixture_integrity.py").read_text())
for node in ast.walk(tree):
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "TEST_TO_VERIFICATION":
        for k, v in zip(node.value.keys, node.value.values):
            binds.extend((f"TEST_TO_VERIFICATION:{k.value.rsplit('.',1)[-1]}", e.value) for e in v.elts)
bad = [(w, b) for w, b in binds if b.split("/")[1] not in defined[b.split("/")[0]]]
for w, b in bad: print(f"FAIL {w}: {b} is not defined in the contract at {commit}")
print(f"defined IDs: " + ", ".join(f"{d}={len(s)}" for d, s in defined.items()))
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(binds)-len(bad)}/{len(binds)}")
sys.exit(1 if bad else 0)
