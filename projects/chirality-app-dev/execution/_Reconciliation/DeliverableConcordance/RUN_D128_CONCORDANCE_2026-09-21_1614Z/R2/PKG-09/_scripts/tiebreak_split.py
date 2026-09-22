#!/usr/bin/env python3
"""PKG-09 DEL-09-02 double-blind: Addendum 5 tie-break and Addendum 6 / R4-Qn measures. Appends §9-§10 to
../DOUBLE_BLIND_DEL-09-02.md (run double_blind.py first). Same comparison unit as double_blind.py §1 (value set per
indexed base key). Baselines DEL-06-02 (19/35, wave 1, before Addendum 5) and DEL-05-02 (24/33, wave 2) are the
figures given by HELP_HUMAN at dispatch; their ledgers are not re-read."""
import csv, io, os, re, collections
H = os.path.dirname(os.path.abspath(__file__)); PKG = os.path.dirname(H)
SS, RSM = "STALE_SPECIFICATION", "REMAINING_STATE_MISMATCH"
LOCAL = re.compile(r"#(REGISTER|STATE)-\d+$"); QN = re.compile(r"R4(?:-Q[1-5])?")
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip()
    t = t[:-6] if t.endswith('"#END"') else (t[:-4] if t.endswith("#END") else t)
    return list(csv.DictReader(io.StringIO(t)))
def base(k): return re.sub(r"\.\d+$", "", k)
def grp(rs):
    g = collections.OrderedDict()
    for r in rs: g.setdefault(base(r["ClaimKey"]), []).append(r)
    return g
def sets(g, k, f="Disposition"): return frozenset(r[f] for r in g[k])
def qn(g, k): return frozenset(t for r in g[k] for t in QN.findall(r["HumanDecisionNeeded"]))
ga = grp(rows(os.path.join(PKG, "DEL-09-02_A", "DEL-09-02_claims.csv"))); gb = grp(rows(os.path.join(PKG, "DEL-09-02_B", "DEL-09-02_claims.csv")))
common = sorted(k for k in set(ga) & set(gb) if not LOCAL.search(k))
agree = [k for k in common if sets(ga, k) == sets(gb, k)]
cls = collections.OrderedDict((("SS_vs_RSM", []), ("SS_or_RSM_other", []), ("other", [])))
for k in common:
    a, b = sets(ga, k), sets(gb, k)
    if a == b: continue
    d = a ^ b
    if d <= {SS, RSM} and SS in d and RSM in d: cls["SS_vs_RSM"].append(k)
    elif (a | b) & {SS, RSM}: cls["SS_or_RSM_other"].append(k)
    else: cls["other"].append(k)
touch = [k for k in common if (sets(ga, k) | sets(gb, k)) & {SS, RSM}]
touch_agree = [k for k in touch if sets(ga, k) == sets(gb, k)]
rowc = lambda g, v: sum(1 for k in g for r in g[k] if r["Disposition"] == v)
def pct(a, b): return f"{a}/{b} ({100*a/max(b,1):.0f}%)"
hdn = [k for k in common if sets(ga, k, "HumanDecisionNeeded") == sets(gb, k, "HumanDecisionNeeded")]
r4 = [k for k in common if qn(ga, k) or qn(gb, k)]
r4a = [k for k in r4 if qn(ga, k) == qn(gb, k)]
q1a = sorted(k for k in common if "R4-Q1" in qn(ga, k)); q1b = sorted(k for k in common if "R4-Q1" in qn(gb, k))
q1both = sorted(set(q1a) & set(q1b))
coarse = sum(bool(qn(ga, k)) == bool(qn(gb, k)) for k in common)
out = ["", "## 9. Disposition agreement, STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH splits, and HumanDecisionNeeded (R4-Qn)", "",
       "> Script-derived by `R2/PKG-09/_scripts/tiebreak_split.py`. Both workers received the Addendum 5 tie-break, the Addendum 6 subject test, the HELP_HUMAN rule-3 clarification and the R4-Q4/R4-Q5 vocabulary verbatim in the same brief, before dispatch (STATE.jsonl). Baselines are the figures given at dispatch. Agent measurement, not a ruling.", "",
       "| Measure | DEL-09-02 (wave 5) | DEL-05-02 (wave 2) | DEL-06-02 (wave 1, pre-tie-break) |", "|---|---|---|---|",
       f"| Disposition exact agreement, indexed base keys | {pct(len(agree), len(common))} | 24/33 | 19/35 |",
       f"| Disagreements that are pure SS vs RSM splits | {len(cls['SS_vs_RSM'])} | – | – |",
       f"| Disagreements involving SS or RSM plus another verdict | {len(cls['SS_or_RSM_other'])} | – | – |",
       f"| Other disagreements | {len(cls['other'])} | – | – |",
       f"| Agreement on keys where either worker used SS or RSM | {pct(len(touch_agree), len(touch))} | – | – |",
       f"| Rows STALE_SPECIFICATION (A / B) | {rowc(ga, SS)} / {rowc(gb, SS)} | – | – |",
       f"| Rows REMAINING_STATE_MISMATCH (A / B) | {rowc(ga, RSM)} / {rowc(gb, RSM)} | – | – |",
       f"| HumanDecisionNeeded exact agreement (value set) | {pct(len(hdn), len(common))} | – | – |",
       f"| R4/R4-Qn token-set agreement on keys where either cites R4 | {pct(len(r4a), len(r4))} | – | – |",
       f"| Cites any R4 token vs none (coarse) | {pct(coarse, len(common))} | – | – |",
       f"| Base keys citing R4-Q1 (A / B / both) | {len(q1a)} / {len(q1b)} / {len(q1both)} | – | – |", ""]
for c, ks in cls.items():
    out.append(f"- {c}: " + (", ".join(f"{k.split('#')[1]} (A {'/'.join(sorted(sets(ga, k)))}; B {'/'.join(sorted(sets(gb, k)))})" for k in ks) or "none"))
out.append("- R4 token disagreements: " + (", ".join(f"{k.split('#')[1]} (A {'/'.join(sorted(qn(ga, k))) or 'none'}; B {'/'.join(sorted(qn(gb, k))) or 'none'})" for k in r4 if k not in r4a) or "none"))
p = os.path.join(PKG, "DOUBLE_BLIND_DEL-09-02.md")
t = open(p).read().split("\n## 9. ")[0].rstrip("\n") + "\n"
open(p, "w").write(t + "\n".join(out) + "\n")
print("\n".join(out))
