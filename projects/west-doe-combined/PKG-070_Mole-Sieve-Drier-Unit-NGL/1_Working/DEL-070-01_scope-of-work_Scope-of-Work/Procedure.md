# Procedure — DEL-070-01 Scope of Work (PKG-070 Mole Sieve Drier Unit (NGL))

> Operational procedure for *producing* the EPC Integrator Scope of Work
> deliverable for the NGL Mole Sieve Drier Unit package. (The Scope of Work
> is a planning artifact; operational/use procedures for the physical
> package belong to the vendor and to DEL-070-03 Construction Work Package
> and downstream operations documentation.)

## Prerequisites

### Required inputs (deliverable-local)
- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts.
- `_REFERENCES.md` — authoritative decomposition basis pointers.
- `_DEPENDENCIES.md` — declared upstream/downstream (none declared at
  PREPARATION; advisory only).
- `_STATUS.md` — current lifecycle state (must be in `ALLOW_OVERWRITE_STATES`
  for the four-document skill to write).

### Required inputs (decomposition snapshot, GATE-07)
- `DELIVERABLE_REGISTER.csv` row `DEL-070-01_scope-of-work`.
- `PACKAGE_REGISTER.csv` row `PKG-070`.
- `SCOPE_LEDGER.csv` rows `SOW-0145`, `SOW-0146`, `SOW-0147`, `SOW-0148`.
- `INTERFACE_REGISTER.csv` rows for `PKG-070` (12 rows).
- `OBJECTIVE_REGISTER.csv` rows `OBJ-001`, `OBJ-003`..`OBJ-010`.

### Required inputs (source slices — accessibility status)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — present; SEC-06 is the closest
  analogous source (gas-phase sieve), use as ASSUMPTION only for NGL claims.
- `_Sources/26020-Package_Requirements.docx` heading 24 — referenced but
  **not locally accessible as text slice**; mark dependent claims TBD.
- `Bid Docs/Budgetary/26020-01-PT-RFQ-22-003_NGL-Mole-Sieve-Dehy.docx` —
  referenced but **not present in `_Sources/`**; mark dependent claims TBD.

### Required role authority
- EPC Integrator (responsible party per `_CONTEXT.md`).

## Steps

### Step 1 — Read deliverable-local metadata
Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`,
and (if present) `_SEMANTIC.md` and `_SEMANTIC_LENSING.md`. Confirm
deliverable identity (`DEL-070-01_scope-of-work`), parent package
(`PKG-070`), and that current state is in `ALLOW_OVERWRITE_STATES`.

### Step 2 — Load decomposition rows
From the GATE-07 snapshot folder, extract the rows enumerated under
Prerequisites. Treat these as the authoritative routing basis for the SoW.

### Step 3 — Identify and assess accessible source slices
List each source referenced in `PACKAGE_REGISTER.csv` SourceRefs and in
`SCOPE_LEDGER.csv` for SOW-0145..SOW-0148. For each, mark **accessible** or
**not locally accessible**. Carry the assessment into Datasheet "References"
and Specification "Standards".

### Step 4 — Draft the Datasheet (descriptive)
Populate Identification, Attributes, Conditions, Construction, and References
sections strictly from accessible decomposition rows and source slices. Use
`TBD` for any value not present in an accessible source. Do not invent
per-vessel tags, dimensions, or material classes — these belong to
DEL-070-02.

### Step 5 — Draft the Specification (normative)
Write the Scope (in/out), Requirements (R-1..R-10), Standards, Verification,
and Documentation sections. Every requirement must cite either the
decomposition row or the source document (with "location TBD" when the
source is inaccessible).

### Step 6 — Draft the Guidance (directional)
Write Purpose, Principles, Considerations, Trade-offs, Examples, and the
Conflict Table. Capture any decomposition-vs-source or source-vs-source
tensions as Conflict Table rows.

### Step 7 — Draft this Procedure (operational)
Document the deliverable-production procedure (this file). Defer operational
use/operate-the-equipment procedures to the vendor and to DEL-070-03.

### Step 8 — Cross-document consistency check (Pass 2)
For each of the cross-document checks below, verify and remediate:

| Check | What to verify |
|---|---|
| Datasheet ↔ Specification | Capacity, configuration, outlet spec, design pressures/temperatures, and battery-limit lists agree exactly. |
| Specification ↔ Guidance | Every R-* has rationale or trade-off coverage in Guidance, or is explicitly out-of-scope for Guidance. |
| Specification ↔ Procedure | Every R-* has a verification approach (Specification §Verification) and a production step (Procedure §Steps). |
| Terminology | "NGL molecular sieve dehydration package", "three-tower configuration", "regeneration", "adsorption", "C3+ NGL", "battery limits" used consistently. |
| Values | 2,385 m³/d (15,000 bbl/d); <7 ppmw outlet water; 1,978/1,943 kPag adsorption in/out; 29.7/46.3/51.8 °C inlet; <4 psid SoL / <10 psid EoL; 24 h adsorption — identical across documents. |

### Step 9 — Status update (safe)
If `_STATUS.md` Current State is `OPEN`, update to `INITIALIZED` with reason
`TASK+four-documents` (per skill Step 7). Do not regress state from any
other value.

### Step 10 — Persist run record
Write `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` with the required
YAML frontmatter and Markdown body headings (per AGENT_TASK §Run-record
file format).

## Verification

- All four documents (`Datasheet.md`, `Specification.md`, `Guidance.md`,
  `Procedure.md`) exist in the deliverable folder after the run.
- Each document carries the default schema sections for its type.
- Every substantive claim cites a decomposition row, an accessible source
  slice, or is marked `TBD` / `ASSUMPTION` with a reason.
- The twelve PKG-070 interface types are listed in the Datasheet and
  referenced in Specification R-5.2.
- The "by others" exclusions from SCOPE_LEDGER SOW-0148 appear in both
  Datasheet (Construction) and Specification (Scope/Out of scope).
- No writes occurred outside the deliverable folder.
- `_STATUS.md` updated `OPEN → INITIALIZED` only if state was `OPEN`.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the
  four-document kit (this run).
- `_STATUS.md` — updated to `INITIALIZED` (if Step 9 applied).
- `_run_records/TASK_RUN_<timestamp>.md` — durable run record.
- Conflict Table entries (Guidance §Conflict Table) — surface for human
  ruling; not closed in this run.
