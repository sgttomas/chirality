"""RV113 (RV-R): a further C2 probe for SR-PY repair 02's mutant P18 (P31 is already killed by r2:cb_kernel_no_run):
a source error on an unavailable case beside a selected Run (the case's source reference null, as the schema's
decline variant requires), rehash "all". `want` is the ruled first failure (C2's table at G5 ATTEMPT), bound and unbound.
Usage: python gen_probes_py2x.py <probes_ts1.json> <out json>
"""
import copy
import json
import sys

P = {p["id"]: p for p in json.load(open(sys.argv[1]))}
ATT = {"gate": "G5", "code": "RETAINED_PRECISION_ATTEMPT_MISMATCH"}
OBS = {"observe": True}
out = []

# 2. A source error on a case beside a selected Run: C2's source_error branch needs no Run.
s = copy.deepcopy(P["r2:ca_precondition_beside_run"])
case = s["edits"][0]["value"]
decline = copy.deepcopy(P["r2:cb_source_error_ok"]["edits"][0]["value"]["source_decline"])
decline["input_owner"]["case_id"] = case["basis_ref"]["ref_id"]
case["reason"] = {"code": "source_unavailable", "phase": "preparation", "cause": {"kind": "source_error", "error": copy.deepcopy(decline["error"])}}
case["source_decline"] = decline
case["source_ref"] = None
out.append({"id": "x:c2_source_error_beside_run", "item": "C2x", "base": s["base"], "edits": s["edits"],
            "invocation_edits": s.get("invocation_edits", []), "rehash": "all", "want": {"bound": ATT, "unbound": ATT, "transport": OBS},
            "note": "source_error branch: no Run (P18)"})
json.dump(out, open(sys.argv[2], "w"), indent=1)
print(len(out), "probes")
