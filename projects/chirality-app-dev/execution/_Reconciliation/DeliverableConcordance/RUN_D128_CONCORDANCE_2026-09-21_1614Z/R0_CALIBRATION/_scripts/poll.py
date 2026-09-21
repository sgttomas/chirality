#!/usr/bin/env python3
"""Report file-state of each R0 unit: exists, #END, validator result, sha256, notes present."""
import os, subprocess, hashlib, sys, json
H = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.dirname(H); RUN = os.path.dirname(R0)
APP = os.path.abspath(os.path.join(RUN, "..", "..", "..", ".."))
V = os.path.join(RUN, "_scripts", "validate_ledger.py"); IDX = os.path.join(RUN, "R1_INVENTORY", "CLAIM_INDEX.csv")
CAP = os.path.join(R0, "SURFACES", "HARNESS_capabilities.csv")
units = {"F-01": "DEL-01-01", "F-02": "DEL-02-05", "F-03A": "DEL-03-01_A", "F-03B": "DEL-03-01_B", "F-04": "DEL-04-05",
         "F-06": "DEL-06-04", "F-08": "DEL-08-04", "F-09": "DEL-09-07", "F-10": "DEL-10-01"}
def st(path, mode, extra):
    if not os.path.exists(path): return None
    end = open(path, encoding="utf-8").read().rstrip("\n").split("\n")[-1].strip() == "#END"
    r = subprocess.run(["python3", V, mode] + extra + [path], cwd=APP, capture_output=True, text=True)
    res = [l for l in r.stdout.splitlines() if l.startswith("RESULT")]
    return {"end": end, "val": res[0] if res else r.stdout[-200:], "sha": hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]}
out = {}
c = st(CAP, "capabilities", []); out["S-H"] = c
for u, f in units.items():
    d = f[:9]
    out[u] = {"fwd": st(os.path.join(R0, f, d + "_claims.csv"), "ledger", ["--index", IDX]),
              "notes": os.path.exists(os.path.join(R0, f, d + "_notes.md")),
              "rev": st(os.path.join(R0, f, d + "_reverse.csv"), "reverse", ["--capabilities", CAP]) if os.path.exists(CAP) else None}
for k, v in out.items(): print(k, json.dumps(v))
