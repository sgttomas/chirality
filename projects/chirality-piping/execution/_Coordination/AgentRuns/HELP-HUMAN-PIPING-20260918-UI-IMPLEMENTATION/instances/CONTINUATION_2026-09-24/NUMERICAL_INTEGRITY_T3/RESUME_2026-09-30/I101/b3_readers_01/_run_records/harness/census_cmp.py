"""I101 (B3 readers): the census at b2 (e67c364680, corpus 07m) against I100's I4' 07m census
(A = R/I100/b1_sc_01/_run_records/acceptance), every read in full: input digest; bound, unbound,
transport; RS's standing. 0 changes is required.
Usage: census_cmp.py <A> <S/out> <label>"""
import gzip, json, sys
A, O, L = sys.argv[1:4]
load = lambda p: [json.loads(l) for l in (gzip.open(p, "rt") if p.endswith(".gz") else open(p)) if l.strip()]
res = {}
for r in ("rs", "ts"):
    me = load(f"{O}/{L}_{r}_census.jsonl"); i4p = load(f"{A}/census_07m_i4p_{r}.jsonl.gz")
    keys = ("input_sha256", "bound", "unbound", "transport") + (("standing",) if r == "rs" else ())
    assert [(x["set"], x["i"], x["id"]) for x in me] == [(x["set"], x["i"], x["id"]) for x in i4p]
    ch = [(x["id"], k) for x, y in zip(i4p, me) for k in keys if x.get(k) != y.get(k)]
    sets = {s: sum(1 for x in me if x["set"] == s) for s in ("base", "mutation", "must_pass")}
    res[r] = {"entries": len(me), "sets": sets, "changes_vs_I4p": ch}
    print(r, {"entries": len(me), "sets": sets, "changes vs I4'": len(ch)})
json.dump(res, open(f"{O}/CENSUS_CMP_{L}.json", "w"), indent=1)
