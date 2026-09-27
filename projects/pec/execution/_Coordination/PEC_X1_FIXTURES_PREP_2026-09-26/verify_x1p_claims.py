#!/usr/bin/env python3
"""Two-sided checks for the draft proposal.
- State claims (claims/hash_claims.json): each abbreviated hash `pppppppp…sss` the draft prints
  equals SHA-256 of the named file at the named commit (or of a prep-folder file, commit "prep"; or a 64-hex value recorded in an evidence file, commit "evidence"),
  and the abbreviation occurs in the draft. Every abbreviation in the draft must be claimed.
- Quotes (claims/quotes.json): each quoted text occurs verbatim in the named file at the named
  commit (source side) and in the draft (draft side).
Usage: verify_x1p_claims.py <repo> <prep dir>"""
import hashlib, json, re, subprocess, sys
from pathlib import Path
repo, prep = sys.argv[1], Path(sys.argv[2])
draft = (prep / "DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md").read_text()
def src(commit, path):
    if commit == "prep": return (prep / path).read_bytes()
    return subprocess.run(["git", "-C", repo, "show", f"{commit}:{path}"], capture_output=True, check=True).stdout
bad = 0; n = 0
claims = json.loads((prep / "claims/hash_claims.json").read_text())
claimed = set()
for c in claims:
    n += 1; ab = c["abbrev"]; pre, suf = ab.split("…")
    if c["commit"] == "evidence":  # a recorded 64-hex value in a prep-folder evidence file
        found = re.findall(rf"\b{pre}[0-9a-f]{{{64 - len(pre) - len(suf)}}}{suf}\b", (prep / c["path"]).read_text())
        h = found[0] if found else "0" * 64
    else:
        h = hashlib.sha256(src(c["commit"], c["path"])).hexdigest()
    ok = h.startswith(pre) and h.endswith(suf) and f"`{ab}`" in draft
    claimed.add(ab)
    if not ok: bad += 1; print(f"FAIL claim {ab} {c['commit']}:{c['path']} actual {h[:8]}…{h[-5:]} in_draft={f'`{ab}`' in draft}")
for ab in sorted(set(re.findall(r"`([0-9a-f]{8}…[0-9a-f]{3,5})`", draft)) - claimed):
    n += 1; bad += 1; print(f"FAIL unclaimed abbreviation in draft: {ab}")
for q in json.loads((prep / "claims/quotes.json").read_text()):
    norm = lambda t: " ".join(t.split())
    n += 1; s_ok = norm(q["text"]) in norm(src(q["commit"], q["path"]).decode("utf-8")); d_ok = norm(q["text"]) in norm(draft)
    if not (s_ok and d_ok): bad += 1; print(f"FAIL quote {q['id']}: source={s_ok} draft={d_ok}")
print(f"RESULT {'PASS' if not bad else 'FAIL'} {n-bad}/{n}")
sys.exit(1 if bad else 0)
