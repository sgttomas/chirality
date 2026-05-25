# Procedure: DEL-027-01_scope-of-work

## Purpose

Operational procedure for producing the EPC Scope of Work for `PKG-027`, the Transformer `TXP-8301-1` STEP DOWN DISTRIBUTION TRANSFORMER (20/26 MVA, 13.8/6.9/0.4 kV) package, in a source-grounded form consistent with the Datasheet, Specification, and Guidance for this deliverable.

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` for this deliverable.
- Access the Gate 7 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` including `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, and `ARTIFACT_REGISTER.csv`.
- Access the workbook source `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 29.
- Access the facility electrical design basis `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, specifically the 13.8 kV switchgear distribution paragraph, the 6.9 kV motor distribution paragraph, the transformers paragraph (foundations, spacing, secondary containment), and the grounding paragraphs (including the "each 6.9 kV transformer" NGR rule).
- No declared upstream dependencies; downstream consumers include DEL-027-02 (Package Datasheet), DEL-027-03 (Construction Work Package), DEL-027-04 (Vendor Engineered Equipment Package), DEL-027-05 (Vendor Document Turnover Package), and DEL-027-06 (EPC Vendor Package Review and Acceptance).

## Steps

1. Confirm package identity using workbook row 29 and `PACKAGE_REGISTER.csv` row `PKG-027`. Record the package name verbatim, including the labelled voltage relationship and rating.
2. Record the tagged equipment list. For `PKG-027`, list `TXP-8301-1` as the single tagged transformer; do not infer additional auxiliaries beyond what is named in source.
3. Draft the package function statement using the DBM electrical distribution paragraphs: 13.8 kV switchgear distributes radially through step-down transformers to the 6.9 kV motor distribution. Frame `TXP-8301-1` as one such step-down transformer.
4. Record the responsibility split exactly as stated in `PACKAGE_REGISTER.csv` row `PKG-027` (Package Vendor versus EPC Integrator scope), without paraphrasing in a way that shifts responsibility.
5. List the applicable interface facts using `INTERFACE_REGISTER.csv` rows for `PKG-027`: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
6. Apply the DBM facility electrical rules that affect this package: the 6.9 kV side neutral grounding via 100 A, 10 s NGR operated as a tripping system; CEC spacing for large oil-filled transformers; structural-steel or precast bearing foundation; secondary containment review.
7. Capture explicit `TBD` items: cooling class (ONAN/ONAF), impedance, BIL, vector group, tap configuration, losses, noise level, oil volume, host electrical building/area, and the technical role of the labelled 0.4 kV winding.
8. Capture explicit `ASSUMPTION` items: oil-filled construction; dual-rating cooling-class interpretation of "20/26 MVA"; mapping of "0.4 kV" to an auxiliary or vendor-specified winding; objective associations carried under `PACKAGE_HEURISTIC`.
9. Cross-check the draft against the Datasheet (identity, attributes, interfaces), the Specification (requirements, verification), and the Guidance (principles, conflicts). Resolve inconsistencies in favour of the cited source; record unresolved conflicts in the Conflict Table in `Guidance.md`.
10. Surface human-ruling items (HRR-027-01-001, HRR-027-01-002, HRR-027-01-003) in the run record so the next-instance state is visible.

## Verification

- Identity completeness: every identity field traces to workbook row 29 or the Gate 7 registers.
- Function narrative fidelity: every function or distribution statement traces to a DBM source slice.
- Interface completeness: all seven `INTERFACE_REGISTER.csv` interface facts for `PKG-027` appear in the Scope of Work.
- Responsibility fidelity: vendor/EPC split language matches `PACKAGE_REGISTER.csv` row `PKG-027`.
- Source fidelity: every non-trivial value or requirement cites a source slice; unsupported values are `TBD` or `ASSUMPTION`.
- Cross-document consistency: package name, tag, voltage/rating labels, interfaces, and TBDs are identical across the four documents.

## Records

- Datasheet, Specification, Guidance, and Procedure files in `{DeliverablePath}`.
- Conflict Table entries in `Guidance.md` (CONF-027-01-001, CONF-027-01-002).
- Human-ruling items (HRR-027-01-001, HRR-027-01-002, HRR-027-01-003) surfaced in the run record for this task.
- TASK run record at `{DeliverablePath}/_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md`.
- Updated `_STATUS.md` (safe `OPEN → INITIALIZED` transition under the Pass 1/2 status rule when applicable).
