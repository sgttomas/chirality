# Procedure: DEL-086-01_scope-of-work — Scope of Work

> Operational procedure for producing the EPC Integrator Scope of Work artifact for PKG-086 (Flare Stack — Low Pressure). Steps reference source-grounded inputs from the Gate 7 PROJECT_DECOMP snapshot. Where judgment requires a source slice not yet local, the step marks the deliverable `TBD`.

## Purpose

Produce the Scope of Work artifact and supporting records that satisfy the requirements in `Specification.md` and the directional intent in `Guidance.md`, while preserving the responsibility split, package boundary, interface set, and procurement-authority note from the upstream source basis.

## Prerequisites

- Read access to:
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
  - Gate 7 snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
    - `DELIVERABLE_REGISTER.csv` (row `DEL-086-01_scope-of-work`)
    - `PACKAGE_REGISTER.csv` (row `PKG-086`)
    - `SCOPE_LEDGER.csv` (rows `SOW-0091`..`SOW-0094`)
    - `INTERFACE_REGISTER.csv` (rows with ParentPackageID `PKG-086`)
    - `OBJECTIVE_REGISTER.csv` (rows `OBJ-002`, `OBJ-004`..`OBJ-010`)
- Where available locally, the upstream source materials:
  - `_Sources/26020-Package_Requirements.docx` (package heading 39)
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages row 59)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- No declared upstream deliverable dependencies (see `_DEPENDENCIES.md`).

## Steps

1. **Confirm deliverable identity.** Verify identity fields in `_CONTEXT.md` against `DELIVERABLE_REGISTER.csv` row `DEL-086-01_scope-of-work`. Resolve any mismatch before drafting.
2. **Extract package identity and function.** From `PACKAGE_REGISTER.csv` row `PKG-086`, capture: package name, discipline, WBS, tracking number, function description, and the responsibility-model paragraph verbatim.
3. **Extract major included equipment.** From `SCOPE_LEDGER.csv` row `SOW-0093`, capture the major included equipment list verbatim: LP flare stack, air-assist blower, pilot, pilot proving, auto-ignition, supplemental fuel gas/dilution gas provisions, stack interface details.
4. **Assemble tagged equipment list.** If `_Sources/26020-Package_Requirements.docx` package heading 39 is locally accessible, extract per-tag entries. Otherwise, populate the tagged-equipment table with `TBD — location TBD` and add a note that the source slice has not been brought into the deliverable folder.
5. **Carry forward procurement-authority note.** From `SCOPE_LEDGER.csv` row `SOW-0094`, capture the 4-25 / 3-25 boundary note verbatim into the SoW.
6. **Enumerate facility-integration interfaces.** From `INTERFACE_REGISTER.csv`, list all rows with ParentPackageID `PKG-086`. Confirm count is 8 with `Applicable = YES`.
7. **Write the responsibility-assignment record.** Render the Package Vendor / EPC Integrator split verbatim from `PACKAGE_REGISTER.csv` PKG-086. Append a delegation note pointing to sibling deliverables DEL-086-02..06 for the work that the SoW does not own.
8. **Write the integration narrative.** Describe how PKG-086 integrates into the facility using the eight interface types as the boundary set. Tie each interface back to the supporting objective(s) (e.g., Relief/Flare/Vent and Drain/Containment to OBJ-007 and OBJ-009; Electrical Power and Grounding/Bonding to OBJ-005; I&C/Control Cabling and Fire & Gas to OBJ-006 and OBJ-009; Structural to OBJ-008).
9. **Demonstrate objective coverage.** For each of OBJ-002, OBJ-004..010, write a one- to two-sentence contribution statement explaining how PKG-086's SoW supports the objective. Use objective statements from `OBJECTIVE_REGISTER.csv` as the anchor.
10. **Cross-reference siblings.** Insert a delegation table identifying which work is owned by DEL-086-02 (Package Datasheet), DEL-086-03 (CWP), DEL-086-04 (Vendor Equipment Package), DEL-086-05 (Vendor Document Turnover), DEL-086-06 (EPC Vendor Review and Acceptance).
11. **Mark all unsourced statements.** Any value, requirement, or claim not traceable to a row in the Gate 7 snapshot or to a locally accessible source slice shall be labeled `ASSUMPTION` or `TBD` with `location TBD`.
12. **Self-verify against `Specification.md`.** Walk each REQ-086-01-NNN and confirm the SoW satisfies it. Record any unsatisfied requirement as an open item in `MEMORY.md` (when created) rather than silently dropping it.

## Verification

| Check | Method |
|---|---|
| Identity match | Diff identity fields between SoW and `DELIVERABLE_REGISTER.csv`. |
| Responsibility verbatim | String match the responsibility paragraph against `PACKAGE_REGISTER.csv` PKG-086. |
| Interface count = 8 | Count `Applicable = YES` rows in `INTERFACE_REGISTER.csv` filtered by `ParentPackageID = PKG-086`. |
| SOW-0091..0094 coverage | Confirm each `SOW-009X` statement appears or is represented in the SoW. |
| Objective coverage | Confirm a contribution statement exists for each of OBJ-002, OBJ-004..010. |
| Sibling delegation present | Confirm DEL-086-02..06 are referenced as owners of out-of-scope work. |
| `TBD` discipline | Confirm any non-source-grounded statement is labeled `TBD` or `ASSUMPTION`. |
| No vendor-design ownership assigned to EPC | Review SoW for any statement that implies the EPC performs vendor engineering/design/documentation/supply. |

## Records

The following records shall result from execution of this procedure (within the deliverable folder):

- The Scope of Work artifact itself (the SoW narrative document, anchored by this deliverable's four-document kit).
- Tagged equipment and package identity list (table embedded in the SoW; `TBD` rows are records of source-slice gaps).
- Responsibility assignment record (table or paragraph in the SoW, verbatim from `PACKAGE_REGISTER.csv` PKG-086).
- Package function and integration narrative.
- Open-item log in `MEMORY.md` (when created in a later pass) capturing every `TBD` and every source slice not yet locally accessible.
- A run record at `_run_records/TASK_RUN_*.md` for each TASK invocation.
