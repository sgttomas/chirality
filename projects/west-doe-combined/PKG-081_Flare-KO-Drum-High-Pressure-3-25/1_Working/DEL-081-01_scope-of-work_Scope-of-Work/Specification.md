# Specification: DEL-081-01 — Scope of Work (PKG-081 Flare KO Drum (High Pressure) 3-25)

> Normative requirements for the EPC Integrator-authored Scope of Work document for package PKG-081. Requirements derive from accessible sources (Gate-7 PROJECT_DECOMP snapshot and accessible DBM sections). Inferred requirements are labeled `ASSUMPTION`. Unknowns are marked `TBD`.

## Scope

### In scope
- The Scope of Work document SHALL describe, at the EPC Integrator level, the full package scope for PKG-081 "Flare KO Drum (High Pressure) 3-25", including:
  - tagged major equipment and package identity (V-4100-2, V-4150-2, P-4100-2, P-4150-2);
  - package function (sour HP relief liquid knockout and liquid transfer to slop);
  - source basis and authoritative references;
  - package boundaries (battery limits and interface types);
  - whole-facility integration narrative;
  - responsibility assignment between Package Vendor and EPC Integrator.
  Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row DEL-081-01; `ARTIFACT_REGISTER.csv` rows.
- The document SHALL cover scope items `SOW-0071`, `SOW-0072`, `SOW-0073`, `SOW-0074`. Source: `SCOPE_LEDGER.csv`; `_CONTEXT.md`.
- The document SHALL identify all 10 active facility-level interface types listed in `INTERFACE_REGISTER.csv` for PKG-081.

### Out of scope (carried by other PKG-081 deliverables)
- Vendor engineering, package design, vendor documentation, and physical equipment supply — covered by `DEL-081-04_vendor-engineered-equipment-package` and `DEL-081-05_vendor-document-turnover-package`.
- EPC technical handoff datasheet to vendor — covered by `DEL-081-02_package-datasheet`.
- Construction work package and tie-in execution — covered by `DEL-081-03_construction-work-package`.
- EPC vendor package review and acceptance record — covered by `DEL-081-06_epc-vendor-package-review-and-acceptance`.
Source: `DELIVERABLE_REGISTER.csv` PKG-081 rows.

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| REQ-SOW-01 | The Scope of Work SHALL identify the package by Package ID `PKG-081`, Workbook row 54, WBS 02, CoA tracking 26020-02-17-001, and discipline Mechanical. | `PACKAGE_REGISTER.csv` |
| REQ-SOW-02 | The Scope of Work SHALL list the tagged major equipment: V-4100-2, V-4150-2, P-4100-2, P-4150-2. | `SCOPE_LEDGER.csv` SOW-0073; DBM SEC-07 |
| REQ-SOW-03 | The Scope of Work SHALL state the basic package scope as supply of two HP flare KO drums and two dedicated transfer pumps. | `SCOPE_LEDGER.csv` SOW-0072; DBM SEC-09 sparing row |
| REQ-SOW-04 | The Scope of Work SHALL describe package function as: HP flare relief liquid knockout (both drums manifold to the HP flare) and liquid transfer to the condensate slop tank via the dedicated KO drum transfer pumps, with truck-out provision. | `SCOPE_LEDGER.csv` SOW-0073; DBM SEC-07 |
| REQ-SOW-05 | The Scope of Work SHALL declare responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment supply; EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). | `PACKAGE_REGISTER.csv` description; `ARTIFACT_REGISTER.csv` ART-00ABFE7374; `OBJ-004` register entry |
| REQ-SOW-06 | The Scope of Work SHALL identify the 10 active facility-level interface types for PKG-081: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` (10 rows for PKG-081) |
| REQ-SOW-07 | The Scope of Work SHALL surface the unresolved scope-conflict open item: SOW-0074 records that flare-system equipment is technically described but listed as excluded in the DBM scope table; final in/out boundary requires owner/engineering ruling. | `SCOPE_LEDGER.csv` SOW-0074 |
| REQ-SOW-08 | The Scope of Work SHALL state that the HP/Cryo and LP dual flare stack and incinerator are shared-interface systems between 03-25 and 04-25 and that exact service split is an open interface item. | DBM SEC-01 Shared Interface Notes; DBM SEC-07 |
| REQ-SOW-09 | The Scope of Work SHALL cite, but not reproduce, external governing documents that are not locally accessible (notably `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy and `26020-Package_Requirements.docx` package heading 34). Items derived solely from these inaccessible artifacts SHALL be marked `location TBD`. | `_REFERENCES.md`; DBM SEC-07; `_Sources` directory listing |
| REQ-SOW-10 | The Scope of Work SHALL link supported objectives `OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010` to package responsibility, marking the association as `ASSUMPTION (PACKAGE_HEURISTIC)` per the run brief. | `OBJECTIVE_DELIVERABLE_MAP.csv`; brief `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` |
| REQ-SOW-11 | The Scope of Work SHALL NOT include vendor-engineering technical content (design pressures, vessel sizing, pump curves, datasheet values) — those belong to the Package Datasheet (`DEL-081-02`) and the vendor package (`DEL-081-04`). | `DELIVERABLE_REGISTER.csv` PKG-081 rows; `_CONTEXT.md` Notes |
| REQ-SOW-12 | The Scope of Work SHALL retain the source-row identifiers (Workbook Packages row 54; `26020-Package_Requirements.docx` package heading 34) as evidence anchors throughout. | `_CONTEXT.md` Source Reference; `_REFERENCES.md` |

## Standards

| Standard / Governing Source | Status in workspace | Notes |
|---|---|---|
| Gate-7 PROJECT_DECOMP snapshot (`GATE-07_Final_Published_2026-05-24`) | Accessible | Authoritative decomposition basis. |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Accessible | Source for HP flare basis, sparing, isolation, sour-service, site data. |
| `_Sources/26020-Package_Requirements.docx` (package heading 34) | Present as binary docx; markdown extraction not in workspace | Clause-level requirements `location TBD` until extracted. |
| `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy | Not in workspace | Required for final blowdown sequencing; `location TBD`. |
| Project codes and standards (ASME, API, CSA Z662, etc.) | Not enumerated in accessible sources for this deliverable | `TBD` — to be confirmed when DBM SEC-15 / project codes register is extracted. |

## Verification

| Verification Activity | Confirms |
|---|---|
| Cross-check Scope of Work content against `_CONTEXT.md` identity table and `DELIVERABLE_REGISTER.csv` row | REQ-SOW-01, REQ-SOW-05 |
| Cross-check tagged equipment and basic scope statements against `SCOPE_LEDGER.csv` rows SOW-0071..SOW-0074 and DBM SEC-07 | REQ-SOW-02, REQ-SOW-03, REQ-SOW-04, REQ-SOW-07 |
| Cross-check interface enumeration against `INTERFACE_REGISTER.csv` filtered by PKG-081 (expect 10 rows) | REQ-SOW-06 |
| Cross-check responsibility narrative against `PACKAGE_REGISTER.csv` description column and `ARTIFACT_REGISTER.csv` ART-00ABFE7374 | REQ-SOW-05 |
| Confirm objective association labelled `ASSUMPTION (PACKAGE_HEURISTIC)` per brief | REQ-SOW-10 |
| Confirm absent-source claims carry `location TBD` markers (no values invented from inaccessible sources) | REQ-SOW-09 |
| Confirm Scope of Work does not contain values that belong to Package Datasheet | REQ-SOW-11 |

## Documentation

Documentation outputs (mapped to `ARTIFACT_REGISTER.csv`):
- `ART-3A59CA7249` Package scope of work (the Scope of Work artifact itself)
- `ART-531950B8A7` Tagged equipment and package identity list
- `ART-8045E643FB` Package function and whole-facility integration narrative
- `ART-00ABFE7374` Package responsibility assignment record
- `ART-F37B133BFD` Detailed mechanical package scope extraction evidence

Conflict and TBD items SHALL be carried in `Guidance.md` Conflict Table when source ambiguity cannot be resolved.
