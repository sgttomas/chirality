"""Reproduce bounded PKG07 changed-claim accounting and document checks."""
from pathlib import Path
import csv,hashlib,re,json,subprocess
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[7]
RUN=OUT.parents[1]
APP=ROOT/'projects/chirality-app-dev'
H=lambda b:hashlib.sha256(b).hexdigest()
def writecsv(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def blocks(t):
    return {m[1]:(m[0],t[m.end():].splitlines()[0] if t[m.end():] else 'EOF') for m in re.finditer(r'^### (CLM-\d{3})\b[^\n]*\n(?:(?!^### CLM-|^## ).)*',t,re.M|re.S)}
reasons={
('DEL-07-01','CLM-003'):('D-GOV-43 item 4; D-APP-127; P-09/P-13','Lift obsolete mandatory-hook inventory to the current policy boundary, preserving normative root and protection obligations.'),
('DEL-07-01','CLM-005'):('D-GOV-43 item 4; D-APP-127; existing K-PATH/K-ROOT/K-HOOK obligations; P-09/P-13','Replace construction/module-TBD snapshot with input, reuse and write-protection outcomes, named tests and actual live/legacy evidence limits.'),
('DEL-07-01','CLM-013'):('D-GOV-43 item 4; D-APP-127; original REQ-07-01-001..011; P-09/P-13','Bind all verification requirements to named evidence and candidate/policy/path, retaining missing cases and removing perpetual historic MATCH assertion.'),
('DEL-07-01','CLM-014'):('D-GOV-44 §3.1; existing SOW-002/SOW-027; P-09/P-13','Replace implementation-location TBDs and source-state snapshot with evidence requirements; preserve human assignment and held organisation decisions.'),
('DEL-07-02','CLM-005'):('D-GOV-43/D-APP-127 A2; original scaffold and PREPARATION requirements; P-15','Lift component plan to structure, validation and idempotence outcomes, retaining explicit live scaffold 501 and required implementation verification.'),
('DEL-07-03','CLM-005'):('D-GOV-44 §3.1; existing metadata/document-kit requirements; preserved held migration decisions','Lift scanner component description to deliverable identity, metadata/representation validity, memory and semantic requirements; name current test hooks without accepting a migration.'),
('DEL-07-04','CLM-003'):('SPEC §4.3/§17.2; D-GOV-43/D-APP-127; P-07/P-14','Correct API source and reversal scope, qualify MCP as compatibility, retain actual human authority and open actor/SHA enforcement gap.'),
('DEL-07-04','CLM-005'):('SPEC §4.3; K-GATE-1/K-STATUS-2; D-GOV-43/D-APP-127; P-07/P-14','Lift parser/validator/MCP construction inventory to lifecycle and evidence obligations; retain live enforcement remedy even without a UI.'),
('DEL-07-04','CLM-014'):('D-APP-56 R4-P19; K-GATE-1/K-STATUS-2; D-GOV-43/D-APP-127; P-07/P-14','Replace implementation and actor-map TBDs with known evidence hooks; preserve schema, policy and human authentication/candidate-binding residuals.'),
('DEL-07-05','CLM-014'):('Existing REQ-DEL-07-05-001..018; D-GOV-43/D-APP-127; P-09/P-13','Lift implementation-name assumption and generic test prescriptions to complete requirement-linked named checks with actual gaps and legacy-tool limits.'),
('DEL-07-06','CLM-006'):('K-SNAP-1/K-AUTH-1/K-AUTH-2; SOW-032/033/034; D-GOV-44 §3.1','Lift artifact construction inventory to immutable-snapshot, bypass, candidate-bound approval and tool continuity obligations with named verification.'),
('DEL-07-06','CLM-018'):('D-GOV-44 §3.1; source-verification and preserved human-approval conventions','Replace perpetual source MATCH and obsolete four-document checking procedure with current candidate-bound source and claim review; preserve remaining method obligations.'),
('DEL-07-06','CLM-019'):('D-GOV-44 §3.1; K-AUTH-1/K-AUTH-2; original convention acceptance checklist','Replace MATCH-display requirement with actual source verification and bind documentary review to the candidate; keep all substantive convention checks.')}
rows=[r for r in csv.DictReader((RUN/'R3/CLAIM_CONCORDANCE.csv').open()) if (r.get('DeliverableID') or '').startswith('DEL-07-')]
assert len(rows)==len({r['ClaimKey'] for r in rows})
manifest=[];complement=[];files=[];changes=set();validators=[];reference_checks=[]
AUTH='Current owner authorization as applied by Agent 0, D-APP-131 (not a new human option-letter ruling); execution/_Coordination/AgentRuns/HELP-HUMAN-20260922-CROSS-PROJECT-R5R6/AGENT0_DISPOSITIONS.md; D-GOV-44/kernel Rev2 §3.1; '
for n in range(1,7):
    d=f'DEL-07-{n:02}'
    p=next((APP/'execution').glob(f'PKG-07*/1_Working/{d}*/ScopeOfWork.md'))
    before=(OUT/'before'/f'{d}.ScopeOfWork.md').read_text();after=p.read_text()
    assert after==(OUT/'after'/f'{d}.ScopeOfWork.md').read_text()
    base=subprocess.run(['git','show',f'379df923927d157be3ebb51d8a1dcf783d970112:{p.relative_to(ROOT)}'],cwd=ROOT,capture_output=True,check=True).stdout
    assert base==before.encode(),f'{d} preimage differs from source basis'
    old,new=blocks(before),blocks(after);assert old.keys()==new.keys()
    changed={c for c in old if old[c][0]!=new[c][0]}
    assert changed=={c for dd,c in reasons if dd==d}
    restored=after
    for c in sorted(changed):
        assert after.count(new[c][0])==1
        restored=restored.replace(new[c][0],old[c][0],1)
        changes.add((d,c))
        for phase,b in [('before',old[c][0]),('after',new[c][0])]:
            (OUT/'blocks'/f'{d}.{c}.{phase}.md').write_text(b)
        # Check every explicit file hook/reference in changed units; relative test leaf is anchored explicitly below.
        for ref in sorted(set(re.findall(r'`((?:frontend/|execution/_Scripts/)[^`]+)`',new[c][0]))):
            exists=(APP/ref).exists()
            reference_checks.append(dict(DeliverableID=d,Block=c,Reference=ref,Exists=exists))
            assert exists,(d,c,ref)
    assert restored==before,f'{d}: unlisted source change'
    files.append(dict(DeliverableID=d,Path=str(p.relative_to(ROOT)),BeforeSHA256=H(before.encode()),AfterSHA256=H(after.encode()),Before=str((OUT/'before'/f'{d}.ScopeOfWork.md').relative_to(ROOT)),After=str((OUT/'after'/f'{d}.ScopeOfWork.md').relative_to(ROOT)),ChangedBlocks=len(changed),SourceBasisPreimageEqual=True))
    for r in [r for r in rows if r['DeliverableID']==d]:
        c=r['ClaimID'].split('.')[0]
        if c not in changed:
            complement.append(dict(ClaimKey=r['ClaimKey'],DeliverableID=d,Disposition='UNCHANGED_BY_PKG07_SOW_TRANCHE',SourceR3Disposition=r['Disposition'],Reason='Outside changed CLM blocks; no implementation, lifecycle or acceptance closure asserted. Parent retains row-level residual routing.'));continue
        assert not any(f'D-APP-{v}' in str(r) for v in [116,117,118,119]),r['ClaimKey']
        authority,reason=reasons[(d,c)]
        manifest.append(dict(ClaimKey=r['ClaimKey'],DeliverableID=d,Path=str(p.relative_to(ROOT)),StartAnchor='### '+c,EndAnchor=old[c][1],BeforeSHA256=H(old[c][0].encode()),AfterSHA256=H(new[c][0].encode()),Before=str((OUT/'blocks'/f'{d}.{c}.before.md').relative_to(ROOT)),After=str((OUT/'blocks'/f'{d}.{c}.after.md').relative_to(ROOT)),Execution='b',Authority=AUTH+authority,Reason=reason,SourceR3Disposition=r['Disposition'],SourceImplementationEvidence=r['ImplementationEvidence'],SourceVerificationEvidence=r['VerificationEvidence'],SourceRemainingWork=r['RemainingWork'],ApplicationStatus='TEXT_REPAIRED_WITH_RESIDUALS_PRESERVED',BlockCoverage='Every source R3 key in the changed block mapped, including aligned/split keys; no product check rerun or implementation closure asserted'))
    check=subprocess.run(['python3','tools/scope_of_work/validate_scope_of_work.py','--json',str(p.relative_to(ROOT))],cwd=ROOT,capture_output=True,text=True)
    (OUT/'checks'/f'{d}.sow-validation.json').write_text(check.stdout)
    validators.append(dict(DeliverableID=d,ExitCode=check.returncode,Stderr=check.stderr))
assert changes==set(reasons)
assert {r['ClaimKey'] for r in manifest}.isdisjoint(r['ClaimKey'] for r in complement)
assert len(manifest)+len(complement)==len(rows)
assert {r['ClaimKey'] for r in manifest+complement}=={r['ClaimKey'] for r in rows}
writecsv('REPAIR_MANIFEST.csv',sorted(manifest,key=lambda r:r['ClaimKey']))
writecsv('UNCHANGED_KEYS.csv',sorted(complement,key=lambda r:r['ClaimKey']))
writecsv('FILE_BINDINGS.csv',files)
writecsv('checks/reference_existence.csv',reference_checks)
summary=dict(SourceBasis='379df923927d157be3ebb51d8a1dcf783d970112',SourceR3SHA256=H((RUN/'R3/CLAIM_CONCORDANCE.csv').read_bytes()),ChangedFiles=len(files),ChangedBlocks=len(changes),AffectedR3Keys=len(manifest),UnchangedComplement=len(complement),TotalPackageR3Keys=len(rows),ExactKeyPartition=True,SourceBasisPreimageEquality=True,InverseReconstruction=True,ExplicitFileReferenceChecks=len(reference_checks),ProductTestsRun=False,Validators=validators)
(OUT/'checks/verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
assert all(x['ExitCode']==0 for x in validators)
