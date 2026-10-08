"""I100 B3: PY's three readings on another reader's materialized inputs (I101's {name, base, source, invocation} lines),
in I101's reading format, then the comparison with RS's and TS's readings of the same lines (gate and code; G7's
codes are each language's base codes, compared by gate only). Usage: py_on_inputs.py <P root> <inputs> <rs> <ts> <out>"""
import json
import sys

P = sys.argv[1]; sys.path.insert(0, P)
from core.analysis_runs.retained_precision import RetainedPrecisionError, validate_retained_precision, validate_retained_precision_transport  # noqa: E402


def reading(run):
    try:
        r = run()
        return {"ok": {"eligible": bool(r.get("numerical_eligible"))}}
    except RetainedPrecisionError as e:
        return {"gate": e.gate, "code": e.code}


rows = [json.loads(l) for l in open(sys.argv[2]) if l.strip()]
rs = [json.loads(l) for l in open(sys.argv[3]) if l.strip()]
ts = [json.loads(l) for l in open(sys.argv[4]) if l.strip()]
py, diffs = [], []
for d, r, t in zip(rows, rs, ts):
    s, inv = d["source"], d["invocation"]
    line = {"name": d["name"], "base": d["base"], "bound": reading(lambda: validate_retained_precision(s, inv)),
            "unbound": reading(lambda: validate_retained_precision(s)), "transport": reading(lambda: validate_retained_precision_transport(s))}
    py.append(line)
    assert (r["name"], r["base"]) == (t["name"], t["base"]) == (d["name"], d["base"])
    for k in ("bound", "unbound", "transport"):
        key = lambda v: v if "ok" in v or v["gate"] != "G7" else {"gate": "G7"}
        if not (key(line[k]) == key(r[k]) == key(t[k])):
            diffs.append({"name": d["name"], "base": d["base"], "reading": k, "py": line[k], "rs": r[k], "ts": t[k]})
json.dump({"shapes": len(rows), "differences_outside_g7_codes": diffs}, open(sys.argv[5], "w"), indent=1)
print(len(rows), "shapes;", len(diffs), "differences outside G7's per-language codes")
