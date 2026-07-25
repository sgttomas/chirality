# R6 Daemon-Down Credential Status and Runtime Feedback — DEL-02-05

- Date: 2026-07-25
- Run: `APPDEV_DAEMON_SERVICE_2026-07-25`
- Basis: `TRB-APPDEV-DAEMON-SERVICE-2026-07-25`
  (`execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/ADOPTED_BRIEF.md`),
  adopted by owner direction in-session 2026-07-25.
- Branch: `feat/daemon-service` (`8c20f214d` … `45aeaa465`, base
  `e9068c87d76c75b133f3686db8bf453565ce8fa2`).
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged. The single `Remaining`
  item is unchanged — it is gated on the D-APP-73 Desktop migration and security
  review, neither of which this tranche performed.

## What landed for DEL-02-05

**Credential status stops throwing when the daemon is down (`3e7e57e04`).** The
packaged drills surfaced an unhandled rejection on the renderer channel whenever
the daemon was unreachable: the API-key status handlers propagated the missing
operator-token error into the renderer as a raw handler failure. Both the
generic and provider-scoped status channels now catch a daemon-down failure and
return an explicit unavailable snapshot (no key, source none, error attached)
instead of rejecting, while an unsupported provider is still rejected before the
daemon is consulted. A test asserts a real answer is not mislabelled as
unavailable, so the unavailable state cannot mask a genuine result.

**Runtime feedback now has a real connectivity source (`22752cf67`).** Daemon
connectivity is owned in the main process by a binding supervisor with a retry
ladder and a steady liveness probe, published to every window over a dedicated
IPC channel, and rendered as a top-bar chip. Failure reasons are redacted
through the same credential-shaped pattern used by the runtime-control channel,
so no token text can reach the renderer or the log. Runtime feedback is
therefore an observed state rather than a proxy for working-root state; the chip
itself is recorded against DEL-02-01.

**The daemon is a working encrypted credential holder on the packaged app.**
Drill evidence shows an Electron `safeStorage` encrypt/decrypt round trip inside
the headless daemon under `prohibited` activation policy, over the isolated
control socket, including a decrypt by a later daemon process, with negative
controls that flip the recorded state when the stored blob is corrupted and no
Keychain prompt or blocking call. That is evidence toward the deliverable's
gated "daemon as single encrypted credential owner" scope; it is not that scope's
implementation, and the dummy credential was removed before the later drills and
deleted with the isolated tree.

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/instances/V-PACKAGED-DRILLS/RETURN.md`
  §3 (safeStorage verdict and negative controls) and §5 minor findings (the
  renderer-channel throw this tranche fixed);
  `.../instances/V-PACKAGED-DRILLS/evidence/v2/`
- `.../instances/AGENT1-VALIDATOR/ROUND2_REVIEW.md` §1 (minor finding — credential
  status no longer throws to the renderer)
- `.../instances/A-DAEMON-SERVICE/RETURN.md` §5 (connectivity surface, redaction
  of failure reasons)
- `.../HANDOFF_STATE.md`

## Residuals recorded in `_STATUS.md` `## Remaining`

No change. The D-APP-73 item — daemon as the single encrypted credential owner,
plus daemon/provider/model status and explicit activation controls in Desktop
settings — remains open and gated. Nothing in this tranche moved that gate; the
credential round-trip evidence above is a prerequisite observation, and the
settings surface was not touched.
