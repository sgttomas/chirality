import hashlib,json,os,subprocess,shutil,time
from pathlib import Path
E=Path(__file__).resolve().parent
R=E.parents[1]
O=Path('/private/tmp/runtime-execution-20260906/supplier-candidate')
N=O/'candidate3'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def save(n,v): (E/n).write_text(json.dumps(v,indent=2)+'\n')
sm=json.loads((R/'SUPPLIER/BUILD/SOURCE_BEFORE.json').read_text())['source_files']
# Refuse any copied symlink resolving outside Candidate3 (source/git-local links included).
links=[]
for tree in ['source','toolchain','cache','target']:
 for base,dirs,files in os.walk(N/tree,followlinks=False):
  for n in dirs+files:
   p=Path(base)/n
   if p.is_symlink():
    resolved=p.resolve(); links.append({'path':str(p.relative_to(N)),'target':os.readlink(p),'resolved':str(resolved)})
    assert resolved.is_relative_to(N),str(p)
copied={n:sha(N/'source'/n) for n in sm};assert copied==sm
for n in sm:
 a=(O/'source/codex'/n).stat();b=(N/'source'/n).stat();assert (a.st_dev,a.st_ino)!=(b.st_dev,b.st_ino),n
ident={}
paths=['source/codex-rs/Cargo.lock','source/codex-rs/rust-toolchain.toml','toolchain/rustup/toolchains/1.95.0-aarch64-apple-darwin/bin/rustc','toolchain/rustup/toolchains/1.95.0-aarch64-apple-darwin/bin/cargo','cache/v8/librusty_v8_ptrcomp_sandbox_release_aarch64-apple-darwin.a.gz','cache/v8/src_binding_ptrcomp_sandbox_release_aarch64-apple-darwin.rs']
for n in paths:
 old=O/(n.replace('source/','source/codex/',1) if n.startswith('source/') else n)
 assert sha(old)==sha(N/n);ident[n]=sha(N/n)
prebuilt={}
for name in ['codex-app-server','codex-code-mode-host']:
 p=N/'target/aarch64-apple-darwin/release'/name;prebuilt[name]={'sha256':sha(p),'mtime_ns':p.stat().st_mtime_ns,'size':p.stat().st_size,'identity':'copied Candidate2 target only; NOT Candidate3 artifact'}
save('COPIED_BEFORE.json',{'source_files':copied,'dependency_identity':ident,'symlinks':links,'preexisting_target_outputs':prebuilt,'copy_mode':'APFS cp -cR independent inodes; no hardlinks back to original'})
print('prepared',len(copied),flush=True)
