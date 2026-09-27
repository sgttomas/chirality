#!/usr/bin/env python3
"""Corpus-wide dependency quote currency, as gen_d95.py (D-PEC-95) step 3 checks it:
every ACTIVE EXECUTION row of every Dependencies.csv under projects/pec/execution
has its EvidenceQuote as a raw substring of its EvidenceFile (relative to
projects/pec). Usage: check_dep_quote_currency.py <tree root>. Read-only; stdlib only."""
import csv, io, sys
from pathlib import Path
root = Path(sys.argv[1]); pec = root / "projects/pec"
n = ok = 0
for p in sorted((pec / "execution").glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
    for r in csv.DictReader(io.StringIO(p.read_text(encoding="utf-8"), newline="")):
        if (r.get("DependencyClass"), r.get("Status")) != ("EXECUTION", "ACTIVE"):
            continue
        n += 1
        ev = pec / r["EvidenceFile"]
        good = ev.is_file() and r["EvidenceQuote"] in ev.read_text(encoding="utf-8")
        ok += good
        if not good:
            print(f"FAIL {r['DependencyID']} quote not verbatim in {r['EvidenceFile']}")
print(f"RESULT {'PASS' if ok == n and n else 'FAIL'} {ok}/{n}")
sys.exit(0 if ok == n and n else 1)
