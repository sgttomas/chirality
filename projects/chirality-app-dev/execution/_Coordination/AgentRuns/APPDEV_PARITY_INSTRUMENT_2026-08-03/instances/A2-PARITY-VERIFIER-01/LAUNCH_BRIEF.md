# Sealed Brief — A2-PARITY-VERIFIER-01

RequestedBy: `WI-PKG09-DAPP86-A`

RunID: `APPDEV_PARITY_INSTRUMENT_2026-08-03`

ParentInstanceID: `WI-PKG09-DAPP86-A`

ChildInstanceID: `A2-PARITY-VERIFIER-01`

AgentType: fresh ephemeral Agent 2 generalist

Objective: independently verify, without repair, the frozen D-APP-86 Option A
integrated parity evidence produced by `A2-PARITY-EXECUTOR-01`, and return an
`ACCEPT_FAN_IN` or `REJECT_FAN_IN` verdict with exact evidence.

## Governing context to read in full

- repository `AGENTS.md` and `agents/AGENT_TASK.md` for the Agent 2 base contract;
- this brief;
- run-root `ACTIVATION.md`, `WORK_GRAPH.md`,
  `BRIEF_AMENDMENT_01_DEPENDENCY_PROJECTION.md`,
  `BRIEF_AMENDMENT_02_CDP_EQUIVALENT_STATE.md`, `DEPENDENCY_PROJECTION.md`, and
  `DEPENDENCY_PROJECTION_CYCLE_02.md`;
- run-root `RUN_MANIFEST.md`, `EVIDENCE_INDEX.csv`, `PACKAGED_UI_SMOKE.md`,
  `REAL_DAEMON_REPLAY.md`, `VALIDATION.md`, and `HANDOFF.md`;
- executor `LAUNCH_BRIEF.md`, `RETURN.md`, TASK record, and every indexed
  evidence file;
- D-APP-86 packet/ruling, D-APP-88 packet/ruling and R2 return/handoff, and
  D-APP-89 packet/ruling and accepted return/handoff named by the run manifest.

## Allowed reads and tools

- Read-only access to the repository and run evidence.
- Deterministic shell utilities for hashing, parsing, file metadata, Git diff
  inspection, manifest verification, and process/open-file inspection.
- A narrowly escalated read-only `ps` or `lsof` check is allowed only if the
  sandbox blocks the equivalent read-only check.
- Do not launch, package, test, repair, or mutate the product. Do not access or
  expose secrets.

## Allowed writes

- `instances/A2-PARITY-VERIFIER-01/RETURN.md`
- run-root `A2_VERIFIER_RETURN.md`

The two returns must have identical substantive findings. No other write is
authorized. Never edit executor evidence.

## Verification checks

1. Recompute every `EVIDENCE_INDEX.csv` SHA-256 and report row count and any
   mismatch.
2. Recompute the frozen source and package manifests against their recorded
   roots when those roots exist; otherwise verify their recorded check output
   and exact inventory totals. Confirm source 380/380, package 446/446, package
   symlink inventory, executable/app.asar/Info.plist hashes, arm64 identity, and
   adhoc/unsigned posture.
3. Independently parse the captured DOM and accessibility state and correlate
   it with the PNG set. Verify all four D-APP-86 observations:
   - Workbench mounted with live structured deliverable/contract state;
   - Pipeline mounted with DECOMP/PREP/TASK/AUDIT intent;
   - session selection was guarded during a live primary turn and became
     available after completion;
   - real-daemon replay rendered the exact recorded session, two events, one
     transcript item, read-only marker, and terminal event.
4. Confirm replay identity is calibrated exactly: admitted persona
   `WORKING_ITEMS`, role `agent1`; no parent/child attribution is present or
   inferred.
5. Confirm the validation account, including focused 58 tests, typecheck,
   build, sole successful `desktop:pack`, isolated packaged checks, final full
   Vitest 142 files passed / 1 skipped and 1,111 passed / 4 skipped, blocking
   Section 9 16/16, packaged premerge 8/8 plus report-only 16/16, receipt,
   corpus, practitioner, self-check, pytest, dependency lint, manifest checks,
   and secret scan. Confirm the first wrapper's AF_UNIX path-length failure and
   exact shorter-`TMPDIR` retry are disclosed rather than erased.
6. Confirm cleanup and containment: both exact temporary roots absent; no
   child process, CDP/Unix socket/token/open-file residue; owner daemon assets
   untouched; both dependency projections restored to the original real
   `runtime/node_modules` inode/aggregate with no backup residue and zero Root
   diff/status attributable to projection.
7. Confirm D-APP-89 remains at zero compatibility-facade consumers with 13
   rollback probes and the facade retained. Confirm D-APP-88 distinct helper is
   still absent/blocked and is recorded as a non-blocking mandatory future
   parity rerun trigger.
8. Confirm the six D-APP-81 historical relations remain exactly six UNKNOWN,
   with their recorded SHA and no diff.
9. Confirm no D-APP-86 product/config/test/document, foreign-loop, Git,
   receipt, Task Management, decision, deliverable pointer/status, authority,
   decomposition, SCOPE_CHANGE, signing/notarization/release/publication, or
   distribution write occurred.

## Return contract

Return `ACCEPT_FAN_IN` only if every check passes. Otherwise return
`REJECT_FAN_IN`, list each exact failing assertion and evidence path/hash, and
stop without repair. Report evidence limitations truthfully. Record native
token/context occupancy as unavailable if the runtime does not expose it; do
not infer it.

Agent 2 must not delegate.
