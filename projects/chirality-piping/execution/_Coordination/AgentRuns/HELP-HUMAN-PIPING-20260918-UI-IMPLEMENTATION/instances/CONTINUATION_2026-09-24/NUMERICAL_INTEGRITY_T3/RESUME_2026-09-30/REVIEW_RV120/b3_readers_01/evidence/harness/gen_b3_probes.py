"""RV120 (B3 review): materialize reviewer probes for the three B3 readers on identical bytes. Not part of any candidate.
Preview bases come from the corpus (DEF-O's H); exact bases from the Rust reader's own materialized B3b inputs (the 'base'
shapes; DEF-E's H). The 07e format rule (preparation hashes, selected source identities, publication, receipt), with the
route's definition H unless a probe names another; invocation edits rebind the invocation digest.
Usage: python gen_b3_probes.py <P root> <corpus.json> <rs_inputs.jsonl> <out.jsonl>
Controls: three of the Rust reader's own shapes are re-materialized and must equal its dump (rehash parity)."""
import copy, hashlib, json, struct, sys
root, corpus_path, dump_path, out_path = sys.argv[1:5]
sys.path.insert(0, root)
from core.serialization.canonical_json.adapter import canonical_sha256_checked_v1  # noqa: E402
DEF_O = "a7ed7ca0bf0bba6e8b821ca4befa00a0fa9541a83694be8b28ac63e39b1d0349"
DEF_E = "5a3bac430df9bbc77484d5419c75880ad40ae209b439e5f928374458025281af"
PTABLE = "b2b4a54d610aa38c66f5d31921c2d8f3113313e33eb6933e45093ba6f1e3667c"
ALT = hashlib.sha256(b"rv120").hexdigest()
EXACT_ID = "openpipestress.result_semantics/0.3.0/physics-retained-1"
corpus = json.load(open(corpus_path))
dump = [json.loads(l) for l in open(dump_path) if l.strip()]
PREVIEW = {c["id"]: (c["source"], c["invocation"]) for c in corpus["cases"]}
EXACT = {d["base"]: (d["source"], d["invocation"]) for d in dump if d["name"] == "base"}
def h(domain, payload): return canonical_sha256_checked_v1({"domain": domain, "payload": payload})
def walk(v, path):
    for p in path[:-1]:
        if type(p) is int: v = v[p]
        else: v = v.setdefault(p, {})
    return v
def apply(root_value, e):
    at = walk(root_value, e["path"]); last = e["path"][-1]
    if e["op"] == "remove": (at.pop(last, None) if type(at) is dict else at.pop(last))
    elif type(last) is int and last == len(at): at.append(copy.deepcopy(e["value"]))
    else: at[last] = copy.deepcopy(e["value"])
def rehash(source, dh):
    body = source["retained_precision"]["body"]; attempts = body["product_attempts"]
    for s in body["sources"]:
        prep = s.get("preparation")
        if type(prep) is not dict: continue
        a = attempts[prep["attempt_ref"]]; members = a["preparation"]["members"]
        if not all(m["result"]["kind"] == "prepared" for m in members): continue
        prep["sha256"] = h("retained_precision_preparation_v1", {"definition_id": a["definition_id"], "definition_sha256": dh,
            "owner_ref": a["owner_ref"], "ordinary_attempt_ref": a["ordinary_attempt_ref"], "material_basis_ref": a["material_basis_ref"],
            "members": [{"member": m["member"], "old_source": m["old_source"], "old_facts": m["old_facts"], "section": m["result"]["section"]} for m in members]})
    for c in body["cases"]:
        if c["status"] != "selected": continue
        s = copy.deepcopy(body["sources"][c["source_ref"]]); s.pop("index", None)
        c["source_identity_sha256"] = h("retained_precision_source_mp_v2", s)
    body["publication_sha256"] = h("retained_precision_publication_mp_v2", {k: v for k, v in source.items() if k != "retained_precision"})
    source["retained_precision"]["receipt_sha256"] = h("retained_precision_receipt_mp_v2", body)
def materialize(p):
    src, inv = EXACT[p["base"]] if p["route"] == "exact" else PREVIEW[p["base"]]
    source, invocation = copy.deepcopy(src), copy.deepcopy(inv)
    for e in p.get("edits", []): apply(source, e)
    for e in p.get("inv", []): apply(invocation, e)
    if p.get("inv"): source["retained_precision"]["body"]["invocation"]["value"] = h("source_blocks_invocation_v1", invocation)
    dh = p.get("hash") or (DEF_E if source["producer"]["semantic_contract_id"] == EXACT_ID else DEF_O)
    rehash(source, dh)
    for e in p.get("after", []): apply(source, e)
    return source, invocation
S = lambda path, value: {"op": "set", "path": path, "value": value}
R = lambda path: {"op": "remove", "path": path}
M = lambda *t: ["request", "model", *t]
RB = lambda *t: ["retained_precision", "body", *t]
CE = lambda *t: ["contract_evidence", "exact_cases", *t]
def ulp(x, n=1): return struct.unpack(">d", struct.pack(">q", struct.unpack(">q", struct.pack(">d", x))[0] + n))[0]
probes = []
def add(name, route, base, want, **kw): probes.append({"name": name, "route": route, "base": base, "want": want, **kw})
INV, PREP, OK = "G8 INVOCATION_MISMATCH", "G8 PREPARATION_MISMATCH", "eligible"
LEGACY = {"version": "1.0.0", "mode": "legacy_pressure_v1"}
EXACTC = {"version": "2.0.0", "mode": "exact_straight_pressure_v2"}
# Preview route (B3a namespace; the sourced-case rule; S-1 across routes).
for b in ("ordinary_prepared_synthetic", "u8_l0_isolated_node_sparse_interactive"):
    for tag, v in (("false", False), ("0", 0), ("empty string", ""), ("[]", []), ("{}", {})):
        add(f"P namespace: {PREVIEW[b][1]['request']['model']['schema_version']} with pressure_contract {tag}", "preview", b, INV, inv=[S(M("pressure_contract"), v)])
    add("P namespace: explicit pressure_contract null", "preview", b, OK, inv=[S(M("pressure_contract"), None)])
b = "ordinary_prepared_synthetic"
add("P namespace: 0.3.0 with the legacy contract", "preview", b, OK, inv=[S(M("schema_version"), "0.3.0"), S(M("pressure_contract"), LEGACY)])
add("P namespace: 0.3.0 with the legacy contract, keys reordered", "preview", b, OK, inv=[S(M("schema_version"), "0.3.0"), S(M("pressure_contract"), {"mode": "legacy_pressure_v1", "version": "1.0.0"})])
add("P namespace: 0.3.0, legacy contract version as number 1", "preview", b, INV, inv=[S(M("schema_version"), "0.3.0"), S(M("pressure_contract"), {"version": 1, "mode": "legacy_pressure_v1"})])
add("P namespace: 0.3.0, legacy contract version as list", "preview", b, INV, inv=[S(M("schema_version"), "0.3.0"), S(M("pressure_contract"), {"version": ["1.0.0"], "mode": "legacy_pressure_v1"})])
add("P namespace: 0.3.0, legacy contract with an extra key", "preview", b, INV, inv=[S(M("schema_version"), "0.3.0"), S(M("pressure_contract"), {**LEGACY, "x": None})])
add("P namespace: 0.3.0, contract null", "preview", b, INV, inv=[S(M("schema_version"), "0.3.0"), S(M("pressure_contract"), None)])
add("P namespace: 0.3.0, contract absent", "preview", b, INV, inv=[S(M("schema_version"), "0.3.0")])
add("P namespace: 0.3.0, the exact contract", "preview", b, INV, inv=[S(M("schema_version"), "0.3.0"), S(M("pressure_contract"), EXACTC)])
add("P namespace: 0.2.0 with the legacy contract", "preview", b, INV, inv=[S(M("pressure_contract"), LEGACY)])
add("P namespace: schema_version number 0.2", "preview", b, INV, inv=[S(M("schema_version"), 0.2)])
add("P namespace: schema_version list", "preview", b, INV, inv=[S(M("schema_version"), ["0.2.0"])])
add("P namespace: 0.4.0 with the legacy contract", "preview", b, INV, inv=[S(M("schema_version"), "0.4.0"), S(M("pressure_contract"), LEGACY)])
for tag, v, want in (("[]", [], OK), ("null", None, OK), ("{}", {}, PREP), ("empty string", "", PREP), ("0", 0, PREP), ("false", False, PREP), ("one region", [{"id": "region:x", "member_pipe_ids": [], "pressure": {"value": 0, "unit": "Pa"}}], PREP)):
    add(f"P sourced case: pressure_regions {tag}", "preview", b, want, inv=[S(M("load_cases", 0, "pressure_regions"), v)])
for tag, v, want in (("null", None, OK), ("false", False, PREP), ("{}", {}, PREP), ("[]", [], PREP), ("0", 0, PREP)):
    add(f"P sourced case: equivalent_static {tag}", "preview", b, want, inv=[S(M("load_cases", 0, "equivalent_static"), v)])
for tag, v in (("null", None), ("{}", {}), ("false", False)):
    add(f"P sourced case: analysis_state {tag}", "preview", b, PREP, inv=[S(M("load_cases", 0, "analysis_state"), v)])
add("P sourced case: a case-level pressure (not read)", "preview", b, OK, inv=[S(M("load_cases", 0, "pressure"), {"value": 1, "unit": "Pa"})])
add("P sourced case: a case-level pressure null", "preview", b, OK, inv=[S(M("load_cases", 0, "pressure"), None)])
add("P sourced case: 0.3.0 legacy, pressure_regions []", "preview", b, OK, inv=[S(M("schema_version"), "0.3.0"), S(M("pressure_contract"), LEGACY), S(M("load_cases", 0, "pressure_regions"), [])])
add("P sourced case: second case's analysis_state null", "preview", "two_case_synthetic", PREP, inv=[S(M("load_cases", 1, "analysis_state"), None)])
add("P S-1: preview preparation hashed with DEF-E's H", "preview", b, "G1 RECEIPT_MISMATCH", hash=DEF_E)
add("P S-1: preview preparation hashed with an alternate H", "preview", b, "G1 RECEIPT_MISMATCH", hash=ALT)
add("P S-1: preview preparation hashed with PTABLE's sha", "preview", b, "G1 RECEIPT_MISMATCH", hash=PTABLE)
add("P G0: preview attempt's definition_id the exact id (DEF-O H)", "preview", b, "G0 SOURCE_PRODUCER_CONTRACT_UNSUPPORTED", edits=[S(RB("product_attempts", 0, "definition_id"), "RP-PREPARED-EXACT-DUAL-v1")])
add("P G0: preview identity, exact profile", "preview", b, "G0 SOURCE_PRODUCER_CONTRACT_UNSUPPORTED", edits=[S(["formulation_basis", "profile_id"], "exact_straight_retained_w1a_v2")])
# Exact route.
for b in ("ordinary_prepared_synthetic", "m3x_sparse_interactive"):
    for tag, v in (("false", False), ("0", 0), ("empty string", ""), ("[]", []), ("{}", {}), ("null", None)):
        add(f"X namespace: pressure_contract {tag}", "exact", b, INV, inv=[S(M("pressure_contract"), v)])
    add("X namespace: contract keys reordered", "exact", b, OK, inv=[S(M("pressure_contract"), {"mode": "exact_straight_pressure_v2", "version": "2.0.0"})])
    add("X namespace: contract version number 2", "exact", b, INV, inv=[S(M("pressure_contract"), {"version": 2, "mode": "exact_straight_pressure_v2"})])
    add("X namespace: schema_version '0.3.0 '", "exact", b, INV, inv=[S(M("schema_version"), "0.3.0 ")])
    add("X namespace: schema 0.2.0 with the exact contract", "exact", b, INV, inv=[S(M("schema_version"), "0.2.0")])
    add("X namespace: combinations null", "exact", b, INV, inv=[S(M("combinations"), None)])
    add("X namespace: components null", "exact", b, INV, inv=[S(M("components"), None)])
    add("X namespace: reference_configurations null", "exact", b, INV, inv=[S(M("reference_configurations"), None)])
    for tag, v in (("null", None), ("{}", {}), ("false", False)):
        add(f"X sourced case: analysis_state {tag}", "exact", b, PREP, inv=[S(M("load_cases", 0, "analysis_state"), v)])
    for tag, v in (("{}", {}), ("empty string", ""), ("false", False), ("0", 0)):
        add(f"X sourced case: pressure_regions {tag}", "exact", b, PREP, inv=[S(M("load_cases", 0, "pressure_regions"), v)])
    add("X sourced case: equivalent_static null", "exact", b, OK, inv=[S(M("load_cases", 0, "equivalent_static"), None)])
    add("X sourced case: equivalent_static false", "exact", b, PREP, inv=[S(M("load_cases", 0, "equivalent_static"), False)])
    add("X sourced case: a case-level pressure (not read)", "exact", b, OK, inv=[S(M("load_cases", 0, "pressure"), {"value": 1, "unit": "Pa"})])
    add("X S-1: hashed with an alternate H", "exact", b, "G1 RECEIPT_MISMATCH", hash=ALT)
    add("X S-1: hashed with PTABLE's sha", "exact", b, "G1 RECEIPT_MISMATCH", hash=PTABLE)
    add("X S-1: hashed with the exact table's sha", "exact", b, "G1 RECEIPT_MISMATCH", hash="c4987e874889645ac315b5f55f58690082ad5e7745527f20e3e316efa3e70a3d")
    add("X G0: attempt definition_id ordinary, hashed with DEF-O's H", "exact", b, "G0 SOURCE_PRODUCER_CONTRACT_UNSUPPORTED", edits=[S(RB("product_attempts", 0, "definition_id"), "RP-PREPARED-ORDINARY-DUAL-v1")], hash=DEF_O)
    add("X G0: receipt_version 1.0 (float)", "exact", b, OK, edits=[S(RB("receipt_version"), 1.0)])
    add("X G0: receipt_version '1'", "exact", b, "G0 SOURCE_PRODUCER_CONTRACT_UNSUPPORTED", edits=[S(RB("receipt_version"), "1")])
    add("X G8 step 3: modulus_basis_temperature on the case", "exact", b, PREP, inv=[S(M("load_cases", 0, "modulus_basis_temperature"), {"value": 300, "unit": "K"})])
    add("X G8 step 4: authored shear_modulus with an unknown unit", "exact", b, "?", inv=[S(M("materials", 0, "shear_modulus"), {"value": 77, "unit": "furlong"})])
    add("X G8 step 4: authored shear_modulus removed", "exact", b, "?", inv=[R(M("materials", 0, "shear_modulus"))])
    add("X G8 step 4: authored shear_modulus a string value", "exact", b, "?", inv=[S(M("materials", 0, "shear_modulus"), {"value": "77e9", "unit": "Pa"})])
    add("X G8 step 4: authored thermal_expansion_coefficient with an unknown unit", "exact", b, "?", inv=[S(M("materials", 0, "thermal_expansion_coefficient"), {"value": 1.2e-5, "unit": "bogus"})])
    add("X G8 step 4: a temperature point with an unknown-unit modulus", "exact", b, "?", inv=[S(M("materials", 0, "temperature_points"), [{"id": "point:x", "temperature": {"value": 300, "unit": "K"}, "elastic_modulus": {"value": 1, "unit": "bogus"}, "poisson_ratio": {"value": 0.3, "unit": "1"}}])])
    add("X G8 step 4: poisson_ratio value true", "exact", b, PREP, inv=[S(M("materials", 0, "poisson_ratio", "value"), True)])
    add("X G8: an exact_cases entry for a case not in the invocation", "exact", b, "?", edits=[S(CE(1), "COPY0")])
    add("X G8 N-6: an entry's G_pa a string", "exact", b, "?", edits=[S(CE(0, "pipe_materials", 0, "G_pa"), "STR")])
# G5b's order on the exact route (two selected cases): shared G5b over every case, then the evidence (DESIGN §6.2's G5b row).
b = "two_case_synthetic"
sec = EXACT[b][0]["contract_evidence"]["exact_cases"][0]["pipe_sections"][0]["As_m2"]
add("X G5b control: case 0's evidence As_m2 one ulp", "exact", b, "G5b SECTION_MISMATCH", edits=[S(CE(0, "pipe_sections", 0, "As_m2"), ulp(sec))])
add("X G5b control: case 1's body_scales force one ulp", "exact", b, "G5b SCALE_MISMATCH", edits=[S(RB("cases", 1, "selection", "body_scales", 0, "force"), "0000000000000001")])
add("X G5b order: case 0's evidence As_m2 and case 1's body_scales force", "exact", b, "G5b SCALE_MISMATCH", edits=[S(CE(0, "pipe_sections", 0, "As_m2"), ulp(sec)), S(RB("cases", 1, "selection", "body_scales", 0, "force"), "0000000000000001")])
add("X G5b order: case 0's evidence As_m2 and case 1's section term area", "exact", b, "G5b SECTION_MISMATCH", edits=[S(CE(0, "pipe_sections", 0, "As_m2"), ulp(sec)), S(RB("cases", 1, "selection", "section_terms", 0, "area"), "3f00000000000000")])
# Controls: the Rust reader's own shapes, re-materialized.
controls = [("base", "ordinary_prepared_synthetic", {}), ("12 owner entry's As_m2 one ulp", "ordinary_prepared_synthetic", {"edits": [S(CE(0, "pipe_sections", 0, "As_m2"), ulp(EXACT["ordinary_prepared_synthetic"][0]["contract_evidence"]["exact_cases"][0]["pipe_sections"][0]["As_m2"]))]}),
            ("19 invocation contract -> legacy 1.0.0", "ordinary_prepared_synthetic", {"inv": [S(M("pressure_contract"), LEGACY)]}),
            ("27 authored nu changed in the invocation", "m3x_sparse_interactive", {"inv": [S(M("materials", 0, "poisson_ratio", "value"), ulp(EXACT["m3x_sparse_interactive"][1]["request"]["model"]["materials"][0]["poisson_ratio"]["value"]))]})]
ctl = []
for name, base, kw in controls:
    s, i = materialize({"route": "exact", "base": base, **kw})
    d = next(x for x in dump if x["name"] == name and x["base"] == base)
    ctl.append((name, base, s == d["source"] and i == d["invocation"]))
lines = []
for p in probes:
    q = copy.deepcopy(p)
    for e in q.get("edits", []):
        if e.get("value") == "COPY0": e["value"] = copy.deepcopy(EXACT[p["base"]][0]["contract_evidence"]["exact_cases"][0]); e["value"]["load_case_id"] = "case:rv120-other"
        if e.get("value") == "STR": e["value"] = str(EXACT[p["base"]][0]["contract_evidence"]["exact_cases"][0]["pipe_materials"][0]["G_pa"])
    s, i = materialize(q)
    lines.append({"name": f"{p['name']} [{p['base']}]", "want": p["want"], "source": s, "invocation": i})
with open(out_path, "w") as f:
    for l in lines: f.write(json.dumps(l) + "\n")
print(json.dumps({"probes": len(lines), "controls": ctl}))
