"""I101 (07n pins): the census at the head against I100's records (A = R/I100/b1_sc_01/_run_records/acceptance).
- 07m (bases 0..17, mutations 0..294, must-pass 0..28) against I100's I4' 07m census, every read in full (input digest;
  bound, unbound, transport; RS's standing);
- all 638 entries against I100's census at SC's head, every read compared on gate, code, detail, eligibility, standing,
  publication digest and classifications (I100's harness also printed the full class lists, so whole lines differ).
Usage: census_cmp.py <A> <S/out>"""
import gzip, json, sys
A, O = sys.argv[1:3]
load = lambda p: [json.loads(l) for l in (gzip.open(p, "rt") if p.endswith(".gz") else open(p)) if l.strip()]
def short(v):
    if "ok" in v:
        o = v["ok"]; return ("ok", o.get("invocation_bound"), o.get("numerical_eligible"), o.get("standing"), o.get("publication_sha256"), o.get("classifications"), o.get("classifications_sha256"))
    if "err" in v: return ("err", v["err"]["gate"], v["err"]["code"], v["err"].get("detail"))
    return ("other", json.dumps(v))
res = {}
for r in ("rs", "ts"):
    me = load(f"{O}/{r}_census.jsonl"); i4p = load(f"{A}/census_07m_i4p_{r}.jsonl.gz"); sc = load(f"{A}/census_sc_{r}.jsonl.gz")
    lim = {"base": 17, "mutation": 294, "must_pass": 28}
    m07 = [x for x in me if x["i"] < lim[x["set"]]]
    keys = ("input_sha256", "bound", "unbound", "transport") + (("standing",) if r == "rs" else ())
    assert [(x["set"], x["i"], x["id"]) for x in m07] == [(x["set"], x["i"], x["id"]) for x in i4p]
    assert [(x["set"], x["i"], x["id"]) for x in me] == [(x["set"], x["i"], x["id"]) for x in sc]
    c07 = [(x["id"], k) for x, y in zip(i4p, m07) for k in keys if x.get(k) != y.get(k)]
    csc = [(x["id"], k) for x, y in zip(sc, me) for k in ("bound", "unbound", "transport") if short(x[k]) != short(y[k])]
    csc += [(x["id"], k) for x, y in zip(sc, me) for k in ("input_sha256", "standing") if x.get(k) != y.get(k)]
    res[r] = {"entries": len(me), "07m_entries": len(m07), "07m_changes_vs_I4p": c07, "changes_vs_SC_head": csc}
    print(r, {"entries": len(me), "07m": len(m07), "07m changes vs I4'": len(c07), "changes vs SC head": len(csc)})
json.dump(res, open(f"{O}/CENSUS_CMP.json", "w"), indent=1)
