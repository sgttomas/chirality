#!/usr/bin/env python3
"""RV119: E-17's portability entries. The policy file's only change M..H is two appended entries; each path
exists at H with that sha256; the roles and entry types are as RR rules; nothing else in the file changed.
Usage: e17_policy_check.py <repo> <M> <H>"""
import json, subprocess, sys, hashlib
repo, M, H = sys.argv[1:4]
def git(*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,check=True).stdout
P = "projects/chirality-piping/validation/portability_policy.json"
a = json.loads(git("show", f"{M}:{P}")); b = json.loads(git("show", f"{H}:{P}"))
T3 = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
print("top-level keys equal:", sorted(a) == sorted(b))
for k in sorted(b):
    if isinstance(b[k], list):
        pre = b[k][:len(a[k])] == a[k]
        print(f"{k}: {len(a[k])} -> {len(b[k])}; M's list is an exact prefix of H's: {pre}")
        for e in b[k][len(a[k]):]:
            p = e["path"]; ok = subprocess.run(["git","-C",repo,"cat-file","-e",f"{H}:{p}"]).returncode == 0
            sha = hashlib.sha256(git("show", f"{H}:{p}")).hexdigest() if ok else None
            print(f"  appended: {p.replace(T3,'T3/')}\n    exists at H: {ok}; sha256 at H == entry: {sha == e['sha256']} ({e['sha256'][:12]}...)\n    entry_type={e['entry_type']} role={e['role']}\n    authority cites: {e['authority'].split('ROOT_RULINGS_V1, ')[-1]}")
    else:
        print(f"{k}: equal: {a[k] == b[k]}")
# no other change: re-serialise both without the appended entries
bb = {k: (v[:len(a[k])] if isinstance(v, list) else v) for k, v in b.items()}
print("H without the appended entries equals M (parsed):", bb == a)
d = git("diff","--numstat",M,H,"--",P).decode().split()
print(f"numstat: +{d[0]} -{d[1]}")
