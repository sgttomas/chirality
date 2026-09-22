#!/usr/bin/env python3
"""Check a reverse file: every CLAIMED_BY/PARTIAL ClaimKey is a row of the sealed ledger; no duplicate CapabilityID;
print Response counts. Usage: revkeys.py <unit>"""
import csv, io, os, sys, collections
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); u = sys.argv[1]; d = u.split("_")[0]
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip(); t = t[:-4] if t.endswith("#END") else t
    return list(csv.DictReader(io.StringIO(t)))
led = {r["ClaimKey"] for r in rows(os.path.join(P, u, d + "_claims.csv"))}
rv = rows(os.path.join(P, u, d + "_reverse.csv"))
bad = [r["CapabilityID"] + ":" + r["ClaimKey"] for r in rv if r["Response"] != "NOT_MINE" and r["ClaimKey"] not in led]
dup = [k for k, n in collections.Counter(r["CapabilityID"] for r in rv).items() if n > 1]
print(u, dict(collections.Counter(r["Response"] for r in rv)), "rows", len(rv), "badkeys", bad, "dups", dup)
