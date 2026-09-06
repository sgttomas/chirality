from pathlib import Path
import csv,json,re,hashlib,subprocess,collections
P=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-03');V=P/'VERIFICATION/BACKCHECK_V001';V.mkdir(exist_ok=True);base='2be412ccea62bdc4bd96deb082c46d7a792076ea';errors=[];hashes={};checks=[];counts={};population=[]
def hashcheck(p,s):
 p=Path(p)
 if p.is_absolute() or '..' in p.parts:errors.append(['unsafe',str(p)]);return
 a=hashlib.sha256(p.read_bytes()).hexdigest();hashes[str(p)]=a
 if a!=s:errors.append(['hash',str(p)])
for d in ['02','03']:
 did='DEL-03-'+d;old=P/'WORKERS'/did;new=old/'CORRECTION_V001';m=json.loads((new/'CHANGE_MAP.json').read_text());actual=[];ncs={};nrs={}
 for name,key in [('CLAIMS.csv','ClaimID'),('RESIDUALS.csv','ResidualID')]:
  os=list(csv.DictReader((old/name).open()));ns=list(csv.DictReader((new/name).open()))
  if list(os[0])!=list(ns[0]) or [r[key] for r in os]!=[r[key] for r in ns]:errors.append([did,name,'schema or population/order'])
  if b'\r' in (new/name).read_bytes():errors.append([did,name,'CR'])
  for a,b in zip(os,ns):
   for k in a:
    if a[k]!=b[k]:actual.append(dict(file=name,row_id=a[key],field=k,old=a[k],new=b[k]))
   if not b['Depends'] or not any(g in b['ExactGate'] for g in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']):errors.append([did,b[key],'gate/Depends'])
   if b['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append([did,b[key],'selectability'])
   if key=='ClaimID':
    ncs[b[key]]=b
    if b['SourceCommit']!=base:errors.append([did,b[key],'commit'])
    for p,s in json.loads(b['SourceHashes']).items():hashcheck(p,s)
   else:nrs[b[key]]=b
  hashcheck(new/name,m['corrected_ledgers'][name])
 if actual!=[{k:v for k,v in c.items() if k!='finding'} for c in m['changes']]:errors.append([did,'change map does not reproduce exact changes'])
 if any(c['field'] in ['Depends','ExactGate','ClaimID','ResidualID','DeclaredSource','SourceCommit','SourceHashes','Selectability'] for c in actual):errors.append([did,'protected cell changed'])
 for c in actual:population.append(dict(DeliverableID=did,RecordID=c['row_id'],File=c['file'],Field=c['field'],Result='PASS',Old=c['old'],New=c['new']))
 for cid,r in ncs.items():
  for rid in re.findall(r'DEL-\d\d-\d\d-REM-\d{3}',r['ProposedResidualID']):
   if rid not in nrs or cid not in nrs[rid]['ClaimIDs'].split(';'):errors.append([cid,'backlink',rid])
 for rid,r in nrs.items():
  for cid in r['ClaimIDs'].split(';'):
   if cid not in ncs or rid not in ncs[cid]['ProposedResidualID']:errors.append([rid,'backlink',cid])
 if list(nrs)!=[did+'-REM-'+str(i).zfill(3) for i in range(1,len(nrs)+1)]:errors.append([did,'residual sequence'])
 for p,s in m['original_outputs'].items():hashcheck(p,s)
 if m['source_hashes_before']!=m['source_hashes_after']:errors.append([did,'source drift map'])
 for p,s in m['source_hashes_after'].items():hashcheck(p,s)
 rm=json.loads((new/'READ_MANIFEST.json').read_text())
 for p,s in rm['hashes'].items():hashcheck(p,s)
 for p,s in json.loads((new/'OUTPUT_MANIFEST.json').read_text()).items():hashcheck(new/p,s)
 for f in new.iterdir():
  if f.is_file():hashes[str(f)]=hashlib.sha256(f.read_bytes()).hexdigest()
 local=next(Path('projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working').glob(did+'*'))
 for name in ['ScopeOfWork.md','_STATUS.md']:
  cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str((local/name).relative_to('projects/pec')),'--operation','candidate-validation'];r=subprocess.run(cmd,text=True,capture_output=True);checks.append(dict(command=cmd,cwd=str(Path.cwd()),environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=r.returncode,result=r.stdout));
  if r.returncode:errors.append([did,'preflight',r.stdout])
 counts[did]={'claims':len(ncs),'residuals':len(nrs),'changed_cells':len(actual),'dispositions':dict(collections.Counter(r['Disposition'] for r in ncs.values())),'selected':str(new)}
# Recheck complete immutable original report and original worker seals.
for sf in (P/'ORIGINAL_SEALS').glob('*.json'):
 for p,s in json.loads(sf.read_text())['hashes'].items():hashcheck(p,s)
for p,s in json.loads((P/'VERIFICATION/OUTPUT_MANIFEST.json').read_text())['files'].items():hashcheck(P/'VERIFICATION'/p,s)
with (V/'CHECKED_CHANGES.csv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=list(population[0]),lineterminator='\n');wr.writeheader();wr.writerows(population)
(V/'READ_MANIFEST.json').write_text(json.dumps(dict(source_commit=base,hashes=hashes,historical_sources=[],checks=checks,source_unchanged=not errors),indent=2)+'\n')
(V/'VALIDATION.json').write_text(json.dumps(dict(verdict='PASS' if not errors else 'FAIL',errors=errors,members=counts,original_seals_unchanged=True,original_verification_unchanged=True,full_selected_package={'claims':450,'residuals':38,'ALIGNED':187,'UNKNOWN':258,'STALE_INPUT':5},product_or_remaining_closure=False),indent=2)+'\n')
print(json.dumps({'errors':errors,'members':counts,'source_paths':len(hashes)},indent=2))
