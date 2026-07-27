# Decomposition Coverage Report

## Audit identity

| Field | Value |
|---|---|
| Run label | `ROOT_PROJECT_SETUP_DEL0206_POST` |
| Variant | `SOFTWARE` |
| Scope | `ALL` |
| Decomposition revision | `v1.1` |
| Expected source snapshot | `execution/_ScopeChange/SCA-001_2026-07-26_1454/` |
| Expected handoff phase | `PROJECT_SETUP_DEL-02-06_CLOSEOUT` |
| Derivative status | Audit evidence only; not authoritative decomposition truth |

## Outcome

`PASS` for PROJECT_SETUP decomposition/filesystem closure. All 6 packages and
all 46 deliverables have exact declared folders; all 46 contexts match their
accepted register entries; the former DEL-02-06 absent-scaffold blocker is
cleared; stable IDs are unique; every tested register and trace reference
resolves.

## Check verdicts

| Check | Verdict | Evidence |
|---|---|---|
| 1 — Forward coverage: packages | `PASS` | §8 declares 6 packages; all 6 exact package folders exist. |
| 2 — Forward coverage: deliverables | `PASS` | §9/register declare 46 deliverables; all 46 exact folders exist. DEL-02-06 is present under PKG-02. |
| 3 — Reverse coverage: folders | `PASS` | 6 package folders and 46 deliverable folders all trace to declarations; no reverse-only folder. |
| 4 — ID consistency | `PASS` | Folder IDs match declarations. No duplicate/reused package, deliverable, scope-item, objective, or reverse-trace unit ID. |
| 5 — Context fidelity | `PASS` | 46/46 `_CONTEXT.md` files present and exact across name, package, type, responsible party, description, artifacts, scope, objectives, `ContextEnvelope`, envelope notes, and write locus. |
| 6 — Artifact presence and contract form | `PASS` (138 INFO) | 45/45 present contracts validate as `SOW_V1`; no ambiguous dual format. DEL-02-06 has no SOW by authorized scaffold-only design. All 137 anticipated production outputs remain absent at `INITIALIZED`/`OPEN`. |
| 7 — Objective mapping | `PASS` | 7/7 objectives have existing supporting deliverables; objective register and deliverable register mappings agree exactly; no support-only-retired objective. |
| 8 — Scope-ledger integrity | `PASS` | 104/104 unique rows; 95 IN and 9 OUT; every package, deliverable, objective, and cross-register scope reference resolves. |
| 9 — Derivative-package parity | `SKIPPED` | Not variant-owned for `SOFTWARE`, per AUDIT_DECOMP Step 9. |
| 9b — Package-shape conformance | `PASS` | §3 labels canonical/companion roles, Markdown carries summaries rather than heavy duplicate truth, and no derived publication is treated as authority. |
| 10 — Active snapshot/handoff | `PASS` | `_ScopeChange/_LATEST.md` points uniquely to the expected SCA-001 snapshot; required artifacts exist; its scope-change-only handoff is conservative and does not overclaim. |
| 11 — Lifecycle distribution | `PASS` (informational) | 45 `INITIALIZED`, 1 `OPEN`, 0 unknown/retired/in-progress-or-later. |

## Required closure propositions

1. **Topology:** `6/6` packages and `46/46` deliverables.
2. **Context:** `46/46` exact parity; no warning-producing semantic inference.
3. **Former blocker:** DEL-02-06 folder exists with `_CONTEXT.md`,
   `_STATUS.md`, `_SEMANTIC.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and
   `_MEMORY.md`.
4. **Identity:** zero duplicate or reused IDs in the accepted topology,
   companion registers, filesystem, or reverse-trace inventory.
5. **Mapping closure:** zero unresolved references across the scope ledger,
   deliverable register, objective register, forward coverage, and reverse
   trace.
6. **Production boundary:** DEL-02-06 `ScopeOfWork.md` is absent because no SOW
   authoring was authorized in this tranche; the folder is correctly `OPEN`.

## What to fix for a cleaner rerun

Nothing is required for PROJECT_SETUP closeout. A later authorized production
activation may author DEL-02-06's ScopeOfWork and then produce anticipated
artifacts, but doing so is outside this audit and outside the scaffold tranche.
