# Specification — DEL-016-01 Scope of Work (PKG-016 Transformer TXP-8200-1)

## Scope

### In scope

The EPC Integrator Scope of Work for PKG-016 covers the integration of the package "Transformer TXP-8200-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3MVA 13.8kV/600/347V" into the 03-25 process facility. It includes:

- Identification and boundary definition of the tagged equipment (TXP-8200-1) as a distinct flat project package under WBS 02, tracking number 26020-02-30-007. [Source: PACKAGE_REGISTER.csv row PKG-016; SCOPE_LEDGER.csv SOW-0017]
- The package function narrative: stepping 13.8 kV incoming feed down to 600 V (with 347 V neutral derivation implied by package name) for the 600 V MCC serving LV loads. [Source: DBM SEC-12, Incoming Power and Transformers]
- The whole-facility integration narrative locating TXP-8200-1 between the 13.8 kV cross-facility incoming power and the downstream 600 V MCC in the 600 V electrical building context. [Source: DBM SEC-12, SEC-08 Buildings]
- Responsibility assignment between Package Vendor (engineering, design, vendor documentation, physical equipment) and EPC Integrator (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). [Source: PACKAGE_REGISTER.csv RACI text]
- Identification of applicable interface types this package presents to the facility: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. [Source: INTERFACE_REGISTER.csv; PACKAGE_REGISTER.csv]

### Out of scope

- Detailed package engineering/design and physical equipment scope (assigned to the Package Vendor production unit in `DEL-016-04`). [Source: DELIVERABLE_REGISTER.csv]
- The detailed Package Datasheet, vendor handoff basis, and interface requirements matrix (assigned to `DEL-016-02`). [Source: DELIVERABLE_REGISTER.csv]
- Construction work package, installation, tie-in workface plan, and turnover checklist (assigned to `DEL-016-03`). [Source: DELIVERABLE_REGISTER.csv]
- Vendor document register and turnover package (assigned to `DEL-016-05`). [Source: DELIVERABLE_REGISTER.csv]
- EPC Vendor Package Review and Acceptance (assigned to `DEL-016-06`). [Source: DELIVERABLE_REGISTER.csv]
- Detailed electrical studies (harmonic, reactive-power, short-circuit, grounding-resistor sizing). Not part of this SoW; coordinated separately. [Source: DBM SEC-12]

## Requirements

| ID | Requirement | Basis | Verification Approach |
|---|---|---|---|
| SOW-016-01-R01 | The SoW SHALL identify the package by tag TXP-8200-1, package name as registered, WBS 02, tracking number 26020-02-30-007, and workbook row 18. | PACKAGE_REGISTER.csv row PKG-016 | Documentation review against PACKAGE_REGISTER.csv. |
| SOW-016-01-R02 | The SoW SHALL state the package function as 13.8 kV → 600 V (with 347 V neutral notation as carried in the package name) step-down distribution transformer feeding the 600 V MCC for LV loads. | DBM SEC-12, Incoming Power and Transformers table | Cross-reference to DBM SEC-12 row. |
| SOW-016-01-R03 | The SoW SHALL state the boundary of the package: upstream interface at the 13.8 kV cross-facility feed (sub-fed from 04-25 Main Switchgear), downstream interface at the 600 V MCC. | DBM SEC-12, Incoming Power and Transformers | Boundary diagram or narrative cross-checked to DBM SEC-12. |
| SOW-016-01-R04 | The SoW SHALL list applicable interface types for PKG-016: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | INTERFACE_REGISTER.csv (7 rows for PKG-016); PACKAGE_REGISTER.csv interface list | Inspection — every interface type listed in INTERFACE_REGISTER for PKG-016 appears in the SoW. |
| SOW-016-01-R05 | The SoW SHALL identify Package Vendor as owner of package engineering, package design, vendor documentation, and the physical equipment package; and EPC Integrator as owner of facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv RACI text | RACI table inspection. |
| SOW-016-01-R06 | The SoW SHALL state that this deliverable supports objectives OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 (per package-grouping mapping; ASSUMPTION at deliverable-row level). | OBJECTIVE_DELIVERABLE_MAP.csv | Cross-reference to OBJECTIVE_DELIVERABLE_MAP.csv. |
| SOW-016-01-R07 | The SoW SHALL state the general area classification basis: Class I Zone 2, Gas Groups IIA and IIB unless detailed area-classification drawings indicate otherwise. | DBM SEC-12 Area Classification | Cross-reference to DBM SEC-12. |
| SOW-016-01-R08 | The SoW SHALL identify the package location context as the 600 V electrical building context within the 03-25 facility. | DBM SEC-08 Buildings; DBM SEC-12 | Cross-reference. |
| SOW-016-01-R09 (ASSUMPTION) | The SoW SHOULD note that detailed transformer construction parameters (form factor, cooling class, impedance, BIL, tap-changer configuration, accessories) are TBD at SoW stage and will be developed in `DEL-016-02_package-datasheet` and `DEL-016-04_vendor-engineered-equipment-package`. | DELIVERABLE_REGISTER.csv; absence in DBM source slices | Forward-reference confirmed by inspection of `DEL-016-02` and `DEL-016-04` scopes. |
| SOW-016-01-R10 | The SoW SHALL list responsibility for facility-side foundations, raceways, grounding/bonding, lighting in the area, and structural supports as EPC Integrator interface scope. | DBM SEC-08 (Foundations, Buildings); DBM SEC-12 (Raceways, Grounding); INTERFACE_REGISTER.csv | Interface-by-interface cross-check. |

## Standards

| Standard / Document | Applicability | Location |
|---|---|---|
| Project DBM `3-25_Comp_and_Liquids_DBM.md` SEC-12 (Electrical Basis) | Authoritative for system voltages, incoming-power topology, area classification, and raceway separation. | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Project DBM SEC-08 (Buildings, Foundations) | Authoritative for facility civil/structural and building context. | same |
| API RP 505 | Cited by DBM SEC-12 as the basis for hazardous-area classification of process modules/buildings. | location TBD (referenced indirectly via DBM SEC-12) |
| 26020 Package Requirements | Listed in `_Sources` as `26020-Package_Requirements.docx`; package-row-specific applicability TBD. | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — not opened in this run; location TBD for transformer-specific clauses. |
| Industry transformer standards (e.g., IEEE C57 series, IEC 60076) | Likely applicable to a 3 MVA distribution transformer. **ASSUMPTION: likely applicable**; specific clauses cannot be derived without source text. | location TBD |

## Verification

| Requirement ID | Verification Method | Evidence |
|---|---|---|
| R01–R06, R08, R10 | Documentation review against Gate 7 registers and DBM SEC-12. | Cross-reference table in the SoW. |
| R07 | Inspection against DBM SEC-12 Area Classification statement. | Documented citation. |
| R09 | Forward-reference inspection of DEL-016-02 and DEL-016-04 produced four-doc sets. | Cross-deliverable inspection (out of scope for the SoW author; consumed by reviewer). |

## Documentation

Anticipated artifacts (carried forward from `_CONTEXT.md` and ARTIFACT_REGISTER.csv):

- Package scope of work (`ART-9B23EFA6EE`)
- Tagged equipment and package identity list (`ART-65C8336085`)
- Package function and whole-facility integration narrative (`ART-4E2F8A9FDF`)
- Package responsibility assignment record (`ART-F610CDF9EC`)
