# Continuity implementation return

Executor: OpenAI GPT-6; exact serving model ID unavailable. Bounded Agent 2, role not mechanically enforced, instruction-asserted. No delegation, accounts or operational state used.

## Result

Implemented `HostedConsentStore({ canonicalRoot, codexHome })` and `WorkerRetirementCoordinator({ directory })` against the frozen delegated.ts ports. `codexHome` is a readonly property. `configuration(identity)` supplies explicit `env.CODEX_HOME`, posture, `network_access` and label. `destinationPrompt` carries host/protocol and the same-destination queued-request caveat.

Consent is default-off; root-private owner-only storage excludes ambient ~/.codex and symlink aliases, and an immutable binding prevents sharing a home between roots. A daemon-owned home may be outside the project directory. Exact root/account/epoch/policy/canonical-cwd continuity controls consent reuse. Destination approval requires an explicit user act, including acceptForSession. Persisted destination evidence is not an enforcement/firewall implementation, a vendor prompt-delivery proof or a reusable authorization token. A raw-spawn caller cannot treat posture labels as proof of process/network containment.

Prepared records and terminal commits are immutable. Bytes are synced before cross-process exclusive hard-link publication, then the directory is synced. The terminal publication itself defines committed state, avoiding a second mutable commit flag and its crash window. Reconciliation markers never override a terminal. Conflicting identity/thread reuse and differing terminal identities/outcomes fail; an identical terminal retry returns the original timestamp. Restart is blocked until an existing active turn has a terminal record; only complete recorded identity continuity and a recorded thread allow thread/resume. Otherwise a valid new identity starts fresh. No automatic replay or in-flight reattachment.

## Verification

`npx vitest run tests/hosted-consent.test.ts tests/worker-retirement.test.ts`: PASS, 24 tests (11 consent, 13 retirement), 2026-09-06 20:50 local runner time. Includes actual child-process SIGKILL after durable prepare, four independent competing terminal publishers, retry timestamp preservation, conflicting preparation, all identity drifts, reconciliation/terminal race, unpublished crash-temporary exclusion, symlink and permission refusal, explicit consent and labels.

The initial `npm run build` reached an unrelated integration error in delegated-runtime.ts:69, missing protected `RUNTIME_COMPATIBILITY_MISMATCH` enum value. Parent owns that authorized contract integration. No continuity source type error was reported. Parent must run full build/typecheck and full suite after its integration. Focused subprocess tests require normal build output, as existing package tests do.

## Limits / handoff

Exactly-once is a durable terminal-record guarantee, never an arbitrary external side-effect guarantee. Filesystem isolation assumes daemon-owned owner-private storage; this does not sandbox a malicious process with the same OS identity and unrestricted filesystem authority. Arbitrary vendor launch, account use, exact-pin managed-network behavior, operational activation and hold disposition remain outside this bounded implementation. Evidence is derivative implementation/test evidence; no acceptance, lifecycle, release or decomposition claim.

Parent owns exports and API integration. No remaining known local defect; independent parent review and integrated checks remain required.
