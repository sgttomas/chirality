"""I105 J0b, item 3: T2's old text and old digests in every file b2 adds or changes over main (ec5d397359..e582b61f9e),
read at b2's head and at the merged working tree. Forms: the plain text and three fragments; JSON string values
decoded (escapes resolved); Rust/TS text with line continuations removed; the 34 old digests (T2's commit 11a026b628
and the U3 package's radius_sweep.txt); the SHA-256 of the old text (raw and JSON-quoted).
Usage: t2_search.py <repo> <files list> <old hex list...>"""
import hashlib, json, re, subprocess, sys
repo, flist, *hexfiles = sys.argv[1:]
OLD = "Pressure thrust and pressure stress retain the existing preview formulation and capability qualifications; pressure formulation qualification remains open."
FRAGS = [OLD, "retain the existing preview formulation", "pressure formulation qualification remains open", "Pressure thrust and pressure stress"]
hexes = sorted({h.strip() for f in hexfiles for h in open(f) if re.fullmatch(r'[0-9a-f]{64}', h.strip())})
hashed = {hashlib.sha256(OLD.encode()).hexdigest(): 'sha256(old text)', hashlib.sha256(json.dumps(OLD).encode()).hexdigest(): 'sha256(json(old text))'}
def strings(v):
    if isinstance(v, str): yield v
    elif isinstance(v, dict):
        for k, x in v.items(): yield k; yield from strings(x)
    elif isinstance(v, list):
        for x in v: yield from strings(x)
files = [l.strip() for l in open(flist) if l.strip()]
hits = []
for rev in ('e582b61f9e', 'WORKTREE'):
    for f in files:
        if rev == 'WORKTREE':
            try: data = open(f'{repo}/{f}', 'rb').read()
            except FileNotFoundError: continue
        else:
            r = subprocess.run(['git', '-C', repo, 'show', f'{rev}:{f}'], capture_output=True)
            if r.returncode: continue
            data = r.stdout
        text = data.decode('utf-8', 'replace')
        joined = re.sub(r'\\\n\s*', '', text)  # Rust string continuations
        low = text.lower()
        for n in FRAGS:
            if n in text or n in joined or n.lower() in low: hits.append((rev, f, 'text', n[:40]))
        if f.endswith('.json'):
            try:
                for s in strings(json.loads(text)):
                    for n in FRAGS:
                        if n in s: hits.append((rev, f, 'json-decoded', n[:40]))
            except ValueError: pass
        for h in hexes:
            if h in low: hits.append((rev, f, 'old digest', h))
        for h, label in hashed.items():
            if h in low: hits.append((rev, f, label, h))
print(f'files {len(files)}, old digests {len(hexes)}, hashed forms {len(hashed)}, hits {len(hits)}')
for h in sorted(set(hits)): print('HIT', *h)
