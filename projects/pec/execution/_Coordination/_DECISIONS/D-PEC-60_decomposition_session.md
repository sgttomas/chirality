# D-PEC-60 — RULED: open the SOFTWARE_DECOMP session over PRD v2 (D1)

**Status:** RULED 2026-07-24 — direct owner instruction; decomposition-session fence
**Decision ID:** D-PEC-60
**Structure precedent:** `D-PEC-59` (direct owner instruction, ruled behavior, exact fence, verification/rollback)

## Owner direction

Owner direction of record (Ryan Tufts, in-session, 2026-07-24), verbatim:

> "Go — begin the decomposition session over PRD v2.  Adopt the Agent 0
> posture.  Use `opus-5` Agent 1 and 2 instances as appropriate."

This opens tranche **D1** of the standing plan
(`_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`):
`SOFTWARE_DECOMP` over PRD v2.0, Gates 1–7 per
`docs/DECOMPOSITION_STANDARD.md` and `agents/AGENT_SOFTWARE_DECOMP.md`,
human-interactive. **This row authorizes the session and its documentation
surfaces only. It accepts no gate in advance: Gates 1–7 remain individual
owner acts inside the session, and Gate 7 acceptance is recorded in this
packet's closure when it occurs.**

## Ruled behavior

1. **Session form.** The decomposition runs as the `SOFTWARE_DECOMP`
   Agent 1 persona protocol, supervised in the Agent 0 posture, with
   `opus-5` subagent instances dispatched through the platform's native
   subagent facility for bounded extraction, drafting, and adversarial
   verification (the project-loop mechanism permitted by root `AGENTS.md`).
   Gate confirmations are the owner's in-chat words, transcribed verbatim
   into the working package's Gate Log.
2. **Canonical working package.** The package is authored at
   `projects/pec/execution/_Decomposition/`: main working surface
   `SOFTWARE_DECOMP.md` (revision tracked in front matter, not the
   filename), authoritative companion registers co-located in the same
   directory (Scope Ledger, Deliverables, Context Budget QA, Companion
   Inventory as CSV), and a `_LATEST.md` revision pointer kept current.
   `execution/_ScopeChange/` is **not** created by this session; it comes
   into being only with a post-acceptance amendment under the scope-change
   machinery.
3. **Decomposition documents only.** No implementation write, no source
   tree, no dependency, no database, and no change to the frozen reference
   corpus is authorized by this row. Implementation tranches still require
   their own packets (standing plan step 3); `F-PEC-1..4` are otherwise
   unchanged.
4. **Closure.** On Gate 7 acceptance: the working surface is marked
   `current_basis`, the acceptance is recorded in this packet and the
   register row, a loop receipt is appended, and the tranche closes by PR
   under the session conventions of the `D-PEC-58` packet. If the session
   authorization has lapsed by then, the owner merges.

## Exact fence

- `projects/pec/execution/_Decomposition/**` (the canonical working package; new directory)
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-60_decomposition_session.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `_DomainEngines/pec/LOOP_RECEIPTS.md`
- `projects/pec/docs/STATUS.md` (status upkeep for this tranche only — the
  per-tranche packet clause `projects/pec/AGENTS.md` requires)

No other surface. The frozen reference corpus, `docs/PRD.md`, the profile,
root `docs/**`, and all source trees are untouched by this tranche.

## Verification and rollback

- The package satisfies the SPEC completeness and consistency tables of
  `agents/AGENT_SOFTWARE_DECOMP.md` at Gate 7 (scope ledger, telemetry,
  vocabulary map, context-budget QA, package-role labels, companion
  inventory; zero unassigned IN-scope items).
- Adversarial verification (opus-5) runs before Gate 6 material is
  presented and again before the closing PR merges.
- Harness self-check introduces no new BLOCK findings.
- Roll back by reverting the tranche commit(s); reversal of a recorded gate
  acceptance is an owner act on a successor row.

## Human ruling

**RULED (2026-07-24)** by the quoted direction. Gate log lives in the
working surface.

## Closure — Gate 7 acceptance (2026-07-24)

All seven gates were confirmed by the owner in-session the same day, each
verbatim in the working surface's Gate Log. Gate 7 acceptance, verbatim:

> "I rule that this decomposition is now the accepted basis for downstream
> work."

The canonical working package at `projects/pec/execution/_Decomposition/`
(revision 1.0, `current_basis`: `SOFTWARE_DECOMP.md`, `ScopeLedger.csv`
94 rows, `Deliverables.csv` 64 rows, `ContextBudgetQA.csv`,
`Companion_Inventory.csv`, `_LATEST.md` handoff state) is the
**authoritative downstream basis for all build tranches** (standing-plan
tranche D1 complete). Verification evidence: adversarial passes at
revisions 0.3 (16 defects) and 0.8→0.9 (19 defects), all corrected before
the corresponding gate. In-session owner design acts of record: the
PKG-00 restructuring (DL-12) and the OI-010/OI-011 resolutions (DL-10).
Open issues at acceptance: OI-001..009 (§16, none blocking P0–P2),
OI-012 (core-isolation ADR in DEL-00-01), OI-013 (durable register
validator). Evidence pointers in loop Receipt 104.
