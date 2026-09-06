# P4 repair 3 independent review

RUN_STATUS: SUCCESS (review complete; diagnostic admission withheld)
ControlSurface: MERGED; TaskProfile: NONE; TaskSkill: NONE.
ScopePath: /Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/IMPLEMENTATION/REVIEW_P4/REPAIR_3
Attribution: OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent2/nondelegation instruction-asserted. No delegation.

## Verdict and finding P4-R3-1

DO NOT ADMIT frozen role fixture `8730309e7ab901953c8c0700f33b90bfb231d0de8492f317da5e8b852ce39d62` until its first-SessionMeta reader enforces the declared exact supplier path layout.

At exact-role-conformance.test.ts:93, matching regular files are accepted at every depth. The directory branch restricts directory names/depth, but the file branch never requires depth3 and matches any name starting rollout- and ending with the child ID. The reader therefore accepts `sessions/rollout-not-a-date-<child>.jsonl` and `sessions/2026/09/06/rollout-not-a-date-<child>.jsonl`. Both were independently reproduced using the exact extracted/transpiled reader, synthetic first SessionMeta only and reviewer-owned scratch. REPRO.json records accepted=true in both cases. No supplier, transcript or account content was read.

This contradicts the parent exact-layout requirement and the author's claim of the known three date levels. Supplier recorder.rs:1613-1624 constructs sessions/YYYY/MM/DD and RolloutFileName::render in rollout_file_name.rs renders the timestamp as YYYY-MM-DDTHH-MM-SS plus thread ID (an underscore rollout ID suffix is reserved for reverted threads). These are source observations, not inferred conventions. For this newly spawned non-reverted child, require exactly the three valid date levels, a canonical dated filename with the exact child ID and path/date consistency; reject misplaced/malformed candidates before opening their contents. Add negative regressions for both reproduced cases and preserve the existing safety checks. The author should replace its own synthetic rollout-fixture basename with a valid canonical one.

## Other review observations

Trusted adapter dispatch registers exact full InputText after the source-known typed-role prefix. Selection matches only user input_text blocks, rejects duplicate/conflicting primary or child matches and has no fallback role. Child origin is registered only when an actual native spawn is issued, carries that call ID, and is checked against the actual spawn registry; optional inherited Agent1 is allowed while conflicting primary roles reject. Later notification text containing the marker does not become origin. Existing read output call IDs, native spawn/wait IDs and primary collab receiver IDs corroborate the child ID. This remains fixture composition evidence, not mechanical role enforcement.

The metadata reader verifies canonical owned directories, rejects symlinks, stops processing after64entries, selects one candidate, opens O_NOFOLLOW, checks device/inode/canonical path, reads one byte at a time through the first newline only with a256KiB/5s bound and revalidates metadata/path afterwards. It validates exact record type/child/parent/cwd and native source parent/depth1. Retained output excludes base instructions and all other record fields. The same exact private CODEX_HOME is created by the fixture, and reads happen after role workers retire before cleanup. These controls should remain; they do not substitute for the missing candidate path grammar. No transcript/account reader was introduced.

Origin/metadata claims keep productionRoleEnvelopeProven=false, controlled-worker/adapter calibration and instruction-asserted roles. The native SessionMeta supplies source lineage only; no supplier agent_role is promoted to a Runtime role.

## Checks and handoff

Six scoped pure tests passed; actual supplier and author-scratch metadata test skipped. The latter was excluded to preserve reviewer scratch ownership; the exact reader was exercised separately in reviewer-owned scratch. Targeted noEmit exit0. Author-reported7pure1skip is distinct from these independent checks. All seven supplied supplier source pins matched; added rollout_file_name.rs pin is in SOURCE_HASHES.json.

Accepted upstream: sealed parent P4/REPAIR_3 amendment and manager BASIS/PLAN, predecessor accepted specification/owner grants and frozen author return. This is derivative review evidence. Closure: review completed with P4-R3-1 OPEN; actual conformance remains OPEN. Next: author repairs exact candidate path grammar and tests, freezes new source, then fresh bounded backcheck before parent supplier diagnostic. No release/hold/lifecycle/acceptance or governed pointer update follows.

ToolsUsed: functions exec/exec_command (read-only source/Git paths, Python3, Node exact-reader synthetic repro, Vitest scoped pure, TypeScript noEmit), parent messages.
ToolPolicyCompliance: PASS. WriteAuthorization: REVIEW_P4/REPAIR_3 and reviewer-owned scratch only.
Outputs: REPORT.md, CHECKS.json, SOURCE_HASHES.json, REPRO.json, REPRO.mjs.source, OUTPUT_HASHES.json.
MISSING: P4-R3-1 repair/backcheck and actual parent diagnostic.
NEEDS_HUMAN_RULING: none; repair fits current exact-layout grant.
DEPENDENCY_NOTES: parent owns supplier execution; P4 owns source.
