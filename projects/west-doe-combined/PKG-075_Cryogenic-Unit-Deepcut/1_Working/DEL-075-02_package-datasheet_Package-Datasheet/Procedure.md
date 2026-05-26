# Package Datasheet — Procedure — PKG-075 Cryogenic Unit ("Deepcut")

DeliverableID: DEL-075-02_package-datasheet
DecompositionRef: GATE-07_Final_Published_2026-05-24

## Purpose

This procedure describes the operational steps required to **produce** the PKG-075 Package Datasheet deliverable (i.e., to author, review, and issue the Datasheet + supporting documentation for Package Vendor handoff). The use/operate interpretation (running the cryogenic unit) is governed by the Vendor's operating manuals, the facility OMS, and the DBM SEC-06 protective-function basis; it is not duplicated here.

## Prerequisites

- Accepted decomposition snapshot: GATE-07_Final_Published_2026-05-24 (PROJECT_DECOMP).
- DEL-075-02 deliverable-local truth set complete and in INITIALIZED or later state: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Locally accessible authoritative source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-01, SEC-02, SEC-05, SEC-06, SEC-07).
- Decomposition registers available under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`: `PACKAGE_REGISTER.csv` (PKG-075), `DELIVERABLE_REGISTER.csv` (DEL-075-02), `INTERFACE_REGISTER.csv` (PKG-075), `OBJECTIVE_DELIVERABLE_MAP.csv`.
- 26020-Package_Requirements.docx (heading 29) and 26020-Packages_Interfaces_4_export.xlsx located in `_Sources/` (currently binary; require parsed-text equivalents before final issue — see Step 5).
- EPC Integrator point of contact for interface coordination identified.

## Steps

### Step 1 — Identify Datasheet content authority

1.1 Read `_CONTEXT.md` and confirm DeliverableID, package tag (26020-01-PT-28-001), discipline (Mechanical), and EPC-vs-Vendor responsibility split.
1.2 Read the PKG-075 row of `PACKAGE_REGISTER.csv` and the DEL-075-02 row of `DELIVERABLE_REGISTER.csv` to confirm anticipated artifacts and covered SOW items (SOW-0063…SOW-0066).
1.3 Read `_REFERENCES.md` and load DBM SEC-01, SEC-02, SEC-05, SEC-06, SEC-07 source slices.

### Step 2 — Extract design basis

2.1 Extract from DBM SEC-06 "UltraTEF Cryogenic Recovery Basis" the design values, equipment list, operating modes, and open-items table.
2.2 Extract from DBM SEC-02 the site environmental loads.
2.3 Extract from DBM SEC-05 / SEC-07 only the values that condition cryogenic interfaces (sales-gas sulphur strategy; sales pressure expectations).
2.4 Extract from `INTERFACE_REGISTER.csv` the 12 declared interface types for PKG-075.

### Step 3 — Draft Datasheet, Specification, Guidance

3.1 Populate `Datasheet.md` Identification, Attributes, Conditions, Construction, Interfaces, References sections from Step 2 with explicit source citation per row.
3.2 Populate `Specification.md` requirements R1…R10 with source citations (`SourcePath` + `SectionRef`).
3.3 Populate `Guidance.md` Purpose, Principles, Considerations, Trade-offs, Examples.
3.4 For every value or requirement not present in an accessible source slice, mark `TBD` or label `ASSUMPTION:` and add a Conflict Table row in `Guidance.md` when sources disagree.

### Step 4 — Cross-document consistency sweep

4.1 Verify Datasheet entries are reflected in Specification requirements where appropriate (R1.x ↔ Datasheet recovery; R3.x ↔ Datasheet BAHX row; R4.x ↔ turbo-expander/utilities rows; etc.).
4.2 Verify each Specification requirement has a verification approach in Specification "Verification".
4.3 Verify terminology is consistent across all four documents (BAHX, J-T, expander mode, deethanizer, methanol injection).
4.4 Verify numeric values and units are consistent across documents.
4.5 Where conflicts cannot be resolved from drafts alone, re-open the DBM source slice; if still unresolvable, prefer `TBD` and capture in the Conflict Table.

### Step 5 — Vendor handoff reconciliation (pre-issue)

5.1 Obtain parsed-text equivalents of 26020-Package_Requirements.docx (package heading 29) and 26020-Packages_Interfaces_4_export.xlsx; reconcile against Datasheet and Specification. Update `location TBD` markers to specific `SourcePath` + `SectionRef`.
5.2 Resolve the Conflict Table entries that block vendor issue (minimum: CT-01 deethanizer bottoms spec; CT-02 LACT scope clarity for interface boundaries; CT-03 26020 docx requirements list).
5.3 Confirm the package interface requirements matrix is consistent with `INTERFACE_REGISTER.csv` and with the EPC Integrator's interface workbook.

### Step 6 — Status update

6.1 Run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` only when current state is `OPEN`. Skip if not.

### Step 7 — Run record

7.1 Persist run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_{YYYY-MM-DD}_{HHmm}.md` with YAML frontmatter (PENDING → final), all required headings, applied changes, and deliverable-local closeout.

## Verification

| Check | Pass criterion |
|---|---|
| Four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all present under `{DELIVERABLE_PATH}`. |
| Default schema sections present | Datasheet (Identification, Attributes, Conditions, Construction, References); Specification (Scope, Requirements, Standards, Verification, Documentation); Guidance (Purpose, Principles, Considerations, Trade-offs, Examples); Procedure (Purpose, Prerequisites, Steps, Verification, Records). |
| At least one locally accessible source read | DBM SEC-01/02/05/06/07 cited explicitly. |
| Non-trivial values cite sources | Each numeric or normative value carries `SourcePath` + `SectionRef` or `location TBD`. |
| Inferences labeled | `ASSUMPTION:` markers carried where values are inferred (e.g., deethanizer bottoms spec typo reading). |
| Cross-document consistency | Terminology and values reconciled or captured in Conflict Table. |
| `_STATUS.md` safe update | OPEN → INITIALIZED only when state is OPEN; no regression. |
| Run record complete | YAML frontmatter complete; all body headings present; PENDING flipped to final at close. |

## Records

- `{DELIVERABLE_PATH}/Datasheet.md` — package datasheet content set.
- `{DELIVERABLE_PATH}/Specification.md` — normative requirements with verification map.
- `{DELIVERABLE_PATH}/Guidance.md` — purpose, principles, considerations, trade-offs, conflict table.
- `{DELIVERABLE_PATH}/Procedure.md` — this file.
- `{DELIVERABLE_PATH}/_STATUS.md` — lifecycle state (post-run: INITIALIZED).
- `{DELIVERABLE_PATH}/_run_records/TASK_RUN_2026-05-24_2336.md` — durable run record for this invocation.
- Future: 26020-Package_Requirements.docx parsed-text equivalent and 26020-Packages_Interfaces_4_export.xlsx-derived interface matrix (pre-issue prerequisites).
