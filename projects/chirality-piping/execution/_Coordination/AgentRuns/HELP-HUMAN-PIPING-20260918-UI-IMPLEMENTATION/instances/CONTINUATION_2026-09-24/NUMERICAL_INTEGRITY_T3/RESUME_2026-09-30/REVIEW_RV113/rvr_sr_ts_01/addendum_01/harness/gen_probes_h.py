"""RV113 (RV-R): transport header probes (B1's alignment set, item 4: the header at G2 in every reader, as RS has it;
the preview-physics metadata at G7). Each probe edits the successor's public members (rehash "all"); `want` holds
the expected transport verdict (RS's header order: schema version, producer, `source_block_recovery` before
`contract_evidence`, numerical quality, its cases, the formulation basis; `carrier_evidence` left to the G7
metadata check). Bound and unbound are observed only.
Usage: python gen_probes_h.py <corpus json> <out json>
"""
import copy
import json
import sys

d = json.load(open(sys.argv[1]))
C = {c["id"]: c for c in d["cases"]}
O = "ordinary_prepared_synthetic"
src = C[O]["source"]
OBS = {"observe": True}


def G(g, c):
    return {"gate": g, "code": c}


def S(path, value):
    return {"path": list(path), "op": "set", "value": value}


def RM(path):
    return {"path": list(path), "op": "remove"}


probes = []


def probe(pid, edits, want, note=""):
    probes.append({"id": pid, "item": "H", "base": O, "edits": edits, "invocation_edits": [], "rehash": "all",
                   "want": {"bound": OBS, "unbound": OBS, "transport": want}, "note": note})


Q, QC, F = ["numerical_quality"], ["numerical_quality", "cases", 0], ["formulation_basis"]
QI, CI, FI = "SOURCE_NUMERICAL_QUALITY_INVALID", "SOURCE_NUMERICAL_CASE_INVALID", "SOURCE_FORMULATION_BASIS_UNSUPPORTED"
LDF, ER, EVI = "SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN", "SOURCE_PREVIEW_PHYSICS_EVIDENCE_REQUIRED", "SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID"
probe("h_control", [], {"admitted": False})
probe("h_recovery_present", [S(["source_block_recovery"], {})], G("G2", LDF))
probe("h_evidence_null", [S(["contract_evidence"], None)], G("G2", ER))
probe("h_evidence_array", [S(["contract_evidence"], [])], G("G2", ER))
probe("h_recovery_and_evidence_null", [S(["source_block_recovery"], {}), S(["contract_evidence"], None)], G("G2", LDF), "RS's order: recovery first")
probe("h_carrier_present", [S(["carrier_evidence"], {})], G("G7", EVI), "no carrier branch in RS's header; the metadata check refuses it")
probe("h_carrier_and_quality_defect", [S(["carrier_evidence"], {}), S(Q + ["status"], "bogus")], G("G2", QI), "the header defect first")
probe("h_carrier_and_recovery", [S(["carrier_evidence"], {}), S(["source_block_recovery"], {})], G("G2", LDF))
probe("h_quality_extra_member", [S(Q + ["extra"], 1)], G("G2", QI))
probe("h_quality_representation", [S(Q + ["value_representation"], "decimal")], G("G2", QI))
probe("h_quality_quantization", [S(Q + ["publication_quantization"], "x")], G("G2", QI))
probe("h_quality_policy", [S(Q + ["integrity_policy"], "x")], G("G2", QI))
probe("h_quality_status_bogus", [S(Q + ["status"], "bogus")], G("G2", QI))
probe("h_quality_cases_object", [S(Q + ["cases"], {})], G("G2", QI))
probe("h_case_extra_member", [S(QC + ["extra"], 1)], G("G2", CI))
probe("h_case_basis_ref_extra", [S(QC + ["basis_ref", "extra"], 1)], G("G2", CI))
probe("h_case_basis_ref_type_empty", [S(QC + ["basis_ref", "ref_type"], "")], G("G2", CI))
probe("h_case_solve_quality_bogus", [S(QC + ["solve_quality"], "bogus")], G("G2", CI))
probe("h_case_structural_bogus", [S(QC + ["structural_status"], "bogus")], G("G2", CI))
probe("h_case_fidelity_bogus", [S(QC + ["model_matrix_fidelity"], "bogus")], G("G2", CI))
probe("h_case_accuracy_bogus", [S(QC + ["accuracy_evidence"], "bogus")], G("G2", CI))
probe("h_case_evidence_refs_empty_string", [S(QC + ["evidence_refs"], [""])], G("G2", CI))
probe("h_case_evidence_refs_not_list", [S(QC + ["evidence_refs"], "x")], G("G2", CI))
probe("h_case_evidence_refs_empty_list", [S(QC + ["evidence_refs"], [])], OBS, "an empty list passes the header")
probe("h_formulation_extra_member", [S(F + ["extra"], 1)], G("G2", FI))
probe("h_formulation_limitations_empty", [S(F + ["limitations"], [])], G("G2", FI))
probe("h_formulation_limitations_empty_string", [S(F + ["limitations"], [""])], G("G2", FI))
probe("h_formulation_limitations_other", [S(F + ["limitations"], ["rv113"])], G("G7", EVI), "the header admits it; the metadata check wants the table's list")
probe("h_quality_and_formulation", [S(Q + ["status"], "bogus"), S(F + ["limitations"], [])], G("G2", QI), "quality before formulation")
probe("h_case_and_formulation", [S(QC + ["accuracy_evidence"], "bogus"), S(F + ["limitations"], [])], G("G2", CI), "cases before formulation")
probe("h_schema_version_010", [S(["schema_version"], "0.1.0")], OBS, "G0 refuses a successor that is not 0.2.0 first, by reading")
json.dump(probes, open(sys.argv[2], "w"), indent=1)
print(len(probes), "probes ->", sys.argv[2])
