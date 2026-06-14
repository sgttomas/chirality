# SCA-APP-001 Handoff State

**Package Role:** snapshot / handoff artifact
**Status:** GATE_5_COMPLETE_VALIDATED
**Accepted amendment snapshot:** `execution/_ScopeChange/SCA-APP-001_2026-06-13_1819_Provider-General_Runtime_Pi_Pattern-Corpus_v2/`
**Latest pointer:** `execution/_ScopeChange/_LATEST.md`

## Fixed State Fields

| Field | Value | Evidence |
|---|---|---|
| `DecompositionTruthState` | COMPLETE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` includes DEC-017 and SCA-aligned package/deliverable wording. |
| `DerivativePackageState` | TARGETED_LOCAL_REVIEW_COMPLETE_PENDING_AUDIT | Active governance/control-plane docs, impacted `_CONTEXT.md` files, and targeted package-local kit wording have been refreshed or reviewed by `SCA-APP-001-CLOSURE-002`; independent scope-closure audit rerun remains required. |
| `ContentRemediationState` | NOT_REQUIRED | This is SOFTWARE SCOPE_CHANGE; no KTY remediation applies. |
| `DownstreamRerunState` | ADVISORY | Dependency/SCC reruns are advisory because topology did not change; provider-general semantics may affect future tranche selection. |
| `MetadataAlignmentState` | TARGETED_COMPLETE_PENDING_AUDIT | Decision register, active plan, coordination, `_CONTEXT.md` base fields, and targeted local kit wording are aligned to the accepted SCA snapshot; audit rerun remains required. |
| `AuditState` | STATIC_PASS | Static validation recorded in `RUN_SUMMARY.md`. |
| `ReadyForNextPhase` | YES_WITH_AUDIT_RERUN_REQUIRED | Future runtime/governance tranches may proceed from updated authority docs and refreshed package-local contexts, but full SCA closure still requires independent audit rerun. |

## Authoritative Truth Changed In Gate 5

| Surface | State |
|---|---|
| `docs/DIRECTIVE.md` | Narrowly aligned to provider-adapter strategy and capability policy / explicit hard-deny precedence. |
| `docs/PRD.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md` | Aligned to provider-adapter generality, Claude Agent SDK / Anthropic as first/current adapter, Pi pattern-corpus-only posture, and capability-forward permission governance. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Amended with SCA decision, package/deliverable/ledger wording, and provider-expansion open issue; no package/deliverable topology change. |
| `execution/_Coordination/_DECISIONS/_REGISTER.md` and D-APP ruling records | D-APP-01/02/03 are `RULED` with ruling-record pointers. |
| `execution/_Coordination/_COORDINATION.md`, `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`, `execution/_Coordination/_LATEST.md`, `WORKSPACE_MANIFEST.csv` | Active control plane aligned to SCA-APP-001. |
| `plans/PLAN_2026-06-13_runtime_completion.md`, `plans/PLAN_COMPLETION_LOG.md` | Active completion surface and history aligned to the SCA. |
| `frontend/docs/harness/runtime_engine_contract.md` | Runtime contract wording aligned to provider-adapter strategy and first-adapter path. |

## Derivative / Reference Surfaces Changed

| Surface | State | Notes |
|---|---|---|
| `plans/pi-agent-harness-assessment.md` | REFERENCE_ONLY_SUPERSEDED_FOR_IMPLEMENTATION | Pi assessment retained as pattern corpus; no Pi adapter/import/spike authorization. |
| `plans/pi-assessment/*.md` | REFERENCE_ONLY_SUPERSEDED_FOR_IMPLEMENTATION | Per-slice Pi assessments carry SCA status and no-spike/no-import boundaries. |
| `plans/claude-agent-sdk-implementation-followups.md` | FIRST_ADAPTER_REFERENCE | Claude SDK follow-ups remain useful as first-adapter implementation detail only. |
| `plans/prd-revisions-claude-agent-sdk.md` | SUPERSEDED_STRATEGIC_REFERENCE | Retained for historical/first-adapter mechanics; not live strategic authority. |
| 26 impacted deliverable `_CONTEXT.md` files | CONTEXT_REFRESHED_PENDING_AUDIT | `SCA-APP-001-CLOSURE-002` refreshed base identity/scope/traceability fields from the accepted v3.2 decomposition and retained SCA alignment notes. |

## Stale / Deferred Surfaces

| Surface | Status | Required follow-up |
|---|---|---|
| Affected deliverable-local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md` | TARGETED_REVIEW_COMPLETE_PENDING_AUDIT | `SCA-APP-001-CLOSURE-002` reviewed and normalized stale provider/Pi/permission wording where present. Remaining `TBD` values and non-SCA lifecycle states retain prior status. |
| Affected deliverable-local `_DEPENDENCIES.md`, `_REFERENCES.md`, `Dependencies.csv` | TARGETED_REVIEW_COMPLETE_PENDING_AUDIT | `SCA-APP-001-CLOSURE-002` reviewed and normalized stale labels where present. The pre-existing dependency/SCC graph state was not changed. |
| Dependency extraction / SCC graph | ADVISORY_RERUN | Topology unchanged; rerun only if a future planning tranche needs refreshed dependency semantics. |
| Runtime source and package manifests | CURRENT_NO_CHANGE | No runtime implementation or dependency changes were made. |

## Closure Repair State

| Finding | State | Evidence |
|---|---|---|
| SCC-001 | REPAIRED | `execution/_ScopeChange/_LATEST.md` now points to accepted Gate 5 state. |
| SCC-002 | REPAIRED | `Propagation_Plan.md` includes the Gate 5 propagation classification addendum. |
| SCC-005 | REPAIRED | `Supersession_Delta.csv` is canonical and `Supersession_Map.csv` has been generated. |
| SCC-003 | REPAIRED_PENDING_AUDIT_RERUN | `Closure_Repair_002.md` records package-local `_CONTEXT.md` base-field refresh against the amended decomposition. |
| SCC-004 | REPAIRED_PENDING_AUDIT_RERUN | `Closure_Repair_002.md` records targeted local kit and dependency/reference artifact review against the accepted SCA. |

## Remaining Blockers

- `SCA-APP-001` remains open for full derivative-package closure until a fresh `AUDIT_SCOPE_CLOSURE` rerun independently accepts SCC-003 and SCC-004 closure.
- Concrete non-Anthropic provider implementation remains blocked pending bounded future tranche.
- Pi adapter, fork, package import, Node 22 sidecar, runtime-floor migration, and immediate spike remain prohibited unless a future ruling explicitly reverses D-APP-01/D-APP-02.
- Bash/write/subagent/runtime policy expansion remains blocked until its active plan row and validation gates authorize it.

## Recommended Next Runtime Tranche

If scope-change closure remains the priority, rerun `AUDIT_SCOPE_CLOSURE` for `SCA-APP-001` against the repair evidence. Otherwise resume the active runtime spine with the earliest unblocked provider-adapter architecture item in `plans/PLAN_2026-06-13_runtime_completion.md`, expected to remain bounded to provider-adapter architecture/governance before any new provider implementation.
