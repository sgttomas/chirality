# Procedure — Vendor Document Turnover Package (DEL-090-05)

This procedure describes how the Vendor Document Turnover Package is **produced**, **maintained**, and **turned over**. The procedure runs across the package vendor lifecycle, in parallel with DEL-090-04 (Vendor Engineered Equipment Package) and feeding DEL-090-06 (EPC Vendor Package Review and Acceptance).

## Prerequisites

- DEL-090-01 (Scope of Work), DEL-090-02 (Package Datasheet) accepted and accessible (context only; not declared upstream in `_DEPENDENCIES.md`).
- Source slice `26020-Package_Requirements.docx` heading 43 extracted so the required-document list is authoritative. (Currently TBD — extraction is a precondition for high-confidence execution.)
- Project document control conventions (numbering, transmittal, revision, EDMS) communicated to the vendor. (TBD)
- Vendor purchase order or contract in place naming this deliverable.
- DEL-090-04 (Vendor Engineered Equipment Package) kicked off so that documents have a subject.

## Steps

### Step 1 — Initialize the vendor document register
1. Create the register with columns at minimum: document number, title, revision, status, submittal stage, transmittal reference, EPC review disposition, due-by milestone, notes. (ASSUMPTION — final column set TBD per source.)
2. Seed required rows from `26020-Package_Requirements.docx` heading 43 once that source slice is extracted; until then, seed from the anticipated artifact list and the DEL-090-04 design basis.
3. Issue the register to the EPC Integrator for baseline acknowledgement.

### Step 2 — Plan submittal stages
1. For each row, identify the required submittal stage(s) (IFR/IFA/IFC/As-Built or equivalent). Stage rules TBD.
2. Sequence submittals against the DEL-090-04 design and fabrication schedule.
3. Mark critical-path submittals.

### Step 3 — Produce and submit documents
1. Author each document under the vendor's controlled process.
2. Apply the project numbering and transmittal convention (TBD).
3. Issue the document via transmittal; record the transmittal in the register.

### Step 4 — Manage EPC review
1. The EPC Integrator reviews each submittal and returns a disposition (e.g., Approved / Approved with comment / Revise and resubmit / Rejected). Disposition vocabulary TBD per project convention.
2. Update the register entry with the disposition and revision history.
3. Reissue under a new revision where required, until acceptance disposition is reached.

### Step 5 — Compile source-required vendor document table
1. Cross-check the register against the source-required document list (`26020-Package_Requirements.docx` heading 43 — `location TBD`).
2. Treat each source-required row as an artifact entry under this deliverable; do not promote any individual source row to a separate deliverable (`_CONTEXT.md` Notes).
3. Resolve any gaps before turnover.

### Step 6 — Assemble turnover record set
1. Confirm every register row is at an acceptance disposition or carries a documented and accepted deviation.
2. Compile certifications, ITP records, test/inspection reports, and as-built marked-up drawings into the turnover package.
3. Assemble the turnover acceptance statement signed by the vendor.

### Step 7 — Hand over to DEL-090-06
1. Issue the turnover record set to the EPC Integrator under DEL-090-06.
2. Support EPC review/acceptance queries against the turnover evidence.
3. Close the register entries upon EPC acceptance under DEL-090-06.

## Verification

| Step | Verification |
|---|---|
| 1 | Register baseline acknowledged by EPC Integrator; columns conform to project convention |
| 2 | Submittal plan reviewed against DEL-090-04 schedule; critical-path items identified |
| 3 | Every submittal has a transmittal record and a register entry |
| 4 | Every governed document reaches an acceptance disposition (or accepted deviation) |
| 5 | Source-required list reconciled to register with zero open gaps at turnover |
| 6 | Turnover checklist 100 percent complete: register closeout, ITPs, certifications, as-builts |
| 7 | DEL-090-06 acceptance recorded against this turnover evidence |

## Records

- Vendor document register (controlled, current, archived at turnover).
- Transmittal log.
- Submittal set (all revisions through accepted).
- Source-required vendor document table (as artifacts, evidence under this deliverable).
- ITP, certification, and as-built records.
- Vendor turnover acceptance statement.
- EPC review disposition log (cross-referenced; authoritative copy lives with DEL-090-06).
