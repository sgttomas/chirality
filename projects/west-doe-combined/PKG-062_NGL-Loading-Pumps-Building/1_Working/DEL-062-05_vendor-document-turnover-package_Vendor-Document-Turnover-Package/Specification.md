# Specification — DEL-062-05 Vendor Document Turnover Package

## Scope

### In scope
- Assembly and delivery of the **Vendor Document Turnover Package** for `PKG-062 NGL Loading Pumps Building` (source equipment package `26020-01-PT-18-003 — LPG Loading Pumps`; see Conflict Table C-01).
- Vendor document register identifying every vendor-issued document for the package, with revision status and transmittal control.
- Vendor document submittals at the contractually required revision states.
- Source-required vendor documentation as enumerated in `26020-Package_Requirements.docx` heading 16 → Vendor Engineering Deliverables — see `Datasheet.md` for the complete enumerated list.
- Turnover records: inspection release, manufacturing record book / vendor data book, final supplier documentation, logistics/shipping, SPIR, FAT/SAT and energization evidence.
- EPC Integrator review interface (review log, comments, dispositions). The acceptance decision itself is recorded under `DEL-062-06_epc-vendor-package-review-and-acceptance`.

### Out of scope
- Production of the physical equipment package itself (covered by `DEL-062-04_vendor-engineered-equipment-package`).
- EPC Integrator acceptance evidence and acceptance ruling (covered by `DEL-062-06`).
- Project-level (non-package) document control (covered at the EPC scope-of-work level — see `DEL-062-01`).
- Construction installation work product (covered by `DEL-062-03`).

## Requirements

Each requirement labeled `[SRC]` is derived from `26020-Package_Requirements.docx` heading 16; `[ASSUMPTION]` items are inferred and require human confirmation; `[TBD]` items have no source authority yet.

### REQ-01 — Document set completeness `[SRC]`
The turnover package SHALL include every deliverable enumerated in the source vendor deliverables table for PKG-062 (`26020-Package_Requirements.docx` heading 16). The complete enumerated set is reproduced in `Datasheet.md`.

### REQ-02 — Vendor Document Index `[SRC]`
The package SHALL include `PRQ-009 Vendor Document Index` listing every vendor document with: vendor doc number, title, revision, transmittal status, EPC review status. Source: heading 16 vendor deliverables.

### REQ-03 — Vendor Document Control Procedure `[SRC]`
The package SHALL include `DOC-008 Vendor Document Control Procedure` defining numbering, revision control, transmittal mechanics, and acceptance flow.

### REQ-04 — Quality evidence `[SRC]`
The package SHALL include `QLT-003 Inspection and Test Plan`, `QLT-006 Supplier Quality Plan`, `QLT-013 Material Test Reports / Certificates`, `QLT-020 Inspection Release Certificate`, `QLT-021 Manufacturing Record Book / Vendor Data Book`.

### REQ-05 — Final documentation set `[SRC]`
The package SHALL include `PRQ-016 Vendor Data Book / Final Supplier Documentation` and `MEC-023 Vendor Data Book / Mechanical Final Documentation` as the consolidated turnover record.

### REQ-06 — Logistics and spares `[SRC]`
The package SHALL include `PRQ-013 Logistics / Shipping Plan` and `PRQ-015 Spare Parts Interchangeability Record (SPIR)`.

### REQ-07 — Discipline submittals `[SRC]`
The package SHALL include the mechanical, rotating-equipment/pump, loading/metering, relief, piping, utility, drainage, electrical, instrumentation/controls, building/HVAC, fire-and-gas, and structural document IDs enumerated in `Datasheet.md`.

### REQ-08 — FAT and energization evidence `[SRC]`
The package SHALL include `MEC-021 Equipment FAT / Performance Test Procedure`, `MEC-022 Equipment FAT / Performance Test Report`, `ELE-029 Electrical FAT / SAT Procedure`, `ELE-030 Electrical Test Records / Energization Package`.

### REQ-09 — As-built drawings `[SRC]`
The package SHALL include `PIP-028 Piping As-Built Drawings` and `INS-029 Instrument As-Built Drawings`.

### REQ-10 — Fire / building code package `[SRC]`
The package SHALL include `REG-021 Fire Code / Building Code Compliance Package`. (Heading 16's vendor deliverables enumerate REG-021 but not REG-022; pressure-equipment registration is NOT listed for this rotary-pump package — see Guidance C-06.)

### REQ-11 — Pump-specific design basis `[SRC]`
Because the equipment is a four-unit Blackmer LGL4B rotary vane pump package (heading 16 → Basic Scope, Major Included Equipment), the turnover SHALL include `MEC-004 Rotating Equipment Specifications`, `MEC-007 Pump Data Sheets`, `MEC-019 Mechanical Seal / Lube Oil Specification`, `PRO-013 Pump Hydraulic / NPSH Calculations`, `ELE-011 Motor Starting Study`.

### REQ-12 — Motor sizing evidence `[SRC]`
The Motor Starting Study (`ELE-011`) and Pump Hydraulic / NPSH Calculations (`PRO-013`) SHALL evidence motor sizing for the cited basis of "inlet stabilizer composition density at -40 °C start-up condition" (heading 16 → Scope Notes / Open Items).

### REQ-13 — Loading / metering package documentation `[SRC]`
The package SHALL include `INS-015 Metering Package Specification`, `PRO-025 Operating Guidelines / Startup-Shutdown Narrative`, `PIP-004 Tie-In List / Tie-In Scope Sheets`, and `PIP-018 Valve Data Sheets` for the truck-loading interface (heading 16 → Basic Scope: pumps move LPG product from storage to LPG Truck Loading).

### REQ-14 — Capacity / TDH confirmation `[SRC, TBC in source]`
Pump Data Sheets (`MEC-007`) SHALL confirm per-pump capacity of 68 m³/hr @ 345 kPad (300 USGPM @ 50 psid). Source explicitly marks TDH as TBC (heading 16 → Major Included Equipment / Scope Notes / Open Items); the turnover SHALL evidence the final confirmed TDH.

### REQ-15 — Submittal revision stages `[ASSUMPTION]`
Submittals SHOULD follow Bid → IFR → IFA → IFC → As-Built stages. ASSUMPTION (industry-typical); the binding stage labels are defined by the issued `DOC-008` and the EPC Integrator. `[TBD]` until DOC-008 is issued.

### REQ-16 — Review turnaround `[TBD]`
EPC Integrator review turnaround times for each submittal class. `[TBD]` — not stated in heading 16; depends on the project document-control matrix.

### REQ-17 — Transmittal medium `[TBD]`
Transmittal medium (vendor portal, controlled file transfer, or other). `[TBD]` — not stated in heading 16.

### REQ-18 — Document numbering `[ASSUMPTION]`
Vendor-native numbering as listed in PRQ-009 Vendor Document Index; cross-mapping to source vendor-deliverable IDs (e.g., MEC-007, INS-015) maintained in the index. ASSUMPTION on dual numbering — confirm against issued DOC-008.

### REQ-19 — Turnover acceptance interface `[SRC, derived from decomposition]`
The Vendor Document Turnover Package SHALL be issued in a form that supports EPC Integrator review under `DEL-062-06`. Source: `DELIVERABLE_REGISTER.csv` row for DEL-062-06 (review and acceptance consumes vendor documents and turnover evidence).

### REQ-20 — Operating Guidelines coverage `[SRC]`
`PRO-025 Operating Guidelines / Startup-Shutdown Narrative` SHALL cover startup at the design cold-start condition (-40 °C) per the motor sizing basis in heading 16 → Scope Notes / Open Items, and SHALL cover normal LPG truck-loading service.

## Standards

The source heading 16 slice does not enumerate any standard at clause level; standards remain `location TBD` until project-level standards documents (e.g., the Mechanical Design Basis MEC-001 once issued) are accessible.

| Standard | Applicability | Source / status |
|---|---|---|
| Fire / building code (basis for REG-021) | Building / fire code compliance | `location TBD` — heading 16 lists `REG-021` but does not name the code. Likely provincial fire / building code per project location (4-25 West Doe Deepcut). |
| Project / EPC document control standard | Submittal stages, numbering, transmittal | `location TBD` — anticipated to be specified in DOC-008 once issued. |
| Electrical area classification (NFPA / CEC, ASSUMPTION) | LPG/NGL service area classification basis for electrical equipment | `location TBD` — not stated in heading 16; required to ground electrical-equipment data sheets. |
| Pump / piping code (ASME/API, ASSUMPTION) | Hydrotest and pump testing | `location TBD` — not stated in heading 16. |

## Verification

| Requirement | Verification approach | Evidence artifact |
|---|---|---|
| REQ-01 | Cross-check completed Vendor Document Index against source vendor deliverables table | PRQ-009 reconciled to `Datasheet.md` enumerated list |
| REQ-02 | Index review by EPC Integrator | PRQ-009 issued copy + EPC review record |
| REQ-03 | Review of DOC-008 | DOC-008 issued copy + EPC review record |
| REQ-04, REQ-05 | Inclusion check in transmittal | QLT-003, QLT-006, QLT-013, QLT-020, QLT-021, PRQ-016, MEC-023 transmittals |
| REQ-06 | Inclusion check | PRQ-013, PRQ-015 transmittals |
| REQ-07 | Inclusion check against `Datasheet.md` discipline tables | Discipline submittal log |
| REQ-08 | FAT execution and witness records | MEC-021, MEC-022, ELE-029, ELE-030 transmittals |
| REQ-09 | As-built reconciliation against IFC | PIP-028, INS-029 transmittals |
| REQ-10 | Regulatory submission acknowledgement | REG-021 transmittal |
| REQ-11, REQ-13 | Inclusion check | MEC-004, MEC-007, MEC-019, PRO-013, ELE-011, INS-015, PRO-025, PIP-004, PIP-018 transmittals |
| REQ-12 | Cold-start case evidenced in motor starting study and NPSH calc | ELE-011, PRO-013 review |
| REQ-14 | Pump performance curve and TDH confirmation reviewed by EPC Integrator | MEC-007 with finalized TDH; FAT report MEC-022 |
| REQ-15, REQ-16, REQ-17, REQ-18 | TBD until governing document is issued | n/a |
| REQ-19 | Turnover transmittal accepted into DEL-062-06 review workflow | DEL-062-06 review log |
| REQ-20 | Operating narrative reviewed by EPC operations interface | PRO-025 acceptance record |

## Documentation

### Documents the turnover package produces
- `PRQ-009 Vendor Document Index` (master register)
- All vendor documents enumerated in `Datasheet.md` at the contractually required revision
- `PRQ-016 / MEC-023` final consolidated vendor data books
- Transmittal cover sheets / transmittal log
- EPC review log (interface with DEL-062-06)

### Documents the turnover package consumes (upstream context)
- EPC Scope of Work (`DEL-062-01`) — defines vendor scope
- EPC Package Datasheet (`DEL-062-02`) — defines technical handoff content the vendor documents must address
- Vendor Engineered Equipment Package (`DEL-062-04`) — origin of the documents being turned over

### Downstream consumer
- `DEL-062-06_epc-vendor-package-review-and-acceptance` — EPC review and acceptance evidence consumes this turnover package.
