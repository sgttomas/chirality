"""Option-A aggregate: members in bytewise-sorted projects/pec/... path order, concatenated.
usage: aggregate.py <repo> <table.tsv>"""
import hashlib, sys
from pathlib import Path
repo, table = Path(sys.argv[1]), sys.argv[2]
paths = sorted((l.split('\t')[0] for l in open(table, encoding='utf-8')), key=lambda s: s.encode())
h = hashlib.sha256()
for p in paths:
    h.update((repo / p).read_bytes())
pl = hashlib.sha256(''.join(p + '\n' for p in paths).encode()).hexdigest()
print(f"members={len(paths)} aggregate={h.hexdigest()} pathlist(newline-terminated)={pl}")
