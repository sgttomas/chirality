"""RV120 (B3 review) raw runner for the Python reader. Not part of any candidate.
Usage: python rv120_b3_py_raw.py <P root> <in.jsonl> <out.jsonl>  (JSON lines {name, source, invocation})."""
import copy, json, sys
sys.path.insert(0, sys.argv[1])
from core.analysis_runs.retained_precision import RetainedPrecisionError, validate_retained_precision, validate_retained_precision_transport  # noqa: E402
def one(run):
    try:
        v = run(); return {"ok": {"eligible": bool(v["numerical_eligible"]), "bound": bool(v["invocation_bound"])}}
    except RetainedPrecisionError as e:
        return {"gate": e.gate, "code": e.code, "detail": getattr(e, "detail", None)}
    except Exception as e:  # noqa: BLE001
        return {"escape": f"{type(e).__name__}: {e}"}
n = 0
with open(sys.argv[3], "w") as f:
    for text in open(sys.argv[2]):
        if not text.strip(): continue
        d = json.loads(text); s, inv = d["source"], d["invocation"]
        f.write(json.dumps({"name": d["name"], "bound": one(lambda: validate_retained_precision(copy.deepcopy(s), copy.deepcopy(inv))),
                            "unbound": one(lambda: validate_retained_precision(copy.deepcopy(s))),
                            "transport": one(lambda: validate_retained_precision_transport(copy.deepcopy(s)))}) + "\n"); n += 1
print(n, "inputs")
