"""Synthetic reader controls, not produced receipts or native Current evidence."""
import json
import math
import struct
from copy import deepcopy
from fractions import Fraction
from pathlib import Path

import pytest
from core.analysis_runs import retained_precision as rp

ROOT = Path(__file__).resolve().parents[1]


def exact(word):
    word = int(word, 16)
    exponent, significand = (word >> 52) & 2047, word & ((1 << 52) - 1)
    assert exponent != 2047
    if exponent:
        significand |= 1 << 52
    power = exponent - 1075 if exponent else -1074
    q = Fraction(significand) * (Fraction(2) ** power)
    return -q if word >> 63 else q


def assert_least_upper(result, target):
    assert math.isfinite(result) and result >= 0
    value = exact(rp.bits(result))
    assert value >= target
    if result:
        predecessor = struct.unpack(">d", (int(rp.bits(result), 16) - 1).to_bytes(8, "big"))[0]
        assert exact(rp.bits(predecessor)) < target


def corpus():
    return json.loads((ROOT / "fixtures/results/retained_precision_cases.json").read_text())


def test_small_bounds_against_independent_fraction_oracle():
    for row in corpus()["arithmetic"]["small_bounds"]:
        n, s = rp.from_bits(row["value"]), rp.from_bits(row["scale"])
        result = rp.absolute_bound(n, s)
        assert rp.bits(result) == row["expected"], row["id"]
        target = exact(row["b0"]) + exact(row["rounding"]) + Fraction(1, 1 << 1074)
        assert_least_upper(result, target)


def test_products_against_exact_oracle():
    for row in corpus()["arithmetic"]["products"]:
        a, b = rp.from_bits(row["a"]), rp.from_bits(row["b"])
        target = exact(row["a"]) * exact(row["b"])
        if row["expected"] is None:
            with pytest.raises(ValueError): rp.upward_product(a, b)
        else:
            result = rp.upward_product(a, b)
            assert rp.bits(result) == row["expected"]
            assert_least_upper(result, target)


def test_helper_input_rejection_and_far_separated_tail():
    for value in [math.nan, math.inf, -math.inf, -1.0]:
        with pytest.raises(ValueError): rp.upward_product(value, 1.0)
    assert rp.bits(rp.upward_product(-0.0, 1.0)) == "0000000000000000"
    result = rp.upward_small_sum(1.0, math.ldexp(1.0, -1074))
    assert rp.bits(result) == "3ff0000000000001"
    assert_least_upper(result, Fraction(1) + Fraction(2, 1 << 1074))


def test_all_bound_entrypoints_canonicalize_accepted_zero():
    for value in (0.0, -0.0, 1.0, -1.0):
        for scale in (0.0, -0.0):
            assert rp.bits(rp.absolute_bound(value, scale)) == "0000000000000000"
    for power in (53, 64):
        assert rp.bits(rp._scaled_component(-0.0, power)) == "0000000000000000"
    assert rp.bits(rp.upward_small_sum(-0.0, -0.0)) == "0000000000000001"
    for value in (math.nan, math.inf, -math.inf):
        with pytest.raises(ValueError): rp.absolute_bound(value, 0.0)
        with pytest.raises(ValueError): rp.absolute_bound(0.0, value)

def _apply_edits(value, edits):
    for edit in edits:
        parent = value
        for part in edit["path"][:-1]:
            parent = parent[part]
        key = edit["path"][-1]
        if edit["op"] == "remove":
            del parent[key]
        else:
            parent[key] = deepcopy(edit["value"])


def apply_mutation(base, mutation):
    value = deepcopy(base)
    _apply_edits(value, mutation["edits"])
    if mutation.get("_invocation_digest") is not None:
        value["retained_precision"]["body"]["invocation"]["value"] = mutation["_invocation_digest"]
    # D11: the shared format admits only rehash "all". Snapshot 07: when an entry removes the
    # receipt or its body (settled reading 2, a G0 pin), there is nothing to rehash.
    assert mutation["rehash"] == "all", "the shared format admits only rehash: all"
    receipt = value.get("retained_precision")
    if isinstance(receipt, dict) and isinstance(receipt.get("body"), dict):
        body = receipt["body"]
        for source in body["sources"]:
            preparation = source["preparation"]
            if preparation is not None:
                attempt = body["product_attempts"][preparation["attempt_ref"]]
                if all(m["result"]["kind"] == "prepared" for m in attempt["preparation"]["members"]):
                    preparation["sha256"] = rp._hash("retained_precision_preparation_v1", rp._preparation_payload(attempt))
        for case in body["cases"]:
            if case["status"] == "selected":
                case["source_identity_sha256"] = rp._source_hash(body["sources"][case["source_ref"]])
        body["publication_sha256"] = rp._hash("retained_precision_publication_mp_v2", {k:v for k,v in value.items() if k != "retained_precision"})
        receipt["receipt_sha256"] = rp._hash("retained_precision_receipt_mp_v2", body)
    return value


def apply_entry(fixture, entry):
    """Shared-corpus entry semantics (SHARED_SNAPSHOT_06C format): (1) apply `edits` to a copy
    of the base source; (2) apply `invocation_edits` (same edit grammar; absent means none) to a
    copy of the base invocation; (3) when any invocation edit exists, set
    retained_precision.body.invocation.value = H(source_blocks_invocation_v1, edited invocation);
    (4) rehash per `rehash`; then validate the edited source against the edited invocation."""
    invocation = deepcopy(fixture["invocation"])
    invocation_edits = entry.get("invocation_edits") or []
    _apply_edits(invocation, invocation_edits)
    digest = rp._hash("source_blocks_invocation_v1", invocation) if invocation_edits else None
    return apply_mutation(fixture["source"], dict(entry, _invocation_digest=digest)), invocation


def test_complete_synthetic_draft_control_is_not_qualification():
    from copy import deepcopy
    for fixture in corpus()["cases"]:
        source, invocation = deepcopy(fixture["source"]), deepcopy(fixture["invocation"])
        result = rp._validate_draft(source, invocation)
        assert result["classifications"] == fixture["expected_classifications"]
        assert result["invocation_bound"]
        assert result["numerical_eligible"] is False
        assert result["standing"] == "needs_recompute"
        assert source == fixture["source"] and invocation == fixture["invocation"]
        assert rp._validate_draft(source)["numerical_eligible"] is False
        with pytest.raises(rp.RetainedPrecisionError) as error:
            rp.validate_retained_precision(source, invocation)
        assert error.value.gate == "G0"
        assert error.value.code == "SOURCE_PRODUCER_CONTRACT_UNSUPPORTED"


@pytest.mark.parametrize("mutation", corpus()["mutations"], ids=lambda x:x["id"])
def test_shared_draft_first_failure_controls(mutation):
    fixture = next(f for f in corpus()["cases"] if f["id"] == mutation["base"])
    source, invocation = apply_entry(fixture, mutation)
    with pytest.raises(rp.RetainedPrecisionError) as error:
        rp._validate_draft(source, invocation)
    assert {"gate":error.value.gate,"code":error.value.code} == mutation["expected"]


def test_old_operational_error_is_retained_independently_of_new_ready():
    """Reader logic only: a receipt shape whose old operational result is refused while
    the new result is ready must still validate with unchanged classifications. No native
    trigger is established for this coefficient_range refusal on ordinary-magnitude
    operands; this is not a native-faithful producer control (retired from the shared
    corpus as 05c)."""
    fixture = corpus()["cases"][0]
    source = apply_mutation(fixture["source"], {"edits":[{
        "path":["retained_precision","body","product_attempts",0,"operational","old",0,"result"],
        "op":"set","value":{"kind":"refused","error":{"kind":"coefficient_range","coefficient":"torsional_stiffness","operation":"mul"}}
    }], "rehash":"all"})
    result = rp._validate_draft(source, fixture["invocation"])
    assert result["classifications"] == fixture["expected_classifications"]
    assert result["numerical_eligible"] is False


def test_native_source_encoding_domain_and_load_separation():
    from copy import deepcopy
    source = deepcopy(corpus()["cases"][0]["source"]["retained_precision"]["body"]["sources"][0])
    raw, stiffness = rp._native_source_encoding(source, True), rp._native_source_encoding(source, False)
    assert raw[:10] == b"K4SRC\x01\x02\x00\x00\x00"
    assert stiffness[:10] == b"K4STF\x01\x02\x00\x00\x00"
    assert (len(raw), len(stiffness)) == (552, 188)
    source["nodal_terms"][0]["source_id"] = "load:\u03b1"
    assert rp._native_source_encoding(source, True) != raw
    assert rp._native_source_encoding(source, False) == stiffness


COVERAGE = ["retained_precision", "body", "product_attempts", 0, "proof", "summary_coverage"]
SELECTION = ["retained_precision", "body", "cases", 0, "selection"]
VERIFICATION = ["retained_precision", "body", "cases", 0, "run", "records", 1, "verification"]
ZERO = "0000000000000000"


def _set(path, value):
    return {"path": path, "op": "set", "value": value}


@pytest.mark.parametrize("entry", corpus().get("must_pass", []), ids=lambda x: x["id"])
def test_shared_publicly_consistent_attestations_must_pass(entry):
    """I57 s4/s5: public coverage rules are necessary conditions only. These shared
    rewrites keep every public relation, so readers must accept them; only producer
    custody/replay can catch such attested private flags."""
    fixture = next(f for f in corpus()["cases"] if f["id"] == entry["base"])
    assert entry["expected"] == "pass"
    source, invocation = apply_entry(fixture, entry)
    result = rp._validate_draft(source, invocation)
    assert result["classifications"] == fixture["expected_classifications"]
    assert result["numerical_eligible"] is False


def _layout_index(source, predicate):
    layout = source["retained_precision"]["body"]["sources"][0]["layout"]
    return next(i for i, row in enumerate(layout) if predicate(row))


@pytest.mark.parametrize("change", ["force_row_input_derived", "constrained_displacement_not_input_derived", "nonzero_prescription"])
def test_g5a_rederives_canonical_layout_and_zero_prescription(change):
    """Python-only (not shared corpus): D is rederived from source maps, never trusted."""
    fixture = corpus()["cases"][0]
    source = fixture["source"]
    layout = ["retained_precision", "body", "sources", 0, "layout"]
    if change == "force_row_input_derived":
        index = _layout_index(source, lambda r: r["kind"] == "force" and r["quantity"]["tag"] == "reaction")
        edits = [_set(layout + [index, "input_derived"], True)]
    elif change == "constrained_displacement_not_input_derived":
        index = _layout_index(source, lambda r: r["input_derived"])
        edits = [_set(layout + [index, "input_derived"], False)]
    else:
        edits = [_set(["retained_precision", "body", "sources", 0, "constraints", 0, "value"], "3ff0000000000000")]
    with pytest.raises(rp.RetainedPrecisionError) as error:
        rp._validate_draft(apply_mutation(source, {"edits": edits, "rehash": "all"}), fixture["invocation"])
    assert (error.value.gate, error.value.code) == ("G5a", "RETAINED_PRECISION_SCALE_MISMATCH")


def test_p512_floor_phi_follows_native_rounding():
    """C1 G5b 'same E/e-hat/Phi at p512' (verify.rs:321-376). Python-only until the
    C1b p512 ladder base exists: Phi = fl-up(2^-438 * e-hat), e-hat uncoupled at L=0."""
    assert rp._phi_512(0.0) == 0.0
    assert rp._phi_512(1.0) == math.ldexp(1.0, -438)
    # 2^-1038 * (1 + 2^-52) rounds to 2^-1038 in the subnormal range; nearest * 2^438 is
    # below e-hat, so the native next-up applies.
    assert rp._phi_512(math.ldexp(1.0 + 2.0 ** -52, -600)) == math.ldexp(1.0, -1038) + math.ldexp(1.0, -1074)
    assert rp._e_hat([3.0, 0.0], 0.0) == [3.0, 0.0]
    assert rp._e_hat([3.0, 0.0], 2.0) == [3.0, 6.0]
    assert rp._e_hat([0.0, 8.0], 2.0) == [4.0, 8.0]


def _raises(fn, gate, code):
    with pytest.raises(rp.RetainedPrecisionError) as error:
        fn()
    assert (error.value.gate, error.value.code) == (gate, "RETAINED_PRECISION_" + code)


def _fail_g5(ok, code="ATTEMPT_MISMATCH"):
    rp._need(ok, "G5", code)


def test_schedule_replay_terminal_branches_reader_logic():
    """Python-only reader-logic controls for checklist N8-N11 branches that have no native-faithful
    shared base yet (Ceiling, idle/pre-schedule runs, verification-pass terminal)."""
    selected = deepcopy(corpus()["cases"][0]["source"]["retained_precision"]["body"]["cases"][0]["run"])
    idle = dict(selected, records=[], attempts=[], case_charge=0, invocation_increment=0,
                kernel_terminal={"kind": "unresolved", "reason": {"space": "unresolved", "tag": "budget", "scope": "invocation"}})
    rp._g5_schedule(idle, [], [], _fail_g5)
    _raises(lambda: rp._g5_schedule(dict(idle, kernel_terminal={"kind": "selected", "reason": None}), [], [], _fail_g5), "G5", "ATTEMPT_MISMATCH")
    # N10 (adaptive.rs:4994-5002): exhaustion gives Budget(invocation) and requires
    # invocation_before >= the invocation limit; a WorkAccounting idle run is never emitted
    # (C1:66-68) and is rejected.
    body = deepcopy(corpus()["cases"][0]["source"]["retained_precision"]["body"])
    entry = dict(idle, origin=dict(idle["origin"], group=None))
    fault = {"kind": "unresolved", "reason": {"space": "unresolved", "tag": "work_accounting", "fault": "overflow"}}
    _raises(lambda: rp._g5_schedule(dict(entry, kernel_terminal=fault), [], [], _fail_g5, body), "G5", "ATTEMPT_MISMATCH")
    _raises(lambda: rp._g5_schedule(entry, [], [], _fail_g5, body), "G5", "ATTEMPT_MISMATCH")
    rp._g5_schedule(dict(entry, invocation_before=body["work"]["invocation_limit"]), [], [], _fail_g5, body)
    # A rejected candidate at p128 must hand its verification to a reused p256 candidate.
    rejected = deepcopy(selected)
    reason = {"space": "attempt", "tag": "stop_rule", "quantity": {"tag": "displacement", "dof": {"node": 1, "component": "UX"}}, "body": 0, "kind": "translation"}
    rejected["attempts"][0]["outcome"] = rejected["records"][0]["outcome"] = {"kind": "rejected", "reason": reason}
    rejected["records"][1]["outcome"] = {"kind": "solved"}
    rejected["kernel_terminal"] = {"kind": "unresolved", "reason": {"space": "unresolved", "tag": "ceiling"}}
    _raises(lambda: rp._g5_schedule(rejected, rejected["records"], rejected["attempts"], _fail_g5), "G5", "ATTEMPT_MISMATCH")
    # A non-escalating verification-pass failure is terminal (no next attempt, non-selected terminal).
    vfail = deepcopy(selected)
    stop = {"space": "attempt", "tag": "stop", "stop": {"space": "stop", "tag": "structure"}}
    vfail["attempts"][0]["outcome"] = vfail["records"][0]["outcome"] = {"kind": "rejected", "reason": {"space": "attempt", "tag": "verification_failed"}}
    vfail["attempts"][0]["verification"] = {"record": 1, "precision": 256, "phase": "failed", "reason": stop}
    vfail["records"][1]["outcome"] = {"kind": "failed", "reason": stop}
    vfail["kernel_terminal"] = {"kind": "refused", "reason": {"space": "refusal", "tag": "structure"}}
    rp._g5_schedule(vfail, vfail["records"], vfail["attempts"], _fail_g5)
    _raises(lambda: rp._g5_schedule(dict(vfail, kernel_terminal={"kind": "selected", "reason": None}), vfail["records"], vfail["attempts"], _fail_g5), "G5", "ATTEMPT_MISMATCH")
    # Ceiling (N8): the reused p512 candidate is rejected and its p1024 verification only solved.
    ladder = deepcopy(next(f for f in corpus()["cases"] if f["id"] == "p512_ladder_synthetic")["source"]["retained_precision"]["body"]["cases"][0]["run"])
    ladder["attempts"][2]["outcome"] = ladder["records"][2]["outcome"] = {"kind": "rejected", "reason": reason}
    ladder["records"][3]["outcome"] = {"kind": "solved"}
    ladder["kernel_terminal"] = {"kind": "unresolved", "reason": {"space": "unresolved", "tag": "ceiling"}}
    rp._g5_schedule(ladder, ladder["records"], ladder["attempts"], _fail_g5)
    _raises(lambda: rp._g5_schedule(dict(ladder, kernel_terminal={"kind": "refused", "reason": {"space": "refusal", "tag": "structure"}}), ladder["records"], ladder["attempts"], _fail_g5), "G5", "ATTEMPT_MISMATCH")


def test_source_decline_relation_reader_logic():
    """Python-only reader-logic control for checklist O5 (no native-faithful source_decline base yet)."""
    fixture = next(f for f in corpus()["cases"] if f["id"] == "two_case_preparation_failure_synthetic")
    body = deepcopy(fixture["source"]["retained_precision"]["body"])
    diags = fixture["source"]["diagnostics"]
    decline = {"input_owner": {"case_index": 1, "case_id": "case:unavailable-row", "material_basis_ref": 0},
               "constructor_counts": {"nodes": 2, "members": 1, "springs": 0, "constraints": 6, "nodal_terms": 6, "stations": 3, "supports": 1, "id_utf8_bytes": 0, "directional_springs": 0},
               "error": {"tag": "no_nodes"}}
    body["cases"][1]["source_decline"] = decline
    quality = fixture["source"]["numerical_quality"]["cases"]
    rp._g5_ordinary(body, body["cases"], diags, quality)
    body["cases"][1]["source_decline"] = dict(decline, input_owner=dict(decline["input_owner"], case_index=0))
    _raises(lambda: rp._g5_ordinary(body, body["cases"], diags, quality), "G5", "ATTEMPT_MISMATCH")


# RV78 PROBES.json (review evidence, record e2f7fe8b34): exact edits on 06d bases; `expected` is RV78's
# contract reading, each confirmed against rulings D1-D16 and checkpoint A.
RV78_PROBES_JSON = r'''[{"id":"R1a_execution_order_swapped","base":"two_case_synthetic","edits":[{"path":["retained_precision","body","work","execution_order"],"op":"set","value":[{"kind":"case","index":1},{"kind":"case","index":0}]}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R1b_run_id_not_position","base":"two_case_synthetic","edits":[{"path":["retained_precision","body","cases",1,"run","id"],"op":"set","value":5},{"path":["retained_precision","body","calls",0,"run_refs"],"op":"set","value":[0,5]}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R2_old_members_reordered","base":"two_body_synthetic","edits":[{"path":["retained_precision","body","product_attempts",0,"operational","old"],"op":"set","value":[{"member":1,"inputs":["0000000000000000","4014000000000000","0000000000000000","3ff0000000000000","4014000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}},{"member":0,"inputs":["0000000000000000","0000000000000000","0000000000000000","3ff0000000000000","0000000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}}]}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R3_complete_old_short_of_source","base":"two_body_synthetic","edits":[{"path":["retained_precision","body","product_attempts",0,"operational","old"],"op":"set","value":[{"member":0,"inputs":["0000000000000000","0000000000000000","0000000000000000","3ff0000000000000","0000000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}}]}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R4_unavailable_source_backref_foreign","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","sources",1,"preparation","attempt_ref"],"op":"set","value":0}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH"}},{"id":"R5_attempt_and_source_basis_not_ordinary","base":"two_case_two_groups_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"material_basis_ref"],"op":"set","value":0},{"path":["retained_precision","body","sources",1,"material_basis_ref"],"op":"set","value":0}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH"}},{"id":"R6a_native_error_with_selected_run","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"result","error"],"op":"set","value":{"kind":"native","run_ref":1}}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH"}},{"id":"R8_group_call_out_of_range","base":"two_case_synthetic","edits":[{"path":["retained_precision","body","groups",0,"call"],"op":"set","value":3}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T1_escalating_failed_verification_pass_entered","base":"verification_failure_skip_synthetic","edits":[{"path":["retained_precision","body","cases",0,"run","records",1],"op":"set","value":{"index":1,"precision":256,"role":"verification","outcome":{"kind":"failed","reason":{"space":"attempt","tag":"stop","stop":{"space":"stop","tag":"condition"}}},"residual_basis":320,"corrections":0,"pivot_margin_min":null,"rcond":null,"residual_worst":null,"gate":null,"work":{"wide_lme":1,"exact_sum_lme":0,"own_lme":1,"shared_lme":4,"stop_rule_lme":0,"verification_lme":1,"verification_shared_lme":0,"own_stages":{"formation":0,"assembly":0,"residual_formation":0,"factor":0,"condition":0,"rhs":0,"solve":0,"refinement":0,"recovery":0,"stop_rule":0,"bounded_gate":0,"scale":0,"estimate":0,"charge":0,"bound":1,"shift":0,"bounded_formation":0,"wide_formation":0,"uc":0},"shared_stages":{"formation":4,"assembly":0,"residual_formation":0,"factor":0,"condition":0,"rhs":0,"solve":0,"refinement":0,"recovery":0,"stop_rule":0,"bounded_gate":0,"scale":0,"estimate":0,"charge":0,"bound":0,"shift":0,"bounded_formation":0,"wide_formation":0,"uc":0},"shared_built_here":true,"verification_shared_built_here":false},"storage":{"pattern_entries":144,"profile_entries":21,"limbs_per_entry":4},"verification":null,"bound_refusals":[],"shared_build_ref":1,"verification_shared_build_ref":null}},{"path":["retained_precision","body","cases",0,"run","attempts",0],"op":"set","value":{"precision":128,"candidate_record":0,"origin":{"kind":"fresh"},"verification":{"record":1,"precision":256,"phase":"failed","reason":{"space":"attempt","tag":"stop","stop":{"space":"stop","tag":"condition"}}},"outcome":{"kind":"rejected","reason":{"space":"attempt","tag":"verification_failed"}},"charges":[{"record":0,"part":"solve_and_verification"},{"record":0,"part":"candidate_stop"},{"record":1,"part":"solve_and_verification"}],"case_charge":9,"invocation_increment":9}},{"path":["retained_precision","body","cases",0,"run","case_charge"],"op":"set","value":37},{"path":["retained_precision","body","cases",0,"run","invocation_increment"],"op":"set","value":37},{"path":["retained_precision","body","cases",0,"run","invocation_after"],"op":"set","value":37},{"path":["retained_precision","body","calls",0,"invocation_after"],"op":"set","value":37},{"path":["retained_precision","body","work","charged"],"op":"set","value":37}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T2_stop_rule_quantity_other_body","base":"p512_ladder_synthetic","edits":[{"path":["retained_precision","body","cases",0,"run","records",0,"outcome","reason","quantity"],"op":"set","value":{"tag":"displacement","dof":{"node":3,"component":"UX"}}},{"path":["retained_precision","body","cases",0,"run","attempts",0,"outcome","reason","quantity"],"op":"set","value":{"tag":"displacement","dof":{"node":3,"component":"UX"}}}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T3_candidate_record_with_verification","base":"ordinary_prepared_synthetic","edits":[{"path":["retained_precision","body","cases",0,"run","records",0,"verification"],"op":"set","value":{"resolution":[{"body":0,"force":"426d1a94a2000000","moment":"426d1a94a2000000"}],"theta":[{"body":0,"value":"0000000000000000"}],"bound":[{"body":0,"value":"3ff0000000000000"}],"data_blocks":1,"shift_factorizations":0,"g_max":0,"uc_missing":null,"g_violation":null}}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T4a_ordinary_diagnostic_ref_duplicate","base":"ordinary_prepared_synthetic","edits":[{"path":["retained_precision","body","ordinary_attempts",0,"diagnostic_refs"],"op":"set","value":["diagnostic:numerical-integrity:case:six-component-load","diagnostic:numerical-integrity:case:six-component-load"]}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T4b_ordinary_diagnostic_ref_dangling","base":"ordinary_prepared_synthetic","edits":[{"path":["retained_precision","body","ordinary_attempts",0,"diagnostic_refs"],"op":"set","value":["diagnostic:numerical-integrity:case:six-component-load","diagnostic:rv78:absent"]}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T4c_source_identity_stale_receipt_rehashed","base":"ordinary_prepared_synthetic","edits":[],"invocation_edits":[],"post_rehash_edits":[{"path":["retained_precision","body","cases",0,"source_identity_sha256"],"op":"set","value":"0000000000000000000000000000000000000000000000000000000000000000"}],"expected":{"gate":"G1","code":"RETAINED_PRECISION_RECEIPT_MISMATCH"}},{"id":"T4d_ordinary_dangling_plus_adapter_fault","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","ordinary_attempts",1,"diagnostic_refs"],"op":"set","value":["diagnostic:numerical-integrity:case:unavailable-row","diagnostic:rv78:absent"]},{"path":["retained_precision","body","product_attempts",1,"adapter","fault"],"op":"set","value":{"kind":"overflow","event":"map_write"}}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"R2b_unsourced_old_member_noncontiguous","base":"two_case_preparation_failure_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"operational","old",0],"op":"set","value":{"member":1,"inputs":["0000000000000000","0000000000000000","0000000000000000","3ff0000000000000","0000000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}}}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R3b_complete_old_longer_than_source","base":"two_body_synthetic","edits":[{"path":["retained_precision","body","product_attempts",0,"operational","old"],"op":"set","value":[{"member":0,"inputs":["0000000000000000","0000000000000000","0000000000000000","3ff0000000000000","0000000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}},{"member":1,"inputs":["0000000000000000","4014000000000000","0000000000000000","3ff0000000000000","4014000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}},{"member":2,"inputs":["0000000000000000","4014000000000000","0000000000000000","3ff0000000000000","4014000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}}]}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"B_interpolation_target_at_lower_point_equal_point_E","base":"ordinary_prepared_interpolated_material_synthetic","edits":[{"path":["retained_precision","body","material_bases",0,"selector","kelvin"],"op":"set","value":"4072c00000000000"},{"path":["retained_precision","body","material_bases",0,"materials",0,"selection","target_kelvin"],"op":"set","value":"4072c00000000000"}],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","load_cases",0,"modulus_basis_temperature"],"op":"set","value":{"value":300,"unit":"K"}}],"post_rehash_edits":[],"expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}},{"id":"B_interpolation_target_below_range_equal_point_E","base":"ordinary_prepared_interpolated_material_synthetic","edits":[{"path":["retained_precision","body","material_bases",0,"selector","kelvin"],"op":"set","value":"4072b00000000000"},{"path":["retained_precision","body","material_bases",0,"materials",0,"selection","target_kelvin"],"op":"set","value":"4072b00000000000"}],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","load_cases",0,"modulus_basis_temperature"],"op":"set","value":{"value":299,"unit":"K"}}],"post_rehash_edits":[],"expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}},{"id":"B_interpolation_target_at_upper_point_equal_point_E","base":"ordinary_prepared_interpolated_material_synthetic","edits":[{"path":["retained_precision","body","material_bases",0,"selector","kelvin"],"op":"set","value":"4073600000000000"},{"path":["retained_precision","body","material_bases",0,"materials",0,"selection","target_kelvin"],"op":"set","value":"4073600000000000"}],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","load_cases",0,"modulus_basis_temperature"],"op":"set","value":{"value":310,"unit":"K"}}],"post_rehash_edits":[],"expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}},{"id":"B_interpolation_target_above_range_equal_point_E","base":"ordinary_prepared_interpolated_material_synthetic","edits":[{"path":["retained_precision","body","material_bases",0,"selector","kelvin"],"op":"set","value":"4073700000000000"},{"path":["retained_precision","body","material_bases",0,"materials",0,"selection","target_kelvin"],"op":"set","value":"4073700000000000"}],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","load_cases",0,"modulus_basis_temperature"],"op":"set","value":{"value":311,"unit":"K"}}],"post_rehash_edits":[],"expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}},{"id":"B_section_accounting_exact_status","base":"two_case_preparation_failure_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"preparation","members"],"op":"set","value":[{"member":0,"old_source":["42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ed61aa4872838bf","3ed61aa4872838bf","3ee61aa4872838c0"],"old_facts":["3fbeb851eb851eb8","3f847ae147ae147b","3f6c4f3caf32fd23","3ed61aa4872838bf","3ee61aa4872838c0","3f17066b621f3b1c","3faeb851eb851eb8"],"result":{"kind":"refused","error":{"kind":"accounting"}},"work":{"numeric":{"wide_lme":{"kind":"exact","value":0},"exact_sum_lme":{"kind":"exact","value":0},"entries":[{"kind":"exact","value":2},{"kind":"exact","value":4},{"kind":"exact","value":11},{"kind":"exact","value":2},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0}],"f64_arithmetic":{"kind":"exact","value":0},"sticky_status":"exact"},"initialized_endpoints":{"kind":"exact","value":27},"conversions":{"kind":"exact","value":0},"checks":{"kind":"exact","value":0},"endpoint_assignments":{"kind":"exact","value":0},"layout_bytes":[0,0,0,0,0,0,0,0]},"conversions":[]}]},{"path":["retained_precision","body","product_attempts",1,"result"],"op":"set","value":{"kind":"unavailable","error":{"kind":"preparation","capture":{"kind":"association","detail":"annulus preparation refused"},"section":{"kind":"accounting"}}}},{"path":["retained_precision","body","product_attempts",1,"adapter","fault"],"op":"set","value":null}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_WORK_MISMATCH"}},{"id":"B_control_equal_point_E_bracketed","base":"ordinary_prepared_interpolated_material_synthetic","edits":[],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}}],"post_rehash_edits":[],"expected":"pass"},{"id":"Q1_nested_stop_work_accounting_exact_status","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"result"],"op":"set","value":{"kind":"unavailable","error":{"kind":"proof","cause":{"kind":"numeric","cause":{"kind":"arithmetic","cause":{"space":"stop","tag":"work_accounting","fault":"overflow"}}}}}},{"path":["retained_precision","body","product_attempts",1,"adapter","fault"],"op":"set","value":null},{"path":["retained_precision","body","product_attempts",1,"proof","summary_coverage"],"op":"set","value":null},{"path":["retained_precision","body","product_attempts",1,"stages"],"op":"set","value":{"preparation":"completed","native":"completed","proof_start":"completed","projection":"completed","maxima":"completed","values":"completed","aliases":"completed","certificate":"failed","observables":"not_entered","g5a":"not_entered"}},{"path":["retained_precision","body","product_attempts",1,"proof","checks"],"op":"set","value":{"certificate":{"kind":"failed","error":{"kind":"proof","cause":{"kind":"numeric","cause":{"kind":"arithmetic","cause":{"space":"stop","tag":"work_accounting","fault":"overflow"}}}}},"observables":{"kind":"not_entered"},"g5a":{"kind":"not_entered"}}}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_WORK_MISMATCH"}},{"id":"Q2_view_work_fault_exact_status","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"result"],"op":"set","value":{"kind":"unavailable","error":{"kind":"proof","cause":{"kind":"native_source","cause":{"kind":"view","issue":{"kind":"work","fault":"overflow"}}}}}},{"path":["retained_precision","body","product_attempts",1,"adapter","fault"],"op":"set","value":null},{"path":["retained_precision","body","product_attempts",1,"proof","summary_coverage"],"op":"set","value":null},{"path":["retained_precision","body","product_attempts",1,"proof","lanes"],"op":"set","value":[{"law":"admitted_k","state":"completed","error":null,"work":{"numeric":{"wide_lme":{"kind":"exact","value":0},"exact_sum_lme":{"kind":"exact","value":0},"entries":[{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0}],"f64_arithmetic":{"kind":"exact","value":0},"sticky_status":"exact"},"point_lme":{"kind":"exact","value":0},"view":{"visits":{"kind":"exact","value":0},"f64_operations":{"kind":"exact","value":0},"prescribed_capacity":0,"data_capacity":0},"correction":{"cast_lme":{"kind":"exact","value":0},"factor_lme":{"kind":"exact","value":0},"visits":{"kind":"exact","value":0},"calls":{"kind":"exact","value":0},"rhs_capacity":0,"output_capacity":0,"converted_capacity":0},"visits":{"kind":"exact","value":0},"member_builds":{"kind":"exact","value":0},"frame_builds":{"kind":"exact","value":0},"b_products":{"kind":"exact","value":0},"d_products":{"kind":"exact","value":0},"h_products":{"kind":"exact","value":0},"capacities":[],"data_capacity":0}},{"law":"annular_source","state":"failed","error":{"kind":"view","issue":{"kind":"work","fault":"overflow"}},"work":{"numeric":{"wide_lme":{"kind":"exact","value":0},"exact_sum_lme":{"kind":"exact","value":0},"entries":[{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0}],"f64_arithmetic":{"kind":"exact","value":0},"sticky_status":"exact"},"point_lme":{"kind":"exact","value":0},"view":{"visits":{"kind":"exact","value":0},"f64_operations":{"kind":"exact","value":0},"prescribed_capacity":0,"data_capacity":0},"correction":{"cast_lme":{"kind":"exact","value":0},"factor_lme":{"kind":"exact","value":0},"visits":{"kind":"exact","value":0},"calls":{"kind":"exact","value":0},"rhs_capacity":0,"output_capacity":0,"converted_capacity":0},"visits":{"kind":"exact","value":0},"member_builds":{"kind":"exact","value":0},"frame_builds":{"kind":"exact","value":0},"b_products":{"kind":"exact","value":0},"d_products":{"kind":"exact","value":0},"h_products":{"kind":"exact","value":0},"capacities":[],"data_capacity":0}}]},{"path":["retained_precision","body","product_attempts",1,"proof","projection_outcomes"],"op":"set","value":[]},{"path":["retained_precision","body","product_attempts",1,"proof","projection_conversions"],"op":"set","value":{"kind":"exact","value":0}},{"path":["retained_precision","body","product_attempts",1,"proof","completion"],"op":"set","value":{"kind":"not_entered"}},{"path":["retained_precision","body","product_attempts",1,"stages"],"op":"set","value":{"preparation":"completed","native":"completed","proof_start":"failed","projection":"not_entered","maxima":"not_entered","values":"not_entered","aliases":"not_entered","certificate":"not_entered","observables":"not_entered","g5a":"not_entered"}},{"path":["retained_precision","body","product_attempts",1,"proof","checks"],"op":"set","value":{"certificate":{"kind":"not_entered"},"observables":{"kind":"not_entered"},"g5a":{"kind":"not_entered"}}}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_WORK_MISMATCH"}},{"id":"Q4_old_operational_accounting_not_lost","base":"two_case_preparation_failure_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"operational","old",0,"result"],"op":"set","value":{"kind":"refused","error":{"kind":"accounting"}}}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_WORK_MISMATCH"}},{"id":"Q0_control_lane_source_failed_storage","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"result"],"op":"set","value":{"kind":"unavailable","error":{"kind":"proof","cause":{"kind":"native_source","cause":{"kind":"storage"}}}}},{"path":["retained_precision","body","product_attempts",1,"adapter","fault"],"op":"set","value":null},{"path":["retained_precision","body","product_attempts",1,"proof","summary_coverage"],"op":"set","value":null},{"path":["retained_precision","body","product_attempts",1,"proof","lanes"],"op":"set","value":[{"law":"admitted_k","state":"completed","error":null,"work":{"numeric":{"wide_lme":{"kind":"exact","value":0},"exact_sum_lme":{"kind":"exact","value":0},"entries":[{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0}],"f64_arithmetic":{"kind":"exact","value":0},"sticky_status":"exact"},"point_lme":{"kind":"exact","value":0},"view":{"visits":{"kind":"exact","value":0},"f64_operations":{"kind":"exact","value":0},"prescribed_capacity":0,"data_capacity":0},"correction":{"cast_lme":{"kind":"exact","value":0},"factor_lme":{"kind":"exact","value":0},"visits":{"kind":"exact","value":0},"calls":{"kind":"exact","value":0},"rhs_capacity":0,"output_capacity":0,"converted_capacity":0},"visits":{"kind":"exact","value":0},"member_builds":{"kind":"exact","value":0},"frame_builds":{"kind":"exact","value":0},"b_products":{"kind":"exact","value":0},"d_products":{"kind":"exact","value":0},"h_products":{"kind":"exact","value":0},"capacities":[],"data_capacity":0}},{"law":"annular_source","state":"failed","error":{"kind":"storage"},"work":{"numeric":{"wide_lme":{"kind":"exact","value":0},"exact_sum_lme":{"kind":"exact","value":0},"entries":[{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0},{"kind":"exact","value":0}],"f64_arithmetic":{"kind":"exact","value":0},"sticky_status":"exact"},"point_lme":{"kind":"exact","value":0},"view":{"visits":{"kind":"exact","value":0},"f64_operations":{"kind":"exact","value":0},"prescribed_capacity":0,"data_capacity":0},"correction":{"cast_lme":{"kind":"exact","value":0},"factor_lme":{"kind":"exact","value":0},"visits":{"kind":"exact","value":0},"calls":{"kind":"exact","value":0},"rhs_capacity":0,"output_capacity":0,"converted_capacity":0},"visits":{"kind":"exact","value":0},"member_builds":{"kind":"exact","value":0},"frame_builds":{"kind":"exact","value":0},"b_products":{"kind":"exact","value":0},"d_products":{"kind":"exact","value":0},"h_products":{"kind":"exact","value":0},"capacities":[],"data_capacity":0}}]},{"path":["retained_precision","body","product_attempts",1,"proof","projection_outcomes"],"op":"set","value":[]},{"path":["retained_precision","body","product_attempts",1,"proof","projection_conversions"],"op":"set","value":{"kind":"exact","value":0}},{"path":["retained_precision","body","product_attempts",1,"proof","completion"],"op":"set","value":{"kind":"not_entered"}},{"path":["retained_precision","body","product_attempts",1,"stages"],"op":"set","value":{"preparation":"completed","native":"completed","proof_start":"failed","projection":"not_entered","maxima":"not_entered","values":"not_entered","aliases":"not_entered","certificate":"not_entered","observables":"not_entered","g5a":"not_entered"}},{"path":["retained_precision","body","product_attempts",1,"proof","checks"],"op":"set","value":{"certificate":{"kind":"not_entered"},"observables":{"kind":"not_entered"},"g5a":{"kind":"not_entered"}}}],"invocation_edits":[],"post_rehash_edits":[],"expected":"pass"},{"id":"S2_unavailable_source_ref_null_instead_of_absent","base":"two_case_preparation_failure_synthetic","edits":[{"path":["retained_precision","body","cases",1,"source_ref"],"op":"set","value":null}],"invocation_edits":[],"post_rehash_edits":[],"expected":"pass"},{"id":"T4e_selected_case_ordinary_checks_passed","base":"ordinary_prepared_synthetic","edits":[{"path":["numerical_quality","cases",0,"solve_quality"],"op":"set","value":"checks_passed"},{"path":["retained_precision","body","ordinary_attempts",0,"initial","outcome"],"op":"set","value":"checks_passed"}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"layout_nonzero_prescription__k4","base":"ordinary_prepared_synthetic","edits":[{"path":["retained_precision","body","sources",0,"constraints",0,"value"],"op":"set","value":"3ff0000000000000"},{"path":["retained_precision","body","sources",0,"kernel_source_sha256"],"op":"set","value":"8cc6c03a650cfb2b94589eaf94440f41bef2a7746d1756e243fcc52d7519ef6b"}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G5a","code":"RETAINED_PRECISION_SCALE_MISMATCH"}},{"id":"maps_member_ends_swapped__k4","base":"ordinary_prepared_synthetic","edits":[{"path":["retained_precision","body","sources",0,"id_maps","members",0,"node_i"],"op":"set","value":1},{"path":["retained_precision","body","sources",0,"id_maps","members",0,"node_j"],"op":"set","value":0},{"path":["retained_precision","body","sources",0,"kernel_source_sha256"],"op":"set","value":"2e7709028c73c501c79beda97411cdf8fb92da167e8d7bfb0afd6f059bf02115"},{"path":["retained_precision","body","sources",0,"stiffness_sha256"],"op":"set","value":"389b7d25360fc930fd1521150be02208d8aae85f8750b836305f998d4691c535"},{"path":["retained_precision","body","groups",0,"stiffness_sha256"],"op":"set","value":"389b7d25360fc930fd1521150be02208d8aae85f8750b836305f998d4691c535"}],"invocation_edits":[],"post_rehash_edits":[],"expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}}]'''


# ---------------------------------------------------------------------------------------------
# Review repair 07, phase B1 (rulings D1-D16, checkpoint A, settled readings): reader-local pins.
# RV78's PROBES.json edits (06d bases) with the ruled expectation; then constructed relations.
# ---------------------------------------------------------------------------------------------
RV78_PROBES = json.loads(RV78_PROBES_JSON)
B = ["retained_precision", "body"]
A1 = B + ["product_attempts", 1]
F_BASE, P_BASE, O_BASE = "two_case_facade_after_certificate_synthetic", "two_case_preparation_failure_synthetic", "ordinary_prepared_synthetic"


def _cases():
    return {f["id"]: f for f in corpus()["cases"]}


def _validate_entry(base, edits, invocation_edits=None, post=None):
    fixture = _cases()[base]
    source, invocation = apply_entry(fixture, {"edits": edits, "invocation_edits": invocation_edits or [], "rehash": "all"})
    if post:
        _apply_edits(source, post)
        body = source["retained_precision"]["body"]
        body["publication_sha256"] = rp._hash("retained_precision_publication_mp_v2", {k: v for k, v in source.items() if k != "retained_precision"})
        source["retained_precision"]["receipt_sha256"] = rp._hash("retained_precision_receipt_mp_v2", body)
    return rp._validate_draft(source, invocation)


def _expect(expected, fn):
    if expected == "pass":
        fn()
    else:
        _raises(fn, expected[0], expected[1])


@pytest.mark.parametrize("probe", RV78_PROBES, ids=lambda p: p["id"])
def test_rv78_probe_relations(probe):
    """D1, D3-D6, D8, D16 and the strict bracket: each RV78 probe at its ruled first failure."""
    exp = probe["expected"]
    _expect(exp if exp == "pass" else (exp["gate"], exp["code"][len("RETAINED_PRECISION_"):]),
            lambda: _validate_entry(probe["base"], probe["edits"], probe["invocation_edits"], probe["post_rehash_edits"]))


def test_g0_union_d2():
    """D2 + settled readings 1-2: thresholds, canonicalization, receipt_version 1 and an absent
    receipt or body are G0 fields; a mistyped producer is a typed G0 refusal (RV79-N2)."""
    def g0(fn):
        with pytest.raises(rp.RetainedPrecisionError) as error:
            fn()
        assert (error.value.gate, error.value.code) == ("G0", "SOURCE_PRODUCER_CONTRACT_UNSUPPORTED")
    g0(lambda: _validate_entry(O_BASE, [_set(B + ["work", "case_limit"], 20_000_000_001)]))
    g0(lambda: _validate_entry(O_BASE, [_set(B + ["work", "invocation_limit"], 59_999_999_999)]))
    g0(lambda: _validate_entry(O_BASE, [_set(B + ["canonicalization"], "rfc8785")]))
    g0(lambda: _validate_entry(O_BASE, [_set(B + ["receipt_version"], 2)]))
    g0(lambda: _validate_entry(O_BASE, [_set(B + ["receipt_version"], True)]))
    fixture = _cases()[O_BASE]
    for drop in (["retained_precision"], B):
        source = deepcopy(fixture["source"])
        parent = source
        for part in drop[:-1]: parent = parent[part]
        del parent[drop[-1]]
        g0(lambda: rp._validate_draft(source, fixture["invocation"]))
    for key, value in (("producer", []), ("formulation_basis", "x")):
        source = deepcopy(fixture["source"]); source[key] = value
        g0(lambda: rp._validate_draft(source, fixture["invocation"]))


def test_g2_counters_are_json_integers_d10():
    _raises(lambda: _validate_entry(O_BASE, [_set(B + ["cases", 0, "run", "case_charge"], float(_cases()[O_BASE]["source"]["retained_precision"]["body"]["cases"][0]["run"]["case_charge"]))]), "G2", "ENCODING_MISMATCH")


def test_g5b_section_echo_terms_positive_d18():
    """D18 (D10 corrected): an echoed section term equal to the source's but not positive fails
    G5b SECTION_MISMATCH explicitly, never through the arithmetic fallback."""
    for key in ("area", "section_modulus", "length", "axial_stiffness", "torsional_stiffness"):
        for value in ("0000000000000000", "8000000000000000", "bff0000000000000"):
            _raises(lambda: _validate_entry(O_BASE, [_set(B + ["sources", 0, "section_terms", 0, key], value), _set(B + ["cases", 0, "selection", "section_terms", 0, key], value)]), "G5b", "SECTION_MISMATCH")


def test_class1_attempt_defect_wins_over_native_work_d3():
    """D3 class-1 convention: a native WORK defect found first still yields to an ATTEMPT defect."""
    base = _cases()[O_BASE]["source"]["retained_precision"]["body"]
    _raises(lambda: _validate_entry(O_BASE, [_set(B + ["calls", 0, "invocation_before"], 1), _set(B + ["cases", 0, "run", "records", 0, "corrections"], 4)]), "G5", "ATTEMPT_MISMATCH")
    _raises(lambda: _validate_entry(O_BASE, [_set(B + ["calls", 0, "invocation_before"], 1)]), "G5", "WORK_MISMATCH")
    # D16: a dangling build reference is a WORK defect, still deferred behind an ATTEMPT defect.
    _raises(lambda: _validate_entry(O_BASE, [_set(B + ["cases", 0, "run", "records", 0, "shared_build_ref"], 99)]), "G5", "WORK_MISMATCH")
    _raises(lambda: _validate_entry(O_BASE, [_set(B + ["cases", 0, "run", "records", 0, "shared_build_ref"], 99), _set(B + ["cases", 0, "run", "records", 0, "corrections"], 4)]), "G5", "ATTEMPT_MISMATCH")


def test_class2_order_and_dangling_references_d3_d16():
    """Ordinary checks (class 2, ATTEMPT) precede the C3 WORK list; dangling references take
    their own check's code (class 1 ATTEMPT, class 2 ordinary ATTEMPT, class 2 C3 PRODUCT_ATTEMPT)."""
    fault = {"kind": "overflow", "event": "map_write"}
    _raises(lambda: _validate_entry(F_BASE, [_set(A1 + ["adapter", "fault"], fault), _set(B + ["ordinary_attempts", 1, "diagnostic_refs"], ["diagnostic:missing"])]), "G5", "ATTEMPT_MISMATCH")
    _raises(lambda: _validate_entry(O_BASE, [_set(B + ["cases", 0, "run", "attempts", 0, "candidate_record"], 9)]), "G5", "ATTEMPT_MISMATCH")
    _raises(lambda: _validate_entry(O_BASE, [_set(B + ["product_attempts", 0, "ordinary_attempt_ref"], 7)]), "G5", "PRODUCT_ATTEMPT_MISMATCH")


def test_association_d4():
    """D4a-e (C3:146-148, :165, :167; S06 s1), G5 PRODUCT_ATTEMPT."""
    pa = lambda edits, base=F_BASE: _raises(lambda: _validate_entry(base, edits), "G5", "PRODUCT_ATTEMPT_MISMATCH")
    pa([_set(B + ["sources", 1, "preparation"], None)])                                      # a
    pa([_set(B + ["cases", 1, "reason", "cause", "product_attempt_ref"], 0)])               # c
    run_id = _cases()[F_BASE]["source"]["retained_precision"]["body"]["cases"][1]["run"]["id"]
    pa([_set(A1 + ["run_ref"], None), _set(A1 + ["stages", "native"], "not_entered")])      # e
    pa([_set(A1 + ["result"], {"kind": "unavailable", "error": {"kind": "preparation", "capture": {"kind": "storage", "detail": "prepared vector"}, "section": None}}),
        _set(B + ["cases", 1, "reason", "code"], "source_unavailable"), _set(B + ["cases", 1, "reason", "phase"], "preparation")])  # d: preparation with a Run
    pa([_set(A1 + ["result"], {"kind": "unavailable", "error": {"kind": "native", "run_ref": run_id}})])  # d: native with a selected Run


def test_native_records_d5():
    """D5c (rejected verification_failed needs a failed phase) and D5e (a phantom group)."""
    vf = {"kind": "rejected", "reason": {"space": "attempt", "tag": "verification_failed"}}
    _raises(lambda: _validate_entry("p512_ladder_synthetic", [_set(B + ["cases", 0, "run", "records", 0, "outcome"], vf), _set(B + ["cases", 0, "run", "attempts", 0, "outcome"], vf)]), "G5", "ATTEMPT_MISMATCH")
    groups = deepcopy(_cases()[O_BASE]["source"]["retained_precision"]["body"]["groups"])
    groups.append(dict(groups[0], id=1, call=7))
    _raises(lambda: _validate_entry(O_BASE, [_set(B + ["groups"], groups)]), "G5", "ATTEMPT_MISMATCH")


def test_ordinary_pass_d6():
    """D6b (selected quality domain), D6c (W2 trigger and nonzero exponent), D6d (legacy work_ref)."""
    quality = ["numerical_quality", "cases", 0, "solve_quality"]
    _raises(lambda: _validate_entry(O_BASE, [_set(quality, "not_assessed")]), "G5", "ATTEMPT_MISMATCH")
    fixture = _cases()[O_BASE]
    body = deepcopy(fixture["source"]["retained_precision"]["body"]); diags = fixture["source"]["diagnostics"]
    q = [dict(x, solve_quality="failed") for x in fixture["source"]["numerical_quality"]["cases"]]
    o = body["ordinary_attempts"][0]
    report = o["initial"]["report_diagnostic_ref"]
    o["initial"] = {"kind": "formation_failure", "error": {"tag": "numerical_range", "name": "x"}, "basis_index": 0}
    o["w2"] = {"kind": "published", "trigger": {"tag": "formation", "error": {"tag": "numerical_range", "name": "x"}}, "force_scale_exponent": 3, "report_diagnostic_ref": report}
    rp._g5_ordinary(body, body["cases"], diags, q)
    for change in ({"force_scale_exponent": 0}, {"trigger": {"tag": "formation", "error": {"tag": "numerical_range", "name": "y"}}},
                   {"trigger": {"tag": "evaluation", "error": {"tag": "range", "detail": "x"}}}):
        bad = deepcopy(body); bad["ordinary_attempts"][0]["w2"].update(change)
        _raises(lambda: rp._g5_ordinary(bad, bad["cases"], diags, q), "G5", "ATTEMPT_MISMATCH")
    for work_ref, rows in ((0, []), (0, [{"case_index": 1}])):
        bad = deepcopy(body); bad["ordinary_attempts"][0]["legacy_source"]["work_ref"] = work_ref; bad["legacy_source_work"] = rows
        _raises(lambda: rp._g5_ordinary(bad, bad["cases"], diags, q), "G5", "ATTEMPT_MISMATCH")


def test_g4_retained_diagnostic_names_one_requested_case_d7():
    fixture = _cases()[O_BASE]
    extra = deepcopy(next(d for d in fixture["source"]["diagnostics"] if d["code"] == "RETAINED_PRECISION_SELECTED"))
    extra.update(id="diagnostic:retained:orphan", affected_refs=["case:not-requested"])
    diags = fixture["source"]["diagnostics"] + [extra]
    _raises(lambda: _validate_entry(O_BASE, [_set(["diagnostics"], diags)]), "G4", "DIAGNOSTIC_MISMATCH")


def test_accounting_rules_d8_and_r3_both():
    """D8 R1'-R4 reader logic, including R3' with fault `both` (D13)."""
    attempt = deepcopy(_cases()[F_BASE]["source"]["retained_precision"]["body"]["product_attempts"][1])
    assert rp._accounting_rules(attempt) == (True, True, True, True)
    both = deepcopy(attempt)
    both["result"] = {"kind": "unavailable", "error": {"kind": "proof", "cause": {"kind": "work_accounting", "fault": "both"}}}
    assert rp._accounting_rules(both)[2] is False
    both["proof"]["numeric"]["wide_lme"] = {"kind": "unavailable", "fault": "overflow"}
    assert rp._accounting_rules(both)[2] is False
    both["proof"]["numeric"]["sticky_status"] = "inconsistent"
    assert rp._accounting_rules(both)[2] is True
    lane = deepcopy(attempt)  # a lane cause is bound to its own lane's work, not the proof's
    lane["proof"]["numeric"]["sticky_status"] = "overflow"
    lane["proof"]["lanes"][1]["state"] = "failed"; lane["proof"]["lanes"][1]["error"] = {"kind": "numeric", "cause": {"space": "stop", "tag": "work_accounting", "fault": "overflow"}}
    assert rp._accounting_rules(lane)[2] is False
    lane["proof"]["lanes"][1]["work"]["numeric"]["sticky_status"] = "overflow"
    assert rp._accounting_rules(lane)[2] is True
    op = deepcopy(attempt); op["operational"]["old"][0]["result"] = {"kind": "refused", "error": {"kind": "accounting"}}
    assert rp._accounting_rules(op)[1] is False


def test_theta_zero_on_no_data_body_d13():
    quarter = "3fd0000000000000"
    _raises(lambda: _validate_entry("ordinary_prepared_no_data_synthetic", [_set(B + ["cases", 0, "selection", "theta", 0, "value"], quarter),
            _set(B + ["cases", 0, "run", "records", 1, "verification", "theta", 0, "value"], quarter)]), "G5a", "SCALE_MISMATCH")


def test_ceiling_after_p128_verification_solve_failure_d13():
    """D13: an escalating p128 verification-solve failure skips to p512; a rejected p512 ends on the Ceiling."""
    pivot = {"space": "stop", "tag": "pivot", "global_dof": 6}
    rule = {"space": "attempt", "tag": "stop_rule", "quantity": {"tag": "displacement", "dof": {"node": 1, "component": "UX"}}, "body": 0, "kind": "translation"}
    vf = {"kind": "rejected", "reason": {"space": "attempt", "tag": "verification_failed"}}
    rec = lambda i, p, role, outcome: {"index": i, "precision": p, "role": role, "outcome": outcome, "corrections": 0}
    records = [rec(0, 128, "candidate", vf), rec(1, 256, "verification", {"kind": "failed", "reason": {"space": "attempt", "tag": "stop", "stop": pivot}}),
               rec(2, 512, "candidate", {"kind": "rejected", "reason": rule}), rec(3, 1024, "verification", {"kind": "solved"})]
    attempts = [{"precision": 128, "candidate_record": 0, "origin": {"kind": "fresh"}, "outcome": vf,
                 "verification": {"record": 1, "precision": 256, "phase": "failed", "reason": {"space": "attempt", "tag": "stop", "stop": pivot}}},
                {"precision": 512, "candidate_record": 2, "origin": {"kind": "fresh"}, "outcome": {"kind": "rejected", "reason": rule},
                 "verification": {"record": 3, "precision": 1024, "phase": "completed", "reason": None}}]
    run = {"kernel_terminal": {"kind": "unresolved", "reason": {"space": "unresolved", "tag": "ceiling"}}, "case_charge": 1, "invocation_increment": 1, "origin": {"group": 0}}
    rp._g5_schedule(run, records, attempts, _fail_g5)
    _raises(lambda: rp._g5_schedule(dict(run, kernel_terminal={"kind": "unresolved", "reason": {"space": "unresolved", "tag": "exact_sum_span"}}), records, attempts, _fail_g5), "G5", "ATTEMPT_MISMATCH")
    skip_one = deepcopy(attempts); skip_one[1]["precision"] = 256
    _raises(lambda: rp._g5_schedule(run, records, skip_one, _fail_g5), "G5", "ATTEMPT_MISMATCH")


def test_absolute_bound_small_scale_switch_both_sides_d13():
    """C1:158: S < 2^-988 uses the small-scale sum; S = 2^-988 is RU64(2^-64 S) (kills RV79 M11)."""
    s = 2.0 ** -988
    assert rp.bits(rp.absolute_bound(1.0, s)) == rp.bits(2.0 ** -1052)
    below = math.nextafter(s, 0.0)
    result = rp.absolute_bound(1.0, below)
    assert_least_upper(result, exact(rp.bits(rp.upward_product(below, 2.0 ** -64))) + Fraction(1, 1 << 53) + Fraction(1, 1 << 1074))
    assert result > 2.0 ** -54


def test_body_extent_summation_order():
    """verify.rs extent order ((dx^2 + dy^2) + dz^2) (kills RV79 M22)."""
    d = [float.fromhex("0x1.0000000000000p-15"), float.fromhex("0x1.6666666666666p-15"), float.fromhex("0x1.6666666666666p-29")]
    assert rp._extent([(0.0, 0.0, 0.0), tuple(d)]).hex() == "0x1.b87065db6a113p-15"


def test_rv79_surviving_mutants_m06_m09_m14():
    """M06: a passed G5a requires coverage; M09: a values failure is separate_failure; M14: the
    result error matches the first failed stage (P8/P9). Each on F' with a storage cause."""
    pa = lambda edits: _raises(lambda: _validate_entry(F_BASE, edits), "G5", "PRODUCT_ATTEMPT_MISMATCH")
    stages = dict(_cases()[F_BASE]["source"]["retained_precision"]["body"]["product_attempts"][1]["stages"])
    proof_storage = {"kind": "proof", "cause": {"kind": "storage"}}
    pa([_set(A1 + ["stages"], dict(stages, certificate="failed", observables="completed", g5a="completed")),
        _set(A1 + ["proof", "checks"], {"certificate": {"kind": "failed", "error": proof_storage}, "observables": {"kind": "passed"}, "g5a": {"kind": "passed"}}),
        _set(A1 + ["result"], {"kind": "unavailable", "error": proof_storage}), _set(A1 + ["proof", "summary_coverage"], None)])
    nv = dict(stages, values="failed", aliases="not_entered", certificate="not_entered")
    checks = {"certificate": {"kind": "not_entered"}, "observables": {"kind": "not_entered"}, "g5a": {"kind": "not_entered"}}
    values_failed = {"kind": "unavailable", "error": {"kind": "values", "cause": {"kind": "storage"}, "proof": {"kind": "association", "detail": "PP abandoned prepared draft"}}}
    pa([_set(A1 + ["stages"], nv), _set(A1 + ["proof", "checks"], checks), _set(A1 + ["proof", "summary_coverage"], None),
        _set(A1 + ["proof", "completion"], {"kind": "merged"}), _set(A1 + ["result"], values_failed)])
    pa([_set(A1 + ["stages"], dict(stages, maxima="failed", values="not_entered", aliases="not_entered", certificate="not_entered")),
        _set(A1 + ["proof", "checks"], checks), _set(A1 + ["proof", "summary_coverage"], None), _set(A1 + ["result"], values_failed)])


def test_snapshot_07_counts_and_entry_format():
    """Snapshot 07a (I62; D18): 15 cases, 236 mutations, 19 must-pass; only rehash "all" (D11);
    one expectation per entry except the per-reader G7 entry."""
    c = corpus()
    assert (len(c["cases"]), len(c["mutations"]), len(c["must_pass"])) == (15, 236, 19)
    entries = c["mutations"] + c["must_pass"]
    assert all(e["rehash"] == "all" for e in entries)
    assert [e["id"] for e in entries if "expected_by_reader" in e] == ["g7_maximum_off_enclosure"]
    assert len({e["id"] for e in entries}) == len(entries)


def test_class2_ordinary_before_association_d17():
    """D17: inside class 2 an ordinary reference (ATTEMPT) precedes C3 association (PRODUCT_ATTEMPT)."""
    dangling = _set(B + ["ordinary_attempts", 1, "diagnostic_refs"], ["diagnostic:missing"])
    no_prep = _set(B + ["sources", 1, "preparation"], None)
    _raises(lambda: _validate_entry(F_BASE, [dangling]), "G5", "ATTEMPT_MISMATCH")
    _raises(lambda: _validate_entry(F_BASE, [no_prep]), "G5", "PRODUCT_ATTEMPT_MISMATCH")
    _raises(lambda: _validate_entry(F_BASE, [dangling, no_prep]), "G5", "ATTEMPT_MISMATCH")
