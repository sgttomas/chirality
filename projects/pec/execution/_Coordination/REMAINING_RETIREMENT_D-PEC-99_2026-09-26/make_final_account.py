#!/usr/bin/env python3
"""Write FINAL_ROW_ACCOUNT.csv: a copy of the D-PEC-99 account with only AppliedResult set.
Run from the repository root after the generator commit. Stdlib only."""
import csv, hashlib, io, sys
TM = 'projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/'
SRC, OUT = TM + 'SEMANTIC_DECISION_ACCOUNT.csv', TM + 'FINAL_ROW_ACCOUNT.csv'
EX = 'projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md'
ACT = '5066f895c'  # generator commit
src = open(SRC, 'rb').read()
assert hashlib.sha256(src).hexdigest() == 'b240b38d940448a66b37752a1f2509ea4c6783f388c0a8d6cb0d3d21a465f7e2'
exsha = hashlib.sha256(open(EX, 'rb').read()).hexdigest()
assert exsha == '69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e'
text = src.decode('utf-8')
rd = csv.DictReader(io.StringIO(text, newline=''))
fields, rows = rd.fieldnames, list(rd)
ex = 'exhibit `%s` (SHA-256 %s)' % (EX, exsha[:12])
for r in rows:
    live = r['Population'] == 'LIVE_REMAINING'
    tail = ('; its `_STATUS.md` entry removed by the D-PEC-99 generator (commit %s) with a History line naming the key' % ACT) if live \
        else '; frozen carrier item, never applied to any `_STATUS.md`, so nothing was removed and no DEL-01-05 file was written (D-PEC-83 F closed without application, owner "confirm F")'
    c = r['DestinationClass']
    if c == 'EXHIBIT_A_D83E':
        v = 'APPLIED MOVED_EXHIBIT_A: carried verbatim (text, Depends, gate) in Part A of the D-PEC-99 %s, unselected' % ex
    elif c.startswith('EXHIBIT_B_CARRY_'):
        n = c.rsplit('_', 1)[1]
        v = 'APPLIED MOVED_EXHIBIT_B_%s: carried verbatim (text, Depends, gate) with its carry-forward input in Part B (node %s) of the D-PEC-99 %s; no Scope of Work written (the %s packet absorbs it under its own ruling)' % (n, n, ex, n)
    elif c == 'OWNER_DECISION':
        v = 'APPLIED MOVED_EXHIBIT_B_S1: owner question 1 answered (a) ("Q1 a"); carried verbatim (text, Depends, gate) with its carry-forward input in Part B (node S1) of the D-PEC-99 %s; no Scope of Work written' % ex
    elif c == 'CLOSED_ON_RECORD':
        v = 'APPLIED CLOSED_ON_RECORD: closed on the record cited in Evidence; not carried in the exhibit'
    else:
        sys.exit('unexpected class ' + c)
    r['AppliedResult'] = v + tail
buf = io.StringIO(newline='')
w = csv.DictWriter(buf, fieldnames=fields, lineterminator='\r\n' if '\r\n' in text else '\n')
w.writeheader(); w.writerows(rows)
open(OUT, 'w', encoding='utf-8', newline='').write(buf.getvalue())
print('WROTE %s %d rows sha256=%s' % (OUT, len(rows), hashlib.sha256(buf.getvalue().encode('utf-8')).hexdigest()))
