# AB-01 return — TM105 threat evidence

Child: `H2-TM105-AB01-AB09/AB-01`

Posture: evidence only; preparation only
Coverage: only the ten SHA-bound inputs declared in the sealed brief. This is
not a completeness claim about the runtime, adapters, deployment, Piping, or
TM105.

## 1. Input verification

`shasum -a 256` was run against every declared evidence input. Every observed
digest equalled the digest sealed in the brief; input drift status is **NONE**.

| Evidence input | Verified SHA-256 |
|---|---|
| `runtime/packages/contracts/src/engine.ts` | `d76fab70ef8ff7a6b5f4b5d669fb6367fa7707b664256433420b8b210c61ebdb` |
| `runtime/packages/contracts/src/harness/tool-descriptor.ts` | `bcb87844dce118a3f7743b3e2e0ecc0c376627d2dbaf1dee483a281c6f2b767b` |
| `runtime/packages/contracts/src/harness/event-schema.ts` | `8c6d17f0547f9433d9a2b0892ba50c266b08918142e39984ecc0a7d479661a2f` |
| `runtime/packages/contracts/src/harness/engine-conformance.ts` | `53c140a7ffa490e749faac8131ed8bf24b0f18d1392ac5931258a7b3f7d40427` |
| `runtime/packages/core/src/auth-registry.ts` | `28f8bade3372a6b0f1797a0c9623f0ad68f54f4ef2a6dee6638aeaeef20a29fa` |
| `runtime/packages/core/src/agent1-run-coordinator.ts` | `d0e8483df38d837a52c371b1a150a766046de44d17f0da66e5fd34c1415d27e7` |
| `runtime/packages/core/src/turn-coordinator.ts` | `992d501b49629b88cb72e42ad2c54d7934859da7e3a822259c68151e3ab3715b` |
| `runtime/tests/agent1-run.test.ts` | `42dbdd15f73e60839fdfd41b980a871a9a49a4ba62d0bb33df23933568167dff` |
| `runtime/tests/turn-hardening.test.ts` | `e5880870ef7ee94b90ebef4baf72335bf24073ca35b1d829ead05c3be9ee7b2b` |
| `projects/chirality-piping/execution/_Coordination/COORDINATION_RESPONSE_2026-08-02_PIPING_RUNTIME_SURFACE_NEEDS.md` | `e38c5614351ce45d77535c4bb234580bbbb1916a68a482660b6c3f4e230235e7` |

## 2. Inventories

### Assets

| Asset | Evidence-grounded description |
|---|---|
| Runtime client authorization state | Client ID, token hash, optional project ID, scopes, creation and optional revocation times are persisted in a registry (`runtime/packages/core/src/auth-registry.ts:17-29,52-74`). |
| Bearer-token material | A 32-byte random bearer token is returned to the caller and written to a per-client plaintext token file with mode `0600`; the registry stores its SHA-256 hash (`runtime/packages/core/src/auth-registry.ts:52-74`). |
| Provider credentials | The engine contract exposes a provider credential port returning a credential string or configured status; storage, redaction, lifetime, and caller authorization are not in the declared evidence (`runtime/packages/contracts/src/engine.ts:61-64`). |
| Project-root data and tool effects | Tool descriptors classify read, project-root write, shell, network, coordination, and subagent surfaces; these classifications are descriptor evidence, not by themselves invocation-enforcement evidence (`runtime/packages/contracts/src/harness/tool-descriptor.ts:14-106,220-478`). |
| Agent-run control state | Run/project/session IDs, manager and child selections, sealed briefs and hashes, return hash, evidence reference, review hash, approval reference, and status are recorded in `run.json` (`runtime/packages/core/src/agent1-run-coordinator.ts:52-101,384-421,560-601,784-799`). |
| Session/event evidence | Events carry event/session/optional turn/optional parent IDs, timestamp, type, and unconstrained record data; the vocabulary includes tool, subagent, coordination, terminal, and mirror-error events (`runtime/packages/contracts/src/harness/event-schema.ts:1-61`). |
| Piping-local engineering state | The consumer response identifies model/state/run/operation IDs, hashes, structured operation and result evidence, diagnostics, redaction and acceptance records as Piping-local assets; it explicitly does not make them generic authority (`projects/chirality-piping/execution/_Coordination/COORDINATION_RESPONSE_2026-08-02_PIPING_RUNTIME_SURFACE_NEEDS.md:86-120,136-147`). |

### Principals and identity-bearing actors

| Principal/actor | Established facts; unknowns retained |
|---|---|
| Runtime bearer client | Authentication returns client ID, optional project ID and scopes after token, scope, revocation, and conditional project checks (`runtime/packages/core/src/auth-registry.ts:100-134`). Whether this maps to a person, service, device, or organization is `UNKNOWN`. |
| Agent 1 manager session | Created as role `agent1`, with a selected adapter and manager persona; target definition must be Agent type 1 (`runtime/packages/core/src/agent1-run-coordinator.ts:134-161`). Human accountability behind it is `UNKNOWN`. |
| Agent 2 child session | The inspected pilot creates one `agent2`/`TASK`/`readOnly` child with a parent session, approval-ref string, and no allowed write targets (`runtime/packages/core/src/agent1-run-coordinator.ts:213-274`). |
| Engine adapter/provider/model | Selection and initialization carry adapter, provider and model identity, and the coordinator checks initialization attribution (`runtime/packages/core/src/turn-coordinator.ts:217-256`). Vendor guarantees and trustworthiness are `UNKNOWN`. |
| Project registry / authorized project record | Both turn and Agent 1 coordinators require an authorized project before proceeding (`runtime/packages/core/src/turn-coordinator.ts:81-94`; `runtime/packages/core/src/agent1-run-coordinator.ts:123-151`). The authorizing human/policy authority is `UNKNOWN`. |
| Manager runtime and tool bridge | The manager can invoke delegate/review hooks; the bridge binds one exact read tool and produces permission/lifecycle evidence (`runtime/packages/core/src/agent1-run-coordinator.ts:203-438,660-758`). These are code components, not established trusted human principals. |
| Piping user/reviewer | The consumer response records explicit user acceptance and professional-boundary fields on local operation paths (`projects/chirality-piping/execution/_Coordination/COORDINATION_RESPONSE_2026-08-02_PIPING_RUNTIME_SURFACE_NEEDS.md:88-99,127-134`). Actor identity and trust policy remain `UNKNOWN`. |

### Trust boundaries

1. Bearer header to `AuthRegistry`: opaque token material becomes a runtime
   principal after registry lookup, revocation, scope, and optional project
   checks (`runtime/packages/core/src/auth-registry.ts:100-134`).
2. Caller/project context to coordinators: the inspected coordinators rely on
   `ProjectRegistry.requireAuthorized`; how external request authentication is
   bound to those calls is outside this evidence set
   (`runtime/packages/core/src/turn-coordinator.ts:81-94`;
   `runtime/packages/core/src/agent1-run-coordinator.ts:123-151`).
3. Agent 1 manager runtime to coordinator-owned delegation/review hooks: the
   manager supplies the child brief and later reviews the same child, while the
   coordinator fixes the mechanical child shape
   (`runtime/packages/core/src/agent1-run-coordinator.ts:203-308,430-481`).
4. Agent 2/model to native/tool surface: the pilot binds one closure-backed
   `read_file`; the broader descriptor overlay advertises other built-ins and
   MCP tools, but its actual adapter enforcement is not present in the sealed
   evidence (`runtime/packages/core/src/agent1-run-coordinator.ts:660-758`;
   `runtime/packages/contracts/src/harness/tool-descriptor.ts:220-478,984-1289`).
5. Engine/adapter event stream to durable session evidence: the turn
   coordinator checks active session/turn attribution, initialization identity,
   terminal ordering and process exit before persisting/closing
   (`runtime/packages/core/src/turn-coordinator.ts:150-256,263-333`).
6. Runtime process to filesystem evidence and credentials: registry JSON,
   token files, session events, and run JSON cross this boundary. Filesystem
   ACLs, host identities, storage encryption, backup, and tamper resistance are
   `UNKNOWN` except for the token-file `0600` operation shown above.
7. Generic runtime to Piping consumer semantics: Piping retains operation,
   validation, stale-state, units, acceptance, privacy, and professional
   meaning; its current application-owned agent broker and bounded runtime
   grants are explicitly absent/open
   (`projects/chirality-piping/execution/_Coordination/COORDINATION_RESPONSE_2026-08-02_PIPING_RUNTIME_SURFACE_NEEDS.md:101-120,149-170`).

### Attacker-capability inventory

These are capabilities observable from code paths, not claims about a deployed
attacker or topology.

| Capability | Evidence limit |
|---|---|
| Present a copied valid bearer token repeatedly | Authentication has no nonce, audience, expiry, or one-time-use check in the inspected implementation; revocation and scopes are checked (`runtime/packages/core/src/auth-registry.ts:100-145`). Reachability is `UNKNOWN`. |
| Call `ensureClient` again with changed desired scopes/project | An existing valid client/token is returned without comparing the requested scopes or project ID to the stored record (`runtime/packages/core/src/auth-registry.ts:77-98`). Caller authorization is `UNKNOWN`. |
| Supply a non-empty approval-reference string to the Agent 1 coordinator | The inspected check proves non-emptiness only (`runtime/packages/core/src/agent1-run-coordinator.ts:123-133`). API exposure and upstream verification are `UNKNOWN`. |
| As manager runtime, choose a child sealed brief and accept/reject that child | The same manager-facing hook surface provides delegate and review; review is restricted to that manager's child (`runtime/packages/core/src/agent1-run-coordinator.ts:203-308,430-481`). |
| As engine/adapter, emit public and harness events | Cross-session/turn events, attribution mismatch, bad terminal/process ordering, and forged receipt success are rejected by inspected coordinator logic/tests (`runtime/packages/core/src/turn-coordinator.ts:150-333`; `runtime/tests/turn-hardening.test.ts:125-369`). |
| Ask for native tool names through turn options | `request.opts.tools` takes precedence over the coordinator's `toolNames` argument (`runtime/packages/core/src/turn-coordinator.ts:118-129`). Which callers can populate it and whether adapter preflight independently denies it are `UNKNOWN`. |
| Alter runtime files given independent filesystem write access | Run hashes are unkeyed and records are atomically rewritten, but no signature/MAC/hash chain or verifier is shown (`runtime/packages/core/src/agent1-run-coordinator.ts:384-421,560-601,784-799`). Such filesystem access is `UNKNOWN`. |

## 3. Threat matrix

All severity entries are **`UNKNOWN`**. No authoritative severity policy or
deployment impact basis appears in the declared evidence, so this return does
not assign even provisional severity.

| Threat class | Evidence reference | Observed exposure | Present mechanical control | Remaining / unmitigated risk | Severity posture | Evidence that would falsify the control claim |
|---|---|---|---|---|---|---|
| Confused deputy | `runtime/packages/core/src/agent1-run-coordinator.ts:123-151,203-308,430-481`; `runtime/packages/core/src/auth-registry.ts:100-134` | The manager chooses the child brief and reviews its own child. The coordinator accepts any non-empty approval-reference string; the inspected files do not bind that string to a verified issuer, purpose, or exact delegated brief. An unscoped client record also passes the project mismatch condition for any requested project for which it has the required scope. | Authorized project lookup; Agent 1 type check; enabled-adapter check; at most one child; review must name that manager's child; child rights are fixed to one read-only tool. | Semantic-purpose substitution and self-review remain possible within the observed hook shape; upstream caller-to-grant binding and approval validation are not evidenced. Project-wide clients may be intentional, but policy is `UNKNOWN`. | `UNKNOWN` | An in-scope call trace/test showing cryptographically or registry-validated approval subject, purpose, project, parent brief, child brief, expiry, and reviewer separation; negative tests for cross-purpose and cross-project use. |
| Replay | `runtime/packages/core/src/auth-registry.ts:100-145`; `runtime/packages/contracts/src/harness/event-schema.ts:52-61` | A valid bearer token can be presented repeatedly until revocation; events have IDs/timestamps but no shown nonce-consumption or replay cache. | Random 32-byte token, hashed lookup with timing-safe comparison, revocation checks, required scope, conditional project check. | No token expiry, audience, issuance epoch, request nonce, or proof-of-possession is shown. Event-ID uniqueness enforcement is not shown. | `UNKNOWN` | Tests or implementation evidence proving expiry/audience/nonce/epoch enforcement and duplicate request/event refusal across restart and concurrent paths. |
| Stale grants | `runtime/packages/core/src/auth-registry.ts:77-98,136-158` | `ensureClient(clientId, scopes, projectId)` returns the existing token when its file/hash matches, without comparing stored scopes/project to the newly requested values. | Explicit per-client and per-project revocation; missing/mismatched plaintext material rotates through `issueClient`. | Requested policy changes can leave an old non-revoked record and token in effect; no expiry or policy-version binding is shown. | `UNKNOWN` | A negative test showing changed scopes/project cause refusal or rotation and invalidate the old token, plus evidence that policy version/expiry is checked at authentication. |
| Policy mismatch | `runtime/packages/contracts/src/engine.ts:8-19`; `runtime/packages/contracts/src/harness/tool-descriptor.ts:14-106,220-478,984-1289`; `runtime/packages/core/src/turn-coordinator.ts:118-129` | The engine contract uses operation/effect/root permissions, while descriptors use a separate permission/path-scope/human-gate vocabulary. The turn coordinator permits `request.opts.tools` to override supplied tool names. No mapper/enforcer joining these layers is in the sealed set. | Descriptor lookup rejects duplicate aliases and can enumerate current-tranche disallowed SDK names (`runtime/packages/contracts/src/harness/tool-descriptor.ts:1291-1400`); pilot tool closure carries exact allow/read/root permission. | Descriptor metadata or allowed-name calculation could diverge from adapter/native invocation behavior; human-gate fields are not enforcement proof here. | `UNKNOWN` | End-to-end negative tests at the real adapter boundary showing every unrequested/descriptor-only/native alias is denied, `request.opts.tools` cannot widen caller authority, and permission/path/human-gate decisions match the executing closure. |
| Credential leakage | `runtime/packages/core/src/auth-registry.ts:31-35,52-74`; `runtime/packages/contracts/src/engine.ts:61-64`; `runtime/packages/contracts/src/harness/engine-conformance.ts:464-471` | `issueClient` returns the token and token path and stores plaintext token material; provider credential retrieval returns a string. Event data is an open record. | Token registry stores a hash; token file write/chmod uses `0600`; conformance can optionally scan public/persisted evidence for caller-supplied forbidden values. | Process memory, return/log/error channels, backups, token-directory permissions, provider credential handling, and mandatory redaction are not established. The conformance scan is optional and substring-based. | `UNKNOWN` | Filesystem permission tests for directories/files, mandatory end-to-end secret-canary tests over all event/error/log/artifact paths, and implementation evidence that raw credentials cannot enter event `data` or run records. |
| Child widening | `runtime/packages/core/src/agent1-run-coordinator.ts:203-308,660-758`; `runtime/tests/agent1-run.test.ts:225-353` | Manager-supplied `sealedBrief` is not shown as constrained to or derived from the parent brief. Native adapter tool availability beyond the bound bridge is outside this evidence set. | Exact one-child maximum; fixed Agent 2/TASK/read-only session; empty allowed-write targets; exact resident model and enabled adapter; one relative realpath-contained file no larger than 1 MiB; tool schema accepts no properties; execution receipt required; tests fail closed if the child does not execute it. | Semantic widening inside the child prompt is unmitigated by a parent/child brief relation check. Mechanical no-native-tool-bypass depends on enforcement not included here. | `UNKNOWN` | A brief-containment/provenance check and negative real-adapter test where the child tries all SDK/MCP/native tools, alternate paths, symlinks, absolute paths, writes, shell, network, and subagents, with durable denials and no side effects. |
| Native-tool bypass | `runtime/packages/contracts/src/harness/tool-descriptor.ts:125-179,984-1289,1390-1400`; `runtime/packages/core/src/turn-coordinator.ts:118-129`; Piping response `:93-99,149-170` | Descriptors say built-ins are behind overlays/hard-deny/hooks; shell/write are marked exposed in workspace-write mode. Actual overlay/hook/adapter-preflight enforcement is not in the evidence set. Piping explicitly reports no application-owned native-tool broker and bounded grants remain open. | Reserved network, notebook, multi-edit and subagent surfaces are descriptor-only/future-policy; a disallowed-name utility exists; the Agent 1 pilot binds only `read_file`. | Claims of no bypass cannot be warranted outside the one closure-backed pilot. Piping's CLI is explicitly not an agent harness and its fixture fallback is not authoritative success evidence. | `UNKNOWN` | Real-adapter invocation tests demonstrating hard denial of raw SDK aliases and binaries/process/network paths not in the grant, plus Piping-local tests showing UI/API/agent routes cannot bypass consumer validation/acceptance/redaction seams. |
| Evidence tamper | `runtime/packages/contracts/src/harness/engine-conformance.ts:315-428,464-471`; `runtime/packages/core/src/turn-coordinator.ts:150-333`; `runtime/packages/core/src/agent1-run-coordinator.ts:384-421,560-601,784-799`; `runtime/tests/turn-hardening.test.ts:125-369` | Adapter-originated evidence is untrusted; durable run records are rewritten snapshots with unkeyed hashes. Event schema shows no signature/hash-chain fields. | Session/turn attribution, single terminal, initialization attribution, process-exit consistency, required in-process receipt, tool lifecycle/permission-order checks, live-event presence in replay, and optional secret scan. Tests reject foreign-session, late, missing-exit, nonzero-success, and adapter-forged receipt cases. | No authenticity, append-only guarantee, chain/sequence verification, duplicate event-ID check, extra-event comparison, signed time, or verification of run-record hashes is shown. A writer with storage access could plausibly rewrite evidence and recompute unkeyed hashes; actual access is `UNKNOWN`. | `UNKNOWN` | Tamper tests against the actual persistent store covering deletion, insertion, reorder, duplicate IDs, field edits, run-record replacement, hash recomputation, rollback, and restart, with an independently anchored verifier detecting every mutation. |

## 4. Conflicts and non-coverage

### Explicit conflicts / claim tensions

1. Descriptor prose says read built-ins are behind a permission overlay and
   hard-deny policy and that write/shell tools are exposed only after policy and
   hooks (`tool-descriptor.ts:125-179`). The sealed set contains descriptor and
   disallowed-name construction, but not the real adapter invocation wrapper.
   Therefore the statements are implementation claims not independently
   established here.
2. The `delegate_agent` descriptor says managed coordination enforces hierarchy,
   seals, parentage, capabilities, and project boundaries
   (`tool-descriptor.ts:149-155,634-648`). The inspected Agent 1 pilot does enforce
   one direct child and a narrow file closure, but it only checks that
   `approvalReference` is non-empty and lets the manager originate the child
   brief. A generalized `delegate_agent` handler is not among the inputs.
3. Conformance can require tool-permission evidence and compare live event IDs
   with durable replay, but those checks are options and the inspected
   `TurnCoordinator` does not call `runEngineConformance`. Applicability to
   production turns is therefore `UNKNOWN`.
4. Piping describes a deny-by-default plugin declaration and no-bypass concepts,
   while also recording that runtime dispatch, bounded grants, permission
   persistence, agent broker, and runtime-wide guard binding remain absent or
   open (Piping response `:93-99,149-170`). The declaration must not be treated
   as an implemented control.

### Non-coverage

- No external endpoint/service method connecting `AuthRegistry` principals to
  the inspected coordinator calls is in scope.
- No actual SDK/native adapter permission overlay, tool-binding implementation,
  shell hook, write hook, or hard-deny invocation path is in scope.
- No session-store, filesystem helper, project-registry, runtime service,
  deployment, OS account, container, backup, secret store, network, or host
  configuration is in scope.
- No evidence establishes token expiry/audience, approval issuer validation,
  event/run cryptographic integrity, reviewer independence, or event-ID
  uniqueness.
- The tests establish the named fixtures and negative cases only; no tests for
  changed `ensureClient` policy, bearer replay, native-tool bypass, approval
  forgery, or persistent evidence tamper are in the set.
- The Piping response is consumer-local coordination evidence at a stated prior
  repository basis, not generic TM105 semantic authority or current deployment
  evidence.

## 5. Facts remaining `UNKNOWN`

- Grant issuer, approval-policy authority, trust anchors, identity proofing,
  approver/reviewer independence, revocation SLA, token lifetime, and intended
  meaning of an unscoped project client.
- Runtime/application owners for authentication, coordination, adapters,
  evidence storage, incident response, and release decisions.
- Vendor guarantees, adapter/provider operational controls, model behavior,
  platform/OS/container accounts, process isolation, sandbox realization,
  network topology, deployment topology, backup/logging/monitoring systems, and
  filesystem access populations.
- Data classification, regulated/private data presence, retention, encryption,
  acceptable severity, threat likelihood/impact, and product acceptability.
- Piping transport, plugin runtime, permission persistence, signing/isolation,
  operative agent broker, bounded application-agent grants, and runtime-wide
  guard completion, as the Piping response itself records.

## 6. Separately owned next evidence actions

These are acquisition actions only, not control, backend, grammar, policy, or
implementation recommendations.

| Evidence workstream | Accountable owner | Next evidence action |
|---|---|---|
| Runtime authentication | `UNKNOWN` | Produce call-site and test evidence for who may issue/ensure/revoke clients; exercise changed scope/project requests, old-token use, project-wide clients, restart, concurrency, expiry if any, and secret canaries across return/log/event channels. |
| Runtime approval/delegation | `UNKNOWN` | Produce the approval-reference resolver and generalized `delegate_agent` handler evidence, then trace issuer, subject, project, purpose, parent/child brief hashes, expiry/revocation, reviewer identity, and negative cross-purpose behavior. |
| Adapter/tool enforcement | `UNKNOWN` | Produce the actual preflight/tool-resolution/binding/hook code and real-adapter negative-test evidence for aliases, `request.opts.tools`, unrequested built-ins, writes, shell, network, subagent, symlink/path escape, and raw native execution. |
| Durable evidence store | `UNKNOWN` | Produce session-store/filesystem implementation, permissions, ordering/uniqueness rules, recovery behavior, and tamper-test results for events, run records, hashes, rollback, deletion, insertion, and restart. |
| Piping-local owning instruments | Specific accountable human is `UNKNOWN`; local owning surfaces are identified by the Piping response | At the owning Piping cadence, refresh the response's cited evidence for agent broker/grants, plugin/API transport, persistence, guard binding, fixture fallback, and UI/API equivalence; return only observed current state and remaining gaps. |

## 7. Effect boundary

All semantic, implementation, lifecycle, release, reliance, and byte-gate holds
remain intact. This return selects no backend, rights grammar, trust boundary,
severity policy, control, lifecycle posture, product direction, owner, vendor,
or deployment model. It authorizes no implementation or state transition and
has no authority effect beyond returning evidence to the parent under the
sealed brief.
