# Routed coordination notice — Root runtime graceful-stop investigation

**Date:** 2026-08-03

**From:** Chirality App Dev loop, D-APP-88 Option B R2

**To:** Root runtime owner / Root coordination loop

**Status:** `ROUTED — COORDINATION ONLY — NOT AUTHORITY`

## Purpose

Request a bounded Root-owned reproduction or disproof of a graceful-stop
hypothesis surfaced by the App D-APP-88 helper-bundle R2 drill. This notice
does not establish causality, authorize a Root change, or ask App to exercise
authority over Root runtime semantics.

## Reciprocal citations

| Evidence | SHA-256 | Role in this notice |
|---|---|---|
| `execution/_Coordination/_DECISIONS/D-APP-88_RULING_DAEMON_HELPER_BUNDLE_IDENTITY_2026-08-02.md` | `858a0d4be9adfca1adf5b990df672fa69000e41a0d840894164d99b382e196c6` | App authority for the bounded distinct-helper tranche; the implementation remains blocked. |
| `execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/MANAGER_RETURN.md` | `4ed34171427ddb7edaee02495ce7e21b1b5c6ad6ba675fe42f53ee99ab56d2a5` | Final R2 `BLOCKED/PARTIAL` manager return and rollback record. |
| `execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/HANDOFF_STATE.md` | `5ff048a4452e546c0b1b97481c1b8456eee2ad1a9d33cd219ab4d553f1d8c918` | Accepted handoff state naming the exact blocker, derivative status, cleanup, and Root hypothesis. |
| `execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/DRAFT_NOTICE_TO_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION_2026-08-03.md` | `7f1a1f283f81d96501e87b87cbfca812449fadb691b2108156fdfae80f0011da` | App-local unrouted draft from which this ordinary notice was claim-calibrated. |
| `execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/DRILL_REPORT.md` | `0ea6c32de0ed122750d2c759e9aee1a163d4275509c6861258c34f5203c09275` | Exact fresh-pass/post-GUI-fail evidence boundary. |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46` | Root source inspected: `stop()` awaits Node `server.close()` before socket and owner-record cleanup. |
| R2 frozen candidate `evidence/candidate-source/electron/main.ts` | `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491` | App candidate teardown awaits `runtimeHost.stop()` before completion logging. |
| R2 sanitized `evidence/raw/desktop-daemon.log` | `3be7915b764dee035ec2a33d57c14fdac66c92373d14c22f623b9672a49f73b5` | Directly records fresh graceful stop and the later helper restart. |
| R2 sanitized `evidence/raw/desktop-main.log` | `3c9ca281da3ac124dd0eb2ac5e894e21f68de71de68d40e6380ae4ec01faa44a` | Directly records GUI contact, later transport loss, and ordinary GUI shutdown. |

All `execution/...` paths above are relative to
`projects/chirality-app-dev/`. Root may cite this notice and the exact evidence
hashes in any reciprocal response; no foreign register write is requested.

## Exact reproduced boundary

### Fresh helper pass — directly evidenced

- Helper PID `40377` started against isolated user-data/home state and bound
  the Unix control socket.
- Its first `SIGTERM` logged `desktop.shutdown.started` and then
  `desktop.shutdown.completed` with exit code zero.
- The helper exited and the control socket was removed.
- The two shutdown entries are preserved in the sanitized daemon log.

### Post-GUI arm — directly evidenced only to this limit

- Helper PID `40416` restarted against the same isolated store and bound the
  control socket.
- GUI PID `40427` contacted that runtime sufficiently to receive
  `Unknown project: chirality-app-dev`.
- The retained daemon log contains no shutdown entry after that GUI contact.
- The GUI log later reports inability to reach the same socket, then records
  its own ordinary shutdown.

The operator also observed first-signal helper survival/socket retention and
termination after a second signal, but no contemporaneous signal command,
process-survival snapshot, or socket snapshot was retained. Those stronger
observations are unauditable and are not promoted as findings.

## Claim-calibrated hypothesis

`HYPOTHESIS — NOT PROVEN`: an active GUI Unix-socket/SSE connection, or
another long-lived client response, may keep Root `RuntimeDaemon.stop()`
awaiting Node `server.close()`. If so, the App teardown path awaiting
`runtimeHost.stop()` would not reach socket/owner cleanup and
`desktop.shutdown.completed` on the first graceful-stop signal.

The fresh-pass/post-GUI contrast and current source sequence are consistent
with this mechanism. They do not establish it. Other App, Electron, signal,
or environment mechanisms remain possible until controlled Root reproduction
or disproof exists.

## D-APP-88 blocker

D-APP-88 Option B remains `BLOCKED/PARTIAL`. R2 proved that a separately built
Electron helper target is structurally coherent, but it did not produce the
mandatory auditable post-GUI first-signal graceful-stop proof. App will not
weaken the ruling, fake GUI teardown, or treat the fresh-only graceful stop as
proof of post-GUI behavior.

## Product rollback and cleanup

- All R2 product/config/test additions were rolled back; no R2 implementation
  was accepted into product state.
- Existing touched R2 files were restored to their D-APP-89 predecessor; the
  independent live D-APP-89 migration candidate is not an R2 product effect.
- No R2 process, launchd job, temporary tree, token/credential artifact, or
  reversible dependency projection remains.
- The untracked standalone derivative
  `frontend/dist-runtime-helper/` was removed after evidence freeze. Shared
  ignored `frontend/dist/` was left untouched for concurrent validation and is
  explicitly non-authoritative/source-misaligned for R2.
- DEL-09-04 remains `IN_PROGRESS`; its Checking Approval SHA is unchanged.

## Requested Root reproduction, disproof, or action

Under Root authority, please:

1. reproduce `RuntimeDaemon.stop()` with an active Unix-socket client and with
   a live SSE/other long-lived response, preserving signal, process, socket,
   connection, and cleanup evidence;
2. determine whether Node `server.close()` completes in each case and bind the
   result to the exact Root source revision;
3. define the intended Root connection-drain/termination contract for graceful
   daemon shutdown, including socket and owner-record cleanup;
4. add bounded Root tests for ordinary stop with active clients/streams;
5. if a Root defect is established, implement and validate the change through
   Root's own scope, decision, Task Management, validation, and Git gates, then
   return exact commit/test/evidence references to App; or
6. if the hypothesis is disproved or no Root change is warranted, return the
   disproving evidence and identify the next bounded App diagnostic seam.

Root may amend, defer, decline, or disposition this request through its own
instruments. This notice grants no Root source, scope, register, lifecycle,
release, or Git authority and creates no App acceptance of a future response.

`TM-CANDIDATE: Root RuntimeDaemon graceful stop may remain pending on an active Unix-socket/SSE connection, blocking auditable post-GUI first-signal teardown required by D-APP-88 | NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md; D-APP-88 R2 DRILL_REPORT.md SHA-256 0ea6c32de0ed122750d2c759e9aee1a163d4275509c6861258c34f5203c09275; runtime-daemon.ts SHA-256 a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`
