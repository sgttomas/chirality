import csv, re, collections
R='projects/pec/'
spec=open(R+'execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md').read()
prd=open(R+'docs/PRD.md').read()
led={r['ScopeItemID']:r for r in csv.DictReader(open(R+'execution/_Decomposition/ScopeLedger.csv'))}
dl={r['DeliverableID']:r for r in csv.DictReader(open(R+'execution/_Decomposition/Deliverables.csv'))}
# PRD requirement rows: lines starting with | PEC-XXX-NNN
req=collections.OrderedDict()
for m in re.finditer(r'^\|\s*\**`?(PEC-(ORI|RCN|GAT|PRS|STR|API|DSH|SVC)-\d{3})`?\**\s*\|',prd,re.M):
    req.setdefault(m.group(1),0); req[m.group(1)]+=1
fam=collections.Counter(k.split('-')[1] for k in req)
print('PRD requirement row IDs:',len(req),dict(fam))
kinv=sorted(set(re.findall(r'^\|\s*\**`?(PEC-K-\d{2})`?\**\s*\|',prd,re.M)))
print('PRD PEC-K table rows:',len(kinv),kinv)
# Expand ranges in SPEC
def expand(prefix,a,b,width):
    return [f'{prefix}{i:0{width}d}' for i in range(int(a),int(b)+1)]
toks=set()
for m in re.finditer(r'(SOW-)(\d{3})`?\.\.`?(?:SOW-)?(\d{3})',spec): toks.update(expand('SOW-',m.group(2),m.group(3),3))
for m in re.finditer(r'(PEC-[A-Z]{3}-)(\d{3})\.\.(\d{3})',spec): toks.update(expand(m.group(1),m.group(2),m.group(3),3))
for m in re.finditer(r'DEL-(\d\d)-(\d\d)\.\.(\d\d)',spec): toks.update(expand(f'DEL-{m.group(1)}-',m.group(2),m.group(3),2))
toks.update(re.findall(r'\b(?:SOW|OBJ)-\d{3}\b',spec)); toks.update(re.findall(r'\bPKG-\d\d\b',spec)); toks.update(re.findall(r'\bDEL-\d\d-\d\d\b',spec))
toks.update(re.findall(r'\bPEC-(?:ORI|RCN|GAT|PRS|STR|API|DSH|SVC)-\d{3}\b',spec)); toks.update(re.findall(r'\bPEC-K-\d\d\b',spec))
objs={'OBJ-00%d'%i for i in range(1,7)}
pk={'PKG-%02d'%i for i in range(11)}
bad=[]
for t in sorted(toks):
    if t.startswith('SOW-') and t not in led: bad.append(t)
    elif t.startswith('DEL-') and t not in dl: bad.append(t)
    elif t.startswith('OBJ-') and t not in objs: bad.append(t)
    elif t.startswith('PKG-') and t not in pk: bad.append(t)
    elif re.match(r'PEC-[A-Z]{3}-\d{3}',t) and t not in req: bad.append(t)
    elif t.startswith('PEC-K-') and t not in kinv: bad.append(t)
print('SPEC tokens (with ranges expanded):',len(toks),'unresolved:',bad)
print('SPEC SOW tokens:',len([t for t in toks if t.startswith('SOW-')]))
allsow=set(led); missing=sorted(allsow-toks)
print('Ledger items not named in SPEC:',len(missing),missing)
# Family->scope consistency: for each SPEC family row, check ledger SourceRef of named SOW items
rows=re.findall(r'^\| (Orientation|Reconciliation|Gate/slate|Presence|Streams|API|Dashboards|Service) \| (PEC-[A-Z]{3})-(\d{3})\.\.(\d{3}) \|.*\| ([^|]+) \|$',spec,re.M)
for name,pre,a,b,scope in rows:
    s=set()
    for m in re.finditer(r'SOW-(\d{3})(?:\.\.(\d{3}))?',scope):
        s.update(expand('SOW-',m.group(1),m.group(2) or m.group(1),3))
    ids=expand(pre+'-',a,b,3)
    fam=pre.split('-')[1]
    # ledger items whose SourceRef cites this family
    cit=sorted(k for k,r in led.items() if re.search(r'PEC-'+fam+r'-\d{3}',r['SourceRef']))
    print(f'{name}: PRD ids {ids[0]}..{ids[-1]} exist={all(i in req for i in ids)} count_in_PRD={sum(1 for k in req if k.split("-")[1]==fam)}; SPEC scope {len(s)} items; ledger items citing PEC-{fam}: {cit}; in SPEC not citing family: {sorted(x for x in s if x not in cit)}; citing family but not in SPEC: {sorted(x for x in cit if x not in s)}')
