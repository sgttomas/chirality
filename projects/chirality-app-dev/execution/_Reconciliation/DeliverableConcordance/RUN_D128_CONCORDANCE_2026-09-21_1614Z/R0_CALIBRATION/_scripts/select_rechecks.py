#!/usr/bin/env python3
"""Deterministic verifier selection per the manager brief (V (a)-(d)). Writes _verify/SELECTION.csv."""
import csv, os, glob, hashlib, math, re
H = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.dirname(H)
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n").split("\n")
    if t and t[-1].strip() == "#END": t = t[:-1]
    return list(csv.DictReader(t))
def h(s): return hashlib.sha256(s.encode()).hexdigest()
def pick(keys, pct):
    keys = sorted(keys); n = math.ceil(len(keys) * pct)
    sel = [k for k in keys if h(k)[-1] in "012"]
    if len(sel) < n: sel += [k for k in keys if k not in sel][: n - len(sel)]
    return sorted(sel), n
out = []
for f in sorted(glob.glob(os.path.join(R0, "DEL-*", "*_claims.csv"))):
    u = os.path.basename(os.path.dirname(f)); rs = rows(f)
    rn = os.path.join(os.path.dirname(f), os.path.basename(f).replace("_claims.csv", "_reverse_notes.md"))
    flagged = set(re.findall(r"(?:DEL-\d\d-\d\d#)?((?:CLM|SEC|REM|REMTXT|REGISTER|STATE)-\d+(?:\.\d+)?)", open(rn).read())) if os.path.exists(rn) else set()
    al = []
    for r in rs:
        loc = r["ClaimKey"].split("#")[1]
        why = []
        if r["Disposition"] != "ALIGNED": why.append("a:non-ALIGNED")
        if r["Confidence"] == "LOW": why.append("a:LOW")
        if "LEAST-CONFIDENT" in r["Notes"] or "SELF-FLAG" in r["Notes"].upper(): why.append("a:self-flag")
        if loc in flagged: why.append("a:reverse-notes")
        if why: out.append((u, "a", r["ClaimKey"], "", ";".join(why)))
        elif r["Disposition"] == "ALIGNED": al.append(r["ClaimKey"])
    # (b) sample over ALL ALIGNED rows of the unit, excluding ones already in (a)
    allal = [r["ClaimKey"] for r in rs if r["Disposition"] == "ALIGNED"]
    sel, n = pick(allal, 0.15)
    for k in sel:
        if k in al: out.append((u, "b", k, "", f"b:15% of {len(allal)} ALIGNED (n={n})"))
    rv = os.path.join(os.path.dirname(f), os.path.basename(f).replace("_claims.csv", "_reverse.csv"))
    if os.path.exists(rv):
        cl = {r["CapabilityID"] + r["ClaimKey"]: r for r in rows(rv) if r["Response"] in ("CLAIMED_BY", "PARTIAL")}
        sel, n = pick(list(cl), 0.20)
        for k in sel: out.append((u, "c", cl[k]["ClaimKey"], cl[k]["CapabilityID"], f"c:{cl[k]['Response']} 20% of {len(cl)} (n={n})"))
caps = [r["CapabilityID"] for r in rows(os.path.join(R0, "SURFACES", "HARNESS_capabilities.csv"))]
sel = sorted([c for c in caps if h(c)[-1] in "012"])[:10]
sel += [c for c in sorted(caps) if c not in sel][: 10 - len(sel)]
for c in sorted(sel): out.append(("SURFACES", "d", "", c, "d:capability accuracy/granularity"))
os.makedirs(os.path.join(R0, "_verify"), exist_ok=True)
with open(os.path.join(R0, "_verify", "SELECTION.csv"), "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["Unit", "Class", "ClaimKey", "CapabilityID", "Reason"]); w.writerows(out)
import collections
c = collections.Counter((o[0], o[1]) for o in out)
for k in sorted(c): print(k, c[k])
print("TOTAL", len(out))
