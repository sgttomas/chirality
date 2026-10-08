"""I101 repair 03: the N2b two-fault probe (and its swap) on the exact two_case_synthetic, added to PY's RV120 fixture as
edits from the corpus base PY's tests hold, in the fixture's own grammar. input_sha256 is RV120's formula (sha256 of
json.dumps([source, invocation], sort_keys=True, separators=(",", ":"))) over the Rust reader's materialized input, and each
shape must re-materialize through the test module's rv120_input to it. Run from an archive copy of P at b2-p with WT/venv.
Usage: gen_py_n2b.py <P root> <rs inputs dump> <fixture out>"""
import hashlib, json, sys
P, dump, out = sys.argv[1:4]
sys.path[:0] = [P, P + "/tests"]
import test_retained_precision_b3 as t  # noqa: E402
FIX = P + "/fixtures/results/retained_precision_rv120_b3_inputs.json"
text = open(FIX).read(); fixture = json.loads(text)
assert json.dumps(fixture, indent=1) + "\n" == text
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
    if not d["name"].startswith("N2b: "): continue
    assert d["base"] == "two_case_synthetic"
    b = corpus["two_case_synthetic"]
    sha = hashlib.sha256(json.dumps([d["source"], d["invocation"]], sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    shape = {"base": ["corpus", "two_case_synthetic"], "name": d["name"] + " [two_case_synthetic]",
             "want": "G7 SOURCE_PHYSICS_EVIDENCE_INVALID (case profile/material basis; transport: evidence shape)", "input_sha256": sha,
             "edits": diff(b["source"], d["source"]), "invocation_edits": diff(b["invocation"], d["invocation"])}
    t.rv120_input(shape)  # asserts the re-materialized sha256 equals the Rust reader's input
    added.append(shape)
assert len(added) == 2
fixture["description"] += " Repair 03 (I101) adds the N2b two-fault probe on the exact two_case_synthetic (one entry's profile_mode, the other's material_basis) and its swap, materialized by the Rust reader's B3b shape list."
fixture["record"] += "; N2b: the Rust reader's B3B_INPUTS_OUT (repair 03)"
fixture["shapes"] += added
open(out, "w").write(json.dumps(fixture, indent=1) + "\n")
print([(s["name"], len(s["edits"]), len(s["invocation_edits"]), s["input_sha256"]) for s in added])
