# Specification — DEL-031-01 Scope of Work (PKG-031 Transformer TXP-8500-1)

## Scope

### In scope

The EPC Integrator Scope of Work for PKG-031 covers the integration of the package "Transformer TXP-8500-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3MVA 13.8kV/600/347V" into the West Doe Deepcut (04-25) process facility. It includes:

- Identification and boundary definition of the tagged equipment (TXP-8500-1) as a distinct flat project package under WBS 01, CoA tracking number 26020-01-30-022. [Source: PACKAGE_REGISTER.csv row PKG-031; SCOPE_LEDGER.csv SOW-0032]
- The package function narrative: stepping the 13.8 kV facility feed down to 600 V (with 347 V neutral derivation implied by package name) for a 600 V MCC serving low-voltage loads. [Source: DBM-Deepcut Power Distribution narrative, lines 2917–2929, 2959]
- The whole-facility integration narrative locating TXP-8500-1 within the 13.8 kV radial distribution from the plant main switchgear to a 600 V MCC within a prefabricated modular electrical building. [Source: DBM-Deepcut Power Distribution, Electrical Buildings narrative, lines 2973, 2977]
- Responsibility assignment between Package Vendor (engineering, design, vendor documentation, physical equipment) and EPC Integrator (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). [Source: PACKAGE_REGISTER.csv RACI text]
- Identification of applicable interface types this package presents to the facility: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. [Source: INTERFACE_REGISTER.csv (7 rows for PKG-031); PACKAGE_REGISTER.csv]

### Out of scope

- Detailed package engineering/design and physical equipment scope (assigned to the Package Vendor production unit in `DEL-031-04`). [Source: DELIVERABLE_REGISTER.csv]
- The detailed Package Datasheet, vendor handoff basis, and interface requirements matrix (assigned to `DEL-031-02`). [Source: DELIVERABLE_REGISTER.csv]
- Construction work package, installation, tie-in workface plan, and turnover checklist (assigned to `DEL-031-03`). [Source: DELIVERABLE_REGISTER.csv]
- Vendor document register and turnover package (assigned to `DEL-031-05`). [Source: DELIVERABLE_REGISTER.csv]
- EPC Vendor Package Review and Acceptance (assigned to `DEL-031-06`). [Source: DELIVERABLE_REGISTER.csv]
- Detailed electrical studies (harmonic, reactive-power, short-circuit, grounding-resistor sizing). Not part of this SoW; coordinated separately. [Source: DBM-Deepcut Electrical Basis general]

## Requirements

| ID | Requirement | Basis | Verification Approach |
|---|---|---|---|
| SOW-031-01-R01 | The SoW SHALL identify the package by tag TXP-8500-1, package name as registered, WBS 01, CoA tracking number 26020-01-30-022, and workbook row 33. | PACKAGE_REGISTER.csv row PKG-031 | Documentation review against PACKAGE_REGISTER.csv. |
| SOW-031-01-R02 | The SoW SHALL state the package function as 13.8 kV → 600 V (with 347 V neutral notation as carried in the package name) step-down distribution transformer feeding a 600 V MCC for LV loads. | DBM-Deepcut Power Distribution narrative (lines 2919, 2937, 2959) | Cross-reference to DBM-Deepcut electrical basis sections. |
| SOW-031-01-R03 | The SoW SHALL state the boundary of the package: upstream interface at the 13.8 kV facility distribution (radial feed from the plant main 13.8 kV switchgear), downstream interface at the 600 V MCC. | DBM-Deepcut Power Distribution (lines 2917–2929) | Boundary diagram or narrative cross-checked to DBM-Deepcut. |
| SOW-031-01-R04 | The SoW SHALL list applicable interface types for PKG-031: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | INTERFACE_REGISTER.csv (7 rows for PKG-031); PACKAGE_REGISTER.csv interface list | Inspection — every interface type listed in INTERFACE_REGISTER for PKG-031 appears in the SoW. |
| SOW-031-01-R05 | The SoW SHALL identify Package Vendor as owner of package engineering, package design, vendor documentation, and the physical equipment package; and EPC Integrator as owner of facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv RACI text | RACI table inspection. |
| SOW-031-01-R06 (ASSUMPTION) | The SoW SHALL state that this deliverable supports objectives OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 (per package-grouping mapping; ASSUMPTION at deliverable-row level). | OBJECTIVE_DELIVERABLE_MAP.csv | Cross-reference to OBJECTIVE_DELIVERABLE_MAP.csv. |
| SOW-031-01-R07 | The SoW SHALL state the general area classification basis: Class I Zone 2, Gas Groups IIA and IIB unless detailed area-classification drawings indicate otherwise. | DBM-Deepcut "Area Classification" (lines 2905–2913) | Cross-reference to DBM-Deepcut. |
| SOW-031-01-R08 | The SoW SHALL identify the package location context as a prefabricated modular electrical building within the West Doe Deepcut (04-25) facility. | DBM-Deepcut Electrical Buildings (lines 2973, 2977) | Cross-reference. |
| SOW-031-01-R09 (ASSUMPTION) | The SoW SHOULD note that detailed transformer construction parameters (form factor, cooling class, impedance, BIL, tap-changer configuration, accessories) are TBD at SoW stage and will be developed in `DEL-031-02_package-datasheet` and `DEL-031-04_vendor-engineered-equipment-package`. | DELIVERABLE_REGISTER.csv; absence in accessible DBM source slices | Forward-reference confirmed by inspection of `DEL-031-02` and `DEL-031-04` scopes. |
| SOW-031-01-R10 | The SoW SHALL state that the 600 V secondary system is high-resistance grounded with a 5 A continuous resistor at the transformer neutral, and that 600 V ground-fault protection is alarm-only to maintain continuity of operations. | DBM-Deepcut System Voltages table (line 2937); DBM-Deepcut Grounding (line 2985) | Cross-reference to DBM-Deepcut. |
| SOW-031-01-R11 | The SoW SHALL list responsibility for facility-side foundations, raceways, grounding/bonding, lighting in the area, and structural supports as EPC Integrator interface scope. | DBM-Deepcut Electrical Buildings, Raceways, Grounding sections; INTERFACE_REGISTER.csv | Interface-by-interface cross-check. |

## Standards

| Standard / Document | Applicability | Location |
|---|---|---|
| Project DBM `4-25_Deepcut_DBM.md` Electrical Basis sections | Authoritative for system voltages, incoming-power topology, area classification, electrical buildings, raceway separation, and grounding. | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| API RP 505, 2nd Edition | Cited by DBM as the basis for hazardous-area classification of process modules/buildings (Class I Zone 2). | Cited in DBM standards table (line 3382); document location TBD outside DBM citation. |
| API RP 500, 4th Edition | Cited by DBM for Class I, Division 1/2 area classification (applied with NEC and CSA). | Cited in DBM standards table (line 3381); document location TBD outside DBM citation. |
| Canadian Electrical Code (CEC) | Cited by DBM for raceway, grounding, and wiring methods. | Cited in DBM (lines 2991, 3025); document location TBD. |
| 26020 Package Requirements | Listed in `_Sources` as `26020-Package_Requirements.docx`; package-row-specific applicability TBD. | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — not opened in this run; location TBD for transformer-specific clauses. |
| Industry transformer standards (e.g., IEEE C57 series, IEC 60076) | Likely applicable to a 3 MVA distribution transformer. **ASSUMPTION: likely applicable**; specific clauses cannot be derived without source text. | location TBD |

## Verification

| Requirement ID | Verification Method | Evidence |
|---|---|---|
| R01–R06, R08, R11 | Documentation review against Gate 7 registers and DBM-Deepcut electrical basis. | Cross-reference table in the SoW. |
| R07 | Inspection against DBM-Deepcut Area Classification statement (lines 2905–2913). | Documented citation. |
| R09 | Forward-reference inspection of DEL-031-02 and DEL-031-04 produced four-doc sets. | Cross-deliverable inspection (out of scope for the SoW author; consumed by reviewer). |
| R10 | Inspection against DBM-Deepcut System Voltages table and Grounding narrative. | Documented citation. |

## Documentation

Anticipated artifacts (carried forward from `_CONTEXT.md` and ARTIFACT_REGISTER.csv):

- Package scope of work (`ART-38263068FC`)
- Tagged equipment and package identity list (`ART-C52F26582F`)
- Package function and whole-facility integration narrative (`ART-F816DB4F10`)
- Package responsibility assignment record (`ART-23AA8A388B`)
