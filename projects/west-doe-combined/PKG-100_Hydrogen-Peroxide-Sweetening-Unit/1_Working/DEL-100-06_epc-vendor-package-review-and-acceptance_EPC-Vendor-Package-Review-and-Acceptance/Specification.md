# Specification — DEL-100-06 EPC Vendor Package Review and Acceptance

## Scope

### In Scope

EPC Integrator's review of the Package Vendor's Hydrogen Peroxide Sweetening Unit deliverable set, integration acceptance against the EPC Scope of Work, the Package Datasheet, and the Construction Work Package, and handoff readiness evidence for facility integration. (`_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` DEL-100-06)

Specifically covers:

- Review of vendor engineering, package design, vendor documentation, and physical equipment supply for `PKG-100`. (`PACKAGE_REGISTER.csv` PKG-100 responsibility model)
- Verification that the vendor package meets the SOW items `SOW-0107`, `SOW-0108`, `SOW-0109`, `SOW-0110`. (`_CONTEXT.md` Covers Scope Items)
- Acceptance of vendor compliance against the package interface set (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports). (`INTERFACE_REGISTER.csv` PKG-100 rows)
- Production of the four anticipated artifacts: vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence. (`_CONTEXT.md` Anticipated Artifacts)

### Out of Scope

- Vendor-owned package engineering, package design, vendor documentation, and physical equipment supply themselves (owned by Package Vendor per `PACKAGE_REGISTER.csv` PKG-100). The EPC Integrator reviews and accepts these; it does not produce them.
- EPC-scope tie-in execution itemized in `SOW-0110` "By others" (interconnecting piping; DCS integration; foundations; electrical supply to MCC) — these are facility-integration scope tracked elsewhere in PKG-100/EPC-led deliverables. (`SCOPE_LEDGER.csv` SOW-0110)
- Binding approval or certification by any non-human party. (K-AUTH-1, project governance)

## Requirements

| ID | Requirement | Source / Rationale |
|---|---|---|
| REQ-100-06-01 | The acceptance evidence set SHALL include, at minimum, a vendor document review log, a package acceptance checklist, test/inspection evidence, and turnover evidence. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` DEL-100-06 |
| REQ-100-06-02 | The acceptance checklist SHALL verify vendor conformance against `DEL-100-01` (Scope of Work), `DEL-100-02` (Package Datasheet), and `DEL-100-03` (Construction Work Package) line items. | `_CONTEXT.md` Scope ("against the EPC Scope of Work, Package Datasheet, and Construction Work Package") |
| REQ-100-06-03 | Review SHALL confirm that `DEL-100-04` (Vendor Engineered Equipment Package) covers the equipment list in `SOW-0109`: 400 BBL Hydrogen Peroxide Storage Tank; Hydrogen Peroxide Pumps (chemical injection); Static Mixer; Hydrogen Peroxide Reactors; additional PFD equipment; self-framing site building. | `SCOPE_LEDGER.csv` SOW-0109 |
| REQ-100-06-04 | Review SHALL confirm that `DEL-100-05` (Vendor Document Turnover Package) is complete against the vendor document tables referenced by the package requirements document. | `DELIVERABLE_REGISTER.csv` DEL-100-05; `OBJECTIVE_REGISTER.csv` OBJ-010 (vendor-document tables in 26020-Package_Requirements.docx) |
| REQ-100-06-05 | Acceptance SHALL verify capacity and operating-conditions consistency against `SOW-0110`: 24,154 BBL/D treatment capacity; 400 BBL H2O2 storage; sour water at 9 °C, 340.54 kPag, 160 m3/h. | `SCOPE_LEDGER.csv` SOW-0110 |
| REQ-100-06-06 | Acceptance SHALL verify electrical driver basis per `SOW-0110`: pumps on 575 V / 3 PH / 60 Hz motors; DOL or VFD start; local H-O-A or On-Off control; fed from 600 V MCC. | `SCOPE_LEDGER.csv` SOW-0110 |
| REQ-100-06-07 | Acceptance SHALL verify environmental design per `SOW-0110`: ambient −40 °C min / +35 °C max; design conditions TBC (open item to be closed by vendor). | `SCOPE_LEDGER.csv` SOW-0110 |
| REQ-100-06-08 | Acceptance SHALL verify that each applicable interface in `INTERFACE_REGISTER.csv` for `PKG-100` (13 interface types listed) is addressed in vendor deliverables and that EPC-side tie-ins identified as "By others" in `SOW-0110` are routed to the correct EPC deliverable. | `INTERFACE_REGISTER.csv` PKG-100; `SCOPE_LEDGER.csv` SOW-0110 |
| REQ-100-06-09 | Acceptance evidence SHALL capture handoff/turnover readiness criteria consistent with `OBJ-010`: sparing, isolation, winterization, maintenance access, commissioning, turnover, and controlled open-item closure. | `OBJECTIVE_REGISTER.csv` OBJ-010 |
| REQ-100-06-10 | Acceptance disposition (accept / accept-with-conditions / reject) SHALL be issued by a human approver; no agent or automated tool may certify acceptance. | K-AUTH-1 (project governance) |
| REQ-100-06-11 | Open items identified during acceptance (including the explicit TBCs in `SOW-0110` for design conditions and pump capacity) SHALL be tracked to closure with assigned owner and target date. | `SCOPE_LEDGER.csv` SOW-0110; ASSUMPTION on closure-tracking format |
| REQ-100-06-12 | All acceptance records SHALL carry provenance to the source artifact reviewed (vendor document ID / section, or deliverable ID + section). | K-PROV-1 (project governance) |

ASSUMPTION: Specific acceptance thresholds (e.g., percent-complete gate, hold-point criteria) are not stated in accessible references and are TBD pending EPC integrator procedures.

## Standards

| Standard / Specification | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx`, package heading 52 | Governs the Hydrogen Peroxide Sweetening Unit package basic scope, major equipment, scope notes and open items | `_Sources/26020-Package_Requirements.docx` (source slice not copied into deliverable; location TBD at clause level) |
| Workbook Packages row 63 | Governs PKG-100 identity, discipline, interface set, and responsibility model | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 63 (location TBD at cell level) |
| Vendor-document tables referenced by `OBJ-010` | Governs required vendor document deliverables underpinning `DEL-100-05` and therefore reviewed here | `_Sources/26020-Package_Requirements.docx` vendor-document tables (location TBD) |
| Sour-service / safety / fire & gas / regulatory codes per `OBJ-009` | Governs safety- and code-related interfaces that acceptance must confirm | DBM references in `OBJECTIVE_REGISTER.csv` OBJ-009 (location TBD; not opened locally) |
| Electrical-infrastructure codes per `OBJ-005` (for 575 V motor, 600 V MCC interface) | Governs electrical interface acceptance | DBM references in `OBJECTIVE_REGISTER.csv` OBJ-005 (location TBD) |

ASSUMPTION: Specific industry standards (ASME, API, CSA, etc.) likely applicable to a sour-service H2O2 treatment package but not enumerated in the accessible decomposition snapshot — clause-level requirements not derived.

## Verification

| Requirement | Verification Method | Verification Artifact |
|---|---|---|
| REQ-100-06-01 | Inspection of acceptance evidence set against the four anticipated-artifact types | Folder contents of `DEL-100-06` |
| REQ-100-06-02 | Document review (line-by-line cross-check against `DEL-100-01`, `DEL-100-02`, `DEL-100-03`) | Package acceptance checklist |
| REQ-100-06-03 | Document review against equipment list in `SOW-0109` | Package acceptance checklist (Equipment List section) |
| REQ-100-06-04 | Document register check against vendor-document tables | Vendor document review log |
| REQ-100-06-05 | Engineering check of capacity/operating-condition values across vendor documents | Test/inspection evidence; package acceptance checklist |
| REQ-100-06-06 | Electrical interface review against `IFC-62EE7F54FE` (Electrical Power) and vendor electrical schematics | Package acceptance checklist (Electrical section) |
| REQ-100-06-07 | Design conditions cross-check; explicit open item if TBC unresolved | Open-items log |
| REQ-100-06-08 | Interface walkdown across the 13 PKG-100 interface types | Package acceptance checklist (Interfaces section); test/inspection evidence |
| REQ-100-06-09 | Operability/maintainability review per OBJ-010 checklist items | Turnover evidence; package acceptance checklist |
| REQ-100-06-10 | Human sign-off recorded in acceptance disposition record | Acceptance disposition record |
| REQ-100-06-11 | Open-items log review | Open-items log |
| REQ-100-06-12 | Provenance audit of acceptance records | Spot-check of acceptance checklist entries |

## Documentation

Required artifacts produced by this deliverable (from `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence
- Turnover evidence

Additional records (ASSUMPTION, derived from the requirement set above):

- Open-items log (REQ-100-06-11)
- Acceptance disposition record (REQ-100-06-10)
