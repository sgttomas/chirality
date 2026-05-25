# Procedure: DEL-006-01_scope-of-work — Scope of Work

## Purpose

Define the working procedure to produce and verify the `PKG-006 — Containment Berms` EPC scope-of-work deliverable.

## Prerequisites

- Accepted Gate 7 decomposition snapshot dated 2026-05-24.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Gate 7 register rows for `PKG-006`, `DEL-006-01_scope-of-work`, and `SOW-0006`.
- Accessible DBM source slice: `3-25_Comp_and_Liquids_DBM.md`, especially SEC-01, SEC-02, SEC-11, and SEC-15.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Declared downstream dependencies: none declared in `_DEPENDENCIES.md`.

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`.
2. Confirm package identity against `PACKAGE_REGISTER.csv`: `PKG-006`, Containment Berms, Civil, WBS 03, CoA tracking number `26020-03-42-006`.
3. Confirm SOW-0006 against `SCOPE_LEDGER.csv` and retain the package as a distinct flat project package.
4. Build the scope-of-work outline with these minimum sections: package identity, source basis, package function, scope inclusions, exclusions/deferred items, interfaces, responsibility assignment, verification, records, and open/TBD items.
5. Populate interface content from `INTERFACE_REGISTER.csv`: Drain / Containment and Grading / Site Drainage / Spill Containment.
6. Populate civil and drainage context from `3-25_Comp_and_Liquids_DBM.md`, SEC-11. Include surface-water management, process-contaminated drainage routing, current hydrology uncertainty, and final geotechnical confirmation where relevant.
7. Insert `TBD` for berm dimensions, containment volume, slopes, materials, liner system, tie-in coordinates, and detailed construction criteria unless a later accepted source provides them.
8. Record responsibility assignment as EPC Integrator for the deliverable and flag final EPC Integrator vs civil discipline subcontractor execution assignment as TBD.
9. Check the scope narrative against OBJ-002, OBJ-007, OBJ-008, and OBJ-009 only as directionally relevant context from the accepted objective maps.
10. Add a human-ruling item for each unresolved responsibility or design-basis gap that blocks final issue.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable and package identifiers match `_CONTEXT.md`, `PACKAGE_REGISTER.csv`, and `DELIVERABLE_REGISTER.csv`. |
| Interface check | Drain / Containment and Grading / Site Drainage / Spill Containment are included and no unsupported interface type is added. |
| Source fidelity check | General civil and drainage requirements cite `3-25_Comp_and_Liquids_DBM.md`; package-specific values not found in sources remain `TBD`. |
| Dependency check | No blockers are asserted because no declared upstream dependencies exist. |
| Responsibility check | EPC Integrator deliverable ownership is shown; execution responsibility uncertainty remains visible until ruled. |
| Cross-document check | Datasheet attributes, Specification requirements, Guidance considerations, and Procedure steps use consistent package name, identifiers, interfaces, and `TBD` items. |

## Records

- Completed scope-of-work deliverable.
- Source basis list.
- Interface summary.
- Responsibility assignment record.
- `TBD` and human-ruling list.
- Review/approval evidence for final hydrology, geotechnical, civil drawings, and package-specific containment criteria when available.
