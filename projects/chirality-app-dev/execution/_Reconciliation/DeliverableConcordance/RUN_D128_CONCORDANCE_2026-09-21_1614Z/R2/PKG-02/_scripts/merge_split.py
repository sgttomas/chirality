#!/usr/bin/env python3
"""Merge the two sealed DEL-02-01 half ledgers (brief step 3, split deliverable).
Inputs: DEL-02-01/A/DEL-02-01_claims.csv, DEL-02-01/B/DEL-02-01_claims.csv (+ _notes.md).
Checks: identical 25-column header; each half ends with #END; no duplicate ClaimKey across halves;
half A holds only half-A units and run-local keys numbered 1-49, half B only half-B units and 50+.
Output: DEL-02-01/DEL-02-01_claims.csv = header + A rows (in A order) + B rows (in B order) + #END,
written with the csv module (fields re-quoted minimally; values byte-identical); DEL-02-01/DEL-02-01_notes.md
= both notes files verbatim under half headings; DEL-02-01/MERGE_REPORT.md with SHA-256 of every file and
the validator result on the merged ledger (full CLAIM_INDEX). Run from projects/chirality-app-dev."""
import csv, hashlib, io, os, re, subprocess, sys
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); RUN = os.path.dirname(os.path.dirname(PKG))
D = os.path.join(PKG, "DEL-02-01"); VAL = os.path.join(RUN, "_scripts", "validate_ledger.py")
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def load(p):
    r = list(csv.reader(io.StringIO(open(p, encoding="utf-8", newline="").read())))
    assert r[-1] == ["#END"], f"{p}: no #END"
    return r[0], r[1:-1]
def idx(h): return {r[0] for r in csv.reader(open(os.path.join(PKG, "_split", f"INDEX_{h}.csv"), encoding="utf-8")) if len(r) > 3 and r[2] == "DEL-02-01"}
units = {"A": {k.split("#")[1] for k in idx("A")}, "B": {k.split("#")[1] for k in idx("B")}}
errs, out, keys = [], [], set(); hdr0 = None
for h in "AB":
    p = os.path.join(D, h, "DEL-02-01_claims.csv"); hdr, rows = load(p); hdr0 = hdr0 or hdr
    if hdr != hdr0: errs.append(f"{h}: header differs")
    for r in rows:
        k = r[0]; loc = k.split("#")[1]
        if k in keys: errs.append(f"duplicate key {k}")
        keys.add(k)
        m = re.match(r"(REGISTER|STATE)-(\d+)$", loc)
        if m:
            n = int(m.group(2))
            if (h == "A" and n >= 50) or (h == "B" and n < 50): errs.append(f"{h}: run-local {loc} outside its range")
        elif loc.split(".")[0] not in units[h]: errs.append(f"{h}: {loc} is not a half-{h} unit")
        out.append(r)
if errs: print("MERGE FAIL"); print("\n".join(errs)); sys.exit(1)
m = os.path.join(D, "DEL-02-01_claims.csv")
with open(m, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, lineterminator="\n"); w.writerow(hdr0); w.writerows(out); fh.write("#END\n")
with open(os.path.join(D, "DEL-02-01_notes.md"), "w", encoding="utf-8") as fh:
    fh.write("# DEL-02-01 notes (merged by `_scripts/merge_split.py`; halves verbatim)\n\n")
    for h in "AB":
        fh.write(f"\n---\n\n# Half {h} ({'SEC-1..5, CLM-001..015' if h == 'A' else 'CLM-016..030, REM-1..7'})\n\n")
        fh.write(open(os.path.join(D, h, "DEL-02-01_notes.md"), encoding="utf-8").read())
v = subprocess.run(["python3", VAL, "ledger", m], capture_output=True, text=True).stdout.strip().splitlines()
with open(os.path.join(D, "MERGE_REPORT.md"), "w", encoding="utf-8") as fh:
    fh.write("# DEL-02-01 split merge report\n\nScript: `R2/PKG-02/_scripts/merge_split.py` (split plan: `_BRIEFS/SPLIT_PLAN.md`).\n\n")
    fh.write("| File | Rows | SHA-256 |\n|---|---:|---|\n")
    for h in "AB":
        p = os.path.join(D, h, "DEL-02-01_claims.csv"); fh.write(f"| `DEL-02-01/{h}/DEL-02-01_claims.csv` (sealed half) | {len(load(p)[1])} | `{sha(p)}` |\n")
    fh.write(f"| `DEL-02-01/DEL-02-01_claims.csv` (merged ledger of record) | {len(out)} | `{sha(m)}` |\n\n")
    fh.write("Checks: identical header; no duplicate ClaimKey; units and run-local numbering in their half's range.\n\n")
    fh.write("Validator on the merged ledger (full CLAIM_INDEX):\n\n```\n" + "\n".join(v[-2:]) + "\n```\n")
print("\n".join(v[-2:])); print("merged", len(out), sha(m))
