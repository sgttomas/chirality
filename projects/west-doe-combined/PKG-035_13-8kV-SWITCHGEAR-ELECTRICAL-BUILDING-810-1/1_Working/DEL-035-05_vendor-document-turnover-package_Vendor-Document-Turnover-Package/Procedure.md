# Procedure: DEL-035-05 — Vendor Document Turnover Package

## Purpose

Procedure to **produce** the Vendor Document Turnover Package for `PKG-035` 13.8kV Switchgear Electrical Building (810-1): assemble the Vendor Document Register, manage submittals through the EPC interface review cycle, and compile the final turnover package suitable for EPC review and project handoff. Source: `_CONTEXT.md`; Specification R-035-05-001 through R-035-05-010.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in this deliverable folder. (Confirmed at time of Pass 1; `MEMORY.md` not present.)
- Access to `_Sources/26020-Package_Requirements.docx` (Table 4 vendor document set).
- Access to `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages row 37 for `PKG-035`).
- Sibling deliverables `DEL-035-01` (Scope of Work) and `DEL-035-02` (Package Datasheet) for applicability confirmation. Both are currently in `OPEN` state (verified by sibling folder inspection). Until drafted, this Procedure uses the working baseline from this deliverable's Datasheet and Specification.
- No declared upstream dependencies in `_DEPENDENCIES.md` (DECLARED mode).
- Vendor Document Control Procedure (DOC-008) authored by Package Vendor before submittals begin.

## Steps

### Step 1 — Establish the Vendor Document Register skeleton (PRQ-009)

1. Create the Vendor Document Index (PRQ-009) with one row per document, populated from:
   - Core vendor documents (Table 4 rows 1–11): PRQ-009, DOC-008, QLT-006, QLT-003, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015, PRQ-016.
   - Electrical discipline documents (Table 4 rows 64–80): ELE-002, ELE-003, ELE-014, ELE-015, ELE-016, ELE-020, ELE-027, ELE-028, ELE-029, ELE-030, ELE-017, ELE-012, ELE-019.
   - Cross-discipline documents per workbook row 37 `X` flags: applicable INS-*, CTL-026, TSF-*, STR-*; plus `TBD` rows for HVAC, Communications/Network, Maintenance Access, Grading, Utility Piping (per HRR-035-05-001).
2. Mark each row with one of: Required / Conditional (pending `DEL-035-01`/`DEL-035-02`) / Not Applicable (workbook row 37 = None) / TBD.

Source: Specification R-035-05-001, R-035-05-006, R-035-05-007.

### Step 2 — Issue Vendor Document Control Procedure (DOC-008)

Package Vendor authors and issues DOC-008 covering: document numbering, revision control, transmittal mechanics, review-comment incorporation, and turnover handover.

Source: Specification R-035-05-002.

### Step 3 — Confirm applicability with `DEL-035-01` and `DEL-035-02`

When the EPC Scope of Work and Package Datasheet are drafted:
1. Cross-check each Conditional row in the Register against the SOW/Datasheet scope.
2. Promote Conditional → Required or demote Conditional → Not Applicable.
3. Resolve `TBD` cross-discipline rows by adopting document IDs named in `DEL-035-01`/`DEL-035-02`, or escalate as a Conflict Table item if still unresolved.

Source: Specification "Scope"; Guidance Principle 3; HRR-035-05-001.

### Step 4 — Submit and track vendor documents through the review cycle

For each Required row:
1. Package Vendor issues the document with vendor doc number/rev and updates the Register with: status (Issued for Review), submittal date.
2. Submit to EPC Integrator for interface/integration review (`DEL-035-06`).
3. Receive review disposition; update Register with: disposition (Approved / Approved with Comments / Rejected), review-cycle date.
4. If Approved with Comments or Rejected, vendor reissues at next revision; repeat until Approved.

Source: Specification R-035-05-008, R-035-05-010.

### Step 5 — Compile core quality and inspection documentation

Confirm the following are present and at Approved status before turnover:
- QLT-006 Supplier Quality Plan
- QLT-003 Inspection and Test Plan (ITP) (executed records included)
- QLT-013 Material Test Reports / Certificates
- QLT-020 Inspection Release Certificate
- ELE-029 Electrical FAT / SAT Procedure
- ELE-030 Electrical Test Records / Energization Package

Source: Specification R-035-05-003; R-035-05-006.

### Step 6 — Compile logistics, spares, and shipping records

Confirm PRQ-013 Logistics / Shipping Plan and PRQ-015 Spare Parts Interchangeability Record (SPIR) are at Approved status before turnover.

Source: Specification R-035-05-005.

### Step 7 — Assemble turnover compilation

1. Finalize PRQ-009 Vendor Document Index (every row at final status/disposition).
2. Compile QLT-021 Manufacturing Record Book / Vendor Data Book.
3. Compile PRQ-016 Vendor Data Book / Final Supplier Documentation.
4. Either embed individual documents into QLT-021/PRQ-016 or reference them with stable document-control identifiers (decision per HRR-035-05-003).
5. Confirm every Required row in PRQ-009 is either embedded or unambiguously referenced.

Source: Specification R-035-05-004, R-035-05-009.

### Step 8 — Submit turnover package for EPC review

Submit the assembled turnover package to the EPC Integrator for `DEL-035-06` (EPC Vendor Package Review and Acceptance). Incorporate review dispositions back into the Register; reissue updated turnover package if material comments arise.

Source: Specification R-035-05-010; `DELIVERABLE_REGISTER.csv` row `DEL-035-06`.

## Verification

| Step | Verification |
|---|---|
| 1 | Register skeleton enumerates Core + Electrical + cross-discipline rows per Datasheet "Construction"; Not Applicable rows match workbook row 37 None flags |
| 2 | DOC-008 issued and on file |
| 3 | Every Register row has applicability decision recorded; no row left as Conditional after `DEL-035-01`/`DEL-035-02` are accepted |
| 4 | Every Required row reaches Approved (or Approved with Comments resolved) status before Step 7 |
| 5 | All listed quality/inspection documents present at Approved status |
| 6 | PRQ-013 and PRQ-015 present at Approved status |
| 7 | Turnover compilation includes final PRQ-009, QLT-021, PRQ-016; every Required document embedded or referenced |
| 8 | EPC review log (`DEL-035-06`) records turnover-package acceptance disposition |

## Records

- Final Vendor Document Index (PRQ-009)
- Vendor Document Control Procedure (DOC-008)
- All Required vendor document submittals (per Register) with review-cycle history
- Manufacturing Record Book / Vendor Data Book (QLT-021)
- Vendor Data Book / Final Supplier Documentation (PRQ-016)
- Turnover-package transmittal record to EPC Integrator
- Cross-reference to `DEL-035-06` review log
