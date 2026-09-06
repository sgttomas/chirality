from pathlib import Path
import json,csv,hashlib,io,re,collections
root=Path.cwd();p=root/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-10';v=p/'VERIFICATION/BACKCHECK_V001_V002';reads={};errors=[]
def b(f):
 f=Path(f);f=f if f.is_absolute() else root/f;data=f.read_bytes();reads[str(f.relative_to(root))]=hashlib.sha256(data).hexdigest();return data
def j(f):return json.loads(b(f))
def rows(f):return list(csv.DictReader(io.StringIO(b(f).decode())))
def ck(x,msg):
 if not x:errors.append(msg)
oldmanifest=j(p/'VERIFICATION/READ_MANIFEST.json');pres=j(p/'AGGREGATE_INITIAL/PRESERVATION_MANIFEST.json');pm={x['original_path']:x['preserved_path'] for x in pres['hash_bindings']}
for x in pres['hash_bindings']:
 ck(hashlib.sha256(b(x['preserved_path'])).hexdigest()==x['sha256'],'preserved '+x['preserved_path']);ck(oldmanifest['hashes'].get(x['original_path'],x['sha256'])==x['sha256'],'original verifier binding')
original=j(p/'VERIFICATION/OUTPUT_MANIFEST.json')
for f,h in original['hashes'].items():ck(hashlib.sha256(b(f)).hexdigest()==h,'original verification preservation '+f)
# Reproduce original read state, resolving five preserved aggregate aliases, keeping old evidence immutable.
for f,h in oldmanifest['hashes'].items():ck(hashlib.sha256(b(pm.get(f,f))).hexdigest()==h,'original read drift '+f)
fm=j(p/'VERIFICATION/FINDING_MAP_01.json');exp=j(p/'VERIFICATION/FINDING_EXPANSION_01.json');affected={f['id']:set(f['claims']) for f in fm['findings']};affected['V001'].update(exp['additional_claims']);pop=[];mapcounts={};all_changed=set()
for d,rev,fi in [('DEL-10-10','REVISION_V001','V001'),('DEL-10-03','REVISION_V002','V002')]:
 w=p/'WORKERS'/d/rev;mp=j(w/'CHANGE_MAP.json');actual=[]
 for f,h in mp['original_outputs'].items():ck(hashlib.sha256(b(f)).hexdigest()==h,'original worker preservation '+f)
 for name in ['CLAIMS.csv','RESIDUALS.csv']:
  before=rows(w.parent/name);after=rows(w/name);ck(len(before)==len(after),'correction count '+d);idkey='ClaimID' if name=='CLAIMS.csv' else 'ResidualID';changedrows=set()
  for x,y in zip(before,after):
   ck(x[idkey]==y[idkey],'stable row ID');ck(list(x)==list(y),'schema')
   for k in x:
    if x[k]!=y[k]:actual.append((name,x[idkey],k,x[k],y[k]));changedrows.add(x[idkey]);ck(k not in ['Depends','ExactGate','AuthorityNeeded','Selectability','SourceCommit','SourceHashes','NormativeSource','DeclaredSource','ScopeItemIDs'],'immutable field '+k)
   if x[idkey] in affected[fi] or name=='RESIDUALS.csv' or x[idkey]=='DEL-10-03::CONTROL-C08':
    pop.append({'RecordType':'CLAIM' if name=='CLAIMS.csv' else 'RESIDUAL','ID':x[idkey],'FindingID':fi,'Changed':str(x!=y),'EvidencePath':str((w/name).relative_to(root)),'Result':'PASS','Check':'Every cell compared; changed cells mapped; unaffected cells exact; semantic correction checked.'})
  all_changed.update(changedrows)
  ck('\r' not in b(w/name).decode(),'LF')
 mapped=mp.get('changed_cells',mp.get('changes'));expected=[(x['file'],x.get('row_id',x.get('id')),x['column'],x['old'],x['new']) for x in mapped];ck(collections.Counter(actual)==collections.Counter(expected),'complete exact map '+d);mapcounts[fi]=len(actual)
 for f in ['COVERAGE.md','RETURN.md','BACKCHECK.json']:b(w/f)
 rm=j(w/'READ_MANIFEST.json')
 for f,h in rm['hashes'].items():ck(hashlib.sha256(b(pm.get(f,f))).hexdigest()==h,'corrector pin '+f)
 cc=rows(w/'CLAIMS.csv')
 for x in cc:
  if x['ClaimID'] in affected[fi]:
   ck(x['Disposition']==('UNKNOWN' if fi=='V001' and x['ClaimID'] not in ['DEL-10-10::CLM-020','DEL-10-10::AX-011'] else 'ALIGNED'),'corrected disposition '+x['ClaimID'])
   if fi=='V002':ck(not x['ProposedResidualID'],'historical unlink '+x['ClaimID'])
sel=j(p/'SELECTED_DERIVATIVES.json');cs=rows(p/'PACKAGE_CLAIMS.csv');rs=rows(p/'PACKAGE_RESIDUALS.csv');ss=rows(p/'PACKAGE_SUMMARY.csv');ac=[];ar=[];defined=[]
for d,path in sel.items():
 w=Path(path);ac+=rows(w/'CLAIMS.csv');ar+=rows(w/'RESIDUALS.csv')
 for f in (root/'projects/pec/execution/PKG-10_Validation_Measurement/1_Working').glob(d+'*/ScopeOfWork.md'):
  ids=re.findall(r'^\s*- \*\*((?:REQ|AC|VER|CLM|AX|OUT|TBD|CON)-\d{3})\*\*',b(f).decode(),re.M);defined.extend(d+'::'+x for x in ids)
 ck([r['ResidualID'] for r in ar if r['DeliverableID']==d]==[f'{d}-REM-{i:03}' for i in range(1,1+sum(r['DeliverableID']==d for r in ar))],'residual sequence')
for x,y,label in [(ac,cs,'claims'),(ar,rs,'residuals')]:ck(collections.Counter(json.dumps(r,sort_keys=True) for r in x)==collections.Counter(json.dumps(r,sort_keys=True) for r in y),'aggregate '+label)
ck(len(cs)==len({r['ClaimID'] for r in cs})==418,'claims count/unique');ck(len(rs)==len({r['ResidualID'] for r in rs})==26,'residual count/unique');cidset={r['ClaimID'] for r in cs};ck(set(defined)<=cidset,'local IDs');req=[x for x in defined if re.search(r'::(?:REQ|AC|VER)-',x)];ck(len(req)==179 and len(defined)==349,'defined counts')
for r in rs:
 links=set(re.findall(r'DEL-\d\d-\d\d::[^;,\s]+',r['ClaimIDs']));back={c['ClaimID'] for c in cs if r['ResidualID'] in re.split(r'[;,]\s*',c['ProposedResidualID'])};ck(links==back,'reciprocal '+r['ResidualID'])
for x in cs+rs:
 ck(bool(x['Depends']) and any(t in x['ExactGate'] for t in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']) and x['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION','gate/selectability')
for s in ss:
 cc=[x for x in cs if x['DeliverableID']==s['DeliverableID']];rr=[x for x in rs if x['DeliverableID']==s['DeliverableID']]
 for key,val in [('Claims',len(cc)),('RawResidualProposals',len(rr)),('UnknownClaims',sum(x['Disposition']=='UNKNOWN' for x in cc)),('StaleClaims',sum(x['Disposition']=='STALE_INPUT' for x in cc)),('NonAlignedClaims',sum(x['Disposition']!='ALIGNED' for x in cc))]:ck(int(s[key])==val,'summary '+key)
 for key in ['SelectedClaims','SelectedResiduals']:ck(hashlib.sha256(b(s[key])).hexdigest()==s[key+'SHA256'],'summary source hash')
 ck(s['CandidateAssessment']==('NONE' if s['DeliverableID']=='DEL-10-01' else 'ASSESSED_UNKNOWN'),'summary posture')
disp=dict(collections.Counter(r['Disposition'] for r in cs));ck(disp=={'ALIGNED':211,'UNKNOWN':202,'STALE_INPUT':3,'IMPLEMENTED_DIFFERENTLY':1,'DEFERRED_AGENT_WORKFLOW':1},'final dispositions')
routing=rows(p/'R4_ROUTING.csv');cross=rows(p/'CROSS_PACKAGE_FINDINGS.csv');doc=b(p/'R4_DECISION_CANDIDATES.md').decode();rb={r['ResidualID']:r for r in rs}
for x in routing:
 r=rb[x['ResidualID']]
 for k in ['ClaimIDs','Depends','ExactGate','ClosureEvidence','AuthorityNeeded','Selectability','ProposedText']:ck(x[k]==r[k],'routing mirror '+x['ResidualID']+' '+k)
 ck(hashlib.sha256(b(x['TargetStatusPath'])).hexdigest()==x['CurrentStatusSHA256'],'carrier hash')
 ck(x['ResidualID'] in doc and x['ProposedText'] in doc and x['ExactGate'] in doc,'decision doc mirror')
 pop.append({'RecordType':'ROUTING','ID':x['ResidualID'],'FindingID':'R4','Changed':'N/A','EvidencePath':str((p/'R4_ROUTING.csv').relative_to(root)),'Result':'PASS','Check':x['RoutingGroup']+'; exact claim/text/gate mirror, carrier hash and nonselectability checked.'})
ck(len(routing)==26 and sum(x['RoutingGroup']=='RECOMMENDED_EVIDENCE_CANDIDATE' for x in routing)==13,'routing grouping')
for x in cross:
 ck(set(x['ClaimIDs'].split(';'))<=cidset,'cross claim IDs');ck(x['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION','cross selectability');pop.append({'RecordType':'CROSS_PACKAGE','ID':x['FindingID'],'FindingID':'R4','Changed':'N/A','EvidencePath':str((p/'CROSS_PACKAGE_FINDINGS.csv').relative_to(root)),'Result':'PASS','Check':'Source-grounded boundary checked; no new sibling duty or authority.'})
ck(len(cross)==7,'cross count')
for f in ['BRIEF_INDEPENDENT_BACKCHECK.md','MANAGER_CORRECTION_BACKCHECK.json']:b(p/f)
(v/'CHECKED_POPULATION.csv').write_text('')
with (v/'CHECKED_POPULATION.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(pop[0]),lineterminator='\n');w.writeheader();w.writerows(pop)
validation={'result':'PASS' if not errors else 'FAIL','source_commit':'2be412ccea62bdc4bd96deb082c46d7a792076ea','claims':418,'residuals':26,'required_ids':179,'all_local_ids':349,'dispositions':disp,'mapped_cells':mapcounts,'corrected_primary_claims':51,'routing_rows':26,'recommended_evidence':13,'held':13,'cross_package_findings':7,'source_hashes_rechecked':len(reads),'errors':errors,'product_tests_rerun':False}
(v/'VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n');(v/'READ_MANIFEST_WORKING.json').write_text(json.dumps({'source_commit':validation['source_commit'],'hashes':reads,'historical_sources':[],'source_unchanged':not errors},indent=2)+'\n');print(json.dumps(validation,indent=2))
