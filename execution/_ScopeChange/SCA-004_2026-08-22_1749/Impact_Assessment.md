# SCA-004 Gate-1 impact assessment

Status: `AWAITING_OWNER_ACCEPTANCE`
Assessment posture: preliminary Gate-1 impact trace; not an accepted Gate-2
assessment and not an amendment.

## Summary

The v3 pathway is a consequential Root generic-runtime change whose accepted
scope already exists but whose implementation breadth exceeds the single
M-envelope carried by DEL-02-06. The lawful decomposition path is to preserve
DEL-02-06 as standing integration/release assurance, split implementation into
bounded PKG-02 deliverables, add a bounded PKG-04 Root receipt-validator
carrier, and retain existing governance/evidence deliverables as gates and
consumers rather than silently expanding a DOC_UPDATE into a test suite.

The App is an actually affected client in the accepted DEL-02-06
compatibility package. Root may send and consume coordination notices but may
not write App truth. SCA-APP-008 must reciprocate under App authority.

## Root-side semantic change set

| Concern | Required candidate effect | Current Root planning carrier / crosscheck | Gate / hold |
|---|---|---|---|
| Root/App K-CONTROL-1 | Authorize exactly the existing project-scoped daemon socket plus one private daemon-to-supervisor socket; both remain Unix-only under `0700`/`0600`, owner/generation records, rotated tokens, stale recovery; second socket is never renderer/CLI-callable | DEL-02-07 candidate; DEL-03-01 containment crosscheck; App mirror by notice | G0.5 contract acceptance; implementation held |
| K-ROLE-2 | Add role-posture/effective-config digest to worker identity solely for selected authority posture; never durable model assignment; record actual adapter/provider/model/substitution | DEL-02-09/10 candidates; DEL-02-04 and DEL-02-03 governance predecessors | D-GOV-35/DEL-02-03 M2 plus G-ROLE; A3 evidence label applies |
| K-NET-1 | Enumerate OpenAI account/model/turn service endpoints separately from command network. Each canonical root chooses: (1) no command network by default; (2) ask per destination with routed `networkApprovalContext`, visible host/protocol, grouping caveat, and `acceptForSession` only by explicit user act; or (3) labelled `network_access = true` | DEL-02-08/09/10 candidates; DEL-02-04/03-01 crosschecks; App K-NET-1 mirror by notice | G0 A7 supersedes plan denial; G-APPR exact-pin proof; no current network grant |
| Root runtime API v2 | Version one attributed approval request/decision across project, Chirality session, source/root thread, turn, request/item, kind, ancestry, and decision actor; route managed-network prompts rather than deny them; preserve grouping caveat | DEL-02-10 candidate; DEL-04-02 attribution crosscheck | contract/API acceptance then implementation act |
| HarnessEvent v2 | Closed type-indexed discriminated union before coordinator/persistence; map `turn.completed`, `turn.failed`, `turn.interrupted`, `turn.cancelled`; reject/project/redact unknown wire payloads | DEL-02-10 candidate; DEL-05-04/05-06 evidence and mutation crosschecks | G-WIRE and accepted migration |
| `DelegatedHarnessProcessSupervisorPort` | Root/profile worker acquisition, inventory/reconnect, generation fencing, `closeRoot`/`closeAll`; lifecycle not forced onto every engine | DEL-02-07 candidate | G-HELPER/G-DUAL and implementation act |
| `WorkerRetirementCoordinatorPort` | Prepared/committed/reconciliation-required journal, exactly-once terminalization of captured active turns outside engine generators, root quarantine on partial persistence | DEL-02-11 candidate | G-SIG/G-DUAL and implementation act |
| `HostedEngineConsentPort` | Assert project/canonical-root/account-or-epoch/policy/role/generation/cwd continuity before worker, thread, and turn; root-private app-owned `CODEX_HOME`; fresh consent rules when identity cannot be proven | DEL-02-09 candidate | A9; G3/G-SENT/G4 and implementation act |
| Restart semantics | Retirement/crash terminalizes active turns. Next action uses `thread/resume` only when canonical root, account identity, and policy digest match and cwd is fixed to the canonical root; otherwise starts fresh. No in-flight re-attach claim | DEL-02-11 candidate | A4; proposed TM-ROOT-108 route; evidence still required |
| Two-job renderer | Amend `runtime/packages/cli/src/launch-agent.ts` and related launchd/install surfaces for daemon plus process supervisor; resolve physical bundle/cadence empirically at G-HELPER | DEL-02-07 candidate; App installer notice edge | B2; proposed TM-ROOT-042 route; no spike/download/implementation now |
| Root receipt validator | Build a Root-specific validator over the shared receipt contract, append-only numbering, transcription/hash requirements, and Root loop conventions; do not reuse App/Piping validators as Root authority | DEL-04-11 candidate; DEL-04-05, DEL-05-02, and DEL-05-06 crosschecks | later M2 tool tranche and acceptance |
| `source_identity` at G0.5 | Bind exact accepted implementation source bytes/hashes before WP-03/WP-05; repository/planning commit is not source identity | DEL-02-06 integration plus DEL-02-12 conformance candidate | remains `HELD_UNAVAILABLE`; proposed TM-ROOT-035 route |

## Candidate decomposition actions and affected surfaces

| Action | Decomposition sections / companions | Downstream workflow | Risk if omitted |
|---|---|---|---|
| Modify DEL-02-06 as standing integration carrier | Deliverables, Scope Ledger, deliverable register, forward/reverse trace, telemetry, change log | SCOPE_CHANGE exact-byte gates; WORKING_ITEMS only after acceptance/activation | one M-envelope silently absorbs six implementation domains; REQ-027 breached |
| Add DEL-02-07..12 under PKG-02 | same surfaces; later PREPARATION folders and local dependency surfaces | PROJECT_SETUP/PREPARATION after accepted amendment | unseated implementation, overlapping write ownership, no bounded SOWs |
| Add DEL-04-11 Root Loop Receipt Validator under PKG-04 | Deliverables, Scope Ledger, deliverable register, trace/telemetry, change log; later PREPARATION folder and dependency surface | later M2 tool tranche; DEL-04-05/05-02/05-06 validation fan-in | Root receipts remain unchecked or borrow a foreign-loop validator; artifact-kind granularity is blurred |

No Package, Objective, PRD, or scope-item addition is proposed. No current
deliverable folder is deleted, moved, retired, or assigned a new parent.

## DEL-02-06 REQ-027 and exclusion boundary

REQ-027 limits the first activation to exact specification, read-only consumer
inventory, evidence-matrix design, and change planning; it explicitly forbids
implementation bytes. The accepted first-activation exclusion block keeps the
DEL-02-06 clean contract/lifecycle surfaces, decomposition/governance, all
`runtime/**`, agents, skills, tools, App, PEC, Piping, Tier-0, and product or
release files read-only. SCA-004 does not weaken that boundary and does not
edit DEL-02-06.

The six proposed implementation carriers do not become a workaround around
REQ-027. Each requires accepted decomposition/SOW bytes, lawful local profile
and checks, explicit implementation activation, exact write ownership, and
its own return/rollback contract before any source write.

## Ten held bindings — unchanged matrix

| # | Accepted binding key | Current state | Required owning act / routing |
|---|---|---|---|
| 1 | `binding_groups.2_source_and_release_identities.source_identity` | `HELD_UNAVAILABLE` | exact Root implementation source identity accepted at G0.5; SCA routes, does not populate |
| 2 | `binding_groups.2_source_and_release_identities.release_identity` | `HELD_UNAVAILABLE` | exact release identity at G6a |
| 3 | `binding_groups.4_conformance_or_migration_evidence.clients[0]` — App | `HELD_UNAVAILABLE` | App-owned conformance at G5 and exact-release rerun at G7 |
| 4 | `binding_groups.4_conformance_or_migration_evidence.clients[1]` — Root CLI | `HELD_UNAVAILABLE` | Root CLI conformance at G5/G7 |
| 5 | `binding_groups.5_root_semantic_and_regression_evidence` | `HELD_UNAVAILABLE` | accepted Root implementation/check evidence at G5/G7 |
| 6 | `binding_groups.6_census_relationship_routing_notice_and_findings.notice` | `HELD_UNAVAILABLE` | accepted release-fan-in notice after implementation/client evidence |
| 7 | `binding_groups.6_census_relationship_routing_notice_and_findings.tier_0_relationship` | `HELD_UNAVAILABLE` | independent Tier-0 owner act |
| 8 | `binding_groups.8_accountable_human_acts.implementation_act` | `HELD_UNAVAILABLE` | exact implementation activation at G0.5 after accepted carriers/SOWs |
| 9 | `binding_groups.8_accountable_human_acts.cutover_act` | `HELD_UNAVAILABLE` | accountable-human cutover after accepted G2–G5 fan-in |
| 10 | `binding_groups.8_accountable_human_acts.release_act` | `HELD_UNAVAILABLE` | exact-artifact release act at G6a |

Authority source: accepted compatibility snapshot
`DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md`
and accepted JSON SHA-256
`e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`.

## Task Management disposition candidates

These are candidate dispositions only. The register is untouched; see
`Task_Management_Harvest.csv`.

| Row | SCA-004 treatment | Closure condition |
|---|---|---|
| TM-ROOT-035 | route exact `source_identity` to G0.5 before code | remain OPEN until accountable-human identity act is recorded; then `RESOLVED_BY_DECISION` under Task Management |
| TM-ROOT-042 | carry logical-composition/physical-bundling question to G-HELPER | remain OPEN until accepted G-HELPER evidence/ruling; no bundling answer inferred now |
| TM-ROOT-107 | this is the ancestor concern answered by SCA-004 | after owner accepts the SCA Gate-1 intake, Task Management may set `SUPERSEDED_BY_SCOPE_CHANGE` with exact ScaRef; not before |
| TM-ROOT-108 | carry A4 terminalize/resume-or-fresh semantics into DEL-02-11 | remain OPEN until implemented restart/replay evidence satisfies its existing closure target |
| TM-ROOT-106 | named G1 blocker only; no Pi pin amendment | unchanged OPEN; separate routine Task Management decision + validation evidence |
| TM-ROOT-122 | named G1 blocker only; no Electron pin amendment | unchanged OPEN; separate App-owned disposition/Root closure evidence |

No other Task Management row is selected.

## Package-role and derivative-state classification

| Surface | Role | Current effect | Later owner/workflow action |
|---|---|---|---|
| Root decomposition + companion registers | working surface / authoritative companion registers | `NO_CHANGE` | exact Gate-3 candidate only after Gate 1 and Gate 2 acceptance |
| SCA-004 snapshot | snapshot / handoff artifact; derivative assessment | new, `AWAITING_OWNER_ACCEPTANCE` | owner Gate-1 ruling |
| WORK_GRAPH / DAG | derivative coordination package | current for this assessment only | re-derive after any accepted carrier topology change |
| AUDIT_DEP_CLOSURE return | derivative audit evidence | current for exact graph hash only | rerun on graph drift or post-amendment graph |
| DEL-02-06 accepted compatibility package | accepted derivative semantic/compatibility package | unchanged; all holds remain | owning acts only |
| DEL-02-06 ScopeOfWork / status / run records | deliverable-local contract/evidence | `NO_CHANGE` | none in this tranche |
| Root `docs/**`, `runtime/**`, `tools/**` | authoritative/operative downstream surfaces | `NO_CHANGE`, read-only | separate accepted tranches |
| App surfaces | foreign authority | `NO_CHANGE`; notice only | SCA-APP-008 under App authority |

## Evidence basis for current-state claims

| Surface | SHA-256 | Claim supported |
|---|---|---|
| `docs/CONTRACT.md` | `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679` | current Root K-RUNTIME-1/K-CONTROL-1/K-ROLE-2 wording |
| `projects/chirality-app-dev/docs/CONTRACT.md` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | current App K-EVENT/K-NET and related contract posture |
| `runtime/packages/contracts/src/harness/event-schema.ts` | `8c6d17f0547f9433d9a2b0892ba50c266b08918142e39984ecc0a7d479661a2f` | current open HarnessEvent shape requiring v2 closure |
| `runtime/packages/contracts/src/harness/agent-engine-port.ts` | `c51d2b6a173f300acedee468f8e51b29cea2bd946bcdec300eaaa4a3d06a8e5d` | current live engine-port boundary |
| `runtime/packages/core/src/session-store.ts` | `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` | fixed-root/session persistence impact |
| `runtime/packages/core/src/turn-coordinator.ts` | `992d501b49629b88cb72e42ad2c54d7934859da7e3a822259c68151e3ab3715b` | terminal and approval coordinator impact |
| `runtime/packages/cli/src/launch-agent.ts` | `1c3992ff3ca595cedfb648c9cae0aebfd557c2bb9b68e620b8b89799ddfcea27` | current daemon-only renderer targeted by the later two-job change |
| `tools/validation/loop_receipt_contract.py` | `1b6907f5cc9ec4506a9954562a99df3e43c4fa62fab120f1dbec2726c4f687aa` | shared receipt contract exists |
| `tools/validation/validate_app_dev_loop_receipts.py` / `validate_piping_loop_receipts.py` | `daf01933ecade2e62db95cbb48cdb763ae99f64da85b31e0e8b934ebbfd62f64` / `b6891b75614a183e4f0e33be8315a8ac49a2a4baa9a9d11ccfd8f704504a7965` | foreign-loop validators exist while a Root-specific validator does not |

## Invariant and risk assessment

- Stable IDs are preserved; proposed IDs are collision-free and unmaterialized.
- Package discipline remains flat: runtime carriers stay in PKG-02; loop
  validator stays in PKG-04.
- Existing scope coverage remains unchanged at this gate. Later exact bytes
  must keep every IN scope item mapped and every objective supported.
- The principal context risk is silent expansion of DEL-02-06 beyond M;
  splitting is therefore a Gate-1 requirement, not implementation detail.
- The principal authority risk is reading notices, plan prose, current code,
  or a planning commit as an accepted contract/source/implementation act.
- The principal cross-loop risk is circular readiness. All reciprocal App
  edges are notice-only and non-gating until decomposed and accepted.
- The principal network risk is erasing G0 A7 by retaining the plan's older
  denial text. Later candidates must carry the three postures and grouping
  caveat exactly.
- The principal recovery risk is claiming in-flight re-attach. Only
  terminalize plus conditional persisted-thread resume is in scope.

## G1 blockers and later reruns

TM-ROOT-106 and TM-ROOT-122 remain explicit G1 blockers. They do not block the
owner from accepting this Gate-1 intake, but they block G1 passage and identity
freeze. SCA-004 carries no pin change.

If Gate 1 is accepted, Gate 2 must refine exact carrier impacts. Later gates
must run AUDIT_DECOMP before and after the exact amendment, regenerate the
release-pathway graph, rerun dependency closure, create accepted SOWs and
folders through their owning workflows, and route exact notices without
foreign writes.
