#!/usr/bin/env python3
"""File-state of each PKG-04 unit: #END, validator RESULT, sha256 prefix. No judgment."""
import os, subprocess, hashlib, json, glob, sys
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H); RUN = os.path.dirname(os.path.dirname(P))
APP = os.path.abspath(os.path.join(RUN, "..", "..", "..")); V = os.path.join(RUN, "_scripts", "validate_ledger.py")
def st(path, mode, extra):
    if not os.path.exists(path): return None
    end = open(path, encoding="utf-8").read().rstrip("\n").split("\n")[-1].strip() == "#END"
    r = subprocess.run(["python3", V, mode] + extra + [path], cwd=APP, capture_output=True, text=True)
    res = [l for l in r.stdout.splitlines() if l.startswith("RESULT") or l.startswith("RULES")]
    return {"end": end, "val": " ".join(res), "sha": hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]}
units = sys.argv[1:] or ["DEL-04-01", "DEL-04-02", "DEL-04-03", "DEL-04-04", "DEL-04-05"]
for u in units:
    d = os.path.join(P, u); b = u[:9]
    cap = os.path.join(P, "_reverse_inputs", u + "_capabilities.csv")
    o = {"pregather": os.path.exists(os.path.join(d, "PREGATHER.md")),
         "fwd": st(os.path.join(d, b + "_claims.csv"), "ledger", []),
         "notes": os.path.exists(os.path.join(d, b + "_notes.md")),
         "rev": st(os.path.join(d, b + "_reverse.csv"), "reverse", ["--capabilities", cap]) if os.path.exists(cap) else None,
         "errata": st(os.path.join(d, b + "_errata.csv"), "errata", []),
         "revnotes": os.path.exists(os.path.join(d, b + "_reverse_notes.md"))}
    print(u, json.dumps(o))
