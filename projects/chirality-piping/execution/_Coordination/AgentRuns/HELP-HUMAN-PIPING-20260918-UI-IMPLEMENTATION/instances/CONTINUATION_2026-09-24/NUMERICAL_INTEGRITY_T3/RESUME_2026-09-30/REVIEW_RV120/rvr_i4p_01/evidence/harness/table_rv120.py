"""RV120: a readable table of one or more readers' verdicts on chosen probes. Usage: table_rv120.py <prefixes,..> <label=jsonl> ..."""
import json, sys
def short(v):
    if v is None: return '-'
    if 'ok' in v: return 'adm(%s)' % v['ok']['numerical_eligible']
    if 'err' in v:
        e = v['err']; d = e.get('detail') or ''
        return e['gate'] + ' ' + e['code'].replace('SOURCE_PREVIEW_PHYSICS_', '…') + (' [' + d.split(': ', 1)[-1] + ']' if e['gate'] == 'G7' and d else '')
    return str(v)[:60]
pre = sys.argv[1].split(',')
runs = {}
for p in sys.argv[2:]:
    k, f = p.split('=', 1); runs[k] = {json.loads(l)['id']: json.loads(l) for l in open(f) if l.strip()}
first = next(iter(runs.values()))
for i in first:
    if any(i.startswith(x) for x in pre):
        for k, R in runs.items():
            r = R.get(i)
            print(i[:40].ljust(40), k.ljust(8), '|', *(short(r[e])[:58].ljust(58) + '|' if r else '-' for e in ('bound', 'unbound', 'transport')))
