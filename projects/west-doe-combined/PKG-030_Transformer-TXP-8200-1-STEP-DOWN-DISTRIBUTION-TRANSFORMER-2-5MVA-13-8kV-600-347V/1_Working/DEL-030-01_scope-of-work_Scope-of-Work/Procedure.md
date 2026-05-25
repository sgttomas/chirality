# Procedure: DEL-030-01 Scope of Work

## Purpose

This procedure describes how the EPC Integrator drafts, reviews, and maintains the Scope of Work for PKG-030 (`TXP-8200-1`, 2.5 MVA 13.8 kV / 600 V step-down distribution transformer) so that it remains source-grounded and consistent with the Gate 7 PROJECT_DECOMP snapshot.

## Prerequisites

- Read access to the deliverable folder: `PKG-030_*/1_Working/DEL-030-01_scope-of-work_Scope-of-Work/`.
- Read access to the accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Read access to the deliverable-local truth set: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Read access to the shared sources at `_Sources/`, in particular the DBM Deepcut document (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) and the workbook export (`_Sources/26020-Packages_Interfaces_4_export.xlsx`, specifically Packages row 32).
- Declared upstream / downstream dependencies: none declared at PREPARATION (`_DEPENDENCIES.md`). Treat unlisted relationships as advisory only.

## Steps

1. **Confirm identity from authoritative sources.** Read workbook Packages row 32 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-030. Confirm package ID, workbook ID, workbook row, WBS, tracking number, discipline, package name spelling, and the seven interface flags.
2. **Confirm deliverable role.** Read Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-030-01_scope-of-work` and the `PROJECT_DECOMP.md` narrative to confirm this deliverable is the mandatory EPC anchor Scope of Work for PKG-030.
3. **Read facility context slices from the DBM Deepcut document.** Required source slices:
   - Electrical System section (utility supply, 13.8 kV switchgear, radial step-down distribution list).
   - System Voltages table (13.8 kV, 4.16 kV, 600 V, 208/120 V rows).
   - Transformers section (CEC spacing, oil-filled installation basis, secondary containment review).
   - Electrical Buildings section (600 V EBs, cable entry, enclosure types).
   - Grounding and Bonding section (600 V transformer neutral grounding by 5 A continuous high-resistance grounding resistor).
4. **Draft `Datasheet.md`.** Populate Identification, Attributes, Conditions, Construction, and References sections using values from the workbook row, Gate 7 register, and DBM source slices. Mark every package-internal design value (vector group, impedance, BIL, taps, cooling, enclosure, dimensions, etc.) as `TBD`.
5. **Draft `Specification.md`.** Generate requirements `SOW-030-01..SOW-030-12` that map identity, responsibility split, interface set, facility context preservation, TBD discipline, secondary-side grounding, destination-EB ambiguity, oil-filled installation basis, and the secondary-system nomenclature discrepancy. Each requirement carries a verification hook against a named source.
6. **Draft `Guidance.md`.** Capture interpretation principles (workbook-authoritative identity, Gate-7-authoritative responsibility split, DBM-authoritative facility context, vendor-authoritative package design), considerations (600 V destination EB, secondary grounding, oil-filled vs dry insulation, lighting interface flag), trade-offs (source fidelity over completeness), and a Conflict Table with `HR-030-01-01` (destination EB), `HR-030-01-02` (600/347 V secondary nomenclature), and `HR-030-01-03` (shared `TXP-8200-1` tag with PKG-016).
7. **Cross-reference consistency (Pass 2).**
   - Confirm Datasheet attributes are reflected in Specification requirements and verification hooks where appropriate.
   - Confirm Specification requirements have rationale or considerations in Guidance.
   - Confirm Specification requirements have verification hooks that align with Procedure.
   - Confirm terminology (`PKG-030`, `TXP-8200-1`, "2.5 MVA", "13.8 kV / 600 V", "high-resistance grounded") is used consistently across all four documents.
   - Confirm numeric values and units (2.5 MVA; 13.8 kV; 600 V; 5 A continuous; 25 kV / 13.8 kV / 50 MVA utility) are consistent across documents and match source values.
   - Re-open DBM source slices when conflicts cannot be resolved from drafts alone.
8. **Update `_STATUS.md` (safe update only).** If current state is `OPEN`, transition to `INITIALIZED` and append a History line citing this run.
9. **Write a run record.** Persist `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` per `AGENT_TASK.md` and the `four-documents` skill contract.

## Verification

- All four documents (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) exist in the deliverable folder with the default schema sections present.
- Every non-trivial claim cites a source from `_REFERENCES.md` or the Gate 7 snapshot, or is marked `TBD` / `ASSUMPTION`.
- Cross-document terminology and values are consistent; remaining conflicts are captured in the `Guidance.md` Conflict Table.
- `_STATUS.md` reflects the safe `OPEN → INITIALIZED` transition with a History line when Pass 1 / Pass 2 ran.
- No files outside the deliverable folder were modified.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in the deliverable folder.
- Updated `_STATUS.md` (safe transition only).
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` documenting inputs, tools, outputs, missing items, and human-ruling items.
