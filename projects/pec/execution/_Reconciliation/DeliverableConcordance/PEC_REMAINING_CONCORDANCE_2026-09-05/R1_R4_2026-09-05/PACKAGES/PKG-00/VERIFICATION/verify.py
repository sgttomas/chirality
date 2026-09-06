import pathlib,csv,json,hashlib,re
root=pathlib.Path.cwd();v=pathlib.Path(__file__).resolve().parent;p=v.parent
hashes={};errors=[]
def read(path):
 path=pathlib.Path(path);path=path if path.is_absolute() else root/path
 b=path.read_bytes();hashes[str(path.relative_to(root))]=hashlib.sha256(b).hexdigest();return b.decode()
def rows(path):return list(csv.DictReader(read(path).splitlines()))
cs=[];rs=[];union={};coverage={}
for d in ['DEL-00-01','DEL-00-02','DEL-00-03']:
 w=p/'WORKERS'/d;m=json.loads(read(w/'READ_MANIFEST.json'))
 for x,h in m['hashes'].items():
  read(x)
  if hashes[x]!=h:errors.append('hash drift '+x)
  union[x]=h
 for f in ['COVERAGE.md','RETURN.md']:read(w/f)
 c=rows(w/'CLAIMS.csv');r=rows(w/'RESIDUALS.csv');cs+=c;rs+=r
 for c1 in c:
  raw=c1['SourceHashes'];m1=json.loads(raw) if raw.startswith('{') else dict(x.split('=',1) for x in raw.split(';') if x)
  for x,h in m1.items():
   read(x)
   if hashes[x]!=h:errors.append('claim hash '+c1['ClaimID']+' '+x)
 candidates=[x for x in m['hashes'] if x.endswith('/ScopeOfWork.md') and '/'+d+'_' in x]
 defs=set()
 if candidates:defs=set(re.findall(r'^- \*\*((?:REQ|AC|VER)-\d+)\*\*',read(candidates[0]),re.M))
 actual={x['ClaimID'].split('::')[1] for x in c}
 missing=defs-actual
 if missing:errors.append('coverage '+d+str(missing))
 coverage[d]={'claims':len(c),'residuals':len(r),'defined_REQ_AC_VER':len(defs),'missing':sorted(missing)}
for f in ['PACKAGE_BASIS.md','SOURCE_MANIFEST.json','validate_package.py','BRIEFS/VERIFIER.md']:read(p/f)
read(p/'WORKERS/DEL-00-01/GAP_ANALYSIS.md')
if rows(p/'PACKAGE_CLAIMS.csv')!=cs:errors.append('aggregate claim mismatch')
if rows(p/'PACKAGE_RESIDUALS.csv')!=rs:errors.append('aggregate residual mismatch')
for c in cs:
 links={x.strip() for x in c['ProposedResidualID'].split(';')}-{ '','NONE','N/A'}
 expected={r['ResidualID'] for r in rs if c['ClaimID'] in {x.strip() for x in r['ClaimIDs'].split(';')}}
 if links!=expected:errors.append('exact reciprocal '+c['ClaimID'])
for r in rs:
 if set(x.strip() for x in r['ClaimIDs'].split(';'))-set(c['ClaimID'] for c in cs):errors.append('unknown linked claim')
# Exact original ID convention, separately recorded finding rather than hidden by validator PASS.
invalid_res=[r['ResidualID'] for r in rs if not re.fullmatch(re.escape(r['DeliverableID'])+r'-REM-\d{3}',r['ResidualID'])]
# Verify each of eleven fallback quoted strings against its recorded quote hash and full declared source.
w=p/'WORKERS/DEL-00-02';md=read(w/'COVERAGE.md');mapping=[]
for line in md.splitlines():
 if not line.startswith('| DEL-00-02::'):continue
 cells=[s.strip() for s in line.split('|')[1:-1]]
 ident,title,locus,h,quote=cells
 path=re.search(r'`([^`]+)`',locus).group(1);source=read(path)
 ok=hashlib.sha256(quote.encode()).hexdigest()==h.strip('`') and quote in source
 mapping.append({'ClaimID':ident,'ok':ok})
 if not ok:errors.append('fallback mapping '+ident)
# Confirm exact source bytes are those separately accepted, independent of copied worker summaries.
b=pathlib.Path('projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working')
accept_checks=[]
for d,f,expected in [('DEL-00-01','artifacts/v2/ADRs.md','f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5'),('DEL-00-03','artifacts/v2/SPEC.md','cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae'),('DEL-00-03','ScopeOfWork.md','3e4f0efc775849b11ae5bdfa851e0d3c125804db87d70f55aac9bc7c77e65741')]:
 target=next(b.glob(d+'_*'))/f;read(target);ok=hashes[str(target)]==expected;accept_checks.append({'path':str(target),'accepted_sha256':expected,'match':ok})
 if not ok:errors.append('acceptance hash '+str(target))
read('projects/pec/execution/_Coordination/_DECISIONS/D-PEC-81_remaining_concordance_activation_2026-09-05.md')
selected=json.loads((v/'selected_ids.json').read_text());byid={x['ClaimID']:x for x in cs}
with (v/'CHECKED_CLAIMS.csv').open('w',newline='') as f:
 writer=csv.writer(f,lineterminator='\n');writer.writerow(['ClaimID','ClaimClass','Disposition','SelectionReason','Result','Evidence'])
 for i in selected:
  c=byid[i];reason='ALL_NONALIGNED_AND_RESIDUAL' if c['Disposition']!='ALIGNED' else 'DETERMINISTIC_CLASS_SAMPLE_OR_ACCEPTANCE_BOUNDARY'
  result='CORRECTION_REQUIRED_CLASS' if i=='DEL-00-03::CON-001' else 'SEMANTICS_SUPPORTED_RESIDUAL_ID_CORRECTION' if i=='DEL-00-01::AC-002' else 'SUPPORTED_WITH_STATED_LIMITS'
  writer.writerow([i,c['ClaimClass'],c['Disposition'],reason,result,c['NormativeSource']+'; '+c['EvidenceReferences']])
validation={'status':'CORRECTION_REQUIRED','mechanical_status':'PASS' if not errors else 'FAIL','errors':errors,'claims':len(cs),'residuals':len(rs),'source_hashes_reproduced':len(union),'coverage':coverage,'checked_claims':len(selected),'nonaligned_checked':sum(byid[x]['Disposition']!='ALIGNED' for x in selected),'residuals_checked':len(rs),'invalid_original_residual_ids':invalid_res,'fallback_mappings':mapping,'exact_acceptance_hash_checks':accept_checks,'findings':['V001','V002']}
(v/'VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n')
checks=json.loads((v/'checks.json').read_text());checks.append({'command':'python3 '+str(v.relative_to(root)/'verify.py'),'cwd':str(root),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0 if not errors else 1,'result':validation})
unchanged=all(hashlib.sha256((root/x).read_bytes()).hexdigest()==h for x,h in hashes.items())
(v/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':'2be412ccea62bdc4bd96deb082c46d7a792076ea','hashes':dict(sorted(hashes.items())),'historical_sources':[],'checks':checks,'source_unchanged':unchanged},indent=2)+'\n')
print(json.dumps(validation,indent=2));print('read hashes',len(hashes),'unchanged',unchanged)
