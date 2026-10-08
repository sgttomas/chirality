"""I100 B3 repair 01: RV120's exact inputs as edits from bases PY's tests already hold (07n grammar, as B3's shapes):
the corpus's preview cases (RS's exact construction starts from them) and lane P's m3x successor. Each re-materializes,
by the 07e format rule with DEF-E's H (PY's `reseal`), byte-equal to RV120's input (sha256 as RV120's INPUTS_INDEX).
Usage: rep1_compact.py <P root with B3's tests> <inputs dir> <out.json>"""
import copy, hashlib, json, sys
P = sys.argv[1]; sys.path[:0] = [P, P + "/tests"]
import test_retained_precision_b3 as t  # noqa: E402
from core.analysis_runs import retained_precision as rp  # noqa: E402
HASHES = [("retained_precision", "receipt_sha256"), ("retained_precision", "body", "publication_sha256"), ("retained_precision", "body", "invocation", "value")]
def computed(p):
    p = tuple(p)
    return p in HASHES or (p[:3] == ("retained_precision", "body", "sources") and p[4:] == ("preparation", "sha256")) or (
        p[:3] == ("retained_precision", "body", "cases") and p[4:] == ("source_identity_sha256",))
def diff(a, b, path=()):
    if computed(path): return []
    if type(a) is dict and type(b) is dict:
        out = [{"path": list(path) + [k], "op": "remove"} for k in a if k not in b]
        for k in b: out += diff(a[k], b[k], path + (k,)) if k in a else [{"path": list(path) + [k], "op": "set", "value": b[k]}]
        return out
    if type(a) is list and type(b) is list and len(a) == len(b):
        return [e for i, (x, y) in enumerate(zip(a, b)) for e in diff(x, y, path + (i,))]
    same = type(a) is type(b) and json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
    return [] if same else [{"path": list(path), "op": "set", "value": b}]
canon = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":"))
corpus = {c["id"]: c for c in json.load(open(f"{P}/fixtures/results/retained_precision_cases.json"))["cases"]}
BASES = {"ordinary_prepared_synthetic": ("corpus", "ordinary_prepared_synthetic"), "two_case_synthetic": ("corpus", "two_case_synthetic"),
         "m3x_sparse_interactive": ("m3x_producer", "sparse_interactive")}
def base(name):
    kind, key = BASES[name]
    return (corpus[key]["source"], corpus[key]["invocation"]) if kind == "corpus" else t.m3x_producer(key)
out = []
for f in ("g5b_order", "forge_eg"):
    for r in map(json.loads, open(f"{sys.argv[2]}/{f}.jsonl")):
        bname = r["name"].rsplit("[", 1)[1].rstrip("]")
        bs, bi = base(bname)
        edits, inv_edits = diff(bs, r["source"]), diff(bi, r["invocation"])
        s, i = copy.deepcopy(bs), copy.deepcopy(bi)
        for value, es in ((s, edits), (i, inv_edits)):
            for e in es:
                at = value
                for k in e["path"][:-1]: at = at[k]
                if e["op"] == "remove": del at[e["path"][-1]]
                else: at[e["path"][-1]] = copy.deepcopy(e["value"])
        sealed = t.reseal(s, i, rp.EXACT_DEFINITION_HASH)
        sha = hashlib.sha256(canon([r["source"], r["invocation"]]).encode()).hexdigest()
        same = canon([sealed, i]) == canon([r["source"], r["invocation"]])
        out.append({"name": r["name"], "base": list(BASES[bname]), "want": r["want"], "edits": edits, "invocation_edits": inv_edits, "input_sha256": sha})
        print(r["name"], "edits", len(edits), len(inv_edits), "bytes", len(json.dumps([edits, inv_edits])), "rematerializes:", same)
json.dump(out, open(sys.argv[3], "w"), sort_keys=True)
