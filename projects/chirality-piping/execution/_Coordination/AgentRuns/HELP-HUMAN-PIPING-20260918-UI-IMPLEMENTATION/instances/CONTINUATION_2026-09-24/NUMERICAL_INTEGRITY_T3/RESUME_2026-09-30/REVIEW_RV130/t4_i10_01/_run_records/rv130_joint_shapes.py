"""RV130, self-contained: enumerate expansion-joint input shapes against T4-I10's
section 4.2 classification, as amended by T4_RULINGS at 1b682630e4 (residual
shape -> legacy code; annotation joints refused on the exact route: v2 by the
composition refusal, v3 by the seam's named refusal). Every shape must reach a
named blocking code or an admitted path; nothing may fall through.

Usage: python -I rv130_joint_shapes.py
"""
from itertools import product

VERSIONS = ["0.1.0/0.2.0", "v2 exact", "v3 exact"]
CONNECTOR = ["absent", "v1.0.0 valid", "v1.0.0 invalid-or-topology", "other version"]
CONSUMPTION = ["absent", "not_solver_consumed", "mechanics_geometry_only",
               "mechanics_geometry_and_user_flexibility", "other string"]
PIPE_REF = [False, True]
RATES = ["none", "some", "all four"]


def classify(version, connector, consumption, pipe_ref, rates):
    if connector != "absent":
        if version == "0.1.0/0.2.0":
            return "PREVIEW_CONTRACT_VERSION_MISMATCH", "spec"
        if connector == "other version":
            return "OBJECTIVE_CONNECTOR_VERSION_UNSUPPORTED", "spec"
        if version == "v2 exact":
            return "OBJECTIVE_CONNECTOR_NOT_IMPLEMENTED + EXACT_PRESSURE_COMPOSITION_UNSUPPORTED", "spec"
        legacy_alongside = pipe_ref or rates != "none"
        if connector == "v1.0.0 invalid-or-topology" or legacy_alongside:
            return "OBJECTIVE_CONNECTOR_INPUT_INCOMPLETE / _TOPOLOGY_UNRESOLVED / JOINT_* (named)", "spec"
        if consumption not in ("absent",):
            # A valid v3 connector whose mechanics_interface declares another consumption:
            # section 4.2 does not say whether this is "legacy fields alongside it".
            return "admitted as connector (consumption field not stated)", "UNSPECIFIED"
        return "admitted (connector)", "spec"
    if consumption == "not_solver_consumed":
        if version == "0.1.0/0.2.0":
            return "admitted as annotation + EXPANSION_JOINT_ANNOTATION_ONLY", "spec"
        if version == "v2 exact":
            return "EXACT_PRESSURE_COMPOSITION_UNSUPPORTED", "ruling"
        return "v3 seam's named refusal (code not named in SLOT_TABLE)", "ruling"
    if pipe_ref or rates != "none":
        return "LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED [component, pipe?]", "spec"
    return "LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED [component] (residual)", "ruling"


counts = {}
unspecified = []
for shape in product(VERSIONS, CONNECTOR, CONSUMPTION, PIPE_REF, RATES):
    outcome, basis = classify(*shape)
    assert outcome, shape
    counts[(outcome, basis)] = counts.get((outcome, basis), 0) + 1
    if basis == "UNSPECIFIED":
        unspecified.append(shape)
total = sum(counts.values())
print(f"{total} shapes (version x connector x consumption x pipe_ref x rates); none falls through")
for (outcome, basis), n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"   {n:4d}  [{basis}] {outcome}")
print(f"unspecified (admitted, consumption semantics not stated): {len(unspecified)}, e.g. {unspecified[0]}")
