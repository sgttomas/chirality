# Procedure: DEL-032-01_scope-of-work — Scope of Work

Operational procedure to produce and verify the EPC Integrator Scope of Work for PKG-032 Cathodic Protection Design and Installation.

## Purpose

Provide a repeatable procedure for authoring, reviewing, and finalizing this SOW deliverable so that it satisfies the Specification requirements and respects the Guidance principles.

## Prerequisites

- Read `_CONTEXT.md` for deliverable identity and anticipated artifacts.
- Read `_REFERENCES.md` for authoritative basis pointers.
- Read `_DEPENDENCIES.md` for declared upstream/downstream constraints (currently none declared).
- Access the Gate-7 published snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (DELIVERABLE_REGISTER, PACKAGE_REGISTER, OBJECTIVE_DELIVERABLE_MAP).
- Access source slices:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-12 §Cathodic Protection and SEC-12 Assumptions/TBDs table.
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` electrical-design scope statements.
- Confirm `_STATUS.md` is in a state authorized for overwrite (`OPEN`, `INITIALIZED`).
- Coordinate with the owner cathodic-protection design basis owner; identify a point of contact (TBD until human confirmation).

## Steps

1. **Frame identity.** Populate the Datasheet identification block from `_CONTEXT.md` and PACKAGE_REGISTER row PKG-032.
2. **Restate the boundary.** In the SOW narrative, quote or paraphrase the DBM-Deepcut SEC-12 §Cathodic Protection exclusion (line 3073-3075) and the Assumptions/TBDs row (line 3092). Distinguish this from the facility-side electrical-support language in DBM-Comp_and_Liquids.
3. **Allocate responsibilities.** Populate the responsibility assignment record using PACKAGE_REGISTER ownership statements: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
4. **List interfaces.** Enumerate the four applicable interface types (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network) and state the facility-side support obligation for each.
5. **Populate the tagged equipment list.** Insert vendor-provided tags when available; otherwise mark TBD with a pointer to the vendor package datasheet.
6. **Cover scope items.** Confirm SOW-0033 coverage by cross-checking DELIVERABLE_REGISTER `covers_scope`.
7. **Trace objectives.** Record OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-009, OBJ-010 as directional context (ASSUMPTION per package-grouping heuristic) pending human ruling.
8. **Surface gaps.** Carry unresolved items (CP system type, current density, tagged equipment list, owner basis location) as TBD; do not invent values.
9. **Cross-check consistency.** Compare Datasheet ↔ Specification ↔ Guidance for terminology and numeric/identifier consistency before submission.
10. **Submit for review.** Notify ORCHESTRATOR / human reviewer; record any human ruling in `MEMORY.md` (if created) or in the Conflict Table.

## Verification

| Verification | Pass Criterion |
|---|---|
| Identity | Package tag `26020-03-30-023`, ParentPackageID `PKG-032`, WBS 03, Discipline Electrical present and consistent. |
| Boundary | DBM-Deepcut SEC-12 exclusion text is quoted or accurately paraphrased with source citation. |
| Responsibility split | Vendor and EPC Integrator scopes match PACKAGE_REGISTER ownership statements. |
| Interfaces | All four interface types appear with facility-side obligations. |
| Coverage | SOW-0033 coverage is explicit. |
| Conflict register | CFL-032-01-001 and CFL-032-01-002 are present in Guidance Conflict Table or explicitly resolved. |
| Epistemics | Unknown values are marked `TBD`; inferences are labeled `ASSUMPTION`. |

## Records

- The finalized `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in this deliverable folder.
- Updated `_STATUS.md` reflecting `INITIALIZED` after Pass 1/2 (or later authorized progression).
- Run record(s) in `_run_records/`.
- Conflict Table entries in `Guidance.md`.
- Any human ruling records (e.g., entries to be added to `MEMORY.md` when created).
