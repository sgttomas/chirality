# R6 Woven Dialogue Visual Redesign & IA Consolidation — DEL-02-04

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

## What landed for DEL-02-04

**PR #323 (merge `403f228f4`).** The rollback-safe
`chirality.woven-workspace/v1` convenience-state store was implemented: it can
copy recognized legacy file-tree geometry into Navigator geometry, records which
fields were mapped, and leaves the legacy keys intact. Switching the project
root clears project-scoped artifact and replay references without deleting the
prior project's data
(`.../APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/PACKAGE_RETURNS.md`
§PKG-02; `.../REVIEW.md` §Corrections made during review).

**This tranche (branch `feat/woven-redesign`).**

| Commit | Content bearing on DEL-02-04 |
|---|---|
| `2afcd8474` | Stage A — additive `theme` field (`light`/`dark`/`system`, default `light`) under the **unchanged** `chirality.woven-workspace/v1` schema string; sanitize-with-fallback reader; theme-preserving merge in the state writer plus a dedicated theme writer so whole-object rewrites cannot silently revert the theme; stored-blob compatibility retained; guarded pre-paint stamp, no `matchMedia` dependency |
| `b17ab9d39` | Stage B2 — additive v1 fields `sessionSurfaces` (bounded map, cap 500, first-attribution-wins, oldest-evicted on read *and* write) and `navigatorExpandedSurfaces`; pure writers `recordWovenSessionSurface` / `toggleWovenNavigatorExpandedSurface`; insertion positions chosen to keep the existing exact `JSON.stringify` write assertions valid |
| `04d3b4f5f` | Stage C — reduced-motion policy and responsive behaviour over the persisted layout state; `--pane-*` custom properties and `layout-state` untouched |
| `1cfd3e293` | Merge of `main` into `feat/woven-redesign` |

The schema-version discipline named in ADOPTED_BRIEF §4 was honoured exactly:
the schema constant was **not** bumped, so no stored state is silently
discarded by the `woven-workspace-state.ts` hard-reject path; both new field
groups are optional-with-default; the `'document'` value is rejected by the
sanitizer; and first-attribution-wins returns the same object reference so no
spurious re-render or write occurs (`expect(retagged).toBe(tagged)`).
Non-destructive migration and per-project isolation are test-covered, including
the case that the new fields survive a project-scoped clear (session ids are
globally unique; expansion is a layout preference)
(`.../instances/AGENT1-VALIDATOR/ROUND4_REVIEW.md` §Workspace-state,
§Recording semantics).

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/instances/A-TOKENS-CHROME/RETURN.md`
  (theme field; 9 new tests incl. defaults, fallback, persistence, stale
  snapshot)
- `.../instances/B2-NAV-SESSIONS/RETURN.md` (`sessionSurfaces` +
  `navigatorExpandedSurfaces`; workspace-state tests 11 → 18)
- `.../instances/AGENT1-VALIDATOR/ROUND3_REVIEW.md` (theme mechanism, v1
  schema unchanged, stored-blob compat)
- `.../instances/AGENT1-VALIDATOR/ROUND4_REVIEW.md` (bounded eviction on read
  and write; exact write assertions hold structurally; retag impossible)
- `.../instances/V1-INVARIANT-SWEEP/RETURN.md` (theme and additive fields
  persist under the unchanged v1 schema, independently reproduced)
- `.../instances/V2-RENDER-EVIDENCE/EVIDENCE.md` +
  `.../evidence/navigator-system-1440-oslight.png`,
  `navigator-system-1440-osdark.png`,
  `dialogue-system-1440-osdark.png`,
  `*-reducedmotion.png` (Auto follows the OS in both directions; reduced-motion
  honoured; every capture taken with `chirality.wovenWorkspace.v1` cleared
  first, so each frame is a genuine first-run state)

## Residual recorded in `_STATUS.md` `## Remaining`

Nothing new is owed beyond keeping the schema-version discipline for future
workspace-state fields: additions stay optional-with-default under the
unchanged `chirality.woven-workspace/v1` schema string, or a versioned read
branch must land in the same tranche.

## Other notes of record

- Adopted default D2 governs the honesty framing of `sessionSurfaces`: it is a
  local projection convenience that creates no project truth, retroactive
  surface derivation is impossible, and canonical daemon-side surface metadata
  on `SessionCreateRequest` would require root `runtime/packages/{contracts,core}`
  changes outside this loop's write fence (ADOPTED_BRIEF §4, §8-D2).
- Gate figures cited here were measured before the `1cfd3e293` upstream merge;
  the authoritative post-merge full-gate run is owned by Agent 0 at closeout.
