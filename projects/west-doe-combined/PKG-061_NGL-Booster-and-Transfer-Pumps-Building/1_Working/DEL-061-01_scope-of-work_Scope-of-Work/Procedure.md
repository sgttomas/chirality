# Procedure — DEL-061-01 Scope of Work (PKG-061 NGL Booster and Transfer Pumps Building)

This Procedure describes the steps the EPC Integrator follows to produce, issue, and maintain the Scope of Work artifact for PKG-061. (Operation of the pumps is governed by the Vendor O&M turnover package, DEL-061-05, and is not in scope here.)

## Purpose

Produce a source-grounded, single-version EPC Integrator Scope of Work that fully defines the PKG-061 package boundary, function, equipment, exclusions, and responsibility assignment, and that anchors the downstream Gate-5 deliverables (DEL-061-02 through DEL-061-06).

## Prerequisites

- Read access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, OBJECTIVE_SCOPE_MAP.csv).
- Read access to source slice: 26020-Package_Requirements.docx heading 17 (Basic scope, Major included equipment, Scope notes and open items) — currently captured verbatim in SCOPE_LEDGER.csv rows SOW-0149..SOW-0152.
- Read access to DBM-Deepcut/4-25_Deepcut_DBM.md for downstream/upstream interface basis (NGL storage, NGL C3+ product disposition, LACT scope status).
- `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` for this deliverable.
- No declared upstream deliverable dependencies (per `_DEPENDENCIES.md`).

## Steps

### Step 1 — Establish package identity

1. Confirm DeliverableID, ParentPackageID, PackageName, Discipline, Type, and ResponsibleParty from `_CONTEXT.md` and DELIVERABLE_REGISTER.csv.
2. Record covered scope items (SOW-0149..SOW-0152) and supported objectives (OBJ-001, OBJ-003..OBJ-010) in the Datasheet identification block.

### Step 2 — Capture authoritative source slice

1. Open SCOPE_LEDGER.csv rows SOW-0149, SOW-0150, SOW-0151, SOW-0152. These rows contain heading 17 text verbatim (Basic scope; Major included equipment; Scope notes and open items).
2. Cross-check the tagged-equipment row in DBM-Deepcut/4-25_Deepcut_DBM.md (line 2609) for package type, count, tags, and API 610 multi-stage can characterization.
3. Capture identity-relevant DBM-Deepcut interface text: NGL product disposition (lines 57, 446), NGL storage basis (line 448), LACT status (lines 62, 82).

### Step 3 — Populate the Datasheet

1. Identification, attributes, conditions, construction-included, construction-excluded, and references sections per the captured source slice (Datasheet.md).
2. For each entry, record source pointer (SOW-### or DBM-Deepcut line).
3. Mark missing values (TDH, NPSHA, suction conditions) as TBD and list them in the TBD section.

### Step 4 — Draft the Specification

1. Write Scope (in/out) reflecting EPC Integrator authority and package boundary.
2. Write requirements R-1 through R-13 such that every requirement carries an inline source citation.
3. Populate the Standards table with explicit references (API 610, API 682, CRN, TSBC) and label unconfirmed standards as ASSUMPTION or location TBD.
4. Map each requirement to a verification approach in the Verification table.
5. List the four anticipated artifacts (per DELIVERABLE_REGISTER.csv) in the Documentation section and cross-reference downstream deliverables DEL-061-02..06.

### Step 5 — Draft the Guidance

1. State the purpose, principles, considerations, trade-offs, and examples grounded in source slice and DBM-Deepcut analogues.
2. Open the Conflict Table for items requiring human ruling:
   - LPG vs NGL nomenclature (CT-061-01-01)
   - LACT inclusion/exclusion at facility level (CT-061-01-02)
   - "145 m3/h at 150% capacity" reading (CT-061-01-03)
   - Motor voltage 575 V vs facility MV/LV basis (CT-061-01-04)

### Step 6 — Cross-document consistency sweep (Pass 2)

1. Verify Datasheet attributes (tags, flow, differential, voltage, seal plan, exclusions) match Specification requirements R-2..R-9 and R-11..R-12.
2. Verify each Specification standard appears consistently in Guidance principles and Datasheet references.
3. Verify Conflict Table entries are reflected as ASSUMPTION or TBD in the affected Datasheet/Specification rows.
4. Confirm terminology: package referred to as "NGL Booster and Transfer Pumps Building" everywhere; "LPG" appears only when quoting heading 17.

### Step 7 — Update `_STATUS.md` (safe transition)

1. Read current state from `_STATUS.md`.
2. If state is `OPEN`, transition to `INITIALIZED` via `tools/scaffolding/write_status.sh` with reason `TASK+four-documents`.
3. If state is anything other than `OPEN`, do not modify `_STATUS.md` and record the skip in the run record.

### Step 8 — Write the run record

1. Create `_run_records/TASK_RUN_<timestamp>.md` capturing input echo, resolved skill state, tools used, outputs, missing items, dependency notes, and applied changes.

## Verification

| Check | Pass criterion |
|---|---|
| All four documents present | Datasheet.md, Specification.md, Guidance.md, Procedure.md exist in deliverable folder |
| Default schema sections present | Identification/Attributes/Conditions/Construction/References (Datasheet); Scope/Requirements/Standards/Verification/Documentation (Specification); Purpose/Principles/Considerations/Trade-offs/Examples (Guidance); Purpose/Prerequisites/Steps/Verification/Records (Procedure) |
| Tagged equipment consistent | P-9570-1 and P-9580-1 in Datasheet, Specification R-2, and Guidance examples |
| Source citation on substantive claims | Every value/requirement cites SOW-### or DBM-Deepcut line; missing values labeled TBD; inferences labeled ASSUMPTION |
| Conflict Table coverage | All identified conflicts captured with proposed authority and TBD ruling |
| `_STATUS.md` safe update | Updated OPEN -> INITIALIZED only; no regression |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md` (this file)
- `_STATUS.md` (transitioned OPEN -> INITIALIZED)
- `_run_records/TASK_RUN_2026-05-25_0435.md`
