# Specification: DEL-096-05 — Vendor Document Turnover Package

## Scope

This specification governs the **Vendor Document Turnover Package** for `PKG-096 Tanks, Sour Condensate (API 650)`. It defines the required content, structure, submittal/review lifecycle, and turnover artifacts for vendor-produced documentation associated with the package.

**In scope**
- Vendor document register for PKG-096.
- Vendor document submittals against that register.
- Source-required vendor documentation called out by `26020-Package_Requirements.docx` package heading 48 (location TBD; clause-level content not locally accessible).
- Turnover records (transmittals, acceptance evidence, final accepted document set).

**Out of scope**
- Engineered equipment design content itself (covered by `DEL-096-04 Vendor Engineered Equipment Package`).
- EPC review/acceptance workflow execution (covered by `DEL-096-06 EPC Vendor Package Review and Acceptance`).
- Package scope of work (`DEL-096-01`) and package datasheet (`DEL-096-02`).

## Requirements

| ID | Requirement | Source | Label |
|---|---|---|---|
| R-1 | The package vendor shall produce and maintain a Vendor Document Register that lists every document required for PKG-096. | `3-25_Comp_and_Liquids_DBM.md` line 617 ("Package deliverables shall include … vendor document registers"); `_CONTEXT.md` | derived |
| R-2 | The Vendor Document Register shall, at minimum, identify for each row: document number, title, document type, revision, submittal date, review/comment status, turnover status, and the SOW item(s) it satisfies (`SOW-0217` … `SOW-0220`). | `_CONTEXT.md` SOW mapping | ASSUMPTION (industry-standard register columns; exact column set per `26020-Package_Requirements.docx` heading 48 is location TBD) |
| R-3 | The vendor shall submit each registered document for EPC Integrator review prior to turnover. | `_CONTEXT.md` ResponsibleParty | derived |
| R-4 | The EPC Integrator shall perform interface/integration review on each vendor submittal and return comments through the controlled document-control channel. | `_CONTEXT.md` ResponsibleParty | derived |
| R-5 | Documents required by `26020-Package_Requirements.docx` package heading 48 shall be produced and tracked through the register. | `_CONTEXT.md` Source Reference | location TBD — clause-level content not accessible |
| R-6 | A Turnover Records set shall be produced at package handover comprising: the final accepted document index, transmittal manifests, and acceptance evidence for each register row. | `_CONTEXT.md` Anticipated Artifacts | derived |
| R-7 | Where the source set contains a vendor document table, individual row entries shall be carried as evidence artifacts in the register, not as separate deliverables. | `_CONTEXT.md` Notes ("individual source document rows remain artifacts/evidence, not separate deliverables") | source-grounded |
| R-8 | The deliverable's documentation shall be consistent with the package design envelope (ambient -40 deg C to +35 deg C; API 650 governing standard; sour service) where vendor documents address those attributes. | `3-25_Comp_and_Liquids_DBM.md` lines 94-101, 145, 406; PKG-096 title | derived |
| R-9 | Specific clause-level documentation requirements from `26020-Package_Requirements.docx` heading 48 — **TBD** (source not locally accessible as markdown). | — | TBD |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API 650 — Welded Tanks for Oil Storage | Governs design of the equipment that the vendor documents describe; vendor documentation must reference applicable API 650 clauses where relevant | location TBD (PKG-096 title; clause text not accessible in workspace) |
| `26020-Package_Requirements.docx` heading 48 — Vendor Documentation requirements | Defines the source-required vendor document set for this package class | location TBD |
| Project Document Control procedures | Govern numbering, revision control, transmittal, and turnover | TBD — not identified in accessible sources |
| BCER Consultation and Notification Manual | Not directly applicable to vendor document turnover; noted only as a project-level regulatory context | `3-25_Comp_and_Liquids_DBM.md` line 880 area (context only) |

## Verification

| Requirement | Verification Method | Verification Record |
|---|---|---|
| R-1, R-2 | Inspection of the Vendor Document Register against template/source-required columns | Register file (latest revision) |
| R-3, R-4 | Transmittal log audit showing each register row submitted and reviewed | Transmittal log; comment-resolution records |
| R-5 | Crosscheck register against `26020-Package_Requirements.docx` heading 48 list | Coverage matrix (heading-48 item → register row) — pending source access |
| R-6 | Turnover acceptance — every register row in `Accepted` status with attached evidence | Turnover manifest signed by EPC Integrator |
| R-7 | Inspection of register rows against source vendor document table rows | Source-row trace appendix |
| R-8 | Spot-check of vendor documents for design-envelope consistency (sour service, -40 deg C, API 650) | Review comments / dispositions |
| R-9 | Re-verify once source slices accessible | TBD |

## Documentation

Required artifacts produced by this deliverable:

- Vendor Document Register (PKG-096) — tabular index, latest revision.
- Vendor Document Submittals — the set of vendor-issued documents tracked through the register.
- Source-row evidence appendix (where the source set contains a vendor document table).
- Turnover Records:
  - Final accepted document index,
  - Transmittal manifests,
  - Acceptance evidence per register row.
- Coverage matrix mapping register rows to `SOW-0217`…`SOW-0220` and (when accessible) `26020-Package_Requirements.docx` heading-48 items.
