# R13 second-turn diagnosis return

Status: bounded read-only diagnosis complete; product/native qualification remains open.

Upstream: this directory's BRIEF.md; current Runtime source in owner-alignment-inspection-db4335 (brief identifies signed HEAD 1c3ff3a44); owner native event relayed by parent: second turn 16b2047a-0c53-49f4-a79a-44621b8dab4e at 20:13:22.722Z, DESCENDANT_RECONCILIATION_REQUIRED, leaderObserved true, observed 1, scans 65, detachedCount 0, ownedGroupCount 1, identityChangedCount 0, censusFailed false. This return is derivative diagnostic evidence, not accepted decomposition truth or native closure proof.

## Finding

A deterministic synthetic reproduction confirms a stale in-flight census bug. `packages/core/src/descendant-tracker.ts:65-69` coalesces `sample()` onto an already pending census. `reconcile()` at lines 94-95 merely calls `sample()`. Consequently the final reconciliation at `packages/daemon/src/codex-supervisor.ts:310`, although invoked after awaited transport cleanup, can consume a census that started before cleanup completed. The active timer remains running until line 311.

Reproduction sequence: initial synthetic leader census; pre-cleanup reconcile; start and hold another census containing the leader; change synthetic live state to empty (cleanup completed); request post-cleanup reconcile; resolve the held old census. Post-cleanup result has ownedGroupCount 1, scans 3. A truly new reconcile returns ownedGroupCount 0, scans 4. No live census, process inspection, provider call, native call, or Runtime dist rebuild was performed. Source was transpiled into own /tmp scratch only. Exact reproduction: `/tmp/r13-second-turn-diagnosis/repro.mjs`; result `/tmp/r13-second-turn-diagnosis/repro.log`; copied/transpiled source `/tmp/r13-second-turn-diagnosis/descendant-tracker.mjs`. Node v24.18.0, assertions passed twice.

The supplied native signature is consistent with this bug: the sole observed identity is the leader, there are no detached descendants or changed identities, and no census failure. Native source `codex-authenticated-transport.ts:155-189` already awaits leader observation, exact reap, and proven process-group absence before normal cleanup resolves. Successful cleanup followed by one observed leader therefore especially implicates a census snapshot crossing the cleanup boundary. This is a supported causal hypothesis, not proof that native timing followed the synthetic schedule.

No tracker reuse across turns was found. `codex-supervisor.ts:325-327` consumes the preadmitted candidate once; subsequent acquisition launches a new admitted candidate with its own tracker. Existing supervisor tests cover clean/detached/census failure and resumed selection but use immediate synthetic census returns; they do not cover the pending-census cleanup boundary.

## Minimal repair proposal

Add explicit fresh reconciliation semantics: drain any in-flight census and then start a census after the cleanup boundary. Apply that to the supervisor's final reconciliation, retaining failure, detached, changed-identity, and owned-group guards unchanged. A normal concurrent sample can still coalesce; the terminal reconciliation must guarantee its census starts after cleanup. Do not solve this by ignoring leader/owned-group rows, clearing census failures, sleeping, retrying until success, or allowing signaling from tracker observations.

Add a controlled regression at tracker level and, preferably, supervisor observed-close level with a deferred synthetic census begun before controlled cleanup and released after it. Assert clean retirement after a newly initiated empty census; also retain rejection when that fresh census still contains a leader or detached descendant or fails.

The duplicate same-object retirement diagnostic is separate: `withRetirementFailure(primary, retirement)` lacks an identity check and can set `primary.cause = primary`. Parent owns that non-overlapping fix and regression.

## Handoff

Closure verdict: diagnosis complete, repair and native rerun required. No product files edited. No protected trial state, account identity, binding, Codex home, keychain, saved session records, native process metadata, or provider was accessed. Accepted upstream snapshot references remain those in BRIEF; derivative status of this return is explicit. Remaining blockers: parent acceptance of proposed source repair; controlled regression; normal package/review path; owner-controlled repeat native chat/continuation test before native closure. Exact native diagnostic removes census-failure/detached-child hypotheses for this event but cannot alone prove stale timing.

## Authorized repair extension and final handoff

Parent subsequently extended this brief to permit the bounded tracker repair and regressions; the earlier read-only/no-product-edit status above describes the diagnosis phase only and is superseded here.

Changed `projects/chirality-runtime/packages/core/src/descendant-tracker.ts`: reconciliation now drains a pending scan before calling sample, so the census it consumes is initiated after the reconciliation call/cleanup boundary. Existing sample coalescing, scan limits, sticky failure evidence, classifications, and supervisor fail-closed guard remain unchanged. No supervisor source edit was needed.

Changed `projects/chirality-runtime/tests/descendant-tracker.test.ts`: five deferred-census variants verify newly observed gone/live/detached/changed-identity/failure outcomes. The failure variant also confirms a subsequent successful empty census does not erase prior failure evidence.

Verification:
- Preserved prepatch transpiled source plus the new tests: all five regression variants fail deterministically (only two census starts; fresh third scan absent). `/tmp/r13-second-turn-diagnosis/prepatch-tests.log`.
- Patched tracker tests selected to exclude actual host census: 7 passed, 1 skipped. `/tmp/r13-second-turn-diagnosis/focused-tests.log`.
- Existing supervisor detached-survivor/primary-failure/census-failure/clean-closure/initial-observation guards: 5 passed, 37 skipped. `/tmp/r13-second-turn-diagnosis/supervisor-tests.log`.
- `git diff --check` passed.

No dist build, commit, native call, provider call, or broad live process inspection performed. Controlled supervisor fixtures launch only their fake JSONL supplier. No protected identity/session state was accessed. Final closure verdict: bounded source repair + controlled regression complete; parent integration/review, packaging, and native continuation rerun remain required. The repaired race matches native diagnostic shape but native causal qualification remains pending.
