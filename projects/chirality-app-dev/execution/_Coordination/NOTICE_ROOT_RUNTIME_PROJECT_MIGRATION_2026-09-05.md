# Root runtime project migration — integration notice

Owner direction: Ryan Tufts, 2026-09-05, “Merge PR #726 then proceed with the migration.” PR #726 merged at 5068899690ab2580fa3360f751f63952e6bdc563.

The migration candidate relocates all 79 tracked runtime workspace files byte-identically from runtime/ to projects/chirality-runtime/. Package identities, public APIs, operational socket/data locations and existing accepted evidence are preserved. Root CI now builds/tests the destination; PEC CI also triggers on runtime-project changes. Eight frozen frontend paths and independent code-review evidence are in this project’s migration AgentRuns return. Local registered premerge requires CI daemon/socket/token bindings; it is not recorded as passing.

This notice routes coordination, not authority. Technical candidate and formal source/destination authority transfer have distinct closure states. Root’s accepted PRD/decomposition remain unchanged pending exact owning acceptance gates. No lifecycle promotion, conformance acceptance, historical pin rebinding, live account/state migration or new PR merge is implied. The destination has no autonomous feature-work grant from this notice.

Evidence and remaining transfer candidates: execution/_Coordination/AgentRuns/ROOT_RUNTIME_MIGRATION_2026-09-05/. Receiving loop may cite this notice and its scoped child return when the migration lands; follow-on acceptance remains with that loop’s instruments. If source paths change, rerun dependent checks. Rollback restores the tracked source move, consumer paths and CI together; there is no database conversion.

Prepared by /root HELP_HUMAN, OpenAI GPT-6, exact serving model ID unavailable; Agent 0 role not mechanically enforced.
