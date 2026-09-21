#!/usr/bin/env python3
"""Deterministic verifier selection for PKG-07 (brief step 7; CONVENTIONS §10), R0 method.
Units: the ledgers of record (DEL-07-02_A for the double-blind DEL-07-02; B is compared, not verified).
Classes: a = LOW, self-flagged (LEAST-CONFIDENT / SELF-FLAG), AUTHORITY_CONFLICT, UNKNOWN, REMAINING_WORK rows;
a30 = 30% of the other non-ALIGNED rows; b = 15% of ALIGNED rows; c = 20% of CLAIMED_BY/PARTIAL responses;
e = every errata row. Sampling: keys sorted, those whose sha256 ends in 0/1/2 first, topped up in key order
(R0 select_rechecks.py pick()). Shards <= 50 items. Writes _verify/SELECTION.csv."""
import csv, glob, hashlib, io, math, os, collections
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNITS = __import__("sys").argv[1:] or ["DEL-07-01", "DEL-07-02_A", "DEL-07-03", "DEL-07-04", "DEL-07-05", "DEL-07-06"]
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip()
    if t.endswith("#END"): t = t[:-4]
    return list(csv.DictReader(io.StringIO(t)))
def h(s): return hashlib.sha256(s.encode()).hexdigest()
def pick(keys, pct):
    keys = sorted(keys); n = math.ceil(len(keys) * pct)
    sel = [k for k in keys if h(k)[-1] in "012"]
    if len(sel) < n: sel += [k for k in keys if k not in sel][: n - len(sel)]
    return sorted(sel), n
out = []
for u in UNITS:
    d = u.split("_")[0]; f = os.path.join(P, u, d + "_claims.csv")
    if not os.path.exists(f): continue
    rs = rows(f); items = []; rest = []
    for r in rs:
        why = []
        if r["Confidence"] == "LOW": why.append("LOW")
        if "LEAST-CONFIDENT" in r["Notes"] or "SELF-FLAG" in r["Notes"].upper(): why.append("self-flag")
        if r["Disposition"] in ("AUTHORITY_CONFLICT", "UNKNOWN"): why.append(r["Disposition"])
        if r["ClaimType"] == "REMAINING_WORK": why.append("REMAINING_WORK")
        if why: items.append((u, "a", r["ClaimKey"], "", "", "a:" + ";".join(why)))
        elif r["Disposition"] != "ALIGNED": rest.append(r["ClaimKey"])
    sel, n = pick(rest, 0.30)
    items += [(u, "a30", k, "", "", f"a30:30% of {len(rest)} other non-ALIGNED (n={n})") for k in sel]
    al = [r["ClaimKey"] for r in rs if r["Disposition"] == "ALIGNED"]
    aa = {i[2] for i in items}
    sel, n = pick([k for k in al if k not in aa], 0.15)
    items += [(u, "b", k, "", "", f"b:15% of {len(al)} ALIGNED (n={n})") for k in sel]
    rv = os.path.join(P, u, d + "_reverse.csv")
    if os.path.exists(rv):
        cl = {r["CapabilityID"] + "|" + r["ClaimKey"]: r for r in rows(rv) if r["Response"] in ("CLAIMED_BY", "PARTIAL")}
        sel, n = pick(list(cl), 0.20)
        items += [(u, "c", cl[k]["ClaimKey"], cl[k]["CapabilityID"], "", f"c:{cl[k]['Response']} 20% of {len(cl)} (n={n})") for k in sel]
    er = os.path.join(P, u, d + "_errata.csv")
    if os.path.exists(er):
        items += [(u, "e", r["ClaimKey"], "", r["Field"], "e:errata") for r in rows(er)]
    out += items
by = collections.OrderedDict()
for o in out: by.setdefault(o[0], []).append(o)
final = []
for u, its in by.items():
    k = math.ceil(len(its) / 50); size = math.ceil(len(its) / k)
    for i, o in enumerate(its):
        final.append((f"V-{u}" + (f"-{i // size + 1}" if k > 1 else ""),) + o)
os.makedirs(os.path.join(P, "_verify"), exist_ok=True)
with open(os.path.join(P, "_verify", "SELECTION.csv"), "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["Shard", "Unit", "Class", "ClaimKey", "CapabilityID", "ErrataField", "Reason"]); w.writerows(final)
c = collections.Counter((o[0], o[2]) for o in final)
for k in sorted(c): print(k, c[k])
print("SHARDS", sorted(set(o[0] for o in final))); print("TOTAL", len(final))
