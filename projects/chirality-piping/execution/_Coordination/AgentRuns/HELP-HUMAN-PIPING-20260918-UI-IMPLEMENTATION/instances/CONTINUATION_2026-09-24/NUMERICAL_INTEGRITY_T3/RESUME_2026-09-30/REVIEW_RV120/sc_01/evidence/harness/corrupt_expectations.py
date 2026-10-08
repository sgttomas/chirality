"""RV120 (SC): corrupt chosen 07n expectations in a scratch copy of the corpus, one field per entry, to show that each
reader's own tests read that field and fail on a wrong value. Usage: python3 corrupt_expectations.py <corpus in> <corpus out> <list out>"""
import json
import sys

c = json.load(open(sys.argv[1]))
idx = {e["id"]: e for e in c["mutations"] + c["must_pass"]}
bases = {x["id"]: x for x in c["cases"]}
G5A = {"gate": "G5", "code": "RETAINED_PRECISION_ATTEMPT_MISMATCH"}
done = []


def note(eid, field, old, new, readers):
    done.append({"entry": eid, "field": field, "from": old, "to": new, "should_fail_in": readers})


e = idx["d38_m4_execution_order_lists_case"]; note(e["id"], "expected", e["expected"], G5A, "RS, TS, PY (bound)"); e["expected"] = G5A
e = idx["h_carrier_present"]; new = {"gate": "G7", "code": "SOURCE_PREVIEW_PHYSICS_NUMBER_INVALID"}
note(e["id"], "expected_by_reader.rust and expected_unbound_by_reader.rust", e["expected_by_reader"]["rust"], new, "RS only (bound, unbound)")
e["expected_by_reader"]["rust"] = new; e["expected_unbound_by_reader"]["rust"] = new
e = idx["t_case_extra_member"]; new = {"gate": "G7", "code": "SOURCE_PREVIEW_PHYSICS_EVIDENCE_REQUIRED"}
note(e["id"], "expected, expected_by_reader.python/.typescript and expected_unbound_by_reader.python/.typescript", e["expected"], new, "TS and PY only (bound, unbound)")
e["expected"] = new
for r in ("python", "typescript"):
    e["expected_by_reader"][r] = new; e["expected_unbound_by_reader"][r] = new
e = idx["f_mb_index_1"]; note(e["id"], "expected_unbound", e["expected_unbound"], "pass", "RS, TS, PY (unbound)"); e["expected_unbound"] = "pass"
e = idx["g_combinations_null"]; new = {"gate": "G2", "code": "SOURCE_NUMERICAL_QUALITY_INVALID"}
note(e["id"], "expected_transport", e["expected_transport"], new, "RS, TS, PY (transport)"); e["expected_transport"] = new
e = idx["g_combinations_absent"]; note(e["id"], "expected_eligibility.standing", e["expected_eligibility"]["standing"], "needs_recompute", "TS, PY (RS pins numerical_eligible, not standing)")
e["expected_eligibility"]["standing"] = "needs_recompute"
e = idx["ca_receipt_ok_receipt_encoding"]; note(e["id"], "expected_classifications", "n=%d" % len(e["expected_classifications"]), "last class dropped", "RS, TS, PY (must-pass)")
e["expected_classifications"] = e["expected_classifications"][:-1]
e = idx["cb_source_error_ok"]; note(e["id"], "expected_unbound (must-pass)", e["expected_unbound"], G5A, "RS, TS, PY (unbound)"); e["expected_unbound"] = G5A
b = bases["d38_beside_selected"]; note(b["id"], "base expected_classifications", "n=%d" % len(b["expected_classifications"]), "first class dropped", "RS, TS, PY (base)")
b["expected_classifications"] = b["expected_classifications"][1:]
json.dump(c, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
json.dump(done, open(sys.argv[3], "w"), indent=1)
print(len(done), "corruptions")
