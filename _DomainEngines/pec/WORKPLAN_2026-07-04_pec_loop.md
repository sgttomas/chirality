# PEC Work Loop — standing plan (pec tier-0 registration → standing pec loop)

> **Epistemic status: agent-authored plan — not authority.** Written at owner direction
> (Ryan Tufts, K-AUTH-1) on 2026-07-04. This plan never authorizes work: owner-adopted
> specifications and owner rulings/directions do. Sources govern on any disagreement.
> This file is a PROTOCOL plus pointer indexes; it carries NO status, NO work history,
> and NO measurements — each loop iteration re-derives state from the live tree, and
> loop closes append a minimal receipt to `_DomainEngines/pec/LOOP_RECEIPTS.md` (rules
> live at the top of that file).

## Owner intent (recorded 2026-07-04)

**The loop's goal** (owner direction of record, quoted verbatim in
`LOOP_RECEIPTS.md` Receipt 0): *"I want to create a new development loop to
implement this plan."* — where "this plan" is
`plans/pec_bridge_integration_plan_2026-07-04.md`: register `projects/pec/` as
the second domain engine in `_DomainEngines/` (DRAFT profile, prep snapshot,
decision slate D-T0-11..16, pec-side governance surfaces) and stage the
practitioner-harness tranche, stopping at every owner gate. This section is the
goal's single durable home — the generic launcher (`init/init-prompt.md` §4) and
`LOOP_INIT.md` deliberately point here instead of restating it.

Execute the plan as a series of loops across sessions, discovering state fresh
each iteration. **After the registration slate is ruled**, the standing goal
proposed in the plan — "keep the pec project surface governably aligned with the
framework and move the pec standing plan forward as far as live authority
permits" — takes over **once the owner adopts that wording via D-T0-15**; until
then the implementation goal above governs.

**Addendum (2026-07-04, owner direction of record — quoted verbatim in
`LOOP_RECEIPTS.md` Receipt 4):** the staged integration ladder is a core
inherent goal of the project: *"That's exactly the progression this needs to
follow from L1, L2 to L3. It's one of the core inherent goals of the project
now."* — said of the ruled D-T0-13 staging. This directs loop priority; it
changes no ruling. The lawful path remains exactly the ruled staging — L0 now →
proven read-only L1 evidence → per-operation L2 → L3 future-only pending a pec
proposal-shaped API — inside fences F-PEC-1..4 and the D-T0-14 residency gate
(CLOSED default; the real-data case arrives via D-PEC-01). Under CLOSED
residency, L1 evidence work over committed fixtures and scratch databases is
already lawful; instance-content capture is not.

## Why any staging remains (the compelling reasons)

1. **Adoption, ruling, and direction are human acts** (K-AUTH-1; D-GOV-04): the
   registration package lands as DRAFT/PROPOSAL and terminates in the decision
   slate; profile lifecycle is DRAFT → VALIDATED (deterministic validator) →
   ADOPTED (owner Gate 2). No agent fills a `HumanRuling`.
2. **The harness tranche is gated** — harness code changes (the multi-profile
   adapter fix, aliases, bridge-status/self-check registration) execute only
   under the tranche-authorization ruling (provisionally D-T0-16; renumber from
   the live register).
3. **Fences F-PEC-1..4** (below) bound what any tranche may touch regardless of
   ambition; D-T0-15 ratifies them as the standing set.

## The loop protocol (every iteration)

0. **Discover (mandatory core).** Clean `git` state and branch awareness (log
   since the last receipt; a concurrent app-dev↔piping bridge loop is live —
   keep write scopes disjoint from `_DomainEngines/bridge/**` and both sibling
   project subtrees); read the latest receipt(s) in
   `_DomainEngines/pec/LOOP_RECEIPTS.md`; check the tier-0 decision register and
   (once it exists) the pec project register for rulings newer than the last
   receipt — new rulings are how work unlocks, look every time; renumber the
   plan's provisional decision IDs from the live register.
   `PYTHONDONTWRITEBYTECODE=1` harness `self-check`; full harness pytest at
   discovery only if `tools/**` changed since the last receipt (always mandatory
   at closeout — step 4). **K-INVENT-1 note:** harness `status`/`drift`/`next`/
   `brief --project pec` and `bridge-status` rows do NOT exist for pec until the
   harness tranche lands — do not fabricate those commands for pec; repo-wide
   `self-check` and pytest are the deterministic checks available now. Verify
   any derivative statement — including this plan, the registration plan file,
   and your own tasking — against the live tree before relying on it; on
   disagreement the live tree wins and the delta goes in the receipt.
1. **Select.** The widest lawful tranche(s) now, re-derived. Principles, in
   order: (a) work that discharges a gate prerequisite beats work that doesn't;
   (b) owner-directed items beat agent-inferred ones; (c) doc/design-level
   before any binding; (d) the registration plan's Lane A (tier-0 package) and
   Lane B (pec-side surfaces) are owner-directed work under this workplan's
   recorded intent; coordination/control artifacts beyond the plan's inventory
   take explicit owner direction.
2. **Brief / slate.** The adopted work specification for the registration work
   is `plans/pec_bridge_integration_plan_2026-07-04.md` (owner-directed
   2026-07-04). The registration run terminates in the D-T0-11..16 decision
   slate (options + non-binding recommendation + on-ruling mechanism) presented
   to the owner. Later deliverable-shaped work follows whatever brief/vehicle
   convention the ruled slate establishes.
3. **Gate.** STOP; adoption/ruling/direction is the owner's act (K-AUTH-1;
   D-GOV-04). Directions/rulings given in-session are quoted verbatim in the
   receipt and recorded in their governed artifact (decision packet, register
   row) as part of execution. Record every gate outcome in the receipt —
   including no-ops and their reason.
4. **Execute + check.** Branch-first + PR unless the owner directs main-direct;
   never self-merge; mutually exclusive write scopes when parallel (and always
   disjoint from the concurrent bridge loop's). Inside fences + standing
   constraints below. Checks per the plan's Verification section: profile
   validator green; repo-wide `self-check` exit 0 with conscious live-pin
   updates riding the same PR; FULL harness pytest including the live-baseline
   suite at the exact final commit SHA of each PR (any edit after a check run
   invalidates that run — re-run at the final SHA); adversarial review of
   citations + git-diff scope containment; pec belt-and-braces
   (`npm run typecheck && npm test && npm run build && npm run drill` still
   green). CI green; owner merges.
5. **Receipt.** Append a minimal receipt to `_DomainEngines/pec/LOOP_RECEIPTS.md`
   per its local rules — pointers, verbatim owner directions, gate outcomes,
   check pass/fail. No narrative here or anywhere else. Next iteration starts
   at 0.

## Standing constraints — fences F-PEC-1..4 (all iterations; D-T0-15 ratifies)

- **F-PEC-1 (engine truth):** no writes under `projects/pec/**` except
  `execution/_Coordination/**`, `AGENTS.md`, and the one-time `docs/STATUS.md`
  pointer edit sanctioned in the registration packet; never `pec.db`/`-wal`/
  `-shm`, `backups/**`, `core/**`, `server/**`, `web/**`, `tools/**`,
  `fixtures/**`, or root manifests; never run the pec server or a mutating CLI
  against a non-scratch DB.
- **F-PEC-2 (lifecycle/status):** no invention or file-level mutation of pec
  record states — approvals, checks, decisions, holds exist only as app-created
  RBAC'd append-only records or cited owner statements; no pilot-readiness,
  go-live, or issuance claims.
- **F-PEC-3 (release/egress):** no `npm publish` or release/packaging act; no
  new pec runtime dependencies (ADR-002 zero-dep posture); no pec
  instance-content egress absent the data-residency ruling (provisionally
  D-T0-14).
- **F-PEC-4 (tier-0 scope):** tier-0 writes only under `_DomainEngines/pec/**`
  and `_DomainEngines/proposals/pec/**`; never the ADOPTED
  `profiles/open_pipe_stress.yaml`, closed snapshots, sealed logs, the bridge
  loop's surfaces, or the three owner-retained self-check fixtures; no
  integration-level advance past L0 without the staging ruling (provisionally
  D-T0-13); no harness code changes without the tranche ruling (provisionally
  D-T0-16). The pec DRAFT profile stays OUT of `_DomainEngines/profiles/`
  until that tranche (the multi-profile adapter defect is the reason — see the
  plan's live-tree facts).
  *Grant note (2026-07-06, owner D-T0-19 O-1A ruling — dated pointer, no
  fence rewrite):* the fence set gains the enumerated app-dev
  **decision/coordination packet** paths
  (`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/**` rows
  authored as PROPOSALs by this loop); app-dev **source** stays behind D-APP
  rulings; deconfliction note in the app-dev register preamble; twin notes in
  the D-T0-19 and D-T0-15 packets.

## Where live work is re-derived (pointer index — never a status surface)

- **The work specification:** `plans/pec_bridge_integration_plan_2026-07-04.md`
  (file inventory, profile content, decision slate, sequencing, verification);
  companion draft `plans/pec_domain_engine_harness_bridge_plan_2026-07-04.md`
  (reconciled inside the registration plan's header).
- **Decision registers** (open rows are the owner-gated surface):
  `_DomainEngines/_DECISIONS/_REGISTER.md` ·
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (created by
  Lane B; D-PEC-XX rows — never bare `D-XX`, which collides with piping's
  series).
- **The staged profile:** `_DomainEngines/pec/profile/pec.DRAFT.yaml` (+
  `_validation/` report) once authored; registry row in
  `_DomainEngines/DOMAIN_ENGINE_INDEX.md`.
- **pec's own track:** `projects/pec/docs/STATUS.md` (state + what's next) and
  `projects/pec/docs/TRACEABILITY.md`; pec conventions live in
  `projects/pec/AGENTS.md` once authored.
- **Cross-loop awareness:** `_DomainEngines/bridge/LOOP_RECEIPTS.md` (scope
  dedup only — this loop never writes the bridge loop's surfaces).
- **Queued harness work:** `tools/practitioner_harness/BACKLOG.md`.
- **Handoff context** (owner directions, gate outcomes, stale-map deltas):
  `_DomainEngines/pec/LOOP_RECEIPTS.md`.
