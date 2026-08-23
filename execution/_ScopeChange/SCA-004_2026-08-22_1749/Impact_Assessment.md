---
amendment_id: SCA-004
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
gate: 2
created: 2026-08-22
status: awaiting_owner_gate_2_acceptance
accepted_basis: main@b143444bd497eae1b1b638670a33e6df756d9084
gate_1_authority: R1-C; owner accepted eight parsed actions on 2026-08-22
---

# SCA-004 Gate 2 — impact assessment

Status: `AWAITING_OWNER_GATE_2_ACCEPTANCE`

This assessment refines the impact of the eight actions accepted at Gate 1.
It changes no decomposition truth, companion register, deliverable contract,
lifecycle state, dependency surface, estimate, schedule, runtime, tool, App
truth, or `_LATEST.md`. It does not open Gate 3.

## Accepted Gate-1 basis and boundary

R1-C accepted the parse against these exact subjects:

| Subject | Accepted SHA-256 |
|---|---|
| `Brief.md` | `cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126` |
| `Gate_1_Validation.md` | `812d0d3a33f0c2740dc89be31566a7b1f30ec833bfd99f3afe45f7bc11c99c14` |
| `WORK_GRAPH.json` | `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9` |

The accepted action family is one `MODIFY` plus seven `ADD` actions. There is
no package, objective, PRD scope-item, removal, reclassification, merge,
split, retirement, or renumbering action. Candidate IDs remain
unmaterialized until later exact-byte gates.

If all eight actions are later approved and applied exactly, projected
topology changes from 46 to 53 deliverables: PKG-02 from 6 to 12 and PKG-04
from 10 to 11. Package count remains 6, scope-item count 104, and objective
count 7. These are impact projections, not live counts.

## Impact summary — all eight accepted actions

Abbreviations in the table: `WS` is the SOFTWARE decomposition working
surface; `DR` is the deliverable register; `SL` is the scope ledger; `OR` is
the objective register; `F/R/T` are forward trace, reverse trace, and coverage
telemetry. Exact row bytes, final objective mappings, artifact lists, types,
Context Envelopes, and write loci belong to Gate 3.

| Seq / action | Decomposition structure | Variant-local files and metadata | Downstream consumers / workflows | Invariant and telemetry risk |
|---|---|---|---|---|
| 1 — `MODIFY DEL-02-06` | Preserve DEL-02-06 under PKG-02 as the standing semantic integration and release-assurance carrier; narrow its decomposition allocation so six implementation domains no longer collapse into its M envelope. `SOW-104` and OBJ-001/002/004/007 continuity must remain explicit. | Later exact `WS`, `DR`, `SL`, `OR`, `F/R/T` changes. Existing DEL-02-06 `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_DEPENDENCIES.md`, and accepted compatibility package are `NO_CHANGE` in this SCA. | SCOPE_CHANGE exact-byte gates; later WORKING_ITEMS fan-in only after accepted application/activation; re-derived dependency graph and conformance fan-in. | Highest risk is accidental semantic retirement or a silent weakening of REQ-027. Gate 3 must prove the standing carrier, accepted SOW-104 coverage, four objective mappings, M split requirement, and all ten holds survive. |
| 2 — `ADD DEL-02-07` Process Supervisor and Purpose-Limited Control | Add one PKG-02 leaf carrier for `DelegatedHarnessProcessSupervisorPort`, the purpose-limited second private socket, worker acquisition/inventory/reconnect, generation fencing, and the daemon-plus-supervisor launch topology. | Later new rows in `WS`/`DR`, allocation in `SL`/`OR`, recomputed `F/R/T`; later PREPARATION-owned folder and local metadata/dependency surface. | G-HELPER, G-DUAL, containment crosscheck through DEL-03-01, two-job renderer/installer work, App installer notice edge. | Parent exists and ID is collision-free. Risk is creating a second runtime or renderer/CLI-callable socket; exact bytes must retain one daemon as runtime broker, Unix-only `0700`/`0600` controls, token/owner/generation/stale-recovery rules, and no TCP listener. |
| 3 — `ADD DEL-02-08` Exact Supply and Protocol Pinning | Add one PKG-02 leaf carrier for exact App Server supply/protocol pinning and separately enumerated OpenAI account/model/turn service endpoints. | Same later `WS`/`DR`/`SL`/`OR` direct edits and `F/R/T` recomputation; later folder/SOW/dependency surfaces. | Exact-pin protocol/conformance gates, G-WIRE/G-SUPPLY evidence, downstream adapter and release consumers. | Risk is conflating service endpoints with command network or smuggling a pin change into SCA-004. TM-ROOT-106 and TM-ROOT-122 remain separate G1 blockers and no pin value changes here. |
| 4 — `ADD DEL-02-09` Hosted Account and Consent Boundary | Add one PKG-02 leaf carrier for `HostedEngineConsentPort`, root-private app-owned `CODEX_HOME`, account/epoch and policy continuity, K-ROLE-2 role-posture digest, and per-root consent state. | Same later decomposition/register/trace/telemetry changes plus PREPARATION-owned local surfaces. | G3/G-SENT/G4 consent proof, account/root registration, worker identity consumers, App consent mirror by notice. | Risk is reading ambient `~/.codex`, treating role/model as durable assignment, or reusing consent across root/account/policy drift. Exact bytes must require fresh consent when continuity cannot be proven. |
| 5 — `ADD DEL-02-10` Adapter Event Schema and Approval API v2 | Add one PKG-02 leaf carrier for Root runtime API v2, attributed approval request/decision, closed HarnessEvent schema v2, adapter projection, and approval routing. | Same later decomposition/register/trace/telemetry changes plus PREPARATION-owned local surfaces. | DEL-04-02 attribution, DEL-05-04 claim labels, DEL-05-06 mutation controls, daemon/Electron/client fixtures and compatibility tests. | Risk is provider-shaped persistence, unattributed decisions, unknown wire payload persistence, or erasing G0 A7 by denying prompts. The four terminal events remain `turn.completed`, `turn.failed`, `turn.interrupted`, and `turn.cancelled`; unknown payloads must be rejected/projected/redacted. |
| 6 — `ADD DEL-02-11` Worker Retirement, Restart, and Terminal Reconciliation | Add one PKG-02 leaf carrier for `WorkerRetirementCoordinatorPort`, prepared/committed/reconciliation-required journal state, exactly-once terminalization, and restart semantics. | Same later decomposition/register/trace/telemetry changes plus PREPARATION-owned local surfaces. | G-SIG/G-DUAL, session-store/turn-coordinator migration, recovery and replay evidence, TM-ROOT-108 closure path. | G0 A4 controls: active turns terminalize on retirement/crash; the next action may use `thread/resume` only with canonical-root, account-identity, and policy-digest continuity and cwd fixed to canonical root; otherwise a fresh thread. No in-flight re-attach or automatic replay claim is permitted. |
| 7 — `ADD DEL-02-12` Runtime Conformance Evidence and Shared-Release Fan-in | Add one PKG-02 leaf carrier for Root/client conformance, exact source identity at G0.5, shared-release evidence fan-in, and hold-aware disposition. | Same later decomposition/register/trace/telemetry changes plus PREPARATION-owned local surfaces. | DEL-05-04/05-06/05-07 evidence and closure, DEL-06-01 self-application, DEL-06-07 release authority, App reciprocal notice/evidence. | Risk is treating planning/repository identity as `source_identity`, instruction-asserted evidence as mechanism proof, or evidence completeness as release authority. All ten compatibility bindings remain held until their named acts. |
| 8 — `ADD DEL-04-11` Root Loop Receipt Validator | Add one PKG-04 `TEST_SUITE` leaf carrier for a deterministic Root-specific validator; preserve DEL-04-05 as receipt doctrine and DEL-05-02 as evidence-discipline crosscheck. Gate 3 must decide exact SOW-041/SOW-053 allocation. | Later `WS`/`DR` row, exact `SL` and `OR` mappings, recomputed `F/R/T`; later PREPARATION folder and a separately authorized `tools/**` M2 write locus. | DEL-04-05, DEL-05-02, DEL-05-06; Root loop closeout and CI; future validator implementation tranche. | Risk is leaving a new deliverable unmapped, mixing a test suite into DOC_UPDATE DEL-04-05, or borrowing App/Piping validators as Root authority. No tool write is authorized at Gate 2. |

## G0 amendment carriage

These amendments are controlling inputs to every later exact carrier:

| Amendment | Required impact disposition |
|---|---|
| G0 A3 — role parity | Agent 0/1/2 role entry is always offered for Codex sessions. When G-ROLE cannot mechanically prove Agent-2 non-delegation, explicit Agent 2/TASK remains offered as `role not mechanically enforced`; governed-workflow evidence is `instruction-asserted`, and delegated-harness-native K-SUBAGENT non-delegation is instruction+config asserted rather than mechanism-proven. Hard filesystem/network/process containment is unchanged. This affects DEL-02-07/09/10/12 and their conformance evidence. |
| G0 A4 — restart | Active turns terminalize; a later action resumes the stored thread through `thread/resume` only under canonical-root, account-identity, and policy-digest continuity with canonical cwd, otherwise creates a fresh thread. No in-flight turn re-attach. This is centered in DEL-02-11 and crosschecked by DEL-02-10/12. |
| G0 A7 — command network | Each canonical root chooses under consent: no command network by default; ask per destination with routed `networkApprovalContext`, visible host/protocol, the stated caveat that a grant may unblock queued requests to the same destination, and `acceptForSession` only by explicit user act; or labelled `network_access = true`. OpenAI account/model/turn service endpoints remain separately enumerated. G-APPR must prove prompt delivery and observe grouping empirically at the exact pin. This affects DEL-02-08/09/10/12. |

## DEL-02-06 REQ-027 and ten-binding hold matrix

REQ-027 still limits the first DEL-02-06 activation to exact specification,
read-only consumer inventory, evidence-matrix design, and change planning; it
forbids implementation bytes. Adding candidate implementation carriers does
not bypass that boundary: each later carrier needs accepted decomposition and
SOW bytes, PREPARATION, exact activation, declared writes/checks, and its own
return/rollback contract.

The accepted `root-runtime-1` epoch-1 compatibility package remains unchanged:

| # | Binding | Gate/owner that remains required | Gate-2 state |
|---:|---|---|---|
| 1 | `binding_groups.2_source_and_release_identities.source_identity` | exact Root implementation source bytes/hashes accepted at G0.5 | `HELD_UNAVAILABLE` |
| 2 | `binding_groups.2_source_and_release_identities.release_identity` | exact release identity at G6a | `HELD_UNAVAILABLE` |
| 3 | `binding_groups.4_conformance_or_migration_evidence.clients[0]` — App | App-owned conformance at G5 and exact-release rerun at G7 | `HELD_UNAVAILABLE` |
| 4 | `binding_groups.4_conformance_or_migration_evidence.clients[1]` — Root CLI | Root CLI conformance at G5/G7 | `HELD_UNAVAILABLE` |
| 5 | `binding_groups.5_root_semantic_and_regression_evidence` | accepted Root implementation/check evidence at G5/G7 | `HELD_UNAVAILABLE` |
| 6 | `binding_groups.6_census_relationship_routing_notice_and_findings.notice` | release-fan-in notice after implementation/client evidence | `HELD_UNAVAILABLE` |
| 7 | `binding_groups.6_census_relationship_routing_notice_and_findings.tier_0_relationship` | independent Tier-0 owner act | `HELD_UNAVAILABLE` |
| 8 | `binding_groups.8_accountable_human_acts.implementation_act` | exact implementation activation at G0.5 | `HELD_UNAVAILABLE` |
| 9 | `binding_groups.8_accountable_human_acts.cutover_act` | accountable-human cutover after G2–G5 fan-in | `HELD_UNAVAILABLE` |
| 10 | `binding_groups.8_accountable_human_acts.release_act` | exact-artifact release act at G6a | `HELD_UNAVAILABLE` |

Authority: `DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md`
and accepted JSON SHA-256
`e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`.

## Derivative-package status

| Package | Owner | Status at this Gate-2 assessment | Required rerun / closure action |
|---|---|---|---|
| SCA-004 Gate-2 assessment | SCOPE_CHANGE | `AWAITING_OWNER_GATE_2_ACCEPTANCE` | Owner accepts, corrects, or declines exact Gate-2 bytes. |
| Gate-1 `WORK_GRAPH.json` / `DAG.md` | SCOPE_CHANGE / AUDIT_DEP_CLOSURE | `CURRENT_FOR_UNCHANGED_GATE_1_GRAPH` | No rerun now because graph bytes are unchanged. Re-derive after any accepted carrier topology is materialized, then rerun AUDIT_DEP_CLOSURE. |
| Gate-1 scoped AUDIT_DECOMP baseline | AUDIT_DECOMP / SCOPE_CHANGE consumer | `CURRENT_FOR_PROTECTED_GATE_1_BASIS` | Before application, rerun if any bound decomposition/register/pointer byte drifts; after application, run fresh post-change audit and exact delta. |
| Root decomposition coverage/trace derivatives | SCOPE_CHANGE at application | `CURRENT_NOW`; `STALE_REBUILD_REQUIRED` after an accepted topology edit | Recompute forward trace, reverse trace, and telemetry from exact accepted rows; validate zero unmapped IN items/objectives/deliverables. |
| DEL-02-06 accepted compatibility package | DEL-02-06 owner | `CURRENT_UNCHANGED_WITH_TEN_HOLDS` | No regeneration at Gate 2. Later implementation/conformance acts populate only their owned bindings. |
| New deliverable folders, SOWs, local metadata, dependencies | PROJECT_SETUP / PREPARATION and later WORKING_ITEMS | `NOT_CREATED_NOT_AUTHORIZED` | Only after accepted Gate-3/4/5 amendment: prepare exact folders/SOW candidates, dependency extraction, validation, and separate activation. |
| Root estimate/schedule packages | estimate-snapshot / PROJECT_SETUP scheduling | `NO_ACCEPTED_SURFACE_IDENTIFIED_FOR_CURRENT_CANDIDATES`; would be stale after topology application | Produce fresh estimates for seven new carriers and reassess DEL-02-06; recompute schedule only after exact dependencies and activation gates exist. |
| App SCA-APP-008 carrier/contract package | App SCOPE_CHANGE and App owners | `FOREIGN_AUTHORITY_NOTICE_ONLY` | App reciprocates under its own SCA; Root consumes only accepted notice/evidence. |

## Derivative-surface classification

Classification describes the later impact if Gate 3 exact bytes, Gate 4
propagation, and Gate 5 application are separately approved. Nothing in the
table authorizes those writes now.

| Surface | Package role | Classification | Authority basis / Gate-2 disposition |
|---|---|---|---|
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | working surface | `DIRECT_EDIT` later | Eight accepted actions; exact semantic-section diff required at Gate 3. `NO_CHANGE` now. |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | authoritative companion register | `DIRECT_EDIT` later | One modified plus seven added deliverable rows; exact bytes required at Gate 3. |
| `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` | authoritative companion register | `DIRECT_EDIT` later | Preserve SOW-104 and allocate carriers; decide exact SOW-041/SOW-053 receipt mapping at Gate 3. |
| `execution/_Decomposition/chirality_root_objective_register_v1_0.csv` | authoritative companion register | `DIRECT_EDIT` later | Add exact accepted deliverable mappings without creating objectives. |
| `execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv` | authoritative trace derivative | `RECOMPUTE` later | Recompute from accepted scope/deliverable/objective rows. |
| `execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv` | authoritative trace derivative | `RECOMPUTE` later | Add seven live deliverable traces and revalidate all existing units. |
| `execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md` | authoritative telemetry derivative | `RECOMPUTE` later | Projected deliverable/package counts and envelope distribution must be generated from exact Gate-3 rows. |
| `execution/_ScopeChange/SCA-004_2026-08-22_1749/Decision_Log.md`, `Impact_Assessment.md`, `Handoff_State.md` | snapshot / handoff artifacts | `DIRECT_EDIT` now | Owner R1-C opens Gate 2; this tranche owns only these Gate-2 state records. |
| `Brief.md`, `Gate_1_Validation.md`, `Parsed_Actions.csv`, `WORK_GRAPH.json`, `DAG.md` | protected Gate-1 snapshot/evidence | `NO_CHANGE` | R1-C binds the first three subjects; steer requires all five byte-identical. |
| `Evidence/AUDIT_DEP_CLOSURE/**` | derivative audit evidence | `NO_CHANGE` | Exact graph unchanged; existing return remains evidence only for graph SHA `86159f1e…78e9`. |
| `execution/_ScopeChange/_LATEST.md` | snapshot pointer | `NO_CHANGE` in Phase 0b | Explicit tranche prohibition; future Gate-5 pointer treatment requires its own accepted authority. |
| DEL-02-06 `ScopeOfWork.md`, `_STATUS.md`, accepted compatibility bytes | deliverable contract/lifecycle/accepted derivative | `NO_CHANGE` | R1-C changes no SOW/lifecycle/binding; REQ-027 and all ten holds remain. |
| Root `docs/**`, `runtime/**`, `tools/**` | normative/operative downstream surfaces | `NO_CHANGE` by N2 | Later separately authorized contract, implementation, or M2 tool tranches only. N1's separately bounded D-GOV-35/DEL-02-03 application is not an N2 write. |
| App and Piping truth | foreign authority | `NO_CHANGE` | Notices coordinate; they do not confer authority. |

## Orphan, mapping, and structural risk

| Risk measure | Current live state | Projected / required disposition |
|---|---:|---|
| Parentless live deliverables | 0 introduced | All six runtime additions bind to existing PKG-02; receipt validator binds to existing PKG-04. |
| Removed/reused IDs | 0 | None permitted; all existing IDs stable. Candidate IDs remain reserved-only until application. |
| Parent child-closure actions | 0 | Not triggered: no package or other parent is removed, moved, merged, split, or reclassified. |
| Candidate deliverables awaiting exact scope mapping | 7 | They are not live or orphaned. Gate 3 must bind DEL-02-07..12 to retained SOW-104 allocation and bind DEL-04-11 to the exact accepted SOW-041/SOW-053 choice. |
| Candidate deliverables awaiting exact objective mapping | 7 | Gate 3 must name the objective set for every row and update the objective register consistently. |
| Candidate folders/SOW/dependency records absent | 7 | Expected and non-blocking at Gate 2; they remain forbidden until later accepted amendment and PREPARATION acts. |
| Current IN scope items without mapping / objectives without support | 0 / 0 | Must remain zero after deterministic post-amendment register and AUDIT_DECOMP validation. |

The main orphan risk is therefore not a current dangling row; it is applying
candidate deliverables without the exact synchronized working-surface,
register, trace, telemetry, and later folder/SOW/dependency set. Gate 3 and
Gate 4 must show that full set before Gate 5 can be considered.

## Estimate and schedule staleness

No accepted estimate or schedule surface for these seven candidate
deliverables exists, so Gate 2 does not mark a live estimate file stale.
After topology application:

1. DEL-02-06's prior M-envelope assumptions must be reassessed against its
   narrowed integration/fan-in role.
2. Each added carrier requires its own estimate only after exact SOW, Context
   Envelope, anticipated artifacts, write locus, dependencies, and gates are
   accepted.
3. Dependency extraction precedes schedule recomputation. Cross-loop App
   notices remain non-gating; only an accepted later fan-in criterion can
   affect readiness sequencing.
4. TM-ROOT-106 and TM-ROOT-122 remain G1 blockers and may change schedule risk
   only through separate owner disposition; no pin assumption is embedded
   here.

## Active snapshot and handoff impact

- The accepted decomposition basis remains revision 1.2 at SHA-256
  `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`.
- `_LATEST.md` remains byte-identical at SHA-256
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`
  and continues to identify applied SCA-002. SCA-004 is the single evolving
  assessment folder but is not accepted decomposition truth.
- D-GOV-35 is `RULED` by R1-A. Its DEL-02-03 M2 application belongs to sibling
  N1 and does not itself accept this Gate-2 assessment or open Gate 3.
- `Handoff_State.md` moves from the completed Gate-1 decision to
  `AWAITING_OWNER_GATE_2_ACCEPTANCE`; `ReadyForNextPhase` remains `NO`.
- TM-ROOT-107 and TM-ROOT-126 dispositions belong to sibling N3 routine Task
  Management. They do not change SCA-004's decomposition authority.

## Recommended reruns and later owning workflows

| Trigger | Required action | Owner |
|---|---|---|
| Before drafting Gate 3 | Reverify all bound decomposition/register/pointer hashes and candidate-ID absence; rerun the accepted Gate-1 AUDIT_DECOMP baseline if any bound input drifted. | SCOPE_CHANGE + AUDIT_DECOMP |
| Gate 3 candidate | Draft exact synchronized bytes for the working surface, deliverable/scope/objective registers, forward/reverse trace, and telemetry; prove package discipline, artifact-kind granularity, Context Envelopes, mappings, and count parity. | SCOPE_CHANGE |
| Gate 4 candidate | Enumerate PREPARATION handoffs, seven SOW candidates, dependency extraction, estimate/schedule follow-ons, notices, exact write ownership, and validation. | SCOPE_CHANGE → PROJECT_SETUP/PREPARATION and downstream owners |
| After separately approved application | Run deterministic register/coverage checks and fresh scoped AUDIT_DECOMP; compare against Gate-1 baseline. | SCOPE_CHANGE + AUDIT_DECOMP |
| After new folders become live | Re-derive `WORK_GRAPH.json`/`DAG.md` using live nodes, recompute SCCs, and rerun AUDIT_DEP_CLOSURE. | SCOPE_CHANGE + AUDIT_DEP_CLOSURE |
| Before implementation | Resolve exact accepted SOWs, D-GOV-35/DEL-02-03 role basis, G-HELPER/G-SBX/G-PROT/G-ROLE/G-APPR/G-WIRE gates, TM-ROOT-106/122, and accountable-human implementation acts. | owning Root workflows / Ryan Tufts |
| Cross-loop fan-in | Route/consume SCA-APP-008 notices and later accepted App conformance without Root writing App truth. | Root/App coordination under separate authorities |

## Gate-2 conclusion and question

`PASS_TO_OWNER_GATE_2_WITH_EXACT_GATE_3_REQUIREMENTS`.

The eight accepted actions are impact-assessable without changing live truth.
Their lawful path requires synchronized decomposition/register/trace/telemetry
bytes, later PREPARATION and dependency work, explicit estimate/schedule
refresh, and re-derived graph/audit evidence after topology is live. G0
A3/A4/A7 and the ten held bindings remain explicit and unchanged.

Does the owner accept this Gate-2 impact assessment? Until that answer is
recorded against these exact bytes, Gate 3 remains closed.
