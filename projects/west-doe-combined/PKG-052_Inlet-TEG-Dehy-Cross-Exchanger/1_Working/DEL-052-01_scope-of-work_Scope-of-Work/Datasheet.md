# Datasheet: DEL-052-01 — Scope of Work, PKG-052 Inlet / TEG Dehy Cross Exchanger

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-052-01_scope-of-work | _CONTEXT.md |
| Deliverable Name | Scope of Work | _CONTEXT.md |
| Parent Package ID | PKG-052 | _CONTEXT.md; PACKAGE_REGISTER.csv row 62 |
| Parent Workbook ID | 52 (Workbook Packages row 62) | PACKAGE_REGISTER.csv row 62 |
| Package Name | Inlet / TEG Dehy Cross Exchanger | PACKAGE_REGISTER.csv row 62 |
| Equipment Tag / RFQ | 26020-01-PT-16-001 — Inlet TEG Cross Exchanger | PACKAGE_REGISTER.csv row 62 (Equipment Tag) |
| Primary Equipment Tag | E-5718-1 | DBM-Deepcut/4-25_Deepcut_DBM.md "Inlet / TEG Dehy Cross Exchanger"; Equipment register row 2586 |
| Discipline | Mechanical | PACKAGE_REGISTER.csv; _CONTEXT.md |
| Deliverable Type | EPC Scope of Work | _CONTEXT.md |
| Responsible Party (this deliverable) | EPC Integrator | _CONTEXT.md |
| Package Vendor Responsibility | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv row 62 (Responsibility) |
| EPC Integrator Responsibility | Integration into the functional process facility: interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv row 62 (Responsibility) |
| Host Facility | 04-25 West Doe Deep Cut Gas Plant expansion | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-01 |
| Covers Scope Items | SOW-0103, SOW-0104, SOW-0105, SOW-0106 | _CONTEXT.md; DELIVERABLE_REGISTER.csv row 336 |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC association) | _CONTEXT.md; DELIVERABLE_REGISTER.csv row 336 |

## Attributes

### Tagged Equipment / Package Identity

| Attribute | Value | Source |
|---|---|---|
| Equipment description | One (1) Inlet / TEG Dehy Cross Exchanger (E-5718-1), TEMA 'R' BEM shell-and-tube heat exchanger, with accompanying piping/instrumentation and skid | PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" |
| Quantity | 1 | PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" design table |
| Type | Shell and tube; TEMA R, BEM configuration | PACKAGE_REGISTER.csv row 62 (Scope: "TEMA 'R' BEM"); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" |
| Process function | Cold sour gas from the inlet separator flows to the TEG heat exchanger, where it exchanges heat with sweet gas leaving the amine sweetening unit; the sour gas flows to the inlet compressors | PACKAGE_REGISTER.csv row 62 (Scope) |
| Heat integration role | Heats inlet separator overhead gas (cold side) and cools a downstream warm process gas stream before that gas flows to process-gas molecular-sieve inlet filter/coalescers | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" |

### Process Conditions

| Parameter | Value | Source |
|---|---|---|
| Duty | 5,514.3 kW (18.82 MMBTU/hr) | PACKAGE_REGISTER.csv row 62 (Scope) |
| Design pressure | 9,756 kPag (1,415 psig) | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" design table |
| Design temperature | 66 deg C | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" design table |
| Cold-side service | Cold sour inlet separator overhead gas | PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" |
| Warm-side service | Warm process gas (CONFLICT: workbook scope states "sweet gas leaving the amine sweetening unit"; DBM-Deepcut states warm-side identity is unresolved between dehydrated TEG-contactor overhead gas and warm sweet gas leaving the amine sweetening unit — see Guidance Conflict Table) | PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger"; DBM-Deepcut "Interfaces" |
| Cold-side outlet routing | To inlet compressors (per workbook scope) | PACKAGE_REGISTER.csv row 62 (Scope) |
| Warm-side outlet routing | To process-gas molecular-sieve inlet filter/coalescers | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" |

### Construction Scope

| Attribute | Value | Source |
|---|---|---|
| Skid / mounting | Dedicated skid with package piping and instrumentation | PACKAGE_REGISTER.csv row 62 (Scope) |
| Materials of construction | TBD — not stated in accessible sources |  |
| Insulation | TBD — not stated in accessible sources |  |

## Conditions

### Process Boundaries

| Boundary | Description | Source |
|---|---|---|
| Cold-side inlet | Sour gas from inlet separator overheads (E-5718-1 cold side) | PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" |
| Cold-side outlet | Sour gas routed to inlet compressors | PACKAGE_REGISTER.csv row 62 (Scope) |
| Warm-side inlet | Warm process gas — identity unresolved (see Conflict Table in Guidance.md) | PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Interfaces" |
| Warm-side outlet | To process-gas molecular-sieve inlet filter/coalescers | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" |

### Interface Types (EPC Integrator scope)

Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports.

Source: PACKAGE_REGISTER.csv row 62 (Applicable interface types).

### Adjacent Packages and Systems

| Adjacent Item | Relationship | Source |
|---|---|---|
| Inlet Separators 4-25 (PKG-056) | Supplies cold-side sour gas (inlet separator overhead) | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger"; PACKAGE_REGISTER.csv row 68 |
| Inlet / Sales Compressors (PKG-048) | Receives cold-side outlet sour gas | PACKAGE_REGISTER.csv row 62 (Scope); PACKAGE_REGISTER.csv row 65 |
| TEG Dehydration Unit (PKG-068) | Candidate warm-side source/return (TEG contactor dehydrated gas) — unresolved | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger"; PACKAGE_REGISTER.csv row 97 |
| Amine sweetening unit | Candidate warm-side source (sweet gas from amine absorbers) — unresolved | PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Interfaces" |
| Process-gas molecular-sieve inlet filter/coalescers | Receives warm-side outlet | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Skid configuration | Vendor-supplied package skid with piping and instrumentation | PACKAGE_REGISTER.csv row 62 (Scope) |
| Foundation / supports | EPC Integrator scope (Structural / Foundations / Supports interface) | PACKAGE_REGISTER.csv row 62 (Applicable interface types) |
| Tie-ins | EPC Integrator scope: process piping, utility piping, drains, EHT, grounding, area lighting, I&C/control cabling | PACKAGE_REGISTER.csv row 62 (Applicable interface types) |
| Maintenance access | EPC Integrator scope: tube-bundle pull length, lifting access, valve/instrument access | PACKAGE_REGISTER.csv row 62 (Applicable interface types); ASSUMPTION: tube-pull length derived from BEM convention |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row 62, PKG-052)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row 336, DEL-052-01)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — sections "Inlet / TEG Dehy Cross Exchanger" and "Interfaces"
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — package heading 7 (location TBD; binary not extracted to markdown)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 62 (location TBD; binary not extracted to markdown)
