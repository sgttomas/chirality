"""I101 addendum 01: a census over 07n (638 entries) against I100's census at SC's head (A = R/I100/b1_sc_01/_run_records/
acceptance, census_sc_{rs,ts}), every read compared on gate, code, detail, eligibility, standing, publication digest and
classifications (I100's harness also printed the full class lists, so whole lines differ); input digest and RS's standing.
As I101's b1_sc_pins_01 harness/census_cmp.py. Usage: census_cmp_07n.py <A> <dir> <label>"""
import gzip, json, sys
A, O, L = sys.argv[1:4]
load = lambda p: [json.loads(l) for l in (gzip.open(p, "rt") if p.endswith(".gz") else open(p)) if l.strip()]
def short(v):
    if "ok" in v:
        o = v["ok"]; return ("ok", o.get("invocation_bound"), o.get("numerical_eligible"), o.get("standing"), o.get("publication_sha256"), o.get("classifications"), o.get("classifications_sha256"))
    if "err" in v: return ("err", v["err"]["gate"], v["err"]["code"], v["err"].get("detail"))
    return ("other", json.dumps(v))
res = {}
for r in ("rs", "ts"):
    me = load(f"{O}/{L}_{r}_census.jsonl"); sc = load(f"{A}/census_sc_{r}.jsonl.gz")
    assert [(x["set"], x["i"], x["id"]) for x in me] == [(x["set"], x["i"], x["id"]) for x in sc]
    ch = [(x["id"], k) for x, y in zip(sc, me) for k in ("bound", "unbound", "transport") if short(x[k]) != short(y[k])]
    ch += [(x["id"], k) for x, y in zip(sc, me) for k in ("input_sha256", "standing") if x.get(k) != y.get(k)]
    res[r] = {"entries": len(me), "changes_vs_SC_head": ch}
    print(r, {"entries": len(me), "changes vs SC head": len(ch)})
json.dump(res, open(f"{O}/CENSUS07N_CMP_{L}.json", "w"), indent=1)
