# SCA-APP-001 Impact Assessment

**Package Role:** snapshot / handoff artifact
**Gate:** 2 - Impact Assessment
**Status:** PREVIEW_PENDING_HUMAN_ACCEPTANCE

This assessment covers the requested provider-general runtime and Pi pattern-corpus reorientation. It is based on the active decomposition, active governance docs, current coordination docs, active completion plan, decision register, runtime contract docs, and Pi assessment plans.

## Summary

The change is a semantic and governance amendment, not a topology amendment. It does not require new package IDs, deliverable IDs, source files, dependencies, lockfiles, runtime wrappers, or package manifests. It does require coordinated edits to decomposition truth and governance/control-plane documents if approved.

The highest-risk inconsistency is leaving the current docs split between:

- existing Anthropic / Claude Agent SDK privileged wording;
- existing Pi adapter / spike possibility wording;
- existing "deny-first" blanket phrasing;
- the human's new provider-general and Pi-pattern-corpus rulings.

Until Gate 5 is approved and executed, active project truth remains unchanged and those conflicts remain intentionally visible.

## Impact Summary

| Action | Affected sections/files | Affected workflows | Required closure action |
|---|---|---|---|
| A001 provider-adapter strategy | `docs/PRD.md`, `docs/PLAN.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, decomposition sections 3, 4, 7, 8, 9, 10A, 11, 12 | Runtime planning, adapter design, validation planning, future provider implementation selection | Gate 5 direct edits after approval; hash/reference posture reviewed after docs changes |
| A002 Pi pattern-corpus posture | `execution/_Coordination/_DECISIONS/_REGISTER.md`, new ruling records, `plans/pi-agent-harness-assessment.md`, `plans/pi-assessment/*.md`, active completion plan, coordination prompt | Tranche selection, future research references, package/runtime guardrails | Record rulings; supersede Pi adapter/spike language; preserve Pi as reference corpus only |
| A003 provider expansion gate | `docs/CONTRACT.md` K-NET, `docs/SPEC.md` network/provider sections, `docs/PRD.md` NFR/provider scope, decomposition SOW-020, coordination prompt | Security validation, release checks, future adapter work | Current shipped path remains loopback + Anthropic; every concrete new provider needs bounded tranche and validation |
| A004 permission/tool-use posture | `docs/CONTRACT.md` K-PERM/K-TOOL/K-BASH, `docs/SPEC.md` permission and tool sections, `docs/TYPES.md` permission vocabulary, decomposition PKG-06/DEL-06-01/SOW-055 | Permission overlay, tool descriptors, validation, future write/bash/subagent work | Replace blanket deny-first with capability-forward policy mediation and explicit hard-deny precedence |
| A005 active control-plane alignment | `_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, `plans/PLAN_2026-06-13_runtime_completion.md`, `frontend/docs/harness/runtime_engine_contract.md` | Agentic development loop and tranche selection | Stop selecting Pi adapter/spike work; select provider-neutral adapter/governance tranches after approval |

## Decomposition Structure Impact

| Decomposition surface | Impact | Closure requirement |
|---|---|---|
| Gate Log | No status change required. | None. |
| References | Docs hashes become stale if docs are edited. | Recompute or explicitly mark source hashes for refresh during Gate 5. |
| Intake Summary | Must change runtime direction from SDK-privileged / Claude SDK preferred spine to provider-adapter-general / contract-owned / capability-forward. | Direct edit after Gate 3 approval. |
| Vocabulary Map | Must generalize SDK/provider vocabulary and add Pi pattern-corpus vocabulary. | Direct edit after approval. |
| Packages | PKG-04 and PKG-06 descriptions should be generalized; package IDs remain stable. | Direct edit after approval. No folder rename required in this SCA. |
| Deliverables | DEL-04-01, DEL-04-02, DEL-04-03, DEL-04-05, DEL-06-01, DEL-06-02, DEL-06-05, DEL-09-02, DEL-09-06 are semantically affected. | Direct description edits after approval. No deliverable ID changes. |
| Scope Ledger | SOW-018, SOW-020, SOW-044, SOW-045, SOW-050, SOW-055, SOW-062, SOW-063, SOW-064 are likely affected. | Direct row edits after approval. |
| Non-PRD Control Coverage | K-SDK/K-ENGINE/K-PERM/K-NET ownership language must be generalized. | Direct edit after approval. |
| Open Issues | OI-001 and OI-003 should become provider-adapter / first-adapter issues; add or modify an open issue for concrete non-Anthropic provider implementation gates. | Direct edit after approval. |
| Decision Log / Change Log | Add `SCA-APP-001` decision entry. | Direct edit after approval. |

## Package and Deliverable Impact

| Package | Role | Impact |
|---|---|---|
| PKG-01 Product Governance and Reliance Boundaries | Working surface | High semantic impact. Human authority, project truth, reliance boundaries, and scope boundaries must be preserved while permission governance is reframed around human intent alignment and validation gates. DEL-01-01 through DEL-01-04 are affected as review surfaces. |
| PKG-04 SDK Adapter, Prompt, Provider, and Settings | Working surface | High semantic impact. The package must be interpreted as provider-adapter architecture with Claude Agent SDK / Anthropic as first concrete adapter, not as permanent Anthropic-centered scope. DEL-04-01 through DEL-04-05 are affected. |
| PKG-06 Permissioned Tools, MCP, and Hooks | Working surface | High semantic impact. DEL-06-01 and related tool/hook deliverables must implement useful tool enablement through policy-mediated capability exposure and evidence, while preserving explicit deny precedence. |
| PKG-09 Validation, Packaging, Security, and Release | Working surface | Medium impact. Validation must prove provider-adapter boundaries, current network scope, no unauthorized provider expansion, and no package/runtime migration. DEL-09-02 and DEL-09-06 are most affected. |
| PKG-10 Domain Engine Future Boundary | Working surface | Medium impact. Future domain provider/profile work remains human-gated and cannot become a side path for unvalidated provider/network expansion. DEL-10-01 through DEL-10-05 remain future-boundary work. |

## Governance Corpus Impact

| File | Current posture affected | Expected Gate 5 action |
|---|---|---|
| `docs/PRD.md` | Claude Agent SDK preferred spine; Anthropic-only outbound policy; deny-first overlay language. | Generalize runtime direction; keep current shipped adapter path; reframe permission policy. |
| `docs/CONTRACT.md` | K-ENGINE-3, K-PERM-1, K-NET-1, K-BASH-1 are phrased around SDK privilege, deny precedence, Anthropic policy, and bash default. | Preserve hard boundaries while removing blanket suppressive framing; update shipped/current vs strategic/future provider distinction. |
| `docs/SPEC.md` | SDK runtime configuration, SDK tool mapping, permission mapping, and network policy are Claude/Anthropic-centered. | Generalize sections to external provider/SDK adapters; retain Claude SDK as first concrete adapter. |
| `docs/TYPES.md` | Runtime vocabulary and permission vocabulary likely use SDK-specific or deny-first phrasing. | Add/adjust provider-adapter, pattern-corpus, and policy-mediated permission terms. |
| `docs/PLAN.md` | Strategic roadmap makes Claude Agent SDK the preferred runtime spine and says deny-first permission precedence. | Keep roadmap strategic, but shift it to provider-adapter architecture with first-adapter implementation. |

## Coordination and Planning Impact

| Surface | Current conflict | Expected Gate 5 action |
|---|---|---|
| `execution/_Coordination/_COORDINATION.md` | Says Pi is a reference / possible later backend-adapter spike and Claude Agent SDK is current privileged adapter path. | Change to provider-adapter-general focus; Pi pattern corpus only. |
| `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` | Instructs agents to use Pi reference and says Pi may be a possible constrained backend-adapter spike. | Remove Pi spike path; instruct discovery from active provider-general plan and decision register. |
| `plans/PLAN_2026-06-13_runtime_completion.md` | Human decision rows remain NOT_PREPARED; dependency spine includes "Pi adapter packet". | Update D-APP rows after ruling records; replace Pi adapter packet with provider-expansion packet language. |
| `plans/PLAN_COMPLETION_LOG.md` | Historical log only. | Add closeout entry only if Gate 5 lands. |
| `execution/_Coordination/WORKSPACE_MANIFEST.csv` | Index may not include `_ScopeChange` surfaces. | Add scope-change pointer only if desired by coordination policy; not required for Gate 5 validity. |

## Runtime Contract and Pi Assessment Impact

| Surface | Impact |
|---|---|
| `frontend/docs/harness/runtime_engine_contract.md` | Should identify provider adapters generically; Claude Agent SDK / Anthropic remains the current concrete conformance path. |
| `plans/pi-agent-harness-assessment.md` | Must be superseded or amended so Pi is a pattern corpus only, with no adapter/fork/import/spike path. |
| `plans/pi-assessment/*.md` | Must be marked historical/reference or amended to remove active spike/import/sidecar implications. |
| `plans/claude-agent-sdk-implementation-followups.md` | Should be reinterpreted as first-adapter followups, not permanent provider strategy. |

## Derivative-Package Status

| Package / surface | Owner | Status after approved amendment | Required rerun / closure action |
|---|---|---|---|
| Active decomposition markdown | SCOPE_CHANGE | STALE_UNTIL_GATE_5 | Apply approved amendments. |
| Governance docs under `docs/` | Governance / WORKING_ITEMS | STALE_UNTIL_GATE_5 | Apply provider-general and permission-policy edits after approval. |
| Active completion plan | WORKING_ITEMS | STALE_UNTIL_GATE_5 | Update dependency spine and D-APP mirror rows after ruling records. |
| Decision register | Human decision tracking | STALE_UNTIL_GATE_5 | Add ruling records and set D-APP-01/02/03 to RULED. |
| Coordination prompt/policy | WORKING_ITEMS | STALE_UNTIL_GATE_5 | Update next-instance instructions to remove Pi spike language. |
| Runtime contract docs | Runtime governance | STALE_UNTIL_GATE_5 | Generalize adapter language. |
| Pi assessment docs | Reference docs | STALE_UNTIL_GATE_5 | Mark as pattern-corpus reference only or superseded. |
| Source code / tests | Runtime implementation | NO_CHANGE | No rerun required beyond static no-source-change verification. |
| Package manifests / lockfiles / wrappers | Build/runtime platform | NO_CHANGE | Verify no changes. |

## Surface Classification

| Surface | Package role | Classification for this SCA | Authority basis |
|---|---|---|---|
| `execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/` | snapshot / handoff artifact | DIRECT_EDIT | SCOPE_CHANGE owns amendment snapshot artifacts. |
| `execution/_ScopeChange/_LATEST.md` | snapshot pointer | DIRECT_EDIT | SCOPE_CHANGE owns active pointer. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | authoritative working surface | DIRECT_EDIT_AFTER_APPROVAL | Gate 3 and Gate 5 only. |
| `docs/PRD.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md` | governed docs | DIRECT_EDIT_AFTER_APPROVAL | Human plan explicitly includes governance propagation; SCOPE_CHANGE protocol requires approval first. |
| `execution/_Coordination/*` | control-plane surfaces | DIRECT_EDIT_AFTER_APPROVAL | Human plan explicitly includes active coordination and decision register propagation. |
| `plans/*.md` | planning / reference surfaces | DIRECT_EDIT_AFTER_APPROVAL | Human plan explicitly includes completion plan/log and Pi assessment docs. |
| `frontend/docs/harness/runtime_engine_contract.md` | runtime contract doc | DIRECT_EDIT_AFTER_APPROVAL | Human plan explicitly includes runtime contract docs. |
| `frontend/src/**`, package manifests, lockfiles, desktop wrapper files | runtime source / build surfaces | NO_CHANGE | Out of scope. |

## Orphan and Telemetry Risk

| Risk | Assessment |
|---|---|
| Package orphaning | Low. No package add/remove/reclassify is proposed. |
| Deliverable orphaning | Low. No deliverable add/remove/reclassify is proposed. |
| Scope ledger dangling mappings | Low if SOW row text is edited in place. |
| Folder path mismatch | Low to medium if package/deliverable names are generalized but existing folder names retain historical "SDK" wording. This SCA should avoid folder renames unless separately approved. |
| Governance semantic split | High until Gate 5 lands. Active docs currently conflict with the human rulings. |
| Runtime implementation drift | Medium if future runtime tranches proceed before docs/decomposition are aligned. |
| Validation under-specification | Medium. Provider-adapter strategy requires tests that distinguish current shipped adapter from future strategic provider expansion. |

## Recommended Downstream Reruns

After Gate 5 approval and edits:

1. Run static governance checks listed in `Propagation_Plan.md`.
2. Run targeted grep checks for stale Pi adapter/spike/import language.
3. Run targeted grep checks for blanket "deny-first" language and ensure remaining instances mean explicit deny precedence.
4. Validate `docs/MANIFEST.json` if it changes.
5. Run `git diff --check -- docs plans execution frontend/docs/harness`.
6. No frontend test suite is required unless source or runtime docs with generated validation hooks are changed beyond prose.
