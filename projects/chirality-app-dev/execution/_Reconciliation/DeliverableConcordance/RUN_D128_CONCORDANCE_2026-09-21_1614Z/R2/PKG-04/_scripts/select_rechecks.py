#!/usr/bin/env python3
"""Deterministic verifier selection for PKG-04 (brief step 7; CONVENTIONS §10). Writes _verify/SELECTION.csv.
Class a  : every LOW, self-flagged (LEAST-CONFIDENT/SELF-FLAG), AUTHORITY_CONFLICT, UNKNOWN and REMAINING_WORK row.
Class n  : 30% of the other non-ALIGNED rows.
Class b  : 15% of ALIGNED rows (not already selected).
Class c  : 20% of CLAIMED_BY/PARTIAL reverse responses.
Class e  : every errata row.
Sampling as in R0: sorted keys whose sha256(key) ends in 0/1/2 first, topped up in key order to ceil(pct*N)."""
import csv, io, os, glob, hashlib, math, collections
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H)
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n")
    body = t[: t.rfind("\n#END")] if t.endswith("#END") else t
    return list(csv.DictReader(io.StringIO(body)))
def h(s): return hashlib.sha256(s.encode()).hexdigest()
def pick(keys, pct):
    keys = sorted(keys); n = math.ceil(len(keys) * pct)
    sel = [k for k in keys if h(k)[-1] in "012"][:n]
    if len(sel) < n: sel += [k for k in keys if k not in sel][: n - len(sel)]
    return sorted(sel), n
out = []
for f in sorted(glob.glob(os.path.join(P, "DEL-*", "*_claims.csv"))):
    u = os.path.basename(os.path.dirname(f)); rs = rows(f); a = set(); other = []
    for r in rs:
        why = []
        if r["Confidence"] == "LOW": why.append("LOW")
        if "LEAST-CONFIDENT" in r["Notes"] or "SELF-FLAG" in r["Notes"].upper(): why.append("self-flag")
        if r["Disposition"] == "AUTHORITY_CONFLICT": why.append("AUTHORITY_CONFLICT")
        if r["Disposition"] == "UNKNOWN": why.append("UNKNOWN")
        if r["ClaimType"] == "REMAINING_WORK": why.append("REMAINING_WORK")
        if why: out.append((u, "a", r["ClaimKey"], "", "", ";".join(why))); a.add(r["ClaimKey"])
        elif r["Disposition"] != "ALIGNED": other.append(r["ClaimKey"])
    sel, n = pick(other, 0.30)
    out += [(u, "n", k, "", "", f"30% of {len(other)} other non-ALIGNED (n={n})") for k in sel]
    al = [r["ClaimKey"] for r in rs if r["Disposition"] == "ALIGNED" and r["ClaimKey"] not in a]
    sel, n = pick(al, 0.15)
    out += [(u, "b", k, "", "", f"15% of {len(al)} ALIGNED (n={n})") for k in sel]
    rv = f.replace("_claims.csv", "_reverse.csv")
    if os.path.exists(rv):
        cl = {r["CapabilityID"] + "|" + r["ClaimKey"]: r for r in rows(rv) if r["Response"] in ("CLAIMED_BY", "PARTIAL")}
        sel, n = pick(list(cl), 0.20)
        out += [(u, "c", cl[k]["ClaimKey"], cl[k]["CapabilityID"], "", f"{cl[k]['Response']} 20% of {len(cl)} (n={n})") for k in sel]
    er = f.replace("_claims.csv", "_errata.csv")
    if os.path.exists(er):
        out += [(u, "e", r["ClaimKey"], "", r["Field"], "errata row") for r in rows(er)]
os.makedirs(os.path.join(P, "_verify"), exist_ok=True)
with open(os.path.join(P, "_verify", "SELECTION.csv"), "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["Unit", "Class", "ClaimKey", "CapabilityID", "ErrataField", "Reason"]); w.writerows(out)
c = collections.Counter((o[0], o[1]) for o in out)
for k in sorted(c): print(k, c[k])
print("TOTAL", len(out))
