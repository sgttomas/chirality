# Procedure — DEL-088-01 Scope of Work (PKG-088 Caustic Treating, Condensate Mercaptan Removal)

This Procedure describes how to **produce** the Scope of Work artifact for PKG-088 to the Specification requirements (SOW-R-01..SOW-R-10) in source-grounded form.

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, `_STATUS.md`.
- Access to the GATE-07 Final Published PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`, including:
  - `DELIVERABLE_REGISTER.csv` (PKG-088 rows)
  - `PACKAGE_REGISTER.csv` (PKG-088 row)
  - `INTERFACE_REGISTER.csv` (PKG-088 rows; not consumed in Pass 1 — applicable interface list is taken from PACKAGE_REGISTER.csv)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (PKG-088 grouping)
- Access to DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md as the locally accessible authoritative source.
- Declared upstream dependencies: none declared during PREPARATION (see `_DEPENDENCIES.md`). No upstream blocker.
- Open items: `26020-Package_Requirements.docx` heading 41 and `26020-Packages_Interfaces_4_export.xlsx` are referenced as authoritative but binary; clause-level reads remain TBD.

## Steps

1. **Confirm package identity.** Transcribe PackageID, PackageTag, Workbook row, Word heading, discipline, WBS, mandatory flag, scope-item coverage, and objective association from PACKAGE_REGISTER.csv and `_CONTEXT.md` into `Datasheet.md` Identification. Label objective association ASSUMPTION (package-grouping heuristic).

2. **Define package function.** Write the package function statement from DBM-Comp_and_Liquids §Condensate Mercaptan Treating: non-regenerative caustic treating, 20,000 bbl/d C5+, Merichem or equivalent, caustic regeneration excluded, continuous fresh caustic and make-up water consumption, spent caustic and DSO produced. Cite source.

3. **Enumerate tagged equipment.** Populate `Datasheet.md` Tagged Equipment List from the DBM equipment enumeration (caustic C5+ contactor, pre-heater, caustic outlet filter, water wash, fresh-/spent-caustic/fresh-water/DSO tanks, incinerator interfaces). Mark P&ID-level tag numbers TBD pending `26020-Package_Requirements.docx` heading 41 slice access.

4. **Document boundaries and interfaces.** Transcribe applicable interface types from PACKAGE_REGISTER.csv (InterfaceTypes column) into `Datasheet.md` Construction and `Specification.md` Scope. Identify each as a Package Vendor / EPC Integrator boundary.

5. **Build responsibility assignment record.** In `Datasheet.md` Construction and `Specification.md` Scope, allocate work between Package Vendor and EPC Integrator per PACKAGE_REGISTER.csv IntegrationModel. Reference DEL-088-02..DEL-088-06 for downstream owned deliverables.

6. **Capture conditions and material restrictions.** Include the caustic-building aluminum prohibition, caustic drain 300# ANSI / 121 deg C TBC / material embrittlement note, LP fuel-gas blanket on caustic tanks, spent-caustic vent to incinerator via flame arrestor, fresh caustic NOT connected to VRU, and -40 deg C site basis. All citations to DBM-Comp_and_Liquids.

7. **Write the integration narrative.** In `Guidance.md`, write the whole-facility integration narrative (incinerator system, LP fuel gas, drain segregation, F&G mercaptan considerations, truck logistics for spent caustic). Reference but do not duplicate facility-wide systems.

8. **Construct the Conflict Table.** In `Guidance.md`, surface conflicts that cannot be resolved without (a) the Word package requirements slice, (b) the Scope-Item register slice, or (c) a human ruling on objective association mode.

9. **Cross-reference consistency sweep (Pass 2).** Verify:
   - Datasheet equipment/attributes are reflected in Specification requirements where appropriate.
   - Specification requirements have rationale in Guidance.
   - Specification requirements have verification hooks in Specification §Verification.
   - Terminology is consistent across the four documents (e.g., "non-regenerative", "PKG-088", "EPC Integrator", "Package Vendor").
   - Numeric values are consistent (treating capacity 20,000 bbl/d, DSO entrainment 30 / 50 ppmw, 300# ANSI drain minimum).

10. **Update `_STATUS.md`.** If current state is `OPEN`, call `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` to transition to INITIALIZED. If not OPEN, skip and report.

11. **Write run record.** Persist `_run_records/TASK_RUN_<timestamp>.md` per AGENT_TASK Step 5.

## Verification

| Step | Verification check |
|---|---|
| 1 | All identity fields present in `Datasheet.md` match PACKAGE_REGISTER.csv. |
| 2 | Package function statement cites DBM-Comp_and_Liquids §Condensate Mercaptan Treating. |
| 3 | Tagged equipment list matches DBM equipment enumeration; P&ID-level tags marked TBD. |
| 4 | Applicable interface types match PACKAGE_REGISTER.csv InterfaceTypes column exactly. |
| 5 | Responsibility text matches PACKAGE_REGISTER.csv IntegrationModel; DEL-088-02..DEL-088-06 referenced. |
| 6 | All material restrictions and integration conditions cite the DBM section. |
| 7 | Integration narrative references facility systems by name and cites DBM sections. |
| 8 | Conflict Table covers at least: authority precedence (Word vs. DBM), Scope-Item register access, objective association mode. |
| 9 | Pass 2 cross-reference sweep produces no unresolved inconsistencies or surfaces them in the Conflict Table. |
| 10 | `_STATUS.md` updated only if OPEN; History entry recorded. |
| 11 | Run record contains required YAML frontmatter and headings. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` produced in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated OPEN -> INITIALIZED (when safe).
- `_run_records/TASK_RUN_<timestamp>.md` recording inputs, sources read, outputs, missing items, and rulings needed.
