"""RV123: validate the exact successor fixtures' receipt (and raw rows) against SCHEMA, and the
milestone successors as a control."""
import json, sys
from jsonschema import Draft202012Validator
root = sys.argv[1]
schema = json.load(open(f'{root}/schemas/retained_precision_mp_v2.schema.json'))
Draft202012Validator.check_schema(schema)
v = Draft202012Validator(schema)
raw_row = dict(schema['$defs']['RawRow']); raw_row['$defs'] = schema['$defs']; raw_row.setdefault('$schema', schema.get('$schema'))
vr = Draft202012Validator(raw_row)
print('definition_id enum:', schema['$defs']['ProductAttempt']['properties']['definition_id'])
for name in ['exact_successor_sparse_interactive', 'exact_successor_dense_scrutiny', 'milestone_successor_sparse_interactive', 'milestone_successor_dense_scrutiny']:
    d = json.load(open(f'{root}/fixtures/results/retained_precision_{name}.json'))['source']
    errs = sorted(v.iter_errors(d['retained_precision']), key=lambda e: list(e.path))
    rerrs = [e for r in d['results'] for e in vr.iter_errors(r)]
    print(name, 'receipt errors', len(errs), 'row errors', len(rerrs))
    for e in errs[:5]: print('  ', list(e.path), e.message[:200])
    for e in rerrs[:5]: print('  row', list(e.path), e.message[:200])
    # a negative control: the exact id swapped for an unknown id must fail
    bad = json.loads(json.dumps(d['retained_precision'])); bad['body']['product_attempts'][0]['definition_id'] = 'RP-PREPARED-UNKNOWN-v1'
    print('  control (unknown definition id) errors:', len(list(v.iter_errors(bad))))
