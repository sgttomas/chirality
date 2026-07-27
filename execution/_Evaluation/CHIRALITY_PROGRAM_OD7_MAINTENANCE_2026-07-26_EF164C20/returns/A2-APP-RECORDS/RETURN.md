# A2-APP-RECORDS terminal return

## Dispatch and basis

- DispatchID: `A2-APP-RECORDS`
- Parent: `EVALUATION`
- AcceptedBasisCommit: `ef164c20c8a903a7ecff9450f677938a4111392f`
- Mode: bounded read-only ephemeral Agent 2 generalist
- Subject-state writes: none
- Prior review and OD-6 packages supplied lineage only; current bytes governed.

## Files inspected

- `AGENTS.md`
- `projects/chirality-app-dev/AGENTS.md`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-75_RULING_2026-07-26.md`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `projects/chirality-app-dev/execution/_Coordination/APP_HOLD_REGISTER.csv`
- App coordination notices for D-GOV-21, D-GOV-23, D-GOV-24, D-GOV-26, and D-GOV-28
- `projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json`
- `projects/chirality-app-dev/execution/_Reconciliation/References/reconcile_authority_corpus.py`
- `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md`
- App D-APP-48, D-APP-49, and D-APP-73 ruling/contract records
- OD-6 `FINDINGS.csv`, D-APP-48/49 return, and runtime-consumer return
- PEC PRD v2, D-PEC-56, D-PEC-58, D-T0-23, and the PEC D-GOV-28 notice
- Piping D-30 consumption record and D-31 ruling
- current-basis App, PEC, and Piping notice filenames.

Read-only checks confirmed: `HEAD` equals the basis; the App corpus reports
8/8 declared members `MATCH`; D-APP-48 pull-only validation passes; combined
D-APP-48/Piping-D-30 validation fails on `source.commitSha`; APP-HOLD-1 state
commit `4cdf469cf3aa3f76681e52aeeb7e833c52e1faee` and PR-363 merge
`18e5dda568689daadaa05aff65bd4b810489409b` are both ancestors of the basis.

## Issue dispositions

| Issue | CurrentStatus | Claim | EvidenceRefs | OwningAuthority | SmallestInstrument | DecisionClass | Dependencies | WriteScope | RequiredNotices | Unknowns | RerunTrigger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| APP-OD7-001 D-APP-75 effective-state residue | OPEN_DEFECT | APP-HOLD-1 is integrated and active, but the ruling and register still say PR merge is pending. This is record lag only and authorizes no repin. The deterministic merge identity is `18e5dda568689daadaa05aff65bd4b810489409b`. | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-75_RULING_2026-07-26.md:3-11`; `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-75_RULING_2026-07-26.md:95-114`; `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md:90`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/FINDINGS.csv:17` | App owner; D-APP-75 closeout | Dated additive D-APP-75 effective-state addendum naming the merge SHA, plus register-row correction. Preserve frozen candidate and original ruling bytes under supersede-never-edit. | MECHANICAL | None | App decision addendum and register only | None | None about integration; state and merge commits have distinct roles | Hold supersession or contradictory Git ancestry |
| APP-OD7-002 false D-GOV-26 detector statement | OPEN_DEFECT | The notice says App's corpus pins the Root SPEC/CONTRACT files changed by D-GOV-26. The tool resolves those names to App-local documents, so that asserted Root-doc detector cannot fire. This does not prove universal detector failure. | `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-26_SPEC_CONTRACT_AMENDMENTS.md:24-36`; `projects/chirality-app-dev/execution/_Reconciliation/References/reconcile_authority_corpus.py:32-50`; `projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json:269-281`; `AGENTS.md:182` | Root notice issuer for correction; App receiving loop for disposition | Additive corrective notice withdrawing only the false detector assertion, plus App disposition. Do not edit history or add Root docs to the App corpus in this act. | COORDINATION_ONLY | None | Root correction/receipt and App disposition are disjoint | Corrected Root→App notice; App response visible to Root | Any future Root-doc pinning design is separate | Corpus path/membership or detector-claim change |
| APP-OD7-003 D-GOV-28 receiving-loop disposition | OPEN_OBSERVATION | App received the Root runtime-stewardship notice. It requires no immediate acknowledgment, but explicitly leaves unacknowledged routing open. SCA-APP-005 is the natural disposition home. | `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-28_ROOT_RUNTIME_STEWARDSHIP_PRD.md:1-19`; `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-28_ROOT_RUNTIME_STEWARDSHIP_PRD.md:21-32`; `projects/chirality-app-dev/AGENTS.md:160-177` | App SCOPE_CHANGE / receiving loop | Record adopt, amend, decline, or defer in SCA-APP-005 decision log/handoff; otherwise one App response | COORDINATION_ONLY | Accepted SCA-APP-005 basis if disposition rides that SCA | SCA package or one App response | Disposition tracked to Root | SCA-APP-005 is absent from current main | SCA-APP-005 merge or D-GOV-28 change |
| APP-OD7-004 stale RB-PEC-ADAPTER row | OPEN_DEFECT | App still describes PEC adapter RBAC and the old scratch/demo adapter as current. PEC v2 retires the prototype role ontology/RBAC and old L3 product and partially supersedes D-PEC-56 behavior 1; only no-dual-loop and human-only-act restrictions survive unchanged. | `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md:137-148`; `projects/pec/docs/PRD.md:215-226`; `projects/pec/docs/PRD.md:370-385`; `projects/pec/docs/PRD.md:428-436`; `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md:69-81` | App DEL-01-02 owns its consumer evidence; PEC D-PEC-58 owns PEC truth; Root owns generic runtime | Owner-gated App register maintenance: retire or mark the row superseded, preserve surviving restrictions, state the register is consumer-side, and do not invent v2 enforcement. Route the proposed disposition to PEC. Root daemon-row re-homing is separate. | OWNER_DECISION | D-PEC-58 already adopted; a replacement row waits for accepted PEC v2 adapter truth | App register plus App→PEC notice; PEC response separately owned | App→PEC exact-row notice; Root only if later re-home is proposed | Replacement v2 enforcement does not yet exist; retire versus explicit pending marker is owner judgment | PEC v2 adapter/profile adoption or Root re-home |
| APP-OD7-005 PEC runtime-migration receiving acts | SUPERSEDED | No new App-origin migration notice is needed to establish the boundary: D-T0-23 and D-PEC-56 were companion owner acts, D-PEC-58 superseded the retired adapter mechanics, and D-GOV-28 is routed to PEC. The remaining App→PEC item is APP-OD7-004. | `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md:1-26`; `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-56_shared_runtime_agent_migration.md:1-24`; `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md:69-81`; `projects/pec/execution/_Coordination/NOTICE_D-GOV-28_ROOT_RUNTIME_STEWARDSHIP_PRD.md:1-32` | Existing Tier-0 and PEC acts | None for migration authority | NONE | None | None | None beyond APP-OD7-004 | Governed live PEC daemon consumption remains OD-6 UNKNOWN | New PEC authority claim or companion-ruling change |
| APP-OD7-006 Piping runtime-migration notice | CLOSED | Piping is not a Root-runtime client and D-30 says no runtime dependency is installed. No Piping notice is due merely from App/PEC migration; its open issue is stale D-APP-48 metadata in APP-OD7-007. | `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/returns/A2-RUNTIME-CONSUMERS/RETURN.md:40-42`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/returns/A2-RUNTIME-CONSUMERS/RETURN.md:84-95`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_HARNESS_CONTRACT_CONSUMPTION_2026-07-04.json:28-35` | None | None | NONE | None | None | None | Future client adoption possible but absent | New Piping runtime-client import, manifest, or decision |
| APP-OD7-007 D-APP-48/Piping synchronized-consumption route | OPEN_DEFECT | App pull contract pins `55a066fd…`; Piping D-30 pins `ee290e22…`; combined validation fails. D-31/DEC-063 are not current synchronized-consumption evidence. This remains OD-6 contract evidence, not an independent OD-7 repin. App must notify Piping when proposing the D-APP-48 disposition. | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_RULING_2026-07-04.md:21-36`; `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json:7-26`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_HARNESS_CONTRACT_CONSUMPTION_2026-07-04.json:8-26`; `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-31_RULING_2026-07-04.md:26-55`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/FINDINGS.csv:8-12` | App owner for D-APP-48; Piping for D-30/D-31/DEC-063; Tier-0 for version identity | Keep in OD-6: decide retain/supersede D-APP-48, route exact App→Piping notice, then Piping amends/supersedes/declines. No mechanical repin or invented provenance. | OWNER_DECISION | App boundary SCA; accepted D-APP-48 disposition; D-APP-49 audit where compatibility is claimed | Separate App and Piping tranches; Tier-0 only if version identity changes | App→Piping mismatch notice; Tier-0 for version decision | Current semantic compatibility is unproved; Piping has metadata only | D-APP-48 disposition, D-APP-49 audit, record change, or green combined validator |
| APP-OD7-008 D-APP-49 current-location notice posture | UNKNOWN | The two source types migrated byte-identically to Root and App has compatibility re-exports, but no admitted current-location executable audit exists. No PEC-specific corrective notice or semantic-failure claim is yet supported. | `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/returns/A2-DAPP48-49/RETURN.md:41-58`; `projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/returns/A2-DAPP48-49/RETURN.md:88-102`; `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-49_RULING_2026-07-04.md:25-50` | Root contract and App facade owners | Run OD-6 current-location audit, then decide historical-successor wording, facade posture, and exact consumer notices | OWNER_DECISION | Current-location audit and consumer inventory | OD-6 only; no OD-7 subject write | None until an affected consumer is established | Executable conformance, facade retirement, cross-release compatibility | Audit, facade/root contract change, or demonstrated consumer effect |
| APP-OD7-009 universal Root-doctrine pinning redesign | SUPERSEDED | A broad App pinning redesign is not warranted. The root rule's deterministic-detection statement is scoped to changes under `agents/`; App already pins two Root agent instructions. OD-7 corrects only APP-OD7-002. | `AGENTS.md:174-182`; `projects/chirality-app-dev/execution/_Reconciliation/References/reconcile_authority_corpus.py:40-50`; `execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/SUPERVISORY_META_FANIN.md:93-96`; `execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/SUPERVISORY_META_FANIN.md:122-131` | None currently | None in OD-7 | NONE | None | None | None | Future intentional inheritance remains a separate question | New accepted Root-doc detector claim |

## Closed and superseded confirmation

- APP-HOLD-1 remains active, scan-authoritative, entry-path-independent, and
  no-repin (`projects/chirality-app-dev/AGENTS.md:94-119`;
  `projects/chirality-app-dev/execution/_Coordination/APP_HOLD_REGISTER.csv:1-7`).
- PEC's old adapter-retention mechanics are superseded; surviving no-dual-loop
  and human-only-act boundaries remain.
- App's instruction and PRD surfaces already state Root-owner/App-client
  runtime alignment (`projects/chirality-app-dev/AGENTS.md:160-177`;
  `projects/chirality-app-dev/docs/PRD.md:1692-1720`).
- No Piping runtime-migration item is open; only D-APP-48 metadata coordination
  remains.
- D-APP-48/49 basis/audit work remains OD-6. OD-7 supplies only the bounded
  coordination route and performs no repin.

## Limitations and escalation conditions

- No runtime was started. D-APP-49 executable conformance and governed live PEC
  daemon consumption remain `UNKNOWN`.
- Basis-scoped filename/content censuses found no App-origin
  RB-PEC-ADAPTER notice and no Piping notice for the current D-APP-48 mismatch;
  rerun the census before staging notices.
- The passing 8/8 App corpus status proves only its declared local corpus is
  current; it does not make it a Root-doc detector.
- SCA-APP-005 is absent from current main. Re-evaluate APP-OD7-003 and
  APP-OD7-007 after it lands.
- Escalate before changing RB-PEC-ADAPTER semantics, choosing D-APP-48
  retention/supersession, expanding corpus membership, or changing version
  identity. D-APP-75 backfill and exact D-GOV-26 correction are
  mechanical/coordination acts only.

## Engine, provider, and model

- Engine: `Codex`
- Provider: `OpenAI`
- Model: `GPT-5`
