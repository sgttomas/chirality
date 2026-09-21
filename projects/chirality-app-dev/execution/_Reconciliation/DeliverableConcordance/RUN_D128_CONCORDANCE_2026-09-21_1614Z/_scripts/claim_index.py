#!/usr/bin/env python3
"""Build CLAIM_INDEX.csv: the 100%-coverage checklist of audit units for RUN_D128.

Deterministic; no model judgment. Reads the frozen source state (a checkout at the
pinned basis) and writes one row per audit unit:

- CLM   every `### CLM-NNN` heading in a ScopeOfWork.md            -> DEL-xx-yy#CLM-NNN
- SEC   every other `### ` heading inside a non-standard `## ` section,
        or a whole ontology/epistemology/praxeology/axiology/non-standard
        section that has no `### ` headings                          -> DEL-xx-yy#SEC-n
- REM   every top-level bullet in `_STATUS.md ## Remaining`
        (the D-APP-128 bootstrap item is excluded)                   -> DEL-xx-yy#REM-n
- REMTXT every non-bullet prose paragraph in `## Remaining`
        other than a lone `None.`                                    -> DEL-xx-yy#REMTXT-n

Usage: claim_index.py --project-root <checkout>/projects/chirality-app-dev --out CLAIM_INDEX.csv
"""
import argparse, csv, glob, os, re

EVIDENCE_ONLY = {"Purpose and Objective Traceability", "Output and Evaluation Matrix"}
STANDARD = {
    "Deliverable Definition — Ontology",
    "Completion and Reliance Basis — Epistemology",
    "Production and Verification Method — Praxeology",
    "Governing Values and Decisions — Axiology",
}
CLM = re.compile(r"^### (CLM-\d{3})\b\s*[—-]?\s*(.*)$")
BOOTSTRAP = "(gated: D-APP-128)"


def sow_units(path, del_id):
    rows, sec_n = [], 0
    section, section_line, section_has_sub = None, 0, False
    lines = open(path, encoding="utf-8").read().split("\n")

    def close_section():
        nonlocal sec_n
        if section and section not in EVIDENCE_ONLY and not section_has_sub:
            sec_n += 1
            rows.append((f"{del_id}#SEC-{sec_n}", "SEC", f"SEC-{sec_n}", section, "", section_line))

    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            close_section()
            section, section_line, section_has_sub = line[3:].strip(), i, False
            continue
        if line.startswith("### ") and section:
            section_has_sub = True
            m = CLM.match(line)
            if m:
                rows.append((f"{del_id}#{m.group(1)}", "CLM", m.group(1), section, m.group(2).strip(), i))
            elif section not in STANDARD and section not in EVIDENCE_ONLY:
                sec_n += 1
                rows.append((f"{del_id}#SEC-{sec_n}", "SEC", f"SEC-{sec_n}", section, line[4:].strip(), i))
    close_section()
    return rows


def remaining_units(path, del_id):
    lines = open(path, encoding="utf-8").read().split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "## Remaining")
    except StopIteration:
        return []
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    rows, rem_n, txt_n, para = [], 0, 0, None
    for i in range(start + 1, end):
        line = lines[i]
        if line.startswith("- "):
            para = None
            if BOOTSTRAP in line or line.strip() in ("- None.",):
                continue
            rem_n += 1
            rows.append((f"{del_id}#REM-{rem_n}", "REM", f"REM-{rem_n}", "## Remaining", line[2:120].strip(), i + 1))
        elif line.strip() and not line.startswith((" ", "\t")) and para is None:
            if line.strip() == "None.":
                continue
            txt_n += 1
            para = txt_n
            rows.append((f"{del_id}#REMTXT-{txt_n}", "REMTXT", f"REMTXT-{txt_n}", "## Remaining", line[:120].strip(), i + 1))
        elif not line.strip():
            para = None
    return rows


SUBITEM = re.compile(r"^(?:> )?(?:- \*\*|\| *)((?:REQ|AC|VER)-\d{3})\b")


def attach_subitems(path, rows):
    """Append the REQ/AC/VER items defined inside each SoW unit's line span (R0 §7.2 splitting rule)."""
    lines = open(path, encoding="utf-8").read().split("\n")
    starts = sorted(r[5] for r in rows)
    out = []
    for r in rows:
        nxt = min([x for x in starts if x > r[5]] or [len(lines) + 1])
        # a unit's span ends at the next unit start or the next ## heading
        end = next((i for i in range(r[5], nxt - 1) if lines[i].startswith("## ")), nxt - 1)
        subs = []
        for l in lines[r[5]:end]:
            m = SUBITEM.match(l)
            if m and m.group(1) not in subs:
                subs.append(m.group(1))
        out.append(r + ("|".join(subs),))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-root", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = []
    for d in sorted(glob.glob(os.path.join(a.project_root, "execution/PKG-*/1_Working/DEL-*"))):
        del_id = os.path.basename(d)[:9]
        pkg = os.path.basename(os.path.dirname(os.path.dirname(d)))[:6]
        sow = os.path.join(d, "ScopeOfWork.md")
        for key, kind, local, sec, label, line, subs in attach_subitems(sow, sow_units(sow, del_id)):
            out.append([key, pkg, del_id, kind, local, "ScopeOfWork.md", line, sec, label, subs])
        for key, kind, local, sec, label, line in remaining_units(os.path.join(d, "_STATUS.md"), del_id):
            out.append([key, pkg, del_id, kind, local, "_STATUS.md", line, sec, label, ""])
    keys = [r[0] for r in out]
    assert len(keys) == len(set(keys)), "duplicate claim keys"
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["ClaimKey", "PackageID", "DeliverableID", "UnitKind", "LocalID", "SourceFile", "SourceLine", "Section", "Label", "SubItems"])
        w.writerows(out)
    kinds = {}
    for r in out:
        kinds[r[3]] = kinds.get(r[3], 0) + 1
    print(len(out), kinds, len({r[2] for r in out}), "deliverables")


if __name__ == "__main__":
    main()
