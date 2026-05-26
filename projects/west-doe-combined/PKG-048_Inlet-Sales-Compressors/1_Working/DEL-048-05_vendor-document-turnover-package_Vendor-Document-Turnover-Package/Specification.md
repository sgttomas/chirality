# Specification — DEL-048-05 Vendor Document Turnover Package

## Scope

### In scope
- Assembly and delivery of the **Vendor Document Turnover Package** for `PKG-048 Inlet / Sales Compressors`.
- Vendor document register (PRQ-009) identifying every vendor-issued document for the package, with revision status and transmittal control, and disambiguating inlet-duty vs sales-duty unit documents where applicable.
- Vendor document submittals at the contractually required revision states.
- Source-required vendor documentation as enumerated in `26020-Package_Requirements.docx` heading 3 vendor engineering deliverables table (`location TBD` — see `Datasheet.md` for the expected enumerated framework).
- Turnover records: inspection release, manufacturing record book / vendor data book, final supplier documentation, logistics/shipping, SPIR, FAT/SAT and energization evidence.
- EPC Integrator review interface (review log, comments, dispositions). The acceptance decision itself is recorded under `DEL-048-06_epc-vendor-package-review-and-acceptance`.

### Out of scope
- Production of the physical equipment package itself (covered by `DEL-048-04_vendor-engineered-equipment-package`).
- EPC Integrator acceptance evidence and acceptance ruling (covered by `DEL-048-06`).
- Project-level (non-package) document control (covered at the EPC scope-of-work level — see `DEL-048-01`).
- Construction installation work product (covered by `DEL-048-03`).

## Requirements

Each requirement labeled `[SRC]` is derived from the `26020-Package_Requirements.docx` heading 3 framework (analogous to the sibling heading-33 table for PKG-080); `[ASSUMPTION]` items are inferred and require human confirmation; `[TBD]` items have no source authority yet. All `[SRC]` items remain pending direct re-verification against the heading 3 slice when extracted.

### REQ-01 — Document set completeness `[SRC, location TBD]`
The turnover package SHALL include every deliverable enumerated in the source vendor deliverables table for PKG-048 (`26020-Package_Requirements.docx` heading 3). The expected enumerated framework is reproduced in `Datasheet.md` and must be reconciled against the heading 3 source slice once extracted.

### REQ-02 — Vendor Document Index `[SRC, location TBD]`
The package SHALL include `PRQ-009 Vendor Document Index` listing every vendor document with: vendor doc number, title, revision, transmittal status, EPC review status, and a unit/duty attribute distinguishing inlet-compression vs sales-compression units.

### REQ-03 — Vendor Document Control Procedure `[SRC, location TBD]`
The package SHALL include `DOC-008 Vendor Document Control Procedure` defining numbering, revision control, transmittal mechanics, and acceptance flow.

### REQ-04 — Quality evidence `[SRC, location TBD]`
The package SHALL include `QLT-003 Inspection and Test Plan`, `QLT-006 Supplier Quality Plan`, `QLT-013 Material Test Reports / Certificates`, `QLT-020 Inspection Release Certificate`, `QLT-021 Manufacturing Record Book / Vendor Data Book`.

### REQ-05 — Final documentation set `[SRC, location TBD]`
The package SHALL include `PRQ-016 Vendor Data Book / Final Supplier Documentation` and `MEC-023 Vendor Data Book / Mechanical Final Documentation` as the consolidated turnover record.

### REQ-06 — Logistics and spares `[SRC, location TBD]`
The package SHALL include `PRQ-013 Logistics / Shipping Plan` and `PRQ-015 Spare Parts Interchangeability Record (SPIR)`.

### REQ-07 — Discipline submittals `[SRC, location TBD]`
The package SHALL include the mechanical, rotating-equipment, relief, piping, utility, drainage, electrical, instrumentation/controls, building/HVAC, fire-and-gas, and structural document IDs enumerated in `Datasheet.md`.

### REQ-08 — FAT and energization evidence `[SRC, location TBD]`
The package SHALL include `MEC-021 Equipment FAT / Performance Test Procedure`, `MEC-022 Equipment FAT / Performance Test Report`, `ELE-029 Electrical FAT / SAT Procedure`, `ELE-030 Electrical Test Records / Energization Package`.

### REQ-09 — As-built drawings `[SRC, location TBD]`
The package SHALL include `PIP-028 Piping As-Built Drawings` and `INS-029 Instrument As-Built Drawings`.

### REQ-10 — Regulatory packages `[SRC, location TBD]`
The package SHALL include `REG-022 Pressure Equipment Registration Package` and `REG-021 Fire Code / Building Code Compliance Package`. Jurisdiction and code reference are `TBD` — see Guidance Conflict Table.

### REQ-11 — Compressor-specific design basis `[ASSUMPTION]`
Because the equipment is a sour-service combined inlet/sales compressor package, the turnover SHOULD include `MEC-004 Rotating Equipment Specifications`, `MEC-008 Compressor Data Sheets`, `MEC-019 Mechanical Seal / Lube Oil Specification`, `ELE-011 Motor Starting Study`. ASSUMPTION pending heading 3 confirmation. Compressor-stage specifics (reciprocating vs centrifugal, drivers) `TBD`.

### REQ-12 — NACE compliance evidence `[ASSUMPTION]`
Material certification (`QLT-013`) SHOULD evidence NACE-compliant materials and seals for sour-service items. ASSUMPTION based on plant-basis sour-service designation in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-04; heading 3 NACE callout `location TBD`.

### REQ-13 — Submittal revision stages `[ASSUMPTION]`
Submittals SHOULD follow Bid -> IFR -> IFA -> IFC -> As-Built stages. ASSUMPTION (industry-typical); binding stage labels are defined by the issued `DOC-008` and the EPC Integrator. `[TBD]` until DOC-008 is issued.

### REQ-14 — Review turnaround `[TBD]`
EPC Integrator review turnaround times for each submittal class. `[TBD]` — not stated in source slice; depends on the project document-control matrix.

### REQ-15 — Transmittal medium `[TBD]`
Transmittal medium (vendor portal, controlled file transfer, or other). `[TBD]` — not stated in source slice.

### REQ-16 — Document numbering `[ASSUMPTION]`
Vendor-native numbering as listed in PRQ-009; cross-mapping to source vendor-deliverable IDs (e.g., MEC-008, INS-002) maintained in the index. ASSUMPTION on dual numbering — confirm against issued DOC-008.

### REQ-17 — Turnover acceptance interface `[SRC, derived from decomposition]`
The Vendor Document Turnover Package SHALL be issued in a form that supports EPC Integrator review under `DEL-048-06`. Source: `DELIVERABLE_REGISTER.csv` and `_CONTEXT.md` package decomposition (Gate-07 snapshot).

### REQ-18 — Unit-duty disambiguation `[ASSUMPTION]`
For unit-specific documents (compressor data sheets, FAT reports, motor starting studies, etc.), PRQ-009 SHOULD distinguish inlet-duty units from sales-duty units to ensure each unit's vendor data is identifiable and traceable. ASSUMPTION based on the combined `Inlet / Sales Compressors` package scope; heading 3 unit count and duty split `TBD`.

## Standards

| Standard | Applicability | Source / status |
|---|---|---|
| NACE materials / seals standard (e.g., NACE MR0175 / ISO 15156 — ASSUMPTION on exact reference) | Materials and seals selection for sour service | Plant sour-service basis per DBM-Comp_and_Liquids; heading 3 NACE callout `location TBD`. |
| Provincial pressure-equipment regulation (basis for REG-022) | Pressure equipment registration | `location TBD` — heading 3 likely lists REG-022 without naming jurisdiction. |
| Fire / building code (basis for REG-021) | Building / fire code compliance | `location TBD` — heading 3 likely lists REG-021 without naming code. |
| Project / EPC document control standard | Submittal stages, numbering, transmittal | `location TBD` — anticipated to be specified in DOC-008 once issued. |

## Verification

| Requirement | Verification approach | Evidence artifact |
|---|---|---|
| REQ-01 | Cross-check completed Vendor Document Index against source vendor deliverables table (heading 3) once extracted | PRQ-009 reconciled to `Datasheet.md` enumerated list and to heading 3 |
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
| REQ-17 | Turnover transmittal accepted into DEL-048-06 review workflow | DEL-048-06 review log |
| REQ-18 | Inspect PRQ-009 unit/duty column completeness | PRQ-009 export |

## Documentation

### Documents the turnover package produces
- `PRQ-009 Vendor Document Index` (master register)
- All vendor documents enumerated in `Datasheet.md` at the contractually required revision
- `PRQ-016 / MEC-023` final consolidated vendor data books
- Transmittal cover sheets / transmittal log
- EPC review log (interface with DEL-048-06)

### Documents the turnover package consumes (upstream context)
- EPC Scope of Work (`DEL-048-01`) — defines vendor scope
- EPC Package Datasheet (`DEL-048-02`) — defines technical handoff content the vendor documents must address
- Construction Work Package (`DEL-048-03`) — interfaces installation/commissioning content
- Vendor Engineered Equipment Package (`DEL-048-04`) — origin of the documents being turned over

### Downstream consumer
- `DEL-048-06_epc-vendor-package-review-and-acceptance` — EPC review and acceptance evidence consumes this turnover package.
