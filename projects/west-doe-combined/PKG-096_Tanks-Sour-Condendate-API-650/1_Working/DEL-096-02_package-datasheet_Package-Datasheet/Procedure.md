# Procedure — DEL-096-02 Package Datasheet (Tanks, Sour Condensate, API 650)

> Operational deliverable. Procedure describes the steps to **produce** the package datasheet artifact (the deliverable's headline output) so a third-party vendor can engineer the tanks.

## Purpose

Produce the EPC Integrator package datasheet for the sour condensate atmospheric storage tanks at the 03-25 Liquids Hub, suitable for vendor handoff and discipline-package engineering. The procedure also defines verification steps and the records that must result.

## Prerequisites

- Declared upstream dependencies: **none declared** in `_DEPENDENCIES.md` during PREPARATION. Effective upstream context includes:
  - Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
  - Governed Liquids Hub DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`).
  - Workbook Packages row 92 and `26020-Package_Requirements.docx` heading 48 — referenced but **not locally accessible** (binary). Per CT-05.
- Access to API 650 (current edition) for clause-level requirements. **Not locally accessible** at draft time.
- Access to final tank register if/when it supersedes the DBM count (per DBM line 406).
- VRU header design basis (capacity at tank tie-in) confirmed.

## Steps

### Step 1 — Confirm Identity and Scope
1.1 Verify deliverable identity against `_CONTEXT.md`.
1.2 Confirm package boundary against the DBM Liquids Hub section (SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 376–417).
1.3 Confirm scope exclusions (LACT, pumps, treating package, other tank packages, withdrawn 03-25 stabilization/SOC/dehydration).

### Step 2 — Lock Tank Count and Capacity
2.1 Adopt **2 × 3,800 bbl sour inlet condensate tanks** and **4 × 3,800 bbl sour condensate tanks** as the current basis (DBM line 406).
2.2 Open a controlled change record if/when the final tank register supersedes this allocation (CT-03).

### Step 3 — Establish Design Code Basis
3.1 Adopt **API 650** as the design code (per package title) — see Specification R-3.
3.2 Resolve CT-01 (API 650 vs. "API-650 Modified") with the EPC Integrator. Record the human ruling in the Conflict Table.
3.3 Where API 650 clause-level requirements are needed, obtain the standard and update `_REFERENCES.md` with accessible source slices.

### Step 4 — Define Service and Stored Fluid
4.1 Confirm stored fluid as stabilized sour C5+ condensate from 04-25 and future third-party (DBM lines 376–382).
4.2 Capture the mercaptan family from DBM line 210 in the material-compatibility section of the vendor datasheet.
4.3 Capture facility ambient minimum −40 °C (DBM line 145) and require winterization (insulation, heating, heat tracing).

### Step 5 — Define Tank Construction Specifics
5.1 Carry external insulation and heating as a requirement (consistent with site basis; produced-water tank precedent at DBM line 421 is the nearest accessible analogue — ASSUMPTION for condensate service).
5.2 Mark internal coating as `TBD` with Devchem 253 carried as a candidate pending vendor compatibility data (CT-02).
5.3 Mark foundation, roof type, materials of construction, nozzle schedule, and instrumentation as `TBD` — downstream of this package datasheet.
5.4 Note that aluminum is prohibited in the caustic building (DBM line 402); the equivalent restriction for sour condensate tanks is `TBD` — recommend exclusion based on sour-service convention (ASSUMPTION).

### Step 6 — Define Interfaces
6.1 List tank-roof vapour nozzle to VRU suction header (DBM line 434).
6.2 List tank outlet nozzle to sour condensate booster pump suction (DBM line 412; pumps outside package).
6.3 List tank inlet nozzle from facility receiving piping (04-25 and future third-party receipts; DBM lines 380, 382).
6.4 Record VRU discharge route to 04-25 SOC per SCA-002 (DBM line 436) for downstream awareness.

### Step 7 — Resolve Source Gaps
7.1 Convert `26020-Package_Requirements.docx` heading 48 to plain-text/Markdown source slice (CT-05) and re-run drafting passes if material changes appear.
7.2 If `26020-Packages_Interfaces_4_export.xlsx` contains binding interface data, extract and add to `_REFERENCES.md`.

### Step 8 — Cross-Document Consistency Sweep
8.1 Verify terminology and numeric values are identical across Datasheet, Specification, Guidance, and Procedure.
8.2 Update the Conflict Table in `Guidance.md` if new inconsistencies are surfaced.

### Step 9 — Handoff
9.1 Compile vendor package containing: this datasheet, the specification, the guidance (including Conflict Table with HRR items), and this procedure.
9.2 Flag all HRR items (CT-01 through CT-05) for EPC Integrator ruling **before** the vendor RFQ is issued.

## Verification

| Verification | Method | Pass Criterion |
|---|---|---|
| V-1 Tank count and capacity match DBM | Documentation check vs. `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 406 | 2 sour inlet + 4 sour condensate × 3,800 bbl recorded |
| V-2 Code basis stated | Specification R-3 reviewed | API 650 explicitly stated; CT-01 raised |
| V-3 Ambient basis stated | Specification R-4 reviewed | −40 °C explicitly stated with source ref |
| V-4 Vapour routing stated | Specification R-6 reviewed | VRU header tie-in stated |
| V-5 Mercaptan compatibility stated | Specification R-8 reviewed | Mercaptan list reproduced with source ref |
| V-6 Conflict Table complete | Guidance reviewed | All known conflicts captured with PROPOSAL + TBD ruling |
| V-7 Anticipated artifacts listed | Specification § Documentation reviewed | All four anticipated artifacts from `_CONTEXT.md` listed |
| V-8 No out-of-scope content | Specification § Scope reviewed | LACT, pumps, treating, stabilization/SOC excluded |

## Records

The procedure shall produce / preserve:
- `Datasheet.md` — descriptive package datasheet (this deliverable folder).
- `Specification.md` — normative requirements (this deliverable folder).
- `Guidance.md` — directional content including the Conflict Table (this deliverable folder).
- `Procedure.md` — this document (this deliverable folder).
- `_STATUS.md` — lifecycle state advanced `OPEN → INITIALIZED` upon completion of Pass 1/Pass 2.
- `_run_records/TASK_RUN_<timestamp>.md` — auditable run record for this invocation.
- Conflict Table HRR entries flagged for EPC Integrator ruling before vendor issuance.
