"""I100: further transport probes, for the shapes where PY's transport metadata check and RS's and TS's differ
after rulings 1 and 2 (none is a ruled shape; each is reported to ROOT, not changed). Each edit is applied after
rehash "all" (`after_rehash`): a transport read does not verify the omitted publication, and the checked-JSON
authority could not hash the unsafe integers. Usage: gen_probes_i100x.py <out.json>"""
import json
import sys

E = ["contract_evidence", "preview_cases", 0, "pipe_stress_extrema", 0]
gates = [{"combination_id": f"combination:i100:{k}", "withheld": True, "reason": "NONLINEAR_COMBINATION_REQUIRES_SOLVE"} for k in range(16385)]
probes = [
    {"id": "x100:t_gates_16384", "item": "schema maxItems", "edits": [], "after_rehash": [{"path": ["contract_evidence", "combination_gates"], "op": "set", "value": gates[:16384]}],
     "note": "16,384 distinct gates: at PY's schema-walk default maxItems"},
    {"id": "x100:t_gates_16385", "item": "schema maxItems", "edits": [], "after_rehash": [{"path": ["contract_evidence", "combination_gates"], "op": "set", "value": gates}],
     "note": "16,385 distinct gates: over PY's schema-walk default maxItems (source_blocks._shape); RS and TS have no bound"},
    {"id": "x100:t_span_index_2p53_plus_1", "item": "unsafe integer", "edits": [], "after_rehash": [{"path": E + ["span_index"], "op": "set", "value": 9007199254740993}],
     "note": "an integer above 2^53: RS's safe_integer and TS's Number.isSafeInteger refuse it"},
    {"id": "x100:t_span_index_1e300", "item": "unsafe integer", "edits": [], "after_rehash": [{"path": E + ["span_index"], "op": "set", "value": 1e300}],
     "note": "an integral float far above 2^53: RS and TS refuse it (RV113's RS addendum 02, section 6)"},
]
for p in probes:
    p.update(base="ordinary_prepared_synthetic", invocation_edits=[], rehash="all", want={"bound": {"observe": True}, "unbound": {"observe": True}, "transport": {"observe": True}})
json.dump(probes, open(sys.argv[1], "w"))
print(len(probes), "probes")
