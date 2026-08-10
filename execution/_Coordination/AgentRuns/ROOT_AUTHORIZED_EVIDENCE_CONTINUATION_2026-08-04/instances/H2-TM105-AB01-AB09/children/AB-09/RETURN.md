# AB-09 — DEL compatibility evidence crosswalk

- Child: `H2-TM105-AB01-AB09/AB-09`
- Posture: evidence only; declared evidence set only
- Result: `COMPLETED_WITH_UNRESOLVED_FACTS`
- Completeness claim: none beyond the 18 declared inputs and the sealed brief

## 1. Input and accepted-member verification

Every declared input matched the SHA-256 sealed in the launch brief. There is
no observed input drift.

| ID | Declared evidence path | Verified SHA-256 | Result |
|---|---|---|---|
| S0 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003/ACCEPTED_SEMANTIC_SNAPSHOT.md` | `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa` | MATCH |
| S1 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003/ACCEPTED_SEMANTIC_MEMBERS.sha256` | `e1f841d808e73642e28a6dec0b19adfdcf0e0c4800b6541701a9d8e7ee6a2874` | MATCH |
| D1 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/candidate_v2/AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md` | `2bff966d3806078472370cfd0e7f1546064660f325d4a0e2534a71a1a67c7d13` | MATCH |
| D2 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/candidate_v2/DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md` | `7f64cfd2ef567bbceab2d89046137b9d6fbf7ccd49920fa34a76f373547f9153` | MATCH |
| D3 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/candidate_v2/EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md` | `d7c1838cf244595cb287173e44b073dfe73db2bdecd9b9946e851978ed89d95a` | MATCH |
| D4 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/candidate_v2/OWNER_DECISION_RECORD_CANDIDATE_V2.md` | `2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c` | MATCH |
| D5 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/candidate_v2/ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md` | `cbe36a275bfe882c575673c8c70d8598b7f0c724b96fdf9ccae962a036677bc1` | MATCH |
| D6 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/candidate_v2/ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md` | `9b023b347dca4bd255e6c7f2fb499e5654d3ab455f90004be29dd1b545eaf5f8` | MATCH |
| C1 | `runtime/packages/contracts/src/session.ts` | `22e49ccf47a83e93d065a1d731a0e726cba6559f8436f78c3451d4db2fd8bf51` | MATCH |
| C2 | `runtime/packages/contracts/src/events.ts` | `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` | MATCH |
| C3 | `runtime/packages/contracts/src/harness/types.ts` | `7e035b3a7b1d50176b7f0605b62da9695502305a38d61e27b7c3799531de70e3` | MATCH |
| C4 | `runtime/packages/contracts/src/harness/transcript-replay.ts` | `05cd1eae2a8c911775b00e8957ff9b4141f2072e6f063eaadec9b3bc62b1b99a` | MATCH |
| R1 | `runtime/packages/core/src/session-store.ts` | `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` | MATCH |
| R2 | `runtime/packages/core/src/project-registry.ts` | `7b803aa01fc4fae97b3544f66cfafef1d2742270b670dec4011ba352f2fbce71` | MATCH |
| R3 | `runtime/packages/core/src/runtime-service.ts` | `43b2dd4dbf8b1a91a057350558229616e34bfec258b2b9ad8f5e36c058c7c74d` | MATCH |
| C5 | `runtime/packages/client/src/client.ts` | `38a55c95ba2ffa488e46a1debb48939a4aa8af2da89b80777e9d28f6f0c4adf4` | MATCH |
| T1 | `runtime/tests/session-and-residency.test.ts` | `5d9c1cda16267557ea8ca599109568718fcb7a22b3dcb8f58a67f760fa596b02` | MATCH |
| A1 | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-84_PACKET_PI_OMLX_AGENT2_CAPABILITY_EXPANSION_REVISION_2_2026-08-02.md` | `59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9` | MATCH |

`shasum -a 256 -c ACCEPTED_SEMANTIC_MEMBERS.sha256` returned `OK` for all six
accepted members. S0 §“Accepted exact bytes” binds those six exact hashes as
human-accepted DEL-02-06 semantic bytes. The member manifest itself also
matches its sealed input hash. Drift verdict: `NO_DRIFT`; accepted-member
verification: `PASS_6_OF_6`.

## 2. Field-by-field compatibility matrix

“TM105 coverage” below means coverage available from this sealed evidence
crosswalk; it does not select a TM105 value.

| Surface | Current session/event/client/runtime evidence | Accepted DEL-02-06 treatment | TM105 coverage / unresolved delta |
|---|---|---|---|
| Identity | A session is a generated UUID stored with `projectId`, `projectRoot`, `sessionId`, role and engine selection (C1 lines 3-17; R1 lines 28-58). Events carry event, project, session and turn identities (C2 lines 17-28). Client routing is by project/session and Unix socket/token (C5 lines 39-45, 271-399, 491-540). | Compatibility identity is a distinct Root-owned `root-runtime-<positive-decimal-epoch>` value, declared by both daemon and affected client and compared byte-for-byte before every consequential operation (D5 §§“Identity grammar”, “Declaration and comparison”). It is not a session ID, route namespace, package version, runtime fingerprint, source/release commit or Tier-0 identity. | Current identities do not cover the DEL compatibility identity. Exact TM105 identity is `UNKNOWN` and held; the DEL placeholder is not a runtime value (S0 §“Preserved unresolved and authority boundaries”; D5 §“Identity grammar”). |
| Lifetime | Current records have `createdAt`/`updatedAt`, but no expiry, support window, lease, generation lifetime or compatibility-lifetime field (C1 lines 7-10; C3 lines 28-68). Session deletion is explicit and leaves a deletion marker (R1 lines 117-125). | DEL specifies per-operation equality, no implicit session-start carry-forward, and a new epoch for consequential client-visible semantic change (D5 §§“Declaration and comparison”, “Epoch-change criteria”). | Exact compatibility lifetime, client support window, grace period, and coexistence duration are `UNKNOWN`. No TM105 lifetime is selected. |
| Parentage | `parentSessionId` is optional in create/session records; the generic harness record also has optional parent instance/type fields (C1 lines 12-13, 24-34; C3 lines 28-68). Session creation persists only a supplied `parentSessionId` among those parent fields (R1 lines 39-57). | DEL recovery preserves `project_id`, `session_id`, `turn_id`, `accepted_event_id`, and `recovery_run_id`; it creates no automatic retry lineage or `supersedes_turn_id` (D6 §§“Recovery terminal policy”, “Retry replay and resume”). | Parentage is distinct from continuation/migration identity. Whether TM105 adds generation parentage, rollover lineage, or a new-session link is `UNKNOWN`. |
| Generation / epoch | `residencyEpoch` is optional on the session and event attribution (C1 line 14; C2 lines 29-36). It is model-residency attribution, not a declared compatibility epoch. | A positive-decimal Root epoch is required for consequential client-visible changes; the exact future epoch remains owner-supplied and unresolved (D5 §§“Identity grammar”, “Epoch-change criteria”; S0 §“Preserved unresolved and authority boundaries”). | No current compatibility epoch field exists in the declared runtime/client evidence. Exact TM105 epoch and rollover trigger remain held/`UNKNOWN`; residency epoch must not be repurposed. |
| Profile / fingerprint / digest | Boot produces a runtime fingerprint and its SHA-256, then a boot fingerprint over project manifest hash, persona, mode and runtime fingerprint (R3 lines 347-399; C3 lines 164-196). Project registration stores a manifest hash and rejects later drift (R2 lines 29-58, 69-84). The declared client requests carry no compatibility, profile or transcript-prefix digest (C5 lines 271-399). | One immutable complete binding manifest must bind compatibility identity, all six accepted semantic hashes and package-manifest identity, source/release identities, every affected-client basis/operation, migration/conformance artifacts, evidence, census/open findings, cutover/rollback/replay disposition, and human acts (D5 §“Compatibility binding record”). | Runtime/boot fingerprints and manifest hashes are useful evidence inputs but are not the DEL compatibility identity or complete binding manifest. Exact TM105 profile/digest scheme, canonicalization and migration are `UNKNOWN`. A1 §4/R1 proposes sandbox-profile identity plus transcript/event-prefix SHA-256, but A1 is `AWAITING_RULING`, not accepted. |
| Status / terminal | Session summary status is only `idle`, `running`, `completed`, `failed`, or `interrupted` (C1 lines 15-16). The runtime event union exposes completed/failed/interrupted but not recovery-indeterminate (C2 lines 1-15). Transcript replay supports completed/failed/cancelled/interrupted and retains the last recognized terminal status (C4 lines 7-16, 60-64, 120-132, 318-353). | DEL keeps completed, failed, cancelled, interrupted and `turn.recovery_indeterminate` distinct; the latter maps to session-summary `recovery_required`. Every startup enters the four-state recovery machine (`RECOVERY_REQUIRED`, `RECOVERY_SCANNING`, `RECOVERY_BLOCKED`, `READY`) before readiness (D6 §§“Recovery terminal policy”, “Daemon recovery state machine”). | Current contracts do not encode `turn.recovery_indeterminate`, `recovery_required`, or daemon recovery state. Exact TM105 status mapping remains unselected; compatibility delta is evidenced, not implemented. |
| Interrupted work | There is a client interrupt route and runtime interrupt fan-out (C5 lines 383-390; R3 lines 463-468); `turn.interrupted` is recognized by replay/current boot terminal validation (C4 lines 120-132; R3 lines 274-289). Declared evidence does not establish resend/resume behavior after transport loss. | Live interruption remains distinct from process-loss-after-acceptance indeterminacy. An indeterminate turn is never retried, replayed, resumed, resent, or inferred complete; a later authorized operation is a new independent turn (D6 §§“Recovery terminal policy”, “Retry replay and resume”). | Current interrupt exists, but exact TM105 interruption/continuation behavior and client UX are `UNKNOWN`. DEL’s no-resend boundary must remain separate from session interruption. |
| Partial / indeterminate work | Transcript replay can retain streamed `message.delta` text as a `started` item when no completed assistant message exists (C4 lines 220-298). Session-store replay skips malformed lines from the event list while reporting a malformed count (R1 lines 156-207). There is no declared current indeterminate terminal or quarantine state. | Partial output is preserved and classified as indeterminate evidence; completion is never inferred. Malformed/contradictory units are byte-preserved, quarantined, never auto-repaired, and keep global consequential readiness closed pending disposition (D3 §“Recovery cutover replay and indeterminate completion”; D6 §§“Malformed and contradictory evidence”, “Daemon recovery state machine”). | The current started-delta view is not an accepted indeterminate-work disposition. Exact TM105 partial-output carrier, persistence and client presentation are `UNKNOWN`. |
| Rollover / migration | SessionStore performs lazy legacy-to-v2 central migration on `get`, preserves the legacy source, copies legacy events, and records migration metadata (R1 lines 82-103, 223-270; T1 lines 39-75). Project manifest drift requires re-registration (R2 lines 69-84). No declared client compatibility migration is present. | Recovery adoption is a compatibility `DELTA`; a later owner must supply the exact epoch, accept the binding manifest, and separately authorize implementation. Cutover freezes exact bases, does not retry/replay indeterminate turns, preserves partial output, and crosses an irreversible boundary at the first recovery write (D5 §“Recovery compatibility disposition”; D3 §§“Recovery cutover replay and indeterminate completion”, “Cutover rollback and irreversible boundary”). | Legacy storage migration is not compatibility/profile migration. Exact TM105 rollover, migration window, old-reader policy, profile repin and client transition remain `UNKNOWN` and held. |

## 3. Compatibility/migration delta and old/new client behavior

The accepted DEL bytes establish a compatibility `DELTA` within DEL’s scope:
recovery-before-readiness, a distinct recovery terminal, new machine-readable
states/results, and new admission conditions are consequential client-visible
semantics (D5 §“Recovery compatibility disposition”, accepted by S0 §“Accepted
exact bytes”). They do not supply the exact epoch or complete future binding
manifest, and they authorize no implementation.

| Topic | Current/old-client evidence | DEL-conforming future behavior | Compatibility or migration fact still absent |
|---|---|---|---|
| Per-operation declaration | Current `RuntimeClient` sends ordinary JSON/SSE requests over the configured Unix socket with bearer token; the declared request methods contain no compatibility identity/basis field (C5 lines 93-180, 271-399, 491-540). | Client declares its exact accepted Root compatibility identity in every consequential request; daemon preflight declares its own; exact equality is required before work (D5 §“Declaration and comparison”). | Exact request/header/envelope locus, epoch value and binding manifest: `UNKNOWN`/unproduced. |
| Old client after future activation | Current behavior continues until separately authorized implementation; no current byte is changed by DEL acceptance (S0 §“No implied downstream act”). | An absent, malformed, stale, inferred or unequal identity rejects before consequential work. No range negotiation, downgrade or multi-version inference is supported (D5 §“Declaration and comparison”). | Supported old-client versions, compatibility shim, warning/grace period and migration window: `UNKNOWN`. |
| Mismatch | Current errors are mapped from non-2xx responses; no declared client special case for DEL mismatch exists (C5 lines 118-165). | Exact code `RUNTIME_COMPATIBILITY_MISMATCH`, `retryable:false`, `consequential_work_started:false`, safe compared identities and basis hashes; Root generic client/CLI preserves machine fields (D5 §“Mismatch envelope”; D2 §§“Ten-condition identifiers and envelopes”, “Precedence retry and evidence fields”). | HTTP status, exact transport schema locus, CLI exit code and App presentation: `UNKNOWN` pending owned contract/conformance work. |
| Retry/resend | The declared client exposes cancellation/abort, but no evidence here proves automatic retry or its absence after uncertain transport outcome (C5 lines 137-210, 491-540). | No automatic retry/resend. Repair/reconnect/rebind starts new precondition evaluation, not replay of indeterminate work (D2 §“Precedence retry and evidence fields”; D6 §“Retry replay and resume”). | Client-version-specific retry behavior and migration remediation: `UNKNOWN`. |
| Recovery/partial work | Current replay reconstructs messages/tools/recognized terminals and can show unfinished deltas; malformed lines are omitted from returned events but counted (C4 lines 220-353; R1 lines 156-207). | Preserve partial output as indeterminate evidence; emit distinct recovery-indeterminate terminal only under the accepted conditions; no inferred completion or reconstructed result (D3 §“Recovery cutover replay and indeterminate completion”; D6 §“Recovery terminal policy”). | Exact old-corpus conversion, partial-output schema and UI mapping: `UNKNOWN`; App mapping remains App-owned. |
| Digest/profile migration | Current runtime/boot fingerprint and project manifest hash exist, while A1 proposes—without a ruling—resume equality over Root identity, Pi version, sandbox-profile identity, model, residency epoch and transcript-prefix SHA-256 (R3 lines 347-399; R2 lines 29-58; A1 §4/R1). | Binding manifest must include exact semantic/source/release/client/migration/evidence/disposition hashes; missing or placeholder values block implementation/release (D5 §“Compatibility binding record”). | Exact profile identity, accepted Pi version, transcript digest algorithm/canonical prefix, repin plan and support window: `UNKNOWN`. |
| Rollback | Current declared runtime evidence contains no DEL cutover rollback implementation. | Source/runtime rollback only before first recovery-corpus mutation; afterward require proven old-reader coverage or separately approved forward repair, preserving history/audit and never replaying work (D3 §“Cutover rollback and irreversible boundary”). | Exact old-reader versions/corpus compatibility and operational window: `UNKNOWN`. |

Thus “new client” denotes a future separately accepted client contract bound to
the exact future Root identity; it does not denote any version currently
accepted by this evidence. “Old client” support facts are absent. No migration
window, dual-stack interval, fallback, lifecycle promise, or release acceptance
may be inferred.

## 4. Interrupted/partial-work and digest/profile migration treatment

1. Preserve three distinct facts: live `turn.interrupted`; ordinary observed
   completion/failure/cancellation; and process-loss-after-acceptance
   `turn.recovery_indeterminate`. Do not map one to another (D6 §“Recovery
   terminal policy”).
2. For the indeterminate case, preserve partial output only as evidence; do not
   reconstruct output, infer engine result, resume, replay, retry or resend. A
   later authorized operation has a new turn identity and no automatically
   inferred lineage (D6 §“Retry replay and resume”; D3 §“Recovery cutover replay
   and indeterminate completion”).
3. Acceptance-time attribution must durably bind provider, engine, model,
   local/remote classification and residency epoch. Missing or ambiguous
   attribution is a blocker, not a value to infer from current selection (D6
   §§“Drain reconstruction”, “Acceptance-time attribution”). Current event
   attribution is optional and lacks an explicit engine and local/remote field
   (C2 lines 29-36), so coverage is not proven.
4. Do not treat the current `runtimeFingerprint`, `bootFingerprint`, project
   `manifestHash`, `residencyEpoch`, or App-proposed sandbox/transcript digest
   as interchangeable. They bind different objects. The exact compatibility
   manifest must name each accepted basis separately (D5 §§“Identity grammar”,
   “Compatibility binding record”).
5. Current lazy legacy migration is storage migration, not compatibility
   rollover. Moreover, a DEL retained diagnostic must perform no migration
   while recovery is required (D2 §“Recovery readiness and retained
   functions”), whereas current `SessionStore.get` may lazily migrate a legacy
   record (R1 lines 82-103, 223-270). A future Root-owned design must reconcile
   this seam before claiming retained list/get conformance.

## 5. Affected-client census and acceptance partition

| Client/surface | Accepted DEL classification/claim | App-local direction | Current declared runtime evidence | Acceptance absent / separately owned follow-on |
|---|---|---|---|---|
| Root CLI and generic-client path | `AFFECTED`; future exact equality, fail-closed, no-replay and machine-envelope conformance required (D1 §“Accepted census disposition”). | Not App-owned. | Generic `RuntimeClient` supports session CRUD/boot/replay/turn/interrupt over Unix socket, but no compatibility declaration appears (C5 lines 271-399, 491-540). Root CLI implementation is not in the declared evidence set. | Root implementation plus Root CLI/generic-client conformance/evidence acceptance. Exact CLI behavior/version support: `UNKNOWN`. |
| Chirality App | `AFFECTED`; future session/proxy/compatibility/presentation/interruption/evidence conformance required, under an App-owned gate (D1 §§“Accepted census disposition”, “Client conformance package partition”). | A1 recommends B1/V1/P1/X1/H1/R1 and strict replay-and-bind, but is explicitly `PROPOSAL REVISION 2 / AWAITING_RULING`; it creates no Root/runtime/resume effect (A1 lines 1-44, §4/R1, §13). | A1 reports current Pi descriptors `durableResume:false`, replay does not hydrate a fresh Pi session, and a Pi version authority conflict (`0.80.10` versus `0.82.0`) (A1 §2). These are evidence claims in an unaccepted proposal, not owner acceptance. | App ruling, App SCOPE_CHANGE after accepted Root semantics, App implementation/conformance tranche, exact Pi/version/profile acceptance. All remain absent. |
| PEC v2 | `UNRESOLVED`; no work, dependency, veto or classification created (D1 §§“Accepted census disposition”, “PEC v2 disposition”). | None established by A1. | No PEC runtime source is in the declared evidence set. | PEC-owned exact-operation or explicit no-effect ruling. Source currency and outcome: `UNKNOWN`. |
| Chirality Piping | `NOT_AFFECTED` on current evidence; no Root runtime implementation/migration obligation (D1 §§“Accepted census disposition”, “Piping disposition”; S0 §“Preserved unresolved and authority boundaries”). | None. | No Piping source is in the declared evidence set. | Reopen only on a later Piping-owned accepted instrument proving an exact obligation. No current work/dependency. |
| Tier-0 domain coordination | `NOT_AFFECTED` as a runtime-client obligation; relationship coordination is separate (D1 §“Accepted census disposition”). | A1 does not adopt a Tier-0 relationship. | No Tier-0 client source is in the declared evidence set. | Independent Tier-0 relationship act where applicable; current posture remains preparation/routing only (S0 §“Preserved unresolved and authority boundaries”). |

No generic cross-client matrix can substitute for the separate Root and App
ownership partitions. PEC evidence is forbidden absent a PEC ruling (D1
§“Client conformance package partition”; D3 §“Semantic conformance and
regression matrix”).

## 6. Conflict and non-coverage register

| ID | Conflict / non-coverage | Exact evidence | Treatment and separately owned follow-on |
|---|---|---|---|
| CN-01 | Exact Root compatibility epoch is unresolved and the complete binding manifest is unproduced. | S0 §“Preserved unresolved and authority boundaries”; D5 §§“Identity grammar”, “Compatibility binding record”; hashes S0/D5 above. | Hard hold. Accountable human supplies epoch; Root-owned later package produces and accepts complete manifest. No TM105 value inferred. |
| CN-02 | Embedded member status banners say candidate/not accepted, while the later acceptance snapshot binds the exact member bytes as human accepted. | D2/D5/D6 opening status lines; S0 §§“Accepted exact bytes”, “No implied downstream act”; hashes above. | Provenance/status-text tension, not byte drift. S0 is the later acceptance carrier; embedded no-effect/implementation holds remain. Do not rewrite accepted bytes. |
| CN-03 | Current event/session contracts lack `turn.recovery_indeterminate`, session `recovery_required`, and the four daemon recovery states. | C1 lines 15-16; C2 lines 1-15; D6 §§“Recovery terminal policy”, “Daemon recovery state machine”. | Root contract/source/evidence tranche required. No current compatibility conformance claim. |
| CN-04 | Current contract surfaces disagree about cancellation: `events.ts` omits `turn.cancelled`, while harness transcript and boot validation recognize it. | C2 lines 1-15; C4 lines 120-132; R3 lines 274-289. | Root contracts owner must reconcile event unions/schema loci before DEL terminal mapping. No winner inferred. |
| CN-05 | Current replay drops malformed lines from returned events while counting them; DEL requires byte-preservation/quarantine, no auto-repair/winner selection, and readiness hold. | R1 lines 156-207; D6 §“Malformed and contradictory evidence”. | Root storage/recovery implementation and adversarial evidence required. Existing behavior is not DEL conformance. |
| CN-06 | Current `get` can mutate by lazily migrating a legacy session, but DEL recovery-mode retained list/get diagnostics must not migrate or otherwise mutate. | R1 lines 82-103, 223-270; D2 §“Recovery readiness and retained functions”; T1 lines 39-75. | Root route/direct-entry census and recovery gating must resolve this exact seam. No implementation selected here. |
| CN-07 | Current acceptance attribution coverage is not proven: event attribution is optional and lacks explicit engine and local/remote classification. | C2 lines 29-36; D6 §§“Drain reconstruction”, “Acceptance-time attribution”. | Root event-contract/persistence design and corpus migration evidence required; missing legacy attribution remains blocker, not inferred data. |
| CN-08 | Current runtime/boot fingerprint, project manifest hash and optional residency epoch do not equal the DEL compatibility identity or complete binding manifest. | R3 lines 347-399; R2 lines 29-84; C1 line 14; D5 §§“Identity grammar”, “Compatibility binding record”. | Root must specify separately typed fields and canonical bindings; no digest/profile substitution. |
| CN-09 | Current client has no evidenced per-operation compatibility declaration or exact DEL mismatch handling. | C5 lines 93-180, 271-399; D5 §§“Declaration and comparison”, “Mismatch envelope”. | Root generic-client/CLI contract, implementation and conformance evidence gate. Old-version support remains `UNKNOWN`. |
| CN-10 | App proposes strict resume binding and a version target, but the packet awaits ruling and reports `durableResume:false` plus a `0.80.10`/`0.82.0` authority conflict. | A1 lines 1-44, §2, §4/V, §4/R, §13; hash A1 above. | App owner ruling and later App SCOPE_CHANGE/conformance, sequenced after Root semantics. No App acceptance or TM105 decision inferred. |
| CN-11 | DEL N3 evidence is design-complete but unexecuted; the declared tests cover legacy migration and model residency only, not the complete DEL matrix. | D3 §“Semantic conformance and regression matrix”; T1 lines 39-140; S0 §“Preserved unresolved and authority boundaries”. | Keep `N3=DESIGN_COMPLETE_NOT_EXECUTED`; future authorized Root/App evidence execution and acceptance. |
| CN-12 | Client versions, support/grace window, migration schedule, exact lifecycle commitments, HTTP/CLI mapping, old-reader coverage and acceptance are absent. | D1 §§“Client conformance package partition”, “No-effect boundary”; D3 §§“Cutover rollback and irreversible boundary”, “No-effect boundary”; S0 §“No implied downstream act”. | `UNKNOWN`. Separate Root/App owners and accountable-human cutover/lifecycle/release gates. |
| CN-13 | Declared evidence does not prove a complete current route/direct-entry readiness census or current recovery admission gate. | D2 §“Recovery readiness and retained functions”; D3 §“Semantic conformance and regression matrix”; R3 lines 181-405 and 430-495 only show selected service surfaces. | Root-owned exhaustive census/evidence remains required; no completeness inferred from the sealed subset. |

## 7. Authority and hold statement

DEL-02-06 scope was not widened. This return only crosswalks its accepted
stewardship/recovery/compatibility/degraded-mode/affected-client/evidence and
owner-decision semantics against the declared current surfaces. It does not
select or authorize any TM105 identity, lifetime, rollover, continuation,
digest/profile, support window, migration, backend, implementation, lifecycle,
release, reliance or byte-gate semantic.

The unresolved Root compatibility epoch, unproduced binding manifest, PEC
`UNRESOLVED`, App ownership, Piping `NOT_AFFECTED`, Tier-0 preparation/routing,
and `N3=DESIGN_COMPLETE_NOT_EXECUTED` boundaries remain intact. No source,
test, contract, client, register, receipt, notice, foreign-loop, Git or PR act
is authorized or performed. All TM105 semantic/implementation/lifecycle/
release/reliance/byte-gate holds remain intact.
