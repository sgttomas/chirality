# Procedure — DEL-070-02 Package Datasheet (Mole Sieve Drier Unit, NGL)

This Procedure describes how to **produce** and maintain the Package Datasheet artifact for PKG-070. Operational procedures for the physical NGL mole-sieve unit (start-up, regeneration cycling, change-out) belong to vendor operating manuals and to DEL-070-03 (Construction Work Package) / DEL-070-06 (EPC Vendor Package Review and Acceptance); they are out of scope here.

## Prerequisites

### Upstream inputs (declared)

- `_DEPENDENCIES.md` declares no upstream dependencies as of PREPARATION. Production of this Package Datasheet currently relies on:
  - the accepted GATE-07 PROJECT_DECOMP snapshot,
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` in this deliverable folder,
  - source slice `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Current-Scope NGL Molecular-Sieve Dehydration.

### Source access

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` must be locally accessible.
- `_Sources/26020-Package_Requirements.docx` heading 24 and `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 74 — preferred but not text-accessible at present; carry as `location TBD` until extracted.

### Tooling

- Markdown editor with table support.
- (Optional) `tools/scaffolding/write_status.sh` for `_STATUS.md` safe updates.

## Steps

### Step 1 — Read context

1. Read `_CONTEXT.md` to confirm DeliverableID, ParentPackageID, scope items (SOW-0145..SOW-0148), and the package interface-evidence intent (`Notes`).
2. Read `_REFERENCES.md` to identify reference materials.
3. Read `_DEPENDENCIES.md` (declared upstream/downstream).
4. Locate the deliverable row in `DELIVERABLE_REGISTER.csv` to confirm the descriptive narrative and anticipated artifacts.

### Step 2 — Read accessible source slices

1. Read DBM-Deepcut §Current-Scope NGL Molecular-Sieve Dehydration (lines 1574-1623).
2. Read DBM-Deepcut §Sales-Gas and NGL Treating Overview (lines 1400-1410) for service framing.
3. Cross-reference DBM-Deepcut §Molecular-Sieve Dehydration and Mercury Removal Basis (lines 1239-1296) ONLY to keep the **process-gas** vs. **NGL** systems distinct; do not transfer process-gas values into the NGL Package Datasheet.

### Step 3 — Populate `Datasheet.md`

1. Identification: from `_CONTEXT.md`.
2. Attributes / Conditions / Construction: copy values from the DBM source slice tables verbatim with units and a per-row source citation (file + line range or section). Use `TBD` when the source slice does not contain a value; use `TBC` exactly when the source uses `TBC`.
3. Interfaces: enumerate every interface present in the source slice with counterparty and service identified.
4. References: cite source files plus inaccessible references explicitly.

### Step 4 — Populate `Specification.md`

1. State scope and exclusions consistent with `_CONTEXT.md` and PKG-070 sibling deliverables.
2. Translate each material design fact in `Datasheet.md` into a numbered requirement (R-N) on the Package Datasheet's content; do not write requirements on the physical equipment except where the DBM states them.
3. Mark each requirement with its source citation.
4. Carry `location TBD` for standards/codes whose text is not currently accessible.

### Step 5 — Populate `Guidance.md`

1. Explain purpose and principles, grounded in the source slice and `_CONTEXT.md` Notes.
2. Surface trade-offs the DBM explicitly raises (sparing, regeneration isolation, outlet filter type, winter cooler operation).
3. Open or update the Conflict Table for any internal inconsistency in the source slice (e.g., the three-way water-content framing) and for any inaccessible-source citations.

### Step 6 — Populate `Procedure.md` (this file)

1. State the procedure to produce and maintain the Package Datasheet.
2. Include the verification checks below.
3. Note operational concerns for the physical unit only insofar as the source slice already states them; defer detailed operating procedures to DEL-070-03/06 and vendor manuals.

### Step 7 — Cross-document consistency sweep

1. Verify identification fields are identical across all four documents.
2. Verify numeric values (throughput, pressures, temperatures, water content, pressure drops) match across `Datasheet.md` and `Specification.md`.
3. Verify each requirement R-N in `Specification.md` is traceable to a row in `Datasheet.md` and to the source citation.
4. Verify every TBC/TBR/TBD marker in the source slice is reproduced.
5. Verify the Conflict Table covers every unresolved internal contradiction or inaccessible source.

### Step 8 — Safe status update

- If `_STATUS.md` Current State is `OPEN`, update it to `INITIALIZED` using `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` (or by direct edit when scripts are unavailable, preserving the History log).
- Do not regress state.

## Verification

| Check | Pass condition |
|---|---|
| All four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present in `{DELIVERABLE_PATH}`. |
| Default schema sections | Datasheet has Identification, Attributes, Conditions, Construction, References. Specification has Scope, Requirements, Standards, Verification, Documentation. Guidance has Purpose, Principles, Considerations, Trade-offs, Examples. Procedure has Purpose (implicit in intro), Prerequisites, Steps, Verification, Records. |
| Source-grounding | Every non-trivial value in `Datasheet.md` has a source citation; inferred values are labeled `ASSUMPTION`; missing values are `TBD`. |
| Cross-document consistency | Identifiers, numeric values, and interface descriptions agree across documents. |
| TBC preservation | Every TBC/TBR marker from DBM-Deepcut §1574-1623 appears in the Package Datasheet. |
| Conflict table | Internal inconsistencies and inaccessible-source items are entered in `Guidance.md` Conflict Table. |
| `_STATUS.md` discipline | Updated only on safe `OPEN → INITIALIZED` transition; no regression. |

## Records

- Run record: `_run_records/TASK_RUN_<timestamp>.md` (this run plus any subsequent runs of the four-documents skill).
- Conflict Table entries in `Guidance.md` (CONF-070-02-001, -002, -003 as of this run).
- Source citations embedded within `Datasheet.md` and `Specification.md`.
- Status history in `_STATUS.md`.
