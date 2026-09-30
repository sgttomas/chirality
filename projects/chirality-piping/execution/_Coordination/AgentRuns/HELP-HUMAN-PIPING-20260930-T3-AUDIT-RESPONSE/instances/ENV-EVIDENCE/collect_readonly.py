"""One-shot read-only inventory; writes only adjacent evidence; no guard/kill/build/install."""
import datetime, hashlib, importlib.metadata as md, json, os, pathlib, platform, shutil, subprocess, sys
ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'], text=True).strip())
OUT=pathlib.Path(__file__).resolve().parent
P=ROOT/'projects/chirality-piping'
env=dict(os.environ, RUSTUP_AUTO_INSTALL='0', PYTHONDONTWRITEBYTECODE='1', PIP_DISABLE_PIP_VERSION_CHECK='1', GIT_OPTIONAL_LOCKS='0')
rows=[]
def portable(s):
    return (s.replace(str(ROOT),'<REPO_ROOT>').replace(str(pathlib.Path.home()),'<USER_HOME>')
            .replace(sys.prefix,'<PYTHON_PREFIX>').replace('/opt/homebrew','<NODE_PREFIX>')
            .replace('/Library/Developer/CommandLineTools','<CLT_ROOT>')
            .replace('/System/Volumes/Data','<DATA_VOLUME>').replace('/private/tmp','<TEMP_ROOT>'))
def run(label,args,extra=None,filter_process=False):
    stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        p=subprocess.run(args,cwd=ROOT,env=dict(env,**(extra or {})),text=True,capture_output=True)
        stdout=p.stdout
        if filter_process and p.returncode==0:
            names={'cargo','rustc','rustup','clang','cc','make','python','python3','node','npm','memguard.sh','pytest'}
            stdout='\n'.join(line for line in stdout.splitlines() if line.startswith('  PID') or any(pathlib.Path(tok).name in names for tok in line.split()))+'\n'
        row={'label':label,'utc':stamp,'argv':[portable(a) for a in args],'environment_overrides':dict(RUSTUP_AUTO_INSTALL='0',PYTHONDONTWRITEBYTECODE='1',PIP_DISABLE_PIP_VERSION_CHECK='1',GIT_OPTIONAL_LOCKS='0',**(extra or {})), 'exit_code':p.returncode, 'stdout':portable(stdout),'stderr':portable(p.stderr),'stdout_raw_sha256':hashlib.sha256(p.stdout.encode()).hexdigest(),'stderr_raw_sha256':hashlib.sha256(p.stderr.encode()).hexdigest()}
        if filter_process: row['scope']='Only relevant executable names retained; no argument strings collected.'
    except OSError as exc:
        row={'label':label,'utc':stamp,'argv':args,'unavailable':str(exc)}
    rows.append(row)
    print(label, json.dumps({k:row[k] for k in ('exit_code','stdout','stderr','unavailable') if k in row}))
    (OUT/'observations.json').write_text(json.dumps(rows,indent=2)+'\n')
run('head',['git','rev-parse','HEAD'])
run('tree',['git','rev-parse','HEAD^{tree}'])
run('platform',['uname','-smr'])
run('macos',['sw_vers'])
run('memory_pressure',['memory_pressure','-Q'])
run('vm_stat',['vm_stat'])
run('physical_memory',['sysctl','-n','hw.memsize'])
run('logical_cpus',['sysctl','-n','hw.logicalcpu'])
run('swap',['sysctl','vm.swapusage'])
run('pressure_level',['sysctl','kern.memorystatus_vm_pressure_level'])
run('disk',['df','-k',str(ROOT),'/private/tmp'])
run('own_process',['ps','-p',str(os.getpid()),'-o','pid,ppid,pgid,sess,lstart,rss,comm'])
run('relevant_processes',['ps','-U',str(os.getuid()),'-o','pid,ppid,pgid,sess,lstart,rss,comm'],filter_process=True)
run('toolchains',['rustup','toolchain','list'])
run('pinned_rustc',['rustc','--version','--verbose'],{'RUSTUP_TOOLCHAIN':'1.97.1'})
run('pinned_cargo',['cargo','--version'],{'RUSTUP_TOOLCHAIN':'1.97.1'})
run('default_rustc',['rustc','--version','--verbose'])
run('default_cargo',['cargo','--version'])
run('installed_targets',['rustup','target','list','--installed'],{'RUSTUP_TOOLCHAIN':'1.97.1'})
run('clang',['clang','--version'])
run('sdk',['xcrun','--show-sdk-path'])
run('node',['node','--version'])
run('npm',['npm','--version'])
run('python',['python3','-B','--version'])
packages={}
for name in ['pytest','pytest-xdist','numpy','scipy','mpmath','sympy','jsonschema','pydantic','pip','setuptools']:
    try: packages[name]=md.version(name)
    except md.PackageNotFoundError: packages[name]=None
paths=['.venv','venv','node_modules','apps/desktop/node_modules','core/solver/frame_kernel/target','core/solver/performance_harness/target','validation/benchmarks/numerical_robustness/target']
checks=[{'path':'projects/chirality-piping/'+p,'exists':(P/p).exists(),'is_dir':(P/p).is_dir()} for p in paths]
for p in ['.claude/t3','.claude/worktrees/swbpipe-control-layer-8a41be/.claude/t3','.claude/worktrees/swbpipe-control-layer-8a41be/projects/chirality-piping/.venv','.venv']:
    checks.append({'path':p,'exists':(ROOT/p).exists(),'is_dir':(ROOT/p).is_dir()})
data={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python_executable':portable(sys.executable),'python_version':platform.python_version(),'prefix':portable(sys.prefix),'base_prefix':portable(sys.base_prefix),'active_venv':sys.prefix!=sys.base_prefix,'relevant_packages_metadata_only':packages,'command_paths':{name:portable(shutil.which(name)) if shutil.which(name) else None for name in ['python3','python','node','npm','cargo','rustc','rustup','clang','cc','cmake','make','ninja','pkg-config','memory_pressure','vm_stat','sysctl','ps','pgrep','df','xcrun']},'path_checks':checks,'scope':'Exact project-owned runtime paths only; no whole-home or other-worktree scan.'}
(OUT/'runtime_inventory.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
