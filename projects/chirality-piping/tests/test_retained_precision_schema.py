"""Schema controls are synthetic shape checks, never numerical qualification."""
from copy import deepcopy
import json
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/retained_precision_mp_v2.schema.json").read_text())
CORPUS = json.loads((ROOT / "fixtures/results/retained_precision_cases.json").read_text())


def validate(value, name=None):
    schema = SCHEMA if name is None else {"$defs":SCHEMA["$defs"], "$ref":"#/$defs/"+name}
    jsonschema.Draft202012Validator(schema).validate(value)


def test_schema_itself_and_full_synthetic_receipt():
    jsonschema.Draft202012Validator.check_schema(SCHEMA)
    for fixture in CORPUS["cases"]:
        validate(fixture["source"]["retained_precision"])
        for row in fixture["source"]["results"]:
            validate(row, "RawRow")


@pytest.mark.parametrize("token", [None, 1, {}, [], True])
def test_direct_method_has_string_shape(token):
    row = deepcopy(CORPUS["cases"][0]["source"]["results"][0])
    row["recovery_method"] = token
    with pytest.raises(jsonschema.ValidationError): validate(row, "RawRow")


@pytest.mark.parametrize("token", ["", "wrong", "contribution_preserving_multiprecision_v1"])
def test_string_value_scope_is_reserved_for_g6(token):
    row = deepcopy(CORPUS["cases"][0]["source"]["results"][0])
    row["recovery_method"] = token
    validate(row, "RawRow")


def test_g5a_discriminator_does_not_collide_with_quantity_payload():
    for kind in ["sanity", "lower"]:
        variant = next(v for v in SCHEMA["$defs"]["G5aError"]["oneOf"] if v["properties"]["kind"].get("const") == kind)
        assert "quantity_kind" in variant["required"]
        assert variant["properties"]["quantity_kind"] == {"enum":[0,1]}
        assert variant["additionalProperties"] is False


def test_all_object_definitions_are_closed():
    def walk(value):
        if isinstance(value, dict):
            if value.get("type") == "object":
                assert value.get("additionalProperties") is False
                assert set(value["required"]) <= value["properties"].keys()
            for child in value.values(): walk(child)
        elif isinstance(value, list):
            for child in value: walk(child)
    walk(SCHEMA)

def test_results_successor_branch_is_explicit_and_old_branches_reject_receipt():
    from tests.test_load_reference_schema import _results_document
    from tests.schema_validation import validate_instance
    schema = json.loads((ROOT / "schemas/results.v0.3.schema.yaml").read_text())
    jsonschema.Draft202012Validator.check_schema(schema)
    source = CORPUS["cases"][0]["source"]
    document = _results_document(source, source["producer"]["semantic_contract_id"])
    document["result_envelope"]["retained_precision"] = deepcopy(source["retained_precision"])
    validate_instance(schema, document, instance_label="synthetic retained derivative shape")
    del document["result_envelope"]["retained_precision"]
    with pytest.raises(AssertionError):
        validate_instance(schema, document, instance_label="missing required receipt")
    old = json.loads((ROOT / "fixtures/results/preview_physics_connected_sparse.json").read_text())
    document = _results_document(old, old["producer"]["semantic_contract_id"])
    validate_instance(schema, document, instance_label="historical preview shape")
    document["result_envelope"]["retained_precision"] = deepcopy(source["retained_precision"])
    with pytest.raises(AssertionError):
        validate_instance(schema, document, instance_label="receipt on historical branch")

