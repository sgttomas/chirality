# Fresh independent review of cf3b1338b

Reviewer: `/root/live_recovery_final_review`, gpt-6-astra/high, no authorship.
Verbatim return follows.

FAIL — one remaining actionable finding.

**[P1] Persist the submission identity before observing a plan execution.**

Location: `projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx:1379–1384`; deferred association at `1404–1408`, permissive recovery settlement at `1212–1217`.

Trigger: an Execute plan POST has an ambiguous response while an unrelated earlier turn remains active—for example, another observer started that turn and the new POST’s rejection response is lost. Reload before observation settles. The running plan record was persisted without `turnId`; the new UUID exists only in the abandoned observation. Recovery correctly attaches to the earlier active turn, but `settleRecoveredExecution` accepts an identity-less running attempt and assigns that earlier turn’s completion to it.

Impact: a plan that never executed can display Completed. The same missing durable association also prevents accurate replay settlement when the requested turn actually finishes while the renderer is absent.

Evidence: `beginPlanExecution` creates the running record without an identity; the storage effect persists it. `attachPlanExecutionTurn` runs only after `observeTurn` returns. Recovery rejects mismatches only when both identities exist. Existing reload-plan coverage seeds a record already containing `turnId`, bypassing this submission path.

Repair: associate and persist the preallocated UUID with the execution attempt before POST. Settle recovered attempts only against a proven matching identity; legacy identity-less records must remain unknown without independent correlation. Add a submission → reload regression with an unrelated active turn and verify no false plan completion, resend, or restored draft.

The missing early association predates this diff, but leaves the prior P1 unresolved in the newly supported ambiguous-submission/reload flow. No other actionable finding found.

Coverage and verification:

- Read all 42 files in `85f19f019589b798331c804c4b206e34849eeab5..cf3b1338b38c855bd2e92bf790076d6982f15678`, including source, tests, briefs, returns, and historical packaging records; no diff exclusions.
- Verified request forwarding, atomic retained-stream matching, scoped replay, starting-turn retry, cancellation, shutdown cause persistence/publication, explicit Stop, and constrained panel sizing.
- Scope validator passed: 42 paths, zero violations. HEAD matched the candidate.
- Read filtered results: Runtime 321 passed; frontend 2179 passed, four skipped; frontend and Electron typechecks passed.
- `git diff --check` reports only the intentional Markdown hard break in the verbatim prior review at `returns/REVIEW_LIVE_RECOVERY_1.md:9`.
- No tests, live actions, writes, signals, protected-state reads, or delegation performed.

Residual limits: the reported Pi/oMLX concurrent timeout and intermittent `STOPPED_DEGRADED` failure remain unresolved observations. Direct service-loss evidence covers graceful SIGTERM, not an unhandled crash. Parent’s final UUID/reload completion, replacement packaging, and owner install-over acceptance remain separate evidence.

Fresh read-only TASK, software-code-review, gpt-6-astra/high. This is not owner or release approval.
