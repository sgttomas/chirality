#!/bin/bash
# RV120 B3 (lane T): the producer-derived exact documents against lane T's carrier branches (TS head 77aaaa61d1 schemas):
# the four committed derivative goldens against results.v0.3 (plus two negatives); PY's (b7721d27e9) exact AnalysisRun,
# built from lane P's m3x successors and validated by PY, against analysis_run.v0.3 (plus a negative).
WT=WT
O=$WT/scratch/rv120_rvr/b3/carriers
B=$WT/targets/rv120b3-pybins/release
export OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1
(cd $WT/rv120b3/py/projects/chirality-piping && $WT/venv/bin/python - "$O" <<'PY'
import json, sys
sys.path.insert(0, ".")
from core.analysis_runs.compatibility import build_analysis_run, validate_analysis_run_v0_3
for mode in ("sparse_interactive", "dense_scrutiny"):
    doc = json.load(open(f"fixtures/results/retained_precision_exact_successor_{mode}.json"))
    rec = build_analysis_run(doc["source"], input_manifest_ref={"object_type": "InputManifest", "ref": "manifest:rv120"}, input_manifest_hash="1" * 64)
    validate_analysis_run_v0_3(rec, doc["source"])
    json.dump(rec, open(f"{sys.argv[1]}/exact_analysis_run_{mode}.json", "w"), sort_keys=True)
    print("PY built and validated the exact AnalysisRun", mode, rec["analysis_run"]["reproducibility"]["semantic_contract"]["id"])
PY
)
(cd $WT/rv120b3/ts/projects/chirality-piping && $WT/venv/bin/python - "$O" <<'PY'
import copy, json, sys
sys.path.insert(0, ".")
from tests.test_retained_precision_schema import carrier_schema
from tests.schema_validation import validate_instance
def verdict(schema, doc, label):
    try: validate_instance(schema, doc, instance_label=label); return "valid"
    except AssertionError: return "refused"
rs = carrier_schema("results.v0.3.schema.yaml")
for name in ("retained_precision_exact_successor_derivative_sparse_interactive.json", "retained_precision_exact_successor_derivative_dense_scrutiny.json",
             "retained_precision_successor_derivative_sparse_interactive.json", "retained_precision_successor_derivative_dense_scrutiny.json"):
    print("results.v0.3", name, verdict(rs, json.load(open("fixtures/results/" + name)), name))
doc = json.load(open("fixtures/results/retained_precision_exact_successor_derivative_sparse_interactive.json"))
d = copy.deepcopy(doc); d["result_envelope"]["formulation_basis"]["profile_id"] = "product_preview_retained_w1a_v2"; print("results.v0.3 exact golden, preview profile:", verdict(rs, d, "n1"))
d = copy.deepcopy(doc); del d["result_envelope"]["retained_precision"]; print("results.v0.3 exact golden, no receipt:", verdict(rs, d, "n2"))
ar = carrier_schema("analysis_run.v0.3.schema.json")
for mode in ("sparse_interactive", "dense_scrutiny"):
    rec = json.load(open(f"{sys.argv[1]}/exact_analysis_run_{mode}.json"))
    print("analysis_run.v0.3 PY exact record", mode, verdict(ar, rec, mode))
    r = copy.deepcopy(rec); del r["analysis_run"]["retained_precision"]; print("analysis_run.v0.3 PY exact record without receipt", mode, verdict(ar, r, "n3"))
PY
)
