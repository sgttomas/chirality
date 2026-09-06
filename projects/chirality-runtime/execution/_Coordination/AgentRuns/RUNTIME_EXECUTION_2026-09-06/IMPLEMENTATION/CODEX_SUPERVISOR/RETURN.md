# Codex supervisor bridge return — AMENDMENT4

Executor: OpenAI GPT-6, exact serving model ID unavailable; bounded Agent 2, instruction-asserted role, not mechanically enforced. No delegation, actual hosted account, provider network, vendor execution, installation or operational state used by this specialist.

## Applied composition

`CodexSupervisor` implements the existing private supervisor port, including `verifyHostedBoundary`. It accepts only trusted constructor settings: fixed accepted executable, explicit model, canonical identity, dedicated worker-private directory/CODEX_HOME, exact owner-private auth.json SHA256 and attributed provider network consent. No account material is logged or returned. It checks exact supply before launch and revalidates immediately before sandbox-exec; auth identity bytes are checked around account selection. A changed auth-file binding requires an explicit operator rebind. This binds file identity, not an invented semantic proof of provider account identity.

Actual execution uses the contained process's JSONL through CodexTurnSession: initialize, account/read with actual account required, fresh thread/start or broker-provided already-checked resumeThreadId, turn/start, and genuine terminal notification. WorkerResult carries the actual threadId. Failed/interrupted terminals retain failure status; protocol errors, retry notifications without supported completion, crashes and deadlines never become completed output. Handles are generation-bound, with bounded process-group retirement; close waits for pending acquisitions to clean up. No automatic replay or in-flight reattachment.

The private turn envelope contains prompt, optional resumeThreadId, requestedRole and roleEvidence. Typed roles require truthful `role not mechanically enforced` / `instruction-asserted` labels; the exact original prompt is preserved after explicit role context. Missing/untyped selection adds no role. The separately named controlled test launcher cannot satisfy verifyHostedBoundary and cannot establish provider-observed admission.

## Standalone integration and corrected isolation

Standalone config now has closed controlled-worker and hosted-validation variants. Hosted worker settings require `privateDirectory` relative to runtimeDirectory, explicit model, auth binding and provider consent; arbitrary argument vectors are not admitted in this variant. The exact executable and CODEX_HOME both lie inside the dedicated worker-private subtree. Project and runtime roots are disjoint, and the worker subtree is disjoint from config, sockets, supervisor credentials, auth/project/session registries, approvals and retirement journals. A parent review identified the earlier broad runtimeDirectory proposal as unsafe; it was corrected before final fan-in and no hosted process used that proposal.

The bin reports its actual mode and sets its own umask077. Broker model attribution is codex-app-server/openai/the exact configured model; controlled attribution remains not-applicable. ApprovalStore sits in broker-private runtimeDirectory/approvals and resolves liveness through the actual DelegatedRuntime. There is no public approval-request minting or unsupported provider approval forwarding.

Boundary preflight deliberately allows consent management for all stored postures, including on-to-off revocation. Actual worker acquisition independently requires an explicit recorded off posture. Trusted provider network consent is separately mandatory. Provider-enabled sandbox network remains configuration-only for command-network separation, exactly as the containment adapter reports; this is not mechanism-proven subprocess network isolation. Public hosted readiness, successful initialization or an accepted payload alone are not a provider-turn success claim.

## Verification

`npm run build`: PASS. `npx vitest run tests/codex-supervisor.test.ts tests/standalone.test.ts`: PASS, 24 tests (14 supervisor, 10 standalone). Actual tests include controlled JSONL subprocesses, real two-job RuntimeClient turns, resume-thread selection, genuine failure/interruption, retry/crash/deadline rejection, acquisition/close race, stale generation, labelled role and byte-preserved prompt, fixture-production separation, config/credential isolation and rotation. An actual macOS sandbox-exec test denied both read and write of a sibling broker auth secret and verified unchanged bytes. Unix socket/sandbox tests used approved escalation; no provider account or network was used.

The exact vendor binary and account were not exercised here; positive hosted smoke remains with the parent's separately authorized actor. The invalid vendor signature remains open, and current actor method coverage is a candidate adapter dialect with explicitly bounded unsupported events.

## Handoff

Historical pre-AMENDMENT4 standalone source/tests/bin bytes are preserved losslessly, with the reconstructed bin preimage verified against its earlier sealed SHA. Current source snapshots accompany OUTPUTS hashes so later login integration may supersede this code without rewriting this evidence. Parent owns exports, contract/wire/broker changes, login integration, independent review and full validation. This is derivative implementation evidence, not accepted lifecycle completion, production activation or hold release.
