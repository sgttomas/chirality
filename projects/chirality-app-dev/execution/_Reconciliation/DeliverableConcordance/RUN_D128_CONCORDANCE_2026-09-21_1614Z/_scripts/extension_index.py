#!/usr/bin/env python3
"""Build EXTENSION_INDEX.csv: the coverage checklist for the R0-gate scope extension
(D-APP-129 item D; CONVENTIONS.md §8), items 3-7.

Deterministic; no model judgment. Reads the frozen tree (a checkout at 00115c719) and
writes one row per audit unit:

- Item 3  DEC:D-APP-nnn   every `_REGISTER.md` row D-APP-86..D-APP-127 whose State cell
                          starts with `RULED` (RULED, RULED / ..., RULED (...))
- Item 4  DOC:<DOCID>#<n> every `##`/`###` heading of BUILDREL, RQGATES, VALSTRAT, RQRUN,
                          RELIANCE (n = 1-based ordinal in file order); plus `#0` for the
                          preamble between the `#` title and the first `##`/`###` heading
                          when it holds non-blank text
- Item 5  SOW:SOW-nnn     every row of `## 9. Scope Ledger` in the v3.2 decomposition
- Item 6  DOC:PRODAGENTS#<n>  as item 4, for `instructions/AGENTS.md`
- Item 7  DOC:<STEM>#<n>  as item 4, for each `frontend/docs/harness/*.md`
                          (DOCID = uppercase file stem)

Headings inside fenced code blocks are ignored. Paths are repo-relative.
Output: header `UnitKey,Item,SourcePath,SourceLine,Label`, rows, then `#END`.

Usage: extension_index.py --frozen <frozen-tree-root> --out R1_INVENTORY/EXTENSION_INDEX.csv
"""
import argparse, csv, glob, io, os, re, sys

APP = "projects/chirality-app-dev"
REGISTER = f"{APP}/execution/_Coordination/_DECISIONS/_REGISTER.md"
DECOMP = f"{APP}/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
ITEM4 = [
    ("BUILDREL", f"{APP}/docs/BUILD_AND_RELEASE.md"),
    ("RQGATES", f"{APP}/docs/RELEASE_QUALITY_GATES.md"),
    ("VALSTRAT", f"{APP}/docs/VALIDATION_STRATEGY.md"),
    ("RQRUN", f"{APP}/docs/RELEASE_QUALITY_RUNBOOK.md"),
    ("RELIANCE", f"{APP}/docs/harness/reliance_boundary_register.md"),
]
ITEM6 = [("PRODAGENTS", f"{APP}/instructions/AGENTS.md")]
ITEM7_GLOB = f"{APP}/frontend/docs/harness/*.md"
DEC_LO, DEC_HI = 86, 127
HEADING = re.compile(r"^(#{2,3}) (.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def lines_of(root, rel):
    return open(os.path.join(root, rel), encoding="utf-8").read().split("\n")


def clean(label):
    return re.sub(r"\s+", " ", label).strip()[:160]


def dec_units(root):
    out = []
    for i, line in enumerate(lines_of(root, REGISTER), 1):
        if not line.startswith("| D-APP-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        m = re.match(r"^D-APP-(\d+)$", cells[0])
        if not m or not (DEC_LO <= int(m.group(1)) <= DEC_HI) or len(cells) < 4:
            continue
        if cells[3].startswith("RULED"):
            out.append((f"DEC:{cells[0]}", 3, REGISTER, i, clean(cells[1])))
    return out


def doc_units(root, docid, rel, item):
    out, fenced, first_heading, title_line = [], False, None, None
    lines = lines_of(root, rel)
    n = 0
    for i, line in enumerate(lines, 1):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if fenced:
            continue
        if title_line is None and line.startswith("# "):
            title_line = i
            continue
        m = HEADING.match(line)
        if m:
            if first_heading is None:
                first_heading = i
            n += 1
            out.append((f"DOC:{docid}#{n}", item, rel, i, clean(m.group(1) + " " + m.group(2))))
    start = title_line or 0
    stop = (first_heading or len(lines) + 1) - 1
    body = [l for l in lines[start:stop] if l.strip()]
    if body:
        out.insert(0, (f"DOC:{docid}#0", item, rel, start + 1, "(preamble)"))
    return out


def sow_units(root):
    out, inside = [], False
    for i, line in enumerate(lines_of(root, DECOMP), 1):
        if line.startswith("## "):
            inside = line.strip() == "## 9. Scope Ledger"
            continue
        if inside:
            m = re.match(r"^\| (SOW-\d{3}) \| ([A-Z]+) \| ([^|]*)\|", line)
            if m:
                out.append((f"SOW:{m.group(1)}", 5, DECOMP, i, clean(f"{m.group(2)}: {m.group(3)}")))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows = dec_units(a.frozen)
    for docid, rel in ITEM4:
        rows += doc_units(a.frozen, docid, rel, 4)
    rows += sow_units(a.frozen)
    for docid, rel in ITEM6:
        rows += doc_units(a.frozen, docid, rel, 6)
    for path in sorted(glob.glob(os.path.join(a.frozen, ITEM7_GLOB))):
        rel = os.path.relpath(path, a.frozen).replace(os.sep, "/")
        stem = os.path.splitext(os.path.basename(path))[0].upper()
        rows += doc_units(a.frozen, stem, rel, 7)
    keys = [r[0] for r in rows]
    dup = {k for k in keys if keys.count(k) > 1}
    assert not dup, f"duplicate unit keys: {sorted(dup)}"
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["UnitKey", "Item", "SourcePath", "SourceLine", "Label"])
    w.writerows(rows)
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        fh.write(buf.getvalue() + "#END\n")
    counts = {}
    for r in rows:
        counts[r[1]] = counts.get(r[1], 0) + 1
    docs = {}
    for r in rows:
        if r[0].startswith("DOC:"):
            d = r[0][4:].split("#")[0]
            docs[d] = docs.get(d, 0) + 1
    print("total", len(rows), "per item", dict(sorted(counts.items())))
    print("per DOCID", dict(sorted(docs.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
