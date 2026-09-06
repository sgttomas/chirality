from pathlib import Path
import json,csv,hashlib,subprocess,collections
r=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05');p=r/'SYNTHESIS/APPLICATION_PREPARATION';o=p/'FULL_01';sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest();base='2be412ccea62bdc4bd96deb082c46d7a792076ea'
def dump(n,v):(o/n).write_text(json.dumps(v,indent=2)+'\n')
hashes={};checks=[]
for f in [p/'INITIAL_READS.json',p/'SOURCE_CHECK.json',o/'RELEASE_READS.json',o/'ADDITIVE_SOURCE_READS.json',o/'PUBLICATION_REBIND.json']:
 doc=json.loads(f.read_text());hashes.update(doc['hashes']);checks+=doc['checks']
def preflight(path,operation='consume'):
 cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str(Path(path).relative_to('projects/pec')),'--operation',operation];a=subprocess.run(cmd,text=True,capture_output=True);assert a.returncode==0;checks.append({'command':cmd,'exit_code':0,'result':a.stdout.strip()})
selections=[]
for k in range(11):
 root=r/f'PACKAGES/PKG-{k:02}'
 for f in ['OUTPUT_MANIFEST.json','PACKAGE_CLAIMS.csv','PACKAGE_RESIDUALS.csv']:
  path=root/f;preflight(path);hashes[str(path)]=sha(path)
 m=json.loads((root/'OUTPUT_MANIFEST.json').read_text());mh=m.get('hashes',m.get('files',{}))
 for f in ['PACKAGE_CLAIMS.csv','PACKAGE_RESIDUALS.csv']:
  full=str(root/f);assert full in mh;expected=mh[full];expected=expected['sha256'] if isinstance(expected,dict) else expected;assert sha(root/f)==expected
 selections.append({'PackageID':f'PKG-{k:02}','OutputManifestPath':str(root/'OUTPUT_MANIFEST.json'),'OutputManifestSHA256':sha(root/'OUTPUT_MANIFEST.json'),'SelectedClaimsPath':str(root/'PACKAGE_CLAIMS.csv'),'SelectedClaimsSHA256':sha(root/'PACKAGE_CLAIMS.csv'),'SelectedResidualsPath':str(root/'PACKAGE_RESIDUALS.csv'),'SelectedResidualsSHA256':sha(root/'PACKAGE_RESIDUALS.csv'),'selected_aggregate_hashes_reproduce':True})
car=list(csv.DictReader((o/'CARRIER_DISPOSITIONS.csv').open()));items=list(csv.DictReader((o/'PROPOSED_ITEMS.csv').open()));mapping=json.loads((o/'CLAIM_TO_PROPOSAL_MAP.json').read_text());app=json.loads((o/'APPLICATION_MANIFEST.json').read_text())
for c in car:preflight(c['CarrierPath'],'candidate-validation');assert sha(c['CarrierPath'])==c['PreimageSHA256']
for e in app['entries']:
 b=Path(e['PreimageCopy']).read_bytes();after=Path(e['CandidateCopy']).read_bytes();assert after.startswith(b);assert b'## Remaining' not in b and after.count(b'## Remaining')==1;assert sha(e['CandidateCopy'])==e['ProposedPostimageSHA256'];assert sha(e['PreimageCopy'])==e['CurrentPreimageSHA256']
assert len(mapping)==165 and len(items)==92 and len(car)==64 and len(app['entries'])==58
assert all(x['Depends']=='NONE' and '/_run_records/REMAINING_EVIDENCE_'+x['ResidualID']+'/' in x['ItemGate'] for x in items if x['Route']=='EVIDENCE')
assert not any('calibration' in x['ProposedText'].lower() or 'D82' in x['ItemGate'] for x in items)
assert len(set(i['ResidualID'] for i in items))==92
assert all(x['ProposedItem'] is None for x in mapping if x['ProposedRoute'] in ['HELD','CONDITIONAL'])
scanner=json.loads((r/'SYNTHESIS/SCANNER/OUTPUT_MANIFEST.json').read_text());assert all(sha(f)==h for f,h in scanner['hashes'].items())
for f in ['OUTPUT_MANIFEST.json','ORIGINAL_LINKED_CLAIMS.json','ORIGINAL_RESIDUALS.json','READ_MANIFEST.json','SOURCE_CHECK.json']:hashes[str(p/f)]=sha(p/f)
drift=[f for f,h in hashes.items() if sha(f)!=h];assert not drift,drift
version=subprocess.check_output(['python3','--version'],text=True).strip()
for c in checks:c.setdefault('cwd',str(Path.cwd()));c.setdefault('environment',{'python':version,'bytecode':'not generated; no product-module import'})
dump('SELECTED_PACKAGE_INPUTS.json',selections)
dump('VALIDATION.json',{'status':'PASS_FOR_FULL_APPLICATION_PREPARATION','source_commit':base,'carrier_count':64,'proposed_item_count':92,'candidate_carrier_count':58,'no_application_carrier_count':6,'original_residual_count':165,'route_counts':dict(collections.Counter(x['ProposedRoute'] for x in mapping)),'item_counts':dict(collections.Counter(x['Route'] for x in items)),'all64_exact_preflight_allow':True,'all64_source_preimages_equal_current':True,'all58_apply_inverse_nonremaining_checks_pass':True,'original_scanner_unchanged':True,'selected11_aggregate_hashes_match_manifests':True,'all_declared_final_read_hashes_reproduce':True,'source_target_writes':0,'product_suite_run':False,'independent_final_R4_review':'REQUIRED; author validation only'})
dump('READ_MANIFEST.json',{'source_commit':base,'native_identity':'/root/pec_corpus_synthesis/scanner_proposal','parent_native_identity':'/root/pec_corpus_synthesis','role':'ephemeral Agent2; instruction-asserted nondelegation','hashes':hashes,'historical_sources':[],'checks':checks,'source_unchanged':True,'scope':'Declared final input hashes and all64 carrier/source bytes; excludes unrelated concurrent workspace state. Changed original package publication identities preserved in partial records and explicit PKG00/PKG08 successor maps.','partial_current_drift_disposition':'Final selection uses released corrected00 and lossless08 successor; partial original hashes remain historical, not current.'})
for name in ['PROPOSAL.md','HANDOFF.md']:
 f=o/name;t=f.read_text()
 for a,b in {'All64':'All 64','all64':'all 64','all58':'all 58','All57':'All 57','are92':'are 92','in58':'in 58','copies:78':'copies: 78','inquiries,6':'inquiries, 6','obligations,6':'obligations, 6','and2':'and 2','The165':'The 165','accounted:70':'accounted: 70','plus3':'plus 3','artificial64':'artificial 64','The78':'The 78','The6':'The 6','The2':'The 2','source base2':'source base 2','accounted:92':'accounted: 92','and6':'and 6','writes0':'writes 0',';58':'; 58'}.items():t=t.replace(a,b)
 t=t.replace('after final input-publication rebinding','with final released package-publication identities rebound');f.write_text(t)
f=o/'PROPOSAL.md';t=f.read_text();t+='\nEach evidence item names its proposed derivative output root under its owning deliverable `_run_records/REMAINING_EVIDENCE_<ResidualID>/`. These exact future report/evidence-manifest creation paths remain gated in the item; no directory was created there and no report production is authorized by this preparation.\n';f.write_text(t)
files={str(f):sha(f) for f in sorted(o.rglob('*')) if f.is_file() and f.name!='OUTPUT_MANIFEST.json'};dump('OUTPUT_MANIFEST.json',{'kind':'full64_exact_application_preparation_derivative','source_commit':base,'native_identity':'/root/pec_corpus_synthesis/scanner_proposal','status':'READY_FOR_MANAGER_AND_INDEPENDENT_R4_REVIEW','self_excluded':True,'hashes':files})
print('FULL_01 sealed',len(files),'outputs;',len(hashes),'read hashes;',len(checks),'checks. Manifest SHA',sha(o/'OUTPUT_MANIFEST.json'))
