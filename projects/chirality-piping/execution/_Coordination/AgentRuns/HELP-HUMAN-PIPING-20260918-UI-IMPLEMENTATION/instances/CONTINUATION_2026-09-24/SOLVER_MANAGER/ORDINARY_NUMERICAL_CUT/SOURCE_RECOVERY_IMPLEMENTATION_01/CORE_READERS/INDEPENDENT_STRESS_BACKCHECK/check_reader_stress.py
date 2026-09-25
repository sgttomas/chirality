"""Narrow independent reader probes; no producer, build, suite or native run."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, math, sys

HERE = Path(__file__).resolve().parent
PROJECT = next(p for p in HERE.parents if (p/'core/analysis_runs/source_blocks.py').is_file())
sys.path.insert(0, str(PROJECT))
from core.analysis_runs.source_blocks import validate_source_blocks, _derived, STRESS_ARITHMETIC_BOUND, STRESS_INPUT_RELATIVE_LIMIT
from core.analysis_runs.compatibility import numerical_use_standing

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text(), parse_int=lambda token: -0.0 if token == '-0' else int(token))
fixtures = PROJECT/'fixtures/product_preview/source_blocks'
negative = fixtures/'rejected_stress_range'
capture = read(negative/'CAPTURE.json')
for row in capture['files']:
    assert sha(negative/row['path']) == row['sha256']
results = []
for mode in ['dense_scrutiny','sparse_interactive']:
    path = negative/f'{mode}.raw.json'; request = negative/f'{mode}.request.json'
    before = path.read_bytes(); source = read(path)
    context = {'request':read(request),'solver_mode':mode}
    assert source['source_block_recovery']['body']['status'] == 'qualified'
    try:
        validate_source_blocks(source, context)
        raise AssertionError('Unsafe earlier source accepted')
    except ValueError as error:
        assert str(error) in {'SOURCE_BLOCKS_STRESS_OUTPUT_RANGE','SOURCE_BLOCKS_SUMMARY_INPUT_RANGE'}
        reason = str(error)
    bases = [{'ref_type':'load_case','ref_id':c['id']} for c in context['request']['model']['load_cases']]
    assert numerical_use_standing(source, bases, context) != 'numerically_eligible'
    assert path.read_bytes() == before
    results.append({'path':str(path.relative_to(PROJECT)), 'sha256':sha(path), 'claimed_status':'qualified', 'reader_refusal':reason, 'bytes_unchanged':True})
for name, mode in [('n05','dense_scrutiny'),('n06','sparse_interactive')]:
    path = fixtures/f'{name}-{mode}.raw.json'; request = fixtures/f'{name}-{mode}.request.json'
    before = path.read_bytes(); source = read(path); context = {'request':read(request),'solver_mode':mode}
    assert validate_source_blocks(source,context) is True
    assert validate_source_blocks(source) is False
    assert path.read_bytes() == before
    results.append({'path':str(path.relative_to(PROJECT)), 'sha256':sha(path), 'with_context':True, 'without_context':False, 'bytes_unchanged':True})

def scalar(action, output, location='midspan'):
    row={'kind':'element_local_axial_normal_stress','unit':'MPa','entity_ref':'scope:reader','value':output,'metadata':{'location':location,'component':'axial_normal_stress'}}
    input_row={'kind':'element_local_axial_force','unit':'N','entity_ref':'scope:reader','value':action,'metadata':{'location':location}}
    try:
        _derived('straight_open_stress_v1',row,[input_row])
        return 'accepted'
    except ValueError as error:
        return str(error)

boundary=[('exact_zero',0.0,0.0,'midspan',True),('negative_zero',0.0,-0.0,'midspan',True),
          ('normal_boundary',1.0,sys.float_info.min,'midspan',True),
          ('below_normal_boundary',1.0,math.nextafter(sys.float_info.min,0.0),'midspan',False),
          ('nonzero_erased',1.0,0.0,'midspan',False),('zero_invented',0.0,1.0,'midspan',False),
          ('endpoint_sign',-1.0,1.0,'end_i',True),('wrong_endpoint_sign',1.0,1.0,'end_i',False),
          ('observed_pa_overflow',1.0,sys.float_info.max,'midspan',False),('nonfinite_output',1.0,math.inf,'midspan',False)]
scalar_results=[]
for name,action,value,location,accepted in boundary:
    result=scalar(action,value,location);assert (result=='accepted')==accepted
    scalar_results.append({'name':name,'result':result})

# The algebraic composition is r+a+r*a. This reports the actual binary64
# threshold and its representational distance, not a hidden arithmetic proof.
r,a=Fraction.from_float(STRESS_INPUT_RELATIVE_LIMIT),Fraction.from_float(STRESS_ARITHMETIC_BOUND)
composed=r+a+r*a
table=PROJECT/'fixtures/results/semantic_contract_v0_3_precision_1.json'
source_table=PROJECT/'fixtures/results/semantic_contract_v0_3_source_blocks_1.json'
old,new=read(table),read(source_table)
assert sha(table)=='d75aacee175e178dbdeb256d89a65f4b375265f7da077725ee635af33df51d7e'
assert new['rows'][:60] == old['rows']
output={'scope':'Actual retained received packets and scalar reader guards only; no fresh solve/native/source-authentication claim',
        'packet_results':results,'scalar_results':scalar_results,
        'composition':{'arithmetic_bound':STRESS_ARITHMETIC_BOUND,'input_limit':STRESS_INPUT_RELATIVE_LIMIT,'composed_as_float':float(composed),'exact_composed_minus_binary64_limit':float(composed-Fraction.from_float(1e-9))},
        'p1_sha256':sha(table),'source_table_sha256':sha(source_table),'unchanged_p1_rows':True}
(HERE/'INDEPENDENT_PROBES.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
