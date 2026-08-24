# Proposed App Contract Amendments — SCA-APP-008

**Status:** `PROPOSED_NOT_APPLIED`
**Target if later owner-approved:** `projects/chirality-app-dev/docs/CONTRACT.md`
**Current target SHA-256:** `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`

This file is a Gate-1/Gate-3 drafting aid. It changes no contract. Exact wording remains subject to owner acceptance, invariant-ID review, Root/App concordance, authority-corpus reconciliation, and an approved Gate-5 propagation plan.

## Existing rows proposed for amendment

### K-CONTROL-1 — two purpose-limited sockets

**Current:** Runtime control is exposed only over one authenticated project-scoped HTTP/1.1 API on a Unix-domain socket beneath a `0700` parent with a `0600` socket; no TCP listener.

**Proposed exact row text:**

| ID | Invariant | Verification |
| --- | --- | --- |
| **K-CONTROL-1** | Runtime control uses exactly two purpose-limited Unix-domain sockets and no TCP control listener: (1) the existing authenticated project-scoped daemon HTTP/1.1 API, and (2) one private daemon-to-Delegated-Harness-Process-Supervisor socket that is never renderer- or CLI-callable. Both sockets reside beneath app-owned `0700` runtime directories, are mode `0600`, bind to verified same-UID path ownership and owner/generation records, use rotated high-entropy bearer tokens delivered only through app-private state, fail closed on stale or mismatched identity, and recover stale sockets explicitly. No peer-credential guarantee is claimed where the runtime cannot inspect peer credentials. | Socket permission/owner/generation/token tests; stale recovery; renderer/CLI denial; two-listener inventory; no-TCP inspection; G-HELPER/G-DUAL/AT-054/058. |

### K-ROLE-2 — authority role and enforcement profile

**Current:** Agent 0/1/2 roles describe authority and responsibility, not durable engine/model assignment; actual adapter/provider/model and substitution are recorded.

**Proposed exact row text:**

| ID | Invariant | Verification |
| --- | --- | --- |
| **K-ROLE-2** | Agent 0/1/2 roles describe authority and responsibility, not a durable engine or model assignment. A deliberately selected role-posture/configuration digest may participate in worker identity solely to enforce that role's accepted authority semantics. Agent 0/1/2 role entry is always offered for Codex sessions. If G-ROLE cannot mechanically prove non-delegation, Agent 2/TASK entry remains available only with the label `role not mechanically enforced`, and governed-workflow evidence is marked `instruction-asserted`. Native descendants acquire no Agent 0/1/2 role by descent. Every run records selected role state, actual adapter/provider/model, configuration/policy digest, and any substitution. | G-ROLE profile/readback tests; role/native-class fixtures; label/copy checks; AgentRun/session attribution; actual-model evidence; governance scan for model-to-role prescriptions. |

### K-NET-1 — enumerated service traffic and per-root command consent

**Current:** loopback plus Anthropic API, with a bounded authenticated loopback oMLX exception; broader network requires a governed tranche.

**Proposed exact row text:**

| ID | Invariant | Enforcement |
| --- | --- | --- |
| **K-NET-1** | Outbound network is deny-by-default and limited to enumerated product transports: the existing loopback/Anthropic path, the bounded D-APP-72 authenticated `127.0.0.1` oMLX exception, and exact accepted OpenAI account, model, and turn service endpoints for the delegated-harness adapter. There is no generic service-traffic exemption. Each canonical root selects under explicit consent one command-network posture: (1) no command network, the default; (2) ask per destination through managed-network prompts that show the available host/protocol context and warn that an upstream grant may unblock queued requests to the same destination, with `acceptForSession` permitted only as an explicit user act; or (3) command network on through `network_access = true`, visibly labelled. Redirects, embedded URL credentials, remote MCP/providers, undeclared endpoints, and network outside the selected posture fail closed. | Endpoint allowlist and redirect tests; root-consent/state fixtures; prompt delivery and empirical grouping evidence at the exact pin; `networkApprovalContext` projection tests; no-network default; account/root continuity; G-APPR/G-SBX/AT-020. |

### K-KEY-1 — expanded credential taxonomy and typed failure

**Current:** API keys are non-project convenience state and excluded from project files, events, logs, transcripts where avoidable, and tool artifacts.

**Proposed exact row text:**

| ID | Invariant | Enforcement |
| --- | --- | --- |
| **K-KEY-1** | Credentials and authentication ceremony data—including API keys, OAuth access/refresh tokens, device codes, browser callback parameters, cookies, Keychain items, App Server keyring state, and Electron `safeStorage` ciphertext/plaintext—are non-project private state. They must not appear in project files, durable event payloads, logs, support bundles, tool artifacts, or SDK transcripts where avoidable. Storage and UI contracts distinguish at least `missing`, `storageUnavailable`, `decryptFailed`, and `available`; a decrypt or signature-transition failure is typed, non-destructive, redacted, and requires explicit reauthentication rather than null-collapse or silent loss. Root-private login state is never copied or symlinked from ambient `~/.codex`. | safeStorage/keyring and A→B identity-transition tests; six-channel IPC sender authorization; secret-evidence scanner; redaction fixtures; root-account transition/logout tests; G-KEY/G-CSP/AT-044/051/057. |

### K-EVENT-3 — four terminal types

**Proposed exact row text:**

| ID | Invariant | Enforcement |
| --- | --- | --- |
| **K-EVENT-3** | Every accepted turn ends with exactly one durable terminal outcome in closed `HarnessEvent` schema v2: completed, failed, interrupted, or cancelled. Adapter-specific terminals are validated and mapped before the coordinator; retirement/recovery must not invent success or duplicate terminals. | Closed-union type validation; exact-pin codec; terminal mapping/recovery tests; replay and sink backchecks; G-WIRE/AT-032/055. |

### K-EVENT-4 — versioned Root record and legacy App migration

**Proposed exact row text:**

| ID | Invariant | Enforcement |
| --- | --- | --- |
| **K-EVENT-4** | The Root-owned shared-runtime session store and its accepted versioned JSON/JSONL path are the canonical runtime audit record. Project-local `.chirality/sessions/<id>/events.jsonl` is a legacy App compatibility source that may be read and lazily migrated non-destructively; it is not a second active writer or an authority replacement. Browser `UIEvent` streaming and selected replay remain projections of accepted runtime records. | Root/App storage-contract concordance; one-writer tests; lazy migration/rollback; replay path/version tests; no-dual-store inspection. |

The final accepted row must substitute the exact Root schema/path identity; `TBD` path invention is forbidden.

### K-EVENT-6 — closed schema and exhaustive sink redaction

**Proposed exact row text:**

| ID | Invariant | Enforcement |
| --- | --- | --- |
| **K-EVENT-6** | Only fields admitted by closed, versioned `HarnessEvent` schema v2 may cross from an adapter into the coordinator, persistence, browser SSE projection, status/replay views, logs, crash/helper/App Server/launchd diagnostics, or support bundles. Structural redaction runs before every sink. Unknown upstream event types become bounded diagnostic codes and never raw payloads. Secrets, tokens, device-login ceremony values, callback parameters, cookies, credentials, and private machine state are excluded; ephemeral ceremony display data is destroyed with its view. | Generated schema/type exhaustiveness; synthetic-secret corpus across JSONL, both SSE hops, logs and bundles; unknown-type fixtures; scanner extension coverage; G-WIRE/AT-024/025/057. |

## Proposed new rows

The IDs below are proposed candidates and must be checked against the live invariant catalog before application.

### K-CONSENT-1 — HostedEngineConsentPort

| ID | Invariant | Enforcement |
| --- | --- | --- |
| **K-CONSENT-1** | `HostedEngineConsentPort` is the sole App coordinator boundary for admitting a hosted-engine worker, thread, or turn. Before worker boot/acquisition, thread creation/resume, and every turn, it validates server-owned canonical root, project identity, adapter, exact non-secret account digest or volatile null-email epoch, notice/policy digest, selected role posture, effective configuration digest, and worker generation. Consent is per canonical root and cannot be reused across root, account, policy, or generation changes. Revocation retires the affected root generation and invalidates its private home. Caller-supplied `cwd` never overrides the stored canonical root. | Contract injection tests; account A/B/null-email fixtures; root/policy/generation mismatch denials; revocation/retirement journal; stored-root mutation rejection; G-SENT/G-DUAL/AT-003/007/044/056. |

### K-UNTYPED-1 — untyped and native-descendant classification

| ID | Invariant | Enforcement |
| --- | --- | --- |
| **K-UNTYPED-1** | An untyped primary Codex session may use delegated-harness-native descent only inside Chirality's hard filesystem, network, process, canonical-root, account-identity, and policy envelope. Native descent does not assign an Agent 0/1/2 role, does not enter managed delegation, and does not imply inherited authority or capability. Chirality-managed descendants remain subject to their separate hierarchy, sealed brief, approval, allowlist/generalist, tool, context, cwd, write-scope, and durable-evidence checks. Native origin/lineage and instruction/config-asserted non-delegation are recorded truthfully. | Origin/lineage fixtures; managed-vs-native route tests; containment and cancellation tests; AgentRun evidence calibration; no-role-by-descent checks; G-ROLE/G-APPR/G-SBX/G4. |

## Consequential enforcement-map amendments

If the owner later accepts these rows, the Gate-3 diff must also propose exact enforcement-map updates for:

- process supervisor/control sockets: K-CONTROL-1;
- consent/account/root continuity: K-CONSENT-1, K-NET-1, K-KEY-1;
- role/native classification: K-ROLE-2, K-UNTYPED-1, K-SUBAGENT-1/2/3;
- event codec/coordinator/persistence/SSE/replay/support sinks: K-EVENT-3/4/6;
- renderer credential IPC: K-KEY-1 and K-CONSENT-1;
- release validation: exact-candidate D-APP-97/F-APP-2 gate, RQG §13, and the A1 frontend re-stage rule.

## Concordance and supersession requirements before application

1. Compare exact Root contract rows after SCA-004 application; App text may specialize but must not weaken Root semantics.
2. Produce a prospective supersession binding for the D-APP-74 tranche-scoped multi-child/Agent-graph exclusion without editing its immutable ruling.
3. Reconcile D-APP-68/DEL-08-04 managed-delegation wording with D-GOV-35 and preserve the managed/native class distinction.
4. Reconcile K-EVENT-4 against the exact live Root session path before acceptance.
5. Update the invariant coverage register only in a later approved Gate-5 tranche.
6. Re-run authority corpus and RQG §13 mapping after any accepted contract write.

No text in this file is dispatch authority or a release, signing, notarization, distribution, lifecycle, or acceptance claim.
