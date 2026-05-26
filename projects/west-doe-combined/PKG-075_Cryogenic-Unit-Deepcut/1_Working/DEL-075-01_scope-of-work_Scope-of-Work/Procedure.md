# Procedure — DEL-075-01 Scope of Work (PKG-075 Cryogenic Unit "Deepcut")

## Purpose

This procedure describes the steps the EPC Integrator uses to **produce, issue, and maintain** the PKG-075 Scope of Work deliverable. It is operational (how to author and govern the SoW), not an operating procedure for the cryogenic unit itself. (Per the four-documents skill interpretation rule: procedure may describe steps to produce the deliverable artifact or to use/operate it. For this deliverable, "produce" is primary, since the artifact is itself a definitional document.)

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` for this deliverable.
- Access to the locally accessible source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-06 "UltraTEF Cryogenic Recovery Basis", lines 1293-1396; and SEC-06 intro lines 1098-1115).
- Access to the accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (deliverable register row 276; package register; objective-deliverable map).
- Awareness that `_Sources/26020-Package_Requirements.docx` heading 29 is a referenced source not currently in machine-readable form; content depending solely on it is `TBD`.
- No human-declared upstream/downstream dependencies are recorded in `_DEPENDENCIES.md` at this time; PKG-075 sibling deliverables (DEL-075-02..06) are downstream consumers of this SoW.

## Steps

1. **Confirm scope and authority.** Confirm DeliverableID, ParentPackageID, Discipline, Type, Responsible Party, and Covers/Supports lists in `_CONTEXT.md` against the deliverable register row. If any differ, surface the discrepancy; do not silently reconcile.
2. **Read the source slice.** Open SEC-06 "UltraTEF Cryogenic Recovery Basis" in DBM-Deepcut (lines 1293-1396) and the SEC-06 introduction (lines 1098-1115). Identify package function, design point, inlet/sales conditions, equipment list, operating modes, interfaces, and open items.
3. **Populate Datasheet.md** (Identification, Attributes, Conditions, Construction, References). Anchor every non-trivial value to a DBM source line. Where a tag number, value, or qualifier is not in the source slice, write `TBD`.
4. **Populate Specification.md** (Scope, Requirements R-01..R-23, Standards, Verification, Documentation). Make each requirement source-anchored; label any inferred requirement `ASSUMPTION`; mark unsourced contractual requirements `TBD` (especially those that would live in Package_Requirements.docx heading 29).
5. **Populate Guidance.md** (Purpose, Principles, Considerations, Trade-offs, Examples, Conflict Table). Translate the design-basis intent into directional guidance for vendor bidders and integrator reviewers. Add a Conflict Table row for every irreconcilable item.
6. **Run a cross-document consistency sweep.** Verify: tag list in Datasheet matches the equipment named in Specification; values (flows, temperatures, pressures, recovery percentages, tray counts, pump sizing) match across Datasheet and Specification; terminology (e.g., "expander mode" / "J-T mode", "BAHX", "propane absorber", "deethanizer") is used consistently; verification approaches map back to requirements.
7. **Reconcile or defer conflicts.** Where consistency cannot be achieved from drafts alone, re-read the DBM source slice. If still unresolved, add a Conflict Table row in Guidance.md and mark the affected Specification text accordingly. Do not guess.
8. **Author the responsibility assignment record (TBD body).** Draft a RACI/RAM matrix covering EPC Integrator, Package Vendor, and other-discipline responsibilities for engineering, design, fabrication/supply, installation, integration, inspection, and turnover. Initial content is `TBD`; populate once Package_Requirements.docx and a project responsibility template are available.
9. **Update `_STATUS.md` safely.** When Pass 1/Pass 2 (P1_P2) completes successfully and current state is `OPEN`, invoke `tools/scaffolding/write_status.sh <DELIVERABLE_PATH> INITIALIZED TASK+four-documents`. Do not regress state.
10. **Persist a run record** at `_run_records/TASK_RUN_<timestamp>.md` echoing the brief, listing inputs read, outputs produced, missing items, and any human-ruling needs.
11. **Hand off downstream.** Notify DEL-075-02 (Package Datasheet), DEL-075-03 (Construction Work Package), DEL-075-04 (Vendor Engineered Equipment Package), DEL-075-05 (Vendor Document Turnover), and DEL-075-06 (EPC Vendor Package Review and Acceptance) that the SoW is at `INITIALIZED`. Do not modify those deliverables from this task scope.

## Verification

| Check | Pass criterion |
|---|---|
| File presence | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all exist in the deliverable folder. |
| Source anchoring | Every non-trivial value or requirement in Datasheet and Specification cites a DBM-Deepcut SEC-06 line (or another locally accessible source) or is marked `TBD`/`ASSUMPTION`. |
| Cross-document consistency | Equipment, values, units, and terminology are consistent across the four documents (verified via the Step 6 sweep). |
| Conflict capture | Every irreconcilable item appears in Guidance.md's Conflict Table with proposed authority and `TBD` human ruling. |
| Status safety | `_STATUS.md` transitions only `OPEN -> INITIALIZED` and only when authorized; no state regression occurs. |
| Run record | `_run_records/TASK_RUN_<timestamp>.md` exists and records inputs, outputs, missing items, and rulings. |
| Scope boundary | No file outside the deliverable folder is modified by this task. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated to `INITIALIZED` (when applicable).
- `_run_records/TASK_RUN_<timestamp>.md`.
- Downstream consumers' references back to this SoW (created by their own runs, not by this task).
