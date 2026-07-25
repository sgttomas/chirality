# R2 Real Daemon Session Reachable on the Packaged App — DEL-05-04

- Date: 2026-07-25
- Run: `APPDEV_DAEMON_SERVICE_2026-07-25`
- Basis: `TRB-APPDEV-DAEMON-SERVICE-2026-07-25`
  (`execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/ADOPTED_BRIEF.md`),
  adopted by owner direction in-session 2026-07-25.
- Branch: `feat/daemon-service` (`8c20f214d` … `45aeaa465`, base
  `e9068c87d76c75b133f3686db8bf453565ce8fa2`).
- Predecessor record: `_run_records/R1_WOVEN_REDESIGN_2026-07-24.md`, which
  recorded the replay-lens evidence gap this record narrows the cause of.
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged. No replay or transcript
  code was touched by this tranche.

## What landed for DEL-05-04

Nothing in the replay lens or the transcript view changed. What changed is the
precondition that blocked its evidence.

The 2026-07-24 browser-evidence pass ran with no runtime daemon available and
substituted declared fixtures for the session list and session events, so the
lens showed an empty transcript list: its read-only framing, provenance block and
event count were evidenced, but the transcript items were not.

This tranche removed the daemon-unavailability cause on the packaged app. The
daemon runs as a supervised machine-local service, the GUI binds without manual
action and rebinds by itself after an outage, and a stub-adapter turn ran
end-to-end through the packaged GUI's harness surface and terminated with a zero
process exit. A real daemon-owned session with recorded events therefore exists
and is producible on demand; the drill evidence retains the session-create
response and the turn event stream.

Two boundaries the record must keep straight:

1. The session produced in the drills lived under the isolated temporary user
   data and was deleted at cleanup; only the evidence copies survive. The claim
   is that the route to a real daemon session is proved, not that a durable
   session was left behind for a later pass.
2. Session state lived entirely daemon-side under the daemon's own user data —
   registering a project root did not by itself cause writes into the registered
   worktree. That matters for how a future replay-evidence pass locates the
   session it renders.

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/instances/V-PACKAGED-DRILLS/RETURN.md`
  §1 (drill V9), §4 (binding and rebinding timings), §5 minor notes (daemon-side
  session location); `.../evidence/v9/turn-sse.txt`,
  `.../evidence/v9/session-create.json`, `.../evidence/v3/summary.json`
- `.../instances/AGENT1-VALIDATOR/ROUND2_REVIEW.md` §1, §3
- `.../HANDOFF_STATE.md`

## Residuals recorded in `_STATUS.md` `## Remaining`

Both items stay open. The transcript-item Remaining entry is amended only to
record that daemon unavailability no longer blocks it and to point at the
evidence that a real daemon-owned session is reachable from the packaged app.
The transcript list itself is still unevidenced, and the gated
Desktop-and-CLI-replay item is untouched.
