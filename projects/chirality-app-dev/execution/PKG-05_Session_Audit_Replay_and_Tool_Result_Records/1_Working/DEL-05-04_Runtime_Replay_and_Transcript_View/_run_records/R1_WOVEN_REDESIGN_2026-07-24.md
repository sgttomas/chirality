# R1 Woven Dialogue Visual Redesign & IA Consolidation — DEL-05-04

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
- Consumption posture: the 2026-07-24 tranche consumed DEL-05-04 semantics
  **read-only**. ADOPTED_BRIEF §2 lists DEL-05-04 as consumed, not owned, and
  §1 withholds authorization for any runtime or replay-semantic change.
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged by this record.

## What landed for DEL-05-04

**PR #323 (merge `403f228f4`).** The provider-neutral semantic projection of
canonical UI events and the GET-only selected-session replay boundary were
implemented. Replay is bounded, identifies its source session, suppresses
foreign-session content and discloses the suppression, and exposes no send,
interrupt, permission, resume, boot, delete, or lifecycle action. The primary
live dialogue stays mounted while the replay lens or an artifact is focused
(`.../APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/PACKAGE_RETURNS.md`
§PKG-05; `.../REVIEW.md`).

**This tranche (branch `feat/woven-redesign`).** No replay semantics changed.
Stage B2 (`b17ab9d39`) made the lens reachable from the recomposed navigator:
recorded-session rows call the existing guarded path
(`onSelectSession={loadReplay}`), and validation confirmed
`guardRecordedSessionSelection` remains a single call site with an unchanged
argument shape (`.../instances/B2-NAV-SESSIONS/RETURN.md`;
`.../AGENT1-VALIDATOR/ROUND4_REVIEW.md` §Replay routing). Stages A/C
(`2afcd8474`, `04d3b4f5f`) restyled the lens through tokens only, and round 7
(`787e18146`) widened the provenance-label track so the `Source` value has more
room. `1cfd3e293` merged `main` into the branch.

Isolation was live-proven, not assumed. V1 exercised the lens in the running
app and confirmed exactly one `<button>`, zero forbidden verbs
(Send/Continue/Interrupt/Allow/Deny/Resume/Boot/Delete), a primary-dialogue
draft that survives the round trip, a primary controller node that is never
remounted, and double-guarded selection
(`.../instances/V1-INVARIANT-SWEEP/RETURN.md`). V2 walked the keyboard path
from a navigator session row into the lens and back
(`.../instances/V2-RENDER-EVIDENCE/RETURN.md`).

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/instances/V1-INVARIANT-SWEEP/RETURN.md`
  (replay isolation live proof)
- `.../instances/AGENT1-VALIDATOR/ROUND4_REVIEW.md` (guarded routing unchanged)
- `.../instances/V2-RENDER-EVIDENCE/EVIDENCE.md` §1.1 (declared fixture
  pass-through) and `.../evidence/replay-{light,dark}-{900,1180,1440}.png`
- `.../instances/AGENT1-VALIDATOR/ROUND7_REVIEW.md` (F-3 provenance-label
  track, corrected diagnosis)

## Residuals recorded in `_STATUS.md` `## Remaining`

1. The pre-existing gated item — Desktop and CLI replaying the same
   daemon-owned canonical session with manager/child attribution preserved
   across restart and lazy migration — is **retained verbatim**; it remains
   gated on the daemon/client vertical slice and was not touched by this
   tranche.
2. The SCA-APP-004 replay-lens item is rewritten to its true residual: replay
   **transcript-item rendering against a real daemon session remains
   unevidenced**. No runtime daemon was available for the 2026-07-24 evidence
   pass — `GET /api/harness/session/list` returned
   `503 ENGINE_UNAVAILABLE` — so `session/list` and `session/:id/events` were
   served by a declared local fixture proxy. All application code paths
   exercised were the real ones, but the fixture events do not match the
   transcript-derivation schema, so the lens reported
   `Transcript items shown 0`: its READ-ONLY framing, provenance block and
   event count are evidenced, the transcript list itself is not
   (`.../instances/V2-RENDER-EVIDENCE/EVIDENCE.md` §1.1;
   `.../instances/V2-RENDER-EVIDENCE/RETURN.md` caveat 1). The honest
   daemon-unavailable state is captured in
   `.../evidence/navigator-{light,dark}-1440-nostub.png`.

## Other note of record

Gate figures cited here were measured before the `1cfd3e293` upstream merge;
the authoritative post-merge full-gate run is owned by Agent 0 at closeout.
