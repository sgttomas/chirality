import sys
from rvlib import load
_,c=load('R3/CLAIM_CONCORDANCE.csv'); _,e=load('R3/EXTENSION_CONCORDANCE.csv')
idx={r['ClaimKey']:r for r in c+e}
fields=['Disposition','CauseTag','HumanDecisionNeeded','LatestDecision','SealedDisposition','ImplementationEvidence','Notes','AltReading']
for k in sys.argv[1:]:
    r=idx.get(k); print('==',k)
    if not r: print('MISSING'); continue
    for f in fields: print(' ',f,':',r[f][:400])
