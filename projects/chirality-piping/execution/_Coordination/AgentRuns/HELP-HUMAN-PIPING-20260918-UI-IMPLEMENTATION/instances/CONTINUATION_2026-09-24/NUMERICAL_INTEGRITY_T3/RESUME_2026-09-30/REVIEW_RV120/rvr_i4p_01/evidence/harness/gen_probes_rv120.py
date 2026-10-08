"""RV120 (RV-R): probes of my own for the round toward I4' (RR "I4 made at 30f3d1b24a; ...", rulings 2 and 3).

Written from the ruling, not from I100's or I101's tests. Each probe edits one shared-corpus base (07m at I4) and is
rehashed as the snapshot format rule says. `want` states the transport verdict where the ruling fixes it; the raw
verdicts are per reader (RS's raw code is ...NUMBER_INVALID, TS's and PY's ...EVIDENCE_INVALID: B1_SC item 13), so
they are left `observe` here and checked per reader by compare_rv120.py.
Usage: python3 gen_probes_rv120.py <out.json>
"""
import json
import sys

G7 = {"gate": "G7", "code": "SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID"}
OBS = {"observe": True}


def x(case, k, member):
    return ["contract_evidence", "preview_cases", case, "pipe_stress_extrema", k, member]


def probe(pid, base, edits, transport, note=""):
    return {"id": "rv120:" + pid, "item": "I4P", "base": base, "edits": edits, "invocation_edits": [], "rehash": "all",
            "want": {"bound": OBS, "unbound": OBS, "transport": transport}, "note": note, "set_name": "rv120"}


def setx(case, k, member, value):
    return {"path": x(case, k, member), "op": "set", "value": value}


ORD = "ordinary_prepared_synthetic"
P = []
# Ruling 2/3: each non-number shape of each member, on the first extremum of the first case.
for member, shapes in (("global_upper_bound_pa", [("str", "x"), ("null", None), ("true", True), ("false", False), ("list", [1.0]),
                                                  ("empty_list", []), ("object", {}), ("numeric_string", "1e6")]),
                       ("certified_gap_pa", [("null", None), ("str", "0"), ("true", True), ("list", [0.0]), ("object", {"v": 0}),
                                             ("empty_string", "")])):
    tag = "gub" if member == "global_upper_bound_pa" else "gap"
    for name, value in shapes:
        P.append(probe(f"{tag}_{name}", ORD, [setx(0, 0, member, value)], G7, f"{member} = {json.dumps(value)}"))
# Both members bad at once.
P.append(probe("both_null", ORD, [setx(0, 0, "global_upper_bound_pa", None), setx(0, 0, "certified_gap_pa", None)], G7))
# Positions: a later case (two_case_synthetic's case 1) and a later extremum (two_body_synthetic's extremum 1); the u8 L = 0 bases.
P.append(probe("gub_str_case1", "two_case_synthetic", [setx(1, 0, "global_upper_bound_pa", "x")], G7))
P.append(probe("gap_null_case1", "two_case_synthetic", [setx(1, 0, "certified_gap_pa", None)], G7))
P.append(probe("gub_null_extremum1", "two_body_synthetic", [setx(0, 1, "global_upper_bound_pa", None)], G7))
P.append(probe("gap_str_extremum1", "two_body_synthetic", [setx(0, 1, "certified_gap_pa", "0")], G7))
P.append(probe("gap_null_u8_sparse", "u8_l0_isolated_node_sparse_interactive", [setx(0, 0, "certified_gap_pa", None)], G7))
P.append(probe("gub_str_u8_dense", "u8_l0_isolated_node_dense_scrutiny", [setx(0, 0, "global_upper_bound_pa", "x")], G7))
P.append(probe("gap_null_two_groups_case1", "two_case_two_groups_synthetic", [setx(1, 0, "certified_gap_pa", None)], G7))
# Numbers stay admitted on transport (never eligible there); raw verdicts observed.
for name, value in (("int0", 0), ("neg", -1.0), ("big_frac", 123456789.125), ("int_big", 41354909)):
    P.append(probe(f"gub_{name}", ORD, [setx(0, 0, "global_upper_bound_pa", value)], {"admitted": False}))
    P.append(probe(f"gap_{name}", ORD, [setx(0, 0, "certified_gap_pa", value)], {"admitted": False}))
# Order: the demand follows the extrema shape and identity, and precedes fractions, integers and bounds.
P.append(probe("order_shape_first", ORD, [setx(0, 0, "global_upper_bound_pa", "x"), setx(0, 0, "extra", 1)], G7, "extrema shape first"))
P.append(probe("order_identity_first", ORD, [setx(0, 0, "global_upper_bound_pa", "x"), setx(0, 0, "approximation", "other")], G7, "identity first"))
P.append(probe("order_before_fractions", ORD, [setx(0, 0, "certified_gap_pa", None), setx(0, 0, "station_fraction", 2.0)], G7, "numbers before fractions"))
P.append(probe("order_before_integers", ORD, [setx(0, 0, "certified_gap_pa", None), setx(0, 0, "span_index", -1)], G7, "numbers before integers"))
P.append(probe("order_before_bounds", ORD, [setx(0, 0, "global_upper_bound_pa", None), setx(0, 0, "value_lower_pa", -1.0)], G7, "numbers before bounds"))
# Missing member: the shape demand refuses it first.
P.append(probe("gap_missing", ORD, [{"path": x(0, 0, "certified_gap_pa"), "op": "remove"}], G7, "extrema shape"))
# Ruling 2's withheld-multiset shape, and its neighbours (observed; the three readers must agree).
W = ["contract_evidence", "preview_cases"]
s1 = {"support_id": "s", "reason": "CONSTANT_EFFORT_NOT_CONSUMED"}
def wh(case, recs):
    return {"path": W + [case, "support_attribution", "withheld"], "op": "set", "value": recs}
P.append(probe("withheld_dup_case1_only", "two_case_synthetic", [wh(0, [s1]), wh(1, [s1, s1])], G7, "case 1 withholds s twice, case 0 once"))
P.append(probe("withheld_dup_both", "two_case_synthetic", [wh(0, [s1, s1]), wh(1, [s1, s1])], OBS, "both cases withhold s twice"))
P.append(probe("withheld_dup_three_vs_two", "two_case_synthetic", [wh(0, [s1, s1, s1]), wh(1, [s1, s1])], G7, "multiplicities 3 and 2"))
P.append(probe("withheld_same_once", "two_case_synthetic", [wh(0, [s1]), wh(1, [s1])], OBS, "control: once in each case"))
s2 = {"support_id": "s", "reason": "SUPPORT_ACTION_ATTRIBUTION_WITHHELD"}
P.append(probe("withheld_reason_differs", "two_case_synthetic", [wh(0, [s1]), wh(1, [s2])], G7, "same support, other reason"))
json.dump(P, open(sys.argv[1], "w"), indent=1)
print(len(P), "probes")
