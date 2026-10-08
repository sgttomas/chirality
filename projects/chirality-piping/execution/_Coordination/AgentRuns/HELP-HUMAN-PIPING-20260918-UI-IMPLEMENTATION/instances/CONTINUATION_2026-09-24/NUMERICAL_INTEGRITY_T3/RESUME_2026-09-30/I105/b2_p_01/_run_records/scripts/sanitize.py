"""I105: copy a text file into the records with placeholder paths only.
Usage: sanitize.py <src> <dst>
Machine paths become WT (the T3 host), APPWT (the App worktree), MAIN (the main checkout),
TMP (the system temp area) and HOME. A line over 4,000 bytes is cut to 1,000 bytes, followed by
its length and sha256 (the producer's cfg(test) prints). The prefixes are assembled from parts,
so this file's own copy in the records reads as written."""
import hashlib, re, sys
U, P = '/' + 'Users' + '/', '/' + 'private' + '/'
NAME = r'[^/\s"]+'
REPL = [
    (re.compile(re.escape(U) + NAME + '/dev/chirality-t3'), 'WT'),
    (re.compile(re.escape(U) + NAME + '/dev/chirality/' + re.escape('.' + 'claude' + '/' + 'work' + 'trees/') + NAME), 'APPWT'),
    (re.compile(re.escape(U) + NAME + '/dev/chirality'), 'MAIN'),
    (re.compile(re.escape(P) + r'(tmp|var)/[^\s"]*'), 'TMP'),
    (re.compile(re.escape(U) + NAME), 'HOME'),
]
out = []
for line in open(sys.argv[1], encoding='utf-8', errors='replace').read().splitlines():
    for r, s in REPL:
        line = r.sub(s, line)
    if len(line.encode()) > 4000:
        b = line.encode()
        line = b[:1000].decode('utf-8', 'ignore') + f' …[cut: {len(b)} bytes, sha256 {hashlib.sha256(b).hexdigest()}]'
    out.append(line)
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
