#!/usr/bin/env python3
"""PR-01 source/received-evidence backcheck; no solver, build or source writes."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import hashlib,json,math,random,sys
root=next(p for p in Path(__file__).resolve().parents if (p/'agents/AGENT_TASK.md').is_file())
p=root/'projects/chirality-piping'
d=p/'execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT/SOURCE_RECOVERY_IMPLEMENTATION_01'
r=d/'PRODUCER_READER_REVIEW'
def sha(f): return hashlib.sha256(f.read_bytes()).hexdigest()
def read(f): return json.loads(f.read_text(),parse_int=lambda x:-0.0 if x=='-0' else int(x))
def decimal(q):
    with localcontext() as c:
        c.prec=100
        return str(Decimal(q.numerator)/Decimal(q.denominator))

# Exact reversal of the three bounded producer additions reproduces the
# previously inspected initial file hash. No source snapshot is written.
file=p/'core/product_physics/src/source_receipt/rows.rs'; text=file.read_text()
a=text.index('    // Stress and its summary are two arithmetic layers after projection.')
b=text.index('    let mut out = Vec::new();',a); text=text[:a]+text[b:]
a=text.index('            for (value, action) in [');b=text.index('            let local = open_formula_summary_mpa',a);text=text[:a]+text[b:]
a=text.index('            let nonzero_normal = ');b=text.index('            summary = summary.max(local);',a)
text=text[:a]+'            if !local.is_finite() {\n                return Err(bad("summary range"));\n            }\n'+text[b:]
assert hashlib.sha256(text.encode()).hexdigest()=='bc89b3df80838e0b7690b2a4d9ab47225c2d8745858b95d61bab11a33c7c8ba9'

original=read(d/'_run_records/stress_range_before/dense_scrutiny.raw.json')
assert original['producer']['semantic_contract_id'].endswith('/precision-1')
assert 'source_block_recovery' not in original and original['numerical_quality']['status']=='sensitive'
assert any('exact radix loses represented bits' in v['message'] for v in original['diagnostics'])

records=[]
negative=p/'fixtures/product_preview/source_blocks/rejected_stress_range'
capture=read(negative/'CAPTURE.json')
for f in capture['files']:
    assert sha(negative/f['path'])==f['sha256']
    assert (negative/f['path']).read_bytes()==(d/'_run_records/stress_range_scaled_before'/f['path']).read_bytes()
for mode in ['dense_scrutiny','sparse_interactive']:
    before=d/'_run_records/stress_range_scaled_before'/f'{mode}.raw.json'
    after=d/'_run_records/stress_range_after'/f'{mode}.raw.json'
    request=d/'_run_records/stress_range_scaled_before'/f'{mode}.request.json'
    assert request.read_bytes()==(d/'_run_records/stress_range_after'/f'{mode}.request.json').read_bytes()
    req=read(request); old=read(before); new=read(after)
    assert old['source_block_recovery']['body']['status']=='qualified'
    model=req['model']; section=model['pipe_segments'][0]['section']
    od=section['outside_diameter']['value']; wall=section['wall_thickness']['value']; inner=od-2*wall
    area=math.pi*(od**2-inner**2)/4
    force=model['load_cases'][0]['primitive_loads'][0]['magnitude']['value']
    expected=Q(force)/Q(area)/10**6
    samples=[v for v in old['results'] if v['kind'] in ['element_local_axial_normal_stress','open_formula_stress_summary']]
    assert len(samples)==6
    errors=[abs(Q(v['value'])-expected)/expected for v in samples]
    assert all(v>Q(1,10**9) for v in errors)
    assert new['status']['mechanics']=='MODEL_INCOMPLETE' and 'source_block_recovery' not in new
    failures=[v for v in new['diagnostics'] if v['code']=='SOURCE_BLOCK_RECOVERY_FINALIZATION_FAILED']
    assert len(failures)==1 and 'straight stress MPa publication range' in failures[0]['message']
    records.append({'mode':mode,'request_sha256':sha(request),'before_sha256':sha(before),'after_sha256':sha(after),
        'area_hex':area.hex(),'force_hex':force.hex(),'exact_MPa_fraction':str(expected),'exact_MPa_decimal100':decimal(expected),
        'relative_error_decimal100':decimal(errors[0]),'bad_rows':len(samples),'after_failure':failures[0]['message']})

# Check the successful-case artifact freeze is intact, including the UI pairs.
old_manifest=read(r/'_run_records/FINAL_BASIS.json')
positive=[v for v in old_manifest['inputs'] if '/fixtures/product_preview/source_blocks/' in v['path']]
assert len([v for v in positive if v['path'].endswith('.raw.json')])==12
assert all(sha(root/v['path'])==v['sha256'] for v in positive)

# Simple independent stress pipeline error checks in the newly admitted range.
def normal(x): return math.isfinite(x) and abs(x)>=sys.float_info.min
def admitted(action,pa):
    mpa=pa/1e6
    return (action==0 and pa==0 and mpa==0) or (action!=0 and normal(pa) and normal(mpa))
rng=random.Random(92501); accepted=0; max_error=Q(0)
for _ in range(300):
    action=math.ldexp(rng.choice([-1,1])*rng.uniform(.5,1),rng.randrange(-500,500))
    denominator=math.ldexp(rng.uniform(.5,1),rng.randrange(-300,300))
    pa=action/denominator
    if not admitted(action,pa): continue
    expected=Q(action)/Q(denominator)/10**6; measured=Q(pa/1e6)
    error=abs(measured-expected)/abs(expected)
    max_error=max(max_error,error); assert error<Q(128*sys.float_info.epsilon)
    accepted+=1
assert admitted(0.,0.) and admitted(-0.,-0.)
assert not admitted(1.,0.) and not admitted(0.,1.)
assert not admitted(1.,sys.float_info.min) # normal Pa does not suffice for MPa
assert not admitted(1.,math.inf)
log=d/'_run_records/source_product_public_08.log'
assert '4 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out' in log.read_text()
print(json.dumps({'scope':'narrow source and received-evidence backcheck; no reviewer product execution',
 'producer_sha256':sha(file),'reverse_exact_repair_recovers_initial_hash':True,
 'first_probe_unreachable_and_p1_sensitive_preserved':True,'actual_red_green_records':records,
 'maintained_bad_packets_match_originals':True,'positive_12_pairs_unchanged':True,
 'normal_stress_pipeline_cases':accepted,'max_pipeline_relative_error':decimal(max_error),
 'public08_log_sha256':sha(log),'public08_passes':4,
 'reader_closure':'pending separate final reader freeze/checks'},indent=2))
