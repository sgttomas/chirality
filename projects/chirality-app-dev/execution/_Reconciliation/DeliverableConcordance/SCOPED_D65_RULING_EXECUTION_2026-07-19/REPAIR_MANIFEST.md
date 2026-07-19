# Exact Repair Manifest — D-APP-68

All paths are repository-relative and exact. A path absent from this manifest
is read-only for the package managers. Each listed `ScopeOfWork.md` change is
an append/current-state reconciliation under the existing SOW-v1 structure;
it must not alter frontmatter identity, decomposition references, or lifecycle
state. Each listed `_STATUS.md` change is one dated History line only, with
`Current State`, `Checking Approval SHA`, and unrelated `Remaining` text
byte-preserved. Each listed `MEMORY.md` change is an append-only current-memory
note. Each listed run record is new and records D-APP-68 authority, exact
changed paths, checks, exclusions, and no lifecycle transition.

## Frozen claim/evidence joins

These accepted, source-state-bound rows prove why each package slice exists.
Companion `MEMORY.md`, `_STATUS.md`, and run-record paths listed below inherit
the same row/ruling join; they record the governed repair and do not add scope.

| Manager | Ruling | Accepted scoped claim/evidence rows | Exact live repair owner |
|---|---:|---|---|
| WI-PKG00-01 | 1 | PKG-00 ledger: `DEL-00-01-REQ-001`, `REQ-DEL-00-02-002`, `DEL-00-02-SCOPED-S01` | DEL-00-01 and DEL-00-02 `ScopeOfWork.md` |
| WI-PKG00-01 | 1–2 | PKG-01 ledger: `DEL-01-01-SCOPED-S01/S02`, `DEL-01-02-SCOPED-S01`, `DEL-01-03-SCOPED-S01`, `DEL-01-04-ACC-001`, `DEL-01-04-SCOPED-S01` | DEL-01-01..04 exact SOW/dependency paths below |
| WI-PKG04 | 8 | PKG-04 ledger: `DEL-04-01-REQ-013`, `DEL-04-01-SCOPED-S01`; live D-APP-52 probe evidence | DEL-04-01 exact decision/evidence/truth paths below |
| WI-PKG05 | 3 | PKG-05 ledger: `DEL-05-01-SCOPED-S02`, `DEL-05-02-SCOPED-S02` | DEL-05-01 and DEL-05-02 SOWs |
| WI-PKG05 | 7 | PKG-05 ledger: DEL-05-03 `UNMAPPED-1`; D-APP-52 transport envelope; D-APP-67 Option B | DEL-05-03 SOW |
| WI-PKG06 | 3 | PKG-06 ledger: `DEL-06-01-SCOPED-S02`, `DEL-06-02-SCOPED-S02`, `DEL-06-03-SCOPED-S02`, `DEL-06-04-SCOPED-S02`, `DEL-06-05-SCOPED-S02` | DEL-06-01..05 SOWs |
| WI-PKG06 | 6 | PKG-06 ledger: DEL-06-05 `UNMAPPED-1`; live `tool-shell-policy.ts` constants | DEL-06-05 SOW |
| WI-PKG08 | 3 | PKG-08 ledger: `DEL-08-05-SCOPED-S01` plus the cross-package DEL-05-05 `UNMAPPED-1` handle resolved by D-APP-56 R4-P32 | DEL-08-05 SOW |
| WI-PKG08 | 4 | PKG-08 ledger: `DEL-08-04-R05/R06`, DEL-08-04 `UNMAPPED-1`, `DEL-08-04-SCOPED-S01/S02`; D-GOV-14 item 7 | DEL-08-04 SOW |
| NONE | 5 | D-APP-56 R4-P32 plus live DEL-08-05 adoption note and DEL-05-05 exclusion note | no change |
| NONE | refuted Pipeline item | D-APP-56 R4-P28 plus live DEL-02-02 ownership note and Receipt-74 | no change |

The PKG-01 dependency changes implement recommendation 2 only for the four
live registers identified by the accepted scoped rows above. They annotate
operative dangling `EvidenceFile`/`SourceRef` cells with current SOW CLM
locations. They do not rewrite immutable D-APP-55/R6/scoped concordance
ledgers, and they do not mass-recode historical extraction provenance. If a
manager encounters another operative dangling citation that requires a write,
that is a missing target and must return to HELP_HUMAN for a manifest
amendment; it is not implicit authority to widen a package slice.

## Consolidated managed-orchestration ownership map (ruling 3)

No new deliverable is created. The nine accepted ownership rows are
distributed exactly once to their nearest existing owners:

| Implemented surface | Sole documentary owner | Boundary preserved |
|---|---|---|
| optional managed-delegation `SessionRecord` fields | DEL-05-01 | canonical session identity and migration precedence unchanged |
| `coordination.notice/update/acknowledged` events | DEL-05-02 | provider-neutral append-only event schema only |
| `artifacts/subagents/` child-output persistence and its 16 KiB/512 KiB policy | DEL-08-05 | DEL-05-05 retains only ordinary tool-result `descriptor.resultBudget` and ToolResultStore semantics |
| `coordination` descriptor class and v7 mode deny | DEL-06-01 | deny-first mode/capability mapping |
| four coordination descriptors, names, catalog rows, and registry validation | DEL-06-02 | descriptor/registry ownership only |
| in-process Chirality MCP co-location/composition | DEL-06-03 | no duplication of DEL-06-02 descriptors or read-slice expansion |
| managed-child declared read/write path enforcement | DEL-06-04 | symlink-safe path-policy ownership |
| managed-child Bash project-root read+write gate | DEL-06-05 | serialized Bash policy ownership |
| managed-child lifecycle, parent/scope linkage, and replayable child records | DEL-08-05 | DEL-08-04 retains admission/delegation-mechanism ownership |

## DEL-04-01 twelve-area evidence and required assessment (ruling 8)

WI-PKG04 must carry all twelve rows into the new adoption-decision record. The
primary live record is
`projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`;
its two JSON summaries are SHA-bound there. The SOW's CLM requirement set is
the normative risk census. Additional evidence below is accepted at the
source basis and stays read-only unless separately listed as a repair target.

| # | Residual area | Evidence to cite | Required `ADOPT_WITH_RESIDUAL_RISK` assessment |
|---:|---|---|---|
| 1 | SDK API drift | `projects/chirality-app-dev/frontend/package.json`, `projects/chirality-app-dev/frontend/package-lock.json`, D-APP-52 live probe | pin SDK `0.3.150` and Claude Code `2.1.150`; regression and fresh ruling on upgrade |
| 2 | Settings leakage | live probe controlled `CLAUDE_CONFIG_DIR` observations; `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-options-builder.test.ts` | accept `settingSources: []` posture while retaining SDK-created config files as an observed substrate effect |
| 3 | Allowed-tools misconception | DEL-04-01 SOW REQ-015; `projects/chirality-app-dev/frontend/src/lib/harness/persona-manager.ts`; permission/hook tests | `allowedTools` alone is not a boundary; Chirality mode, deny, hooks, `canUseTool`, and human gates remain authoritative |
| 4 | Transcript location | live probe transcript path and config-root observations; runtime evidence contract | SDK transcript/store linkage is secondary adapter metadata; Chirality JSONL remains canonical |
| 5 | Electron packaging | packaged live proof summary; DEL-04-01 `Evidence_CODEV-001_SDK_Probe_Record.md`; `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md` | accept unsigned local `darwin:arm64`/`app.asar.unpacked` proof only; exclude signing, notarization, distribution, and other platforms |
| 6 | SDK security boundary | DEL-04-01 SOW residual method; permission/path/redaction/event contracts | treat SDK/subprocess as privileged substrate behind Chirality-owned boundaries |
| 7 | Subagent inherited permissions | D-GOV-14 item 7; root `AGENTS.md`; managed-delegation/path-policy evidence in scoped PKG-08 ledger | managed child sessions require sealed context and explicit scopes; retired SDK Agent bridge is not fallback |
| 8 | Session-mirror reliability | live SDK session IDs/transcript placement; `projects/chirality-app-dev/frontend/docs/harness/runtime_engine_contract.md` | SDK mirror/linkage is secondary and cannot replace canonical Chirality events/session identity |
| 9 | Product-identity drift | DEL-04-01 SOW REQ-015; DEL-01-03 product-boundary SOW; root product contracts | Claude/Anthropic names remain implementation metadata, not Chirality identity or authority |
| 10 | Platform dependency | live probe `darwin:arm64`; packaged proof macOS binary path | macOS arm64 demonstrator only; Windows, Linux, and other architectures unproven |
| 11 | Reliance-boundary ambiguity | DEL-01-02 reliance-boundary SOW/register; DEL-04-01 SOW residual method | accept only observed, mapped, fail-closed Chirality behavior; opaque/unverifiable behavior triggers fallback |
| 12 | Engine-adapter lock-in | `projects/chirality-app-dev/frontend/packages/harness-contract/src/agent-engine-port.ts`; provider-neutral runtime contracts | retain the pinned SDK as first adapter behind `AgentEnginePort`; preserve custom-runtime fallback |

The verdict remains demonstrator-scoped. It conveys no release approval,
issuance, certification, professional acceptance, signing, notarization,
publication, or external distribution.

## WI-PKG00-01 — rulings 1 and 2

### DEL-00-01

- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure/ScopeOfWork.md`
  — reconcile CLM-015/016 so `CLOSURE_D53A` is current and
  `CLOSURE_SCC_SAFE_MOVES_001` is historical first-proof evidence.
- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure/_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md`

### DEL-00-02

- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/ScopeOfWork.md`
  — reconcile CLM-005/017 to D53A-current; reconcile CLM-006/028 to the
  D-APP-65 ResponsibleParty assignment; repoint CLM-010 REQ-010's deleted
  `Procedure.md (Records)` source to the Records CLM in this SOW.
- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md`

### DEL-01-01

- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/ScopeOfWork.md`
  — replace false live four-document-kit assertions in CLM-011/017/018 with
  the SOW-v1 production set; reconcile CLM-008/016/022 and the CLM-012 artifact
  TBD to the D-APP-65/current artifact state.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/Dependencies.csv`
  — append dated D-GOV-16/D-APP-68 migration notes in affected live rows and
  replace live EvidenceFile/SourceRef pointers to deleted kit files with the
  corresponding `ScopeOfWork.md` CLM anchors; preserve row identity/status.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/_DEPENDENCIES.md`
  — append a dated current-source annotation; preserve historical extraction
  prose rather than rewriting it as though the original extraction used SOW.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md`

### DEL-01-02

- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/ScopeOfWork.md`
  — reconcile CLM-020/037 live references to the SOW-v1 production set.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/Dependencies.csv`
  — dated D-GOV-16/D-APP-68 source-migration annotations and current SOW CLM
  anchors for affected live EvidenceFile/SourceRef cells; preserve row states.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/_DEPENDENCIES.md`
  — append-only current-source annotation; historical extraction text stays.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md`

### DEL-01-03

- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/ScopeOfWork.md`
  — reconcile CLM-005/019 live locations to SOW CLMs and render REF-007 as a
  repository-relative path.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/Dependencies.csv`
  — dated D-GOV-16/D-APP-68 source-migration annotations and current SOW CLM
  anchors for affected live EvidenceFile/SourceRef cells; preserve row states.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/_DEPENDENCIES.md`
  — append-only current-source annotation; historical extraction text stays.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md`

### DEL-01-04

- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register/ScopeOfWork.md`
  — reconcile CLM-012/013/018 to SOW-v1, CLM-017 lifecycle wording to
  `_STATUS.md`, remove the stale hash-warning clause, and fix the doubled
  “the current” phrase without changing scope.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register/Dependencies.csv`
  — dated D-GOV-16/D-APP-68 source-migration annotations and current SOW CLM
  anchors for affected live EvidenceFile/SourceRef cells; preserve row states.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register/_DEPENDENCIES.md`
  — append-only current-source annotation; historical extraction text stays.
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register/_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md`

## WI-PKG04 — ruling 8

- `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`
  — create the demonstrator-scoped `ADOPT_WITH_RESIDUAL_RISK` decision,
  version pins, live observations, all twelve residual-risk assessments,
  fallback triggers, and explicit non-release/non-professional limits.
- `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/ScopeOfWork.md`
  — replace live adoption-TBD slots with the D-APP-68 verdict and link the new
  decision while retaining dated pre-ruling text as history.
- `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Evidence_CODEV-001_SDK_Probe_Record.md`
  — append a dated supersession note for the stale subprocess-version and
  interrupt `BLOCKED_TBD` cells, pointing to D-APP-52 live evidence; do not
  rewrite the historical 2026-05-24 observations.
- `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_CONTEXT.md`
  — append the D-APP-68 verdict and demonstrator/non-release bounds.
- `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_run_records/TASK_RUN_2026-07-19_DAPP68_adoption_verdict.md`

The two D-APP-52 JSON summaries and `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`
are read-only evidence and must remain byte-identical.

## WI-PKG05 — rulings 3 and 7

For each deliverable below, update only the named SOW ownership boundary, add
one Memory note, one History line, and the named run record.

- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/ScopeOfWork.md`
  — own the optional managed-delegation `SessionRecord` fields without changing
  canonical session identity or migration precedence.
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL/ScopeOfWork.md`
  — own the three `coordination.*` event categories within the provider-neutral
  append-only schema.
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-03_Redacted_RunLogger_and_Secret_Hygiene/ScopeOfWork.md`
  — own PEC credential/cookie envelope hygiene, citing D-APP-52 and D-APP-67;
  state that credentials remain excluded by construction and runtime generic
  secret-registry expansion is not authorized.
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-03_Redacted_RunLogger_and_Secret_Hygiene/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-03_Redacted_RunLogger_and_Secret_Hygiene/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-03_Redacted_RunLogger_and_Secret_Hygiene/_run_records/TASK_RUN_2026-07-19_DAPP68_pec_hygiene_ownership.md`

DEL-05-05 receives no write. Its live R4-P32 note already assigns both
`artifacts/subagents/` child-output persistence and the 16 KiB/512 KiB policy
to DEL-08-05, while retaining only the distinct ordinary tool-result
`descriptor.resultBudget` and ToolResultStore semantics.

## WI-PKG06 — rulings 3 and 6

- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping/ScopeOfWork.md`
  — map the `coordination` descriptor class and v7 mode hard-deny behavior.
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/ScopeOfWork.md`
  — own the four coordination tool descriptors, names, catalog entries, and
  registry validation; do not absorb DEL-06-03 composition ownership.
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/ScopeOfWork.md`
  — record coordination-tool co-location/composition on the in-process MCP
  server and preserve the read-slice exclusion/DEL-06-02 descriptor owner.
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/ScopeOfWork.md`
  — own managed-child declared read/write path scope and symlink-safe denial.
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy/ScopeOfWork.md`
  — own the managed-child Bash project-root read+write scope gate and replace
  numeric timeout TBD wording with default `120000` ms / maximum `600000` ms.
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`

## WI-PKG08 — rulings 3 and 4; ruling 5 recorded no-op

- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/ScopeOfWork.md`
  — cite D-GOV-14 item 7; replace current SDK-Agent-bridge assertions with
  `delegate_agent` managed delegation; state SDK `Agent` is not model-visible;
  reconcile R02/R05/R06 with parent-relative hierarchy and root `AGENTS.md`.
- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_delegation_refresh.md`
- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/ScopeOfWork.md`
  — own `artifacts/subagents/` child-output persistence, managed-child
  lifecycle/parent linkage/declared-scope linkage, and coordination-aware
  persistence. Preserve the existing R4-P32 statement verbatim in substance:
  16 KiB/512 KiB remain normative here and distinct from DEL-05-05
  `descriptor.resultBudget`.
- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`

No file is assigned for ruling 5 itself: it is an authorized no-change row.

## Authorized no-change accounting

| Item | Disposition | Evidence | Write count |
|---|---|---|---:|
| Recommendation 5 child-output thresholds | NO-OP — already ruled by D-APP-56 R4-P32 solely under DEL-08-05; DEL-05-05 exclusion already live | DEL-08-05 SOW R4-P32 note; DEL-05-05 SOW ownership-exclusion note | 0 |
| Earlier Pipeline scaffold slate item | REFUTED / NO-OP — already owned by DEL-02-02 under D-APP-56 R4-P28 | DEL-02-02 SOW R4-P28 note; Receipt-74 render-test closeout | 0 |
| Standalone D-APP pointer merely for D-GOV-16 | NO-OP — D-GOV-16 is already conversion authority; the pending D-APP-68 transcription cites it only as omnibus basis | D-GOV-16 ruled record; owner recommendation 2 and frozen chronology | 0 |

The R4-P28 and R4-P32 rows above are explicit authorized no-change rows for
R6 accounting; neither row silently disappears merely because its write count
is zero.

## Shared exclusions

- No prior concordance ledger, accepted snapshot, decomposition file, authority
  corpus document, frontend source/test, loop receipt, completion log, or
  another control instance may change in a package slice.
- No new deliverable, dependency row, tool, provider, network path,
  domain-engine apply/accept surface, lifecycle transition, issuance, release,
  certification, or professional-reliance claim.
- Dependency rows receive citation/Notes/LastSeen changes only as required for
  source migration; row identity, direction, target, status, satisfaction, and
  lifecycle semantics remain unchanged.

## Per-package validation and fan-in criteria

1. `python3 tools/scope_of_work/validate_scope_of_work.py <each changed ScopeOfWork.md>` passes.
2. `python3 tools/validation/validate_dependencies_schema.py <each changed Dependencies.csv>` and the project dependency validator pass where CSV changes.
3. Markdown/JSON structure, exact-path existence, `git diff --check`, and a
   package-scoped changed-path allowlist pass.
4. Search proves every ruled mapping/value appears, every named contradiction
   is absent or explicitly superseded, and immutable history was not silently
   recoded.
5. `_STATUS.md` lifecycle/Approval SHA and unrelated Remaining lines compare
   byte-for-byte except the authorized History append.
6. D-APP-38 authority corpus status and the app-dev receipt validator pass;
   no frontend runtime suite is required because runtime source is excluded.
7. The manager return supplies exact paths, ruling/claim coverage, before/after
   disposition, checks, exclusions, and blockers. Partial or out-of-scope
   returns fail fan-in.
8. V1 independently verifies all five slices against D-APP-68 and this exact
   manifest before serialized loop closeout.
