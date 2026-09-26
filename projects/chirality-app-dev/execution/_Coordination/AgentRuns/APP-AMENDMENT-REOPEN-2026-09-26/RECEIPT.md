# Receipt — APP-AMENDMENT-REOPEN-2026-09-26

Derivative account. The [work graph](../../WorkGraphs/app-lifecycle-deps-2026-09-26/WORK_GRAPH.md)
(row FU1) carries execution, and the sources below keep their authority.

## Owner direction

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. Ryan Tufts, 2026-09-26, Claude Code
conversation, on the parent session's D1–D4 recommendations and work plan:

> D1 and D2 as recommended, D3 (a), and D4 yes proceed that way. Your work plan is approved.

As the parent session relayed it to this run, the approved plan covers:

- **FU1.** The App status tools check the amendment record before admitting
  `ISSUED -> IN_PROGRESS`, mirroring the Root checker
  `tools/validation/check_amendment_reopen.py` (PR #968,
  `ROOT-DGOV50-ENFORCEMENT-20260926`).
- **D2 as recommended.** `Authorization Basis`, `Accepted Basis SHA` and
  `Accepted ScopeOfWork SHA-256` are gate evidence. Caller metadata may set them
  only on HUMAN-actor transitions; any other key stays settable by any actor.
  The approval SHA fields and the lifecycle fields were already reserved.

The parent session relayed only these two items to this run. D1, D3 and D4 are
recorded here only as part of the quoted decision.

## Root notice adoption

| Notice | This loop's adoption |
|---|---|
| `NOTICE_2026-09-26_DGOV50_ENFORCEMENT.md` | Adopted for DEL-07-04. `transition.ts`, the transition API, the MCP `status_transition` tool and the client type admit `ISSUED -> IN_PROGRESS` only for a HUMAN actor with a format-valid approval SHA and an `amendment` that passes the ported check, with the notice's refusal codes and legacy-register rule. This answers DEL-07-04 REQ-004 in the validator. App SPEC §4.3 states the rule and its limits. |

## Result

- New `frontend/src/lib/lifecycle/amendment-reopen.ts`: a port of
  `check_amendment_reopen.py` at `be76d5b9e`. It keeps the three admission checks,
  the sixteen refusal codes, the legacy `ScopeChanging` rule and the containment:
  paths are resolved after symbolic links inside the project root and inside the
  scope-change root. To decide as the Python checker does, the port reproduces
  Python's path, `realpath`, `csv` (excel dialect), `str.strip` and `repr`
  behaviour. The App adapter uses the Git work-tree top level above the working
  root, found from the filesystem, as the project root, as `write_status.sh`
  does. It falls back to the working root when there is none. It refuses a
  scope-change root outside the working root as `PATH_ESCAPE`.
- `transition.ts`: a rule `ISSUED -> IN_PROGRESS` (HUMAN, `amendmentReopen`).
  Without `amendment` the move stays `BACKWARD_TRANSITION`. With one, the actor,
  approval SHA and metadata are checked first, and a `ruling` is rejected
  (`RULING_NOT_APPLICABLE`). `transitionStatusFile` then runs the check on the
  deliverable folder. A refusal is `AMENDMENT_NOT_ADMITTED`, carrying the
  checker's code; an unreadable record or a missing project root is
  `AMENDMENT_CHECK_ERROR`. An `amendment` on any other transition is
  `AMENDMENT_NOT_APPLICABLE`. The history entry reads
  `[reopened from ISSUED; amendment: <ID> (<group-3 snapshot>); action: <register> ActionSeq <n> <type>; register SHA-256: <sha>; approval SHA: <sha>]`.
  Existing approval fields are left as history, as `write_status.sh` leaves them.
- D2: the transition metadata guard rejects the three gate-evidence labels
  (normalized form) unless the actor is HUMAN/USER/OPERATOR.
- `amendment` is wired through `deliverable-contracts.ts`, the transition route,
  `deliverable-api.ts` and the MCP `status_transition` zod schema, as `ruling` was.
- Parity: `src/__tests__/fixtures/amendment-reopen/generate_expected.py` builds
  the fixture trees into `cases.json`: 66 trees and 79 queries, mirroring the
  Root tests plus CSV, heading, path and symlink cases. It records the Root
  checker's decisions in `expected.json`, together with 10 queries on the real
  PEC SCA-005/SCA-006, Piping SCA-011, Runtime SCA-003 and App SCA-APP-010
  records. `--check` reports drift.
  `amendment-reopen-parity.test.ts` materializes the same trees and compares
  every decision field, reason text included. It skips a real case whose
  records are absent.
- App SPEC §4.3, work-graph FU1, DEL-07-04 MEMORY, `loop/LOOP_RECEIPTS.md`
  Receipt-267 and the tranche manifest
  `docs/governance_harness/tranche_manifests/APP-AMENDMENT-REOPEN-20260926.yaml`.

## D2 caller scan

- Tracked `_STATUS.md` files (NUL-separated `git ls-files -z`): 698. The
  gate-evidence labels occur in the Root `execution/` tree (`Authorization Basis`
  212, `Accepted Basis SHA` 180, `Accepted ScopeOfWork SHA-256` 32), written by
  Root project-setup materialization and Root tools, not by App transitions.
  They also occur in 53 App files (`Authorization Basis` only). Those were written
  by the 2026-06-20 INSP-01 transitions, with actor `HUMAN`
  (`plans/artifacts/insp01_status_transition_log_2026-06-20.json`). PEC, Piping,
  Runtime and `_DomainEngines` have none.
- App callers that pass metadata: the transition API route passes the
  caller's `metadata` through; the MCP `status_transition` tool passes the
  agent's `metadata` through; the workbench and pipeline forms pass none. No App
  source, instruction, workflow or skill sets these keys. The only in-repo writer
  through App metadata is INSP-01, with a HUMAN actor. The one test that sets
  them with an agent actor calls `updateStatusDocument` directly, below the
  transition guard, and is unchanged.
- Result: no current agent-actor caller sets these keys.

## Checks (worktree candidate)

Recorded in the commit's hand-off to the parent session: APP-HOLD-1 `dispatch`
ALLOW for DEL-07-04 and `scan --require-register-match` exit 0; typecheck;
focused and full Vitest; the negative control (the new transition, API and MCP
tests fail against the prior source); generator `--check`; export
regeneration; the Root validators.

## Limits

- The App runs no git process: no existing App pattern runs git, and this run
  adds no process spawning. It therefore does not check that the approval SHA is
  a reachable commit, that the group-3 `DECISION.md` exists at that commit, or
  that the amendment records are committed. It reads the working-tree records,
  so uncommitted edits to them are not detected. `write_status.sh` makes the git
  checks and is the anchored check.
- The actor is caller-asserted, as for the other human gates (REQ-005 live
  limit). An agent that supplies HUMAN, a well-formed SHA and an amendment whose
  records pass can reopen through the MCP tool, exactly as it can reach
  CHECKING or ISSUED.
- The Git work-tree top level is found by the nearest `.git` directory or file.
  `GIT_DIR`, `GIT_CEILING_DIRECTORIES` and similar git discovery settings are
  not honoured.
- The port follows the Root checker at `be76d5b9e`. A later Root change needs a
  matching App change and a regenerated `expected.json`; `generate_expected.py
  --check` reports the drift.
- The Runtime `status_transition` descriptor does not list `ruling` or
  `amendment` (FU2), and the workbench and pipeline forms have no reopening input
  (FU3). No lifecycle transition, approval-SHA refresh, authority-corpus repin,
  release or issuance.

Execution: a Claude Code subagent (TASK-type executor, no delegation) in an
isolated worktree for the parent session. Model identifiers are withheld at the
dispatching session's instruction; the commit's session trailer identifies the
run.
