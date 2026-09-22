import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_scripts'))
from r3lib import read_csv
h, rows = read_csv(os.path.join(os.path.dirname(__file__), '..', '..', 'CLAIM_CONCORDANCE.csv'))
keys = ['DEL-02-01#'+k for k in sys.argv[1].split(',')]
fields = sys.argv[2].split(',')
for r in rows:
    if r['ClaimKey'] in keys:
        print('=== ', r['ClaimKey'])
        for f in fields: print(f'  {f}: {r[f]}')
