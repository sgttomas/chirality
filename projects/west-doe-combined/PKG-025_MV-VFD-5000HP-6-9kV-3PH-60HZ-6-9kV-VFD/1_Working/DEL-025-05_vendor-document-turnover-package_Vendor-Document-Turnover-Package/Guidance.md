# Guidance: DEL-025-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists to give the Package Vendor a single, reviewable channel for the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records for `PKG-025` (MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD). It feeds the EPC Integrator's interface and integration review and the downstream EPC Vendor Package Review and Acceptance deliverable (`DEL-025-06`) without duplicating vendor engineering scope held by `DEL-025-04` or the EPC anchor deliverables (`DEL-025-01`, `DEL-025-02`, `DEL-025-03`).

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD" because that is the workbook and Gate 7 register spelling.
- Treat individual source vendor document table rows as artifacts/evidence of vendor documentation, not as separate deliverables (per `_CONTEXT.md` Notes).
- Keep vendor documentation responsibility with the Package Vendor and integration review with the EPC Integrator.
- Use `TBD` for per-document register content, vendor transmittal IDs, hold codes, and turnover record schedule until a source-supported package-specific basis is available.
- Use the DBM mechanical packages organisation paragraph at the level it supports: as a content category checklist for vendor documentation, not as an exhaustive package-specific requirement set.
- Surface the vendor-documentation source gap recorded by `ARTIFACT_REGISTER.csv` row `ART-5D23A5F2CB` rather than masking it with invented register entries.

## Considerations

The DBM mechanical packages organisation paragraph is the strongest accessible source that bears on vendor-document content. It establishes that "Package deliverables shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers." This is mechanical-packages framing; for an Electrical MV VFD package, several categories (e.g., relief/load data) may legitimately be N/A, and several Electrical-specific items (drive controls, harmonic studies, MV cable termination, grounding terminations) are likely required but are not enumerated by the accessible source.

`PKG-025` carries six applicable interface facts in `INTERFACE_REGISTER.csv` (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports). Vendor documentation should cover each of these interfaces with appropriate documents (datasheets, schematics, interconnection diagrams, cable schedules, communication-protocol descriptions, maintenance access drawings, and structural support details), but the exact document list and revision plan are not defined by accessible sources.

The DBM Deepcut electrical/process design basis confirms MV-driven equipment patterns in the Deepcut facility (e.g., MV motors and starting VFD usage) but does not provide a package-specific vendor-document requirement set for `PKG-025`. The package-specific Word requirements source (`26020-Package_Requirements.docx`) did not produce a `PKG-025` match accessible to this deliverable.

Turnover record content is conventionally project-defined (FAT/SAT certificates, calibration sheets, spare-parts lists, training records, as-built marks, warranty documents). The accessible source set does not define this set for `PKG-025`, so it must be carried as `TBD` and resolved by the project turnover/handover standard or human ruling.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Vendor document register field schema | Define the minimum useful field set (identifier, title, revision, status, submittal date, turnover state) and label any extensions as `ASSUMPTION`. | DBM requires a vendor document register but does not enumerate its fields; project document-control standard is not locally accessible. |
| Per-document content list | Anchor on DBM mechanical packages content categories with explicit N/A entries for non-applicable mechanical items; do not invent Electrical-specific document titles. | DBM gives a content category list, not a per-document title list; package-specific source is missing. |
| Turnover record set | Mark detailed turnover record types as `TBD` pending project turnover standard. | No source-supported turnover record list for `PKG-025`. |
| Interface coverage | Require vendor documentation to demonstrably cover each of the six `PKG-025` interface facts; do not assume coverage. | Six interfaces are explicit register facts; coverage must be evidenced. |
| Standards | List project document-control, project turnover, project electrical, and CEC as governing bases with locations `TBD`. | These bases are referenced by DBM but the specific documents/clauses are not in the deliverable folder. |

## Examples

- Acceptable register entry: "Vendor document register field set: identifier, title, revision, status, submittal date, turnover state. Source: DBM mechanical packages organisation paragraph (requires a vendor document register); field-level schema labelled `ASSUMPTION` pending project document-control standard."
- Acceptable interface-coverage entry: "Communications / Network interface (`IFC-EF46C006CC`) shall be supported by vendor documentation describing the VFD network/protocol interface; specific document title and revision: `TBD`."
- Acceptable source-gap entry: "Turnover record schedule: `TBD`. No package-specific source slice or project turnover standard accessible."
- Not acceptable without new source: "Vendor shall submit drawings A, B, C at revision 3 with hold code H2 by week 14." The accessible source set does not establish this.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-025-05-001 | DBM vendor-document content categories are written for mechanical packages, but `PKG-025` is an Electrical MV VFD package; some categories (e.g., relief/load data) are not naturally applicable and other Electrical-specific items (harmonic study, MV termination, drive control narrative) are likely required but not enumerated. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages organisation paragraph | Workbook Packages row 27; `PACKAGE_REGISTER.csv` row `PKG-025` (discipline Electrical) | Datasheet Attributes/Construction; Specification Requirements REQ-025-05-005; Procedure Steps | Use DBM as a content category checklist with explicit N/A entries; add Electrical-specific document categories only after a source-supported Electrical vendor-document standard is accepted. | TBD |
| HRR-025-05-002 | No accessible source defines the per-document register schedule, hold codes, transmittal IDs, or turnover record set for `PKG-025`; `ARTIFACT_REGISTER.csv` row `ART-5D23A5F2CB` records this as a vendor documentation gap. | `ARTIFACT_REGISTER.csv` row `ART-5D23A5F2CB`; `_Sources/26020-Package_Requirements.docx` (no PKG-025 match) | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-025-05` | Datasheet Attributes/Construction; Specification Requirements REQ-025-05-004, REQ-025-05-008, REQ-025-05-009; Procedure Steps | Keep detailed register and turnover content as `TBD` until project document-control and turnover standards or vendor-supplied lists are accepted. | TBD |
