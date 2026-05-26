# Procedure — DEL-083-02 Package Datasheet (PKG-083 Inlet Separators 3-25)

Status: INITIALIZED (P1_P2 draft). Operational steps to produce the EPC-issued Package Datasheet for PKG-083 and to verify it before handoff to the Package Vendor.

Interpretation: This procedure describes producing the Package Datasheet artifact (the EPC handoff to the Package Vendor), not operating the equipment.

## Prerequisites

- Read and current: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, this kit's Datasheet.md, Specification.md, and Guidance.md.
- Locally accessible: DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (SEC-02, SEC-03, SEC-04, SEC-05). Source: `_REFERENCES.md` "Shared Source Root".
- Required upstream snapshot: Gate-07 PROJECT_DECOMP snapshot (DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, INTERFACE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv). Source: `_REFERENCES.md`.
- Binary source artifacts that should be made text-accessible (TBD): 26020-Package_Requirements.docx (heading 36), 26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx.
- Declared dependencies: `_DEPENDENCIES.md` declares none; treat DEL-083-01 (Scope of Work) as the implicit scope envelope by package convention (ASSUMPTION).

## Steps

### Step 1 — Confirm package identity and source basis

1. Pull PKG-083 row from PACKAGE_REGISTER.csv (Gate-07 snapshot) and confirm name, WBS, discipline, equipment tag, source-basis pointers.
2. Pull DEL-083-02 row from DELIVERABLE_REGISTER.csv and confirm scope items (SOW-0123..SOW-0126) and supported objectives.
3. Record verification in the run record.

### Step 2 — Populate Identification (Datasheet.md "Identification")

1. Transcribe identity fields from `_CONTEXT.md` Identity table.
2. Cite the source documents (DBM SEC-04; PACKAGE_REGISTER row 67; 26020-Package_Requirements.docx heading 36).

### Step 3 — Populate Per-Separator Design Basis

1. Re-read DBM SEC-04 "Inlet Separation" design table (lines 246-256).
2. Transcribe each row verbatim into Datasheet.md "Per-Separator Process Design Basis"; do not synthesize values.
3. Where the source uses dual units (SI / imperial), retain both.

### Step 4 — Populate Operating Conditions

1. Re-read DBM SEC-04 line 258 (low/design/maximum/normal-high operating pressures and inlet design temperature).
2. Re-read DBM SEC-04 line 230 for inlet ESDV shutdown pressure (635 psig).
3. Mark unstated values TBC (normal-high) and TBD (delivery-point ESDV shutdown).
4. Capture the inlet-temperature reconciliation in Guidance.md Conflict Table (CF-01).

### Step 5 — Populate Internals, Control, and Building

1. Re-read DBM SEC-04 line 260 for internals and coating; transcribe.
2. Re-read DBM SEC-04 "Flow Distribution and Controls" for the parallel-CV and dP-limit requirements; transcribe to Specification.md R-5.
3. Note heated-building extent as TBD.

### Step 6 — Populate Interfaces

1. Pull all rows from INTERFACE_REGISTER.csv where PackageID = PKG-083 (11 rows expected).
2. Transcribe IFC-IDs and types into Datasheet.md "Package Interfaces" table.
3. For each interface type, defer clause-level requirements to TBD pending EPC interface specification.

### Step 7 — Identify Standards (with explicit ASSUMPTION labels)

1. Where the DBM source slice names a standard (e.g., CSA Z662 for sour-gas export pipeline), record it with its source citation.
2. Where a standard is conventional but not explicit in the accessible source (ASME VIII, NACE MR0175, ASME B16.5), record it under Specification.md "Standards" with ASSUMPTION and a TBD location.

### Step 8 — Cross-document consistency sweep (Pass 2)

1. Datasheet ↔ Specification: confirm every Datasheet design value appears as a normative requirement in Specification or is explicitly contextual.
2. Specification ↔ Guidance: confirm every requirement has a rationale or principle backing in Guidance, or is purely tabular.
3. Specification ↔ Procedure: confirm every requirement has a verification hook here in Step 9.
4. Terminology: confirm "inlet separator", "horizontal three-phase separator", "Devchem 253", and tag identifiers V-1600-2 / V-1700-2 are used consistently.
5. Numeric units: confirm SI-imperial pairs match exactly across all four documents.

### Step 9 — Verification gates (before handoff)

| Gate | Check | Pass criterion |
|---|---|---|
| G-1 | All Datasheet "Per-Separator Process Design Basis" rows trace to DBM SEC-04 | 100% citation coverage |
| G-2 | All eleven PKG-083 interface rows from INTERFACE_REGISTER.csv appear in Datasheet | 11/11 present |
| G-3 | All TBDs and ASSUMPTIONs are explicit and traceable | No silent inference |
| G-4 | Conflict Table contains CF-01 (inlet temperature) and CF-02 (binary source extraction) | Both present |
| G-5 | `_STATUS.md` transitioned OPEN -> INITIALIZED only on successful Pass 1/2 | Transition logged |

### Step 10 — Status update and run record

1. Update `_STATUS.md` OPEN -> INITIALIZED with provenance "TASK+four-documents". Source: skill Step 7.
2. Write the run record under `_run_records/TASK_RUN_<timestamp>.md` capturing tools used (none), outputs produced, missing items, and any rulings needed.

## Verification

- Verify Datasheet, Specification, Guidance, Procedure all exist in `{DELIVERABLE_PATH}` after run.
- Verify default schema sections are present in each (Datasheet: Identification/Attributes/Conditions/Construction/References; Specification: Scope/Requirements/Standards/Verification/Documentation; Guidance: Purpose/Principles/Considerations/Trade-offs/Examples; Procedure: Purpose/Prerequisites/Steps/Verification/Records).
- Verify `_STATUS.md` shows INITIALIZED and history entry.
- Verify run record contains all required YAML frontmatter and body headings.

## Records

- `{DELIVERABLE_PATH}/Datasheet.md`
- `{DELIVERABLE_PATH}/Specification.md`
- `{DELIVERABLE_PATH}/Guidance.md`
- `{DELIVERABLE_PATH}/Procedure.md`
- `{DELIVERABLE_PATH}/_STATUS.md` (updated)
- `{DELIVERABLE_PATH}/_run_records/TASK_RUN_2026-05-24_2348.md`
