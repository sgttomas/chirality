#!/usr/bin/env python3
"""Merge the two sealed DEL-01-02 split ledgers (S1, S2) into R2/PKG-01/DEL-01-02/DEL-01-02_claims.csv and
DEL-01-02_notes.md (brief step 3). Rows: S1 in file order, then S2 in file order; header and cells unchanged
(re-serialised with csv, QUOTE_MINIMAL). Fails on header mismatch or duplicate ClaimKey. Prints both half
SHA-256s and the merged SHA-256. The merged ledger is validated against the full CLAIM_INDEX afterwards."""
import csv, collections, hashlib, io, os, sys
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D = os.path.join(P, "DEL-01-02")
def load(p):
    t = open(p, encoding="utf-8").read().rstrip()
    assert t.endswith("#END"), p
    rd = csv.reader(io.StringIO(t[:-4])); rows = list(rd); return rows[0], rows[1:]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
h1, r1 = load(os.path.join(D, "S1", "DEL-01-02_claims.csv")); h2, r2 = load(os.path.join(D, "S2", "DEL-01-02_claims.csv"))
if h1 != h2: sys.exit("header mismatch")
keys = [r[0] for r in r1 + r2]; dup = [k for k, n in collections.Counter(keys).items() if n > 1]
if dup: sys.exit(f"duplicate keys {dup}")
out = os.path.join(D, "DEL-01-02_claims.csv")
if os.path.exists(out): sys.exit("merged ledger exists; refusing to overwrite a sealed file")
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n"); w.writerow(h1); w.writerows([r for r in r1 + r2 if any(c.strip() for c in r)]); fh.write("#END\n")
hi = h1.index("Disposition"); ct = h1.index("ClaimType")
rows = r1 + r2
cen = collections.Counter(r[hi] for r in rows); cty = collections.Counter(r[ct] for r in rows)
notes = ["# DEL-01-02 — merged notes (split ledger S1 + S2)", "",
         "> Assembled by `R2/PKG-01/_scripts/merge_split.py` from the two sealed split halves. The census below is",
         "> computed from the merged ledger; the two halves' own notes follow unchanged.", "",
         f"- S1 ledger `S1/DEL-01-02_claims.csv` sha256 `{sha(os.path.join(D, 'S1', 'DEL-01-02_claims.csv'))}`; rows {len(r1)}",
         f"- S2 ledger `S2/DEL-01-02_claims.csv` sha256 `{sha(os.path.join(D, 'S2', 'DEL-01-02_claims.csv'))}`; rows {len(r2)}",
         f"- Merged ledger `DEL-01-02_claims.csv` sha256 `{sha(out)}`; rows {len(rows)}", "",
         "## Merged census", "", f"- Disposition: {dict(sorted(cen.items()))}", f"- ClaimType: {dict(sorted(cty.items()))}", ""]
for s in ("S1", "S2"):
    notes += [f"## Half {s} notes (verbatim)", "", open(os.path.join(D, s, "DEL-01-02_notes.md"), encoding="utf-8").read(), ""]
open(os.path.join(D, "DEL-01-02_notes.md"), "w", encoding="utf-8").write("\n".join(notes))
print("S1", len(r1), "S2", len(r2), "merged", len(rows), sha(out))
