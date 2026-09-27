#!/usr/bin/env python3
"""Corpus-wide dependency quote-currency check (the D-PEC-95 rule, as gen_d95.py
step 3 applies it), for the S4 (provisional D-PEC-102) act.

For every row of every projects/pec/execution/PKG-*/1_Working/DEL-*/Dependencies.csv
under --tree with Status ACTIVE and DependencyClass EXECUTION, the EvidenceQuote
must be a raw (unnormalized) substring of the file its EvidenceFile names
(relative to projects/pec). Prints one line per failing row, then a summary
line, then the rows whose EvidenceFile is a ScopeOfWork.md (each PASS/FAIL).

The runner compares the pre-act and post-act outputs: they must be identical
(no row may start or stop failing), and every row citing an S4 contract must
pass after the act (SCA-006 Propagation_Plan.md §B4, D-PEC-95 carry-forward).

Usage: check_quote_currency.py --tree <export root>
Exit 0 always when the scan completes (the comparison is the check); 2 on a read
error. Read-only; stdlib only.
"""
import argparse, csv, io, sys
from pathlib import Path

ap = argparse.ArgumentParser(); ap.add_argument("--tree", required=True)
a = ap.parse_args()
pec = Path(a.tree) / "projects/pec"
n = ok = 0; fails = []; sow = []
try:
    for p in sorted((pec / "execution").glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
        for r in csv.DictReader(io.StringIO(p.read_text(encoding="utf-8"), newline="")):
            if (r.get("DependencyClass"), r.get("Status")) != ("EXECUTION", "ACTIVE"):
                continue
            n += 1
            ev = pec / (r.get("EvidenceFile") or "")
            good = ev.is_file() and (r.get("EvidenceQuote") or "") in ev.read_text(encoding="utf-8")
            if good: ok += 1
            else: fails.append(f"{r['DependencyID']} -> {r.get('EvidenceFile')}")
            if (r.get("EvidenceFile") or "").endswith("ScopeOfWork.md"):
                sow.append(f"{'PASS' if good else 'FAIL'} SOW-cited {r['DependencyID']} -> {r['EvidenceFile']}")
except OSError as e:
    print(f"ERROR {e}"); sys.exit(2)
for f in fails: print("NOT_VERBATIM " + f)
print(f"SUMMARY active_execution_quotes_verbatim {ok}/{n}")
for s in sow: print(s)
