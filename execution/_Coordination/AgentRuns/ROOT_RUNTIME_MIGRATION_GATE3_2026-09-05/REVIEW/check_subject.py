from pathlib import Path
import csv,hashlib,json,collections
ROOT=Path(__file__).resolve().parents[5]
P=ROOT/'execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN'
B=ROOT/'execution/_ScopeChange/SCA-005_2026-09-05_2344'
OUT=Path(__file__).parent
checks={}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return list(csv.DictReader(p.open()))
def seal(base,file,expected):
 m=base/file; errors=[]; lines=m.read_text().splitlines()
 for l in lines:
  h,s=l.split(maxsplit=1);p=base/s.lstrip('*')
  if not p.is_file() or digest(p)!=h:errors.append(s)
 return {'digest':digest(m),'expected':expected,'members':len(lines),'errors':errors,'pass':digest(m)==expected and not errors}
checks['gate3']=seal(B,'FINAL_INTEGRATION_V3/COMBINED_ARTIFACTS.sha256','547d1f3369e71aa96d1b61561f6b1603b978016c7335fca39f86df97ddd73fc3')
checks['gate4']=seal(P,'FINAL_ARTIFACTS.sha256','917656f3a828d7e05e2feaf22e14394f1f6dc9fbb26bb99760b633e0ceb17efd')
w=rows(P/'WRITE_TARGETS.csv');errors=[];verified=collections.Counter()
for r in w:
 for pk,hk in [('ApprovedSource','ApprovedSHA256'),('Target','CurrentSHA256')]:
  h=r[hk]
  if len(h)==64:
   p=ROOT/r[pk];verified[hk]+=1
   if not p.is_file() or digest(p)!=h:errors.append([r['Target'],pk])
checks['targets']={'count':len(w),'unique':len({r['Target'] for r in w}),'verified_pins':dict(verified),'errors':errors,'classes':dict(collections.Counter(r['SurfaceClass'] for r in w))}
checks['exact_closure_copies']={f:(P/f).read_bytes()==s.read_bytes() for f,s in [('ROOT_6_PACKAGE_CLOSURE.csv',B/'SOURCE/ROOT_6_PACKAGE_CLOSURE.csv'),('ROOT_53_DISPOSITIONS.csv',B/'SOURCE/ROOT_53_DISPOSITIONS.csv'),('SCOPE_104_SUCCESSOR_MAP.csv',B/'ADDENDUM_REVIEW/SOURCE_104_MAP_POSTIMAGE.csv'),('HOLD_SUCCESSOR_MAP.csv',B/'RUNTIME/HOLD_SUCCESSOR_MAP.csv'),('DEPENDENCY_DISTRIBUTION.csv',B/'RUNTIME/DEPENDENCY_DISTRIBUTION_PREVIEW.csv')]}
c=rows(P/'ROOT_6_PACKAGE_CLOSURE.csv');d=rows(P/'ROOT_53_DISPOSITIONS.csv');r=rows(P/'RUNTIME_METADATA_BINDINGS.csv');s=rows(P/'SCOPE_104_SUCCESSOR_MAP.csv')
checks['closure']={'parents':len(c),'children':len(d),'scope_rows':len(s),'runtime':len(r),'unique_successors':len({x['Successor'] for x in d}),'governance':sum('GovernanceControls/GOV-' in x['Successor'] for x in d),'full_child_sets':all(set(x['Children'].split(';'))=={v['SourceID'] for v in d if v['SourcePackage']==x['SourcePackage']} for x in c),'runtime_initial_open':all(x['InitialState']=='OPEN' for x in r)}
selector=rows(B/'FINAL_INTEGRATION_V3/FINAL_SUBJECT_SELECTOR.csv');old={x['PriorSubject'] for x in selector};checks['obsolete_payload_sources']=[x['ApprovedSource'] for x in w if x['ApprovedSource'] in old]
checks['accounting']={'derivative_rows':len(rows(P/'DERIVATIVE_RECONCILIATION.csv')),'evidence_roots':len(rows(P/'EVIDENCE_OUTPUT_SCOPES.csv')),'guard_paths':len(rows(P/'GUARDS/WRITE_PATH_INVENTORY.csv')),'guard_case_groups':len(rows(P/'GUARDS/ACCEPTANCE_CHECKS.csv')),'reference_index_declared':any(x['Target'].endswith('PKG-02_Runtime_Product/0_References/_REFERENCE_INDEX.md') for x in w)}
assert checks['gate3']['pass'] and checks['gate4']['pass']
assert not errors and len(w)==len({r['Target'] for r in w})==197
assert all(checks['exact_closure_copies'].values()) and not checks['obsolete_payload_sources']
assert checks['closure']['full_child_sets'] and checks['closure']['governance']==46
(OUT/'CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
