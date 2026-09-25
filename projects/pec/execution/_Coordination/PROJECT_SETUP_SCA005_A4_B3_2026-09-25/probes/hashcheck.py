"""usage: hashcheck.py <repo> <table.tsv> pre|post"""
import hashlib, sys
from pathlib import Path
repo, table, mode = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
ok = bad = 0
for line in open(table, encoding='utf-8'):
    path, act, pre, post = line.rstrip('\n').split('\t')
    p = repo / path
    want = pre if mode == 'pre' else post
    if want == 'absent':
        got = 'absent' if not p.exists() else 'PRESENT'
    else:
        got = hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else 'MISSING'
    flag = 'OK' if got == want else 'MISMATCH'
    ok += flag == 'OK'; bad += flag != 'OK'
    print(f"{flag}\t{act}\t{path}\t{got}")
print(f"TOTAL {ok + bad} OK {ok} MISMATCH {bad}")
