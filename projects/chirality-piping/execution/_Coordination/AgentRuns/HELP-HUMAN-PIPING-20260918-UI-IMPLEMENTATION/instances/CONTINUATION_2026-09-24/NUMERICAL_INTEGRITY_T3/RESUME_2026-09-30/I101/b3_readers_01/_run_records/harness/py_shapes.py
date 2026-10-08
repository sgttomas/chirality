"""I101: the PY reader's three readings of the B3b shapes, on the Rust reader's materialized inputs (identical bytes).
Run from an archive copy of P at I100's committed PY head, with WT/venv. Not part of any candidate.
Usage: python py_shapes.py <inputs.jsonl[.gz]> <out.jsonl>"""
import gzip, json, sys
sys.path.insert(0, ".")
from core.analysis_runs.retained_precision import RetainedPrecisionError, validate_retained_precision, validate_retained_precision_transport
src, out = sys.argv[1:3]
rows = [json.loads(l) for l in (gzip.open(src, "rt") if src.endswith(".gz") else open(src)) if l.strip()]
def reading(run):
    try:
        r = run()
        return {"ok": {"eligible": bool(r.get("numerical_eligible"))}}
    except RetainedPrecisionError as e:
        return {"gate": e.gate, "code": e.code}
with open(out, "w") as f:
    for d in rows:
        s, inv = d["source"], d["invocation"]
        line = {"name": d["name"], "base": d["base"],
                "bound": reading(lambda: validate_retained_precision(s, inv)),
                "unbound": reading(lambda: validate_retained_precision(s)),
                "transport": reading(lambda: validate_retained_precision_transport(s))}
        f.write(json.dumps(line) + "\n")
print(len(rows), "shapes")
