# Procedure — DEL-059-06 EPC Vendor Package Review and Acceptance

## Purpose

Define the operational sequence by which the EPC Integrator reviews, accepts, and documents the vendor-engineered NGL storage bullet package (PKG-059), producing the four anticipated artifacts referenced in `_CONTEXT.md`.

This procedure describes how to **produce** the acceptance deliverable (review-and-acceptance evidence). It is not an operating procedure for the bullets themselves.

## Prerequisites

| Prerequisite | Source / Reference |
|---|---|
| Accepted snapshot of DEL-059-01 Scope of Work | DELIVERABLE_REGISTER row 462 |
| Accepted snapshot of DEL-059-02 Package Datasheet | DELIVERABLE_REGISTER row 463 |
| Accepted snapshot of DEL-059-03 Construction Work Package | DELIVERABLE_REGISTER row 464 |
| Vendor engineered equipment package submittal (DEL-059-04) | DELIVERABLE_REGISTER row 465 |
| Vendor document turnover package (DEL-059-05) | DELIVERABLE_REGISTER row 466 |
| Access to DBM design basis (storage bullet sections) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Access to 26020-Package_Requirements.docx heading 14 | Not locally extracted — location TBD |
| Plot plan CIV-235633-5002 (for layout verification) | Open external gap (`4-25_Deepcut_DBM.md` line 237) — TBD |
| Declared upstream dependencies | None declared during PREPARATION (`_DEPENDENCIES.md`) |

## Steps

### Step 1 — Confirm basis-document maturity
Verify DEL-059-01/02/03 are at their accepted snapshots. If any is not at acceptance, record the affected acceptance items as `partial / blocked` and continue with the items that are unblocked. (Specification R-01.)

### Step 2 — Inventory vendor submittals (input to R-02)
List every vendor submittal received under DEL-059-04 and DEL-059-05 with document ID, revision, and submittal date. This list is the index for the vendor document review log.

### Step 3 — Review each vendor submittal (R-02)
For each entry in Step 2, record:
- Reviewer
- Review date
- Disposition (`accept` / `accept with comment` / `reject`)
- Comments referencing the EPC basis section that the comment relates to.
Output: `vendor document review log` artifact.

### Step 4 — Build the package acceptance checklist (R-03)
- Row for each SOW item: SOW-0181, SOW-0182, SOW-0183, SOW-0184.
- Row for each Package Datasheet attribute (from DEL-059-02 once available).
- Status per row: `covered` / `partial` / `open`, with cited evidence.
Output: `package acceptance checklist` artifact.

### Step 5 — Collect test and inspection evidence (R-04)
- Pull vendor ITP records, witness reports, and certification records from DEL-059-04 / DEL-059-05.
- Acceptance criteria: TBD — to be defined by DEL-059-02 Package Datasheet.
Output: `test/inspection evidence` artifact.

### Step 6 — Verify spacing/siting against API 2510 (R-06)
Using the current plot plan revision (or note `pending CIV-235633-5002`), verify each distance listed in the DBM Pressurized Bullet Spacing table (`4-25_Deepcut_DBM.md` lines 245-266). Record each distance as `verified`, `non-conforming`, or `TBD pending plot plan`.

### Step 7 — Verify storage capacity (R-07)
Confirm the as-built or as-engineered configuration totals 16 x 120,000 USG NGL bullets at 04-25 (`4-25_Deepcut_DBM.md` line 1629; line 492).

### Step 8 — Verify spill control and grading interface (R-08)
Confirm civil grading and containment provisions per DBM line 2722. If grading basis is not yet developed, mark this acceptance item TBD and flag the civil interface.

### Step 9 — Collect turnover evidence (R-05)
Aggregate turnover records produced under DEL-059-03 (construction turnover items) and DEL-059-05 (vendor turnover documentation).
Output: `turnover evidence` artifact.

### Step 10 — Compile acceptance recommendation
Aggregate findings from Steps 3-9 into an overall acceptance recommendation:
- `Accept`
- `Accept with conditions` (list conditions)
- `Reject` (list non-conformities)
- `Pending` (list open TBDs and blockers, e.g., plot plan CIV-235633-5002).
Binding approval remains with the human owner (Guidance — "Acceptance != approval").

### Step 11 — Provenance audit (R-09)
Sample-audit acceptance findings to confirm each cites its evidence (vendor doc ID + revision + section, or EPC basis section, or `location TBD`).

## Verification

| Step | Verification |
|---|---|
| Steps 2-3 | Vendor document review log includes every received submittal |
| Step 4 | Each of SOW-0181..0184 has at least one checklist row |
| Step 5 | Test/inspection evidence file present even if acceptance criteria are TBD (TBDs documented) |
| Step 6 | API 2510 spacing table fully addressed (each row `verified` / `non-conforming` / `TBD pending plot plan`) |
| Step 7 | Bullet count and size match DBM basis or non-conformity captured |
| Step 8 | Grading/containment item present with status |
| Step 9 | Turnover evidence file references both DEL-059-03 and DEL-059-05 outputs (or notes their absence) |
| Step 10 | Single overall recommendation present with cited findings |
| Step 11 | Provenance audit sample (size TBD) shows >= ASSUMPTION threshold of cited findings; non-citing findings marked TBD |

## Records

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence record
- Turnover evidence record
- Acceptance recommendation memo (Step 10 output)
- Provenance audit log (Step 11 output)

Storage location, naming convention, and retention rules: TBD (program documentation standards).
