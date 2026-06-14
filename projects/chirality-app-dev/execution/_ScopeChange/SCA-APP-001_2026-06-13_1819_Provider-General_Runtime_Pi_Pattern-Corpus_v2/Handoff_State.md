# SCA-APP-001 Handoff State

**Package Role:** snapshot / handoff artifact
**Status:** GATE_5_COMPLETE_VALIDATED
**Accepted amendment snapshot:** `execution/_ScopeChange/SCA-APP-001_2026-06-13_1819_Provider-General_Runtime_Pi_Pattern-Corpus_v2/`
**Latest pointer:** `execution/_ScopeChange/_LATEST.md`

## Fixed State Fields

| Field | Value | Evidence |
|---|---|---|
| `DecompositionTruthState` | COMPLETE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` includes DEC-017 and SCA-aligned package/deliverable wording. |
| `DerivativePackageState` | PARTIAL_LOCAL_REVIEW_REQUIRED | Active governance/control-plane docs and impacted `_CONTEXT.md` files are aligned; deliverable-local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` remain stale until bounded package-local review. |
| `ContentRemediationState` | NOT_REQUIRED | This is SOFTWARE SCOPE_CHANGE; no KTY remediation applies. |
| `DownstreamRerunState` | ADVISORY | Dependency/SCC reruns are advisory because topology did not change; provider-general semantics may affect future tranche selection. |
| `MetadataAlignmentState` | PARTIAL | Decision register, active plan, coordination, and `_CONTEXT.md` pointers are aligned; local four-doc-kit metadata remains `STALE_LOCAL_REVIEW_REQUIRED`. |
| `AuditState` | STATIC_PASS | Static validation recorded in `RUN_SUMMARY.md`. |
| `ReadyForNextPhase` | YES_WITH_STALE_LOCAL_ARTIFACT_WARNINGS | Future runtime/governance tranches may proceed from updated authority docs and contexts, but must not treat deliverable-local kits as refreshed until reviewed. |

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
| 26 impacted deliverable `_CONTEXT.md` files | CONTEXT_ALIGNED_REVIEW_REQUIRED | Each includes `SCA-APP-001 Context Alignment` with primary impact and stale-local-artifact warning. |

## Stale / Deferred Surfaces

| Surface | Status | Required follow-up |
|---|---|---|
| Affected deliverable-local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md` | STALE_LOCAL_REVIEW_REQUIRED | Review through bounded package-local tranches before relying on local kit details that encode prior provider/Pi/permission assumptions. |
| Affected deliverable-local `_DEPENDENCIES.md`, `_REFERENCES.md` | STALE_LOCAL_REVIEW_REQUIRED | Refresh or confirm against accepted SCA and current dependency/SCC graph. |
| Dependency extraction / SCC graph | ADVISORY_RERUN | Topology unchanged; rerun only if a future planning tranche needs refreshed dependency semantics. |
| Runtime source and package manifests | CURRENT_NO_CHANGE | No runtime implementation or dependency changes were made. |

## Remaining Blockers

- No blockers remain for closing SCA-APP-001.
- Concrete non-Anthropic provider implementation remains blocked pending bounded future tranche.
- Pi adapter, fork, package import, Node 22 sidecar, runtime-floor migration, and immediate spike remain prohibited unless a future ruling explicitly reverses D-APP-01/D-APP-02.
- Bash/write/subagent/runtime policy expansion remains blocked until its active plan row and validation gates authorize it.

## Recommended Next Runtime Tranche

Resume the active runtime spine with the earliest unblocked provider-adapter architecture item in `plans/PLAN_2026-06-13_runtime_completion.md`, expected to remain bounded to provider-adapter architecture/governance before any new provider implementation.
