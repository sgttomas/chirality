#!/usr/bin/env python3
"""Check the commit-anchored state claims of the S2 (provisional D-PEC-100)
candidates against Git, from claims/<DEL>.json.

Every claim is read with `git show` / `git ls-tree` / `git merge-base` at the
commit the entry names, so the result does not depend on any working tree.
Each entry also carries "candidate_text", which must occur (whitespace
collapsed) in the candidate ScopeOfWork.md: the claim is checked on both sides.

Entry kinds (fields: id, commit, kind, path, value, candidate_text):
  sha256         SHA-256 of <commit>:<path> equals value (64 hex)
  sha256_prefix  SHA-256 of <commit>:<path> starts with value (>= 12 hex)
  contains       <commit>:<path> contains value (whitespace collapsed)
  not_contains   <commit>:<path> exists and does not contain value
  exists         <commit>:<path> exists (file or tree)
  absent         <commit>:<path> does not exist
  ancestor       commit is an ancestor of value (a commit)
  csv_cell       in CSV <commit>:<path>, the row with value["key_column"] ==
                 value["key"] has value["column"] equal to value["equals"]
                 (or containing value["contains"])
  count_glob     number of paths under <commit> matching the fnmatch pattern
                 value["pattern"] equals value["count"]; optional
                 value["contains"] counts only files containing that text

Usage: verify_s2p_state_claims.py --gitdir <repo> --prep <prep dir> [--only DEL-XX-YY ...]
Exit 0 when every check passes; 1 otherwise. Stdlib only; read-only.
"""
import argparse, csv, fnmatch, hashlib, io, json, re, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--gitdir", required=True)
ap.add_argument("--prep", required=True)
ap.add_argument("--only", nargs="*")
a = ap.parse_args()
prep = Path(a.prep)

def git(*args, text=False):
    return subprocess.run(["git", "-C", a.gitdir, *args], capture_output=True, text=text)
_show = {}
def show(c, p):
    k = (c, p)
    if k not in _show:
        r = git("show", f"{c}:{p}")
        _show[k] = r.stdout if r.returncode == 0 else None
    return _show[k]
def exists(c, p):
    return git("cat-file", "-e", f"{c}:{p}").returncode == 0
_ls = {}
def ls_all(c):
    if c not in _ls:
        _ls[c] = git("ls-tree", "-r", "--name-only", c, text=True).stdout.splitlines()
    return _ls[c]
def ws(s): return re.sub(r"\s+", " ", s).strip()

def cand_path(deliv):
    hits = sorted(prep.glob(f"candidates/projects/pec/execution/PKG-*/1_Working/{deliv}_*/ScopeOfWork.md"))
    return hits[0] if len(hits) == 1 else None

checks = []
def ok(cond, name): checks.append((bool(cond), name))

for cf in sorted((prep / "claims").glob("DEL-*.json")):
    spec = json.loads(cf.read_text(encoding="utf-8"))
    deliv = spec["deliverable"]
    if a.only and deliv not in a.only:
        continue
    cp = cand_path(deliv)
    if cp is None:
        ok(False, f"{deliv} candidate file not found exactly once"); continue
    cand = ws(cp.read_text(encoding="utf-8"))
    ids = set()
    for e in spec["claims"]:
        cid, c, kind, p, v = e["id"], e["commit"], e["kind"], e.get("path"), e.get("value")
        if cid in ids:
            ok(False, f"{deliv} {cid} duplicate id"); continue
        ids.add(cid)
        try:
            if kind == "sha256":
                b = show(c, p); res = b is not None and hashlib.sha256(b).hexdigest() == v
            elif kind == "sha256_prefix":
                b = show(c, p); res = b is not None and len(v) >= 12 and hashlib.sha256(b).hexdigest().startswith(v)
            elif kind == "contains":
                b = show(c, p); res = b is not None and ws(v) in ws(b.decode("utf-8"))
            elif kind == "not_contains":
                b = show(c, p); res = b is not None and ws(v) not in ws(b.decode("utf-8"))
            elif kind == "exists":
                res = exists(c, p)
            elif kind == "absent":
                res = not exists(c, p)
            elif kind == "ancestor":
                res = git("merge-base", "--is-ancestor", c, v).returncode == 0
            elif kind == "csv_cell":
                b = show(c, p); res = False
                if b is not None:
                    for row in csv.DictReader(io.StringIO(b.decode("utf-8"), newline="")):
                        if row.get(v["key_column"]) == v["key"]:
                            cell = row.get(v["column"]) or ""
                            res = (cell == v["equals"]) if "equals" in v else (ws(v["contains"]) in ws(cell))
                            break
            elif kind == "count_glob":
                paths = [x for x in ls_all(c) if fnmatch.fnmatch(x, v["pattern"])]
                if "contains" in v:
                    paths = [x for x in paths if (show(c, x) or b"").decode("utf-8", "replace").find(v["contains"]) >= 0]
                res = len(paths) == int(v["count"])
            else:
                res = False; kind = f"UNKNOWN KIND {kind}"
        except Exception as ex:
            res = False; kind = f"{kind} error {ex}"
        in_c = ws(e["candidate_text"]) in cand and len(ws(e["candidate_text"])) >= 4
        ok(res and in_c, f"{deliv} {cid} {kind} {c}:{p or ''} [git={'yes' if res else 'NO'}; candidate={'yes' if in_c else 'NO'}]")

npass = sum(1 for c, _ in checks if c)
for c, name in checks:
    print(("PASS " if c else "FAIL ") + name)
print(f"RESULT {'PASS' if npass == len(checks) and checks else 'FAIL'} {npass}/{len(checks)}")
sys.exit(0 if npass == len(checks) and checks else 1)
