# Procedure — DEL-065-02 Package Datasheet (PKG-065 Tanks, Caustic (API 650) 4-25)

## Purpose

Operational procedure to **produce, review, and issue** the Package Datasheet for PKG-065 (Caustic Tanks). This procedure governs the production of the deliverable artifact, not the operation of the physical caustic tanks (operating procedures are downstream).

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in the deliverable folder. (CONFIRMED for this run.)
- Accepted upstream decomposition snapshot available at GATE-07 (CONFIRMED via `_REFERENCES.md`).
- Locally accessible source materials read:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (CONFIRMED — used for caustic-tank attributes, conditions, materials, vapour-space discipline, and plant spacing).
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` heading 20 (NOT locally readable — binary; `location TBD`).
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` (NOT locally readable — binary; interface matrix deferred).
- No declared upstream dependencies (per `_DEPENDENCIES.md`).
- `_STATUS.md` `Current State` in `ALLOW_OVERWRITE_STATES` (OPEN, INITIALIZED). (CONFIRMED OPEN for this run.)

## Steps

### Step 1 — Establish DOMAIN and TASK
1.1 Read `_CONTEXT.md`. Confirm discipline (Mechanical), type (EPC Package Datasheet), responsible party (EPC Integrator), and package name ("Tanks, Caustic (API 650) 4-25").
1.2 Read the deliverable row in the GATE-07 `DELIVERABLE_REGISTER.csv` and confirm anticipated artifacts and objective coverage from `OBJECTIVE_DELIVERABLE_MAP.csv` (FACT: OBJ-001, OBJ-003 through OBJ-010 explicitly listed for DEL-065-02).
1.3 Read `_REFERENCES.md` and identify locally accessible source materials.

### Step 2 — Read Authoritative Source Slices
2.1 Read all DBM sections naming "caustic", "tank", "API 650", and "atmospheric tank": specifically §"NGL Mercaptan Treating Unit" (lines 1511-1566), §"Disulphide Oil, Spent Caustic, and Waste Amine" (lines 526-532), §"Atmospheric Tank and General Plant Spacing" (lines 261-298), and the SOC interface mentions of pressurized caustic drain drum.
2.2 Record source-supported facts directly (with line citation). Where a value is TBC in the DBM, propagate as TBD.
2.3 Mark every value or requirement that would otherwise rely on `26020-Package_Requirements.docx` heading 20 or `26020-Packages_Interfaces_4_export.xlsx` as `location TBD` until a text-readable extract is produced (out of scope for this deliverable).

### Step 3 — Draft Datasheet.md
3.1 Populate Identification from `_CONTEXT.md`.
3.2 Populate Attributes (equipment roster: fresh and spent caustic tanks) from DBM §MTU.
3.3 Populate Conditions (service, SG, temperature, vapour-space, spacing basis) from DBM with explicit citations.
3.4 Populate Construction (materials, prohibited materials, insulation cladding, appurtenances) from DBM line 1566 and 1562.
3.5 Populate References with locally accessible and `location TBD` items.

### Step 4 — Draft Specification.md
4.1 Define Scope (in/out) referencing other PKG-065 deliverables.
4.2 Express requirements R1-R11 with FACT/PROPOSAL/ASSUMPTION labels and citations.
4.3 List Standards with local-accessibility status.
4.4 Build the Verification table (requirement → verification method).
4.5 List Documentation (anticipated artifacts from `_CONTEXT.md`).

### Step 5 — Draft Guidance.md
5.1 Express Purpose, Principles, Considerations, Trade-offs, Examples from source-grounded reasoning.
5.2 Populate the Conflict Table (CONF-01 through CONF-04 in this run).

### Step 6 — Draft Procedure.md
6.1 Capture production-of-deliverable steps (this document).
6.2 Capture verification of the production output.
6.3 Capture records produced.

### Step 7 — Cross-Document Consistency
7.1 Verify Datasheet entities appear in Specification requirements where appropriate.
7.2 Verify Specification requirements have rationale in Guidance and verification in Procedure (Verification section above and Specification Verification table).
7.3 Verify terminology consistency: "fresh caustic tank", "spent caustic tank", "MTU building", "fuel-gas blanket", "incinerator header", "flame arrestor".
7.4 Verify numeric values consistency: 400 bbl tanks, 50 wt% NaOH (fresh), 14.7 wt% NaOH (circulating, TBC), SG 1.75 fresh (TBC).
7.5 Where unresolvable, prefer TBD and surface in the Guidance Conflict Table.

### Step 8 — Safe Status Update
8.1 If `_STATUS.md` Current State is `OPEN`, transition to `INITIALIZED` and append a history row.
8.2 If state is not `OPEN`, do not modify; report skipped.

### Step 9 — Run Record
9.1 Write `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` with YAML frontmatter and required headings per `AGENT_TASK.md` §"Run-record file format".

## Verification

| Verification | Method | Pass criterion |
|---|---|---|
| All four documents exist and use canonical names | `ls {DELIVERABLE_PATH}` | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present |
| Default schema sections present | Section-heading scan | Each document includes its default sections per skill §"Default schema sections" |
| Authoritative source consulted | Citation scan | At least one DBM citation per substantive datasheet/specification entry |
| Unsupported claims marked | Token scan | TBD / ASSUMPTION / PROPOSAL labels present where DBM is silent or binary sources govern |
| Conflict Table present | Heading scan in Guidance | `## Conflict Table (for human ruling)` exists with at least one row when conflicts exist |
| `_STATUS.md` transition safe | State diff | `OPEN → INITIALIZED` only; no regression |
| Run record present | File presence | `_run_records/TASK_RUN_*.md` written |
| No edits outside deliverable folder | Path scan of writes | All writes within `{DELIVERABLE_PATH}` |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four governed documents.
- Updated `_STATUS.md` with `INITIALIZED` history row (when applicable).
- `_run_records/TASK_RUN_<timestamp>.md` — run record (status, tools, outputs, missing, rulings).
