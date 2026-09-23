---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-05
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-062]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-05

## Purpose and Objective Traceability

This Scope of Work defines `DEL-06-05` in service of project scope [SOW-062] and package objectives [OBJ-005].

- **OUT-001** — App shell-policy and native command-conformance evidence for denied non-execution, applicable timeout limits, truthful cancellation/interruption, safe stream/artifact metadata and declared child scope; native policy is user-selected and legacy fixed defaults are identified as compatibility behavior.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-05 Bash Governance and Timeout Policy

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-06-05 |
> | Deliverable name | Bash Governance and Timeout Policy |
> | Package | PKG-06 Permissioned Tools, MCP, and Hooks |
> | Type | SECURITY_CONTROL |
> | Responsible party | TBD |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Context envelope | M |
> | Scope items | SOW-062 |
> | Objective context | OBJ-005 |
> | Anticipated artifacts | Bash deny/default tests; timeout/capture policy; output metadata tests |
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger row SOW-062.
>

### CLM-003 — Attributes

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

### CLM-004 — Conditions

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

### CLM-005 — Construction

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

Unfinished delivery: Produce live command-denial/timeout/interrupt/output/scope witnesses; implement missing applicable timeout and artifact controls or route an actual scope change through the owning authority. D-APP-68 constants and managed-child protections are not silently waived.

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` Sections 2.8, 2.9, 4.1, 4.2, and 5 | Product-owned runtime governance, reliance boundaries, bash exposure sequencing | HISTORICAL_MATCH |
> | REF-002 | `docs/CONTRACT.md` Sections 1.5 and 1.6 | Binding event, permission, hook, path, and Bash invariants | HISTORICAL_MATCH |
> | REF-003 | `docs/SPEC.md` Sections 10, 13, 14, and 15 | Engine responsibilities, option/tool resolution, tool names, mode mapping, hooks | HISTORICAL_MATCH |
> | REF-004 | `docs/TYPES.md` Sections 7 and 8 | Event vocabulary, permission modes, decision records, tool terms, artifact path fields | HISTORICAL_MATCH |
> | REF-005 | `docs/PLAN.md` R4 | Sequencing, implementation targets, and Bash acceptance criteria | HISTORICAL_MATCH |
> | REF-006 | `docs/PRD.md` Sections 8.15 and R4 | Product requirements for Bash, result storage, context mirror, and audit behavior | HISTORICAL_MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-06-05 Bash Governance and Timeout Policy

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-008 — Scope

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

### CLM-009 — Requirements

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-06-05-REQ-001 | Native command execution follows user-selected Codex policy; the fixed SDK default-deny mechanism is historical. Chirality-owned shell operations still require accepted authorization. |
| DEL-06-05-REQ-002 | Prove denied commands do not execute for the supported restricted policy; do not infer native restrictions from a legacy readOnly label. |
| DEL-06-05-REQ-003 | Use the supported native no-prompt/approval outcome. The legacy dontAsk shell rule does not authorize an App veto of user Codex configuration. |
| DEL-06-05-REQ-004 | Tool availability/allowedTools does not authorize shell execution; verify native command policy and applicable application-operation gates. |
| DEL-06-05-REQ-005 | A denied command request must not spawn or execute the denied process. |
| DEL-06-05-REQ-006 | Preserve D-APP-68 managed-App-shell timeout default 120000 ms and maximum 600000 ms. Native Codex equivalence is unverified and requires explicit implementation/evidence or an owning scope change, not silent waiver. |
| DEL-06-05-REQ-007 | Preserve distinct stdout/stderr attribution where provided; verify whether native output supplies the required separation and retain the gap otherwise. |
| DEL-06-05-REQ-008 | Bound medium/large shell output with previews/artifact references; unbounded inline deltas or fixed truncation alone do not satisfy accepted artifact behavior. |
| DEL-06-05-REQ-009 | Preserve safe terminal/artifact metadata under D-APP-42: tool/turn identity, byte lengths, truncation, exact stored-byte SHA-256, relative path and stream labels; preserve actual interruption outcome. |
| DEL-06-05-REQ-010 | Support available interruption/cancellation and record the actual terminal outcome or residual risk when interruption cannot be performed. |
| DEL-06-05-REQ-011 | Make command permission/start/completion/failure/timeout/interruption auditable through current Runtime records. |
| DEL-06-05-REQ-012 | App-controlled shell validation/hook failures fail closed; native Codex requests follow the actual selected policy. |
| DEL-06-05-REQ-013 | Application-owned shell retains applicable containment, ordinary instruction-root protection, redaction and provenance. Verify native host enforcement truthfully; lexical command inspection cannot prove arbitrary-shell containment. |
| DEL-06-05-REQ-014 | Keep Chirality operation evidence and upstream native command identity/payload distinct and preserve them after required redaction. |
| DEL-06-05-REQ-015 | Verify denied-never-spawns, current approval/sandbox behavior, timeout, stream attribution, artifact metadata and interruption on the actual live path. |
| DEL-06-05-REQ-016 | Retain managed App shell preflight constraints for its compatibility interface. Native command/network behavior follows Codex policy; verify actual metadata/timeout/path/network outcomes without reintroducing retired supplier containment. |

Verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

Evidence locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners. These are hooks and source locations, not newly executed results.

### CLM-010 — Standards

> ##### Standards
>
> | Standard or governing source | Applicability |
> |---|---|
> | `docs/CONTRACT.md` Section 1.6 | Binding permission, tool exposure, hook, path, and Bash invariants. |
> | `docs/CONTRACT.md` Section 1.5 | Runtime event and audit mirror invariants. |
> | `docs/SPEC.md` Sections 14 and 15 | SDK tool naming, tool surface rules, permission mode mapping, required hooks, and fail-closed hook behavior. |
> | `docs/TYPES.md` Section 8 | Permission mode vocabulary, permission decision shape, tool-surface terms, and `ToolResultStore`. |
> | `docs/PLAN.md` R4 | Roadmap sequencing and acceptance criteria for Bash, result budgeting, and context mirror behavior. |
> | `docs/PRD.md` Section 8.15 | Product requirements for tool output storage, Bash, context management, and audit mirror; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |
>

### CLM-011 — Verification

Required current checks: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

Named evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Produce live command-denial/timeout/interrupt/output/scope witnesses; implement missing applicable timeout and artifact controls or route an actual scope change through the owning authority. D-APP-68 constants and managed-child protections are not silently waived.

### CLM-012 — Documentation

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

Unfinished delivery: Produce live command-denial/timeout/interrupt/output/scope witnesses; implement missing applicable timeout and artifact controls or route an actual scope change through the owning authority. D-APP-68 constants and managed-child protections are not silently waived.

### CLM-013 — Traceability

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

- **AC-001** — Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-06-05 Bash Governance and Timeout Policy

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-015 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-06-05 Bash governance implementation and timeout/capture policy evidence. It is written for the deliverable artifact, not as an end-user shell runbook.
>

### CLM-016 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Current implementation/adoption evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-017 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.
4. Verify verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.
5. Retain inputs, source/candidate identity, commands, output and limitations; update governing scope and any selected work graph only for backchecked outcomes.

Locus and checks: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-018 — Verification

Required current checks: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

Named evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Produce live command-denial/timeout/interrupt/output/scope witnesses; implement missing applicable timeout and artifact controls or route an actual scope change through the owning authority. D-APP-68 constants and managed-child protections are not silently waived.

### CLM-019 — Records

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

Unfinished delivery: Produce live command-denial/timeout/interrupt/output/scope witnesses; implement missing applicable timeout and artifact controls or route an actual scope change through the owning authority. D-APP-68 constants and managed-child protections are not silently waived.

- **VER-001** — Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-06-05 Bash Governance and Timeout Policy

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-021 — Purpose

> ##### Purpose
>
> DEL-06-05 exists to prevent the SDK `Bash` surface from becoming an accidental escape hatch. Bash is powerful enough to read, write, delete, invoke networks, spawn long-running work, and produce unbounded output, so Chirality treats it as denied by default and enables it only after product-owned governance, timeout, result storage, interruption, and audit behavior are ready.
>
> Sources: `_CONTEXT.md`; decomposition row SOW-062; `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4.
>

### CLM-022 — Principles

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

### CLM-023 — Considerations

> ##### Considerations
>

### CLM-024 — Mode Behavior

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

### CLM-025 — Timeout And Capture Policy

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

### CLM-026 — Hooks And Path Policy

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

### CLM-027 — PRD Hash Status

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Produce live command-denial/timeout/interrupt/output/scope witnesses; implement missing applicable timeout and artifact controls or route an actual scope change through the owning authority. D-APP-68 constants and managed-child protections are not silently waived.

### CLM-028 — Trade-offs

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

### CLM-029 — Examples

Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

Named verification: Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification. Evidence: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners.

### CLM-030 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Govern App-owned shell operations and verify current Codex command approval, outcomes and output hygiene. The fixed SDK Bash modes and command-string preflight remain compatibility mechanisms.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Produce live command-denial/timeout/interrupt/output/scope witnesses; implement missing applicable timeout and artifact controls or route an actual scope change through the owning authority. D-APP-68 constants and managed-child protections are not silently waived.

### CLM-031 — D-APP-68 Managed-Child Bash Gate and Timeout Ratification (2026-07-19)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-68 Managed-Child Bash Gate and Timeout Ratification (2026-07-19)
>
> DEL-06-05 owns the managed-child Bash admission rule. Because arbitrary Bash
> cannot be proven package-bounded by lexical command inspection, a Bash-bearing
> managed child is admitted only when both its declared read scope and declared
> write scope explicitly cover the full active project root. Otherwise Bash
> hard-denies and the caller must use bounded file tools or a deterministic
> registered tool. An admitted Bash-bearing child is the serialized integration
> owner for that stage; this rule does not weaken DEL-06-04's path policy for
> bounded file tools.
>
> D-APP-68 chronology item 6 ratifies the live timeout constants: default
> `120000` ms and maximum `600000` ms. These values replace former numeric-TBD
> wording throughout this live Scope of Work; genuinely unrelated TBDs remain.
>
> Evidence: D-APP-68 chronology items 3 and 6; root `AGENTS.md` managed-Bash
> rule; `frontend/src/lib/harness/tool-shell-policy.ts`;
> `frontend/src/__tests__/lib/chirality-hooks.test.ts`.

- **AC-002** — Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Denied commands must not execute. Preserve timeout/interrupt/cancel outcomes, stdout/stderr provenance where supplied, bounded previews/artifacts, D-APP-42 exact-byte metadata and secret exclusion. D-APP-68 ratified 120000 ms default and 600000 ms maximum for the managed App shell; no evidence establishes equivalent native Codex enforcement, so its applicability/implementation remains explicit follow-through rather than an invented waiver. Managed App Bash required full-project read/write admission and a serialized integration owner; native descendants need truthful scope and host-enforcement evidence. Lexical command inspection cannot prove arbitrary shell containment.

- **VER-002** — Verify denied-never-spawns, actual timeout including maximum override, interruption versus failure, stream labels, output size/preview/artifact metadata, redaction and native-child scope. Preserve unavailable observations and do not transfer historical constant tests into native qualification.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-062 OBJ-005 | CLM-009 CLM-031 | AC-001 AC-002 | VER-001 VER-002 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
