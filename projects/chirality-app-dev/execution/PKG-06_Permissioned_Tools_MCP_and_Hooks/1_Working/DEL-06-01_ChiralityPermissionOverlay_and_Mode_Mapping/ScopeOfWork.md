---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-01
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-054, SOW-055, SOW-056, SOW-058]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-06-01` in service of project scope [SOW-054, SOW-055, SOW-056, SOW-058] and package objectives [OBJ-005].

- **OUT-001** — App approval/request presentation and decision evidence for supported Codex policy selections, exact request identity, denial/non-execution and human-gate enforcement, preserving separate authorization of Chirality-owned operations and native tool policy.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-06-01 |
> | Deliverable name | ChiralityPermissionOverlay and Mode Mapping |
> | Package | PKG-06 Permissioned Tools, MCP, and Hooks |
> | Type | SECURITY_CONTROL |
> | Responsible party | TBD |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Context envelope | M |
> | Scope items | SOW-054, SOW-055, SOW-056, SOW-058 |
> | Objective context | OBJ-005 |
> | Anticipated artifacts | Permission overlay module; decision records; readOnly/dontAsk/ask tests |
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger rows SOW-054 through SOW-058.
>


Current deliverable responsibility: App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

### CLM-003 — Attributes

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-004 — Conditions

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-005 — Construction

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

Unfinished delivery: Complete live permission/request identity and deny-non-execution witnesses; repair any actor/SHA gate enforcement gaps on served application APIs and verify native descendant policy/scope evidence without weakening domain controls.

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-002 | `docs/CONTRACT.md` Section 1.6 | Binding permission, tool, MCP, hook, path, and bash invariants | HISTORICAL_MATCH |
> | REF-003 | `docs/SPEC.md` Sections 14 and 15 | Tool names, MCP tools, tool surface rules, mode mapping, hook requirements | HISTORICAL_MATCH |
> | REF-004 | `docs/TYPES.md` Section 8 | Permission modes, decision record, tool-surface terms | HISTORICAL_MATCH |
> | REF-005 | `docs/PLAN.md` R2 and R3 | Sequencing and acceptance context | HISTORICAL_MATCH |
> | REF-006 | `docs/PRD.md` Sections 9.4, R2, R3, NFR-007, KG-023 | Product requirements and implementation direction | HISTORICAL_MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-008 — Scope

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

### CLM-009 — Requirements

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-06-01-REQ-001 | Record permission requests and decisions with exact request/session/turn identity, tool/action, outcome, reason/source/time and safe metadata; distinguish pending from completed decisions. |
| DEL-06-01-REQ-002 | Resolve each native Codex server request through its supported response contract; never leave an unfamiliar request unanswered or claim a decision that did not occur. |
| DEL-06-01-REQ-003 | Explicit denials remain binding for Chirality-owned operations. Native Codex approvals and sandbox enforcement follow the selected user policy without a hidden App override. |
| DEL-06-01-REQ-004 | Tool names or allowedTools lists are not enforcement. Verify the actual native sandbox/approval boundary and application-operation validation separately. |
| DEL-06-01-REQ-005 | When the selected Codex policy restricts writes or execution, prove the corresponding requests do not execute outside that policy; the old readOnly SDK surface is compatibility evidence. |
| DEL-06-01-REQ-006 | Use the selected Codex approval behavior, including its supported no-prompt outcomes. The retired dontAsk mapping does not impose an extra App policy. |
| DEL-06-01-REQ-007 | Present and record supported native approvals with exact request linkage; resolve the response through Runtime and preserve safe decision evidence. |
| DEL-06-01-REQ-008 | Workspace write behavior follows the selected Codex sandbox/approval policy; Chirality-owned mutations additionally retain their accepted validation. |
| DEL-06-01-REQ-009 | Full access is user-selectable under D-GOV-43. It grants no normative authority, changes no domain-stage control and proves no blanket governed-path containment. |
| DEL-06-01-REQ-010 | Retain safe permission/denial audit evidence, reasons and available upstream metadata for actual observed attempts. |
| DEL-06-01-REQ-011 | Prompt text is never a filesystem, tool, shell, delegation or domain enforcement boundary. |
| DEL-06-01-REQ-012 | Registered application tools retain handler authorization, path, redaction and event controls; native Codex tools follow native policy. |
| DEL-06-01-REQ-013 | Keep Chirality-owned approval interfaces distinct while preserving upstream request identity and payloads after redaction as D-GOV-43 requires. |
| DEL-06-01-REQ-014 | Verify the supported native approval/sandbox combinations, denied non-execution and durable request/decision evidence; historical fixed-mode tests do not establish current qualification. |
| DEL-06-01-REQ-015 | Provide enough explicit request/session/turn/action and chosen policy context to resolve approvals correctly; never derive human identity from a caller-supplied HUMAN label. |

Verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

Evidence locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures. These are hooks and source locations, not newly executed results.

### CLM-010 — Standards

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-011 — Verification

Required current checks: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

Named evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Complete live permission/request identity and deny-non-execution witnesses; repair any actor/SHA gate enforcement gaps on served application APIs and verify native descendant policy/scope evidence without weakening domain controls.

### CLM-012 — Documentation

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

Unfinished delivery: Complete live permission/request identity and deny-non-execution witnesses; repair any actor/SHA gate enforcement gaps on served application APIs and verify native descendant policy/scope evidence without weakening domain controls.

### CLM-013 — Pass 3 Semantic Lensing Disposition

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Semantic Lensing Disposition
>
> | ItemID | Disposition | Evidence and source reread |
> |---|---|---|
> | C-001 | Incorporated as bounded interface requirements while preserving exact implementation shape as TBD. | Datasheet Construction and DEL-06-01-REQ-015 now identify the minimum product-owned context. Reread: `docs/TYPES.md` Section 8.2; `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` Section 1.5. |
> | F-001 | Incorporated as verification evidence for workspaceWrite hook-pass gating, with hook internals deferred to DEL-06-04. | Verification keeps hook implementation out of this deliverable but requires contract/integration proof before edits can allow. Reread: `docs/SPEC.md` Section 15.1; decomposition PKG-06 rows for DEL-06-04. |
> | X-002 | Converted to explicit path-TBD verification evidence requirements rather than invented test names. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | E-002 | Incorporated as MCP parity verification with concrete source obligation and adjacent wrapper ownership. | DEL-06-01-REQ-012 and verification require parity; wrapper detail remains with DEL-06-03. Reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2; decomposition PKG-06 rows for DEL-06-03. |
>


Current requirement and verification boundary: Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

### CLM-014 — Traceability

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-015 — D-APP-56 permission-class amendment (2026-07-12)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-56 permission-class amendment (2026-07-12)
>
> R4-P33 adds the D-APP-10-governed subagent/Agent class to REQ-005: delegated children are allowed only under `workspaceWrite`; other modes hard-deny through `evaluateSubagentPreflight`. DEL-06-01 owns the declaration and DEL-08-04 consumes it.

- **AC-001** — Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-017 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-06-01 permission overlay implementation and mode mapping evidence. It is written for the deliverable artifact, not as an end-user operation runbook.
>

### CLM-018 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Current implementation/adoption evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-019 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.
4. Verify exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.
5. Retain inputs, source/candidate identity, commands, output and limitations; update governing scope and any selected work graph only for backchecked outcomes.

Locus and checks: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-020 — Verification

Required current checks: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

Named evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Complete live permission/request identity and deny-non-execution witnesses; repair any actor/SHA gate enforcement gaps on served application APIs and verify native descendant policy/scope evidence without weakening domain controls.

### CLM-021 — Records

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

Unfinished delivery: Complete live permission/request identity and deny-non-execution witnesses; repair any actor/SHA gate enforcement gaps on served application APIs and verify native descendant policy/scope evidence without weakening domain controls.

### CLM-022 — Pass 3 Semantic Lensing Disposition

The table below preserves the historical Pass 3 disposition. Its SDK hook/MCP path and unresolved call-path descriptions are not current implementation prerequisites. The current obligation is durable, truthful permission-decision evidence through the Runtime-owned event writer, with request/session/turn identity and safe metadata preserved. Current inspection and verification locations are Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts` and their request/event tests; existing files identify implementation evidence, while ordering, denied non-execution and actor attribution still require current witnesses. No new ownership vote or guessed frontend call path is required.

> ##### Pass 3 Semantic Lensing Disposition
>
> | ItemID | Disposition | Evidence and source reread |
> |---|---|---|
> | D-001 | Converted to explicit Records blockers rather than invented paths. | Records now name required implementation, fixture, hook-gating, MCP parity, and decision-schema evidence as TBD. Reread: `_CONTEXT.md` anticipated artifacts; `docs/SPEC.md` Sections 14 and 15; decomposition PKG-06 rows. |
> | D-002 | Incorporated as a dependency closure distinction. | Prerequisites now distinguish extracted dependency records from still-TBD human-declared upstream closure. Reread: `_DEPENDENCIES.md` Dependency Tracking and Extracted Dependency Register; `Dependencies.csv` v3.1. |
> | E-001 | Converted from ASSUMPTION to tracked blocker. | Step 5 no longer states the event writer/session JSONL API as accepted fact; it depends on the owning writer contract and keeps exact call path TBD. Reread: `docs/SPEC.md` Section 9.2 and Section 9.4; `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `_DEPENDENCIES.md` DEP-06-01-014 warning. |
> | E-002 | Incorporated as explicit MCP parity procedure and record evidence. | Step 7 and Records require MCP parity evidence while leaving wrapper points to DEL-06-03 or a shared overlay hook point. Reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2; decomposition PKG-06 rows for DEL-06-03. |

- **VER-001** — Verify supported native approval/sandbox combinations, exact request/session/turn identity, durable truthful decisions, denied non-execution, separate Stop versus per-request denial and actual human-gate enforcement; historical fixed-mode tests do not qualify the native path.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-024 — Purpose

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

### CLM-025 — Principles

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-026 — Considerations

> ##### Considerations
>

### CLM-027 — Mode Mapping

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-028 — Decision Provenance

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-029 — PRD Hash Status

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Complete live permission/request identity and deny-non-execution witnesses; repair any actor/SHA gate enforcement gaps on served application APIs and verify native descendant policy/scope evidence without weakening domain controls.

### CLM-030 — Trade-offs

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-031 — Examples

App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Named verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures.

### CLM-032 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. App approval UI and permission evidence conform to Runtime server requests and the user-selected Codex policy. The Claude permission overlay and fixed modes are compatibility evidence.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Complete live permission/request identity and deny-non-execution witnesses; repair any actor/SHA gate enforcement gaps on served application APIs and verify native descendant policy/scope evidence without weakening domain controls.

### CLM-033 — Pass 3 Semantic Lensing Disposition

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Semantic Lensing Disposition
>
> | ItemID | Disposition | Evidence and source reread |
> |---|---|---|
> | X-001 | Incorporated as an explicit PRD MATCH disposition. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |


Current requirement and verification boundary: Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

Verification: Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

### CLM-034 — D-APP-68 Managed-Orchestration Ownership Mapping (2026-07-19)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-68 Managed-Orchestration Ownership Mapping (2026-07-19)
>
> DEL-06-01 owns the `coordination` descriptor permission class and the
> `harness-permission.v7.coordination-mode` mode-policy behavior. Coordination
> tools mutate the orchestration control plane and therefore hard-deny in every
> mode except `workspaceWrite`; in `workspaceWrite` they are admitted only to
> their handler-level hierarchy, seal, parentage, capability, and project-path
> validation. This permission-class mapping does not transfer descriptor,
> in-process MCP composition, child path-policy, Bash-policy, or child-record
> ownership from DEL-06-02, DEL-06-03, DEL-06-04, DEL-06-05, or DEL-08-05.
>
> Evidence: D-APP-68 chronology item 3;
> `frontend/src/lib/harness/permission-overlay.ts`;
> `frontend/packages/harness-contract/src/tool-descriptor.ts`.

- **AC-002** — Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Preserve request/session/turn identity, truthful allow/deny/pending outcomes, reason/source/time and safe metadata, denied-operation non-execution, evidence before resolution where required, separate whole-turn Stop and per-request denial. Never accept a caller HUMAN string as proof of human approval. Application/domain operations retain deterministic deny and human-gate checks; native delegation must preserve actual parentage, supplied basis and scope without promising the old SDK coordination mode table.

- **VER-002** — Exercise each supported approval/sandbox combination, deny/accept/cancel/unfamiliar requests, durable decisions, exact request identity, denied non-execution and actor-evidence enforcement. Map current S-1–S-8/conformance evidence rather than require all legacy fixed-mode tests.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-054 SOW-055 SOW-056 SOW-058 OBJ-005 | CLM-009 CLM-034 | AC-001 AC-002 | VER-001 VER-002 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
