# Package Datasheet — Procedure (DEL-056-02, PKG-056 Inlet Separators 4-25)

> Operational document. Describes how the EPC Integrator produces and issues the Package Datasheet artifact set for Vendor handoff. Steps are derived from the Specification requirements and `_REFERENCES.md`; `TBD` is used where judgment or unavailable basis is required.

## Purpose

Define the producer-side procedure for assembling, reviewing, and issuing the PKG-056 Package Datasheet from accepted upstream decomposition truth, source material slices, and the Specification, so that the artifact is fit for inclusion in the Vendor RFQ for `26020-01-PT-17-004 - Inlet Separators`.

## Prerequisites

### Declared upstream prerequisites
- Accepted decomposition snapshot at maturity threshold INITIALIZED or better: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (currently no in-file declared upstream dependencies per `_DEPENDENCIES.md`; the snapshot is the de facto upstream).
- Sibling DEL-056-01 (Scope of Work) at maturity INITIALIZED or better — required so package scope statements are coherent. **TBD** if not yet at threshold.

### Reference prerequisites
- `26020-Package_Requirements.docx` accessible and converted to text (this run used `/usr/bin/textutil -convert txt`).
- `26020-Packages_Interfaces_4_export.xlsx` row 68 reviewed. (Binary — direct cell extraction is **TBD** beyond what is restated in `26020-Package_Requirements.docx` heading 11.)
- DBM source slice `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 589-660 and 809-852 accessible.
- Vendor RFQ source `Bid Docs/Budgetary/26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` (referenced by Package Requirements heading 11). Extraction: **TBD**.

### Roles
- **EPC Integrator (responsible):** authors and issues the Datasheet artifact set.
- **Process Engineering:** rules on Conflict Table items CONF-001 through CONF-004 (in `Guidance.md`).
- **Operations review:** confirms mist-eliminator selection and weir adjustability (Specification R1.3, R2.x).
- **EPC discipline leads:** sign off on interface applicability matrix and vendor deliverable scope before Vendor RFQ issue.

## Steps

### Step P1 — Initialize the deliverable folder
Already complete (PREPARATION). Verify `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` exist and that `_STATUS.md` Current State is OPEN or INITIALIZED.

### Step P2 — Read source slices
1. Read `_CONTEXT.md` (identity, scope, anticipated artifacts, supports objectives).
2. Read the deliverable register row for DEL-056-02 in the decomposition snapshot.
3. Extract Package Requirements heading 11 (`26020-01-PT-17-004 - Inlet Separators`) and capture: Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables.
4. Read DBM 4-25 inlet-separator design parameters and inlet-separator related operability sections.
5. Record locations of inaccessible sources (e.g., the Vendor RFQ binary) as `TBD` in the Datasheet References.

### Step P3 — Populate the Datasheet
Author `Datasheet.md` covering: Identification, Attributes (equipment inventory), Conditions (Operating, Design), Construction, Interface Applicability Matrix, Process Interfaces, References. Every non-trivial value cites its source slice; unknown values are `TBD`; inferred items are labeled `ASSUMPTION`.

### Step P4 — Author the Specification
Author `Specification.md` with normative requirements R1-R8 derived only from accessible sources. Map each requirement to its source line/heading. Where standards are not stated in source, list candidate standards as `ASSUMPTION` with `location TBD`.

### Step P5 — Author the Guidance
Author `Guidance.md` with purpose, principles, considerations, trade-offs, vendor document set expansion, and a populated Conflict Table for human ruling.

### Step P6 — Cross-document consistency sweep (Pass 2)
Verify:
- Equipment items in Datasheet appear as requirements in Specification (R1.x).
- Operating/design values in Datasheet and Specification match to the digit (Pressure, Temperature, Flow, Retention).
- Interface applicability matrix matches verbatim between Datasheet and the source row 68 restatement.
- Terminology — "inlet separator", "MPFF", "drive gas", "HIPPS", "Devchem 253", "PCV" — used consistently across all four documents.
- Conflict Table in `Guidance.md` covers every disagreement noted in any document.

### Step P7 — Status update
If `_STATUS.md` Current State is `OPEN`, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` to transition to INITIALIZED.

### Step P8 — Issue for review
Stage the four documents for review by Process Engineering and EPC discipline leads. Issuance to Vendor RFQ requires acceptance of Conflict Table rulings, resolution of `TBD` items material to bid scope, and management approval (out of agent scope per K-AUTH-1).

## Verification

| Check | Pass criterion |
|---|---|
| All four documents present | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` exist in `{DELIVERABLE_PATH}` |
| Default schema sections present | Datasheet has Identification/Attributes/Conditions/Construction/References; Specification has Scope/Requirements/Standards/Verification/Documentation; Guidance has Purpose/Principles/Considerations/Trade-offs/Examples; Procedure has Purpose/Prerequisites/Steps/Verification/Records |
| Source grounding | Each non-trivial value cites a source slice; unsourced inferences carry `ASSUMPTION` |
| Cross-document numeric consistency | Datasheet vs Specification values match to the digit |
| Conflict Table completeness | Every cross-source disagreement captured (CONF-001 .. CONF-004) |
| `_STATUS.md` transition | OPEN -> INITIALIZED applied via the safe-update helper |
| `_run_records/` entry | Run record present with `run-status: SUCCESS` and populated completion headings |

## Records

The following records evidence the producer-side execution of this Procedure:

- `_run_records/TASK_RUN_2026-05-25_0425.md` — TASK run record for this drafting pass (Pass 1 + Pass 2).
- `_STATUS.md` history entry transitioning OPEN -> INITIALIZED.
- (Future) Process Engineering ruling on CONF-001 through CONF-004 (record location: **TBD**, likely `_MEMORY.md` once human-ruled).
- (Future) `_SEMANTIC_LENSING.md` register and a subsequent Pass-3 TASK run record (per ORCHESTRATOR Phase 2.5).
- (Future) Review/approval evidence prior to Vendor RFQ issuance (out of agent scope).
