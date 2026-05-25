# Specification: DEL-031-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-031`, the Transformer TXP-8500-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3 MVA, 13.8 kV / 600/347 V package. It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-031-01`) and the EPC Package Datasheet (`DEL-031-02`), and is subject to EPC Integrator integration review through `DEL-031-06_epc-vendor-package-review-and-acceptance`.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Construction installation, on-site tie-ins, foundation construction, and field turnover activities are excluded (covered by `DEL-031-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-031-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-031-06_epc-vendor-package-review-and-acceptance`.
- The upstream 13.8 kV switchgear (and the 04-25 → 03-25 sub-feed) is outside this package; the vendor package interface terminates at its 13.8 kV primary terminations.
- The downstream 600 V MCC and any 600 V switchboards / panelboards are outside this package; the vendor package interface terminates at the 600 V secondary terminations (and the 347 V neutral takeoff where supplied).
- Package-specific winding configuration, impedance, cooling class, insulation type (oil-filled vs. dry-type), tap-changer arrangement, accessories, protection package, foundation design, and installation location remain `TBD` where the accessible source set does not provide confirmed package-specific values; the vendor shall resolve these in vendor data during package engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-031-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-031-01`) and EPC Package Datasheet (`DEL-031-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-031-01`, `DEL-031-02`, `DEL-031-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-031-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-031`. | Responsibility statement review against Gate 7 package register. |
| REQ-031-04-003 | The vendor package shall be engineered to the seven applicable package interfaces: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 33; `INTERFACE_REGISTER.csv` rows for `PKG-031`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-031`. |
| REQ-031-04-004 | The transformer shall be engineered for the workbook-stated nameplate: 3 MVA, 13.8 kV primary, 600/347 V secondary. Frequency 60 Hz consistent with facility electrical service basis. Source: Workbook Packages row 33; `PACKAGE_REGISTER.csv` row `PKG-031`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table. | Vendor nameplate review against EPC Package Datasheet and workbook row 33. |
| REQ-031-04-005 | The 13.8 kV primary side shall be designed for connection to the facility 13.8 kV distribution bus (3 phase, 3 wire, 60 Hz, low-resistance grounded), sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building when allocated to the 03-25 facility. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services and 13.8 kV switchgear distribution paragraphs; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers". | Vendor single-line review against accepted facility distribution basis. |
| REQ-031-04-006 | The 600 V secondary shall be high-resistance grounded with a 5 A continuous grounding resistor; ground/resistor fault detection shall be provided on the served 600 V MCC; ground-fault protection on the 600 V system shall be alarm-only to maintain continuity of operations. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Vendor secondary grounding scheme review. |
| REQ-031-04-007 | The package shall meet major-equipment grounding requirements: direct connection to the ground grid at two points; ground well at the transformer for maintenance and operational testing with bolted ground connections at the test point; a separate copper ground conductor sized per CEC, in addition to the grounding conductor run with power wiring or cables. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs (incl. line ~2991). | Vendor grounding design review against DBM grounding basis and CEC. |
| REQ-031-04-008 | Where the vendor package supplies or terminates 13.8 kV primary cable, the cable shall be three-conductor copper TECK rated 15 kV with 133 percent insulation, shielded. Where the vendor package supplies or terminates the 600 V secondary feeder to the 600 V MCC, the cable shall be ACWU; single-conductor cables shall be avoided. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable paragraph and cable type table. | Vendor cable specification review. |
| REQ-031-04-009 | Foundation/support provisions shall accommodate either structural-steel transformer base or precast concrete bearing foundation, with spacing per CEC where an oil-filled transformer is selected; secondary containment shall be reviewed where applicable. Final foundation design is owned by EPC integration. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph and foundations table. | Vendor support/foundation interface review against the Structural / Foundations / Supports interface (`IFC-15FCC571C7`). |
| REQ-031-04-010 | The vendor package shall not include the upstream 13.8 kV switchgear, the downstream 600 V MCC, or facility lighting/panelboard loads; the vendor package terminates at its 13.8 kV primary and 600/347 V secondary terminations. Source: package boundary definition in this Specification, Scope and Exclusions; `_CONTEXT.md`, Scope. | Vendor design boundary review at EPC integration review (`DEL-031-06`). |
| REQ-031-04-011 | The vendor package shall not engineer a 13.8 kV-level emergency generator interface; standby power is provided at the 600 V MCC level via LV standby natural-gas generators with transfer switches and is outside this package's scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "600V MCC and Standby Power". | Vendor design review confirms no 13.8 kV emergency-generator tie-in is engineered. |
| REQ-031-04-012 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-031-04`. | Artifact register check against vendor delivery. |
| REQ-031-04-013 | Source gaps for winding configuration, impedance, cooling class, insulation type, tap-changer arrangement, accessories, protection package, foundation design, and installation location shall be resolved by vendor data during package engineering and informed by `DEL-031-02`; values shall not be invented in advance of vendor design. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` not extracted into deliverable-local truth set. | Vendor data review at EPC vendor package acceptance (`DEL-031-06`). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding (incl. separate copper ground conductor sizing), conduit support, transformer spacing for oil-filled units, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable where the host electrical building, transformer pad, or external cable routes encounter hazardous-area classification. | Applicable; package location/classification TBD. |
| Industry distribution-transformer standards (e.g., IEEE/CSA dry-type and liquid-immersed distribution transformer standards) | Likely applicable to vendor transformer design, type testing, sound, and efficiency. ASSUMPTION: standard family applies; specific edition/clause TBD pending source confirmation. | ASSUMPTION; not extracted from accessible sources. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-031-01`) and EPC Package Datasheet (`DEL-031-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-031-01` Scope of Work and `DEL-031-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 33 and Gate 7 registers. | Package name, IDs, discipline, WBS (01), and CoA tracking number (26020-01-30-022) match. |
| Nameplate fidelity | Compare vendor transformer nameplate to workbook-stated 3 MVA, 13.8 kV / 600/347 V. | Nameplate matches workbook row 33 and EPC Package Datasheet. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-031`. | All seven applicable interfaces (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) are addressed. |
| Service basis fidelity | Compare vendor primary/secondary basis to DBM medium-voltage and low-voltage services. | 13.8 kV LRG primary and 600 V HRG secondary basis preserved. |
| Distribution topology | Compare vendor single-line diagram to DBM 13.8 kV distribution paragraph and 03-25 "Incoming Power and Transformers". | The vendor package is represented as a downstream step-down transformer fed from 13.8 kV and supplying a 600 V MCC; not redefined as switchgear or MCC scope. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to `DEL-031-05` (turnover) and `DEL-031-06` (acceptance) workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (the TXP-8500-1 transformer assembly, including windings, bushings, tap changer, cooling system, accessories, protection devices, and monitoring as scoped by vendor data).
- Vendor package design basis.
- Vendor package datasheet set (nameplate, winding configuration, impedance, cooling class, insulation type, tap arrangement, primary/secondary terminations, ground bushing/connection, protection package, accessories, dimensions/weights, sound level, environmental ratings).
- Source-gap / `TBD` list to be closed by vendor data during package engineering.

The deliverable shall cite the Gate 7 snapshot, workbook row 33, applicable Gate 7 registers, and the DBM electrical source slices used for the 13.8 kV / 600 V step-down transformer design basis, and shall reference the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
