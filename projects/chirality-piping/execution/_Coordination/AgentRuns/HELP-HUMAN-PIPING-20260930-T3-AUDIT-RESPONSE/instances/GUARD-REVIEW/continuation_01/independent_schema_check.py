"""Independent reviewer argv witnesses; all files and live capabilities faked."""
from contextlib import ExitStack
import importlib.util
import io
import json
from pathlib import Path
import sys
from unittest.mock import patch

HERE=Path(__file__).resolve().parent
RUN=HERE.parents[2]
FORBIDDEN=('os.kill','os.killpg','os.fork','os.execvpe','os.execve','os.setsid',
           'os.setpgid','os._exit','fcntl.flock','subprocess.Popen','ctypes.CDLL',
           'socket.socketpair','signal.signal','time.sleep','os.getsid','os.getpgid',
           'os.getpgrp','os.getpid','os.getuid','os.geteuid')
def blocked(*args,**kwargs): raise AssertionError('LIVE CAPABILITY FORBIDDEN')
with ExitStack() as fence:
 for target in FORBIDDEN:fence.enter_context(patch(target,side_effect=blocked))
 spec=importlib.util.spec_from_file_location('reviewer_guard_v2',RUN/'tools/host_guard_v2.py')
 guard=importlib.util.module_from_spec(spec);sys.modules[spec.name]=guard;spec.loader.exec_module(guard)
binary=b'reviewer fake executable'
flags=['--offline','--locked','-j','1']
cases=[
 ('valid build',['/fake/cargo','build',*flags],True),
 ('original forwarded controls',['/fake/cargo','run','--jobs','8','--',*flags],False),
 ('original cargo selector',['/fake/cargo','+stable','build',*flags],False),
 ('original rustc selector',['/fake/rustc','+stable','input.rs'],False),
 ('valid canonical cargo selector',['/fake/cargo','+1.97.1','build',*flags],True),
 ('valid canonical rustc selector',['/fake/rustc','+1.97.1','input.rs'],True),
 ('duplicate same jobs',['/fake/cargo','build',*flags,'--jobs=1'],False),
 ('conflicting jobs alias',['/fake/cargo','build',*flags,'-j8'],False),
 ('jobs in compiler tail',['/fake/cargo','rustc','--offline','--locked','--','-j','1'],False),
 ('offline in program tail',['/fake/cargo','run','--locked','-j','1','--','--offline'],False),
 ('locked consumed as package operand',['/fake/cargo','build','--offline','--package','--locked','-j','1'],False),
 ('jobs-looking feature operand',['/fake/cargo','build','--offline','--locked','--features=-j1'],False),
 ('wrong jobs attached',['/fake/cargo','build','--offline','--locked','--jobs=01'],False),
 ('valid long jobs',['/fake/cargo','build','--offline','--locked','--jobs=1'],True),
 ('valid short jobs',['/fake/cargo','check','--offline','--locked','-j1'],True),
 ('selector after subcommand',['/fake/cargo','build','+stable',*flags],False),
 ('duplicate canonical selector',['/fake/cargo','+1.97.1','+1.97.1','build',*flags],False),
 ('native-triple selector outside grammar',['/fake/cargo','+1.97.1-aarch64-apple-darwin','build',*flags],False),
 ('direct rustc path no selector',['/fake/rustc','input.rs','--emit=llvm-ir'],True),
 ('rustc second selector',['/fake/rustc','+1.97.1','+stable','input.rs'],False),
 ('cargo compiler forwarding',['/fake/cargo','rustc','--manifest-path','/fake/Cargo.toml','--lib',*flags,'--','--emit=llvm-ir','-C','opt-level=0'],True),
 ('build forwarding outside grammar',['/fake/cargo','build',*flags,'--','-C','opt-level=0'],False),
 ('forwarded literal is not proxy selector',['/fake/cargo','run',*flags,'--','+stable'],True),
 ('config override refused',['/fake/cargo','build',*flags,'--config','build.jobs=8'],False),
]
results=[]
with ExitStack() as fence:
 for target in FORBIDDEN:fence.enter_context(patch(target,side_effect=blocked))
 fence.enter_context(patch.object(Path,'is_dir',return_value=True))
 for name,argv,expected in cases:
  job={'job_id':'review-v2','run_id':guard.RUN_ID,'candidate_sha':'a'*40,
       'kind':'compile','containment':'inherited-group','cwd':'/fake','command':argv,
       'env':{'RUSTUP_TOOLCHAIN':'1.97.1','RUSTUP_AUTO_INSTALL':'0','CARGO_INCREMENTAL':'0',
              'CARGO_BUILD_JOBS':'1','RUST_TEST_THREADS':'1'},
       'input_hashes':{argv[0]:guard.hashlib.sha256(binary).hexdigest()},
       'limits':{'cap_bytes':128*guard.MIB,'allowance_bytes':64*guard.MIB,
                 'disk_write_budget_bytes':64*guard.MIB,'disk_reserve_bytes':guard.GIB,'max_seconds':8}}
  raw=json.dumps(job).encode()
  def fake_open(path,mode):
   assert mode=='rb'
   assert str(path) in ('/fake/job.json',argv[0])
   return io.BytesIO(raw if str(path)=='/fake/job.json' else binary)
  with patch('builtins.open',side_effect=fake_open):
   try: guard.read_job(Path('/fake/job.json'));actual=True;reason=None
   except guard.Refusal as exc:actual=False;reason=str(exc)
  results.append({'name':name,'argv':argv,'expected_accept':expected,'actual_accept':actual,'reason':reason,'matches':actual==expected})
print(json.dumps({'source_sha256':guard.hashlib.sha256((RUN/'tools/host_guard_v2.py').read_bytes()).hexdigest(),
 'live_capabilities':'blocked','fake_files_only':True,'cases':results,'all_match':all(r['matches'] for r in results)},indent=2))
assert all(r['matches'] for r in results)
