"""Static live-packet backcheck; reads files only, invokes no provider or process."""
from pathlib import Path
import hashlib,json,os
HERE=Path(__file__).resolve().parent;RUN=HERE.parents[2];Q=RUN/'instances/ROOT-GUARD-QUALIFICATION'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def events(p):return [json.loads(l) for l in p.read_text().splitlines() if l]
manifest=[]
for line in (Q/'SHA256SUMS').read_text().splitlines():
 expected,name=line.split(maxsplit=1);actual=sha(Q/name)
 manifest.append({'path':name,'match':expected==actual})
raw_inventory=json.loads((Q/'RAW_INVENTORY.json').read_text());binding=json.loads((RUN/'RUNTIME_BINDING.json').read_text())
runtime=Path(os.environ['TMPDIR'])/binding['runtime_directory_name']
raw_checks=[]
for e in raw_inventory:
 raw=runtime/e['raw_alias'].removeprefix('<RESPONSE_RUNTIME>/');portable=Q/e['portable_path']
 raw_checks.append({'alias':e['raw_alias'],'portable_path':e['portable_path'],
  'raw_hash_matches':sha(raw)==e['raw_sha256'],'raw_size_matches':raw.stat().st_size==e['raw_bytes'],
  'portable_hash_matches':sha(portable)==e['portable_sha256']})
by_portable={e['portable_path']:e for e in raw_inventory}
expected=json.loads((Q/'LIVE_RESULTS.json').read_text());cases=[]
for stored in expected:
 folder=Q/'cases'/stored['job_id'];c=json.loads((folder/'controller-controller-result.json').read_text())
 m=events(folder/'guard-monitor.jsonl');s=events(folder/'guard-supervisor.jsonl');reg=json.loads((folder/'guard-registry.json').read_text());job=json.loads((folder/'controller-job.json').read_text())
 samples=[e for e in m if e['kind']=='sample'];term=[e for e in s if e['kind']=='signal-intent' and e['data']['signal']=='TERM'];kill=[e for e in s if e['kind']=='signal-intent' and e['data']['signal']=='KILL'];drain=[e for e in s if e['kind']=='group-drained'];stops=[e for e in m if e['kind']=='stop-request'];sampleat=[e['data']['sample']['at'] for e in samples]
 actual={'sample_count':len(samples),'sampled_rss_peak_bytes':max(e['data']['sample']['rss_bytes'] for e in samples),'sampled_footprint_peak_bytes':max(e['data']['sample']['footprint_bytes'] for e in samples),'max_observed_sample_start_gap_seconds':max((b-a for a,b in zip(sampleat,sampleat[1:])),default=None),'term_to_kill_seconds':kill[0]['at']-term[0]['at'] if kill and term else None,'group_drained_at':drain[0]['at'] if drain else None}
 if c.get('monitor_kill_at') and term:actual['monitor_kill_to_term_seconds']=term[0]['at']-c['monitor_kill_at']
 if c.get('monitor_kill_at') and drain:actual['monitor_kill_to_group_drained_seconds']=drain[0]['at']-c['monitor_kill_at']
 if c.get('monitor_stopped_at'):
  actual['monitor_stop_to_term_seconds']=term[0]['at']-c['monitor_stopped_at'];actual['monitor_stop_to_group_drained_seconds']=drain[0]['at']-c['monitor_stopped_at'];actual['controller_check_after_stop_seconds']=c['post_stall_observation_at']-c['monitor_stopped_at']
 if stops and term and term[0]['at']>=stops[0]['at']:actual['request_to_term_seconds']=term[0]['at']-stops[0]['at']
 checks={'event_copy_identity':c['monitor_events']==m and c['supervisor_events']==s,
  'source_hash':c['guard_sha256']==sha(RUN/'tools/host_guard.py'),
  'job_spec_hash':reg['spec_sha256']==c['job_sha256']==by_portable['cases/'+stored['job_id']+'/controller-job.json']['raw_sha256'],
  'job_registry_agree':reg['job_id']==job['job_id']==stored['job_id'] and reg['limits']==job['limits'] and reg['candidate_sha']==job['candidate_sha'] and reg['input_hashes']==job['input_hashes'],
  'sentinel_survived_unchanged':c['sentinel_survived'] and c['sentinel_unchanged'] and c['sentinel_before']==c['sentinel_after'],
  'sentinel_outside_group':c['sentinel_before']['pgid']!=reg['supervisor']['pgid'],
  'no_controller_errors':not c['errors'],
  'all_final_owned_absent':all(x['state']=='absent' for x in c['owned_exit_observations']),
  'signal_identity_matches_owned_supervisor':all(e['data']['identity']==reg['supervisor'] for e in term+kill),
  'three_quiet_preflight_samples':len([e for e in m if e['kind']=='preflight'])==3,
  'stored_numbers_recompute':all(stored[k]==v for k,v in actual.items() if k in stored)}
 if c['active_latch_remains']:
  resolved=json.loads((folder/'guard-ROOT_LATCH_RESOLUTION.json').read_text());checks['resolved_exact_latch_hash']=resolved['active_sha256']==sha(folder/'guard-ACTIVE.resolved.json');checks['latch_refuses_new_job']=c['latch_probe']['returncode']==2 and 'previous-job-not-cleared-by-root' in c['latch_probe']['stderr']
 elif c['mode']=='clean':checks['concurrent_lock_refuses']=c['lock_probe']['returncode']==2 and 'heavy-slot-busy' in c['lock_probe']['stderr']
 cases.append({'job_id':stored['job_id'],'checks':checks,'derived':actual,'signal_reasons':[e['data']['reason'] for e in term],'workload_exit_events':[e for e in s if e['kind']=='worker-exit']})
p=json.loads((Q/'provider-witness-01.json').read_text());pchecks={'source_hash':p['guard_sha256']==sha(RUN/'tools/host_guard.py'),'three_samples':len(p['samples'])==3,'identities_stable':all(x['identity']==p['samples'][0]['identity'] for x in p['samples']),'normal_pressure':all(x['sample']['pressure']==1 for x in p['samples']),'stable_swap':len({(x['sample']['swap_used_bytes'],x['sample']['swapouts']) for x in p['samples']})==1,'positive_own_metrics':all(x['own_rss_bytes']>0 and x['own_footprint_bytes']>0 for x in p['samples'])}
res={'manifest_count':len(manifest),'manifest_checks':manifest,'raw_file_count':len(raw_checks),'raw_checks':raw_checks,'case_checks':cases,'provider_checks':pchecks,'current_active_latch_present':(runtime/'guard/ACTIVE.json').exists(),'fixture_sha256':sha(Q/'fixture.py'),'max_observed_normal_start_gap':max(c['derived']['max_observed_sample_start_gap_seconds'] or 0 for c in cases),'all_checks_pass':all(x['match'] for x in manifest) and all(all(x[k] for k in ('raw_hash_matches','raw_size_matches','portable_hash_matches')) for x in raw_checks) and all(all(c['checks'].values()) for c in cases) and all(pchecks.values()),'limit':'Existing-file integrity/derivation only; no process/provider reexecution; root resolution booleans remain ROOT-reported checks.'}
print(json.dumps(res,indent=2));assert res['all_checks_pass']
