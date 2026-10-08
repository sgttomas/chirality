"""I105: SCHEMA (G1 shape) of each successor document's receipt body, and of the milestone's as a control.
Usage: schema_check.py <schema> <document.json>..."""
import json, sys
from jsonschema import Draft202012Validator
schema = json.load(open(sys.argv[1]))
v = Draft202012Validator(schema)
for path in sys.argv[2:]:
    doc = json.load(open(path))
    src = doc.get('source', doc)
    body = src['retained_precision']
    errors = sorted(v.iter_errors(body), key=lambda e: list(e.path))
    print(path.rsplit('/', 1)[-1], 'errors', len(errors))
    for e in errors[:5]:
        print('  ', list(e.path)[:8], e.message[:200])
