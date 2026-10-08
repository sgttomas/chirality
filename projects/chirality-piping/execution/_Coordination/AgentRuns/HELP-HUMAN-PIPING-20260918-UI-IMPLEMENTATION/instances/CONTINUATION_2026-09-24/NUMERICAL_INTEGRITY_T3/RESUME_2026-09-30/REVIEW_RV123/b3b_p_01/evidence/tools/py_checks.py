"""RV123: PY's physics-1 base reader (G7's projection) on the exact successor fixtures, and on the
candidate's noticed m3x/m3x_mix_anchor Direct publications against their plain bytes (N-11).
Usage: py_checks.py <candidate P root> <bytes dir>"""
import json, sys, copy
from pathlib import Path
P = Path(sys.argv[1]).resolve(); B = Path(sys.argv[2])
sys.path.insert(0, str(P))
from core.analysis_runs import compatibility as c
from core.analysis_runs import retained_precision as rpy
fails = 0
for mode in ['sparse_interactive', 'dense_scrutiny']:
    doc = json.loads((P / f'fixtures/results/retained_precision_exact_successor_{mode}.json').read_text())
    src = doc['source']
    p = copy.deepcopy(src); p.pop('retained_precision')
    p['producer']['semantic_contract_id'] = c.PHYSICS_CONTRACT_ID
    p['formulation_basis']['profile_id'] = 'exact_straight_pressure_v2'
    for r in p['results']: r.pop('recovery_method', None)
    try:
        con = c._source_contract(p)[:2]; ok = con == (c.PHYSICS_CONTRACT_ID, c.PHYSICS_CONTRACT_SHA256)
    except Exception as e:
        con = repr(e)[:200]; ok = False
    refs = [{"ref_type": "load_case", "ref_id": k["id"]} for k in doc['invocation']['request']['model']['load_cases']]
    print(f'PY_G7 {mode} contract={con} ok={ok} standing={c.numerical_use_standing(p, refs) if ok else None}')
    fails += not ok
    # Today's PY retained reader on the exact successor itself.
    try:
        out = rpy.validate_retained_precision(src, doc['invocation'])
        print(f'PY_RETAINED {mode} accepted {out!r:.120}')
    except Exception as e:
        print(f'PY_RETAINED {mode} refused {type(e).__name__}: {str(e)[:160]}')
for name in ['i99_m3x', 'i99_m3x_mix_anchor']:
    for mode in ['sparse_interactive', 'dense_scrutiny']:
        plain = json.loads((B / 'cand' / f'{name}.{mode}.plain.json').read_text())
        direct = json.loads((B / 'cand' / f'{name}.{mode}.direct.json').read_text())
        inv = json.loads((P / f'fixtures/results/retained_precision_exact_successor_{mode}.json').read_text())['invocation'] if name == 'i99_m3x' else None
        model = (inv['request'] if inv else json.loads((Path(sys.argv[3]) / 'm3x_mix_anchor.json').read_text()))['model']
        refs = [{"ref_type": "load_case", "ref_id": k["id"]} for k in model['load_cases']]
        a, b = c._source_contract(plain)[:2], c._source_contract(direct)[:2]
        ok = a == b == (c.PHYSICS_CONTRACT_ID, c.PHYSICS_CONTRACT_SHA256) and c.standing_reason(plain) == c.standing_reason(direct) \
            and c.numerical_use_standing(plain, refs) == c.numerical_use_standing(direct, refs)
        n = sum(d['code'] == 'RETAINED_PRECISION_UNAVAILABLE' for d in direct['diagnostics'])
        print(f'PY_N11 {name} {mode} notices={n} standing={c.numerical_use_standing(direct, refs)} ok={ok}')
        fails += not ok
print(f'PY_FAILS {fails}')
