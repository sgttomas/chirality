"""Freeze the exact non-generated candidate delta and complete path/hash manifest."""
from pathlib import Path
import hashlib
import gzip
import json
import subprocess

root = Path(__file__).resolve().parents[4]
out = Path(__file__).resolve().parent
generated = {
    str((out / 'CANDIDATE_DIFF.patch.gz').relative_to(root)),
    str((out / 'OUTPUT_MANIFEST.json').relative_to(root)),
}
status = subprocess.check_output(
    ['git', '-C', str(root), 'status', '--porcelain=v1', '--untracked-files=all'],
    text=True).splitlines()
paths = sorted({line[3:] for line in status if line[3:] not in generated})
chunks = [subprocess.check_output(['git', '-C', str(root), 'diff', '--binary', '--',
                                   *[path for path in paths
                                     if subprocess.run(['git', '-C', str(root), 'ls-files',
                                                        '--error-unmatch', path],
                                                       capture_output=True).returncode == 0]])]
for path in paths:
    if subprocess.run(['git', '-C', str(root), 'ls-files', '--error-unmatch', path],
                      capture_output=True).returncode:
        result = subprocess.run(['git', '-C', str(root), 'diff', '--no-index', '--binary',
                                 '--', '/dev/null', path], capture_output=True)
        if result.returncode not in (0, 1):
            raise SystemExit(result.returncode)
        chunks.append(result.stdout)
with gzip.GzipFile(filename=str(out / 'CANDIDATE_DIFF.patch.gz'), mode='wb', mtime=0) as stream:
    stream.write(b''.join(chunks))

all_paths = sorted(paths + [str((out / 'CANDIDATE_DIFF.patch.gz').relative_to(root))])
files = []
for path in all_paths:
    raw = (root / path).read_bytes()
    files.append({'path': path, 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
manifest = {
    'schema': 'root-runtime-account-authority-adoption-output/v1',
    'pathBase': 'repository root',
    'status': 'FROZEN_AUTHOR_PASS_PENDING_INDEPENDENT_REVIEW',
    'initialHead': 'c3e9ab0f8e49314befc1fc81a9e01346641a7344',
    'prBaseRecorded': 'd4b8a8cec2e4d3c636740cb97a27fe3b1a3ef327',
    'manifestSelfHash': 'EXCLUDED_BY_CONTRACT',
    'candidateDiffScope': 'all changed paths except CANDIDATE_DIFF.patch.gz and OUTPUT_MANIFEST.json',
    'files': files,
}
(out / 'OUTPUT_MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n')
print('FROZEN', len(files), 'files')
