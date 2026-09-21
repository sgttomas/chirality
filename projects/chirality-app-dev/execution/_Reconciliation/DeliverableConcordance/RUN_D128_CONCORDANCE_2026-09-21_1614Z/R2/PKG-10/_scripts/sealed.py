#!/usr/bin/env python3
"""List units whose forward pass looks sealed: claims ends #END, notes present, validator PASS, claims unchanged >= 90 s.
Usage: sealed.py [unit ...]  (default: all DEL-* folders). Prints 'unit STATUS sha'."""
import glob, hashlib, os, subprocess, sys, time
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); RUN = os.path.dirname(os.path.dirname(P)); APP = os.path.abspath(os.path.join(RUN, "../../../.."))
us = sys.argv[1:] or [os.path.basename(d) for d in sorted(glob.glob(os.path.join(P, "DEL-*")))]
for u in us:
    d = u.split("_")[0]; c = os.path.join(P, u, d + "_claims.csv"); n = os.path.join(P, u, d + "_notes.md")
    if not os.path.exists(c): print(u, "NONE"); continue
    t = open(c, encoding="utf-8", errors="replace").read().rstrip()
    if not t.endswith("#END"): print(u, "PARTIAL"); continue
    if not os.path.exists(n): print(u, "NO_NOTES"); continue
    if time.time() - os.path.getmtime(c) < 90: print(u, "FRESH"); continue
    r = subprocess.run(["python3", os.path.join(RUN, "_scripts", "validate_ledger.py"), "ledger", c], cwd=APP, capture_output=True, text=True).stdout.strip().splitlines()
    print(u, "SEALED" if r and "PASS" in r[-1] else "FAIL:" + (r[-1] if r else "?"), hashlib.sha256(open(c, "rb").read()).hexdigest())
