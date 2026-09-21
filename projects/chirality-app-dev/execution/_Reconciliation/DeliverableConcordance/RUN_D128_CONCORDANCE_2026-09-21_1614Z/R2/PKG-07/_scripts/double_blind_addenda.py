#!/usr/bin/env python3
"""Append §9 (Addenda 5 and 6 effects) to DOUBLE_BLIND_DEL-07-02.md. Run after double_blind.py.
Measures on indexed base keys (value sets per base key, as in double_blind.py):
 - Disposition agreement overall (exact and overlap);
 - STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH splits (Addendum 5 tie-break);
 - HumanDecisionNeeded agreement overall, and R4-Q1 presence agreement (Addendum 6 subject test);
 - REACH tags per worker on the R4-Q1 split keys."""
import csv, os, re, collections
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H)
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip()
    t = t[:-4] if t.endswith("#END") else t
    import io; return list(csv.DictReader(io.StringIO(t)))
def base(k): return re.sub(r"\.\d+$", "", k)
def group(rs):
    g = collections.OrderedDict()
    for r in rs: g.setdefault(base(r["ClaimKey"]), []).append(r)
    return g
ra = rows(os.path.join(P, "DEL-07-02_A", "DEL-07-02_claims.csv")); rb = rows(os.path.join(P, "DEL-07-02_B", "DEL-07-02_claims.csv"))
ga, gb = group(ra), group(rb)
LOCAL = re.compile(r"#(REGISTER|STATE)-\d+$")
common = [k for k in ga if k in gb and not LOCAL.search(k)]
def vs(g, k, f): return set(r[f] for r in g[k])
def reach(g, k): return sorted(set(t for r in g[k] for t in re.findall(r"REACH=(\w+)", r["ImplementationEvidence"]))) or ["no-code"]
n = len(common)
ex = [k for k in common if vs(ga, k, "Disposition") == vs(gb, k, "Disposition")]
ov = [k for k in common if vs(ga, k, "Disposition") & vs(gb, k, "Disposition")]
SR = {"STALE_SPECIFICATION", "REMAINING_STATE_MISMATCH"}
srk = [k for k in common if vs(ga, k, "Disposition") != vs(gb, k, "Disposition") and ((vs(ga, k, "Disposition") | vs(gb, k, "Disposition")) & SR)]
srpure = [k for k in srk if (vs(ga, k, "Disposition") - vs(gb, k, "Disposition")) <= SR and (vs(gb, k, "Disposition") - vs(ga, k, "Disposition")) <= SR and (vs(ga, k, "Disposition") ^ vs(gb, k, "Disposition")) <= SR and len((vs(ga, k, "Disposition") | vs(gb, k, "Disposition")) & SR) == 2]
bothSR = [k for k in common if ((vs(ga, k, "Disposition") | vs(gb, k, "Disposition")) & SR)]
hx = [k for k in common if vs(ga, k, "HumanDecisionNeeded") == vs(gb, k, "HumanDecisionNeeded")]
def q1(g, k): return any("R4-Q1" in r["HumanDecisionNeeded"] for r in g[k])
q1a = [k for k in common if q1(ga, k)]; q1b = [k for k in common if q1(gb, k)]
q1agree = [k for k in common if q1(ga, k) == q1(gb, k)]
rowq1 = lambda rs: sum("R4-Q1" in r["HumanDecisionNeeded"] for r in rs)
alsom = lambda rs: sum("ALSO_MODULE:" in r["Notes"] for r in rs)
also = lambda rs: sum("ALSO:" in r["Notes"] for r in rs)
o = ["", "## 9. Addenda 5 and 6 effects (manager supplement, `_scripts/double_blind_addenda.py`)", "",
     "Both workers received the Addendum 5 tie-break and the Addendum 6 subject test verbatim and identically (`BRIEFS/WORKER_BRIEF.md`).", "",
     "| Measure | Result |", "|---|---|",
     f"| Disposition, exact (value sets per base key) | {len(ex)}/{n} ({100*len(ex)/n:.0f}%) |",
     f"| Disposition, overlap | {len(ov)}/{n} ({100*len(ov)/n:.0f}%) |",
     f"| Keys where either worker used STALE_SPECIFICATION or REMAINING_STATE_MISMATCH | {len(bothSR)} |",
     f"| …of which the workers disagree on Disposition | {len(srk)} |",
     f"| …of which the disagreement is purely STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH | {len(srpure)} ({', '.join(srpure) or 'none'}) |",
     f"| HumanDecisionNeeded, exact | {len(hx)}/{n} ({100*len(hx)/n:.0f}%) |",
     f"| R4-Q1 presence (either row of the base key cites it), agreement | {len(q1agree)}/{n} ({100*len(q1agree)/n:.0f}%) |",
     f"| Base keys citing R4-Q1: A / B / both | {len(q1a)} / {len(q1b)} / {len(set(q1a)&set(q1b))} |",
     f"| Rows citing R4-Q1: A / B | {rowq1(ra)} / {rowq1(rb)} |",
     f"| Rows with `ALSO_MODULE:` in Notes: A / B | {alsom(ra)} / {alsom(rb)} |",
     f"| Rows with `ALSO:` in Notes: A / B | {also(ra)} / {also(rb)} |", "",
     "### 9.1 Disposition disagreements with STALE_SPECIFICATION / REMAINING_STATE_MISMATCH", "",
     "| Base key | A | B |", "|---|---|---|"]
o += [f"| {k} | {' / '.join(sorted(vs(ga,k,'Disposition')))} | {' / '.join(sorted(vs(gb,k,'Disposition')))} |" for k in srk] or ["| none | | |"]
o += ["", "### 9.2 R4-Q1 splits, with each worker's REACH tags", "", "| Base key | A HDN | A REACH | B HDN | B REACH |", "|---|---|---|---|---|"]
for k in common:
    if q1(ga, k) != q1(gb, k):
        o.append(f"| {k} | {' / '.join(sorted(vs(ga,k,'HumanDecisionNeeded')))} | {','.join(reach(ga,k))} | {' / '.join(sorted(vs(gb,k,'HumanDecisionNeeded')))} | {','.join(reach(gb,k))} |")
ra_t = collections.Counter(t for r in ra for t in re.findall(r"REACH=(\w+)", r["ImplementationEvidence"]))
rb_t = collections.Counter(t for r in rb for t in re.findall(r"REACH=(\w+)", r["ImplementationEvidence"]))
o += ["", f"REACH tag counts (all rows): A {dict(ra_t)}; B {dict(rb_t)}.", ""]
f = os.path.join(P, "DOUBLE_BLIND_DEL-07-02.md")
t = open(f).read().split("\n## 9. Addenda")[0].rstrip("\n")
rd = os.path.join(H, "double_blind_reading.md")
if os.path.exists(rd): o += [open(rd).read().rstrip(), ""]
open(f, "w").write(t + "\n" + "\n".join(o) + "\n")
print("\n".join(o))
