"""Preimage check against a commit (post-hoc record of the pre-run check).
usage: precheck_commit.py <repo> <table.tsv> <commit>"""
import hashlib, subprocess, sys
repo, table, commit = sys.argv[1], sys.argv[2], sys.argv[3]
ok = bad = 0
for line in open(table, encoding='utf-8'):
    path, act, pre, post = line.rstrip('\n').split('\t')
    r = subprocess.run(['git', '-C', repo, 'show', f'{commit}:{path}'], capture_output=True)
    got = hashlib.sha256(r.stdout).hexdigest() if r.returncode == 0 else 'absent'
    flag = 'OK' if got == pre else 'MISMATCH'
    ok += flag == 'OK'; bad += flag != 'OK'
    print(f"{flag}\t{act}\t{path}\t{got}")
print(f"COMMIT {commit} TOTAL {ok + bad} OK {ok} MISMATCH {bad}")
