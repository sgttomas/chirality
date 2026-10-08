"""I100 B3: the shared new shapes for the three-reader comparison, from the PY lane's B3 test module.

Writes a portable file in the shared corpus grammar (07n), with bases materialized and each shape as edits:
  {"bases": [{"id", "source", "invocation"}],
   "shapes": [{"id", "base", "edits", "invocation_edits", "rehash": "all", "definition_sha256", "expected_python"}]}
`definition_sha256` is the hash the format rule's preparation step uses for that shape (the route's H: DEF-E's on the
exact bases, DEF-O's otherwise; entry 11 deliberately DEF-O's on an exact base). The rest of the rule is 07e's:
invocation digest when invocation edits exist, preparation hashes, selected source identities, publication, receipt.
Every shape is re-materialized from the file and checked equal to the test module's own construction.
Then PY's verdicts (bound, unbound, transport) are written in RV113's harness line format.
Usage: b3_shapes.py <P root> <shapes.json> <py.jsonl> [<inputs.jsonl>]"""
import copy
import hashlib
import json
import sys

P = sys.argv[1]
sys.path[:0] = [P, P + "/tests"]
import test_retained_precision_b3 as t  # noqa: E402
from core.analysis_runs import retained_precision as rp  # noqa: E402

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


bases, shapes, built = [], [], []
for mode in t.MODES:
    m = mode.split("_")[0]
    for name, (source, invocation) in (("milestone", t.milestone(mode)), ("m3l", t.m3l(mode)), ("m3x", t.m3x(mode)), ("m3xp", t.m3x_producer(mode))):
        bases.append({"id": f"{name}_{m}", "source": source, "invocation": invocation})
    base = {b["id"]: b for b in bases}

    def add(sid, base_id, doc, h, expected):
        b = base[base_id]
        shape = {"id": f"{sid} [{m}]", "base": base_id, "edits": diff(b["source"], doc[0]), "invocation_edits": diff(b["invocation"], doc[1]),
                 "rehash": "all", "definition_sha256": h, "expected_python": expected}
        shapes.append(shape); built.append(doc)

    # B3a on m3l (DEF-O's H).
    add("b3a 00 m3l base must-pass", f"m3l_{m}", t.m3l(mode), rp.DEFINITION_HASH, ["pass", True, "eligible"])
    for label, (change, expected) in sorted(t.B3A_REFUSALS.items()):
        s, inv = t.m3l(mode); inv = t.edited_invocation(inv, change)
        add(f"b3a {label}", f"m3l_{m}", (t.reseal(s, inv), inv), rp.DEFINITION_HASH, list(expected))
    s, inv = t.milestone(mode)
    for version in ("0.1.0", "0.2.0"):
        for value, vname in (({}, "{}"), (False, "false"), ([], "[]"), ("", '""'), (0, "0"), (dict(t.LEGACY), "legacy")):
            bad = t.edited_invocation(inv, lambda mm: mm.update(schema_version=version, pressure_contract=copy.deepcopy(value)))
            add(f"b3a L {version} pressure_contract {vname}", f"milestone_{m}", (t.reseal(s, bad), bad), rp.DEFINITION_HASH, list(t.INVOCATION))
        fine = t.edited_invocation(inv, lambda mm: mm.update(schema_version=version, pressure_contract=None))
        add(f"b3a L {version} pressure_contract null must-pass", f"milestone_{m}", (t.reseal(s, fine), fine), rp.DEFINITION_HASH, ["pass", True, "eligible"])
    bare = t.edited_invocation(inv, lambda mm: mm.update(schema_version="0.3.0"))
    add("b3a 0.3.0 without a contract", f"milestone_{m}", (t.reseal(s, bare), bare), rp.DEFINITION_HASH, list(t.INVOCATION))
    # B3b on the synthetic m3x and on lane P's m3x successor (m3xp) (DEF-E's H; entries 09 and 11 as stated).
    for kind, short in (("synthetic", "m3x"), ("producer", "m3xp")):
        add(f"b3b 00 {short} base must-pass", f"{short}_{m}", t.exact_base(mode, kind), rp.EXACT_DEFINITION_HASH, ["pass", True, "eligible"])
        for label in sorted(t.B3B_REFUSALS) + sorted(t.B3B_SPECIAL) + sorted(t.B3B_PASSES):
            if kind == "producer" and label.startswith("09"):
                continue  # its base is the preview milestone either way
            expected = list(t.B3B_REFUSALS[label][1]) if label in t.B3B_REFUSALS else list(t.B3B_SPECIAL[label]) if label in t.B3B_SPECIAL else ["pass", True, "eligible"]
            doc = t.exact_shape(mode, label, kind)
            base_id = f"milestone_{m}" if label.startswith("09") else f"{short}_{m}"
            h = rp.EXACT_DEFINITION_HASH if not (label.startswith("09") or label.startswith("11")) else rp.DEFINITION_HASH
            add(f"b3b {label}" + (" (on m3xp)" if kind == "producer" else ""), base_id, doc, h, expected)

# Portability check: every shape re-materializes, from the file's own content, to the module's construction.
base = {b["id"]: b for b in bases}
for shape, doc in zip(shapes, built):
    b = base[shape["base"]]
    source, invocation = copy.deepcopy(b["source"]), copy.deepcopy(b["invocation"])
    apply(source, shape["edits"]); apply(invocation, shape["invocation_edits"])
    sealed = t.reseal(source, invocation, shape["definition_sha256"])
    assert canon([sealed, invocation]) == canon(list(doc)), shape["id"]
json.dump({"format": "07n grammar plus definition_sha256 (I100 B3)", "bases": bases, "shapes": shapes}, open(sys.argv[2], "w"), sort_keys=True)


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


misses = 0
with open(sys.argv[3], "w") as f:
    for i, (shape, (source, invocation)) in enumerate(zip(shapes, built)):
        line = {"set": "b3_shape", "i": i, "id": shape["id"], "input_sha256": hashlib.sha256(canon([source, invocation]).encode()).hexdigest(),
                "bound": verdict(lambda: rp.validate_retained_precision(copy.deepcopy(source), copy.deepcopy(invocation))),
                "unbound": verdict(lambda: rp.validate_retained_precision(copy.deepcopy(source))),
                "transport": verdict(lambda: rp.validate_retained_precision_transport(copy.deepcopy(source)))}
        got = line["bound"]
        got = ["pass", got["ok"]["numerical_eligible"], got["ok"]["standing"]] if "ok" in got else [got["err"]["gate"], got["err"]["code"]] if "err" in got else ["escape"]
        line["matches_expected_python"] = got == shape["expected_python"]
        misses += not line["matches_expected_python"]
        f.write(json.dumps(line, sort_keys=True) + "\n")
if len(sys.argv) > 4:
    # The materialized inputs in I101's line format ({name, base, source, invocation}), for the RS and TS harnesses.
    with open(sys.argv[4], "w") as f:
        for shape, (source, invocation) in zip(shapes, built):
            f.write(json.dumps({"name": shape["id"], "base": shape["base"], "source": source, "invocation": invocation}) + "\n")
print(len(bases), "bases;", len(shapes), "shapes;", misses, "bound verdicts differ from the expectation")
