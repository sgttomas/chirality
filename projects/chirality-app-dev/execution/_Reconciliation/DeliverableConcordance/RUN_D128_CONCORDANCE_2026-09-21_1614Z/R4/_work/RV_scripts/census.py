from collections import Counter, defaultdict
from rvlib import load
_,c=load('R3/CLAIM_CONCORDANCE.csv'); _,e=load('R3/EXTENSION_CONCORDANCE.csv')
rows=c+e
d=Counter(r['Disposition'] for r in rows); print(len(rows)); print(d)
g={'ALIGNED':'match','NOT_AUDITABLE':'match','STALE_SPECIFICATION':'stale','PARTIALLY_IMPLEMENTED':'partial','IMPLEMENTED_DIFFERENTLY':'partial','DOCUMENTED_UNIMPLEMENTED':'partial','AUTHORITY_CONFLICT':'conflict','REMAINING_STATE_MISMATCH':'todo','RETIRED_BY_RULING':'retired','ACCEPTED_DIVERGENCE':'retired','UNKNOWN':'unknown'}
G=Counter(g.get(k,'other') for k in (r['Disposition'] for r in rows)); print(G)
h=[r for r in rows if r['HumanDecisionNeeded'] not in ('','NO')]; print('HDN non-NO',len(h))
q=Counter();
for r in h:
  for t in r['HumanDecisionNeeded'].split(';'):
    q[t.strip()]+=1
print(q.most_common(40))
_,pi=load('R4/PACKET_INDEX.csv')
pc=defaultdict(Counter)
for r in pi: pc[r['PacketID']][r['Role']]+=1
for k in sorted(pc): print(k, dict(pc[k]))
_,sq=load('R4/PACKET_SUBQUESTIONS.csv')
sc=defaultdict(Counter)
for r in sq: sc[r['PacketID']][r['SubQ']]+=1
for k in sorted(sc): print(k, dict(sc[k]))
keys=set(r['ClaimKey'] for r in rows)
prim=Counter(r['ClaimKey'] for r in pi if r['Role']=='PRIMARY')
print('primary dup',[k for k,v in prim.items() if v>1][:5],'missing',len(keys-set(prim)),'extra',len(set(prim)-keys))
