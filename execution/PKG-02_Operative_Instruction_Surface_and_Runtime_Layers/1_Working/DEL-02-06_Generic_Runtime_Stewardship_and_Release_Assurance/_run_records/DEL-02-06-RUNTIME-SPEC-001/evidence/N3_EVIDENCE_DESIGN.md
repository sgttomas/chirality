# N3 recovery evidence design

RunID: `DEL-02-06-RUNTIME-SPEC-001`
Node: `N3`
Status: `DESIGN_COMPLETE_NOT_EXECUTED`
Verdict: `ACCEPT_FOR_N4`
Date: `2026-08-03`

## Boundary and interpretation

This is a candidate evidence design for `TM-ROOT-108`. It executes no runtime,
test, replay, implementation, cutover, rollback, Git, lifecycle, release, or
reliance act. `PENDING` in an artifact or hash cell means that a later,
separately authorized implementation/check tranche must create and hash the
artifact. `DESIGNED_NOT_EXECUTED` is not a passing runtime result.

The matrices do not choose the recovery terminal type, retry/resume posture,
audit payload or redaction, transaction boundary, drain reconstruction rule,
or retained endpoint set. Those choices remain human-gated in section 8.

## 1. Accepted source coverage

| SourceRef | SHA-256 | N3 use |
|---|---|---|
| `ScopeOfWork.md` | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` | REQ-010 through REQ-016, REQ-022, REQ-026, REQ-033 through REQ-039, REQ-044 through REQ-052; AC-006/007/010/011/012/014/015; VER-006/008/009/011/012/013; TBD-006/008/009/014/016. |
| `execution/_Coordination/_TaskManagement/DEL-02-06_HANDOFF_TM-ROOT-108_2026-08-02.md` | `da191f8c12207398c676531daf8941148797dc4f206c33ad58797a1e74a77fbc` | Exact restart-reconciliation concern and closure-evidence contract. |
| `execution/_Coordination/NOTICE_D-APP-85_C06_DAEMON_RECOVERY_ROOT_ROUTE_2026-08-02.md` | `0b34cefdc9abd5927db1b6bdda07225c37c42806ff5b3f946bb182227f08dc41` | Verified contradiction and inspected source locus. |
| `READ_SCOPE_AMENDMENT_1.md` | `01320cbe83e72fbcf7861bb30651654904764d27f3200b56ff4e118764331206` | Authorizes the eleven recovery-relevant static reads listed below. |
| `basis/N0_R2_RETURN.md` | `ca8c1b18f6bd3d32ab7f1bad5d0cdc15d3bd31c811d3a2484ed38f61c64ac522` | Accepted prerequisite verdict and planning-input boundary. |
| `basis/BASIS_REPORT_R2.json` | `e11d4c2888d9d449e463c85ef5b06dad138b8eca7b9da00b123e51a346c97cd8` | Machine-readable N0 checks, exact packet hashes, and manager-fan-in prerequisite. |
| `briefs/N3.md` | `c4d97e2ad8998c67efd407aad2e2a470997159dc538ee0f46f48cf1055a21b7e` | Governing objective, tools, outputs, criteria, and exclusions. |
| `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/instances/W6-DEL0206-POST-N0-PLANNING/children/N3/LAUNCH_BRIEF.md` | `ea8c8a3a283fa4d5ea4f28bd91180fa8c61fb785451fc49b70fe9d0a453266a7` | Sealed child identity, read/write containment, and hard stop. |
| `runtime/packages/contracts/src/events.ts` | `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` | Runtime terminal vocabulary and attribution shape. |
| `runtime/packages/contracts/src/harness/event-schema.ts` | `8c6d17f0547f9433d9a2b0892ba50c266b08918142e39984ecc0a7d479661a2f` | Harness terminal vocabulary, including `turn.cancelled`. |
| `runtime/packages/core/src/turn-coordinator.ts` | `992d501b49629b88cb72e42ad2c54d7934859da7e3a822259c68151e3ab3715b` | `turn.accepted` persistence, in-process active lock, residency admission/release, and terminal paths. |
| `runtime/packages/core/src/agent1-run-coordinator.ts` | `d0e8483df38d837a52c371b1a150a766046de44d17f0da66e5fd34c1415d27e7` | Governed Agent 1 accepted-to-terminal window and memory-only active map. |
| `runtime/packages/core/src/session-store.ts` | `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` | JSONL append, event-id-only deduplication, replay, malformed-line counting/skipping, and session status. |
| `runtime/packages/core/src/runtime-service.ts` | `43b2dd4dbf8b1a91a057350558229616e34bfec258b2b9ad8f5e36c058c7c74d` | Session boot, turn and Agent 1 admission, model/session access, and missing recovery gate. |
| `runtime/packages/core/src/residency-coordinator.ts` | `9b37829aaa97cdf0f4e3ed6fde9135a57bf0b33a345b3b5cc8f7e6d4175dc327` | Memory-only `activeTurns`, drain, activation, residency persistence, and evidence. |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46` | Startup order, socket admission, model activation route, turn/run routes, and replay route. |
| `runtime/tests/daemon.test.ts` | `bbcfcabb48dd7c4b5c5e0645b14601efd89404e34a5cdde322a0bef5b22a693e` | Existing daemon, disconnect, and canonical terminal fixtures; no restart reconciliation fixture. |
| `runtime/tests/turn-hardening.test.ts` | `e5880870ef7ee94b90ebef4baf72335bf24073ca35b1d829ead05c3be9ee7b2b` | Existing terminal, malformed engine behavior, session-lock, and boot-validation fixtures. |
| `runtime/tests/session-and-residency.test.ts` | `5d9c1cda16267557ea8ca599109568718fcb7a22b3dcb8f58a67f760fa596b02` | Existing drain and residency drift fixtures; drain is only proven within one process. |

All eleven paths admitted by `READ_SCOPE_AMENDMENT_1.md` are represented.

## 2. Requirement-to-evidence matrix

| Requirement | Condition | Positive evidence | Negative/adversarial evidence | Owner | Accepted basis | Artifact SHA-256 | Result | Gate |
|---|---|---|---|---|---|---|---|---|
| N3-R01 / TM-ROOT-108.1 | Before request admission or model activation, enumerate every persisted `turn.accepted` with no terminal in all registered central sessions, including normal and governed Agent 1 turns. | Inventory fixture with clean, terminal, and orphan turns; reconciliation report lists only exact orphans with project/session/turn/event identities. | Omit one project; include already terminal turn; duplicate accepted IDs; deleted/legacy/missing session. | Root runtime implementation owner | TM-ROOT-108; REQ-026/033/038 | `PENDING:N3-R01` | `DESIGNED_NOT_EXECUTED` | Exact Root implementation and check authorization. |
| N3-R02 / TM-ROOT-108.2 | Reconciliation is idempotent for one orphan and for a multi-session batch. | First pass records one ruled outcome per orphan; second and third pass produce zero new terminals and an unchanged canonical digest. | Crash after each recovery write; rerun with same and reordered inventory; concurrent second reconciler. | Root runtime implementation owner | REQ-012/026/033/034 | `PENDING:N3-R02` | `DESIGNED_NOT_EXECUTED` | Human ruling D1/D4, then implementation/check gate. |
| N3-R03 / TM-ROOT-108.3 | Reconciliation completes before daemon admission and before any model activation or local-turn admission. | Timestamped/latch evidence proves recovery terminal persistence and audit completion precede socket readiness and residency activation/admission. | Race requests at each startup boundary; direct service calls; model activate during recovery; recovery failure. All consequential paths remain closed. | Root daemon + runtime service owners | REQ-010/011/022/026/044 | `PENDING:N3-R03` | `DESIGNED_NOT_EXECUTED` | Human ruling D6, then implementation/check gate. |
| N3-R04 / exactly-one terminal | Each accepted `turnId` has exactly one member of the human-ruled terminal set; multiple or conflicting terminals fail closed. | Corpus query proves cardinality 1 after normal completion, interruption, failure, and recovery. | Duplicate same terminal, conflicting terminals, terminal without accepted, accepted after terminal, foreign session/turn attribution. | Root contracts + session-store owners | REQ-026/033; AC-006/012 | `PENDING:N3-R04` | `DESIGNED_NOT_EXECUTED` | Human ruling D1 and contract adoption before implementation. |
| N3-R05 / no silent replay | Unknown completion is never resumed, resent, or inferred complete during restart/rebind. | Engine/adapter spy records zero `preflight`, `startTurn`, tool, provider, or model calls for every orphan during recovery. | Same `turnId` resubmission, new `turnId` with same payload, retry flag, reconnect, boot, and Agent 1 run attempt while unresolved. | Root runtime owner; affected clients own later client proof | REQ-012/026/034/048/049 | `PENDING:N3-R05` | `DESIGNED_NOT_EXECUTED` | Human ruling D2, then Root and any affected-client gates. |
| N3-R06 / stable drain accounting | Restart reconstructs or otherwise safely accounts for every unresolved local turn before activation; the reported count and activation posture are stable across repeated restart. | Fixture binds accepted turn to exact local selection/model/epoch basis and proves expected recovery/drain state before and after reconciliation. | Memory resets to zero; missing/changed selection; absent epoch; remote/local ambiguity; multiple models; unmanaged loaded model; duplicate release. | Root residency + recovery owners | REQ-010/026/039/044/045 | `PENDING:N3-R06` | `DESIGNED_NOT_EXECUTED` | Human rulings D5/D8, then implementation/check gate. |
| N3-R07 / session truth | Session status, event truth, and recovery audit agree after every recovery result and survive restart. | Exact pre/post session record and event-log hashes; status matches ruled terminal/recovery state. | Crash after terminal before status update; stale `running`; status changed without terminal; terminal append failure. | Root session-store owner | REQ-026/033/039 | `PENDING:N3-R07` | `DESIGNED_NOT_EXECUTED` | Human ruling D4, then implementation/check gate. |
| N3-R08 / malformed evidence | Malformed, truncated, unsupported-schema, misattributed, or non-canonical evidence blocks admission/activation and preserves the original bytes for diagnosis. | Quarantine/failure evidence identifies exact path, line/offset, source hash, reason, and zero consequential admissions. | Current partial replay behavior (count-and-skip); torn final line; invalid UTF-8; oversized entry; forged terminal; path/symlink substitution. | Root session-store + daemon owners | REQ-011/024/033/038/039 | `PENDING:N3-R08` | `DESIGNED_NOT_EXECUTED` | Human rulings D3/D4/D7, then implementation/check gate. |
| N3-R09 / durable audit | Every recovery attempt has a stable run identity, exact input/output hashes, classification, ruled disposition reference, start/end state, and result; repeated runs retain provenance. | Append-only audit plus manifest verifies hashes and ordering across success, block, crash, and rerun. | Missing field, redaction leak, overwritten record, unverifiable artifact, audit write failure, clock reordering. | Root recovery-evidence owner | REQ-033/034/037/039/045 | `PENDING:N3-R09` | `DESIGNED_NOT_EXECUTED` | Human ruling D3 and evidence-schema adoption. |
| N3-R10 / crash consistency | The accepted-to-terminal reconciliation transaction boundary cannot yield a falsely reconciled record or more than one terminal after power/process loss. | Fault injection at every durability boundary; restart converges to one truthful state with preserved preimage. | Terminal persisted but audit absent; audit persisted but terminal absent; status only; partial JSONL append; directory sync loss. | Root storage/recovery owner | REQ-012/026/033/034 | `PENDING:N3-R10` | `DESIGNED_NOT_EXECUTED` | Human ruling D4, then implementation/check gate. |
| N3-R11 / Agent 1 parity | Governed Agent 1 `turn.accepted` records receive the same discovery, no-replay, terminal-cardinality, status, and audit guarantees. | Agent 1 crash fixture at acceptance, delegation, child return, review, and terminal boundaries. | Restart loses manager/child active maps; child result reused as automatic completion; new manager admitted before orphan reconciliation. | Root Agent 1 coordinator owner | REQ-026/030/033/043 | `PENDING:N3-R11` | `DESIGNED_NOT_EXECUTED` | Human rulings D1-D4, then implementation/check gate. |
| N3-R12 / recovery concurrency | Only one authenticated recovery writer owns a corpus/batch; additional daemon or recovery attempts fail closed without mutation. | Owner/lease evidence binds daemon, pid/process instance, corpus basis, and recovery run. | Two startups; stale owner ambiguity; lease expiry mid-write; copied runtime directory; clock skew. | Root daemon/recovery owner | REQ-011/033/039 | `PENDING:N3-R12` | `DESIGNED_NOT_EXECUTED` | Human ruling D4, then implementation/check gate. |
| N3-R13 / retained functions | During recovery, only a human-accepted, non-consequential retained-function set is available; it is not represented as an alternate runtime. | Endpoint/function census records allowed/blocked result, authority owner, and zero mutation for each retained operation. | Turn/run/boot/model activation, registration, credential mutation, scaffold, permission, or replay-induced mutation attempted while recovery is incomplete. | Root owns generic endpoint floor; each client owns its retained-function claim | REQ-013/015/032/048/049/050 | `PENDING:N3-R13` | `DESIGNED_NOT_EXECUTED` | Human ruling D6 plus any affected-client gate. |
| N3-R14 / cutover and rollback | Exact before/after identities, abort/restore path, indeterminate-operation treatment, and evidence preservation are proven without silent replay. | Isolated cutover, failed cutover, restore, and post-restore restart evidence match the plan in section 6. | Basis drift, mixed-version bytes, failed migration, rollback after partial recovery, rollback tool failure. | Root implementation/deployment owner; CHANGE for Git acts | REQ-034/035/036/038; AC-007/010/011 | `PENDING:N3-R14` | `DESIGNED_NOT_EXECUTED` | Human rulings D1-D4/D9 and exact cutover/rollback gate. |
| N3-R15 / source and release binding | Every executed result binds exact contracts, source bytes, test fixture bytes, runtime artifact identity, and accountable approval. | Immutable evidence manifest with independent hash verification and source/release identities. | Result copied from a different source tree, uncommitted drift, missing fixture hash, stale contract identity. | Root evidence integration owner | REQ-007/033/037/038 | `PENDING:N3-R15` | `DESIGNED_NOT_EXECUTED` | N4/N5 fan-in then later human acceptance/release gates. |
| N3-R16 / no authority expansion | Recovery adds no TCP/in-process fallback, alternate daemon/model, automatic scheduling, credential transfer, client write, lifecycle, release, or reliance effect. | Negative surface scan and runtime spies show only the separately authorized recovery effects. | Force fallback, range/downgrade, automatic model load/switch, foreign project mutation, client retry. | Root integration owner; foreign owners retain their gates | REQ-011/032/035/040/041/042/044/046/047 | `PENDING:N3-R16` | `DESIGNED_NOT_EXECUTED` | Implementation review and accountable-human release disposition. |

## 3. Restart and replay scenario matrix

| Scenario | Fixture / interruption point | Expected invariant and observation | Planned artifact | Result | Gate |
|---|---|---|---|---|---|
| RR-01 clean restart | Sessions contain no orphan accepted turns. | Recovery reports zero; readiness opens once; corpus hashes unchanged. | `PENDING:RR-01` | `DESIGNED_NOT_EXECUTED` | Implementation/check gate. |
| RR-02 crash after `turn.accepted` | Normal turn stops immediately after durable acceptance. | One orphan discovered; no engine replay; one ruled terminal/recovery outcome after reconciliation. | `PENDING:RR-02` | `DESIGNED_NOT_EXECUTED` | D1/D2/D4. |
| RR-03 crash after nonterminal stream evidence | Acceptance plus `session.init`, `turn.started`, deltas, or tool events; no terminal. | Partial output is retained and classified indeterminate; no completion or replay inferred. | `PENDING:RR-03` | `DESIGNED_NOT_EXECUTED` | D1/D2/D3. |
| RR-04 crash during terminal append | Truncated/torn/invalid terminal JSONL line. | Evidence is malformed and startup remains closed; original bytes and exact error locus preserved. | `PENDING:RR-04` | `DESIGNED_NOT_EXECUTED` | D4/D7. |
| RR-05 terminal durable, status stale | Valid single terminal exists; session remains `running`. | Not classified orphan; status reconciliation follows ruled transaction policy; no second terminal. | `PENDING:RR-05` | `DESIGNED_NOT_EXECUTED` | D4. |
| RR-06 duplicate/conflicting terminal | Same turn has two identical or different terminal types. | Fail closed; do not append a third terminal or choose a winner implicitly. | `PENDING:RR-06` | `DESIGNED_NOT_EXECUTED` | D1/D7. |
| RR-07 repeated restart | Reboot/reconcile same recovered corpus three times. | Terminal count, drain count, audit semantics, and canonical output digest remain stable. | `PENDING:RR-07` | `DESIGNED_NOT_EXECUTED` | D3/D4/D5. |
| RR-08 recovery crashes mid-batch | Multiple projects/sessions; stop after each possible write boundary. | Every rerun converges without duplicate terminal; completed subset remains provable; readiness stays closed until batch complete. | `PENDING:RR-08` | `DESIGNED_NOT_EXECUTED` | D4. |
| RR-09 concurrent startups | Two daemons/reconcilers target one runtime directory. | At most one writer; loser returns typed fail-closed result; no double terminal. | `PENDING:RR-09` | `DESIGNED_NOT_EXECUTED` | D4. |
| RR-10 local orphan and model activation | Accepted local turn; process restart resets `activeTurns`; activation requested. | Activation and local admission remain blocked until recovery and ruled drain treatment finish. | `PENDING:RR-10` | `DESIGNED_NOT_EXECUTED` | D5/D6/D8. |
| RR-11 remote orphan | Accepted non-local turn plus loaded local model. | Recovery still precedes daemon admission; local drain effect follows explicit classification, not inference. | `PENDING:RR-11` | `DESIGNED_NOT_EXECUTED` | D5/D8. |
| RR-12 selection/epoch ambiguity | Session selection changed or accepted evidence lacks exact model/epoch. | Fail closed or use only a separately ruled classification; never invent attribution. | `PENDING:RR-12` | `DESIGNED_NOT_EXECUTED` | D5/D8. |
| RR-13 Agent 1 restart | Crash after manager acceptance, during delegation, after child return, or before manager terminal. | Same orphan rules apply; no automatic manager or child replay/completion. | `PENDING:RR-13` | `DESIGNED_NOT_EXECUTED` | D1-D4. |
| RR-14 manual retry/resubmit | Client resends same `turnId`, same payload/new ID, or retry flag before/after reconciliation. | Behavior follows explicit retry ruling; no silent resend or duplicate terminal. | `PENDING:RR-14` | `DESIGNED_NOT_EXECUTED` | D2. |
| RR-15 malformed corpus | Invalid UTF-8/JSON/schema/session attribution/event type; terminal without accepted; symlink/path substitution. | Entire affected recovery unit stays closed; exact malformed source preserved; no partial-success admission. | `PENDING:RR-15` | `DESIGNED_NOT_EXECUTED` | D3/D4/D7. |
| RR-16 deleted or legacy session | Deleted marker, absent central record, or legacy migration contains an orphan. | Treatment is explicit and evidence-bearing; no resurrection, omission, or mutation of authoritative legacy source. | `PENDING:RR-16` | `DESIGNED_NOT_EXECUTED` | D4/D7. |
| RR-17 readiness race | Health/status/replay and every consequential route are called at pre-scan, mid-scan, mid-write, failure, and completion. | Only the ruled retained set responds; all consequential admission/activation remains closed until success. | `PENDING:RR-17` | `DESIGNED_NOT_EXECUTED` | D6. |
| RR-18 rollback after recovery start | Cutover fails before scan, during scan, after one recovery write, and after completion. | Restore never erases historical evidence, never silently replays, and re-enters recovery when state is indeterminate. | `PENDING:RR-18` | `DESIGNED_NOT_EXECUTED` | D4/D9. |

## 4. Drain-accounting matrix

| Case | Persisted basis required | Expected accounting evidence | Adversarial proof | Result | Gate |
|---|---|---|---|---|---|
| DA-01 active local turn in one process | Exact session, accepted turn, selected local provider/model, residency epoch where available. | Admission increments once and terminal/finalization releases once. | Double release, throw before acceptance, throw after acceptance, disconnect. | `DESIGNED_NOT_EXECUTED` | Existing behavior plus later check authorization. |
| DA-02 local orphan after restart | Exact durable classification inputs named by D5/D8. | Startup reports ruled unresolved contribution and blocks activation/admission until reconciliation. | `activeTurns` starts at zero; missing epoch; stale selection; changed managed model. | `DESIGNED_NOT_EXECUTED` | D5/D8. |
| DA-03 remote orphan | Provider/model classification is exact and evidence-bound. | Generic reconciliation occurs; local drain contribution is explicit. | Treat all orphans as local or ignore remote orphan globally. | `DESIGNED_NOT_EXECUTED` | D5/D8. |
| DA-04 mixed batch | Multiple local/remote turns, sessions, projects, and models. | Per-turn ledger sums to reported totals; repeated restart is stable. | Duplicate accepted, same turn across sessions, foreign attribution, partial batch crash. | `DESIGNED_NOT_EXECUTED` | D4/D5/D8. |
| DA-05 reconciliation failure | One turn cannot be classified or terminalized. | Admission/activation remains closed; evidence names exact unresolved count and reason. | Continue with decremented count or activate because in-memory count is zero. | `DESIGNED_NOT_EXECUTED` | D1/D4/D5. |
| DA-06 activation race | Activation requested while recovery/drain resolution is incomplete. | Typed rejection; no unload/load request; persisted residency identity unchanged. | Direct coordinator call, HTTP route, repeated request, concurrent request. | `DESIGNED_NOT_EXECUTED` | D6. |

## 5. Exactly-one-terminal evidence matrix

The terminal set itself is not selected here. Current static sources differ:
`events.ts` exposes completed/failed/interrupted, while the harness schema and
coordinators also recognize cancelled. D1 must accept the exact recovery
terminal vocabulary and payload before implementation.

| Corpus shape | Required classification | Permitted mutation | Cardinality assertion | Result | Gate |
|---|---|---|---|---|---|
| One accepted, zero terminal | `ORPHAN_ACCEPTED` | Exactly one human-ruled recovery terminal/record under D1/D4. | Postcondition terminal count = 1. | `DESIGNED_NOT_EXECUTED` | D1/D4. |
| One accepted, one valid terminal | `ALREADY_TERMINAL` | No terminal append. | Count remains 1 through repeated restart. | `DESIGNED_NOT_EXECUTED` | Contract/check gate. |
| One accepted, duplicate same terminal | `INVALID_DUPLICATE_TERMINAL` | None automatically; block and preserve. | No third terminal; readiness closed. | `DESIGNED_NOT_EXECUTED` | D7. |
| One accepted, conflicting terminals | `INVALID_CONFLICTING_TERMINAL` | None automatically; block and preserve. | No winner inferred; readiness closed. | `DESIGNED_NOT_EXECUTED` | D1/D7. |
| Zero accepted, terminal present | `INVALID_UNBOUND_TERMINAL` | None automatically; block and preserve. | No synthetic accepted record. | `DESIGNED_NOT_EXECUTED` | D7. |
| Multiple accepted for one turn ID | `INVALID_DUPLICATE_ACCEPTANCE` | None automatically; block and preserve. | No terminal appended until ruled repair. | `DESIGNED_NOT_EXECUTED` | D4/D7. |
| Malformed possible terminal | `MALFORMED_INDETERMINATE` | None automatically; quarantine/preserve according to D7. | No partial replay classification. | `DESIGNED_NOT_EXECUTED` | D3/D4/D7. |
| Foreign session/turn attribution | `INVALID_ATTRIBUTION` | None automatically. | No cross-session terminal satisfies an acceptance. | `DESIGNED_NOT_EXECUTED` | D7. |

## 6. Cutover and rollback evidence plan

| Stage | Exact identity / precondition | Planned act (later gate only) | Abort condition | Restore / rollback evidence | Owner and gate |
|---|---|---|---|---|---|
| CO-01 baseline freeze | Source, contracts, fixtures, runtime corpus, accepted SOW, and decision-record hashes. | Create immutable pre-change manifest and isolated copy. | Drift, unhashable input, malformed baseline, unresolved D1-D9. | No mutation; record abort manifest. | Root integration owner; human evidence-plan acceptance. |
| CO-02 candidate validation | Exact implementation candidate and check profile are separately authorized. | Static validation and isolated executable scenarios RR-01..18. | Any missing case, nonzero/unexplained result, unbound artifact, or authority expansion. | Discard candidate; preserve results and baseline. | Root implementation/check owner. |
| CO-03 cutover rehearsal | Exact old/new runtime identities and corpus fixture. | Start new bytes against isolated copy; prove recovery-before-readiness. | Admission/activation opens early, replay occurs, or terminal/drain invariant fails. | Stop candidate; restore untouched copy; hash-compare. | Human cutover rehearsal gate. |
| CO-04 failed-cutover rehearsal | Fault injection points from RR-04/RR-08/RR-18. | Exercise abort at each durability boundary. | Historical evidence loss or non-convergent rerun. | Restore by exact accepted mechanism; retain both preimage and failure evidence. | D4/D9 plus check gate. |
| CO-05 authorized cutover | Complete accepted evidence, zero unresolved release blocker, exact deployment act. | Apply only exact approved bytes and run startup reconciliation. | Basis drift, malformed evidence, unresolved recovery, hash mismatch, failed readiness checks. | Execute exact approved restore act; no silent replay. | Separate deployment/CHANGE act and human cutover acceptance. |
| CO-06 post-cutover observation | Exact post-change source/release/runtime identity. | Repeat RR-01/RR-07/RR-10/RR-17 and preserve evidence. | Any terminal/drain/readiness divergence. | Enter fail-closed recovery; use approved rollback only. | Root runtime owner; human regression-evidence acceptance. |
| CO-07 rollback | Exact last accepted baseline and current indeterminate-operation ledger. | Restore approved baseline without rewriting event/audit history. | Restore identity mismatch or baseline cannot interpret current corpus safely. | Remain stopped; escalate with both manifests and blocker ledger. | D9; CHANGE/deployment and accountable-human gate. |

## 7. Retained-function evidence matrix

No row below is adopted as allowed or blocked. D6 must accept the exact set.
The later test must classify every daemon route and direct service entry point,
not just the examples.

| Surface | Candidate classification to be ruled | Required evidence | Adversarial evidence | Authority owner | Result | Gate |
|---|---|---|---|---|---|---|
| Health and daemon status | `TBD_RETAINED_READ_ONLY` | Response reveals recovery readiness truth without mutation or false `ok`. | Reports ready while recovery incomplete; leaks sensitive audit data. | Root runtime | `DESIGNED_NOT_EXECUTED` | D3/D6. |
| Session/event replay | `TBD_RETAINED_READ_ONLY` | Byte-stable read, truthful malformed count/class, no repair-on-read. | Replay skips malformed line and presents partial corpus as complete; transcript mutates state. | Root runtime | `DESIGNED_NOT_EXECUTED` | D6/D7. |
| Project/session listing and get | `TBD_RETAINED_READ_ONLY` | No admission, migration, or status repair side effect; recovery state visible. | Lazy legacy migration or other write occurs during supposedly read-only access. | Root runtime/project authority | `DESIGNED_NOT_EXECUTED` | D6/D7. |
| Turn and governed Agent 1 run | `CONSEQUENTIAL_BLOCKED_UNTIL_RECOVERY` candidate | Typed block before acceptance, engine, tool, delegation, or model action. | Race produces a new `turn.accepted` during recovery. | Root runtime | `DESIGNED_NOT_EXECUTED` | D6. |
| Session boot | `CONSEQUENTIAL_BLOCKED_UNTIL_RECOVERY` candidate | Zero engine preflight/start and zero persisted boot identity while blocked. | Boot creates engine work before recovery completes. | Root runtime | `DESIGNED_NOT_EXECUTED` | D6. |
| Model activate and local admit | `CONSEQUENTIAL_BLOCKED_UNTIL_RECOVERY` candidate | Zero load/unload/admission and stable residency evidence while blocked. | Direct or HTTP activation bypasses daemon startup latch. | Root residency | `DESIGNED_NOT_EXECUTED` | D5/D6. |
| Project registration, session create/delete, credentials, scaffold, permissions | `TBD_MUTATION_CLASS` | Each operation individually classified; blocked operations produce no mutation. | Broad “admin” bypass or foreign authority expansion. | Root plus project/client owners as applicable | `DESIGNED_NOT_EXECUTED` | D6 and owning gate. |
| File-native governance outside runtime | `RETAINED_SEPARATELY_OWNED` candidate | Owning loop proves function remains available and is not an alternate agent runtime. | Runtime claims or mutates foreign-loop authority. | Respective project/loop owner | `DESIGNED_NOT_EXECUTED` | Separate owner acceptance. |

## 8. Human-gated decision ledger

| Decision | Unresolved exact bytes | Accepted basis | Why N3 does not decide it | Required next instrument |
|---|---|---|---|---|
| D1 recovery terminal policy | Exact terminal type/vocabulary, payload, status mapping, and treatment of cancelled/interrupted/failed/recovery-specific outcomes. | TBD-006/TBD-016; REQ-026/036 | Semantic selection is explicitly excluded. | Root semantic decision record accepted by accountable human before N4 adoption/implementation. |
| D2 retry/replay/resume policy | Whether any operator-initiated retry exists; identity, timing, preconditions, and proof; automatic replay remains prohibited. | TBD-006/TBD-008/TBD-016; REQ-012/034 | N3 may prove no silent replay but cannot authorize retry. | Human-accepted recovery/retry decision. |
| D3 audit payload and redaction | Schema, mandatory fields, classification identifiers, sensitive fields, retention, ordering, and hashing. | TBD-008/TBD-016; REQ-033/039/045 | Audit semantics and privacy posture require owner acceptance. | Human-accepted evidence-schema record. |
| D4 transaction/durability boundary | Atomic unit spanning terminal, session status, recovery audit/marker, lock/lease, and fsync/durability semantics. | TBD-006/TBD-016; REQ-026/034 | Static design cannot choose storage guarantees or repair semantics. | Human-accepted storage/reconciliation decision plus implementation brief. |
| D5 drain reconstruction | Which unresolved turns contribute to drain; release point; handling absent/stale model and residency epoch. | TBD-016; REQ-010/026/044/045 | Current `activeTurns` is memory-only and accepted evidence may be insufficient. | Human-accepted drain-accounting decision. |
| D6 admission and retained-function boundary | Exact readiness latch and route/direct-entry allowlist during recovery. | TBD-009/TBD-016; REQ-013/015/048/049/050 | Retained functions and client behavior remain separately owned/gated. | Root decision plus affected-client decisions where actually affected. |
| D7 malformed/contradictory evidence treatment | Quarantine, blocking granularity, repair authority, preservation, and resumption criteria. | TBD-008/TBD-016; REQ-024/033/038 | Current skip-and-count behavior cannot answer the fail-closed policy. | Human-accepted malformed-evidence decision. |
| D8 attribution/classification basis | Durable local/remote/model/epoch facts used for drain and recovery classification. | TBD-016; REQ-039/044/045 | N3 cannot invent missing attribution or equate mutable session state with acceptance-time fact. | Human-accepted evidence/attribution schema. |
| D9 cutover/rollback authority | Exact restore mechanism, safe baseline, abort thresholds, post-restore corpus compatibility, and deployment/Git acts. | TBD-006; REQ-034/035/036 | Cutover and rollback require later human and deployment/CHANGE gates. | Exact cutover/rollback acceptance and separately authorized act. |

All decisions remain open. No test, source behavior, or candidate wording is
treated as acceptance by implication.

## 9. Static findings

| Finding | Severity | Exact observation | Evidence |
|---|---|---|---|
| N3-F01 | `BLOCKING_FOR_IMPLEMENTATION` | Daemon startup establishes owner/auth/socket readiness without a persisted accepted-turn reconciliation phase. | `runtime-daemon.ts` `start()` and routes; source hash in section 1. |
| N3-F02 | `BLOCKING_FOR_IMPLEMENTATION` | Residency `activeTurns` is process memory only; restart begins with zero regardless of persisted orphan turns. | `residency-coordinator.ts`; source hash in section 1. |
| N3-F03 | `BLOCKING_FOR_IMPLEMENTATION` | `replayDetailed()` counts and skips malformed lines, so a partial event set can be returned; this is insufficient for fail-closed recovery classification. | `session-store.ts`; source hash in section 1. |
| N3-F04 | `BLOCKING_FOR_IMPLEMENTATION` | Event persistence deduplicates only by `eventId`; no accepted-turn/terminal uniqueness transaction is present. | `session-store.ts` and `turn-coordinator.ts`; hashes in section 1. |
| N3-F05 | `BLOCKING_FOR_IMPLEMENTATION` | Governed Agent 1 runs also persist `turn.accepted` before a later terminal and track active work only in memory. | `agent1-run-coordinator.ts`; source hash in section 1. |
| N3-F06 | `HUMAN_DECISION_REQUIRED` | Runtime and harness event vocabularies are not identical for terminal types, and accepted events do not by themselves settle recovery terminal, retry, audit, transaction, or drain semantics. | `events.ts`, `event-schema.ts`, TBD-006/008/016. |
| N3-F07 | `EVIDENCE_GAP` | Existing tests cover in-process terminal hardening, disconnect interruption, and in-process drain, but not daemon restart reconciliation, repeated-restart idempotence, or recovery-before-admission. | Three test files and hashes in section 1. |

These findings are expected inputs to later semantic, implementation, and
evidence gates. They do not authorize repairs.

## 10. N3 disposition

`ACCEPT_FOR_N4` means only that the evidence design is complete enough for
N4 candidate integration and later owner review. N4 must preserve D1-D9 as
unresolved human-gated fields. N3 makes no semantic adoption, executes no
evidence, and supplies no closure evidence for `TM-ROOT-108`.
