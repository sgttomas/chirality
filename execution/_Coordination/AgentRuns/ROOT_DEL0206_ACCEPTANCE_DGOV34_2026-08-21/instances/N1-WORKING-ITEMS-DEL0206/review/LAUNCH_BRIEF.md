# Fresh independent review brief — N1 DEL-02-06 exact-byte acceptance

RequestedBy: `WORKING_ITEMS`

RunID: `ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21`

ParentInstanceID: `N1-WORKING-ITEMS-DEL0206`

ChildInstanceID: `N1-FRESH-ACCEPTANCE-REVIEW-01`

AgentType: bounded ephemeral Agent 2 generalist, read-only reviewer

Objective: Independently review 100% of the N1 acceptance-record diff against
the D1 exact-byte ruling, the sealed N1 launch brief, the accepted DEL-02-06
Scope of Work, source preparation evidence, and the semantic-byte acceptance
precedent. Return `PASS` only with zero actionable findings; otherwise enumerate
every finding with exact path/line, violated criterion, and required repair.

RequiredReads:

- root `AGENTS.md` and this brief;
- `execution/_Coordination/AgentRuns/ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21/OWNER_DIRECTION_TRANSCRIPT_2026-08-21.md`;
- parent `LAUNCH_BRIEF.md`;
- DEL-02-06 `ScopeOfWork.md`, pre-diff `_STATUS.md` from basis
  `33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0`, run
  `DEL-02-06-COMPATIBILITY-COMPLETION-004`, and precedent
  `DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003`;
- all current N1 writes: `DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/**`,
  DEL-02-06 `_STATUS.md`, and
  `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-21_ROOT_DEL0206_COMPATIBILITY_ACCEPTANCE.md`.

AllowedTools: repository reads; `git diff`; `git show`; `wc`; `shasum`; `jq`;
source-run deterministic validator. No network, commit, push, PR, merge, or
delegation.

AllowedWriteTargets:

- this review directory's `STATUS.md` and `RETURN.md` only.

AcceptanceCriteria:

1. Candidate at the sealed path is exactly 14,191 bytes and SHA-256
   `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`.
2. Transcript SHA-256 is
   `f38f725f38ab82df105976eb11dc344192b7ffca58bbad3672a1f3d7c6ce36af`,
   accountable human is Ryan Tufts, and D1 is transcribed verbatim.
3. Acceptance snapshot names the exact candidate path, length, SHA, source
   run, and source package-manifest SHA
   `4e6b7062cd4776e7561c0d6a3040342132b1e1641381afe4581219b0bf244e05`.
4. Member verification re-hashes the exact candidate, accepted semantic
   snapshot, sorted semantic manifest, all six semantic members, and source
   run package manifest with no drift.
5. Snapshot/activation/status/notice make no acceptance claim beyond D1,
   preserve all ten held objects, REM-002, REM-003, and `INITIALIZED`, and do
   not infer OUT-*/AC-* evaluation.
6. Scope of Work supplies no automatic lifecycle transition on package
   acceptance; citations and interpretation are accurate.
7. App notice cites exact accepted bytes plus acceptance-record path and SHA,
   routes only coordination for App-owned disposition, and makes no App
   register write or disposition.
8. No accepted historical candidate/member is edited; writes are contained
   to the launch brief's allowed targets; Markdown/JSON/diff hygiene pass.

Escalation: Any mismatch, excess authority claim, missing held object,
historical-byte edit, or out-of-scope write is a blocking finding. Do not
repair. Return findings to the manager for a fresh repair/re-review cycle.
