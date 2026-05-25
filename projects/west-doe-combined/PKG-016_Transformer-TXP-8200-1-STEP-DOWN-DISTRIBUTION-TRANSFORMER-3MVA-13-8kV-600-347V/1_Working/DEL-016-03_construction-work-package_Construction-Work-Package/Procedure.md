# Procedure: DEL-016-03 — Construction Work Package (Transformer TXP-8200-1)

This Procedure describes how to **produce** the PKG-016 Construction Work Package (CWP) deliverable. (Operation of the transformer itself is out of scope; commissioning/operation belongs to subsequent EPC and facility deliverables.)

## Prerequisites

| Item | Status / Source |
|---|---|
| `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` initialized | Present (PREPARATION) |
| DBM electrical and civil basis | DBM SEC-02, SEC-11, SEC-12 (`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) |
| PKG-016 Scope of Work (`DEL-016-01`) | Concurrent or upstream deliverable |
| PKG-016 Package Datasheet (`DEL-016-02`) | Concurrent or upstream deliverable |
| Vendor Engineered Equipment Package (`DEL-016-04`) | May be in progress; CWP references vendor data when available |
| Detailed Electrical Construction Specification | Not locally accessible — referenced as `location TBD` |
| Final geotechnical report | Not locally accessible — required for foundation design closure (DBM SEC-11) |
| Hazardous-area classification drawings | Not locally accessible — referenced as `location TBD` |

## Steps

### Step 1 — Establish CWP scope baseline
1. Read `_CONTEXT.md` and confirm DEL-016-03 identity, scope, anticipated artifacts, scope items (`SOW-0017`), and supported objectives.
2. Read `_REFERENCES.md` and load the accessible DBM source slices (SEC-02, SEC-11, SEC-12).
3. Read the PACKAGE_REGISTER.csv row 18 and DELIVERABLE_REGISTER.csv rows 78-83 (all PKG-016 deliverables) to establish adjacent scope boundaries.

### Step 2 — Capture transformer identity and installation envelope
1. Populate the Datasheet identification and attributes from the DBM electrical basis.
2. Record ambient/site conditions from DBM SEC-02.
3. Record area classification basis from DBM SEC-11.
4. Mark indoor/outdoor as `TBD` until detailed design confirms.

### Step 3 — Define construction scope items
1. List EPC construction-scope items from DBM SEC-01 "Construction Scope Summary" applicable to a transformer install (foundation/pile, module setting, terminations, raceway, grounding tie-in, heat tracing/winterization where applicable).
2. Confirm boundary against vendor scope: vendor delivers the transformer; EPC sets, terminates, ties in, tests, and turns over.

### Step 4 — Define tie-ins
1. Enumerate primary feeder tie-in (from 04-25 13.8 kV Main Switchgear).
2. Enumerate secondary feeder tie-in (to 600 V MCC lineup, MCC-8200).
3. Enumerate grounding tie-in (to facility ground grid).
4. Enumerate building/HVAC tie-ins if indoor installation is confirmed.
5. Record each tie-in for inclusion in the project tie-in register.

### Step 5 — Draft installation and tie-in workface plan
1. Sequence: foundation → equipment setting → primary cable pull/terminate → secondary cable pull/terminate → grounding → segregation walkdown → pre-energization tests → punch list → turnover.
2. Identify hold points (pre-pour inspection, anchor-bolt as-built, grout cure, cable termination QC, grounding test, pre-energization checks).
3. Identify interface meetings with the 04-25 switchgear scope and the 600 V MCC scope.

### Step 6 — Draft construction interface and turnover checklist
1. List required test records (continuity, IR/megger, TTR, polarity, oil quality where applicable, grounding resistance).
2. List required as-built deliverables (redlined drawings, cable schedule updates, raceway updates, ground-grid updates).
3. Define punch-list categorization (A: blocks turnover; B: complete before commissioning; C: complete during operations).
4. Define signature authorities and acceptance criteria for transfer to commissioning.

### Step 7 — Cross-document consistency sweep
1. Verify the Datasheet, Specification, and Guidance documents in this deliverable use the same tag (TXP-8200-1), ratings (3 MVA, 13.8 kV / 600 V), and grounding basis (HRG, 5 A continuous resistor at 600 V).
2. Verify each Specification requirement (R-CWP-01 through R-CWP-12) has a corresponding verification entry.
3. Verify each anticipated artifact in `_CONTEXT.md` is reflected in Specification Documentation.

### Step 8 — Record open items
1. List `TBD` items and ASSUMPTIONs.
2. Add or refresh Conflict Table entries in `Guidance.md` for unresolved source disagreements.
3. Surface dependency-chain issues (e.g., detailed-design inputs, geotechnical report) in the run record under "Needs Human Ruling" or "Dependency Notes" as appropriate.

## Verification

| Check | Pass Criterion |
|---|---|
| Identity consistency | TXP-8200-1, PKG-016, DEL-016-03 used consistently in all four documents |
| Rating consistency | 3 MVA, 13.8 kV / 600 V used consistently |
| Grounding consistency | 600 V HRG with 5 A continuous resistor stated identically |
| Scope-boundary consistency | EPC integration vs vendor scope split stated identically in Datasheet, Specification, and Guidance |
| Source citation | Non-trivial values cite DBM section or workbook row; ASSUMPTIONs and TBDs labeled |
| Anticipated artifacts coverage | Each anticipated artifact appears in Specification Documentation |
| Requirements → verification | Each R-CWP-* has a Verification Method entry |
| Tie-in coverage | Primary, secondary, grounding, and building-services (conditional) tie-ins each enumerated |

## Records

The following evidence and records should result from executing this Procedure (and from the eventual IFC-stage CWP that this deliverable seeds):

- This four-document set (Datasheet, Specification, Guidance, Procedure) under DEL-016-03.
- Construction Work Package document at IFC issue.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Tie-in register entries for primary feeder, secondary feeder, grounding, and conditional building services.
- Pre-energization test record set.
- As-built redlines and updated cable/raceway/ground-grid schedules.
- Signed construction turnover certificate (transfer to commissioning).
- Updated `_STATUS.md` reflecting deliverable state transitions per the project lifecycle.
