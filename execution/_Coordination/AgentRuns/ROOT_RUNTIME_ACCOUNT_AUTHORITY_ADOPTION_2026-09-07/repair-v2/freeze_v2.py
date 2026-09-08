"""Verify preserved evidence and freeze the complete repaired candidate."""
from pathlib import Path
import gzip
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parents[5]
run = Path(__file__).resolve().parents[1]
original_manifest = run / 'OUTPUT_MANIFEST.json'
assert hashlib.sha256(original_manifest.read_bytes()).hexdigest() == \
    '7a4df3f1b9595ff9163dcc80d9362647e199541a527aa51259ca387463768afa'
for item in json.loads(original_manifest.read_text())['files']:
    if item['path'] in {
        'tools/validation/root_runtime_successors.py',
        'tools/validation/test_root_runtime_successors.py',
    }:
        continue
    raw = (root / item['path']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item['sha256'] and len(raw) == item['bytes']
preserved = {
    run / 'CANDIDATE_DIFF.patch.gz':
        '4f8ae520b4dc4a90a40a8507ccf4cea0de7e26354d79d297f57a882c71575ce9',
    run / 'review-v1/MANIFEST.json':
        '96fc52b9bb9425b1a2bdf3ed0048077f7d3d5aab6fb3d659bf47c3b1039b9522',
    run / 'review-v1/RETURN.md':
        'b6e97b0b2d941957245205b056557a718e86e8d5f776775ed9fe553ceee0ef74',
}
for path, expected in preserved.items():
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected

diff_path = run / 'CANDIDATE_DIFF_v2.patch.gz'
manifest_path = run / 'OUTPUT_MANIFEST_v2.json'
generated = {str(diff_path.relative_to(root)), str(manifest_path.relative_to(root))}
status = subprocess.check_output(
    ['git', '-C', str(root), 'status', '--porcelain=v1', '--untracked-files=all'],
    text=True).splitlines()
paths = sorted({line[3:] for line in status if line[3:] not in generated})
tracked = [path for path in paths if subprocess.run(
    ['git', '-C', str(root), 'ls-files', '--error-unmatch', path],
    capture_output=True).returncode == 0]
chunks = [subprocess.check_output(['git', '-C', str(root), 'diff', '--binary', '--', *tracked])]
for path in paths:
    if path in tracked:
        continue
    result = subprocess.run(['git', '-C', str(root), 'diff', '--no-index', '--binary',
                             '--', '/dev/null', path], capture_output=True)
    assert result.returncode in (0, 1)
    chunks.append(result.stdout)
with gzip.GzipFile(filename=str(diff_path), mode='wb', mtime=0) as stream:
    stream.write(b''.join(chunks))

all_paths = sorted(paths + [str(diff_path.relative_to(root))])
files = []
for path in all_paths:
    raw = (root / path).read_bytes()
    files.append({'path': path, 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
manifest = {
    'schema': 'root-runtime-account-authority-adoption-output/v2',
    'pathBase': 'repository root',
    'status': 'FROZEN_REPAIR_PASS_PENDING_FRESH_INDEPENDENT_REVIEW',
    'reviewV1Finding': 'P1 baseline fast-path account-supplement omission repaired',
    'manifestSelfHash': 'EXCLUDED_BY_CONTRACT',
    'candidateDiffScope': 'all changed paths except CANDIDATE_DIFF_v2.patch.gz and OUTPUT_MANIFEST_v2.json',
    'originalEvidencePreserved': True,
    'files': files,
}
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
print('FROZEN V2', len(files), 'files')
