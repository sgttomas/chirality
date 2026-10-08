"""I100 B3 addendum 01: the shared shapes for the three-reader comparison, in B3's shapes format (b3_shapes.py: 07n
grammar plus definition_sha256 and expected_python; RV113's line format for PY's verdicts; I101's input line format).
Bases: PP's milestone successors, the synthetic m3x and lane P's m3x successors (m3xp), both modes, as in B3.
Shapes: the 44 sourced-case probes on the preview route (invocation edits; DEF-O's H), expected from the module's
SOURCED_CASE; and on the exact bases x08 (analysis_state) and p02 (a case-level pressure key) (DEF-E's H).
Every shape re-materializes from the file to the test module's own construction.
Usage: add1_shapes.py <P root> <probes.json> <shapes.json> <py.jsonl> <inputs.jsonl>"""
import copy
import hashlib
import json
import sys

P = sys.argv[1]
sys.path[:0] = [P, P + "/tests"]
import test_retained_precision_b3 as t  # noqa: E402
from core.analysis_runs import retained_precision as rp  # noqa: E402


# From B3's b3_shapes.py, verbatim: the computed paths, diff, apply, materialize, canon and verdict.
HASHES = [("retained_precision", "receipt_sha256"), ("retained_precision", "body", "publication_sha256"), ("retained_precision", "body", "invocation", "value")]


def computed(path):
    """Paths the format rule recomputes (never edits)."""
    p = tuple(path)
    if p in HASHES:
        return True
    if p[:3] == ("retained_precision", "body", "sources") and p[4:] == ("preparation", "sha256"):
        return True
    return p[:3] == ("retained_precision", "body", "cases") and p[4:] == ("source_identity_sha256",)


def diff(a, b, path=()):
    if computed(path):
        return []
    if type(a) is dict and type(b) is dict:
        out = [{"path": list(path) + [k], "op": "remove"} for k in a if k not in b]
        for k in b:
            out += diff(a[k], b[k], path + (k,)) if k in a else [{"path": list(path) + [k], "op": "set", "value": b[k]}]
        return out
    if type(a) is list and type(b) is list and len(a) == len(b):
        return [e for i, (x, y) in enumerate(zip(a, b)) for e in diff(x, y, path + (i,))]
    same = json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True) and type(a) is type(b)
    return [] if same else [{"path": list(path), "op": "set", "value": b}]


def apply(value, edits):
    for e in edits:
        at = value
        for k in e["path"][:-1]:
            at = at[k]
        if e["op"] == "remove":
            del at[e["path"][-1]]
        else:
            at[e["path"][-1]] = copy.deepcopy(e["value"])


def materialize(base, shape):
    source, invocation = copy.deepcopy(base["source"]), copy.deepcopy(base["invocation"])
    apply(source, shape["edits"]); apply(invocation, shape["invocation_edits"])
    sealed = t.reseal(source, invocation, shape["definition_sha256"])
    return sealed, invocation


def canon(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"))


def verdict(run):
    try:
        v = run()
        cls = json.dumps(v["classifications"], sort_keys=True, default=str)
        return {"ok": {"invocation_bound": v["invocation_bound"], "numerical_eligible": v["numerical_eligible"], "standing": v["standing"],
                       "publication_sha256": v["publication_sha256"], "classifications": len(v["classifications"]),
                       "classifications_sha256": hashlib.sha256(cls.encode()).hexdigest()}}
    except rp.RetainedPrecisionError as e:
        return {"err": {"gate": e.gate, "code": e.code, "detail": e.detail}}
    except Exception as e:  # noqa: BLE001
        return {"escape": f"{type(e).__name__}: {e}"}

SHORT = {"sparse_interactive": "sparse", "dense_scrutiny": "dense"}
EXPECTED = {(k, canon(v)): list(e or ("pass", True, "eligible")) for k, v, e in t.SOURCED_CASE}

bases, shapes, built = [], [], []
for mode in t.MODES:
    for name, doc in (("milestone", t.milestone(mode)), ("m3x", t.m3x(mode)), ("m3xp", t.m3x_producer(mode))):
        bases.append({"id": f"{name}_{SHORT[mode]}", "source": doc[0], "invocation": doc[1]})
base = {b["id"]: b for b in bases}
for probe in json.load(open(sys.argv[2])):
    mode = probe["base"].removeprefix("milestone_")
    (edit,) = probe["invocation_edits"]
    key, value = edit["path"][-1], edit["value"]
    source, invocation = t.milestone(mode)
    invocation = t.edited_invocation(invocation, lambda m: m["load_cases"][0].update({key: copy.deepcopy(value)}))
    doc = (t.reseal(source, invocation), invocation)
    b = base[f"milestone_{SHORT[mode]}"]
    shapes.append({"id": probe["id"], "base": b["id"], "edits": diff(b["source"], doc[0]), "invocation_edits": diff(b["invocation"], doc[1]),
                   "rehash": "all", "definition_sha256": rp.DEFINITION_HASH, "expected_python": EXPECTED[(key, canon(value))]})
    assert shapes[-1]["invocation_edits"] == probe["invocation_edits"] and shapes[-1]["edits"] == [], probe["id"]
    built.append(doc)
for mode in t.MODES:
    for kind, name in (("synthetic", "m3x"), ("producer", "m3xp")):
        for label in ("x08 a case with analysis_state", "p02 a case-level pressure key (PP's typed case has none; addendum 01)"):
            doc = t.exact_shape(mode, label, kind)
            b = base[f"{name}_{SHORT[mode]}"]
            expected = list(t.B3B_REFUSALS[label][1]) if label in t.B3B_REFUSALS else ["pass", True, "eligible"]
            shapes.append({"id": f"add1 exact {label.split()[0]} on {name} [{SHORT[mode]}]", "base": b["id"], "edits": diff(b["source"], doc[0]),
                           "invocation_edits": diff(b["invocation"], doc[1]), "rehash": "all", "definition_sha256": rp.EXACT_DEFINITION_HASH,
                           "expected_python": expected})
            built.append(doc)
for shape, doc in zip(shapes, built):
    b = base[shape["base"]]
    source, invocation = copy.deepcopy(b["source"]), copy.deepcopy(b["invocation"])
    apply(source, shape["edits"]); apply(invocation, shape["invocation_edits"])
    assert canon([t.reseal(source, invocation, shape["definition_sha256"]), invocation]) == canon(list(doc)), shape["id"]
json.dump({"format": "07n grammar plus definition_sha256 (I100 B3 addendum 01)", "bases": bases, "shapes": shapes}, open(sys.argv[3], "w"), sort_keys=True)

misses = 0
with open(sys.argv[4], "w") as f, open(sys.argv[5], "w") as g:
    for i, (shape, (source, invocation)) in enumerate(zip(shapes, built)):
        line = {"set": "add1_shape", "i": i, "id": shape["id"], "input_sha256": hashlib.sha256(canon([source, invocation]).encode()).hexdigest(),
                "bound": verdict(lambda: rp.validate_retained_precision(copy.deepcopy(source), copy.deepcopy(invocation))),
                "unbound": verdict(lambda: rp.validate_retained_precision(copy.deepcopy(source))),
                "transport": verdict(lambda: rp.validate_retained_precision_transport(copy.deepcopy(source)))}
        got = line["bound"]
        got = ["pass", got["ok"]["numerical_eligible"], got["ok"]["standing"]] if "ok" in got else [got["err"]["gate"], got["err"]["code"]] if "err" in got else ["escape"]
        line["matches_expected_python"] = got == shape["expected_python"]
        misses += not line["matches_expected_python"]
        f.write(json.dumps(line, sort_keys=True) + "\n")
        g.write(json.dumps({"name": shape["id"], "base": shape["base"], "source": source, "invocation": invocation}) + "\n")
print(len(bases), "bases;", len(shapes), "shapes;", misses, "bound verdicts differ from the expectation")
