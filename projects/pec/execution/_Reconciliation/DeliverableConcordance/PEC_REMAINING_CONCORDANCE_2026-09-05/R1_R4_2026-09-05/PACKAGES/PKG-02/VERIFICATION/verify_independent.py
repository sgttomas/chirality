from pathlib import Path
import csv,json,hashlib,re,subprocess,collections
R=Path.cwd();P=R/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-02';V=P/'VERIFICATION'; reads={};errs=[]; checks=[]
def read(p):
 p=Path(p);p=p if p.is_absolute() else R/p;b=p.read_bytes();reads[str(p.relative_to(R))]=hashlib.sha256(b).hexdigest();return b.decode()
def js(p):return json.loads(read(p))
def rows(p):return list(csv.DictReader(read(p).splitlines()))
for n in ['validate_members.py','check_output_manifests.py']:
 read(P/n);s=subprocess.run(['python3',str(P/n)],capture_output=True,text=True,env=__import__('os').environ|{'PYTHONDONTWRITEBYTECODE':'1'});checks.append({'command':['python3',str((P/n).relative_to(R))],'cwd':'.','environment':'read-only; bytecode disabled','exit_code':s.returncode,'result':json.loads(s.stdout)});errs.extend([] if not s.returncode else [n])
for n in ['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_RECONCILIATION.md','docs/DELIVERABLE_CONCORDANCE_METHOD.md','projects/pec/loop/LOOP_INIT.md','projects/pec/software-workflow.json']:read(n)
for f in (R/'projects/pec/execution/_Coordination/_DECISIONS').glob('D-PEC-8[12]*'):
 if f.is_file():read(f)
for f in P.parent.parent.joinpath('COMMON').glob('*'):
 if f.is_file():read(f)
read(P.parent.parent.parent/'CONVENTIONS.md')
for f in P.glob('*'):
 if f.is_file():read(f)
for f in (P/'BRIEFS').glob('*'):read(f)
C=[];RR=[];pop=[];stats=[]
for w in sorted((P/'WORKERS').glob('DEL-*')):
 for f in w.iterdir():
  if f.is_file():read(f)
 cs=rows(w/'CLAIMS.csv');rs=rows(w/'RESIDUALS.csv');C+=cs;RR+=rs
 for k,h in js(w/'READ_MANIFEST.json')['hashes'].items():
  if Path(k).is_absolute() or '..' in Path(k).parts:errs.append('unsafe input '+k);continue
  read(k)
  if reads[k]!=h:errs.append('source mismatch '+k)
 # Independent strict output manifest check, including resolved containment and complete file population.
 omf=w/'OUTPUT_MANIFEST.json';o=js(omf);entries=o.get('hashes',o.get('outputs',o));seen=set()
 for k,h in entries.items():
  if k in ('source_commit','self_exclusion'):continue
  if not isinstance(h,str) or not re.fullmatch('[0-9a-f]{64}',h):errs.append('invalid output hash '+str(k));continue
  f=R/k if k.startswith('projects/') else w/k
  if Path(k).is_absolute() or '..' in Path(k).parts or not f.resolve().is_relative_to(w.resolve()) or f.resolve()==omf.resolve():errs.append('output containment '+k)
  if f.resolve() in seen:errs.append('duplicate output '+k)
  seen.add(f.resolve())
  if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:errs.append('output hash '+k)
 omitted={f.resolve() for f in w.iterdir() if f.is_file() and f!=omf}-seen
 if omitted:errs.append('unmanifested output '+str(sorted(str(f) for f in omitted)))
 # source hashes: tolerate the two declared serializations, require every full hash match
 for c in cs:
  s=c['SourceHashes'];hm=json.loads(s) if s.startswith('{') else dict(z.split('=',1) for z in s.split(';') if z)
  for k,h in hm.items():
   read(k)
   if reads[k]!=h:errs.append('row hash '+c['ClaimID']+' '+k)
 source=next(R/k for k in js(w/'READ_MANIFEST.json')['hashes'] if k.endswith('/ScopeOfWork.md') and '/'+w.name+'_' in k)
 txt=read(source);ids=re.findall(r'^\|\s*(?:\*\*|`)?((?:REQ|AC|VER|CLM|OUT|TBD|CON|AX)-\d{3})(?:\*\*|`)?\s*\|',txt,re.M)
 # Local SOW definitions are anchors rather than necessarily pipe rows
 ids+=re.findall(r'\{#((?:REQ|AC|VER|CLM|OUT|TBD|CON|AX)-\d{3})\}',txt)
 ids+=re.findall(r'^- \*\*((?:REQ|AC|VER|CLM|OUT|TBD|CON|AX)-\d{3})\*\*',txt,re.M)
 defined=set(ids);actual={c['ClaimID'].split('::')[1] for c in cs};missing=sorted(defined-actual)
 if missing:errs.append('coverage '+w.name+' '+str(missing))
 deps=rows(source.parent/'Dependencies.csv');targets={x['TargetDeliverableID'] for x in deps if x['DependencyClass']=='EXECUTION'}
 for c in cs+rs:
  if c['Depends']!='NONE' and not set(re.split('[;|]',c['Depends']))<=targets:errs.append('depends '+str(c))
 aligned=sorted(c['ClaimID'] for c in cs if c['Disposition']=='ALIGNED')
 # all population expanded to inspect documentary current-history and class boundary consistency
 for c in cs:pop.append({'Kind':'CLAIM','ID':c['ClaimID'],'ClaimClass':c['ClaimClass'],'Disposition':c['Disposition'],'SelectionReason':'required nonaligned/flagged' if c['Disposition']!='ALIGNED' or c['ProposedResidualID'] else ('lowest-ID aligned sample' if c['ClaimID']==aligned[0] else 'expanded documentary/class/acceptance review'),'Source':c['NormativeSource'],'Result':'CHECKED; see VERIFICATION.md boundary adjudication'})
 for c in rs:pop.append({'Kind':'RESIDUAL','ID':c['ResidualID'],'ClaimClass':'residual proposal','Disposition':'NON_SELECTABLE_PENDING_OWNER_APPLICATION','SelectionReason':'every residual required','Source':str((w/'RESIDUALS.csv').relative_to(R)),'Result':'CHECKED; owner-held candidate only'})
 stats.append({'DeliverableID':w.name,'Claims':len(cs),'Residuals':len(rs),'Unknowns':sum(c['Disposition']=='UNKNOWN' for c in cs),'NonAligned':sum(c['Disposition']!='ALIGNED' for c in cs),'LocalDefinitions':len(defined),'REQ_AC_VER':len([i for i in defined if i.startswith(('REQ-','AC-','VER-'))]),'Missing':missing,'AlignedSample':aligned[0]})
# ensure no aggregate substitutions, additions or dropped rows
for nm,allrows in [('PACKAGE_CLAIMS.csv',C),('PACKAGE_RESIDUALS.csv',RR)]:
 ag=rows(P/nm)
 if collections.Counter(json.dumps(x,sort_keys=True) for x in ag)!=collections.Counter(json.dumps(x,sort_keys=True) for x in allrows):errs.append('aggregate '+nm)
for s,t in zip(stats,rows(P/'PACKAGE_SUMMARY.csv')):
 for a,b in [('Claims','Claims'),('Residuals','RawResidualProposals'),('Unknowns','UnknownClaims'),('NonAligned','NonAlignedClaims')]:
  if s[a]!=int(t[b]):errs.append('summary '+s['DeliverableID']+' '+b)
# original manifests verification
om=js(P/'ORIGINAL_WORKER_MANIFEST.json')
def scan(obj):
 if isinstance(obj,dict):
  for k,v in obj.items():
   if isinstance(v,str) and re.fullmatch('[0-9a-f]{64}',v) and ('/' in k or (P/k).is_file()):
    f=R/k if (R/k).is_file() else P/k
    if f.is_file() and hashlib.sha256(f.read_bytes()).hexdigest()!=v:errs.append('original '+k)
   else:scan(v)
 elif isinstance(obj,list):
  for z in obj:scan(z)
scan(om)
# inventory active v2 files: inspect exact source, no mutation or product execution
for f in (R/'projects/pec/v2').rglob('*'):
 if f.is_file() and '__pycache__' not in f.parts:read(f)
# final rehash equality
for k,h in list(reads.items()):
 if hashlib.sha256((R/k).read_bytes()).hexdigest()!=h:errs.append('drift '+k)
with (V/'CHECKED_POPULATION.csv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=list(pop[0]),lineterminator='\n');wr.writeheader();wr.writerows(pop)
out={'source_commit':'2be412ccea62bdc4bd96deb082c46d7a792076ea','structural_errors':sorted(set(errs)),'member_counts':stats,'totals':{'claims':len(C),'residuals':len(RR),'unknowns':sum(c['Disposition']=='UNKNOWN' for c in C),'nonaligned':sum(c['Disposition']!='ALIGNED' for c in C),'checked_population':len(pop)},'checks':checks,'source_unchanged':not any('drift' in e or 'mismatch' in e for e in errs)}
(V/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n');(V/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':out['source_commit'],'hashes':dict(sorted(reads.items())),'historical_sources':[],'checks':checks,'source_unchanged':out['source_unchanged'],'read_kind':'hash/structural comparison for every manifest input; semantic evidence review bounded to checked claims and source loci'},indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
