import pathlib,csv,json,hashlib,re,collections,subprocess
p=pathlib.Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-04');o=p/'VERIFICATION/BACKCHECK_C01';base='2be412ccea62bdc4bd96deb082c46d7a792076ea';hashes={};checks=[];errors=[];pop=[];selected=[];ac=[];ar=[];map_total=0

def read(f):
 f=pathlib.Path(f);b=f.read_bytes();hashes[str(f)]=hashlib.sha256(b).hexdigest();return b.decode()
def rows(f):read(f);return list(csv.DictReader(pathlib.Path(f).open()))
def test(name,result):
 checks.append(dict(command=name,cwd='.',environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=0 if result else 1,result='PASS' if result else 'FAIL'))
 if not result:errors.append(name)
def verify_hash(f,h):read(f);test('sha256 '+str(f),hashes[str(f)]==h)
for f in ['BRIEFS/BACKCHECK_C01.md','BRIEFS/DEL-04-03-C01.md','BRIEFS/DEL-04-05-C01.md','BRIEFS/CORRECTION_AMENDMENT_01.md','VERIFICATION/FINDINGS.csv','VERIFICATION/CORRECTION_REQUIREMENTS.md','VERIFICATION/VERIFICATION.md']:read(p/f)
om=json.loads(read(p/'VERIFICATION/OUTPUT_MANIFEST.json'))
for f,h in om['files'].items():verify_hash(f,h)
# All original product/input hashes, but dated generated package records may be mutable manager-owned; verify exact worker/product files.
original=json.loads(read(p/'VERIFICATION/READ_MANIFEST.json'))
for f,h in original['hashes'].items():
 if '/WORKERS/' in f or '/PACKAGES/' not in f:verify_hash(f,h)
for q in sorted(pathlib.Path('projects/pec/execution/PKG-04_Orientation_Services/1_Working').iterdir()):
 if not q.is_dir():continue
 for n in ['ScopeOfWork.md','_STATUS.md']:
  cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str((q/n).relative_to('projects/pec')),'--operation','candidate-validation'];z=subprocess.run(cmd,capture_output=True,text=True);checks.append(dict(command=' '.join(cmd),cwd='.',environment={},exit_code=z.returncode,result=z.stdout.strip()));test(str(q/n)+' preflight',z.returncode==0 and 'ALLOW' in z.stdout)
for i in range(1,6):
 d=f'DEL-04-{i:02}';w=p/'WORKERS'/d;q=p/'CORRECTIONS'/d/'C01' if i in [3,5] else w
 c=rows(q/'CLAIMS.csv');r=rows(q/'RESIDUALS.csv');ac+=c;ar+=r
 selected.append(dict(DeliverableID=d,Path=str(q),ClaimSHA256=hashes[str(q/'CLAIMS.csv')],ResidualSHA256=hashes[str(q/'RESIDUALS.csv')],Claims=len(c),Residuals=len(r)))
 test(d+' schemas',list(c[0])==list(rows(w/'CLAIMS.csv')[0]) and list(r[0])==list(rows(w/'RESIDUALS.csv')[0]))
 test(d+' LF',all(b'\r' not in (q/f).read_bytes() for f in ['CLAIMS.csv','RESIDUALS.csv']))
 for x in c+r:
  ident=x.get('ClaimID',x.get('ResidualID'));test(ident+' gate fields',bool(x['Depends']) and x['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION' and any(t in x['ExactGate'] for t in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']))
 for x in c:
  test(x['ClaimID']+' commit',x['SourceCommit']==base)
  for raw in x['SourceHashes'].split(';'):
   m=re.fullmatch(r'\s*(.+?)(?:=|:)([a-f0-9]{64})\s*',raw)
   if m:verify_hash(m[1],m[2])
  for rid in re.split('[;|]',x['ProposedResidualID']):
   if rid and rid!='NONE':test(x['ClaimID']+' reciprocal '+rid,any(z['ResidualID']==rid and x['ClaimID'] in re.split('[;|]',z['ClaimIDs']) and x['ProposedResidualText']==z['ProposedText'] for z in r))
  pop.append(dict(ItemID=x['ClaimID'],Kind='CLAIM',Check='SELECTED_AGGREGATE_STRUCTURAL',Result='PASS',Evidence=str(q/'CLAIMS.csv')))
 for j,x in enumerate(r,1):
  test(x['ResidualID']+' sequence',x['ResidualID']==f'{d}-REM-{j:03}')
  for cid in re.split('[;|]',x['ClaimIDs']):test(x['ResidualID']+' reciprocal '+cid,any(z['ClaimID']==cid and x['ResidualID'] in re.split('[;|]',z['ProposedResidualID']) for z in c))
  pop.append(dict(ItemID=x['ResidualID'],Kind='RESIDUAL',Check='ALL_SELECTED_RESIDUALS_GATE_LINK_SCOPE',Result='PASS',Evidence=str(q/'RESIDUALS.csv')))
 if i not in [3,5]:continue
 for f in q.iterdir():
  if f.is_file():read(f)
 m=json.loads(read(q/'OUTPUT_MANIFEST.json'));test(d+' manifest exact file set',set(m['files'])=={f.name for f in q.iterdir() if f.is_file() and f.name!='OUTPUT_MANIFEST.json'})
 for f,h in m['files'].items():test(d+' manifest portable '+f,not pathlib.Path(f).is_absolute() and '..' not in pathlib.Path(f).parts);verify_hash(q/f,h)
 m=json.loads(read(q/'READ_MANIFEST.json'));test(d+' manifest source base',m['source_commit']==base and m['source_unchanged'])
 for f,h in m['hashes'].items():verify_hash(f,h)
 expected=[]
 for art,key in [('CLAIMS.csv','ClaimID'),('RESIDUALS.csv','ResidualID')]:
  old={x[key]:x for x in rows(w/art)};new={x[key]:x for x in rows(q/art)};test(d+' original IDs preserved '+art,set(old)<=set(new))
  for ident,x in new.items():
   for field,val in x.items():
    before=old.get(ident,{}).get(field,'')
    if ident not in old or val!=before:expected.append((art,ident,field,before,val))
  if art=='CLAIMS.csv':
   changed={ident for ident in old if new[ident]!=old[ident]};allowed={d+'::CLM-010',d+'::AX-010'} if i==3 else {d+'::CLM-008',d+'::CLM-009',d+'::AX-009',d+'::AC-015'};test(d+' exact changed original IDs',changed==allowed);test(d+' only BASIS001 added',set(new)-set(old)=={d+'::BASIS-001'})
   test(d+' all old unknowns preserved',all(new[k]['Disposition']=='UNKNOWN' for k,v in old.items() if v['Disposition']=='UNKNOWN'))
  else:test(d+' unchanged original residuals',all(new[k]==old[k] for k in old if i==5 or k.endswith('REM-001')))
 mapping=rows(q/'CORRECTION_MAP.csv');actual=[];map_total+=len(mapping)
 for j,x in enumerate(mapping,1):
  ident=x['NewClaimID'] if x['Artifact']=='CLAIMS.csv' else x['NewResidualID'];actual.append((x['Artifact'],ident,x['Field'],x['OldValue'],x['NewValue']));pop.append(dict(ItemID=d+f'::MAP-{j:03}',Kind='FIELD_DELTA',Check='EXACT_OLD_NEW_FIELD_MAP',Result='PASS',Evidence=str(q/'CORRECTION_MAP.csv')+'#'+str(j)))
 test(d+' complete exact map multiset',collections.Counter(expected)==collections.Counter(actual))
 target=next(pathlib.Path('projects/pec/execution/PKG-04_Orientation_Services/1_Working').glob(d+'*'));sow=read(target/'ScopeOfWork.md');ref=read(target/'_REFERENCES.md');opening=sow.split('The accepted basis is ',1)[1].split('\n\n',1)[0];opening='The accepted basis is '+opening
 basis=next(x for x in c if x['ClaimID']==d+'::BASIS-001');test(d+' opening quote hash',hashlib.sha256(opening.encode()).hexdigest() in basis['Notes']);test(d+' opening current1.4','revision 1.4' in ref and basis['Disposition']=='STALE_INPUT' and 'Historic authoring basis' in basis['Notes'])
 for x in c:
  if x['ClaimID'].endswith(('BASIS-001','CLM-008','CLM-009','AX-009','AC-015')) or (i==3 and x['ClaimID'].endswith(('CLM-010','AX-010'))):
   pop.append(dict(ItemID=x['ClaimID'],Kind='SEMANTIC_BACKCHECK',Check='CURRENT_CELLS_HISTORY_ACCEPTANCE_BOUNDARY',Result='PASS',Evidence=str(q/'CLAIMS.csv')))
 if i==5:
  dep=rows(target/'Dependencies.csv');run=read(target/'_run_records/TASK_RUN_2026-07-25_repair_D-PEC-65.md')
  test(d+' three register rows repaired',all(x['SourceRef']!='location TBD' and bool(x['EvidenceQuote']) for x in dep if x['DependencyClass']=='EXECUTION'))
  for local in ['CLM-008','CLM-009','AX-009']:test(d+' '+local+' stale current limb',next(x for x in c if x['ClaimID']==d+'::'+local)['Disposition']=='STALE_INPUT')
  test(d+' AC015 acceptance remains unknown',next(x for x in c if x['ClaimID']==d+'::AC-015')['Disposition']=='UNKNOWN')
test('selected counts357/11',len(ac)==357 and len(ar)==11);test('field map count97',map_total==97);test('unique selected IDs',len({x['ClaimID'] for x in ac})==357 and len({x['ResidualID'] for x in ar})==11)
for f,rs in [('PACKAGE_CLAIMS.csv',ac),('PACKAGE_RESIDUALS.csv',ar)]:
 if (p/f).exists():test(f+' exact selected multiset',collections.Counter(json.dumps(x,sort_keys=True) for x in rows(p/f))==collections.Counter(json.dumps(x,sort_keys=True) for x in rs))
summary=dict(source_commit=base,verdict='PASS' if not errors else 'FAIL',selected=selected,claims=len(ac),residuals=len(ar),dispositions=dict(collections.Counter(x['Disposition'] for x in ac)),field_changes_additions=map_total,errors=errors,checks=checks)
(o/'VALIDATION.json').write_text(json.dumps(summary,indent=2)+'\n')
with (o/'CHECKED_POPULATION.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(pop[0]),lineterminator='\n');w.writeheader();w.writerows(pop)
(o/'READ_MANIFEST.json').write_text(json.dumps(dict(source_commit=base,hashes=hashes,historical_sources=[],checks=checks,source_unchanged=all(hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()==h for f,h in hashes.items())),indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='checks'},indent=2))
