import re, glob, os
from collections import Counter
from rvlib import RUN, load
_,sq=load('R4/PACKET_SUBQUESTIONS.csv'); _,pi=load('R4/PACKET_INDEX.csv')
C=Counter((r['PacketID'],r['SubQ']) for r in sq)
P=Counter((r['PacketID'],r['Role']) for r in pi)
for f in sorted(glob.glob(os.path.join(RUN,'R4/PACKETS/*.md'))):
    t=open(f).read(); pid=re.search(r'id: (\S+)',t).group(1)
    for s,n in re.findall(r'- P-[0-9EX]+\.([a-e]): (\d+) rows',t):
        if C[(pid,s)]!=int(n): print('SUBQ MISMATCH',pid,s,n,C[(pid,s)])
    # prose mentions like **P-09.a** (161 rows)
    for s,n in re.findall(r'\*\*P-[0-9EX]+\.([a-e])\*\*[^\n(]*\((\d+) rows?',t):
        if C[(pid,s)]!=int(n): print('PROSE SUBQ MISMATCH',pid,s,n,C[(pid,s)])
    for s,n in re.findall(r'P-[0-9EX]+\.([a-e])\*\* — [^\n]*?\((\d+) rows?',t):
        if C[(pid,s)]!=int(n): print('PROSE2',pid,s,n,C[(pid,s)])
    m=re.search(r'\*\*(\d+) rows are decided in this packet\*\* \(PRIMARY\); (\d+) more',t)
    if m and (int(m.group(1))!=P[(pid,'PRIMARY')] or int(m.group(2))!=P[(pid,'ALSO')]+P[(pid,'CONTEXT')]): print('COUNT',pid,m.groups())
    subs=sorted(set(s for (p,s) in C if p==pid)); print(pid,'csv subq',subs)
