"""I105: the mutant results for the records (no timing field) and a one-line-per-mutant table.
Usage: mut_summary.py <results.json>... <out json>  (later files override earlier ids)."""
import json, pathlib, sys
rows = {}
for f in sys.argv[1:-1]:
    for r in json.loads(pathlib.Path(f).read_text()):
        r.pop('seconds', None)
        rows[r['id']] = r
out = [rows[k] for k in sorted(rows, key=lambda x: int(x.split('-')[1]))]
pathlib.Path(sys.argv[-1]).write_text(json.dumps(out, indent=1) + '\n')
from collections import Counter
print(Counter(r['verdict'] for r in out))
for r in out:
    print(r['id'], r['verdict'], r['check'], (r['failed'][0] if r['failed'] else ''), len(r['failed']))
