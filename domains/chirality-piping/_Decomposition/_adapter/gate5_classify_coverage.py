#!/usr/bin/env python3
"""Gate 5 zero-coverage classification + attestation for chirality-piping.

Operator decision: machine-classify cov-empty in-scope sections, auto-attest the
structural/boilerplate ones, and surface only genuine-gap candidates for review.

For each cov-empty (INAtomCount==0) in-scope section in Section_Coverage_Register.csv:
  STRUCTURAL_COMPONENT_HEADER  title starts "Component:" or "Source Pack" (grouped
                               pack boundary/header — holds no atoms by design)
  STRUCTURAL_PARENT            a descendant section (by line-range containment in the
                               same source) carries IN atoms — atoms live in children
  OUT_TBD_ONLY                 section has only OUT/TBD atoms (TotalAtomCount>0) —
                               in-scope but content dispositioned OUT/TBD (ties OI-013)
  TEMPLATE_SUBSECTION          leaf, 0 atoms, but a standard empty KT-doc template
                               header (References/Records/Known TBDs/Baseline/...) —
                               scaffold-for-fill empty template slot
  GENUINE_GAP_CANDIDATE        leaf, in-scope, 0 atoms, not a known template header —
                               surfaced for operator review

The structural / OUT_TBD / template buckets are bulk-attested ACCEPTED_GATE5
(scaffold-for-fill / boilerplate). GENUINE_GAP_CANDIDATE rows are listed for review.
Writes AttestationStatus/AttestationNote back into Section_Coverage_Register.csv,
emits Gate5_ZeroCoverage_Classification.csv + Gate5_GenuineGap_Shortlist.csv.

Usage:  python3 _adapter/gate5_classify_coverage.py
Run with cwd = MONOREPO_ROOT. Prints a JSON summary.
"""
from __future__ import annotations
import csv, json, io
from pathlib import Path
from collections import defaultdict, Counter

MONO = Path.cwd()
DEC = MONO / "domains/chirality-piping/_Decomposition"
REG = DEC / "Section_Coverage_Register.csv"

TEMPLATE_HEADERS = {
    "references", "records", "known tbds", "baseline", "acceptance criteria",
    "evidence inventory", "substantiation boundary", "affected deliverables",
    "action candidates", "gate-by-gate use", "row-specific procedure",
    "records required after human-initiated scope_change", "notes", "scope",
    "inputs", "outputs", "exceptions", "preconditions", "quality checks",
    "decision points", "options", "principles", "when to use", "do/don't",
    "related concepts", "fields/sections", "instructions", "examples", "checklist items",
}


def truthy(v): return str(v).strip().lower() in ("true", "1", "yes")


def main():
    rows = list(csv.DictReader(open(REG, encoding="utf-8")))
    fields = list(rows[0].keys())

    # per-source sections with IN atoms, for descendant containment
    by_src = defaultdict(list)
    for r in rows:
        by_src[r["SourceDocID"]].append(r)

    def has_in_descendant(sec, src_rows):
        try:
            ls, le, d = int(sec["LineStart"]), int(sec["LineEnd"]), int(sec["Depth"])
        except ValueError:
            return False
        for o in src_rows:
            if o is sec:
                continue
            try:
                ols, ole, od = int(o["LineStart"]), int(o["LineEnd"]), int(o["Depth"])
            except ValueError:
                continue
            if od > d and ols >= ls and ole <= le and int(o["INAtomCount"]) > 0:
                return True
        return False

    cls_counts = Counter()
    classification = []
    shortlist = []
    for r in rows:
        if not truthy(r["InScope"]) or r["CoverageClass"] != "cov-empty":
            # non-empty in-scope already accepted by the builder; leave as-is
            if truthy(r["InScope"]) and int(r["INAtomCount"]) > 0 and not r.get("AttestationStatus"):
                r["AttestationStatus"] = "ACCEPTED_GATE5_NONZERO"
                r["AttestationNote"] = ""
            continue
        title = r["Title"].strip()
        tl = title.lower()
        total = int(r["TotalAtomCount"])
        if tl.startswith("component:") or tl.startswith("source pack"):
            cls = "STRUCTURAL_COMPONENT_HEADER"
        elif total > 0:
            cls = "OUT_TBD_ONLY"
        elif has_in_descendant(r, by_src[r["SourceDocID"]]):
            cls = "STRUCTURAL_PARENT"
        elif tl in TEMPLATE_HEADERS:
            cls = "TEMPLATE_SUBSECTION"
        else:
            # leaf, 0 atoms: distinguish empty header stub (scaffold-for-fill) from a
            # section with substantial un-atomized source text (genuine gap candidate).
            try:
                span = int(r["LineSpan"])
            except ValueError:
                span = 0
            cls = "GENUINE_GAP_CANDIDATE" if span > 8 else "EMPTY_STUB_SCAFFOLD"
        cls_counts[cls] += 1
        if cls == "GENUINE_GAP_CANDIDATE":
            r["AttestationStatus"] = "PENDING_GENUINE_GAP_REVIEW"
            r["AttestationNote"] = "leaf in-scope section, 0 atoms, non-template header — review"
            shortlist.append(r)
        else:
            r["AttestationStatus"] = "ACCEPTED_GATE5_SCAFFOLD_FOR_FILL"
            r["AttestationNote"] = f"{cls}: auto-attested (structural/boilerplate/OUT-TBD, not a Phase-2 gap)."
        classification.append({"SourceDocID": r["SourceDocID"], "SectionID": r["SectionID"],
                               "Depth": r["Depth"], "Title": title, "TotalAtomCount": total,
                               "Classification": cls, "AttestationStatus": r["AttestationStatus"]})

    # write back register
    buf = io.StringIO(); w = csv.DictWriter(buf, fieldnames=fields); w.writeheader(); w.writerows(rows)
    REG.write_text(buf.getvalue(), encoding="utf-8")
    # classification + shortlist
    with open(DEC / "Gate5_ZeroCoverage_Classification.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["SourceDocID", "SectionID", "Depth", "Title",
                                          "TotalAtomCount", "Classification", "AttestationStatus"])
        w.writeheader(); w.writerows(classification)
    with open(DEC / "Gate5_GenuineGap_Shortlist.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["SourceDocID", "SectionID", "Depth", "Title", "RepoRelPath"])
        for r in shortlist:
            w.writerow([r["SourceDocID"], r["SectionID"], r["Depth"], r["Title"], r["RepoRelPath"]])

    summary = {"cov_empty_in_scope": sum(cls_counts.values()),
               "classification": dict(cls_counts),
               "genuine_gap_candidates": len(shortlist),
               "genuine_gap_title_freq": Counter(r["Title"].strip() for r in shortlist).most_common(15)}
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
