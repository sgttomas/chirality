#!/usr/bin/env python3
"""Report file state of EXT worker folders: RETURN.md present, per-ledger #END, validator result.
Usage: poll.py [FOLDER ...]   (default: all worker folders). Exit 0 if all named folders are DONE."""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extlib import EXT, RUN, sha

STEMS = {"DEC": ["DEC"], "DOC_REL": ["DOC-BUILDREL", "DOC-RQGATES", "DOC-RQRUN"],
         "DOC_VAL": ["DOC-VALSTRAT", "DOC-RELIANCE"], "SOW_A": ["SOW"], "SOW_B": ["SOW"],
         "DOC_DEV": ["DOC-PRODAGENTS", "DOC-ADDING_A_TOOL", "DOC-README",
                     "DOC-RUNTIME_ENGINE_CONTRACT", "DOC-TOOL_CATALOG", "DOC-TRACEABILITY"]}
VAL = os.path.join(RUN, "_scripts", "validate_ledger.py")
folders = sys.argv[1:] or list(STEMS)
alldone = True
for f in folders:
    d = os.path.join(EXT, f); ret = os.path.exists(os.path.join(d, "RETURN.md"))
    parts = []
    for s in STEMS[f]:
        p = os.path.join(d, f"{s}_claims.csv")
        if not os.path.exists(p): parts.append(f"{s}:-"); continue
        end = open(p, encoding="utf-8").read().rstrip().endswith("#END")
        res = "?"
        if ret and end:
            args = ["python3", VAL, "ledger"]
            if f.startswith("SOW_"):
                args += ["--extension-index", os.path.join(EXT, "_inputs", f"EXTENSION_INDEX_SOW_{f[-1]}.csv")]
            r = subprocess.run(args + [p], capture_output=True, text=True)
            res = [l for l in r.stdout.splitlines() if l.startswith("RESULT")][-1:] or ["?"]
            res = res[0].replace("RESULT ", "")
        parts.append(f"{s}:{'END' if end else 'noEND'}:{res}:{sha(p)[:12]}")
    ok = ret and all("PASS" in x for x in parts)
    alldone &= ok
    print(f"{f:8} {'DONE' if ok else ('RET' if ret else '...')}  " + "  ".join(parts))
sys.exit(0 if alldone else 1)
