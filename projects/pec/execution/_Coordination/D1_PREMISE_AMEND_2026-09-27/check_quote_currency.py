#!/usr/bin/env python3
"""Corpus-wide dependency quote-currency check (the D-PEC-95 rule, as gen_d95.py
step 3 applies it), for the D1 premise amendment (provisional D-PEC-105).
Adapted from the S4 preparation's check_quote_currency.py.

For every row of every projects/pec/execution/PKG-*/1_Working/DEL-*/Dependencies.csv
under --tree with Status ACTIVE and DependencyClass EXECUTION, the EvidenceQuote
must be a raw (unnormalized) substring of the file its EvidenceFile names
(relative to projects/pec). Prints one line per failing row and the summary line
(unchanged from S4). It then applies the same raw rule to every ACTIVE row of any
class (a second summary, informational) and prints one line for each ACTIVE row,
of any class, whose EvidenceFile is one of the D1 targets in <prep>/targets.json
(PASS/FAIL), followed by a count line.

The runner compares the pre-act and post-act outputs: they must be identical (no
row may start or stop failing), and no D1-target-cited row may FAIL after the act.

Usage: check_quote_currency.py --tree <export root> --prep <prep dir>
Exit 0 always when the scan completes (the comparison is the check); 2 on a read
error. Read-only; stdlib only.
"""
import argparse, csv, io, json, sys
from pathlib import Path

ap = argparse.ArgumentParser(); ap.add_argument("--tree", required=True); ap.add_argument("--prep", required=True)
a = ap.parse_args()
pec = Path(a.tree) / "projects/pec"
targets = {t["path"][len("projects/pec/"):]: t["key"]
           for t in json.loads((Path(a.prep) / "targets.json").read_text(encoding="utf-8"))["targets"]}
n = ok = 0; n_all = ok_all = 0; fails = []; cited = []
try:
    for p in sorted((pec / "execution").glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
        for r in csv.DictReader(io.StringIO(p.read_text(encoding="utf-8"), newline="")):
            if r.get("Status") != "ACTIVE":
                continue
            ef = r.get("EvidenceFile") or ""
            ev = pec / ef
            good = bool(ef) and ev.is_file() and (r.get("EvidenceQuote") or "") in ev.read_text(encoding="utf-8")
            n_all += 1; ok_all += good
            if r.get("DependencyClass") == "EXECUTION":
                n += 1
                if good: ok += 1
                else: fails.append(f"{r['DependencyID']} -> {ef}")
            if ef in targets:
                cited.append(f"{'PASS' if good else 'FAIL'} TARGET-cited {targets[ef]} {r['DependencyID']} "
                             f"({r.get('DependencyClass')}) -> {ef}")
except OSError as e:
    print(f"ERROR {e}"); sys.exit(2)
for f in fails: print("NOT_VERBATIM " + f)
print(f"SUMMARY active_execution_quotes_verbatim {ok}/{n}")
print(f"INFO active_all_classes_quotes_verbatim {ok_all}/{n_all}")
for s in cited: print(s)
print(f"TARGET-cited active rows: {len(cited)}")
