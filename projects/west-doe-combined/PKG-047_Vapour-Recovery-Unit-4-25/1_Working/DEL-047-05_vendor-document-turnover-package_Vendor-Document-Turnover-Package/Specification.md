# Specification: Vendor Document Turnover Package (DEL-047-05)

## Scope

### In scope
- The complete vendor document register for `PKG-047 — Vapour Recovery Unit 4-25` (equipment tag `26020-01-PT-12-002`), including: index, controlled submittals, vendor deliverable artifacts (data sheets, drawings, calculations, procedures, certificates), and the consolidated turnover records (manufacturing record book / vendor data book / final supplier documentation).
- The submittal lifecycle: transmittal, EPC Integrator review/comment cycles, vendor revision, status closure, and final acceptance.
- The mapping of each vendor-document row in the source-listed "Vendor Engineering Deliverables" table (see `Datasheet.md` Construction section) to its produced artifact, current revision, and status.
- Pressure Equipment Registration Package (REG-022) submission for the in-scope pressure equipment in the VRU package.
- Final turnover (issue of PRQ-016 and QLT-021) to the Owner / EPC Integrator at mechanical completion.

### Out of scope (this deliverable)
- Authoring the engineering content of the listed vendor documents (those are the Package Vendor's engineering deliverables; this deliverable receives, controls, and turns them over).
- Substituting for the underlying disciplinary review (process, mechanical, electrical, I&C, structural, technical safety) — those are addressed by the disciplinary deliverables of `PKG-047`.
- Site-installation document turnover that is owned by the EPC Integrator (e.g., site as-built consolidation beyond what the Package Vendor produces).

## Requirements

Source-grounded requirements are marked **R-#**. Each cites its source slice.

- **R-1 Vendor Document Index (PRQ-009).** The Package Vendor SHALL produce and maintain a Vendor Document Index that lists every document in the turnover package by Document ID, name, revision, status, transmittal number, and date. (Source: 26020-Package_Requirements.docx, "26020-01-PT-12-002 - Vapour Recovery Unit", Vendor Engineering Deliverables → Core vendor documents → PRQ-009.)
- **R-2 Vendor Document Control Procedure (DOC-008).** Document control SHALL operate under a vendor-issued Vendor Document Control Procedure governing numbering, revision, transmittal, review-status codes, hold/superseded handling, and retention. (Source: same; row DOC-008.)
- **R-3 Supplier Quality Plan (QLT-006) and ITP (QLT-003).** The vendor document set SHALL include the Supplier Quality Plan and the Inspection and Test Plan, with the ITP traceable to the package equipment scope. (Source: same; QLT-006, QLT-003.)
- **R-4 Inspection / Material Records.** Material Test Reports / Certificates (QLT-013) and Inspection Release Certificates (QLT-020) SHALL be collected before release-to-ship and incorporated into the Manufacturing Record Book / Vendor Data Book (QLT-021). (Source: same.)
- **R-5 Final Vendor Data Book / Final Supplier Documentation (PRQ-016).** A consolidated PRQ-016 SHALL be produced as the final turnover artifact, and SHALL include or index every accepted vendor document listed in the Vendor Engineering Deliverables table. (Source: same.)
- **R-6 Logistics and SPIR.** Logistics / Shipping Plan (PRQ-013) and Spare Parts Interchangeability Record (PRQ-015) SHALL be included as numbered rows in the register. (Source: same.)
- **R-7 Equipment FAT records.** Equipment FAT / Performance Test Procedure (MEC-021) and Equipment FAT / Performance Test Report (MEC-022) SHALL be transmitted and held as accepted-revision artifacts in the register before final turnover. (Source: same; Core package engineering.)
- **R-8 Mechanical final documentation.** Vendor Data Book / Mechanical Final Documentation (MEC-023) and Mechanical Equipment IOM Manual (MEC-025) SHALL be issued. (Source: same.)
- **R-9 Pressure equipment registration.** A Pressure Equipment Registration Package (REG-022) SHALL be assembled to support pressure equipment registration for the VRU pressure boundary equipment. (Source: same; Rotating equipment / compressors.) Jurisdiction-specific submission requirements are **location TBD**.
- **R-10 Discipline-specific vendor deliverables.** The register SHALL track all rows enumerated in the source's Vendor Engineering Deliverables table (Datasheet Construction), including process/relief, piping, utilities, drainage, electrical/EHT/grounding, I&C, fire and gas / technical safety, and structural/foundation deliverables. (Source: same; corresponding subsection rows.)
- **R-11 Source vendor document rows as artifacts.** Where individual source-document rows are available, those rows SHALL be carried as artifacts/evidence in the turnover package rather than promoted to separate deliverables. (Source: `_CONTEXT.md` Notes; consistent with source's row-level listing.)
- **R-12 EPC Integrator review.** Every document submitted under this register SHALL be subject to EPC Integrator interface/integration review per the agreed review-status code set. (Source: `_CONTEXT.md` ResponsibleParty; review-status code set itself: **TBD** in available source slice.)
- **R-13 SOW coverage.** The register SHALL evidence coverage of `SOW-0253`, `SOW-0254`, `SOW-0255`, `SOW-0256`. (Source: `_CONTEXT.md` Covers Scope Items. The exact textual content of each SOW row is **location TBD** in the slice consulted.)
- **R-14 Linkage to vendor data book.** Final turnover SHALL not be declared complete until QLT-021 (Manufacturing Record Book / Vendor Data Book) and PRQ-016 (Vendor Data Book / Final Supplier Documentation) are accepted by EPC Integrator review. (Source: 26020-Package_Requirements.docx Vendor Engineering Deliverables.) ASSUMPTION: "accepted by EPC Integrator review" is the gating criterion; the explicit acceptance signature workflow is **TBD** in available source.

## Standards

- Pressure equipment registration jurisdiction and the applicable boiler-and-pressure-vessel code regime for REG-022 are **TBD** (location TBD in available source). ASSUMPTION: ABSA/CRN regime is likely for a Canadian facility, but this is not stated in the available source slice and MUST be confirmed.
- NACE designation applies to the package's pressure-containing/wetted components per the source ("NACE designation applies"). The specific NACE document version is **location TBD**.
- API-style designations are not enumerated in the source slice for this package (the analogous Acid Gas Compressor section cites API-661 for air cooler; for the VRU, the source slice does not list governing API standards). Treat any cross-package code carryover as **ASSUMPTION** and require human confirmation before adoption.
- Document-control standard for the vendor data book structure (e.g., IOGP/ISO 15489 information governance) is **TBD** — the source slice prescribes only the controlling document is DOC-008.

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 | Inspection of issued PRQ-009 against the source's Vendor Engineering Deliverables list (Datasheet Construction); every row present with rev + status. |
| R-2 | Document review of DOC-008; check that all transmittals reference DOC-008 numbering and revision conventions. |
| R-3, R-4 | Audit of QLT-006, QLT-003, QLT-013, QLT-020 against ITP hold-points; certificate completeness check. |
| R-5, R-8, R-14 | Final review of PRQ-016, MEC-023, MEC-025, QLT-021; sign-off in EPC Integrator review log (workflow TBD). |
| R-6 | Spot check of PRQ-013 and PRQ-015 contents. |
| R-7 | Witness or review of MEC-021 procedure; review of MEC-022 results against acceptance criteria in MEC-021. |
| R-9 | Inspection of REG-022 contents; confirm jurisdiction submission receipts (jurisdiction TBD). |
| R-10 | Cross-table audit: every row in the source's Vendor Engineering Deliverables list maps to a register row with status. |
| R-11 | Register row metadata identifies source vendor document rows as evidence artifacts, not promoted deliverables. |
| R-12 | EPC Integrator review log present and current for every transmittal. |
| R-13 | SOW coverage matrix attached to the register (SOW-0253..0256 → register rows). |

## Documentation (artifacts produced under this deliverable)

- The vendor document register itself (the controlling index — instantiated as PRQ-009 plus any local register view used by EPC Integrator).
- All transmitted vendor submittals (rows enumerated in `Datasheet.md` Construction).
- Turnover records: QLT-021 Manufacturing Record Book / Vendor Data Book, PRQ-016 Vendor Data Book / Final Supplier Documentation, MEC-023 Vendor Data Book / Mechanical Final Documentation, ELE-030 Electrical Test Records / Energization Package, PIP-028 Piping As-Built Drawings, INS-029 Instrument As-Built Drawings.
- The EPC Integrator review log (review-status outcomes for each transmittal). Workflow detail **TBD**.
- The SOW coverage matrix (SOW-0253..0256 ↔ register rows).
