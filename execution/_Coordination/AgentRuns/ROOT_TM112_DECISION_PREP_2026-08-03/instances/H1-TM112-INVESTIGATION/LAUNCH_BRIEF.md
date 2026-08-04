# H1 launch brief — TM-ROOT-112 graceful-stop investigation

Parent: `HELP_HUMAN` (Agent 0)
Role: `HELPS_HUMANS` (Agent 1 manager)
Node: `N1`
RunID: `ROOT_TM112_DECISION_PREP_2026-08-03`

## Objective

Execute the bounded graceful-stop reproduction/disproof investigation at exact
HEAD/origin-main `88e7590d3664d4f1daf91bed2a8899bda0748b92`, grounded in live row
`TM-ROOT-112` and the exact App notice of record.

## Declared context

- `AGENTS.md` and `agents/AGENT_HELPS_HUMANS.md`.
- `runtime/packages/daemon/src/runtime-daemon.ts` and existing daemon tests.
- App notice:
  `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md`.
- Live register row `TM-ROOT-112`.
- Node runtime and local Unix-socket execution environment.

## Permissions and boundaries

Read repo-wide. Write only under this RunID and disposable `/tmp` paths. Run
local build/test/reproducer commands. Do not implement a runtime fix or modify
source/tests/governance/register/App/Piping/lifecycle/release/reliance/Git.
Do not select intended runtime semantics. No Agent 2 delegation is used.

## Outputs and acceptance

Preserve exact revision/hashes, fixture and commands, timestamped raw output,
timeouts, process/connection/socket/cleanup results, static-vs-executed claim
calibration, hypothesis verdict, contract fact/gap, warranted next scope and
gate, coverage gaps, rerun requirements, containment and cleanliness checks.
Produce manager return, run handoff, and instance return/status.

