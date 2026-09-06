# Approval actor corrective brief

Parent-released bounded repair. OpenAI GPT-6; exact serving model ID unavailable; Agent 2 instruction-asserted, not mechanically enforced. Own codex-session.ts and its tests only. No supplier/account/provider use.

Exact official 0.149 source permissions.rs:120–131 sets profile-derived proxy config enabled=false; features NetworkProxy defaults false; config/mod.rs:3555 requires the feature and profile enabled. Parent fixes compiler. Actor must require explicit features.network_proxy true in ask/on, false in off, on each native policy check; missing/null/wrong values are errors. Controlled native fixtures state feature explicitly.

Reviewer also reproduced async writable failure yielding premature sent:true. Actor reply must await a bounded successful write callback. Enter sending state before await, reject replay/conflict, fail closed on callback error/timeout. This receipt still means transport write only, never vendor execution acknowledgement. Core/supervisor already await the promise. Add positive and failing-writable regressions.
