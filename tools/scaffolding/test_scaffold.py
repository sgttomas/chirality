import os
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent


def test_created_manifest_and_no_overwrite(tmp_path):
    args=['zsh',str(HERE/'scaffold_deliverable.sh'),str(tmp_path),'DEL-01','Test','--memory']
    first=subprocess.run(args,text=True,capture_output=True,check=True)
    created=[line.split(': ',1)[1] for line in first.stdout.splitlines() if line.startswith('CREATED_PATH:')]
    assert len(created)==7
    created=[p for p in created if Path(p).is_file()]
    assert len(created)==6
    assert (tmp_path/"DEL-01_Test"/"MEMORY.md").is_file()
    assert not (tmp_path/"DEL-01_Test"/"_MEMORY.md").exists()
    assert all(Path(p).is_file() for p in created)
    for p in created:Path(p).write_text('human content')
    second=subprocess.run(args,text=True,capture_output=True,check=True)
    assert 'CREATED_PATH:' not in second.stdout
    assert all(Path(p).read_text()=='human content' for p in created)


def test_package_rerun_and_path_boundary(tmp_path):
    args=['zsh',str(HERE/'scaffold_package.sh'),str(tmp_path),'PKG-01','Test']
    assert subprocess.run(args,text=True,capture_output=True).returncode==0
    assert 'CREATED_PATH:' not in subprocess.run(args,text=True,capture_output=True).stdout
    bad=['zsh',str(HERE/'scaffold_deliverable.sh'),str(tmp_path),'../../outside','Test']
    assert subprocess.run(bad,capture_output=True).returncode==2


def test_legacy_memory_requires_explicit_consolidation(tmp_path):
    target=tmp_path/'DEL-01_Test'
    target.mkdir()
    legacy=target/'_MEMORY.md'
    legacy.write_text('retained human context')
    result=subprocess.run(['zsh',str(HERE/'scaffold_deliverable.sh'),str(tmp_path),'DEL-01','Test','--memory'],text=True,capture_output=True)
    assert result.returncode==2
    assert legacy.read_text()=='retained human context'
    assert not (target/'MEMORY.md').exists()
    assert set(target.iterdir())=={legacy}


def _snapshot(tmp_path, root):
    # Pin `date` so runs land in the same minute deterministically.
    stub=tmp_path/'bin'
    stub.mkdir(exist_ok=True)
    (stub/'date').write_text('#!/bin/sh\necho 2026-01-01_1200\n')
    (stub/'date').chmod(0o755)
    env=dict(os.environ,PATH=f"{stub}{os.pathsep}{os.environ['PATH']}")
    return subprocess.run(['zsh',str(HERE/'create_snapshot_folder.sh'),str(root),'REV','DEL-01-01'],text=True,capture_output=True,env=env)


def test_snapshot_folder_is_never_reused(tmp_path):
    root=tmp_path/'_Reviews'
    first=_snapshot(tmp_path,root)
    assert first.returncode==0
    assert first.stdout.strip()==f"{root}/REV_DEL-01-01_2026-01-01_1200"
    (Path(first.stdout.strip())/'Decision_Log.md').write_text('frozen')
    second=_snapshot(tmp_path,root)
    assert second.returncode==0
    assert second.stdout.strip()==f"{root}/REV_DEL-01-01_2026-01-01_1200_02"
    assert list(Path(second.stdout.strip()).iterdir())==[]
    assert (Path(first.stdout.strip())/'Decision_Log.md').read_text()=='frozen'


def test_snapshot_folder_fails_rather_than_reuse(tmp_path):
    root=tmp_path/'_Reviews'
    base=root/'REV_DEL-01-01_2026-01-01_1200'
    base.mkdir(parents=True)
    for n in range(2,100):
        Path(f"{base}_{n:02d}").mkdir()
    result=_snapshot(tmp_path,root)
    assert result.returncode==1
    assert result.stdout==''
    assert 'refusing to reuse' in result.stderr
