"""T6 run-wide call (e): DEL-02-01 half A / half B split remaps. Values decided by the T6 examiner."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_scripts'))
from r3lib import write_csv, read_csv
P = 'DEL-02-01#'
EV_RET = ('projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md:94-108 '
          '(current UI remains a compatibility surface until separately retired; old-UI retirement needs separate owner acceptance); '
          'projects/chirality-app-dev/docs/PRD.md:591,602 (FR-001, FR-007 legacy 3x4 matrix remains compatible); '
          'projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:171,175 (SOW-001, SOW-005); '
          'no App register row rules the 9b005c23a retirement')
EV_CODE = ('projects/chirality-app-dev/frontend/src/components/woven-dialogue/woven-dialogue-route.tsx:16-18 (void legacy; git show 9b005c23a removed the ?legacy=1 and non-dialogue legacy render); '
           'projects/chirality-app-dev/frontend/src/components/portal/agent-matrix.tsx:38-59 (role directory, no grid)')
EV = EV_RET + '; ' + EV_CODE
EV_Q3 = ('projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md:48 (Q3); '
         'git show 03e61f38f woven-dialogue-route.tsx (non-dialogue routes render the legacy element) then git show 9b005c23a (legacy element voided)')
rows = []
def add(k, f, v, ev): rows.append({'ClaimKey': P + k, 'Field': f, 'NewValue': v, 'Call': 'e', 'Evidence': ev})

for k, disp, hdn in [('CLM-017', 'IMPLEMENTED_DIFFERENTLY', None),
                     ('CLM-025', 'IMPLEMENTED_DIFFERENTLY', None),
                     ('CLM-020.3', 'IMPLEMENTED_DIFFERENTLY', '-NO +R4-Q4'),
                     ('CLM-020.4', 'DOCUMENTED_UNIMPLEMENTED', '-NO +R4-Q4'),
                     ('CLM-020.5', 'DOCUMENTED_UNIMPLEMENTED', '-NO +R4-Q4')]:
    add(k, 'Disposition', disp, EV)
    add(k, 'CauseTag', 'OTHER:V3_ROLE_ADOPTION', EV_CODE)
    if hdn: add(k, 'HDN_TOKENS', hdn, EV_RET)
    add(k, 'Notes+', 'R3_SPLIT(e): half B read ACCEPTED_DIVERGENCE. No GOVERNING ruling permits removing the legacy '
        'matrix/loop-first compatibility surface; D-APP-74 requires separate owner acceptance for old-UI retirement. '
        'R3 aligns with half A (CLM-010.1, CLM-010.4-010.6). Primary cause now OTHER:V3_ROLE_ADOPTION; the older '
        'CAUSE2 token in this cell is superseded (secondary: SHELL_REDESIGN).', EV)

add('CLM-020.8', 'Notes+', 'R3_SPLIT(e): half A read IMPLEMENTED_DIFFERENTLY (CLM-010.10, LOW). Both readings defensible: '
    'SCA-APP-010 retired Pipeline presentation from the active shell, but /pipeline rendered it until 9b005c23a. Disposition kept.', EV_Q3)
add('CLM-010.10', 'Notes+', 'R3_SPLIT(e): half B read ACCEPTED_DIVERGENCE (CLM-020.8). Both readings defensible: '
    'SCA-APP-010 retired Pipeline presentation from the active shell, but /pipeline rendered it until 9b005c23a. Disposition kept.', EV_Q3)
for k in ['CLM-010.2', 'CLM-020.1', 'CLM-029.3']:
    add(k, 'Notes+', 'R3_RUNWIDE(e): other reading IMPLEMENTED_DIFFERENTLY with R4-Q4. Q3 was implemented by 03e61f38f as '
        'the URL rendering the retired legacy surface; 9b005c23a made the URL render the Dialogue only. Q3 wording '
        '(reachable by URL, no 404, unmounted) still holds literally, so ACCEPTED_DIVERGENCE kept; halves agree.', EV_Q3)
add('CLM-021', 'HDN_TOKENS', '-NO +R4-Q4', EV_CODE)
add('CLM-021', 'Notes+', 'R3_RUNWIDE(e): the matrix-test evidence values went stale through 9b005c23a; the repair direction '
    '(restore the matrix or rewrite the text) turns on R4-Q4, as on CLM-012.2-012.5 (half A).', EV_CODE)

out = os.path.join(os.path.dirname(__file__), '..', 'T6_REMAPS.csv')
write_csv(out, ['ClaimKey', 'Field', 'NewValue', 'Call', 'Evidence'], rows)
h, back = read_csv(out)
print(len(back), 'rows')
