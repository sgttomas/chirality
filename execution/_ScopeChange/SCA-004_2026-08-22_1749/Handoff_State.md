# SCA-004 Gate-3/Gate-4 draft handoff state

Status: `AWAITING_OWNER_GATE_3_APPROVAL`

## Four-state handoff

| State | Value |
|---|---|
| Accepted upstream state | R1-C records `G1-ACCEPTED` for eight actions. R2-A records `G2-ACCEPTED` against `Impact_Assessment.md` SHA-256 `ff370baa…ed3d3`, prior `Decision_Log.md` SHA-256 `bfc184ff…94dc`, and prior `Handoff_State.md` SHA-256 `971c63bb…947c`. Root SOFTWARE decomposition revision 1.2 remains accepted at SHA-256 `23f6ae0f…64f3d`; `_LATEST.md` remains applied SCA-002 at SHA-256 `b2849c6e…80a1`. |
| Authoritative truth state | `UNCHANGED` — the exact Gate-3 candidate is a snapshot copy only. No live decomposition/companion register, pointer, folder, SOW, lifecycle, dependency, estimate, schedule, runtime, tool, App, or held-binding byte changes. |
| Derivative package state | `Gate_3_Candidate/` contains seven synchronized candidate surfaces, `Gate_3_Exact_Amendment.diff` is the full native-line-ending patch, and `Gate_3_Validation.json` reports `PASS` (98 checks, 0 failures) after review-cycle-1 through review-cycle-5 repairs. `Amendment_Preview.md`, `Propagation_Plan.md`, and the schema-complete nine-column `Amendment_Actions.csv` await separate owner Gate-3/Gate-4 approvals. |
| Closure / next state | `OPEN_PENDING_OWNER_GATE_3_AND_GATE_4_APPROVAL`; Gate 5 is closed. Next owner is Ryan Tufts through HELP_HUMAN. |

## Fixed state fields

| Field | Value |
|---|---|
| AmendmentID | `SCA-004` |
| DecompositionTruthState | `INCOMPLETE` — exact candidate drafted, live revision 1.2 unchanged |
| DerivativePackageState | `INCOMPLETE` — current candidate is bound to revision 1.2, but owner Gate-3/Gate-4 approval remains pending |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` — no Gate-5 copy, PREPARATION, SOW, dependency, estimate, schedule, graph, audit, implementation, or App act is authorized |
| MetadataAlignmentState | `NOT_REQUIRED` |
| AuditState | `NON_BLOCKING_PASS` — Gate-3/Gate-4 deterministic validation 98/98; Gate-1 AUDIT_DECOMP and AUDIT_DEP_CLOSURE evidence remain current for their protected live bases |
| ReadyForNextPhase | `NO` |
| ClosureVerdict | `OPEN_PENDING_OWNER_GATE_3_AND_GATE_4_APPROVAL` |

## Exact candidate identity

| Candidate surface | SHA-256 |
|---|---|
| Working surface | `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641` |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| Scope ledger | `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc` |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| Coverage telemetry | `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765` |

The projected candidate topology is 53 deliverables: PKG-02=12,
PKG-04=11, other package counts unchanged; packages=6, scope items=104,
objectives=7; Context Envelopes S=14, M=38, L=1, XL=0. There are zero IN
scope items without a mapping, zero objectives without support, and zero
untraced reverse units.

## Derivative-package state

| Package | Owner | Current status | Evidence | Next required action |
|---|---|---|---|---|
| Exact Gate-3 candidate | SCOPE_CHANGE | `AWAITING_OWNER_GATE_3_APPROVAL` | `Gate_3_Candidate/**`; `Gate_3_Exact_Amendment.diff`; `Gate_3_Validation.json` | Owner approves, corrects, or declines the exact bytes. |
| Gate-4 propagation plan | SCOPE_CHANGE | `AWAITING_OWNER_GATE_4_APPROVAL` | `Propagation_Plan.md`; `Amendment_Actions.csv` | Owner rules separately from Gate 3. |
| Gate-1 release-pathway graph | SCOPE_CHANGE / AUDIT_DEP_CLOSURE | `CURRENT_FOR_LIVE_46_DELIVERABLE_TOPOLOGY` | protected `WORK_GRAPH.json` SHA-256 `86159f1e…e78e9`; existing audit return | Re-derive only after accepted application and seven live folders, then rerun AUDIT_DEP_CLOSURE. |
| Gate-1 decomposition baseline | AUDIT_DECOMP / SCOPE_CHANGE consumer | `CURRENT_FOR_PROTECTED_REVISION_1_2_BASIS` | `Evidence/AUDIT_DECOMP/coverage_summary.json` SHA-256 `2210e77f…de9e45` | Run post-application backcheck; rerun baseline first only if a protected input drifts. |
| Live decomposition package | SOFTWARE_DECOMP / SCOPE_CHANGE | `CURRENT_REVISION_1_2_UNCHANGED` | seven bound live SHA-256 identities | Only a later owner-approved Gate-5 exact copy may apply candidate bytes. |
| DEL-02-06 compatibility package | DEL-02-06 owner | `CURRENT_UNCHANGED_WITH_TEN_HOLDS` | accepted compatibility JSON SHA-256 `e5ae4e87…0467c` | Named later acts only; SCA-004 drafting lifts no hold. |
| Seven candidate folders/SOWs/dependencies | PROJECT_SETUP / PREPARATION / WORKING_ITEMS | `NOT_CREATED_NOT_AUTHORIZED` | Gate-4 plan only | Wait for approved amendment and exact downstream authorization. |
| Estimates and schedule | estimate-snapshot / PROJECT_SETUP scheduling | `NOT_CREATED_FOR_CANDIDATES` | Gate-2 impact and Gate-4 advisory | Run only after accepted SOWs and dependencies. |
| App SCA-APP-008 work | App owning loop | `FOREIGN_AUTHORITY_NOTICE_ONLY` | Gate-1 notice edges | App reciprocates under its own instruments. |

## Active derivative-surface state

| Surface | Classification | Status | Evidence / authority |
|---|---|---|---|
| Candidate working surface, deliverable/scope/objective registers | `DIRECT_EDIT` | synchronized candidate only | Gate-3 files and 98-check PASS; OI-011 covers all 53 assigned rows, D-12 names PKG-04=11, and DEL-02-07/10 carry the complete accepted control sets |
| Candidate forward/reverse trace and telemetry | `RECOMPUTE` | synchronized candidate only | Gate-3 files and 98-check PASS; full reverse inverse, OI-011 concordance, and explicit current-state scan included |
| `Amendment_Actions.csv` | `DIRECT_EDIT` | nine-column STRUCTURE schema; 8/8 `SupersessionBindingPresent=NO` | structural/allocation actions; no admitted-authority fact superseded |
| `Decision_Log.md`, `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions.csv`, `Handoff_State.md` | `DIRECT_EDIT` | Gate-3/4 decision package drafted | R2-A drafting authority |
| `Brief.md`, `Gate_1_Validation.md`, `Parsed_Actions.csv`, `WORK_GRAPH.json`, `DAG.md` | `NO_CHANGE` | protected and current for their exact bases | R1-C and Phase-0c protected-surface checks |
| `Evidence/AUDIT_DEP_CLOSURE/**`, `Evidence/AUDIT_DECOMP/**` | `NO_CHANGE` | current for exact live bases | existing immutable returns |
| Live working surface plus six companion/trace/telemetry files | `NO_CHANGE` | accepted revision 1.2 | owner Gate-3/4 and later Gate-5 authority absent |
| `execution/_ScopeChange/_LATEST.md` | `NO_CHANGE` | still identifies applied SCA-002 | pointer treatment requires separate accepted authority |
| Every `_STATUS.md` and package/deliverable folder | `NO_CHANGE` | no materialization/lifecycle act | explicit Phase-0c prohibition |

## Held bindings and controlling amendments

All ten DEL-02-06 compatibility objects remain `HELD_UNAVAILABLE`: source
identity, release identity, App conformance, Root CLI conformance, Root
semantic/regression evidence, fan-in notice, Tier-0 relationship,
implementation act, cutover act, and release act.

G0 A3/A4/A7 remain explicit in the candidate rows. Agent 0/1/2 role entry is
always offered for Codex sessions; when G-ROLE cannot mechanically prove
Agent-2 non-delegation, explicit Agent 2/TASK remains offered labelled
`role not mechanically enforced`, governed-workflow evidence is marked
`instruction-asserted`, and delegated-harness-native K-SUBAGENT
non-delegation is instruction+config asserted rather than mechanism-proven.
Hard filesystem/network/process containment is unchanged. Active turns
terminalize before conditional `thread/resume` under canonical-root,
account-identity, and policy-digest continuity, with a fresh thread otherwise.
Each canonical root chooses under consent: no command network by default;
ask per destination with routed `networkApprovalContext` showing
host/protocol, the caveat that a grant may unblock queued requests to the
same destination, and `acceptForSession` only by explicit user act; or
labelled command network on (`network_access = true`). OpenAI service
endpoints remain separately enumerated, and G-APPR must prove prompt delivery
and observe destination grouping empirically at the exact pin.

## Blockers / human decisions

1. Owner Gate-3 approval, correction, or decline of the exact candidate bytes.
2. Separate owner Gate-4 approval, correction, or decline of the propagation
   plan. Gate-4 approval cannot be inferred from Gate-3 approval or vice versa.
3. Gate 5 remains closed; exact live copy and applied-state validation need a
   later owner act.
4. `_LATEST.md` pointer treatment requires its own accepted authority.
5. Seven folder INITs, seven SOWs, DEL-02-06 context propagation,
   dependencies, estimates, schedule, graph re-derivation, and audit reruns
   remain downstream and unexecuted.
6. TM-ROOT-106 and TM-ROOT-122 remain G1 blockers; no pin change occurs.
7. SCA-APP-008 remains App authority; Root carries notice/fan-in edges only.
8. C1 artifact download, runtime/tool implementation, hold lifts, cutover,
   and release remain unauthorized.

## Rerun requirements

- Before any application, reverify all seven live basis SHAs, candidate
  identities, candidate-ID absence, and `_LATEST.md`; rerun
  `validate_gate3_candidate.py` and require 98/98 PASS.
- Apply only the exact owner-approved candidate bytes; then run deterministic
  register/trace/telemetry validation and fresh scoped AUDIT_DECOMP against
  the Gate-1 baseline.
- After seven folders are live, re-derive the objective-relative graph,
  recompute SCCs, and rerun AUDIT_DEP_CLOSURE.
- Extract dependencies before estimates and schedule; then reassess the
  narrowed DEL-02-06 carrier and estimate each accepted new carrier.
- Keep closure validation separate from Gate-5 writes and record all
  downstream derivative states before any closure claim.

## Next owner

Ryan Tufts through HELP_HUMAN: decide Gate 3 against the exact candidate
identities, then decide Gate 4 separately against the propagation-plan bytes.
No later gate or downstream authority is inferred.
