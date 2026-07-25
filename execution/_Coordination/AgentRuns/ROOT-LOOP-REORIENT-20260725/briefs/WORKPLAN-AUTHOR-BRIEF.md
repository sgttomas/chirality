# Sealed Brief — N1: Author successor root workplan (ROOT-LOOP-REORIENT-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25
Executor: Agent 1, `PROJECT_SETUP` posture, model `opus-5` (owner direction of record)
Basis: `main@ee4215729` (D-GOV-21 EffectiveSHA)

## Purpose

Author the successor standing workplan for the root governance loop,
reflecting the D-GOV-21 in-force state, and update the deterministic pointer
`execution/_Coordination/CURRENT_WORKPLAN.md` to select it. This executes
D-GOV-21 sequence step 4 (loop reorientation), which must complete before
root-PRD development begins.

## Role loading

Read `agents/AGENT_PROJECT_SETUP.md` and operate within its Agent 1 contract
as applied to the root loop's control-loop reorientation. Do not delegate;
this is a single bounded objective. Where the instruction package and this
brief conflict, stop and return the conflict.

## Declared context (read scope)

- `execution/_Coordination/LOOP_INIT.md` (already rewritten for D-GOV-21)
- `execution/_Coordination/CURRENT_WORKPLAN.md` (current pointer, CLOSED target)
- `execution/_Coordination/WORKPLAN_2026-07-15_pkg00_post_consolidation.md`
  (the closed predecessor — read-only, immutable history)
- `execution/_Coordination/HANDOFF_STATE.md` (prior closure state; historical)
- `execution/_Coordination/LOOP_RECEIPTS.md` (esp. Receipts 31–32)
- `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md`
  (the ruled candidate — §§5, 6, 7, 11 govern the sequence you encode)
- `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md`
- Root `AGENTS.md`; `docs/DIRECTIVE.md` §2.6; `docs/SPEC.md` §0.2.2 (as amended)

## Write targets (exactly two; anything else is a fan-in rejection)

1. **Create** `execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md`
2. **Update** `execution/_Coordination/CURRENT_WORKPLAN.md` — pointer body
   only: new Status line and new Target line; keep the file's existing
   deterministic-pointer framing paragraph.

## Required content of the new workplan

Follow the structural conventions of the predecessor workplan (Status/Date/
Supervising role header; Step 0 preflight; explicit lanes; stop state). It
must contain:

1. **Header:** Status `ACTIVE — ROOT PRODUCT DEVELOPMENT`; Date 2026-07-25;
   Supervising role `HELP_HUMAN`.
2. **Goal:** develop the root product under D-GOV-21 through the remaining
   ruled sequence (packet §6 steps 5–9), stopping at every human gate.
3. **Authority basis (cited, not claimed):** D-GOV-21 RULED 2026-07-25
   (AcceptedCandidateSHA `c038c493e871c95871823281b45890ba9404624b`,
   PublicationSHA `75b7aa6d1fb019846ac76fb775df2fc1652ab8a8`, EffectiveSHA
   `ee42157290618e3f84be0e0b651c041387ad6ee0`). State plainly that the
   workplan itself carries no authority (LOOP_INIT discipline).
4. **Step 0 preflight:** resolve REPO_ROOT; require synchronized `main`
   containing the EffectiveSHA; read the D-GOV-21 record, packet, and
   implementation handoff; run the governance-harness suite, `self-check`,
   and `tools/validation/validate_root_materialization_fence.py` (G0) and
   require G0 PASS; treat any BLOCK or unexplained delta as a new decision
   request.
5. **Live lanes** (each with its gate):
   - **Lane A — candidate root PRD development** (packet §6 step 5;
     authorized basis, adoption reserved). Must record the four reserved
     decisions of packet §11 (genus wording; accountability model including
     who may amend `docs/governance_harness/human_actors.md`; adoption
     instrument + DIRECTIVE §1 concordance map; placement vs. the
     public-export boundary) as owner decisions the PRD track must surface,
     never resolve unilaterally.
   - **Lane B — guard capability G1–G4** (packet §6 step 6; validator code
     + CI wiring per packet §5.3), preceded by the §7 preflight: run the
     full harness/validation suites against a scratch materialization of a
     root `PKG-*` skeleton (in a throwaway worktree, never committed) to
     confirm the §5.1 finding before G1–G4 design.
   - Lanes A and B may run in parallel (step 4 — this reorientation — is
     complete when this workplan is the standing pointer).
6. **Gated-downstream section** (not released by this workplan): PRD
   adoption (separate instrument, exact bytes, owner-ruled); first root
   decomposition from the adopted PRD; root Project Setup instantiating the
   G2 register and first accepted work graph; materialization under root
   `execution/` only with G0–G4 registered and passing (§5.3 gate).
7. **Parked lanes** (independent; not blockers): packet §7 class (b)
   historical reconciliation (D-GOV-19/20 root receipts; K-WRITE-2 gloss)
   and class (c) conditional runtime work (root `chirality.project.json`
   containment test before any runtime-backed root execution). Also carry
   forward the Receipt 31/32 standing follow-ons (App Dev managed-delegation
   deflake per its sealed brief; optional strict branch-protection
   hardening; CHANGE merge-verdict standing rule) so they are not orphaned
   by the pointer move.
8. **Stop state:** every lane stops at its named human gate; consequential
   ambiguity returns to the owner (AGENTS.md "consequential" enumeration).

## Constraints

- Coordination surface only: no writes to `AGENTS.md`, `agents/`, `skills/`,
  `tools/`, root `docs/`, `init/`, or any `projects/*`/`domains/*` path.
- Do not create any `PKG-*`/`DEL-*` structure anywhere (G0 must stay
  PASS-idle).
- Do not modify the closed workplans, `LOOP_RECEIPTS.md`, `HANDOFF_STATE.md`,
  or `LOOP_INIT.md`.
- No machine-absolute paths in either file (SPEC §0.2.4).
- Repo-relative paths throughout; cite decisions by ID + SHA, never by
  narrative recollection.
- The pointer file keeps its "do not select by modification time" paragraph
  verbatim.

## Terminal return (structured)

Return, as your final text: (1) the two file paths written; (2) the new
workplan's section outline; (3) confirmation of each constraint above
(explicitly: no other file touched, no absolute paths, pointer resolves);
(4) any conflict, ambiguity, or discovered inconsistency you did NOT
resolve, for Agent 0 disposition. Your final text is a data return to the
parent, not a user-facing message.

## Acceptance checks (applied by Agent 0 at fan-in)

Diff limited to the two write targets; pointer resolves to an existing file;
required content items 1–8 present; constraints held; path-anchor validation
passes repo-wide.
