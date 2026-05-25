# Procedure — DEL-023-01 Scope of Work (PKG-023)

Operational steps to **produce** the EPC Integrator Scope of Work artifact for PKG-023 "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD". This procedure governs the authoring and review of the Scope of Work itself, not the use of the MV VFD equipment.

## Purpose

Produce a source-grounded, scope-bounded EPC Scope of Work for PKG-023 that supplies the four required artifacts (ART-D70FE712E8, ART-2C8B496DD1, ART-26BB26779C, ART-A3F647F3C3) and that downstream Gate 5 deliverables can rely on without rework.

## Prerequisites

- Read access to:
  - Gate 7 snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - This deliverable's `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- Declared upstream dependencies: none (per `_DEPENDENCIES.md`). PKG-011 (4160V Switchgear) is an ASSUMPTION-only upstream until confirmed (HRR-023-01-004).
- Pending human rulings: HRR-023-01-001 (driven service), HRR-023-01-002 (quantity/spare), HRR-023-01-003 (MV-in/MV-out interpretation), HRR-023-01-004 (PKG-011 upstream).
- Authoring agent has authority to write inside `DEL-023-01_scope-of-work_Scope-of-Work/` only.

## Steps

1. **Reconfirm identity.** From `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`, copy package ID, workbook ID, title, WBS, CoA, discipline, responsible party, scope item (SOW-0024), and supported objectives into the Datasheet Identification table. Do not paraphrase the package title.
2. **Resolve interfaces.** From `INTERFACE_REGISTER.csv`, list the six IFC rows for PKG-023 by IFC ID and interface type. Mirror the list into Specification REQ-023-01-004 and the integration narrative.
3. **Resolve artifacts.** From `ARTIFACT_REGISTER.csv`, list the four ART rows whose `Source Deliverable` is `DEL-023-01_scope-of-work`. Bind each artifact to a Scope-of-Work section.
4. **Read the Deepcut DBM slice.** Read the relevant lines of `4-25_Deepcut_DBM.md`: line 893 (Starting VFD on inlet/sales compressor), line 932-942 (sales gas booster compressor 6,700 HP / 4,000 V), lines 2957-2961 and 3088 (4.16 kV MCC posture, Zone 2 marking, motor voltage class). Use only these slices to constrain the SoW; do NOT extend slice content into driven-service claims for PKG-023.
5. **Write the integration narrative.** Compose a short narrative covering: (a) package function as stated by the workbook title, (b) facility-level role per `PACKAGE_REGISTER.csv` overview, (c) the vendor/integrator responsibility split, (d) interface types, (e) explicit open items (HRR list). Keep technical ratings beyond the title `TBD`.
6. **Cross-check Datasheet ↔ Specification ↔ Guidance ↔ Procedure** for: package title verbatim; identical interface list; consistent treatment of HRR items; no requirement asserting topology, harmonic class, or driven service.
7. **Write the Conflict Table** in `Guidance.md` capturing all open conflicts (already populated in this draft) and route them to the human via the run report's `Needs Human Ruling` section.
8. **Update `_STATUS.md`** from `OPEN` to `INITIALIZED` only if the current state is `OPEN`. Append a history line.
9. **Write the run record** under `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` per AGENT_TASK format.

## Verification

| Verification | Criterion |
|---|---|
| Package title verbatim | Title string in Datasheet, Specification, Guidance, Procedure matches `PACKAGE_REGISTER.csv` (workbook row 25). |
| Interface enumeration | Six IFC IDs appear in the Datasheet Construction table and Specification REQ-023-01-004. |
| Artifact enumeration | Four ART IDs from `ARTIFACT_REGISTER.csv` appear in Datasheet and Specification documentation tables. |
| HRR routing | Each HRR-023-01-00x appears in `Guidance.md` Conflict Table and is surfaced in the run report. |
| No unsourced technical claim | No requirement or attribute asserts VFD topology, harmonic class, bypass, cooling, or driven service without a cited source slice. |
| Status discipline | `_STATUS.md` updated only when prior state was `OPEN`; history line appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in this deliverable folder.
- Updated `_STATUS.md` with appended history line.
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` capturing inputs, resolved state, outputs, missing items, HRR list, and applied changes.
- Conflict Table entries (HRR-023-01-001..004) remain open until human ruling is recorded.
