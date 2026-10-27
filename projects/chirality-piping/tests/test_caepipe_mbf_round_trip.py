#!/usr/bin/env python3
"""Round trip of the DEL-17-04 SI MBF writer and MBF importer on invented models (Design `caepipe-mbf-import.md`
§18.1 items 3 to 6, §18.2).

For each model A in the reversible subset, W = writer(A) and I = import(W) with the bound sidecar:
(a) canonical equality within the derived per-scalar bounds; (a') unbound imports: under profile decision PD-1
canonical equality by CAEPIPE name, and under the base rule the named refusal MBF-IMPORT-TBD-17-04-007;
(b) the identities and splits the sidecar preserves are restored, and every other identity is reported;
(c) byte reproduction writer(I) == W for the byte-reproducible subset, with every formatting collision reported;
(d) solve equality against a provisional threshold; (e) determinism. Then the English/SI units check, the bend
boundary case and schema validation. Every model and fixture here is invented; none is engineering data.
"""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
for extra in (ROOT, ROOT / "tests", ROOT / "tools" / "validation"):
    if str(extra) not in sys.path:
        sys.path.insert(0, str(extra))

import caepipe_mbf_canonical as canon  # noqa: E402
from core.handoff.caepipe_mbf import importer as importer_module  # noqa: E402
from core.handoff.caepipe_mbf import render_caepipe_mbf_si  # noqa: E402
from core.handoff.caepipe_mbf.importer import import_caepipe_mbf  # noqa: E402
from schema_validation import JsonSchemaDependencyMissing, _skip_or_note_missing_jsonschema, validate_instance  # noqa: E402
from test_model_schema import desktop_entity_requirements  # noqa: E402
import test_caepipe_mbf_si_writer as writer_tests  # noqa: E402
import test_caepipe_mbf_importer as importer_tests  # noqa: E402
from tools.caepipe_correlation.run_pilot import load_cases, solve_swbpipe  # noqa: E402


INVENTED = {"*": {"origin": "project_invented", "source_name": "invented round-trip model",
                  "redistribution_status": "public_permissive"}}
FIXTURES = ROOT / "fixtures" / "caepipe_mbf" / "invented" / "import"
DESKTOP_SCHEMA = {"$schema": "https://json-schema.org/draft/2020-12/schema",
                  "$ref": "https://openpipestress.org/schemas/model.schema.yaml#/$defs/DesktopDocument"}


def both_given_material():
    model = writer_tests.cantilever()
    model["materials"][0] = {"id": "mat:CS", "elastic_modulus": writer_tests.q(2.0e11, "Pa"),
                             "poisson_ratio": writer_tests.q(0.25, "1"), "shear_modulus": writer_tests.q(8.0e10, "Pa"),
                             "thermal_expansion_coefficient": writer_tests.q(1.2e-5, "1/K")}
    return model


def weighted():
    model = writer_tests.cantilever()
    od, wall = 0.1683, 0.00711
    area = math.pi / 4.0 * (od**2 - (od - 2 * wall) ** 2)
    model["nodes"].append(writer_tests.node("N2", 6.0))
    model["pipe_segments"].append(writer_tests.pipe("S2", "N1", "N2", od, wall, "m"))
    model["load_cases"][0]["primitive_loads"].append(
        {"id": "w1", "category": "weight", "target": {"type": "element", "pipe": "S1"}, "direction": "global_y",
         "magnitude": writer_tests.q(-area * 7850.0 * 9.80665, "N/m"), "dimension": "force_per_length"})
    return model


def reversed_bend():
    model = writer_tests.bent_l()
    model["supports"] = [{"id": "SB", "node": "B", "restraints": list(writer_tests.SIX)}]
    return model


def bend_boundary(residual: bool = True):
    """Invented 90 degree bend, R = 999 mm, tangent lengths 999.0000008991 mm, adjacent straights 0.5 mm (§18.1 item 5)."""
    tangent = 999.0000008991 if residual else 999.0
    model = writer_tests.model_shell("mm")
    ti = 0.5 + tangent
    model["nodes"] = [writer_tests.node("P", 0.0), writer_tests.node("N", 0.5), writer_tests.node("F", ti, 0.0, tangent),
                      writer_tests.node("Q", ti, 0.0, tangent + 0.5)]
    model["pipe_segments"] = [writer_tests.pipe("S1", "P", "N", 168.3, 7.11, "mm"),
                              writer_tests.pipe("BEND", "N", "F", 168.3, 7.11, "mm"),
                              writer_tests.pipe("S2", "F", "Q", 168.3, 7.11, "mm")]
    for item in model["pipe_segments"]:
        item["y_reference"] = {"x": 0.0, "y": 1.0, "z": 0.0}
    model["pipe_segments"][1]["y_reference"] = {"x": 1.0, "y": 0.0, "z": -1.0}
    model["supports"] = [{"id": "AP", "node": "P", "restraints": list(writer_tests.SIX)},
                         {"id": "AQ", "node": "Q", "restraints": list(writer_tests.SIX)}]
    model["components"] = [{"id": "bend-b", "kind": "bend", "node": "N",
                            "geometry": {"bend_pipe_ref": "BEND", "bend_radius": writer_tests.q(999.0, "mm")},
                            "modifiers": {"flexibility_factor_user_value": writer_tests.q(1.0, "none")},
                            "mechanics_interface": {"solver_consumption": "curved_bend_macro_element"}}]
    model["load_cases"] = [{"id": "case:th", "primitive_loads": [
        {"id": f"t:{pipe_id}", "category": "thermal", "target": {"type": "element", "pipe": pipe_id},
         "direction": "global_x", "magnitude": writer_tests.q(50.0, "degC"), "dimension": "temperature_interval"}
        for pipe_id in ("S1", "BEND", "S2")]}]
    return model


CLOSURE = {"closure_transfer": "transfers_to_wall", "provenance": "invented round-trip declaration"}
# Invented Z-vertical files (Design §5.1) with pressure (§9.4), in SI (bar) and English (psi) units. The SI file's
# skew straight meets the next straight at a corner, so its import has two regions.
Z_VERTICAL_SI = (
    "INVENTED Z-VERTICAL SI", "VERSION", "15.10", "OPTIONS", "HGRA,SI,Z", "OPTEMP", "20", "MATERIAL",
    "M1,7850,0.3,1,1,CS,invented steel", "M1,20,200000,1.2e-05", "PIPE", "P1,168.3,7.11,0,0,0,0,0,0", "LOADS",
    "L1,120,15,0", "LAYOUT", "F10,KA,MM1,PP1,CL=L1", "T20,X1000,Y2000,Z3000,CFOR(10,20,30),FLC=1",
    "T30,KI,B250,X4000,CFF=1.5", "T40,KA,Z3000")
Z_VERTICAL_ENGLISH = (
    "INVENTED Z-VERTICAL ENGLISH", "VERSION", "15.10", "OPTIONS", "HGRA,Z", "OPTEMP", "70", "MATERIAL",
    "M1,0.283,0.3,1,1,CS,invented steel", "M1,70,29000000,6.5e-06", "PIPE", "P1,6.625,0.28,0,0,0,0,0,0", "LOADS",
    "L1,250,150,0", "LAYOUT", "F10,KA,MM1,PP1,CL=L1", "T20,X10'6\",CFOR(0,0,-1000),FLC=1", "T30,KA,Y8")


def z_import(lines: tuple[str, ...]):
    data = "".join(line + "\r\n" for line in lines).encode("ascii")
    result = import_caepipe_mbf(data, material_provenance=INVENTED, pressure_closure=CLOSURE, source_label=lines[0])
    assert result.status == "imported", result.diagnostics
    return result


def models() -> dict[str, tuple[dict, str, float]]:
    found = {case["case_id"]: (case["model"], case["title"], case["reference_temperature_c"]) for case in load_cases()}
    found.update({
        "writer-cantilever-m": (writer_tests.cantilever("m"), "INVENTED CANTILEVER", 20.0),
        "writer-cantilever-mm": (writer_tests.cantilever("mm"), "INVENTED CANTILEVER", 20.0),
        "writer-branched": (writer_tests.branched(), "INVENTED BRANCH", 20.0),
        "writer-weight": (weighted(), "WEIGHT", 20.0),
        "writer-bent-l": (writer_tests.bent_l(), "INVENTED L", 20.0),
        "writer-nu-and-g": (both_given_material(), "NU AND G", 20.0),
        "writer-straight-run": (writer_tests.straight_run(20), "RUN", 20.0),
        "bend-boundary": (bend_boundary(), "BEND BOUNDARY", 20.0),
        "writer-cancelling-forces": (writer_tests.cancelling_cantilever(), "CANCEL", 20.0),
        "pressure-l-pa": (writer_tests.pressurized_l(), "PRESSURE L", 20.0),
        "pressure-tee-bar": (writer_tests.pressurized_tee(), "PRESSURE TEE", 20.0),
        "pressure-us-psi": (writer_tests.pressurized_us_cantilever(), "PRESSURE US", 20.0),
        "z-vertical-si": (z_import(Z_VERTICAL_SI).model, "Z VERTICAL SI", 20.0),
        "z-vertical-english": (z_import(Z_VERTICAL_ENGLISH).model, "Z VERTICAL ENGLISH", 20.0),
    })
    return found


MODELS = models()
# Reversible subset (§18.2): written, no MBF-SI-SHEAR-MODULUS-NOT-EXPORTED, printed values valid, distinct keys kept.
REVERSIBLE = sorted(MODELS)
# Excluded by name, with the reason: the component names the far tangent node, which the sidecar does not carry
# (the importer reports MBF-IMPORT-ID-UNRECOVERABLE for every bound bend component node).
EXCLUDED = {"writer-bent-l-reversed": (reversed_bend(), "component node is the far tangent node; not in the sidecar")}
# Byte-reproducible subset (§18.2): bound sidecar, identical writer settings, no formatting collision.
BYTE_REPRODUCIBLE = sorted(MODELS)
SOLVE_THRESHOLD_FACTOR = 1e3  # ASSUMPTION (Design §18.1(d)): provisional, not a derived bound
SOLVE_R_IN_LIMIT = 1e-8
# Models whose source A the headless solve itself refuses, so there is no solve to compare (listed by name).
SOLVE_EXCLUDED = {
    "writer-branched": "A authors nu without G or a constitutive basis, which the solve refuses",
    "writer-straight-run": "A has no primitive load",
}
PRESSURE_MODELS = {name for name, (model, _, _) in MODELS.items() if model.get("pressure_contract")}


def unbound_closure(trip) -> dict | None:
    """The closure declaration an unbound import of `trip` needs: its source's, by CAEPIPE node name."""
    if trip.name not in PRESSURE_MODELS:
        return None
    nodes = {trip.writer.node_map[terminal["node_ref"]]: terminal["closure_transfer"]
             for case in trip.model["load_cases"] for region in case.get("pressure_regions") or []
             for terminal in region["terminals"] if terminal["closure_transfer"] != "transfers_to_wall"}
    return {**CLOSURE, "nodes": nodes}


class Trip:
    def __init__(self, name: str, model: dict, title: str, t_ref: float) -> None:
        self.name, self.model, self.title, self.t_ref = name, model, title, t_ref
        self.writer = render_caepipe_mbf_si(model, title=title, reference_temperature_c=t_ref)
        assert self.writer.status == "written", self.writer.diagnostics
        assert "MBF-SI-SHEAR-MODULUS-NOT-EXPORTED" not in {item["code"] for item in self.writer.diagnostics}
        self.text = self.writer.text
        self.data = self.text.encode("ascii")
        self.sidecar = {**{key: value for key, value in self.writer.to_dict().items() if key.endswith("_map")},
                        "mbf_sha256": hashlib.sha256(self.data).hexdigest()}
        self.bound = import_caepipe_mbf(self.data, sidecar=self.sidecar, material_provenance=INVENTED, source_label=name)
        self.printed = canon.read_printed(self.text)

    def kinds(self, model: dict) -> dict[str, str]:
        labels = {"Sustained (W+P)": "sustained", "Expansion (T1)": "expansion"}
        mapping = {}
        for case in model.get("load_cases") or []:
            label = case.get("label") or self.writer.load_case_map.get(case["id"])
            if label in labels:
                mapping[case["id"]] = labels[label]
        return mapping

    def reference(self) -> canon.Canonical:
        nu = {record["swbpipe_material"]: record["poisson_ratio"] for record in self.writer.material_map.values()}
        return canon.canonical(self.model, self.writer.node_map, self.kinds(self.model), oriented=True, writer_nu=nu)

    def imported(self, result, *, oriented: bool) -> canon.Canonical:
        names = {swb_id: name for name, swb_id in result.id_map["node_map"].items()}
        return canon.canonical(result.model, names, self.kinds(result.model), oriented=oriented)

    def limits(self, reference, *, residuals: bool = True):
        return canon.bounds(self.model, self.writer, self.printed, self.writer.node_map, reference, residuals=residuals)


@pytest.fixture(scope="module")
def trips() -> dict[str, Trip]:
    return {name: Trip(name, *MODELS[name]) for name in REVERSIBLE}


# --- (a) canonical equality, bound ----------------------------------------------------------------
@pytest.mark.parametrize("name", REVERSIBLE)
def test_bound_import_equals_the_source_within_the_derived_bounds(trips, name):
    trip = trips[name]
    assert trip.bound.status == "imported", trip.bound.diagnostics
    assert trip.bound.source["binding"] == "bound"
    reference = trip.reference()
    result = canon.compare(reference, trip.imported(trip.bound, oriented=True), trip.limits(reference))
    assert result.failures == []
    assert result.compared > 0


def test_every_excluded_loss_and_model_is_listed():
    assert len(canon.EXCLUDED_LOSSES) == 8
    assert set(EXCLUDED) == {"writer-bent-l-reversed"}
    trip = Trip("writer-bent-l-reversed", *([EXCLUDED["writer-bent-l-reversed"][0], "REVERSED L", 20.0]))
    reference = trip.reference()
    failures = canon.compare(reference, trip.imported(trip.bound, oriented=True), trip.limits(reference)).failures
    assert [item for item in failures if "'node')" in item]  # the far-node component is why it is excluded
    assert all("'node')" in item for item in failures)


# --- (a') unbound imports ----------------------------------------------------------------------------
@pytest.mark.parametrize("name", REVERSIBLE)
def test_unbound_import_under_pd1_equals_by_caepipe_name(trips, name):
    trip = trips[name]
    result = import_caepipe_mbf(trip.data, material_provenance=INVENTED, pressure_closure=unbound_closure(trip),
                                source_label=name)
    assert result.status == "imported", result.diagnostics
    assert any("PD-1" in note for note in result.assumptions)
    reference = trip.reference()
    reference_unoriented, limits = canon.unoriented(reference, trip.limits(reference))
    comparison = canon.compare(reference_unoriented, trip.imported(result, oriented=False), limits)
    assert comparison.failures == []


@pytest.mark.parametrize("name", REVERSIBLE)
def test_unbound_import_under_the_base_rule_gives_the_named_refusal(trips, name, monkeypatch):
    monkeypatch.setattr(importer_module, "PD1_VERSIONS", ())
    trip = trips[name]
    result = import_caepipe_mbf(trip.data, material_provenance=INVENTED, source_label=name)
    assert result.status == "refused" and result.model is None
    refused = [item for item in result.diagnostics if item["code"] == "MBF-IMPORT-TBD-17-04-007"]
    assert any("L=" in item["message"] for item in refused)  # the writer always writes L= on the first row
    has_force = any(record["mbf"] in ("FOR", "MOM") for record in trip.writer.load_map.values())
    assert any("without FLC" in item["message"] for item in refused) == has_force
    # With the bound sidecar the writer's conventions apply and the same bytes import.
    assert import_caepipe_mbf(trip.data, sidecar=trip.sidecar, material_provenance=INVENTED,
                              source_label=name).status == "imported"


# --- (b) identities ---------------------------------------------------------------------------------------
@pytest.mark.parametrize("name", REVERSIBLE)
def test_bound_import_restores_the_sidecar_identities_and_reports_the_rest(trips, name):
    trip = trips[name]
    source, imported = trip.model, trip.bound.model
    ids = lambda items: {item["id"] for item in items or []}  # noqa: E731
    exported_nodes = set(trip.writer.node_map)
    assert ids(imported["nodes"]) == exported_nodes
    assert {pipe["id"]: (pipe["from"], pipe["to"]) for pipe in imported["pipe_segments"]} == {
        pipe["id"]: (pipe["from"], pipe["to"]) for pipe in source["pipe_segments"]}
    assert {support["id"]: (support["node"], sorted(support["restraints"]), support.get("family"))
            for support in imported["supports"]} == {
        support["id"]: (support["node"], sorted(canon._DOF_TOKEN[token] for token in support["restraints"]),
                        support.get("family")) for support in source["supports"]}
    assert ids(imported["components"]) == ids(source.get("components"))
    assert ids(imported["materials"]) == {pipe["material"] for pipe in source["pipe_segments"]}
    assert ids(imported["load_cases"]) <= ids(source["load_cases"])
    unrecoverable = " ".join(item["location"] + " " + item["reason"] for item in trip.bound.loss_report
                             if item["code"] == "MBF-IMPORT-ID-UNRECOVERABLE")
    restored = {load["id"] for case in imported["load_cases"] for load in case["primitive_loads"]}
    for case in source["load_cases"]:
        for load in case.get("primitive_loads") or []:
            if load["magnitude"]["value"] == 0:
                continue
            assert load["id"] in restored or "keeps its formed id" in unrecoverable, load["id"]
    for pipe in source["pipe_segments"]:  # straight orientation travels in the sidecar
        if pipe.get("y_reference") is not None and pipe["id"] not in {
                component["geometry"]["bend_pipe_ref"] for component in source.get("components") or []}:
            restored = next(item for item in imported["pipe_segments"] if item["id"] == pipe["id"])
            assert restored["y_reference"] == {axis: float(pipe["y_reference"][axis]) for axis in "xyz"}
    for component in imported["components"]:  # the component's tangent node is not in the sidecar
        assert f"bend {component['label'].split()[-1]}" in unrecoverable
    assert "not export" in unrecoverable


def test_summed_primitives_are_many_to_one_and_reported():
    model = writer_tests.cantilever()
    model["load_cases"][0]["primitive_loads"].append(writer_tests.force("tip2", "N1", "global_y", -1000.0))
    trip = Trip("summed", model, "SUMMED", 20.0)
    loads = trip.bound.model["load_cases"][0]["primitive_loads"]
    assert [(load["id"], load["magnitude"]["value"]) for load in loads] == [
        ("load:concentrated_force:N1:global_y", -7000.0)]
    assert any(item["code"] == "MBF-IMPORT-ID-UNRECOVERABLE" and item["location"] == loads[0]["id"]
               for item in trip.bound.loss_report)


def test_merged_anchor_is_split_back_by_the_sidecar():
    model = writer_tests.cantilever()
    model["supports"] = [{"id": "T", "node": "N0", "restraints": ["UX", "UY", "UZ"], "family": None},
                         {"id": "R", "node": "N0", "restraints": ["RX", "RY", "RZ"]}]
    trip = Trip("split", model, "SPLIT", 20.0)
    assert "KA" in trip.text.split("\r\n")[trip.text.split("\r\n").index("LAYOUT") + 1]
    supports = {support["id"]: support["restraints"] for support in trip.bound.model["supports"]}
    assert supports == {"T": ["UX", "UY", "UZ"], "R": ["RX", "RY", "RZ"]}
    unbound = import_caepipe_mbf(trip.data, material_provenance=INVENTED, source_label="split")
    assert [(support["id"], support["family"]) for support in unbound.model["supports"]] == [("support:10", "anchor")]


def test_a_sidecar_without_family_reports_the_family_unrecoverable():
    trip = Trip("old-sidecar", writer_tests.cantilever(), "OLD", 20.0)
    sidecar = deepcopy(trip.sidecar)
    for entry in sidecar["support_map"].values():
        del entry["family"]
    result = import_caepipe_mbf(trip.data, sidecar=sidecar, material_provenance=INVENTED, source_label="old")
    assert any(item["code"] == "MBF-IMPORT-ID-UNRECOVERABLE" and "family" in item["reason"]
               for item in result.loss_report)


def regions(model: dict) -> list[tuple]:
    return [(case["id"], region["id"], region["member_pipe_ids"], region["terminals"])
            for case in model["load_cases"] for region in case.get("pressure_regions") or []]


@pytest.mark.parametrize("name", sorted(PRESSURE_MODELS))
def test_bound_import_restores_the_pressure_contract_and_regions(trips, name):
    trip = trips[name]
    imported = trip.bound.model
    assert imported["pressure_contract"] == trip.model["pressure_contract"]
    assert regions(imported) == regions(trip.model)  # ids, member order, terminals, closure and their provenance
    assert all(case.get("pressure_regions") is not None for case in imported["load_cases"])
    assert all(pipe["section"]["corrosion_allowance"]["value"] == 0.0 for pipe in imported["pipe_segments"])


def test_the_shear_model_travels_only_in_the_sidecar():
    trip = Trip("timoshenko", writer_tests.pressurized_l(shear="timoshenko_annulus_energy_v1"), "TIMOSHENKO", 20.0)
    assert trip.bound.model["pressure_contract"]["shear_model"] == "timoshenko_annulus_energy_v1"
    unbound = import_caepipe_mbf(trip.data, material_provenance=INVENTED, pressure_closure=CLOSURE, source_label="t")
    assert unbound.model["pressure_contract"]["shear_model"] == "euler_bernoulli"
    assert "MBF-SI-SHEAR-MODEL-NOT-EXPORTED" in {item["code"] for item in trip.writer.loss_report}


def test_a_pressure_map_that_does_not_match_the_file_is_refused(trips):
    trip = trips["pressure-tee-bar"]
    for change in ("merge", "drop", "terminal"):
        sidecar = deepcopy(trip.sidecar)
        stored = sidecar["pressure_map"]["regions"]
        if change == "merge":  # one region over two legs at a tee: members still pressurized, but owned twice
            stored[1]["members"] = stored[0]["members"] + stored[1]["members"]
        elif change == "drop":  # a pressurized leg in no region
            stored.pop()
        else:
            stored[0]["terminals"][0]["closure_transfer"] = "open"
        result = import_caepipe_mbf(trip.data, sidecar=sidecar, material_provenance=INVENTED, source_label="tamper")
        assert result.status == "refused", change
        assert any(item["code"] == "MBF-IMPORT-SIDECAR-CONFLICT" and item["location"] == "pressure_map"
                   for item in result.diagnostics), change


def test_the_pressure_bound_is_half_a_unit_of_the_printed_bar_value(trips):
    # 150 psi = 150 x 4.4482216152605 / 0.00064516 Pa = 1034213.5939752541... Pa, printed as 10.34213594 bar.
    # delta(10.34213594) = 0.5e-8 bar = 5e-4 Pa, plus 4 eps |p|; the import reads 1034213.594 Pa.
    trip = trips["pressure-us-psi"]
    lines = trip.text.split("\r\n")
    assert lines[lines.index("LOADS") + 1] == "L1,120,10.34213594,0"  # T1 = 20 C + 180 degF x 5/9
    reference = trip.reference()
    key = next(key for key in reference.values if key[0] == "pressure")
    assert reference.values[key] == float(150 * Fraction("4.4482216152605") / Fraction("0.00064516"))
    imported = trip.imported(trip.bound, oriented=True)
    assert imported.values[key] == 1034213.594
    limit = trip.limits(reference)[key]
    assert limit == pytest.approx(5e-4 + 4 * canon.EPS * 10.34213594 * 1e5, rel=1e-12)
    assert abs(imported.values[key] - reference.values[key]) < limit


def test_z_vertical_positions_are_the_exact_rotation_of_the_printed_coordinates():
    # The test's own exact sum of the printed offsets, rotated (X, Y, Z) -> (X, Z, -Y) and rounded once, equals
    # every imported position bit for bit.
    lines = ("INVENTED ROTATION", "VERSION", "15.10", "OPTIONS", "HGRA,SI,Z", "OPTEMP", "20", "MATERIAL",
             "M1,0,0.3,1,1,CS,invented", "M1,20,200000,1.2e-05", "PIPE", "P1,168.3,7.11,0,0,0,0,0,0", "LOADS",
             "L1,20,0,0", "LAYOUT", "F10,KA,MM1,PP1,X0.1,Y-0.2,Z0.3,CL=L1", "T20,X1000.1,Y2000.2,Z-3000.3",
             "T30,X0.7,Y0.1,Z0.2", "T40,KA,Y-1e-3")
    text = "".join(line + "\r\n" for line in lines)
    result = import_caepipe_mbf(text.encode("ascii"), material_provenance=INVENTED, source_label="rotation")
    assert result.status == "imported", result.diagnostics
    expected = {name: tuple(float(value) for value in canon.rotate_z_vertical(position))
                for name, position in canon.printed_positions(text).items()}
    assert {node["label"]: tuple(node["position"].values()) for node in result.model["nodes"]} == expected
    assert expected["20"] == (1000.2, -3000.0, -2000.0)  # (0.1 + 1000.1, 0.3 - 3000.3, -(-0.2 + 2000.2))


# --- (c) byte reproduction ---------------------------------------------------------------------------
def collisions(original: str, rewritten: str | None) -> list[str]:
    """Every field of W that writer(I) prints differently, by line and field."""
    if rewritten is None:
        return ["writer(I) refused"]
    a, b = original.split("\r\n"), rewritten.split("\r\n")
    found = [f"line count {len(a)} != {len(b)}"] if len(a) != len(b) else []
    for number, (left, right) in enumerate(zip(a, b), start=1):
        for index, (x, y) in enumerate(zip(left.split(","), right.split(",")), start=1):
            if x != y:
                found.append(f"line {number} field {index}: {x!r} -> {y!r}")
        if left.count(",") != right.count(","):
            found.append(f"line {number}: field count differs")
    return found


@pytest.mark.parametrize("name", REVERSIBLE)
def test_byte_reproducible_models_are_written_again_byte_for_byte(trips, name):
    trip = trips[name]
    imported = trip.bound.model
    t_ref = float(canon.read_printed(trip.text).t_ref)  # the imported OPTEMP value; the writer takes it as an argument
    again = render_caepipe_mbf_si(imported, title=imported["project"]["name"], reference_temperature_c=t_ref,
                                  max_layout_rows=20)
    found = collisions(trip.text, again.text)
    if name in BYTE_REPRODUCIBLE:
        assert found == [], found
        assert again.text.encode("ascii") == trip.data
    else:
        assert found  # reported, never absorbed


def test_a_formatting_collision_is_reported_by_line_and_field():
    assert collisions("A,1\r\nB,2.5", "A,1\r\nB,2.6") == ["line 2 field 2: '2.5' -> '2.6'"]
    assert collisions("A", None) == ["writer(I) refused"]


# --- (d) solve equality ---------------------------------------------------------------------------------
SI_RESULT = {"m": 1.0, "mm": 1e-3, "rad": 1.0, "deg": math.pi / 180.0, "N": 1.0, "kN": 1e3, "N*m": 1.0, "kN*m": 1e3}
FAMILIES = {"global_nodal_displacement": "translation", "global_nodal_rotation": "rotation"}


def result_table(output) -> dict[str, dict[tuple, float]]:
    families: dict[str, dict[tuple, float]] = {}
    for row in output["payload"]["mechanics_envelope"]["results"]:
        kind = row.get("kind", "")
        if kind.startswith("global_nodal_displacement_") or kind.startswith("global_nodal_rotation_"):
            family = FAMILIES[kind.rsplit("_", 1)[0]]
        elif kind == "support_reaction_component_v2":
            family = "reaction_" + (row.get("metadata") or {}).get("component", "?")[0]
        else:
            continue
        key = (kind, row.get("entity_ref"), (row.get("basis_ref") or {}).get("ref_id"),
               (row.get("metadata") or {}).get("component"))
        families.setdefault(family, {})[key] = row["value"] * SI_RESULT[row["unit"]]
    return families


def runner_binary() -> str:
    runner = os.environ.get("OPENPIPESTRESS_RUNNER_BIN")
    if not runner or not Path(runner).is_file():
        pytest.skip("the headless runner (OPENPIPESTRESS_RUNNER_BIN) is not available in this session")
    return runner


def oriented(model: dict) -> dict:
    """The source model A as the solve accepts it: an explicit y_reference on every pipe that lacks one (global Y,
    or global X for a pipe along Y) and a provenance string on every record that lacks one; the writer-test models
    omit both. The import needs no such help: it assigns the documented local y (MBF-IMPORT-ORIENTATION-DEFAULTED)."""
    model = deepcopy(model)
    records = [*model["nodes"], *model["pipe_segments"], *model["supports"], *(model.get("materials") or []),
               *(model.get("components") or []), *(model.get("load_cases") or []),
               *(load for case in model.get("load_cases") or [] for load in case.get("primitive_loads") or [])]
    for record in records:
        record.setdefault("provenance", "invented round-trip test model; not engineering data")
    nodes = {node["id"]: node["position"] for node in model["nodes"]}
    for pipe in model["pipe_segments"]:
        if pipe.get("y_reference") is None:
            a, b = nodes[pipe["from"]], nodes[pipe["to"]]
            along_y = a["x"] == b["x"] and a["z"] == b["z"]
            pipe["y_reference"] = {"x": 1.0, "y": 0.0, "z": 0.0} if along_y else {"x": 0.0, "y": 1.0, "z": 0.0}
    return model


@pytest.mark.parametrize("name", REVERSIBLE)
def test_solves_of_source_and_bound_import_agree_within_the_provisional_threshold(trips, name):
    trip = trips[name]
    reference = trip.reference()
    r_in = canon.compare(reference, trip.imported(trip.bound, oriented=True), trip.limits(reference)).r_in
    if name in SOLVE_EXCLUDED:
        pytest.skip(f"{name} is excluded from solve equality: {SOLVE_EXCLUDED[name]}")
    if r_in > SOLVE_R_IN_LIMIT:
        pytest.skip(f"{name} is excluded from solve equality: r_in = {r_in:.3g} > {SOLVE_R_IN_LIMIT}")
    runner = runner_binary()
    _, source, error = solve_swbpipe(runner, {"case_id": name, "model": oriented(trip.model)})
    assert error == ""
    _, imported, error = solve_swbpipe(runner, {"case_id": name, "model": trip.bound.model})  # as imported
    assert error == ""
    a, b = result_table(source), result_table(imported)
    assert set(a) == set(b)
    for family, rows in a.items():
        assert set(rows) == set(b[family]), family
        scale = max(abs(value) for value in rows.values())
        threshold = SOLVE_THRESHOLD_FACTOR * r_in * scale
        worst = max(abs(rows[key] - b[family][key]) for key in rows)
        assert worst <= threshold, (family, worst, threshold)


def test_the_bend_boundary_case_is_excluded_from_solve_equality(trips):
    trip = trips["bend-boundary"]
    reference = trip.reference()
    assert canon.compare(reference, trip.imported(trip.bound, oriented=True), trip.limits(reference)).r_in > SOLVE_R_IN_LIMIT


def test_the_runtime_admits_every_region_the_importer_forms():
    # Judged by the exact route itself (VER-002 r1 and r2): Codex's run whose first two straights fail alone, the
    # zigzag run, and a corner each import and solve; the drifting run the importer refuses is refused by the route
    # too (PRESSURE_REGION_NONCOLLINEAR) when authored as one region.
    runner = runner_binary()
    files = {"nonmonotonic": ("F10,KA,MM1,PP1,CL=L1", *importer_tests.NONMONOTONIC),
             "zigzag": ("F10,KA,MM1,PP1,CL=L1", *importer_tests.ZIGZAG),
             "corner": ("F10,KA,MM1,PP1,CL=L1", "T20,X1000", "T30,KA,X1000,Y2"),
             "reversed": importer_tests.REVERSED}  # VER-002 r3: emitted 30 -> 10, the order the route admits
    for name, rows in files.items():
        result = importer_tests.run(importer_tests.mbf(*rows, pipe=("P1,168.3,7.11,0",), loads=("L1,20,10,0",)),
                                    pressure_closure=importer_tests.CLOSURE)
        assert result.status == "imported", result.diagnostics
        _, _, error = solve_swbpipe(runner, {"case_id": name, "model": result.model})
        assert error == "", name
    drift = importer_tests.run(importer_tests.mbf("F10,KA,MM1,PP1,CL=L1", *importer_tests.DRIFT)).model
    drift["pressure_contract"] = {"version": "3.0.0", "mode": "exact_pressure_v3", "shear_model": "euler_bernoulli"}
    for pipe in drift["pipe_segments"]:
        pipe["section"]["corrosion_allowance"] = {"value": 0.0, "unit": "mm"}
    drift["load_cases"] = [{"id": "case:p", "label": "Sustained (W+P)", "kind": "sustained", "status": "draft",
                            "primitive_loads": [], "provenance": "invented", "pressure_regions": [
        {"id": "region:drift", "member_pipe_ids": [pipe["id"] for pipe in drift["pipe_segments"]],
         "pressure_basis": "internal_differential_zero_external_v1", "pressure": {"value": 10.0, "unit": "bar"},
         "provenance": "invented", "terminals": [
             {"node_ref": node, "closure_transfer": "transfers_to_wall", "provenance": "invented"}
             for node in ("node:10", "node:170")]}]}]
    _, output, error = solve_swbpipe(runner, {"case_id": "drift-one-region", "model": drift})
    assert error and "PRESSURE_REGION_NONCOLLINEAR" in json.dumps(output)
    # The reversed run as the file orders it (10 -> 30) is refused by the route; and Codex's equal-decimal bores
    # (VER-002 r3), which the importer refuses, are refused by the route as one region too.
    for name, rows, pipes, code in (
            ("reversed-file-order", importer_tests.REVERSED, ("P1,168.3,7.11,0",), "PRESSURE_REGION_NONCOLLINEAR"),
            ("bores", importer_tests.BORE_ROWS, importer_tests.BORE_PIPES, "PRESSURE_REGION_BORE_MISMATCH")):
        model = importer_tests.run(importer_tests.mbf(*rows, pipe=pipes)).model
        model["pressure_contract"] = drift["pressure_contract"]
        for pipe in model["pipe_segments"]:
            pipe["section"]["corrosion_allowance"] = {"value": 0.0, "unit": "mm"}
        region = deepcopy(drift["load_cases"][0])
        region["pressure_regions"][0]["member_pipe_ids"] = [pipe["id"] for pipe in model["pipe_segments"]]
        for terminal, node in zip(region["pressure_regions"][0]["terminals"], ("node:10", "node:30")):
            terminal["node_ref"] = node
        model["load_cases"] = [region]
        _, output, error = solve_swbpipe(runner, {"case_id": name, "model": model})
        assert error and code in json.dumps(output), name


def test_an_import_whose_allowance_is_deleted_is_not_round_tripped_with_an_authored_zero():
    # Codex VER-002 r2 item 2: import a pressure MBF with P1,168.3,7.11,0, delete the allowance, export.
    data = importer_tests.mbf("F10,KA,MM1,PP1,CL=L1", "T20,KA,X3000", pipe=("P1,168.3,7.11,0",), loads=("L1,20,10,0",))
    imported = importer_tests.run(data, pressure_closure=importer_tests.CLOSURE)
    assert imported.status == "imported", imported.diagnostics
    model = deepcopy(imported.model)
    del model["pipe_segments"][0]["section"]["corrosion_allowance"]
    written = render_caepipe_mbf_si(model, title="NO ALLOWANCE")
    assert written.status == "refused" and written.text is None
    assert {item["code"] for item in written.diagnostics if item["severity"] == "error"} == {
        "MBF-SI-CORROSION-ALLOWANCE-MISSING"}
    assert render_caepipe_mbf_si(imported.model, title="WITH ALLOWANCE").status == "written"


# VER-002 r4: two regions the model's values admit but the writer's 10-digit print would not. (a) Bores: 168.30000004
# - 2 x 7.11000002 = 154.08 = 170.3 - 2 x 8.11, and in m both radii are 0.07704; printed, P1 becomes 168.3, 7.11000002.
# (b) Geometry: offsets (1000.0000004, 2000.0000008) then (1999.9999996, 3999.9999992), collinear as read; printed to
# 10 digits, the run is not.
FORMAT_CASES = {
    "bores": (("P1,168.30000004,7.11000002,0", "P2,170.3,8.11,0"),
              ("F10,KA,MM1,PP1,CL=L1", "T20,X1000", "T30,KA,X1000,PP2"), "MBF-IMPORT-PRESSURE-BORE-MISMATCH"),
    "geometry": (("P1,168.3,7.11,0",), ("F10,KA,MM1,PP1,CL=L1", "T20,X1000.0000004,Y2000.0000008",
                                        "T30,KA,X1999.9999996,Y3999.9999992"), "MBF-IMPORT-PRESSURE-RUN-NONCOLLINEAR"),
}


def format_case(name: str):
    pipes, rows, _ = FORMAT_CASES[name]
    result = importer_tests.run(importer_tests.mbf(*rows, pipe=pipes, loads=("L1,20,10,0",)),
                                pressure_closure=importer_tests.CLOSURE)
    assert result.status == "imported", result.diagnostics
    assert [region["id"] for region in result.model["load_cases"][0]["pressure_regions"]] == ["region:mbf-10-30"]
    return result.model


@pytest.mark.parametrize("name", sorted(FORMAT_CASES))
def test_the_writer_refuses_a_region_its_printed_values_would_break(name, monkeypatch):
    model = format_case(name)
    written = render_caepipe_mbf_si(model, title="FORMAT")
    assert written.status == "refused" and written.text is None
    errors = [item for item in written.diagnostics if item["severity"] == "error"]
    assert {(item["code"], item["entity"]) for item in errors} == {
        ("MBF-SI-PRESSURE-REGION-FORMAT", "region:region:mbf-10-30")}
    assert any(item["code"] == "MBF-SI-PRESSURE-REGION-FORMAT" for item in written.loss_report)
    # Without the preflight, the bound import of the printed file refuses the restored region by name, in its
    # declared order, without cutting it.
    from core.handoff.caepipe_mbf import si_writer
    monkeypatch.setattr(si_writer._Writer, "survives_reimport", lambda self, result: True)
    unchecked = render_caepipe_mbf_si(model, title="FORMAT")
    data = unchecked.text.encode("ascii")
    sidecar = {**{key: value for key, value in unchecked.to_dict().items() if key.endswith("_map")},
               "mbf_sha256": hashlib.sha256(data).hexdigest()}
    bound = import_caepipe_mbf(data, sidecar=sidecar, material_provenance=INVENTED, source_label=name)
    assert bound.status == "refused" and bound.source["binding"] == "bound"
    assert {(item["code"], item["location"]) for item in bound.diagnostics if item["severity"] == "error"} == {
        (FORMAT_CASES[name][2], "pressure_map region region:mbf-10-30")}


def test_the_runtime_solves_the_format_cases_as_imported():
    runner = runner_binary()
    for name in FORMAT_CASES:
        _, _, error = solve_swbpipe(runner, {"case_id": name, "model": format_case(name)})
        assert error == "", name


# --- VER-002 r5: the closed guard set ----------------------------------------------------------------------------------
TEE_ROWS = ("F10,KA,MM1,PP1,CL=L1", "T20,X1000", "T30,KA,X1000", "F20", "T40,KA,Y1000")


def bound_parts(model: dict, monkeypatch=None):
    """The writer's text and byte-bound sidecar for `model`, with the preflight bypassed when `monkeypatch` is given."""
    if monkeypatch is not None:
        from core.handoff.caepipe_mbf import si_writer
        monkeypatch.setattr(si_writer._Writer, "survives_reimport", lambda self, result: True)
    written = render_caepipe_mbf_si(model, title="GUARD")
    assert written.status == "written", written.diagnostics
    data = written.text.encode("ascii")
    return data, {**{key: value for key, value in written.to_dict().items() if key.endswith("_map")},
                  "mbf_sha256": hashlib.sha256(data).hexdigest()}


def refusals(result) -> set[tuple[str, str]]:
    return {(item["code"], item["location"]) for item in result.diagnostics if item["severity"] == "error"}


def test_a_restored_region_through_a_tee_is_refused_by_name_and_by_the_route():
    # Codex's case: the tee imports as three regions; a sidecar joining 10-20-30 passes through 20, where 20-40 joins.
    model = importer_tests.run(importer_tests.mbf(*TEE_ROWS, loads=("L1,20,10,0",)),
                               pressure_closure=importer_tests.CLOSURE).model
    assert [region["id"] for region in model["load_cases"][0]["pressure_regions"]] == [
        "region:mbf-10-20", "region:mbf-20-30", "region:mbf-20-40"]
    data, sidecar = bound_parts(model)
    stored = sidecar["pressure_map"]["regions"]
    stored[0]["members"] = stored[0]["members"] + stored[1]["members"]
    stored[0]["terminals"][1] = stored[1]["terminals"][1]
    del stored[1]
    bound = import_caepipe_mbf(data, sidecar=sidecar, material_provenance=INVENTED, source_label="tee")
    assert refusals(bound) == {("MBF-IMPORT-PRESSURE-INTERNAL-BRANCH", "pressure_map region region:mbf-10-20")}
    joined = deepcopy(model)  # the same region authored in the model: the writer refuses it, and so does the route
    regions = joined["load_cases"][0]["pressure_regions"]
    regions[0]["member_pipe_ids"] += regions[1]["member_pipe_ids"]
    regions[0]["terminals"][1] = regions[1]["terminals"][1]
    del regions[1]
    written = render_caepipe_mbf_si(joined, title="TEE")
    assert written.status == "refused"
    assert {item["code"] for item in written.diagnostics if item["severity"] == "error"} == {"MBF-SI-PREFLIGHT-REFUSED"}
    assert "MBF-IMPORT-PRESSURE-INTERNAL-BRANCH" in " ".join(item["message"] for item in written.diagnostics)
    _, output, error = solve_swbpipe(runner_binary(), {"case_id": "tee-joined", "model": joined})
    assert error and "PRESSURE_REGION_INTERNAL_BRANCH" in json.dumps(output)


def test_the_preflight_refuses_any_failed_reimport_with_its_code():
    # Codex's case: OD 100.00000004 and wall 50 import (2t < OD) and solve; printed, the OD is 100 = 2t.
    data = importer_tests.mbf("F10,KA,MM1,PP1,CL=L1", "T20,KA,X1000", pipe=("P1,100.00000004,50,0",),
                              loads=("L1,20,10,0",))
    model = importer_tests.run(data, pressure_closure=importer_tests.CLOSURE).model
    _, _, error = solve_swbpipe(runner_binary(), {"case_id": "thin-od", "model": model})
    assert error == ""
    written = render_caepipe_mbf_si(model, title="THIN")
    assert written.status == "refused" and written.text is None
    errors = [item for item in written.diagnostics if item["severity"] == "error"]
    assert {item["code"] for item in errors} == {"MBF-SI-PREFLIGHT-REFUSED"}
    assert any("MBF-IMPORT-VALUE-OUT-OF-RANGE" in item["message"] for item in errors)


def renamed(model: dict, names: dict[str, str]) -> dict:
    text = json.dumps(model)
    for old, new in names.items():
        text = text.replace(f'"{old}"', f'"{new}"')
    return json.loads(text)


def test_ids_equal_once_colons_read_as_hyphens_are_refused(monkeypatch):
    # The route's check_suffixes reads ':' as '-' per kind (EXACT_PRESSURE_RESULT_ID_COLLISION): pipes P:1 and P-1.
    model = renamed(writer_tests.pressurized_l(), {"S1": "P:1", "S2": "P-1"})
    written = render_caepipe_mbf_si(model, title="IDS")
    assert written.status == "refused"
    assert "MBF-IMPORT-PRESSURE-ID-COLLISION" in " ".join(item["message"] for item in written.diagnostics)
    data, sidecar = bound_parts(model, monkeypatch)
    bound = import_caepipe_mbf(data, sidecar=sidecar, material_provenance=INVENTED, source_label="ids")
    assert refusals(bound) == {("MBF-IMPORT-PRESSURE-ID-COLLISION", "pipe P:1, P-1")}


def test_restored_region_ids_must_be_present_and_unique(trips):
    trip = trips["pressure-tee-bar"]
    for change in ("empty", "duplicate"):
        sidecar = deepcopy(trip.sidecar)
        stored = sidecar["pressure_map"]["regions"]
        stored[1]["id"] = " " if change == "empty" else stored[0]["id"]
        result = import_caepipe_mbf(trip.data, sidecar=sidecar, material_provenance=INVENTED, source_label=change)
        assert result.status == "refused"
        assert ("MBF-IMPORT-SIDECAR-CONFLICT", "pressure_map") in refusals(result), change


def test_a_restored_orientation_the_frame_cannot_use_takes_the_documented_one():
    # frame_kernel: the y_reference's part perpendicular to the axis must exceed 1e-12; one along the axis has none.
    trip = Trip("parallel", writer_tests.cantilever(), "PARALLEL", 20.0)
    sidecar = deepcopy(trip.sidecar)
    sidecar["element_map"]["S1"]["y_reference"] = {"x": 2.0, "y": 0.0, "z": 0.0}  # S1 runs along +x
    result = import_caepipe_mbf(trip.data, sidecar=sidecar, material_provenance=INVENTED, source_label="parallel")
    assert result.model["pipe_segments"][0]["y_reference"] == {"x": 0.0, "y": 1.0, "z": 0.0}
    assert "MBF-IMPORT-ORIENTATION-DEFAULTED" in {item["code"] for item in result.diagnostics}
    assert importer_module.frame_y_reference_usable((0, 0, 0), (3, 0, 0), (0.0, 1e-12, 0.0)) is False
    assert importer_module.frame_y_reference_usable((0, 0, 0), (3, 0, 0), (0.0, 2e-12, 0.0)) is True


# --- (e) determinism ----------------------------------------------------------------------------------
@pytest.mark.parametrize("name", REVERSIBLE)
def test_importing_twice_gives_identical_bytes(trips, name):
    trip = trips[name]
    again = import_caepipe_mbf(trip.data, sidecar=deepcopy(trip.sidecar), material_provenance=dict(INVENTED),
                               source_label=name)
    assert again.model_bytes() == trip.bound.model_bytes()
    assert again.report_bytes() == trip.bound.report_bytes()
    assert again.id_map_bytes() == trip.bound.id_map_bytes()


# --- bend boundary case (§18.1 item 5) ---------------------------------------------------------------------
def test_bend_boundary_residuals_are_covered_only_with_the_residual_term(trips):
    trip = trips["bend-boundary"]
    assert trip.writer.diagnostics == [] or all(item["severity"] != "error" for item in trip.writer.diagnostics)
    residuals = canon.bend_residuals(trip.model, "BEND")
    assert residuals["tangent_near"] == pytest.approx(8.991e-10, rel=1e-3)  # 8.991e-7 mm in m
    reference = trip.reference()
    imported = trip.imported(trip.bound, oriented=True)
    near = trip.writer.node_map["N"]
    shift = abs(imported.values[("node", near, 0)] - reference.values[("node", near, 0)])
    assert 8e-10 < shift < 1e-9  # about 9e-7 mm
    assert canon.compare(reference, imported, trip.limits(reference)).failures == []
    without = canon.compare(reference, imported, trip.limits(reference, residuals=False)).failures
    assert any(f"'{near}', 0)" in item for item in without)


def test_bend_plane_compares_by_projection_perpendicular_to_the_chord(trips):
    # The invented y_reference (2, 0, 0) on the L bend reconstructs as (1, 0, -1)/sqrt(2): 45 degrees apart raw,
    # the same projected direction.
    model = writer_tests.bent_l(y_reference=(2.0, 0.0, 0.0))
    trip = Trip("projection", model, "PROJECTION", 20.0)
    plane = trip.bound.model["pipe_segments"][1]["y_reference"]
    assert (plane["x"], plane["y"], plane["z"]) == pytest.approx((math.sqrt(0.5), 0.0, -math.sqrt(0.5)), abs=1e-15)
    reference = trip.reference()
    assert canon.compare(reference, trip.imported(trip.bound, oriented=True), trip.limits(reference)).failures == []


# --- tolerance regressions with hand-derived values ----------------------------------------------------------
def test_delta_is_half_a_unit_in_the_tenth_significant_digit():
    assert canon.delta("0") == 0.0
    assert canon.delta("20.12345679") == pytest.approx(5e-9, rel=1e-12)  # floor(log10 20.1) = 1: 0.5e-8
    assert canon.delta("3000") == pytest.approx(5e-7, rel=1e-12)
    assert canon.delta("1e-05") == pytest.approx(5e-15, rel=1e-12)
    assert canon.delta("100") == pytest.approx(5e-8, rel=1e-12)  # exactly a power of ten
    assert canon.delta("-0.5729577951") == pytest.approx(5e-11, rel=1e-12)


def test_small_delta_t_has_an_absolute_bound_only():
    # Design §18.2 example: dT 0.123456789 C at 20 C prints T1 = 20.12345679; the import returns about 1e-9 C off.
    model = writer_tests.cantilever()
    model["load_cases"].append({"id": "case:th", "primitive_loads": [
        {"id": "dt", "category": "thermal", "target": {"type": "element", "pipe": "S1"}, "direction": "global_x",
         "magnitude": writer_tests.q(0.123456789, "degC"), "dimension": "temperature_interval"}]})
    trip = Trip("small-dt", model, "SMALL DT", 20.0)
    assert "L1,20.12345679,0,0" in trip.text.split("\r\n")
    reference = trip.reference()
    imported = trip.imported(trip.bound, oriented=True)
    key = ("load", "expansion", "thermal", ("10", "20"))
    error = abs(imported.values[key] - reference.values[key])
    assert error == pytest.approx(1e-9, rel=0.05)
    assert error / 0.123456789 > 5e-9  # about 8e-9 relative: a relative bound would be meaningless here
    # delta(20.12345679) = 5e-9 and delta(20) = 0.5e-8 by the 10-digit formula (§18.2), plus 4 eps |T1|.
    assert trip.limits(reference)[key] == pytest.approx(5e-9 + 5e-9 + 4 * canon.EPS * 20.12345679, rel=1e-12)
    assert canon.compare(reference, imported, trip.limits(reference)).failures == []


def test_weight_per_length_bound_is_the_documented_relative_sum():
    trip = Trip("weight", weighted(), "WEIGHT", 20.0)
    reference = trip.reference()
    key = ("load", "sustained", "weight", ("10", "20"))
    od, t = 168.3, 7.11
    area = math.pi / 4 * (od**2 - (od - 2 * t) ** 2)
    expected = (canon.delta("7850") / 7850 + (math.pi * t * 5e-8 + math.pi * (od - 2 * t) * 5e-10) / area
                + 8 * canon.EPS) * abs(reference.values[key])
    assert trip.limits(reference)[key] == pytest.approx(expected, rel=1e-12)


def test_g_bound_adds_the_writer_agreement_threshold_when_both_were_authored():
    trip = Trip("nu-and-g", both_given_material(), "NU AND G", 20.0)
    reference = trip.reference()
    key = ("pipe", ("10", "20"), "G")
    expected = (1e-9 + canon.delta("200000") / 200000 + canon.delta("0.25") / 1.25 + 8 * canon.EPS) * 8.0e10
    assert trip.limits(reference)[key] == pytest.approx(expected, rel=1e-12)


# --- units check, independent of the writer (§18.1 item 4) -----------------------------------------------------
INCH = Fraction("0.0254")
LBF = Fraction("4.4482216152605")
POUND = Fraction("0.45359237")


def own_length(text: str) -> Fraction:
    """The test's own evaluation of the two feet-inch forms in the English fixture."""
    text = text.replace("\u2019", "'").replace("\u201d", '"').rstrip('"')
    feet, _, rest = text.partition("'")
    inches, _, fraction = rest.partition("-")
    value = Fraction(int(feet) * 12 + int(inches))
    if fraction:
        numerator, denominator = fraction.split("/")
        value += Fraction(int(numerator), int(denominator))
    return value


def fixture(stem: str):
    path = FIXTURES / f"{stem}.mbf"
    declaration = json.loads((FIXTURES / f"{stem}.provenance.json").read_text(encoding="utf-8"))
    return path.read_bytes(), declaration


def test_si_fixture_values_are_the_exact_conversions_of_the_english_fixture():
    english = fixture("units_english")[0].decode("utf-8").splitlines()
    si = fixture("units_si")[0].decode("ascii").splitlines()

    def close(printed: str, exact: Fraction) -> bool:
        decimals = len(printed.partition(".")[2].lower().partition("e")[0])
        exponent = int(printed.lower().partition("e")[2] or 0)
        return abs(Fraction(printed) - exact) <= Fraction(1, 2) * Fraction(10) ** (exponent - decimals)

    e_mat, s_mat = english[english.index("MATERIAL") + 1].split(","), si[si.index("MATERIAL") + 1].split(",")
    assert close(s_mat[1], Fraction(e_mat[1]) * POUND / INCH**3)  # lbf/in3 -> kgf/m3
    e_row, s_row = english[english.index("MATERIAL") + 2].split(","), si[si.index("MATERIAL") + 2].split(",")
    assert close(s_row[2], Fraction(e_row[2]) * LBF / INCH**2 / 10**6)  # psi -> N/mm2
    assert close(s_row[3], Fraction(e_row[3]) * Fraction(9, 5))  # 1/degF -> 1/degC
    assert close(s_row[1], (Fraction(e_row[1]) - 32) * Fraction(5, 9))
    e_pipe, s_pipe = english[english.index("PIPE") + 1].split(","), si[si.index("PIPE") + 1].split(",")
    for index in (1, 2):
        assert close(s_pipe[index], Fraction(e_pipe[index]) * 254 / 10)  # in -> mm
    e_layout, s_layout = english[english.index("LAYOUT") + 3:], si[si.index("LAYOUT") + 3:]
    assert close(s_layout[0].split(",")[1][1:], own_length(e_layout[0].split(",")[1][1:]) * 254 / 10)
    assert close(s_layout[1].split(",")[1][1:], own_length(e_layout[1].split(",")[1][1:]) * 254 / 10)
    assert close("4448.2216152605", 1000 * LBF) and "FOR(0,-4448.2216152605,0)" in s_layout[0]
    assert close("677.9089741657002", 500 * Fraction("0.3048") * LBF) and "MOM(0,0,677.9089741657002)" in s_layout[0]
    assert "D(0,12.7,0)" in s_layout[1] and "D(0,0.5,0)" in e_layout[1]


def test_english_positions_equal_the_tests_own_rational_evaluation():
    data, declaration = fixture("units_english")
    result = import_caepipe_mbf(data, material_provenance=declaration["material_provenance"], source_label="english")
    assert result.status == "imported", result.diagnostics
    x = own_length("10'6\"")
    z = own_length("7\u20193-1/4\u201d")
    assert (x, z) == (Fraction(126), Fraction(349, 4))
    assert [tuple(node["position"].values()) for node in result.model["nodes"]] == [
        (0.0, 0.0, 0.0), (float(x), 0.0, 0.0), (float(x), 0.0, float(z))]
    assert result.model["project"]["units"]["length"] == "in"


def test_english_and_si_imports_of_one_model_agree():
    imports = {}
    for stem in ("units_english", "units_si"):
        data, declaration = fixture(stem)
        imports[stem] = import_caepipe_mbf(data, material_provenance=declaration["material_provenance"], source_label=stem)
        assert imports[stem].status == "imported", imports[stem].diagnostics
    forms = {}
    for stem, result in imports.items():
        names = {swb_id: name for name, swb_id in result.id_map["node_map"].items()}
        kinds = {case["id"]: "sustained" if case["kind"] == "sustained" else "expansion"
                 for case in result.model["load_cases"]}
        forms[stem] = canon.canonical(result.model, names, kinds, oriented=True)
    english, si = forms["units_english"], forms["units_si"]
    assert set(english.values) == set(si.values) and english.sets == si.sets
    for key, value in english.values.items():
        # The SI fixture prints non-terminating conversions to 15 significant digits: 5e-15 relative, plus the
        # binary64 rounding of each side.
        assert si.values[key] == pytest.approx(value, rel=5e-15 + 8 * canon.EPS, abs=1e-300), key
    runner = runner_binary()
    tables = []
    for stem, result in imports.items():
        _, output, error = solve_swbpipe(runner, {"case_id": stem, "model": result.model})
        assert error == ""
        tables.append(result_table(output))
    for family, rows in tables[0].items():
        scale = max(abs(value) for value in rows.values())
        assert set(rows) == set(tables[1][family])
        assert max(abs(rows[key] - tables[1][family][key]) for key in rows) <= 1e-9 * scale, family


def test_an_english_import_round_trips_through_the_si_writer_by_exact_normalization():
    # O-2: the SI writer normalizes the English import by exact definitions; importing its MBF again (bound)
    # reproduces the English import within the Design's tolerances.
    data, declaration = fixture("units_english")
    english = import_caepipe_mbf(data, material_provenance=declaration["material_provenance"], source_label="english")
    assert any("exact normalization" in note for note in english.assumptions)
    trip = Trip("english-round-trip", english.model, "ENGLISH", 20.0)
    normalized = [item for item in trip.writer.diagnostics if item["code"] == "MBF-SI-UNITS-NORMALIZED"]
    assert normalized and all(text in normalized[0]["message"] for text in ("1 in = 25.4 mm", "1 psi", "1 lbf*ft",
                                                                           "1/degF = 9/5 per degC", "1 lbf/in"))
    lines = trip.text.split("\r\n")
    assert "T20,X3200.4,CFOR(0,-4448.221615,0),MOM(0,0,677.9089742)" in lines  # 126 in; 1000 lbf; 500 lbf*ft
    assert trip.bound.status == "imported", trip.bound.diagnostics
    assert trip.bound.model["project"]["units"]["length"] == "mm"
    reference = trip.reference()
    assert canon.compare(reference, trip.imported(trip.bound, oriented=True), trip.limits(reference)).failures == []


# --- schema (§18.1 item 6) -----------------------------------------------------------------------------------------
def all_imports(trips):
    found = [(name, trip.bound.model) for name, trip in trips.items()]
    for stem in ("units_english", "units_si"):
        data, declaration = fixture(stem)
        found.append((stem, import_caepipe_mbf(data, material_provenance=declaration["material_provenance"],
                                               source_label=stem).model))
    found += [("z-vertical-si-file", z_import(Z_VERTICAL_SI).model),
              ("z-vertical-english-file", z_import(Z_VERTICAL_ENGLISH).model)]
    return found


def test_every_imported_document_validates_against_the_desktop_profile(trips):
    requirements = desktop_entity_requirements()
    for name, model in all_imports(trips):
        try:
            validate_instance(DESKTOP_SCHEMA, model, schema_label="schemas/model.schema.yaml", instance_label=name)
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)
        for collection, (fields, optional) in requirements.items():
            if collection == "diagnostics":
                assert model["diagnostics"] == []
                continue
            items = model.get(collection)
            assert items is not None or optional, (name, collection)
            for item in items or []:
                for member in fields:
                    assert isinstance(item.get(member), str) and item[member].strip(), (name, collection, member)
        assert model["schema_version"] == json.loads((ROOT / "schemas" / "model.schema.yaml").read_text(
            encoding="utf-8"))["properties"]["schema_version"]["enum"][0]


def test_canonical_sums_are_exact_and_independent_of_the_writer(trips):
    # Codex VER-002 r1: three same-node Y forces 1e9, 0.001 and -1e9 lbf. By hand the canonical sum is
    # 0.001 x 4.4482216152605 = 0.0044482216152605 N; a binary64 running sum of the converted forces is 0.0044479370.
    trip = trips["writer-cancelling-forces"]
    reference = trip.reference()
    key = ("load", "sustained", "concentrated_force", trip.writer.node_map["N1"], 1)
    assert reference.values[key] == 0.0044482216152605
    running = 0.0
    for value in (1e9, 0.001, -1e9):
        running += value * 4.4482216152605
    assert abs(running - 0.0044482216152605) > 1e-7  # the error the exact sum avoids
    imported = trip.imported(trip.bound, oriented=True)
    assert imported.values[key] == 0.004448221615  # the writer's printed, correctly rounded sum
    assert canon.compare(reference, imported, trip.limits(reference)).failures == []


def test_canonical_form_of_a_tiny_bend_uses_scaled_norms():
    # Codex VER-002 r2 (P3): an imported bend with R = 1e-200 mm and perpendicular legs of 1e-199 mm. The squares of
    # its chord components (about 1e-400) underflow, so an unscaled norm divided by zero. By hand: TI (1e-199, 0, 0);
    # t = 1e-200 x tan 45 deg; the projected bend plane is unit(TI - chord middle) = (1, 0, -1)/sqrt 2.
    data = ("INVENTED TINY BEND\r\nVERSION\r\n15.10\r\nOPTIONS\r\nHGRA,SI\r\nOPTEMP\r\n20\r\nMATERIAL\r\n"
            "M1,0,0.3\r\nM1,20,200000,1.2e-05\r\nPIPE\r\nP1,168.3,7.11\r\nLOADS\r\nL1,20,0,0\r\nLAYOUT\r\n"
            "F10,KA,MM1,PP1,CL=L1\r\nT20,KI,B1e-200,X1e-199,CFF=1\r\nT30,KA,Z1e-199\r\n").encode("ascii")
    result = import_caepipe_mbf(data, material_provenance=INVENTED, source_label="tiny")
    assert result.status == "imported", result.diagnostics
    names = {swb_id: name for name, swb_id in result.id_map["node_map"].items()}
    form = canon.canonical(result.model, names, {}, oriented=True)
    plane = form.sets[("bend", ("20A", "20B"), "plane")]
    assert plane == pytest.approx([math.sqrt(0.5), 0.0, -math.sqrt(0.5)], abs=1e-12)
    assert form.values[("bend", ("20A", "20B"), "R")] == pytest.approx(1e-203, rel=1e-15)  # 1e-200 mm in m


# --- VER-002 r6: what the solve forms in metres, and restored ids ----------------------------------------------------
MITRE_ROWS = ("F10,KA,MM1,PP1,X1e15,CL=L1", "T20,KI,B50,X1000,CFF=1", "T30,KA,Y1000")


def authored_region(model: dict, terminals: tuple[str, str], pressure: float = 10.0) -> dict:
    """`model` with all its pipes in one 10 bar exact-pressure region between `terminals`, as a user authors it."""
    model = deepcopy(model)
    model["pressure_contract"] = {"version": "3.0.0", "mode": "exact_pressure_v3", "shear_model": "euler_bernoulli"}
    for pipe in model["pipe_segments"]:
        pipe["section"]["corrosion_allowance"] = {"value": 0.0, "unit": "mm"}
    model["load_cases"] = [{"id": "case:p", "label": "Sustained (W+P)", "kind": "sustained", "status": "draft",
                            "primitive_loads": [], "provenance": "invented", "pressure_regions": [
        {"id": "region:r", "member_pipe_ids": [pipe["id"] for pipe in model["pipe_segments"]],
         "pressure_basis": "internal_differential_zero_external_v1", "pressure": {"value": pressure, "unit": "bar"},
         "provenance": "invented", "terminals": [
             {"node_ref": node, "closure_transfer": "transfers_to_wall", "provenance": "invented"}
             for node in terminals]}]}]
    return model


def test_a_bend_whose_arc_in_metres_is_not_tangent_is_refused_whole_on_both_routes():
    # Codex VER-002 r6 (P2). By hand, in mm: TI 20 at (1e15 + 1000, 0, 0) with legs along +X and +Y, theta = 90 deg,
    # t = 50 tan 45 deg = 49.99999999999999, so 20A = (1e15 + 950, 0, 0) and 20B = (1e15 + 1000, 49.99999999999999, 0)
    # (the binary64 spacing at 1e15 mm is 0.125). Read to m (x 0.001, whose binary64 is 0.001 (1 + 2.08e-17)) the
    # spacing at 1e12 is 2^-13: 20A's x is 1e12 + 7783/8192 (0.9500208 x 8192 = 7782.57) and 20B's 1e12 + 1. The
    # arc's chord is (409/8192, 0.04999999999999999, 0) m with R = 0.05 m, and its start tangent leaves the incoming
    # straight (+X) by atan2(c_y, c_x) - asin(|c|/2R), about 1.4648e-3 rad > alpha_tan = 1e-3: a mitre at 20A.
    chord = (409 / 8192, 49.99999999999999 * 0.001)
    theta = math.atan2(chord[1], chord[0]) - math.asin(math.hypot(*chord) / (2 * 0.05))
    assert 1.4648e-3 < theta < 1.4649e-3
    data = importer_tests.mbf(*MITRE_ROWS, pipe=("P1,50,2,0",), loads=("L1,20,10,0",))
    unbound = importer_tests.run(data, pressure_closure=importer_tests.CLOSURE)
    assert refusals(unbound) == {("MBF-IMPORT-PRESSURE-MITRE", "elements 10-20A, 20A-20B, 20B-30")}
    message = next(item["message"] for item in unbound.diagnostics if item["code"] == "MBF-IMPORT-PRESSURE-MITRE")
    assert "at node 20A" in message and f"{theta:.6g} rad" in message
    terminals = [{"node_ref": node, "closure_transfer": "transfers_to_wall", "provenance": "invented"}
                 for node in ("node:10", "node:30")]
    sidecar = {"mbf_sha256": hashlib.sha256(data).hexdigest(), "pressure_map": {
        "contract": {"version": "3.0.0", "mode": "exact_pressure_v3", "shear_model": "euler_bernoulli"},
        "regions": [{"id": "region:r", "members": ["pipe:10-20A", "pipe:20A-20B", "pipe:20B-30"],
                     "terminals": terminals}]}}
    bound = import_caepipe_mbf(data, sidecar=sidecar, material_provenance=INVENTED, source_label="mitre")
    assert refusals(bound) == {("MBF-IMPORT-PRESSURE-MITRE", "pressure_map region region:r")}
    # The route refuses the same region authored on the file's pressure-free import.
    model = importer_tests.run(importer_tests.mbf(*MITRE_ROWS, pipe=("P1,50,2,0",))).model
    _, output, error = solve_swbpipe(runner_binary(), {"case_id": "mitre",
                                                       "model": authored_region(model, ("node:10", "node:30"))})
    assert error and "PRESSURE_REGION_MITRE_UNSUPPORTED" in json.dumps(output)


def test_a_restored_y_reference_the_frame_kernel_refuses_is_replaced_and_listed():
    # Codex VER-002 r6 (P2): the straight 10 -> 20 runs along (1, 2, 0) m and the sidecar's y_reference is
    # (1, 2.00000001, 0). Its part perpendicular to the axis is exactly 1e-8 (-2, 1, 0)/5, of norm 4.47e-9, but the
    # binary64 projection y.x carries an error of order 1e-16, which the subtraction leaves in y: the kernel's y is
    # about 4e-8 from orthogonal to x, far above its 1e-12 ("local axes must be mutually orthogonal"). The pipe takes
    # the documented local y: Y - (Y.x)x for x = (1, 2, 0)/sqrt 5 is (-2/5, 1/5, 0), normalized (-2, 1, 0)/sqrt 5.
    data = importer_tests.mbf("F10,KA,MM1,PP1,CL=L1", "T20,KA,X1000,Y2000", loads=("L1,20,10,0",))
    restored = {"x": 1.0, "y": 2.00000001, "z": 0.0}
    sidecar = {"mbf_sha256": hashlib.sha256(data).hexdigest(),
               "element_map": {"s": {"from": "10", "to": "20", "y_reference": restored}}}
    result = import_caepipe_mbf(data, sidecar=sidecar, material_provenance=INVENTED, source_label="parallel",
                                pressure_closure=importer_tests.CLOSURE)
    assert result.status == "imported", result.diagnostics
    assert tuple(result.model["pipe_segments"][0]["y_reference"].values()) == pytest.approx(
        (-2 / math.sqrt(5), 1 / math.sqrt(5), 0.0), abs=1e-15)
    assert [(item["location"], item["category"]) for item in result.loss_report
            if item["code"] == "MBF-IMPORT-ORIENTATION-DEFAULTED"] == [("s", "approximated")]
    assert importer_module.frame_y_reference_usable((0, 0, 0), (1.0, 2.0, 0), (1.0, 2.00000001, 0.0)) is False
    runner = runner_binary()
    authored = deepcopy(result.model)
    authored["pipe_segments"][0]["y_reference"] = restored
    _, output, error = solve_swbpipe(runner, {"case_id": "parallel-authored", "model": authored})
    assert error and "mutually orthogonal" in json.dumps(output)
    _, _, error = solve_swbpipe(runner, {"case_id": "parallel-replaced", "model": result.model})
    assert error == ""


def test_the_preflight_refuses_an_orientation_its_printed_positions_would_replace(monkeypatch):
    # A y_reference 8.1e-8 off the straight's axis: the kernel forms orthonormal axes from it on the authored end
    # (434.3743180726007, 2006.440216234222, 0) mm, but not on the printed one (434.3743181, 2006.440216, 0), where
    # the rounding left in y exceeds 1e-12. The solve is the judge of both.
    end = "X434.3743180726007,Y2006.440216234222"
    model = importer_tests.run(importer_tests.mbf("F10,KA,MM1,PP1,CL=L1", f"T20,KA,{end}", loads=("L1,20,10,0",)),
                               pressure_closure=importer_tests.CLOSURE).model
    restored = {"x": 434.3743180726007, "y": 2006.440379564788, "z": 0.0}
    model["pipe_segments"][0]["y_reference"] = restored
    runner = runner_binary()
    _, _, error = solve_swbpipe(runner, {"case_id": "orientation-authored", "model": model})
    assert error == ""
    written = render_caepipe_mbf_si(model, title="ORIENTATION")
    assert written.status == "refused"
    assert {(item["code"], item["entity"]) for item in written.diagnostics if item["severity"] == "error"} == {
        ("MBF-SI-PREFLIGHT-REFUSED", "model.pipe_segments[pipe:10-20].y_reference")}
    data, sidecar = bound_parts(model, monkeypatch)  # printed, the import replaces it
    bound = import_caepipe_mbf(data, sidecar=sidecar, material_provenance=INVENTED, source_label="printed")
    assert bound.model["pipe_segments"][0]["y_reference"] != restored
    printed = deepcopy(bound.model)
    printed["pipe_segments"][0]["y_reference"] = restored
    _, output, error = solve_swbpipe(runner, {"case_id": "orientation-printed", "model": printed})
    assert error and "local axes" in json.dumps(output)


def test_blank_restored_ids_are_refused_by_kind():
    # Codex VER-002 r6 (P2): the solve refuses an id that Rust's trim() empties (EMPTY_ID; a region member also
    # PRESSURE_REGION_MEMBERS_INVALID). Its whitespace is Unicode White_Space: U+3000 is, U+001C is not (although
    # Python's str.strip removes it).
    data = importer_tests.mbf("F10,KA,MM1,PP1,CL=L1", "T20,KA,X1000", loads=("L1,20,10,0",))
    sidecar = {"mbf_sha256": hashlib.sha256(data).hexdigest(), "element_map": {"": {"from": "10", "to": "20"}}}
    result = import_caepipe_mbf(data, sidecar=sidecar, material_provenance=INVENTED, source_label="empty",
                                pressure_closure=importer_tests.CLOSURE)
    assert refusals(result) == {("MBF-IMPORT-SIDECAR-CONFLICT", "pipe id ''")}
    model = importer_tests.run(data, pressure_closure=importer_tests.CLOSURE).model
    _, output, error = solve_swbpipe(runner_binary(), {"case_id": "empty-id",
                                                       "model": renamed(model, {"pipe:10-20": ""})})
    assert error and all(code in json.dumps(output) for code in ('"EMPTY_ID"', '"PRESSURE_REGION_MEMBERS_INVALID"'))
    data, base = bound_parts(writer_tests.bent_l())

    def rename(mapping: dict, old: str, new: str) -> None:
        mapping[new] = mapping.pop(old)

    changes = {
        "node": lambda sidecar: rename(sidecar["node_map"], "A", " "),
        "pipe": lambda sidecar: rename(sidecar["element_map"], "S1", "　"),
        "component": lambda sidecar: sidecar["element_map"]["BEND"]["bend"].update(component="\t"),
        "material": lambda sidecar: sidecar["material_map"]["M1"].update(swbpipe_material=" "),
        "support": lambda sidecar: rename(sidecar["support_map"], "SA", " "),
        "load case": lambda sidecar: rename(sidecar["load_case_map"], "case:th", " "),
        "primitive load": lambda sidecar: rename(sidecar["load_map"], "case:th/t:S1", "case:th/ "),
    }
    blank = {"node": " ", "pipe": "　", "component": "\t", "material": " ", "support": " ",
             "load case": " ", "primitive load": " "}
    for kind, change in changes.items():
        sidecar = deepcopy(base)
        change(sidecar)
        result = import_caepipe_mbf(data, sidecar=sidecar, material_provenance=INVENTED, source_label=kind)
        assert result.status == "refused", kind
        assert ("MBF-IMPORT-SIDECAR-CONFLICT", f"{kind} id {blank[kind]!r}") in refusals(result), kind
    assert importer_module.runtime_blank("\x1c") is False and "\x1c".strip() == ""
    kept = deepcopy(base)
    rename(kept["element_map"], "S1", "\x1c")
    assert import_caepipe_mbf(data, sidecar=kept, material_provenance=INVENTED, source_label="kept").status == "imported"


def test_sections_are_checked_on_their_binary64_values_in_metres():
    # OD 504 mm, wall 251.99999999999997 mm (the binary64 below 252, 252 - 2^-45): 2t < OD in mm. In m the wall is
    # 251.99999999999997158 x 0.001 (1 + 2.08e-17) = 0.2519999999999999768, above the midpoint 0.2519999999999999740
    # of its neighbours, so it rounds to the binary64 0.2520000000000000018; the OD, 0.50400000000000001049, rounds to
    # 0.5040000000000000036, twice that: 2t = OD in m. And OD 1 with wall 0.49999999999999999: 2t < OD in decimals,
    # but the wall's binary64 is 0.5 (it lies 1e-17 below 0.5, the binary64 spacing there 5.6e-17).
    runner = runner_binary()
    for name, section, wall in (("metres", "P1,504,251.99999999999997,0", 251.99999999999997),
                                ("decimal", "P1,1,0.49999999999999999,0", 0.5)):
        data = importer_tests.mbf("F10,KA,MM1,PP1,CL=L1", "T20,KA,X1000", pipe=(section,))
        importer_tests.refused(importer_tests.run(data), "MBF-IMPORT-VALUE-OUT-OF-RANGE",
                               importer_tests.layout_line(data, "P1,"))
        od = float(section.split(",")[1])
        model = authored_region(importer_tests.run(importer_tests.mbf(
            "F10,KA,MM1,PP1,CL=L1", "T20,KA,X1000", pipe=(f"P1,{od},{od / 4},0",))).model, ("node:10", "node:20"))
        model["pipe_segments"][0]["section"]["wall_thickness"]["value"] = wall
        _, output, error = solve_swbpipe(runner, {"case_id": f"section-{name}", "model": model})
        assert error and "PIPE_DIMENSION_INVALID" in json.dumps(output), name


def test_a_pressure_beyond_binary64_in_pascals_is_refused():
    # 1e304 bar is finite, but the route reads it as 1e304 x 1e5 = 1e309 Pa, beyond the binary64 maximum (about
    # 1.8e308), and refuses it (PRESSURE_REGION_PRESSURE_INVALID). The headless runner's checked-JSON reader stops
    # such a value earlier (an integral float above 2^53), so the arithmetic, not a solve, is the reference here.
    assert 1e304 * 100000.0 == math.inf
    data = importer_tests.mbf("F10,KA,MM1,PP1,CL=L1", "T20,KA,X1000", loads=("L1,20,1e304,0",))
    importer_tests.refused(importer_tests.run(data, pressure_closure=importer_tests.CLOSURE),
                           "MBF-IMPORT-VALUE-UNREPRESENTABLE", importer_tests.layout_line(data, "L1,"))
