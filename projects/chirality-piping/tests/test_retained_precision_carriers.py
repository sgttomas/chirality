"""U6b (I66): the F2a preview successor through the Python carriers (dispatch,
standing, binding refusal, classification summary, the AnalysisRun, and the
refusals of the legacy wrapper and the stress-neutral packager).

The milestone inputs are byte-identical copies of PP's pinned successor files
(D-U6-5): producer test outputs, not native Current evidence. Eligibility is held,
so standing is needs_recompute (D-U6-6); U7 owns the switch."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

import pytest

from core.analysis_runs import compatibility as c
from core.analysis_runs import retained_precision as rp

ROOT = Path(__file__).resolve().parents[1]
SUCC = c.PREVIEW_PHYSICS_RETAINED_CONTRACT_ID
PINNED = {
    "sparse_interactive": ("ac6986b0680e0df9d88c33a5bf4635372fc3b83cbb9080da44e6d32dbdca59dc",
                           "efc1a39bbe83840df6bd0761c932b8020285d3b8c005ba8fd0b45ba10d667494", [25, 69, 3, 1]),
    "dense_scrutiny": ("6cd1d249e5352aaffbd2b7d7349c74a1d0e0572df35500f66be49c3cad95c9b5",
                       "3e26499f17caff8f5fc0d46406bbe54acf43e8cb16e761784aa5074413b0ac4a", [25, 69, 3, 2]),
}
MODES = sorted(PINNED)
NOTICE = "Retained-precision recovery is unavailable for this load case. Its published rows keep their ordinary values, standing and diagnostics."


def milestone(mode):
    """D-U6-5: the pinned bytes, checked here; returns (source, invocation)."""
    raw = (ROOT / f"fixtures/results/retained_precision_milestone_successor_{mode}.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PINNED[mode][0]
    doc = json.loads(raw)
    assert doc["source"]["retained_precision"]["receipt_sha256"] == PINNED[mode][1]
    assert doc["invocation"]["solver_mode"] == mode
    return doc["source"], doc["invocation"]


def requested(invocation):
    return [{"ref_type": "load_case", "ref_id": case["id"]} for case in invocation["request"]["model"]["load_cases"]]


def rehash(source):
    """A forged but hash-consistent statement: the edit reaches the gate it targets."""
    source = deepcopy(source)
    body = source["retained_precision"]["body"]
    body["publication_sha256"] = rp._hash("retained_precision_publication_mp_v2", {k: v for k, v in source.items() if k != "retained_precision"})
    source["retained_precision"]["receipt_sha256"] = rp._hash("retained_precision_receipt_mp_v2", body)
    return source


def projected(source):
    """The reader's G7 projection: the same statement under the base identity."""
    base = deepcopy(source)
    del base["retained_precision"]
    base["producer"]["semantic_contract_id"] = c.PREVIEW_PHYSICS_CONTRACT_ID
    base["formulation_basis"]["profile_id"] = "product_preview_mechanics_v1"
    for row in base["results"]:
        row.pop("recovery_method", None)
    return base


def build(source):
    return c.build_analysis_run(source, input_manifest_ref={"object_type": "InputManifest", "ref": "manifest:u6b"}, input_manifest_hash="1" * 64)


def dispatch(source):
    try:
        c._source_contract(source)
        return "ok"
    except ValueError as error:
        return str(error)


def raises(code, fn, *args):
    with pytest.raises(ValueError) as error:
        fn(*args)
    assert str(error.value) == code, str(error.value)


@pytest.mark.parametrize("mode", MODES)
def test_dispatch_admits_the_successor_through_the_accepted_reader_only(mode):
    source, invocation = milestone(mode)
    contract, sha, path = c._source_contract(source)
    assert (contract, sha, path.name) == (SUCC, c.PREVIEW_PHYSICS_RETAINED_CONTRACT_SHA256, "semantic_contract_v0_3_preview_physics_retained_1.json")
    assert hashlib.sha256(path.read_bytes()).hexdigest() == rp.TABLE_HASH == sha
    assert c.is_fresh_contract_id(SUCC) and SUCC in c.CURRENT_RECORD_CONTRACT_IDS
    assert c.standing_reason(source) is None
    # The reader's first code; a G7 failure keeps the base validator's own text.
    broken = deepcopy(source)
    broken["retained_precision"]["receipt_sha256"] = "0" * 64
    raises("RETAINED_PRECISION_RECEIPT_MISMATCH", c._source_contract, broken)
    unit = deepcopy(source)
    index = next(i for i, row in enumerate(unit["results"]) if row["kind"] == "linear_solver_mode_basis")
    unit["results"][index]["unit"] = "m"
    unit = rehash(unit)
    with pytest.raises(rp.RetainedPrecisionError) as reader:
        rp.validate_retained_precision(unit)
    assert reader.value.gate == "G7" and reader.value.detail and reader.value.detail != reader.value.code
    raises(reader.value.detail, c._source_contract, unit)
    # The Python reader has no transport validator: a transported successor is refused.
    raises("SOURCE_PRODUCER_CONTRACT_UNSUPPORTED", lambda s: c._source_contract(s, check_receipt=False), source)


@pytest.mark.parametrize("mode", MODES)
def test_standing_is_needs_recompute_and_comes_only_from_the_receipt(mode):
    source, invocation = milestone(mode)
    refs = requested(invocation)
    assert c.numerical_use_standing(source, refs) == "needs_recompute"
    assert c.numerical_use_standing(source, refs, invocation) == "needs_recompute"
    validation = rp.validate_retained_precision(source, invocation)
    assert validation["invocation_bound"] and not validation["numerical_eligible"]
    row = deepcopy(source)
    row["results"][0]["value"] = row["results"][0]["value"] * 2.0 + 1.0
    assert c.numerical_use_standing(row, refs) == "unsupported"
    assert c.numerical_use_standing(row, refs, invocation) == "unsupported"
    foreign = deepcopy(invocation)
    foreign["solver_mode"] = MODES[1 - MODES.index(mode)]
    assert c.numerical_use_standing(source, refs, foreign) == "unsupported"
    # numerical_quality never contributes: a hash-consistent checks_passed claim is
    # refused by the reader (D6b), never read by the ordinary branch.
    claimed = deepcopy(source)
    claimed["numerical_quality"]["status"] = "checks_passed"
    claimed["numerical_quality"]["cases"][0].update(solve_quality="checks_passed", structural_status="passive_model_basis",
                                                     model_matrix_fidelity="represented_equations_retained")
    claimed = rehash(claimed)
    with pytest.raises(rp.RetainedPrecisionError):
        rp.validate_retained_precision(claimed)
    assert c.numerical_use_standing(claimed, refs) == "unsupported"
    assert c.numerical_use_standing(claimed, refs, invocation) == "unsupported"


def test_standing_rule_conjuncts_with_eligibility_set():
    """The post-U7 rule, through the seam with eligibility set; no flag is touched."""
    source, invocation = milestone("sparse_interactive")
    refs = requested(invocation)
    validation = dict(rp.validate_retained_precision(source, invocation), numerical_eligible=True)
    assert c._retained_standing_from(validation, source, refs) == "numerically_eligible"
    assert c._retained_standing_from(dict(validation, numerical_eligible=False), source, refs) == "needs_recompute"
    assert c._retained_standing_from(dict(validation, invocation_bound=False), source, refs) == "needs_recompute"
    for other in ([], [{"ref_type": "load_case", "ref_id": "other"}], refs + [{"ref_type": "load_case", "ref_id": "other"}]):
        assert c._retained_standing_from(validation, source, other) == "needs_recompute"
    unsolved = deepcopy(source)
    unsolved["status"]["mechanics"] = "MODEL_INCOMPLETE"
    assert c._retained_standing_from(validation, unsolved, refs) == "needs_recompute"
    not_required = deepcopy(source)
    not_required["retained_precision"]["body"]["cases"][0]["status"] = "not_required"
    q = not_required["numerical_quality"]["cases"][0]
    q.update(solve_quality="checks_passed", structural_status="passive_model_basis",
             model_matrix_fidelity="represented_equations_retained", accuracy_evidence="not_claimed")
    assert q["evidence_refs"]
    assert c._retained_standing_from(validation, not_required, refs) == "numerically_eligible"
    for field, value in (("solve_quality", "sensitive"), ("structural_status", "numerically_unresolved"),
                         ("model_matrix_fidelity", "assembly_uncertainty"), ("accuracy_evidence", "unresolved"),
                         ("evidence_refs", []), ("evidence_refs", ["diagnostic:absent"]),
                         ("basis_ref", {"ref_type": "load_case", "ref_id": "other"})):
        bad = deepcopy(not_required)
        bad["numerical_quality"]["cases"][0][field] = value
        assert c._retained_standing_from(validation, bad, refs) == "needs_recompute", field
    duplicate = deepcopy(not_required)
    duplicate["results"].append(deepcopy(duplicate["results"][0]))
    assert c._retained_standing_from(validation, duplicate, refs) == "needs_recompute"
    short = deepcopy(not_required)
    short["numerical_quality"]["cases"] = []
    assert c._retained_standing_from(validation, short, refs) == "needs_recompute"
    # Any other case status is not eligible, even with ordinarily eligible quality.
    for status in ("unavailable", "other", None):
        case = deepcopy(not_required)
        case["retained_precision"]["body"]["cases"][0]["status"] = status
        assert c._retained_standing_from(validation, case, refs) == "needs_recompute", status


def test_shared_carrier_cases_python():
    """The 14 shared standing-parity scenarios: the same expectations Rust (U6a)
    and TypeScript (U6d) read from this file."""
    cases = json.loads((ROOT / "fixtures/results/retained_precision_carrier_cases.json").read_text())
    assert cases["format"] == "I66-U6-CARRIER-CASES-v1"
    fixtures = {}
    for fid, spec in cases["fixtures"].items():
        raw = (ROOT / spec["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == spec["sha256"]
        fixtures[fid] = json.loads(raw)
    for case in cases["cases"]:
        doc = fixtures[case["fixture"]]
        source, invocation = deepcopy(doc["source"]), deepcopy(doc["invocation"])
        for edit in case["edits"]:
            assert edit["op"] == "set"
            target = source if edit["target"] == "source" else invocation
            for key in edit["path"][:-1]:
                target = target[key]
            target[edit["path"][-1]] = edit["value"]
        refs = requested(doc["invocation"]) if case["requested"] == "invocation" else case["requested"]
        context = invocation if case["invocation"] is not None else None
        assert c.numerical_use_standing(source, refs, context) == case["expected_standing"], case["id"]
        assert dispatch(source) == case["expected_dispatch"], case["id"]
    assert len(cases["cases"]) == 14


@pytest.mark.parametrize("mode", MODES)
def test_analysis_run_carries_the_complete_receipt_and_it_comes_back_out(mode):
    from tests.schema_validation import validate_instance
    source, invocation = milestone(mode)
    original = deepcopy(source)
    record = build(source)
    assert source == original
    run = record["analysis_run"]
    assert run["retained_precision"] == source["retained_precision"]
    assert run["reproducibility"]["semantic_contract"] == {"id": SUCC, "sha256": c.PREVIEW_PHYSICS_RETAINED_CONTRACT_SHA256}
    assert all(ref["semantic_contract"]["id"] == SUCC for ref in run["result_refs"])
    assert "contract_evidence" not in run and "source_block_recovery" not in run
    assert c.verify_analysis_run_record(record) == "match"
    c.validate_analysis_run_v0_3(record, source)
    validate_instance(json.loads((ROOT / "schemas/analysis_run.schema.json").read_text()), record, instance_label=f"{mode} successor record")
    # Back out: the record's receipt authenticates the raw publication again.
    back = deepcopy(source)
    back["retained_precision"] = deepcopy(run["retained_precision"])
    assert rp.validate_retained_precision(back, invocation) == rp.validate_retained_precision(source, invocation)
    # Drop or alter the carried receipt.
    dropped = deepcopy(record)
    del dropped["analysis_run"]["retained_precision"]
    raises(c.ANALYSIS_RETAINED_PRECISION_RECEIPT_MISMATCH, c.validate_analysis_run_v0_3, dropped, source)
    altered = deepcopy(record)
    altered["analysis_run"]["retained_precision"]["body"]["work"]["charged"] = 1
    raises(c.ANALYSIS_RETAINED_PRECISION_RECEIPT_MISMATCH, c.validate_analysis_run_v0_3, altered, source)
    resealed = deepcopy(record)
    resealed["analysis_run"]["retained_precision"]["receipt_sha256"] = "0" * 64
    raises(c.ANALYSIS_RETAINED_PRECISION_RECEIPT_MISMATCH, c.validate_analysis_run_v0_3, resealed, source)
    # A record checked against an edited statement fails at the reader first.
    edited = deepcopy(source)
    edited["retained_precision"]["receipt_sha256"] = "1" * 64
    raises("RETAINED_PRECISION_RECEIPT_MISMATCH", c.validate_analysis_run_v0_3, record, edited)


@pytest.mark.parametrize("mode", MODES)
def test_downgrades_are_refused(mode):
    source, invocation = milestone(mode)
    refs = requested(invocation)
    relabelled = deepcopy(source)
    relabelled["producer"]["semantic_contract_id"] = c.PREVIEW_PHYSICS_CONTRACT_ID
    relabelled["formulation_basis"]["profile_id"] = "product_preview_mechanics_v1"
    raises(c.RETAINED_PRECISION_DOWNGRADE_FORBIDDEN, c._source_contract, relabelled)
    raises(c.RETAINED_PRECISION_DOWNGRADE_FORBIDDEN, build, relabelled)
    assert c.numerical_use_standing(relabelled, refs, invocation) == "unsupported"
    tokens = deepcopy(relabelled)
    del tokens["retained_precision"]
    raises(c.RETAINED_PRECISION_DOWNGRADE_FORBIDDEN, c._source_contract, tokens)
    assert c.numerical_use_standing(tokens, refs) == "unsupported"
    # As Rust's header-only for_source_metadata, the transport dispatch reads no
    # rows; the raw dispatch, which the packager also runs, refuses them.
    assert c._source_contract(tokens, check_receipt=False)[:2] == (c.PREVIEW_PHYSICS_CONTRACT_ID, c.PREVIEW_PHYSICS_CONTRACT_SHA256)
    base = projected(source)
    assert dispatch(base) == "ok"
    null = deepcopy(base)
    null["retained_precision"] = None
    raises(c.RETAINED_PRECISION_DOWNGRADE_FORBIDDEN, c._source_contract, null)
    # A base record carrying a receipt is refused; the legacy 0.2 builder refuses one too.
    record = build(base)
    c.validate_analysis_run_v0_3(record, base)
    record["analysis_run"]["retained_precision"] = deepcopy(source["retained_precision"])
    raises(c.ANALYSIS_RETAINED_PRECISION_DOWNGRADE_FORBIDDEN, c.validate_analysis_run_v0_3, record, base)
    legacy = {"schema_version": "0.2.0", "run_id": "run:legacy", "model_ref": base["model_ref"], "results": [], "diagnostics": [],
              "retained_precision": deepcopy(source["retained_precision"])}
    raises("ANALYSIS_LEGACY_SOURCE_DOWNGRADE_FORBIDDEN", lambda s: c.build_analysis_run_v0_2(s, input_manifest_ref={"object_type": "InputManifest", "ref": "m"}, input_manifest_hash="1" * 64), legacy)


@pytest.mark.parametrize("mode", MODES)
def test_binding_refusal_follows_the_validated_class_only(mode):
    source, _ = milestone(mode)
    validation = rp.validate_retained_precision(source)
    rows = {row["id"]: row for row in source["results"]}
    expected = {"absolute_verified": c.RULE_QUANTITY_BELOW_VERIFIED_FLOOR, "not_covered": c.RULE_QUANTITY_NOT_COVERED}
    for item in validation["classifications"]:
        assert c.rule_binding_refusal(source, rows[item["result_id"]]) == expected.get(item["class"]), item["result_id"]
    # The headline maxima: the displacement is relative-verified, the stress absolute-verified.
    headline = {key: c.rule_binding_refusal(source, rows[source["summary"][key]["result_ref"]]) for key in ("max_displacement", "max_open_formula_stress")}
    assert headline == {"max_displacement": None, "max_open_formula_stress": c.RULE_QUANTITY_BELOW_VERIFIED_FLOOR}
    broken = deepcopy(source)
    broken["results"][0]["value"] = 12345.0
    assert all(c.rule_binding_refusal(broken, row) == c.RULE_QUANTITY_NOT_COVERED for row in source["results"])
    # A row the statement does not classify (as in Rust) has no class to refuse.
    assert c.rule_binding_refusal(source, {"id": "result:absent"}) is None
    assert c.rule_binding_refusal(source, {}) is None
    base = projected(source)
    assert all(c.rule_binding_refusal(base, row) is None for row in base["results"])


def test_each_class_maps_to_its_refusal():
    assert c._class_binding_refusal("absolute_verified") == c.RULE_QUANTITY_BELOW_VERIFIED_FLOOR
    assert c._class_binding_refusal("not_covered") == c.RULE_QUANTITY_NOT_COVERED
    for cls in ("relative_verified", "input_derived", "non_quantity", None):
        assert c._class_binding_refusal(cls) is None


@pytest.mark.parametrize("mode", MODES)
def test_classification_summary_counts_validated_classes(mode):
    source, invocation = milestone(mode)
    relative, absolute, input_derived, non_quantity = PINNED[mode][2]
    case_id = invocation["request"]["model"]["load_cases"][0]["id"]
    expected = [{"case_id": case_id, "relative_verified": relative, "absolute_verified": absolute, "interval_bindable": 0,
                 "not_covered": 0, "input_derived": input_derived, "non_quantity": non_quantity,
                 "withheld": relative + absolute + input_derived}]
    assert c.classification_summary(source, invocation) == expected
    assert c.classification_summary(source) == expected
    broken = deepcopy(source)
    broken["results"][0]["value"] = 12345.0
    assert c.classification_summary(broken, invocation) == []
    assert c.classification_summary(projected(source)) == []
    # After U7 (through the seam): only absolute and not-covered rows stay withheld.
    validation = dict(rp.validate_retained_precision(source, invocation), numerical_eligible=True)
    current = deepcopy(expected)
    current[0]["withheld"] = absolute
    assert c._classification_summary_from(validation, source, invocation) == current
    assert c._classification_summary_from(validation, source, None) == expected
    other = deepcopy(invocation)
    other["request"]["model"]["load_cases"][0]["id"] = "other"
    assert c._classification_summary_from(validation, source, other) == expected
    classes = deepcopy(validation["classifications"])
    index = next(i for i, item in enumerate(classes) if item["class"] == "relative_verified")
    classes[index]["class"] = "not_covered"
    uncovered = deepcopy(current)
    uncovered[0].update(relative_verified=relative - 1, not_covered=1, withheld=absolute + 1)
    assert c._classification_summary_from(dict(validation, classifications=classes), source, invocation) == uncovered
    uncovered[0]["withheld"] = relative + absolute + input_derived
    assert c._classification_summary_from(dict(validation, classifications=classes, numerical_eligible=False), source, invocation) == uncovered
    # Counts are per case: a classification under another case is not counted here.
    stray = dict(classes[index], basis_ref={"ref_type": "load_case", "ref_id": "other"})
    assert c._classification_summary_from(dict(validation, classifications=classes + [stray], numerical_eligible=False), source, invocation) == uncovered


@pytest.mark.parametrize("mode", MODES)
def test_stress_neutral_packager_still_refuses_the_successor(mode):
    """T6's refusal stands (D2 4.9.6; C1:162): schema support is shape only."""
    from core.handoff.stress_neutral import package_v0_3 as sn
    from tests.test_stress_neutral_physics_source import arguments
    source, _ = milestone(mode)
    record = build(source)
    raises("SN-SOURCE-METHOD-UNSUPPORTED", lambda: sn.build_stress_neutral_export_package_v0_3(source_envelope=source, analysis_record=record, **arguments(source, record)))
    base = projected(source)
    base_record = build(base)
    packet = sn.build_stress_neutral_export_package_v0_3(source_envelope=base, analysis_record=base_record, **arguments(base, base_record))
    packet.update(producer=dict(packet["producer"], semantic_contract_id=SUCC), retained_precision=deepcopy(source["retained_precision"]),
                  semantic_contract={"id": SUCC, "sha256": c.PREVIEW_PHYSICS_RETAINED_CONTRACT_SHA256})
    raises("SOURCE_PRODUCER_CONTRACT_UNSUPPORTED", sn.validate_stress_neutral_export_package_v0_3, packet)


@pytest.mark.parametrize("mode", MODES)
def test_legacy_record_wrapper_refuses_a_receipt(mode):
    """D-U6-9: the historical 0.1.0 wrapper cannot carry a receipt."""
    from core.analysis_runs.records import build_preview_analysis_run_envelope
    source, _ = milestone(mode)
    raises("ANALYSIS_RETAINED_PRECISION_DOWNGRADE_FORBIDDEN", build_preview_analysis_run_envelope, source)
    # The wrapper's own preview input still builds; the same input carrying a
    # receipt member (even an empty one) is refused before anything is recorded.
    preview = json.loads((ROOT / "fixtures/product_preview/invented_mechanics_result.json").read_text())
    assert build_preview_analysis_run_envelope(preview)["schema_version"] == "0.1.0"
    for receipt in (deepcopy(source["retained_precision"]), None):
        raises("ANALYSIS_RETAINED_PRECISION_DOWNGRADE_FORBIDDEN", build_preview_analysis_run_envelope, dict(preview, retained_precision=receipt))


@pytest.mark.parametrize("mode", MODES)
def test_r2_noticed_ordinary_envelope_keeps_its_base_behaviour(mode):
    """R-2: a base publication carrying the unavailable notice is an ordinary
    preview-physics-1 envelope; its carriers and standing equal the plain base."""
    source, invocation = milestone(mode)
    plain = projected(source)
    case_id = invocation["request"]["model"]["load_cases"][0]["id"]
    noticed = deepcopy(plain)
    noticed["diagnostics"].append({"id": f"diagnostic:retained-precision:{case_id}:unavailable", "code": "RETAINED_PRECISION_UNAVAILABLE",
                                   "severity": "info", "message": NOTICE, "source": "core/product_physics", "affected_refs": [case_id]})
    refs = requested(invocation)
    assert c._source_contract(noticed)[:2] == c._source_contract(plain)[:2] == (c.PREVIEW_PHYSICS_CONTRACT_ID, c.PREVIEW_PHYSICS_CONTRACT_SHA256)
    assert c.numerical_use_standing(noticed, refs) == c.numerical_use_standing(plain, refs)
    record = build(noticed)
    c.validate_analysis_run_v0_3(record, noticed)
    assert record["analysis_run"]["diagnostics"][-1]["source_annotation"]["code"] == "RETAINED_PRECISION_UNAVAILABLE"
    assert "retained_precision" not in record["analysis_run"]
    assert all(c.rule_binding_refusal(noticed, row) is None for row in noticed["results"])
