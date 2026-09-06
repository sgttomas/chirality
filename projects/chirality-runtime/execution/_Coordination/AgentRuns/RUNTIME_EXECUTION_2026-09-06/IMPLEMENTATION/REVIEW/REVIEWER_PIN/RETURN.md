# Independent reviewer pin initial verdict

OpenAI GPT-6; exact serving ID unavailable. Actual Agent2 instruction-asserted/not mechanically enforced. Read-only product/supplier source and controlled fixture tests; no vendor/provider/account execution, product writes, build, owner acts or delegation.

## Changes required: R1 persisted operation reviewer overrides global pin

Compiler v5 explicitly pins approvals_reviewer=user and includes it in the identity. Actor requires exactly user, rejecting absent/null/automatic/legacy reviewer values, before native thread start/resume and turn start. That global config/read check alone is insufficient for a resumed thread.

Exact supplier source HEAD758ef40f50c1a458425c7cfbf1eb12cbc07af0b0 confirms app-server thread_processor.rs:3913–3921 restores persisted approval_policy and approvals_reviewer when typed/request overrides are absent. Lines3638–3651 apply those values then load_for_cwd. config_manager.rs:192–205 combines CLI config and typed overrides; core/config/mod.rs:3594–3596 chooses the typed approvals reviewer ahead of the configured value. Thread resume response at thread_processor.rs:3846–3856 exposes actual approval policy/reviewer. Current actor resume sends neither explicit field and only checks returned thread ID, permitting persisted auto_review despite config/read user.

A controlled actor reproduction passes while demonstrating this gap: config/read user/on-request; resume asserts omitted operation reviewer/policy and responds auto_review/never; actor then starts and completes a turn. No vendor source is executed. Source captures are gzip-pinned in SUPPLIER_SOURCE_PINS.json, and fixture is preserved .test.ts.source. This is a real approval-boundary mismatch; parent accepted R1 and dispatched explicit operation pins and response verification. Trusted posture-derived approvalPolicy should accompany approvalsReviewer=user on start/resume/turn; caller overrides remain forbidden.

## Validation and calibration

64 existing focused tests passed after continuity confirmed its stable window complete. One extra reproduction passed demonstrating R1. Compiler scope remains unchanged except explicit reviewer identity; strict missing/null/automatic rejection is useful but not closure until operation precedence is covered. Tests here do not show that prior null reviewer caused native ask failure, do not prove vendor network enforcement, and do not supply source/release acceptance. Preserve this verdict and supersede it only with an immutable repair backcheck.
