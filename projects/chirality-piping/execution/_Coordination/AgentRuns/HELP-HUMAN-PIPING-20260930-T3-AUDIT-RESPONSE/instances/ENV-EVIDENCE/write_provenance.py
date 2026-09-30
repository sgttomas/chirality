"""Record provenance of this bounded read-only checkpoint; owned output only."""
import datetime, hashlib, json, pathlib, subprocess
ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
OUT=pathlib.Path(__file__).resolve().parent
RUN=OUT.parent.parent
P=ROOT/'projects/chirality-piping'
T3=P/'execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3'
def sha(b):return hashlib.sha256(b).hexdigest()
def entry(p,scope):
 b=p.read_bytes()
 return {'origin':'repository working tree','path':str(p.relative_to(ROOT)),'sha256':sha(b),'bytes':len(b),'read_scope':scope}
inputs=[]
for p,scope in [
 (ROOT/'AGENTS.md','full body'),(P/'AGENTS.md','full body'),(ROOT/'agents/AGENT_TASK.md','full body'),
 (RUN/'instances/DELIVERY/ENV_EVIDENCE_BRIEF.md','full sealed body; exact supplied hash verified'),
 (RUN/'ACTIVATION.md','full body'),(RUN/'PLANNING_BASIS.json','full JSON; listed other-role bodies are references, not loaded'),
 (P/'execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE/WORK_GRAPH.md','full body through bounded chunks'),
 (T3/'AUDIT/HANDOFF.md','full body'),(T3/'AUDIT/REPORT.md','heading/search inspection; lines 58-175 environment/replay/merge/figure limits'),
 (T3/'HANDOFF_2026-09-30_AUDIT_PAUSE.md','initial combined read output partly truncated; explicit sections 0, 5, 6, 9 and search results retained'),
 (T3/'OPERATING_NOTES_2026-09-30.md','initial combined read output partly truncated; inspected source/role background, sections 4 and 8 environment/replay and available later output'),
 (P/'requirements-dev.txt','full body'),(P/'package.json','full JSON'),(P/'apps/desktop/package.json','full JSON'),
 (P/'package-lock.json','existence and hash only; no dependency install'),
 (P/'core/solver/frame_kernel/tests/retained_k4/gen_k4_vectors.py','lines 1-160 read; AST parsed only PINNED mapping, not imported/executed'),
 (ROOT/'.github/workflows/piping-desktop-e2e.yml','lines 155-205 numerical CI sparse checkout'),
 (P/'core/solver/performance_harness/src/bin/k6_observe/alloc.rs','lines 1-145 allocator/backstop model'),
 (P/'core/solver/performance_harness/src/bin/k6_observe/main.rs','search matches and lines 480-550 cap requirement'),
 (T3/'IMPLEMENTATION/KF2/RETURN.md','bounded search for raw gate provenance; no full return review'),
 (T3/'IMPLEMENTATION/KF2/_run_records/b/INDEX.txt','full body'),
 (T3/'IMPLEMENTATION/KF2/_run_records/b/gate/part1/SUMMARY.txt','full body'),
 (T3/'IMPLEMENTATION/KF2/_run_records/b/gate/uncommitted_sha256.txt','full body'),
 (T3/'IMPLEMENTATION/M03_SKEW_PIN_MERGE/dec025/dec025_mac.sh.txt','full body; not executed'),
 (RUN/'ROOT_HOST_OBSERVATION.json','full JSON; supplied ROOT evidence, not this TASK execution')]:
 inputs.append(entry(p,scope))
for name in ['K4','KF1','VK','K6B','KF3','KF2']:
 d=T3/'IMPLEMENTATION'/(name+'_MERGE')
 for rel in ['RECORD.md','SHA256SUMS','dec025/meta.txt','dec025/suites.log','dec025/suites_vs_baseline.txt','dec025/sweep_json_original_sha256.txt']:
  inputs.append(entry(d/rel,'bounded metadata/recovery inspection; complete file hashed; manifest targets mechanically verified'))
inv=json.loads((OUT/'evidence_inventory.json').read_text())
for pin in inv['k4']['pins']:
 inputs.append(entry(ROOT/pin['path'],'complete bytes hashed against K4 pinned digest only; no execution'))
messages=[
 {'from':'/root/delivery_manager','kind':'launch addendum','text':'ROOT adds E0 specifics: set RUSTUP_AUTO_INSTALL=0 even for version probes so missing pinned toolchain cannot trigger implicit download. Guard proposal should use an explicit registry of response-owned process groups with PID/start identity and separate sessions, never command-substring kills. Verify monitoring permissions and label memory readings snapshots. No activation/process kills. Record this launch addendum in context; sealed initial brief remains unchanged.'},
 {'from':'/root/delivery_manager','kind':'supplied ROOT observation','text':"ROOT observed approved read-only host check outside default sandbox: hw.memsize=17179869184, logicalcpu=8; vm.swapusage total=4096.00M, used=3118.19M, free=977.81M; own-shell ps exposes PID/PPID/PGID/RSS; /usr/bin/time -l exposes max RSS and peak footprint. Record explicitly as ROOT's supplied observation, not your own execution. Sandbox denial is not host absence; monitoring needs approved host boundary. Existing ~3.1 GB swap makes free% alone insufficient; guard must baseline and monitor pressure/swap without claiming old swapped pages prove current job trouble. No heavy grant."},
 {'from':'/root/delivery_manager','kind':'supplied evidence pointer and network observation','text':'ROOT host evidence now at Run/ROOT_HOST_OBSERVATION.json in working tree, ROOT-owned; read/hash for your supplied observation record. ROOT also made approved read-only HEAD request to https://static.rust-lang.org/dist/channel-rust-1.97.1.toml: HTTP 200, last-modified 2026-07-16. Exact pinned distribution is available; no download/install. Provide isolated setup proposal with exact 1.97.1, never installed 1.92 substitution. Preserve distinctions between missing suite logs and four KF2 part-2 raw records.'}
]
for m in messages:m['text_utf8_sha256']=sha(m['text'].encode())
context={'record_kind':'TASK read-only environment/evidence checkpoint','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_agent_id':'/root/delivery_manager/env_evidence','canonical_task_name':'/root/delivery_manager/env_evidence','agent_id_source':'native NEW_TASK routing and collaboration.list_agents returned agent_name','additional_uuid':'not exposed by available native result','parent':'/root/delivery_manager','root':'/root','role':'TASK / Type 2','mechanism':'collaboration.spawn_agent','fresh_context':'fork_turns=none, as sealed by parent brief','model':'inherited configured model; no override requested; exact runtime model ID not exposed here','delegated_children':[],'selected_workflow':None,'selected_skill_body':None,'wider_role_bodies_loaded':[],'basis':{'source_audit':'3bddc2b05f6106e969c7cf43373b230845c7cc66','planning':'5506e1f48db66f0119667c52058efa992ed14a5d','activation':'86bb36d6fb88e7699df595bce1d6a31f5fbd6be5','observed_HEAD':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'observed_HEAD_tree':subprocess.check_output(['git','rev-parse','HEAD^{tree}'],text=True).strip()},'sealed_brief_sha256_expected':'8f3fa504c19e56f5b791c71ac86cfebbc6bce7935225af43b6dc49aeee6ee947','sealed_brief_sha256_actual':sha((RUN/'instances/DELIVERY/ENV_EVIDENCE_BRIEF.md').read_bytes()),'launch_addenda_and_supplied_observations':messages,'host_owner_statement':'M3 MacBook Air, 16 GB; original M5 Max 128-GB host and workspace unavailable here','enforcement':'Per-agent write, no-build/no-install/no-kill/no-delegation and Git fences are prompt-only on a shared filesystem. The actual default host sandbox is the enforced outer boundary. No escalation was requested/executed by this TASK. ROOT separately supplied an approved host probe.','writes':str(OUT.relative_to(ROOT))+'/** only','unexpected_writes_observed':None,'unexpected_writes_limit':'No complete host write audit exists; own explicit writes are confined to this folder and Python bytecode was disabled. No source/Git/index mutation command was invoked. Concurrent other agents own other changes.','command_record':'observations.json; runtime_inventory.json; collect_readonly.py; inventory_evidence.py; READ_PROVENANCE.md','inputs':inputs}
assert context['sealed_brief_sha256_expected']==context['sealed_brief_sha256_actual']
(OUT/'CONTEXT.json').write_text(json.dumps(context,indent=2)+'\n')
print('Context entries',len(inputs),'brief hash matches; actual agent /root/delivery_manager/env_evidence')
