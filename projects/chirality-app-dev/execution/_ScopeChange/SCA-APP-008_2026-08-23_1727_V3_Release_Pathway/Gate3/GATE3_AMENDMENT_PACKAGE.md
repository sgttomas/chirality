# SCA-APP-008 Gate 3 — Exact Amendment Package

**State:** `AWAITING_OWNER_APPROVAL`
**ReadyForNextPhase:** `NO`
**Authority effect:** `CANDIDATE_ONLY — NOT_APPLIED`
**Basis commit:** `f485b5d3b663f42be8f8cab8432ced9024d7381b`
**Stable-ID posture:** additions to carrier duties only; no package, deliverable, scope-item, objective, or parent/topology change.

## Owner decision requested

Approve, revise, or reject these exact Gate-3 bytes. Approval would accept an exact amendment candidate for later Gate-4/Gate-5 planning; it would not itself edit the decomposition or contract, move `_LATEST.md`, activate a carrier, dispatch implementation, route the Root notice, alter lifecycle, or authorize a release act.

The contract transactions below are all `CONCORDANCE_GATED_CANDIDATE`. They are exact candidates, not accepted App or Root truth. They remain ineligible for application until Root/App concordance resolves the named questions and the owner separately approves application.

## Basis and frozen-input verification

| Surface | Basis SHA-256 | Live region used |
| --- | --- | --- |
| `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | lines 297, 357–358, 368, 584–623 |
| `projects/chirality-app-dev/docs/CONTRACT.md` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | lines 71–74, 116–125, 145–168, 186–204 |
| `Brief.md` | `4bf54dc38e91da03a7b21c36b0ba4b89a4d358dfa7ac974f06652328902071d5` | line 55 D-APP-103 semantics |
| `Impact_Assessment.md` | `068c7b29734ea7ca4a0af9bc63d6355beb23f2083b668725d93c951bf53f4cf0` | accepted Gate-2 impact basis |
| `Carrier_Map.md` | `72a1b55b5307b6df5131011e30581e323737e95f3bcf85471121481ded25b619` | exact four-carrier duties and holds |
| `Contract_Amendments.proposed.md` | `8a6a799912eb9f610c8e1f6635d7eaf3f90e08614823ab3f715c3006bc0d1485` | exact proposed invariant wording |
| `DAG.md` | `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996` | accepted SCC orderings |
| `WORK_GRAPH.json` | `273c14cc9abe8b2f61696757507b1879479f2ac5d0b94138b6a8fcc07d5e6428` | 21 nodes, 32 edges, three SCCs |
| `Handoff_State.md` | `7fa51832df1223ad131d3a1330b66f078ebf9a2aa88f47b7a5f858a21293de52` | frozen Gate-1/2 handoff |
| `DRAFT_NOTICE_TO_ROOT.md` | `8ebc728b6d6c408a3dfeb60ae07887dbe7d5b88ba8fe06c1b954e98e8a380f72` | remains unrouted |
| `Audit/AUDIT_DEP_CLOSURE_RETURN.md` | `7ddc86e042547c90c7c9b9bd71fe5c2e842cbb885401d6aac2a749f8edc08d6e` | assessment-only PASS |
| `Audit/closure_summary.json` | `30dd016f9e358b0989cd14cc46ea5d0ebe33f8ba1ae14272378bbf98b611bce9` | assessment-only PASS summary |
| `Audit/Dependency_Closure_IssueLog.csv` | `deca04cd9717b8685c81cd4027638523d9193c02b10e5ffcfce189ca9dc27dcb` | header-only issue log |

All cited identities were verified at the basis before authoring. Existing assessment bytes remain frozen.

## Application grammar

Each transaction below is byte-precise:

1. require the target file's basis SHA-256 to match;
2. require the `PRE-IMAGE` bytes to occur exactly once and at the cited live line/anchor;
3. replace those bytes with the `POST-IMAGE` bytes exactly, including the terminating LF;
4. fail closed if the pre-image is missing, duplicated, or drifted;
5. apply no transaction until its separately stated gate is satisfied.

No later paraphrase or re-expression is permitted. The Gate-5 operator must use these post-image bytes directly.

In-memory application of the transactions below yields these exact candidate identities:

| Target | Pre-image SHA-256 | Candidate post-image SHA-256 |
| --- | --- | --- |
| `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` |
| `projects/chirality-app-dev/docs/CONTRACT.md` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `41cb6a62c6991c37559d1fcffeb75d9c76be2432ea84b1d1c5f864d8a3d9c9a6` |

The contract post-image identity is the exact question-bearing `CONCORDANCE_GATED_CANDIDATE`; it is not an eligible authoritative post-image while K-EVENT-4 and invariant-ID concordance remain unresolved.

## Transaction D-01 — DEL-02-05 carrier row

**Target:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Target basis SHA-256:** `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`
**Live citation:** line 297
**Action:** stable-ID `MODIFY`; no SOW relation, objective, context-envelope, parent, or topology change.

### PRE-IMAGE

```text
| DEL-02-05 | API Key UI and Runtime Feedback | TBD | UX_UI_SLICE | Provide API key entry/status UI, secure-storage feedback, selected-working-root attachment selection with multi-select preview and remove/clear controls, typed runtime errors, and retry-preserving draft and attachment failure states. | API key settings panel; attachment picker and preview chips; remove/clear controls; typed error display; secure-storage error UI; retry-state preservation tests | SOW-013, SOW-019, SOW-023 | OBJ-001, OBJ-008 | S | Cohesive dialogue-input and runtime-feedback UI slice; DEL-09-06 retains server-side attachment, network, key, and renderer security validation. |
```

### POST-IMAGE

```text
| DEL-02-05 | API Key UI and Runtime Feedback | TBD | UX_UI_SLICE | Provide API key entry/status UI, secure-storage feedback, selected-working-root attachment controls, typed runtime errors, and retry-preserving failure states; serve as the explicit App account/consent UX carrier by consuming `HostedEngineConsentPort`, explaining per-root login and root-private app-owned `CODEX_HOME`, presenting login/logout/account and consent/revocation state, distinguishing `missing`, `storageUnavailable`, `decryptFailed`, and `available`, and offering the three per-root command-network postures: no command network by default, ask per destination with host/protocol context and the queued-request caveat plus explicit-user-only `acceptForSession`, or labelled command network on through `network_access = true`. Agent 0/1/2 role entry remains available for Codex sessions; Agent 2/TASK is labelled `role not mechanically enforced` when G-ROLE fails, and the product posture is labelled `Opt-in Preview`. | API key and account settings panel; `HostedEngineConsentPort` UI adapter; per-root login and command-network consent controls; attachment picker and preview chips; typed storage/runtime error display; consent/revocation and retry-state tests | SOW-013, SOW-019, SOW-023 | OBJ-001, OBJ-008 | S | Explicit App account/consent UX carrier; Root retains account/consent semantics. No ambient `~/.codex` read or project-truth secret persistence. DEL-09-06 retains server-side attachment, network, key, credential-IPC, and renderer security validation. Live claims remain gated by the accepted Root/App account/consent contract, G3, G-CSP, and G4. |
```

## Transaction D-02 — DEL-08-04 carrier row

**Target:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Target basis SHA-256:** `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`
**Live citation:** line 357
**Action:** stable-ID `MODIFY`; DEL-08-04 remains the managed-delegation bridge; no topology change.

### PRE-IMAGE

```text
| DEL-08-04 | Type 2 Subagent Governance Bridge | TBD | BACKEND_FEATURE_SLICE | Bridge checkout-contained agent instructions, sealed context, project permissions, and approval references to daemon-owned operational delegation with restricted child tools/cwd. | App project-authority bridge; daemon-client dispatch; sealed-brief and restricted-child conformance tests | SOW-063 | OBJ-005, OBJ-007 | M | Project authority/client-dispatch slice; the daemon owns operational delegation execution. |
```

### POST-IMAGE

```text
| DEL-08-04 | Type 2 Subagent Governance Bridge | TBD | BACKEND_FEATURE_SLICE | Remain the Chirality-managed delegation bridge and prospectively carry multi-child managed execution plus the root `AGENTS.md` Agent 0/1/2 graph for v3 work, while consuming delegated-harness-native descent as a distinct Root-originated class. Enforce managed hierarchy, named allowlist or declared generalist policy, sealed brief, approvals, context/cwd/tool/write boundaries, active-sibling write-overlap fail-close, cancellation/cleanup, and class-aware routing; native descent assigns no Agent 0/1/2 role. Agent 0/1/2 role entry is offered for Codex sessions, with Agent 2/TASK labelled `role not mechanically enforced` and governed evidence marked `instruction-asserted` when G-ROLE cannot mechanically prove non-delegation. | App project-authority and managed-delegation bridge; daemon-client dispatch; class-aware `subagent-governance` behavior; managed sibling-overlap checks; role/native-origin fixtures; sealed-brief, containment, approval, cancellation, and cleanup conformance tests | SOW-063 | OBJ-005, OBJ-007 | M | Project authority/client-dispatch slice; daemon owns operational managed delegation and Root owns delegated-harness-native semantics. The D-APP-74 exclusion remains historical and tranche-scoped to SCA-APP-004; this v3 carrier prospectively supersedes it without retroactive edit. D-GOV-35 is necessary but App carrier acceptance and WP-03/05 fixtures remain required. |
```

## Transaction D-03 — DEL-08-05 carrier row

**Target:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Target basis SHA-256:** `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`
**Live citation:** line 358
**Action:** stable-ID `MODIFY`; evidence carrier only; no topology change.

### PRE-IMAGE

```text
| DEL-08-05 | Subagent Child Run Records and Artifacts | TBD | DATA_MODEL_CHANGE | Preserve checkout-contained parent-child AgentRuns, status, evidence, and accepted artifact paths linked to daemon operational delegation records. | Checkout AgentRun records; daemon linkage metadata; child output evidence paths; replay fixtures | SOW-063 | OBJ-003, OBJ-007 | M | Project evidence slice; daemon operational state is non-authoritative. |
```

### POST-IMAGE

```text
| DEL-08-05 | Subagent Child Run Records and Artifacts | TBD | DATA_MODEL_CHANGE | Preserve reconstructible checkout-contained records for Chirality-managed and delegated-harness-native descendants without conflating the classes: parentage, native origin/lineage, selected role-entry state, actual adapter/provider/model, instruction/brief and policy/configuration digests, approvals, status, return/output and accepted artifact paths, cancellation/cleanup, and truthful `instruction-asserted` calibration where G-ROLE cannot mechanically prove Agent 2/TASK non-delegation. | Checkout AgentRun and native-descendant evidence records; parentage/origin and daemon linkage metadata; role/config/model attribution; child output evidence paths; managed/native replay and reconstruction fixtures | SOW-063 | OBJ-003, OBJ-007 | M | Project evidence slice; daemon operational state is non-authoritative, native descent assigns no Agent 0/1/2 role, and managed sealed-brief evidence remains distinct and required. Evidence schema follows accepted class semantics. |
```

## Transaction D-04 — DEL-09-05 carrier row

**Target:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Target basis SHA-256:** `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`
**Live citation:** line 368
**Action:** stable-ID `MODIFY`; explicit release-operations carrier assignment; no topology change.

### PRE-IMAGE

```text
| DEL-09-05 | CI Artifact and Release Verification Workflow | TBD | CI_CD_CHANGE | Maintain CI premerge workflow, stable artifact upload, local command sequence, and manual release verification checklist. | CI workflow; stable artifact upload; release verification runbook | SOW-035, SOW-036, SOW-072 | OBJ-008 | M | CI/release workflow slice. |
```

### POST-IMAGE

```text
| DEL-09-05 | CI Artifact and Release Verification Workflow | TBD | CI_CD_CHANGE | Maintain CI premerge and stable artifact verification and serve as the explicit release-operations carrier with a strict phase boundary: WP-09 may author and review the exact signing, nested-signing-order, fuses/entitlements, notarization/stapling/Gatekeeper, recovery/rollback, version-identity, custody, GitHub-prerelease, and download-backcheck runbook, but WP-11 may execute release acts only after Ryan Tufts names and rules the exact candidate at G6a. | CI workflow and stable artifact evidence; WP-09 reviewed preparation/release runbook candidate; exact-candidate identity and custody checklist; separately authorized WP-11 owner/CHANGE execution record | SOW-035, SOW-036, SOW-072 | OBJ-008 | M | WP-09 authoring/review is not a signing, notarization, publication, distribution, release-readiness, or lifecycle act. D-APP-97/F-APP-2 remain active through preparation. WP-11 execution is a later owner act requiring G6a and the exact owner artifact ruling; no automatic transition from preparation is permitted. macOS arm64 is the rc.1 target and a second target requires a post-rc.1 scope change. |
```

## Transaction D-05 — decomposition decision/change record

**Target:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Target basis SHA-256:** `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`
**Live citations:** decision table anchor line 609 and change-log anchor line 623
**Action:** insert the following exact rows immediately after their respective exact anchors; IDs and topology remain stable.

### DECISION PRE-IMAGE ANCHOR

```text
| DEC-022 | 2026-07-27 | SCA-APP-006 makes the 81-ID/48-family CONTRACT invariant coverage register live, establishes field-level authority precedence and Scope Ledger / Deliverables reverse-view parity, and reconciles seven supported mappings without changing topology or activating OUT scope. | The owner selected OD6-G1-P1 / OD6-G2-I1 / OD6-G2-M1-A; deterministic invariant census and assignment comparison require explicit machine-truth coverage while preserving CONTRACT, accepted App topology, and external-owner authority. |
```

### DECISION POST-IMAGE INSERTION

```text
| DEC-023 | 2026-08-23 | SCA-APP-008 prospectively seats the v3 account/consent, managed/native delegation, descendant-evidence, and release-operations duties on stable DEL-02-05, DEL-08-04, DEL-08-05, and DEL-09-05 carriers without changing the 10-package/51-deliverable topology. | Ryan Tufts accepted the Gate-1/2 assessment and all three SCC moves in A2; exact contract text remains Root/App-concordance-gated, implementation remains separately authorized, and WP-09 runbook authoring remains strictly separate from WP-11 owner release acts. |
```

### CHANGE-LOG PRE-IMAGE ANCHOR

```text
- 2026-07-27: SCA-APP-006 created the authoritative 81-ID/48-family CONTRACT invariant companion register, established field-level authority and Scope Ledger reverse-view precedence, reconciled seven supported Section 8/9 relations, refreshed REF-006, and added DEC-022 without changing topology, context envelopes, lifecycle state, dependencies, estimates, schedule, or implementation authority.
```

### CHANGE-LOG POST-IMAGE INSERTION

```text
- 2026-08-23: SCA-APP-008 prospectively assigned v3 account/consent UX, class-aware managed/native delegation, descendant evidence, and owner-gated release-operations duties to existing stable carriers without changing topology, scope-item mappings, context envelopes, lifecycle, dependencies, estimates, schedule, implementation authority, or release authority.
```

## Contract transaction set — `CONCORDANCE_GATED_CANDIDATE`

All transactions C-01 through C-10 target `projects/chirality-app-dev/docs/CONTRACT.md` at basis SHA-256 `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`. They are an atomic candidate set for owner review but remain individually blocked from application until Root/App concordance confirms semantic compatibility and invariant-ID availability.

| Transaction | Candidate surface | Explicit state |
| --- | --- | --- |
| C-01 | K-CONTROL-1 | `CONCORDANCE_GATED_CANDIDATE` |
| C-02 | K-ROLE-2 | `CONCORDANCE_GATED_CANDIDATE` |
| C-03 | K-NET-1 | `CONCORDANCE_GATED_CANDIDATE` |
| C-04 | K-KEY-1 | `CONCORDANCE_GATED_CANDIDATE` |
| C-05 | K-EVENT-3 | `CONCORDANCE_GATED_CANDIDATE` |
| C-06 | K-EVENT-4 | `CONCORDANCE_GATED_CANDIDATE` |
| C-07 | K-EVENT-6 | `CONCORDANCE_GATED_CANDIDATE` |
| C-08 | K-CONSENT-1 | `CONCORDANCE_GATED_CANDIDATE` |
| C-09 | K-UNTYPED-1 | `CONCORDANCE_GATED_CANDIDATE` |
| C-10 | Consequential enforcement-map rows | `CONCORDANCE_GATED_CANDIDATE` |
| C-11 | SCA-APP-008 accepted-scope-change row | `CONCORDANCE_GATED_CANDIDATE_AND_GATE5_GATED` |

## Transaction C-01 — K-CONTROL-1

**Live citation:** line 200

### PRE-IMAGE

```text
| **K-CONTROL-1** | Runtime control is exposed only over an authenticated project-scoped HTTP/1.1 API on a Unix-domain socket beneath a `0700` parent with a `0600` socket. No TCP control listener is permitted. | Permission/authorization tests; stale-socket recovery; listener inspection. |
```

### POST-IMAGE

```text
| **K-CONTROL-1** | Runtime control uses exactly two purpose-limited Unix-domain sockets and no TCP control listener: (1) the existing authenticated project-scoped daemon HTTP/1.1 API, and (2) one private daemon-to-Delegated-Harness-Process-Supervisor socket that is never renderer- or CLI-callable. Both sockets reside beneath app-owned `0700` runtime directories, are mode `0600`, bind to verified same-UID path ownership and owner/generation records, use rotated high-entropy bearer tokens delivered only through app-private state, fail closed on stale or mismatched identity, and recover stale sockets explicitly. No peer-credential guarantee is claimed where the runtime cannot inspect peer credentials. | Socket permission/owner/generation/token tests; stale recovery; renderer/CLI denial; two-listener inventory; no-TCP inspection; G-HELPER/G-DUAL/AT-054/058. |
```

## Transaction C-02 — K-ROLE-2

**Live citation:** line 204

### PRE-IMAGE

```text
| **K-ROLE-2** | Agent 0/1/2 roles describe authority and responsibility, not a durable engine or model assignment. Every run records the actual adapter/provider/model and any substitution. | AgentRun/session attribution tests; governance scan for model-to-role prescriptions. |
```

### POST-IMAGE

```text
| **K-ROLE-2** | Agent 0/1/2 roles describe authority and responsibility, not a durable engine or model assignment. A deliberately selected role-posture/configuration digest may participate in worker identity solely to enforce that role's accepted authority semantics. Agent 0/1/2 role entry is always offered for Codex sessions. If G-ROLE cannot mechanically prove non-delegation, Agent 2/TASK entry remains available only with the label `role not mechanically enforced`, and governed-workflow evidence is marked `instruction-asserted`. Native descendants acquire no Agent 0/1/2 role by descent. Every run records selected role state, actual adapter/provider/model, configuration/policy digest, and any substitution. | G-ROLE profile/readback tests; role/native-class fixtures; label/copy checks; AgentRun/session attribution; actual-model evidence; governance scan for model-to-role prescriptions. |
```

## Transaction C-03 — K-NET-1

**Live citation:** line 124

### PRE-IMAGE

```text
| **K-NET-1** | Outbound network access is limited to explicit product scope. The default path remains loopback plus Anthropic API. D-APP-72 / SCA-APP-002 additionally permits authenticated oMLX only at `127.0.0.1` loopback for the bounded Pi child path; non-loopback oMLX, redirects, embedded URL credentials, remote providers, remote MCP, and broader network access remain prohibited without a new governed tranche. | Electron network guardrails; provider policy; loopback validation; redirect/authentication tests. |
```

### POST-IMAGE

```text
| **K-NET-1** | Outbound network is deny-by-default and limited to enumerated product transports: the existing loopback/Anthropic path, the bounded D-APP-72 authenticated `127.0.0.1` oMLX exception, and exact accepted OpenAI account, model, and turn service endpoints for the delegated-harness adapter. There is no generic service-traffic exemption. Each canonical root selects under explicit consent one command-network posture: (1) no command network, the default; (2) ask per destination through managed-network prompts that show the available host/protocol context and warn that an upstream grant may unblock queued requests to the same destination, with `acceptForSession` permitted only as an explicit user act; or (3) command network on through `network_access = true`, visibly labelled. Redirects, embedded URL credentials, remote MCP/providers, undeclared endpoints, and network outside the selected posture fail closed. | Endpoint allowlist and redirect tests; root-consent/state fixtures; prompt delivery and empirical grouping evidence at the exact pin; `networkApprovalContext` projection tests; no-network default; account/root continuity; G-APPR/G-SBX/AT-020. |
```

## Transaction C-04 — K-KEY-1

**Live citation:** line 125

### PRE-IMAGE

```text
| **K-KEY-1** | API keys are non-project convenience state and must never be written to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. | SafeStorage; env handling; redaction tests. |
```

### POST-IMAGE

```text
| **K-KEY-1** | Credentials and authentication ceremony data—including API keys, OAuth access/refresh tokens, device codes, browser callback parameters, cookies, Keychain items, App Server keyring state, and Electron `safeStorage` ciphertext/plaintext—are non-project private state. They must not appear in project files, durable event payloads, logs, support bundles, tool artifacts, or SDK transcripts where avoidable. Storage and UI contracts distinguish at least `missing`, `storageUnavailable`, `decryptFailed`, and `available`; a decrypt or signature-transition failure is typed, non-destructive, redacted, and requires explicit reauthentication rather than null-collapse or silent loss. Root-private login state is never copied or symlinked from ambient `~/.codex`. | safeStorage/keyring and A→B identity-transition tests; six-channel IPC sender authorization; secret-evidence scanner; redaction fixtures; root-account transition/logout tests; G-KEY/G-CSP/AT-044/051/057. |
```

## Transaction C-05 — K-EVENT-3

**Live citation:** line 71

### PRE-IMAGE

```text
| **K-EVENT-3** | Every accepted turn must end with a durable success, failure, cancellation, or interruption event. | `TurnEngine`; `Stop`/terminal mapping; replay tests. |
```

### POST-IMAGE

```text
| **K-EVENT-3** | Every accepted turn ends with exactly one durable terminal outcome in closed `HarnessEvent` schema v2: completed, failed, interrupted, or cancelled. Adapter-specific terminals are validated and mapped before the coordinator; retirement/recovery must not invent success or duplicate terminals. | Closed-union type validation; exact-pin codec; terminal mapping/recovery tests; replay and sink backchecks; G-WIRE/AT-032/055. |
```

## Transaction C-06 — K-EVENT-4 open concordance question

**Live citation:** line 72
**Required unresolved question:** **What is the exact live Root session path, including its accepted schema/version identity, that the App contract must name?**

This package does not answer that question. The exact candidate below records the question as a blocking value and must not be applied until HELP_HUMAN presents the Root/App concordance answer for owner approval.

### PRE-IMAGE

```text
| **K-EVENT-4** | `.chirality/sessions/<id>/events.jsonl` is the product-owned Chirality runtime audit mirror. | Session store; replay; R0/R1 storage decision. |
```

### POST-IMAGE

```text
| **K-EVENT-4** | The Root-owned shared-runtime session store at the exact accepted versioned JSON/JSONL path is the canonical runtime audit record. **Open concordance question: What is the exact live Root session path, including its accepted schema/version identity?** Until that question is owner-resolved, this row is `CONCORDANCE_GATED_CANDIDATE` and cannot be applied. Project-local `.chirality/sessions/<id>/events.jsonl` is a legacy App compatibility source that may be read and lazily migrated non-destructively; it is not a second active writer or an authority replacement. Browser `UIEvent` streaming and selected replay remain projections of accepted runtime records. | Root/App storage-contract concordance; one-writer tests; lazy migration/rollback; replay path/version tests; no-dual-store inspection. |
```

## Transaction C-07 — K-EVENT-6

**Live citation:** line 74

### PRE-IMAGE

```text
| **K-EVENT-6** | Runtime events, run logs, tool artifacts, and provider errors must redact secrets and avoid storing API keys. | `RunLogger`; redaction helper; tests. |
```

### POST-IMAGE

```text
| **K-EVENT-6** | Only fields admitted by closed, versioned `HarnessEvent` schema v2 may cross from an adapter into the coordinator, persistence, browser SSE projection, status/replay views, logs, crash/helper/App Server/launchd diagnostics, or support bundles. Structural redaction runs before every sink. Unknown upstream event types become bounded diagnostic codes and never raw payloads. Secrets, tokens, device-login ceremony values, callback parameters, cookies, credentials, and private machine state are excluded; ephemeral ceremony display data is destroyed with its view. | Generated schema/type exhaustiveness; synthetic-secret corpus across JSONL, both SSE hops, logs and bundles; unknown-type fixtures; scanner extension coverage; G-WIRE/AT-024/025/057. |
```

## Transaction C-08 — new K-CONSENT-1

**Live insertion anchor:** line 125, immediately after K-KEY-1
**Invariant-ID condition:** Root/App concordance must confirm that `K-CONSENT-1` is collision-free before application.

### BASIS PRE-IMAGE ANCHOR

```text
| **K-KEY-1** | API keys are non-project convenience state and must never be written to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. | SafeStorage; env handling; redaction tests. |
```

### APPLICATION ANCHOR AFTER C-04

```text
| **K-KEY-1** | Credentials and authentication ceremony data—including API keys, OAuth access/refresh tokens, device codes, browser callback parameters, cookies, Keychain items, App Server keyring state, and Electron `safeStorage` ciphertext/plaintext—are non-project private state. They must not appear in project files, durable event payloads, logs, support bundles, tool artifacts, or SDK transcripts where avoidable. Storage and UI contracts distinguish at least `missing`, `storageUnavailable`, `decryptFailed`, and `available`; a decrypt or signature-transition failure is typed, non-destructive, redacted, and requires explicit reauthentication rather than null-collapse or silent loss. Root-private login state is never copied or symlinked from ambient `~/.codex`. | safeStorage/keyring and A→B identity-transition tests; six-channel IPC sender authorization; secret-evidence scanner; redaction fixtures; root-account transition/logout tests; G-KEY/G-CSP/AT-044/051/057. |
```

### POST-IMAGE INSERTION

```text
| **K-CONSENT-1** | `HostedEngineConsentPort` is the sole App coordinator boundary for admitting a hosted-engine worker, thread, or turn. Before worker boot/acquisition, thread creation/resume, and every turn, it validates server-owned canonical root, project identity, adapter, exact non-secret account digest or volatile null-email epoch, notice/policy digest, selected role posture, effective configuration digest, and worker generation. Consent is per canonical root and cannot be reused across root, account, policy, or generation changes. Revocation retires the affected root generation and invalidates its private home. Caller-supplied `cwd` never overrides the stored canonical root. | Contract injection tests; account A/B/null-email fixtures; root/policy/generation mismatch denials; revocation/retirement journal; stored-root mutation rejection; G-SENT/G-DUAL/AT-003/007/044/056. |
```

At application, C-04 replaces the basis pre-image first. The application anchor above must then occur exactly once; insert K-CONSENT-1 immediately after it. The insertion position is between K-KEY-1 and K-ATTACH-1.

## Transaction C-09 — new K-UNTYPED-1

**Live insertion anchor:** line 118, immediately after K-SUBAGENT-3
**Invariant-ID condition:** Root/App concordance must confirm that `K-UNTYPED-1` is collision-free before application.

### PRE-IMAGE ANCHOR

```text
| **K-SUBAGENT-3** | Child runs produce reconstructible parentage, plan/brief/instruction hashes, status, return/output references, and any notice/update/amendment/acknowledgment evidence. | `HarnessEvent`; `execution/_Coordination/AgentRuns`; Section 9 validation. |
```

### POST-IMAGE INSERTION

```text
| **K-UNTYPED-1** | An untyped primary Codex session may use delegated-harness-native descent only inside Chirality's hard filesystem, network, process, canonical-root, account-identity, and policy envelope. Native descent does not assign an Agent 0/1/2 role, does not enter managed delegation, and does not imply inherited authority or capability. Chirality-managed descendants remain subject to their separate hierarchy, sealed brief, approval, allowlist/generalist, tool, context, cwd, write-scope, and durable-evidence checks. Native origin/lineage and instruction/config-asserted non-delegation are recorded truthfully. | Origin/lineage fixtures; managed-vs-native route tests; containment and cancellation tests; AgentRun evidence calibration; no-role-by-descent checks; G-ROLE/G-APPR/G-SBX/G4. |
```

## Transaction C-10 — consequential enforcement-map rows

**Live insertion anchor:** line 167, immediately after the existing `Release validation` row and before `Future domain profile validator`

### PRE-IMAGE ANCHOR

```text
| Release validation | K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1, K-NET-1, K-SDK-1 |
```

### POST-IMAGE INSERTION

```text
| Delegated-harness process supervisor and control sockets | K-CONTROL-1, K-ROOT-1, K-PATH-2, K-KEY-1 |
| `HostedEngineConsentPort` and account/root continuity | K-CONSENT-1, K-NET-1, K-KEY-1, K-ROLE-2 |
| Role entry and managed/native descendant classification | K-ROLE-2, K-UNTYPED-1, K-SUBAGENT-1, K-SUBAGENT-2, K-SUBAGENT-3 |
| Event codec, coordinator, persistence, SSE, replay, diagnostics, and support sinks | K-EVENT-3, K-EVENT-4, K-EVENT-6, K-KEY-1 |
| Renderer credential IPC | K-KEY-1, K-CONSENT-1, K-AUTH-1 |
| Exact-candidate release validation | K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1, K-NET-1, K-SDK-1, K-CONTROL-1, K-KEY-1 |
```

The existing `Release validation` row is retained byte-for-byte. These six rows are additional exact enforcement-map candidates; they do not claim implementation exists.

## Transaction C-11 — accepted-scope-change row candidate

**Live insertion anchor:** line 193, immediately after the SCA-APP-004 row
**Application condition:** only in the separately owner-approved Gate-5 act that applies SCA-APP-008; never during Gate-3/Gate-4 drafting.

### PRE-IMAGE ANCHOR

```text
| `SCA-APP-004` | 2026-07-23 | Selects Woven Dialogue with a Work/Agents Coordination Panel as the target information architecture; extends K-FS-1, K-NOMEM-1, and K-BIND-1 for provenance-labelled informational projection and strict primary-dialogue/read-only-replay separation while preserving runtime, API, SSE, security, history, compatibility, and human-authority boundaries. |
```

### POST-IMAGE INSERTION

```text
| `SCA-APP-008` | 2026-08-23 | Prospectively seats stable v3 account/consent UX, class-aware managed/native delegation, descendant evidence, and owner-gated release-operations carriers; carries the concordance-approved K-CONTROL-1, K-ROLE-2, K-NET-1, K-KEY-1, K-EVENT-3/4/6, K-CONSENT-1, K-UNTYPED-1, and enforcement-map amendments without changing App topology, Root ownership, lifecycle, or release authority. |
```

## D-APP-103 interaction — unchanged

The accepted Gate-1/2 interaction statement is restated without semantic change:

> D-APP-103 **defers**: the per-attempt decision-replay packet is prepared after SCA-APP-008 applies so it covers both descendant classes once.

No decision-replay packet is created or authorized by this Gate-3 package.

## Transaction ordering and atomicity

For a later separately approved Gate-5 act:

1. verify both target basis SHA-256 values;
2. apply D-01 through D-05 in order to one decomposition post-image;
3. do not apply any C transaction until Root/App concordance and invariant-ID collision checks pass and the owner approves the exact resolved contract candidate;
4. when eligible, apply C-01 through C-07 replacements, C-08/C-09 insertions, C-10 enforcement-map insertions, and C-11 accepted-scope-change insertion in that order;
5. validate stable IDs and unchanged 10-package/51-deliverable topology;
6. re-extract amended carrier dependencies and dispatch a fresh named dependency-closure audit; the frozen assessment PASS cannot substitute;
7. move `_LATEST.md` only if that same separately approved Gate-5 act expressly authorizes it.

The decomposition and contract transaction groups are not silently coupled: the stable carrier amendments can be approved while contract transactions remain held by concordance. No partial contract group may be represented as a completed concordance result.

## Four-state return

| State | Value | Meaning |
| --- | --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` | Exact Gate-3 transaction bytes are present. |
| `AuthorityState` | `NO_NEW_AUTHORITY` | Nothing is applied, accepted, routed, activated, or released. |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` | Decomposition, contract, SOWs, registers, lifecycle, dependencies, pointer, code, docs, frontend, Root, and other projects remain unchanged by this package. |
| `NextGateState` | `OWNER_GATE3_REVIEW_REQUIRED` | Ryan Tufts must approve, revise, or reject these exact bytes; contract application additionally requires Root/App concordance and a separate Gate-5 act. |

`ReadyForNextPhase = NO`.
