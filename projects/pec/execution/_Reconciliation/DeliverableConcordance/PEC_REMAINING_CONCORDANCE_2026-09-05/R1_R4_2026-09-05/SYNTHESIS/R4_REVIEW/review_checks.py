from pathlib import Path
import json,csv,hashlib,subprocess,re,collections,io
ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip()); B=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05'); S=B/'SYNTHESIS'; O=S/'R4_REVIEW'; A=S/'APPLICATION_PREPARATION/FULL_01'; F=S/'FULL_02'
reads={}; checks=[]; errors=[]
def read(p):
 p=Path(p); raw=p.read_bytes();reads[str(p)]=hashlib.sha256(raw).hexdigest();return raw
def j(p):return json.loads(read(p))
def rows(p):return list(csv.DictReader(io.StringIO(read(p).decode())))
def check(ok,name,detail=None):
 checks.append({'check':name,'pass':bool(ok),'detail':detail})
 if not ok:errors.append(checks[-1])
def sha(p):read(p);return reads[str(p)]
pins={str(F/'OUTPUT_MANIFEST.json'):'0062cc22f1a234444f9438d49c0f470448cdaa60fa2922eac670960c2beea92d',str(A/'OUTPUT_MANIFEST.json'):'26fe5361866e8a600af90f1d5048d689d1c8f754c2adf1ae336aa12a4c0880bd',str(S/'AGGREGATE_ADDITIVE/FINAL_STRUCTURAL_ACCOUNTING/OUTPUT_MANIFEST.json'):'c378d3b9dd643539bb4ed1753219e85a9c9f5abb17613d4db8e3d449a92c0bfb'}
for p,h in pins.items():check(sha(p)==h,'selected manifest pin',p)
for folder in [F,A,S/'SCANNER',S/'AGGREGATE_ADDITIVE/FINAL_STRUCTURAL_ACCOUNTING']:
 m=j(folder/'OUTPUT_MANIFEST.json'); h=m.get('hashes',{})
 check(bool(h),'manifest has hashes',str(folder))
 for p,v in h.items():check(sha(p)==v,'manifest member',p)
for p in [Path('AGENTS.md'),Path('projects/pec/AGENTS.md'),Path('agents/AGENT_RECONCILIATION.md'),Path('docs/DELIVERABLE_CONCORDANCE_METHOD.md'),B.parent/'CONVENTIONS.md',*list((B/'COMMON').glob('*.md')),*list((B/'COMMON/BRIEFS').glob('*SYNTHESIS*')),*list(S.glob('PHASED*.md')),*list(S.glob('PUBLICATION*.md')),*list(Path('projects/pec/execution/_Coordination/_DECISIONS').glob('D-PEC-81*.md')),*list(Path('projects/pec/execution/_Coordination/_DECISIONS').glob('D-PEC-82*.md')),S/'BRIEFS/FINAL_R4_REVIEW.md'] :read(p)
check(sha(B.parent/'CONVENTIONS.md')=='e7095343267c04b814410f7fb55a58d25088283d46c3c26e161737e2fc609097','accepted conventions pin')
c=rows(F/'CONSOLIDATED_CLAIMS.csv');r=rows(F/'CONSOLIDATED_RESIDUALS.csv');d=rows(F/'DELIVERABLE_CENSUS.csv');items=rows(A/'PROPOSED_ITEMS.csv');car=rows(A/'CARRIER_DISPOSITIONS.csv');mapping=j(A/'CLAIM_TO_PROPOSAL_MAP.json');app=j(A/'APPLICATION_MANIFEST.json');rb=j(A/'ROLLBACK_MANIFEST.json')
check((len(c),len(r),len(d),len(items),len(car),len(app['entries']))==(2604,165,64,92,64,58),'population counts')
check(len({x['ClaimID'] for x in c})==2604,'unique claims');check(len({x['ResidualID'] for x in r})==165,'unique residuals')
ci={x['ClaimID']:x for x in c};ri={x['ResidualID']:x for x in r};ii={x['ResidualID']:x for x in items}; di={x['DeliverableID']:x for x in d}
for x in d:
 dc=[a for a in c if a['DeliverableID']==x['DeliverableID']];dr=[a for a in r if a['DeliverableID']==x['DeliverableID']];ct=collections.Counter(a['Disposition'] for a in dc)
 check(len(dc)==int(x['ClaimCount']) and len(dr)==int(x['RawResidualCount']) and ct==json.loads(x['DispositionCounts']) and ct['UNKNOWN']==int(x['UnknownClaimCount']),'carrier claim/residual census',x['DeliverableID'])
 if ct['UNKNOWN']:check(x['Assessment']=='ASSESSED_UNKNOWN' and x['WarrantedNONE']=='NO','unknown prevents NONE',x['DeliverableID'])
 for key in ['SelectedClaims','SelectedResiduals']:check(sha(x[key])==x[key+'SHA256'],'selected package CSV pin',x[key])
check([x['DeliverableID'] for x in d if x['WarrantedNONE'].startswith('YES')]==['DEL-10-01'],'sole bounded NONE')
for x in mapping:
 rid=x['ResidualID'];orig=x['OriginalResidual'];check(orig==ri[rid],'raw residual exact equality',rid)
 ids=[i.strip() for i in orig['ClaimIDs'].split(';')];check(collections.Counter(ids)==collections.Counter(y['ClaimID'] for y in x['OriginalLinkedClaims']),'many-to-many linkage',rid)
 for y in x['OriginalLinkedClaims']:check(y==ci[y['ClaimID']],'linked source row exact equality',y['ClaimID'])
 if x['ProposedItem']:
  check(x['ProposedItem']==ii[rid] and [i.strip() for i in ii[rid]['ClaimIDs'].split(';')]==ids,'proposed item linkage',rid)
  if ii[rid]['Route']=='EVIDENCE':check(ii[rid]['Depends']=='NONE' and 'read-only inquiry' in ii[rid]['ProposedText'] and 'separate ruling' in ii[rid]['ProposedText'] and x['ProductionBoundary']['original_depends']==orig['Depends'],'explicit evidence narrowing retains production targets',rid)
 else:check(x['ProposedRoute'] in ['HELD','CONDITIONAL'] and rid not in ii,'held remains outside Remaining',rid)
check(len(mapping)==165 and {x['ResidualID'] for x in mapping}==set(ri),'all raw routes represented')
check(collections.Counter(x['Route'] for x in items)=={'EVIDENCE':78,'PRODUCT_OBLIGATION':6,'DOCUMENTARY':6,'CONFIRMED_SCANNER_REPAIR':2},'proposed class count')
preflights=[];register=Path('projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv');read(register);read('projects/pec/execution/_Scripts/pec_reliance_hold.py')
for x in car:
 target=x['CarrierPath'];cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register',str(register),'--target',target.removeprefix('projects/pec/'),'--operation','consume'];p=subprocess.run(cmd,text=True,capture_output=True);preflights.append({'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr});check(p.returncode==0,'exact hold preflight',target)
 check(sha(target)==x['PreimageSHA256']==sha(x['PreimageCopy']),'all64 current carrier/preimage equality',target)
 check(int(x['ProposedItemCount'])==sum(y['DeliverableID']==x['DeliverableID'] for y in items),'carrier item count',x['DeliverableID'])
for x in app['entries']:
 pre=read(x['PreimageCopy']);post=read(x['CandidateCopy']);target=read(x['TargetPath']);rid=x['DeliverableID'];inverse=next(t for t in rb['entries'] if t['DeliverableID']==rid)
 check(pre==target and sha(x['CandidateCopy'])==x['ProposedPostimageSHA256'] and sha(x['PreimageCopy'])==x['CurrentPreimageSHA256'],'apply source bindings',rid)
 check(post.startswith(pre),'append-only exact preimage preserved',rid)
 added=post[len(pre):];check(len(added)==x['ExpectedAppendBytes'] and post[:-len(added)]==pre and pre+added==post,'independent apply/inverse simulation',rid)
 check(inverse['TargetPath']==x['TargetPath'] and inverse['ExpectedAppliedPostimageSHA256']==sha(x['CandidateCopy']) and inverse['RestorePreimageSHA256']==sha(x['PreimageCopy']),'inverse binding',rid)
 check(b'## Remaining' in pre or b'## Remaining' in added,'Remaining append locus',rid)
 check(not re.search(rb'^## (?!Remaining)',added,re.M),'no new non-Remaining section',rid)
 for item in [y for y in items if y['DeliverableID']==rid]:check(all(t.encode() in added for t in [item['ResidualID'],item['ProposedText'],item['ItemGate'],'Depends: '+item['Depends']]),'exact item bytes in carrier',item['ResidualID'])
 if rid=='DEL-01-05':check(x['FrozenRebindRequired'] and x['PreparationState']=='CONDITIONAL_FROZEN_PREVIEW','frozen rebind hold')
for x in j(S/'SCANNER/TARGETS.json')['targets']:
 check(sha(x['path'])==x['preimage_sha256'],'scanner preimage',x['path']);cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register',str(register),'--target',x['path'].removeprefix('projects/pec/'),'--operation','consume'];p=subprocess.run(cmd,text=True,capture_output=True);preflights.append({'command':cmd,'exit_code':p.returncode,'stdout':p.stdout});check(p.returncode==0,'scanner exact hold preflight',x['path'])
for p in [F/'READ_MANIFEST.json',A/'READ_MANIFEST.json',S/'SCANNER/READ_MANIFEST.json']:
 v=j(p)
 for t,h in v.get('hashes',{}).items():check(sha(t)==h,'current read manifest hash',t)
for p in list(F.glob('*.md'))+list((F/'R4_DECISION_PACKETS').glob('*.md'))+list((S/'SCANNER').glob('*.md'))+list(A.glob('*.md')):read(p)
# Every original cross-package finding must remain mapped by identity.
xc=rows(F/'CROSS_PACKAGE_INPUTS.csv');xm=rows(F/'CROSS_PACKAGE_FINDINGS.csv');check({x['FindingID'] for x in xc}=={i.strip() for x in xm for i in x['SourceFindingIDs'].split(';')},'all cross-package finding IDs mapped');
for x in xc:check(sha(x['SourcePath'])==x['SourceSHA256'],'cross-package source hash',x['FindingID'])
deps=rows(F/'DEPENDENCY_ROWS.csv'); actual=[]
for carrier in car:
 dp=str(Path(carrier['CarrierPath']).with_name('Dependencies.csv'))
 cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register',str(register),'--target',dp.removeprefix('projects/pec/'),'--operation','consume'];pr=subprocess.run(cmd,text=True,capture_output=True);preflights.append({'command':cmd,'exit_code':pr.returncode,'stdout':pr.stdout});check(pr.returncode==0,'dependency exact preflight',dp)
 for row in rows(dp):
  if row['Status']=='ACTIVE' and row['DependencyType']=='PREREQUISITE' and row['TargetType']=='DELIVERABLE':actual.append({'SourcePath':dp,'SourceSHA256':sha(dp),**row})
check(len(actual)==119 and collections.Counter(json.dumps(x,sort_keys=True) for x in actual)==collections.Counter(json.dumps(x,sort_keys=True) for x in deps),'119 exact active prerequisite source rows')
graph=collections.defaultdict(set)
for row in deps:graph[row['FromDeliverableID']].add(row['TargetDeliverableID'])
def cyclic(v,trail):
 if v in trail:return True
 return any(cyclic(w,trail|{v}) for w in graph.get(v,()))
check(not any(cyclic(v,set()) for v in graph),'no cycles in exact active prerequisite graph; excludes separate C01/C02 questions')
for rid in ['DEL-00-02-REM-001','DEL-05-01-REM-001']:
 x=next(y for y in mapping if y['ResidualID']==rid);check(x['ProductionBoundary']['original_depends'] not in ('','NONE'),'risk original production prerequisites retained',rid)
# Preserve every consumed byte identity, including authority and independently inspected current targets.
(O/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':'2be412ccea62bdc4bd96deb082c46d7a792076ea','hashes':reads,'historical_sources':[],'source_unchanged':True,'note':'Hash inspection of complete aggregate surfaces; no duplication of package semantic/test suites.'},indent=2)+'\n')
(O/'CHECK_RESULTS.json').write_text(json.dumps({'checks':checks,'errors':errors,'preflights':preflights,'pins':pins},indent=2)+'\n')
print(json.dumps({'checks':len(checks),'errors':errors,'read_files':len(reads),'routes':dict(collections.Counter(x['ProposedRoute'] for x in mapping))},indent=2))
