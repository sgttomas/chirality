"""Behavioral tests of dependency queries and their observation boundaries."""
import json
from pathlib import Path
import subprocess
import sys

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent))
import cli


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()


@pytest.fixture
def repo(tmp_path, monkeypatch):
    git(tmp_path, 'init', '-q')
    git(tmp_path, 'config', 'user.email', 'fixture@example.com')
    git(tmp_path, 'config', 'user.name', 'Fixture')
    (tmp_path / 'project').mkdir()
    (tmp_path / '.keep').write_text('fixture')
    git(tmp_path, 'add', '.')
    git(tmp_path, 'commit', '-qm', 'initial')
    monkeypatch.chdir(tmp_path)
    return tmp_path


def put(repo, identifier, needs=(), **fields):
    path = repo / 'project' / 'execution' / identifier / 'deliverable.yaml'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(dict(id=identifier, needs=list(needs), **fields)))
    return path


def query(capsys, *args):
    code = cli.main(['--project', 'project', *args])
    return code, json.loads(capsys.readouterr().out)


def test_unknown_conditions_cycles_and_non_gating_are_not_completion(repo, capsys):
    put(repo, 'DEL-01-01', [{'from': 'DEL-01-02', 'condition': 'interface'},
                           {'from': 'DEL-01-02', 'condition': 'qualification', 'gating': False},
                           {'from': 'DEL-99-99', 'condition': 'future input'}])
    put(repo, 'DEL-01-02', [{'from': 'DEL-01-01', 'condition': 'mutual design'}])
    code, result = query(capsys, 'check')
    assert code == 0
    assert result['cycles'] == [['DEL-01-01', 'DEL-01-02']]
    assert len(result['needs']) == 4
    assert all(row['suitability'] == 'unknown' for row in result['needs'])
    assert len(result['unknown']) == 1
    assert result['basis']['revision'] == git(repo, 'rev-parse', 'HEAD')
    assert result['basis']['working_tree_changes']
    code, result = query(capsys, 'impact', 'DEL-01-01')
    assert result['affected'] == ['DEL-01-02']


def test_typed_targets_and_present_evidence_do_not_claim_satisfaction(repo, capsys):
    (repo / 'project' / 'interface.md').write_text('a stub')
    put(repo, 'DEL-01-01', [{'from': 'doc:interface.md', 'condition': 'correct interface',
                           'evidence': 'interface.md::contract'},
                          {'from': 'external:consumer', 'condition': 'provide schema',
                           'direction': 'downstream', 'gating': False},
                          {'from': 'package:PKG-02', 'condition': 'package input'}])
    code, result = query(capsys, 'neighborhood', 'DEL-01-01')
    assert code == 0
    assert len(result['outputs']) == 1
    assert len(result['upstream']) == 2
    assert result['upstream'][0]['supplier']['state'] == 'observed'
    assert result['upstream'][0]['suitability'] == 'unknown'
    assert 'no check executed' in result['upstream'][0]['evidence_fact']['meaning']


def test_touches_shared_relevance_and_unmapped_paths(repo, capsys):
    for identifier in ['DEL-01-01', 'DEL-01-02']:
        put(repo, identifier, code_paths=['src/**'])
    put(repo, 'DEL-01-03')
    (repo / 'project' / 'src').mkdir()
    (repo / 'project' / 'src' / 'a.py').write_text('old')
    git(repo, 'add', '.')
    git(repo, 'commit', '-qm', 'code')
    (repo / 'project' / 'src' / 'a.py').write_text('new')
    (repo / '.keep').write_text('unmapped')
    code, result = query(capsys, 'touches', 'HEAD')
    assert code == 0
    assert sorted(result['relevant']) == ['DEL-01-01', 'DEL-01-02']
    assert result['unknown_deliverables'] == ['DEL-01-03']
    assert result['unmapped_paths'] == ['.keep']


def test_dag_diff_tracks_conditions_and_gating_but_not_folder_moves(repo, capsys):
    original = put(repo, 'DEL-01-01', [{'from': 'external:vendor', 'condition': 'v1', 'gating': False}])
    git(repo, 'add', '.')
    git(repo, 'commit', '-qm', 'baseline')
    git(repo, 'tag', 'baseline')
    moved = repo / 'project' / 'execution' / 'PKG-01' / '1_Working' / 'DEL-01-01' / 'deliverable.yaml'
    moved.parent.mkdir(parents=True)
    original.rename(moved)
    code, result = query(capsys, 'dag-diff', 'baseline')
    assert code == 0 and result['added'] == result['removed'] == []
    data = yaml.safe_load(moved.read_text())
    data['needs'][0].update(condition='v2', gating=True)
    moved.write_text(yaml.safe_dump(data))
    code, result = query(capsys, 'dag-diff', 'baseline')
    assert result['added'][0]['condition'] == 'v2'
    assert result['added'][0]['gating'] is True
    assert result['removed'][0]['condition'] == 'v1'


def test_escaped_paths_and_symlinks_are_not_read(repo, capsys):
    put(repo, 'DEL-01-01', code_paths=['../private/**'])
    code, result = query(capsys, 'check')
    assert code == 2 and 'escapes' in result['errors'][0]
    target = repo / 'outside.yaml'
    target.write_text('id: DEL-02-02\nneeds: []\n')
    path = repo / 'project' / 'evil' / 'deliverable.yaml'
    path.parent.mkdir()
    path.symlink_to(target)
    code, result = query(capsys, 'check')
    assert code == 2 and any('contained regular file' in error for error in result['errors'])


def test_reference_symlink_is_unknown_without_reading_target(repo, capsys):
    outside = repo / 'private.txt'
    outside.write_text('private')
    (repo / 'project' / 'link.txt').symlink_to(outside)
    put(repo, 'DEL-01-01', [{'from': 'doc:link.txt', 'condition': 'input'}])
    code, result = query(capsys, 'check')
    assert code == 0
    assert result['needs'][0]['supplier']['state'] == 'unknown'


def test_duplicate_yaml_and_identities_fail_with_partial_results(repo, capsys):
    put(repo, 'DEL-01-01')
    duplicate = repo / 'project' / 'duplicate' / 'deliverable.yaml'
    duplicate.parent.mkdir()
    duplicate.write_text('id: DEL-01-01\nneeds: []\n')
    code, result = query(capsys, 'check')
    assert code == 2 and 'duplicate identity' in result['errors'][0]
    duplicate.write_text('id: DEL-01-02\nneeds: []\nneeds: []\n')
    code, result = query(capsys, 'check')
    assert code == 2 and 'duplicate or non-string YAML key' in result['errors'][0]
    assert result['deliverables'] == 1


def test_missing_project_or_identity_is_explicit(repo, capsys):
    code, result = query(capsys, 'neighborhood', 'DEL-01-01')
    assert code == 0 and result['state'] == 'unknown'
    code = cli.main(['--project', '../outside', 'check'])
    result = json.loads(capsys.readouterr().out)
    assert code == 2 and result['errors']
