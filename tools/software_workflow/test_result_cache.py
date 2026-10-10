"""Successful verification reuse follows inputs, command selection and environment."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

import yaml

spec = importlib.util.spec_from_file_location('result_cache', Path(__file__).with_name('result_cache.py'))
cache = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cache)
ROOT = Path(__file__).resolve().parents[2]


def test_input_key_changes_for_code_tests_fixtures_commands_and_image(tmp_path):
    def git(*args):
        subprocess.run(['git', '-C', str(tmp_path), *args], check=True, capture_output=True)
    git('init', '-q'); git('config', 'user.email', 'test@example.invalid'); git('config', 'user.name', 'Fixture')
    def commit(path, content):
        p = tmp_path / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content)
        git('add', '.'); git('commit', '-qm', 'fixture')
    def key(commands=None, environment=None):
        return cache.fingerprint(tmp_path, 'numerical', commands or ['cargo test'], environment or {'image': 'v1'})
    commit('projects/chirality-piping/core/lib.rs', 'one')
    first = key()
    commit('projects/chirality-piping/execution/PKG-01/DEL-01-01/Design/note.md', 'prose')
    assert key() == first
    for path in ['projects/chirality-piping/core/lib.rs', 'projects/chirality-piping/tests/test_one.py',
                 'projects/chirality-piping/fixtures/handoff/one.json', '.github/workflows/piping-desktop-e2e.yml']:
        before = key(); commit(path, 'new'); assert key() != before
    assert key(['cargo test --lib']) != key()
    assert key(environment={'image': 'v2'}) != key()
    git('rm', 'projects/chirality-piping/core/lib.rs'); git('commit', '-qm', 'delete')
    assert key() != first


def test_reuse_rejects_missing_wrong_or_failed_record(tmp_path):
    record = tmp_path / 'result.json'
    env = {**os.environ, 'RESULT_KEY': 'expected', 'GITHUB_STEP_SUMMARY': str(tmp_path / 'summary')}
    command = [sys.executable, str(Path(cache.__file__)), 'reuse', '--suite', 'numerical', '--record', str(record)]
    for data in [None, {'key': 'wrong', 'conclusion': 'success'}, {'key': 'expected', 'conclusion': 'failure'}]:
        if data is not None: record.write_text(json.dumps(data))
        assert subprocess.run(command, env=env, capture_output=True).returncode != 0
    record.write_text(json.dumps({'key': 'expected', 'conclusion': 'success', 'head': 'original', 'run': 'https://github.com/example/repo/actions/runs/1'}))
    result = subprocess.run(command, env=env, capture_output=True, text=True)
    assert result.returncode == 0
    assert 'No tests executed' in result.stdout


def test_workflow_saves_only_success_and_never_restores_partial_keys():
    workflow = yaml.load((ROOT / '.github/workflows/piping-desktop-e2e.yml').read_text(), Loader=yaml.BaseLoader)
    for job in ['product', 'numerical']:
        steps = workflow['jobs'][job]['steps']
        restore = next(s for s in steps if s.get('uses') == 'actions/cache/restore@v4')
        assert restore['if'] == "github.event_name == 'pull_request'"
        assert 'restore-keys' not in restore['with']
        save = next(s for s in steps if s.get('uses') == 'actions/cache/save@v4')
        assert 'success()' in save['if']
        assert save['with']['key'] == restore['with']['key']
        for name in ['Locked Cargo numerical suite'] if job == 'numerical' else ['Production build', 'Core browser journey and save/reopen']:
            step = next(s for s in steps if s.get('name') == name)
            assert step['if'] == "steps.verified.outputs.cache-hit != 'true'"
