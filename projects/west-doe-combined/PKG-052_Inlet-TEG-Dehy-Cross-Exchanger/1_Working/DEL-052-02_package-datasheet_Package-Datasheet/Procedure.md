# Procedure — DEL-052-02 Package Datasheet (PKG-052 Inlet / TEG Dehy Cross Exchanger)

## Purpose

Operational procedure to produce, source-ground, review, and accept the Package Datasheet artifact (`Datasheet.md`) for PKG-052 — Inlet / TEG Dehy Cross Exchanger (E-5718-1), such that the artifact satisfies the requirements in `Specification.md` and the principles in `Guidance.md`, and is fit to serve as the EPC Integrator handoff basis to a third-party vendor or discipline package engineering team.

Source: `_CONTEXT.md`; `Specification.md`; `Guidance.md`.

## Prerequisites

### Declared upstream dependencies

- None declared during PREPARATION. Source: `_DEPENDENCIES.md`.
- ASSUMPTION (working): the accepted upstream Gate 7 PROJECT_DECOMP snapshot is the controlling decomposition truth; no other deliverable is a hard upstream blocker for the Package Datasheet draft itself, but consumer deliverables (DEL-052-03 Work Package, DEL-052-04 Vendor Engineered Equipment Package, DEL-052-05 Vendor Documentation, DEL-052-06 EPC Vendor Package Review) consume this artifact.

### Required references

- `_CONTEXT.md` (deliverable identity and scope).
- `_REFERENCES.md` (source pointers and shared source root).
- Accepted upstream Gate 7 snapshot:
  - `PACKAGE_REGISTER.csv` row 62 (PKG-052).
  - `DELIVERABLE_REGISTER.csv` row 337 (DEL-052-02).
  - `ARTIFACT_REGISTER.csv` (anticipated artifacts cross-check).
  - `INTERFACE_REGISTER.csv` (PKG-052 interface rows, where present).
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (objective association — package-grouped heuristic; ASSUMPTION per `_CONTEXT.md`).
- Locally accessible source slices:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Inlet / TEG Dehy Cross Exchanger" (lines ~595-606); §"Inlet Pipeline Pressure and Flow"; §Module 520 equipment list (line 1131); §Process Description (lines 1119-1120, 1193); §Equipment table (lines 2537, 2586).
- Source-cited but locally inaccessible (location TBD):
  - `26020-Package_Requirements.docx` package heading 7.
  - `Bid Docs/Budgetary/26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx`.

### Required deliverable-local fileset

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` present (minimum viable fileset from PREPARATION).
- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` exist after a successful four-documents run.

## Steps

### Step 1 — Confirm deliverable identity and scope

1. Read `_CONTEXT.md`. Confirm DeliverableID `DEL-052-02_package-datasheet`, ParentPackageID `PKG-052`, package name "Inlet / TEG Dehy Cross Exchanger", Discipline Mechanical, Type "EPC Package Datasheet", ResponsibleParty "EPC Integrator".
2. Confirm coverage of SOW scope items `SOW-0103`, `SOW-0104`, `SOW-0105`, `SOW-0106` (per `_CONTEXT.md`).
3. Confirm package-heuristic objective association (`OBJ-001`, `OBJ-003`..`OBJ-010`) as ASSUMPTION (best-effort mapping per skill default `PACKAGE_HEURISTIC`).

### Step 2 — Read authoritative source slices

1. Read PACKAGE_REGISTER.csv row 62: extract package identity, Lead Equipment Tag (26020-01-PT-16-001), Description (E-5718-1 shell-and-tube TEMA "R" BEM; duty 5,514.3 kW / 18.82 MMBTU/hr), Word Source Basis, Responsibility, Applicable interface types.
2. Read DBM-Deepcut/4-25_Deepcut_DBM.md §"Inlet / TEG Dehy Cross Exchanger" and surrounding sections: extract design pressure (9,756 kPag / 1,415 psig), design temperature (66 °C), quantity (1), process function statement, module assignment (Module 520).
3. Read DBM §"Inlet Pipeline Pressure and Flow" and §"Inlet Compression": record facility-level pressure/flow envelope (300 MMSCFD design vapour, 1,300 psig MAOP basis, 625/1,130 psig compressor suction/discharge).
4. For any value not present in accessible sources, mark `TBD` in the Datasheet. Do not invent.

### Step 3 — Draft `Datasheet.md`

Populate, in order:
1. Identification table (from `_CONTEXT.md` and PACKAGE_REGISTER row 62).
2. Tagged Equipment table (E-5718-1 row).
3. Process Function paragraph (cite DBM line 606 and supporting process-description lines).
4. Design Attributes table for E-5718-1 (FACT where source-supported, ASSUMPTION/TBD otherwise; cite every cell).
5. Process Conditions Context table (facility-level envelope, with sources).
6. Construction / Integration table.
7. Applicable Interface Types list (verbatim from PACKAGE_REGISTER row 62 "Applicable interface types").
8. Package Interface Requirements Matrix (one row per applicable interface type; EPC vs. Vendor split; tie-in `TBD` where not in source).
9. References list (path-qualified).

### Step 4 — Draft `Specification.md`

1. Scope (Covers / Excludes) per DELIVERABLE_REGISTER.csv rows 336-341 and `_CONTEXT.md`.
2. Requirements R-1 through R-10 covering identity, tagged equipment, process function, design conditions, warm-side identity conflict handling, interface matrix, source-grounding, responsibility split, stable structure, SOW traceability.
3. Standards table — list TEMA, ASME BPVC VIII Div. 1, CSA B51, and 26020-Package_Requirements.docx heading 7 with explicit local-accessibility status.
4. Verification table — each requirement mapped to an inspection or coverage check.
5. Documentation list — the four documents plus mapping to `_CONTEXT.md` anticipated artifacts.

### Step 5 — Draft `Guidance.md`

1. Purpose paragraph (EPC Integrator handoff basis).
2. Principles: source fidelity over convenience; responsibility-split discipline; interface scope bounded by upstream register; TBD as first-class; decomposition routes / sources decide.
3. Considerations: warm-side identity unresolved; TEMA classification granularity; standards basis implicit; module/system context; process-condition envelope.
4. Trade-offs table.
5. Examples (1-3 short illustrations of correct provenance treatment).
6. Conflict Table — enter every cross-document or cross-source disagreement requiring human ruling:
   - CONF-1 Warm-side stream identity (DBM line 606 internal disagreement vs. PACKAGE_REGISTER Description).
   - CONF-2 TEMA-type granularity (register row vs. DBM phrasing).
   - CONF-3 Code-of-construction basis implicit.
   - Each row: Conflict ID, Conflict statement, Source A, Source B, Impacted sections, Proposed authority (PROPOSAL), Human ruling (TBD).

### Step 6 — Cross-document consistency sweep (Pass 2)

For each cross-reference check, verify and correct in the drafts only:

| Check | Verify |
|---|---|
| Datasheet ↔ Specification | Every Specification requirement that names a value (duty, design P/T, tagged equipment, interfaces) is reflected in the Datasheet with the same value and the same source. |
| Specification ↔ Guidance | Every Specification requirement with rationale needs has a corresponding Guidance principle/consideration; CONFLICT requirement R-5 is mirrored by Conflict Table CONF-1. |
| Specification ↔ Procedure | Every Specification requirement has at least one Procedure step or verification check that exercises it. |
| Terminology | Equipment tag "E-5718-1"; package "PKG-052"; lead tag "26020-01-PT-16-001"; package name "Inlet / TEG Dehy Cross Exchanger" used identically in all four documents. |
| Values | Duty 5,514.3 kW / 18.82 MMBTU/hr; design pressure 9,756 kPag / 1,415 psig; design temperature 66 °C; identical and same source across all four documents. |
| Provenance | Every non-trivial value cites PACKAGE_REGISTER row 62, a DBM section, `_CONTEXT.md`, or is labeled `ASSUMPTION` / `TBD` / `location TBD`. |

Where a discrepancy cannot be resolved from the drafts alone, re-open the relevant authoritative source slice. If still unresolvable, add a Conflict Table row in `Guidance.md` rather than guessing.

### Step 7 — Resolve warm-side stream identity (handoff prerequisite, not a blocker for this skill)

This step is performed by the human reviewer or by a follow-on TASK that has authority to resolve a source conflict. The four-documents skill must not unilaterally pick.

1. Re-read DBM line 606 in context; re-read DBM Module 520 grouping (line 1131) and process-description lines 1119-1120 and 1193.
2. Re-read PACKAGE_REGISTER row 62 Description.
3. Record the chosen warm-side stream identity in the Conflict Table CONF-1 "Human ruling" cell.
4. Propagate the ruling to:
   - Datasheet Process Function paragraph (remove the CONFLICT note).
   - Datasheet Design Attributes "Shell-side fluid" cell (replace TBD/ASSUMPTION).
   - Specification R-5 (relax the SHALL-flag-as-conflict clause).

### Step 8 — Resolve standards basis (handoff prerequisite)

1. Convert `26020-Package_Requirements.docx` package heading 7 to local markdown under `_Sources/`.
2. Re-read the converted heading.
3. Update Specification Standards table: replace `location TBD` with explicit references; update Guidance Conflict Table CONF-3.

### Step 9 — Acceptance review

Performed by EPC Integrator reviewer (human). Each check is pass/fail.

| ID | Check | Pass criterion |
|---|---|---|
| AC-1 | Identity completeness | Identification table populated; SOW coverage and objective association recoverable from `_CONTEXT.md`. |
| AC-2 | Tagged equipment correctness | E-5718-1 row matches PACKAGE_REGISTER row 62 (Description and Lead Equipment Tag). |
| AC-3 | Source fidelity | Each non-trivial value cites PACKAGE_REGISTER row 62, a specific DBM section, `_CONTEXT.md`, or carries `ASSUMPTION`/`TBD`. No invented values. |
| AC-4 | Conflict surfacing | Warm-side identity, TEMA granularity, and standards basis appear in Guidance Conflict Table; Datasheet does not unilaterally resolve. |
| AC-5 | Interface matrix coverage | Each interface type in PACKAGE_REGISTER row 62 Applicable interface types appears exactly once in the interface matrix. |
| AC-6 | Responsibility split | Package Vendor vs. EPC Integrator split is stated and consistent across documents. |
| AC-7 | Stable structure | Default sections present in each of the four documents. |
| AC-8 | Cross-document consistency | Equipment tag, package name, duty, design pressure, and design temperature identical across documents. |
| AC-9 | Provenance audit | Spot-check at least five non-trivial values; each has a usable source pointer (or labeled `ASSUMPTION`/`TBD`). |
| AC-10 | Out-of-scope exclusions | Vendor-internal mechanical detail (tube count, materials, baffle layout, heat transfer area) is not specified in the Datasheet (deferred to vendor scope or to DEL-052-04). |

### Step 10 — Handoff

1. Confirm `_STATUS.md` is at the appropriate state to release the artifact (Gate 5 anchor per `_CONTEXT.md` notes).
2. Confirm DEL-052-01 (Package Scope of Work) and this deliverable are consistent, since both are upstream of DEL-052-03..06.
3. Issue the Datasheet to the third-party vendor or discipline package engineering team along with the resolved standards list and warm-side identity ruling.

## Verification

Verification checks for the Datasheet production itself are recorded in `Specification.md` (R-1..R-10) and exercised by the cross-document consistency sweep (Step 6) and acceptance review (Step 9). Specifically:

- All ten Specification requirements are exercised by at least one Procedure step or acceptance check.
- Every Conflict Table entry has at least one downstream Procedure step (Step 7, Step 8) that, when performed, closes it.
- The interface matrix coverage check (AC-5) is mechanical: count rows against PACKAGE_REGISTER row 62 Applicable interface types.

## Records

The following records SHALL be produced or retained when this procedure is executed:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this file) — deliverable-local artifacts under version control.
- `_STATUS.md` history rows — record state transitions (`OPEN → INITIALIZED` after four-documents Pass 1/2; further transitions per project lifecycle).
- `_run_records/TASK_RUN_*.md` — execution evidence for every skill invocation that produced or modified the four documents.
- Conflict Table rulings — recorded in `Guidance.md` when each conflict is closed by a human ruling.
- Acceptance review record — TBD (carried in EPC Integrator review system; not stored in this deliverable folder unless explicitly mirrored).
- Source-conversion artifacts — when `26020-Package_Requirements.docx` heading 7 and the RFQ document are converted to local markdown, store under `_Sources/` and update `_REFERENCES.md` in a subsequent authorized TASK (not modified by this skill).
