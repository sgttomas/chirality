# Procedure — DEL-098-03 Construction Work Package

> Pass: P1_P2 (initial draft + cross-reference). Operational steps to **produce** the Construction Work Package artifact (the document set) for PKG-098 (Tanks, Sour Water, API 650, 3-25 — `26020-03-PT-19-007`). The CWP itself, once issued, describes the **field execution** sequence; the production-side procedure follows below.

## Purpose

Produce the Construction Work Package master document, the installation and tie-in workface plan, and the construction interface and turnover checklist, in a form that EPC field execution and turnover can run against without further engineering interpretation.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present (PREPARATION complete). Confirmed.
- Declared upstream dependencies: none declared during PREPARATION (`_DEPENDENCIES.md`). Effective upstream inputs:
  - Vendor engineering deliverables for `26020-03-PT-19-007` (full list under `26020-Package_Requirements.docx` heading 50; IFC revisions required for tie-in execution; ASSUMPTION on revision-state).
  - Decomposition snapshot GATE-07 (PACKAGE_REGISTER, DELIVERABLE_REGISTER, INTERFACE_REGISTER, ARTIFACT_REGISTER, OBJECTIVE_DELIVERABLE_MAP).
  - SOW items SOW-0221, SOW-0222, SOW-0223, SOW-0224 text — location TBD locally.
  - Project HSE plan, project construction execution plan, project quality plan — location TBD.
  - Site-final geotechnical report (DBM §Civil line 688 cites this as required before foundation closure).
- Access to vendor `MEC-`, `STR-`, `PIP-`, `INS-`, `ELE-`, `PLN-`, `CTL-`, `CIV-`, `PRO-`, `QLT-`, `PRQ-`, `DOC-` deliverable categories enumerated in `26020-Package_Requirements.docx` heading 50.

## Steps

S-01. **Confirm package boundary.** Reconcile DEL-098-03 scope statement (Item 1 only) against vendor heading-50 listing (Items 1–3) per Guidance CT-01; document final boundary in CWP §Scope.

S-02. **Assemble vendor input register.** From `26020-Package_Requirements.docx` heading 50 Vendor Engineering Deliverables, list each deliverable (MEC/STR/PIP/INS/ELE/PLN/CTL/CIV/PRO/QLT/PRQ/DOC IDs) with required revision state, receipt date, and CWP-section consumer. Output: CWP §Input Register.

S-03. **Build SOW-to-workpack matrix.** Map each of SOW-0221..SOW-0224 to one or more workpacks (e.g., FND-001 Foundations, ERC-001 Tank Erection, COAT-001 Coating Touch-Up, INS-001 Insulation/EHT, PIP-001..N Process Tie-ins, INST-001 I&C, ELE-001 Electrical, CIV-001 Containment/Grading, COMM-001 Cathodic Protection, HYD-001 Hydrotest, TO-001 Turnover). Output: CWP §SOW Traceability Matrix. SOW text not locally available → mapping rationale TBD until SOW source confirmed.

S-04. **Draft foundation/erection workface plan.** Reference vendor `STR-005`/`STR-006`/`STR-013` and `MEC-017`/`MEC-018`; sequence: grading & survey → footings/ring-wall → cure → anchor-bolt embedment → release-to-erect → bottom plate → shell → roof → internals (Kennilworth skim) → coating touch-up. Output: CWP §Workface Plan / Mechanical Erection.

S-05. **Draft coating, insulation, and EHT workface plan.** Sequence: coating inspection at receipt → erection-related touch-up per coating manufacturer → hydrotest first → EHT installation → insulation/cladding → continuity tests. Sources: `26020-Package_Requirements.docx` heading 50 (coating, insulation, EHT); DBM §Site Basis. Output: CWP §Coating/Insulation/EHT Plan.

S-06. **Draft hydrotest plan.** Per vendor `PIP-024`; address test medium, fill rate, hold time, acceptance, freeze risk, test-water disposal. Detail TBD pending vendor procedure and project HSE plan. Output: CWP §Hydrotest Plan.

S-07. **Draft tie-in / interface workface plan.** For each Yes-interface (Process Piping, Relief/Flare/Vent, Drain/Containment, Grounding/Bonding, Lighting, Cathodic Protection, I&C/Control Cabling, Grading/Spill Containment, Structural/Foundations/Supports), reference vendor drawing IDs; populate a tie-in walkdown register from `PIP-004` Tie-In List. Note interface-table source line for Lighting: `26020-Packages_Interfaces.3.xlsx` column M row 93. Output: CWP §Tie-in/Interface Plan.

S-08. **Draft E&I installation plan.** Reference `INS-002`/`INS-006`/`INS-008`/`INS-011`/`INS-018`/`INS-029` and `ELE-012`/`ELE-017`/`ELE-019`. Output: CWP §E&I Installation Plan.

S-09. **Compile inspection & test plan (CWP-level ITP).** Roll up vendor `QLT-003` ITP with field activities: weld NDE, coating DFT/holiday, anchor-bolt torque, hydrotest, EHT continuity, earthing resistance, CP energization, loop checks, lighting illumination survey. Output: CWP §ITP.

S-10. **Compile turnover & mechanical-completion checklist.** Consolidate vendor `QLT-020` Inspection Release Certificate, `QLT-013` MTRs, `QLT-021` Manufacturing Record Book, `MEC-023`/`PRQ-016` Vendor Data Book, plus field execution records. Define mechanical completion boundary, system completion boundary, and ready-for-commissioning handover criteria. Output: CWP §Turnover Checklist.

S-11. **Cross-document QA on the CWP itself.** Verify CWP scope ↔ Specification ↔ Guidance ↔ Datasheet consistency (terminology, tank tag IDs, design conditions). Resolve or escalate any inconsistency per Guidance Conflict Table.

S-12. **Issue CWP for review.** Route through EPC PM, Construction Manager, QA/QC Lead, Commissioning Lead, HSE Lead. Capture comments; revise. Issue IFC.

S-13. **Register run record.** Create `_run_records/TASK_RUN_<date>_<HHMM>.md` summarizing pass directive, sources consulted, outputs produced, status update, RUN_STATUS.

S-14. **Status update (safe).** If `_STATUS.md` Current State is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh`. If not `OPEN`, skip and record reason.

## Verification

| Step | Verification |
|---|---|
| S-01 | CWP §Scope explicitly enumerates tank tag IDs and adjudicates CT-01. |
| S-02 | Input Register row count matches vendor deliverable list under heading 50; each row carries a CWP-section consumer. |
| S-03 | Each SOW-0221..SOW-0224 maps to ≥1 work pack; reverse: every work pack traces to ≥1 SOW. |
| S-04..S-08 | Each workface-plan section references vendor drawing ID(s); no orphan steps. |
| S-09 | ITP coverage: every Specification R-* requirement has at least one ITP row (excluding R-19 which is mapping-only). |
| S-10 | Turnover checklist includes vendor and field documentation categories. |
| S-11 | Cross-document terminology check passes (tank IDs, design conditions, coating spec, skim system name). |
| S-12 | Review comments closed; IFC issuance recorded. |
| S-13 | `_run_records/TASK_RUN_*.md` exists with RUN_STATUS. |
| S-14 | `_STATUS.md` updated only when current state was `OPEN`; history line appended. |

## Records

- This deliverable's four-document set: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
- Run record: `_run_records/TASK_RUN_2026-05-25_<HHMM>.md`.
- `_STATUS.md` updated per safe-update rules.
- (Downstream / field-execution records — produced during construction, not by this skill — listed under Specification §Documentation.)
