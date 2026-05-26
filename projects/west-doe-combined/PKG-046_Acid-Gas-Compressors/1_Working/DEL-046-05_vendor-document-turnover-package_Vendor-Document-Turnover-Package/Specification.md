# Specification: DEL-046-05 — Vendor Document Turnover Package (PKG-046 Acid Gas Compressors)

## Scope

This specification establishes the normative requirements the Package Vendor must satisfy when assembling and transmitting the Vendor Document Turnover Package for the PKG-046 Acid Gas Compressors. It covers the controlled set of engineering, quality, operations, and certification documents that constitute formal handover from the Package Vendor to the EPC Integrator and ultimately to the Owner/Operator.

In scope:
- The Vendor Document Register (VDR) and all referenced submittal artifacts associated with the two acid gas injection compressor packages and the spare compressor (PACKAGE_REGISTER PKG-046; DBM-Deepcut lines 878, 885).
- Source vendor document table rows that serve as artifacts/evidence (`_CONTEXT.md` Notes).
- Turnover transmittals, mechanical completion sign-offs, and acceptance records.

Out of scope:
- Engineering of the equipment itself (covered by DEL-046-04 Vendor Engineered Equipment Package).
- Construction work package (DEL-046-03).
- EPC Integrator's review/acceptance disposition (DEL-046-06).

## Requirements

### REQ-046-05-R-01 — Vendor Document Register (VDR) shall be the master index

The Package Vendor shall maintain a single controlled VDR identifying every required submittal by document number, title, revision, intended status (e.g., IFA / IFR / IFC / AB — exact set **TBD**, confirm against `26020-Package_Requirements.docx` package heading 1), transmittal date, and reviewer disposition.

- Source: `_CONTEXT.md` (Anticipated Artifacts: "Vendor document register"); DBM-Comp_and_Liquids line 617 (mechanical package deliverables shall include "vendor document registers"); location TBD inside `26020-Package_Requirements.docx`.

### REQ-046-05-R-02 — All required vendor submittals shall be transmitted via the VDR

Every document identified in REQ-046-05-R-01 shall be transmitted on the schedule and revision sequence defined by the Package Requirements. The required document list, mandatory revision codes, and submittal milestones are **TBD** pending access to the `26020-Package_Requirements.docx` package heading 1 source slice.

- Source: `_CONTEXT.md` (Anticipated Artifacts: "vendor document submittals"); 26020-Package_Requirements.docx (location TBD).

### REQ-046-05-R-03 — Engineering submittals shall cover the design basis disciplines

At minimum, engineering submittals shall include: process datasheets, general arrangement (GA) drawings, P&IDs, electrical one-lines/schematics, instrument index, cause-and-effect matrices, and pulsation/vibration analysis reports for the reciprocating compressors. The full list and per-item acceptance criteria are **TBD** pending source access.

- Source: DBM-Comp_and_Liquids line 617 ("datasheets, cause-and-effect inputs, utility load summaries, ... vendor document registers"); DBM-Deepcut (reciprocating compressor design basis, lines 990-1033).

### REQ-046-05-R-04 — Quality and inspection records shall be included

Material certifications, NDE records, hydrotest records, ITP sign-offs, and code-stamp data reports (e.g., ASME U-1A where applicable) shall be assembled into the turnover package. Specific code stamp and certification requirements are **TBD** pending source access.

- Source: ASSUMPTION grounded in standard mechanical package practice and PACKAGE_REGISTER PKG-046 (Mechanical discipline, MAWP basis at DBM-Deepcut line 1006); specific items TBD per 26020-Package_Requirements.docx.

### REQ-046-05-R-05 — Operations and maintenance documentation shall be included

IOM manuals, lubrication/seal references, spare parts lists (commissioning, two-year, capital), and special-tool lists shall be provided as part of turnover.

- Source: ASSUMPTION grounded in standard vendor turnover practice; specific composition TBD per 26020-Package_Requirements.docx.

### REQ-046-05-R-06 — Source vendor document table rows preserved as artifacts

Where the Package Requirements source provides a table of required vendor documents, those rows shall be preserved as evidence/artifacts (not as separate deliverables) per `_CONTEXT.md` Notes.

- Source: `_CONTEXT.md` Notes ("individual source document rows remain artifacts/evidence, not separate deliverables").

### REQ-046-05-R-07 — Turnover records shall evidence transmittal completion

A formal turnover record set shall include transmittal letters, punch list (open/closed), mechanical completion certificate, and EPC Integrator acceptance sign-off (acceptance disposition itself is recorded under DEL-046-06).

- Source: `_CONTEXT.md` Anticipated Artifacts: "turnover records".

### REQ-046-05-R-08 — EPC Integrator interface/integration review

The EPC Integrator shall perform interface/integration review on submitted vendor documents. Review-cycle expectations (turnaround days, comment-resolution mechanism, conditional acceptance rules) are **TBD** pending source access.

- Source: `_CONTEXT.md` ResponsibleParty (EPC Integrator interface/integration review); ASSUMPTION on cycle parameters.

## Standards

Governing standards referenced by the Package Requirements document and the Acid Gas Compressor design basis are **TBD** at clause level pending text-accessible source slices. Anticipated families include (all **location TBD**):

- ASME B&PV Section VIII Division 1 / 2 — pressure vessels and cylinders (MAWP basis per DBM-Deepcut line 1006).
- API 618 — Reciprocating Compressors for Petroleum, Chemical, and Gas Industry Services (ASSUMPTION: typical governing standard for separable reciprocating compressors of this class).
- API 619 / API 11P — as applicable.
- NACE MR0175 / ISO 15156 — sour service materials (H2S service per PACKAGE_REGISTER PKG-046).
- Electrical area classification per Canadian Electrical Code Section 18 / IEC 60079 series (ASSUMPTION: Canadian project; jurisdiction TBD).

Each standard shall be confirmed against `26020-Package_Requirements.docx` package heading 1 and the Word Source Basis `Bid Docs/Budgetary/26020-01-PT-RFQ-12-001_Acid Gas Compressor.docx` (cited in PACKAGE_REGISTER PKG-046 Source Reference; not locally text-accessible).

## Verification

| Requirement | Verification Method | Evidence Recorded In |
|---|---|---|
| REQ-046-05-R-01 | Document review — VDR completeness against Package Requirements VDR template | VDR transmittal record |
| REQ-046-05-R-02 | Transmittal log audit — all VDR rows reach the required final status | VDR closeout report |
| REQ-046-05-R-03 | Discipline document review by EPC Integrator | DEL-046-06 acceptance record |
| REQ-046-05-R-04 | QA/QC record audit; code stamp presence verification | Mechanical completion certificate |
| REQ-046-05-R-05 | O&M completeness review against IOM checklist | Turnover acceptance log |
| REQ-046-05-R-06 | Cross-reference vendor document table rows to VDR | Artifact register entry |
| REQ-046-05-R-07 | Turnover transmittal review; punch list closure status | Mechanical completion certificate |
| REQ-046-05-R-08 | EPC Integrator review cycle audit | DEL-046-06 acceptance record |

Specific acceptance thresholds (e.g., percentage punch closure required for mechanical completion) are **TBD** pending source access.

## Documentation

Documentation produced by this deliverable:

- Vendor Document Register (VDR) — controlled master.
- Vendor document submittals — full set per VDR.
- Source vendor document table rows — preserved as artifacts/evidence.
- Turnover records — transmittals, punch lists, mechanical completion certificate, sign-offs.

Source: `_CONTEXT.md` Anticipated Artifacts.
