# Public readiness REPAIR_2 review

RUN_STATUS: SUCCESS — review complete with one narrow finding; actual admission held.
ControlSurface: MERGED
TaskProfile: NONE
TaskSkill: NONE
WriteAuthorization: ALLOWED_WRITE_TARGETS — this review subtree only.
ToolsUsed: read/diff/hash commands; Python evidence; configured --no-cache default-skip Vitest; configured tsc --noEmit.
ToolPolicyCompliance: PASS
Attribution: OpenAI GPT-6; exact serving ID unavailable. Native Agent2/nondelegation instruction-asserted. No delegation or implementation edits, supplier/provider/network/account/build execution.

## Finding

P2: waitForOwnedMarkerIdentity in tests/exact-process-runtime-conformance.test.ts:56-68 checks failure/staleness and target identityChanged, then retries whenever target is absent from ownedGroup/detached. It does not reject target PID in snapshot.gone. DescendantTracker.reconcile puts previously observed but now absent records in gone; that is affirmative disappearance, distinct from the intended not-yet-tracked child race. A later reappearance can consequently be retried into readiness despite the explicit no-disappearance-retry contract. Require immediate rejection when gone contains the target PID, before searching/retrying, and a pure gone-target control. Keep retry only for fresh never-observed absence. Manager acknowledged and dispatched isolated REPAIR_3; actual rerun remains held.

Other mechanics are coherent: a single actionStartedAt+10000 deadline limits identity polling after the existing 8s marker wait; fresh census/stale failures and identityChanged immediately reject; once live tracked, a separate current census must match all ProcessIdentity fields; current disappearance/reuse reject immediately. Markers are reread with exact unchanged PID, full prefix and absent finished marker before interrupt. Original post-retirement disappearance, real retirement/journal/ACK/error correlation, cleanup and time limits remain unchanged. Event parity remains unresolved. No assertion permits fixture cleanup to repair a failed public profile.

Read original Candidate2 public cancel-primary failure: lifetime-ready assertion failed before interrupt; publicRuntimeCancellationProven false; elapsed9712ms; daemon-stop/workers-close each retained DESCENDANT_RECONCILIATION_REQUIRED. Shell-first tracked scan40 and sleep in scan41 support retrying not-yet-tracked absence only. Historical process IDs provide no present signal authority.

## Validation and evidence

Frozen test a7b6cb99a3f19ff6a97601b4a935065d0ea0e14be966da4a588f437fb5f07f97. Author OUTPUTS seal03947f7cdaa99ac86925fda28e50f871e9c48125fbdbe38e8be5b34e91d1e355 and every package file verified. Independent configured no-cache checks: six pure passed, supplier skipped; noEmit exit0. Source before/after stable: True. Manifests record exact read subjects; no source edited by reviewer.

Closure: review complete with gone-target finding. Admit no new actual lifetime rerun until REPAIR_3 freeze/backcheck. Parent owns exact supplier generation and later public profiles. This derivative review inherits accepted OWNER_DIRECTION/SPEC_FAN_IN through manager BASIS/author briefs and leaves original failed evidence immutable. Public cancellation, event parity, production launcher, full G-SBX/orphan, supplier/account/client/release/hold acceptance remain separate.

Outputs: REPORT.md; SOURCE_BEFORE/AFTER.json; INPUT_PACKAGE_VERIFICATION.json; CHECKS.log; OUTPUTS.json.
MISSING: gone-target correction/backcheck and parent actual profiles.
NEEDS_HUMAN_RULING: none.
DEPENDENCY_NOTES: author REPAIR_3 then reviewer and parent actual run; no cycle.
