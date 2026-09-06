"""Candidate3 only. Execute a single admitted phase; never fetch or mutate old trees."""
import hashlib,json,os,re,subprocess,sys,time
from pathlib import Path
ROOT=Path('/private/tmp/runtime-execution-20260906/supplier-candidate/candidate3')
EVIDENCE=Path('/Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/SUPPLIER_CANDIDATE3')
SOURCE=ROOT/'source/codex-rs/exec-server/src/fs_sandbox.rs'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
phase=sys.argv[1]
commands={
 'helper-tests':['cargo','test','--frozen','--release','--target','aarch64-apple-darwin','-p','codex-exec-server','--lib','fs_sandbox::tests','-j','4','--','--test-threads=4','--nocapture'],
 'protected-glob-tests':['cargo','test','--frozen','--release','--target','aarch64-apple-darwin','-p','codex-sandboxing','--lib','unreadable_globs_','-j','4','--','--test-threads=4'],
 'candidate3':['cargo','build','--frozen','--release','--target','aarch64-apple-darwin','--bin','codex-app-server','--bin','codex-code-mode-host','-j','4'],
}
cmd=commands[phase]
release=json.loads((EVIDENCE/'BUILD_RELEASE.json').read_text())
assert release['status']=='ADMITTED', 'manager admission required'
assert release['source_sha256']==sha(SOURCE), 'reviewed source mismatch'
assert release['runner_sha256']==sha(Path(__file__)), 'reviewed runner mismatch'
assert phase in release['phases'], 'phase not admitted'
if phase=='candidate3':
 for required in ['helper-tests','protected-glob-tests']:
  receipt=json.loads((ROOT/'builds'/f'{required}.json').read_text())
  assert receipt['exit']==0 and receipt['source_sha256']==sha(SOURCE)
  assert receipt['runner_sha256']==sha(Path(__file__))
  log=(ROOT/'builds'/f'{required}.log').read_text()
  assert receipt['log_sha256']==sha(ROOT/'builds'/f'{required}.log')
  summaries=re.findall(r'^test result: ok\. (\d+) passed; (\d+) failed;',log,re.MULTILINE)
  assert summaries and all(int(passed)>0 and int(failed)==0 for passed,failed in summaries), 'required source checks did not pass'
for suffix in ['log','json']:
 assert not (ROOT/'builds'/f'{phase}.{suffix}').exists(), 'refuse evidence overwrite'
env={k:os.environ[k] for k in ['HOME','USER','LOGNAME'] if k in os.environ}
env.update(PATH=str(ROOT/'toolchain/rustup/toolchains/1.95.0-aarch64-apple-darwin/bin')+':'+str(ROOT/'toolchain/bin')+':/usr/bin:/bin:/usr/sbin:/sbin',RUSTUP_HOME=str(ROOT/'toolchain/rustup'),CARGO_HOME=str(ROOT/'cache/cargo'),CARGO_TARGET_DIR=str(ROOT/'target'),TMPDIR=str(ROOT/'tmp'),CARGO_BUILD_JOBS='4',CARGO_NET_OFFLINE='true',CARGO_NET_GIT_FETCH_WITH_CLI='true',GIT_CONFIG_GLOBAL='/dev/null',GIT_CONFIG_NOSYSTEM='1',GIT_TERMINAL_PROMPT='0',LC_ALL='C',LANG='C',XDG_CACHE_HOME=str(ROOT/'cache/xdg'),CLANG_MODULE_CACHE_PATH=str(ROOT/'cache/clang-modules'),CARGO_INCREMENTAL='0',RUSTY_V8_ARCHIVE=str(ROOT/'cache/v8/librusty_v8_ptrcomp_sandbox_release_aarch64-apple-darwin.a.gz'),RUSTY_V8_SRC_BINDING_PATH=str(ROOT/'cache/v8/src_binding_ptrcomp_sandbox_release_aarch64-apple-darwin.rs'))
policy='(version 1)(allow default)(deny network*)(deny file-write* (require-not (require-any (subpath '+json.dumps(str(ROOT))+') (literal "/dev/null"))))'
cmd=['/usr/bin/sandbox-exec','-p',policy]+cmd
started=time.time();source_before=sha(SOURCE);runner_hash=sha(Path(__file__))
with (ROOT/'builds'/f'{phase}.log').open('x') as f:
 p=subprocess.Popen(cmd,cwd=ROOT/'source/codex-rs',env=env,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
 (ROOT/'builds'/f'{phase}.pid.json').write_text(json.dumps({'runner_pid':os.getpid(),'child_pid':p.pid,'owned_pgid':p.pid,'started':started})+'\n')
 rc=p.wait()
receipt={'phase':phase,'command':cmd,'exit':rc,'started':started,'completed':time.time(),'elapsed_seconds':time.time()-started,'source_sha256':source_before,'source_after_sha256':sha(SOURCE),'runner_sha256':runner_hash,'release_sha256':sha(EVIDENCE/'BUILD_RELEASE.json'),'environment':env,'log_sha256':sha(ROOT/'builds'/f'{phase}.log'),'scope':'all child writes restricted to Candidate3 or /dev/null; all network denied; no provider/canary execution'}
with (ROOT/'builds'/f'{phase}.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['environment','command']}),flush=True)
sys.exit(rc)
