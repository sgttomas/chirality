# Procedure — DEL-094-01 Scope of Work, PKG-094 Tanks, Caustic (API 650) 3-25

> Operational procedure for **producing** the Scope of Work deliverable artifact. (This Procedure document does not operate the caustic tanks; equipment operating procedures are downstream of vendor engineering.)

## Purpose

Produce a source-grounded, audit-ready EPC Scope of Work document for PKG-094 that satisfies the requirements in `Specification.md`, with traceability to SOW-0193..0196 and the GATE-07 PROJECT_DECOMP snapshot.

## Prerequisites

### Inputs (must be available before starting)
- `_CONTEXT.md` (deliverable-local identity and scope) — present.
- `_REFERENCES.md` (authoritative references list) — present.
- GATE-07 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `DELIVERABLE_REGISTER.csv` — present.
  - `SCOPE_LEDGER.csv` — present (rows SOW-0193..0196).
  - `INTERFACE_REGISTER.csv` — present.
  - `OBJECTIVE_PACKAGE_MAP.csv` — present.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — present.
- `_Sources/26020-Package_Requirements.docx` — referenced; text extraction TBD (HRR CONF-094-05).
- `_Sources/Bid Docs/_Budgetary/26020-03-PT-RFQ-19-002_Tanks_Caust_1_R0.docx` — referenced; not opened (HRR CONF-094-06).

### Declared upstream dependencies
- None declared in `_DEPENDENCIES.md` as of PREPARATION (2026-05-24).

### Required references
- API 650 (Modified) — location `TBD`; the SoW need not reproduce clauses but shall correctly cite.

### Roles
- **Author:** EPC Integrator package engineer.
- **Reviewer:** EPC Integrator discipline lead (Mechanical).
- **Approver:** Human (per K-AUTH-1; no agent approves).

## Steps

### Step 1 — Read deliverable-local context
- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Record deliverable ID, package ID, discipline, responsible party.

### Step 2 — Pull source-grounded scope from the GATE-07 snapshot
- Open `SCOPE_LEDGER.csv` and extract rows SOW-0193, SOW-0194, SOW-0195, SOW-0196.
- Preserve verbatim text for any clause containing numbers, tags, or "by others" exclusions.

### Step 3 — Pull facility integration basis from the DBM
- Open `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Extract the Caustic Mercaptan Treating package narrative (fresh/spent caustic tank role, NaOH/H2O 50 wt% basis, fuel-gas blanket, aluminum prohibition, vent path, truck-out, VRU non-connection).
- Extract the Site basis (-40 °C minimum ambient, BC site).

### Step 4 — Enumerate interfaces
- From `INTERFACE_REGISTER.csv`, list all rows where ParentPackageID == `PKG-094` (9 interfaces expected per current snapshot).
- Carry interface IDs and topics into the SoW interface table.

### Step 5 — Identify responsibility split
- From `DELIVERABLE_REGISTER.csv`, read DEL-094-01..06 to confirm:
  - EPC Integrator owns DEL-094-01, -02, -03, -06.
  - Package Vendor (with EPC integration review) owns DEL-094-04, -05.
- Record `by others` items from SOW-0196.

### Step 6 — Draft package identity and scope statement
- Use Datasheet.md Identification / Attributes content as identity.
- Use SOW-0194 verbatim for the Basic Scope statement.

### Step 7 — Draft tagged equipment table
- Carry TK-6930-2 with all attributes from SOW-0195.
- Carry Fresh Caustic Tank with function from SOW-0194 and `ASSUMPTION` capacity (Item 2 in SOW-0196). Mark per HRR CONF-094-01.

### Step 8 — Draft design conditions
- Carry SOW-0195/0196 atmospheric / 32 oz / 1.0 oz vacuum / 400 bbl values.
- Carry DBM caustic chemistry (SG 1.75 TBC), heater minimum (32.2 °C / 90 °F), and site ambient (-40 °C).
- Mark all source-declared opens (capacity TBC, flow rate TBD, material/coating TBC).

### Step 9 — Draft integration narrative
- Write 1-2 paragraphs tying PKG-094 caustic tanks into the 03-25 Liquids Hub non-regenerative caustic mercaptan treating system per DBM.
- Cover fresh-caustic supply, spent-caustic receipt, vent/incinerator path, truck-out, VRU exclusion.

### Step 10 — Draft responsibility assignment
- Tabulate EPC Integrator vs Package Vendor vs By Others using `DELIVERABLE_REGISTER.csv` rows and SOW-0196.

### Step 11 — Build traceability matrix
- One row per scope statement linked back to SOW-0193, SOW-0194, SOW-0195, or SOW-0196.

### Step 12 — Compile open items / HRR register
- Reproduce the Guidance.md Conflict Table entries CONF-094-01..06 as the open-items register inside the SoW deliverable.

### Step 13 — Internal QA against Specification.md
- Verify each R1..R9 requirement is reflected in the SoW draft.
- Run the cross-document consistency check (Datasheet ↔ Specification ↔ Guidance ↔ Procedure) per the `four-documents` Step 5 table.
- Resolve drafting-only inconsistencies; escalate source-driven ambiguities into the Conflict Table.

### Step 14 — Submit for human review
- Route to EPC Integrator Mechanical discipline lead for review.
- Route to human approver per K-AUTH-1 for the binding approval record.

## Verification

| Check | How |
|---|---|
| All SOW-0193..0196 reflected | Inspect SoW traceability matrix |
| TK-6930-2 attributes verbatim | Compare against `SCOPE_LEDGER.csv` SOW-0195 |
| "By others" items preserved | Compare against `SCOPE_LEDGER.csv` SOW-0196 |
| All 9 PKG-094 interfaces listed | Compare against `INTERFACE_REGISTER.csv` |
| DBM facility-integration narrative present | Document review |
| Conflict Table CONF-094-01..06 carried into SoW | Document review |
| `_STATUS.md` advanced only via safe update | Verify `OPEN → INITIALIZED` history entry |
| No invention beyond source | Reviewer spot-check |
| All TBD/TBC items visible | Open-items register present |

## Records

- The compiled Scope of Work document (Word/PDF) as the deliverable artifact.
- Updated `_STATUS.md` reflecting lifecycle state.
- Run record(s) under `_run_records/`.
- `MEMORY.md` entries capturing decisions, human rulings on HRR items, and rejected/accepted proposals (when produced).
- Conflict Table rulings, once human-resolved, recorded back into `Guidance.md` and propagated to dependent deliverables (DEL-094-02..06).
