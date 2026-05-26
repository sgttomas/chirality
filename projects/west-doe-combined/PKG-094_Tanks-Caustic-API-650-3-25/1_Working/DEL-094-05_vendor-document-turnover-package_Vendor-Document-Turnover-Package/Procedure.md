# Procedure: DEL-094-05 — Vendor Document Turnover Package

## Purpose

This procedure describes how the Vendor Document Turnover Package is *assembled and turned over* for PKG-094. The Package Vendor is the executing role; the EPC Integrator is the reviewing/accepting role.

## Prerequisites

- DEL-094-01 (Scope of Work) and DEL-094-02 (Package Datasheet) issued and accepted, so vendor scope is fixed. [Source: DELIVERABLE_REGISTER rows DEL-094-01, DEL-094-02]
- DEL-094-04 (Vendor Engineered Equipment Package) in progress; vendor authoring documents per its design basis. [Source: DELIVERABLE_REGISTER row DEL-094-04]
- Source vendor document table (`_Sources/26020-Package_Requirements.docx` package heading 46) accessible for extraction. **Currently `location TBD` — see HRR-001 in Guidance Conflict Table.**
- `_REFERENCES.md` populated with locally accessible reference materials.
- `_DEPENDENCIES.md` declared upstream/downstream lists current (none declared at PREPARATION).

## Steps

### Step 1 — Initialize the vendor document register

1.1 Create the master register with the standard columns identified in Specification R1.2.
1.2 Pre-populate row classes from DBM 3-25 line 617 (datasheets, cause-and-effect, utility loads, relief/load data, tie-in lists, envelopes, sparing, materials/coating, maintenance access, shipped-loose, registers). [Source: DBM 3-25 line 617]

### Step 2 — Populate from source vendor document table

2.1 Extract rows from `_Sources/26020-Package_Requirements.docx` package heading 46. *(TBD: source extraction blocked in current run — see HRR-001.)*
2.2 For each source row, add or reconcile a register row.
2.3 Where a standard class from Step 1.2 is absent in the source table, record the absence explicitly (do not silently drop).

### Step 3 — Define document submittal plan

3.1 Assign each register row to a planned submittal date.
3.2 Identify hold items per Guidance Conflict Table (HRR-002 through HRR-007) and tag affected register rows.
3.3 Confirm interface points with DEL-094-01, DEL-094-02, DEL-094-03 owners (EPC).

### Step 4 — Author and submit vendor documents (Package Vendor)

4.1 Author each document per its row class.
4.2 Submit to EPC Integrator with revision identity and source row reference.
4.3 Update register row status on submission.

### Step 5 — EPC Integrator review

5.1 EPC Integrator reviews each submittal for interface/integration consistency with DEL-094-01, DEL-094-02, DEL-094-03. [Source: `_CONTEXT.md`]
5.2 Record disposition (e.g., approved / approved with comments / rejected) against the register row.
5.3 Route any disposition that affects a different deliverable (e.g., Construction Work Package) to the responsible owner.

### Step 6 — Iterate to acceptance

6.1 Iterate Steps 4–5 per row until the row reaches an acceptable disposition.
6.2 Close out hold items (HRR-002..HRR-007) explicitly — either by accepted submittal or by recorded ruling.

### Step 7 — Assemble turnover records

7.1 Collect MTRs, code certifications, inspection/NDE/hydrotest records, painting/coating records, O&M manuals, commissioning spares list. [Source: Specification R4.2 ASSUMPTION]
7.2 Attach each turnover record to its register row.
7.3 Confirm the API 650 (modified) code stamp / nameplate record is present. [Source: SOW-0195]

### Step 8 — Final turnover to DEL-094-06

8.1 Issue the final vendor document register and turnover record set to DEL-094-06 (EPC Vendor Package Review and Acceptance). [Source: DELIVERABLE_REGISTER row DEL-094-06]
8.2 Confirm all HRR items either closed or carried as recorded open items at package-handoff time.

## Verification

| Check | Method |
|---|---|
| All source-table rows present in register | Row-by-row reconciliation (currently blocked by HRR-001). |
| All register rows have a disposition | Register column audit. |
| All HRR items have a disposition (closed or carried) | HRR table audit against Guidance Conflict Table. |
| Code-required records present (API 650 family) | Inspection of nameplate, code-stamp, MTR rows. |
| Hydrotest, NDE, coating records present | Inspection of turnover-records section. |
| EPC Integrator review log complete | Cross-check between register and review log. |

## Records

- Vendor document register (final issued state).
- Vendor document submittals (each with revision identity).
- EPC Integrator review log (one entry per register row per cycle).
- Turnover record set (per Step 7).
- HRR closure log (per Step 6.2 and Step 8.2).
- Any extracted side-file of the source vendor document table created to close HRR-001.
