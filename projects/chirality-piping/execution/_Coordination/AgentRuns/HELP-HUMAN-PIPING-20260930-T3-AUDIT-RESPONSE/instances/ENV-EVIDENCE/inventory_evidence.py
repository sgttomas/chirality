"""Read-only hash/inventory checks. Does not import generators or replay gates."""
import ast, datetime, hashlib, json, pathlib, re, subprocess
ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
OUT=pathlib.Path(__file__).resolve().parent
P=ROOT/'projects/chirality-piping'
T3=P/'execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3'
FK=P/'core/solver/frame_kernel'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''): h.update(b)
 return h.hexdigest()
def item(p):
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)}
def manifest(p):
 rows=[]
 for line in p.read_text().splitlines():
  if not line.strip():continue
  digest, rel=line.split(None,1)
  f=p.parent/rel.lstrip('*')
  actual=sha(f) if f.is_file() else None
  rows.append({'relative_path':rel,'expected_sha256':digest,'actual_sha256':actual,'matches':digest==actual})
 return {'manifest':item(p),'base':str(p.parent.relative_to(ROOT)),'entries':len(rows),'all_match':all(x['matches'] for x in rows),'results':rows}
merges=[]
for name in ['K4','KF1','VK','K6B','KF3','KF2']:
 d=T3/'IMPLEMENTATION'/(name+'_MERGE'); dec=d/'dec025'
 files=[item(x) for x in sorted(d.rglob('*')) if x.is_file()]
 raw=[str(x.relative_to(ROOT)) for x in dec.rglob('*.log') if 'suites' in x.relative_to(dec).parts[:-1]]
 summary=(dec/'suites.log').read_text().splitlines()
 heads=re.findall(r'head ([0-9a-f]{40})',(dec/'meta.txt').read_text())
 sweeps=[x for x in dec.glob('SWEEP_*.json')]
 merges.append({'slice':name,'candidate_head':heads[0], 'historical_recovery_root':'<M5_T3>/scratch/sweep_'+name.lower(),'raw_suite_logs_here':raw,'suite_manifest_count':sum('Cargo.toml' in l for l in summary),'retained_summary_sha256':sha(dec/'suites.log'),'retained_comparison_sha256':sha(dec/'suites_vs_baseline.txt'),'original_unsanitized_sweep_json_sha256':(dec/'sweep_json_original_sha256.txt').read_text().strip(),'sanitized_sweep_files':[item(x) for x in sweeps],'original_suite_hashes':'No individual original suites/*.log hashes found in inspected merge manifests; do not substitute sanitized summary hashes.','files':files,'manifest_verification':manifest(d/'SHA256SUMS')})
b=T3/'IMPLEMENTATION/KF2/_run_records/b'
gate_files=[item(x) for x in sorted((b/'gate').rglob('*')) if x.is_file()]
review=T3/'REVIEW/_run_records/kf2_review/gate'
review_files=[item(x) for x in sorted(review.glob('*.jsonl'))]
part2=b/'gate/part2/runs.jsonl'
part2_count=sum(1 for _ in part2.open())
GEN=FK/'tests/retained_k4/gen_k4_vectors.py'
paths={'K3_GEN':FK/'tests/retained_wide_k3/gen_wide_k3_vectors.py','R1_PY':T3/'REFERENCES/references.py','R1_JSON':T3/'REFERENCES/references.json','FLOOR_JSON':T3/'DESIGN_NUMERICS/_run_records/floor_kinds.json','KD5_MODELS':P/'core/solver/nonlinear_integration/src/structural_adapter/kd5_models.rs','K2B_MODELS':P/'core/solver/nonlinear_integration/src/structural_adapter/k2b_models.rs','NI_FIXTURES':P/'validation/benchmarks/numerical_integrity/fixtures.json'}
tree=ast.parse(GEN.read_text());pins=[]
for node in tree.body:
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PINNED' for t in node.targets):
  for key,val in zip(node.value.keys,node.value.values):
   f=paths[key.id]; expected=ast.literal_eval(val)
   pins.append(dict(item(f),symbol=key.id,expected_sha256=expected,matches=sha(f)==expected,requires_dated_execution_tree='execution' in f.relative_to(P).parts))
data={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'basis_head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'scope':'Six final merge folders (including retained earlier subfolders for hash verification); KF2 B gate and retained reviewer JSONL; seven statically parsed K4 pins. No generator/gate execution or source edits.','merges':merges,'kf2':{'recorded_original_hashes_source':item(b/'gate/uncommitted_sha256.txt'),'originals_recorded_text':(b/'gate/uncommitted_sha256.txt').read_text(),'gate_files':gate_files,'checkpoint_b_manifest_verification':manifest(b/'SHA256SUMS'),'part2_raw_record_count':part2_count,'retained_reviewer_jsonl':review_files,'part1_raw_originals_in_checked_locations':False,'absence_scope':'No part1_base/runs.jsonl or part1_cand/runs.jsonl under this checkpoint-B records folder; historical M5_T3 root absent at mapped project-owned path. No whole-disk content search.'},'k4':{'generator':item(GEN),'pins':pins,'all_pins_match':all(x['matches'] for x in pins),'generator_executed':False,'sparse_checkout_source':item(ROOT/'.github/workflows/piping-desktop-e2e.yml')}}
(OUT/'evidence_inventory.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'merges':[{'slice':m['slice'],'candidate':m['candidate_head'],'raw_suite_logs':len(m['raw_suite_logs_here']),'manifest_summaries':m['suite_manifest_count'],'manifest_entries':m['manifest_verification']['entries'],'hashes_match':m['manifest_verification']['all_match']} for m in merges],'kf2_b_entries':data['kf2']['checkpoint_b_manifest_verification']['entries'],'kf2_b_hashes_match':data['kf2']['checkpoint_b_manifest_verification']['all_match'],'kf2_part2_raw_records':part2_count,'k4_pins':len(pins),'k4_pins_match':data['k4']['all_pins_match'],'retained_reviewer_jsonl':[x['path'].split('/gate/')[-1] for x in review_files]},indent=2))
