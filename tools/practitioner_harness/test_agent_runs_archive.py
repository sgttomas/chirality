"""Archive resolver contracts (D-GOV-45) and live archive-index integrity."""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest

import agent_runs_archive
from agent_runs_archive import archive_tag

LIVE_REPO = Path(__file__).resolve().parents[2]
INDEXES = sorted(p for pattern in agent_runs_archive.INDEX_GLOBS for p in LIVE_REPO.glob(pattern))


def test_resolves_archived_runs_inner_paths_and_files(tmp_path):
    index = tmp_path / 'projects/p/execution/_Coordination/AgentRuns/ARCHIVE_INDEX.json'
    index.parent.mkdir(parents=True)
    run = 'projects/p/execution/_Coordination/AgentRuns/OLD-RUN'
    kept_binary = 'projects/p/execution/_Coordination/AgentRuns/ACTIVE/trace.zip'
    index.write_text(json.dumps({'archives': [{'tag': 'archive/t', 'runs': [run], 'files': [kept_binary]}]}))
    agent_runs_archive._entries.cache_clear()
    assert archive_tag(tmp_path, run) == 'archive/t'
    assert archive_tag(tmp_path, run + '/nested/RESULT.md') == 'archive/t'
    assert archive_tag(tmp_path, tmp_path / run / 'x.json') == 'archive/t'
    assert archive_tag(tmp_path, kept_binary) == 'archive/t'
    for other in ['projects/p/execution/_Coordination/AgentRuns/OLD-RUN-2/x.md',
                  'projects/p/execution/_Coordination/AgentRuns/ACTIVE/other.zip',
                  run + '/../ELSEWHERE/x.md', '/etc/passwd']:
        assert archive_tag(tmp_path, other) is None


def test_index_entries_outside_run_records_never_resolve(tmp_path):
    index = tmp_path / 'execution/_Coordination/AgentRuns/ARCHIVE_INDEX.json'
    index.parent.mkdir(parents=True)
    index.write_text(json.dumps({'archives': [{'tag': 'archive/t', 'runs': [
        'docs', 'execution/PKG-01', 'execution/_Coordination/AgentRuns/../../PKG-01', 'execution/_Coordination/AgentRuns/'],
        'files': ['execution/_harness/root_guards.yaml', 'execution/_Coordination/AgentRuns/R/t.zip']}]}))
    agent_runs_archive._entries.cache_clear()
    for path in ['docs/SPEC.md', 'execution/PKG-01/x.md', 'execution/_harness/root_guards.yaml',
                 'execution/_Coordination/AgentRuns/OTHER/x.md']:
        assert archive_tag(tmp_path, path) is None, path
    assert archive_tag(tmp_path, 'execution/_Coordination/AgentRuns/R/t.zip') == 'archive/t'


@pytest.mark.skipif(not INDEXES and os.environ.get('CHIRALITY_REQUIRE_LIVE_TESTS') != '1',
                    reason='no live archive index')
def test_live_archive_indexes_are_held_by_their_tags_and_no_longer_tracked():
    assert INDEXES, 'live archive indexes are required'
    for index in INDEXES:
        data = json.loads(index.read_text())
        assert data['schema'] == 'chirality-agent-runs-archive-index/v1'
        for archive in data['archives']:
            commit = subprocess.check_output(
                ['git', '-C', str(LIVE_REPO), 'rev-parse', '--verify', archive['tag'] + '^{commit}'], text=True).strip()
            assert commit == archive['commit'], f"{archive['tag']} moved"
            paths = archive['runs'] + archive['files']
            for chunk in range(0, len(paths), 300):
                listed = subprocess.check_output(
                    ['git', '-C', str(LIVE_REPO), 'ls-tree', '--name-only', commit, '--', *paths[chunk:chunk + 300]],
                    text=True).split('\n')
                missing = set(paths[chunk:chunk + 300]) - set(listed)
                assert not missing, f'not held by {archive["tag"]}: {sorted(missing)[:3]}'
            for chunk in range(0, len(paths), 300):
                tracked = subprocess.check_output(
                    ['git', '-C', str(LIVE_REPO), 'ls-files', '--', *paths[chunk:chunk + 300]], text=True)
                assert not tracked, f'archived path still tracked: {tracked.splitlines()[:3]}'
