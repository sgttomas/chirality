# SCA-APP-001 Brief

**Package Role:** snapshot / handoff artifact
**Amendment label:** `SCA-APP-001 Provider-General Runtime and Pi Pattern-Corpus Reorientation`
**Date:** 2026-06-13
**DECOMP_VARIANT:** SOFTWARE
**CONTEXT_ROOT:** `execution`
**DECOMPOSITION_PATH:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**SCOPE_CHANGE_ROOT:** `execution/_ScopeChange/`
**Gate state:** Gates 1-4 preview prepared; Gate 5 not executed.

## Human Change Request

The human ruled the active D-APP decisions and requested a formal SCOPE_CHANGE before mutating governance or decomposition truth.

The requested strategic change is:

- D-APP-01: Pi is a strong pattern corpus / reference for stable agentic work patterns. Do not build a Pi adapter, fork Pi, import Pi packages, or run an immediate Pi spike.
- D-APP-02: Study and adapt Pi package patterns, but do not import Pi packages and do not change the Chirality runtime floor or introduce a Node 22 sidecar for Pi.
- D-APP-03: Approve the strategic shift from Anthropic-centered runtime scope to provider-adapter generality. Anthropic / Claude Agent SDK remains the first concrete adapter and current shipped path. Concrete new providers require bounded future implementation tranches.
- Governance should support effective agent tool use by aligning with human intention, evidence, and validation gates. It should not use a blanket "deny-first" posture to suppress useful agent behavior. Explicit hard-deny precedence still applies at reliance boundaries, secrets, protected paths, release/professional claims, destructive actions, and unvalidated provider/network expansion.

## Gate 1 Resolution

| Variable | Resolved value |
|---|---|
| `DECOMP_VARIANT` | SOFTWARE |
| `CONTEXT_ROOT` | `execution` |
| `DECOMPOSITION_PATH` | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| `SCOPE_CHANGE_ROOT` | `execution/_ScopeChange/` |
| `ALLOW_RENUMBERING` | false |

## Parsed Atomic Actions

| ActionSeq | ActionType | EntityType | EntityID | RequestedChange | AffectedSections |
|---|---|---|---|---|---|
| A001 | MODIFY | Runtime strategy | DEC-005, SOW-018, SOW-044, SOW-045, PKG-04 | Replace Anthropic-centered / Claude-SDK-only strategic language with provider-adapter architecture language while retaining Anthropic / Claude Agent SDK as first concrete adapter. | Intake Summary, Vocabulary Map, Packages, Deliverables, Scope Ledger, Open Issues, Decision Log |
| A002 | MODIFY | Pi posture | D-APP-01, D-APP-02 | Reclassify Pi from possible adapter/spike/package path to pattern corpus / reference only. Prohibit Pi adapter, fork, direct import, Node 22 sidecar, or immediate spike. | Coordination docs, decision register, Pi assessment plans, runtime completion plan |
| A003 | MODIFY | Provider expansion gate | D-APP-03, K-NET-1, SOW-020 | Record strategic approval for provider-adapter generality while requiring bounded future implementation tranches and validation for every concrete non-Anthropic provider. | CONTRACT, SPEC, PRD, PLAN, decomposition scope ledger, coordination docs |
| A004 | MODIFY | Permission / tool-use posture | K-PERM-1, K-PERM-3, SOW-055, DEL-06-01 | Replace blanket "deny-first" framing with capability-forward, policy-mediated, evidence-recorded tool use. Preserve explicit deny precedence at hard boundaries. | CONTRACT, SPEC, TYPES, PLAN, PRD, decomposition hard constraints, PKG-06 descriptions |
| A005 | MODIFY | Active planning and governance surfaces | D-APP register, active completion plan, coordination prompt, runtime contract docs | Align active coordination and planning documents to select future runtime tranches from the provider-general spine and stop presenting Pi adapter/spike work as active future intent. | `_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, `plans/PLAN_2026-06-13_runtime_completion.md`, `frontend/docs/harness/runtime_engine_contract.md` |

## Gate 1 Validation

| Check | Result | Notes |
|---|---|---|
| Human initiated | PASS | Request was explicit in chat and supplied a SCOPE_CHANGE plan. |
| Variant and path resolved | PASS | Active SOFTWARE_DECOMP file exists at the requested path. |
| Stable IDs preserved | PASS | The preview does not add, remove, split, merge, reclassify, or renumber packages, deliverables, objectives, or SOW IDs. |
| Parent closure risk | PASS | No parent package or deliverable is removed or moved. |
| Structural contract change | WARNING | The amendment changes runtime strategy semantics and permission-governance interpretation. This is a contract-level governance change and requires explicit approval before Gate 5. |
| Direct runtime mutation | PASS | No source, package, lockfile, dependency, runtime-language, or wrapper changes are proposed. |

## Gate 1 Confirmation State

The human plan is treated as authority to prepare this SCOPE_CHANGE preview package. It is not treated as Gate 3 / Gate 4 approval of exact text because those exact amendments are first drafted in this snapshot.
