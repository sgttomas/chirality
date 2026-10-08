import json, hashlib, sys
# Independent H(domain, payload): JCS of {"domain":..., "payload":...}; floats refused (none expected).
def chk(v):
    if isinstance(v, float): raise SystemExit("float present: JCS number form needed")
    if isinstance(v, dict): [chk(x) for x in v.values()]
    if isinstance(v, list): [chk(x) for x in v]
def jcs(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
root = sys.argv[1]
for name in ["retained_precision_prepared_ordinary_v1", "retained_precision_prepared_combination_v1", "retained_precision_prepared_exact_v1"]:
    d = json.load(open(f"{root}/fixtures/results/{name}.json"))
    chk(d)
    h = hashlib.sha256(jcs({"domain": "retained_precision_formation_v1", "payload": d}).encode()).hexdigest()
    print(name, d.get("id") or d.get("definition_id"), h)
