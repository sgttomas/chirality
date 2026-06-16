# Source Pack: SRC-EGOV-SCOPECHANGE-SCA-APP-001-2026-06-13-1755-PROVIDER-GENERAL-RUNTIME-PI-PATTERN-CORPUS

Grouping: `GROUPED_FOLDER`  RepoGlob: `execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/Amendment_Preview.md

### SCA-APP-001 Amendment Preview

**Package Role:** snapshot / handoff artifact
**Gate:** 3 - Amendment Approval
**Status:** PREVIEW_PENDING_HUMAN_APPROVAL

This file previews exact amendment intent. It does not apply changes to decomposition truth or governed docs.

#### Decomposition Amendments

##### Section 2.2 - v3.2 Revision Posture

Current invariant:

```text
no implementation work that exposes write, bash, subagent execution, remote MCP, plugins, or domain operations ahead of PLAN sequencing;
```

Proposed replacement:

```text
no implementation work that exposes write, bash, subagent execution, remote MCP, plugins, unvalidated provider/network expansion, or domain operations ahead of the approved provider-adapter and capability-policy sequencing;
```

##### Section 3 - Intake Summary

Current strategic paragraph:

```text
The approved runtime direction is SDK-privileged, contract-owned, and Chirality-governed. The Claude Agent SDK is the preferred engine for generic agent-loop mechanics, but Chirality owns the runtime contract, permission semantics, audit mirror, filesystem boundaries, persona composition, professional boundaries, and fallback criteria.
```

Proposed replacement:

```text
The approved runtime direction is provider-adapter-general, contract-owned, and Chirality-governed. Chirality owns the runtime contract, permission semantics, audit mirror, filesystem boundaries, persona composition, professional boundaries, and fallback criteria. External provider SDKs may supply agent-loop mechanics only behind Chirality adapters. The Claude Agent SDK / Anthropic path remains the first concrete adapter and current shipped path; concrete non-Anthropic adapters require bounded future implementation tranches and validation.
```

Current implementation objective paragraph:

```text
The next implementation objective is to mature the existing desktop shell into a governed runtime by establishing `AgentEnginePort` / `RuntimeEngineContract`, SDK conformance, SDK-backed `TurnEngine`, append-only `HarnessEvent` JSONL, prompt/persona composition, settings isolation, run logging, and a reliance-boundary register before expanding read tools, writes, bash, subagents, or domain-engine profiles.
```

Proposed replacement:

```text
The next implementation objective is to mature the existing desktop shell into a governed provider-adapter runtime by establishing `AgentEnginePort` / `RuntimeEngineContract`, adapter conformance, the first Claude Agent SDK / Anthropic-backed `TurnEngine`, append-only `HarnessEvent` JSONL, prompt/persona composition, settings isolation, run logging, and a reliance-boundary register before expanding read tools, writes, bash, subagents, concrete non-Anthropic providers, or domain-engine profiles.
```

##### Section 3 - Hard Constraints Captured

Proposed row-level edits:

| Current | Proposed |
|---|---|
| R0/R1 runtime contract and SDK adoption remain the immediate implementation slice. | R0/R1 runtime contract, provider-adapter architecture, and the first Claude Agent SDK / Anthropic adapter remain the immediate implementation slice. |
| `allowedTools` alone is not a restriction boundary. | Tool availability alone is not a restriction boundary; exposure requires capability policy, explicit deny precedence, hooks where needed, and evidence records. |
| Write, bash, subagent, remote MCP, plugin, and domain-operation capabilities remain gated until governance deliverables pass validation. | Write, bash, subagent, remote MCP, plugin, concrete non-Anthropic provider, and domain-operation capabilities remain gated until their governance and validation deliverables pass. |
| P0 reliance boundaries must be enforced by Chirality code, verified SDK callbacks/hooks, deterministic tools, release checks, or human gates; prompt text alone is insufficient. | P0 reliance boundaries must be enforced by Chirality code, verified adapter callbacks/hooks, deterministic tools, release checks, or human gates; prompt text alone is insufficient. |

Add hard constraint:

```text
Pi is a pattern corpus / reference source only. This amendment authorizes no Pi adapter, fork, direct package import, Node 22 sidecar, runtime-floor change, or immediate Pi spike.
```

Add hard constraint:

```text
Permission governance is capability-forward and policy-mediated. Useful agent tool use is enabled when allowed by mode, boundary policy, evidence capture, and human gates. Explicit hard denies override allows at reliance boundaries, secrets, protected paths, release/professional claims, destructive actions, and unvalidated provider/network expansion.
```

##### Section 4 - Vocabulary Map

Proposed additions / modifications:

| Term | Proposed definition |
|---|---|
| EngineAdapter | Provider or SDK adapter behind Chirality-owned contracts. Provider-specific terms, events, sessions, permission modes, and tool names are translated at this boundary. |
| Provider Adapter | Concrete integration layer for an external agent provider or SDK. The current shipped concrete adapter is Claude Agent SDK / Anthropic. |
| Pi Pattern Corpus | Reference corpus for stable agentic patterns observed in Pi packages and behavior. It is not a runtime dependency, adapter target, fork target, or package import path. |
| Capability Policy | Chirality policy that decides which tools/capabilities are exposed and executable for a session, persona, mode, provider adapter, and validation state. |
| Explicit Deny Precedence | A hard-deny rule that overrides allows at defined reliance, secret, protected-path, professional, destructive-action, or unvalidated expansion boundaries. This replaces blanket "deny-first" as the governing posture. |

##### Section 7 - Packages

Proposed package description changes:

| Package | Proposed description adjustment |
|---|---|
| PKG-04 | Interpret the package as provider-adapter, prompt, first-adapter SDK, provider, and settings work. Keep the current package ID and folder path; no rename is required in this SCA. |
| PKG-06 | Replace "deny-first permission overlay" with "capability-forward permission policy with explicit deny precedence, tool exposure, MCP wrappers, hooks, writes, bash, and compaction hooks." |
| PKG-09 | Add validation responsibility for provider-adapter conformance and no unauthorized provider/network expansion. |

##### Section 8 - Deliverables

Proposed deliverable description changes:

| Deliverable | Proposed adjustment |
|---|---|
| DEL-04-01 | Probe provider-adapter viability and Claude Agent SDK / Anthropic as first concrete adapter; record fallback and future-provider criteria. |
| DEL-04-02 | Build deterministic adapter options from session, persona, mode, tools, hooks, MCP, subagents, resume, and settings policy. |
| DEL-04-03 | Translate provider/SDK stream messages into stable `UIEvent`s and provider-neutral `HarnessEvent`s. |
| DEL-04-05 | Preserve API key precedence, current Anthropic network policy, provider error classification, and redacted adapter environment handoff for the current shipped path. |
| DEL-06-01 | Implement structured permission decisions, explicit deny precedence, capability-policy mode mapping, and `canUseTool` approval mediation. |
| DEL-06-02 | Resolve requested tools to provider/SDK built-ins or Chirality MCP names while preserving read-before-write rollout. |
| DEL-06-05 | Keep Bash unavailable unless explicitly enabled by a governed mode and validated timeout/capture/output/audit behavior. |
| DEL-09-02 | Add runtime validation IDs for provider-adapter conformance, first-adapter mapper, event log, settings isolation, permissions, MCP, hooks, compaction, and subagents. |
| DEL-09-06 | Verify renderer allowlist, API key redaction/storage, current provider endpoint policy, and no unauthorized provider/network expansion. |

##### Section 9 - Scope Ledger

Proposed row text edits:

| SOW | Proposed change |
|---|---|
| SOW-018 | Change "SDK-backed Anthropic runtime path" to "Provider-adapter runtime path with Claude Agent SDK / Anthropic as first concrete adapter." |
| SOW-020 | Change "Base URL and network allowlist" to "Provider endpoint and network allowlist for current shipped adapter; concrete provider expansion requires bounded future tranche." |
| SOW-044 | Change "SDK message mapping" to "Provider/SDK message mapping into Chirality contracts." |
| SOW-045 | Change "SDK settings isolation" to "Provider/SDK settings isolation, with Claude Agent SDK settings isolation required for the current shipped adapter." |
| SOW-050 | Preserve "Read tools before writes/bash" as rollout sequencing, not a blanket denial of useful tool use. |
| SOW-055 | Change "Permission modes and deny-first overlay" to "Permission modes, capability policy, and explicit deny precedence." |
| SOW-062 | Preserve Bash as denied until explicitly governed and validated, without using Bash as a reason to suppress unrelated read/tool capability. |
| SOW-063 | Governed subagent runtime remains future-gated and provider-adapter-aware. |
| SOW-064 | MCP extension boundaries remain governed and cannot bypass adapter/permission/hook policy. |

##### Section 10A - Non-PRD Control Coverage

Proposed coverage edits:

- Replace "SDK isolation, conformance, fallback" with "provider/SDK adapter isolation, first-adapter conformance, fallback."
- Replace "Deny-first policy" with "capability policy with explicit deny precedence."
- Add provider/network expansion checks under `K-NET`, `K-KEY`, `K-RELEASE`, and `K-VALIDATE` coverage.

##### Section 11 - Open Issues

Proposed changes:

| Issue | Proposed change |
|---|---|
| OI-001 | Reword as first-adapter probe: Claude Agent SDK / Anthropic viability, message categories, settings behavior, hooks, permissions, MCP, sessions, and packaging. |
| OI-003 | Keep packaging issue for the first adapter and avoid implying all future provider packaging is solved. |
| OI-006 | Add new provider-expansion issue: concrete non-Anthropic adapters require bounded implementation tranches, provider-network policy, conformance fixtures, error classification, and release/security checks. |
| OI-007 | Add Pi pattern-corpus issue if useful: Pi reference review may inform architecture, but no adapter/fork/import/spike is authorized. |

##### Section 12 - Decision Log / Change Log

Add decision:

```text
| DEC-017 | 2026-06-13 | SCA-APP-001 reorients runtime strategy to provider-adapter generality, keeps Claude Agent SDK / Anthropic as first concrete adapter, treats Pi as a pattern corpus only, and reframes permission governance as capability-forward with explicit deny precedence. | Human ruled D-APP-01/02/03 and requested formal SCOPE_CHANGE before project-truth mutation. |
```

Add change-log line:

```text
- 2026-06-13: SCA-APP-001 preview prepared for provider-general runtime and Pi pattern-corpus reorientation; authoritative edits pending human approval.
```

#### Governance Doc Amendments

These are proposed propagation amendments, not applied edits.

| File | Proposed amendment |
|---|---|
| `docs/PRD.md` | Replace Claude-SDK-only strategic framing with provider-adapter architecture. Keep Claude Agent SDK / Anthropic as first concrete shipped adapter. Replace "Anthropic-only" as strategic policy with "current shipped provider scope is loopback plus Anthropic; new providers require bounded tranches." Reframe deny-first language as explicit deny precedence within capability policy. |
| `docs/CONTRACT.md` | Amend K-ENGINE/K-SDK wording so external SDKs/providers are adapter substrates, not governance authorities. Amend K-PERM so explicit deny precedence remains hard while useful tool capability can be exposed through policy. Amend K-NET so provider-general strategy is approved but current shipped network remains bounded. |
| `docs/SPEC.md` | Generalize SDK runtime configuration, message mapping, tool surface, permission mapping, and network policy to provider/SDK adapters. Keep first concrete adapter details where implementation is current. |
| `docs/TYPES.md` | Add or adjust vocabulary for provider adapters, first adapter, Pi pattern corpus, capability policy, and explicit deny precedence. |
| `docs/PLAN.md` | Update strategic roadmap to describe provider-adapter runtime with Claude Agent SDK / Anthropic as first adapter. Keep read-before-write/bash sequencing and human gates. |

#### Decision Records

Proposed decision register state after Gate 5:

| ID | State | Ruling record |
|---|---|---|
| D-APP-01 | RULED | `execution/_Coordination/_DECISIONS/D-APP-01_RULING_2026-06-13.md` |
| D-APP-02 | RULED | `execution/_Coordination/_DECISIONS/D-APP-02_RULING_2026-06-13.md` |
| D-APP-03 | RULED | `execution/_Coordination/_DECISIONS/D-APP-03_RULING_2026-06-13.md` |

#### Control-Plane Amendments

| File | Proposed amendment |
|---|---|
| `execution/_Coordination/_COORDINATION.md` | Current strategic focus becomes provider-adapter-general Chirality runtime, Claude Agent SDK / Anthropic first concrete adapter, Pi pattern corpus only. |
| `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` | Next agents read active plan/coordination/decision register, select one earliest unblocked item, and treat provider-general work as governance-approved but implementation-bounded. |
| `plans/PLAN_2026-06-13_runtime_completion.md` | Replace "Pi adapter packet" with "provider expansion packet / future adapter packet" and update D-APP mirror rows to RULED after ruling records exist. |
| `frontend/docs/harness/runtime_engine_contract.md` | Generalize adapter contract wording while preserving current concrete adapter path. |
| `plans/pi-agent-harness-assessment.md` and `plans/pi-assessment/*.md` | Mark as pattern-corpus references or superseded by SCA-APP-001; remove active Pi spike/import/sidecar implications. |

#### Gate 3 Approval Question

Do you approve these amendments to the decomposition document and the proposed governance/control-plane propagation surfaces for Gate 5 execution?

## Component: execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/Brief.md

### SCA-APP-001 Brief

**Package Role:** snapshot / handoff artifact
**Amendment label:** `SCA-APP-001 Provider-General Runtime and Pi Pattern-Corpus Reorientation`
**Date:** 2026-06-13
**DECOMP_VARIANT:** SOFTWARE
**CONTEXT_ROOT:** `execution`
**DECOMPOSITION_PATH:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**SCOPE_CHANGE_ROOT:** `execution/_ScopeChange/`
**Gate state:** Gates 1-4 preview prepared; Gate 5 not executed.

#### Human Change Request

The human ruled the active D-APP decisions and requested a formal SCOPE_CHANGE before mutating governance or decomposition truth.

The requested strategic change is:

- D-APP-01: Pi is a strong pattern corpus / reference for stable agentic work patterns. Do not build a Pi adapter, fork Pi, import Pi packages, or run an immediate Pi spike.
- D-APP-02: Study and adapt Pi package patterns, but do not import Pi packages and do not change the Chirality runtime floor or introduce a Node 22 sidecar for Pi.
- D-APP-03: Approve the strategic shift from Anthropic-centered runtime scope to provider-adapter generality. Anthropic / Claude Agent SDK remains the first concrete adapter and current shipped path. Concrete new providers require bounded future implementation tranches.
- Governance should support effective agent tool use by aligning with human intention, evidence, and validation gates. It should not use a blanket "deny-first" posture to suppress useful agent behavior. Explicit hard-deny precedence still applies at reliance boundaries, secrets, protected paths, release/professional claims, destructive actions, and unvalidated provider/network expansion.

#### Gate 1 Resolution

| Variable | Resolved value |
|---|---|
| `DECOMP_VARIANT` | SOFTWARE |
| `CONTEXT_ROOT` | `execution` |
| `DECOMPOSITION_PATH` | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| `SCOPE_CHANGE_ROOT` | `execution/_ScopeChange/` |
| `ALLOW_RENUMBERING` | false |

#### Parsed Atomic Actions

| ActionSeq | ActionType | EntityType | EntityID | RequestedChange | AffectedSections |
|---|---|---|---|---|---|
| A001 | MODIFY | Runtime strategy | DEC-005, SOW-018, SOW-044, SOW-045, PKG-04 | Replace Anthropic-centered / Claude-SDK-only strategic language with provider-adapter architecture language while retaining Anthropic / Claude Agent SDK as first concrete adapter. | Intake Summary, Vocabulary Map, Packages, Deliverables, Scope Ledger, Open Issues, Decision Log |
| A002 | MODIFY | Pi posture | D-APP-01, D-APP-02 | Reclassify Pi from possible adapter/spike/package path to pattern corpus / reference only. Prohibit Pi adapter, fork, direct import, Node 22 sidecar, or immediate spike. | Coordination docs, decision register, Pi assessment plans, runtime completion plan |
| A003 | MODIFY | Provider expansion gate | D-APP-03, K-NET-1, SOW-020 | Record strategic approval for provider-adapter generality while requiring bounded future implementation tranches and validation for every concrete non-Anthropic provider. | CONTRACT, SPEC, PRD, PLAN, decomposition scope ledger, coordination docs |
| A004 | MODIFY | Permission / tool-use posture | K-PERM-1, K-PERM-3, SOW-055, DEL-06-01 | Replace blanket "deny-first" framing with capability-forward, policy-mediated, evidence-recorded tool use. Preserve explicit deny precedence at hard boundaries. | CONTRACT, SPEC, TYPES, PLAN, PRD, decomposition hard constraints, PKG-06 descriptions |
| A005 | MODIFY | Active planning and governance surfaces | D-APP register, active completion plan, coordination prompt, runtime contract docs | Align active coordination and planning documents to select future runtime tranches from the provider-general spine and stop presenting Pi adapter/spike work as active future intent. | `_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, `plans/PLAN_2026-06-13_runtime_completion.md`, `frontend/docs/harness/runtime_engine_contract.md` |

#### Gate 1 Validation

| Check | Result | Notes |
|---|---|---|
| Human initiated | PASS | Request was explicit in chat and supplied a SCOPE_CHANGE plan. |
| Variant and path resolved | PASS | Active SOFTWARE_DECOMP file exists at the requested path. |
| Stable IDs preserved | PASS | The preview does not add, remove, split, merge, reclassify, or renumber packages, deliverables, objectives, or SOW IDs. |
| Parent closure risk | PASS | No parent package or deliverable is removed or moved. |
| Structural contract change | WARNING | The amendment changes runtime strategy semantics and permission-governance interpretation. This is a contract-level governance change and requires explicit approval before Gate 5. |
| Direct runtime mutation | PASS | No source, package, lockfile, dependency, runtime-language, or wrapper changes are proposed. |

#### Gate 1 Confirmation State

The human plan is treated as authority to prepare this SCOPE_CHANGE preview package. It is not treated as Gate 3 / Gate 4 approval of exact text because those exact amendments are first drafted in this snapshot.

## Component: execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/Handoff_State.md

### SCA-APP-001 Handoff State

**Package Role:** snapshot / handoff artifact
**Status:** OPEN_PENDING_HUMAN_APPROVAL
**Accepted amendment snapshot:** none yet
**Pending preview snapshot:** `execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/`

#### Fixed State Fields

| Field | Value | Evidence |
|---|---|---|
| `DecompositionTruthState` | INCOMPLETE | No authoritative decomposition edits have been applied. |
| `DerivativePackageState` | INCOMPLETE | Governance/control-plane surfaces remain stale relative to the human rulings. |
| `ContentRemediationState` | NOT_REQUIRED | This is SOFTWARE SCOPE_CHANGE; no KTY remediation applies. |
| `DownstreamRerunState` | FROZEN | Downstream reruns are advisory after Gate 5 and not started. |
| `MetadataAlignmentState` | NOT_REQUIRED | No KTY metadata alignment applies. |
| `AuditState` | WARNINGS | Preview/static assessment only; no post-change validation yet. |
| `ReadyForNextPhase` | NO | Human approval and Gate 5 execution are required. |

#### Authoritative Truth Changed In This Run

None. This run created a SCOPE_CHANGE preview snapshot only.

#### Pending Authoritative Changes

| Surface | Status | Next required action |
|---|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | STALE_PENDING_APPROVAL | Apply approved Gate 3 amendments at Gate 5. |
| `docs/PRD.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md` | STALE_PENDING_APPROVAL | Apply approved governance propagation at Gate 5. |
| `execution/_Coordination/_DECISIONS/_REGISTER.md` | STALE_PENDING_APPROVAL | Add D-APP ruling records and update rows at Gate 5. |
| Active completion/coordination docs | STALE_PENDING_APPROVAL | Remove Pi adapter/spike selection language and update provider-general focus at Gate 5. |
| Runtime contract and Pi assessment docs | STALE_PENDING_APPROVAL | Generalize adapter language and mark Pi as pattern corpus only at Gate 5. |

#### Derivative-Package State

| Package / surface | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Decomposition package | SCOPE_CHANGE | STALE_PENDING_APPROVAL | `Amendment_Preview.md` | Human approval, then Gate 5 edits. |
| Governance docs | WORKING_ITEMS / governance | STALE_PENDING_APPROVAL | `Impact_Assessment.md` | Human approval, then Gate 5 edits. |
| Coordination and planning | WORKING_ITEMS | STALE_PENDING_APPROVAL | `Propagation_Plan.md` | Human approval, then Gate 5 edits. |
| Runtime source | Runtime implementation owner | CURRENT_NO_CHANGE | No source writes in this preview | No action in this SCA. |

#### Active Snapshot State

| Item | State |
|---|---|
| Snapshot folder exists | YES |
| `_LATEST.md` points to this snapshot | YES |
| Required preview artifacts exist | YES |
| Gate 5 closure artifacts finalized | NO |
| Post-change coverage available | NO |

#### Remaining Blockers

1. Human must accept the impact assessment.
2. Human must approve the amendment preview.
3. Human must approve the propagation plan.
4. Gate 5 must then apply and validate the approved changes.

#### Next Owning Workflow

SCOPE_CHANGE remains the owner until Gate 5 completes or the human rejects/modifies the preview. CHANGE should only own staging/commit/push after a validated closeout or a deliberately committed preview package.

## Component: execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/Impact_Assessment.md

### SCA-APP-001 Impact Assessment

**Package Role:** snapshot / handoff artifact
**Gate:** 2 - Impact Assessment
**Status:** PREVIEW_PENDING_HUMAN_ACCEPTANCE

This assessment covers the requested provider-general runtime and Pi pattern-corpus reorientation. It is based on the active decomposition, active governance docs, current coordination docs, active completion plan, decision register, runtime contract docs, and Pi assessment plans.

#### Summary

The change is a semantic and governance amendment, not a topology amendment. It does not require new package IDs, deliverable IDs, source files, dependencies, lockfiles, runtime wrappers, or package manifests. It does require coordinated edits to decomposition truth and governance/control-plane documents if approved.

The highest-risk inconsistency is leaving the current docs split between:

- existing Anthropic / Claude Agent SDK privileged wording;
- existing Pi adapter / spike possibility wording;
- existing "deny-first" blanket phrasing;
- the human's new provider-general and Pi-pattern-corpus rulings.

Until Gate 5 is approved and executed, active project truth remains unchanged and those conflicts remain intentionally visible.

#### Impact Summary

| Action | Affected sections/files | Affected workflows | Required closure action |
|---|---|---|---|
| A001 provider-adapter strategy | `docs/PRD.md`, `docs/PLAN.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, decomposition sections 3, 4, 7, 8, 9, 10A, 11, 12 | Runtime planning, adapter design, validation planning, future provider implementation selection | Gate 5 direct edits after approval; hash/reference posture reviewed after docs changes |
| A002 Pi pattern-corpus posture | `execution/_Coordination/_DECISIONS/_REGISTER.md`, new ruling records, `plans/pi-agent-harness-assessment.md`, `plans/pi-assessment/*.md`, active completion plan, coordination prompt | Tranche selection, future research references, package/runtime guardrails | Record rulings; supersede Pi adapter/spike language; preserve Pi as reference corpus only |
| A003 provider expansion gate | `docs/CONTRACT.md` K-NET, `docs/SPEC.md` network/provider sections, `docs/PRD.md` NFR/provider scope, decomposition SOW-020, coordination prompt | Security validation, release checks, future adapter work | Current shipped path remains loopback + Anthropic; every concrete new provider needs bounded tranche and validation |
| A004 permission/tool-use posture | `docs/CONTRACT.md` K-PERM/K-TOOL/K-BASH, `docs/SPEC.md` permission and tool sections, `docs/TYPES.md` permission vocabulary, decomposition PKG-06/DEL-06-01/SOW-055 | Permission overlay, tool descriptors, validation, future write/bash/subagent work | Replace blanket deny-first with capability-forward policy mediation and explicit hard-deny precedence |
| A005 active control-plane alignment | `_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, `plans/PLAN_2026-06-13_runtime_completion.md`, `frontend/docs/harness/runtime_engine_contract.md` | Agentic development loop and tranche selection | Stop selecting Pi adapter/spike work; select provider-neutral adapter/governance tranches after approval |

#### Decomposition Structure Impact

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

#### Package and Deliverable Impact

| Package | Role | Impact |
|---|---|---|
| PKG-01 Product Governance and Reliance Boundaries | Working surface | High semantic impact. Human authority, project truth, reliance boundaries, and scope boundaries must be preserved while permission governance is reframed around human intent alignment and validation gates. DEL-01-01 through DEL-01-04 are affected as review surfaces. |
| PKG-04 SDK Adapter, Prompt, Provider, and Settings | Working surface | High semantic impact. The package must be interpreted as provider-adapter architecture with Claude Agent SDK / Anthropic as first concrete adapter, not as permanent Anthropic-centered scope. DEL-04-01 through DEL-04-05 are affected. |
| PKG-06 Permissioned Tools, MCP, and Hooks | Working surface | High semantic impact. DEL-06-01 and related tool/hook deliverables must implement useful tool enablement through policy-mediated capability exposure and evidence, while preserving explicit deny precedence. |
| PKG-09 Validation, Packaging, Security, and Release | Working surface | Medium impact. Validation must prove provider-adapter boundaries, current network scope, no unauthorized provider expansion, and no package/runtime migration. DEL-09-02 and DEL-09-06 are most affected. |
| PKG-10 Domain Engine Future Boundary | Working surface | Medium impact. Future domain provider/profile work remains human-gated and cannot become a side path for unvalidated provider/network expansion. DEL-10-01 through DEL-10-05 remain future-boundary work. |

#### Governance Corpus Impact

| File | Current posture affected | Expected Gate 5 action |
|---|---|---|
| `docs/PRD.md` | Claude Agent SDK preferred spine; Anthropic-only outbound policy; deny-first overlay language. | Generalize runtime direction; keep current shipped adapter path; reframe permission policy. |
| `docs/CONTRACT.md` | K-ENGINE-3, K-PERM-1, K-NET-1, K-BASH-1 are phrased around SDK privilege, deny precedence, Anthropic policy, and bash default. | Preserve hard boundaries while removing blanket suppressive framing; update shipped/current vs strategic/future provider distinction. |
| `docs/SPEC.md` | SDK runtime configuration, SDK tool mapping, permission mapping, and network policy are Claude/Anthropic-centered. | Generalize sections to external provider/SDK adapters; retain Claude SDK as first concrete adapter. |
| `docs/TYPES.md` | Runtime vocabulary and permission vocabulary likely use SDK-specific or deny-first phrasing. | Add/adjust provider-adapter, pattern-corpus, and policy-mediated permission terms. |
| `docs/PLAN.md` | Strategic roadmap makes Claude Agent SDK the preferred runtime spine and says deny-first permission precedence. | Keep roadmap strategic, but shift it to provider-adapter architecture with first-adapter implementation. |

#### Coordination and Planning Impact

| Surface | Current conflict | Expected Gate 5 action |
|---|---|---|
| `execution/_Coordination/_COORDINATION.md` | Says Pi is a reference / possible later backend-adapter spike and Claude Agent SDK is current privileged adapter path. | Change to provider-adapter-general focus; Pi pattern corpus only. |
| `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` | Instructs agents to use Pi reference and says Pi may be a possible constrained backend-adapter spike. | Remove Pi spike path; instruct discovery from active provider-general plan and decision register. |
| `plans/PLAN_2026-06-13_runtime_completion.md` | Human decision rows remain NOT_PREPARED; dependency spine includes "Pi adapter packet". | Update D-APP rows after ruling records; replace Pi adapter packet with provider-expansion packet language. |
| `plans/PLAN_COMPLETION_LOG.md` | Historical log only. | Add closeout entry only if Gate 5 lands. |
| `execution/_Coordination/WORKSPACE_MANIFEST.csv` | Index may not include `_ScopeChange` surfaces. | Add scope-change pointer only if desired by coordination policy; not required for Gate 5 validity. |

#### Runtime Contract and Pi Assessment Impact

| Surface | Impact |
|---|---|
| `frontend/docs/harness/runtime_engine_contract.md` | Should identify provider adapters generically; Claude Agent SDK / Anthropic remains the current concrete conformance path. |
| `plans/pi-agent-harness-assessment.md` | Must be superseded or amended so Pi is a pattern corpus only, with no adapter/fork/import/spike path. |
| `plans/pi-assessment/*.md` | Must be marked historical/reference or amended to remove active spike/import/sidecar implications. |
| `plans/claude-agent-sdk-implementation-followups.md` | Should be reinterpreted as first-adapter followups, not permanent provider strategy. |

#### Derivative-Package Status

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

#### Surface Classification

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

#### Orphan and Telemetry Risk

| Risk | Assessment |
|---|---|
| Package orphaning | Low. No package add/remove/reclassify is proposed. |
| Deliverable orphaning | Low. No deliverable add/remove/reclassify is proposed. |
| Scope ledger dangling mappings | Low if SOW row text is edited in place. |
| Folder path mismatch | Low to medium if package/deliverable names are generalized but existing folder names retain historical "SDK" wording. This SCA should avoid folder renames unless separately approved. |
| Governance semantic split | High until Gate 5 lands. Active docs currently conflict with the human rulings. |
| Runtime implementation drift | Medium if future runtime tranches proceed before docs/decomposition are aligned. |
| Validation under-specification | Medium. Provider-adapter strategy requires tests that distinguish current shipped adapter from future strategic provider expansion. |

#### Recommended Downstream Reruns

After Gate 5 approval and edits:

1. Run static governance checks listed in `Propagation_Plan.md`.
2. Run targeted grep checks for stale Pi adapter/spike/import language.
3. Run targeted grep checks for blanket "deny-first" language and ensure remaining instances mean explicit deny precedence.
4. Validate `docs/MANIFEST.json` if it changes.
5. Run `git diff --check -- docs plans execution frontend/docs/harness`.
6. No frontend test suite is required unless source or runtime docs with generated validation hooks are changed beyond prose.

## Component: execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/Propagation_Plan.md

### SCA-APP-001 Propagation Plan

**Package Role:** snapshot / handoff artifact
**Gate:** 4 - Propagation Plan Approval
**Status:** PREVIEW_PENDING_HUMAN_APPROVAL

This plan is limited to governance, decomposition, coordination, planning, and runtime-contract documentation. It excludes runtime source, package manifests, dependencies, lockfiles, coding-language migrations, desktop wrapper changes, Pi imports, Pi adapter work, and concrete non-Anthropic provider implementation.

#### Approved-After-Human-Acceptance Write Scope

| Surface | Gate 5 action |
|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Apply approved semantic amendments; preserve IDs and topology. |
| `execution/_ScopeChange/SCA-APP-001_2026-06-13_1755_Provider-General_Runtime_Pi_Pattern-Corpus/` | Update RUN_SUMMARY/Handoff/Post_Change_Coverage after Gate 5. |
| `execution/_Coordination/_DECISIONS/_REGISTER.md` | Set D-APP-01/02/03 to RULED and point to ruling records. |
| `execution/_Coordination/_DECISIONS/D-APP-*_RULING_2026-06-13.md` | Create ruling records from the human rulings and SCA approval. |
| `docs/PRD.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md` | Apply provider-general, Pi pattern-corpus, and capability-policy amendments. |
| `execution/_Coordination/_COORDINATION.md`, `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` | Align active agentic-development loop to approved strategy. |
| `plans/PLAN_2026-06-13_runtime_completion.md` | Update active queue and decision mirror. |
| `plans/PLAN_COMPLETION_LOG.md` | Add closeout entry only after Gate 5 lands. |
| `frontend/docs/harness/runtime_engine_contract.md` | Align runtime adapter contract docs. |
| `plans/pi-agent-harness-assessment.md`, `plans/pi-assessment/*.md`, `plans/claude-agent-sdk-implementation-followups.md` | Mark Pi as pattern corpus only and Claude SDK work as first-adapter work. |

#### Explicit No-Write Scope

| Surface | Reason |
|---|---|
| `frontend/src/**` | Runtime implementation is out of scope. |
| `package.json`, package manifests, lockfiles | No dependency/runtime-floor/wrapper migration authorized. |
| desktop wrapper files | No application wrapper migration authorized. |
| Pi package import paths | D-APP-01 and D-APP-02 prohibit import/fork/adapter/spike work. |
| concrete non-Anthropic provider code | D-APP-03 approves strategy only; implementation requires future bounded tranche. |

#### Gate 5 Steps

1. Apply decomposition text amendments exactly as approved in `Amendment_Preview.md`.
2. Create D-APP ruling records and update `_DECISIONS/_REGISTER.md`.
3. Update `docs/PRD.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, and `docs/PLAN.md`.
4. Update active coordination and completion-plan surfaces.
5. Update runtime contract docs and Pi/SDK reference plans.
6. Update this SCA snapshot:
   - `Post_Change_Coverage.json`
   - `Decision_Log.md`
   - `Handoff_State.md`
   - `RUN_SUMMARY.md`
7. Run static validation.
8. Stage, commit, and push the validated Gate 5 tranche.

#### Downstream Rerun Advisory

| Downstream owner | Required after Gate 5? | Notes |
|---|---|---|
| Dependency extraction / SCC graph | Advisory | Topology does not change, but provider-general semantics may alter future tranche selection. No immediate dependency CSV rewrite is required by this SCA. |
| REVIEW / governance audit | Advisory | Recommended after docs/decomposition alignment if release claims are later considered. |
| Runtime tests | Not required by this SCA | No source code changes are authorized. |
| Frontend test suite | Not required by this SCA | No frontend behavior changes are authorized. |
| Build/release checks | Not required by this SCA | No build/package changes are authorized. |

#### Validation Plan

Run after Gate 5 edits:

```bash
git diff --check -- docs plans execution frontend/docs/harness
node -e "JSON.parse(require('fs').readFileSync('docs/MANIFEST.json','utf8'))"
rg "possible later.*Pi|Pi adapter|pi-ai|pi-agent-core|Node 22 sidecar|runtime floor.*Pi" docs plans execution frontend/docs/harness
rg "deny-first" docs plans execution frontend/docs/harness
git diff --name-only -- frontend/src package.json package-lock.json pnpm-lock.yaml yarn.lock desktop electron
```

Expected results:

- `git diff --check` passes.
- `docs/MANIFEST.json` parses if changed.
- Pi adapter/import/spike language is absent from active instruction/planning docs, except historical references explicitly marked superseded or prohibited.
- Any remaining `deny-first` wording is either historical or explicitly means hard-deny precedence, not blanket tool suppression.
- No source/package/runtime-wrapper files are modified.

#### Closure Criteria

Gate 5 can close only when:

- the decomposition document contains the SCA decision entry;
- D-APP-01/02/03 ruling records exist and the register rows are RULED;
- active coordination and completion plan no longer select Pi adapter/spike work;
- active strategy says provider-adapter generality is approved, while concrete new providers remain future bounded implementation items;
- the SCA handoff state records changed surfaces, stale/deferred surfaces, validation, and next recommended runtime tranche;
- no runtime source, package manifests, dependencies, lockfiles, or desktop wrapper files are modified.
