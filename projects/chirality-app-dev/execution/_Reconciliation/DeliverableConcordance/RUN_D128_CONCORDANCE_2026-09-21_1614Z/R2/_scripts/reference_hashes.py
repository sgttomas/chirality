#!/usr/bin/env python3
"""Evidence pack item 3: REFERENCE_HASHES.csv (CONVENTIONS §9), per package.

Usage: reference_hashes.py --frozen <frozen-tree> --inventory <R1_INVENTORY/DELIVERABLE_INVENTORY.csv>
                           (--package PKG-xx | --all) --out <REFERENCE_HASHES.csv>

Files are read from the frozen tree only (no git). For each deliverable of the package (from
DELIVERABLE_INVENTORY.csv) and each Document in CONTRACT, SPEC, PRD:
- The deliverable's `_REFERENCES.md` is parsed as Markdown tables. A row refers to the Document when
  its `Path` cell is exactly `docs/<Document>.md` (backticks stripped; the App's own docs, relative
  to projects/chirality-app-dev). The first such row that carries a 64-hex hash wins; otherwise the
  first such row.
- RecordedSha256 = the row's `ActualSHA256` cell, else its `ExpectedSHA256` cell, when 64 hex;
  else `NOT_RECORDED`. RecordedVerdict = the row's `Status` cell (e.g. `MATCH`), else `NOT_RECORDED`.
  A missing `_REFERENCES.md` or no row for the Document gives `NOT_RECORDED` for both.
- List-format files (`- REF-nnn — Location: `docs/<Document>.md` — ... — Accepted SHA-256: `<hex>``)
  are also read: RecordedSha256 = the Accepted SHA-256; RecordedVerdict = a `Status:`/`Verdict:`
  token on that line, else `NOT_RECORDED`.
- RecomputedSha256 = SHA-256 of projects/chirality-app-dev/docs/<Document>.md at the frozen basis
  (equivalent to `shasum -a 256`).
- Match = YES (recorded == recomputed), NO (recorded hash differs), NOT_RECORDED (no recorded hash).
Sort: DeliverableID, Document.
"""
import argparse
import csv
import hashlib
import io
import os
import re

DOCS = ["CONTRACT", "PRD", "SPEC"]
HEX = re.compile(r"^[0-9a-f]{64}$")
LIST_ROW = re.compile(r"^\s*[-*]\s*REF-\d+\s*.*Location:\s*`docs/(CONTRACT|SPEC|PRD)\.md`")


def cells(line):
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return None
    return [c.strip().strip("`").strip() for c in s[1:-1].split("|")]


def parse_refs(path):
    out = {}
    if not os.path.exists(path):
        return out
    header = None
    for line in open(path, encoding="utf-8", errors="replace"):
        lm = LIST_ROW.search(line)
        if lm and lm.group(1) not in out:
            sm = re.search(r"SHA-?256:\s*`([0-9a-f]{64})`", line)
            vm = re.search(r"(?:Status|Verdict):\s*`?([A-Z_]+)`?", line)
            out[lm.group(1)] = (sm.group(1) if sm else "NOT_RECORDED", vm.group(1) if vm else "NOT_RECORDED")
        c = cells(line)
        if c is None:
            header = None
            continue
        if header is None:
            header = c
            continue
        if all(re.fullmatch(r":?-{3,}:?", x or "---") for x in c):
            continue
        row = dict(zip(header, c))
        m = re.fullmatch(r"docs/(CONTRACT|SPEC|PRD)\.md", row.get("Path", ""))
        if not m:
            continue
        doc = m.group(1)
        rec = row.get("ActualSHA256", "")
        if not HEX.match(rec):
            rec = row.get("ExpectedSHA256", "")
        rec = rec if HEX.match(rec) else "NOT_RECORDED"
        verdict = row.get("Status", "").strip() or "NOT_RECORDED"
        if doc not in out or (out[doc][0] == "NOT_RECORDED" and rec != "NOT_RECORDED"):
            out[doc] = (rec, verdict)
    return out


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
    recomputed = {d: hashlib.sha256(open(os.path.join(a.frozen, "projects/chirality-app-dev/docs", f"{d}.md"), "rb").read()).hexdigest()
                  for d in DOCS}
    rows = []
    for r in inv:
        refs = parse_refs(os.path.join(a.frozen, r["Path"], "_REFERENCES.md"))
        for d in DOCS:
            rec, verdict = refs.get(d, ("NOT_RECORDED", "NOT_RECORDED"))
            match = "NOT_RECORDED" if rec == "NOT_RECORDED" else ("YES" if rec == recomputed[d] else "NO")
            rows.append((r["DeliverableID"], d, rec, verdict, recomputed[d], match))
    rows.sort(key=lambda x: (x[0], x[1]))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["DeliverableID", "Document", "RecordedSha256", "RecordedVerdict", "RecomputedSha256", "Match"])
    w.writerows(rows)
    buf.write("#END\n")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "w", encoding="utf-8", newline="").write(buf.getvalue())


if __name__ == "__main__":
    main()
