#!/usr/bin/env python3
"""Finalize Gate-1 deterministic registers: Companion_Inventory.csv and
Open_Issues_Register.csv for the chirality-piping domain pack.

Reads the intake registers produced by run_intake.py and emits the two
remaining companion registers. The main control-surface markdown is authored at
Gate 6.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[2]
DECOMP = PACK_ROOT / "_Decomposition"
PACK_REL = "domains/chirality-piping"
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
    tel = json.loads((DECOMP / "Intake_Telemetry.json").read_text(encoding="utf-8"))
    n_units = tel["atomizable_source_units"]
    n_sec = tel["total_sections"]
    n_disp = tel["dispatch_units"]
    n_idx = tel["index_only_files"]
    n_manifest = tel["manifest_file_rows"]

    companion = []
    static = [
        ("_Sources/Source_Manifest.csv", "authoritative companion register",
         f"File-level source-admission manifest ({n_manifest} rows) with SHA-256."),
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
         "Index-only files (schemas + api contract + docs manifest): retrieval-visible, not atomized."),
        ("_Decomposition/Open_Issues_Register.csv", "authoritative companion register",
         "Gate-1 open issues and required human rulings."),
        ("_Decomposition/Validation_Checks.csv", "authoritative companion register",
         "Phase-1 validation checks."),
        ("_Decomposition/Companion_Inventory.csv", "authoritative companion register",
         "This inventory of the canonical working package."),
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
        ("OI-001", "AWAITING_GATE_1", "MAJOR", "source code admission",
         "Live code (~330 files across core/apps/tests/tools/validation, 3 languages) admitted as FIVE grouped atomized source units (one per top-level code folder) per operator direction; each file is one section in the grouped pack.",
         "Operator confirms code is AtomizeInV1=YES as 5 grouped units (COMPONENT_MAP provenance).",
         "Code-comment lines are indented in pack markdown so they are never misparsed as Markdown headings -> one section per code file; .md components keep structure."),
        ("OI-002", "AWAITING_GATE_1", "MAJOR", "process logs + deliverable meta docs",
         "Process logs (TASK_RUN_*=913, RUN_SUMMARY, Decision_Log, Brief, _REVIEW, QA_Report) and deliverable meta docs (_SEMANTIC/_SEMANTIC_LENSING/_CONTEXT/_DEPENDENCIES/_REFERENCES/_STATUS/MEMORY) excluded entirely (not indexed) per operator direction.",
         "Human confirms process provenance + deliverable meta are out of the V1 corpus.",
         "Leave excluded; they remain in the live repo and can be admitted in a future scope-change cycle."),
        ("OI-003", "AWAITING_GATE_1", "MAJOR", "execution deliverable admission",
         "Each deliverable admits its four canonical knowledge-type docs by basename suffix (Datasheet/Specification/Guidance/Procedure) -> 101 source units, 404 component files. Non-KT files not admitted.",
         "Operator confirms deliverable admission (4 KT docs/deliverable) + per-deliverable grouping.",
         "404 deliverable component files admitted across 101 units."),
        ("OI-004", "AWAITING_GATE_1", "MAJOR", "execution governance scope",
         "Execution governance restricted to _Decomposition/ + _ScopeChange/ (9 docs -> 5 grouped units). _DAG, _Aggregation, _Evaluation, _Reconciliation, _Coordination, _Change excluded as process provenance per operator direction.",
         "Operator confirms only _Decomposition + _ScopeChange carry decomposable knowledge.",
         "REVIEW_HANDOFF_TO_NEXT_INSTANCE.md removed per the NEXT_INSTANCE/NEXT_SESSION exclusion rule (inter-session coordination, not knowledge)."),
        ("OI-005", "AWAITING_GATE_1", "MINOR", "schemas + fixtures disposition",
         f"schemas/*.{{yaml,json}} (36) + api contract + docs/MANIFEST.json admitted INDEX-ONLY ({n_idx} files); fixtures/ test data excluded entirely.",
         "Operator confirms schemas are retrieval-visible but not atomized, fixtures excluded.",
         "Schemas atomize poorly via the heading-based tooling; retrieval catalog still indexes them as domain models."),
        ("OI-006", "RECORDED", "INFO", "cross-repo SourceRef",
         "Pack lives in the monorepo (domains/chirality-piping) while sources live in projects/chirality-piping; @repo resolves against the source repo.",
         "No action; recorded for Phase 2.5 catalog build (--repo-root projects/chirality-piping).",
         "Pass --repo-root projects/chirality-piping to build/validate_source_database.py."),
        ("OI-007", "ACCEPTED_GATE_1", "MINOR", "Gate 1.5 asset surfaces",
         "Per-kind asset surfaces (equations/figures/tables/images/folios) and the 1.5-P prose-validate prefilter are N/A for this markdown+code corpus (no PDF-extracted assets).",
         "Human accepts that Gate 1.5 reduces to 1.5-S skeleton review only.",
         "Use structure-mode section review HTML only; asset manifests carry no assets."),
        ("OI-008", "ACCEPTED_STAGE_PHASE_2", "MAJOR", "Phase 2 staging",
         f"{n_units} source units / {n_sec} sections / {n_disp} dispatch units; operator accepts staged atomization batches.",
         "Run staged atomization batches after Gate 1 (e.g. docs+root first, then deliverables by PKG, then governance + code units).",
         "Batches of 4-8 dispatch units run in parallel to disjoint per-unit CSV paths."),
        ("OI-009", "ACCEPTED_GATE_1", "INFO", "in-scope heuristic",
         f"All {n_sec} admitted sections default in-scope (no book-style front/back-matter detected). Grouped-unit pack-boilerplate headers (## Source Pack) will be trimmed OUT at Gate 1.5-S.",
         "Refine at Gate 1.5-S where the human tags any residual out-of-scope sections.",
         "No front-matter overrides applied at intake; review_15s applies pack-boilerplate trim (R2)."),
        ("OI-010", "RESOLVED_GATE_1", "MINOR", "INIT.md",
         "INIT.md is a session-bootstrap launcher (3 lines: read X, adopt WORKING_ITEMS persona) with no headings and no decomposable knowledge.",
         "Resolved: excluded from the V1 corpus.",
         "Bootstrap launchers are operational, not domain knowledge."),
    ]
    write_csv(DECOMP / "Open_Issues_Register.csv", OPEN_ISSUE_FIELDS,
              [dict(zip(OPEN_ISSUE_FIELDS, row)) for row in issues])

    print(f"companion_rows={len(companion)} open_issues={len(issues)} "
          f"units={n_units} sections={n_sec} dispatch={n_disp} index_only={n_idx}")


if __name__ == "__main__":
    raise SystemExit(main())
