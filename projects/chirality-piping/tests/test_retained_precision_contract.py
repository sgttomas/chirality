"""Synthetic reader controls, not produced receipts or native Current evidence."""
import json
import math
import struct
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
