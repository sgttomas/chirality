"""RV120 (B3): materialize I100's B3 shapes file (07n grammar plus definition_sha256) for the raw runners; 07e's format
rule with the shape's own definition H (RV113's apply rule: a missing key on a path is created). Not part of any candidate.
Usage: python gen_i100_shapes.py <P root> <b3_shapes.json.gz> <out.jsonl>"""
import copy, gzip, json, sys
sys.path.insert(0, sys.argv[1])
from core.serialization.canonical_json.adapter import canonical_sha256_checked_v1  # noqa: E402
d = json.load(gzip.open(sys.argv[2], "rt"))
bases = {b["id"]: b for b in d["bases"]}
def h(domain, payload): return canonical_sha256_checked_v1({"domain": domain, "payload": payload})
def apply(root_value, e):
    at = root_value
    for p in e["path"][:-1]: at = at[p] if type(p) is int else at.setdefault(p, {})
    last = e["path"][-1]
    if e["op"] == "remove": (at.pop(last, None) if type(at) is dict else at.pop(last))
    elif type(last) is int and last == len(at): at.append(copy.deepcopy(e["value"]))
    else: at[last] = copy.deepcopy(e["value"])
def rehash(source, dh):
    body = source.get("retained_precision", {}).get("body") if type(source.get("retained_precision")) is dict else None
    if type(body) is not dict: return
    attempts = body["product_attempts"]
    for s in body["sources"]:
        prep = s.get("preparation")
        if type(prep) is not dict: continue
        ai = prep.get("attempt_ref")
        if type(ai) is not int or ai >= len(attempts) or type(attempts[ai]) is not dict: continue
        a = attempts[ai]; members = a["preparation"]["members"]
        if not all(m["result"]["kind"] == "prepared" for m in members): continue
        prep["sha256"] = h("retained_precision_preparation_v1", {"definition_id": a["definition_id"], "definition_sha256": dh,
            "owner_ref": a["owner_ref"], "ordinary_attempt_ref": a["ordinary_attempt_ref"], "material_basis_ref": a["material_basis_ref"],
            "members": [{"member": m["member"], "old_source": m["old_source"], "old_facts": m["old_facts"], "section": m["result"]["section"]} for m in members]})
    for c in body["cases"]:
        if c.get("status") != "selected": continue
        s = copy.deepcopy(body["sources"][c["source_ref"]]); s.pop("index", None)
        c["source_identity_sha256"] = h("retained_precision_source_mp_v2", s)
    body["publication_sha256"] = h("retained_precision_publication_mp_v2", {k: v for k, v in source.items() if k != "retained_precision"})
    source["retained_precision"]["receipt_sha256"] = h("retained_precision_receipt_mp_v2", body)
n = 0
with open(sys.argv[3], "w") as f:
    for sh in d["shapes"]:
        b = bases[sh["base"]]; source, inv = copy.deepcopy(b["source"]), copy.deepcopy(b["invocation"])
        for e in sh.get("edits") or []: apply(source, e)
        for e in sh.get("invocation_edits") or []: apply(inv, e)
        if sh.get("invocation_edits"): source["retained_precision"]["body"]["invocation"]["value"] = h("source_blocks_invocation_v1", inv)
        assert sh["rehash"] == "all"; rehash(source, sh["definition_sha256"])
        for e in sh.get("after_rehash") or []: apply(source, e)
        ep = sh.get("expected_python")
        f.write(json.dumps({"name": f"{sh['id']} [{sh['base']}]", "want": "?", "expected_python_i100": ep, "source": source, "invocation": inv}) + "\n"); n += 1
print(n, "shapes")
