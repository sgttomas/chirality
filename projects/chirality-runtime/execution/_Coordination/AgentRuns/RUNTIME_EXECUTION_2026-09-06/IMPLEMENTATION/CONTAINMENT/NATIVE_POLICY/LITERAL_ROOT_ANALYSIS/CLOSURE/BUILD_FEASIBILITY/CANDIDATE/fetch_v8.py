from pathlib import Path
import urllib.request,hashlib,json
root=Path('/private/tmp/runtime-execution-20260906/supplier-candidate');out=root/'cache/v8';out.mkdir(parents=True,exist_ok=True)
base='https://github.com/openai/codex/releases/download/rusty-v8-v150.4.0/'
names=['librusty_v8_ptrcomp_sandbox_release_aarch64-apple-darwin.a.gz','src_binding_ptrcomp_sandbox_release_aarch64-apple-darwin.rs']
manifest='rusty_v8_ptrcomp_sandbox_release_aarch64-apple-darwin.sha256'
checks=urllib.request.urlopen(base+manifest,timeout=60).read();(out/manifest).write_bytes(checks)
parsed={line.split()[1].lstrip('*'):line.split()[0] for line in checks.decode().splitlines() if line.strip()}
if set(parsed)!=set(names):raise RuntimeError('Unexpected V8 checksum manifest members')
records=[]
for name in names:
 path=out/name;h=hashlib.sha256()
 with urllib.request.urlopen(base+name,timeout=120) as src,path.open('wb') as target:
  while chunk:=src.read(1024*1024):h.update(chunk);target.write(chunk)
 if h.hexdigest()!=parsed[name]:raise RuntimeError('V8 checksum mismatch')
 records.append({'url':base+name,'sha256':h.hexdigest(),'bytes':path.stat().st_size})
(out/'VERIFIED.json').write_text(json.dumps({'manifest_url':base+manifest,'manifest_sha256':hashlib.sha256(checks).hexdigest(),'files':records},indent=2)+'\n');print(json.dumps(records))
