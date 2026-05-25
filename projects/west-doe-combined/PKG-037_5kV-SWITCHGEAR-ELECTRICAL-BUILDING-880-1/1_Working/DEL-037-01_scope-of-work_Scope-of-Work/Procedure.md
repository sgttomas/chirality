# Procedure: DEL-037-01_scope-of-work — Scope of Work

## Purpose

Define the working procedure to produce and verify the `PKG-037 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)` EPC scope-of-work deliverable.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot dated 2026-05-24.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Gate 7 register rows for `PKG-037`, `DEL-037-01_scope-of-work`, and `SOW-0038`.
- `INTERFACE_REGISTER.csv` rows for `PKG-037` (twelve declared interfaces).
- `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-037-01_scope-of-work` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010).
- `ARTIFACT_REGISTER.csv` rows for `DEL-037-01_scope-of-work` (`ART-53C9B45AD0`, `ART-CD3C1783C4`, `ART-1DFABB8A68`, `ART-833F44316B`).
- Accessible DBM source slice: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Electrical Basis (system voltages, electrical buildings, grounding and bonding, cable tray and conduit, area classification, building designations, governing codes).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Declared downstream dependencies: none declared in `_DEPENDENCIES.md`.

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row `DEL-037-01_scope-of-work`.
2. Confirm package identity against `PACKAGE_REGISTER.csv` row `PKG-037`: vendor-owned Electrical package, WBS 01, CoA tracking number `26020-01-30-028`.
3. Confirm `SOW-0038` against `SCOPE_LEDGER.csv` and retain PKG-037 as a distinct flat project package.
4. Build the scope-of-work outline with these minimum sections: package identity, source basis, package function, scope inclusions, exclusions/deferred items, interfaces (twelve declared types), responsibility assignment (Package Vendor vs EPC Integrator), whole-facility integration narrative, verification, records, and open/TBD/human-ruling items.
5. Populate the interface content from `INTERFACE_REGISTER.csv` for `PKG-037`: Utility Piping (`IFC-524BC4670F`); Drain / Containment (`IFC-A8DC0D3056`); Electrical Power (`IFC-35A170DE7F`); Grounding / Bonding (`IFC-E26DA604FB`); Area / Exterior Lighting (`IFC-8F0D1E29F1`); I&C / Control Cabling (`IFC-F5B78B59CE`); Communications / Network (`IFC-1ECBDB6397`); Building HVAC / Services (`IFC-D6D4CB07AF`); Fire & Gas / Safety Systems (`IFC-4D8A22B2CA`); Maintenance Access (`IFC-CE2AC83D1D`); Grading / Site Drainage / Spill Containment (`IFC-65DF6F2E88`); Structural / Foundations / Supports (`IFC-8012069CE2`).
6. Populate the electrical-building context from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Electrical Buildings, Grounding and Bonding, Area Classification, and Cable Systems subsections. Include the prefabricated/modular basis, general-purpose area location, n + 1 HVAC, bottom cable entry / pile elevation, TECK/ACIC wiring, EMT use, outdoor GFI receptacle, and equipment-door provisions.
7. Carry the 880-1 tag and "5kV switchgear" label from the workbook package name as identity-only; record building location, dimensions, foundations, bus voltage, switchgear rating, lineup, breaker count, protection scheme, and tagged equipment as `TBD`.
8. Record the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
9. Check the scope narrative against the supported objectives (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010) only as directionally relevant context (PACKAGE_HEURISTIC, ASSUMPTION) from the accepted objective maps.
10. Add a human-ruling item for each unresolved design-basis gap that blocks final issue (see Guidance Conflict Table HRR-037-01-001 through HRR-037-01-003).

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable and package identifiers match `_CONTEXT.md`, `PACKAGE_REGISTER.csv` row `PKG-037`, and `DELIVERABLE_REGISTER.csv` row `DEL-037-01_scope-of-work`. |
| Scope item check | `SOW-0038` is cited and retained as distinct flat project package per `SCOPE_LEDGER.csv`. |
| Interface check | All twelve declared interface types are included and no unsupported interface type is added. |
| Electrical-building check | Electrical-building basis (prefabricated, modular, general-purpose area, n + 1 HVAC, bottom cable entry, pile elevation, TECK/ACIC wiring, EMT, GFI receptacle, equipment-door provisions) cites `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12. |
| Source fidelity check | 880-1 building location, bus voltage class, and switchgear rating remain `TBD` because accessible source does not support specific values. |
| Responsibility check | Package Vendor / EPC Integrator split is preserved and not collapsed to one party. |
| Dependency check | No blockers are asserted because no declared upstream dependencies exist. |
| Cross-document check | Datasheet attributes, Specification requirements, Guidance considerations, and Procedure steps use consistent package name, identifiers, interfaces, and `TBD` items. |

## Records

- Completed scope-of-work deliverable (`ART-53C9B45AD0`).
- Tagged equipment and package identity list (`ART-CD3C1783C4`) — entries `TBD` where source does not support equipment tags for the 880-1 building.
- Package function and whole-facility integration narrative (`ART-1DFABB8A68`).
- Package responsibility assignment record (`ART-833F44316B`).
- Interface summary covering the twelve declared PKG-037 interfaces.
- Source basis list and open / `TBD` / human-ruling list (including HRR-037-01-001, HRR-037-01-002, HRR-037-01-003).
- Review/approval evidence for 880-1 building location, 5 kV switchgear interpretation, and package-specific exclusions when available.
