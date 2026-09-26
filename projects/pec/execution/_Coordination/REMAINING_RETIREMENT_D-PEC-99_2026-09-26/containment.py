#!/usr/bin/env python3
"""Containment of the RR3 branch diff (read-only). Run from the repository root:
python3 <run root>/containment.py [base]   (default base origin/main; compares base...HEAD)
Allowed: the 62 paths in the generator report, the run root, FINAL_ROW_ACCOUNT.csv, the RR3 brief and
return copies. HELP_HUMAN's later graph/STATUS/README/register lines are reported separately, not failed."""
import subprocess, sys
base = sys.argv[1] if len(sys.argv) > 1 else 'origin/main'
RR = 'projects/pec/execution/_Coordination/REMAINING_RETIREMENT_D-PEC-99_2026-09-26/'
grant = {l.split()[2] for l in open(RR + 'checks/gen_act.out', encoding='utf-8') if l.startswith('POST ')}
extra = {'projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/FINAL_ROW_ACCOUNT.csv',
         'projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/RR3_D99_RETIREMENT_ACT.md',
         'projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/RR3_D99_RETIREMENT_ACT.md'}
hh = ('projects/pec/execution/_Coordination/WorkGraphs/', 'projects/pec/docs/STATUS.md', 'projects/pec/README.md',
      'projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md', 'projects/pec/execution/_Coordination/AgentRuns/')
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
out = subprocess.check_output(['git', 'diff', '--name-status', base + '...HEAD'], text=True).splitlines()
seen, bad, hhs, rr = set(), [], [], 0
for l in out:
    st, p = l.split('\t')[0], l.split('\t')[-1]
    if p in grant:
        seen.add(p)
    elif p.startswith(RR):
        rr += 1
    elif p in extra:
        pass
    elif p.startswith(hh):
        hhs.append(l)
    else:
        bad.append(l)
    if st.startswith('D'):
        bad.append('deleted ' + p)
print('HEAD %s base %s' % (head, base))
print('grant paths in diff %d/62; run-root files %d; other allowed %s; HELP_HUMAN-owned %d; outside %d'
      % (len(seen), rr, sorted(p for p in extra if any(l.endswith(p) for l in out)), len(hhs), len(bad)))
for l in hhs: print('HELP_HUMAN ' + l)
for l in bad: print('OUTSIDE ' + l)
print('RESULT', 'PASS' if len(seen) == 62 and not bad else 'FAIL')
sys.exit(0 if len(seen) == 62 and not bad else 1)
