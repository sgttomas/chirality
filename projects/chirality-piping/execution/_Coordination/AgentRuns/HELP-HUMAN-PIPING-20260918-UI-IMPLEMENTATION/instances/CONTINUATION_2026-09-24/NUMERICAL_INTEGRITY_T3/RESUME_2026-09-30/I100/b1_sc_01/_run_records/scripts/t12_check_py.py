"""I100 B1 SC: PY's check of SP's several-notice bytes (T-12; I85's F/t12_bytes, RETURN §3.6), at the scratch merge.

Usage: t12_check_py.py <P root> <t12_bytes dir> <out.json>

For each mode, the W-C2 ordinary envelope (base), and the same envelope with case-a's and case-c's
RETAINED_PRECISION_UNAVAILABLE notices, plain and with the receipt detail on case-a's only: Python's base readers give
the same contract (raw and transport dispatch), the same standing for the requested cases, the same binding refusals
and classification summary, and an AnalysisRun record that validates against its envelope. The notices are counted.
"""
import copy
import hashlib
import json
import sys
from pathlib import Path

root, t12, out = sys.argv[1:4]
sys.path.insert(0, root)
from core.analysis_runs import compatibility as c  # noqa: E402

request = json.loads(Path(t12, "w_c2_request.json").read_text())
refs = [{"ref_type": "load_case", "ref_id": x["id"]} for x in request["model"]["load_cases"]]
res = {"request_sha256": hashlib.sha256(Path(t12, "w_c2_request.json").read_bytes()).hexdigest(), "modes": {}}
ok = True


def read(env):
    o = {}
    for name, fn in (("raw", lambda e: c._source_contract(e)[:2]), ("transport", lambda e: c._source_contract(e, check_receipt=False)[:2])):
        try:
            o[name] = list(fn(copy.deepcopy(env)))
        except ValueError as error:
            o[name] = f"refused: {error}"
    o["standing"] = c.numerical_use_standing(copy.deepcopy(env), refs)
    o["binding"] = [c.rule_binding_refusal(env, row) for row in env["results"]]
    o["summary"] = c.classification_summary(copy.deepcopy(env), None, refs)
    try:
        record = c.build_analysis_run(copy.deepcopy(env), input_manifest_ref={"object_type": "InputManifest", "ref": "manifest:t12"}, input_manifest_hash="1" * 64)
        c.validate_analysis_run_v0_3(record, copy.deepcopy(env))
        o["record"] = "validates"
    except Exception as error:  # noqa: BLE001 -- recorded, not hidden
        o["record"] = f"{type(error).__name__}: {error}"
    return o


for mode in ("sparse_interactive", "dense_scrutiny"):
    files = {k: Path(t12, f"w_c2_{k}_{mode}.json") for k in ("base", "noticed_plain", "noticed_receipt")}
    docs = {k: json.loads(p.read_text()) for k, p in files.items()}
    base_ids = {d["id"] for d in docs["base"]["diagnostics"]}
    m = {"sha256": {k: hashlib.sha256(p.read_bytes()).hexdigest() for k, p in files.items()}}
    reads = {k: read(v) for k, v in docs.items()}
    m["reads"] = {k: {kk: vv for kk, vv in v.items() if kk not in ("binding", "summary")} for k, v in reads.items()}
    m["notices"] = {k: [d["id"] for d in v["diagnostics"] if d["id"] not in base_ids and d["code"] == "RETAINED_PRECISION_UNAVAILABLE"] for k, v in docs.items()}
    m["same_as_base"] = {k: reads[k] == reads["base"] for k in ("noticed_plain", "noticed_receipt")}
    m["only_notices_added"] = {k: [d for d in docs[k]["diagnostics"] if d["id"] in base_ids] == docs["base"]["diagnostics"]
                               and {kk: vv for kk, vv in docs[k].items() if kk != "diagnostics"} == {kk: vv for kk, vv in docs["base"].items() if kk != "diagnostics"}
                               for k in ("noticed_plain", "noticed_receipt")}
    ok = ok and all(m["same_as_base"].values()) and all(m["only_notices_added"].values()) and all(len(m["notices"][k]) == 2 for k in ("noticed_plain", "noticed_receipt")) \
        and reads["base"]["standing"] == "needs_recompute" and isinstance(reads["base"]["raw"], list)
    res["modes"][mode] = m
res["ok"] = ok
Path(out).write_text(json.dumps(res, indent=1) + "\n")
print(json.dumps({"ok": ok, **{mode: {"same_as_base": v["same_as_base"], "notices": {k: len(x) for k, x in v["notices"].items()}, "base": v["reads"]["base"]} for mode, v in res["modes"].items()}}, indent=1))
