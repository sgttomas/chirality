# Procedure: DEL-060-02 — Package Datasheet (Tank Farm Pump Building 4-25)

## Purpose

This procedure describes how the EPC Integrator produces (and how downstream consumers use) the `Package Datasheet` for `PKG-060` (Tank Farm Pump Building 4-25, RFQ `26020-01-PT-18-002`). It is operational: it converts the requirements in `Specification.md` and the rationale in `Guidance.md` into ordered steps with verification hooks.

## Prerequisites

### Inputs (must be available before starting)

- Deliverable-local truth set:
  - `_CONTEXT.md`
  - `_REFERENCES.md`
  - `_DEPENDENCIES.md`
  - `_STATUS.md`
- Authoritative decomposition basis (Gate 7 snapshot):
  - `PACKAGE_REGISTER.csv` row 85
  - `DELIVERABLE_REGISTER.csv` row `DEL-060-02_package-datasheet`
  - `INTERFACE_REGISTER.csv` (for interface conditions)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (for traceability)
- Locally accessible source materials:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (§Product Pumps lines 1667-1679; Package Roster line 2555; Package Line-Item table lines 2618-2622; SEC-11 module / electrical sections)
- Reference source materials (cited; location TBD locally):
  - Workbook Packages row 85
  - `26020-Package_Requirements.docx` package heading 15
  - `26020-01-PT-RFQ-18-002-Tank_Farm_Pump.docx`

### Declared dependencies

`_DEPENDENCIES.md` declares no upstream or downstream constraints for this deliverable (DECLARED mode). Run `TASK + dependency-extract` if critical edges need to be declared in-file before the datasheet is published.

## Steps

### Step 1 — Identification block

1. Populate the Identification table from `_CONTEXT.md` and PACKAGE_REGISTER row 85.
2. Confirm the package name resolves the `Tank Farm Pump Building 2` vs `Tank Farm Pump Building 4-25` discrepancy (see Guidance Conflict Table, C2). Use the `_CONTEXT.md` name as authoritative for deliverable identity; carry the DBM name as an alias note.

Verification: identification fields match `_CONTEXT.md` and PACKAGE_REGISTER row 85.

### Step 2 — Scope of supply

1. List every pump service from PACKAGE_REGISTER row 85 (scope-of-supply narrative).
2. For each service, list tag designators from DBM Package Line-Item table (lines 2618-2622).
3. For the condensate recycle pump, mark the tag `TBD` (see Conflict C3).
4. For the recycle/skim split (Conflict C1), include both DBM-line-1671 ("Product recycle pump") and DBM-line-1672 ("Condensate skim pump") as candidate units; flag the consolidation question for human ruling.

Verification: every pump service in the source materials appears in the datasheet with quantity, configuration, and tag (or `TBD`).

### Step 3 — Design conditions

1. Populate condensate-transfer design conditions from DBM lines 1673-1679 (differential, sparing, NPSHR ceiling, motor sizing, minimum-flow control valve).
2. Populate recycle/skim design conditions from DBM lines 1671-1672 (20 m3/h at 80 m TDH, TBC).
3. For the water-transfer, sour-water-treatment, process-water-transfer, and fresh-caustic-transfer services, mark operating conditions as `TBD` with `location TBD` against `26020-Package_Requirements.docx` package heading 15.
4. Inherit cold-startup motor sizing (-40 °C, JT-mode) as a facility-wide constraint where applicable.

Verification: every design-condition field is either source-cited (with DBM line) or explicitly `TBD`.

### Step 4 — Interface conditions

1. For each interface type in PACKAGE_REGISTER row 85, write a short interface statement covering: medium (where applicable), boundary location, EPC vs. vendor split, and applicable references.
2. Cross-check with INTERFACE_REGISTER (Gate 7) — if the register lists explicit `IFC-*` rows for `PKG-060`, cite them; if no interface IDs are explicit for this package, mark `TBD` and reference the register as a placeholder.

Verification: every interface type from PACKAGE_REGISTER row 85 is addressed.

### Step 5 — Module / construction basis

1. Record the module designator `920-1` (DBM line 2817) and its shop-module status.
2. Record the electrical-area source: 4.16 kV / 600 V General Area / Tank Farm / Process Electrical Building (DBM line 2925).
3. Record the field-run cable-tray allowance (DBM line 2999).

Verification: module references match DBM lines 2817, 2925, 2999.

### Step 6 — Responsibility boundary

1. Insert the responsibility boundary clause from PACKAGE_REGISTER row 85 verbatim or with light editorial cleanup.

Verification: clause matches PACKAGE_REGISTER row 85 narrative.

### Step 7 — References & traceability

1. Cite every source by file path + section/line where locally available.
2. For sources not locally accessible as parsed text (`Workbook Packages row 85`, `26020-Package_Requirements.docx`, `26020-01-PT-RFQ-18-002-Tank_Farm_Pump.docx`), cite with `location TBD`.
3. Map deliverable to objectives from `_CONTEXT.md` (OBJ-001, OBJ-003 through OBJ-010) as ASSUMPTION (PACKAGE_HEURISTIC mapping) per `OBJECTIVE_ASSOCIATION_MODE`.

Verification: every section that carries a non-trivial claim has a citation or an explicit `TBD`/`ASSUMPTION` label.

### Step 8 — QA sweep

1. Run cross-document consistency checks per `four-documents` Step 5:
   - Datasheet attributes ↔ Specification R2;
   - Specification requirements ↔ Procedure verification hooks;
   - Terminology consistency (pump tags, package name);
   - Numeric values consistency (differential, NPSHR, TDH).
2. If unresolved inconsistencies remain, add to the Guidance Conflict Table.

Verification: no inconsistencies between the four documents, or all remaining inconsistencies are captured in the Conflict Table.

## Verification

The deliverable is verified when:
- All eight steps above are completed.
- Every requirement in `Specification.md` has a corresponding section in `Datasheet.md`.
- Conflict Table in `Guidance.md` is populated for every unresolved conflict.
- `_STATUS.md` reflects the appropriate state (`INITIALIZED` after this run; subsequent state changes per project lifecycle).

## Records

The following records are produced or updated:
- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this run);
- `_STATUS.md` (updated `OPEN → INITIALIZED` by this run when state is `OPEN`);
- `_run_records/TASK_RUN_<timestamp>.md` (this run);
- Downstream: vendor responses to `26020-01-PT-18-002` (out of scope here); EPC review record (`DEL-060-06`).
