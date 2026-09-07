# Credential custody decision slate v1

Status: PROPOSED — NOT RULED. Preserve the owner-confirmed target: one OpenAI sign-in experience with independent consent for each folder. Human-approval assurance remains a separate decision. This derivative slate does not amend authority, adopt a supplier or authorize execution.

## Evidence and limits

Parent freshness01:04:32Z: HEAD/main2c75eb4, all242custody paths preserved. Parent verified69incoming manifest members, manifest SHA256 e9e6766e4060cee21e7095e88c2388926e0121eb30d0cebc30bf426324a970fa, at `/private/tmp/chirality-runtime-contract-completion-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CREDENTIAL_BOUNDARY_2026-09-06`. Parent reviewed HANDOFF, official RECOMMENDATION, SUPERSESSION and backcheck, and checked D-GOV-20 items2–3. Supersession controls earlier recommendations.

Parent also read current official [App Server documentation](https://learn.chatgpt.com/docs/app-server) for managed authentication and its maturity caveat, and [authentication documentation](https://learn.chatgpt.com/docs/auth) distinguishing explicit keyring configuration from auto selection. This is documentary feasibility evidence, not proof of the exact selected binary or operational behavior.

## Three owner choices

| Choice | Recommended narrow boundary | Consequence / alternative |
|---|---|---|
| **1. Credential custodian and storage exception** | Permit the exact daemon-owned trusted supplier authentication process with explicitly configured built-in keyring as a narrow exception to Electron safeStorage. Each root independently acquires authentication. Prohibit cross-root credential copying, shared homes, ambient credentials, client/tool-worker access and plaintext fallback. Operational reliance remains conditional on exact qualification. | Route the exception through Root/Runtime/App owning instruments before reliance. Keep current exact authority and hosted behavior unavailable if not selected. Use a custom adapter only for a demonstrated remaining gap, not as a default parallel solution. |
| **2. Sign-in before choosing a folder** | Permit an account-only, nonexecuting bootstrap namespace for sign-in before a folder exists. It grants no project/no-folder execution or folder consent, and credentials are not copied into root contexts. | Without this accepted namespace, pre-folder sign-in remains unavailable under the current boundary. It is not a substitute for B2 isolated execution-context design or acceptance. |
| **3. Switch/sign-out and cleanup semantics** | Global account switch/sign-out fences every hosted context in the active generation. Local contexts remain unaffected; disconnecting a folder is local to that folder. Preserve corrected cleanup order: a bounded authorized remote-revoke attempt occurs before auth retirement/local clearing. If ungranted, offline or impossible, perform local cleanup and report remote state unknown. | No promise of browser-wide or provider-global revocation. Do not quietly shrink global hosted fencing to one root. Retain current exact authority/hosted-unavailable behavior until these semantics are adopted and qualified. |

## Next step if selected

Adopt the exact selected boundaries through their Root, Runtime and App owning instruments, then prepare the exact configuration/status-adaptation and bootstrap+A/B inquiry brief with scope, identities, proof conditions and return contract. Significant remaining choices return to owner. This slate does **not** authorize unspecified live qualification, source implementation, login, provider/credential operations, protected-fixture work, supplier acceptance, publication, merge or release. No human-assurance alternative is selected here.
