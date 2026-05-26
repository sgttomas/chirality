# Procedure — DEL-097-01 Scope of Work

Operational procedure for **producing** the EPC Scope of Work artifact for `PKG-097`. The output is the issued Scope-of-Work document (and its companion artifacts) consumed by the Package Vendor and by downstream `PKG-097` deliverables.

## Purpose

Produce the Gate-5 EPC anchor Scope of Work for `PKG-097` such that it satisfies every requirement in `Specification.md`, is fully provenanced to the Gate-07 published decomposition snapshot and to the locally accessible source materials, and is consistent with `Datasheet.md` and `Guidance.md`.

## Prerequisites

1. Confirmed read access to the Gate-07 snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — registers used:
   - `PACKAGE_REGISTER.csv` (row 88)
   - `DELIVERABLE_REGISTER.csv` (row 492)
   - `SCOPE_LEDGER.csv` (`SOW-0201`..`SOW-0204`)
   - `INTERFACE_REGISTER.csv` (nine `PKG-097` rows)
   - `OBJECTIVE_REGISTER.csv` (`OBJ-002`..`OBJ-010`)
2. Confirmed read access to the 03-25 facility DBM: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
3. Awareness that `26020-Package_Requirements.docx` heading 49 is the upstream Word source; the workbook-extracted ledger rows (`SOW-0202`..`SOW-0204`) are used as the slice surface for this run.
4. No declared upstream dependencies block this deliverable per `_DEPENDENCIES.md`.
5. `_STATUS.md` is in `OPEN` or `INITIALIZED` (i.e., within `ALLOW_OVERWRITE_STATES`).

## Steps

1. **Read the package identity row.** Open `PACKAGE_REGISTER.csv` row 88 and capture: package name (preserve workbook spelling "Condendate"), discipline (Mechanical), WBS (03), tracking number (26020-03-19-006), responsibility model, basic scope, applicable interface types, and source-reference cell.

2. **Read scope-ledger rows.** Open `SCOPE_LEDGER.csv` and extract `SOW-0201`, `SOW-0202`, `SOW-0203`, `SOW-0204` verbatim. These are the normative facts for the Scope of Work.

3. **Read interface inventory.** Filter `INTERFACE_REGISTER.csv` to rows with `PackageID = PKG-097`. Record the nine interface types and their interface IDs. Do *not* attempt to populate tie-in facts here; those live in `DEL-097-02_package-datasheet`.

4. **Read facility integration basis.** Open `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and read the sections "Facility Overview", "Condensate and Produced-Water Receipts", and "Condensate Storage and Product Handling". Extract: (a) where the product tanks sit (03-25 Liquids Hub), (b) where their feed comes from (stabilized condensate returning from 04-25 plus 06-29 Canlin and future third-party), (c) where their product goes (sales condensate via non-regenerative caustic mercaptan treating → LACT → NRM NEBC Connector).

5. **Author the Scope of Work body.** Compose the issued Scope of Work using the structure below. Each numbered clause shall be sourced (citation to `SOW-####`, `PACKAGE_REGISTER.csv` row 88, or DBM section), and unknown items shall be marked `TBD`:
   - 1.0 Identity and tracking
   - 2.0 Package function and facility integration
   - 3.0 Basic equipment and configuration
   - 4.0 Codes and standards (modified API 650; API 2000; Devchem 253)
   - 5.0 Operating and design conditions
   - 6.0 Per-tank fittings and protection
   - 7.0 Fill control and nozzle sizing
   - 8.0 Interfaces (nine declared types, by interface type only)
   - 9.0 Battery limits and By-Others exclusions
   - 10.0 Responsibility model (Vendor vs. EPC)
   - 11.0 Documentation/turnover handoff (Vendor doc table referenced via `DEL-097-05`)
   - 12.0 Scope-ledger traceability (cite `SOW-0201`..`SOW-0204`)
   - 13.0 Objective traceability (`OBJ-002`..`OBJ-010` — ASSUMPTION per `_CONTEXT.md`)

6. **Produce the tagged-equipment list.** A short companion list naming the four 3,800 bbl Condensate Product Storage Tanks. Tag numbers are `TBD` (not present in the available source slices); the list shall hold tag-number placeholders pending the 03-25 tank register.

7. **Produce the responsibility-assignment record.** Restate the Vendor/EPC split from `PACKAGE_REGISTER.csv` row 88 as a single-page record.

8. **Produce the integration narrative.** A 1–2 paragraph narrative situating `PKG-097` in the 03-25 Liquids Hub per the DBM read in Step 4. Cite DBM section headings.

9. **Cross-consistency sweep against `Datasheet.md` and `Specification.md`.** Reconcile any numeric or wording drift; do not silently change values. If drift is unresolvable, add or update an entry in the Conflict Table in `Guidance.md`.

10. **Provenance pass.** Verify that every non-trivial clause carries a citation; mark anything unsupported as `TBD` and surface in the Conflict Table if a downstream user would otherwise read it as a fact.

11. **Hand off.** Place the Scope of Work and companion artifacts under this deliverable folder for review against the QA checks (see Verification).

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| All requirements in `Specification.md` represented in the issued Scope of Work | Tabular review | 18/18 requirements addressed (with `TBD` where source-limited) |
| All nine `PKG-097` interfaces present (by type) | Diff against `INTERFACE_REGISTER.csv` | All nine types listed |
| Operating + design conditions match `SOW-0204` | Side-by-side numeric check | Exact match (atmospheric/0 °C–40 °C operating; 32 oz/-40 °C–60 °C design; 94,940 kg/h; 3,187 Am3/d) |
| Responsibility model wording matches `PACKAGE_REGISTER.csv` row 88 | Text diff | Substantive equivalence |
| Tank count = 4; size = 3,800 bbl | Text check | Exact |
| Package name "Tanks, Condendate (API 650) 3-25" used verbatim for package identity | Text check | Verbatim |
| Conflict-Table conflicts CT-097-01-A..D are reflected in the issued Scope of Work either as resolved language or as flagged `TBD`s | Manual review | All four addressed |
| No unsourced numeric or normative statement | Provenance pass | Every clause cites a source or carries `TBD` |
| `_STATUS.md` transitioned `OPEN → INITIALIZED` only via `tools/scaffolding/write_status.sh` | Run-record review | Recorded |

## Records

- The issued Scope-of-Work document (this deliverable's primary artifact).
- The tagged-equipment list (companion).
- The responsibility-assignment record (companion).
- The integration narrative (companion or appendix).
- A run record under `_run_records/` capturing the run timestamp, the pass directive (`P1_P2`), source slices consulted, and any conflict-table entries created or updated.
- `_STATUS.md` history line recording the state transition.
