# Specification — DEL-101-02 Package Datasheet (PKG-101 Precast concrete foundations)

> Normative requirements that the Package Datasheet artifact set must satisfy as the EPC Integrator's technical handoff to third-party vendor or discipline package engineering for PKG-101.

## Scope

**In scope.** This specification governs the content and conformance of the Package Datasheet for PKG-101 "Precast concrete foundations" (Structural, WBS 01, Workbook row 102) as a mandatory EPC Integrator technical handoff deliverable. The datasheet shall provide the technical basis, battery limits, design expectations, and source-supported requirements required for third-party vendor or discipline package engineering and design of precast concrete foundations supporting West Doe Deepcut equipment (notably transformers, compressors, and other structures using precast block on driven steel piles). Source: `_CONTEXT.md` Scope; PACKAGE_REGISTER.csv row PKG-101.

**Out of scope.** Detailed civil implementation, foundation design, drainage design, geotechnical interpretation, and discipline-specific equipment design (DBM `4-25_Deepcut_DBM.md` line 184); package-specific exclusions are otherwise unstated in source materials (PACKAGE_REGISTER.csv Exclusions = TBD). The construction work package itself is `DEL-101-03`, not this deliverable (ARTIFACT_REGISTER.csv).

## Requirements

> Each requirement is REQ-101-02-NN. Requirements derive from `_CONTEXT.md`, the GATE-07 registers, the deliverable's anticipated-artifact list, and DBM `4-25_Deepcut_DBM.md` source slices. Inferred items are labeled **ASSUMPTION**.

| ID | Requirement | Source |
|---|---|---|
| REQ-101-02-01 | The datasheet shall identify the package (PKG-101, CoA 26020-01-36-001, Workbook row 102, WBS 01, Structural). | `_CONTEXT.md`; PACKAGE_REGISTER.csv row PKG-101 |
| REQ-101-02-02 | The datasheet shall state the package responsibility model: EPC Integrator or discipline subcontractor, source-dependent; no separate vendor-package ownership model is to be inferred. | PACKAGE_REGISTER.csv ResponsibilityModel, row PKG-101 |
| REQ-101-02-03 | The datasheet shall enumerate the applicable interface types: (a) Grading / Site Drainage / Spill Containment (IFC-26343B703C) and (b) Structural / Foundations / Supports (IFC-BED3DE4194), and carry them as interface evidence (ART-B722B4EE97, ART-1D7D43BEDB). | INTERFACE_REGISTER.csv; ARTIFACT_REGISTER.csv |
| REQ-101-02-04 | The datasheet shall provide a Package Interface Requirements Matrix (ART-6679E64F6F) keyed to the registered interfaces. | ARTIFACT_REGISTER.csv |
| REQ-101-02-05 | The datasheet shall cite the governing codes/standards applicable to precast concrete foundations: National Building Code of Canada; CAN/CSA A23.3 (concrete design); CSA A23.1 / A23.2 (concrete materials, construction, testing); Canadian Foundation Engineering Manual; and CAN/CSA-S16 / CSA G40.20/G40.21 for any structural steel interfaces. | DBM `4-25_Deepcut_DBM.md` § "Governing Civil and Structural Basis" (lines 2670-2679) |
| REQ-101-02-06 | The datasheet shall state the default foundation support basis: driven steel piles, unless a more specific basis applies (e.g., precast concrete bearing foundations for transformers; precast concrete block on driven steel piles for compressors). | DBM § "Piles and Foundations" (lines 2740, 2745-2749) |
| REQ-101-02-07 | The datasheet shall record that compressor foundations using precast concrete block on driven steel piles are subject to dynamic analysis, and that dynamic analysis results are currently TBD. | DBM lines 2746, 2838, 2852 |
| REQ-101-02-08 | The datasheet shall record the alternate compressor concept (direct steel-skid-to-pile welding) as TBD, considered unlikely for this compressor size, pending Propak verification. | DBM lines 2747, 2839, 2853 |
| REQ-101-02-09 | The datasheet shall record the requirement that compressor skid/foundation design consider containment and management of on-skid oil leaks. | DBM line 2748 |
| REQ-101-02-10 | The datasheet shall record geotechnical inputs as TBD pending the geotechnical assessment report: bearing capacity, LPILE load-deflection curves, dynamic design criteria. | DBM § "Geotechnical and Topographical Assumptions" (lines 2687-2693); § "External Dependencies" (lines 2832-2839) |
| REQ-101-02-11 | The datasheet shall record the grading interface constraints relevant to top-of-pile-cap elevations (pad slope 1.5% nominal; may be reduced to 1.0% where required) and the spill-containment / surface-control expectations around equipment. | DBM § "Site Grading and Surface Water Management" (lines 2702, 2710-2711) |
| REQ-101-02-12 | The datasheet shall not state package-specific exclusions beyond those supported by source. Exclusions are currently TBD (no package-specific exclusions in source). | PACKAGE_REGISTER.csv Exclusions, row PKG-101 |
| REQ-101-02-13 | Every non-trivial value in the datasheet shall cite a source path and section. Where the source cannot be located locally, `location TBD` shall be used; values shall not be invented. | Skill `four-documents` non-negotiable constraints |
| REQ-101-02-14 | The datasheet shall demonstrate support of the package's objectives: OBJ-001 and OBJ-008 (per DELIVERABLE_REGISTER.csv). **ASSUMPTION:** the OBJ-001/OBJ-008 association is consumed as directional context from the package register / deliverable register; objective texts not consulted in this run. | DELIVERABLE_REGISTER.csv; PACKAGE_REGISTER.csv |
| REQ-101-02-15 | The datasheet shall identify the workbook source row (Packages row 102) and the DBM source slice (4-25_Deepcut_DBM.md, "Piles and Foundations"); where cell-level workbook data has not been opened, it shall be marked `location TBD`. | `_REFERENCES.md`; PACKAGE_REGISTER.csv SourceRefs |

## Standards

| Standard / Reference | Applicability | Local source slice |
|---|---|---|
| National Building Code of Canada | Building code basis for structures supported on foundations | DBM `4-25_Deepcut_DBM.md` line 2672; `location TBD` for code text |
| CAN/CSA A23.3 Design of Concrete Structures | Concrete design basis for precast elements | DBM line 2674; code text `location TBD` |
| CSA A23.1 / A23.2 Concrete materials, construction, and testing | Construction and QA basis for precast concrete elements | DBM line 2677; code text `location TBD` |
| Canadian Foundation Engineering Manual | Foundation engineering basis | DBM line 2675; `location TBD` |
| CAN/CSA-S16 Design of Steel Structures | Adjacent structural-steel interface | DBM line 2673; `location TBD` |
| CSA G40.20/G40.21 (350W W/HSS; 300W channels/plates/angles) | Structural steel material grades for interfacing steel | DBM line 2676 |

## Verification

| Requirement | Verification Method |
|---|---|
| REQ-101-02-01, -02, -03, -04 | Document review against `_CONTEXT.md` and GATE-07 registers (DELIVERABLE / PACKAGE / INTERFACE / ARTIFACT). |
| REQ-101-02-05 | Document review against DBM `4-25_Deepcut_DBM.md` § "Governing Civil and Structural Basis" with code citations. |
| REQ-101-02-06, -07, -08, -09 | Document review against DBM § "Piles and Foundations" rows; verify each precast-related entry is reflected. |
| REQ-101-02-10 | Confirm geotechnical TBDs are surfaced (not silently resolved) and tied to DBM "External Dependencies." |
| REQ-101-02-11 | Cross-check against DBM § "Site Grading and Surface Water Management" values for pad slope and surface control. |
| REQ-101-02-12, -13 | QA gate: no invented values; absent exclusions explicitly marked TBD; all non-trivial values cite source. |
| REQ-101-02-14 | Confirm objective association recorded as ASSUMPTION (PACKAGE_HEURISTIC) until human ruling. |
| REQ-101-02-15 | Confirm workbook source row and any unread cell-level slices are marked `location TBD`. |

## Documentation

The Package Datasheet artifact set shall include:

- Package technical datasheet (ART-7208F665C3)
- Vendor engineering handoff basis (ART-080F36F89C)
- Package interface requirements matrix (ART-6679E64F6F)
- Interface fact records (ART-B722B4EE97 → IFC-26343B703C; ART-1D7D43BEDB → IFC-BED3DE4194)

Source: ARTIFACT_REGISTER.csv (GATE-07 snapshot), rows ParentDeliverableID=`DEL-101-02_package-datasheet`.
