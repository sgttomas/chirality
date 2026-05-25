# Procedure — DEL-031-01 Scope of Work (PKG-031 Transformer TXP-8500-1)

This procedure describes the steps to **produce** the SoW deliverable (the four anticipated artifacts) for PKG-031. Production by a human author is assumed; agent-produced content remains a proposal until human acceptance.

## Prerequisites

- Read deliverable-local files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`. [Source: deliverable folder]
- Read Gate 7 PROJECT_DECOMP snapshot rows for PKG-031:
  - `PACKAGE_REGISTER.csv` row `PKG-031`
  - `DELIVERABLE_REGISTER.csv` rows `DEL-031-01` through `DEL-031-06`
  - `INTERFACE_REGISTER.csv` rows for PKG-031 (7 interface types)
  - `ARTIFACT_REGISTER.csv` rows for DEL-031-01 (4 artifacts)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-031-01
  - `SCOPE_LEDGER.csv` row `SOW-0032`
- Read DBM source slice: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis sections, specifically Power Distribution (lines 2917–2929), System Voltages (line 2937), 600 V MCC (line 2959), Electrical Buildings (lines 2973, 2977), Area Classification (lines 2905–2913), and Grounding (lines 2985, 2991).
- Declared upstream dependencies: none. Declared downstream dependencies: none. [Source: `_DEPENDENCIES.md`]
- No deliverable-specific source slices were copied during PREPARATION; production must rely on shared `_Sources/` and Gate 7 registers. [Source: `_REFERENCES.md`]

## Steps

1. **Establish package identity.** Compose the identity block from `PACKAGE_REGISTER.csv` row `PKG-031`: tag TXP-8500-1, package name, WBS 01, CoA tracking number 26020-01-30-022, workbook row 33, discipline Electrical.
2. **State the package function.** Restate the 13.8 kV → 600 V step-down role using DBM-Deepcut Power Distribution and System Voltages narrative (lines 2919, 2937, 2959). Cite the DBM section.
3. **State the package boundary.** Upstream interface = 13.8 kV facility distribution radial feed from the plant main 13.8 kV switchgear. Downstream interface = 600 V MCC for LV loads. Cite DBM-Deepcut Power Distribution narrative.
4. **Compose the integration narrative.** Locate the package within a prefabricated modular electrical building (DBM-Deepcut Electrical Buildings, lines 2973, 2977), under the general area classification basis Class I Zone 2 IIA/IIB (DBM-Deepcut Area Classification, lines 2905–2913). Note raceway separation requirements between power and control/instrument circuits.
5. **Enumerate interface types.** List all 7 declared interface types for PKG-031 from `INTERFACE_REGISTER.csv`: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Use these as the section structure for the integration narrative.
6. **Compose the RACI / responsibility assignment record.** Transcribe the PACKAGE_REGISTER.csv RACI text verbatim where practical: Package Vendor owns package engineering, package design, vendor documentation, physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration.
7. **Record objective associations as ASSUMPTION.** List OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 from `OBJECTIVE_DELIVERABLE_MAP.csv`; label as best-effort package-grouped association per the skill's `PACKAGE_HEURISTIC` rule.
8. **State the grounding basis.** Record that the 600 V secondary is HRG with a 5 A continuous resistor at the transformer neutral and that 600 V ground-fault protection is alarm-only (DBM-Deepcut Grounding, line 2985).
9. **Explicitly carry exclusions.** Reflect the package-row exclusion stance "TBD; no package-specific exclusions stated in source materials." Add the standing out-of-scope items: detailed package engineering/design (`DEL-031-04`), Package Datasheet (`DEL-031-02`), Construction Work Package (`DEL-031-03`), Vendor Document Turnover Package (`DEL-031-05`), and EPC Vendor Package Review and Acceptance (`DEL-031-06`).
10. **Mark unresolved items.** Mark transformer construction parameters (form factor, cooling, impedance, BIL, taps, accessories), detailed environmental conditions, and the 600/347 V vs. 3-wire-HRG secondary-configuration question as `TBD` and route them to `DEL-031-02` and `DEL-031-04`.
11. **Compose the four anticipated artifacts.** Produce or update:
    - `ART-38263068FC` Package scope of work
    - `ART-C52F26582F` Tagged equipment and package identity list
    - `ART-F816DB4F10` Package function and whole-facility integration narrative
    - `ART-23AA8A388B` Package responsibility assignment record
12. **Cross-check four-document consistency.** Confirm identity values (tag, MVA, voltages, WBS, tracking number) are identical across `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`. Confirm interface inventory matches `INTERFACE_REGISTER.csv` exactly.
13. **Surface conflicts.** Add or update the Conflict Table in `Guidance.md` for any source disagreements found; do not silently reconcile.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| Identity values consistent across four documents | Inspection | Tag, MVA, voltages, WBS, tracking number, package row identical. |
| Interface inventory matches register | Comparison to `INTERFACE_REGISTER.csv` rows for PKG-031 | All 7 interface types present, none added. |
| Function statement matches DBM-Deepcut electrical basis | Comparison to DBM-Deepcut Power Distribution / System Voltages | Function statement cites the 13.8 kV → 600 V step-down narrative and the 600 V HRG service. |
| RACI matches package register | Comparison to `PACKAGE_REGISTER.csv` RACI text | Vendor vs. Integrator split reproduced. |
| Objective associations labeled ASSUMPTION | Inspection | OBJ-001/004/005/006/008/009/010 labeled package-grouped ASSUMPTION. |
| Grounding statement cites DBM | Inspection | 5 A continuous HRG resistor and alarm-only GF protection cited to DBM-Deepcut line 2985. |
| Unresolved items marked TBD or routed to Conflict Table | Inspection | No invented transformer parameters; downstream routing stated. |
| Status update safe-rule honored | Inspection of `_STATUS.md` | OPEN → INITIALIZED only after Pass 1+2 success. |

## Records

- Four production artifacts (per ARTIFACT_REGISTER.csv) embedded in or referenced by the four-document kit.
- Updated `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in this deliverable folder.
- `_STATUS.md` History line for the OPEN → INITIALIZED transition (when applicable).
- TASK run record at `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md` capturing inputs, outputs, conflicts, and tool usage.
