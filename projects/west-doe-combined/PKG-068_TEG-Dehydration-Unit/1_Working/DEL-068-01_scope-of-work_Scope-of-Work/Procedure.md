# Procedure — DEL-068-01 Scope of Work (PKG-068 TEG Dehydration Unit)

**Interpretation:** This procedure describes the operational steps to **produce** the EPC Scope of Work artifact for PKG-068 (not to operate the TEG unit). Operation of the TEG unit is a vendor/operations concern outside this deliverable.

## Prerequisites

1. Read the deliverable-local truth set:
   - `_CONTEXT.md` (identity, scope, anticipated artifacts)
   - `_STATUS.md` (current lifecycle state; must allow overwrite per skill policy)
   - `_REFERENCES.md` (authoritative basis)
   - `_DEPENDENCIES.md` (declared upstream/downstream — currently none declared)
   - `_SEMANTIC.md` (placeholder; informational only)
2. Read decomposition source rows from `GATE-07_Final_Published_2026-05-24`:
   - `DELIVERABLE_REGISTER.csv` row `DEL-068-01_scope-of-work`
   - `PACKAGE_REGISTER.csv` row `PKG-068`
   - `OBJECTIVE_DELIVERABLE_MAP.csv` rows where `DeliverableID = DEL-068-01_scope-of-work`
3. Read the locally accessible authoritative source slice:
   - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-06 "Process-Gas TEG Dehydration Basis" (lines 1187–1237).
4. Confirm declared upstream dependencies: none declared in `_DEPENDENCIES.md` at PREPARATION. (See `_DEPENDENCIES.md` Declared Upstream Dependencies.)
5. Note locally missing references and treat content depending solely on them as `TBD`:
   - `26020-Package_Requirements.docx` package heading 23 (binary; not directly readable)
   - `Bid Docs/Budgetary/26020-01-PT-RFQ-22-001_TEG Dehy Unit.docx` (not present under `_Sources/`)

## Steps

### Step 1 — Establish package identity

1. Populate Datasheet `Identification` and Specification `R-068-01-01` from `PACKAGE_REGISTER.csv` row PKG-068.
2. Record Workbook row 97, package tag 26020-01-22-001, source identifier 26020-01-PT-22-001, discipline Mechanical, WBS 01.

### Step 2 — Enumerate tagged equipment

1. Copy the 13-item equipment list verbatim from `PACKAGE_REGISTER.csv` row PKG-068 scope statement into Datasheet `Attributes — Package Identity and Tagged Equipment` and Specification `R-068-01-02`.
2. For each item, cross-reference DBM SEC-06 (l.1216–1234) where the item is named in the design basis; leave the tag-number column as `TBD` (vendor-assigned in DEL-068-02).

### Step 3 — Capture process design envelope (framing only)

1. Lift the design-value table from DBM SEC-06 (l.1199–1214) into Datasheet `Conditions`.
2. Mark the operating-pressure conflict (1100 vs. 1085 psig) and add to the Conflict Table in `Guidance.md` (CFL-068-01-01).
3. Do not derive new design values; values not present in DBM remain `TBD` pending DEL-068-02.

### Step 4 — Define responsibility split

1. Populate Specification `R-068-01-04` (Package Vendor) and `R-068-01-05` (EPC Integrator) from `PACKAGE_REGISTER.csv` row PKG-068 description.
2. Enumerate the 13 applicable interface types from `PACKAGE_REGISTER.csv` row PKG-068 `interfaces` column into Specification `R-068-01-06` and Datasheet `Construction`.

### Step 5 — Draft integration narrative

1. Compose Specification `R-068-01-07` from DBM SEC-06 process description (l.1187–1193) plus SEC-04 SOC interfaces (l.842).
2. Acknowledge the upstream inlet/TEG cross-exchanger warm-side open item (Conflict Table CFL-068-01-03) without resolving it here.

### Step 6 — Record source basis, coverage, and objective traceability

1. Populate Specification `R-068-01-08` source-basis section; mark RFQ and Word slice as `location TBD`.
2. Populate Specification `R-068-01-09` with SOW items SOW-0237, SOW-0238, SOW-0239, SOW-0240 (from `_CONTEXT.md`).
3. Populate Specification `R-068-01-10` with OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (from `OBJECTIVE_DELIVERABLE_MAP.csv`).

### Step 7 — Capture exclusions and conflicts

1. Populate Specification `R-068-01-11` exclusions section as `TBD` (per `PACKAGE_REGISTER.csv` row PKG-068).
2. Confirm the Conflict Table in `Guidance.md` lists each open item with a `TBD` human ruling column.

### Step 8 — Cross-document consistency sweep

1. Verify that Datasheet equipment list, Specification `R-068-01-02`, and Procedure Step 2 reference the same 13 items in the same order.
2. Verify that interface lists are identical across Datasheet, Specification, and DBM-derived source.
3. Verify that objective IDs match across Datasheet, Specification, and `OBJECTIVE_DELIVERABLE_MAP.csv` rows.
4. Verify that all `TBD` and `ASSUMPTION` labels carry source pointers or explicit "location TBD" markers.

### Step 9 — Safe status update

1. Re-read `_STATUS.md`.
2. If `Current State = OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.
3. If `Current State` is not `OPEN`, do not modify `_STATUS.md`; record the skip in the run record.

## Verification

| Verification check | Pass criterion | Evidence target |
|---|---|---|
| V-01 Equipment list completeness | 13 items present, matching PACKAGE_REGISTER row PKG-068 verbatim | Datasheet `Attributes`; Specification `R-068-01-02` |
| V-02 Responsibility split | Vendor vs. EPC scopes match PACKAGE_REGISTER row PKG-068 description | Specification `R-068-01-04`, `R-068-01-05` |
| V-03 Interface coverage | All 13 interface types declared | Specification `R-068-01-06` |
| V-04 Objective trace | All 9 OBJ IDs match OBJECTIVE_DELIVERABLE_MAP rows | Specification `R-068-01-10` |
| V-05 Source citations | Each non-trivial claim cites a source slice or marks `location TBD` | All four docs |
| V-06 Conflict capture | Open items recorded with `TBD` ruling | `Guidance.md` Conflict Table |
| V-07 Status discipline | `_STATUS.md` modified only via safe update path | `_STATUS.md`; run record |
| V-08 Cross-doc consistency | Terms, values, and IDs consistent across Datasheet/Spec/Guidance/Procedure | All four docs |

## Records

The following records result from executing this procedure:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`
- Safe `_STATUS.md` update (`OPEN -> INITIALIZED`) when applicable
- Run record at `_run_records/TASK_RUN_<timestamp>.md`
- Conflict Table entries (in `Guidance.md`) flagged for human ruling
- Open-source register entries (in `Guidance.md` "TBD / Missing References Register")
