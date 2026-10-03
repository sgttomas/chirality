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

def apply_mutation(base, mutation):
    from copy import deepcopy
    value = deepcopy(base)
    for edit in mutation["edits"]:
        parent = value
        for part in edit["path"][:-1]:
            parent = parent[part]
        key = edit["path"][-1]
        if edit["op"] == "remove":
            del parent[key]
        else:
            parent[key] = deepcopy(edit["value"])
    if mutation["rehash"]:
        body = value["retained_precision"]["body"]
        if mutation["rehash"] == "all":
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
        value["retained_precision"]["receipt_sha256"] = rp._hash("retained_precision_receipt_mp_v2", body)
    return value


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
    source = apply_mutation(fixture["source"], mutation)
    with pytest.raises(rp.RetainedPrecisionError) as error:
        rp._validate_draft(source, fixture["invocation"])
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


def rebind_invocation(source, invocation):
    source["retained_precision"]["body"]["invocation"]["value"] = rp._hash("source_blocks_invocation_v1", invocation)
    return apply_mutation(source, {"edits": [], "rehash": "all"})


def test_project_length_units_are_normalized_before_node_binding():
    from copy import deepcopy
    fixture = corpus()["cases"][0]
    source, invocation = deepcopy(fixture["source"]), deepcopy(fixture["invocation"])
    model = invocation["request"]["model"]
    model["project"]["units"]["length"] = "mm"
    for node in model["nodes"]:
        for axis in "xyz": node["position"][axis] *= 1000
    source = rebind_invocation(source, invocation)
    result = rp._validate_draft(source, invocation)
    assert result["classifications"] == fixture["expected_classifications"]
    model["nodes"][1]["position"]["x"] /= 1000
    with pytest.raises(rp.RetainedPrecisionError) as error:
        rp._validate_draft(rebind_invocation(source, invocation), invocation)
    assert (error.value.gate, error.value.code) == ("G8", "RETAINED_PRECISION_PREPARATION_MISMATCH")


def interpolated_control():
    from copy import deepcopy
    fixture = corpus()["cases"][0]
    source, invocation = deepcopy(fixture["source"]), deepcopy(fixture["invocation"])
    model = invocation["request"]["model"]
    # The source order returns200e9; the algebraically equivalent weighted sum
    # rounds one ulp lower. This makes the chosen binary64 operation order decisive.
    lower, upper, fraction = 199999999999.99997, 200000000000.00012, 0.1
    assert lower + fraction * (upper - lower) == 200e9
    assert (1 - fraction) * lower + fraction * upper != 200e9
    model["materials"][0]["temperature_points"] = [
        {"id": name, "temperature": {"value": temperature, "unit": "K"},
         "elastic_modulus": {"value": elastic, "unit": "Pa"},
         "shear_modulus": {"value": 77e9, "unit": "Pa"},
         "thermal_expansion_coefficient": {"value": 1e-5, "unit": "1/K"}}
        for name, temperature, elastic in (("lo", 300, lower), ("hi", 310, upper))
    ]
    model["load_cases"][0]["modulus_basis_temperature"] = {"value": 301, "unit": "K"}
    basis = source["retained_precision"]["body"]["material_bases"][0]
    basis["selector"] = {"kind": "temperature", "kelvin": rp.bits(301.0)}
    basis["materials"][0]["selection"] = {"kind": "interpolated", "lower_point_id": "lo", "upper_point_id": "hi", "target_kelvin": rp.bits(301.0)}
    return rebind_invocation(source, invocation), invocation


def test_temperature_uses_strict_bracket_and_source_operation_order():
    source, invocation = interpolated_control()
    assert rp._validate_draft(source, invocation)["invocation_bound"]
    for temperature in (299, 300, 310, 311):
        invocation["request"]["model"]["load_cases"][0]["modulus_basis_temperature"]["value"] = temperature
        basis = source["retained_precision"]["body"]["material_bases"][0]
        basis["selector"]["kelvin"] = rp.bits(float(temperature))
        basis["materials"][0]["selection"]["target_kelvin"] = rp.bits(float(temperature))
        with pytest.raises(rp.RetainedPrecisionError) as error:
            rp._validate_draft(rebind_invocation(source, invocation), invocation)
        assert error.value.gate == "G8"


@pytest.mark.parametrize("change", ["missing_alpha", "duplicate_temperature"])
def test_temperature_source_refusals_are_not_filled_from_base(change):
    source, invocation = interpolated_control()
    points = invocation["request"]["model"]["materials"][0]["temperature_points"]
    if change == "missing_alpha": del points[0]["thermal_expansion_coefficient"]
    else: points[1]["temperature"] = dict(points[0]["temperature"])
    with pytest.raises(rp.RetainedPrecisionError) as error:
        rp._validate_draft(rebind_invocation(source, invocation), invocation)
    assert error.value.gate == "G8"


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
    result = rp._validate_draft(apply_mutation(fixture["source"], entry), fixture["invocation"])
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
    rp._g5_ordinary(body, body["cases"], diags)
    body["cases"][1]["source_decline"] = dict(decline, input_owner=dict(decline["input_owner"], case_index=0))
    _raises(lambda: rp._g5_ordinary(body, body["cases"], diags), "G5", "ATTEMPT_MISMATCH")
