# HELPS_HUMANS route return v1 — D-APP-88 R2 Root investigation notice

**Date:** 2026-08-03

**Version:** `v1`

**Status:** `APP NOTICE ROUTED — NO FOREIGN WRITE`

## Routed artifact

App coordination notice:

`projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md`

SHA-256:
`4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656`.

The notice is addressed to the Root runtime owner / Root coordination loop but
lives only on the App loop's own ordinary coordination surface. No Root or
other foreign surface was written.

## Accepted route basis

| Basis | SHA-256 |
|---|---|
| `MANAGER_RETURN.md` | `4ed34171427ddb7edaee02495ce7e21b1b5c6ad6ba675fe42f53ee99ab56d2a5` |
| `HANDOFF_STATE.md` | `5ff048a4452e546c0b1b97481c1b8456eee2ad1a9d33cd219ab4d553f1d8c918` |
| `DRAFT_NOTICE_TO_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION_2026-08-03.md` | `7f1a1f283f81d96501e87b87cbfca812449fadb691b2108156fdfae80f0011da` |
| `instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/DRILL_REPORT.md` | `0ea6c32de0ed122750d2c759e9aee1a163d4275509c6861258c34f5203c09275` |
| Root `runtime/packages/daemon/src/runtime-daemon.ts` | `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46` |
| frozen candidate `evidence/candidate-source/electron/main.ts` | `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491` |
| sanitized `evidence/raw/desktop-daemon.log` | `3be7915b764dee035ec2a33d57c14fdac66c92373d14c22f623b9672a49f73b5` |
| sanitized `evidence/raw/desktop-main.log` | `3c9ca281da3ac124dd0eb2ac5e894e21f68de71de68d40e6380ae4ec01faa44a` |

## Claim and boundary carried

The notice carries only this hypothesis: an active GUI Unix-socket/SSE or
other long-lived client response may keep Root `RuntimeDaemon.stop()` awaiting
Node `server.close()`, which may prevent the App teardown path from reaching
socket/owner cleanup and `desktop.shutdown.completed`.

It also carries the exact evidence boundary:

- fresh helper first-signal graceful stop, zero exit, and socket removal are
  directly evidenced;
- after helper restart and GUI contact, the retained daemon log has no later
  shutdown entry and the GUI later reports transport loss; and
- observed first-signal survival/socket retention and second-signal
  termination remain unauditable and are not promoted as findings.

D-APP-88 remains `BLOCKED/PARTIAL`. Product rollback and cleanup are recorded;
no R2 implementation is accepted.

## Root request and authority boundary

The notice asks Root to reproduce or disprove the hypothesis with active
Unix-socket/SSE clients, define intended drain/termination semantics, add
bounded tests, and return exact evidence. Any Root change remains subject to
Root's own scope, decision, Task Management, validation, and Git gates. The
notice creates no App authority over Root and no App acceptance of a future
Root response.

The notice includes the required harvest marker:

`TM-CANDIDATE: Root RuntimeDaemon graceful stop may remain pending on an active Unix-socket/SSE connection, blocking auditable post-GUI first-signal teardown required by D-APP-88 | NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md; D-APP-88 R2 DRILL_REPORT.md SHA-256 0ea6c32de0ed122750d2c759e9aee1a163d4275509c6861258c34f5203c09275; runtime-daemon.ts SHA-256 a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`

## Validation

- Every reciprocal source path resolved and every cited SHA-256 reproduced.
- Notice wording distinguishes direct evidence, unauditable observations, and
  the unproven hypothesis.
- Targeted high-confidence secret-pattern scan returned no match.
- Trailing-whitespace scan returned no match.
- `git diff --check` passed over the shared working tree at route time.
- Write containment for this route is exactly the App notice and this
  versioned route return; no decision/register/Task Management/receipt/source/
  deliverable/Git or foreign-loop write was made by HELPS_HUMANS.

## Handoff

Root is the next lawful owner for reproduction, disproof, or disposition. App
holds D-APP-88 open and should not retry packaging identity work until the
graceful-stop mechanism is dispositioned or another bounded App diagnostic
seam is evidenced.
