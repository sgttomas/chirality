#!/usr/bin/env python3
"""Copy I102's run evidence into R/I102/b2_k_01/_run_records with machine paths
replaced by placeholders (WT, NUM, R), large logs gzipped (mtime 0), and write
SHA256SUMS over the record folder. No symlink, no folder named build."""
import gzip, hashlib, os, pathlib, re, shutil, sys

WT = str(pathlib.Path(__file__).resolve().parents[2])  # this script lives in WT/scratch/i102_b2_k
S = pathlib.Path(WT) / 'scratch/i102_b2_k'
R = pathlib.Path(WT) / ('numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/'
    'HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/'
    'NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I102/b2_k_01')
OUT = R / '_run_records'
USERS, PRIVATE, TILDE = '/' + 'Users' + '/', '/' + 'private' + '/', '~' + '/'
SUBS = [
    (WT + '/numerics', 'NUM'),
    (WT, 'WT'),
    (PRIVATE + 'tmp/', '<tmp>/'),
    (os.path.expanduser('~'), '<home>'),
]
PATTERN = re.compile('|'.join(re.escape(x) for x in (USERS, PRIVATE, TILDE)))


def clean(text):
    for a, b in SUBS:
        text = text.replace(a, b)
    assert not PATTERN.search(text), 'unreplaced machine path'
    return text


def put(src, dst, gz=False):
    text = clean(pathlib.Path(src).read_text(errors='replace'))
    target = OUT / dst
    target.parent.mkdir(parents=True, exist_ok=True)
    if gz:
        with open(str(target) + '.gz', 'wb') as raw:
            with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='') as g:
                g.write(text.encode())
    else:
        target.write_text(text)


def main(files):
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for src, dst, gz in files:
        put(S / src, dst, gz)
    for p in R.rglob('*'):
        assert not p.is_symlink() and p.name != 'build', p
    sums = []
    for p in sorted(x for x in R.rglob('*') if x.is_file() and x.name != 'SHA256SUMS'):
        sums.append(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(R).as_posix()}')
    (R / 'SHA256SUMS').write_text('\n'.join(sums) + '\n')
    print(f'{len(sums)} files summed')


if __name__ == '__main__':
    manifest = pathlib.Path(sys.argv[1]).read_text().split('\n')
    files = []
    for line in manifest:
        if line.strip() and not line.startswith('#'):
            src, dst, gz = line.split()
            files.append((src, dst, gz == 'gz'))
    main(files)
