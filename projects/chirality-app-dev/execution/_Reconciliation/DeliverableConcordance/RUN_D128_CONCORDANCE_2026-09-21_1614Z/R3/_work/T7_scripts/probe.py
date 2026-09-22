import sys,collections,re,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','..','_scripts'))
from r3lib import read_csv, hdn_tokens
_,C=read_csv('R3/CLAIM_CONCORDANCE.csv'); _,E=read_csv('R3/EXTENSION_CONCORDANCE.csv')
A=C+E
F=['ClaimType','NormativeSource','DeclaredState','LatestDecision','ImplementationEvidence','VerificationEvidence','DirectionEvidence','Notes','RemainingWork','RecordedRemaining','RemainingGate','CauseTag','HumanDecisionNeeded','AltReading']
def txt(r): return '\n'.join(r[f] for f in F)
for pat in sys.argv[1:]:
    rx=re.compile(pat, re.I)
    hits=[r for r in A if rx.search(txt(r))]
    print(f'== {pat}: {len(hits)}', dict(collections.Counter(r['PackageID'] for r in hits)))
    print('   disp', dict(collections.Counter(r['Disposition'] for r in hits)))
    if len(hits)<=25: print('  ', ' '.join(r['ClaimKey'] for r in hits))
