#!/usr/bin/env python3
"""Evidence pack item 4: DECISION_HITS.csv (CONVENTIONS §9), per package.

Usage: decision_hits.py --frozen <frozen-tree> --inventory <R1_INVENTORY/DELIVERABLE_INVENTORY.csv>
                        (--package PKG-xx | --all) --out <DECISION_HITS.csv>

Files are read from the frozen tree only (no git). Deliverables and folders come from
DELIVERABLE_INVENTORY.csv. `D` below is the deliverable ID, matched as `D` not followed by a digit
(so `DEL-03-01-V3-01` names DEL-03-01).
- Source=DELIVERABLE: every distinct (DecisionID, file, line) where `D-APP-<n>` or `D-GOV-<n>` occurs
  in any text file under the deliverable's folder (recursive).
- Source=REGISTER: every row of execution/_Coordination/_DECISIONS/_REGISTER.md (a table line whose
  first cell is `D-APP-<n>`) whose text names D; DecisionID is that row's ID.
- Source=RULING: every ruling record execution/_Coordination/_DECISIONS/D-APP-<n>_RULING*.md whose
  text names D; one row per record at the first line naming D; DecisionID from the file name.
IDs are written in the register's spelling (e.g. `D-APP-01`) when the register has that number,
else as `D-APP-<n>` / `D-GOV-<n>` without leading zeros.
Kind ∈ D-APP, D-GOV. RegisterState = first word of the App register State cell for D-APP IDs
(`NOT_IN_REGISTER` if absent), `ROOT` for D-GOV.
Paths are repo-relative. Sort: DeliverableID, DecisionID, Path, Line (numeric).
"""
import argparse
import csv
import io
import os
import re

DEC_DIR = "projects/chirality-app-dev/execution/_Coordination/_DECISIONS"
IDRE = re.compile(r"\bD-(APP|GOV)-(\d+)(?!\d)")
TEXT_EXT = {".md", ".csv", ".txt", ".json", ".jsonl", ".yaml", ".yml", ".html", ".ts", ".tsx", ".mjs", ".js"}


def load_register(frozen):
    reg = {}
    rows = []
    p = os.path.join(frozen, DEC_DIR, "_REGISTER.md")
    for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
        m = re.match(r"^\|\s*(D-APP-(\d+))\s*\|", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        state = cells[3].split()[0].strip("*`,;()") if len(cells) > 3 and cells[3].split() else "UNKNOWN"
        n = int(m.group(2))
        reg.setdefault(n, (m.group(1), state))
        rows.append((i, m.group(1), line))
    return reg, rows


def norm(kind, n, reg):
    if kind == "APP":
        return reg[n][0] if n in reg else f"D-APP-{n}"
    return f"D-GOV-{n}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen", required=True)
    ap.add_argument("--inventory", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--package")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    inv = [r for r in csv.DictReader(open(a.inventory, encoding="utf-8", newline=""))
           if r["PackageID"] and not r["PackageID"].startswith("#")
           and (a.all or r["PackageID"] == a.package)]
    if not inv:
        raise SystemExit(f"no deliverables for package {a.package!r}")
    reg, reg_rows = load_register(a.frozen)
    rulings = []
    for f in sorted(os.listdir(os.path.join(a.frozen, DEC_DIR))):
        m = re.match(r"^D-APP-(\d+)_RULING.*\.md$", f)
        if m:
            rulings.append((f"{DEC_DIR}/{f}", int(m.group(1))))

    def state(kind, n):
        if kind == "GOV":
            return "ROOT"
        return reg[n][1] if n in reg else "NOT_IN_REGISTER"

    rows = set()
    for r in inv:
        d = r["DeliverableID"]
        dre = re.compile(re.escape(d) + r"(?!\d)")
        base = os.path.join(a.frozen, r["Path"])
        for dirpath, dirs, files in os.walk(base):
            dirs.sort()
            for f in sorted(files):
                if os.path.splitext(f)[1].lower() not in TEXT_EXT:
                    continue
                full = os.path.join(dirpath, f)
                rel = os.path.relpath(full, a.frozen).replace(os.sep, "/")
                for i, line in enumerate(open(full, encoding="utf-8", errors="replace"), 1):
                    for m in IDRE.finditer(line):
                        k, n = m.group(1), int(m.group(2))
                        rows.add((d, norm(k, n, reg), f"D-{k}", "DELIVERABLE", rel, i, state(k, n)))
        for i, did, line in reg_rows:
            if dre.search(line):
                n = int(did.split("-")[2])
                rows.add((d, did, "D-APP", "REGISTER", f"{DEC_DIR}/_REGISTER.md", i, state("APP", n)))
        for rel, n in rulings:
            for i, line in enumerate(open(os.path.join(a.frozen, rel), encoding="utf-8", errors="replace"), 1):
                if dre.search(line):
                    rows.add((d, norm("APP", n, reg), "D-APP", "RULING", rel, i, state("APP", n)))
                    break
    out = sorted(rows, key=lambda x: (x[0], x[1], x[4], x[5], x[3]))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["DeliverableID", "DecisionID", "Kind", "Source", "Path", "Line", "RegisterState"])
    w.writerows(out)
    buf.write("#END\n")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "w", encoding="utf-8", newline="").write(buf.getvalue())


if __name__ == "__main__":
    main()
