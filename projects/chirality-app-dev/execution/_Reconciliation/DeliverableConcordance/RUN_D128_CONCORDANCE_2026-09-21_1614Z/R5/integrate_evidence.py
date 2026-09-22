#!/usr/bin/env python3
"""Integrate independent lookup/mapping and exact changed status-source rows.

Writes derivative evidence only. Production claim/status bytes are read-only.
"""
from pathlib import Path
import csv,hashlib,importlib.util,re,subprocess,tempfile,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;RUN=HERE.parent
ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
BASE='379df923927d157be3ebb51d8a1dcf783d970112'
spec=importlib.util.spec_from_file_location('original_claim_index',RUN/'_scripts/claim_index.py')
indexer=importlib.util.module_from_spec(spec);spec.loader.exec_module(indexer)
def read(p):return [r for r in csv.DictReader(p.open()) if next(iter(r.values()))!='#END']
def write(p,rows,fields=None):
    p.parent.mkdir(exist_ok=True,parents=True)
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)
def sha(t):return hashlib.sha256(t.encode()).hexdigest()
def units(text,d):
    with tempfile.NamedTemporaryFile(mode='w',suffix='.md') as f:
        f.write(text);f.flush();found=indexer.remaining_units(f.name,d)
    lines=text.splitlines(keepends=True);out={}
    for key,kind,local,section,label,line in found:
        start=line-1
        # Include a complete top-level work item, preserving its nested contract.
        end=next((i for i in range(start+1,len(lines)) if lines[i].startswith(('- ','## '))),len(lines))
        out[key]=''.join(lines[start:end])
    return out

source=read(RUN/'R3/CLAIM_CONCORDANCE.csv')+read(RUN/'R3/EXTENSION_CONCORDANCE.csv')
accounting=read(HERE/'ROW_ACCOUNTING.csv');rows={x['ClaimKey']:x for x in accounting}
status=[]
for r in read(HERE/'STATUS_REPAIR_MANIFEST.csv'):
    path=ROOT/r['Path'];d=r['DeliverableID']
    oldtext=subprocess.check_output(['git','show',BASE+':'+r['Path']],text=True);newtext=path.read_text()
    old,new=units(oldtext,d),units(newtext,d)
    for unit,oldblock in old.items():
        if oldblock==new.get(unit):continue
        keys=[x['ClaimKey'] for x in source if x['ClaimKey']==unit or x['ClaimKey'].startswith(unit+'.')]
        if not keys:continue # New/bootstrap-only controls are in the 54-status manifest.
        newblock=new.get(unit,'')
        before=HERE/'STATUS_CLAIMS_BEFORE'/f'{unit.replace("#","_")}.md'
        after=HERE/'STATUS_CLAIMS_AFTER'/before.name
        before.parent.mkdir(exist_ok=True);after.parent.mkdir(exist_ok=True)
        before.write_text(oldblock);after.write_text(newblock)
        for key in keys:
            status.append(dict(ClaimKey=key,DeliverableID=d,Path=r['Path'],Execution='b',Before=before.relative_to(ROOT).as_posix(),After=after.relative_to(ROOT).as_posix(),BeforeSHA256=sha(oldblock),AfterSHA256=sha(newblock),Authority='D-APP-131; D-APP-127 affected-check and retired-helper application',Reason='Preserve remaining obligation; remove completed bootstrap and obsolete live trigger; seat exact residuals. Whitespace-only changes are included in exact physical accounting.',Tranche='STATUS'))
            rows[key]['Action']='REMAINING_RECORD_UPDATED_RESIDUAL_PRESERVED'
write(HERE/'STATUS_CLAIM_REPAIR_MANIFEST.csv',status)
combined=read(HERE/'REPAIR_MANIFEST.csv')+status
assert len({x['ClaimKey'] for x in combined})==len(combined)
write(HERE/'ALL_CHANGED_CLAIM_MANIFEST.csv',combined)

conversion={r['ClaimKey']:r for r in read(HERE/'CONVERSION_EVIDENCE_REVIEW.csv')}
conformance={r['ClaimKey']:r for r in read(HERE/'CONFORMANCE_MAPPING.csv')}
current={r['ClaimKey']:r for r in combined}
notes={r['CurrentObligationSnapshot']:r for r in read(HERE/'CURRENT_RESIDUAL_NOTES.csv')}
original_rows={r['ClaimKey']:r for r in source}
assert set(notes)=={r['After'] for r in combined if r['Tranche']!='STATUS'}
for r in accounting:
    assert r['RemainingWork']==original_rows[r['ClaimKey']]['RemainingWork']
    r['RemainingWorkSemantics']='FROZEN_R3_DISCOVERY_PROPOSAL_ONLY'
    r['AdditionalEvidence']='NONE'
    r['CurrentObligationSource']='UNCHANGED_SOURCE: '+r['SourceLedger']
    r['CurrentObligationSnapshot']='NONE';r['CurrentObligationSnapshotSHA256']='NONE'
    r['CurrentResidual']=('No current remediation assigned by this row.' if r['ResidualCategory']=='NONE' else
        'Retired history only; no production work.' if r['ResidualCategory']=='RETIRED_NO_ACTIVATION' else
        'Unapplied discovery proposal: '+r['RemainingWork']+' Revalidate against D-APP-131 and the packet/subquestion disposition before execution; a settled direction is not a new owner prompt. Gate: '+r['Gate'])
    completed=''
    if r['ClaimKey'] in current:
        m=current[r['ClaimKey']]
        snapshot=ROOT/m['After'];text=snapshot.read_text()
        assert sha(text)==m['AfterSHA256']
        assert text in (ROOT/m['Path']).read_text()
        r['CurrentObligationSource']=m['Path']
        r['CurrentObligationSnapshot']=m['After']
        r['CurrentObligationSnapshotSHA256']=m['AfterSHA256']
        completed='The identified record edit is complete. '
        if r['ResidualCategory']=='NONE':
            r['CurrentResidual']=completed+'No new remediation is assigned to this previously aligned/non-action row. Its current stable obligations are bound by CurrentObligationSnapshot; separately keyed mixed gaps remain separate.'
        elif m['Tranche']=='STATUS':
            r['CurrentResidual']=completed+'Carry forward only the surviving work in the exact current Remaining item bound by CurrentObligationSnapshot, including its named holds and evidence limits. The frozen discovery proposal does not reinstate completed bootstrap or retired live triggers. Gate: '+r['Gate']
        else:
            note=notes[m['After']]
            assert note['CurrentObligationSnapshotSHA256']==m['AfterSHA256']
            assert r['ClaimKey'] in note['ClaimKeys'].split(';')
            r['CurrentResidual']=completed+note['SurvivingFollowthrough']+' Gate: '+r['Gate']
    if r['ClaimKey'] in conversion:
        x=conversion[r['ClaimKey']]
        r['AdditionalEvidence']='R5/CONVERSION_EVIDENCE_REVIEW.csv: '+x['Disposition']
        r['CurrentResidual']=completed+'Historical mechanical conversion evidence recovered (PASS). Lift one-time conversion procedure to historical evidence. Current candidate parity and personal human review are not established by the recovered historic record; evaluate only surviving current claim obligations.'
        if r['Action']=='EXPLICIT_UNCHANGED_RESIDUAL':r['Action']='HISTORICAL_EVIDENCE_RECOVERED_CURRENT_BINDING_OPEN'
    if r['ClaimKey'] in conformance:
        x=conformance[r['ClaimKey']]
        r['AdditionalEvidence']='R5/CONFORMANCE_MAPPING.csv conditions '+x['ConditionIDs']
        mapping=x['MappingDisposition']+' Named current tests and source-equal historical execution are mapped; do not rerun the whole legacy suite. Specific remaining conditions and evidence limits are in CONFORMANCE_MAPPING.md (notably C10 secret sentinel, C13 actual instructed child, C15 packaged/native outcomes).'
        r['CurrentResidual']=(r['CurrentResidual']+' Additional current mapping: '+mapping if r['ClaimKey'] in current else mapping+' Gate: '+r['Gate'])
        if r['ResidualCategory']=='NONE':r['CurrentResidual']+=' This source row retains no new remediation assignment; separately keyed uncovered conditions remain at their owners.'
write(HERE/'ROW_ACCOUNTING.csv',accounting)
for d in sorted({r['DeliverableID'] for r in accounting if r['DeliverableID'].startswith('DEL-')}):
    selected=[r for r in accounting if r['DeliverableID']==d and r['ResidualCategory'] not in {'NONE','RETIRED_NO_ACTIVATION'}]
    write(HERE/'RESIDUALS'/f'{d}.csv',selected,list(accounting[0]))
write(HERE/'EXTENSION_RESIDUALS.csv',[r for r in accounting if r['DeliverableID']=='NONE' and r['ResidualCategory'] not in {'NONE','RETIRED_NO_ACTIVATION'}],list(accounting[0]))
print(f'{len(status)} changed status-source keys; {len(combined)} total changed source keys; {len(conversion)} historical conversion recoveries; {len(conformance)} conformance mapped keys')
