#!/usr/bin/env python3
"""Build the new R5 derivative and deliverable-local residuals from frozen rows.

The source ledgers are never modified. Production status files are regenerated
from the named pre-repair Git basis, not from a previous generated derivative.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv, hashlib, json, re, subprocess

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
ROOT = Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
PROJECT = ROOT/'projects/chirality-app-dev'
BASE = '379df923927d157be3ebb51d8a1dcf783d970112'
R6 = RUN/'BACKCHECK/R6_2026-09-22'
R6.mkdir(parents=True,exist_ok=True)

def read(p): return [r for r in csv.DictReader(p.open()) if next(iter(r.values())) != '#END']
def write(p,rows,fields=None):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)
def sha(b): return hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
def original(path):return subprocess.check_output(['git','show',BASE+':'+path.relative_to(ROOT).as_posix()],text=True,stderr=subprocess.DEVNULL)

source=read(RUN/'R3/CLAIM_CONCORDANCE.csv')+read(RUN/'R3/EXTENSION_CONCORDANCE.csv')
assert len(source)==3568
assert len({r['ClaimKey'] for r in source})==3568
source_by_key={r['ClaimKey']:r for r in source}
manifest=[]
for group in ['CARRIERS','PKG04','PKG08','PKG06','PKG07']:
    p=HERE/group/'REPAIR_MANIFEST.csv'
    assert p.exists(),str(p)
    for r in read(p):
        manifest.append(dict(ClaimKey=r['ClaimKey'],DeliverableID=r.get('DeliverableID',r['ClaimKey'].split('#')[0]),Path=r.get('Path',r.get('TargetPath')),Execution=r['Execution'],Before=r.get('BeforeSnapshot',r.get('Before',r.get('BeforePath'))),After=r.get('AfterSnapshot',r.get('After',r.get('AfterPath'))),BeforeSHA256=r.get('BeforeSHA256',r.get('BeforeBlockSHA256')),AfterSHA256=r.get('AfterSHA256',r.get('AfterBlockSHA256')),Authority=r['Authority'],Reason=r.get('Reason',r.get('GranularityBasis','Claim-level lift preserving obligations')),Tranche=group))
assert len({r['ClaimKey'] for r in manifest})==len(manifest)
write(HERE/'REPAIR_MANIFEST.csv',manifest)
changed={r['ClaimKey'] for r in manifest}

packet_index=read(RUN/'R4/PACKET_INDEX.csv')
primary={r['ClaimKey']:r['PacketID'] for r in packet_index if r['Role']=='PRIMARY'}
subqs={(r['PacketID'],r['ClaimKey']):r['SubQ'] for r in read(RUN/'R4/PACKET_SUBQUESTIONS.csv')}
policies={
 'P-01':('NARROWS','PRESERVE_OWNER_RESERVED','Owner-deferred DEL-06-02 keys retain both readings; record repair elsewhere may proceed.'),
 'P-02':('NARROWS','PRESERVE_TESTIMONY_AND_UNKNOWN','Carry recorded OC answers; recover actual result records; never infer event absence.'),
 'P-03':('NARROWS','APPLY_PRIOR_RELEASE_DIRECTION','Signing/notarization and prior named candidates already directed; keep future candidate authority and unknown outcomes.'),
 'P-04':('DISSOLVES_REPEAT_QUESTION','APPLY_PRIOR_OWNER_ANSWER','Apply recorded R4-Q6 and D-GOV-43 by exact subject; preserve surviving controls.'),
 'P-05':('DISSOLVES_BASIC_CHOICE','APPLY_EVENT_PRESERVATION','Keep full Codex notifications inspectable; structural redaction remains separate.'),
 'P-06':('NARROWS','APPLY_CURRENT_ROLE_INSTRUCTIONS','Use current four-role instructions; retain exact-byte acceptance and corpus application gaps.'),
 'P-07':('LEAVES_GUARANTEE','ROUTE_ENFORCEMENT_REMEDY','Caller-asserted actor is not proof of human authority; preserve gate and route missing enforcement.'),
 'P-08':('NARROWS','MAP_RETAINED_CONFORMANCE','Map surviving conditions to current checks/S1-S8; only uncovered distinct checks remain; no blanket legacy-suite gate.'),
 'P-09':('DISSOLVES_MECHANISM_DISPUTE','LIFT_PRESERVE_PURPOSE','Historical mechanisms move to evidence; stable live obligations and co-held decisions remain.'),
 'P-10':('NARROWS','APPLY_RULED_PRESERVE_UNRULED','Apply already ruled decisions; D-APP-116..119 stay unruled and held.'),
 'P-11':('MIXED','APPLY_EXACT_PRIOR_DIRECTION','Native resume, A2 and work graph have prior direction; remaining UI/scope facts require exact source mapping.'),
 'P-12':('LEAVES_OBLIGATION','ROUTE_REDACTION_IMPLEMENTATION','Runtime structural redaction obligation and evidence gap remain; no code fix asserted.'),
 'P-13':('NARROWS','CONDITIONAL_HOST_ENFORCEMENT','User-selected sandbox replaces fixed policy; normative authority and domain constraints remain.'),
 'P-14':('LEAVES_GAP','ROUTE_HUMAN_GATE_REMEDY','Preserve human act and expose technical limit; absent UI is not sufficiency.'),
 'P-15':('LEAVES_OBLIGATION','ROUTE_SCAFFOLD_IMPLEMENTATION','Keep still-claimed scaffold operation; route live composition/501 gap.'),
 'P-16':('DISSOLVES_RELEASE_PREREQUISITE','PRESERVE_ACCESSIBLE_HISTORY','No import feature is an MVP release prerequisite; do not promise automatic migration.'),
 'P-17':('DISSOLVES_REPEAT_PERMISSION','APPLY_CARRIER_DIRECTION','Apply D127 consequential changes; SOW079 formal carrier remains scope/materialization residual.'),
 'P-18':('NARROWS','LIFT_STALE_METADATA','Preserve original basis; no automatic global repin; corpus amendments retain governing controls.'),
 'P-19':('NARROWS','LIFT_PRESERVE_REQUIREMENT','Pre-v3 code is evidence, not new scope authority; retain genuine gaps.'),
 'P-20':('DISSOLVES_REPEAT_DIRECTION','APPLY_CODEX_CUSTODY','Codex-only MVP and Codex-held credentials already directed; retained legacy is evidence.'),
 'P-21':('DISSOLVES_REPEAT_DIRECTION','APPLY_A2_OWNERSHIP','Apply App-owned Runtime extraction and explicit retirements; retain controls.'),
 'P-22':('NARROWS','APPLY_SHELL_DIRECTION','Apply accepted shell/current role instructions, not acceptance inferred from code.'),
 'P-23':('NARROWS','PRESERVE_LIVE_GATES','Apply settled scope and native delegation; retain domain and unruled decision gates.'),
 'P-24':('NARROWS','NO_BLANKET_DONE_ACT','Contextual declaration stays context; prior acts apply separately; unknown results remain unknown.'),
 'P-EX':('NARROWS','PRESERVE_AND_CORRECT_RECORD','Preserve evidence rationale honestly; no invented snapshot engine or runbook behavior.')}
packet_rows=[]
for p in sorted(policies):
    members=[r for r in packet_index if r['PacketID']==p]
    effect,action,reason=policies[p]
    for r in members or [{'ClaimKey':'NONE','Role':'NO_PRIMARY_ROWS'}]:
        packet_rows.append(dict(PacketID=p,SubQ=subqs.get((p,r['ClaimKey']),'UNSPLIT'),ClaimKey=r['ClaimKey'],Role=r['Role'],PostureEffect=effect,Application=action,Reason=reason,Authority='D-APP-131; R5/PACKET_AUTHORITY_REVIEW.md; parent AGENT0_DISPOSITIONS.md'))
write(HERE/'PACKET_APPLICATION.csv',packet_rows)

benign={'ALIGNED','NOT_AUDITABLE','ACCEPTED_DIVERGENCE','RETIRED_BY_RULING'}
accounting=[]
for r in source:
    key=r['ClaimKey'];packet=primary.get(key,'NONE');disp=r['Disposition'];d=r['DeliverableID']
    held=packet=='P-01' or bool(re.search(r'D-APP-11[6-9]',r['HumanDecisionNeeded']))
    if held: category='RESERVED_AUTHORITY';gate=r['HumanDecisionNeeded'] if packet!='P-01' else 'Owner-reserved P-01'
    elif d=='DEL-09-07': category='RETIRED_NO_ACTIVATION';gate='D-APP-127 retirement; no production work'
    elif disp in benign: category='NONE';gate='NONE'
    elif disp=='UNKNOWN':category='EVIDENCE_RESULT';gate='Actual result artifact or newly authorized dated check; no inferred outcome'
    elif disp in {'STALE_ASSESSMENT','STALE_VERIFICATION','LIFECYCLE_REASSESSMENT_REQUIRED'}:category='VERIFICATION';gate='Current claim-level evidence; human act remains required for lifecycle'
    elif disp in {'STALE_SPECIFICATION','REMAINING_STATE_MISMATCH'}:category='RECORD_REPAIR';gate='D-APP-131 bounded record authority; preserve substantive gates'
    elif disp=='DEFERRED_AGENT_WORKFLOW':category='SEPARATE_METHOD_SCOPE';gate='Separate instruction/workflow scope and owning authority'
    elif disp=='AUTHORITY_CONFLICT':category='AUTHORITY_APPLICATION';gate='Apply exact prior decision where settled; otherwise retain named owner/scope decision'
    else:category='IMPLEMENTATION_OR_EVIDENCE';gate='Revalidate current live obligation and evidence; bounded implementation brief for code changes'
    # Only the documentary defect is discharged by a lift. Compound requirement,
    # implementation, source, and verification limits are not silently closed.
    if key in changed and disp=='STALE_SPECIFICATION':
        action='RECORD_LIFT_APPLIED';category='CHANGED_CLAIM_FOLLOWTHROUGH';gate='Verify surviving requirements against current evidence; no product completion inferred'
    elif key in changed: action='CLAIM_LIFT_APPLIED_RESIDUAL_PRESERVED'
    elif category=='NONE':action='AUTHORIZED_NO_CHANGE'
    elif category=='RETIRED_NO_ACTIVATION':action='RETIRED_HISTORY_PRESERVED'
    else:action='EXPLICIT_UNCHANGED_RESIDUAL'
    accounting.append(dict(ClaimKey=key,DeliverableID=d,PackageID=r['PackageID'],PacketID=packet,SubQ=subqs.get((packet,key),'UNSPLIT'),SourceDisposition=disp,Action=action,ResidualCategory=category,Gate=gate,RemainingWork=r['RemainingWork'],SourceAuthority=r['NormativeSource'],PriorHumanDecisionNeeded=r['HumanDecisionNeeded'],SourceLedger=r['SourceLedger'],NextOwner='Retired: none' if category=='RETIRED_NO_ACTIVATION' else ('WORKING_ITEMS with owning authority' if category not in {'NONE'} else 'NONE')))
write(HERE/'ROW_ACCOUNTING.csv',accounting)

prior_status={x['Path']:x for x in read(HERE/'STATUS_REPAIR_MANIFEST.csv')} if (HERE/'STATUS_REPAIR_MANIFEST.csv').exists() else {}
status_manifest=[];remaining_census=[];source_status_changes=[]
inventory=read(RUN/'R1_INVENTORY/DELIVERABLE_INVENTORY.csv')
for inv in inventory:
    d=inv['DeliverableID'];folder=ROOT/inv['Path'];path=folder/'_STATUS.md'
    before=original(path)
    rel=path.relative_to(ROOT).as_posix()
    permitted={sha(before)}
    if rel in prior_status:permitted.add(prior_status[rel]['AfterFileSHA256'])
    assert sha(path.read_bytes()) in permitted, 'Refusing to overwrite independently edited status: '+rel
    m=re.search(r'(?ms)^## Remaining\n(.*?)(?=^## |\Z)',before);assert m,d
    old=m.group(1);remaining=old
    remaining=re.sub(r'^- Run claim-level concordance per the reconciliation method.*\n','',remaining,flags=re.M)
    remaining=remaining.replace('Step 0 must carry the A1 re-stage declaration because `frontend/` is touched','D-APP-127 requires repeating checks whose evidence is invalidated by affected source, configuration or packaging changes')
    remaining=remaining.replace('any `frontend/` touch carries the A1 re-stage declaration','affected source, configuration or packaging changes require the D-APP-127 affected-check assessment')
    remaining=re.sub(r'Mandatory non-blocking rerun trigger: if a later accepted D-APP-88\ndistinct-helper implementation lands, rerun the D-APP-86 packaged parity\ninstrument against that changed package identity\.', 'D-APP-127 retires the D-APP-88 distinct-helper packaging subject. Repeat only surviving parity checks whose source, configuration or packaging evidence is invalidated; the former helper trigger is historical.', remaining)
    remaining=re.sub(r'- Rerun the D-APP-86 packaged parity instrument if a distinct D-APP-88\n  headless helper implementation is later accepted and landed, so the guarded\n  navigator result is re-evidenced against the successor packaging/runtime\n  identity bytes\. This is a non-blocking rerun advisory until that trigger\n  fires\. \(gated: accepted and landed D-APP-88 distinct-helper implementation\)', '- Preserve current guarded-navigation parity evidence and repeat affected checks after a relevant source, configuration or packaging change (D-APP-127). The former distinct-helper trigger is retired; no helper implementation is awaited.', remaining)
    if d=='DEL-03-02':
        remaining=remaining.replace("the App's thread index keyed by Codex thread ID carries the bound policy", "replacement storage/interface ownership for the bound policy remains to be established; D-APP-127 does not assign that field")
        remaining=remaining.replace("so the App binds the policy in the boot request and keeps it in its own thread index; no Root acceptance is awaited", "the surviving request-binding obligation remains, with replacement storage/interface ownership to be resolved; no acceptance from that retired Root deliverable is awaited")
    ar=[r for r in accounting if r['DeliverableID']==d and r['ResidualCategory'] not in {'NONE','RETIRED_NO_ACTIVATION'}]
    write(HERE/'RESIDUALS'/f'{d}.csv',ar,fields=list(accounting[0]))
    if d=='DEL-09-07':
        assert not ar
        remaining='\nNone. Retired subject; D-APP-128 concordance bootstrap completed by D-APP-131.\n\n'
    elif ar:
        counts=', '.join(f'{n} {k.lower().replace("_"," ")}' for k,n in sorted(Counter(x['ResidualCategory'] for x in ar).items()))
        remaining=remaining.strip()+f'\n\n- **{d}-R5-RESIDUALS** — Complete the remaining claim-level reconciliation and owning implementation/evidence follow-through: {counts}. Exact source keys, required work and individual gates: `execution/_Reconciliation/DeliverableConcordance/{RUN.name}/R5/RESIDUALS/{d}.csv` (D-APP-131). Apply existing decisions without asking for them again; preserve specifically reserved owner decisions, unknown off-code results, scope/instruction boundaries and human lifecycle acts. Select a bounded subset from this item, revalidate its current source/evidence, and close only the independently backchecked keys. The CSV is supporting evidence for this Remaining item, not a second work-selection surface.\n\n'
        remaining='\n'+remaining.lstrip()
    else:remaining='\n'+(remaining.strip() or 'None.')+'\n\n'
    if d=='DEL-01-01':
        extension_count=sum(x['DeliverableID']=='NONE' and x['ResidualCategory'] not in {'NONE','RETIRED_NO_ACTIVATION'} for x in accounting)
        remaining+=f'- **{d}-R5-EXTENSION-ROUTING** — Route the {extension_count} unseated extension findings in the run\'s `R5/EXTENSION_RESIDUALS.csv` to their already owning document, scope or instruction authority; apply exact prior decisions and preserve real gates. This coordination item authorizes routing and record repair within D-APP-131, not new instruction or product scope.\n\n'
    if d=='DEL-01-04':
        remaining+='- **DEL-01-04-R5-REVERSE-OWNERSHIP** — Review the 107 capability records in the run\'s frozen `R3/UNMAPPED_IMPLEMENTATION.csv` under kernel §3.1: identify stable scope needing its owning scope process, or map mechanism detail to evidence of an existing keyed claim. Do not manufacture 107 new requirements merely because code has no claim. Preserve the exact capability IDs and verify current reach before assigning ownership.\n\n'
    after=before[:m.start(1)]+remaining+before[m.end(1):]
    after=re.sub(r'^\*\*Last Updated:\*\* .*$', '**Last Updated:** 2026-09-22',after,flags=re.M)
    hist='- 2026-09-22 — D-APP-131 R5/R6: completed the D-APP-128 bootstrap, recorded exact residual keys and applied any named carrier repairs. D-APP-127 affected-check rule replaces obsolete A1 re-stage wording in live Remaining only. Historical results, lifecycle and Checking Approval SHA are unchanged.\n'
    after=after.replace('## History\n','## History\n'+hist,1)
    path.write_text(after)
    beforepath=HERE/'STATUS_BEFORE'/f'{d}.md';afterpath=HERE/'STATUS_AFTER'/f'{d}.md'
    beforepath.parent.mkdir(exist_ok=True);afterpath.parent.mkdir(exist_ok=True)
    beforepath.write_text(old);afterpath.write_text(remaining)
    status_manifest.append(dict(ClaimKey=d+'#R5-REMAINING',DeliverableID=d,Path=path.relative_to(ROOT).as_posix(),Before=beforepath.relative_to(ROOT).as_posix(),After=afterpath.relative_to(ROOT).as_posix(),BeforeSHA256=sha(old),AfterSHA256=sha(remaining),BeforeFileSHA256=sha(before),AfterFileSHA256=sha(after),Action='BOOTSTRAP_CLOSEOUT_AND_EXACT_RESIDUAL_SEATING'))
    memory=folder/'MEMORY.md'
    try:memorybefore=original(memory)
    except subprocess.CalledProcessError:memorybefore=f'# MEMORY — {d}\n'
    memory.write_text(memorybefore.rstrip()+f'\n\n- 2026-09-22 — D-APP-131: bounded R5 repair and R6 backcheck recorded in `execution/_Reconciliation/DeliverableConcordance/{RUN.name}/BACKCHECK/R6_2026-09-22/`. Current work is only in `_STATUS.md ## Remaining`; prior evidence and lifecycle remain unchanged.\n')
    record=folder/'_run_records/R5_R6_DAPP131_2026-09-22.md';record.parent.mkdir(exist_ok=True)
    record.write_text(f'# D-APP-131 R5/R6 — {d}\n\nAgent application under the current human reconciliation instruction. Source basis `{BASE}`. Repair keys: '+(', '.join(sorted(changed & {r['ClaimKey'] for r in source if r['DeliverableID']==d})) or 'No ScopeOfWork blocks changed; bootstrap closeout and exact residual seating only.')+f'\n\nR5 manifests, prior/final bytes and individual gates: `execution/_Reconciliation/DeliverableConcordance/{RUN.name}/R5/`. R6 derivative: same run `BACKCHECK/R6_2026-09-22/`. This record claims no new product test result, lifecycle transition, dependency acceptance or release. Actual native delegation and review are recorded by the parent run and R5 tranche returns.\n')
    # The census represents every top-level item, including explicit NONE.
    bullets=re.findall(r'(?ms)^- .*?(?=^- |\Z)',remaining)
    if not bullets:bullets=['NONE']
    for i,item in enumerate(bullets,1):
        remaining_census.append(dict(DeliverableID=d,Item=i,Kind='NONE' if item=='NONE' else 'REMAINING',Text=item.strip(),Path=path.relative_to(ROOT).as_posix(),StatusSHA256=sha(after),Lifecycle=re.search(r'^\*\*Current State:\*\* (.+)$',after,re.M).group(1),R5ResidualKeys=len(ar)))
write(HERE/'STATUS_REPAIR_MANIFEST.csv',status_manifest)
write(R6/'REMAINING_WORK_CENSUS.csv',remaining_census)
write(R6/'PACKAGE_SUMMARY.csv',[dict(PackageID=p,Rows=len(rs),ChangedClaimRows=sum(x['ClaimKey'] in changed for x in rs),ResidualRows=sum(x['ResidualCategory'] not in {'NONE','RETIRED_NO_ACTIVATION'} for x in rs)) for p in sorted({x['PackageID'] for x in accounting}) for rs in [[x for x in accounting if x['PackageID']==p]]])
write(HERE/'EXTENSION_RESIDUALS.csv',[x for x in accounting if not x['DeliverableID'].startswith('DEL-') and x['ResidualCategory'] not in {'NONE','RETIRED_NO_ACTIVATION'}],fields=list(accounting[0]))
print(json.dumps({'source_rows':len(source),'changed_sow_source_rows':len(manifest),'changed_sow_deliverables':len({x['DeliverableID'] for x in manifest}),'status_deliverables':len(status_manifest),'remaining_census_rows':len(remaining_census),'actions':dict(Counter(x['Action'] for x in accounting))},indent=2))
