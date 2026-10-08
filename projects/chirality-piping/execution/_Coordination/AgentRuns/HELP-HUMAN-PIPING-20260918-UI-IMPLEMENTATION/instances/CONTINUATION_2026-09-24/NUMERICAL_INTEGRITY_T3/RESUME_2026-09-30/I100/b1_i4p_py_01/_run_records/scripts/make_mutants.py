"""I100: the mutant copy. Each mutant is one guarded edit to the head's reader files, active only when the
environment variable I100_MUT names it (unset: the head's behaviour, the control). Every replaced text is asserted
unique in its file. Usage: make_mutants.py <mutant P root> <out MUTANTS.json>"""
import json
import sys
from pathlib import Path

P = Path(sys.argv[1])
G = '__import__("os").environ.get("I100_MUT")'
MUTANTS = [
    ("M1", "core/analysis_runs/compatibility.py", "ruling 1: the carrier branch restored on the retained transport header",
     'if "carrier_evidence" in source and not rust_header_order:',
     f'if "carrier_evidence" in source and (not rust_header_order or {G} == "M1"):'),
    ("M2", "core/analysis_runs/compatibility.py", "ruling 1: recovery not moved before the evidence demand (Python's order kept on transport)",
     "if rust_header_order and recovery_forbidden:",
     f'if rust_header_order and recovery_forbidden and {G} != "M2":'),
    ("M3", "core/analysis_runs/retained_precision.py", "ruling 1: the transport step does not ask for Rust's order (both moves undone)",
     "_source_contract(projected,check_receipt=False,rust_header_order=True)",
     f'_source_contract(projected,check_receipt=False,rust_header_order={G} != "M3")'),
    ("M4", "core/analysis_runs/compatibility.py", "ruling 1's scope: Rust's order for every caller of _source_contract (the non-retained dispatch too)",
     "    if _is_retained(source):\n        return _retained_contract(source, check_receipt=check_receipt)\n",
     f'    rust_header_order = rust_header_order or {G} == "M4"\n    if _is_retained(source):\n        return _retained_contract(source, check_receipt=check_receipt)\n'),
    ("M5", "core/analysis_runs/preview_physics_evidence.py", "ruling 2: the transport metadata check compares withheld records as sets again",
     "_cases(evidence, withheld_multiset=True)",
     f'_cases(evidence, withheld_multiset={G} != "M5")'),
    ("M6", "core/analysis_runs/preview_physics_evidence.py", "ruling 2: the multiset compared as an ordered list (not sorted)",
     "withheld = (lambda records: tuple(sorted(records))) if withheld_multiset else frozenset",
     f'withheld = (lambda records: tuple(records) if {G} == "M6" else tuple(sorted(records))) if withheld_multiset else frozenset'),
    ("M7", "core/analysis_runs/preview_physics_evidence.py", "ruling 2's scope: the raw evidence check compares multisets too",
     "def _cases(evidence: Mapping[str, Any], *, withheld_multiset: bool = False) -> dict[str, Mapping[str, Any]]:\n",
     f'def _cases(evidence: Mapping[str, Any], *, withheld_multiset: bool = False) -> dict[str, Mapping[str, Any]]:\n    withheld_multiset = withheld_multiset or {G} == "M7"\n'),
    ("M8", "core/analysis_runs/retained_precision.py", "ruling 5: C2's kernel branch without its Run-present conjunct (RV113's P31)",
     'fail(phase == "kernel" and run is not None and code == "kernel_" + run["kernel_terminal"]["kind"]',
     f'fail(phase == "kernel" and (run is not None or {G} == "M8") and code == "kernel_" + run["kernel_terminal"]["kind"]'),
    ("M9", "core/analysis_runs/preview_physics_evidence.py", "kept (ruling 2): the extrema-number demand without global_upper_bound_pa and certified_gap_pa in _cases",
     '_require(all(_number(extremum[key]) for key in ("station_fraction", "local_fraction", "value_lower_pa", "value_upper_pa", "global_upper_bound_pa", "certified_gap_pa")), "extrema numbers")',
     f'_require(all(_number(extremum[key]) for key in ("station_fraction", "local_fraction", "value_lower_pa", "value_upper_pa") + (() if {G} in ("M9", "M10") else ("global_upper_bound_pa", "certified_gap_pa"))), "extrema numbers")'),
    ("M10", "core/analysis_runs/preview_physics_evidence.py", "kept (ruling 2): both PY demands on the two members gone on transport (M9 and the schema walk skipped)",
     '_require(schema_shape(evidence, schema["$defs"]["PreviewPhysicsContractEvidence"], schema), "transport evidence shape")',
     f'_require({G} == "M10" or schema_shape(evidence, schema["$defs"]["PreviewPhysicsContractEvidence"], schema), "transport evidence shape")'),
]
for mid, rel, what, old, new in MUTANTS:
    f = P / rel
    text = f.read_text()
    assert text.count(old) == 1, (mid, rel, text.count(old))
    f.write_text(text.replace(old, new))
json.dump([{"id": m, "file": r, "edit": w} for m, r, w, _, _ in MUTANTS], open(sys.argv[2], "w"), indent=1)
print(len(MUTANTS), "mutants")
