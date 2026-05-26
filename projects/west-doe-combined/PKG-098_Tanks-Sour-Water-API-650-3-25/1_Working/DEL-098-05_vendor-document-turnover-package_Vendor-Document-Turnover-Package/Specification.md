# Specification — DEL-098-05 Vendor Document Turnover Package

## Scope

This specification governs the Vendor Document Turnover Package for PKG-098 Tanks, Sour Water (API 650) 3-25. It defines the set of vendor-authored documents that the Package Vendor must produce, control, submit, and turn over to the EPC Integrator for the seven sour-water / produced-water storage tanks listed in SOW-0223, together with the register, submittal, and turnover-record evidence required to demonstrate completeness.

In scope:
- Vendor document register (Vendor Document Index) and supporting control procedure.
- Vendor document submittals organized by category, as enumerated in `Datasheet.md` (Core vendor documents; Core package engineering; Storage tanks; Relief / flare / vent design; Process piping interfaces; Drainage / containment interfaces; Electrical / grounding; Cathodic protection; Instrumentation and controls; Structural / access; Civil grading / spill containment).
- Turnover records (Manufacturing Record Book / Vendor Data Book; Vendor Data Book / Final Supplier Documentation; FAT Reports; Material Test Reports; Inspection Release Certificate; SPIR).
- EPC Integrator interface and integration review of vendor documentation.

Out of scope (by others; not vendor scope):
- Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc. (SCOPE_LEDGER SOW-0224). The vendor produces interface-side documents (e.g., Anchor Bolt / Embedment Drawings, Foundation Design Calculations) where listed in ARTIFACT_REGISTER; physical execution of "by others" items is outside this deliverable.
- Decomposition truth maintenance; this deliverable consumes the Gate 7 Final Published PROJECT_DECOMP snapshot, it does not modify it.

## Requirements

| ID | Requirement | Source | Verification (see "Verification") |
|---|---|---|---|
| REQ-01 | The Package Vendor shall maintain a Vendor Document Index (PRQ-009) covering every document required by `26020-Package_Requirements.docx` heading 50, Vendor Engineering Deliverables table. | ARTIFACT_REGISTER DEL-098-05 (PRQ-009) | V-01 |
| REQ-02 | A Vendor Document Control Procedure (DOC-008) shall govern numbering, revision, transmittal, and status of all vendor-issued documents. | ARTIFACT_REGISTER DEL-098-05 (DOC-008) | V-02 |
| REQ-03 | A Supplier Quality Plan (QLT-006) and Inspection and Test Plan (QLT-003) shall be issued before fabrication and maintained through turnover. | ARTIFACT_REGISTER DEL-098-05 (QLT-006, QLT-003) | V-03 |
| REQ-04 | Material Test Reports / Certificates (QLT-013) shall be compiled for each tank and pressure-retaining component and included in the Manufacturing Record Book / Vendor Data Book (QLT-021). | ARTIFACT_REGISTER DEL-098-05 (QLT-013, QLT-021) | V-04 |
| REQ-05 | An Inspection Release Certificate (QLT-020) shall accompany shipment of each tank. | ARTIFACT_REGISTER DEL-098-05 (QLT-020) | V-05 |
| REQ-06 | Logistics / Shipping Plan (PRQ-013) and SPIR (PRQ-015) shall be submitted prior to shipment. | ARTIFACT_REGISTER DEL-098-05 (PRQ-013, PRQ-015) | V-06 |
| REQ-07 | A final Vendor Data Book / Final Supplier Documentation (PRQ-016) shall be issued as the turnover record. | ARTIFACT_REGISTER DEL-098-05 (PRQ-016) | V-07 |
| REQ-08 | Mechanical Design Basis (MEC-001), Mechanical Equipment List (MEC-002), and Mechanical Equipment Data Sheets (MEC-003) shall be submitted for review. | ARTIFACT_REGISTER DEL-098-05 (MEC-001, MEC-002, MEC-003) | V-08 |
| REQ-09 | Tanks shall be designed and fabricated to modified API 650. The vendor documentation shall include Storage Tank Data Sheets and Static Equipment Specifications that record the modifications. | SCOPE_LEDGER SOW-0223; ARTIFACT_REGISTER DEL-098-05 (Storage tanks category) | V-09 |
| REQ-10 | Internal coating documentation shall reflect Devchem 253 applied to floor, walls, and roof. | SCOPE_LEDGER SOW-0223 | V-10 |
| REQ-11 | External insulation with electric heating shall be reflected in the vendor's mechanical and electrical interface documents. | SCOPE_LEDGER SOW-0223 | V-11 |
| REQ-12 | A Kennilworth type HCL float skim system, one per tank, shall be reflected in equipment data sheets and IOM. | SCOPE_LEDGER SOW-0223 | V-12 |
| REQ-13 | Design conditions in vendor documentation shall be: 32 oz test pressure; design temperature -40 deg C (min) and 60 deg C (max); operating pressure atmospheric; operating temperature 10 deg C (Item No. 2 operating temperature TBD per source). | SCOPE_LEDGER SOW-0224 | V-13 |
| REQ-14 | Vendor interface documents shall be produced for each interface type identified for PKG-098: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | INTERFACE_REGISTER PKG-098; PACKAGE_REGISTER PKG-098 | V-14 |
| REQ-15 | All vendor-issued documents shall carry traceable identifiers and revision status compatible with the EPC Integrator's document control system. ASSUMPTION: specific EPC numbering convention not extracted in source slice. | Inferred from REQ-01, REQ-02 | V-15 |
| REQ-16 | The Package Vendor shall submit documents in the form/state required for EPC Integrator interface and integration review (REQ-14 deliverables form the review surface). | `_CONTEXT.md` Responsible Party; PACKAGE_REGISTER PKG-098 (responsibility text) | V-14, V-15 |

## Standards

| Standard / Reference | Applicability | Local Source / Location |
|---|---|---|
| API 650 (modified) | Tank design and fabrication | Cited in SOW-0223; clause-level text not locally accessible — location TBD |
| 26020-Package_Requirements.docx, package heading 50, Vendor Engineering Deliverables table | Vendor document set definition | `_Sources/26020-Package_Requirements.docx` (binary; quoted slices via ARTIFACT_REGISTER and SCOPE_LEDGER) |
| Project specifications (insulation, painting, piping line class, electrical, instrumentation) | Vendor compliance basis | 3-25_Comp_and_Liquids_DBM.md (final standards register to be verified against latest project specification index) — location TBD for individual specs |
| ASSUMPTION: CSA / Canadian regulatory regime (site in BC) | Likely applicable for pressure equipment registration | Inferred from site location (3-25_Comp_and_Liquids_DBM.md); ASSUMPTION |

## Verification

| ID | Verification activity | Evidence artifact |
|---|---|---|
| V-01 | Index completeness check against the Vendor Engineering Deliverables table at submittal of each issue. | Vendor Document Index (PRQ-009) |
| V-02 | Procedure review and adherence audit on a sample of transmittals. | Vendor Document Control Procedure (DOC-008); transmittal log |
| V-03 | Pre-fabrication review of QLT-006 and QLT-003; ITP sign-off log. | Supplier Quality Plan; ITP |
| V-04 | MTR compilation cross-check against bill of material; inclusion in MRB. | QLT-013; QLT-021 |
| V-05 | Inspection release issued per tank; shipment hold-point. | QLT-020 |
| V-06 | Pre-shipment review of logistics plan and SPIR. | PRQ-013; PRQ-015 |
| V-07 | Turnover review of Vendor Data Book / Final Supplier Documentation. | PRQ-016 |
| V-08 | EPC Integrator review of MEC-001, MEC-002, MEC-003 against datasheet (DEL-098-02) and SOW (DEL-098-01). | MEC-001; MEC-002; MEC-003 |
| V-09 | API 650 compliance evidenced in Storage Tank Data Sheets and Static Equipment Specifications; vendor's modified-API-650 deviations register. TBD: deviation list not in source slice. | Storage Tank Data Sheets; Static Equipment Specifications |
| V-10 | Coating system documentation review (Devchem 253 application records). | Coating procedure / records (TBD specific artifact) |
| V-11 | External insulation / electric heating drawings and load summary reviewed in vendor / interface submittal. | Vendor mechanical and electrical interface drawings |
| V-12 | Equipment data sheets and IOM include Kennilworth HCL float skim system. | Mechanical Equipment Data Sheets; Mechanical Equipment IOM Manual |
| V-13 | Design conditions checked across Storage Tank Data Sheets, Mechanical Calculation Package, and Relief Valve Data Sheets. | Storage Tank Data Sheets; Mechanical Calculation Package |
| V-14 | EPC Integrator interface walk-down per interface type with checklist against ARTIFACT_REGISTER interface categories. | Vendor interface documents per category |
| V-15 | Document control audit confirms traceable IDs and revision status. | Transmittal log; Document Index |

## Documentation

Required artifacts (mapped from `_CONTEXT.md` "Anticipated Artifacts" and ARTIFACT_REGISTER):

- Vendor document register.
- Vendor document submittals (by category, per `Datasheet.md` Construction section).
- Source vendor document table rows as artifacts where available.
- Turnover records (MRB / Vendor Data Book; Final Supplier Documentation; Inspection Release Certificate; FAT reports; Material Test Reports; SPIR; Logistics / Shipping Plan).

Storage location: `1_Working/DEL-098-05_vendor-document-turnover-package_Vendor-Document-Turnover-Package` while drafting; promoted to `2_Checking` and `3_Issued` per package lifecycle.
