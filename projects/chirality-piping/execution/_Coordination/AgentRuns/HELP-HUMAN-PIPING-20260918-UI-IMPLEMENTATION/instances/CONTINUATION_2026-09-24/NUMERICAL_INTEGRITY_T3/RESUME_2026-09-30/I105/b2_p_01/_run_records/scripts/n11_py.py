"""I105 (B3b-P, N-11): physics-1's PY base reader on each exact fallback envelope.
For each <tag>_base.json / <tag>_noticed.json pair: the same source contract (id and sha256), standing
reason and numerical-use standing for the requested cases. Usage: n11_py.py <P root> <out dir>"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]).resolve()))
from core.analysis_runs import compatibility as c
out = Path(sys.argv[2])
failures = 0
for base_path in sorted(out.glob('*_base.json')):
    tag = base_path.name[:-len('_base.json')]
    base = json.loads(base_path.read_text())
    noticed = json.loads((out / f'{tag}_noticed.json').read_text())
    invocation = json.loads((out / f'{tag}_invocation.json').read_text())
    refs = [{"ref_type": "load_case", "ref_id": case["id"]} for case in invocation["request"]["model"]["load_cases"]]
    contract = c._source_contract(base)[:2]
    ok = (contract == (c.PHYSICS_CONTRACT_ID, c.PHYSICS_CONTRACT_SHA256)
          and c._source_contract(noticed)[:2] == contract
          and c.standing_reason(noticed) == c.standing_reason(base)
          and c.numerical_use_standing(noticed, refs) == c.numerical_use_standing(base, refs))
    notices = [d for d in noticed["diagnostics"] if d["code"] == "RETAINED_PRECISION_UNAVAILABLE"]
    print(f"N11_PY {tag} contract={contract[0]} standing={c.numerical_use_standing(noticed, refs)} notices={len(notices)} ok={ok}")
    # Negative control: the same reader refuses the noticed envelope with a non-empty connector.
    bad = json.loads(json.dumps(noticed))
    bad["contract_evidence"]["connector"] = [{}]
    try:
        c._source_contract(bad)
        refused = False
    except Exception as error:  # the reader's own refusal
        refused = True
    print(f"N11_PY {tag} negative_control_refused={refused}")
    failures += (not ok) + (not refused)
print(f"N11_PY failures={failures}")
sys.exit(1 if failures else 0)
