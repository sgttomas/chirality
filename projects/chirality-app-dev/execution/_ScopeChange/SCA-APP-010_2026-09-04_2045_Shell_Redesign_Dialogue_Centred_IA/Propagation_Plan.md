# SCA-APP-010 Gate-4 Propagation Plan

**State:** `AWAITING_OWNER_APPROVAL`
**Gate-3 approval:** `Decision_Log.md` G3-CONFIRM, 2026-09-04
**Gate-3 approval basis:** `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`
**Variant:** `SOFTWARE`
**Snapshot:** `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/`
**Approved action ledger:** `Amendment_Actions.csv`, SHA-256 `8b579266d3a4f7b73c093467691f2f9d7fe140bf8a0cb6f5d7c6c1ac2ef0a109`, 30 rows (25 MODIFY, 5 ADD)

This plan is limited to the approved write scope. It names what Gate 5 writes
directly, what it materialises as snapshot evidence, and what it hands to
downstream owners. It does not describe any downstream rerun as satisfied by
the Gate-5 write pass.

## 1. Approved transaction and retained exclusions

The Gate-5 authoritative transaction is exactly the 30 actions in
`Amendment_Actions.csv`, realised as two full-file replacements:

- the decomposition, pre-image `e46084ab…` → post-image
  `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`;
- the companion register, pre-image `e47fced6…` → post-image
  `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`.

Both are regenerated at Gate 5 by `Gate3/build_gate3_candidate.py` from the
frozen pre-images; SHA parity with the approved candidates is required.

Resulting cardinalities: 10 packages, 52 deliverables, 84 scope rows
(79 `IN` / 4 `OUT` / 1 `TBD`), envelopes S9 / M41 / L2 / XL0, 8 open
issues, companion 83 rows / 50 families.

No `ADD DELIVERABLE`, `REMOVE`, `RECLASSIFY`, `MERGE`, or `SPLIT` exists, so
no PREPARATION dispatch, no lifecycle transition, no folder relocation, and no
child-closure set arises. The following stay separate and unauthorized:

- any product, frontend, runtime, test, or CSS byte (implementation is
  seated work under `LOOP_INIT.md`, selected after the owner seats it);
- any Root semantic, contract, decomposition, or register write; the Root
  notice is coordination only (§6);
- `_ScopeChange/_LATEST.md` movement (§5, pointer sub-gate);
- SCA-APP-009 derivative closure and the nine-node SCC;
- deliverable-local `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`,
  `MEMORY.md`, `_REFERENCES.md`, `Dependencies.csv`, and
  `_DEPENDENCIES.md` bytes: downstream owner writes, never SCOPE_CHANGE.

## 2. Frozen inputs

| Input | Required identity |
| --- | --- |
| Decomposition pre-image | SHA-256 `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97` |
| Approved decomposition post-image | SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` |
| Companion pre-image | SHA-256 `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70` |
| Approved companion post-image | SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` |
| Builder | `Gate3/build_gate3_candidate.py`, SHA-256 `9d4774bffb9d29798bcd25a3f43475678c727136c93c9bc51f55ba26f88cc6cf` |
| Amendment actions | SHA-256 `8b579266d3a4f7b73c093467691f2f9d7fe140bf8a0cb6f5d7c6c1ac2ef0a109` |
| Supersession delta | 11 rows, SHA-256 `c610f49478e314aeda673ec67befcc3369a50d559f98a18ddf5484a9b8449562` |
| Prior cumulative map | SCA-APP-009 `Supersession_Map.csv` (34 rows) |
| Expected cumulative map | 45 rows, SHA-256 `2045684e8d2d1aff5a46663016f07c16f0c60462c8c8d729ea3c3c1a64f8dbb6`, zero findings |
| Gate-3 independent review | `PASS`, SHA-256 `8c4b1ef94edbf2ecfbe5800a3d1a54dc801a98c3160a02b9bab81465920abec6` |
| `_LATEST.md` pre-image | SHA-256 `f235ced4526aac51c4e7f5307ac619f3500e824c3549960b106bb80b67a6e17c` (SCA-APP-009; not moved by Gate 5) |
| SCA-APP-009 snapshot tree | unchanged versus the basis |
| Authority corpus | v20, no drift; the decomposition is not a corpus member, so no bump is required |

Any mismatch is a stop, not a repair.

## 3. Package-role classification and write authority

`FUTURE_WRITE_SET.csv` (132 rows) is the machine-readable write set.

| Surface | Role | Classification | Writer |
| --- | --- | --- | --- |
| decomposition | authoritative truth | `DIRECT_EDIT` at Gate 5 (D-001) | SCOPE_CHANGE, exact post-image |
| companion register | authoritative companion | `RECOMPUTE` at Gate 5 (D-002) | SCOPE_CHANGE, exact post-image, RECONCILIATION check |
| SCA-APP-010 snapshot (36 rows S-001..S-036) | immutable decision and evidence snapshot | `DIRECT_EDIT` | SCOPE_CHANGE, AUDIT_DECOMP, RECONCILIATION |
| `_LATEST.md` (P-001) | active pointer | `NO_CHANGE` inside the transaction; pointer sub-gate later | SCOPE_CHANGE after owner ruling |
| 13 carriers × `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `MEMORY.md`, `_REFERENCES.md` (WI-001..WI-065) | working surfaces | `STALE_REBUILD_REQUIRED` after application | WORKING_ITEMS under sealed briefs; Remaining items seated by the owner |
| 13 carriers × `Dependencies.csv`, `_DEPENDENCIES.md` (DEP-001..DEP-026) | derivative metadata | `STALE_REBUILD_REQUIRED` | TASK + `dependency-extract`, report-only first |
| Root coordination notice (N-001) | cross-loop coordination | new file after owner-authorized routing | HELP_HUMAN |
| Task Management register (TM-001) | derivative label | `STALE_REBUILD_REQUIRED` (DEL-02-02 name only) | TASK_MANAGEMENT |
| `docs/CONTRACT.md`, all other authority docs | authority | `NO_CHANGE` | none |

## 4. Gate-5 prerequisites

1. Durable owner records for Gate 1 to Gate 4 and an explicit Gate-5
   execution authorization (`OWNER_ACTION_MATRIX.csv` steps 1 and 2).
2. An isolated clean branch or worktree whose basis is the approval basis or
   a verified fast-forward descendant with every frozen input exact.
3. A fresh pre-change `AUDIT_DECOMP` at the actual basis with no new blocker
   relative to the Gate-1 baseline.
4. Collision scan: `SOW-081` to `SOW-084`, `DEC-025`, `OI-008` absent from
   the live decomposition.
5. Rollback bundle of both pre-images and the pointer pre-image captured
   outside the repository with hashes.

## 5. Exact Gate-5 sequence

`OWNER_ACTION_MATRIX.csv` is normative for ownership and stop conditions.

1. **Preflight, read-only.** Record the actual basis; verify frozen inputs;
   fresh pre-change audit into `Evidence/Gate5/PRE_CHANGE_AUDIT/`.
2. **Rollback bundle** in scratch.
3. **Regenerate the candidates** with the builder into a candidate mirror;
   require SHA parity with the approved post-images.
4. **Fresh post-change audit** of the candidate mirror into
   `Evidence/Gate5/AUDIT_DECOMP/` and `Post_Change_Coverage.json`; require
   the §1 cardinalities and no new blocker or major versus step 1.
5. **Fresh independent Gate-5 review** of the candidate post-state, audit,
   and path boundary; require `PASS` with zero BLOCKER and zero MAJOR.
6. **Regenerate the cumulative supersession map**; require 45 rows, the
   expected hash, zero findings.
7. **Apply the authoritative pair** as one rollback unit; recheck both
   hashes.
8. **RECONCILIATION**: authority-corpus status (v20, no drift) and companion
   reconciliation; write `Evidence/Gate5/RECONCILIATION_REPORT.md`.
9. **Complete the snapshot**: `Decision_Log.md` (owner decisions only),
   `Handoff_State.md`, `RUN_SUMMARY.md`, `Evidence/Gate5/CHECKS.md`,
   `Evidence/Gate5/POINTER_CANDIDATE_VALIDATION.md` (literal pointer
   post-image validated without moving the live pointer), `MANIFEST.sha256`
   last.
10. **Scope backcheck**: changed paths are exactly D-001, D-002, and the
    snapshot; `_LATEST.md` and the SCA-APP-009 tree unchanged; repository
    validators pass.
11. **Freeze** and return `POINTER_SUBGATE_READY` or the blocking condition.
12. **Pointer sub-gate (separate owner act).** The pointer moves only after
    the owner dispositions SCA-APP-009's derivative closure or rules
    SCA-APP-010 the active snapshot, and answers the literal pointer
    question. Post-pointer parity backcheck is read-only.
13. **CHANGE**: stage, commit, push, and PR on owner direction; only the
    approved write set is staged.

## 6. Downstream handoffs (not executed at Gate 5)

`DOWNSTREAM_HANDOFFS.csv` is normative. In order:

1. **Owner seating.** The owner seats the Remaining items in the thirteen
   carriers: the proposals in
   `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` §7, minus the
   scope this SCA now carries in decomposition rows, adopted, amended, or
   declined per carrier with one dated history line each. Seating is an
   owner act; nothing here seats anything.
2. **WORKING_ITEMS alignment** of the thirteen carriers (WI-001..WI-065)
   under sealed briefs: re-pin `ScopeOfWork.md` `decomposition_basis` to the
   applied commit, align `project_scope_refs` and objective refs to the
   post-image rows, add a "SCA-APP-010 Gate-5 Current Contract" section in
   the DEL-02-02 form, align `_CONTEXT.md` identity and scope prose, add the
   snapshot and post-image references to `_REFERENCES.md`, and record one
   `_STATUS.md` history line. Paired `_STATUS.md` and `MEMORY.md` reads
   before any write; APP-HOLD dispatch preflight before dispatch; lifecycle,
   approval SHA, and F-APP fences untouched. Exact prose is reviewed before
   write; this plan authorizes paths and meaning, not unreviewed bytes.
3. **TASK + dependency-extract** for the thirteen carriers (DEP-001..DEP-026):
   report-only preview first; write only reviewed rows; retire rather than
   delete; stop for a separate owner transaction if any preview proposes an
   edge inside the live nine-node SCC or any Root path.
4. **AUDIT_DEP_CLOSURE — SCA-APP-010-GATE5-POST-APPLICATION.**
5. **RECONCILIATION** and **AUDIT_DECOMP** reruns after alignment, recorded
   on their own versioned surfaces; the frozen SCA-APP-010 snapshot is not
   mutated by later evidence.
6. **Root notice** (N-001): `DRAFT_NOTICE_TO_ROOT.md` is routed by
   HELP_HUMAN to `execution/_Coordination/` only after the owner authorizes
   routing; it records OI-008's three Root-owned dependencies as coordination.
7. **Task Management** (TM-001): DEL-02-02 label refresh only.
8. **Owner rulings still open:** Q15 and Q16 before the Workflows view item
   becomes selectable; SCA-APP-009 derivative closure before the pointer.
9. **Agent-index change notice:** when the DEL-08-01 instruction clauses
   (A024) are implemented under `agents/` or `skills/`, that tranche ships
   the routed notices and its G4 manifest; not a Gate-5 act.

Derivative-package state after Gate 5:

| Package | State | Owner of closure |
| --- | --- | --- |
| Decomposition, companion | `CURRENT` | SCOPE_CHANGE (applied) |
| 13 carrier working surfaces | `STALE_REBUILD_REQUIRED` | WORKING_ITEMS after owner seating |
| 13 carrier dependency registers | `STALE_REBUILD_REQUIRED` | TASK + dependency-extract |
| Dependency closure audit | `STALE_REBUILD_REQUIRED` | AUDIT_DEP_CLOSURE |
| Supersession map | `CURRENT` (45 rows) | SCOPE_CHANGE |
| Authority corpus | `CURRENT` (v20) | RECONCILIATION |
| Task Management register | `STALE_REBUILD_REQUIRED` (label) | TASK_MANAGEMENT |
| SCA-APP-009 derivative closure | `OPEN_PENDING_DERIVATIVE_CLOSURE` (its own state; unchanged by this SCA; no deferral has been ruled) | owner and the SCA-APP-009 downstream owners |

Deviations from the accepted Gate-2 figures, stated so they are not read as
drift: the authority corpus is `CURRENT` rather than the predicted
`RECOMPUTE`, because `AUTHORITY_CORPUS.json` v20 has no decomposition
member; and the estimate and schedule derivatives named by the protocol's
Gate-4 rerun advisory do not exist for this project (Impact Assessment
"Estimate and schedule staleness"), so no derivative is created or deferred.

Protocol narrowing, stated: the Gate-5 protocol permits SCOPE_CHANGE to
update `_CONTEXT.md` for `MODIFY` actions. This plan narrows that to zero
deliverable-local SCOPE_CHANGE writes and routes every carrier surface to
WORKING_ITEMS under sealed briefs, as SCA-APP-009 did, so that presentation
prose is reviewed before it is written and the owner's seating act stays
distinct from the amendment.

Interim state, stated: after step 13 of §5 the applied decomposition may be
merged to `main` while `_LATEST.md` still points to SCA-APP-009. In that
interval the decomposition is truth and the pointer is the active-snapshot
record only. Owner seating (§6 item 1) and WORKING_ITEMS alignment (§6 item
2) may proceed on the merged truth; they do not wait for the pointer
sub-gate, and neither claims closure.

## 7. Pre/post validation and closure criteria

`VALIDATION_AND_ROLLBACK_MATRIX.csv` is normative. Minimum success conditions:

- exact or fast-forward basis, clean tree, frozen inputs exact;
- builder regeneration with SHA parity; both post-image hashes on the live
  files after application; full-file diff parity with the Gate-3 patches;
- 10 / 52 / 84; 79 / 4 / 1; S9 M41 L2 XL0; reverse-view parity; no duplicate
  IDs or dangling mappings; companion 83 / 50 / 18 with only the K-PATH-2
  mapping change beyond the pin;
- cumulative map 45 rows, expected hash, zero findings;
- fresh post-change audit with no new blocker or major versus the fresh
  pre-change audit; carried warnings remain explicit;
- independent Gate-5 review `PASS`, zero BLOCKER, zero MAJOR;
- RECONCILIATION no drift;
- changed paths exactly D-001, D-002, and the snapshot; `_LATEST.md` and
  SCA-APP-009 unchanged; `git diff --check`, receipts validator, harness
  self-check, candidate whitespace, and G0–G4 pass.

Fixed handoff posture at Gate-5 freeze:

| Field | Value |
| --- | --- |
| `DecompositionTruthState` | `COMPLETE` after exact post-image validation |
| `DerivativePackageState` | `INCOMPLETE` (carrier surfaces and dependency registers stale until downstream alignment) |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` pending owner seating and separately authorized dispatches |
| `MetadataAlignmentState` | `NOT_STARTED` |
| `AuditState` | actual fresh result; expected `WARNINGS` for carried findings |
| `ReadyForNextPhase` | `NO` |
| Closure verdict | `OPEN_PENDING_DERIVATIVE_CLOSURE` |

`CLOSED_FOR_SCOPE_CHANGE_ONLY` becomes available only after downstream
alignment, dependency reruns, and the closure audit, and only after the
pointer sub-gate. No implementation, lifecycle, release, or reliance claim
follows from this amendment.

## 8. Rollback and backcheck

- **Failure before application:** discard the candidate mirror; nothing in
  the repository changed.
- **Failure after application, before commit:** restore both authoritative
  files from the scratch bundle as one unit; discard only new snapshot files
  written after the failure point; leave `_LATEST.md` and SCA-APP-009
  untouched; re-verify pre-image hashes and changed-path scope.
- **Failure after a separately authorized commit:** do not rewrite published
  history; route a corrective transaction through CHANGE and SCOPE_CHANGE.
- **Downstream failure after acceptance:** do not roll back accepted truth;
  leave the downstream state open in its own evidence and obtain owner
  direction.

## 9. Gate-4 decision requested

**Do you approve this propagation plan?**

Approval authorizes only progression to a separately explicit Gate-5
execution decision. It does not itself authorize any repository write,
pointer movement, downstream dispatch, seating, commit, push, or merge.
