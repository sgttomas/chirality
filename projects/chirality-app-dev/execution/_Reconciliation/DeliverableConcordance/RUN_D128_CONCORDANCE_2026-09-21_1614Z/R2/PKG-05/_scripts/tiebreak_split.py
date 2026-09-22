#!/usr/bin/env python3
"""Addendum 5 tie-break test for the DEL-05-02 double-blind (manager direction, wave 2).
Appends §9-§10 to ../DOUBLE_BLIND_DEL-05-02.md (run double_blind.py first).
Measures, on indexed base keys (same unit as double_blind.py §1: set of Disposition values per base key):
  - overall Disposition exact agreement;
  - disagreements classified: SS_vs_RSM (the two value sets differ only by STALE_SPECIFICATION <-> REMAINING_STATE_MISMATCH),
    SS_or_RSM_other (one side uses SS or RSM, the other differs by something else), other;
  - agreement restricted to keys where either worker used SS or RSM.
The same measures are computed read-only for PKG-06's DEL-06-02 double-blind (pre-Addendum-5 baseline, 19/35).
Also reports the R4-Q1 HumanDecisionNeeded comparison (Addendum 6 reached A before sealing and B after)."""
import csv, io, os, re, collections, hashlib
H = os.path.dirname(os.path.abspath(__file__)); PKG = os.path.dirname(H); R2 = os.path.dirname(PKG)
SS, RSM = "STALE_SPECIFICATION", "REMAINING_STATE_MISMATCH"
LOCAL = re.compile(r"#(REGISTER|STATE)-\d+$")
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
def measure(fa, fb):
    ga, gb = grp(rows(fa)), grp(rows(fb))
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
    return dict(ga=ga, gb=gb, common=common, agree=agree, cls=cls, touch=touch, touch_agree=touch_agree,
                hist={v: (rowc(ga, v), rowc(gb, v)) for v in (SS, RSM)})
def pct(a, b): return f"{a}/{b} ({100*a/max(b,1):.0f}%)"
m5 = measure(os.path.join(PKG, "DEL-05-02_A", "DEL-05-02_claims.csv"), os.path.join(PKG, "DEL-05-02_B", "DEL-05-02_claims.csv"))
m6 = measure(os.path.join(R2, "PKG-06", "DEL-06-02_A", "DEL-06-02_claims.csv"), os.path.join(R2, "PKG-06", "DEL-06-02_B", "DEL-06-02_claims.csv"))
out = ["", "## 9. Addendum 5 tie-break test (STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH)", "",
       "> Script-derived by `R2/PKG-05/_scripts/tiebreak_split.py`. Same comparison unit as §1 (Disposition value set per indexed base key). "
       "PKG-06 DEL-06-02 (pre-Addendum-5 baseline) is recomputed read-only from its two sealed ledgers. Agent measurement, not a ruling.", "",
       "| Measure | DEL-05-02 (wave 2, tie-break given to A and B verbatim before dispatch) | DEL-06-02 (wave 1, before the tie-break) |", "|---|---|---|",
       f"| Disposition exact agreement, indexed base keys | {pct(len(m5['agree']), len(m5['common']))} | {pct(len(m6['agree']), len(m6['common']))} |",
       f"| Disagreements that are pure SS vs RSM splits | {len(m5['cls']['SS_vs_RSM'])} | {len(m6['cls']['SS_vs_RSM'])} |",
       f"| Disagreements involving SS or RSM plus another verdict | {len(m5['cls']['SS_or_RSM_other'])} | {len(m6['cls']['SS_or_RSM_other'])} |",
       f"| Other disagreements | {len(m5['cls']['other'])} | {len(m6['cls']['other'])} |",
       f"| Agreement on keys where either worker used SS or RSM | {pct(len(m5['touch_agree']), len(m5['touch']))} | {pct(len(m6['touch_agree']), len(m6['touch']))} |",
       f"| Agreement if pure SS-vs-RSM splits were counted as agreement | {pct(len(m5['agree']) + len(m5['cls']['SS_vs_RSM']), len(m5['common']))} | {pct(len(m6['agree']) + len(m6['cls']['SS_vs_RSM']), len(m6['common']))} |",
       f"| Rows STALE_SPECIFICATION (A / B) | {m5['hist'][SS][0]} / {m5['hist'][SS][1]} | {m6['hist'][SS][0]} / {m6['hist'][SS][1]} |",
       f"| Rows REMAINING_STATE_MISMATCH (A / B) | {m5['hist'][RSM][0]} / {m5['hist'][RSM][1]} | {m6['hist'][RSM][0]} / {m6['hist'][RSM][1]} |", ""]
for lab, m in (("DEL-05-02", m5), ("DEL-06-02", m6)):
    for c, ks in m["cls"].items():
        out.append(f"- {lab} {c}: " + (", ".join(f"{k.split('#')[1]} (A {'/'.join(sorted(sets(m['ga'], k)))}; B {'/'.join(sorted(sets(m['gb'], k)))})" for k in ks) or "none"))
# Addendum 6
ga, gb = m5["ga"], m5["gb"]
def q1(g, k): return any("R4-Q1" in r["HumanDecisionNeeded"] for r in g[k])
qa = sorted(k for k in m5["common"] if q1(ga, k)); qb = sorted(k for k in m5["common"] if q1(gb, k))
hdn = sum(sets(ga, k, "HumanDecisionNeeded") == sets(gb, k, "HumanDecisionNeeded") for k in m5["common"])
out += ["", "## 10. Addendum 6 (R4-Q1 subject test) — stage difference between A and B", "",
        "- RUN_BASIS Addendum 6 was adopted while both DEL-05-02 workers were in pass 1. The PKG-05 manager sent the identical notice "
        "(`BRIEFS/RULE_NOTICE_ADDENDUM6.md`) to A and B by SendMessage at the same moment (STATE.jsonl `rule_adopted`, 2026-09-21T20:25Z).",
        "- **Worker A received it before sealing and applied it. Worker B had already sealed** (its claims file hash at send time equals its sealed hash) "
        "and left the ledger unchanged, listing the rows the test would touch in its notes §6a. The two ledgers are therefore not at the same rule stage "
        "for R4-Q1; R3 re-derives R4-Q1 on B's sealed rows by script from the REACH tags (Addendum 6 scope).",
        f"- Base keys citing R4-Q1: A {len(qa)} ({', '.join(k.split('#')[1] for k in qa) or 'none'}); B {len(qb)} ({', '.join(k.split('#')[1] for k in qb) or 'none'}).",
        f"- HumanDecisionNeeded exact agreement on indexed base keys: {pct(hdn, len(m5['common']))}. "
        "Disposition is unaffected by the test's rule 3 (R4-Q1 citation) but rules 1–2 can move a row between module-level and live-path readings.",
        "- RUN_BASIS Addendum 7 (R4-Q5) was adopted after **both** A and B had sealed their forward ledgers (STATE.jsonl `rule_adopted` Addendum 7), so neither received it and both are at the same stage for R4-Q5; any plain `R4` rows on the stored-as-received vs translated question are mapped by R3.", ""]
p = os.path.join(PKG, "DOUBLE_BLIND_DEL-05-02.md")
t = open(p).read()
t = t.split("\n## 9. Addendum 5")[0].rstrip("\n") + "\n"
open(p, "w").write(t + "\n".join(out) + "\n")
print("\n".join(out[:16]))
