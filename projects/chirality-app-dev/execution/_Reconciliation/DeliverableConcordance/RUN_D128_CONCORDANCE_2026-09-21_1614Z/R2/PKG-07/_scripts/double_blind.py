#!/usr/bin/env python3
"""Deterministic F-07-02A vs F-07-02B comparison for DEL-07-02. Writes ../DOUBLE_BLIND_DEL-07-02.md.
Run from anywhere: python3 double_blind.py"""
import csv, hashlib, os, re, collections
H = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.dirname(H)
A = os.path.join(R0, "DEL-07-02_A"); B = os.path.join(R0, "DEL-07-02_B")
FIELDS = ["ClaimType", "Disposition", "AuthorityTier", "CauseTag"]

def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n").split("\n")
    if t and t[-1].strip() == "#END": t = t[:-1]
    return list(csv.DictReader(t))

def base(k): return re.sub(r"\.\d+$", "", k)
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

def group(rs):
    g = collections.OrderedDict()
    for r in rs: g.setdefault(base(r["ClaimKey"]), []).append(r)
    return g

def vals(lst, f): return tuple(sorted(set(r[f] for r in lst)))

out = []
fa, fb = os.path.join(A, "DEL-07-02_claims.csv"), os.path.join(B, "DEL-07-02_claims.csv")
ra, rb = rows(fa), rows(fb)
ga, gb = group(ra), group(rb)
keys = sorted(set(ga) | set(gb))
LOCAL = re.compile(r"#(REGISTER|STATE)-\d+$")
runlocal = sorted(k for k in keys if LOCAL.search(k))
common = [k for k in keys if k in ga and k in gb and not LOCAL.search(k)]
out.append("# DOUBLE_BLIND_COMPARISON — DEL-07-02 (F-07-02A vs F-07-02B)\n")
out.append("> Script-derived by `R2/PKG-07/_scripts/double_blind.py` (R0 script adapted by path only). Agent measurement, not a ruling.\n")
out.append(f"- A ledger: `DEL-07-02_A/DEL-07-02_claims.csv` sha256 `{sha(fa)}`; rows {len(ra)}; base keys {len(ga)}")
out.append(f"- B ledger: `DEL-07-02_B/DEL-07-02_claims.csv` sha256 `{sha(fb)}`; rows {len(rb)}; base keys {len(gb)}")
out.append(f"- Base keys in both: {len(common)}; only A: {sorted(set(ga)-set(gb))}; only B: {sorted(set(gb)-set(ga))}\n")
out.append(f"- Indexed base keys compared: {len(common)}. Run-local keys (REGISTER-n/STATE-n) are numbered independently by each worker, so they are excluded from agreement and listed in §6.")
out.append("Comparison unit: the base key (`.n` split suffix removed). Two readings agree on a field when the *set* of values across that base key's rows is identical; a secondary 'overlap' measure counts keys whose value sets intersect.\n")
out.append("## 1. Field agreement on base keys\n")
out.append("| Field | Exact agreement | Overlap agreement | Keys compared |\n|---|---|---|---|")
dis = {}
for f in FIELDS:
    ex = sum(vals(ga[k], f) == vals(gb[k], f) for k in common)
    ov = sum(bool(set(vals(ga[k], f)) & set(vals(gb[k], f))) for k in common)
    n = len(common) or 1
    out.append(f"| {f} | {ex}/{len(common)} ({100*ex/n:.0f}%) | {ov}/{len(common)} ({100*ov/n:.0f}%) | {len(common)} |")
    dis[f] = [k for k in common if vals(ga[k], f) != vals(gb[k], f)]
# Confidence secondary
exc = sum(vals(ga[k], "Confidence") == vals(gb[k], "Confidence") for k in common)
out.append(f"| Confidence (secondary) | {exc}/{len(common)} | – | {len(common)} |")
out.append("\n## 2. Split rate\n")
def split(g): 
    s = sum(1 for k, v in g.items() if len(v) > 1 or any(re.search(r"\.\d+$", r["ClaimKey"]) for r in v))
    return s, len(g)
sa, na = split(ga); sb, nb = split(gb)
out.append(f"- A: {sa}/{na} base keys split ({100*sa/max(na,1):.1f}%); rows/base key {len(ra)/max(na,1):.2f}")
out.append(f"- B: {sb}/{nb} base keys split ({100*sb/max(nb,1):.1f}%); rows/base key {len(rb)/max(nb,1):.2f}")
out.append(f"- Split-rate difference: {abs(100*sa/max(na,1)-100*sb/max(nb,1)):.1f} percentage points")
both = [k for k in common if (len(ga[k])>1) and (len(gb[k])>1)]
out.append(f"- Keys split by both: {len(both)}; only A: {sorted(k for k in common if len(ga[k])>1 and len(gb[k])<=1)}; only B: {sorted(k for k in common if len(gb[k])>1 and len(ga[k])<=1)}")
out.append("\n## 3. Histograms\n")
for f in ["Disposition", "CauseTag", "ClaimType", "AuthorityTier", "Confidence"]:
    ca = collections.Counter(r[f] for r in ra); cb = collections.Counter(r[f] for r in rb)
    out.append(f"**{f}** (rows) — A: {dict(sorted(ca.items()))}; B: {dict(sorted(cb.items()))}\n")
out.append("## 4. Reverse Response agreement\n")
pa, pb = os.path.join(A, "DEL-07-02_reverse.csv"), os.path.join(B, "DEL-07-02_reverse.csv")
if os.path.exists(pa) and os.path.exists(pb):
    xa = {r["CapabilityID"]: r for r in rows(pa)}; xb = {r["CapabilityID"]: r for r in rows(pb)}
    cc = sorted(set(xa) & set(xb))
    resp = [c for c in cc if xa[c]["Response"] == xb[c]["Response"]]
    own = [c for c in resp if xa[c]["Response"] != "NOT_MINE" and base(xa[c]["ClaimKey"]) == base(xb[c]["ClaimKey"])]
    claimed = [c for c in resp if xa[c]["Response"] != "NOT_MINE"]
    coarse = [c for c in cc if (xa[c]["Response"] == "NOT_MINE") == (xb[c]["Response"] == "NOT_MINE")]
    out.append(f"- A sha256 `{sha(pa)}`; B sha256 `{sha(pb)}`")
    out.append(f"- Capabilities answered by both: {len(cc)}")
    out.append(f"- Exact Response agreement: {len(resp)}/{len(cc)} ({100*len(resp)/max(len(cc),1):.0f}%)")
    out.append(f"- Coarse agreement (mine vs NOT_MINE): {len(coarse)}/{len(cc)} ({100*len(coarse)/max(len(cc),1):.0f}%)")
    out.append(f"- Same claiming base key where both CLAIMED_BY/PARTIAL agree: {len(own)}/{len(claimed)}")
    out.append(f"- Response histogram A: {dict(collections.Counter(r['Response'] for r in xa.values()))}; B: {dict(collections.Counter(r['Response'] for r in xb.values()))}")
    rdis = [c for c in cc if xa[c]["Response"] != xb[c]["Response"] or (xa[c]["Response"] != "NOT_MINE" and base(xa[c]["ClaimKey"]) != base(xb[c]["ClaimKey"]))]
else:
    out.append("- Reverse files not both present; not compared."); rdis = []; xa = xb = {}
out.append("\n## 5. Every disagreement, both readings\n")
out.append("### 5.1 Forward fields\n")
out.append("| Base key | Field | A reading | B reading |\n|---|---|---|---|")
for k in common:
    for f in FIELDS:
        if k in dis[f]:
            out.append(f"| {k} | {f} | {' / '.join(vals(ga[k], f))} | {' / '.join(vals(gb[k], f))} |")
for k in sorted((set(ga) ^ set(gb)) - set(runlocal)):
    out.append(f"| {k} | presence | {'present' if k in ga else 'absent'} | {'present' if k in gb else 'absent'} |")
out.append("\n### 5.2 Reverse responses\n")
out.append("| CapabilityID | A | B |\n|---|---|---|")
for c in rdis:
    out.append(f"| {c} | {xa[c]['Response']} {xa[c]['ClaimKey']} | {xb[c]['Response']} {xb[c]['ClaimKey']} |")
out.append("\n## 6. Run-local rows (not key-comparable)\n")
out.append("| Worker | Key | ClaimType | Disposition | CauseTag | DeclaredState (first 90 chars) |\n|---|---|---|---|---|---|")
for lab, g in (("A", ga), ("B", gb)):
    for k in runlocal:
        for r in g.get(k, []):
            out.append(f"| {lab} | {r['ClaimKey']} | {r['ClaimType']} | {r['Disposition']} | {r['CauseTag']} | {r['DeclaredState'][:90].replace('|','/')} |")
out.append("\n## 7. Row-level agreement where both split a key identically\n")
same = [k for k in common if sorted(r["ClaimKey"] for r in ga[k]) == sorted(r["ClaimKey"] for r in gb[k]) and len(ga[k]) > 1]
tot = sum(len(ga[k]) for k in same)
for f in FIELDS:
    ag = sum(1 for k in same for ra_, rb_ in zip(sorted(ga[k], key=lambda r: r["ClaimKey"]), sorted(gb[k], key=lambda r: r["ClaimKey"])) if ra_[f] == rb_[f])
    out.append(f"- {f}: {ag}/{tot} sub-rows agree across {len(same)} identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)")
single = [k for k in common if len(ga[k]) == 1 and len(gb[k]) == 1]
out.append("\n## 8. Strict agreement on keys neither worker split\n")
out.append(f"Keys unsplit by both: {len(single)}.\n")
out.append("| Field | Agreement |\n|---|---|")
for f in FIELDS:
    ag = sum(ga[k][0][f] == gb[k][0][f] for k in single)
    out.append(f"| {f} | {ag}/{len(single)} ({100*ag/max(len(single),1):.0f}%) |")
ag = sum((ga[k][0]["Disposition"] == "ALIGNED") == (gb[k][0]["Disposition"] == "ALIGNED") for k in single)
out.append(f"| ALIGNED vs non-ALIGNED | {ag}/{len(single)} |")
open(os.path.join(R0, "DOUBLE_BLIND_DEL-07-02.md"), "w").write("\n".join(out) + "\n")
print("\n".join(out[:25]))
