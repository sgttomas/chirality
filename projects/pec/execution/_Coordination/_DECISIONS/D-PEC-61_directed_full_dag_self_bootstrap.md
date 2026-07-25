# D-PEC-61 — RULED: directed full-DAG self-bootstrap and SCA-001 opening

**Status:** RULED 2026-07-24 — owner-directed documentation amendment and
scope-change-session opening
**Decision ID:** D-PEC-61
**Structure precedent:** `D-PEC-58` (PRD adoption) + `D-PEC-60`
(human-gated decomposition session)

## Owner direction

Owner direction of record (Ryan Tufts, in-session, 2026-07-24), verbatim:

> "PLEASE IMPLEMENT THIS PLAN:"

The direction accompanied and adopted the complete plan titled
`PEC SCA-001 — Directed Full-DAG Self-Bootstrap`. That owner-supplied plan is
the exact execution basis summarized below; this packet does not broaden it.

## Ruled behavior

1. **PRD v2.1 clarification.** `projects/pec/docs/PRD.md` advances from v2.0
   to v2.1. Section 12 records that PEC's own build uses the accepted full
   dependency DAG as its initial file-native coordination state; P1 first
   ingests that build graph; later nodes consume only capabilities already
   produced and accepted by predecessors; observed friction may generate
   evidence-linked candidate functions, boundary decisions, and scope-change
   requests but grants no authority and changes no scope without human
   acceptance; the fallback remains operable; generality is tested against a
   structurally different loop after self-ingestion.
2. **Project Setup posture.** `FULL_GRAPH` is the owner-selected coordination
   representation for PEC Project Setup. Blocked/available state will be
   computed from the complete accepted dependency graph once PROJECT_SETUP
   materializes it. Dependency maturity threshold and register-storage
   choices remain the normal PROJECT_SETUP Phase 1.3 owner gate.
3. **SCA-001 opening.** SCOPE_CHANGE opens `SCA-001` with
   `DECOMP_VARIANT=SOFTWARE` against accepted decomposition revision 1.0.
   Its requested endpoint is revision 1.1 with four `MODIFY` actions: add
   directed-bootstrap constraint C16; expand SOW-064; strengthen DEL-10-10;
   reconcile OBJ-006 mappings, summaries, source basis, and revision history.
4. **Five gates remain live.** This ruling authorizes the session and its
   documentation surfaces. It does not pre-approve SCOPE_CHANGE Gates 1–5.
   Decomposition truth is not edited until Gate 3's exact amendment has owner
   approval and Gate 4's propagation plan has owner approval.
5. **Setup hold.** PROJECT_SETUP must not materialize the final DAG from
   decomposition revision 1.0. It resumes from the accepted SCA-001 successor
   only after Gate 5 validation and owner confirmation.
6. **No product-topology expansion.** The amendment adds no package,
   deliverable, objective, product function, runtime API, implementation
   surface, dependency register, estimate, or schedule. Stable IDs and the
   accepted 94-scope-item / 64-deliverable / 11-package / 6-objective topology
   are preserved.

## Exact fence

Owner-governance writes:

- `projects/pec/docs/PRD.md`
- `projects/pec/AGENTS.md`
- `projects/pec/README.md`
- `projects/pec/docs/STATUS.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-61_directed_full_dag_self_bootstrap.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `_DomainEngines/pec/LOOP_RECEIPTS.md`

SCOPE_CHANGE session writes, only as released by its gates:

- `projects/pec/execution/_ScopeChange/**`
- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`
- `projects/pec/execution/_Decomposition/ScopeLedger.csv`
- `projects/pec/execution/_Decomposition/Deliverables.csv`
- `projects/pec/execution/_Decomposition/ContextBudgetQA.csv`
- `projects/pec/execution/_Decomposition/_LATEST.md`

`Companion_Inventory.csv` remains unchanged unless Gate 3 demonstrates that
revision-pointer parity requires an exact approved edit.

No implementation, scaffolding, `Dependencies.csv`, estimate, schedule,
frozen-reference-corpus, database, dependency, or external-system write is
authorized. Existing unrelated worktree changes are outside this fence.

## Verification and rollback

- Confirm PRD v2.1 contains only the ruled release-strategy clarification and
  header/pointer updates.
- Confirm live PEC pointers name v2.1 and D-PEC-61; historical decision
  records remain unchanged.
- Confirm no decomposition truth changes before Gate 3 and Gate 4 approvals.
- At SCA-001 closure, compare deterministic pre/post register-integrity
  baselines and preserve the expected pre-scaffold AUDIT_DECOMP limitation.
- Run `git diff --check`, path-anchor validation, and applicable governance
  checks.
- Roll back the PRD/pointer tranche by reverting its scoped commit. Roll back
  any later decomposition amendment only through a successor owner act;
  immutable SCA evidence remains historical.

## Human ruling

**RULED 2026-07-24.** The quoted direction adopts the supplied plan. PRD v2.1
and its live pointers may be applied now; SCA-001 opens at Gate 1. Gates 1–5
remain distinct in-session owner acts.

## Closure — SCA-001 accepted

SCOPE_CHANGE Gates 1–5 were separately owner-confirmed on 2026-07-24.
Final Gate 5 confirmation, verbatim:

> "I confirm the post-change state and accept decomposition revision 1.1 as
> the current basis."

SCA-001 is closed with
`ClosureVerdict=CLOSED_FOR_SCOPE_CHANGE_ONLY`. The accepted current basis is
`projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1,
with immutable amendment evidence at
`projects/pec/execution/_ScopeChange/SCA-001_2026-07-24_2206/`.

Deterministic pre/post checks preserve 94 scope items (71 IN / 14 OUT /
9 TBD), 64 deliverables, 11 packages, and 6 objectives; validate
`SOW-064 → PKG-10 → DEL-10-10 → OBJ-006`; and confirm Context Envelope
counts S 28 / M 34 / L 2 / XL 0. The only audit warning is the expected
pre-scaffold `AUDIT_DECOMP FAILED_INPUTS` result because no package or
deliverable folders exist yet.

`PROJECT_SETUP` is released as the next owning workflow with `FULL_GRAPH`
already selected. Project Setup still owns dependency-edge materialization,
blocker computation, scaffolding, and its normal Phase 1.3 maturity-threshold
and dependency-register-storage gate. No implementation, dependency,
estimate, schedule, scaffold, staging, or commit occurred in SCA-001.
