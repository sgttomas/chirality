import csv, re, collections
R='projects/pec/'
led=list(csv.DictReader(open(R+'execution/_Decomposition/ScopeLedger.csv')))
c=collections.Counter(r['InOutStatus'] for r in led)
print('ScopeLedger rows',len(led),dict(c))
ids=[r['ScopeItemID'] for r in led]
print('ScopeItem ID range',ids[0],'..',ids[-1],'unique',len(set(ids)))
for s in ['SOW-029','SOW-035','SOW-037','SOW-087','SOW-077','SOW-089','SOW-095','SOW-096','SOW-097','SOW-098','SOW-099','SOW-100','SOW-065','SOW-069','SOW-084','SOW-085','SOW-093','SOW-064','SOW-025','SOW-055','SOW-058','SOW-003']:
    r=[x for x in led if x['ScopeItemID']==s]
    print(s, r[0]['InOutStatus'], r[0]['PackageID'], r[0]['DeliverableIDs'], r[0]['SourceRef'], '|', r[0]['ScopeItemStatement'][:110]) if r else print(s,'MISSING')
print('TBD items',[r['ScopeItemID'] for r in led if r['InOutStatus']=='TBD'])
print('OUT items',[r['ScopeItemID'] for r in led if r['InOutStatus']=='OUT'])
dl=list(csv.DictReader(open(R+'execution/_Decomposition/Deliverables.csv')))
print('Deliverables rows',len(dl))
pk=collections.OrderedDict()
for r in dl: pk.setdefault(r['PackageID'],[]).append(r['DeliverableID'])
for k,v in pk.items(): print(k,len(v),v[0],'..',v[-1])
ret=[r['DeliverableID'] for r in dl if 'retire' in (r['Name']+r['Description']+r['PhaseHint']+r['Type']+r['ContextEnvelopeNotes']).lower()]
print('rows mentioning retire:',ret)
for r in dl:
    if r['DeliverableID'] in ('DEL-06-04','DEL-07-02','DEL-07-04','DEL-07-05','DEL-00-03'):
        print(r['DeliverableID'],'|',r['Name'],'|',r['Type'],'|',r['PhaseHint'],'|',r['CoversScopeItems'],'|',r['Description'][:160],'|',r['ContextEnvelopeNotes'][:120])
# scope item ranges cited in SPEC table
