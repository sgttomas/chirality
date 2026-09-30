#!/usr/bin/env python3
"""Read-only source/binding verification. Never invokes a Rust tool or provider."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

root=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
run=root/'projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE'
binding=json.loads((run/'RUNTIME_BINDING.json').read_text())
manifest_path=run/'runtime_setup/01_native_rust/A1_SOURCE_SNAPSHOT.json'
manifest=json.loads(manifest_path.read_text())
runtime=Path(tempfile.gettempdir())/binding['runtime_directory_name']
snapshot=runtime/manifest['runtime_relative_path']
sha=lambda b:hashlib.sha256(b).hexdigest()
expected={f['path'] for f in manifest['files']}
actual={str(p.relative_to(snapshot)) for p in snapshot.rglob('*') if p.is_file()}
assert actual==expected and len(actual)==36
assert manifest['source_commit']=='3bddc2b05f6106e969c7cf43373b230845c7cc66'
checked=[]
for f in manifest['files']:
    snapshot_hash=sha((snapshot/f['path']).read_bytes())
    source_hash=sha(subprocess.check_output(['git','show',manifest['source_commit']+':'+f['path']],cwd=root))
    working_hash=sha((root/f['path']).read_bytes())
    assert snapshot_hash==source_hash==working_hash==f['sha256'],f['path']
    checked.append(dict(path=f['path'],sha256=snapshot_hash,snapshot_matches_frozen_git_and_working_bytes=True))
tools=[]
for name in ['cargo','rustc']:
    rel='rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/'+name
    p=runtime/rel
    tools.append(dict(runtime_relative_path=rel,size_bytes=p.stat().st_size,sha256=sha(p.read_bytes()),invoked=False))
result=dict(status='PASS',actual_coordination_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),
            authority_coordination_commit='53a7bad25fef1e1ddfe1a9df21688279f823aaf3',
            frozen_source_commit=manifest['source_commit'],runtime_directory_name=binding['runtime_directory_name'],
            runtime_resolution='Path(tempfile.gettempdir()) / runtime_directory_name',
            snapshot_manifest_sha256=sha(manifest_path.read_bytes()),binding_sha256=sha((run/'RUNTIME_BINDING.json').read_bytes()),
            setup_sha256=sha((run/'runtime_setup/01_native_rust/SETUP.json').read_bytes()),
            file_set_exact=True,file_count=36,files=checked,native_toolchain_file_hashes=tools,
            toolchain_version_basis='SETUP.json prior installation record; no Rust invocation performed',
            snapshot_written=False,provider_query=False)
print(json.dumps(result,indent=2))
