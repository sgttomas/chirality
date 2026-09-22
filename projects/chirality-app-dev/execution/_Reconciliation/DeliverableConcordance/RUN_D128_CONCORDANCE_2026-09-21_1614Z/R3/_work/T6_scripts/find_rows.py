import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_scripts'))
from r3lib import read_csv
h, rows = read_csv(os.path.join(os.path.dirname(__file__), '..', '..', 'CLAIM_CONCORDANCE.csv'))
pat = re.compile(r'agent matrix|agent-matrix|matrix|PORTAL|loop-first|Workbench|Pipeline|composer|9b005c23a|R4-Q4|four-role|Portal', re.I)
mode = sys.argv[1] if len(sys.argv) > 1 else 'list'

for r in rows:
    d = r
    if d['DeliverableID'] != 'DEL-02-01': continue
    txt = ' '.join(d.values())
    hit = pat.search(txt)
    if mode == 'list':
        print(d['ClaimKey'], '|', d['Disposition'], '|', d['CauseTag'], '|', d['HumanDecisionNeeded'], '|', 'HIT' if hit else '', '|', d['DeclaredState'][:90].replace('\n',' '))
    elif mode == 'full' and d['ClaimKey'] in sys.argv[2:]:
        for k in h: print(f'  {k}: {d[k]}')
        print('-----')
