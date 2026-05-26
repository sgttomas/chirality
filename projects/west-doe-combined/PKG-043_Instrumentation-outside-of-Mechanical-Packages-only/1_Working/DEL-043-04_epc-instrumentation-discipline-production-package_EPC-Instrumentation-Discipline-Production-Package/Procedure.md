# Procedure — DEL-043-04 EPC / Instrumentation Discipline Production Package

## Purpose

Operational procedure to produce the EPC / Instrumentation Discipline Production Package for `PKG-043` (Instrumentation outside of Mechanical Packages only). This procedure covers how to assemble the discipline production-unit basis, the (TBD) discipline deliverable register, and the source-limited requirements closure record (source: `DELIVERABLE_REGISTER.csv` row DEL-043-04 AnticipatedArtifacts).

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` for this deliverable.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (source: `_REFERENCES.md`).
- No declared upstream dependencies during PREPARATION (source: `_DEPENDENCIES.md`). Any later-declared upstream items must be reflected here.
- TBD: locally accessible slice of Workbook Packages row 45 and `DBM-Deepcut/4-25_Deepcut_DBM.md`. Production-quality closure requires these slices (source: `_REFERENCES.md` Missing/Deferred References; `PACKAGE_REGISTER.csv` SourceRef).
- Companion package deliverables for situational awareness: `DEL-043-01_scope-of-work`, `DEL-043-02_package-datasheet`, `DEL-043-03_construction-work-package` (source: `DELIVERABLE_REGISTER.csv` rows under PKG-043).

## Steps

1. **Confirm identity and scope.** Verify deliverable identity from `_CONTEXT.md` and the row in `DELIVERABLE_REGISTER.csv` for DEL-043-04. Confirm PKG-043 attributes from `PACKAGE_REGISTER.csv`.
2. **Enumerate scope items and objectives.** Record `SOW-0044` coverage and the six supported objectives from `OBJECTIVE_DELIVERABLE_MAP.csv`. Treat objective association as ASSUMPTION (PACKAGE_HEURISTIC) unless human confirms.
3. **Cross-walk interfaces.** For each of the five package-level interface rows in `INTERFACE_REGISTER.csv` (IFC-AE83B2D0FC, IFC-F41620D435, IFC-E5A8000199, IFC-4929B68CCD, IFC-35EBF9CD91), note any discipline-production implications and ensure the Gate 6 plug-n-play disposition is honored.
4. **Draft the Discipline Production Package basis.** Capture the production-unit's role (non-vendor, conservatively carried) and how it covers package scope outside Mechanical Packages. Cite sources for each statement.
5. **Draft the discipline deliverable register (TBD content).** Enumerate candidate discipline deliverables only where source-supported; otherwise list as TBD with the reason and Gate 5 referral.
6. **Draft the source-limited requirements closure record.** For each anticipated requirement, record: requirement text, source slice (or `location TBD`), disposition (closed / Gate 5 referral / TBD).
7. **Coordinate responsibility allocation.** Surface the TBD responsibility allocation (EPC Integrator vs. discipline subcontractor) for human ruling; do not pre-allocate.
8. **Run consistency check.** Compare Datasheet, Specification, Guidance, and Procedure for consistent terminology, identifiers, and values. Resolve from sources or escalate to the Conflict Table.
9. **Refer outstanding items to Gate 5.** Compile the TBD list for Gate 5 disposition.

## Verification

- All anticipated artifacts from `DELIVERABLE_REGISTER.csv` row DEL-043-04 have a corresponding draft section or explicit TBD with Gate 5 referral.
- Every package interface row for PKG-043 is addressed (covered or explicit TBD).
- All non-trivial statements cite a source slice or are marked `TBD` / `ASSUMPTION`.
- Responsibility allocation is surfaced as TBD, not pre-decided.
- Cross-document consistency check (per Specification verification table) has been performed.

## Records

- Discipline Production Package basis document
- Discipline deliverable register (TBD content as appropriate)
- Source-limited requirements closure record (table of requirement / source slice / disposition)
- Interface coverage cross-walk against `INTERFACE_REGISTER.csv` rows for PKG-043
- Conflict Table entries (in `Guidance.md`) when source disagreement is detected
- Gate 5 disposition referral list (TBD)
