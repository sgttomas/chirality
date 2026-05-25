# Procedure — DEL-016-01 Scope of Work (PKG-016 Transformer TXP-8200-1)

This procedure describes the steps to **produce** the SoW deliverable (the four anticipated artifacts) for PKG-016. Production by a human author is assumed; agent-produced content remains a proposal until human acceptance.

## Prerequisites

- Read deliverable-local files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`. [Source: deliverable folder]
- Read Gate 7 PROJECT_DECOMP snapshot rows for PKG-016:
  - `PACKAGE_REGISTER.csv` row `PKG-016`
  - `DELIVERABLE_REGISTER.csv` rows `DEL-016-01` through `DEL-016-06`
  - `INTERFACE_REGISTER.csv` rows for PKG-016 (7 interface types)
  - `ARTIFACT_REGISTER.csv` rows for DEL-016-01 (4 artifacts)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-016-01
  - `SCOPE_LEDGER.csv` row `SOW-0017`
- Read DBM source slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 (Electrical Basis), specifically System Voltages and Incoming Power and Transformers; supporting reads from SEC-08 (Buildings, Foundations).
- Declared upstream dependencies: none. Declared downstream dependencies: none. [Source: `_DEPENDENCIES.md`]
- No deliverable-specific source slices were copied during PREPARATION; production must rely on shared `_Sources/` and Gate 7 registers. [Source: `_REFERENCES.md`]

## Steps

1. **Establish package identity.** Compose the identity block from `PACKAGE_REGISTER.csv` row `PKG-016`: tag TXP-8200-1, package name, WBS 02, tracking number 26020-02-30-007, workbook row 18, discipline Electrical.
2. **State the package function.** Restate the 13.8 kV → 600 V step-down role using the exact DBM SEC-12 row (`13.8 kV to 600V, 3 MVA transformer | 600V MCC for LV loads`). Cite the DBM section.
3. **State the package boundary.** Upstream interface = 13.8 kV cross-facility feed sub-fed from 04-25 Main Switchgear. Downstream interface = 600 V MCC for LV loads. Cite DBM SEC-12.
4. **Compose the integration narrative.** Locate the package within the 600 V electrical building context (DBM SEC-08), under the general area classification basis Class I Zone 2 IIA/IIB (DBM SEC-12). Note raceway separation requirements between 13.8 kV/4.16 kV/600 V power and control/instrument circuits.
5. **Enumerate interface types.** List all 7 declared interface types for PKG-016 from `INTERFACE_REGISTER.csv`: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Use these as the section structure for the integration narrative.
6. **Compose the RACI / responsibility assignment record.** Transcribe the PACKAGE_REGISTER.csv RACI text verbatim where practical: Package Vendor owns package engineering, package design, vendor documentation, physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration.
7. **Record objective associations as ASSUMPTION.** List OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 from `OBJECTIVE_DELIVERABLE_MAP.csv`; label as best-effort package-grouped association per the skill's `PACKAGE_HEURISTIC` rule.
8. **Explicitly carry exclusions.** Reflect the package-row exclusion stance "TBD; no package-specific exclusions stated in source materials." Add the standing out-of-scope items: detailed package engineering/design (`DEL-016-04`), Package Datasheet (`DEL-016-02`), Construction Work Package (`DEL-016-03`), Vendor Document Turnover Package (`DEL-016-05`), and EPC Vendor Package Review and Acceptance (`DEL-016-06`).
9. **Mark unresolved items.** Mark transformer construction parameters (form factor, cooling, impedance, BIL, taps, accessories), detailed environmental conditions, and the 600/347 V vs. 3-wire-HRG secondary-configuration question as `TBD` and route them to `DEL-016-02` and `DEL-016-04`.
10. **Compose the four anticipated artifacts.** Produce or update:
    - `ART-9B23EFA6EE` Package scope of work
    - `ART-65C8336085` Tagged equipment and package identity list
    - `ART-4E2F8A9FDF` Package function and whole-facility integration narrative
    - `ART-F610CDF9EC` Package responsibility assignment record
11. **Cross-check four-document consistency.** Confirm identity values (tag, MVA, voltages, WBS, tracking number) are identical across `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`. Confirm interface inventory matches `INTERFACE_REGISTER.csv` exactly.
12. **Surface conflicts.** Add or update the Conflict Table in `Guidance.md` for any source disagreements found; do not silently reconcile.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| Identity values consistent across four documents | Inspection | Tag, MVA, voltages, WBS, tracking number, package row identical. |
| Interface inventory matches register | Comparison to `INTERFACE_REGISTER.csv` rows for PKG-016 | All 7 interface types present, none added. |
| Function statement matches DBM SEC-12 row | Comparison to DBM SEC-12 Incoming Power and Transformers | Function statement cites the `13.8 kV to 600V, 3 MVA transformer` row. |
| RACI matches package register | Comparison to `PACKAGE_REGISTER.csv` RACI text | Vendor vs. Integrator split reproduced. |
| Objective associations labeled ASSUMPTION | Inspection | OBJ-002/004/005/006/008/009/010 labeled package-grouped ASSUMPTION. |
| Unresolved items marked TBD or routed to Conflict Table | Inspection | No invented transformer parameters; downstream routing stated. |
| Status update safe-rule honored | Inspection of `_STATUS.md` | OPEN → INITIALIZED only after Pass 1+2 success. |

## Records

- Four production artifacts (per ARTIFACT_REGISTER.csv) embedded in or referenced by the four-document kit.
- Updated `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in this deliverable folder.
- `_STATUS.md` History line for the OPEN → INITIALIZED transition (when applicable).
- TASK run record at `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md` capturing inputs, outputs, conflicts, and tool usage.
