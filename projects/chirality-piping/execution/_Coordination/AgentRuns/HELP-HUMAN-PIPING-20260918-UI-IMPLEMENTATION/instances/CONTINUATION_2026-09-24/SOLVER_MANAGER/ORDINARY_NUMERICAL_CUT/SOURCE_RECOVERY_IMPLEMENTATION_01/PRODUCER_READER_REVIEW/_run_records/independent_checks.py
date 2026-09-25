#!/usr/bin/env python3
"""Bounded analytical and static checks; no solver/build/canonicalizer execution."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
import math
import random
import struct

root = next(p for p in Path(__file__).resolve().parents if (p/'agents/AGENT_TASK.md').is_file())
project = root/'projects/chirality-piping'
sys.path.insert(0,str(project))
from core.analysis_runs.source_blocks import _derived

def bits(v): return struct.pack('>d',v).hex()
def recipe(x):
    m=max(abs(v) for v in x)
    if m==0: return 0.0
    a,b,c=[v/m for v in x]
    return m*math.sqrt((a*a+b*b)+c*c)
def reader(x,y,support=False):
    kinds=['global_nodal_displacement_x','global_nodal_displacement_y','global_nodal_displacement_z']
    comps=['Fx','Fy','Fz']
    inputs=[{'kind':'support_reaction_component_v2' if support else kinds[i],
             'metadata':{'component':comps[i]},'entity_ref':'independent-review','value':v} for i,v in enumerate(x)]
    row={'kind':'reaction_resultant' if support else 'displacement_magnitude',
         'unit':'N' if support else 'mm','entity_ref':'independent-review','value':y}
    _derived('support_force_norm_scaled_v1' if support else 'translation_norm_scaled_v1',row,inputs)

cases=[[0.,-0.,0.],[3.,4.,0.],[sys.float_info.min,0.,0.],
       [1e-160,1e-300,0.],[1e308,1e-300,0.],[1.,math.ulp(0.),0.],
       [math.ulp(0.),0.,0.],[sys.float_info.max,sys.float_info.max,0.]]
rng=random.Random(9252026)
for _ in range(400):
    scale=rng.randrange(-1022,1023)
    cases.append([math.ldexp(rng.choice([-1,1])*rng.uniform(.5,1),max(-1074,scale-rng.randrange(0,1100))) for _ in range(3)])
max_relative=Decimal(0); successes=0; rejected=0; mutations=0
with localcontext() as ctx:
    ctx.prec=150
    for x in cases:
        y=recipe(x)
        eligible=math.isfinite(y) and (all(v==0 for v in x) or y>=sys.float_info.min)
        for support in [False,True]:
            try: reader(x,y,support)
            except ValueError:
                assert not eligible
            else: assert eligible
        if not eligible:
            rejected+=1; continue
        successes+=1
        oracle=sum(Decimal.from_float(v)**2 for v in x).sqrt()
        error=abs(Decimal.from_float(y)-oracle)/oracle if oracle else Decimal(0)
        max_relative=max(max_relative,error)
        assert error < Decimal.from_float(64*sys.float_info.epsilon)
        if y==0: assert bits(y)=='0000000000000000'
        bad=math.nextafter(y,math.inf)
        if math.isfinite(bad):
            try: reader(x,bad)
            except ValueError: mutations+=1
            else: raise AssertionError('one-ULP mutation accepted')

# Structural ledger math: rejected reservations never increase charged work;
# reserved-unobserved failure is separate and is debited only once.
ledger_checks=0
for cap in [0,1,7,100,4_000_000,64_000_000]:
    for accepted in [0,min(1,cap),cap]:
        for attempted in [0,1,cap,cap+1]:
            next_charged=accepted+attempted if attempted<=cap-accepted else accepted
            denied=0 if attempted<=cap-accepted else attempted
            assert next_charged<=cap
            if denied: assert next_charged==accepted
            ledger_checks+=1

old=json.loads((project/'fixtures/results/semantic_contract_v0_3_precision_1.json').read_text())
new=json.loads((project/'fixtures/results/semantic_contract_v0_3_source_blocks_1.json').read_text())
assert new['rows'][:60]==old['rows']
assert len(new['rows'])==66
assert {r['component'] for r in new['rows'][60:]}=={'Fx','Fy','Fz','Mx','My','Mz'}
assert hashlib.sha256((project/'fixtures/results/semantic_contract_v0_3_precision_1.json').read_bytes()).hexdigest()=='d75aacee175e178dbdeb256d89a65f4b375265f7da077725ee635af33df51d7e'

fixture_dir=project/'fixtures/product_preview/source_blocks'
fixture_records=[]
for p in sorted(fixture_dir.rglob('*.raw.json')):
    source=json.loads(p.read_text(),parse_int=lambda token:-0.0 if token=='-0' else int(token))
    body=source['source_block_recovery']['body']; work=body['invocation_work']
    summed=sum(c['work']['charged']+c['work']['reserved_unobserved_failure'] for c in body['cases'])
    assert summed+work['publication_charged']==work['charged']<=work['limit']<=64_000_000
    assert all(c['work']['charged']+c['work']['reserved_unobserved_failure']<=c['work']['limit']<=4_000_000 for c in body['cases'])
    norms=0
    rows={r['id']:r for r in source['results']}
    for case in body['cases']:
        for row in case['rows']:
            recipe_id=row['recipe_id']
            if recipe_id in ['translation_norm_scaled_v1','support_force_norm_scaled_v1']:
                target=rows[row['result_id']]; inputs=[rows[i] for i in row['input_result_ids']]
                assert bits(recipe([r['value'] for r in inputs]))==bits(target['value'])
                _derived(recipe_id,target,inputs); norms+=1
    fixture_records.append({'path':str(p.relative_to(root)),
        'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'norm_rows':norms,
        'case_count':len(body['cases']),'invocation_charged':work['charged'],
        'negative_zero_rows':sum(bits(r['value'])=='8000000000000000' for r in source['results'])})
print(json.dumps({'scope':'bounded independent Decimal/rational accounting/static checks and actual Python recipe only; no solver/build/native/full validator execution',
 'norm_cases':len(cases),'accepted_normal_or_zero':successes,'range_rejections':rejected,
 'max_observed_relative_error_against_150_digit_decimal':str(max_relative),
 'one_ulp_mutations_rejected':mutations,'small_ledger_checks':ledger_checks,
 'p1_60_signatures_and_hash_unchanged':True,'received_artifacts':fixture_records},indent=2))
