# Procedure: DEL-015-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the procedure for producing the four-document kit and the EPC Vendor Package Review and Acceptance evidence set for `DEL-015-06`, covering the `PKG-015` step-down distribution transformer package (Transformer TXP-8300-1, 12/15MVA, 13.8kV/4160/2400V).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local truth set: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` (placeholder).
- Gate 7 registers: `PACKAGE_REGISTER.csv` (row PKG-015), `DELIVERABLE_REGISTER.csv` (rows DEL-015-01 through DEL-015-06), `INTERFACE_REGISTER.csv` (7 rows for PKG-015), `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `OBJECTIVE_SCOPE_MAP.csv`, `SCOPE_LEDGER.csv` (row SOW-0016).
- Companion deliverable: `DEL-015-02_package-datasheet` (Package Datasheet) in its current state.
- EPC Scope of Work for `PKG-015` (when accessible) — `location TBD`.
- Construction Work Package for `PKG-015` (when accessible) — `location TBD`.
- Vendor data package for `PKG-015` (when accessible) — `location TBD`.
- DBM source slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (site basis lines 96, 100-101, 145, 686; electrical lines 732-768).
- Declared upstream/downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before generating or revising the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against the `DEL-015-06_epc-vendor-package-review-and-acceptance` row in `DELIVERABLE_REGISTER.csv`.
3. Read `PACKAGE_REGISTER.csv` row `PKG-015` and carry forward identity, responsibility split, applicable interfaces, and objective support into the Datasheet.
4. Read `INTERFACE_REGISTER.csv` rows for `PKG-015` (7 entries) and confirm all seven package interfaces (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) appear in the acceptance checklist scope.
5. Read the companion Package Datasheet `DEL-015-02_package-datasheet/` artifacts (when present) to align identity, responsibility split, interface list, and `TBD` set.
6. Read DBM electrical and site-basis slices (3-25, lines 96, 100-101, 145, 686, 732-768) and capture only the conditions and requirements supported by the source slice; do not extend the DBM to cover the 2400 V tap or the 15 MVA upper rating, since the accessible slice does not describe them.
7. Attempt to locate the EPC SoW for `PKG-015` and the Construction Work Package for `PKG-015` in the accessible source set. If absent, mark dependent acceptance criteria as `TBD` and surface in the Guidance Conflict Table.
8. Draft `Datasheet.md` with identity, attributes, conditions, construction, and references. Cite only values supported by accessible sources; preserve unsupported values as `TBD`.
9. Draft `Specification.md` requirements REQ-015-06-01 through REQ-015-06-13 with explicit verification hooks. Cite source clause locations as `TBD` rather than inventing clause references.
10. Draft `Guidance.md` with principles, considerations, trade-offs, illustrative examples, and a Conflict Table that records every unresolved source gap (including HRR-015-06-001 for the 2400 V tap and HRR-015-06-002 for the 12/15 MVA dual rating) as a Human Ruling Required item.
11. Draft this `Procedure.md` so the production and acceptance sequence is repeatable.
12. Vendor review execution (for the operational use of this deliverable, once vendor data exists):
    a. For each vendor document received, log document name, revision, reviewer, disposition, and the EPC SoW / Package Datasheet clause it satisfies (or `TBD`).
    b. For each of the seven package interfaces, record a checklist disposition with a supporting vendor evidence pointer.
    c. For test/inspection (FAT, SAT, dielectric, ratio/polarity, no-load loss, load loss, sound level, grounding/bonding), record evidence pointers and acceptance against EPC SoW criteria (or `TBD`).
    d. For turnover (mechanical-complete, energization-readiness, handover-to-operations), record evidence pointers and acceptance against Construction Work Package criteria (or `TBD`).
    e. Reconcile the 2400 V tap and 12/15 MVA dual rating against the EPC SoW and Package Datasheet; record the disposition and update the Conflict Table.
13. Perform cross-document consistency checks for identity, interface list (7 interfaces), responsibility split, voltage/rating reconciliation status, and the `TBD` set across all four documents.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful Pass 1+2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe per the `four-documents` Step 7 rule. Append a History line.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Identity consistency | Identity fields match `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv` row DEL-015-06, and `PACKAGE_REGISTER.csv` row PKG-015. |
| Interface coverage | All seven package interfaces from `INTERFACE_REGISTER.csv` rows for `PKG-015` appear in the acceptance scope and across documents. |
| Responsibility integrity | Vendor-owned and EPC-owned scopes are not conflated in any of the four documents. |
| Source-gap handling | EPC SoW, Construction Work Package, 2400 V tap, and 12/15 MVA dual rating gaps appear as `TBD` and as Conflict Table entries; no invented clause references. |
| Status-rule compliance | `_STATUS.md` modified only per the safe-update rule; no state regression. |
| Scope compliance | No files modified outside the deliverable folder. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history (this run's transition only)
- `_run_records/TASK_RUN_2026-05-24_*.md`
- (Operational, when vendor data exists) Vendor document review log, acceptance checklist, test/inspection evidence inventory (FAT/SAT, dielectric, grounding/bonding), turnover evidence inventory, and the 2400 V tap / 12/15 MVA rating reconciliation memo.
