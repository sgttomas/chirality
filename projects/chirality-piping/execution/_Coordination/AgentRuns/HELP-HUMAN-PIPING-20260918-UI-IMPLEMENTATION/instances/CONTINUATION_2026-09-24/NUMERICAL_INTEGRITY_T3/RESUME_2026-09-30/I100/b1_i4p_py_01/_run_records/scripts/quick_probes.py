"""I100: a few named probes through RV113's harness functions on one P tree (a light check, not a record run).
Usage: quick_probes.py <P root> <probes.json> <id> [<id> ...]"""
import importlib.util, json, sys
root, pp, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
sys.argv = [sys.argv[0], root, "probes", pp, "/dev/null"]
spec = importlib.util.spec_from_file_location("h", __file__.rsplit("/", 1)[0] + "/rv113_py_harness.py")
src = open(spec.origin).read().replace("\nmain()\n", "\n")
g = {"__name__": "h"}
exec(compile(src, spec.origin, "exec"), g)
P = {p["id"]: p for p in json.load(open(pp))}
for i in ids:
    r = g["evaluate"]("probe", 0, P[i])
    print(i, {k: (v.get("err") and (v["err"]["gate"], v["err"]["code"], (v["err"]["detail"] or "")[:90])) or v for k, v in r.items() if k in ("bound", "unbound", "transport")})
