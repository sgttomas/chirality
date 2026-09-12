# R16 restart admission failure — bounded source diagnosis

Type 2 gpt-6-astra medium. Work only /Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335. Read applicable AGENTS and current RUN_LOG / R16_FUNCTIONAL_FINDINGS. No delegation.

Observed sequence: signed Stage25 R16 (source70a02f74) automatically started daemon, owner OAuth, multiple real text/shell/image/PlanMode turns and two role/model chats succeeded. Actual running tool interruption retired sleep and fresh shell read succeeded. Lead CmdQ at Idle closed GUI10625; daemon10666 stayed. Same guarded launcher --check-only PASS and relaunch created GUI13417, retaining daemon. Owner then tried actual follow-up in retained chat and got:
Harness Request Failed (ENGINE_UNAVAILABLE)
ENGINE_UNAVAILABLE: Runtime v2 admission is missing, invalid, stale or no longer live
Review the request context and retry.
Computer Use cannot attach after restart; this is owner-observed actual failure. Do not infer exact internal reason absent evidence. Known error source packages/daemon/src/runtime-conformance-v2-admission.ts:135.

Objective: trace production admission lifecycle through desktop quit/relaunch with retained daemon; reproduce with contained controlled tests if feasible, and propose smallest repair. Distinguish lease expiry/invalidation, host reconnect identity and stale admission closure. Preserve fail-closed authentication, code-signature/account bindings, supplier restrictions, and owner no-payload-rehash requirement. Reconnection may renew/reestablish warranted admission; never accept stale/invalid approval or suppress actual failure.

First phase write scope: R16_RESTART_ADMISSION diagnosis and scratch test/probe files inside this directory only. Read production Runtime/App source and preserved sanitized evidence. No product edit until lead sees proposed scope; this is coordination to avoid conflicting authors, not an owner gate. No build/sign, live GUI, network/provider probes, live trial account/identity/auth/token/binding/Codex-home/session/event files, keychain, registration or process changes. Never read blocked state through alternatives. Do not repeat broad suites. Return diagnosis strength, minimal change targets and meaningful regression plan promptly. Parent will handle missing live diagnostics with owner if genuinely needed.
