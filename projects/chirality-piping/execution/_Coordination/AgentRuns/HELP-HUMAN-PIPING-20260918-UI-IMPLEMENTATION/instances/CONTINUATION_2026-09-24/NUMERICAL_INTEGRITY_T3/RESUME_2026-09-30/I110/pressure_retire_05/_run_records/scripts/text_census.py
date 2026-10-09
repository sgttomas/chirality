"""I110 round 4: per set and output, how many rows contain each declared old/new string. Usage: text_census.py <jsonl> [...]"""
import json, sys, collections
names = ['T1 curved-bend treatment', 'T3a joint basis', 'T3b joint sign', 'T2 formulation limitation', 'T4 preview-physics limitation', 'V1 joint interface warning', 'V2 joint geometry warning']
for path in sys.argv[1:]:
    c = collections.Counter(); rows = collections.Counter()
    for line in open(path):
        r = json.loads(line)
        rows[r['set']] += 1
        for out, rep in r.get('texts', {}).items():
            for i, (old, new) in enumerate(rep['counts']):
                if old: c[(r['set'], out, names[i], 'old')] += 1
                if new: c[(r['set'], out, names[i], 'new')] += 1
    print(path.split('/')[-1], dict(rows))
    for k, v in sorted(c.items()): print('  ', k, v)
