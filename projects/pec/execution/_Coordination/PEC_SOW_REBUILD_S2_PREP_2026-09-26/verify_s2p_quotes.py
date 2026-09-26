#!/usr/bin/env python3
"""Two-sided quote check for the S2 (provisional D-PEC-100) candidate contracts.

For every entry in quotes/<DEL>.json the quoted text must occur (a) in the
candidate ScopeOfWork.md that carries it and (b) at its cited source. The source
is read from the tree given by --tree, or, when the entry names a "commit", with
`git show <commit>:<source>` from --gitdir. Normalization strips Markdown
blockquote markers (columns 0-3) and collapses whitespace on both sides; an
entry may add "strip_emphasis": true to drop `**` on both sides. Nothing else
is normalized. A quote shorter than 12 normalized characters fails.

Source kinds:
  "text" (default)  substring of the whole normalized file;
  "csv_cell"        substring of one normalized cell of the CSV row whose
                    "key_column" equals "key", in column "column".

Further checks, per candidate:
  - DEP: every ACTIVE row of any Dependencies.csv under the tree whose
    EvidenceFile is this deliverable's ScopeOfWork.md has its EvidenceQuote as
    a raw (unnormalized) substring of the candidate, as gen_d95.py checks it.
  - FORBID: the candidate does not contain the phrase "at the basis".
  - OBS: the candidate names the observation commit given by --observation.

Usage:
  verify_s2p_quotes.py --tree <export root> --gitdir <repo> --prep <prep dir>
                       --observation <short sha> [--only DEL-XX-YY ...]
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

def norm(s, emph=False):
    s = "\n".join(re.sub(r"^ {0,3}> ?", "", l) for l in s.splitlines())
    if emph:
        s = s.replace("**", "")
    return re.sub(r"\s+", " ", s).strip()

_cache = {}
def source_text(rel, commit):
    k = (rel, commit)
    if k not in _cache:
        if commit:
            r = subprocess.run(["git", "-C", a.gitdir, "show", f"{commit}:{rel}"], capture_output=True)
            _cache[k] = r.stdout.decode("utf-8") if r.returncode == 0 else None
        else:
            p = tree / rel
            _cache[k] = p.read_text(encoding="utf-8") if p.is_file() else None
    return _cache[k]

def cand_path(deliv):
    hits = sorted(prep.glob(f"candidates/projects/pec/execution/PKG-*/1_Working/{deliv}_*/ScopeOfWork.md"))
    return hits[0] if len(hits) == 1 else None

checks = []
def ok(cond, name):
    checks.append((bool(cond), name))

qfiles = sorted((prep / "quotes").glob("DEL-*.json"))
for qf in qfiles:
    spec = json.loads(qf.read_text(encoding="utf-8"))
    deliv = spec["deliverable"]
    if a.only and deliv not in a.only:
        continue
    cp = cand_path(deliv)
    if cp is None:
        ok(False, f"{deliv} candidate file not found exactly once"); continue
    raw = cp.read_text(encoding="utf-8")
    cand_n, cand_e = norm(raw), norm(raw, True)
    ids = set()
    for q in spec["quotes"]:
        qid = q["id"]
        if qid in ids:
            ok(False, f"{deliv} {qid} duplicate id"); continue
        ids.add(qid)
        emph = bool(q.get("strip_emphasis"))
        n = norm(q["text"], emph)
        in_c = len(n) >= 12 and n in (cand_e if emph else cand_n)
        src = source_text(q["source"], q.get("commit"))
        in_s = False
        if src is not None and len(n) >= 12:
            if q.get("kind", "text") == "csv_cell":
                for row in csv.DictReader(io.StringIO(src, newline="")):
                    if row.get(q["key_column"]) == q["key"]:
                        in_s = n in norm(row.get(q["column"]) or "", emph)
                        break
            else:
                in_s = n in norm(src, emph)
        where = q["source"] + (f"@{q['commit']}" if q.get("commit") else "")
        ok(in_c and in_s, f"{deliv} {qid} [{len(n)} chars; candidate={'yes' if in_c else 'NO'}; source={'yes' if in_s else 'NO'}] {where}")
    # DEP: dependency EvidenceQuotes that cite this deliverable's contract (raw, as gen_d95.py)
    rel_c = cp.relative_to(prep / "candidates" / "projects" / "pec").as_posix()
    n_dep = 0
    for dp in sorted((tree / "projects/pec/execution").glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
        for r in csv.DictReader(io.StringIO(dp.read_text(encoding="utf-8"), newline="")):
            if r.get("Status") == "ACTIVE" and r.get("EvidenceFile") == rel_c:
                n_dep += 1
                ok(r["EvidenceQuote"] in raw, f"{deliv} DEP {r['DependencyID']} EvidenceQuote raw-verbatim in candidate")
    print(f"INFO {deliv} DEP rows citing this contract: {n_dep}")
    ok("at the basis" not in raw.lower(), f"{deliv} FORBID phrase 'at the basis' absent")
    ok(a.observation in raw, f"{deliv} OBS observation commit {a.observation} named")

npass = sum(1 for c, _ in checks if c)
for c, name in checks:
    print(("PASS " if c else "FAIL ") + name)
print(f"RESULT {'PASS' if npass == len(checks) and checks else 'FAIL'} {npass}/{len(checks)}")
sys.exit(0 if npass == len(checks) and checks else 1)
