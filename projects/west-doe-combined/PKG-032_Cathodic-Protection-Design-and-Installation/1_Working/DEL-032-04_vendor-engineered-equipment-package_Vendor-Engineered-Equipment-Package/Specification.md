# Specification: DEL-032-04_vendor-engineered-equipment-package

## Scope

This specification governs the Package Vendor-owned engineering, design, fabrication/supply, and physical equipment package for `PKG-032`, the Cathodic Protection Design and Installation package. It is a Gate 5 vendor production unit anchored by the EPC Scope of Work (`DEL-032-01`) and Package Datasheet (`DEL-032-02`), and is subject to EPC Integrator integration review via the corresponding sibling acceptance deliverable in PKG-032.

The package is a vendor-owned Electrical package under WBS 03. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Cathodic protection engineering and supply is treated by the Deepcut DBM as outside the facility electrical design scope and as an owner/vendor responsibility with which the facility design coordinates (see `Guidance.md` Conflict Table for the inclusion conflict against the Comp_and_Liquids DBM).

Exclusions:

- Construction installation, on-site tie-ins, and field turnover activities are excluded (covered by `DEL-032-03_construction-work-package` and the EPC Integrator's facility integration scope).
- The vendor document register, submittals, and turnover records are excluded from this deliverable and are covered by `DEL-032-05_vendor-document-turnover-package` (if present).
- EPC vendor package review and acceptance evidence is excluded and is covered by `DEL-032-06_epc-vendor-package-review-and-acceptance` (if present).
- Package-specific cathodic protection method (impressed-current vs. sacrificial anode), anode type and bed configuration, transformer-rectifier ratings, junction-box and test-station design, protected-asset enumeration, and installation locations remain `TBD` where accessible source set does not provide confirmed package-specific values; the vendor shall resolve these in vendor data during package engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-032-04-001 | The vendor package shall be developed from the accepted EPC Scope of Work (`DEL-032-01`) and Package Datasheet (`DEL-032-02`); the vendor shall not invent scope outside those inputs. Source: `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-032-01`, `DEL-032-02`, `DEL-032-04`. | Cross-reference vendor design basis/datasheet against the accepted EPC inputs. |
| REQ-032-04-002 | The vendor package shall preserve the accepted responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-032`. | Responsibility statement review against Gate 7 package register. |
| REQ-032-04-003 | The vendor package shall be engineered to the four applicable package interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, and Communications / Network. Source: `INTERFACE_REGISTER.csv` rows for `PKG-032`. | Vendor interface design review against `INTERFACE_REGISTER.csv` rows for `PKG-032`. |
| REQ-032-04-004 | The vendor package design basis shall be consistent with the 4-25 DBM treatment of cathodic protection: cathodic protection engineering and supply is excluded from the facility electrical design scope and is owner-coordinated; the vendor shall engineer the package to interface with the facility without expanding facility-design scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cathodic Protection section. | Vendor design basis check against the 4-25 DBM Cathodic Protection section. |
| REQ-032-04-005 | The vendor package shall coordinate grounding/bonding with the EPC facility grounding scheme such that cathodic protection does not compromise facility grounding and bonding requirements. Source: `INTERFACE_REGISTER.csv` `IFC-F1FE9DF9DD`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding-and-bonding context. | Vendor grounding/cathodic interaction review against the Grounding / Bonding interface. |
| REQ-032-04-006 | The vendor package shall provide I&C / Control Cabling and Communications / Network interfaces consistent with monitoring, rectifier control, alarm, and remote-monitoring functions where applicable. Source: `INTERFACE_REGISTER.csv` `IFC-4D092EC70F`, `IFC-8594557BD3`. | Vendor I&C and communications interface design review against `INTERFACE_REGISTER.csv`. |
| REQ-032-04-007 | The vendor package shall produce, as artifacts, the vendor engineered physical equipment package and the vendor package design basis and datasheet set. Source: `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-032-04`. | Artifact register check against vendor delivery. |
| REQ-032-04-008 | Source gaps for cathodic protection method, anode/bed design, rectifier ratings, junction/test-station design, protected-asset coverage, quantities, and physical location shall be resolved by vendor data during package engineering; values shall not be invented in advance of vendor design. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package-specific PKG-032 slice not retrieved in this run. | Vendor data review at EPC vendor package acceptance. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical installation basis referenced by DBM electrical sections; applicable to electrical portions of the cathodic protection package (rectifier feeders, enclosures, grounding interaction). | Applicable as source-supported design basis; clause locations TBD. |
| NACE / AMPP cathodic protection standards (e.g., NACE SP0169, SP0286 family) | Conventional standards for cathodic protection design, installation, and testing. | ASSUMPTION: likely applicable to a cathodic protection package; not cited in accessible source slices. Vendor to confirm; location TBD. |
| Project electrical specifications | Voltage/grounding/cable/raceway basis referenced by DBM electrical sections. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical components installed in classified areas (e.g., rectifier cabinets, junction boxes). | Applicable; package-specific classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| EPC Scope of Work (`DEL-032-01`) and EPC Package Datasheet (`DEL-032-02`) | Accepted EPC inputs to vendor package engineering. | Authoritative upstream EPC inputs; status governed by sibling deliverables. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Vendor inputs traceability | Compare vendor design basis to `DEL-032-01` Scope of Work and `DEL-032-02` Package Datasheet. | Vendor scope and parameters trace back to accepted EPC inputs without invented additions. |
| Identity completeness | Compare vendor package identity fields to workbook row 34 and Gate 7 registers. | Package name, IDs, discipline, WBS, and CoA tracking number match. |
| Interface completeness | Compare vendor design interface treatment to `INTERFACE_REGISTER.csv` rows for `PKG-032`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, and Communications / Network are addressed. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as vendor commitments. |
| Responsibility split | Compare vendor scope language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated; integration items remain EPC. |
| Facility-design boundary | Confirm vendor package does not pull cathodic protection engineering/supply into facility electrical design scope counter to 4-25 DBM. | Boundary preserved; owner-coordinated interface posture maintained. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Integration handoff readiness | Confirm vendor package outputs are available to downstream turnover and EPC acceptance workflows. | Outputs identified and listed for EPC review. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor engineered physical equipment package.
- Vendor package design basis.
- Vendor package datasheet set.
- Source-gap / `TBD` list to be closed by vendor data during package engineering.

The deliverable shall cite the Gate 7 snapshot, workbook row 34, applicable Gate 7 registers, the DBM cathodic-protection source slices, and the EPC Scope of Work and Package Datasheet as vendor engineering inputs.
