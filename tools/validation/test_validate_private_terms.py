import gzip
import os
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).with_name('validate_private_terms.py')
# Synthetic machine names, assembled at runtime so this file never carries a matchable form.
TERM = 'Fixture' + 'Laptop' + '-Pro'
OTHER = 'old' + 'box.lan' + '.home'
RUN = 'projects/x/execution/_Coordination/AgentRuns/RUN-1/'
HOST_ATTR = 'host' + 'name'


@pytest.fixture
def repo(tmp_path):
    def git(*args):
        return subprocess.run(['git', *args], cwd=tmp_path, check=True, capture_output=True, text=True)
    git('init', '-q')
    git('config', 'user.name', 'Fixture')
    git('config', 'user.email', 'fixture@example.invalid')
    old = tmp_path / RUN / 'old.md'
    old.parent.mkdir(parents=True)
    old.write_text(f'line one\npre-existing history on {TERM}\n')  # history is not re-scanned
    git('add', '.')
    git('commit', '-qm', 'base')
    return tmp_path, git, git('rev-parse', 'HEAD').stdout.strip()


def write(root, files):
    for name, content in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content if isinstance(content, bytes) else content.encode())


def run(repo, files, terms=(TERM, OTHER), extra=(), commit=True):
    root, git, base = repo
    write(root, files)
    git('add', '.')
    env = {k: v for k, v in os.environ.items() if k != 'PRIVATE_TERMS'}
    if terms:
        env['PRIVATE_TERMS'] = '\n'.join(terms)
    if commit:
        git('commit', '-qm', 'change')
        span = ['--base', base, '--head', 'HEAD']
    else:
        span = ['--staged']
    return subprocess.run([sys.executable, str(SCRIPT), *span, *extra], cwd=root, env=env,
                          capture_output=True, text=True)


def no_term_in(result):
    return all(t.lower() not in (result.stdout + result.stderr).lower() for t in (TERM, OTHER))


@pytest.mark.parametrize('form', [
    TERM,
    TERM.upper(),
    'Fixture' + '""' + 'Laptop' + '-Pro',          # split by quotes
    'Fix' + '[t]' + 'ure' + '[-]' + 'Lap' + 'top' + '\\-Pro',  # character classes and escapes
    'fixture laptop pro',                            # spaces
])
def test_term_in_any_form_blocks_without_printing_it(repo, form):
    result = run(repo, {'docs/notes.md': f'built on {form} today\n'})
    assert result.returncode == 1, result.stdout
    assert 'docs/notes.md:1: private term 1 (any form)' in result.stdout
    assert no_term_in(result)


def test_earlier_dotted_name_blocks(repo):
    result = run(repo, {RUN + 'screen.sh': 'PAT="old[.]box' + '[.]lan[.]home"\n'})
    assert result.returncode == 1
    assert 'private term 2' in result.stdout and no_term_in(result)


def test_gzipped_evidence_is_decompressed(repo):
    result = run(repo, {RUN + 'suite.xml.gz': gzip.compress(f'<x>{TERM}</x>\n'.encode())})
    assert result.returncode == 1
    assert 'suite.xml.gz:1: private term 1' in result.stdout


def test_modified_file_scans_added_lines_only(repo):
    result = run(repo, {RUN + 'old.md': f'line one\npre-existing history on {TERM}\nnew clean line\n'})
    assert result.returncode == 0, result.stdout
    result = run(repo, {RUN + 'old.md': f'line one\npre-existing history on {TERM}\nnew clean line\nnow {TERM}\n'})
    assert result.returncode == 1
    assert 'old.md:4: private term 1' in result.stdout


def test_junit_host_attribute_blocks_in_run_records_without_terms(repo):
    suite = f'<testsuites><testsuite name="pytest" {HOST_ATTR}="build-17.example">x</testsuite></testsuites>\n'
    result = run(repo, {RUN + 'py.xml': suite}, terms=())
    assert result.returncode == 1
    assert 'junit hostname attribute' in result.stdout
    assert 'NOTE: no private terms configured' in result.stdout


@pytest.mark.parametrize('value', ['', '<host>'])
def test_junit_placeholder_or_empty_host_passes(repo, value):
    suite = f'<testsuite name="pytest" {HOST_ATTR}="{value}">x</testsuite>\n'
    result = run(repo, {RUN + 'py.xml.gz': gzip.compress(suite.encode())}, terms=())
    assert result.returncode == 0, result.stdout


def test_junit_attribute_outside_run_records_passes(repo):
    suite = f'<testsuite name="pytest" {HOST_ATTR}="build-17.example">x</testsuite>\n'
    result = run(repo, {'tools/fixtures/py.xml': suite}, terms=())
    assert result.returncode == 0, result.stdout


def test_no_terms_passes_with_a_note(repo):
    result = run(repo, {'docs/notes.md': f'{TERM}\n'}, terms=())
    assert result.returncode == 0
    assert 'NOTE: no private terms configured' in result.stdout


def test_terms_file_and_staged_mode(repo, tmp_path_factory):
    terms = tmp_path_factory.mktemp('private') / 'terms.txt'
    terms.write_text(f'# names\n\n{TERM}\n')
    result = run(repo, {'docs/notes.md': f'{TERM}\n'}, terms=(), extra=['--terms-file', str(terms)], commit=False)
    assert result.returncode == 1
    assert 'docs/notes.md:1: private term 1' in result.stdout and no_term_in(result)


def test_short_terms_are_not_screened(repo):
    result = run(repo, {'docs/notes.md': 'a mac and a pc\n'}, terms=('mac', 'pc'))
    assert result.returncode == 0
    assert '2 term(s) shorter than 6' in result.stdout


def test_binary_files_are_skipped(repo):
    result = run(repo, {'docs/image.png': f'\x89PNG {TERM}'.encode()})
    assert result.returncode == 0, result.stdout
