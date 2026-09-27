#!/usr/bin/env python3
"""Two-sided quote check for the D1 premise-amendment candidates (provisional D-PEC-105).

Adapted from the S4 preparation's verify_s4p_quotes.py; candidates are keyed by
target path (targets.json) instead of by ScopeOfWork.md.

For every entry in quotes/<KEY>.json the quoted text must occur (a) in the
candidate for that key and (b) at its cited source. The source is read with
`git show <commit>:<source>` from --gitdir (every entry must name a commit).
Normalization strips Markdown blockquote markers (columns 0-3) and collapses
whitespace on both sides; "strip_emphasis": true drops `**` on both sides.
Nothing else is normalized. A quote shorter than 12 normalized characters fails.

Source kinds: "text" (default, substring of the normalized file) and
"csv_cell" (substring of one normalized cell: row where key_column == key,
column "column").

Further checks, per candidate:
  - DEP: every ACTIVE row of any Dependencies.csv under the tree whose
    EvidenceFile is this target has its EvidenceQuote as a raw substring of
    the candidate (the gen_d95.py rule).
  - FORBID: the candidate does not contain the phrase "at the basis".
  - PIN: every candidate names the pin commit (targets.json pin_commit).
  - OBS: every "sow" candidate names the observation commit (--observation).
  - MULT: a text that N entries quote from one source occurs >= N times.

Usage: verify_d1p_quotes.py --tree <export root> --gitdir <repo> --prep <prep>
                            --observation <short sha> [--only KEY ...]
Exit 0 when every check passes; 1 otherwise. Stdlib only; read-only.
"""
import argparse, csv, io, json, re, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--tree", required=True)
ap.add_argument("--gitdir", required=True)
ap.add_argument("--prep", required=True)
ap.add_argument("--observation", required=True)
ap.add_argument("--only", nargs="*")
a = ap.parse_args()
tree, prep = Path(a.tree), Path(a.prep)
targets = json.loads((prep / "targets.json").read_text(encoding="utf-8"))
known = {t["key"]: t for t in targets["targets"]}
pin = targets["pin_commit"]

def norm(s, emph=False):
    s = "\n".join(re.sub(r"^ {0,3}> ?", "", l) for l in s.splitlines())
    if emph:
        s = s.replace("**", "")
    return re.sub(r"\s+", " ", s).strip()

_cache = {}
def source_text(rel, commit):
    k = (rel, commit)
    if k not in _cache:
        r = subprocess.run(["git", "-C", a.gitdir, "show", f"{commit}:{rel}"], capture_output=True)
        _cache[k] = r.stdout.decode("utf-8") if r.returncode == 0 else None
    return _cache[k]

checks = []
def ok(cond, name):
    checks.append((bool(cond), name))

for qf in sorted((prep / "quotes").glob("*.json")):
    spec = json.loads(qf.read_text(encoding="utf-8"))
    key = spec["key"]
    if a.only and key not in a.only:
        continue
    t = known.get(key)
    if t is None:
        ok(False, f"{key} unknown key"); continue
    cp = prep / "candidates" / t["path"]
    if not cp.is_file():
        ok(False, f"{key} candidate file missing"); continue
    raw = cp.read_text(encoding="utf-8")
    cand_n, cand_e = norm(raw), norm(raw, True)
    ids = set()
    for q in spec["quotes"]:
        qid = q["id"]
        if qid in ids:
            ok(False, f"{key} {qid} duplicate id"); continue
        ids.add(qid)
        if not q.get("commit"):
            ok(False, f"{key} {qid} names no commit"); continue
        emph = bool(q.get("strip_emphasis"))
        n = norm(q["text"], emph)
        in_c = len(n) >= 12 and n in (cand_e if emph else cand_n)
        src = source_text(q["source"], q["commit"])
        in_s = False
        if src is not None and len(n) >= 12:
            if q.get("kind", "text") == "csv_cell":
                for row in csv.DictReader(io.StringIO(src, newline="")):
                    if row.get(q["key_column"]) == q["key"]:
                        in_s = n in norm(row.get(q["column"]) or "", emph)
                        break
            else:
                in_s = n in norm(src, emph)
        ok(in_c and in_s, f"{key} {qid} [{len(n)} chars; candidate={'yes' if in_c else 'NO'}; source={'yes' if in_s else 'NO'}] {q['source']}@{q['commit']}")
    mult = {}
    for q in spec["quotes"]:
        k = (norm(q["text"], bool(q.get("strip_emphasis"))), bool(q.get("strip_emphasis")), q["source"], q.get("commit"))
        mult[k] = mult.get(k, 0) + 1
    for (n, emph, _s, _c), cnt in mult.items():
        if cnt > 1:
            have = (cand_e if emph else cand_n).count(n)
            ok(have >= cnt, f"{key} MULT text quoted by {cnt} entries occurs {have} times: {n[:60]!r}")
    rel_c = t["path"][len("projects/pec/"):]
    n_dep = 0
    for dp in sorted((tree / "projects/pec/execution").glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
        for r in csv.DictReader(io.StringIO(dp.read_text(encoding="utf-8"), newline="")):
            if r.get("Status") == "ACTIVE" and r.get("EvidenceFile") == rel_c:
                n_dep += 1
                ok(r["EvidenceQuote"] in raw, f"{key} DEP {r['DependencyID']} EvidenceQuote raw-verbatim in candidate")
    print(f"INFO {key} DEP rows citing this target: {n_dep}")
    ok("at the basis" not in raw.lower(), f"{key} FORBID phrase 'at the basis' absent")
    ok(pin in raw, f"{key} PIN pin commit {pin} named")
    if t["kind"] == "sow":
        ok(a.observation in raw, f"{key} OBS observation commit {a.observation} named")

npass = sum(1 for c, _ in checks if c)
for c, name in checks:
    print(("PASS " if c else "FAIL ") + name)
print(f"RESULT {'PASS' if npass == len(checks) and checks else 'FAIL'} {npass}/{len(checks)}")
sys.exit(0 if npass == len(checks) and checks else 1)
