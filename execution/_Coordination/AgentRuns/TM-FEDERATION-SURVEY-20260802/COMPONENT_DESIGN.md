# Component Design — Task Management Invocation-Local Federation Survey

Status: `FROZEN FOR IMPLEMENTATION`
RunID: `TM-FEDERATION-SURVEY-20260802`
Design owner: `HELPS_HUMANS`
Accepted basis: `main@3e03b257748822dba2ad7697453f3495fb7578db`
Human direction: `HUMAN_DIRECTION.md`
Implementation plan: `plans/chirality-task-management/FEDERATION_SURVEY_IMPLEMENTATION_PLAN_2026-08-02.md`

## Objective and evidence

Every invocation of `TASK_MANAGEMENT` for a loop with a canonical register
must first survey every canonical tracked Task Management register. The survey
is read-only and invocation-local. It creates no obligation for any loop to
invoke `TASK_MANAGEMENT`.

The current live set is discovered from Git-tracked paths rather than a new
authority catalog. The design preserves the existing schema and uses only
`ActionItemID`, `SourceRef`, `NoticeRef`, `ElevatedTo`, `Status`, and
`Disposition` to construct relationships. Notes prose is excluded.

## Governing basis

- `docs/CONTRACT.md` K-TM-1..6 and K-WRITE-2.
- `AGENTS.md` runtime hierarchy and agent-index change-notice rule.
- `docs/WORKFLOW_COMPONENT_STANDARD.md`, especially deterministic-tool,
  write-boundary, generated-view, and handoff requirements.
- `agents/AGENT_TASK_MANAGEMENT.md` and `agents/AGENT_TASK.md`.
- D-GOV-32 and the adopted Task Management PRD remain unchanged upstream
  truth; the present ruling is carried by a new proposed Root decision record.

## Runtime position and construction form

- Persistent invocation semantics: existing Agent 1 package
  `agents/AGENT_TASK_MANAGEMENT.md`.
- Deterministic discovery, validation, joining, classification, and projection:
  existing tool `tools/taskmgmt/taskmgmt.py` with focused tests.
- Current-state inventory and fresh verification: sealed ephemeral Agent 2
  generalists with runtime-managed records. No skill or new dedicated package
  is warranted.
- `HELPS_HUMANS` is the sole component integration owner.

## Entry, delegation, escalation, and permissions

The preflight runs only after `TASK_MANAGEMENT` has been invoked. It precedes
every normal mode. No `LOOP_INIT.md`, workplan, schedule, CI, daemon, or other
entry surface is changed.

The helper reads every tracked canonical register and may write only the
invoking register's gitignored `.candidates/federation.json` projection (or an
explicit `--out` projection). It never writes a register. `TASK_MANAGEMENT`
continues to write only the invoking loop's register after a human disposition.

Schema, CONTRACT/PRD, central catalog, loop-entry, automatic invocation,
foreign-write, or authority-effect expansion returns to H1 and is not inferred.

## Inputs, outputs, and artifact classes

### Discovery contract

Enumerate `git ls-files` and accept only these exact path families:

1. `execution/_Coordination/_TaskManagement/REGISTER.csv`;
2. `projects/<one-segment>/execution/_Coordination/_TaskManagement/REGISTER.csv`;
3. `domains/<one-segment>/execution/_Coordination/_TaskManagement/REGISTER.csv`;
4. `_DomainEngines/<one-segment>/_TaskManagement/REGISTER.csv`.

Tracked `_TaskManagement/REGISTER.csv` lookalikes outside those forms and
untracked lookalikes reported by Git are listed as exclusions and never read as
canonical. Archives, exports, fixtures, evaluation copies, and projections are
therefore excluded by form and tracking status.

Each canonical register is validated with the existing schema validator before
its rows participate in the relationship graph. Root's namespace is `ROOT`.
For other valid non-empty registers, the namespace is the single
`ActionItemID` namespace present in its rows; mixed namespaces are ambiguous.
For a valid header-only register, the path segment is normalized to an uppercase
fallback label and the fallback is disclosed.

### Join grammar

- Global primary index: exact `ActionItemID` values.
- Cross-register source link: exact `TM-<LOOP>-<seq>` token in `SourceRef`.
- Elevation link: exact action-item token in `ElevatedTo`; a target in the
  invoking namespace counts as inbound even when the exact row is absent.
- Notice integrity: every non-empty/non-`NONE` semicolon-delimited `NoticeRef`
  path is resolved; quoting/backticks are presentation wrappers only.
- No relationship is inferred from `Notes` or untyped prose outside the named
  fields.

Relative notice paths are tested against the owning working-root anchor and
the repository root. Project/domain working roots are their respective
`projects/<name>` or `domains/<name>` directories; Domain Engine working roots
are `_DomainEngines/<name>`; Root uses the repository root. Zero matches is
`MISSING_NOTICE`; more than one distinct match is `AMBIGUOUS_REFERENCE`.

### Findings and presentation

The complete finding catalog is:

`INBOUND_ELEVATION`, `FOREIGN_LINK_TO_LOCAL`, `LOCAL_LINK_TO_FOREIGN`,
`OUTBOUND_AWAITING_ACK`, `REMOTE_CLOSED_LOCAL_OPEN`,
`LOCAL_CLOSED_REMOTE_OPEN`, `ORPHANED_LINK`, `DUPLICATE_GLOBAL_ID`,
`MISSING_NOTICE`, `AMBIGUOUS_REFERENCE`, `INVALID_REGISTER`, and
`UNREADABLE_REGISTER`.

All findings are observations. Stable finding records include class, invoking
register context, local/remote IDs when applicable, register paths, cited field,
and evidence value. Sort order is deterministic.

Root presentation includes every finding. Non-Root presentation includes
findings involving the invoking register plus program-level integrity findings
(`DUPLICATE_GLOBAL_ID`, `INVALID_REGISTER`, `UNREADABLE_REGISTER`, and global
ambiguity). The JSON retains the complete finding set and separately identifies
the presented subset, so relevance filtering never hides coverage.

`OUTBOUND_AWAITING_ACK` applies to an invoking-loop `ELEVATED` row whose exact
target does not exist, or to an invoking-loop cross-register source link whose
target does not exist. Existing directed links whose targets exist are
acknowledged for this mechanical purpose; the tool does not infer semantic
acceptance.

Closure echoes compare `Status == CLOSED` across each resolved cross-register
source/elevation link. Each undirected row pair yields at most one deterministic
echo for an invocation.

### Projection contract

Default output is `<invoking-register-parent>/.candidates/federation.json`.
It is a generated view: derived, rebuildable, gitignored, and never authority.
The JSON contains tool/version/command identity, invocation identity, authority
label, coverage, complete register inventory and validation, complete and
presented findings, exclusions, ambiguities/errors, and before/after SHA-256 for
every readable register with `register_writes: 0` only when all hashes match.
No timestamp is emitted, preserving byte determinism for unchanged inputs.

Exit behavior: `0` for a completed `COMPLETE` survey; `1` for a completed
`PARTIAL` survey caused by invalid or ambiguously identified canonical input;
`2` for discovery/read/output operational failure. When possible, `PARTIAL`
or operational evidence is still written and must never be summarized as
global absence.

## QA, fan-in, failure, and handoff

Tests must cover every finding class, all path forms, tracked/untracked and
lookalike exclusion, deterministic bytes, Root/global versus non-Root relevance,
COMPLETE/PARTIAL/operational behavior, notice resolution, semicolon notice
lists, duplicate IDs, and before/after register-hash equality. Existing
`validate` and `scan` behavior remains compatible.

An unavailable helper does not waive the preflight: the invoked manager must
perform the same read-only survey manually, disclose coverage, and avoid a
global-absence claim when coverage is incomplete.

Agent 2 returns are factual evidence, not acceptance. HELPS_HUMANS validates
fan-in and hands the candidate to HELP_HUMAN. TASK_MANAGEMENT behavioral
acceptance and H2 publication remain downstream.

## Compatibility and lifecycle

This is a compatible extension of the active Task Management manager and v0
tool. No register bytes, schema columns, existing command flags, adopted PRD,
CONTRACT invariant, or loop entry behavior changes. The federation projection
may be deleted and regenerated without workflow effect.

## Open decisions

None within H0 scope. Any need for the H1 expansions named above is a blocker
and must return to the owner.
