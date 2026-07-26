#!/usr/bin/env python3
"""D-PEC-65 fan-in checker: every EXECUTION row's EvidenceQuote must be a
verbatim substring of its cited EvidenceFile (repo-root-relative path).

Dispatcher-run only (packet section 3.3). Report-only; exit 1 on any MISS.
A whitespace-normalized fallback match is reported as NORM (flagged, not a
pass-equivalent: NORM rows need a human look at fan-in).

Usage: python3 check_verbatim_quotes.py <execution_root> [PKG-filter]
"""
import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def main() -> int:
    root = Path(sys.argv[1])
    pkg_filter = sys.argv[2] if len(sys.argv) > 2 else None
    rows_checked = hits = norms = 0
    misses, empties = [], []
    file_cache = {}
    for reg in sorted(root.glob("PKG-*/*/DEL-*/Dependencies.csv")):
        if pkg_filter and pkg_filter not in str(reg):
            continue
        with open(reg, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("DependencyClass") != "EXECUTION":
                    continue
                rows_checked += 1
                quote = (row.get("EvidenceQuote") or "").strip()
                dep = row.get("DependencyID")
                if not quote:
                    empties.append(dep)
                    continue
                ef = (row.get("EvidenceFile") or "").strip()
                path = REPO_ROOT / "projects" / "pec" / ef if not ef.startswith("projects/") else REPO_ROOT / ef
                if path not in file_cache:
                    file_cache[path] = path.read_text(encoding="utf-8", errors="replace") if path.is_file() else None
                content = file_cache[path]
                if content is None:
                    misses.append((dep, f"EvidenceFile unresolved: {ef}"))
                elif quote in content:
                    hits += 1
                elif norm(quote) in norm(content):
                    norms += 1
                    misses_note = f"NORM-only match in {ef}"
                    print(f"NORM  {dep}  {misses_note}")
                else:
                    misses.append((dep, f"quote not found in {ef}"))
    print(f"EXECUTION rows checked: {rows_checked}")
    print(f"verbatim HIT: {hits}  NORM-only: {norms}  empty-quote: {len(empties)}  MISS: {len(misses)}")
    for dep in empties:
        print(f"EMPTY {dep} (must be waived: two rows, EVQ-003 + EVQ-004)")
    for dep, why in misses:
        print(f"MISS  {dep}  {why}")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main())
