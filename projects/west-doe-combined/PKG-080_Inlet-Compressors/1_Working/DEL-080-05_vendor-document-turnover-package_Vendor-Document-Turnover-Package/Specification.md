# Specification — DEL-080-05 Vendor Document Turnover Package

## Scope

### In scope
- Assembly and delivery of the **Vendor Document Turnover Package** for `PKG-080 Inlet Compressors` (`26020-02-PT-12-001`).
- Vendor document register identifying every vendor-issued document for the package, with revision status and transmittal control.
- Vendor document submittals at the contractually required revision states.
- Source-required vendor documentation as enumerated in `26020-Package_Requirements.docx` heading 33 → Vendor Engineering Deliverables (Table 133) — see `Datasheet.md` for the complete enumerated list.
- Turnover records: inspection release, manufacturing record book / vendor data book, final supplier documentation, logistics/shipping, SPIR, FAT/SAT and energization evidence.
- EPC Integrator review interface (review log, comments, dispositions). The acceptance decision itself is recorded under `DEL-080-06_epc-vendor-package-review-and-acceptance`.

### Out of scope
- Production of the physical equipment package itself (covered by `DEL-080-04_vendor-engineered-equipment-package`).
- EPC Integrator acceptance evidence and acceptance ruling (covered by `DEL-080-06`).
- Project-level (non-package) document control (covered at the EPC scope-of-work level — see `DEL-080-01`).
- Construction installation work product (covered by `DEL-080-03`).

## Requirements

Each requirement labeled `[SRC]` is derived from `26020-Package_Requirements.docx` heading 33; `[ASSUMPTION]` items are inferred and require human confirmation; `[TBD]` items have no source authority yet.

### REQ-01 — Document set completeness `[SRC]`
The turnover package SHALL include every deliverable enumerated in the source vendor deliverables table for PKG-080 (`26020-Package_Requirements.docx` heading 33, Table 133). The complete enumerated set is reproduced in `Datasheet.md`.

### REQ-02 — Vendor Document Index `[SRC]`
The package SHALL include `PRQ-009 Vendor Document Index` listing every vendor document with: vendor doc number, title, revision, transmittal status, EPC review status. Source: heading 33 vendor deliverables.

### REQ-03 — Vendor Document Control Procedure `[SRC]`
The package SHALL include `DOC-008 Vendor Document Control Procedure` defining numbering, revision control, transmittal mechanics, and acceptance flow.

### REQ-04 — Quality evidence `[SRC]`
The package SHALL include `QLT-003 Inspection and Test Plan`, `QLT-006 Supplier Quality Plan`, `QLT-013 Material Test Reports / Certificates`, `QLT-020 Inspection Release Certificate`, `QLT-021 Manufacturing Record Book / Vendor Data Book`.

### REQ-05 — Final documentation set `[SRC]`
The package SHALL include `PRQ-016 Vendor Data Book / Final Supplier Documentation` and `MEC-023 Vendor Data Book / Mechanical Final Documentation` as the consolidated turnover record.

### REQ-06 — Logistics and spares `[SRC]`
The package SHALL include `PRQ-013 Logistics / Shipping Plan` and `PRQ-015 Spare Parts Interchangeability Record (SPIR)`.

### REQ-07 — Discipline submittals `[SRC]`
The package SHALL include the mechanical, rotating-equipment, relief, piping, utility, drainage, electrical, instrumentation/controls, building/HVAC, fire-and-gas, and structural document IDs enumerated in `Datasheet.md`.

### REQ-08 — FAT and energization evidence `[SRC]`
The package SHALL include `MEC-021 Equipment FAT / Performance Test Procedure`, `MEC-022 Equipment FAT / Performance Test Report`, `ELE-029 Electrical FAT / SAT Procedure`, `ELE-030 Electrical Test Records / Energization Package`.

### REQ-09 — As-built drawings `[SRC]`
The package SHALL include `PIP-028 Piping As-Built Drawings` and `INS-029 Instrument As-Built Drawings`.

### REQ-10 — Pressure-equipment registration `[SRC]`
The package SHALL include `REG-022 Pressure Equipment Registration Package` and `REG-021 Fire Code / Building Code Compliance Package`.

### REQ-11 — Compressor-specific design basis `[SRC]`
Because the equipment is a sour reciprocating compressor package (Ariel KBZ/6 per source heading 33 → Major Included Equipment, Table 131 Scope Notes), the turnover SHALL include `MEC-004 Rotating Equipment Specifications`, `MEC-008 Compressor Data Sheets`, `MEC-019 Mechanical Seal / Lube Oil Specification`, `ELE-011 Motor Starting Study`.

### REQ-12 — NACE compliance evidence `[SRC]`
Material certification (`QLT-013`) SHALL evidence NACE-compliant materials and seals as called out in heading 33 → Scope Notes / Open Items (Table 131).

### REQ-13 — Submittal revision stages `[ASSUMPTION]`
Submittals SHOULD follow Bid → IFR → IFA → IFC → As-Built stages. ASSUMPTION (industry-typical); the binding stage labels are defined by the issued `DOC-008` and the EPC Integrator. `[TBD]` until DOC-008 is issued.

### REQ-14 — Review turnaround `[TBD]`
EPC Integrator review turnaround times for each submittal class. `[TBD]` — not stated in heading 33; depends on the project document-control matrix.

### REQ-15 — Transmittal medium `[TBD]`
Transmittal medium (vendor portal, controlled file transfer, or other). `[TBD]` — not stated in heading 33.

### REQ-16 — Document numbering `[ASSUMPTION]`
Vendor-native numbering as listed in PRQ-009 Vendor Document Index; cross-mapping to source vendor-deliverable IDs (e.g., MEC-008, INS-002) maintained in the index. ASSUMPTION on dual numbering — confirm against issued DOC-008.

### REQ-17 — Turnover acceptance interface `[SRC, derived from decomposition]`
The Vendor Document Turnover Package SHALL be issued in a form that supports EPC Integrator review under `DEL-080-06`. Source: `DELIVERABLE_REGISTER.csv` row for DEL-080-06 (review log + acceptance checklist consumes vendor documents and turnover evidence).

## Standards

The following standards are referenced by source heading 33 only as embedded callouts (NACE materials/seals). Other standards are not enumerated at clause level in the source slice and remain `location TBD`.

| Standard | Applicability | Source / status |
|---|---|---|
| NACE materials / seals standard (e.g., NACE MR0175 / ISO 15156 — ASSUMPTION on exact reference) | Materials and seals selection for sour service | Heading 33 → Scope Notes / Open Items (Table 131) calls out "NACE-compliant materials and seals". Exact NACE document `location TBD`. |
| Provincial pressure-equipment regulation (basis for REG-022) | Pressure equipment registration | `location TBD` — heading 33 lists `REG-022` but does not cite a jurisdiction. |
| Fire / building code (basis for REG-021) | Building / fire code compliance | `location TBD` — heading 33 lists `REG-021` but does not name the code. |
| Project / EPC document control standard | Submittal stages, numbering, transmittal | `location TBD` — anticipated to be specified in DOC-008 once issued. |

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
| REQ-10 | Regulatory submission acknowledgement | REG-021, REG-022 transmittals |
| REQ-11 | Inclusion check | MEC-004, MEC-008, MEC-019, ELE-011 transmittals |
| REQ-12 | Material cert review for NACE compliance statement | QLT-013 entries flagged for NACE |
| REQ-13 | Cross-check submittal stage label against DOC-008 (when issued) | Submittal log |
| REQ-14, REQ-15, REQ-16 | TBD until governing document is issued | n/a |
| REQ-17 | Turnover transmittal accepted into DEL-080-06 review workflow | DEL-080-06 review log |

## Documentation

### Documents the turnover package produces
- `PRQ-009 Vendor Document Index` (master register)
- All vendor documents enumerated in `Datasheet.md` at the contractually required revision
- `PRQ-016 / MEC-023` final consolidated vendor data books
- Transmittal cover sheets / transmittal log
- EPC review log (interface with DEL-080-06)

### Documents the turnover package consumes (upstream context)
- EPC Scope of Work (`DEL-080-01`) — defines vendor scope
- EPC Package Datasheet (`DEL-080-02`) — defines technical handoff content the vendor documents must address
- Vendor Engineered Equipment Package (`DEL-080-04`) — origin of the documents being turned over

### Downstream consumer
- `DEL-080-06_epc-vendor-package-review-and-acceptance` — EPC review and acceptance evidence consumes this turnover package.
