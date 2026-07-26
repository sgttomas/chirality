# Root Governance Workplan — Per-Deliverable Initialization (All 45 Scopes of Work)

Status: `ACTIVE — ROOT DELIVERABLE INITIALIZATION`
Date: 2026-07-25
Supervising role: `HELP_HUMAN`

## Goal

Produce a validating `SOW_V1` `ScopeOfWork.md` for every one of the 45
materialized root deliverables and advance all 45 from `OPEN` to
`INITIALIZED`, completing the phase the owner named after the D-GOV-21 §6
sequence closed. The objective is to complete all scopes of work.

## Authority basis (cited, not claimed)

This workplan is a coordination surface. It records intent, protocol,
constraints, gates, and source pointers. **It carries no authority merely
because it exists** (`execution/_Coordination/LOOP_INIT.md` §2, §4). On any
disagreement between this file and a live source, the live source governs and
the delta is recorded in the next receipt.

Owner acts of record (in-session, 2026-07-25):

- Phase named by the owner ahead of closeout: "let's close out what we can
  now before proceeding to the per-deliverable initialization and creation of
  scopes of work." (Receipt 49.)
- Phase opened by owner direction: "Plan out your approach so that delegation
  through the Agent 0/1/2 paradigm can execute efficiently over it. The
  objective is to compete all scopes of work." followed by owner approval of
  the phase plan with four recorded decisions:
  1. **PR waves:** "1 single PR, all 45" — one PR carries all 45 scopes of
     work.
  2. **State flips:** "One closing tranche" — a single closing M2 tranche
     flips all 45 lifecycle states and updates the live CI pin.
  3. **AC minting:** "Briefs authorize candidate AC/VER" — each sealed brief
     explicitly authorizes creating candidate `AC-*`/`VER-*` grounded only in
     the accepted register, `_CONTEXT.md`, scope-ledger statements, and the
     adopted PRD; the owner reviews them at the PR gate; they remain candidate
     until later lifecycle acceptance.
  4. **ResponsibleParty:** "Assign 'Ryan Tufts' to all 45 now" — the closing
     tranche stamps the owner as ResponsibleParty on every `_CONTEXT.md` as a
     human-authorized bulk edit recorded in the receipt, with the deliverable
     register amended as the amendment surface.

Approval vehicle (K-AUTH-2): the owner approved the phase plan in-session;
substantive approval of the produced artifacts binds at the merge SHA of each
human-gated PR carrying them. No exact candidate SHA was designated in
advance. Any owner correction supersedes.

Accepted upstream basis:

- Adopted PRD: `docs/PRD_ROOT.md` (D-GOV-22).
- Accepted decomposition: `execution/_Decomposition/` working surface and
  companion registers (D-GOV-25; EffectiveSHA
  `653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`).
- Materialized state: 45 deliverables at `OPEN` under
  `execution/PKG-*/1_Working/DEL-*/` (step 9, PR #349), five-file minimum
  satisfied, guards G0–G4 registered and passing.
- Phase basis: `main@31b8dc94acca50dbaf9a518a23dad8583c8c6c62` (post-PR-#351;
  D-GOV-26 effective).

## Protocol

Run record: `execution/_Coordination/AgentRuns/ROOT-INIT-SOW-20260725/`
(orchestration plan, sealed briefs, filed returns, evidence). The frozen work
graph, posture, and fan-in gates live there; this workplan does not duplicate
them.

Mechanism summary:

- **Production path:** `TASK + scope-of-work` semantics, `MODE=INIT`, one
  deliverable-local sealed member brief each;
  `tools/scope_of_work/validate_scope_of_work.py` is the deterministic
  acceptance check per member. The skill is lifecycle-neutral: no child
  touches `_STATUS.md`.
- **Transition path (closing tranche only):**
  `tools/scaffolding/write_status.sh <DEL> INITIALIZED "TASK+scope-of-work"`
  per deliverable, after all 45 SOWs validate — the deterministic writer that
  keeps the prose-bullet-v1 drift baseline at 0/45.
- **Delegation:** Agent 0 (`HELP_HUMAN`) → six package-scoped WORKING_ITEMS
  (Agent 1) instances, one per package node, dispatched concurrently in
  isolated git worktrees (M4) → Agent 2 author batches (≤5 members, ascending
  DeliverableID) plus one fresh package verifier per package. Recorded
  fallback: if nested dispatch is unavailable to a manager instance, Agent 0
  dispatches the same frozen author/verifier briefs directly (flat step-8/9
  precedent) with the manager's partition and fan-in criteria governing.
- **G3 dispatch discipline:** all six package nodes set `active` and
  `accepted_basis` re-pinned to the phase basis (M3 re-basing, a recorded
  between-runs act) before dispatch; G3 dispatch mode must PASS over the six
  node briefs before any child is launched. Nodes return to `pending` at the
  closing tranche (nothing is dispatched between phases).

Known transient staleness, recorded not churned: the 45 `_DEPENDENCIES.md`
coordination notes state that all work-graph nodes are `pending`; during this
phase six nodes are `active`, and they return to `pending` at close.

## Tranche structure and gates

1. **PR 1 — all 45 scopes of work.** Phase A enabling state (this workplan,
   pointer repoint, work-graph activation, run record, briefs) plus all 45
   `ScopeOfWork.md` files and per-member TASK run records, Receipt, handoff
   state. Strictly `execution/**` — no instruction-surface path, no tranche
   manifest. Lifecycle states remain `OPEN` (a valid SOW may exist at `OPEN`;
   SPEC §2.2 resolves `INVALID` only at or beyond `INITIALIZED`). **Gate:**
   human-gated PR; owner merges; never self-merge.
2. **PR 2 — closing M2 tranche.** 45 state flips via `write_status.sh`; live
   CI pin update in `tools/practitioner_harness/test_root_adoption.py`
   (`| OPEN | 45 |` → `| INITIALIZED | 45 |`, test renamed; pin discipline:
   same-PR, never silently); ResponsibleParty bulk assignment (owner ruling 4)
   in 45 `_CONTEXT.md` files and the deliverable register; work-graph nodes
   `active → pending`; D-GOV-26 EffectiveSHA backfill; G4 tranche manifest
   `ROOT-INIT-CLOSE-20260725.yaml` with `m2_gate` and pin-survey-driven
   `m6_notice`; Receipt, handoff state. **Gate:** human-gated M2 PR; owner
   merges; never self-merge.

## Verification battery (each PR)

`pytest tools/validation -q`; `pytest tools/practitioner_harness -q` (PR 2
updates the live pin in the same PR); the five guard validators G0–G4;
`tools/validation/validate_path_anchors.py`;
`tools/validation/validate_instruction_entrypoints.py`; G4 diff mode against
`origin/main`; practitioner harness `status` and `drift --project root`
(PR 1: 45 `OPEN`, 0 mismatch; PR 2: 45 `INITIALIZED`, 0 mismatch). Phase
checks: G3 dispatch mode PASS before dispatch;
`validate_scope_of_work.py` exit 0 on all 45, run independently by author,
package verifier, and Agent 0 at fan-in; write-containment verified at every
fan-in.

## Stop state

Every gate is a named human gate: PR 1 merge and PR 2 merge are owner acts.
Beyond those, stop for anything in `LOOP_INIT.md` §6 and for any condition
root `AGENTS.md` enumerates as **consequential**: scope expansion, a change in
consequential risk, a change in authority, an unresolved shared-write or
ownership conflict, or a change in acceptance criteria or lifecycle
acceptance. Any uncertainty about whether one of these conditions applies is
itself returned to the owner. Child failure returns to Agent 0 fan-in; it
does not convert the run into many-to-many coordination.

After PR 2 merges this workplan is complete. The next phase — semantic
enrichment (`INITIALIZED → SEMANTIC_READY`) or direct production dispatch —
is owner-gated future work and is **not** released by this workplan. Open
items carried: OI-005, OI-008, OI-009 in the accepted decomposition; the
owner exact-prose correction packet (four stale enumeration restatements);
the thesis-appendix K-WRITE-2 mirror; export items at next export need.
