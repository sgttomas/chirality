# Specification: DEL-027-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-027`, the Transformer TXP-8301-1 step-down distribution transformer package (20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV per workbook title). It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-027-01`) and Package Datasheet (`DEL-027-02`), and is subject to EPC Integrator integration review through `DEL-027-06_epc-vendor-package-review-and-acceptance`.

The package is a vendor-owned Electrical package under WBS 01 (CoA 26020-01-30-018). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Construction installation, on-site tie-ins, and field turnover activities are excluded (covered by `DEL-027-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-027-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-027-06_epc-vendor-package-review-and-acceptance`.
- Package-specific transformer cooling class (ONAN/ONAF basis for the 20/26 MVA dual rating), tap-changer configuration, BIL, impedance, vector group, exact secondary winding configuration (in particular the 0.4 kV winding), oil-containment design, NGR cubicle location, and installation pad assignment remain `TBD` where the accessible source set does not provide confirmed package-specific values; the vendor shall resolve these in vendor data during package engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-027-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-027-01`) and Package Datasheet (`DEL-027-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-027-01`, `DEL-027-02`, `DEL-027-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-027-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-027`. | Responsibility statement review against Gate 7 package register. |
| REQ-027-04-003 | The vendor package shall be engineered to the seven applicable package interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 29; `INTERFACE_REGISTER.csv` rows for `PKG-027`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-027`. |
| REQ-027-04-004 | The vendor package primary winding shall be compatible with the facility 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded backbone distribution. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage table. | Vendor design basis check against the DBM electrical service basis. |
| REQ-027-04-005 | The vendor package 6.9 kV winding (where applicable) shall be compatible with the facility 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded process AC inverter-drive motor service. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage table. | Vendor design basis check against DBM 6.9 kV service. |
| REQ-027-04-006 | The vendor package 6.9 kV neutral shall be grounded through a 100 A, 10 s neutral grounding resistor operated as a tripping system, where the 6.9 kV winding is provided as a transformer secondary. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph. | Vendor NGR design review against DBM grounding paragraph. |
| REQ-027-04-007 | The vendor package shall meet major-equipment grounding requirements: direct connection to the facility ground grid at two points; ground wells with bolted ground connections at test points at power transformers; CEC-sized separate copper grounding conductor for the distribution transformer in addition to the grounding conductor run with power wiring. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Vendor grounding design review against DBM grounding paragraphs. |
| REQ-027-04-008 | The vendor package supports shall be designed for precast concrete bearing foundations and/or structural-steel transformer bases consistent with DBM transformer practice, and shall comply with CEC spacing for large oil-filled transformers; secondary containment requirements shall be reviewed, and selection shall avoid or limit containment requirements where practical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformer paragraphs. | Vendor support and spacing review against DBM transformer paragraph. |
| REQ-027-04-009 | The vendor package terminations shall be compatible with the facility medium-voltage cable basis: three-conductor copper TECK 15 kV / 133 percent insulation, shielded, on the 13.8 kV side; and three-conductor copper TECK 8 kV / 100 percent insulation, shielded, on the 6.9 kV side. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage cable table. | Vendor termination/bushing/cable-box review against DBM cable table. |
| REQ-027-04-010 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `ARTIFACT_REGISTER.csv` rows `ART-6FA1DBA3D1`, `ART-0723EEECE8`. | Artifact register check against vendor delivery. |
| REQ-027-04-011 | Source gaps for cooling class (ONAN/ONAF for the 20/26 MVA dual rating), BIL, impedance, vector group, tap-changer, exact secondary winding configuration (in particular the 0.4 kV winding), oil-containment design, and installation pad assignment shall be resolved by vendor data during package engineering; values shall not be invented in advance of vendor design. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search returned no PKG-027 match within the source slices accessible to this run. | Vendor data review at EPC vendor package acceptance (`DEL-027-06`). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding (separate copper grounding conductor sizing for distribution transformers), transformer spacing, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage / MCC / grounding / cable / raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Transformer industry standards (e.g., CSA C88, IEEE C57 series) | ASSUMPTION: applicable to a large oil-filled step-down distribution transformer of this rating; specific clause applicability is vendor scope. | ASSUMPTION; not cited in accessible source slices. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-027-01`) and EPC Package Datasheet (`DEL-027-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-027-01` Scope of Work and `DEL-027-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 29 and Gate 7 registers. | Package name, IDs, discipline, WBS, and CoA tracking number match. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-027`. | All seven applicable interfaces are addressed. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to `DEL-027-05` (turnover) and `DEL-027-06` (acceptance) workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package (`ART-6FA1DBA3D1`).
- Vendor package design basis (`ART-0723EEECE8`, design-basis portion).
- Vendor package datasheet set (`ART-0723EEECE8`, datasheet portion).
- Source-gap / `TBD` list to be closed by vendor data during package engineering.

The deliverable shall cite the Gate 7 snapshot, workbook row 29, applicable Gate 7 registers, and the DBM electrical source slices used for the 13.8 kV / 6.9 kV / 600 V electrical voltage basis, step-down transformer distribution paragraph, transformers paragraph, grounding paragraphs, foundations paragraph, electrical buildings paragraph, and medium-voltage cable table, and shall reference the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
