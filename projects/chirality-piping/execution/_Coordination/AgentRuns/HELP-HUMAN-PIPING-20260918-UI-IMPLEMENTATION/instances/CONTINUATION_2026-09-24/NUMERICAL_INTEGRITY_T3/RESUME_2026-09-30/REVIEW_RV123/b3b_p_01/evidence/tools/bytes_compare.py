"""RV123: compare the harness's base and candidate outputs, input by input and mode by mode, and the
committed physics-source raw fixtures; for a candidate publication that differs from its plain
bytes, check it is exactly the plain bytes plus one notice per noticed case (T-12's text)."""
import hashlib, json, sys
from pathlib import Path
B = Path(sys.argv[1]); PS = Path(sys.argv[2])
def notice(case):
    return ('{"id":"diagnostic:retained-precision:%s:unavailable","code":"RETAINED_PRECISION_UNAVAILABLE","severity":"info",'
            '"message":"Retained-precision recovery is unavailable for this load case. Its published rows keep their ordinary values, standing and diagnostics.",'
            '"source":"core/product_physics","affected_refs":["%s"]}') % (case, case)
def with_notices(plain, cases):
    t = plain.decode(); head, tail = t.split('"diagnostics":[', 1); close = tail.find('],"professional_boundary"')
    items, rest = tail[:close], tail[close:]
    for c in cases:
        items = items + (',' if items else '') + notice(c)
    return (head + '"diagnostics":[' + items + rest).encode()
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
names = sorted({p.name.split('.')[0] for p in (B / 'cand').glob('*.plain.json')})
for n in names:
    for mode in ['sparse_interactive', 'dense_scrutiny']:
        f = lambda side, kind: (B / side / f'{n}.{mode}.{kind}.json').read_bytes()
        bp, bd, cp, cd = f('base', 'plain'), f('base', 'direct'), f('cand', 'plain'), f('cand', 'direct')
        line = f'{n:22} {mode:18} plain base==cand {bp == cp}  direct base==cand {bd == cd}  cand direct==plain {cd == cp}'
        if cd != cp:
            noticed = [d['affected_refs'][0] for d in json.loads(cd)['diagnostics'] if d['code'] == 'RETAINED_PRECISION_UNAVAILABLE']
            line += f'  cand direct == plain+notices{noticed} {with_notices(cp, noticed) == cd}'
            if json.loads(cd).get('retained_precision') is not None: line += '  (successor)'
        if bd != cd:
            line += f'  [base direct==base plain {bd == bp}]'
        if n.startswith('ps_'):
            raw = PS / f'{n[3:]}-{mode}.raw.json'
            if raw.exists():
                line += f'  committed raw==cand plain {json.loads(raw.read_text()) == json.loads(cp)} (bytes {raw.read_bytes().rstrip(b"\n") == cp})'
        print(line)
