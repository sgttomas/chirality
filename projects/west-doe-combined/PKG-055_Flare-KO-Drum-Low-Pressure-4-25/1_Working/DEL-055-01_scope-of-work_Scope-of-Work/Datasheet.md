# Datasheet — DEL-055-01 Scope of Work (Flare KO Drum (Low Pressure) 4-25)

> Descriptive identity, attributes, conditions, construction, and references for the EPC Scope of Work production unit for PKG-055.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-055-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-055` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Parent Workbook Row | 57 | PACKAGE_REGISTER.csv (PKG-055) |
| Package Name | Flare KO Drum (Low Pressure) 4-25 | PACKAGE_REGISTER.csv |
| Package Tag Identifier | `26020-01-PT-17-003` | PACKAGE_REGISTER.csv (Package ID column) |
| Companion Equipment Identifier | `26020-01-PT-17-003 - Flare KO Drum (LP)` | PACKAGE_REGISTER.csv (companion register row) |
| WBS | 01 | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | PACKAGE_REGISTER.csv; `_CONTEXT.md` |
| Type | EPC Scope of Work | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| LSD / Area | 4-25 (Deepcut) | DBM-Deepcut/4-25_Deepcut_DBM.md (LSD area for equipment tags) |

## Attributes

### Tagged Equipment within Package Scope

| Tag | Description | Source |
|---|---|---|
| `V-3900-1` | LP Flare KO Drum (one unit) | SCOPE_LEDGER SOW-0085; DBM-Deepcut/4-25_Deepcut_DBM.md line 2582 |
| `P-3900-1` | LP Flare KO Drum Transfer Pump (one unit) | SCOPE_LEDGER SOW-0085; DBM-Deepcut/4-25_Deepcut_DBM.md line 2581 |

### Package Function

The package provides knock-out (liquid separation) for low-pressure flare relief streams routed to the low-pressure flare system, with collected liquids transferred via the LP KO drum transfer pump to the condensate slop tank, with a truck-out provision included (SCOPE_LEDGER SOW-0085).

### Source Basis Summary

| Attribute | Value | Source |
|---|---|---|
| Basic scope statement | Supply one LP flare knock-out drum and one LP flare KO drum transfer pump | SCOPE_LEDGER SOW-0084 (26020-Package_Requirements.docx package heading 10, Basic scope) |
| Included equipment | LP flare KO drum V-3900-1; transfer pump P-3900-1; liquid transfer to condensate slop tank; truck-out provision; package tie-ins | SCOPE_LEDGER SOW-0085 (26020-Package_Requirements.docx package heading 10, Major included equipment) |
| Scope-adjacent open items | LP flare stack and air-assist blower described as connected system equipment; stack sizing and flare tip details are separate from this KO drum package | SCOPE_LEDGER SOW-0086 (26020-Package_Requirements.docx package heading 10, Scope notes and open items) |
| Workbook package row | Row 57; discipline Mechanical; WBS 01 | PACKAGE_REGISTER.csv |

### Whole-Facility Integration Narrative

| Attribute | Value | Source |
|---|---|---|
| LP flare role in facility | Low-pressure equipment, including amine regeneration, TEG regeneration, VRU, and reciprocating compressor seal pot, connects to LP flare | DBM-Deepcut/4-25_Deepcut_DBM.md line 2029 |
| Header sizing | 508 mm (20 in) LP relief header | DBM-Deepcut/4-25_Deepcut_DBM.md line 2029 |
| Drum and pump tags | LP flare KO drum V-3900-1; LP KO drum pump P-3900-1; truck-out provided | DBM-Deepcut/4-25_Deepcut_DBM.md line 2029 |
| Flare stack arrangement | LP flare element piggy-backs on common HP/cryo flare stack | DBM-Deepcut/4-25_Deepcut_DBM.md lines 2029, 2031 |
| Source allocation | Shared 03-25/04-25 allocation noted as open | DBM-Deepcut/4-25_Deepcut_DBM.md line 1834 |

## Conditions

| Field | Value | Source |
|---|---|---|
| Design pressure | location TBD (not stated in accessible package source slice; expected in 26020-Package_Requirements.docx heading 10 datasheet section, not yet locally extracted) | TBD — 26020-Package_Requirements.docx heading 10 |
| Design temperature | location TBD | TBD — 26020-Package_Requirements.docx heading 10 |
| Service fluid | LP flare relief liquids and vapours from amine regeneration, TEG regeneration, VRU, reciprocating compressor seal pot, and other LP equipment (ASSUMPTION: composition envelope inferred from connected-equipment list; no consolidated composition table in accessible source slice) | DBM-Deepcut/4-25_Deepcut_DBM.md line 2029 |
| Freeze protection | LP flare headers outside heated buildings — refer to flare header EHT/insulation rules for HP flare (LP header EHT requirement is ASSUMPTION; source explicitly addresses HP headers and cryogenic headers, LP not explicit) | DBM-Deepcut/4-25_Deepcut_DBM.md line 2033 |
| Operating relief loads | TBD; relief volumes noted as remaining to be determined during detailed design | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1834, 2021 |

## Construction

| Field | Value | Source |
|---|---|---|
| Assembly model | Single equipment package supplied by Package Vendor; integrated into facility by EPC Integrator | PACKAGE_REGISTER.csv Responsibility Description |
| Modularization | LP Flare KO Drum Module identified as 390-1; modularization shop/field designation: Shop | DBM-Deepcut/4-25_Deepcut_DBM.md line 2783 |
| Pump scope | One LP KO drum transfer pump (P-3900-1) included in the package | SCOPE_LEDGER SOW-0084, SOW-0085 |
| Truck-out | Truck-out provision included | SCOPE_LEDGER SOW-0085; DBM-Deepcut line 2029 |
| Excluded adjacent equipment | LP flare stack, common HP/cryo flare stack, and air-assist blower are described as connected system equipment but are not part of the KO drum package | SCOPE_LEDGER SOW-0086 |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- PACKAGE_REGISTER.csv row PKG-055 (Gate 7 final published snapshot)
- DELIVERABLE_REGISTER.csv row `DEL-055-01_scope-of-work`
- SCOPE_LEDGER.csv rows SOW-0083, SOW-0084, SOW-0085, SOW-0086
- DBM-Deepcut/4-25_Deepcut_DBM.md (locally accessible source markdown for 4-25 Deepcut design basis)
- 26020-Package_Requirements.docx package heading 10 — DOCX form not locally extracted to markdown; cited via SCOPE_LEDGER extracted slices; deeper datasheet-level values are `location TBD` until extracted
- Workbook Packages row 57 (26020-Packages_Interfaces_4_export.xlsx)

## Open Items

- TBD: Design pressure, design temperature, material of construction, sizing basis, and instrument list for V-3900-1 and P-3900-1 — to be sourced from 26020-Package_Requirements.docx heading 10 detailed datasheet section once locally extracted.
- TBD: Relief volume basis and LP flare stack sizing (per DBM 4-25 open items list).
- ASSUMPTION: Service envelope inferred from connected-equipment list; not validated against a consolidated process data sheet.
