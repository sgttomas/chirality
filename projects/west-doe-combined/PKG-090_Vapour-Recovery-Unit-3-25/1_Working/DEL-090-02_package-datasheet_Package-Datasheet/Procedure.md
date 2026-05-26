# Procedure — DEL-090-02 Package Datasheet (Vapour Recovery Unit 3-25)

> Operational procedure for **producing** the EPC Package Datasheet artifact for the 3-25 VRU.
> Source-grounded in the 3-25 Comp_and_Liquids DBM and the deliverable-local truth set.
> Steps that would require values not present in accessible source are explicitly marked `TBD`.

## Purpose

Define the steps the EPC Integrator follows to produce, verify, and issue the Package Datasheet artifact set for `PKG-090` (Vapour Recovery Unit 3-25). The procedure operationalizes the requirements in `Specification.md` and the principles in `Guidance.md`.

## Prerequisites

### Inputs that must be in place

- `_CONTEXT.md` — deliverable identity, parent package, discipline, anticipated artifacts. (Present.)
- `_REFERENCES.md` — authoritative reference set. (Present.)
- `_DEPENDENCIES.md` — declared upstream/downstream constraints. (Present; no upstream/downstream declared during PREPARATION.)
- `_STATUS.md` — current lifecycle state. (Present; state `OPEN` → `INITIALIZED` upon this run.)
- Accepted decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Authoritative source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (sections SEC-01, SEC-02, SEC-06, SEC-07).

### Inputs flagged as not locally accessible (mark `TBD` where they would govern)

- `_Sources/26020-Package_Requirements.docx` (heading 43) — binary `.docx`; text slice not accessible. `location TBD`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — binary `.xlsx`; text slice not accessible. `location TBD`.
- Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 — referenced by DBM SEC-07; not locally accessible. `location TBD`.
- 04-25 SOC suction interface envelope (pressure, tag, design conditions) — required to close design discharge values for the VRU. `location TBD`.

### Declared dependencies

- Upstream: none declared (per `_DEPENDENCIES.md`). ASSUMPTION: information dependency on the package SOW (DEL-090-01) and the accepted decomposition snapshot is implicit.
- Downstream: none declared at PREPARATION. ASSUMPTION: DEL-090-03 (Construction Work Package), DEL-090-04 (Vendor Engineered Equipment Package), DEL-090-05 (Vendor Document Turnover), and DEL-090-06 (EPC Vendor Package Review and Acceptance) consume this datasheet.

## Steps

### Step 1 — Load deliverable-local truth set

1. Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
2. Confirm `Current State` is in `ALLOW_OVERWRITE_STATES` (`OPEN, INITIALIZED`) before any artifact write.
3. Record the accepted decomposition snapshot ID (`GATE-07_Final_Published_2026-05-24`).

### Step 2 — Resolve authoritative source slices

1. Open `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
2. Read the source slices relevant to the VRU:
   - SEC-01 Executive Summary — package count, configuration, drive type, discharge routing under SCA-002.
   - SEC-02 Site Basis — facility location and elevation.
   - SEC-06 "Vapour Recovery" — recycle path, blanket-gas regulator, LP-flare bypass V-ball, free-drain/slope to flare KO interface.
   - SEC-07 — Fuel-Gas sulphur and purge hazard basis; instrument-air supply from 04-25 (SCA-006); flare and blowdown context.
3. For any value not stated in an accessible slice, record `TBD` with `location TBD` rather than infer.

### Step 3 — Populate `Datasheet.md`

1. Fill Identification from `_CONTEXT.md`.
2. Populate Attributes (Package Equipment, Process Conditions) from DBM SEC-01, SEC-06, SEC-07.
3. Populate Construction and Interfaces from DBM SEC-06, SEC-07.
4. List Scope Items (`SOW-0249..SOW-0252`) and Objectives (`OBJ-002..OBJ-010`, ASSUMPTION via package heuristic).
5. Cite every non-trivial value (`SourcePath` + `SectionRef`) or mark `TBD`/`ASSUMPTION`.

### Step 4 — Populate `Specification.md`

1. Define In-scope / Out-of-scope using `_CONTEXT.md` and DBM SEC-01 supersession list.
2. Write requirements R-1 through R-8 grounded in DBM SEC-01, SEC-06, SEC-07.
3. List governing standards/sources and mark inaccessible ones as `location TBD`.
4. Map each requirement to a verification approach.
5. List required artifacts (per `_CONTEXT.md` "Anticipated Artifacts").

### Step 5 — Populate `Guidance.md`

1. State the Purpose tying this deliverable to DEL-090-01/03/04/05/06.
2. Capture Principles (source authority, interface-facts-here, supersession discipline, honest gaps, sour-service awareness).
3. Record Considerations for items the vendor will need (04-25 SOC envelope, recycle fail action, LP-flare bypass behavior, blanket-gas pressure, sour-water vapour composition).
4. Document Trade-offs taken.
5. Maintain the **Conflict Table** for HRR items (C-090-02-01 recycle fail action; C-090-02-02 inaccessible 26020 sources; C-090-02-03 objective-association heuristic).

### Step 6 — Cross-document consistency check (Pass 2)

1. Verify Datasheet entities/attributes are reflected in Specification requirements where appropriate.
2. Verify each Specification requirement has rationale/consideration in Guidance and a verification hook here.
3. Verify terminology is consistent across the four documents (e.g., "VRU", "LP-flare bypass V-ball", "04-25 SOC suction", "LP fuel gas").
4. Verify numeric/configuration values are consistent (2 packages; 200 hp each; 2 x 100 percent; electric drive).
5. Where values disagree or are unresolved, add a Conflict Table entry rather than guessing.

### Step 7 — Issue the datasheet artifact set

1. Datasheet package contents (per Specification R-7.1):
   - Package technical datasheet.
   - Vendor engineering handoff basis.
   - Package interface requirements matrix (suction sources; discharge to 04-25 SOC suction; LP fuel gas; instrument air from 04-25; electrical; LP flare via V-3900-2 / P-3900-2; drains).
   - Source-supported equipment and design criteria.
2. Confirm every non-trivial value cites a source or is explicitly `TBD` / `ASSUMPTION` (per Specification R-8).
3. Update `_STATUS.md` only via the safe-update rule (`OPEN → INITIALIZED` on this Pass 1/2 run).

### Step 8 — Handoff

1. Notify downstream owners (DEL-090-03, DEL-090-04, DEL-090-05, DEL-090-06) that the datasheet is `INITIALIZED`.
2. Surface remaining HRR items (Conflict Table in `Guidance.md`) to the human reviewer.
3. Record open `TBD` items for 04-25 SOC interface envelope and 26020 source access.

## Verification

| Check | How verified | Tied to |
|---|---|---|
| Four documents present in the deliverable folder | Folder listing shows `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` | Skill non-negotiable constraint |
| Default schema sections present in each document | Section heading review | Skill QA |
| Equipment basis (2 x 200 hp electric VRU, 2 x 100 percent) consistent across Datasheet and Specification | Side-by-side compare | Specification R-1 |
| Discharge routing to 04-25 SOC suction (SCA-002) stated in Datasheet, Specification, Guidance | Section grep | Specification R-2 |
| Every non-trivial value cites a source or is `TBD` with `location TBD` | Citation audit | Specification R-8.1 |
| Inferences labeled `ASSUMPTION` (objective association; installed-spare interpretation) | Label audit | Specification R-8.2 |
| Conflict Table (HRR items) present in `Guidance.md` | File grep | Skill Step 5 |
| `_STATUS.md` updated `OPEN → INITIALIZED` only when current state was `OPEN` | Status file compare | Skill Step 7 safe-update rule |
| Superseded scope (local 03-25 SOC, local 03-25 stabilization, local 03-25 IA, 03-25 heat medium) not reintroduced | Specification R-8.3 audit | DBM SEC-01 |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four deliverable documents.
- `_STATUS.md` — lifecycle state record (advanced `OPEN → INITIALIZED` on this run).
- `_run_records/TASK_RUN_<timestamp>.md` — durable run record for this invocation.
- HRR items (Conflict Table in `Guidance.md`) — surfaced to human reviewer; not closed by this skill.

## References

- `3-25_Comp_and_Liquids_DBM.md` — SEC-01, SEC-02, SEC-06 (Vapour Recovery), SEC-07 (Utilities, Flare and Blowdown).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` (deliverable-local).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (decomposition row for DEL-090-02).
- `26020-Package_Requirements.docx` heading 43 — text slice not locally accessible (`location TBD`).
- `26020-Packages_Interfaces_4_export.xlsx` — text slice not locally accessible (`location TBD`).
