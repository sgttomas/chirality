# Procedure: DEL-099-05 — Vendor Document Turnover Package

## Purpose

Produce and accept the Vendor Document Turnover Package for `PKG-099 Truck Product Loading Unit 3-25`: assemble the vendor document register, collect and review vendor submittals, capture source-required vendor documents, and compile the turnover dossier. EPC Integrator reviews for interface/integration acceptance.

## Prerequisites

- Accepted Gate 7 decomposition snapshot for `PKG-099` (FACT — `_REFERENCES.md`).
- Locally accessible DBM source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (FACT).
- Access to project package requirements specification `26020-Package_Requirements.docx` heading 51 — **currently not locally parseable; required before steps marked (*) can be fully executed.**
- Access to project specification index referenced in DBM SEC-12 line 888 — **location TBD**.
- Vendor under contract for the `PKG-099` truck loading package (ASSUMPTION — not declared in `_DEPENDENCIES.md`).
- No declared upstream dependencies in `_DEPENDENCIES.md` (FACT); revisit if dependencies are later declared.

## Steps

### S1 — Establish the vendor document register baseline

1. Extract the package-specific required-document list from `26020-Package_Requirements.docx` heading 51. (*)
2. Cross-reference the generic mechanical package deliverable list from DBM SEC-09 (line 617): datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers.
3. Create the vendor document register file with one row per required document number. Columns: DocNumber, Title, Class, RevisionPlanned, RevisionCurrent, IssueStage (IFR/IFC/AB), Source-Required (Y/N), AcceptedForTurnover (Y/N/Date), Reviewer, Notes.

### S2 — Issue register to vendor and receive Issued-For-Review submittals

1. Transmit the baseline register to the vendor with required submittal stages and dates.
2. Receive vendor IFR submittals; log into register; flag missing items.

### S3 — EPC Integrator interface/integration review

1. For each submittal, verify alignment with parent DBM (SEC-06 truck loading basis lines 413-416; SEC-08 driver basis line 526; SEC-09 line 617; SEC-02/SEC-09 line 145 ambient).
2. Verify interface continuity to adjacent packages and to facility-side tie-in (LACT interface remains third-party NRM scope per DBM SEC-06 line 417).
3. Issue review comments back to vendor; track to closure in the register.

### S4 — Progress to Issued-For-Construction

1. Confirm vendor has addressed all IFR comments.
2. Update register IssueStage to IFC for accepted documents.
3. Maintain change control for any post-IFC revisions.

### S5 — Capture source-required vendor documents

1. From the heading 51 list (*), identify documents the project specification names explicitly.
2. Confirm each source-required document is present, current, and reviewed; mark `Source-Required = Y` in the register.

### S6 — Assemble turnover dossier

1. Collect As-Built revisions of all register documents.
2. Collect turnover records (per Specification R5; specific contents TBD until heading 51 list is accessible):
   - as-built drawings (ASSUMPTION)
   - signed FAT and SAT reports (ASSUMPTION)
   - calibration / certification records (ASSUMPTION)
   - punch list with disposition (ASSUMPTION)
   - system handover certificate (ASSUMPTION)
3. Verify per-station and per-pump coverage (three loading stations, three condensate loading pumps; DBM SEC-06 lines 414-415).

### S7 — Acceptance and handover

1. EPC Integrator confirms the register is complete, all items are AB stage, all source-required documents are present, all review comments closed, and turnover dossier items are signed.
2. Mark register entries `AcceptedForTurnover = Yes/<date>`.
3. Issue the turnover package to the operator.

## Verification

| Step | Verification |
|---|---|
| S1 | Register file exists; row count matches the union of heading 51 list and DBM SEC-09 classes (TBD until heading 51 is accessible). |
| S2 | Every register row has an IFR receipt date or a documented gap. |
| S3 | Every IFR submittal has a recorded review disposition and traceable comment closure. |
| S4 | Every IFC row references a closed-comment IFR predecessor. |
| S5 | Every `Source-Required = Y` row maps to a heading 51 line item. |
| S6 | Turnover dossier inventory equals or exceeds Specification R5 list; deviations explained. |
| S7 | Handover certificate signed; register frozen; archived in turnover folder. |

## Records

- Vendor document register (live and frozen-at-turnover versions)
- Vendor submittals (per register, per stage)
- Source-required vendor documents (per heading 51 — TBD list)
- EPC Integrator review/comment log
- Turnover dossier (per S6)
- Signed handover certificate
