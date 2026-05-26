# Procedure: DEL-100-05 — Vendor Document Turnover Package

**Interpretation:** This procedure covers both (a) **producing** the deliverable artifacts (register, submittals, turnover records) and (b) **operating** the document submittal/review/turnover lifecycle they govern.

## Prerequisites

- Accepted GATE-07 PROJECT_DECOMP snapshot 2026-05-24 (`_REFERENCES.md`).
- `_CONTEXT.md` identity and scope established for `DEL-100-05`.
- Package vendor selected for PKG-100 (TBD — not in accessible sources).
- EPC Integrator document control channel established (TBD — project-level procedure not in accessible sources).
- Access to `26020-Package_Requirements.docx` heading 52 source slice (currently **TBD** — not locally parseable as markdown).
- Access to `26020-Packages_Interfaces_4_export.xlsx` row 63 to identify interface-affecting documents (currently **TBD** — not locally parseable).
- Sibling deliverables `DEL-100-01` (SOW), `DEL-100-02` (Package Datasheet), and `DEL-100-04` (Vendor Engineered Equipment Package) sufficiently mature to define what the vendor is producing.

## Steps

1. **Initialize the Vendor Document Register.**
   - Create the register with the column set defined in `Specification.md` R-2 (PROPOSAL columns until heading-52 access).
   - Pre-populate rows for each known required document type (datasheets, drawings, calculations, certifications, manuals, test records, H2O2 safety/handling documentation) — exact list **TBD** pending source heading-52 slice.
   - Map every row to one or more SOW items (`SOW-0107`…`SOW-0110`).
   - Map every row to the applicable interface types from `PACKAGE_REGISTER.csv` row 63 where relevant.
2. **Confirm source-required document list.**
   - When `26020-Package_Requirements.docx` heading 52 becomes accessible, reconcile the register against it and add/remove rows to match the source-required set.
   - Record the reconciliation as evidence (date, source revision, deltas).
3. **Issue register to vendor for population.**
   - Vendor confirms document numbers, planned submittal dates, and any source-table row references.
4. **Vendor submittals.**
   - For each register row, vendor issues the document through the controlled transmittal channel.
   - Update register row: `Submitted` date, transmittal number, revision.
5. **EPC Integrator interface/integration review.**
   - EPC reviewer assesses each submittal for: completeness against the register row; interface/integration consistency with adjacent packages and with the package interface scope (`PACKAGE_REGISTER.csv` row 63); alignment with the package design envelope (e.g., -40 deg C ambient; sour-water service; H2O2 handling); and consistency with `DEL-100-02` Package Datasheet and `DEL-100-04` Vendor Engineered Equipment Package content.
   - Issue comments via document control.
   - Update register row: `Under review` → `Commented` or `Accepted`.
6. **Comment resolution.**
   - Vendor revises and re-submits as needed. Each revision creates a new register transaction (Rev A → Rev B …) until acceptance.
7. **Carry source-row evidence.**
   - Where the source set (e.g., `26020-Packages_Interfaces_4_export.xlsx` row 63) contains a vendor document table row, attach it as evidence on the corresponding register row rather than creating a parallel deliverable. (`_CONTEXT.md` Notes.)
8. **Compile turnover records.**
   - At PKG-100 handover, produce: final accepted document index (snapshot of the register at acceptance), transmittal manifests (all submittals and revisions), acceptance evidence (signed dispositions per row).
9. **Update deliverable status.**
   - When the four documents are first drafted: `_STATUS.md` OPEN → INITIALIZED.
   - Downstream state transitions are handled by the deliverable's normal lifecycle, not by this procedure.

## Verification

- Register column completeness check against `Specification.md` R-2.
- Coverage matrix check: every SOW item (`SOW-0107`…`SOW-0110`) is covered by ≥1 register row.
- Interface coverage check: every applicable interface type in `PACKAGE_REGISTER.csv` row 63 is represented or explicitly dispositioned as not applicable.
- Heading-52 reconciliation completed (or carried as **TBD** with reason).
- Every register row at turnover is in `Accepted` status with attached acceptance evidence.
- H2O2-handling/safety content present in at least one accepted vendor document (or explicit not-applicable disposition with rationale).
- Sample audit: pull a random subset of accepted rows and confirm transmittal, comment-resolution, and acceptance evidence are present and consistent.
- Cross-document consistency: terms (`Vendor Document Register`, `Submittal`, `Turnover Records`) match Datasheet, Specification, and Guidance.

## Records

- `VendorDocumentRegister_PKG-100.xlsx|.csv` (latest revision and turnover snapshot).
- Transmittal log (all transmittals issued vendor → EPC and EPC → vendor for this package).
- Comment-resolution records per submittal revision.
- Source-row evidence appendix (citations to `26020-Packages_Interfaces_4_export.xlsx` row 63 sub-rows where applicable).
- Turnover manifest signed by EPC Integrator at handover.
- Run record(s) for `DEL-100-05` in `_run_records/`.
- Coverage matrix: register row ↔ SOW item ↔ (when accessible) `26020-Package_Requirements.docx` heading-52 item.
- Interface coverage matrix: register row ↔ interface type from `PACKAGE_REGISTER.csv` row 63.
