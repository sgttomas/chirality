"""RV120: probes for I100's two reported PY-only transport differences (ROOT's message): a contract_evidence array over
16,384 items (edited before the rehash), and an integral but unsafe span_index (edited after the rehash: checked JSON
cannot hash the publication with it, and a transport read does not hash the publication). One file per group, because
RS's harness stops at a statement it cannot hash. Usage: python3 gen_probes_rv120x.py <out dir>"""
import json
import sys

out = sys.argv[1]
OBS = {"observe": True}


def probe(pid, edits):
    return {"id": "rv120x:" + pid, "item": "I100-note", "base": "ordinary_prepared_synthetic", "edits": edits,
            "invocation_edits": [], "rehash": "all", "want": {"bound": OBS, "unbound": OBS, "transport": OBS}, "note": "", "set_name": "rv120x"}


def after(pid, after_edits):
    return {"id": "rv120x:" + pid, "item": "I100-note", "base": "ordinary_prepared_synthetic", "edits": [], "after_rehash": after_edits,
            "invocation_edits": [], "rehash": "all", "want": {"bound": OBS, "unbound": OBS, "transport": OBS},
            "note": "edited after rehash (transport does not hash the publication)", "set_name": "rv120x"}


def gates(n):
    return [{"path": ["contract_evidence", "combination_gates"], "op": "set",
             "value": [{"combination_id": f"combination:g{i}", "withheld": True, "reason": "NONLINEAR_COMBINATION_REQUIRES_SOLVE"} for i in range(n)]}]


def span(v):
    return [{"path": ["contract_evidence", "preview_cases", 0, "pipe_stress_extrema", 0, "span_index"], "op": "set", "value": v}]


files = {
    "arrays": [probe("gates_16384", gates(16384)), probe("gates_16385", gates(16385)), probe("gates_1", gates(1))],
    "span_safe": [after("span_2p53m1_after", span(9007199254740991))],
    "span_2p53": [after("span_2p53_after", span(9007199254740992))],
    "span_2p60": [after("span_2p53p1_after", span(9007199254740993)), after("span_2p60_after", span(1152921504606846976))],
}
allp = []
for name, ps in files.items():
    json.dump(ps, open(f"{out}/probes_x_{name}.json", "w"))
    allp += ps
json.dump(allp, open(f"{out}/probes_x_all.json", "w"))
print(len(allp), "written")
