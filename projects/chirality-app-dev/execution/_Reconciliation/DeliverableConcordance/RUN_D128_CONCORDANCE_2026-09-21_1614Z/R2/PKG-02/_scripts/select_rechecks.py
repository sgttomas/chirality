#!/usr/bin/env python3
"""Deterministic verifier selection for PKG-02 (manager brief step 7; CONVENTIONS §10).
Class a: every LOW, self-flagged (LEAST-CONFIDENT / SELF-FLAG), AUTHORITY_CONFLICT, UNKNOWN,
REMAINING_WORK row, and every row with an errata entry (errata rows are listed individually, class e).
Class a30: 30% of the other non-ALIGNED rows. Class b: 15% of ALIGNED rows not already selected.
Class c: 20% of CLAIMED_BY/PARTIAL reverse responses. Sampling uses sha256(key) as in R0
(keys whose digest ends in 0,1,2 first, then sorted order to reach ceil(n*pct)).
Usage: select_rechecks.py [DEL-ID ...]. Writes shards of <= 50 items (_verify/SHARD-<DEL>-<n>.csv) per\ndeliverable; with no argument, all deliverables plus _verify/SELECTION.csv (the union)."""
import csv, glob, hashlib, io, math, os, collections
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def dicts(p):
    r = list(csv.reader(io.StringIO(open(p, encoding="utf-8", newline="").read())))
    if r and r[-1] == ["#END"]: r = r[:-1]
    return [dict(zip(r[0], x)) for x in r[1:]]
def h(s): return hashlib.sha256(s.encode()).hexdigest()
def pick(keys, pct):
    keys = sorted(set(keys)); n = math.ceil(len(keys) * pct)
    sel = [k for k in keys if h(k)[-1] in "012"][:n]
    if len(sel) < n: sel += [k for k in keys if k not in sel][: n - len(sel)]
    return sorted(sel), n
out = []
import sys
only = set(sys.argv[1:])
for d in sorted(glob.glob(os.path.join(PKG, "DEL-*"))):
    u = os.path.basename(d)
    if only and u not in only: continue
    led = os.path.join(d, f"{u}_claims.csv")
    if not os.path.exists(led): continue
    rs = dicts(led)
    er = os.path.join(d, f"{u}_errata.csv"); errs = dicts(er) if os.path.exists(er) else []
    errkeys = {e["ClaimKey"] for e in errs}
    other, al = [], []
    for r in rs:
        k = r["ClaimKey"]; why = []
        if r["Confidence"] == "LOW": why.append("LOW")
        n = r["Notes"]
        if "LEAST-CONFIDENT" in n or "SELF-FLAG" in n.upper(): why.append("self-flag")
        if r["Disposition"] in ("AUTHORITY_CONFLICT", "UNKNOWN"): why.append(r["Disposition"])
        if r["ClaimType"] == "REMAINING_WORK": why.append("REMAINING_WORK")
        if k in errkeys: why.append("errata")
        if why: out.append((u, "a", k, "", "", ";".join(why)))
        elif r["Disposition"] == "ALIGNED": al.append(k)
        else: other.append(k)
    sel, n = pick(other, 0.30)
    for k in sel: out.append((u, "a30", k, "", "", f"30% of {len(other)} other non-ALIGNED (n={n})"))
    sel, n = pick(al, 0.15)
    for k in sel: out.append((u, "b", k, "", "", f"15% of {len(al)} unselected ALIGNED (n={n})"))
    for e in errs: out.append((u, "e", e["ClaimKey"], "", e["Field"], "errata row"))
    rv = os.path.join(d, f"{u}_reverse.csv")
    if os.path.exists(rv):
        cl = {r["CapabilityID"] + "|" + r["ClaimKey"]: r for r in dicts(rv) if r["Response"] in ("CLAIMED_BY", "PARTIAL")}
        sel, n = pick(list(cl), 0.20)
        for k in sel: out.append((u, "c", cl[k]["ClaimKey"], cl[k]["CapabilityID"], "", f"{cl[k]['Response']} 20% of {len(cl)} (n={n})"))
vd = os.path.join(PKG, "_verify"); os.makedirs(vd, exist_ok=True)
H = ["Unit", "Class", "ClaimKey", "CapabilityID", "ErrataField", "Reason"]
def write(p, items):
    with open(p, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n"); w.writerow(H); w.writerows(items); fh.write("#END\n")
if not only: write(os.path.join(vd, "SELECTION.csv"), out)
# shards: per deliverable, chunks of <= 50
shards = []
for u in sorted({o[0] for o in out}):
    items = [o for o in out if o[0] == u]; k = math.ceil(len(items) / 50)
    size = math.ceil(len(items) / k)
    for i in range(k): shards.append((f"SHARD-{u}-{i+1}", items[i*size:(i+1)*size]))
for name, s in shards: write(os.path.join(vd, f"{name}.csv"), s)
c = collections.Counter((o[0], o[1]) for o in out)
for k in sorted(c): print(k, c[k])
print("TOTAL", len(out), "SHARDS", [(n, len(s)) for n, s in shards])
