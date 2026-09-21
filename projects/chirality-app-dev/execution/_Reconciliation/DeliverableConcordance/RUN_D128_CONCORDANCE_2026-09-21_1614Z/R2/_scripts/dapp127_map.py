#!/usr/bin/env python3
"""Evidence pack item 5: D-APP-127_APPLICATION_MAP.csv (CONVENTIONS §9).

Usage: dapp127_map.py --frozen <frozen-tree> --inventory <R1_INVENTORY/DELIVERABLE_INVENTORY.csv> --out <csv>

Deliverables and folders come from DELIVERABLE_INVENTORY.csv (54 rows; `Path` is repo-relative
at the frozen basis). Files are read from the frozen tree only. For each deliverable and each
carrier `_STATUS.md`, `ScopeOfWork.md`, `_CONTEXT.md`, `Dependencies.csv`, `_REFERENCES.md`:
- ABSENT  : the carrier file does not exist.
- YES     : some line cites `D-APP-127` or `D-GOV-43` AND states an applied effect, i.e. the same
            line matches /\\b(application|applied|revised|re-pointed|retired)\\b/i
            (e.g. "2026-09-12 - D-GOV-43 application (...): V3-01 revised ...", "Retired ... (D-APP-127)").
            Evidence = path:line of the first such line.
- PARTIAL : the carrier cites D-APP-127 or D-GOV-43 but no citing line states an applied effect.
            Evidence = path:line of the first citation.
- NO      : the carrier exists and cites neither. Evidence = NONE_FOUND.
The map records carrier text only; it does not judge whether D-APP-127 should reach a deliverable.
Sort: DeliverableID, Carrier.
"""
import argparse
import csv
import io
import os
import re

CARRIERS = ["_STATUS.md", "ScopeOfWork.md", "_CONTEXT.md", "Dependencies.csv", "_REFERENCES.md"]
CITE = re.compile(r"D-APP-127(?!\d)|D-GOV-43(?!\d)")
EFFECT = re.compile(r"\b(application|applied|revised|re-pointed|retired)\b", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen", required=True)
    ap.add_argument("--inventory", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    inv = [r for r in csv.DictReader(open(a.inventory, encoding="utf-8", newline=""))
           if r["PackageID"] and not r["PackageID"].startswith("#")]
    rows = []
    for r in inv:
        for c in CARRIERS:
            rel = f"{r['Path']}/{c}"
            p = os.path.join(a.frozen, rel)
            if not os.path.exists(p):
                rows.append((r["DeliverableID"], c, "ABSENT", "NONE_FOUND"))
                continue
            first_cite = first_effect = None
            for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
                if CITE.search(line):
                    first_cite = first_cite or i
                    if EFFECT.search(line):
                        first_effect = i
                        break
            if first_effect:
                rows.append((r["DeliverableID"], c, "YES", f"{rel}:{first_effect}"))
            elif first_cite:
                rows.append((r["DeliverableID"], c, "PARTIAL", f"{rel}:{first_cite}"))
            else:
                rows.append((r["DeliverableID"], c, "NO", "NONE_FOUND"))
    rows.sort(key=lambda x: (x[0], x[1]))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["DeliverableID", "Carrier", "Revised", "Evidence"])
    w.writerows(rows)
    buf.write("#END\n")
    open(a.out, "w", encoding="utf-8", newline="").write(buf.getvalue())


if __name__ == "__main__":
    main()
