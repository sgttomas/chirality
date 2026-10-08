"""RV120 (B3): consistent E or G-hat forgeries on an exact base, to judge I101's argued-equivalent mutants B28 and B29.
The receipt's E (or G-hat) moves one ulp in every copy (material basis, id-map member, prepared old_source, operational
inputs), the derived operational stiffness (as the readers recompute it: product / length) moves with it in the attempt
results and both section-term copies, the sources' native hashes are resealed with the PY reader's own encoding, then
07e's rehash (DEF-E). For G-hat the evidence G_pa moves too (N-6); for E the evidence E_pa stays authored (S-C).
Usage: python forge_eg.py <PY P root> <rs_inputs.jsonl> <out.jsonl>"""
import copy, hashlib, json, math, struct, sys
P = sys.argv[1]; sys.path.insert(0, P)
from core.analysis_runs.retained_precision import _native_source_encoding  # noqa: E402
from core.serialization.canonical_json.adapter import canonical_sha256_checked_v1  # noqa: E402
DEF_E = "5a3bac430df9bbc77484d5419c75880ad40ae209b439e5f928374458025281af"
def h(domain, payload): return canonical_sha256_checked_v1({"domain": domain, "payload": payload})
f = lambda x: struct.unpack(">d", bytes.fromhex(x))[0]
hx = lambda v: struct.pack(">d", v).hex()
def up(x): return hx(struct.unpack(">d", struct.pack(">q", struct.unpack(">q", bytes.fromhex(x))[0] + 1))[0])
def rehash(source):
    body = source["retained_precision"]["body"]; attempts = body["product_attempts"]
    for s in body["sources"]:
        prep = s.get("preparation")
        if type(prep) is not dict: continue
        a = attempts[prep["attempt_ref"]]; members = a["preparation"]["members"]
        if not all(m["result"]["kind"] == "prepared" for m in members): continue
        prep["sha256"] = h("retained_precision_preparation_v1", {"definition_id": a["definition_id"], "definition_sha256": DEF_E, "owner_ref": a["owner_ref"],
            "ordinary_attempt_ref": a["ordinary_attempt_ref"], "material_basis_ref": a["material_basis_ref"],
            "members": [{"member": m["member"], "old_source": m["old_source"], "old_facts": m["old_facts"], "section": m["result"]["section"]} for m in members]})
    for c in body["cases"]:
        if c["status"] != "selected": continue
        s = copy.deepcopy(body["sources"][c["source_ref"]]); s.pop("index", None)
        c["source_identity_sha256"] = h("retained_precision_source_mp_v2", s)
    body["publication_sha256"] = h("retained_precision_publication_mp_v2", {k: v for k, v in source.items() if k != "retained_precision"})
    source["retained_precision"]["receipt_sha256"] = h("retained_precision_receipt_mp_v2", body)
def forge(source, which):
    s = copy.deepcopy(source); b = s["retained_precision"]["body"]
    key, idx, stiff = ("elastic_modulus", 6, "axial_stiffness") if which == "E" else ("shear_modulus", 7, "torsional_stiffness")
    old = b["material_bases"][0]["materials"][0][key]; new = up(old)
    text = json.dumps(s).replace(f'"{old}"', f'"{new}"'); s = json.loads(text); b = s["retained_precision"]["body"]
    n = text.count(f'"{new}"')
    for a in b["product_attempts"]:
        for side in ("old", "new"):
            for op in a["operational"][side]:
                x = [f(v) for v in op["inputs"]]; d = [x[i + 3] - x[i] for i in range(3)]
                length = math.sqrt(((d[0] * d[0]) + (d[1] * d[1])) + (d[2] * d[2]))
                prod = x[6] * x[8] if which == "E" else x[7] * x[9]
                if op["result"].get(stiff) is not None: op["result"][stiff] = hx(prod / length)
                if side == "new":
                    for src in b["sources"]:
                        for st in src["section_terms"]:
                            if st["member"] == op["member"]: st[stiff] = op["result"][stiff]
    for c in b["cases"]:
        sel = c.get("selection")
        if type(sel) is dict and c.get("source_ref") is not None:
            for left, right in zip(sel.get("section_terms", []), b["sources"][c["source_ref"]]["section_terms"]): left[stiff] = right[stiff]
    if which == "G":
        for e in s["contract_evidence"]["exact_cases"]:
            for pm in e["pipe_materials"]: pm["G_pa"] = f(new)
    swaps = {}
    for src in b["sources"]:
        for include_loads, field in ((True, "kernel_source_sha256"), (False, "stiffness_sha256")):
            swaps[src[field]] = hashlib.sha256(_native_source_encoding(src, include_loads)).hexdigest()
    # Every copy of a resealed native hash (the native runs' call groups, any other reference) moves with it.
    text = json.dumps(s)
    for old_hash, new_hash in swaps.items(): text = text.replace('"' + old_hash + '"', '"' + new_hash + '"')
    s = json.loads(text)
    rehash(s)
    return s, n
dump = [json.loads(l) for l in open(sys.argv[2]) if l.strip()]
out = open(sys.argv[3], "w")
for base in ("ordinary_prepared_synthetic", "m3x_sparse_interactive"):
    d = next(x for x in dump if x["name"] == "base" and x["base"] == base)
    for which in ("E", "G"):
        s, n = forge(d["source"], which)
        out.write(json.dumps({"name": f"forge {which}-hat+1ulp, every copy, native hashes resealed [{base}]", "want": "G8 PREPARATION_MISMATCH", "copies": n, "source": s, "invocation": d["invocation"]}) + "\n")
        print(base, which, "copies", n)
