import sys
from collections import Counter
from rvlib import load
_,c=load('R3/CLAIM_CONCORDANCE.csv'); _,e=load('R3/EXTENSION_CONCORDANCE.csv')
idx={r['ClaimKey']:r for r in c+e}
_,pi=load('R4/PACKET_INDEX.csv'); _,sq=load('R4/PACKET_SUBQUESTIONS.csv')
p=sys.argv[1]; field=sys.argv[2] if len(sys.argv)>2 else 'Disposition'
ks=[r['ClaimKey'] for r in pi if r['PacketID']==p and r['Role']=='PRIMARY']
print(Counter(idx[k][field] for k in ks).most_common(20))
sub={}
for r in sq:
  if r['PacketID']==p: sub.setdefault(r['SubQ'],[]).append(r['ClaimKey'])
for s,v in sorted(sub.items()): print(s,len(v),Counter(idx[k][field] for k in v).most_common(8))
