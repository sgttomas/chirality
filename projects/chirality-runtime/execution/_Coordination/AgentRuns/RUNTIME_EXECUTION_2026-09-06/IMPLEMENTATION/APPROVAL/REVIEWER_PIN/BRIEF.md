# Reviewer pin hardening brief

Parent released bounded actor/fixture implementation after current ask run completed. OpenAI GPT-6 specialist; exact serving ID unavailable; Agent 2 role instruction-asserted, not mechanically enforced. No authority changes, Git, supplier execution, or live provider calls.

Exact source at pinned Codex 758ef40f50c1a458425c7cfbf1eb12cbc07af0b0: core/src/config/config_tests.rs:11080 onward tests default User and explicit reviewer configuration. app-server-protocol/src/protocol/v2/config.rs:267 exposes approvals_reviewer as optional experimental config/read field; shared.rs:242 serializes User as user, AutoReview as auto_review (legacy alias guardian_subagent). Strict readback must reject missing/null; no inferred default. Actual supplier field visibility remains to be empirically checked by parent.

Manager owns compiler serialization of approvals_reviewer=user and policy identity version 5 with approvalsReviewer=user. Specialist owns actor checkNativePolicy strict user check, actor fixture missing/null/auto_review/shadow/drift tests across all three postures, supervisor controlled config fixture, and compiler assertion in containment test. No actor constructor/API change. Existing checks occur before thread start/resume and turn start. Pin every posture so future work cannot inherit automatic review.

Accept: coherent typecheck and focused controlled actor/supervisor/compiler tests; reject changed reviewer before operations and forbid caller reviewer override. This hardening is not established as the cause of the current ask failure and proves neither native network enforcement nor live supplier approval delivery.
