# Procedure — DEL-078-01 Scope of Work (PKG-078 Pig Receivers (Inlet) 4-25)

> Operational procedure for producing the EPC Integrator Scope of Work for `PKG-078`. This procedure governs how the SoW artifact itself is drafted, verified, and turned over; it does not govern the physical pigging operation of the installed receivers.

## Purpose

Produce a source-grounded EPC Scope-of-Work artifact for `PKG-078` that satisfies the requirements in `Specification.md`, traces to the objectives listed in `DELIVERABLE_REGISTER.csv` row DEL-078-01, and anchors the downstream `DEL-078-02` … `DEL-078-06` deliverables.

## Prerequisites

### Declared Upstream Dependencies

- None declared in `_DEPENDENCIES.md` during PREPARATION. (Source: `_DEPENDENCIES.md`.)
- ASSUMPTION (no declared upstream): the working set assumes the GATE-07 PROJECT_DECOMP snapshot is the controlling upstream truth set, per `_REFERENCES.md` and `_CONTEXT.md`.

### Required References (must be locally accessible before drafting)

- GATE-07 snapshot folder: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
  - `PACKAGE_REGISTER.csv` — row `PKG-078`
  - `DELIVERABLE_REGISTER.csv` — row `DEL-078-01_scope-of-work`
  - `SCOPE_LEDGER.csv` — rows `SOW-0161`, `SOW-0162`, `SOW-0163`, `SOW-0164`
  - `OBJECTIVE_REGISTER.csv` — rows `OBJ-001`, `OBJ-003`–`OBJ-010`
- Deliverable-local metadata: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`

### Required Upstream Source Material (referenced via register provenance; re-open before publication)

- `26020-Package_Requirements.docx` package heading 31 — `TBD` (not locally re-read in this initialization pass)
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — relevant sections SEC-04 through SEC-15 cited via OBJ-001; `TBD` for direct re-read
- `Bid Docs/Budgetary/26020-01-PT-RFQ-35-001-Pig_Recv_2.docx` — `TBD` for direct re-read

## Steps

1. **Confirm package identity.** Open `PACKAGE_REGISTER.csv` row `PKG-078` and `DELIVERABLE_REGISTER.csv` row `DEL-078-01`. Confirm: PackageID, Workbook row 78, WBS 01, Discipline Mechanical, Tracking Number `26020-01-35-001`. Record any mismatch as a Conflict Table entry.
2. **Extract source-derived requirements.** From `SCOPE_LEDGER.csv` rows `SOW-0161` (package carriage), `SOW-0162` (basic scope), `SOW-0163` (major included equipment + HIPPS + sour service + vent + purge), `SOW-0164` (process envelope + By-others), populate the equipment list, design envelope, HIPPS architecture, and boundary statements.
3. **Re-open upstream source slices before publication.** Before the SoW is submitted for checking, open `26020-Package_Requirements.docx` package heading 31 and the cited DBM/RFQ documents. For each requirement number in `Specification.md` (R-1 through R-10), confirm or correct against the source slice. Record source slice references inline.
4. **State the responsibility model.** Copy the ResponsibilityModel text from `PACKAGE_REGISTER.csv` PKG-078 verbatim into the SoW responsibility-assignment record. Do not paraphrase.
5. **List boundaries and By-Others.** Enumerate the four By-Others items from `SOW-0164` (interconnecting piping, DCS integration, foundations, electrical supply to MCC). For each, note the EPC scope package or discipline that owns it (TBD pointers if not enumerated in the current decomposition pass).
6. **Acknowledge interfaces.** List the ten applicable interface types from `PACKAGE_REGISTER.csv` PKG-078 InterfaceTypes. Point to `DEL-078-02 Package Datasheet` for detailed interface facts. Do not duplicate the interface matrix here.
7. **Build objective trace.** For each of OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010, write one sentence in the SoW that makes the connection visible.
8. **Record open items.** Carry forward the source `TBC`/`TBD` items (normal flowrate per receiver; HIPPS setpoint; sour-service code enumeration; 04-25 separator package ID) into the open-items section of the SoW and into the Conflict Table in `Guidance.md`.
9. **Cross-document consistency sweep.** Read `Datasheet.md`, `Specification.md`, `Guidance.md`, and this `Procedure.md` together. Confirm: equipment counts, tag IDs, pressures, temperatures, throughput, sour-service basis, HIPPS topology, and By-Others items are stated identically across all four documents.
10. **Update status and produce run record.** When the four-document kit is complete and consistent, the dispatching TASK updates `_STATUS.md` to `INITIALIZED` (via `tools/scaffolding/write_status.sh`) and writes the run record under `_run_records/`.

## Verification

| Step | Verification Check | Pass Condition |
|---|---|---|
| 1 | PackageID / tracking number / discipline match `PACKAGE_REGISTER.csv` PKG-078 | Exact field match |
| 2 | Equipment list reproduces `SOW-0163` major-included-equipment items | All bullets present; no inventions |
| 3 | Each requirement R-x in `Specification.md` carries a source pointer (either register cell or upstream source slice) | 100% coverage; remaining `TBD` items explicitly labeled |
| 4 | ResponsibilityModel text matches `PACKAGE_REGISTER.csv` PKG-078 verbatim | Char-for-char match |
| 5 | By-Others list = {interconnecting piping; DCS integration; foundations; electrical supply to MCC} | Exact set match |
| 6 | Interface-type list = the 10 entries in `PACKAGE_REGISTER.csv` PKG-078 InterfaceTypes | Exact set match |
| 7 | Each of OBJ-001, OBJ-003..010 is named at least once in the SoW with a substantive sentence | 9/9 |
| 8 | Open items include the four documented TBD/TBC items | 4/4 |
| 9 | Cross-document values (equipment counts, pressures, temperatures, throughput, HIPPS topology) are identical across the four documents | Zero deltas |
| 10 | `_STATUS.md` transitioned from `OPEN` to `INITIALIZED` (or skipped with explicit reason) and a run record exists | One run record present |

## Records

The following records result from executing this Procedure:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (the four-document kit; produced by this Pass 1+2 run)
- `_STATUS.md` updated to `INITIALIZED` (when current state is `OPEN`)
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` (durable run record from the dispatching TASK)
- Conflict Table entries in `Guidance.md` (CONF-078-01-01 through CONF-078-01-04 at this initialization)
- (Downstream, not produced here): vendor-document review log, package acceptance checklist, test/inspection evidence, turnover evidence — see `DEL-078-06 EPC Vendor Package Review and Acceptance`.
