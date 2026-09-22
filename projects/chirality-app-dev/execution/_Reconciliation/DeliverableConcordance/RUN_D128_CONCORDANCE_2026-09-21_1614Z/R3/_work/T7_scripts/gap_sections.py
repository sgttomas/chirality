"""Print coverage-gap sections and other gap-term hits from reverse notes of ledgers of record."""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_scripts'))
from r3lib import DELIVERABLE_LEDGERS, R2
pat = re.compile(r'gap|no forward row|no row|unowned|not indexed|missing', re.I)
sel = sys.argv[1:] 
for stem in DELIVERABLE_LEDGERS:
    if sel and not any(stem.startswith(s) for s in sel): continue
    d = os.path.join(R2, stem)
    f = [x for x in os.listdir(d) if x.endswith('_reverse_notes.md')][0]
    lines = open(os.path.join(d, f)).read().splitlines()
    out = []; insec = False
    for i, l in enumerate(lines):
        if l.startswith('#'):
            insec = bool(re.search(r'gap', l, re.I))
        if insec or pat.search(l):
            out.append(f'{i+1}: {l}')
    print(f'## {stem}/{f}'); print('\n'.join(out)); print()
