# E2-CONTRACT-MAP return

Status: `COMPLETE / PASS FOR MANAGER FAN-IN`

Artifact class: `DERIVATIVE DECISION SUPPORT — NON-AUTHORITATIVE`

## Outcome

`SOURCE_CONTRACT_MAP.md` now provides the required line-addressable map of the
accepted Root constraints, current start/stop and cleanup sequence, ordinary
request and SSE disconnect/interruption flow, exact N1/H1 distinctions, all
owner-approved regression cases, unresolved semantic consequences, and the
App/process/SIGTERM calibration.

The central bounded finding is:

- current `RuntimeDaemon.stop()` immediately clears its server field, awaits
  unbounded `server.close()`, and only on successful close proceeds through
  explicit socket unlink and owner cleanup;
- current stop has no request/response inventory, shutdown-driven canonical
  interruption, grace deadline, or forced residual-connection step;
- N1/H1 directly distinguished completed keep-alive from incomplete ordinary
  HTTP and live SSE, and showed socket-path absence can precede close
  completion and owner-record removal; and
- accepted Root contract text defines daemon ownership and the Unix-socket
  HTTP/SSE surface but not the three semantics the owner expressly reserved.

No duration, cancellation order, forced-close behavior, cleanup error rule,
idempotence rule, or restart rule has been silently selected. These remain
human choices. The map also preserves that the Root mechanism is reproduced
while App R2 causality and first-SIGTERM handling remain unproved.

## Exact bindings

- Source revision: `88e7590d3664d4f1daf91bed2a8899bda0748b92`.
- `runtime-daemon.ts` SHA-256:
  `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`.
- Owner ruling transcript SHA-256:
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
- Original App notice SHA-256:
  `4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656`.
- N1/H1 environment: Node v24.18.0, macOS 26.6 arm64
  (`execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/ENVIRONMENT_AND_COMMANDS.md:23-32`).

## Acceptance check

| Requirement | Result |
|---|---|
| Current stop lifecycle and gaps | PASS — mapped at source-line granularity. |
| SSE disconnect/interruption behavior | PASS — run and session-turn paths, identity timing, callback/error behavior, iterator drain, and canonical interruption are separated. |
| Exact reproduced distinctions | PASS — idle, completed keep-alive, incomplete request, live SSE, and child-process SIGTERM are separate. |
| Accepted Root contract constraints | PASS — binding constraints are separated from the absent shutdown semantics. |
| All approved cases | PASS — present proof and remaining regression obligation are mapped case by case. |
| Human consequences remain unselected | PASS — duration, ordering, forced behavior, error/cleanup, concurrency/idempotence, and restart are explicit TBDs. |
| App causality and process/SIGTERM calibration | PASS — Root mechanism is not promoted to sole App cause; stop is not represented as a signal/process owner. |
| Write containment | PASS — only `RETURN.md` and `SOURCE_CONTRACT_MAP.md` were created in the assigned instance directory. |

## Manager fan-in notes

1. E1's installed Node API evidence should determine which implementation
   mechanisms are feasible; this return deliberately does not infer those API
   guarantees.
2. The manager's option set should keep semantic turn interruption distinct
   from transport/socket termination and should state the manager-run
   pre-identity case explicitly.
3. The manager's cleanup clause should define both the socket pathname and
   owner record; N1/H1 proves that one can disappear before the other.
4. The bounded test plan should include sequential and concurrent lifecycle
   behavior if the selected idempotence/restart semantics require it. Current
   source exposes a stop-in-progress race because the server field is cleared
   before close finishes; this is a source-grounded inference, not executed N1
   proof.

No source, tests, docs, registers, App content, lifecycle, or Git state was
modified by this instance.
