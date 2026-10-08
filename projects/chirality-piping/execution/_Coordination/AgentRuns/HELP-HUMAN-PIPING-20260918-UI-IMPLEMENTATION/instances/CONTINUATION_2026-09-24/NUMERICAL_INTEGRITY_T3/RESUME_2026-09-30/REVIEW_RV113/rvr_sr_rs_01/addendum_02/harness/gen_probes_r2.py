"""RV113 (RV-R): probes for confirming SR-RS repair 02 (RR "RV113's three returns verified; I3 made at `2ba2f81863`;
the three-reader alignment set ruled", items 1-4), written from the ruling, not from the candidate's tests.

Each probe is a shared-format entry (base, edits, invocation_edits, rehash "all"). `want` holds this reviewer's
expected RS verdicts at the repaired head, per verdict kind: {"bound": V, "unbound": V, "transport": V}, where V is
{"admitted": eligible}, {"gate": g, "code": c}, or {"observe": true} (no expectation; the readers are compared).

Sections:
  F  item 1: (f)'s family at G3 COVERAGE bound and unbound; the ordinary attempt's basis reference at G5 ATTEMPT;
  G  item 2: the model-scope members at G8 INVOCATION (bound only; unbound and transport admit);
  C  item 3: C2's cause table at G5 ATTEMPT, every branch satisfied and broken, including every cross-code
     precondition pair, on three constructions (a Ready attempt with a selected Run; a case with no product
     attempt, source or Run; a case with an unavailable product attempt) and a kernel reason on an idle Run;
  T  item 4: transport (the header at G2, the preview-physics metadata check at G7).
Usage: python gen_probes_r2.py <corpus json> <out json>
"""
import copy
import json
import sys

d = json.load(open(sys.argv[1]))
C = {c["id"]: c for c in d["cases"]}
MP = {m["id"]: m for m in d["must_pass"]}
R = "RETAINED_PRECISION_"
COV, ATT, PRO, INV, PREP, ROWM = (R + x for x in ("COVERAGE_MISMATCH", "ATTEMPT_MISMATCH", "PRODUCT_ATTEMPT_MISMATCH",
                                                    "INVOCATION_MISMATCH", "PREPARATION_MISMATCH", "ROW_METHOD_MISMATCH"))
EVI = "SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID"


def G(g, c):
    return {"gate": g, "code": c}


def A(e):
    return {"admitted": e}


OBS = {"observe": True}


def rb(*p):
    return ["retained_precision", "body", *p]


def S(path, value):
    return {"path": list(path), "op": "set", "value": value}


def RM(path):
    return {"path": list(path), "op": "remove"}


probes = []


def probe(pid, section, base, edits, bound, unbound=None, transport=None, inv=None, note=""):
    probes.append({"id": pid, "item": section, "base": base, "edits": edits, "invocation_edits": inv or [],
                   "rehash": "all", "want": {"bound": bound, "unbound": unbound if unbound is not None else OBS,
                                             "transport": transport if transport is not None else OBS},
                   "note": note})


O, TC, TG, PB, FB = ("ordinary_prepared_synthetic", "two_case_synthetic", "two_case_two_groups_synthetic",
                     "two_case_preparation_failure_synthetic", "two_case_facade_after_certificate_synthetic")

# ---------------------------------------------------------------------------- F: item 1
for pid, base, edits, note in [
    ("f_mb_index_1", O, [S(rb("material_bases", 0, "index"), 1)], "the one basis labelled 1"),
    ("f_mb_index_swapped", TG, [S(rb("material_bases", 0, "index"), 1), S(rb("material_bases", 1, "index"), 0)], ""),
    ("f_src_index_1", O, [S(rb("sources", 0, "index"), 1)], ""),
    ("f_src_index_swapped", TC, [S(rb("sources", 0, "index"), 1), S(rb("sources", 1, "index"), 0)], ""),
    ("f_mb_case_indices_duplicate", TC, [S(rb("material_bases", 0, "case_indices"), [0, 1, 1])], ""),
    ("f_mb_case_indices_out_of_range", TC, [S(rb("material_bases", 0, "case_indices"), [0, 1, 2])], ""),
    ("f_src_owner_case_id_other", TC, [S(rb("sources", 1, "owner", "case_id"), "case:six-component-load")], "the id of another case"),
    ("f_src_owner_case_id_unknown", TC, [S(rb("sources", 1, "owner", "case_id"), "case:rv113-none")], "an id of no case"),
    ("f_src_owner_case_index_out_of_range", TC, [S(rb("sources", 1, "owner", "case_index"), 5)], ""),
]:
    probe(pid, "F", base, edits, G("G3", COV), G("G3", COV), note=note)
# A source whose owner is another case, consistently (index and id of case 0): G3 passes; the Call position's binding
# (G5 native, ATTEMPT) is next in RS. Observe the three readers.
probe("f_src_owner_other_case_consistent", "F", TC, [S(rb("sources", 1, "owner"), {"kind": "case", "case_index": 0, "case_id": "case:six-component-load"})],
      G("G5", ATT), G("G5", ATT), note="owner consistent but not the source's case: G3 passes; G5's Call binding refuses")
# Item 1's G5 part: the ordinary attempt's basis reference resolves and lists the case.
probe("f_ordinary_basis_ref_dangling", "F", O, [S(rb("ordinary_attempts", 0, "material_basis_ref"), 3)], G("G5", ATT), G("G5", ATT))
probe("f_mb_case_indices_empty", "F", O, [S(rb("material_bases", 0, "case_indices"), [])], G("G5", ATT), G("G5", ATT),
      note="G3 passes (unique, in range); the ordinary attempt's basis no longer lists case 0")
NR = MP["not_required_second_case_checks_passed"]["edits"]
mb0 = C[PB]["source"]["retained_precision"]["body"]["material_bases"][0]
probe("f_b_basis_ref_7", "F", PB, copy.deepcopy(NR) + [S(rb("ordinary_attempts", 1, "material_basis_ref"), 7)], G("G5", ATT), G("G5", ATT),
      note="repair 01's (b) input: now G5 ATTEMPT in all readers by the ruling")
probe("f_c_basis_omits_case_1", "F", PB, copy.deepcopy(NR) + [S(rb("material_bases", 0, "case_indices"), [0])], G("G5", ATT), G("G5", ATT),
      note="repair 01's (c) input")
probe("f_c_basis_out_of_order", "F", PB, copy.deepcopy(NR) + [S(rb("material_bases", 0, "case_indices"), [1, 0])], G("G8", PREP), A(False),
      note="internal facts hold; G8's exact case list by selector refuses")
probe("f_control_07j", "F", PB, copy.deepcopy(NR), A(True), A(False))

# ---------------------------------------------------------------------------- G: item 2
M = ["request", "model"]
for pid, inv, want in [
    ("g_combinations_absent", [RM(M + ["combinations"])], A(True)),
    ("g_combinations_empty_array", [S(M + ["combinations"], [])], A(True)),
    ("g_combinations_null", [S(M + ["combinations"], None)], G("G8", INV)),
    ("g_combinations_empty_object", [S(M + ["combinations"], {})], G("G8", INV)),
    ("g_combinations_object", [S(M + ["combinations"], {"x": 1})], G("G8", INV)),
    ("g_combinations_string", [S(M + ["combinations"], "x")], G("G8", INV)),
    ("g_combinations_zero", [S(M + ["combinations"], 0)], G("G8", INV)),
    ("g_combinations_false", [S(M + ["combinations"], False)], G("G8", INV)),
    ("g_combinations_nonempty", [S(M + ["combinations"], [{"id": "combination:rv113"}])], G("G8", INV)),
    ("g_components_absent", [RM(M + ["components"])], A(True)),
    ("g_components_null", [S(M + ["components"], None)], G("G8", INV)),
    ("g_components_string", [S(M + ["components"], "x")], G("G8", INV)),
    ("g_components_empty_object", [S(M + ["components"], {})], G("G8", INV)),
    ("g_components_nonempty", [S(M + ["components"], [{"id": "component:rv113"}])], G("G8", INV)),
    ("g_reference_configurations_null", [S(M + ["reference_configurations"], None)], G("G8", INV)),
    ("g_reference_configurations_empty", [S(M + ["reference_configurations"], [])], G("G8", INV)),
    ("g_reference_configurations_object", [S(M + ["reference_configurations"], {})], G("G8", INV)),
    ("g_pressure_contract_null", [S(M + ["pressure_contract"], None)], A(True)),
    ("g_pressure_contract_empty_object", [S(M + ["pressure_contract"], {})], G("G8", INV)),
    ("g_pressure_contract_false", [S(M + ["pressure_contract"], False)], G("G8", INV)),
    ("g_pressure_contract_zero", [S(M + ["pressure_contract"], 0)], G("G8", INV)),
    ("g_pressure_contract_empty_string", [S(M + ["pressure_contract"], "")], G("G8", INV)),
    ("g_pressure_contract_empty_array", [S(M + ["pressure_contract"], [])], G("G8", INV)),
]:
    probe(pid, "G", O, [], want, A(False), inv=inv)
# The model-scope check precedes every PREPARATION check: a null combinations list beside a mode code 3.
mode_row = next(i for i, r in enumerate(C[O]["source"]["results"]) if r["kind"] == "linear_solver_mode_basis")
probe("g_order_before_preparation", "G", O, [S(["results", mode_row, "value"], 3.0)], G("G8", INV), A(False),
      inv=[S(M + ["combinations"], None)], note="INVOCATION before the P1 PREPARATION defect")
probe("g_order_control_preparation", "G", O, [S(["results", mode_row, "value"], 3.0)], G("G8", PREP), A(False),
      note="the PREPARATION defect alone")

# ---------------------------------------------------------------------------- C: item 3
# C-a: two_case_synthetic, case 1 unavailable with its Ready attempt and selected Run (D19's receipt_failure form).
tcs = C[TC]["source"]
tc1 = tcs["retained_precision"]["body"]["cases"][1]
di = [i for i, x in enumerate(tcs["diagnostics"]) if x["code"] == "RETAINED_PRECISION_SELECTED" and tc1["basis_ref"]["ref_id"] in x.get("affected_refs", [])][0]
tc_rows = copy.deepcopy(tcs["results"])
for r in tc_rows:
    if r["basis_ref"]["ref_id"] == tc1["basis_ref"]["ref_id"]:
        r.pop("recovery_method", None)


def ca(pid, code, phase, cause, want, note=""):
    case = {"basis_ref": tc1["basis_ref"], "ordinary": tc1["ordinary"], "product_attempt_ref": 1, "status": "unavailable",
            "reason": {"code": code, "phase": phase, "cause": cause}, "diagnostic_ref": tcs["diagnostics"][di]["id"],
            "run": tc1["run"], "source_ref": 1}
    probe(pid, "C-a", TC, [S(rb("cases", 1), case), S(["diagnostics", di, "code"], "RETAINED_PRECISION_UNAVAILABLE"), S(["results"], tc_rows)],
          want, want, note=note)


RF = {"kind": "receipt_failure", "check": "encoding", "field_path": "retained_precision.body"}
FF = {"kind": "facade_failure", "owner_ref": {"kind": "case", "index": 1}, "row_id": None, "recipe": "identity",
      "operand_index": None, "check": "identity", "predicate": None}
RECEIPT_CODES = ["receipt_encoding", "publication_hash_range", "invocation_not_representable"]
PHASES = ["routing", "preparation", "kernel", "facade", "receipt"]
for code in RECEIPT_CODES:
    ca(f"ca_receipt_ok_{code}", code, "receipt", RF, A(False), "satisfied; D19 admits a Ready attempt under receipt_failure")
for phase in PHASES:
    if phase != "receipt":
        ca(f"ca_receipt_phase_{phase}", "receipt_encoding", phase, RF, G("G5", ATT))
for code in ["source_unavailable", "facade_certificate", "kernel_selected", "caller_not_qualified"]:
    ca(f"ca_receipt_code_{code}", code, "receipt", RF, G("G5", ATT))
ca("ca_facade_ok", "facade_certificate", "facade", FF, G("G5", PRO), "satisfied; D19 refuses a Ready attempt under facade_failure")
for phase in PHASES:
    if phase != "facade":
        ca(f"ca_facade_phase_{phase}", "facade_certificate", phase, FF, G("G5", ATT))
ca("ca_facade_code_receipt_encoding", "receipt_encoding", "facade", FF, G("G5", ATT))
ca("ca_facade_owner_other_case", "facade_certificate", "facade", dict(FF, owner_ref={"kind": "case", "index": 0}), G("G5", ATT))
ca("ca_facade_owner_combination", "facade_certificate", "facade", dict(FF, owner_ref={"kind": "combination", "index": 1}), G("G5", ATT))
# A precondition or a source error beside a selected Run: never legal (no Run).
ca("ca_precondition_beside_run", "source_unavailable", "preparation", {"kind": "unavailable_precondition", "precondition": "capture", "affected_refs": []}, G("G5", ATT))
ca("ca_kernel_beside_selected_run", "kernel_selected", "kernel", {"space": "refusal", "tag": "structure"}, G("G5", ATT),
   "a kernel reason needs the cause to equal the terminal's reason; a selected terminal has none")

# C-b: two_case_preparation_failure_synthetic, case 1 unavailable with no product attempt, source or Run.
pbs = C[PB]["source"]
pb1 = pbs["retained_precision"]["body"]["cases"][1]


def cb(pid, code, phase, cause, want, decline=None, note=""):
    case = {"basis_ref": pb1["basis_ref"], "ordinary": pb1["ordinary"], "product_attempt_ref": None, "status": "unavailable",
            "reason": {"code": code, "phase": phase, "cause": cause}, "diagnostic_ref": pb1["diagnostic_ref"], "run": None, "source_ref": None}
    if decline is not None:
        case["source_decline"] = decline
    probe(pid, "C-b", PB, [S(rb("cases", 1), case), RM(rb("product_attempts", 1))], want, want, note=note)


KEYED = {"caller": "caller_not_qualified", "resource_admission": "resource_admission_not_available",
         "upstream_no_wrap": "upstream_no_wrap_not_established", "capture": "source_unavailable", "source_family": "source_unavailable"}
CODES = sorted(set(KEYED.values()))
pre = lambda which: {"kind": "unavailable_precondition", "precondition": which, "affected_refs": []}
for which, keyed in KEYED.items():
    for code in CODES:
        for phase in PHASES:
            ok = code == keyed and phase in ("routing", "preparation")
            cb(f"cb_pre_{which}_{code}_{phase}", code, phase, pre(which), A(False) if ok else G("G5", ATT),
               note="keyed and in phase" if ok else ("cross-code" if code != keyed else "phase"))
ERR = {"tag": "no_nodes"}
counts = {"nodes": 2, "members": 1, "springs": 0, "constraints": 6, "nodal_terms": 6, "stations": 3, "supports": 1, "id_utf8_bytes": 0, "directional_springs": 0}
DECL = lambda e: {"input_owner": {"case_index": 1, "case_id": pb1["basis_ref"]["ref_id"], "material_basis_ref": 0}, "constructor_counts": counts, "error": e}
SE = {"kind": "source_error", "error": ERR}
cb("cb_source_error_ok", "source_unavailable", "preparation", SE, OBS, DECL(ERR), "satisfied: not G5 ATTEMPT (later checks may refuse the hand-made decline)")
cb("cb_source_error_no_decline", "source_unavailable", "preparation", SE, G("G5", ATT))
cb("cb_source_error_decline_error_differs", "source_unavailable", "preparation", SE, G("G5", ATT), DECL({"tag": "node_out_of_range", "node": 0}))
cb("cb_source_error_phase_routing", "source_unavailable", "routing", SE, G("G5", ATT), DECL(ERR))
cb("cb_source_error_code_caller", "caller_not_qualified", "preparation", SE, G("G5", ATT), DECL(ERR))
for code in RECEIPT_CODES:
    cb(f"cb_receipt_ok_{code}", code, "receipt", RF, A(False), note="no Run needed for receipt_failure")
cb("cb_receipt_phase_preparation", "receipt_encoding", "preparation", RF, G("G5", ATT))
cb("cb_facade_no_run", "facade_certificate", "facade", FF, G("G5", ATT), note="facade needs a selected Run")
cb("cb_kernel_no_run", "kernel_refused", "kernel", {"space": "refusal", "tag": "structure"}, G("G5", ATT), note="a kernel reason needs a Run")
cb("cb_control_ppf_reason_missing_attempt", "source_unavailable", "preparation", {"kind": "prepared_product_failure", "product_attempt_ref": 1}, OBS,
   note="ppf is outside C2's table (D4c refuses the missing attempt elsewhere)")

# C-c: two_case_preparation_failure_synthetic as is: case 1's product attempt is unavailable (preparation error).
for which, keyed in KEYED.items():
    probe(f"cc_pre_{which}_keyed", "C-c", PB, [S(rb("cases", 1, "reason"), {"code": keyed, "phase": "preparation", "cause": pre(which)})],
          G("G5", PRO), G("G5", PRO), note="C2 satisfied; D19 (product class) then refuses the unavailable attempt")
probe("cc_pre_capture_cross", "C-c", PB, [S(rb("cases", 1, "reason"), {"code": "caller_not_qualified", "phase": "preparation", "cause": pre("capture")})],
      G("G5", ATT), G("G5", ATT))

# C-d: a kernel reason on an idle, refused Run (F_BASE's case 1; its Run made idle).
fb = C[FB]["source"]["retained_precision"]["body"]
run = copy.deepcopy(fb["cases"][1]["run"])
before = run["invocation_before"]
run.update(records=[], attempts=[], case_charge=0, invocation_increment=0, invocation_after=before)
run["cache_after"] = copy.deepcopy(run["cache_before"])
TERM = {"space": "refusal", "tag": "ledger_unavailable", "error": {"tag": "accumulator", "error": {"tag": "non_finite"}}}
run["kernel_terminal"] = {"kind": "refused", "reason": TERM}
idle = [S(rb("cases", 1, "run"), run), S(rb("calls", 0, "invocation_after"), before), S(rb("work", "charged"), before)]


def cd(pid, code, phase, cause, want, note=""):
    probe(pid, "C-d", FB, idle + [S(rb("cases", 1, "reason"), {"code": code, "phase": phase, "cause": cause})], want, want, note=note)


cd("cd_kernel_ok", "kernel_refused", "kernel", TERM, G("G5", PRO), "C2 satisfied; D19 then refuses the unavailable attempt (cause not ppf)")
cd("cd_kernel_code_unresolved", "kernel_unresolved", "kernel", TERM, G("G5", ATT))
cd("cd_kernel_phase_facade", "kernel_refused", "facade", TERM, G("G5", ATT))
cd("cd_kernel_cause_other", "kernel_refused", "kernel", {"space": "refusal", "tag": "structure"}, G("G5", ATT))
cd("cd_ppf_control", "kernel_refused", "kernel", {"kind": "prepared_product_failure", "product_attempt_ref": 1}, OBS,
   "ppf with the kernel reason: outside C2's table")

# ---------------------------------------------------------------------------- T: item 4 (transport)
ev = ["contract_evidence"]
pc0 = ev + ["preview_cases", 0]
x0 = pc0 + ["pipe_stress_extrema", 0]
MEAS = {"result_id": "result:rv113:measure", "component_id": "component:rv113", "pipe_id": "pipe:fixture-span", "location": "end_i",
        "factor_role": "bend", "sif": 1.5, "sif_source_reference": "rv113", "section_modulus_m3": 1e-4,
        "bending_moment_y_n_m": 1.0, "bending_moment_z_n_m": 2.0}
GATE = {"combination_id": "combination:rv113", "withheld": True, "reason": "NONLINEAR_COMBINATION_REQUIRES_SOLVE"}
T = [
    ("t_control", O, [], A(False)),
    ("t_evidence_extra_member", O, [S(ev + ["extra"], 1)], G("G7", EVI)),
    ("t_preview_cases_not_list", O, [S(ev + ["preview_cases"], {})], G("G7", EVI)),
    ("t_case_extra_member", O, [S(pc0 + ["extra"], 1)], G("G7", EVI)),
    ("t_case_id_empty", O, [S(pc0 + ["load_case_id"], "")], G("G7", EVI)),
    ("t_case_id_duplicate", TC, [S(ev + ["preview_cases", 1, "load_case_id"], "case:six-component-load")], G("G7", EVI)),
    ("t_coverage_complete_false", O, [S(pc0 + ["stress_maximum_coverage", "complete"], False)], G("G7", EVI)),
    ("t_coverage_overlap", O, [S(pc0 + ["stress_maximum_coverage"], {"complete": False, "unavailable_pipe_ids": ["p"], "outside_domain_pipe_ids": ["p"]})], G("G7", EVI)),
    ("t_coverage_duplicate_ids", O, [S(pc0 + ["stress_maximum_coverage"], {"complete": False, "unavailable_pipe_ids": ["p", "p"], "outside_domain_pipe_ids": []})], G("G7", EVI)),
    ("t_attributed_and_withheld", O, [S(pc0 + ["support_attribution", "withheld"], [{"support_id": "support:fixture-root", "reason": "CONSTANT_EFFORT_NOT_CONSUMED"}])], G("G7", EVI)),
    ("t_withheld_reason_unknown", O, [S(pc0 + ["support_attribution", "withheld"], [{"support_id": "s", "reason": "OTHER"}])], G("G7", EVI)),
    ("t_withheld_ok", O, [S(pc0 + ["support_attribution", "withheld"], [{"support_id": "s", "reason": "SUPPORT_ACTION_ATTRIBUTION_WITHHELD"}])], A(False)),
    ("t_attribution_sets_differ", TC, [S(ev + ["preview_cases", 1, "support_attribution", "attributed_support_ids"], [])], G("G7", EVI)),
    ("t_withheld_duplicate_multiset", TC, [S(pc0 + ["support_attribution", "withheld"], [{"support_id": "s", "reason": "CONSTANT_EFFORT_NOT_CONSUMED"}] * 2),
                                           S(ev + ["preview_cases", 1, "support_attribution", "withheld"], [{"support_id": "s", "reason": "CONSTANT_EFFORT_NOT_CONSUMED"}])], OBS),
    ("t_extrema_extra_member", O, [S(x0 + ["extra"], 1)], G("G7", EVI)),
    ("t_extrema_approximation_other", O, [S(x0 + ["approximation"], "other")], G("G7", EVI)),
    ("t_extrema_station_fraction_1_5", O, [S(x0 + ["station_fraction"], 1.5)], G("G7", EVI)),
    ("t_extrema_local_fraction_negative", O, [S(x0 + ["local_fraction"], -0.25)], G("G7", EVI)),
    ("t_extrema_span_index_negative", O, [S(x0 + ["span_index"], -1)], G("G7", EVI)),
    ("t_extrema_span_index_fraction", O, [S(x0 + ["span_index"], 0.5)], G("G7", EVI)),
    ("t_extrema_subdivisions_over", O, [S(x0 + ["subdivisions"], 131073)], G("G7", EVI)),
    ("t_extrema_subdivisions_max", O, [S(x0 + ["subdivisions"], 131072)], A(False)),
    ("t_extrema_bounds_inverted", O, [S(x0 + ["value_lower_pa"], 5e7)], G("G7", EVI)),
    ("t_extrema_lower_negative", O, [S(x0 + ["value_lower_pa"], -1.0)], G("G7", EVI)),
    ("t_extrema_upper_string", O, [S(x0 + ["value_upper_pa"], "x")], G("G7", EVI)),
    ("t_extrema_global_upper_string", O, [S(x0 + ["global_upper_bound_pa"], "x")], OBS),
    ("t_extrema_certified_gap_null", O, [S(x0 + ["certified_gap_pa"], None)], OBS),
    ("t_extrema_pipe_in_unavailable", O, [S(pc0 + ["stress_maximum_coverage"], {"complete": False, "unavailable_pipe_ids": ["pipe:fixture-span"], "outside_domain_pipe_ids": []})], G("G7", EVI)),
    ("t_extrema_pipe_duplicate", O, [S(pc0 + ["pipe_stress_extrema", 1], None)], OBS),
    ("t_measure_ok", O, [S(pc0 + ["intensified_measures"], [MEAS])], A(False)),
    ("t_measure_sif_zero", O, [S(pc0 + ["intensified_measures"], [dict(MEAS, sif=0.0)])], G("G7", EVI)),
    ("t_measure_location_mid", O, [S(pc0 + ["intensified_measures"], [dict(MEAS, location="mid")])], G("G7", EVI)),
    ("t_measure_moment_string", O, [S(pc0 + ["intensified_measures"], [dict(MEAS, bending_moment_y_n_m="1")])], G("G7", EVI)),
    ("t_measure_duplicate_result", O, [S(pc0 + ["intensified_measures"], [MEAS, dict(MEAS, component_id="component:rv113b")])], G("G7", EVI)),
    ("t_gate_ok", O, [S(ev + ["combination_gates"], [GATE])], A(False)),
    ("t_gate_withheld_reason_null", O, [S(ev + ["combination_gates"], [dict(GATE, reason=None)])], G("G7", EVI)),
    ("t_gate_released_with_reason", O, [S(ev + ["combination_gates"], [dict(GATE, withheld=False)])], G("G7", EVI)),
    ("t_gate_released_ok", O, [S(ev + ["combination_gates"], [dict(GATE, withheld=False, reason=None)])], A(False)),
    ("t_gate_duplicate", O, [S(ev + ["combination_gates"], [GATE, GATE])], G("G7", EVI)),
    ("t_gate_withheld_string", O, [S(ev + ["combination_gates"], [dict(GATE, withheld="true")])], G("G7", EVI)),
]
for pid, base, edits, want in T:
    probe(pid, "T", base, edits, OBS, OBS, want)
# t_extrema_pipe_duplicate: replace by a real duplicate entry (same pipe twice) when the case has one extremum.
for p in probes:
    if p["id"] == "t_extrema_pipe_duplicate":
        x = copy.deepcopy(C[O]["source"]["contract_evidence"]["preview_cases"][0]["pipe_stress_extrema"][0])
        p["edits"] = [S(pc0 + ["pipe_stress_extrema"], [x, dict(x, result_id="result:rv113:dup")])]
        p["want"]["transport"] = G("G7", EVI)
ids = [p["id"] for p in probes]
assert len(ids) == len(set(ids))
json.dump(probes, open(sys.argv[2], "w"), indent=1)
print(len(probes), "probes ->", sys.argv[2])
