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

- New `frontend/src/lib/lifecycle/amendment-reopen.ts`: a port of the
  working-tree mode of `check_amendment_reopen.py` as revised at `5038f2554` (the
  Root review fix). It keeps that mode's admission rules and its 18 refusal
  codes: `REFUSAL_CODES` less the at-commit `APPROVAL_SHA_UNREACHABLE` and
  `APPROVAL_SHA_NOT_ANCESTOR`. The port covers:
  - the anchored group-3 heading and the strict decision-folder names;
  - `DELIVERABLE_REMOVED` and `AMENDMENT_ALREADY_USED`;
  - the scope-change root beside the outermost `execution/` folder, with the
    adapter-manifest agreement rule;
  - the latest binding group-2 revision, the `AmendmentID` equal-or-blank rule,
    exact `Role` matching and unstripped register values;
  - containment: paths are resolved after symbolic links inside the project root
    and inside the scope-change root.

  To decide as the Python checker does, the port reproduces Python's path,
  `realpath`, `csv` (excel dialect), `str.strip`, `str.splitlines` and `repr`
  behaviour. The first candidate (`6dc8f8356`) followed `be76d5b9e`, and this
  revision brings it to `5038f2554`. The App adapter uses the Git work-tree top level above the working
  root, found from the filesystem, as the project root, as `write_status.sh`
  does. It falls back to the working root when there is none. It refuses a
  scope-change root outside the working root as `PATH_ESCAPE`.
- `transition.ts`: a rule `ISSUED -> IN_PROGRESS` (HUMAN, `amendmentReopen`).
  Without `amendment` the move stays `BACKWARD_TRANSITION`. With one, the actor,
  approval SHA and metadata are checked first, and a `ruling` is rejected
  (`RULING_NOT_APPLICABLE`). `transitionStatusFile` then runs the check on the
  deliverable folder, passing the `_STATUS.md` content it already read for the
  prior-reopening check. A refusal is `AMENDMENT_NOT_ADMITTED`, carrying the
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
  the fixture trees into `cases.json`: 107 trees and 130 queries. They mirror the
  Root tests, add CSV, heading, path and symlink cases, and add cases for each
  rule of the review fix (heading variants, candidate and revised folder names,
  removal, prior reopening with status files, package and nested execution
  roots, adapter agreement, revised group-2 bindings, `AmendmentID`, `Role` and
  whitespace). It records the Root checker's working-tree decisions (no
  `--at-commit`) in `expected.json`, together with 11 queries on the real PEC
  SCA-005/SCA-006, Piping SCA-011, Runtime SCA-003 and App SCA-APP-010 records.
  `--check` reports drift.
  `amendment-reopen-parity.test.ts` materializes the same trees and compares
  every decision field, reason text included. It also checks that the App's
  refusal codes plus the two Root-only codes equal the Python `REFUSAL_CODES`.
  It skips a real case whose records are absent. In the first candidate the
  test's repository-root path was one level short, so the real cases were
  skipped silently; this revision corrects it, and a mutation that drops the
  removal rule now fails the real PEC SCA-005 case as well as three fixtures.
- App SPEC §4.3, work-graph FU1, DEL-07-04 MEMORY, `loop/LOOP_RECEIPTS.md`
  Receipt-267 and the tranche manifest
  `docs/governance_harness/tranche_manifests/APP-AMENDMENT-REOPEN-20260926.yaml`.

## Review fixes (on `2a0e9841d`)

- **B1: a pre-existing defect, fixed here.** Every App transition rebuilt
  `_STATUS.md` from its parsed form. That dropped every section after
  `## History`, and every history line the list pattern does not read, such as
  an actor containing `)`. It also dropped the reopening line `write_status.sh`
  appends at the end of the file. The reviewer's replay then passed:
  1. `write_status.sh` reopens under SCA-001.
  2. The App moves the deliverable to CHECKING, and the rewrite drops the line.
  3. The App moves it to ISSUED.
  4. The App reopens again under SCA-001, and that was ADMITTED.

  `updateStatusDocument` now edits in place. It changes only:
  - the first `Current State` and `Last Updated` values;
  - the metadata fields it sets, updates or removes above `## History`;
  - the one history line it appends at the end of the History section (a table
    row for table-format history).

  Everything else is kept verbatim, in order and with its line endings.
  `applyLifecycleTransition` also refuses (`HISTORY_NOT_PRESERVED`) a transition
  whose output would drop any `reopened from ISSUED; amendment: <ID>` marker of
  its input.
  - Tests cover the replay with a trailing section, the replay with an actor
    containing `)`, a CRLF trailing section kept byte-for-byte, an unread history
    line, owned-field edits and table history.
  - Negative control: with the old writer in place, the six new preservation
    tests fail, and both replays stop at `HISTORY_NOT_PRESERVED`.
- **Scan of all 698 tracked files ending in `_STATUS.md`**, of which 689 are
  named exactly `_STATUS.md` (NUL-separated list). Each file
  was copied into memory and given a legal next transition through
  `applyLifecycleTransition`, or, for the one ISSUED file, through the writer
  alone.
  - 175 files do not parse for the App (163 `INVALID_STATE`, such as `RETIRED`;
    12 `INVALID_STATUS_FORMAT`), so the App cannot transition them.
  - For the 523 others, every original line is kept in order, apart from the
    owned field values, with nothing added but owned field lines and the new
    history line: 0 files lost content. 110 of them have a trailing section and
    345 have history lines the parser does not read.
  - On the same 523 files, the old writer rewrote or dropped non-owned lines in
    every one, 3,909 lines in all.
- `applyLifecycleTransition` now requires the decision to name the requested
  amendment and the deliverable, and refuses one that does not
  (`AMENDMENT_NOT_ADMITTED`). The requested amendment is the ID given, or the ID
  of the snapshot or decision folder a path names. The deliverable is the one
  whose folder `transitionStatusFile` reads, or the ID in the status title.
- Size bounds: the checker reads amendment records up to 5 MiB, the App
  precedent, and refuses a larger one as `AMENDMENT_CHECK_ERROR`. Of a group-3
  `DECISION.md` it reads only the first 64 KiB, up to the last complete line,
  because only the first non-blank line counts.
- App SPEC §4.3 states the normalized-label rule exactly, the in-place writer
  rule and the check-to-write race.

## D2 caller scan

- Tracked files ending in `_STATUS.md` (NUL-separated `git ls-files -z`): 698,
  of which 689 are named exactly `_STATUS.md`. The
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
  adds no process spawning. It therefore makes none of the Root checker's
  anchored at-commit checks, which are Root-only:
  - that the approval SHA is a reachable commit (`APPROVAL_SHA_UNREACHABLE`);
  - that it is an ancestor of `HEAD` (`APPROVAL_SHA_NOT_ANCESTOR`);
  - that every amendment record is read from that commit (`--at-commit`).

  It reads the working-tree records, so uncommitted edits to them are not
  detected, and its decision is unanchored. `write_status.sh` uses only the
  at-commit mode and is the anchored check.
- The actor is caller-asserted, as for the other human gates (REQ-005 live
  limit). An agent that supplies HUMAN, a well-formed SHA and an amendment whose
  records pass can reopen through the MCP tool, exactly as it can reach
  CHECKING or ISSUED.
- The Git work-tree top level is found by the nearest `.git` directory or file.
  `GIT_DIR`, `GIT_CEILING_DIRECTORIES` and similar git discovery settings are
  not honoured.
- In-place writer limits (recorded after review, in run
  `APP-TRANSITION-FORMS-2026-09-26`):
  - fields and other content below `## History` are preserved but not managed,
    so a stale `Checking Approval SHA` in a trailing section is not removed on
    the reversal;
  - a table-format history row is appended after the last non-blank line of the
    History section, so after any paragraph that follows the table;
  - a `## ` line inside a code fence counts as a heading when the writer finds
    the end of the History section.
- Check-to-write race: `transitionStatusFile` reads `_STATUS.md`, runs the
  asynchronous amendment check and rewrites the file with no lock. A concurrent
  write inside that window can be lost, as for every App transition.
- The App's size bounds differ from the Python checker, which reads records
  whole. An App refusal of a record over 5 MiB is `AMENDMENT_CHECK_ERROR`.
  Invalid UTF-8 beyond the 64 KiB `DECISION.md` prefix is not decoded, so the
  App admits where Python would stop with a usage error. The parity fixtures
  stay within both bounds.
- The port follows the Root checker at `5038f2554`. A later Root change needs a
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
