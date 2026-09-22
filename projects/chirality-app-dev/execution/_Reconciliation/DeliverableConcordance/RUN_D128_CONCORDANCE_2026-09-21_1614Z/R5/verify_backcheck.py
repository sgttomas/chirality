#!/usr/bin/env python3
"""Independent changed-unit extraction from Git/source, not manifest selection.

Uses the original discovery indexer to discover all old/new production units.
Missing and duplicate changed-key negative controls must fail.
"""
from pathlib import Path
from collections import Counter
import csv, hashlib, importlib.util, json, re, subprocess, tempfile, sys
sys.dont_write_bytecode = True

HERE=Path(__file__).resolve().parent;RUN=HERE.parent
ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
BASE='379df923927d157be3ebb51d8a1dcf783d970112'
R6=RUN/'BACKCHECK/R6_2026-09-22'
spec=importlib.util.spec_from_file_location('original_claim_index',RUN/'_scripts/claim_index.py')
indexer=importlib.util.module_from_spec(spec);spec.loader.exec_module(indexer)
def read(p):return [r for r in csv.DictReader(p.open()) if next(iter(r.values()))!='#END']
def sha(b):return hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
def original(path):return subprocess.check_output(['git','show',BASE+':'+path.relative_to(ROOT).as_posix()],text=True)
def units(text,d):
    with tempfile.NamedTemporaryFile(mode='w',suffix='.md') as f:
        f.write(text);f.flush();rows=indexer.sow_units(f.name,d)
    lines=text.splitlines(keepends=True);result={}
    for key,kind,local,section,label,line in rows:
        start=line-1
        end=next((i for i in range(start+1,len(lines)) if re.match(r'^#{2,3} ',lines[i])),len(lines))
        result[key]=''.join(lines[start:end])
    return result
def same_keys(actual,expected):
    assert Counter(actual)==Counter(expected),'changed source-key multiset mismatch'
    assert all(n==1 for n in Counter(actual).values()),'duplicate changed key'

source=read(RUN/'R3/CLAIM_CONCORDANCE.csv')+read(RUN/'R3/EXTENSION_CONCORDANCE.csv')
manifest=read(HERE/'REPAIR_MANIFEST.csv');accounting=read(HERE/'ROW_ACCOUNTING.csv')
inventory=read(RUN/'R1_INVENTORY/DELIVERABLE_INVENTORY.csv')
actual=[];blocks=[];filechecks=[]
for inv in inventory:
    d=inv['DeliverableID'];path=ROOT/inv['Path']/'ScopeOfWork.md'
    before=original(path);after=path.read_text();old=units(before,d);new=units(after,d)
    assert old.keys()==new.keys(),f'{d}: unit identities added/removed without mapping'
    changed=[key for key in old if old[key]!=new[key]]
    reversed_text=after
    for unit in changed:
        source_keys=[r['ClaimKey'] for r in source if r['ClaimKey']==unit or r['ClaimKey'].startswith(unit+'.')]
        assert source_keys,f'{unit}: changed unit has no frozen source rows'
        matches=[r for r in manifest if r['ClaimKey'] in source_keys]
        same_keys([r['ClaimKey'] for r in matches],source_keys)
        for r in matches:
            assert sha(old[unit])==r['BeforeSHA256'],f'{unit}: original block mismatch'
            assert sha(new[unit])==r['AfterSHA256'],f'{unit}: repaired block mismatch'
            assert (ROOT/r['Before']).read_text()==old[unit]
            assert (ROOT/r['After']).read_text()==new[unit]
            actual.append(r['ClaimKey'])
            blocks.append(dict(ClaimKey=r['ClaimKey'],UnitKey=unit,Path=path.relative_to(ROOT).as_posix(),BeforeSHA256=sha(old[unit]),AfterSHA256=sha(new[unit]),Execution=r['Execution'],Result='REEXTRACTED_MATCH'))
        assert reversed_text.count(new[unit])==1
        reversed_text=reversed_text.replace(new[unit],old[unit],1)
    assert reversed_text==before,f'{d}: changed bytes outside declared/discovered units'
    filechecks.append(dict(DeliverableID=d,Path=path.relative_to(ROOT).as_posix(),BeforeSHA256=sha(before),AfterSHA256=sha(after),ChangedUnits=len(changed),InverseReconstruction='EXACT'))
same_keys(actual,[r['ClaimKey'] for r in manifest])
negative=[]
for name,broken in [('missing',actual[:-1]),('duplicate',actual+actual[:1])]:
    try:same_keys(broken,[r['ClaimKey'] for r in manifest])
    except AssertionError:negative.append(name+'_rejected')
    else:raise AssertionError('negative control did not fail: '+name)
same_keys([r['ClaimKey'] for r in accounting],[r['ClaimKey'] for r in source])

status_manifest=read(HERE/'STATUS_REPAIR_MANIFEST.csv');census=read(R6/'REMAINING_WORK_CENSUS.csv')
status_claim_manifest=read(HERE/'STATUS_CLAIM_REPAIR_MANIFEST.csv')
actual_status=[]
def remaining_units(text,d):
    with tempfile.NamedTemporaryFile(mode='w',suffix='.md') as f:
        f.write(text);f.flush();found=indexer.remaining_units(f.name,d)
    lines=text.splitlines(keepends=True);out={}
    for key,kind,local,section,label,line in found:
        start=line-1
        end=next((i for i in range(start+1,len(lines)) if lines[i].startswith(('- ','## '))),len(lines))
        out[key]=''.join(lines[start:end])
    return out
assert {r['DeliverableID'] for r in census}=={r['DeliverableID'] for r in inventory}
for r in status_manifest:
    path=ROOT/r['Path'];before=original(path);after=path.read_text()
    original_units=remaining_units(before,r['DeliverableID']);current_units=remaining_units(after,r['DeliverableID'])
    for unit,oldblock in original_units.items():
        newblock=current_units.get(unit,'')
        if oldblock==newblock:continue
        keys=[x['ClaimKey'] for x in source if x['ClaimKey']==unit or x['ClaimKey'].startswith(unit+'.')]
        matches=[x for x in status_claim_manifest if x['ClaimKey'] in keys]
        same_keys([x['ClaimKey'] for x in matches],keys)
        for row in matches:
            assert sha(oldblock)==row['BeforeSHA256'] and sha(newblock)==row['AfterSHA256']
            assert (ROOT/row['Before']).read_text()==oldblock and (ROOT/row['After']).read_text()==newblock
            actual_status.append(row['ClaimKey'])
            blocks.append(dict(ClaimKey=row['ClaimKey'],UnitKey=unit,Path=r['Path'],BeforeSHA256=sha(oldblock),AfterSHA256=sha(newblock),Execution=row['Execution'],Result='REEXTRACTED_MATCH'))
    old=re.search(r'(?ms)^## Remaining\n(.*?)(?=^## |\Z)',before).group(1)
    new=re.search(r'(?ms)^## Remaining\n(.*?)(?=^## |\Z)',after).group(1)
    assert sha(old)==r['BeforeSHA256'] and sha(new)==r['AfterSHA256']
    assert sha(before)==r['BeforeFileSHA256'] and sha(after)==r['AfterFileSHA256']
    assert old==(ROOT/r['Before']).read_text() and new==(ROOT/r['After']).read_text()
    for field in ['Current State','Checking Approval SHA']:
        pattern=r'^\*\*'+re.escape(field)+r':\*\* (.*)$'
        assert re.findall(pattern,before,re.M)==re.findall(pattern,after,re.M),f'{path}: lifecycle/approval changed'
    old_history=before.split('## History\n',1)[1]
    assert after.split('## History\n',1)[1].endswith(old_history),f'{path}: historical bytes changed'
    assert 'Run claim-level concordance per the reconciliation method' not in new
    assert 'must carry the A1 re-stage' not in new and 'touch carries the A1 re-stage' not in new, f'{path}: obsolete live A1 remains'
    own=[x for x in accounting if x['DeliverableID']==r['DeliverableID'] and x['ResidualCategory'] not in {'NONE','RETIRED_NO_ACTIVATION'}]
    assert not own or r['DeliverableID']+'-R5-RESIDUALS' in new
    extracted=re.findall(r'(?ms)^- .*?(?=^- |\Z)',new) or ['NONE']
    recorded=[x['Text'] for x in census if x['DeliverableID']==r['DeliverableID']]
    assert [x.strip() for x in extracted]==recorded, f'{path}: Remaining census mismatch'

same_keys(actual_status,[r['ClaimKey'] for r in status_claim_manifest])
all_changed=read(HERE/'ALL_CHANGED_CLAIM_MANIFEST.csv')
same_keys(actual+actual_status,[r['ClaimKey'] for r in all_changed])
for broken in [all_changed[:-1],all_changed+all_changed[:1]]:
    try:same_keys([x['ClaimKey'] for x in broken],actual+actual_status)
    except AssertionError:pass
    else:raise AssertionError('combined changed-key negative control did not fail')

# Original discovery/decision packet contents must remain byte-identical.
immutable=[]
for stage in ['R0_CALIBRATION','R0_DONE_DECLARATION','R1_INVENTORY','R2','R3','R4']:
    files=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--',(RUN/stage).relative_to(ROOT).as_posix()],text=True).splitlines()
    for rel in files:
        p=ROOT/rel;old=subprocess.check_output(['git','show',BASE+':'+rel])
        assert p.read_bytes()==old,'Frozen discovery changed: '+rel
    immutable.append(dict(Stage=stage,Files=len(files),Result='UNCHANGED'))

def write(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
write(R6/'CHANGED_CLAIM_REEXTRACTION.csv',blocks)
write(R6/'SOURCE_STATE.csv',filechecks)
summary=dict(verdict='PASS',source_rows=len(source),changed_source_rows=len(actual)+len(actual_status),changed_sow_source_rows=len(actual),changed_status_source_rows=len(actual_status),changed_units=sum(x['ChangedUnits'] for x in filechecks),changed_status_units=len(actual_status),changed_sow_files=sum(x['ChangedUnits']>0 for x in filechecks),source_key_multiset='EXACT',negative_controls=negative,all_sow_inverse_reconstruction='54/54 EXACT',remaining_deliverables=len({x['DeliverableID'] for x in census}),remaining_items=len(census),lifecycle_and_approval_sha='UNCHANGED',historical_status_bytes='PRESERVED',immutable_discovery=immutable)
(R6/'CHECKS.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
