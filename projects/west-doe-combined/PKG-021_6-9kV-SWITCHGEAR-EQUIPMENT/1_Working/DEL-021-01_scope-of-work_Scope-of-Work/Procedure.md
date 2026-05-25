# Procedure: DEL-021-01_scope-of-work

This procedure describes the steps to **produce** the EPC Scope of Work artifact for `PKG-021` (6.9kV SWITCHGEAR EQUIPMENT). It is not a vendor engineering or construction execution procedure; those are produced under `DEL-021-04` and `DEL-021-03` respectively.

## Prerequisites

- Accepted upstream snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Local access to:
  - `DELIVERABLE_REGISTER.csv` row `DEL-021-01_scope-of-work`.
  - `PACKAGE_REGISTER.csv` row `PKG-021`.
  - `INTERFACE_REGISTER.csv` rows for `PKG-021` (`IFC-9D7DF96637`, `IFC-2ACD080082`, `IFC-B44478ADB6`, `IFC-FC8113A0CE`, `IFC-9E975838A2`, `IFC-A795E61D99`).
  - `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-021-01_scope-of-work` (package-heuristic mapping).
- Local access to the DBM electrical source slices in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (medium-voltage services table, electrical buildings list, 6.9 kV MCC paragraph, grounding paragraph, MV cable table, plant distribution paragraph, electrical/instrumentation specifications table, short-circuit study row).
- Deliverable-local truth-set files present: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` (placeholder).
- `_STATUS.md` `Current State` is `OPEN` or `INITIALIZED` (overwrite-safe per skill contract).
- No declared upstream dependencies are blocking (per `_DEPENDENCIES.md`).

## Steps

1. **Confirm identity.** Populate the Scope of Work identification block from `_CONTEXT.md` and `PACKAGE_REGISTER.csv` (deliverable ID, name, parent package, workbook row 23, WBS 01, CoA 26020-01-30-012, discipline Electrical, deliverable type EPC Scope of Work, responsible party EPC Integrator, scope item `SOW-0022`).
2. **State responsibility split.** Copy the responsibility narrative from `PACKAGE_REGISTER.csv` row `PKG-021` verbatim in substance: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination.
3. **State package function.** Use the DBM medium-voltage services table to state: 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded service supporting facility process AC inverter-drive motors rated 5,500 hp and above, including the KM-2150/2250 Inlet/Sales Gas Compressor motors driven via Starting VFDs with synchronous transfer to a normal-service bus.
4. **Locate the package in the facility.** Reference the 820-1 6.9kV Inlet/Sales Compressor Electrical Building (shop-fabricated prefab) from the DBM electrical buildings list as the package home, elevated on piles with bottom cable entry.
5. **State the upstream tie-in.** Use the DBM plant distribution paragraph to describe radial feed from the 13.8 kV plant main switchgear via a 13.8 kV / 6.9 kV step-down transformer to the 6.9 kV electrical building.
6. **Populate the interface list.** Insert all six `INTERFACE_REGISTER.csv` interface facts for `PKG-021`: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports. Cite the IFC IDs.
7. **Record statements-of-design from source.** Include the DBM-stated design constraints: no PFC capacitor banks on the MCC-8200 synchronous-transfer bus; mechanically latched fused contactors with motor protection relays and Ethernet port to the plant PLC; 6.9 kV MV cable is three-conductor copper TECK rated 8 kV / 100% insulation, shielded; each 6.9 kV transformer grounded with 100 A, 10 s NGR operating as a tripping system.
8. **List governing specifications.** Include ELC-QAS-000007-001 Medium Voltage Switchgear, ELC-QAS-000008-001 Medium Voltage Motor Control Centers, ELC-QAS-000005-001 Medium Voltage Induction Motors (adjacent), CEC, and project electrical specifications. Mark clause-level requirements `TBD` until specification text is locally accessible.
9. **Mark open items as TBD.** Bus rating, breaker count, interrupting capacity, protective relay settings, exact installation room, and package-specific exclusions are `TBD`; record them as open items rather than inventing values. Cross-reference the short-circuit study row in DBM as the resolution path.
10. **Declare downstream EPC handoffs.** Name `DEL-021-02` (Package Datasheet), `DEL-021-03` (Construction Work Package), `DEL-021-04` (Vendor Engineered Equipment Package), `DEL-021-05` (Vendor Document Turnover Package), and `DEL-021-06` (EPC Vendor Package Review and Acceptance) as the downstream uses of this Scope of Work.
11. **Record conflicts.** Add any source/decomposition conflicts to the Conflict Table in `Guidance.md` (e.g., Ariel frame KBC/6 vs. KBZ/6; 6,700 hp vs. 7,000 hp motor; unstated package exclusions). Do not silently reconcile.
12. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, function statement, interface list, and TBDs.
13. **Update status (safe).** When current `_STATUS.md` state is `OPEN`, update to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Do not regress state.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| Identity completeness | Compare Scope of Work identification to `_CONTEXT.md`, `PACKAGE_REGISTER.csv`, and `DELIVERABLE_REGISTER.csv`. | All fields match accepted values. |
| Interface completeness | Compare interface list to `INTERFACE_REGISTER.csv` rows for `PKG-021`. | All six interface facts present with IFC IDs. |
| Source fidelity | Trace each non-trivial statement to a cited DBM section or Gate 7 register row. | All non-trivial statements cite source; unsupported values are `TBD` or `ASSUMPTION`. |
| Responsibility split | Compare narrative to `PACKAGE_REGISTER.csv` row `PKG-021`. | Vendor and EPC scopes not conflated. |
| Conflict capture | Inspect Guidance Conflict Table. | All source/decomposition conflicts are listed with proposed authority and human-ruling marker. |
| Cross-document consistency | Compare names, IDs, function statements, and TBDs across Datasheet, Specification, Guidance, Procedure. | No unresolved internal inconsistency. |
| Status safety | Inspect `_STATUS.md` history. | Transition only from `OPEN` to `INITIALIZED`, no regression. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (when safe) with the `OPEN → INITIALIZED` transition and history line.
- TASK run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_2026-05-24_<HHMM>.md`.
- Conflict Table entries in `Guidance.md` for human ruling.
