"""I101 repair 02: RV120's N2 probe (both bases) added to PY's RV120 fixture as edits from bases PY's tests hold, in the
fixture's own grammar; each shape must re-materialize through the test module's rv120_input to RV120's input_sha256.
Run from an archive copy of P at b2-p with WT/venv. Usage: gen_py_n2.py <P root> <rs inputs dump> <INPUTS_INDEX> <fixture out>"""
import copy, json, sys
P, dump, index, out = sys.argv[1:5]
sys.path[:0] = [P, P + "/tests"]
import test_retained_precision_b3 as t  # noqa: E402
FIX = P + "/fixtures/results/retained_precision_rv120_b3_inputs.json"
text = open(FIX).read(); fixture = json.loads(text)
assert json.dumps(fixture, indent=1) + "\n" == text
idx = {d["name"]: d["input_sha256"] for d in map(json.loads, open(index))}
HASHES = [("retained_precision", "receipt_sha256"), ("retained_precision", "body", "publication_sha256"), ("retained_precision", "body", "invocation", "value")]
def computed(p):
    p = tuple(p)
    return p in HASHES or (p[:3] == ("retained_precision", "body", "sources") and p[4:] == ("preparation", "sha256")) \
        or (p[:3] == ("retained_precision", "body", "cases") and p[4:] == ("source_identity_sha256",))
def diff(a, b, path=()):
    if computed(path): return []
    if type(a) is dict and type(b) is dict:
        out = [{"path": list(path) + [k], "op": "remove"} for k in a if k not in b]
        for k in b: out += diff(a[k], b[k], path + (k,)) if k in a else [{"path": list(path) + [k], "op": "set", "value": b[k]}]
        return out
    if type(a) is list and type(b) is list and len(a) == len(b):
        return [e for i, (x, y) in enumerate(zip(a, b)) for e in diff(x, y, path + (i,))]
    same = json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True) and type(a) is type(b)
    return [] if same else [{"path": list(path), "op": "set", "value": b}]
corpus = {c["id"]: c for c in json.load(open(P + "/fixtures/results/retained_precision_cases.json"))["cases"]}
added = []
for d in map(json.loads, open(dump)):
    if not d["name"].startswith("RV120 N2: "): continue
    name = f"X G8: an exact_cases entry for a case not in the invocation [{d['base']}]"
    if d["base"] == "ordinary_prepared_synthetic":
        base = ["corpus", "ordinary_prepared_synthetic"]; b = corpus["ordinary_prepared_synthetic"]; bs, bi = b["source"], b["invocation"]
    else:
        assert d["base"] == "m3x_sparse_interactive"
        base = ["m3x_producer", "sparse_interactive"]; bs, bi = t.m3x_producer("sparse_interactive")
    shape = {"base": base, "name": name, "want": "?", "input_sha256": idx[name], "edits": diff(bs, d["source"]), "invocation_edits": diff(bi, d["invocation"])}
    shape["want"] = "G7 SOURCE_PHYSICS_EVIDENCE_INVALID (transport: maximum result ID)"
    t.rv120_input(shape)  # asserts the re-materialized sha256 equals RV120's
    added.append(shape)
assert len(added) == 2
fixture["description"] += " Repair 02 (I101) adds RV120's N2 probe, an exact_cases entry for a case not in the invocation, on both bases."
fixture["record"] += "; N2: b3_probes (its INPUTS_INDEX sha256)"
fixture["shapes"] += added
open(out, "w").write(json.dumps(fixture, indent=1) + "\n")
print([(s["name"], len(s["edits"]), len(s["invocation_edits"])) for s in added])
