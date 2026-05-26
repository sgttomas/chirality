# Procedure — DEL-106-03 Construction Work Package (Yard Lighting)

> Operational procedure to **produce** the Construction Work Package deliverable artifacts. Procedure for **operating/using** the installed yard-lighting system is out of scope here (belongs to facility operations after `DEL-106-06` acceptance). Source-specific construction parameters are `TBD` until deliverable-local source slices are available.

## Purpose

Produce the three required artifacts under `DEL-106-03`:
1. Construction work package narrative (`ART-88F0D51520`).
2. Installation and tie-in workface plan (`ART-F0EC8767B3`).
3. Construction interface and turnover checklist (`ART-FC16B15401`).

Source: `ARTIFACT_REGISTER.csv` (GATE-07).

## Prerequisites

- Accepted EPC Scope of Work for `PKG-106` (`DEL-106-01_scope-of-work`) at a maturity acceptable to construction planning. Source: `DELIVERABLE_REGISTER.csv` (DEL-106-01).
- Accepted EPC Package Datasheet (`DEL-106-02_package-datasheet`) including the package interface requirements matrix (`ART-51069C3B2D`) and the three interface facts (Electrical Power, Grounding/Bonding, Area/Exterior Lighting). Source: `ARTIFACT_REGISTER.csv`.
- Vendor-engineered equipment package (`DEL-106-04`) available at handoff maturity (vendor design basis, datasheets, drawings). Source: `DELIVERABLE_REGISTER.csv` (DEL-106-04).
- Vendor document turnover content (`DEL-106-05`) accessible as needed for installation references. Source: `DELIVERABLE_REGISTER.csv` (DEL-106-05).
- Deliverable-local source slices for: DBM-Deepcut SEC-11 (civil), SEC-12 (electrical), SEC-14/SEC-15 (safety/regulatory); Workbook Packages row 12 detail; relevant `26020-Package_Requirements.docx` package rows. **Currently TBD** per `_REFERENCES.md`.
- `_DEPENDENCIES.md`: no declared upstream dependencies recorded yet (DECLARED mode). Treat the above as advisory until declared.

## Steps

1. **Read context.** Re-read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, this `Specification.md`, and `Datasheet.md`. Identify which source slices are now locally accessible.
2. **Confirm interface scope.** From `INTERFACE_REGISTER.csv` (PKG-106), enumerate Electrical Power, Grounding/Bonding, Area/Exterior Lighting as the three construction-interface threads.
3. **Draft construction work package narrative (`ART-88F0D51520`).**
   - State package identity, source basis (Workbook Packages row 12), discipline (Electrical), and responsibility split.
   - Describe the construction objective: install vendor-supplied yard-lighting package and integrate it into facility electrical and grounding systems.
   - Identify code/standard regime (`TBD` pending DBM SEC-15 access).
   - Identify hazardous-area / sour-service constraints applicable to fixture suitability and bonding (`TBD`).
4. **Draft installation and tie-in workface plan (`ART-F0EC8767B3`).**
   - For each interface thread, document: tie-in point reference (`TBD`), method (`TBD`), pre-conditions, sequence, responsible craft, inspection hold points, and hand-back conditions.
   - Document civil/structural coordination items (foundations, trenching, conduit, access) as coordination references to the relevant civil/structural packages (per CFL-001 PROPOSAL).
   - Mark every numeric or quantitative parameter as `TBD` until grounded.
5. **Draft construction interface and turnover checklist (`ART-FC16B15401`).**
   - List interface checkpoints by tie-in.
   - List inspection items (per project quality regime — `TBD`).
   - List turnover items: as-built records, commissioning evidence, vendor-document references, operability/maintainability evidence per OBJ-010.
   - Define acceptance handoff to `DEL-106-06`.
6. **Cross-check artifacts.** Ensure terminology and interface references are consistent with `Specification.md` and `Datasheet.md`. Confirm the three artifacts cover R-1 through R-10.
7. **Surface conflicts.** Update `Guidance.md` Conflict Table for any newly observed source/decomposition conflicts.
8. **Record run.** Write `_run_records/TASK_RUN_<date>_<HHMM>.md` capturing: pass set executed, source slices consulted, ASSUMPTION/TBD inventory, and disposition summary.

## Verification

| Step | Verification |
|---|---|
| 2 | All three PKG-106 interfaces enumerated and present in plan. |
| 3 | Narrative cites Workbook Packages row 12 and preserves responsibility model from `PACKAGE_REGISTER.csv`. |
| 4 | Each interface thread has tie-in entries (even if `TBD`). |
| 5 | Checklist maps to `DEL-106-06` acceptance basis. |
| 6 | Terminology audit across the four documents. No unsourced quantitative values present. |
| 7 | Conflict Table updated where new conflicts surfaced. |
| 8 | Run record present and complete. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this skill).
- Constructed artifacts when authored: `ART-88F0D51520`, `ART-F0EC8767B3`, `ART-FC16B15401` (filed under this deliverable folder per project filing convention — `TBD` until decided).
- `_STATUS.md` updated by `tools/scaffolding/write_status.sh`.
- `_run_records/TASK_RUN_*.md`.
- Updated `_DEPENDENCIES.md` (out of scope for this skill; flagged for follow-up dependency-extract run if/when warranted).
