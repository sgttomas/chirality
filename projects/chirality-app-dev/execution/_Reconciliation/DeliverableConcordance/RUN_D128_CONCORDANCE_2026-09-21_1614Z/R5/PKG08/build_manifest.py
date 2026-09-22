"""Reproduce bounded PKG08 R5 changed-block/claim accounting."""
from pathlib import Path
import csv, hashlib, re, json, subprocess
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[7]
RUN=OUT.parents[1]
H=lambda b:hashlib.sha256(b).hexdigest()
def write_csv(name,rows,fields=None):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)
def blocks(text):
    matches=list(re.finditer(r'^### (CLM-\d{3})\b[^\n]*\n(?:(?!^### CLM-|^## ).)*',text,re.M|re.S))
    return {m[1]:(m.group(), text[m.end():].splitlines()[0] if text[m.end():] else 'EOF') for m in matches}
allrows=[r for r in csv.DictReader((RUN/'R3/CLAIM_CONCORDANCE.csv').open()) if (r.get('DeliverableID') or '').startswith('DEL-08-')]
assert len({r['ClaimKey'] for r in allrows})==len(allrows)
manifest=[];complement=[];files=[];changes=set()
AUTH='Current owner R5/R6 authorization, applied by Agent 0 (not a new human ruling); execution/_Coordination/AgentRuns/HELP-HUMAN-20260922-CROSS-PROJECT-R5R6/AGENT0_DISPOSITIONS.md; D-GOV-44/kernel Rev2 §3.1; '
reasons={
 ('DEL-08-01','CLM-005'):('Current App AGENTS.md; D-GOV-43/D-APP-127; preserved SPEC §7/K-WRITE-1 residual','Lift parser/fixture construction snapshots to conformance, packaging and bounded-execution outcomes; retain format acceptance and missing live evidence.'),
 ('DEL-08-02','CLM-005'):('Current App AGENTS.md; D-APP-108 Q3/SCA-APP-010; preserved P06/P22 corpus residual','Lift component/query TBD slots and matrix fixture prescriptions to sourced identity/navigation requirements with named evidence; retain unresolved older corpus/replay obligations.'),
 ('DEL-08-03','CLM-005'):('D-APP-108/SCA-APP-010; existing presentation-neutral dispatch scope','Replace component inventory with decision-bound taxonomy, inert intent, valid scope and non-authority requirements; retain compatibility presentation evidence.'),
 ('DEL-08-03','CLM-006'):('D-APP-108/SCA-APP-010; existing presentation-neutral dispatch scope','Remove implementation-slot claim surface; name neutral dispatch and scope tests as evidence of stable obligations instead.'),
 ('DEL-08-04','CLM-003'):('Root/App AGENTS.md; D-GOV-35; D-GOV-43/D-APP-127; SCA-APP-010; D-APP-68 safeguards','Lift function/sole-path/hierarchy snapshots to class-specific admission and evidence obligations; apply current instructed role relation without D42 blanket acceptance.'),
 ('DEL-08-04','CLM-005'):('D-GOV-35; D-GOV-43/D-APP-127; SCA-APP-010; preserved D-APP-68 managed safeguards','Replace false live-harness assertion with stable managed admission/handoff requirements and correctly qualified compatibility/native evidence.'),
 ('DEL-08-04','CLM-009'):('D-GOV-35; D-GOV-43/D-APP-127; SCA-APP-010; preserved managed admission safeguards','Lift function-specific scope to managed admission interface, retain native distinction, gates and missing live-path residuals.'),
 ('DEL-08-04','CLM-010'):('Current Root/App AGENTS.md; D-GOV-35; SCA-APP-010; D-GOV-43/D-APP-127; D-GOV-14 retirement boundary','Correct only R05 current role eligibility and R06 exclusive-mechanism claim. Other R01-R11 obligations remain unchanged within this changed block.'),
 ('DEL-08-04','CLM-013'):('Current Root/App AGENTS.md; D-GOV-35; SCA-APP-010; D-GOV-43/D-APP-127','Bind verification to actual class, role basis and live/legacy applicability; preserve all missing-metadata/approval/scope/failure/restriction checks and open coverage findings.'),
 ('DEL-08-05','CLM-014'):('D-APP-40; D-APP-56; D-APP-68; existing CLM037; D-GOV-43/D-APP-127','Lift test-method prose to named class-specific evidence; preserve schema conflict, numeric artifact policy, redaction and incomplete live reconstruction.'),
 ('DEL-08-05','CLM-032'):('D-GOV-44 §3.1; D-APP-56 anti-invention; existing CLM037','Remove schema-shaped illustrative snapshot as an independent claim; retain requirement for class/version-bound examples and non-invention, leaving schema conflict open.')}
for n in range(1,6):
    d=f'DEL-08-{n:02}'
    p=next((ROOT/'projects/chirality-app-dev/execution').glob(f'PKG-08*/1_Working/{d}*/ScopeOfWork.md'))
    before=(OUT/'before'/f'{d}.ScopeOfWork.md').read_text();after=p.read_text()
    assert after==(OUT/'after'/f'{d}.ScopeOfWork.md').read_text()
    old,new=blocks(before),blocks(after);assert old.keys()==new.keys()
    changed={c for c in old if old[c][0]!=new[c][0]}
    assert changed=={c for x,c in reasons if x==d},(d,changed)
    files.append(dict(DeliverableID=d,Path=str(p.relative_to(ROOT)),BeforeSHA256=H(before.encode()),AfterSHA256=H(after.encode()),Before=str((OUT/'before'/f'{d}.ScopeOfWork.md').relative_to(ROOT)),After=str((OUT/'after'/f'{d}.ScopeOfWork.md').relative_to(ROOT)),ChangedBlocks=len(changed)))
    for c in changed:
        for phase,b in [('before',old[c][0]),('after',new[c][0])]:
            (OUT/'blocks'/f'{d}.{c}.{phase}.md').write_text(b)
        changes.add((d,c))
    for r in [r for r in allrows if r['DeliverableID']==d]:
        c=r['ClaimID'].split('.')[0]
        if c not in changed:
            complement.append(dict(ClaimKey=r['ClaimKey'],DeliverableID=d,Disposition='UNCHANGED_BY_PKG08_SOW_TRANCHE',R3Disposition=r['Disposition'],Reason='Outside the changed CLM blocks; no semantic closure or applicability change asserted. Parent may separately disposition status/governance residuals.'));continue
        auth,reason=reasons[(d,c)]
        manifest.append(dict(ClaimKey=r['ClaimKey'],DeliverableID=d,Path=str(p.relative_to(ROOT)),StartAnchor='### '+c,EndAnchor=old[c][1],BeforeSHA256=H(old[c][0].encode()),AfterSHA256=H(new[c][0].encode()),Before=str((OUT/'blocks'/f'{d}.{c}.before.md').relative_to(ROOT)),After=str((OUT/'blocks'/f'{d}.{c}.after.md').relative_to(ROOT)),Execution='b',Authority=AUTH+auth,Reason=reason,SourceR3Disposition=r['Disposition'],SourceImplementationEvidence=r['ImplementationEvidence'],SourceVerificationEvidence=r['VerificationEvidence'],SourceRemainingWork=r['RemainingWork'],ApplicationStatus='TEXT_REPAIRED_WITH_RESIDUALS_PRESERVED',BlockCoverage='Every original split key mapped; no claim-level implementation/acceptance closure asserted'))
assert changes==set(reasons)
assert len(manifest)+len(complement)==len(allrows)
assert set(x['ClaimKey'] for x in manifest).isdisjoint(x['ClaimKey'] for x in complement)
assert set(x['ClaimKey'] for x in manifest+complement)==set(r['ClaimKey'] for r in allrows)
write_csv('REPAIR_MANIFEST.csv',sorted(manifest,key=lambda r:r['ClaimKey']))
write_csv('UNCHANGED_KEYS.csv',sorted(complement,key=lambda r:r['ClaimKey']))
write_csv('FILE_BINDINGS.csv',files)
checks=[]
for f in files:
    p=subprocess.run(['python3','tools/scope_of_work/validate_scope_of_work.py','--json',f['Path']],cwd=ROOT,text=True,capture_output=True)
    (OUT/'checks'/f"{f['DeliverableID']}.sow-validation.json").write_text(p.stdout)
    checks.append(dict(DeliverableID=f['DeliverableID'],ExitCode=p.returncode,Stderr=p.stderr))
summary=dict(SourceBasis='379df923927d157be3ebb51d8a1dcf783d970112',SourceR3SHA256=H((RUN/'R3/CLAIM_CONCORDANCE.csv').read_bytes()),ChangedFiles=len(files),ChangedBlocks=len(changes),AffectedR3Keys=len(manifest),UnchangedComplement=len(complement),TotalPackageR3Keys=len(allrows),ExactKeyPartition=True,Validators=checks)
(OUT/'checks/verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
assert all(c['ExitCode']==0 for c in checks), 'SoW validation failure'
