import os,subprocess,sys,json,time
from pathlib import Path
root=Path('/private/tmp/runtime-supplier-resume-20260906/FIXTURE_ADAPTED')
env={k:os.environ[k] for k in ['HOME','USER','LOGNAME'] if k in os.environ}
env.update(PATH=str(root/'toolchain/rustup/toolchains/1.95.0-aarch64-apple-darwin/bin')+':'+str(root/'toolchain/bin')+':/usr/bin:/bin:/usr/sbin:/sbin',RUSTUP_HOME=str(root/'toolchain/rustup'),CARGO_HOME=str(root/'cache/cargo'),CARGO_TARGET_DIR=str(root/'builds/target'),TMPDIR=str(root/'tmp'),CARGO_BUILD_JOBS='4',CARGO_NET_GIT_FETCH_WITH_CLI='true',GIT_CONFIG_GLOBAL='/dev/null',GIT_CONFIG_NOSYSTEM='1',GIT_TERMINAL_PROMPT='0',LC_ALL='C',LANG='C')
v8=root/'cache/v8'
env.update(XDG_CACHE_HOME=str(root/'cache/xdg'),CLANG_MODULE_CACHE_PATH=str(root/'cache/clang-modules'),CARGO_INCREMENTAL='0')
env['RUSTY_V8_ARCHIVE']=str(v8/'librusty_v8_ptrcomp_sandbox_release_aarch64-apple-darwin.a.gz')
env['RUSTY_V8_SRC_BINDING_PATH']=str(v8/'src_binding_ptrcomp_sandbox_release_aarch64-apple-darwin.rs')
phase=sys.argv[1]
commands={'fetch':['cargo','fetch','--locked','--target','aarch64-apple-darwin'],'baseline':['cargo','build','--frozen','--target','aarch64-apple-darwin','--release','--bin','codex-app-server','--bin','codex-code-mode-host','-j','4'],'patched':['cargo','build','--frozen','--target','aarch64-apple-darwin','--release','--bin','codex-app-server','--bin','codex-code-mode-host','-j','4']}
commands['local-tests']=['cargo','test','--frozen','--release','--target','aarch64-apple-darwin','-p','codex-sandboxing','--lib','unreadable_globs_','-j','4','--','--test-threads=4']
commands['candidate2']=commands['patched']
commands['network-policy-tests']=['cargo','test','--frozen','--release','--target','aarch64-apple-darwin','-p','codex-network-proxy','--lib','evaluate_host_policy','-j','4','--','--test-threads=4']
commands['network-approval-tests']=['cargo','test','--frozen','--release','--target','aarch64-apple-darwin','-p','codex-core','--lib','tools::network_approval::tests','-j','4','--','--test-threads=4']
commands['network-constraints-tests']=['cargo','test','--frozen','--release','--target','aarch64-apple-darwin','-p','codex-core','--lib','config::network_proxy_spec::tests','-j','4','--','--test-threads=4']
cmd=commands[phase]
if phase != 'fetch':
 policy='(version 1)(allow default)(deny network*)(deny file-write* (require-not (require-any (subpath '+json.dumps(str(root))+') (literal "/dev/null"))))'
 cmd=['/usr/bin/sandbox-exec','-p',policy]+cmd
t=time.time()
with (root/'builds'/f'{phase}.log').open('w') as f:
 p=subprocess.run(cmd,cwd=root/'source/codex/codex-rs',env=env,stdout=f,stderr=subprocess.STDOUT)
r={'phase':phase,'command':cmd,'exit':p.returncode,'elapsed_seconds':time.time()-t,'environment':env}
(root/'builds'/f'{phase}.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='environment'}));sys.exit(p.returncode)
