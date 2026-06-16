#!/usr/bin/env python3
"""Finalize Gate-1 deterministic registers: Companion_Inventory.csv and
Open_Issues_Register.csv for the chirality-app-dev domain pack.

Reads the intake registers produced by run_intake.py and emits the two
remaining companion registers. The main control-surface markdown and the gate
snapshot are authored/created separately.
"""
from __future__ import annotations
import csv
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[2]
DECOMP = PACK_ROOT / "_Decomposition"
PACK_REL = "domains/chirality-app-dev"
COMPANION_FIELDS = ["Filename", "PackageRole", "Description"]
OPEN_ISSUE_FIELDS = ["IssueID", "Status", "Severity", "Surface", "Issue",
                     "RequiredDisposition", "Recommendation"]


def read_csv(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(p, fields, rows):
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows([{k: r.get(k, "") for k in fields} for r in rows])


def main():
    prefix_rows = read_csv(DECOMP / "Source_Decomp_Prefix_Map.csv")

    companion = []
    static = [
        ("_Sources/Source_Manifest.csv", "authoritative companion register",
         "File-level source-admission manifest (467 rows) with SHA-256."),
        ("_Sources/SOURCE_BOUNDARY.md", "authoritative companion register",
         "V1 source boundary: included/excluded/index-only rules and source groups."),
        ("_Decomposition/Source_Decomp_Prefix_Map.csv", "authoritative companion register",
         "Per source-unit prefix map, grouping, SourceRef adapter metadata, and companion paths."),
        ("_Decomposition/Source_Unit_Component_Map.csv", "authoritative companion register",
         "Grouped source-unit -> @repo component file provenance (line offsets)."),
        ("_Decomposition/Intake_Telemetry.csv", "authoritative companion register",
         "Per source-unit intake/skeleton/section/dispatch telemetry."),
        ("_Decomposition/Intake_Telemetry.json", "authoritative companion register",
         "Phase-1 intake summary telemetry."),
        ("_Decomposition/Index_Only_Register.csv", "authoritative companion register",
         "Index-only files (frontend src + MANIFEST.json): retrieval-visible, not atomized."),
        ("_Decomposition/Open_Issues_Register.csv", "authoritative companion register",
         "Gate-1 open issues and required human rulings."),
        ("_Decomposition/Validation_Checks.csv", "authoritative companion register",
         "Phase-1 validation checks."),
        ("_Decomposition/Companion_Inventory.csv", "authoritative companion register",
         "This inventory of the canonical working package."),
        ("_Decomposition/Chirality_App_Dev_Domain_Decomposition.md", "working surface",
         "Main control surface and Gate-1 confirmation packet."),
        ("_Decomposition/_adapter/", "snapshot / handoff artifact",
         "Pack-local Phase-1 intake adapter scripts (build_manifest.py, run_intake.py, finalize_gate1.py)."),
    ]
    for fn, role, desc in static:
        companion.append({"Filename": f"{PACK_REL}/{fn}", "PackageRole": role, "Description": desc})

    for r in prefix_rows:
        uid = r["SourceUnitID"]
        for col, desc in [("AssetManifestPath", "asset/component manifest"),
                          ("SkeletonPath", "source skeleton"),
                          ("DispatchPlanPath", "dispatch plan"),
                          ("ReviewHtmlPath", "structure review HTML"),
                          ("SectionNodesPath", "section-node retrieval substrate"),
                          ("PackMarkdownPath", "generated grouped pack markdown")]:
            v = r.get(col, "")
            if v:
                companion.append({"Filename": f"{PACK_REL}/{v}",
                                  "PackageRole": "authoritative companion register",
                                  "Description": f"{desc} for {uid}."})
    write_csv(DECOMP / "Companion_Inventory.csv", COMPANION_FIELDS, companion)

    issues = [
        ("OI-001", "RESOLVED_GATE_1", "MAJOR", "frontend/src",
         "frontend application source (147 files) grouped into ONE atomized source unit (SRC-FRONTEND-SRC) per operator direction.",
         "Resolved: FRONTEND_SRC is AtomizeInV1=YES as a single grouped unit (COMPONENT_MAP provenance).",
         "Code is atomized within one source unit; headingless code yields one section per component file."),
        ("OI-002", "ACCEPTED_GATE_1", "MAJOR", "execution process logs",
         "~350 process-log files (_run_records/TASK_RUN_*, RUN_SUMMARY, Decision_Log) excluded entirely (not indexed) by operator direction.",
         "Human confirms process provenance is out of the V1 corpus.",
         "Leave excluded; they remain in the live repo and can be admitted in a future scope-change cycle."),
        ("OI-003", "AWAITING_GATE_1", "MAJOR", "execution deliverable admission+grouping",
         "REVISED (Gate 1 reopened): each deliverable admits its knowledge-type docs by basename SUFFIX (Datasheet/Specification/Guidance/Procedure, incl. nested Packet_/Case_) -> 53 source units, 238 component files; meta docs and other non-KT files are NOT admitted. Governance grouped by folder (26 units).",
         "Operator confirms revised deliverable admission (KT docs by suffix) + grouping.",
         "238 deliverable component files admitted; the 6 meta docs per deliverable excluded from admission."),
        ("OI-004", "ACCEPTED_GATE_1", "MINOR", "Gate 1.5 asset surfaces",
         "Per-kind asset surfaces (equations/figures/tables/images/folios) and the 1.5-P prose-validate prefilter are N/A for this markdown-only corpus.",
         "Human accepts that Gate 1.5 reduces to 1.5-S skeleton review only.",
         "Use structure-mode section review HTML only; no asset manifests carry assets."),
        ("OI-005", "RECORDED", "INFO", "cross-repo SourceRef",
         "Pack lives in the monorepo (domains/chirality-app-dev) while sources live in projects/chirality-app-dev; @repo resolves against the source repo.",
         "No action; recorded for Phase 2.5 catalog build (--repo-root projects/chirality-app-dev).",
         "Pass --repo-root projects/chirality-app-dev to build/validate_source_database.py."),
        ("OI-006", "ACCEPTED_OPTION_A", "MAJOR", "PKG-00 closure deliverables",
         "Under suffix-match admission (OI-009), DEL-00-02 re-admits byte-identical duplicate packets (scc-cases/case-seeds copies mirror scope-change-packets copies of PKG00-SCA-PACKET-002|003|004).",
         "Option A: leave both copies; identical atoms collapse via ContentHash dedup at the Gate-2 merge.",
         "Confirm dedup behavior during Gate 2; no action at intake."),
        ("OI-007", "ACCEPTED_STAGE_PHASE_2", "MAJOR", "Phase 2 staging",
         "96 source units / 3,056 sections / 108 dispatch units; operator accepts staged batches.",
         "Run staged atomization batches after Gate 1 (e.g. by SourceGroup / PKG).",
         "Stage docs+root first, then execution deliverables by PKG, then governance + frontend-src + frontend docs."),
        ("OI-008", "ACCEPTED_GATE_1", "INFO", "in-scope heuristic",
         "All 3,056 admitted sections default in-scope (no front/back-matter detected) since these are not book-style sources.",
         "Refine at Gate 1.5-S where the human tags any residual out-of-scope sections.",
         "No front-matter overrides applied at intake; deliverable scope-trim now handled at admission."),
        ("OI-009", "RESOLVED_SUFFIX_MATCH", "MAJOR", "deliverable meta-doc + nested-packet admission",
         "Operator chose SUFFIX-MATCH admission: deliverable KT docs admitted by basename suffix (Datasheet/Specification/Guidance/Procedure), so DEL-00-01/02 re-admit 26 nested Packet_/Case_ KT docs (DEL-00-01: 4->11, DEL-00-02: 4->23). Meta docs (_SEMANTIC etc.) and non-KT files (Packet_QA/Rationale/Contract, CONTROL/README, SCOPE_CHANGE_INIT) remain excluded.",
         "Resolved: 238 deliverable component files admitted across 53 units.",
         "Duplicate nested packets handled by OI-006 Option A (ContentHash dedup at Gate 2)."),
    ]
    write_csv(DECOMP / "Open_Issues_Register.csv", OPEN_ISSUE_FIELDS,
              [dict(zip(OPEN_ISSUE_FIELDS, row)) for row in issues])

    print(f"companion_rows={len(companion)} open_issues={len(issues)}")


if __name__ == "__main__":
    raise SystemExit(main())
