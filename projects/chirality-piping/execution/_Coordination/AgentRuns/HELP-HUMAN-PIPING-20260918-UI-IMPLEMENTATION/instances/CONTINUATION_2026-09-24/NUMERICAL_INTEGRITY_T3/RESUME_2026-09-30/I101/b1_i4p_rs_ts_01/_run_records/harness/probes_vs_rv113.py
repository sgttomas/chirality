"""I101: my probe outputs at I4 against RV113's recorded outputs on the same 392 probes (probes_ts1.json),
every verdict in full (bound, unbound, transport). Usage: probes_vs_rv113.py <rv113 .jsonl.gz> <mine .jsonl> <label>"""
import gzip, json, sys
a = [json.loads(l) for l in gzip.open(sys.argv[1], "rt") if l.strip()]
b = [json.loads(l) for l in open(sys.argv[2]) if l.strip()][:len(a)]
diff = [(x["id"], k) for x, y in zip(a, b) for k in ("bound", "unbound", "transport") if x["id"] != y["id"] or x.get(k) != y.get(k)]
print(json.dumps({"label": sys.argv[3], "rv113_probes": len(a), "compared": len(b), "verdicts_differing": len(diff), "first": diff[:5]}))
