# Procedure: DEL-028-03_construction-work-package — Construction Work Package

**Interpretation:** This procedure describes the steps to **produce** the Construction Work Package document set for PKG-028. Steps describing how to physically construct TXP-8801-1 in the field belong in the workface plan and vendor IOM and are referenced rather than reproduced here.

## Prerequisites

1. **Declared upstream dependencies:** none declared during PREPARATION (per `_DEPENDENCIES.md`).
2. **Practical upstream references (not declared as blockers):**
   - DEL-028-01 (Scope of Work) — package scope, tagged-equipment basis, integration narrative.
   - DEL-028-02 (Package Datasheet) — EPC-authored technical handoff and interface requirements matrix.
   - DEL-028-04 (Vendor Engineered Equipment Package) and DEL-028-05 (Vendor Document Turnover Package) — vendor IOM, factory test report, and final equipment data.
3. **Accessible reference material:**
   - Gate 7 PROJECT_DECOMP snapshot (DELIVERABLE_REGISTER, PACKAGE_REGISTER, ARTIFACT_REGISTER, INTERFACE_REGISTER, OBJECTIVE_DELIVERABLE_MAP).
   - DBM-Deepcut §§2745, 2919, 2985, 2991.
4. **Deliverable-local truth set:** `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` read at run start.

## Steps

1. **Read deliverable-local context and references.** Confirm equipment tag (TXP-8801-1), rating (7.5 MVA, 13.8 kV / 4160 / 2400 V), discipline (Electrical), responsible party (EPC Integrator), declared interface types, and anticipated artifacts.
2. **Locate package and artifact basis in the Gate 7 registers.** Confirm the DEL-028-03 row, the three anticipated artifacts (ART-C0CF6D35AA, ART-D64770700D, ART-790F01D335), and the seven INTERFACE_REGISTER rows for PKG-028.
3. **Locate authoritative DBM-Deepcut source slices.** Foundation typology (§2745), 13.8 kV distribution context (§2919), transformer grounding scheme (§2985), and CEC ground-conductor requirement (§2991).
4. **Draft the CWP narrative.**
   - Package identity, function, and integration into the plant 13.8 kV distribution architecture.
   - Construction scope boundary against vendor scope (DEL-028-04) and EPC vendor-acceptance scope (DEL-028-06).
5. **Draft the installation and tie-in workface plan (ART-D64770700D) outline.** Receipt and inspection → rigging and setting on foundation → grounding/bonding tie-in → primary 13.8 kV termination → secondary 4160 V and 2400 V terminations → control / communications wiring → pre-energization tests → energization and turnover. Mark detailed step contents `TBD` pending vendor IOM and EPC ITP.
6. **Draft the construction interface and turnover checklist (ART-790F01D335).** One row per declared interface type for PKG-028 (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports), each with construction-side acceptance criteria and sign-off slot.
7. **Cross-check.** Reconcile Datasheet attributes, Specification requirements, Guidance principles, and Procedure steps against the Gate 7 registers and DBM-Deepcut slices. Capture any unresolved tensions in the Conflict Table in `Guidance.md`.
8. **Surface gaps as TBD / ASSUMPTION / HRR.** Vendor technical attributes, exact grounding scheme for 4160 V / 2400 V secondaries, and adjacent-package interface owners are left as Human Ruling items (HRR-028-03-001/002/003).
9. **Update `_STATUS.md`** from `OPEN` → `INITIALIZED` per the safe-update rule (Pass 1/2 completed; current state was `OPEN`).
10. **Persist the run record** at `_run_records/TASK_RUN_2026-05-24_<HHMM>.md`.

## Verification

| Check | Method |
|---|---|
| Datasheet, Specification, Guidance, Procedure all present | File presence in `{DELIVERABLE_PATH}` |
| Default schema sections present in each | Section heading inspection |
| Identification grounded in `_CONTEXT.md` and PACKAGE_REGISTER | Cross-reference against source |
| All seven declared PKG-028 interface types appear in Specification REQ-028-03-003 | Read Specification |
| Foundation type cited against DBM-Deepcut §2745 | Read Datasheet / Specification |
| Grounding requirement cited against DBM-Deepcut §2985 / §2991 | Read Specification REQ-028-03-004 / 005 |
| Unsupported attributes marked `TBD`; inferences labeled `ASSUMPTION`; conflicts captured | Read Datasheet, Guidance Conflict Table |
| Status updated `OPEN` → `INITIALIZED` via `tools/scaffolding/write_status.sh` | Read `_STATUS.md` |
| No writes outside `{DELIVERABLE_PATH}` | Run record audit |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` (updated)
- `_run_records/TASK_RUN_2026-05-24_<HHMM>.md`
