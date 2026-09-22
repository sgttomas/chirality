---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-02
package_id: PKG-06
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-047, SOW-049, SOW-050, SOW-064]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-06-02` in service of project scope [SOW-047, SOW-049, SOW-050, SOW-064] and package objectives [OBJ-005].

- **OUT-001** — Registered Chirality application-tool catalog/call validation and exposure evidence, including unknown-call rejection, collisions, deterministic ordering and applicable activation/domain stages, separate from user-selected native Codex tool policy.

**D-APP-80 concordance note (2026-07-28):** SOW-064 is supported here
through the App/project tool catalog, requested-tool validation, and
name-collision prevention. MCP wrapper implementation and remote MCP,
plugin, or marketplace scope remain excluded.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-06-02 SDK Read Tool Surface and Tool Validation

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-06-02 |
> | Deliverable name | SDK Read Tool Surface and Tool Validation |
> | Package | PKG-06 Permissioned Tools, MCP, and Hooks |
> | Type | BACKEND_FEATURE_SLICE |
> | Responsible party | TBD |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Context envelope | M |
> | Scope items | SOW-047, SOW-049, SOW-050, SOW-064 |
> | Objective context | OBJ-005 |
> | Anticipated artifacts | Tool resolver; unknown-tool tests; deterministic ordering fixtures |
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger rows SOW-047 through SOW-050.
>

### CLM-003 — Attributes

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Named verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

### CLM-004 — Conditions

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Named verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

### CLM-005 — Construction

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

Unfinished delivery: Supply live catalog/exposure and permuted-order witnesses, preserve domain roster/stage checks, and resolve any absent App registration through the accepted application-tool interface. P-01 wording is already released; product verification remains open.

### CLM-006 — Pending Implementation Evidence

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

Unfinished delivery: Supply live catalog/exposure and permuted-order witnesses, preserve domain roster/stage checks, and resolve any absent App registration through the accepted application-tool interface. P-01 wording is already released; product verification remains open.

### CLM-007 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` Sections 2 and 4 | Product-owned runtime governance, filesystem truth, read-before-powerful-tool posture | HISTORICAL_MATCH |
> | REF-002 | `docs/CONTRACT.md` Section 1.6 | Binding permission, tool, and MCP invariants | HISTORICAL_MATCH |
> | REF-003 | `docs/SPEC.md` Sections 14 and 15 | Tool names, MCP tools, surface rules, mode mapping | HISTORICAL_MATCH |
> | REF-004 | `docs/TYPES.md` Section 8 | Permission modes and tool-surface vocabulary | HISTORICAL_MATCH |
> | REF-005 | `docs/PLAN.md` R2/R3 | Implementation sequencing and acceptance context | HISTORICAL_MATCH |
> | REF-006 | `docs/PRD.md` Sections 8.13, 8.14, R2, KG-005, KG-023 | Product requirements and implementation direction | HISTORICAL_MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-06-02 SDK Read Tool Surface and Tool Validation

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-009 — Scope

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

### CLM-010 — Requirements

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-06-02-REQ-001 | Chirality-owned application-tool calls resolve only through the Runtime registered catalog; native Codex tools are not validated by the legacy opts.tools whitelist. |
| DEL-06-02-REQ-002 | Reject unknown or unregistered application calls with structured errors before execution; preserve truthful errors for native requests. |
| DEL-06-02-REQ-003 | Preserve the observed native tool identity and current Codex behavior in safe evidence; the historical Read/LS/Glob/Grep/Write/Edit/Bash SDK mapping is not a current supplier contract. |
| DEL-06-02-REQ-004 | Preserve canonical Chirality operation names, descriptor identity and collision prevention when registering application tools; a name in a compatibility registry is not proof of live exposure. |
| DEL-06-02-REQ-005 | Application-tool exposure must be deterministic for the same effective catalog, policy and request basis; verify any claimed canonical order with permuted-input fixtures. |
| DEL-06-02-REQ-006 | Implementation availability alone never authorizes application-tool exposure; validate catalog and applicable permission/domain-stage gates first. |
| DEL-06-02-REQ-007 | Preserve applicable read-first sequencing for Chirality-owned tool activation; native Codex capability follows the user-selected policy. |
| DEL-06-02-REQ-008 | Keep Chirality-owned write/bash/domain activation behind its accepted stage and handler gates; no retired SDK whitelist may veto native user policy. |
| DEL-06-02-REQ-009 | Do not treat allowedTools as restriction. Actual native sandbox/approval enforcement and application-handler authorization are separate checks. |
| DEL-06-02-REQ-010 | Omit denied application tools from model context where supported and always reject unauthorized application calls at execution. |
| DEL-06-02-REQ-011 | Read-only application operations must remain nonmutating. Native tool behavior must match the actual selected Codex policy, not a legacy mode label. |
| DEL-06-02-REQ-012 | Record the actual safe catalog/tool/policy identity and versions where available; an unrelated boot fingerprint does not prove catalog coverage. |
| DEL-06-02-REQ-013 | Test unknown calls, collisions, deterministic and permuted ordering, applicable read-first sequencing, domain-stage controls and actual live registration/exposure. |

Verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

Evidence locations: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Named verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

### CLM-012 — Verification

Required current checks: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

Named evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Supply live catalog/exposure and permuted-order witnesses, preserve domain roster/stage checks, and resolve any absent App registration through the accepted application-tool interface. P-01 wording is already released; product verification remains open.

### CLM-013 — Pass 3 Verification Evidence Disposition

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ###### Pass 3 Verification Evidence Disposition
>
> | ItemID | Disposition | Source reread evidence |
> |---|---|---|
> | C-001 | Incorporated as a verification-evidence requirement while concrete implementation paths remain TBD. Resolver, registry, deterministic-ordering, and read-first evidence must be named before closure. | `docs/CONTRACT.md` K-TOOL-1/K-TOOL-2; `docs/SPEC.md` Sections 13 and 14.3 |
> | D-001 | Incorporated as explicit tests for permission-boundary bypass cases: `allowedTools` cannot override deny inputs, and implementation availability alone cannot expose a tool. | `docs/CONTRACT.md` K-PERM-3 and K-TOOL-2; `docs/SPEC.md` Section 14.3 |
> | E-001 | Converted to a metadata-path TBD. Safe metadata or boot-fingerprint evidence is required, but the exact record path is not assigned in the current sources. | `docs/SPEC.md` Section 13; `docs/PRD.md` FR-128 with MATCH status — reconciled under D-APP-38 |
>


Current requirement and verification boundary: Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

### CLM-014 — Documentation

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

Unfinished delivery: Supply live catalog/exposure and permuted-order witnesses, preserve domain roster/stage checks, and resolve any absent App registration through the accepted application-tool interface. P-01 wording is already released; product verification remains open.

### CLM-015 — Traceability

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Named verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

- **AC-001** — Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-06-02 SDK Read Tool Surface and Tool Validation

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-017 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-06-02 SDK read tool-surface resolver and validation evidence. It is written for the deliverable artifact, not as an end-user operation runbook.
>

### CLM-018 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Current implementation/adoption evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-019 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.
4. Verify verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.
5. Retain inputs, source/candidate identity, commands, output and limitations; update Remaining only for backchecked outcomes.

Locus and checks: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-020 — Verification

Required current checks: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

Named evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Supply live catalog/exposure and permuted-order witnesses, preserve domain roster/stage checks, and resolve any absent App registration through the accepted application-tool interface. P-01 wording is already released; product verification remains open.

### CLM-021 — Records

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

Unfinished delivery: Supply live catalog/exposure and permuted-order witnesses, preserve domain roster/stage checks, and resolve any absent App registration through the accepted application-tool interface. P-01 wording is already released; product verification remains open.

- **VER-001** — Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-06-02 SDK Read Tool Surface and Tool Validation

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-023 — Purpose

> ##### Purpose
>
> DEL-06-02 exists to make `opts.tools` meaningful without letting SDK defaults or tool implementation availability define Chirality's runtime authority. It is the read-first tool-surface slice of PKG-06: it validates requested names, normalizes deterministic exposure, and hands the resulting surface to permission policy before model execution.
>
> Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Section 14; `docs/PRD.md` Section 8.13 with MATCH status. (reconciled under D-APP-38).
>

### CLM-024 — Principles

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Named verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

### CLM-025 — Considerations

> ##### Considerations
>

### CLM-026 — Resolver Shape

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Named verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

### CLM-027 — Read-First Surface

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Named verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

### CLM-028 — Relationship to Adjacent Deliverables

> ###### Relationship to Adjacent Deliverables
>
> | Adjacent deliverable | Interface point |
> |---|---|
> | DEL-06-01 | Provides capability policy with explicit hard-deny precedence and mode policy that this resolver must consume or preserve. |
> | DEL-06-03 | Provides Chirality MCP read tool definitions that this resolver registers or references. |
> | DEL-06-04 | Provides write/edit hooks and path policy needed before powerful write tools can be exposed. |
> | DEL-06-05 | Provides bash governance needed before `Bash` can be exposed. |
> | DEL-05-05 | Provides tool result budget/artifact policy referenced by later tool-result handling. |
>

### CLM-029 — PRD Hash Status

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Supply live catalog/exposure and permuted-order witnesses, preserve domain roster/stage checks, and resolve any absent App registration through the accepted application-tool interface. P-01 wording is already released; product verification remains open.

### CLM-030 — Terminology Normalization

> ###### Terminology Normalization
>
> Use the following terms distinctly:
>
> | Term | Use |
> |---|---|
> | read-first | Sequencing posture: read tools are enabled before write/edit/bash capability. |
> | read-only | Capability class: tools that do not write, shell out, or perform network-capable side effects. |
> | `readOnly` | Runtime mode token from the permission vocabulary. |
>
> This normalization preserves the difference between staged rollout, tool capability, and runtime mode policy. (P3: B-002)
>

### CLM-031 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Omit denied tools vs include and deny at call time | Prefer omission where possible to reduce context and accidental attempts, but never rely on omission alone; runtime denial must still hold. |
> | Strict registry vs permissive passthrough | Use strict registry behavior. Passthrough conflicts with SOW-047 and makes unknown tool names hard to audit. |
> | Resolver owns permission vs resolver consumes permission | Keep the resolver focused on validation and deterministic exposure. Capability-forward policy with explicit hard-deny precedence semantics belong to permission policy, but resolver output must not bypass it. |
> | SDK-specific names vs Chirality contracts | SDK names are adapter metadata. Public runtime contracts and event schemas should stay Chirality-owned. |
> | Read convenience vs staged governance | Exposing read tools first is useful, but it must not become a back door to write/bash or remote tool expansion. |
>

### CLM-032 — Examples

Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

Named verification: Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed. Evidence: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132.

### CLM-033 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Validate Chirality-owned application-tool descriptors/catalog/calls separately from native Codex tool policy. D-APP-132 releases P-01 CLM-005 and CLM-032; no repeat owner reservation applies.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Supply live catalog/exposure and permuted-order witnesses, preserve domain roster/stage checks, and resolve any absent App registration through the accepted application-tool interface. P-01 wording is already released; product verification remains open.

### CLM-034 — D-APP-56 roster clarification (2026-07-12)

> ##### D-APP-56 roster clarification (2026-07-12)
>
> R4-P27 reconciles the former unsupported/TBD domain-tool roster wording: PKG-10 owns the ruled domain-profile registry and proposal-tool roster. DEL-06-02 remains the SDK read-tool and validation owner and does not duplicate that ownership.

### CLM-035 — D-APP-68 Coordination-Descriptor Ownership (2026-07-19)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-68 Coordination-Descriptor Ownership (2026-07-19)
>
> DEL-06-02 owns the registered descriptor, canonical-name, allowed-name
> catalog, alias, schema, and registry-validation surface for the four
> coordination MCP tools: `delegate_agent`, `report_coordination_notice`,
> `send_agent_update`, and `ack_agent_update` (SDK-facing names
> `mcp__chirality__delegate_agent`,
> `mcp__chirality__report_coordination_notice`,
> `mcp__chirality__send_agent_update`, and
> `mcp__chirality__ack_agent_update`). Unknown names continue to fail closed
> through the deterministic registry. DEL-06-03 separately owns their
> co-location and composition on the in-process Chirality MCP server; this
> mapping does not duplicate that composition boundary.
>
> Evidence: D-APP-68 chronology item 3;
> `frontend/packages/harness-contract/src/mcp/tool-names.ts`;
> `frontend/packages/harness-contract/src/tool-descriptor.ts`;
> `frontend/src/__tests__/lib/tool-descriptor.test.ts`.

- **AC-002** — Native Codex tools follow the user-selected Codex approval and sandbox policy, passed through without an App veto. Full access is selectable and does not grant normative authority. Chirality-owned application operations retain their own authorization, path, domain-stage and evidence controls; prompts and tool-name lists are not enforcement. Registered application names, schemas, aliases and collision rejection must be explicit; unknown/unregistered calls fail with structured errors. Availability is not exposure. Preserve deterministic application-tool exposure, applicable ordering/read-first obligations and PKG-10 domain-stage gates; deduplication preserving request order is not permutation-invariant canonical ordering. The user-shared Codex home may supply native MCP/plugins under Codex policy; this does not authorize a new Chirality provider/tool integration. The retained SDK registry and four coordination descriptors remain compatibility contracts.

- **VER-002** — Verify catalog registration, collisions, schema validation and unknown calls; test permuted input ordering, policy/exposure separation, applicable read-first/domain-stage restrictions and safe metadata. Identify actual App registrations; an available Runtime catalog does not prove those tools are exposed.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-047 SOW-049 SOW-050 SOW-064 OBJ-005 | CLM-010 CLM-035 | AC-001 AC-002 | VER-001 VER-002 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
