# Specification — DEL-053-05 Vendor Document Turnover Package (Flare KO Drum, Cryo)

> Normative specification for the contents, control, submittal, review, and turnover of the vendor documentation set for PKG-053. Vendor document numbers, revisions, and submittal dates remain TBD pending vendor award.

## Scope

### In scope
- The vendor document register for PKG-053 (Flare KO Drum, Cryo).
- All vendor document submittals listed in the Vendor Engineering Deliverables table of `26020-Package_Requirements.docx` (package heading 8), carried as artifacts under this deliverable per the Gate 7 ARTIFACT_REGISTER for `DEL-053-05_vendor-document-turnover-package`.
- Source-required vendor documents organized by category (see Datasheet.md Construction section).
- Turnover records demonstrating that submittals were issued, reviewed, and accepted.
- EPC Integrator interface and integration review of vendor documents (review scope; acceptance is recorded under DEL-053-06).

### Out of scope
- Vendor design and fabrication of the physical equipment package (covered by DEL-053-04).
- EPC-authored Scope of Work, Package Datasheet, and Construction Work Package (DEL-053-01, -02, -03).
- EPC Vendor Package Review and Acceptance log (DEL-053-06).
- Promoting any individual vendor-document row to a standalone deliverable. Per PROJECT_DECOMP DEC-004, vendor-document rows are artifacts under this deliverable, not separate deliverables.

## Requirements

### R-1 — Vendor Document Register (REQUIRED)
The Package Vendor SHALL produce and maintain a Vendor Document Register that lists every document required by the source Vendor Engineering Deliverables table (`26020-Package_Requirements.docx` heading 8). The register SHALL include, per row at minimum:
- Source Doc Ref (e.g., MEC-003, QLT-021, INS-008)
- Vendor Document Number (vendor-assigned)
- Document Title
- Category (per Datasheet.md categories 1-9 and remaining ARTIFACT_REGISTER categories)
- Revision
- Planned Submittal Date
- Actual Submittal Date
- EPC Review Status (e.g., Reviewed-No-Comment / Reviewed-With-Comment / Rejected)
- Turnover Status (e.g., Issued for Construction / Final Turnover / Vendor Data Book Included)

Source: ARTIFACT_REGISTER.csv ART-C0B3DA97E7 (Vendor document register); _CONTEXT.md anticipated artifacts. (location TBD for clause-level requirements within 26020-Package_Requirements.docx)

### R-2 — Document Control Procedure (REQUIRED)
The Package Vendor SHALL maintain a Vendor Document Control Procedure (Source Doc Ref DOC-008; ART-E1545FE7B1) covering revision control, transmittal, hold/issue points, comment incorporation, and final-revision freeze for turnover.

### R-3 — Category Coverage (REQUIRED)
The vendor document set SHALL include all categories represented in the Gate 7 ARTIFACT_REGISTER for DEL-053-05. Categories present (non-exhaustive enumeration; see Datasheet.md):
- Core vendor documents (incl. PRQ-009 Document Index, QLT-006 Supplier Quality Plan, QLT-003 ITP, QLT-013 MTRs, QLT-020 Inspection Release Certificate, QLT-021 MRB, PRQ-013 Logistics, PRQ-015 SPIR, PRQ-016 Final Vendor Data Book).
- Core package engineering (MEC-001 through MEC-025 set as enumerated).
- Static pressure equipment (MEC-005, MEC-009, REG-022).
- Relief/flare/vent design (PRO-014, PRO-015, PRO-016, PRO-017, PRO-018).
- Process piping interfaces (PRO-008 P&IDs, PIP-003..PIP-028 as enumerated).
- Drainage/containment interfaces (PRO-023, CIV-014).
- Electrical, grounding, lighting, heat tracing (as enumerated).
- Instrumentation and controls interfaces (INS-002..INS-029, CTL-003, CTL-005, CTL-006, CTL-026).
- Structural, foundations, access (as enumerated).
- Remaining ARTIFACT_REGISTER rows (97 total) — including additional categories — SHALL be covered.

Source: ARTIFACT_REGISTER.csv (Gate 7) DEL-053-05 row set.

### R-4 — Pressure Equipment Registration Package (REQUIRED if jurisdiction applies)
A Pressure Equipment Registration Package (REG-022; ART-97212D01B9) SHALL be prepared for the pressure-retaining components of the package. ASSUMPTION: jurisdictional registration (e.g., provincial CRN in Canada) is required; final applicability is location TBD pending project location confirmation in source.

### R-5 — Cryogenic Service Documentation (REQUIRED)
Documents covering MDMT, impact testing, material qualification for service below -45.5 degC, and PSV sizing for cryogenic relief SHALL be included. Source basis: DEL-053-04 Datasheet (sibling deliverable) and DBM-Deepcut cryogenic flare row (cited via DEL-053-04). PSV/PRO-015 sizing and PRO-018 blowdown studies SHALL reflect cryogenic relief conditions.

### R-6 — Inspection and Test Plan (REQUIRED)
QLT-003 ITP (ART-459B3C4CAD) SHALL define hold/witness/review/observation points for fabrication, NDE, hydrotest (PIP-024), FAT (MEC-021/022), and final inspection (QLT-020). EPC Integrator SHALL be granted the witness/review opportunities specified in the ITP.

### R-7 — Manufacturing Record Book / Vendor Data Book (REQUIRED)
QLT-021 Manufacturing Record Book and PRQ-016 Final Vendor Data Book SHALL consolidate as-built documents, material test reports (QLT-013), inspection release (QLT-020), FAT reports (MEC-022), calibration certificates, weld maps, NDE reports, and certificates of conformance prior to package release/turnover.

### R-8 — Interface Specification Documents (REQUIRED)
The Package Vendor Interface Specification (CTL-026; ART-18AF0225FB) SHALL define the signal lists, communication protocols, terminations, and physical interface points for I&C integration with the EPC facility DCS/SIS. Companion interface documents (CTL-003 narrative, CTL-005 C&E, CTL-006 DCS I/O list) SHALL be aligned with the interface facts carried as evidence under DEL-053-02 (Package Datasheet).

### R-9 — Submittal Workflow (REQUIRED)
Each document SHALL transition through: Issued for Review -> EPC Review -> Vendor Comment Incorporation -> Issued for Construction (where applicable) -> As-Built/Final Turnover. The Document Control Procedure (DOC-008) SHALL define transmittal codes, retention periods, and final-issue formatting. Detailed transmittal sequence: TBD (vendor scope; location TBD).

### R-10 — Turnover Records (REQUIRED)
Turnover records SHALL evidence that all required documents were issued at final revision, accepted by EPC Integrator review, and bound into PRQ-016 (Vendor Data Book / Final Supplier Documentation) before package handoff for construction and downstream commissioning.

### R-11 — Granularity (NORMATIVE; no sub-deliverables)
No individual vendor-document row from the source Vendor Engineering Deliverables table SHALL be promoted to a separate deliverable. All such rows are carried as artifacts/evidence under this deliverable. Source: PROJECT_DECOMP DEC-004; DELIVERABLE_REGISTER.csv DEL-053-05 Notes.

## Standards

| Reference | Applicability | Source / Location |
|---|---|---|
| 26020-Package_Requirements.docx — package heading 8 — Vendor Engineering Deliverables table | Governs the required vendor document categories and rows. | _Sources/26020-Package_Requirements.docx (location TBD for clause-level text; cited via ARTIFACT_REGISTER) |
| ASME BPVC Section VIII Div. 1 | ASSUMPTION: governs pressure-vessel design/registration evidence within REG-022, MEC-009, MEC-014. | ASSUMPTION (industry convention; not in accessible sources) |
| Jurisdictional pressure equipment regulation (e.g., CRN) | ASSUMPTION: applicable per R-4; location TBD pending site/jurisdiction confirmation. | ASSUMPTION |
| Project DBM (DBM-Comp_and_Liquids, DBM-Deepcut) | Provides cryogenic service basis, header sizes, MOC for adjacent piping; informs cryogenic vendor documents. | _Sources/DBM-Deepcut/* (cited via DEL-053-04) |

## Verification

| Requirement | Verification Method | Evidence Artifact |
|---|---|---|
| R-1 Vendor Document Register completeness | EPC review checks register against ARTIFACT_REGISTER.csv row set for DEL-053-05; no missing rows. | Vendor Document Register (ART-C0B3DA97E7); Vendor Document Index (ART-BE9ACF9A83, PRQ-009) |
| R-2 Document Control Procedure | EPC review of DOC-008 against project document-control expectations. | ART-E1545FE7B1 |
| R-3 Category coverage | Cross-walk register categories vs. ARTIFACT_REGISTER categories for DEL-053-05. | Cross-walk worksheet (TBD); register |
| R-4 Pressure Equipment Registration | Receipt and acceptance of REG-022 package; jurisdictional certificate when issued. | ART-97212D01B9 (REG-022) |
| R-5 Cryogenic-service documentation | Review of MDMT, impact test results, PSV sizing inputs/outputs against DBM cryogenic conditions. | MEC-009; PRO-015; PRO-018; QLT-013 (MTRs with impact test) |
| R-6 ITP | EPC review and signature of QLT-003; witness/hold-point execution. | ART-459B3C4CAD; signed ITP returns |
| R-7 MRB / Vendor Data Book | EPC acceptance of final QLT-021 / PRQ-016. | ART-7A77419C70; ART-1E2BA080C7 |
| R-8 Interface documents | I&C interface walkdown against CTL-026 and DCS/SIS I/O list; alignment with DEL-053-02 interface facts. | ART-18AF0225FB; CTL-006 DCS I/O List (ART-C37EC1316B) |
| R-9 Submittal workflow | Transmittal log inspection; revision history per document; final-issue flag verified. | Register Revision/Submittal columns |
| R-10 Turnover records | Confirm PRQ-016 binder is issued and accepted; turnover checklist signoff. | PRQ-016; DEL-053-06 acceptance evidence |
| R-11 Granularity | Audit that no vendor-document row appears as a separate deliverable in PKG-053. | DELIVERABLE_REGISTER.csv PKG-053 rows (only DEL-053-01..06) |

## Documentation

The following documents SHALL exist as outputs of this deliverable (each is an artifact in ARTIFACT_REGISTER.csv for DEL-053-05):
- Vendor document register (ART-C0B3DA97E7)
- Vendor Document Index (PRQ-009; ART-BE9ACF9A83)
- Vendor Document Control Procedure (DOC-008; ART-E1545FE7B1)
- Supplier Quality Plan (QLT-006; ART-9AAC1CDA13)
- Inspection and Test Plan (QLT-003; ART-459B3C4CAD)
- Material Test Reports (QLT-013; ART-14E72B3562)
- Inspection Release Certificate (QLT-020; ART-D4A7B50D18)
- Manufacturing Record Book (QLT-021; ART-7A77419C70)
- Logistics / Shipping Plan (PRQ-013; ART-748CB943F9)
- SPIR (PRQ-015; ART-FF2FE62703)
- Final Vendor Data Book (PRQ-016; ART-1E2BA080C7)
- All other artifacts in the DEL-053-05 row set of ARTIFACT_REGISTER.csv (mechanical, static pressure, relief/flare, piping, drainage, electrical, I&C, structural, and remaining categories) — see Datasheet.md for the enumeration.

Turnover deliverable bundle: the consolidated PRQ-016 Vendor Data Book is the single binding output that demonstrates all required documents reached final issue, were reviewed, and were accepted.
