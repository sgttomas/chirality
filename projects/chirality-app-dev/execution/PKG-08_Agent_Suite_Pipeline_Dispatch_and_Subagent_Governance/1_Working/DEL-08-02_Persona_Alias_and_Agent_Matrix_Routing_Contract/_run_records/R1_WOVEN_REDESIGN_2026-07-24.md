# R1 Woven Dialogue Visual Redesign & IA Consolidation — DEL-08-02

- Date: 2026-07-24
- Run: `APPDEV_WOVEN_REDESIGN_2026-07-24`
- Basis: `TRB-APPDEV-WOVEN-REDESIGN-2026-07-24`
  (`execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/ADOPTED_BRIEF.md`),
  adopted by the owner in-session 2026-07-24 with defaults D1–D4
  (`.../ORCHESTRATION_PLAN.md` §Adopted authority). Authority basis of record
  remains D-APP-74 / SCA-APP-004 (RULED 2026-07-23) and D-APP-36.
- Reconciliation scope: per adopted default D4, this record also reconciles the
  PR #323 Woven Dialogue implementation (merge `403f228f4`, implementation
  commit `7941722f6`, evidence
  `execution/_Coordination/AgentRuns/APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/`)
  against this deliverable.
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged by this record.

## What landed for DEL-08-02

**PR #323 (merge `403f228f4`).** Exact-record hierarchy construction and
presentation-only guarded session selection were implemented. Parentage is never
inferred; rooted sessions are shown as recorded, and detached, unresolved and
cyclic records stay visible in a separate unsafe-relationship group with their
exact recorded parent identifiers and availability status. The established
`ORCHESTRATE` → `PROJECT_SETUP` compatibility alias remains mapped, and no
execution or delegation behavior was added
(`.../APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/PACKAGE_RETURNS.md`
§PKG-08; `.../REVIEW.md`).

**This tranche (branch `feat/woven-redesign`).** No routing or persona-resolution
semantics changed. Stage B2 (`b17ab9d39`) added a new *caller* for the existing
guarded path: navigator recorded-session rows carry `aria-pressed`, are
`disabled` while a turn is in flight, expose `data-session-id`, and select
through `guardRecordedSessionSelection` into the read-only replay lens. Session
labels are the recorded persona, because `SessionRecord` carries no title field
— the id travels in `data-session-id` (B2 deviation 4, canonical-evidence
honesty). Stage A/C (`2afcd8474`, `04d3b4f5f`) restyled the surrounding chrome
through tokens only; `1cfd3e293` merged `main` into the branch.

Verification of the guard was live, not inferred:

- `guardRecordedSessionSelection` remains a single call site with an unchanged
  argument shape, and the guard is honoured at both row level and authority
  level (`.../instances/AGENT1-VALIDATOR/ROUND4_REVIEW.md` §Replay routing,
  §ARIA).
- V1 proved double-guarded selection in the running app together with strict
  primary draft/context/permission isolation, and confirmed route/query/matrix
  compatibility for `/`, `/chat`, `/workbench`, `/pipeline`, `?agent=`,
  `?legacy=1` and unknown parameters
  (`.../instances/V1-INVARIANT-SWEEP/RETURN.md`).
- The persona/alias regression suite stayed green throughout: vitest
  944 → 961 → 980 → 984 passed with 4 skipped, typecheck PASS at every fan-in
  (`.../instances/AGENT1-VALIDATOR/ROUND3_REVIEW.md`, `.../ROUND4_REVIEW.md`,
  `.../ROUND5_REVIEW.md`).

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/instances/B2-NAV-SESSIONS/RETURN.md`
  (navigator session rows, guarded selection wiring; navigator tests 1 → 11)
- `.../instances/AGENT1-VALIDATOR/ROUND4_REVIEW.md` (guard and ARIA validation)
- `.../instances/V1-INVARIANT-SWEEP/RETURN.md` (live guard + isolation proof;
  routes/params confirmed)
- `.../instances/V2-RENDER-EVIDENCE/EVIDENCE.md` + `.../evidence/`:
  `navigator-{light,dark}-{900,1180,1440}.png`,
  `navigator-allsessions-{light,dark}-1440.png`,
  `route-chat-*` / `legacy-*-1440.png`; full keyboard walk from a session row
  into the replay lens

## Residuals recorded in `_STATUS.md` `## Remaining`

1. `[data-legacy]` is a mock-only contract: it is asserted in
   `woven-dialogue-route.test.tsx` (its sole occurrence under `src`) but is
   never emitted by the real DOM at `?legacy=1`. Pre-existing, not a tranche
   regression; either the test contract or the component should be aligned in a
   future pass (`.../instances/V2-RENDER-EVIDENCE/RETURN.md` caveat 3).
2. Packaged Desktop smoke evidence for the guarded navigator selection path
   (not run this tranche).

## Other note of record

Gate figures cited here were measured before the `1cfd3e293` upstream merge;
the authoritative post-merge full-gate run is owned by Agent 0 at closeout.
