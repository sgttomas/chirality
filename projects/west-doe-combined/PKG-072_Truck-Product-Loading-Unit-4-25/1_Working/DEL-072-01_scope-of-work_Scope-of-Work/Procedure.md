# Procedure — DEL-072-01 Scope of Work

## Purpose

This Procedure describes the operational steps to **produce** the EPC Integrator Scope of Work for PKG-072 from accepted upstream truth (Gate 7 PROJECT_DECOMP snapshot) and the source materials referenced therein. Once produced, the Scope of Work is itself a basis input for sibling PKG-072 deliverables; "use/operate" steps below cover how downstream consumers should reference this document.

## Prerequisites

- Accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — present.
- Deliverable-local truth set: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` — present.
- Source materials (accessible at project `_Sources/` root; deliverable-local source slices not yet extracted):
  - `_Sources/26020-Package_Requirements.docx` (heading 26)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (workbook Packages row 99)
- Declared upstream dependencies: none declared (per `_DEPENDENCIES.md`).
- Current `_STATUS.md` state must be in `ALLOW_OVERWRITE_STATES` (OPEN, INITIALIZED) for production runs.

## Steps

1. **Confirm package identity.** Read PACKAGE_REGISTER.csv row 99 and `_CONTEXT.md`. Confirm PKG-072, workbook row 99, tracking number 26020-01-23-001, package name "Truck Product Loading Unit 4-25". Record any identity discrepancy (see Conflict C-072-01-01) for human ruling rather than silently picking one name. Source: PACKAGE_REGISTER.csv row 99.
2. **Enumerate tagged equipment.** Extract the tagged equipment list from SCOPE_LEDGER.csv SOW-0247 (skid, fuel gas heater with 600 V SCR control and skin-temperature thermocouple override, fuel gas scrubber sized using k = 0.35 cap). Place in Datasheet Identification / Construction sections.
3. **State package function.** Use the SCOPE_LEDGER SOW-0246 wording verbatim for the function statement.
4. **Capture conditions.** Carry SCOPE_LEDGER SOW-0248 operating and design conditions into the Datasheet Conditions table. Preserve TBD entries (Final Flow, MAWP, heater capacity); do not interpolate.
5. **State exclusions / by-others items.** Copy the "By others" clause from SOW-0248 into the Specification scope-exclusion section and Guidance Considerations.
6. **List interface types.** Copy the eleven interface types from PACKAGE_REGISTER.csv row 99 ApplicableInterfaceTypes into the Specification Requirements (R-072-01-07) and Datasheet Construction Interfaces section.
7. **State the responsibility split.** Copy PACKAGE_REGISTER.csv row 99 ResponsibilityModel into Specification Requirement R-072-01-08 and Guidance Principles 2. Cite OBJ-004.
8. **Trace objectives.** List OBJ-001 and OBJ-003 through OBJ-010 in Specification Documentation / Requirements R-072-01-09, with one-line context for each from OBJECTIVE_REGISTER.csv.
9. **Mark open items.** Surface heater capacity, Final Flow, and MAWP as open items in Specification Requirement R-072-01-10. Reference OBJ-010 (controlled open-item closure).
10. **Conflict capture.** Where source rows disagree (currently package name field, see C-072-01-01), record the conflict in Guidance.md Conflict Table; do not silently resolve.
11. **Source slice extraction (recommended follow-up).** Extract the `26020-Package_Requirements.docx` heading 26 text into a deliverable-local reference file so downstream drafts can cite exact source location rather than `location TBD`. Out of scope for this run; record as Conflict C-072-01-02.

### Steps to use this Scope of Work (downstream consumers)

- DEL-072-02 Package Datasheet: consume Datasheet Conditions and Construction sections; expand into a vendor-handoff datasheet without restating the responsibility split.
- DEL-072-03 Construction Work Package: consume Specification R-072-01-06 (by-others) and R-072-01-08 (responsibility) as the construction interface basis.
- DEL-072-04 Vendor Engineered Equipment Package: consume Specification Requirements R-072-01-01 through R-072-01-07 as the vendor scope envelope.
- DEL-072-05 Vendor Document Turnover Package: consume Specification Documentation list as the vendor document register basis (per `26020-Package_Requirements.docx` vendor-document tables, accessed separately).
- DEL-072-06 EPC Vendor Package Review and Acceptance: consume Requirements R-072-01-01 through R-072-01-11 as the acceptance basis.

## Verification

| Check | Method | Pass Criterion |
|---|---|---|
| Identity match | Compare Datasheet Identification table vs PACKAGE_REGISTER.csv row 99 | All identity fields match source (excepting C-072-01-01, recorded as conflict) |
| Equipment list completeness | Compare Datasheet Construction items vs SCOPE_LEDGER.csv SOW-0247 | All three items present (skid, heater, scrubber) with stated source-grounded attributes |
| Conditions fidelity | Compare Datasheet Conditions table vs SCOPE_LEDGER.csv SOW-0248 | Every condition matches source, TBD preserved |
| Exclusions present | Inspect Specification Scope (Out of scope) and Guidance Considerations | "By others" items explicitly listed |
| Interfaces present | Inspect Specification R-072-01-07 evidence | All eleven interface types listed verbatim |
| Responsibility split present | Inspect Specification R-072-01-08 + Guidance Principle 2 | Verbatim vendor/EPC split with OBJ-004 citation |
| Objectives traced | Inspect Specification R-072-01-09 | OBJ-001, OBJ-003-010 listed |
| Open items visible | Inspect Specification R-072-01-10 | Final Flow, MAWP, heater capacity flagged TBD |
| Conflicts captured | Inspect Guidance Conflict Table | At least C-072-01-01 and C-072-01-02 present until human ruling |

## Records

The following records result from this Procedure:

- `Datasheet.md` (identity, attributes, conditions, construction)
- `Specification.md` (scope, requirements, standards, verification, documentation)
- `Guidance.md` (purpose, principles, considerations, trade-offs, examples, Conflict Table)
- `Procedure.md` (this file)
- `_STATUS.md` state transition record (OPEN -> INITIALIZED) on successful production
- `_run_records/TASK_RUN_<timestamp>.md` — TASK run record for this invocation

These records are the deliverable's evidence trail and the basis for EPC review and acceptance recorded in DEL-072-06.
