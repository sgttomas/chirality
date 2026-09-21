#!/usr/bin/env python3
"""Step 7 deterministic verifier selection for PKG-00 (R0 select_rechecks.py method, adapted).
Class a: LOW, self-flagged (LEAST-CONFIDENT/SELF-FLAG), AUTHORITY_CONFLICT, UNKNOWN, REMAINING_WORK,
         rows flagged in reverse_notes.
Class n: 30% of the other non-ALIGNED rows.   Class b: 15% of ALIGNED rows (not already in a).
Class c: 20% of CLAIMED_BY/PARTIAL reverse responses.   Class e: every errata row (ClaimKey+Field).
pick(): keys sorted; those whose sha256 hex ends in 0/1/2 first, topped up in key order to ceil(n*pct).
Writes <PKG>/_verify/SELECTION.csv. Usage: select.py DEL-00-01 [DEL-00-02 ...]"""
import csv, io, os, re, sys, hashlib, math, collections
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n")
    recs = [r for r in csv.reader(io.StringIO(t)) if r and r != ["#END"]]
    return [dict(zip(recs[0], r)) for r in recs[1:]]
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
def pick(keys, pct):
    keys = sorted(keys); n = math.ceil(len(keys) * pct)
    sel = [k for k in keys if h(k)[-1] in "012"]
    if len(sel) < n: sel += [k for k in keys if k not in sel][: n - len(sel)]
    return sorted(sel), n
out = []
for u in sys.argv[1:]:
    D = os.path.join(PKG, u); rs = rows(os.path.join(D, f"{u}_claims.csv"))
    rn = os.path.join(D, f"{u}_reverse_notes.md")
    flagged = set(re.findall(r"DEL-\d\d-\d\d#((?:CLM|SEC|REM|REMTXT|REGISTER|STATE)-\d+(?:\.\d+)?)", open(rn).read())) if os.path.exists(rn) else set()
    a_keys = set(); other_na = []; al = []
    for r in rs:
        loc = r["ClaimKey"].split("#")[1]; why = []
        if r["Confidence"] == "LOW": why.append("LOW")
        if "LEAST-CONFIDENT" in r["Notes"] or "SELF-FLAG" in r["Notes"].upper(): why.append("self-flag")
        if r["Disposition"] in ("AUTHORITY_CONFLICT", "UNKNOWN"): why.append(r["Disposition"])
        if r["ClaimType"] == "REMAINING_WORK": why.append("REMAINING_WORK")
        if loc in flagged: why.append("reverse-notes")
        if why: out.append((u, "a", r["ClaimKey"], "", "", "a:" + ";".join(why))); a_keys.add(r["ClaimKey"])
        elif r["Disposition"] == "ALIGNED": al.append(r["ClaimKey"])
        else: other_na.append(r["ClaimKey"])
    sel, n = pick(other_na, 0.30)
    out += [(u, "n", k, "", "", f"n:30% of {len(other_na)} other non-ALIGNED (n={n})") for k in sel]
    sel, n = pick(al, 0.15)
    out += [(u, "b", k, "", "", f"b:15% of {len(al)} ALIGNED not in a (n={n})") for k in sel]
    rv = os.path.join(D, f"{u}_reverse.csv")
    if os.path.exists(rv):
        cl = {r["CapabilityID"] + "|" + r["ClaimKey"]: r for r in rows(rv) if r["Response"] in ("CLAIMED_BY", "PARTIAL")}
        sel, n = pick(list(cl), 0.20)
        out += [(u, "c", cl[k]["ClaimKey"], cl[k]["CapabilityID"], "Response", f"c:{cl[k]['Response']} 20% of {len(cl)} (n={n})") for k in sel]
    er = os.path.join(D, f"{u}_errata.csv")
    if os.path.exists(er):
        out += [(u, "e", r["ClaimKey"], "", r["Field"], "e:errata row") for r in rows(er)]
os.makedirs(os.path.join(PKG, "_verify"), exist_ok=True)
with open(os.path.join(PKG, "_verify", "SELECTION.csv"), "w", newline="") as fh:
    w = csv.writer(fh, lineterminator="\n"); w.writerow(["Unit", "Class", "ClaimKey", "CapabilityID", "ErrataField", "Reason"]); w.writerows(out); fh.write("#END\n")
c = collections.Counter((o[0], o[1]) for o in out)
for k in sorted(c): print(k, c[k])
print("TOTAL", len(out))
