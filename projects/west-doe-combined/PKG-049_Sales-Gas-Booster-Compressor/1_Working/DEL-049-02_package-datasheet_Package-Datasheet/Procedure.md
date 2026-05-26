# Procedure — DEL-049-02 Package Datasheet (Sales Gas Booster Compressor, PKG-049)

> Operational procedure to **produce** the EPC Package Datasheet artifact for
> PKG-049. (Procedures to operate the physical package belong to the Package
> Vendor's O&M deliverables and are out of scope here.) Steps are
> source-grounded; judgment-bound steps are marked `TBD`.

## Purpose

Provide the EPC Integrator's package-engineering team with the sequence of
steps required to draft, review, and complete the source-grounded Package
Datasheet handoff for the Sales Gas Booster Compressor package, consistent
with `_CONTEXT.md`, `_REFERENCES.md`, the Specification, and the Guidance for
this deliverable.

## Prerequisites

### Declared dependencies

- Declared Upstream Dependencies: none declared at PREPARATION
  (`_DEPENDENCIES.md`). Run `TASK + dependency-extract` if upstream coupling
  needs in-file declaration.
- Declared Downstream Dependencies: none declared at PREPARATION
  (`_DEPENDENCIES.md`).

### Required reference materials

| Reference | Status | Action if missing |
|---|---|---|
| DBM Deepcut markdown (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) | Locally accessible. Use §"Sales Gas Booster Compressor Basis" (lines 932-969) and §"Sales Gas Booster Filter/Coalescer" (lines 1469-1483). | Re-fetch from `_Sources/` if not present. |
| PACKAGE_REGISTER.csv (GATE-07 snapshot) | Locally accessible. Use PKG-049 row 80. | Re-fetch GATE-07 snapshot. |
| DELIVERABLE_REGISTER.csv (GATE-07 snapshot) | Locally accessible. Use DEL-049-02 row. | Re-fetch GATE-07 snapshot. |
| `26020-Package_Requirements.docx` heading 4 | **Not locally accessible as text.** | Request conversion to readable form before completing Specification §2.6 detail. |
| `26020-Packages_Interfaces_4_export.xlsx` | **Not locally accessible as text.** | Request conversion (or CSV export) before completing interface matrix detail. |
| RFQ source `RFQ/Bid Docs/26020-01-PT-RFQ-12-004-Sales Booster Comp.docx` | Not locally accessible. | Request conversion if RFQ-language alignment is required. |

### Deliverable-local prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` present (verified during this run).
- `_STATUS.md` Current State must be in `ALLOW_OVERWRITE_STATES` (OPEN or INITIALIZED) before any rewrite.

## Steps

### Step 1 — Confirm scope and identity

1. Read `_CONTEXT.md` Identity, Scope, Covers Scope Items, Supports Objectives, and Source Reference.
2. Read the DEL-049-02 row of DELIVERABLE_REGISTER.csv to confirm `Anticipated_Artifacts` and `Source_Refs`.
3. Read the PKG-049 row of PACKAGE_REGISTER.csv to confirm Scope_Split and Applicable_Interfaces.
4. Record any discrepancy between `_CONTEXT.md` and registers as a `CONFLICT` in `Guidance.md` Conflict Table.

### Step 2 — Read source slices

1. Open DBM Deepcut markdown and read:
   - §"Sales Gas Booster Compressor Basis" (lines 932-969) — package basis, design conditions, compositions, sub-systems.
   - §"Sales Gas Booster Filter/Coalescer" (lines 1469-1483) — F-3500-1 operating envelope.
   - §"Compression Configuration" table (lines 870-879) — overall compression role.
   - §"HP Sales Header" entries (lines 1434-1436) — suction and discharge routing context.
   - §"Sales booster compressor sweep and purge gas" (line 1712) — sweep/purge flow basis.
   - Open-items list (line 1808) — confirms F-3500-1 design-flow conflict.
2. Capture verbatim values; do not paraphrase units.
3. If a needed value is absent from accessible sources, record as `TBD` in the target document — do not invent.

### Step 3 — Draft Datasheet.md

1. Populate Identification from `_CONTEXT.md` and PACKAGE_REGISTER.csv.
2. Populate Attributes, Conditions, Construction tables from DBM Deepcut §932-§969, preserving source citations on each row.
3. Populate the Filter/Coalescer table from DBM Deepcut §1471-§1483.
4. Populate Interfaces from PACKAGE_REGISTER.csv Applicable_Interfaces; carry process-interface evidence from DBM Deepcut §1434-§1436, §1471.
5. Mark non-process interface scope `TBD` where the underlying Word/Excel sources are not accessible.

### Step 4 — Draft Specification.md

1. Define Scope (in/out) from `_CONTEXT.md` Scope, DELIVERABLE_REGISTER Description, and PACKAGE_REGISTER Scope_Split.
2. Write Requirements groups (Identification, Configuration, Driver, Process Design, Sub-systems, Interfaces). Each requirement cites its source slice. Use `ASSUMPTION` only when the requirement is inferred, never to substitute for missing source.
3. List Standards (NEMA MG 1, API-11P, project DBM) and mark each as locally accessible or `location TBD`.
4. Map each requirement group to a Verification approach.
5. Tie Documentation back to `_CONTEXT.md` Anticipated Artifacts.

### Step 5 — Draft Guidance.md

1. Frame Purpose from `_CONTEXT.md` Scope and Notes.
2. Write Principles, Considerations, Trade-offs from DBM source slices; do not introduce rationale unsupported by source.
3. Surface every cross-source conflict found during Step 2 in the Conflict Table at the bottom of Guidance.md.
4. Cross-check that every Trade-off and every Consideration cites a specific DBM section.

### Step 6 — Draft Procedure.md (this document)

1. Confirm steps describe how to produce the deliverable.
2. Confirm Prerequisites align with `_DEPENDENCIES.md` and `_REFERENCES.md`.
3. Confirm Verification and Records sections (below) align with the Specification's Verification approach.

### Step 7 — Pass 2 cross-reference consistency check

1. Walk the four documents and verify:
   - Datasheet attributes/values appear as requirements in Specification where appropriate.
   - Specification requirements have rationale or trade-off entries in Guidance where appropriate.
   - Specification verification approaches map to Procedure verification steps.
   - Terminology (e.g., "F-3500-1", "HP Sales Header 2", "TCPL") is identical across all four documents.
   - Numeric values and units are identical across all four documents.
2. When values disagree, re-read source slices (Step 2). If unresolvable, add a Conflict Table entry in Guidance.md.

### Step 8 — Status update

1. Verify `_STATUS.md` Current State is `OPEN`.
2. If yes, update to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` with reason `TASK+four-documents (P1_P2)`.
3. If not `OPEN`, do not regress; record the skip in the run record.

### Step 9 — Run record

1. Write `_run_records/TASK_RUN_<timestamp>.md` with all required frontmatter and headings.

## Verification

| Verification | Method |
|---|---|
| All four documents exist | Directory listing of `{DELIVERABLE_PATH}`. |
| Each document contains its default schema sections | Section-heading inspection. |
| At least one locally accessible source was read | Run record `## Tools Used` and `## Outputs Produced` notes; source citations in Datasheet/Specification/Guidance. |
| Substantive values cite a source (`SourcePath` + `SectionRef`) or are marked `TBD`/`location TBD` | Spot-check Datasheet Conditions table and Specification §2.4. |
| Inferences carry `ASSUMPTION` label | Search for `ASSUMPTION` in each document. |
| Terminology and numeric values are consistent across all four documents | Cross-document diff against key terms (e.g., 6,137 kPag, 12,866 kPag, 140 MMSCFD, 6,700 hp, F-3500-1). |
| Conflicts captured in Guidance Conflict Table where unresolvable | Inspect Guidance.md Conflict Table. |
| `_STATUS.md` change (if any) follows safe-update rules | Compare `_STATUS.md` History against Step 8 rule. |
| `_run_records/TASK_RUN_*.md` exists with required headings | File listing and content check. |

## Records

The following records constitute the evidence of this procedure:

- `{DELIVERABLE_PATH}/Datasheet.md`
- `{DELIVERABLE_PATH}/Specification.md`
- `{DELIVERABLE_PATH}/Guidance.md`
- `{DELIVERABLE_PATH}/Procedure.md` (this document)
- `{DELIVERABLE_PATH}/_STATUS.md` (updated only when safe per Step 8)
- `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md`
- Guidance Conflict Table entries for: F-3500-1 design flow (CONF-001), suction temperature envelope (CONF-002), recycle valve fail position (CONF-003), inaccessible Word/Excel sources for interface scope (CONF-004).
