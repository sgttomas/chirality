# Specification — DEL-063-02 Package Datasheet (PKG-063 Tanks, DSO (API 650))

## Scope

This specification governs the **EPC Package Datasheet** for PKG-063, *Tanks, DSO (API 650)*. The deliverable is the EPC Integrator's technical handoff to a third-party package vendor for engineering, design, fabrication, and supply of one (1) atmospheric Disulphide Oil (DSO) storage tank installed at the 04-25 Deep Cut Gas Plant.

**Includes:**
- Technical basis (process function, service fluid, design code, sizing, mechanical attributes) of the DSO storage tank package.
- Interface requirements for the nine workbook-declared interface types applicable to PKG-063 (Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports).
- Vendor scope boundary (package engineering, package design, vendor documentation, physical equipment package).
- EPC Integrator scope boundary (facility-level integration, tie-ins, constructability, procurement/construction coordination).

**Excludes:**
- Construction work package (DEL-063-03) — installation and tie-in workface plan.
- Vendor engineered equipment package (DEL-063-04) — vendor's own engineering/design/datasheet set.
- Vendor document turnover package (DEL-063-05) — vendor document register and turnover.
- EPC vendor package review and acceptance (DEL-063-06).
- Detailed design of the incinerator system, knock-out drum, or shared off-gas header (separate package scope).

Source: PACKAGE_REGISTER.csv PKG-063 (`Description`, `Scope`, `Notes`); DELIVERABLE_REGISTER.csv DEL-063-02; ARTIFACT_REGISTER.csv (artifacts mapped to DEL-063-02).

## Requirements

Requirements are numbered REQ-063-02-NN. Each carries a source citation per K-PROV-1; unsupported items are marked `TBD` or `ASSUMPTION`.

### Process and Service

| ID | Requirement | Source |
|---|---|---|
| REQ-063-02-01 | The package shall provide one (1) Disulphide Oil (DSO) storage tank receiving separated DSO from the upstream DSO separator (level-controlled) within the caustic regeneration system. | PACKAGE_REGISTER.csv PKG-063 (`Process function`) |
| REQ-063-02-02 | The tank shall provide truck-out capability for DSO disposal. | DBM-Deepcut/4-25_Deepcut_DBM.md §"Disulphide Oil, Spent Caustic, and Waste Amine"; ARTIFACT_REGISTER.csv ART-966875EFC3 |
| REQ-063-02-03 | The service fluid is disulphide oil (by-product of NGL non-regenerative caustic treating). | DBM-Deepcut/4-25_Deepcut_DBM.md |

### Sizing and Pressure

| ID | Requirement | Source |
|---|---|---|
| REQ-063-02-04 | Nominal storage capacity shall be 400 bbl. | ARTIFACT_REGISTER.csv ART-966875EFC3; DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-063-02-05 | The tank shall be an atmospheric-pressure tank. | ARTIFACT_REGISTER.csv ART-966875EFC3; DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-063-02-06 | Design pressure shall be 32 oz. | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| REQ-063-02-07 | Design vacuum shall be 1.0 oz. | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| REQ-063-02-08 | The fluid design specific gravity shall be 1.75 (TBC — to be confirmed during detailed engineering). | DBM-Deepcut/4-25_Deepcut_DBM.md |

### Mechanical Design and Code

| ID | Requirement | Source |
|---|---|---|
| REQ-063-02-09 | Tank design and fabrication shall be to modified API 650. | ARTIFACT_REGISTER.csv ART-966875EFC3; 26020-Package_Requirements.docx heading 18 (referenced) |
| REQ-063-02-10 | Enumeration of specific modifications to API 650 is `TBD` (clause-level text not extracted in this pass; `location TBD` in 26020-Package_Requirements.docx heading 18 and 26020-01-PT-RFQ-19-001 binary not locally accessible). | ARTIFACT_REGISTER.csv ART-966875EFC3; PACKAGE_REGISTER.csv PKG-063 (Word Source Basis) |
| REQ-063-02-11 | Internal coating shall cover floor, walls, and roof. | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| REQ-063-02-12 | Specific coating system selection is `TBD` (no locally accessible source slice naming the coating product/grade). | ASSUMPTION — not stated in available sources |

### Thermal / Insulation

| ID | Requirement | Source |
|---|---|---|
| REQ-063-02-13 | A tank heater shall maintain contents at 32.2 °C (90 °F) minimum; heater design is the vendor's responsibility. | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| REQ-063-02-14 | The tank shall be insulated such that DSO remains above its pour point for truck-out and handling. | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| REQ-063-02-15 | Minimum design ambient / DSO low-temperature value is `TBD`. | ARTIFACT_REGISTER.csv ART-966875EFC3 (`Minimum temperature TBD`) |

### Venting, Blanket, and Safety

| ID | Requirement | Source |
|---|---|---|
| REQ-063-02-16 | Tank off-gas shall route to the incinerator header (incinerator located at the 3-25 facility, services 4-25 NGL mercaptan treating). | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-063-02-17 | A flame arrestor shall be provided on the off-gas line for backflash protection. | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-063-02-18 | The tank shall be blanketed with low-pressure fuel gas. | DBM-Deepcut/4-25_Deepcut_DBM.md |
| REQ-063-02-19 | Pumping DSO into the C5+ product stream as an alternate disposal path shall be reviewed during detailed engineering (not part of vendor base scope). | DBM-Deepcut/4-25_Deepcut_DBM.md (`Pumping DSO to C5+ product is subject to detailed-engineering review`) |

### Interfaces (battery limits)

Per PKG-063 the workbook declares the following nine interface types as applicable (`YES` in the X-column). Each shall be defined and dimensioned in the Package Interface Requirements Matrix portion of the Datasheet:

| ID | Interface Type | Interface Register Row |
|---|---|---|
| REQ-063-02-20 | Process Piping | IFC-B8225E1CAC |
| REQ-063-02-21 | Relief / Flare / Vent | IFC-55319DFCC3 |
| REQ-063-02-22 | Drain / Containment | IFC-976437DD6E |
| REQ-063-02-23 | Grounding / Bonding | IFC-F0E7550CA2 |
| REQ-063-02-24 | Area / Exterior Lighting | IFC-BDDC5F17F1 |
| REQ-063-02-25 | Cathodic Protection | IFC-89C542835E |
| REQ-063-02-26 | I&C / Control Cabling | IFC-289323FEB4 |
| REQ-063-02-27 | Grading / Site Drainage / Spill Containment | IFC-391B72231B |
| REQ-063-02-28 | Structural / Foundations / Supports | IFC-DFD52CFB01 |

Source: INTERFACE_REGISTER.csv (filtered to PKG-063). Specific tie-in elevations, nozzle sizes/ratings, set pressures, and cable schedule entries are `TBD` (not in accessible source slices).

### Scope Boundary

| ID | Requirement | Source |
|---|---|---|
| REQ-063-02-29 | Vendor scope: package engineering, package design, vendor documentation, and the physical equipment package. | PACKAGE_REGISTER.csv PKG-063 (`Responsibility`) |
| REQ-063-02-30 | EPC Integrator scope: integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv PKG-063 |

### SOW and Objective Linkage

| ID | Requirement | Source |
|---|---|---|
| REQ-063-02-31 | The datasheet shall fully address SOW items SOW-0209, SOW-0210, SOW-0211, SOW-0212. | DELIVERABLE_REGISTER.csv DEL-063-02 (`Covers Scope Items`) |
| REQ-063-02-32 | The datasheet supports objectives OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION — PACKAGE_HEURISTIC: objectives recorded at the package level; objective-deliverable map propagates these to DEL-063-02 per the PROJECT_DECOMP default association mode). | DELIVERABLE_REGISTER.csv DEL-063-02; PACKAGE_REGISTER.csv PKG-063; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC |

## Standards

| Standard | Status / Location | Source |
|---|---|---|
| API 650 (modified) — Welded Tanks for Oil Storage | Mandatory; specific modifications `location TBD` in 26020-Package_Requirements.docx heading 18 | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| 26020 Project package requirements specification | 26020-Package_Requirements.docx, heading 18 (Word source basis) | PACKAGE_REGISTER.csv PKG-063 |
| 26020-01-PT-RFQ-19-001 — Tanks, DSO (R0) RFQ | Listed as Word Source Basis under `Bid Docs/_Budgetary/`; **not locally accessible during this pass** — `location TBD` | PACKAGE_REGISTER.csv PKG-063 |
| Coating system standard | TBD — not stated in accessible sources | ASSUMPTION |
| Insulation standard | TBD — not stated in accessible sources | ASSUMPTION |
| Cathodic protection standard | TBD — interface declared `YES`, specific code reference not in accessible sources | ASSUMPTION |
| Grounding/bonding standard | TBD — interface declared `YES`, specific code reference not in accessible sources | ASSUMPTION |

## Verification

| Requirement(s) | Verification Method | Records |
|---|---|---|
| REQ-063-02-04 .. REQ-063-02-10 | Vendor design review of API-650 calculation set and general arrangement against the datasheet attributes table. | Vendor design review log; stamped GA drawings; API-650 calc package (per DEL-063-04 / DEL-063-06). |
| REQ-063-02-11 .. REQ-063-02-12 | Coating system specification review and witness of surface prep / DFT measurements during fabrication. | Coating inspection records; ITP (per DEL-063-05 ART-7D83DE2F05). |
| REQ-063-02-13 .. REQ-063-02-15 | Heater sizing calculation review; insulation thickness check against pour-point basis once `REQ-063-02-15` is resolved. | Heater calc; insulation schedule. |
| REQ-063-02-16 .. REQ-063-02-18 | P&ID and tie-in package review; flame-arrestor data sheet review; blanket-gas pressure-control logic review. | Stamped P&IDs; flame-arrestor data sheet; control narrative. |
| REQ-063-02-19 | Detailed-engineering review note (no construction verification required). | Detailed-engineering decision record. |
| REQ-063-02-20 .. REQ-063-02-28 | Interface walk-down against the Package Interface Requirements Matrix; construction-package tie-in inspection (consumed by DEL-063-03 / DEL-063-06). | Interface matrix sign-off; tie-in inspection records. |
| REQ-063-02-29 .. REQ-063-02-30 | EPC vendor package review and acceptance (DEL-063-06). | Acceptance checklist. |
| REQ-063-02-31 | SOW traceability matrix entry. | Traceability matrix in DEL-063-01 / DEL-063-02 closeout. |

## Documentation

Anticipated artifacts produced or referenced by this datasheet (from `_CONTEXT.md` and ARTIFACT_REGISTER.csv DEL-063-02 rows):

- Package technical datasheet (this document set; ART-6C19100F49).
- Vendor engineering handoff basis (ART-DD42CBB223).
- Package interface requirements matrix (ART-F211D13EFF).
- Interface fact evidence rows (ART-25F58D156D, ART-92C50C182D, ART-AFD82DEC15, ART-98E7B43876, ART-7428A3639D, ART-634E917188, ART-B4D0966BE3, ART-31029FE0E8, ART-3EBD1425B4).
- Major included equipment evidence (ART-966875EFC3).

Downstream consumers (per ARTIFACT_REGISTER.csv): DEL-063-03 (Construction Work Package), DEL-063-04 (Vendor Engineered Equipment Package), DEL-063-05 (Vendor Document Turnover Package), DEL-063-06 (EPC Vendor Package Review & Acceptance).
