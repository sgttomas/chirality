from pathlib import Path
import hashlib,json,difflib
r=Path('/Users/ryan/.codex/worktrees/85d6/chirality');w=r/'projects/chirality-app-dev';run=w/'execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06';base=run/'account-scope';out=base/'ruling-application-v1';(out/'candidate').mkdir(exist_ok=True);(out/'preimage').mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest();quote='Runtime A; D122 A; D123 A';d=w/'execution/_Coordination/_DECISIONS';records=[]
def add(key,target,new,owner):
 old=target.read_bytes() if target.exists() else None
 (out/'candidate'/key).write_bytes(new.encode() if isinstance(new,str) else new)
 if old is not None:(out/'preimage'/key).write_bytes(old)
 new=(out/'candidate'/key).read_bytes()
 (out/'candidate'/(key+'.patch')).write_text(''.join(difflib.unified_diff((old or b'').decode().splitlines(True),new.decode().splitlines(True),fromfile=str(target.relative_to(r)),tofile=str(target.relative_to(r)))))
 records.append({'key':key,'owner':owner,'target':str(target.relative_to(r)),'preimage':'ABSENT' if old is None else 'preimage/'+key,'preimage_sha256':None if old is None else sha(old),'candidate':'candidate/'+key,'postimage_sha256':sha(new),'action':'CREATE' if old is None else 'MODIFY'})
source122=base/'candidate-v1';source123=base/'t5-strip-scope';f122=json.loads((base/'CANDIDATE_FREEZE_v2.json').read_text());f123=json.loads((source123/'FROZEN_CANDIDATE.json').read_text())
for item in f122['files']:assert sha((base/item['path']).read_bytes())==item['sha256']
for item in f123['files']:assert sha((source123/item['path']).read_bytes())==item['sha256']
for number,src,delid in [(122,source122,'05'),(123,source123,'04')]:
 target=next(w.glob('execution/PKG-02*/1_Working/DEL-02-'+delid+'*/_STATUS.md'));assert target.read_bytes()==(src/'PREIMAGE__STATUS.md').read_bytes(),target
ruling122='''# D-APP-122 — Account and Settings host prerequisite ruling

Status: RULED (actual owner selection 2026-09-06). OwnerCaseSelection: A. EffectStatus: HELD until this act is observable on fetched origin/main.

## Owner selection — verbatim

> Runtime A; D122 A; D123 A

The owner selected the exact presented slate. Conversation evidence is preserved in `execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/OWNER_STEER_v2.md`; the D122 option is bounded by `D-APP-122_PACKET_ACCOUNT_SETTINGS_HOST_GATE_2026-09-06.md` and its reviewed exact v2 candidate. The other two clauses do not enlarge D122. No additional owner words or publication permission are inferred.

## Operative choice

A adopts only the DEL-02-05-V3-05 prerequisite/locus amendment: replace the whole-T2 gate with the observable DEL-02-01 account-row host supplied with commit/check/run evidence; retain the separate right-panel-host prerequisite for Settings; explicitly name the account/footer, Settings split/controller, ShellFrame and right-panel presentation integration loci. The exact three approved lines are in `execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/account-scope/candidate-v1/STATUS_DIFF.patch`; original approved status preimage SHA-256 `6e78e98c67cfeb5c75fafc626531e9f8af5624df4fb3ce9398e9b365e959ed5d`, postimage `0dba6b613ee94ed5416345d6df4468936e135b24f1456d7aaddf564bf2edec15`; complete reviewed freeze `4f72e6057f38924f37a7b9a57f45f9b83dee724787195fafa6ac3534d7ecf30f`.

The incorporated STATUS_TRUTHFULNESS_ADDENDUM.md remains binding: daemon running/residency is not proof of external oMLX server availability; missing evidence stays unknown and existing actions retain their true daemon target. No new server control/IPC is authorized. D108 Q7 permits only the Local model server status dot, never an OpenAI/API dot; Q8's routed Root notice and Q5's deferred popout remain. Fake adapter/port contract stay byte-unchanged, with labelled fake/unavailable states and no live-login claim, secret exposure or implicit action. ShellFrame retains state/handlers; one existing runtime controller and one ChatPanel serve the presentation.

## Effect and preservation

This is a bounded D108-seated prerequisite/presentation-locus amendment. Existing accepted account scope remains; no SCA truth, contract pin, acceptance obligation, scope/dependency topology or pointer change occurs. It does not mark DEP014/015 satisfied, close full T2/T3, waive no-folder/Finder/native PDF residuals, or authorize Root/provider/network/lifecycle/release changes. DEL-02-05-V3-03 retains Root DEL-02-09 and G3/G-CSP/G4 gates; Current State and Checking Approval SHA remain unchanged.

Recording the actual owner selection and preparing/applying local metadata are distinct from merged observability and implementation. The reviewed application package includes only the approved status delta plus dated event history, memory/run records and register/ruling transcription. Parent fan-in and separate application release remain required for those exact bytes. Account source remains HELD until this owner act is observed on fetched origin/main, the owning WORKING_ITEMS manager re-derives live scope/APP-HOLD and separately establishes host-criterion evidence. Future implementation requires fresh source freeze/review, registered checks, applicable browser evidence and A1 re-stage/fresh owner proof for future live-login claims. No push, PR, merge or other publication is granted.

The original proposal and pre-selection handoff remain immutable history. This ruling supersedes their D122 selection-pending statements only. Candidate/review artifacts are derivative evidence, not decomposition truth. Exact application preimages must be rechecked; any status/history drift requires a refreshed reviewed postimage rather than blind application.

Transcribed by SCOPE_CHANGE under HELP_HUMAN from the actual owner response; delegated-harness-native, instruction-asserted, Codex/OpenAI GPT-6 family (exact model identifier unavailable). Accepted upstream remains SCA-APP-010 and DepClosure1034 with D108/D120. No final source or whole-tranche validation result is asserted here.
'''
ruling123='''# D-APP-123 — Activity strip primary-session caller ruling

Status: RULED (actual owner selection 2026-09-06). OwnerCaseSelection: A. EffectStatus: HELD until this act is observable on fetched origin/main.

## Owner selection — verbatim

> Runtime A; D122 A; D123 A

The owner selected the exact presented slate. Conversation evidence is preserved in `execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/OWNER_STEER_v2.md`; D123 is bounded by `D-APP-123_PACKET_ACTIVITY_STRIP_PRIMARY_SESSION_LOCUS_2026-09-06.md` and its reviewed candidate. The other clauses do not enlarge D123. No extra owner words or publication permission are inferred.

## Operative choice

A adds only `frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx` and `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx` to DEL-02-04-V3-01's existing write locus, solely to pass the already-held `primarySessionId` as an explicit optional presentation prop into ActivityStrip. The exact one-line addition is in `execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/account-scope/t5-strip-scope/STATUS_DIFF.patch`; approved original status preimage SHA-256 `16053333f23dd8905c5567eeae4151de03e56f77f58fa64d7c52d0dc30d249f0`, postimage `165f443bba9907bfbbcc6f1c4a4e2bb6ded61241edf5204510c41062ab4f0265`; complete reviewed freeze `89cd6d3b8490ea52f105412003e2d2c567fa6812346eb60c0468d29d660e23e6`.

Preserve the same ChatPanel, existing event provider, root/session binding, streaming/selection/reconnect/Details handlers and ShellFrame controls. No state schema, event semantics, provider write, runtime/session field, steering, permission, IPC, CSS or Activity-row navigation callback is authorized. Optional prop acceptance/consumption belongs to the already seated strip component/test locus and is separately selected/reviewed with the caller. Do not derive primary identity from the last event; unavailable/truncated/invalid observations remain unknown or observed-only. Counts/timer/row-navigation semantics are not granted by this caller addition, and its acceptance proves no full T5 completion.

## Effect and preservation

This is a D108-seated item-locus amendment. Existing accepted T5 scope remains; no decomposition/SCA truth, acceptance criterion, dependency/status satisfaction, scope/dependency pointer or topology changes. All V3-01 gates, Depends, checks, return/removal criteria, lifecycle and Checking Approval SHA remain unchanged. D120's separate T2 grant is not broadened, D122 remains separately bounded, and full T5 residuals remain open.

The actual owner selection, local ruling/metadata application, fetched-main observability and source implementation are separate events. The exact approved line plus actual event history/memory/run evidence is frozen in the application package and remains subject to parent fan-in and separate application release. New caller/strip source stays HELD until this owner act is observable on fetched origin/main and WORKING_ITEMS re-derives live scope, APP-HOLD and prerequisites. Subsequent source work must refresh current ActivityView identities, serialize shared-file edits, freeze caller and strip implementation/tests together and pass fresh full-source review plus registered frontend/build/premerge/render/harness/receipt checks and A1 obligations. Current ActivityView repairs are outside the proposal review and are not accepted by this ruling. No final source/whole-tranche or live runtime proof result is asserted. No push, PR, merge or other publication is granted.

Original proposals and pre-selection handoffs remain immutable; this ruling supersedes D123 selection-pending statements only. Candidate artifacts remain derivative evidence, not authority substitutes. Any later status/history drift fails closed for refreshed application review. Accepted upstream remains SCA-APP-010, DepClosure1034, D108 and D120; no SCA/DepClosure rerun is caused by this unchanged-truth locus amendment.

Transcribed by SCOPE_CHANGE under HELP_HUMAN from the actual owner response; delegated-harness-native, instruction-asserted, Codex/OpenAI GPT-6 family (exact runtime model identifier unavailable).
'''
p122=d/'D-APP-122_RULING_ACCOUNT_SETTINGS_HOST_GATE_2026-09-06.md';p123=d/'D-APP-123_RULING_ACTIVITY_STRIP_PRIMARY_SESSION_LOCUS_2026-09-06.md';assert not p122.exists() and not p123.exists();add('D122_RULING.md',p122,ruling122,'SCOPE_CHANGE');add('D123_RULING.md',p123,ruling123,'SCOPE_CHANGE')
reg=d/'_REGISTER.md';s=reg.read_text()
for n,ruling in [(122,p122),(123,p123)]:
 line=next(x for x in s.splitlines() if x.startswith(f'| D-APP-{n} |'));assert '| AWAITING_RULING |' in line
 new=line.replace('| AWAITING_RULING |','| RULED (owner selection 2026-09-06; effect HELD until fetched main) |');cols=new.split('|');cols[-2]=' `execution/_Coordination/_DECISIONS/'+ruling.name+'`; option A; source effect HELD until required gates; no publication authority ';new='|'.join(cols);s=s.replace(line,new)
add('REGISTER.md',reg,s,'SCOPE_CHANGE')
for n,src,delid,item in [(122,source122,'05','DEL-02-05-V3-05'),(123,source123,'04','DEL-02-04-V3-01')]:
 folder=next(w.glob('execution/PKG-02*/1_Working/DEL-02-'+delid+'*'));s=(src/'CANDIDATE__STATUS.md').read_text();basis=('account-host prerequisite and exact account/Settings presentation loci' if n==122 else 'existing-primarySessionId ActivityStrip caller/test locus');hist=f'- 2026-09-06 - Owner selected D-APP-{n} A in the exact slate response "Runtime A; D122 A; D123 A": {item} now records the approved {basis}. Ruling effect remains HELD until observed on fetched origin/main; source implementation is not selected here. Full accepted residuals, dependency satisfaction, lifecycle and Checking Approval SHA are unchanged. Evidence: `_run_records/D_APP_{n}_OWNER_SELECTION_2026-09-06.md`; exact reviewed application package `execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/account-scope/ruling-application-v1/`.\n';s=s.replace('## History\n','## History\n'+hist);s=s.replace('**Last Updated:** 2026-09-04','**Last Updated:** 2026-09-06');add(f'DEL02{delid}_STATUS.md',folder/'_STATUS.md',s,'WORKING_ITEMS_PKG02')
 mem=(folder/'MEMORY.md').read_text();mem+=f'\n## 2026-09-06 — D-APP-{n} A owner selection\n\nThe owner selected "Runtime A; D122 A; D123 A". D-APP-{n} A adopts only the {basis} for {item}. Consult its ruling and the exact application snapshot; this memory is non-authoritative. Effect remains HELD until the owner act is observable on fetched origin/main. No new source implementation, dependency satisfaction, full-item/lifecycle closure or publication is established. Existing residuals and gates remain; a later source freeze must use current identities. See `_run_records/D_APP_{n}_OWNER_SELECTION_2026-09-06.md`.\n';add(f'DEL02{delid}_MEMORY.md',folder/'MEMORY.md',mem,'WORKING_ITEMS_PKG02')
 rr=f'''# D-APP-{n} A — owner selection and bounded metadata record

Owner response, verbatim:

> Runtime A; D122 A; D123 A

Selection evidence: `execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/OWNER_STEER_v2.md`. This deliverable records only D-APP-{n} A: {basis} for {item}. The exact approved proposal and new ruling govern; other slate clauses confer no additional scope here.

EffectStatus: HELD until the owner act is observed on fetched origin/main. The application candidate places only the approved status delta plus this dated event history/memory/run evidence; owner choice occurred, but source implementation and full item acceptance did not. Parent review/application release, package ownership, exact preimage checks and final union closeout remain distinct. Current State and Checking Approval SHA remain unchanged. No dependency satisfaction, accepted pointer, SCA truth, Root, product source or publication act is made.

Canonical candidate snapshot: `execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/account-scope/ruling-application-v1/`. Its write manifest provides exact original preimages and complete postimages for independent review/application. Refresh on any drift. Fresh review result is read from the actual snapshot return, never anticipated here.

Accepted upstream: SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA; CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034; D108/D120. This run record is derivative operational evidence, not decomposition truth. No SCA/DepClosure rerun is caused by the unchanged accepted truth. Remaining work: merged owner observability, later selected source/evidence work under all standing gates, full deliverable residuals. No final frontend/source/whole-tranche validation pass is claimed here.

SCOPE_CHANGE prepared the exact candidate under HELP_HUMAN; WORKING_ITEMS PKG02 owns its separately released local application. Native roles are instruction-asserted; no permission inheritance. Runtime/provider/model attribution is Codex/OpenAI GPT-6 family, exact model identifier unavailable.
''';target=folder/f'_run_records/D_APP_{n}_OWNER_SELECTION_2026-09-06.md';assert not target.exists();add(f'DEL02{delid}_RUN_RECORD.md',target,rr,'WORKING_ITEMS_PKG02')
(out/'WRITE_MANIFEST.json').write_text(json.dumps({'status':'CANDIDATE_ONLY_NOT_APPLIED','owner_response':quote,'owner_response_sha256':sha(quote.encode()),'records':records,'application_order':['SCOPE_CHANGE coordination candidates on separate parent release','WORKING_ITEMS_PKG02 local candidates on separate parent release'],'source_authority':'HELD until owner acts observable on fetched origin/main','publication':'NONE'},indent=2)+'\n')
inputs=set()
for sf,root in [(source122/'INPUT_IDENTITIES.json',r),(source123/'INPUT_IDENTITIES.json',r)]:
 for x in json.loads(sf.read_text()):inputs.add(r/x['path'])
for path in [run/'OWNER_STEER_v2.md',run/'WORK_GRAPH_v7.json',run/'ORCHESTRATION_PLAN_v7.md',run/'instances/resume_account_scope/AMENDMENT_v4.md',base/'CANDIDATE_FREEZE_v2.json',source123/'FROZEN_CANDIDATE.json',d/'D-APP-122_PACKET_ACCOUNT_SETTINGS_HOST_GATE_2026-09-06.md',d/'D-APP-123_PACKET_ACTIVITY_STRIP_PRIMARY_SESSION_LOCUS_2026-09-06.md',reg]:inputs.add(path)
(out/'CURRENT_INPUT_IDENTITIES.json').write_text(json.dumps([{'path':str(f.relative_to(r)),'sha256':sha(f.read_bytes())} for f in sorted(inputs)],indent=2)+'\n')
print(json.dumps({'files':len(records),'manifest_sha256':sha((out/'WRITE_MANIFEST.json').read_bytes()),'owner_response_sha256':sha(quote.encode()),'activity_sha256':sha((w/'frontend/src/components/woven-dialogue/activity-shelf.tsx').read_bytes())},indent=2))
