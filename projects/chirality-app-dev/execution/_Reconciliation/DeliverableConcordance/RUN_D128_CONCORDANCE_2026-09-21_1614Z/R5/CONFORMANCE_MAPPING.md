# P-08 retained Codex conformance conditions — R5 evidence map

Status: bounded TASK analysis for Agent 0 and the App manager; integration evidence, not a human acceptance, release decision, amendment, new test result or whole-suite equivalence ruling.

The P-08 alternatives are too coarse. D-GOV-43 items 11–12 preserve request/session correctness and a production-path spike while removing repeated execution for the same condition. The available evidence already demonstrates substantial current Codex behavior. A mandatory replay of the entire legacy evaluator is not established merely by its continued existence. Conversely, “S-1..S-8 PASS” does not prove every surviving condition. Use the condition map below, carry its precise residuals, and apply the parent Agent 0 determination in the governing R5 decision record.

## Assignment, provenance and actual execution

- Parent: `/root`, HELP_HUMAN / Agent 0. Executing native descendant: `/root/app_conformance_map`, TASK; actual mechanism `collaboration.spawn_agent`, not Chirality-managed `delegate_agent`. No descendants launched. App manager `/root/app_manager` notified of bounds and return.
- Engine: Codex; model inherited from the parent host configuration and not separately observable from this TASK's exposed runtime metadata. No substituted model was requested or observed. Do not infer a model from historical proof records.
- Read/write boundary: read the named decision, packet, frozen rows, current contracts/tests and qualification records; only write `R5/CONFORMANCE_MAPPING.md` and `.csv`. No source, governance, deliverable, R0–R4 or release record edits; no build or test execution.
- The native host exposes filesystem/shell access; scope and non-delegation here are instruction-enforced, not a claim of a hard per-child filesystem sandbox. Relevant instruction origins and SHA-256 are below. This task deliberately consulted no other full role body.
- Base: `379df923927d157be3ebb51d8a1dcf783d970112`. Historical test execution basis: `00115c71931bcae79909602d653740d3bb72dfa1` (D-APP-128 freeze).
- APP-HOLD reliance checks ran at the base with entry `Agent0/native-TASK/app_conformance_map`: first targets DEL-01-02, DEL-03-01, DEL-03-02, DEL-04-03, DEL-04-05, DEL-06-04, DEL-09-02, then DEL-04-01 (extension-ledger owner). Both exit 0, verdict ALLOW; each target CLEAR/NOT_HELD, no active holds. Register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan fingerprint `7bd56dd823f28427dd4bfb8ca65017b4fe9c0b8165fb32a702f896e49f8ba6ec`. No dispatch, dependency acceptance or lifecycle promotion occurred.

## Evidence interpretation

`RT` paths are relative to `projects/chirality-runtime/tests/`; `APP` paths to `projects/chirality-app-dev/frontend/src/__tests__/`. Line numbers identify the current unchanged test bytes at the base. A named test asserts only its described condition. Tests using fake Codex transport/supervisor are integration or fixture evidence, not execution of stock Codex.

The historical Runtime gate reports build/typecheck success and 42 files / 407 passing tests; the App gate reports typecheck success and 222 passing files + one skipped / 2,285 passing tests + four skipped. These are preserved reports, not fresh execution. The selected named cases have no skip markers. Whole-workspace source equality was checked with:

```sh
git diff --name-only 00115c71931bcae79909602d653740d3bb72dfa1 379df923927d157be3ebb51d8a1dcf783d970112 -- projects/chirality-runtime projects/chirality-app-dev/frontend
```

Exit 0, empty output: no tracked differences in either source workspace between those revisions. The individual test hashes below independently bind the inspected bytes to both revisions. This supports carrying forward recorded results for these unchanged conditions, without turning broad suite totals into stronger per-condition proof.

The separate real-source spike evidence is dated 2026-09-12 and names session/turn IDs, observations and intervening fixes. It reports S-1..S-8 PASS, but explicitly limits S-5: the full-history child received WORKING_ITEMS and the assignment said TASK; the TASK role body was **not supplied**. That label is not proof of intended TASK role injection. Later fixture tests demonstrate role-file construction, not a replacement real-child witness.

## Stable conditions and their checks

### C01 — Stable session, turn and engine attribution; selected capabilities and model are explicit

- Check/source: `RT delegated-runtime.test.ts:99,252,264; RT app-owned-composition.test.ts:59; RT codex-attachment-adapter.test.ts:125`.
- What it demonstrates: Codex-shaped envelope uses registered cwd/session/turn; committed terminal carries adapter/provider/model/effort; unknown model/effort rejected before dispatch; composition selects Codex and checks session:init precedes chat:delta.
- Existing execution evidence: RT gate (scripted Codex supervisor/transport); source S-2 for real turns.
- Residual/limit: Full legacy descriptor-boolean and duplicate session:init anomaly matrix is not demonstrated for Codex by these cases. Lift exact init-first mechanics to correct identity before dependent output; do not mark every old issue code tested.

### C02 — Accepted input and terminal are durably recorded; replay distinguishes completion, failure and interruption

- Check/source: `RT delegated-runtime.test.ts:99,150; RT app-owned-composition.test.ts:204,223; RT turn-hardening.test.ts:460`.
- What it demonstrates: Delegated retirement record stores the exact committed terminal; App composition replays shutdown terminal by eventId; startup recovery records interruption and accepts continuation; generic shared TurnCoordinator records accepted input before preflight failure.
- Existing execution evidence: RT gate; source S-2 records 158 persisted events and 0 malformed.
- Residual/limit: The accepted-before-failure test uses a scripted Pi descriptor on shared TurnCoordinator, not stock Codex. Source S-2 does not demonstrate crash-atomic recording at every boundary; no such expanded claim is closed here.

### C03 — Failure, interruption and success have truthful terminal outcomes; concurrent/late activity cannot create a false second completion

- Check/source: `RT delegated-runtime.test.ts:191-229; RT app-owned-composition.test.ts:189,204,250; RT turn-registry.test.ts:130,210`.
- What it demonstrates: Interrupt-first and completion-first races settle once; shutdown yields one interrupted terminal; app-server death yields turn.failed and process exit 1; active second start is rejected; mid-stream failure closes subscribers.
- Existing execution evidence: RT gate; source S-7 demonstrates real interrupted terminal and follow-up.
- Residual/limit: Scripted race coverage is sufficient evidence of those named conditions, not proof of every possible provider ordering. Legacy suite exact process:exit vocabulary is an implementation detail, not independent authority.

### C04 — Tool activity and approval outcomes retain identifiers and truthful pairing

- Check/source: `RT app-owned-composition.test.ts:59; RT native-event-adapter.test.ts:22,43; APP lib/harness-event-views-codex.test.ts:58,85`.
- What it demonstrates: Same command item links ask/deny/tool.failed; raw collaboration/activity identifiers survive; parent completion does not fabricate child completion; UI joins tool start/completion using toolUseId.
- Existing execution evidence: RT and APP gates; source S-7 denied command; source disconnect witness records one start/one completion and no duplicate execution.
- Residual/limit: No Codex-specific negative matrix for missing start, orphan result or permission-after-result was found in these maintained tests. Preserve raw evidence rather than inventing legacy tool pairing; if the retained condition requires detecting these anomalies, add bounded cases at the projection boundary.

### C05 — Every server request receives its matching answer, explicit unsupported outcome or cancellation; denied approval remains denial

- Check/source: `RT codex-app-server-client.test.ts:8,29,43; RT codex-supervisor.test.ts:113,151; RT delegated-runtime.test.ts:131; RT app-owned-composition.test.ts:59; APP lib/harness-event-views-codex.test.ts:26,47,58`.
- What it demonstrates: JSON-RPC correlation; pending requests fail on child exit; unanswered client request times out without breaking transport; approvals/input/elicitation/unknown request kinds resolve; duplicate answers reject; pending requests cancel at turn end; denied command is persisted and rendered.
- Existing execution evidence: RT and APP gates; source S-7 demonstrates denial through the live App route and absent target file.
- Residual/limit: Dynamic-tool refusal fixture covers the unregistered-tool condition only. Current registered tools have separate codex-application-tools.test.ts coverage; neither fixture qualifies native child tool inheritance.

### C06 — Explicit Stop interrupts once and leaves a resumable session; observer disconnect does not stop work

- Check/source: `RT codex-supervisor.test.ts:169,195; RT delegated-runtime.test.ts:150,172,191; RT turn-registry.test.ts:179; APP lib/runtime-daemon-harness-port.test.ts:301`.
- What it demonstrates: Stop waits for turn ID during turn/start race; generation checks reject stale operations; cancellation is latched before acquisition; disconnect unsubscribes; explicit interruption routes separately.
- Existing execution evidence: RT and APP gates; source S-7 and renderer-disconnect witness.
- Residual/limit: No blanket rerun needed merely to map these unchanged tests. Packaged/native outcome remains C15, separate from source and fixture evidence.

### C07 — Same chat can continue after host restart with durable provider thread linkage

- Check/source: `RT codex-supervisor.test.ts:96; RT app-owned-composition.test.ts:223; RT delegated-runtime.test.ts:99`.
- What it demonstrates: Unknown thread is resumed after host restart; persisted running state is settled interrupted; next turn resumes/starts appropriately; delegated follow-up carries durable thread ID.
- Existing execution evidence: RT gate; source S-6 reports three quit/relaunches and correct prior-chat recall.
- Residual/limit: Composition test explicitly simulates stale persisted state, not actual SIGKILL. Source S-6 does not close packaged S-6 or prove every later candidate; use affected-condition rule.

### C08 — SSE replay preserves order and reconnect does not repeat execution

- Check/source: `RT turn-registry.test.ts:91,130,179,210,252; APP lib/harness-client-turn-registry.test.ts:20,31,56; APP lib/runtime-daemon-harness-port.test.ts:358`.
- What it demonstrates: Frames numbered/replayed after sequence; active turn exclusion; cancellation only unsubscribes; typed not-active response; stale retained turn cannot masquerade as new start.
- Existing execution evidence: RT and APP gates; source transport and owner window reload witness resumed from seq 22 after seq 21, one execution.
- Residual/limit: Source-run owner window witness is strong evidence for that condition at that source run. It is not a stapled-bundle witness.

### C09 — Upstream names, IDs and payloads remain available with usable normalized views; unfamiliar notifications remain inspectable

- Check/source: `RT codex-supervisor.test.ts:55; RT native-event-adapter.test.ts:22,43; APP lib/harness-event-views-codex.test.ts:74,85`.
- What it demonstrates: Notification method order retained; native params equality asserted; child and primary identities distinguished; raw reasoning/usage notifications remain inspectable; normalized tool summaries coexist.
- Existing execution evidence: RT and APP gates; source S-2/S-5 evidence records real Codex event activity.
- Residual/limit: P-05 governs carrier repair. UNKNOWN_UI_EVENT and provider-name exclusion from the legacy evaluator must not be transplanted as obligations contrary to D-GOV-43 event preservation. This does not narrow the retained audit requirement.

### C10 — Credentials stay in Chirality effective Codex home and private data does not leak to durable evidence or diagnostic channels

- Check/source: `RT codex-effective-home.test.ts:34,51,74,87; RT codex-app-server-client.test.ts:51; RT app-owned-composition.test.ts:59,263; APP lib/redaction-path-matrix.test.ts`.
- What it demonstrates: Effective-home overlay excludes auth and cache entries; stale auth symlinks removed; diagnostic email redaction; account status/logs lack email; sign-out invokes account/logout. App redaction matrix covers legacy Claude hook/persistence/UI channels only.
- Existing execution evidence: RT gate for current Codex custody/diagnostics; APP gate for legacy matrix only; source S-8 demonstrates own auth-file removal and other client unchanged by metadata/process observations.
- Residual/limit: Codex-specific sentinel test across raw notification/request/error payload, durable event replay and renderer not established by this evidence. Legacy API-key redaction pass is not Codex OAuth/event-channel proof. Retain K-KEY-1 and route narrowly scoped coverage review; no credential inspection was performed here.

### C11 — User-selected approval/sandbox policy and native configuration reach Codex without silently reinstating Chirality policy overrides

- Check/source: `RT codex-supervisor.test.ts:55; RT delegated-runtime.test.ts:99; RT codex-effective-home.test.ts:34; RT app-owned-composition.test.ts:59`.
- What it demonstrates: Native config overlay retained; thread/start and turn/start carry selected policy; registered project cwd is used; real S-7 is governed by Codex chosen workspace-write/on-request policy.
- Existing execution evidence: RT gate; source S-7.
- Residual/limit: Do not convert DEL-06-04 legacy hook, hard-deny, exact-edit or instruction-root veto tests into mandatory Codex supplier tests. Stock sandbox enforcement outside the witnessed denial is not established by these fixtures; retain declared host policy and actual enforcement limits.

### C12 — Server-resolved attachment identity, containment, size/type checks and separate untrusted input survive the adapter boundary

- Check/source: `RT codex-attachment-adapter.test.ts:41,64,84,125,135; RT app-owned-composition.test.ts:116,163; APP integration/v3-runtime-proxy.integration.test.ts:49`.
- What it demonstrates: Adapter maps documents/images separately from trusted instructions; rejects unsupported/escaping/symlinked/oversize inputs before dispatch; native selection custody; trusted project/model checks.
- Existing execution evidence: RT and APP gates (controlled adapter/transport).
- Residual/limit: This is attachment validation, not proof of general native tool filesystem containment or every real-provider attachment format.

### C13 — Workflow reuse and changed role/common instructions preserve supplied history and apply only at a verified idle boundary

- Check/source: `RT app-owned-composition.test.ts:315,335,380,441,467; RT codex-supervisor.test.ts:252,282,308,332,369,385,394,406`.
- What it demonstrates: Cold resume/injection order; prior basis bytes retained; active primary/child defers; unknown acknowledgment blocks new turn; each configured native role file contains its intended full role and excludes other role bodies.
- Existing execution evidence: RT gate; source S-3 and S-4 demonstrate save/reuse/change (S-4 after fix). Source S-5 is only partial for intended-role receipt.
- Residual/limit: Original S-5 PASS label is qualified by its own note: full-history child inherited WORKING_ITEMS, TASK assignment named in brief but TASK body not supplied. Current role-file fixtures do not prove a fresh real child received that body. Retrieve later native witness or retain that precise S-5 residual; do not relabel historical outcome.

### C14 — Native Plan Mode supports discussion and recorded revision; native compaction/activity is preserved when supplied

- Check/source: `RT codex-supervisor.test.ts:55,218; RT native-event-adapter.test.ts:22; APP lib/harness-event-views-codex.test.ts:74`.
- What it demonstrates: Plan collaboration mode and plan/clarification items captured; plan revisions and native notification payloads preserved.
- Existing execution evidence: RT and APP gates; source S-1 reports plan revision 1 then revision 2.
- Residual/limit: No compaction-specific Codex case or real compaction witness was found in the selected maintained tests/spike. Generic passthrough supports preservation but does not prove compaction occurrence or legacy compaction start/result pairing. Determine a distinct applicable condition before adding a targeted check.

### C15 — Qualification evidence names source/candidate and preserves distinct packaged/native conditions

- Check/source: `spike/EVIDENCE.md; BUILD_EVIDENCE_20260912.md; NATIVE_CHECKLIST.md; R3/OWNER_CHECK_APPLIED.md OC-06/07/14`.
- What it demonstrates: Source S-1..S-8 plus disconnect recorded; signed candidate 388de6973 has signature, pin, dependency/instruction integrity results. Owner confirms post-A2 Section 8 and full Section 9 runs happened (OC-06/07).
- Existing execution evidence: Historical executed records, not this TASK execution. OC-14 says do not know about packaged S-6/S-8/disconnect.
- Residual/limit: Packaged outcomes cannot be inferred from source pass or signed build. Locate kept native result/summary where possible; otherwise carry unknown outcome by exact candidate. Lack of a record does not mean the event never happened; no release or lifecycle acceptance is made here.

## S-1..S-8 crosswalk

| Spike item | Existing historical record | Condition mapping and limit |
|---|---|---|
| S-1 | Source native-plan session a86fdf49, revision 1 then revision 2 | C14; concrete source witness. |
| S-2 | Source session 5517a692, file reads, 39.9 s silent tool, 158 events / 0 malformed | C02/C08/C09; no stream-silence failure; does not prove all fault cases. |
| S-3 | Source session 30f2b92c wrote and discovered project workflow | C13; concrete source witness. |
| S-4 | Source session d4015835 reused/revised workflow after Runtime fix and App restart | C13; result bound to after-fix run, not failed earlier attempt. |
| S-5 | Source session 96ce0a33 / child 01a09630-2b92; real native delegation | C09/C13; TASK body absent, WORKING_ITEMS inherited. Intended role receipt remains unproved by this record. |
| S-6 | Source quit/relaunch continuation of sessions 5517a692 and d4015835 | C07/C15; packaged/native result unknown in the scoped evidence. |
| S-7 | Source a692d792 denied approval and interrupted sleep; subsequent turn succeeded | C03–C06/C11; actual denied command did not create target file. |
| S-8 | Source App-home sign-out, ambient credential metadata and other client process unchanged | C10/C15; packaged/native result unknown in the scoped evidence. |
| Disconnect | Source transport reconnect and owner Cmd+R window witness, one tool execution | C06/C08/C15; source witness, not stapled candidate result. |

`BUILD_EVIDENCE_20260912.md` binds signature/pin checks to source `388de6973c32730d130b4084fd78996391899e06`, Codex `0.154.0`, product `3.0.0-rc.1`. It explicitly leaves packaged S-6/S-8/disconnect to native verification. R3 owner check OC-14 is “don't know”; no absence-of-event assertion is warranted. OC-06 and OC-07 confirm later Section 8 and Section 9 execution happened, but this does not identify a Codex legacy-evaluator invocation or supply per-condition results.

## Frozen P-08 claim-key crosswalk

The companion CSV preserves all 24 PRIMARY and eight ALSO rows from the frozen packet index, their original R3 dispositions/declared states, and the condition mapping. R3 and R4 remain unchanged. Multiple rows may share one condition/check; do not demand repeat executions for duplicate wording. No row is automatically set ALIGNED merely because it references this map.

| Claim key | Role | Conditions | R5 treatment basis |
|---|---|---|---|
| `DEL-01-02#CLM-006.1` | ALSO | C09 | P-05 carrier governs event semantics; current suite absence is not independent of that supersession. |
| `DEL-01-02#CLM-006.13` | PRIMARY | C01-C15 | Fallback availability is a governed response if a product-critical boundary fails; this map does not require shipping a second engine. |
| `DEL-01-02#CLM-018.4` | ALSO | C09,C10,C11 | Preserve current Codex event/policy/custody conditions; legacy architecture changes are handled by P-05/P-09. |
| `DEL-03-01#CLM-003.8` | PRIMARY | C01-C15 | Map stable issue families; use explicit residuals instead of claiming evaluator equivalence. |
| `DEL-03-01#CLM-003.9` | PRIMARY | C01-C15 | Prior-to-default qualification purpose survives; existing condition evidence plus explicit residuals is the warranted disposition basis. This mapping does not assert whole-suite equivalence or retrospectively manufacture a pre-default pass. |
| `DEL-03-01#CLM-005.4` | PRIMARY | C01-C15 | Prior-to-default qualification purpose survives; existing condition evidence plus explicit residuals is the warranted disposition basis. This mapping does not assert whole-suite equivalence or retrospectively manufacture a pre-default pass. |
| `DEL-03-01#CLM-009.8` | PRIMARY | C01-C15 | Prior-to-default qualification purpose survives; existing condition evidence plus explicit residuals is the warranted disposition basis. This mapping does not assert whole-suite equivalence or retrospectively manufacture a pre-default pass. |
| `DEL-03-01#CLM-009.10` | PRIMARY | C02-C12 | Concrete retained behavioral coverage exists; C04/C10 gaps remain bounded. |
| `DEL-03-01#CLM-009.13` | ALSO | C09 | Provider-name exclusion conflicts with adopted upstream event preservation; P-05 supplies carrier disposition. |
| `DEL-03-01#CLM-011.3` | PRIMARY | C01-C15 | Prior-to-default qualification purpose survives; existing condition evidence plus explicit residuals is the warranted disposition basis. This mapping does not assert whole-suite equivalence or retrospectively manufacture a pre-default pass. |
| `DEL-03-01#CLM-012` | PRIMARY | C01-C15 | This map supplies a Codex evidence index; source contract/TBD carrier repair remains R5 integration work. |
| `DEL-03-01#CLM-013.2` | ALSO | C09,C01-C15 | Split upstream semantics carrier from qualification proof; no automatic whole-suite pass. |
| `DEL-03-01#CLM-018.4` | PRIMARY | C01-C15 | Prior-to-default qualification purpose survives; existing condition evidence plus explicit residuals is the warranted disposition basis. This mapping does not assert whole-suite equivalence or retrospectively manufacture a pre-default pass. |
| `DEL-03-01#CLM-019.1` | PRIMARY | C01-C15 | This is a condition-level evidence/blocked matrix, not a new Codex pass report. |
| `DEL-03-01#CLM-019.2` | PRIMARY | C01-C15 | Retained checks map individually; failures/residuals are not dissolved by fixture totals. |
| `DEL-03-01#CLM-022.2` | PRIMARY | C01-C15 | Prior-to-default qualification purpose survives; existing condition evidence plus explicit residuals is the warranted disposition basis. This mapping does not assert whole-suite equivalence or retrospectively manufacture a pre-default pass. |
| `DEL-03-01#REM-2` | PRIMARY | C05-C09 | Live service/socket and App client evidence establish readiness to assess this item; return contract is not silently declared complete. |
| `DEL-03-02#CLM-009.2` | PRIMARY | C01-C09 | Restate present adapter/service boundary; do not retain IAgentSdkManager/TurnEngine naming as requirement. |
| `DEL-04-03#CLM-004.6` | PRIMARY | C01-C15 | Prior-to-default qualification purpose survives; existing condition evidence plus explicit residuals is the warranted disposition basis. This mapping does not assert whole-suite equivalence or retrospectively manufacture a pre-default pass. |
| `DEL-04-05#CLM-004` | PRIMARY | C10,C11,C15 | Native shared Codex config replaces settingSources isolation premise; keep private authentication and exact-candidate checks. |
| `DEL-06-04#CLM-009.15` | PRIMARY | C11,C12 | Separate native policy from attachment containment; historic hooks do not prove general Codex tool containment. |
| `DEL-06-04#CLM-011` | PRIMARY | C11,C12 | Do not port retired hook machinery; policy and attachment checks retain their own limited claims. |
| `DEL-06-04#CLM-019.1` | PRIMARY | C11,C12 | As above; no fabricated Codex hook/exact-edit verification. |
| `DEL-09-02#CLM-010.2` | PRIMARY | C01-C15 | Use current condition matrix plus existing execution transcripts; Section 9 marker completion not inferred. |
| `SOW:SOW-018.2` | PRIMARY | C01,C05-C09 | First Claude/daemon adapter premise superseded; ownership/carrier handling remains P-04/P-09/P-21. |
| `SOW:SOW-037` | PRIMARY | C01-C15 | Current client/adapter checks replace a blind rerun recommendation; residual conditions remain explicit. |
| `SOW:SOW-044.2` | ALSO | C09,C01-C15 | Current event mapping demonstrated, exact legacy evaluator run absent; preserve distinction. |
| `DOC:RELIANCE#3.1` | ALSO | C09 | Re-anchor current Runtime adapter/supervisor and raw notification views; P-05 governs. |
| `DOC:RELIANCE#3.14` | PRIMARY | C01-C15 | Lift historical Anthropic fallback premise; maintain justified fallback response if retained condition fails. |
| `DOC:RELIANCE#4.1` | ALSO | C09 | Same RB-ENGINE condition; no duplicate test execution. |
| `DOC:RELIANCE#4.14` | PRIMARY | C01-C15 | Same RB-FALLBACK condition; no duplicate proof requirement. |
| `DOC:RUNTIME_ENGINE_CONTRACT#9` | ALSO | C01-C15 | Conformance gates become retained condition references; moved evaluator and Claude-only premise are carrier repair. |

## Bounded next actions for integration

1. Apply the Agent 0 reading: retain current request/session guarantees and map them to current checks; carrier repair should not reintroduce retired translation, SDK setting isolation, per-user daemon, supplier admission or hook machinery.
2. Keep the concrete residuals visible: C10 Codex secret-channel coverage, C13 actual intended-role witness, C15 packaged outcome records. C01/C04/C14 identify narrower anomaly/compaction coverage limits, not proven defects or blanket grounds to rerun the whole legacy suite. Resolve which are distinct required conditions before any engineering test work.
3. Do not use generic fixture or spike totals as proof of no unknown conditions. No complete K-ENGINE-2 qualification finding, acceptance state, lifecycle transition or new owner ruling is created by this analysis.
4. If more evidence exists, retrieve and bind the actual witness before rerunning. If a bounded check is needed, run once for the condition and candidate; repeat only for an affected source/configuration/packaging change under the adopted minimum-not-ceiling clarification.

## Source and instruction manifest

All paths below are repository-relative. SHA-256 hashes bind actual inspected files at this TASK return. `same` in the last column means an exact `git show <frozen>:<path>` byte comparison matched the base file, not a claim that the historical run covered every assertion.

| Source path | SHA-256 | Test bytes equal frozen basis |
|---|---|---|
| `AGENTS.md` | `d151dad92a074abebf8e6225c92c4c6e88fd586f2283377b50b5051eff39be7b` | n/a |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` | n/a |
| `projects/chirality-app-dev/AGENTS.md` | `5d65cce235a8d6f656a858e7f3836e1cbd4229a9567f215c3448353d23ae405c` | n/a |
| `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` | `08bef1e22715b4962e365ec3dce8a0cd66a212ea79cdc21a33ffa818f05f5899` | n/a |
| `docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/D-GOV-43.proposed.md` | `5afadb4ac0d33c26d188abbd86508de31dd08a027bd7858005273a11eab784cc` | n/a |
| `projects/chirality-app-dev/docs/CONTRACT.md` | `57411f8df49e6316d8d3bc9674d698b1c8478e639aad331115d4f67bcca97363` | n/a |
| `projects/chirality-app-dev/frontend/docs/harness/runtime_engine_contract.md` | `91a74ab8d949b24b5d38dff16cd1d01cbf44a64c80b113e6007cdddcfbe5650e` | n/a |
| `projects/chirality-runtime/packages/contracts/src/harness/engine-conformance.ts` | `53c140a7ffa490e749faac8131ed8bf24b0f18d1392ac5931258a7b3f7d40427` | n/a |
| `projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts` | `6c188da4308672207bda088a1b0858194cc6b4029f10fa993c28ecf09616d513` | n/a |
| `projects/chirality-runtime/tests/codex-app-server-client.test.ts` | `15023ea58b4b517d432d51859f6c13e030501537bd9d643020a2c2a273a8ed54` | same |
| `projects/chirality-runtime/tests/codex-supervisor.test.ts` | `4915153f4bc4f1f51ed400d266d0b058f2c6707b696ecf6bc9e340ae9f4a6dff` | same |
| `projects/chirality-runtime/tests/native-event-adapter.test.ts` | `49a6859b17dc816dadc03acdb72a11c7a4b206442b8d80bc19339294b15b5d2d` | same |
| `projects/chirality-runtime/tests/delegated-runtime.test.ts` | `4e1a5a09960ecf524f46d58dbda1296dbcd7b83d21ef54f5bdf52818c37780c1` | same |
| `projects/chirality-runtime/tests/app-owned-composition.test.ts` | `0d905fb5e1c0f35fc58e0eaad237c569774e0f5b72b784dc4aa3975d4d43938c` | same |
| `projects/chirality-runtime/tests/codex-effective-home.test.ts` | `74bfa35291898e9ebf2a766d8e728f59c97c86ce6dd1b11fa96cb1ee9394ee95` | same |
| `projects/chirality-runtime/tests/codex-attachment-adapter.test.ts` | `04a5fa5731bf61744321efcf06ad55e7d27a3e9ac3a6a8ceeae0f4d0ae7648d6` | same |
| `projects/chirality-runtime/tests/turn-registry.test.ts` | `2aeeb38535a50d9a5b487c97bed695e7e0731985e3ef7524b2f440041de7ddcc` | same |
| `projects/chirality-runtime/tests/turn-hardening.test.ts` | `f195b6c9231df785064afc4f0f35d294dccee5ba48f31d484dbd79b88d8be01b` | same |
| `projects/chirality-runtime/tests/codex-application-tools.test.ts` | `01a64d3d8e3e5a06f7d1bd214e205bcdecdb507d63d8115681d997ccc5361798` | same |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts` | `65252b9b8be980e4ec17c71a1ce54469a39309c8772b4c2c1c059c4d1b6a57c4` | same |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-client-turn-registry.test.ts` | `9cbe8f67e6416dc9004480caed26115adb776d126775246ca994860c805eefc7` | same |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-event-views-codex.test.ts` | `f17a466ffe1e712e55e788d42501dae30a9012ede625c13120c0807603e344da` | same |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/redaction-path-matrix.test.ts` | `cb386af8beda2b0158734b2f63e7faad4cd29321761058dff274c19a162295d5` | same |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/engine-conformance.test.ts` | `06e50ab168b26a980af0e16e05258d351af965d86ecb2fea997140ba903dda1b` | same |
| `projects/chirality-app-dev/frontend/src/__tests__/integration/v3-runtime-proxy.integration.test.ts` | `a35dea23c83a60944e564a77b86548fe369a754e300cbe6e70b821d4a75af3a9` | same |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/spike/EVIDENCE.md` | `dd50955d7256db77e9307fd2540c00c4568bd5bf6f2aa60e11aa7fc8abd58bf2` | n/a |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md` | `748ec1a995f79d8d9ed3d6f34dc63b51a9d19afd3ff5d77d2b7ef9fc0839369a` | n/a |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md` | `8348fc03be91537c4df985984fba63622d423d4eeda1e72b6d803e5e97b738b7` | n/a |
| `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R3/CLAIM_CONCORDANCE.csv` | `a6f6cdda685173cac3aa8ab75d8dd823143feadbde2c44a755571337936dd852` | n/a |
| `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R3/EXTENSION_CONCORDANCE.csv` | `eeaaf27fcba05f2b8a16c6429a95be220b071c2b8938c41a3d5ff959854dbb37` | n/a |
| `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R3/OWNER_CHECK_APPLIED.md` | `ddc4f16dcffcb048903d773e8880a2ad2bf904b90472ef8212808518db38aaa2` | n/a |
| `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R4/PACKET_INDEX.csv` | `b17789eb6c6775a36c4ad986e0d423eff4b6218a6e1deea00cd8e696cd399457` | n/a |
| `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R4/PACKETS/P-08_codex-engine-conformance-obligation.md` | `a3ddd93c40212bb799e2d4ddcb3db362aa9928710af4b6e9323c4fc4bc7cd7d6` | n/a |
| `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_APP_00115c719.md` | `5ce79b28230f81e5d44c47870231984a821af32931de589b99e4625e0d652e6f` | n/a |
| `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_RUNTIME_00115c719.md` | `1b57b42494fc883766264da98d0e4ba5fb6f52022b483afb341181f8dde18c83` | n/a |

TASK completion check: 32 unique packet keys; 24 PRIMARY + 8 ALSO; every key found in the frozen R3 ledgers; all mapped condition IDs defined; no new test execution claimed. The CSV is a generated crosswalk from those frozen inputs.
