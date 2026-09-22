import re, glob, os
from rvlib import RUN
H={}
for f in sorted(glob.glob(os.path.join(RUN,'R4/PACKETS/*.md'))):
    t=open(f).read(); m=re.search(r'<!-- PACKET\n(.*?)-->',t,re.S)
    d=dict(l.split(': ',1) for l in m.group(1).strip().split('\n'))
    H[d['id']]=d
book=open(os.path.join(RUN,'R4/R4_DECISION_BOOK.md')).read()
for line in book.split('\n'):
    m=re.match(r'\| \[(P-[0-9EX]+)\]\([^)]*\) — (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$',line)
    if not m: continue
    p,title,q,rows,tier,rec,dep=m.groups(); h=H[p]
    for a,b,n in [(title,h['title'],'title'),(q,h['question'],'question'),(tier,h['tier'],'tier'),(rec,h['recommended'],'rec'),(dep,h['depends_on'],'dep')]:
        if a.strip()!=b.strip(): print(p,n,'BOOK=',a,'| HDR=',b)
# ruling order
order={}
steps=re.findall(r'^(\d)\. (.*?)(?=^\d\. |\Z)',book.split('## 3.')[1].split('## 4.')[0],re.S|re.M)
for s,txt in steps:
    for p in re.findall(r'P-\d\d|P-EX',txt.split('feeds')[0] if 'feeds' in txt else txt):
        order.setdefault(p,int(s))
print(order)
for p,h in H.items():
    for d in [x.strip() for x in h['depends_on'].split(',') if x.strip()!='none']:
        if order.get(d,9)>order.get(p,9): print('ORDER',p,'(step',order.get(p),') depends on',d,'(step',order.get(d),')')
