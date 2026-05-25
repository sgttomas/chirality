# Specification: DEL-038-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-038`, the 600V ELECTRICAL BUILDING (820-1) package. It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-038-01`) and Package Datasheet (`DEL-038-02`), and is subject to EPC Integrator integration review through `DEL-038-06_epc-vendor-package-review-and-acceptance`.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package (the prefabricated, modular electrical building tagged 820-1 and the equipment it houses as required by detailed design). The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Construction installation, on-site tie-ins, and field turnover activities are excluded (covered by `DEL-038-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-038-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-038-06_epc-vendor-package-review-and-acceptance`.
- Package-specific equipment lists, voltage class confirmation for tag 820-1, building dimensions, MCC ratings, transformer kVA, UPS count/rating, battery autonomy, distribution-panel assignments, and installation location remain `TBD` where the accessible source set does not provide confirmed package-specific values; the vendor shall resolve these in vendor data during package engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-038-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-038-01`) and Package Datasheet (`DEL-038-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-038-01`, `DEL-038-02`, `DEL-038-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-038-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-038`. | Responsibility statement review against Gate 7 package register. |
| REQ-038-04-003 | The vendor package shall be engineered to the twelve applicable package interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 40; `INTERFACE_REGISTER.csv` rows for `PKG-038`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-038`. |
| REQ-038-04-004 | The building shall be a prefabricated, modular building, located (per EPC site decision) in a general purpose area, climate controlled with n + 1 HVAC, elevated on piles, with bottom entry for incoming and outgoing power cables. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | Vendor design basis check against DBM electrical-buildings basis. |
| REQ-038-04-005 | The building shall be wired with TECK and ACIC cables; EMT conduit may be used between adjacent equipment (e.g., control panels to contactor panels). An outdoor GFI receptacle shall be provided for exterior maintenance. Equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | Vendor design review against DBM wiring/door provisions. |
| REQ-038-04-006 | The building shall house, as required by detailed design, 600 V MCCs, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, network racks, and 120 V AC / 125 V DC UPS systems with battery banks and distribution panels. The package-specific equipment list shall be resolved by vendor data. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | Vendor equipment list review against DBM permitted equipment set. |
| REQ-038-04-007 | The vendor package shall meet grounding/bonding requirements per the DBM electrical basis: major equipment connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Vendor grounding design review. |
| REQ-038-04-008 | Vendor-supplied internal cable tray and conduit routing shall preserve maintenance access, including door clearances and equipment-removal paths. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs; Maintenance Access interface row for `PKG-038`. | Vendor layout review against the Maintenance Access interface. |
| REQ-038-04-009 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `ARTIFACT_REGISTER.csv` rows `ART-4F595A7D97`, `ART-CF8553E9A3`. | Artifact register check against vendor delivery. |
| REQ-038-04-010 | The vendor design shall not be finalized until the building-tag voltage conflict (CFL-038-04-001: 820-1 labeled "600V" by the workbook package name versus "6.9 kV Inlet / Sales Compressor Electrical Building" by the DBM electrical-buildings table) is resolved through EPC integration. Source: Workbook Packages row 40; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings table. | Open-item review at integration acceptance (`DEL-038-06`). |
| REQ-038-04-011 | Source gaps for package-specific equipment counts/ratings, building dimensions, transformer kVA, MCC schedule, UPS sizing, installation location, and area classification shall be resolved by vendor data during package engineering; values shall not be invented in advance of vendor design. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search returned no PKG-038-specific match. | Vendor data review at EPC vendor package acceptance (`DEL-038-06`). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding (separate copper ground sizing for distribution transformers, panelboards, three-phase motors >100 hp) and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | MCC, distribution, grounding, cable/raceway, and UPS basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification. DBM places electrical buildings in general purpose areas; final classification depends on EPC site assignment. | Applicable; package location/classification TBD. |
| HVAC sizing basis (n + 1) | DBM-defined climate-control redundancy for electrical buildings. | Applicable per DBM. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-038-01`) and EPC Package Datasheet (`DEL-038-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-038-01` Scope of Work and `DEL-038-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 40 and Gate 7 registers. | Package name, IDs, discipline, WBS, and CoA tracking number match. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-038`. | All twelve applicable interfaces are addressed in vendor design. |
| Voltage-class conflict | Confirm the building voltage class for tag 820-1 has been ruled by the EPC Integrator. | Conflict CFL-038-04-001 is resolved or carried explicitly as an EPC integration open item. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, conflicts, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to `DEL-038-05` (turnover) and `DEL-038-06` (acceptance) workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (the 820-1 building and its housed equipment as defined by vendor data).
- Vendor package design basis.
- Vendor package datasheet set (building, MCCs, distribution transformers and panelboards, UPS systems, HVAC, cable systems, grounding, doors).
- Source-gap / `TBD` list to be closed by vendor data during package engineering, including the building-tag voltage-class ruling.

The deliverable shall cite the Gate 7 snapshot, workbook row 40, applicable Gate 7 registers, and the DBM electrical-buildings source slices used for building basis, equipment set, HVAC, wiring, doors, foundations, and grounding, and shall reference the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
