# Procedure — DEL-060-01 Scope of Work (PKG-060 Tank Farm Pump Building 4-25)

> Operational procedure for **producing** the EPC Integrator Scope of Work artifact for PKG-060. (The artifact itself is a scope document, not an operational procedure; therefore this Procedure governs production of the artifact, not operation of the pump building.)

## Purpose

Produce a coherent, source-grounded Scope of Work artifact for PKG-060 that satisfies the requirements in `Specification.md` and respects the guidance in `Guidance.md`.

## Prerequisites

Required inputs (must be available before drafting):

- `_CONTEXT.md` — deliverable identity, package identity, anticipated artifacts, supports/objectives.
- `_REFERENCES.md` — pointer to GATE-07 PROJECT_DECOMP snapshot and shared source root.
- `_DEPENDENCIES.md` — declared upstream/downstream constraints (none declared at PREPARATION).
- GATE-07 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`, specifically:
  - `PACKAGE_REGISTER.csv` row PKG-060.
  - `DELIVERABLE_REGISTER.csv` rows for DEL-060-01..06.
  - `SCOPE_LEDGER.csv` rows SOW-0189, SOW-0190, SOW-0191, SOW-0192.
  - `INTERFACE_REGISTER.csv` 14 IFC rows for PKG-060.
  - `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-003..OBJ-010.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — facility design basis (in particular: SEC-01 identity, SEC-05/06 product/produced-water disposition, Product Pumps subsection at lines ~1667-1679, Process Units table at lines ~2555 and 2618-2622, Electrical Buildings reference at lines ~2816-2817).

Inputs not locally accessible (treat as `TBD` / `location TBD`):

- `26020-Package_Requirements.docx` heading 15 — referenced source basis; clause-level text unavailable.
- Bid Doc `Bid Docs/Budgetary/26020-01-PT-RFQ-18-002-Tank_Farm_Pump.docx` — referenced; not locally accessible.

## Steps

### Step 1 — Confirm package identity

Open `PACKAGE_REGISTER.csv` and locate `PKG-060`. Capture workbook row, tracking number, discipline, WBS, facility, package name, responsibility model. Confirm `_CONTEXT.md` matches; record any disagreement as a Conflict Table entry in `Guidance.md`.

### Step 2 — Capture the scope items

From `SCOPE_LEDGER.csv`, capture the text of SOW-0189, SOW-0190, SOW-0191, SOW-0192 verbatim into working notes. Treat any verbatim quotation in the Scope of Work as the authoritative reading of the workbook / 26020 requirements heading 15.

### Step 3 — Author the package identity and responsibility model

In the Scope of Work document, write the identity section per REQ-SOW-060-01-001 and the responsibility model per REQ-SOW-060-01-002.

### Step 4 — Author the tagged equipment list

Reproduce the SOW-0191 tag list (P-9290-1, P-9293-1; P-9210-1, P-9220-1; P-9200-1; 2 process water transfer pumps; 2 fresh caustic transfer pumps). Cross-check with `DBM-Deepcut/4-25_Deepcut_DBM.md` Process Units table (line 2618-2622) — both sources must agree on the 4-25 tag block; record any disagreement in the Conflict Table.

### Step 5 — Author the process function and capacity narrative

Use SOW-0190 for the process-function statements (water → 3-25; condensate → liquids hub; condensate recycle from skim). Use SOW-0192 for the capacity / driver / building-form / by-others list. Where the source says "TBC", carry it through as `TBC` rather than substituting a value.

### Step 6 — Author the interfaces list

Use the 14 INTERFACE_REGISTER rows for PKG-060. Flag the absence of "Grading / Site Drainage / Spill Containment" (present for PKG-091, absent for PKG-060) as a `TBD` for human ruling.

### Step 7 — Author the integration narrative

Use DBM-Deepcut SEC-05 (line 452 condensate to 3-25), SEC-06 (lines 504-506 produced water to 3-25), and the tank-farm-pump-module / tank-farm-electrical-building references (lines 2816-2817) to describe how the package integrates into the 04-25 facility and the 03-25 Liquids Hub.

### Step 8 — Author the source-basis citations block

Cite: workbook row 85; 26020-Package_Requirements.docx heading 15 (location TBD); bid doc 26020-01-PT-RFQ-18-002 (location TBD); DBM-Deepcut/4-25_Deepcut_DBM.md (Product Pumps + Process Units sections); GATE-07 snapshot registers.

### Step 9 — Cross-check against sibling deliverables

Confirm the Scope of Work does not encroach on:

- DEL-060-02 Package Datasheet (detailed datasheet content).
- DEL-060-03 Construction Work Package (install/turnover).
- DEL-060-04 Vendor Engineered Equipment Package (vendor engineering/design).
- DEL-060-05 Vendor Document Turnover Package (vendor document register).
- DEL-060-06 EPC Vendor Package Review and Acceptance (EPC review process).

If scope leakage is detected, move the offending content to working notes and replace with a pointer to the sibling deliverable.

### Step 10 — Mark unsupported content

For any value not grounded in an accessible source, mark `TBD` (with source pointer and `location TBD` when the source is known but not locally accessible) or label `ASSUMPTION:` with explicit reasoning. Do not invent.

## Verification

| Check | Verification |
|---|---|
| All 11 normative requirements (REQ-SOW-060-01-001..011) addressed | Section-by-section walkthrough of the Scope of Work against `Specification.md` |
| Equipment tags match SOW-0191 and DBM Process Units table | Side-by-side compare of tag list |
| Capacity / driver values match SOW-0192 verbatim | Side-by-side compare of values |
| Interface list matches the 14 INTERFACE_REGISTER rows for PKG-060 | Compare against `INTERFACE_REGISTER.csv` filter `PackageID=PKG-060` |
| Responsibility model matches PACKAGE_REGISTER ResponsibilityModel | Compare against PACKAGE_REGISTER row PKG-060 |
| No content sourced solely from the inaccessible bid doc without `TBD` marker | Citation audit |
| No scope encroachment on DEL-060-02..06 | Scope-boundary review against `_CONTEXT.md` of sibling deliverables |
| All non-trivial values cite source path + section reference | Citation completeness audit |

## Records

The following records shall be produced or updated as evidence:

- The Scope of Work artifact itself (the body of `Datasheet.md` + `Specification.md` together comprise the Scope of Work content for this deliverable in four-document form; the artifact may also be assembled into a single SOW document downstream if required by the EPC Integrator's external workflow).
- `_run_records/TASK_RUN_<timestamp>.md` — this run's record.
- `_STATUS.md` — state transition `OPEN -> INITIALIZED` (this run).
- (downstream) `MEMORY.md` — created only when there is durable context to preserve (no creation this run).
- (downstream) `Dependencies.csv` — created when `TASK + dependency-extract` runs; not in this run's scope.
- (downstream) `_SEMANTIC_LENSING.md` — created by `skills/lens-register/`; required before Pass 3 enrichment of the four documents.
