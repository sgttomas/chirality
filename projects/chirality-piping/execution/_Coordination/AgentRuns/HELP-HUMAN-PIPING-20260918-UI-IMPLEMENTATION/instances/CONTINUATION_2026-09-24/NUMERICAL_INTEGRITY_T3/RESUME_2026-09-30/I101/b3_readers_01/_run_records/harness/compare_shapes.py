"""I101: the B3b shapes, RS against TS. Inputs: each reader's materialized inputs (B3B_INPUTS_OUT) and readings
(B3B_SHAPES_OUT). The inputs must be equal as JSON values (TS cannot print -0; none occurs); the readings must be
equal at every gate and code except G7, where each reader reports its own base code (C1 G7 settlement).
Usage: compare_shapes.py <rs inputs> <ts inputs> <rs readings> <ts readings> <out.json>"""
import gzip, json, sys
def load(p): return [json.loads(l) for l in (gzip.open(p, "rt") if p.endswith(".gz") else open(p)) if l.strip()]
ri, ti, rr, tr, out = sys.argv[1:6]
RI = {(d["name"], d["base"]): d for d in load(ri)}; TI = {(d["name"], d["base"]): d for d in load(ti)}
RR = {(d["name"], d["base"]): d for d in load(rr)}; TR = {(d["name"], d["base"]): d for d in load(tr)}
assert set(RI) == set(TI) == set(RR) == set(TR), "the same shapes"
inputs_equal = [k for k in RI if (RI[k]["source"], RI[k]["invocation"]) == (TI[k]["source"], TI[k]["invocation"])]
expected_equal = [k for k in RI if RI[k]["expected_bound"] == TI[k]["expected_bound"]]
rows, diffs = [], []
for k in sorted(RR):
    row = {"name": k[0], "base": k[1]}
    for m in ("bound", "unbound", "transport"):
        a, b = RR[k][m], TR[k][m]
        row[m] = {"rs": a, "ts": b}
        same = a == b or (a.get("gate") == "G7" and b.get("gate") == "G7")
        if not same: diffs.append({"name": k[0], "base": k[1], "reading": m, "rs": a, "ts": b})
    rows.append(row)
res = {"shapes": len(RR), "inputs_equal": len(inputs_equal), "expected_bound_equal": len(expected_equal),
       "differences_outside_g7": diffs, "readings": rows}
json.dump(res, open(out, "w"), indent=1)
print(json.dumps({k: (v if k != "readings" else len(v)) for k, v in res.items()}, indent=1)[:2000])
