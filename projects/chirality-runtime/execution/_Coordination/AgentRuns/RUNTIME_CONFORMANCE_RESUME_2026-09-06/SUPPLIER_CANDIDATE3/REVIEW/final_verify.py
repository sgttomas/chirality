from pathlib import Path
import datetime, hashlib, json, re, subprocess
E=Path(__file__).resolve().parent
B=E.parent
R=B.parent
N=Path('/private/tmp/runtime-execution-20260906/supplier-candidate/candidate3')
O=N.parent
S=B/'REPAIR_BUILD'
D=N/'builds/attempt2'
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(p):return json.loads(p.read_text())
pins=read(S/'REVIEW_PINS.json')
admission=read(E/'ATTEMPT2_ADMISSION.json')
assert pins==admission['pins']
assert sha(N/'run_attempt2.py')==pins['runner_sha256']
assert sha(S/'capture_attempt2.py')==pins['capture_sha256']
original=read(S/'ORIGINAL_BEFORE.json')
original_mismatches=[p for p,h in original['source_files'].items() if sha(O/'source/codex'/p)!=h]
assert not original_mismatches
repaired=read(S/'SOURCE_REPAIRED.json')['source_files']
repaired_mismatches=[p for p,h in repaired.items() if sha(N/'source'/p)!=h]
assert not repaired_mismatches
assert [p for p,h in repaired.items() if h!=original['source_files'][p]]==['codex-rs/exec-server/src/fs_sandbox.rs']
oldart=[]
for row in original['retained_artifacts']:
    p=Path(row['path']);actual=sha(p);assert actual==row['sha256'];oldart.append({'path':str(p),'sha256':actual,'bytes':p.stat().st_size})
seal=read(R/'SUPPLIER/OUTPUT_MANIFEST.json')
assert all(sha(R/'SUPPLIER'/p)==h for p,h in seal.items())
initial=read(E/'HELPER_TEST_FAILURE_01.json')
assert sha(N/'builds/helper-tests.log')==initial['logSha256']
records={}
for phase in ['helper-tests','protected-glob-tests','candidate3']:
    receipt=read(D/f'{phase}.json'); log=D/f'{phase}.log';t=log.read_text()
    assert receipt['exit']==0
    assert receipt['source_sha256']==receipt['source_after_sha256']==pins['source_sha256']
    assert receipt['runner_sha256']==pins['runner_sha256']
    assert receipt['release_sha256']==sha(B/'BUILD_RELEASE_V2.json')
    assert receipt['log_sha256']==sha(log)
    for suffix in ['json','log','pid.json']:assert sha(D/f'{phase}.{suffix}')==sha(S/f'{phase}.{suffix}')
    summaries=re.findall(r'^test result: ok\. (\d+) passed; (\d+) failed;',t,re.M)
    if phase!='candidate3':assert summaries and all(int(p)>0 and int(f)==0 for p,f in summaries)
    else:assert 'Finished `release` profile' in t
    records[phase]={'receiptSha256':sha(D/f'{phase}.json'),'logSha256':sha(log),'exit':receipt['exit'],'elapsedSeconds':receipt['elapsed_seconds'],'summaries':summaries,'sourceStable':True,'runnerStable':True,'command':receipt['command']}
manifest=read(S/'ARTIFACT_MANIFEST.json'); assert manifest['completion_sha256']==sha(D/'candidate3.json')
assert manifest['source_sha256']==pins['source_sha256'] and manifest['runner_sha256']==pins['runner_sha256']
newart=[]
old=read(S/'COPIED_BEFORE.json')['preexisting_target_outputs']
for row in manifest['artifacts']:
    p=Path(row['path']);assert p.resolve().is_relative_to(N/'artifacts')
    assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
    src=N/'target/aarch64-apple-darwin/release'/row['name'];assert sha(src)==sha(p)
    if row['name']=='codex-app-server':
        assert sha(p)!=old[row['name']]['sha256']
        assert row['source_mtime_ns']>=int(read(D/'candidate3.json')['started']*1e9)
        assert row['version']['exit']==0 and '0.149.0' in row['version']['stdout']
    newart.append({'name':row['name'],'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'versionReceipt':row['version'],'versionIndependentlyExecuted':False,'sameBytesAsPriorTarget':sha(p)==old[row['name']]['sha256'],'magicHex':p.open('rb').read(8).hex()})
policies=[]
for line in (D/'helper-tests.log').read_text().splitlines():
    if 'helper policy writable=' in line:
        label,raw=line[line.index('helper policy writable='):].split(': ',1);policies.append({'label':label,'command':json.loads(raw)})
assert policies==read(S/'GENERATED_HELPER_POLICIES.json') and len(policies)==4
assert sha(D/'helper-tests.log')==read(E/'GENERATED_POLICY_REVIEW.json')['logSha256']
deps=read(S/'COPIED_BEFORE.json')['dependency_identity'];assert all(sha(N/p)==h for p,h in deps.items())
result={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_BOUNDED_CANDIDATE_PREPARATION','pins':pins,'originalSourceCount':len(original['source_files']),'originalSourceMismatches':original_mismatches,'candidateSourceCount':len(repaired),'candidateSourceMismatches':repaired_mismatches,'retainedArtifacts':oldart,'originalSupplierSealFileCount':len(seal),'originalSupplierSealUnchanged':True,'initialHelperFailedLogUnchanged':True,'dependenciesUnchanged':True,'phaseRecords':records,'artifacts':newart,'fourGeneratedPoliciesMatchCapture':True,'reviewerExecutedBinaryOrTests':False,'actualContainmentEstablished':False,'processMetadata':subprocess.check_output(['ps','-axo','pid,ppid,comm'],text=True),'processLimit':'point-in-time command-name census; no exhaustive orphan proof'}
with (E/'FINAL_VERIFICATION.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({k:result[k] for k in ['status','originalSourceCount','candidateSourceCount','originalSupplierSealFileCount','artifacts']}))
