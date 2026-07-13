---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-05
package_id: PKG-04
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-019, SOW-020, SOW-021]
package_objective_refs: [OBJ-004, OBJ-008]
---

# Scope of Work — DEL-04-05

## Purpose and Objective Traceability

This migration candidate defines `DEL-04-05` in service of project scope [SOW-019, SOW-020, SOW-021] and package objectives [OBJ-004, OBJ-008].

- **OUT-001** — Provider wrapper, key handoff tests, base URL/network tests, provider-expansion guard tests, and redaction fixtures for DEL-04-05 that preserve API key precedence, current Anthropic network policy, provider error classification, no unauthorized provider/network expansion, and redacted adapter environment handoff for SOW-019, SOW-020, SOW-021 and supporting OBJ-004, OBJ-008.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":4,"line_start":1,"source_sha256":"89e832fa1a1bd32a8e49606fe6f225dd124744451e0d60c449bcb9f2c7796668","target_id":"CLM-001"} -->
#### Datasheet: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":22,"line_start":5,"source_sha256":"89e832fa1a1bd32a8e49606fe6f225dd124744451e0d60c449bcb9f2c7796668","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-04-05 |
| DeliverableName | Anthropic Provider Key, Base URL, and Network Bridge |
| PackageID | PKG-04 |
| PackageName | SDK Adapter, Prompt, Provider, and Settings |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | SECURITY_CONTROL |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| ScopeItems | SOW-019, SOW-020, SOW-021 |
| Objectives | OBJ-004, OBJ-008 |

Source: `_CONTEXT.md` "Identity", "Traceability"; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` row `DEL-04-05`.

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":37,"line_start":23,"source_sha256":"89e832fa1a1bd32a8e49606fe6f225dd124744451e0d60c449bcb9f2c7796668","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| API key precedence | UI safeStorage key first, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | `docs/SPEC.md` Section 12.3; `docs/PRD.md` Section 8.5 FR-030 |
| API key state class | Non-project convenience state; not project truth. | `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` Section 16.2 |
| API key storage target | Electron `app.getPath('userData')/credentials/api-key.enc` when UI storage is used. | `docs/SPEC.md` Section 16.2 |
| API key status values | `ui`, `env`, or `none`. | `docs/SPEC.md` Section 16.2 |
| Allowed Anthropic base URL | `https://api.anthropic.com` with no credentials and port empty or 443. | `docs/PRD.md` Section 8.5 FR-032 |
| Renderer network policy | Allow loopback and Anthropic API path; cancel non-allowlisted outbound requests. | `docs/SPEC.md` Section 16.3; `docs/PRD.md` Section 8.5 FR-033 |
| Node/SDK network policy | Node/SDK provider calls must not silently broaden network policy. | `docs/SPEC.md` Section 16.3 |
| Provider error classes | Auth, rate limit, timeout, API error, network error, invalid base URL, policy violation. | `docs/PRD.md` Section 8.5 FR-034 |
| SDK boundary | Provider integration is wrapped by the SDK-backed turn boundary, isolated in `TurnEngine`, `sdk-options-builder`, and `sdk-message-mapper`. | `docs/PRD.md` Section 8.5 FR-035 |
| Redaction scope | Provider errors, SDK errors, logs, runtime events, and SDK stderr/debug output must redact secrets. | `docs/CONTRACT.md` K-EVENT-6; `docs/PLAN.md` Section 6.3; `docs/PRD.md` FR-075 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":48,"line_start":38,"source_sha256":"89e832fa1a1bd32a8e49606fe6f225dd124744451e0d60c449bcb9f2c7796668","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Shipped SDK settings isolation | Shipped builds use `settingSources: []`. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| SDK adapter promotion gate | SDK-backed adapter must pass engine conformance tests before becoming the default production path. | `docs/CONTRACT.md` K-ENGINE-2; `docs/SPEC.md` Section 12.1 |
| Product boundary | Public APIs, UI events, harness events, session storage, permission decisions, and governance records remain Chirality-owned, not SDK-shaped. | `docs/CONTRACT.md` K-ENGINE-4 |
| Broader network tools | Remote MCP, plugins, and non-Anthropic network tools require governed future scope. | `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1 |
| Packaging condition | Packaged app must prove SDK execution and API key handoff without leaking secrets. | `docs/PLAN.md` Section 6.4 |
| Source-state warning | `docs/PRD.md` is locally accessible but has `MATCH` in `_REFERENCES.md`; claims from it are used as scoped source guidance and should be reverified before final acceptance. | `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":60,"line_start":49,"source_sha256":"89e832fa1a1bd32a8e49606fe6f225dd124744451e0d60c449bcb9f2c7796668","target_id":"CLM-005"} -->
##### Construction

| Construct | Expected Content |
|---|---|
| Provider wrapper | A provider boundary that resolves API key source, validates Anthropic base URL, supplies SDK environment only for the active turn, normalizes provider/SDK failures, and emits redacted details. Exact module name: TBD. |
| Key handoff tests | Tests proving UI key precedence, environment fallback order, absence of working-root writes, and redacted SDK environment/log/event handoff. Exact test paths: TBD. |
| Base URL/network tests | Tests proving only `https://api.anthropic.com` with no credentials and empty/443 port is accepted, renderer outbound requests are loopback or current shipped Anthropic path only, and Node/SDK calls do not broaden policy. Exact test paths: TBD. |
| Redaction fixtures | Fixtures covering key material, provider error messages, SDK stderr/debug output, and policy-denial metadata. Exact fixture shape: TBD. |
| Status metadata | Safe status source values are `ui`, `env`, or `none`; no key value is recorded. |

ASSUMPTION: "Provider wrapper" may be implemented as an SDK adapter helper, a `TurnEngine` collaborator, or a dedicated provider module. The decomposition names the artifact but the source corpus does not prescribe the exact file path.

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":69,"line_start":61,"source_sha256":"89e832fa1a1bd32a8e49606fe6f225dd124744451e0d60c449bcb9f2c7796668","target_id":"CLM-006"} -->
##### References

| RefID | Source | SectionRef | Status |
|---|---|---|---|
| REF-002 | `docs/CONTRACT.md` | Sections 1.4, 1.9; K-ENGINE-2, K-ENGINE-4, K-EVENT-6, K-NET-1, K-KEY-1 | MATCH |
| REF-003 | `docs/SPEC.md` | Sections 12.1-12.4, 16.2-16.3 | MATCH |
| REF-005 | `docs/PLAN.md` | Sections 6.3-6.4; R1 implementation targets | MATCH |
| REF-006 | `docs/PRD.md` | Section 8.5 FR-030 through FR-035; FR-075; NFR-002 through NFR-003; NFR-028 through NFR-030 | MATCH status — reconciled under D-APP-38 |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOW-019 through SOW-021; OBJ-004, OBJ-008; row `DEL-04-05` | accepted decomposition reference |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":4,"line_start":1,"source_sha256":"3baa856f1581a65f3a2dd5e088d2d1acaf4e7e8a3d7fc7a17b2389e9b1bd19c1","target_id":"CLM-007"} -->
#### Specification: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-008 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":24,"line_start":5,"source_sha256":"3baa856f1581a65f3a2dd5e088d2d1acaf4e7e8a3d7fc7a17b2389e9b1bd19c1","target_id":"CLM-008"} -->
##### Scope

This deliverable covers the security and provider-boundary behavior for Anthropic SDK execution in PKG-04:

- API key precedence and SDK environment handoff.
- Anthropic base URL validation.
- Renderer and Node/SDK network policy bridge.
- Provider and SDK error classification with redaction.
- Tests and fixtures demonstrating the above behavior.

This deliverable excludes:

- General SDK option construction and settings isolation except where required for safe provider handoff; those are primarily DEL-04-02.
- Provider/SDK message mapping except where provider errors cross into stable runtime/UI events; that is primarily DEL-04-03.
- UI API key settings behavior except for the stored-key precedence contract; that is shared with DEL-02-05.
- Redacted run logger ownership except for provider-boundary fixtures and requirements; that is shared with DEL-05-03.
- Project event-store internals beyond redacted metadata handoff, per `_CONTEXT.md`.

Sources: `_CONTEXT.md` "Deliverable Scope"; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` row `DEL-04-05`.

<!-- sow-source-end -->

### CLM-009 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":46,"line_start":25,"source_sha256":"3baa856f1581a65f3a2dd5e088d2d1acaf4e7e8a3d7fc7a17b2389e9b1bd19c1","target_id":"CLM-009"} -->
##### Requirements

| ID | Requirement | Priority | Source |
|---|---|---|---|
| DEL-04-05-RQ-001 | The runtime must resolve the Anthropic API key in this order: UI safeStorage key, `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | P0 | `docs/SPEC.md` Section 12.3; `docs/PRD.md` Section 8.5 FR-030 |
| DEL-04-05-RQ-002 | Key material must not be written to the working root, docs, logs, runtime event payloads, git-tracked execution files, or tool artifacts. | P0 | `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` Section 16.2; `docs/PRD.md` FR-031 and NFR-002 |
| DEL-04-05-RQ-003 | UI-stored key material must use Electron `safeStorage` at `app.getPath('userData')/credentials/api-key.enc`. | P0 | `docs/SPEC.md` Section 16.2 |
| DEL-04-05-RQ-004 | Key source status may expose only `ui`, `env`, or `none`, never the key value or reversible key material. | P0 | `docs/SPEC.md` Section 16.2 |
| DEL-04-05-RQ-005 | SDK environment key handoff must occur only as needed for an active turn and must be redacted from logs and events. | P0 | `docs/SPEC.md` Section 12.3; `docs/PLAN.md` R1 implementation targets |
| DEL-04-05-RQ-006 | Anthropic base URL validation must accept only `https://api.anthropic.com` with no credentials and port empty or 443. | P0 | `docs/PRD.md` Section 8.5 FR-032 |
| DEL-04-05-RQ-007 | Invalid base URLs must fail with a typed provider/runtime error and must not initiate provider network execution. | P0 | `docs/PRD.md` Section 8.5 FR-032, FR-034 |
| DEL-04-05-RQ-008 | Renderer outbound traffic must be canceled unless it targets loopback or the Anthropic API path; logged policy metadata must not contain secrets. | P0 | `docs/SPEC.md` Section 16.3; `docs/PRD.md` Section 8.5 FR-033; `docs/CONTRACT.md` K-NET-1 |
| DEL-04-05-RQ-009 | Node/SDK provider calls must not silently broaden the network policy beyond explicit product scope. | P0 | `docs/SPEC.md` Section 16.3 |
| DEL-04-05-RQ-010 | Remote MCP, plugins, and non-Anthropic network tools must remain out of current scope unless separately governed. | P0 | `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1 |
| DEL-04-05-RQ-011 | Provider and SDK failures must be classified at least as auth, rate limit, timeout, API error, network error, invalid base URL, or policy violation. | P1 | `docs/PRD.md` Section 8.5 FR-034 |
| DEL-04-05-RQ-012 | Classified provider failures must produce typed `SDK_FAILURE` details with key redaction. | P1 | `docs/PRD.md` Section 8.5 FR-034 |
| DEL-04-05-RQ-013 | Provider integration must remain behind the SDK-backed turn boundary and must not move provider-specific semantics into the HTTP route. | P0 | `docs/PRD.md` Section 8.5 FR-035 |
| DEL-04-05-RQ-014 | Provider/SDK-specific identifiers and failure details must remain adapter metadata and must not redefine public Chirality event or API contracts. | P0 | `docs/CONTRACT.md` K-ENGINE-4; `docs/SPEC.md` Sections 10 and 12.4 |
| DEL-04-05-RQ-015 | Shipped builds must keep SDK settings isolated with `settingSources: []`; provider key/base URL behavior must not depend on ambient user/local Claude settings. | P0 | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| DEL-04-05-RQ-016 | The implementation must include key handoff, base URL/network, and redaction fixtures/tests. Exact file paths are TBD. | P0 | `_CONTEXT.md` "Anticipated Artifacts"; decomposition row `DEL-04-05` |
| DEL-04-05-RQ-017 | ASSUMPTION: The provider wrapper should expose only redacted metadata to `HarnessEvent`, `UIEvent`, run logging, and test assertions. | P0 | Inferred from `docs/CONTRACT.md` K-EVENT-6 and K-ENGINE-4 |

<!-- sow-source-end -->

### CLM-010 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":56,"line_start":47,"source_sha256":"3baa856f1581a65f3a2dd5e088d2d1acaf4e7e8a3d7fc7a17b2389e9b1bd19c1","target_id":"CLM-010"} -->
##### Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Chirality runtime engine boundary | Provider integration must remain behind product-owned `AgentEnginePort` / `RuntimeEngineContract` and adapter boundaries. | `docs/CONTRACT.md` Section 1.4 |
| Chirality API key and network invariants | API keys are non-project convenience state; network is loopback plus Anthropic API path unless amended. | `docs/CONTRACT.md` Section 1.9 |
| SDK runtime configuration contract | `settingSources: []`, active-turn-only API key handoff, safe metadata recording. | `docs/SPEC.md` Section 12 |
| Attachments, API keys, and network policy | Electron safeStorage location, key logging prohibitions, renderer and Node/SDK network policy. | `docs/SPEC.md` Section 16 |
| PRD Anthropic provider policy | FR-030 through FR-035 describe key precedence, base URL, renderer network policy, provider error classes, and SDK turn boundary. | `docs/PRD.md` Section 8.5, MATCH status — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-011 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":68,"line_start":57,"source_sha256":"3baa856f1581a65f3a2dd5e088d2d1acaf4e7e8a3d7fc7a17b2389e9b1bd19c1","target_id":"CLM-011"} -->
##### Verification

| Requirement IDs | Verification Approach | Evidence Expected |
|---|---|---|
| RQ-001, RQ-003, RQ-004, RQ-005 | Unit tests for key source resolution and SDK environment construction. | Key handoff tests prove UI key precedence, fallback to `ANTHROPIC_API_KEY`, fallback to `CHIRALITY_ANTHROPIC_API_KEY`, and `none` status with no key. |
| RQ-002, RQ-005, RQ-012, RQ-017 | Redaction tests and fixture snapshots. | No cleartext key or configured secret variant appears in logs, `HarnessEvent`, `UIEvent`, SDK error details, stderr/debug output, or tool artifacts. |
| RQ-006, RQ-007 | Base URL validation tests. | Accepted: `https://api.anthropic.com` with empty or 443 port and no credentials. Rejected: other host, scheme, credentials, non-443 port, malformed URL. |
| RQ-008, RQ-009, RQ-010 | Electron/network guard tests and SDK provider bridge tests. | Renderer non-loopback/non-Anthropic requests are canceled; provider bridge tests show Node/SDK calls do not silently broaden policy. |
| RQ-011, RQ-012 | Provider error classification tests. | Auth, rate limit, timeout, API, network, invalid base URL, and policy violation map to typed `SDK_FAILURE` details with redaction. |
| RQ-013, RQ-014, RQ-015 | Integration/conformance tests and code review. | HTTP route remains transport/lifecycle adapter; provider-specific data stays in adapter metadata; shipped SDK options use `settingSources: []`. |
| RQ-016 | Artifact existence and coverage review. | Provider wrapper, key handoff tests, base URL/network tests, and redaction fixtures exist in implementation paths selected by the owning code change. |

<!-- sow-source-end -->

### CLM-012 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":86,"line_start":69,"source_sha256":"3baa856f1581a65f3a2dd5e088d2d1acaf4e7e8a3d7fc7a17b2389e9b1bd19c1","target_id":"CLM-012"} -->
##### Documentation

Required artifacts for this deliverable:

- Provider wrapper or equivalent SDK adapter boundary module.
- Key handoff tests.
- Base URL and network tests.
- Provider error classification tests.
- Redaction fixtures.
- Notes identifying final implementation paths and any residual risk from SDK behavior, if applicable.

TBD:

- Exact module paths.
- Exact test filenames.
- Whether provider/base URL policy is implemented as a shared helper, `TurnEngine` collaborator, Electron guard module, or a combination.
- Final SDK error object shapes from the accepted SDK package version.

<!-- sow-source-end -->

### CLM-013 — Pass 3 Enrichment Disposition

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":95,"line_start":87,"source_sha256":"3baa856f1581a65f3a2dd5e088d2d1acaf4e7e8a3d7fc7a17b2389e9b1bd19c1","target_id":"CLM-013"} -->
##### Pass 3 Enrichment Disposition

| ItemID | Disposition | Specification Impact | Source Reread Evidence |
|---|---|---|---|
| F-001 | converted to TBD | Exact provider wrapper, key handoff test, base URL/network test, and redaction fixture paths remain required artifacts, but final paths cannot be filled until the owning implementation selects them. | `_CONTEXT.md` "Anticipated Artifacts"; decomposition row `DEL-04-05`; `Specification.md` "Documentation". |
| D-001 | already covered | The `Source-State Warning` remains a final-acceptance blocker for PRD-derived provider-policy rows rather than a specification fact to resolve in P3. | `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.5; `Specification.md` "Source-State Warning". |
| D-003 | converted to TBD | Final SDK error object shapes remain TBD pending the accepted SDK package/version probe; the requirement keeps the stable classification classes without freezing SDK object shapes. | `docs/PRD.md` Section 8.5 FR-034; `docs/CONTRACT.md` K-ENGINE-4; `Specification.md` "Documentation". |
| E-001 | converted to TBD | Redaction evidence is required for logs, events, SDK/provider errors, stderr/debug output, and tool artifacts, but no completed fixture or validation artifact is present in this deliverable folder. | `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1; `docs/PRD.md` FR-075; `Specification.md` "Verification". |

<!-- sow-source-end -->

### CLM-014 — Source-State Warning

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":98,"line_start":96,"source_sha256":"3baa856f1581a65f3a2dd5e088d2d1acaf4e7e8a3d7fc7a17b2389e9b1bd19c1","target_id":"CLM-014"} -->
##### Source-State Warning

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
<!-- sow-source-end -->

- **AC-001** — The DEL-04-05 evidence package contains a provider wrapper, key handoff tests, base URL/network tests, provider-expansion guard tests, and redaction fixtures demonstrating API key precedence, current Anthropic network policy, provider error classification, no unauthorized provider/network expansion, and redacted adapter environment handoff for SOW-019, SOW-020, SOW-021 and OBJ-004, OBJ-008.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":4,"line_start":1,"source_sha256":"4c4d9a6b943b9bf323d698d40f1d79f54f966698995cbd05ebbe8b4af193c488","target_id":"CLM-015"} -->
#### Procedure: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-016 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":10,"line_start":5,"source_sha256":"4c4d9a6b943b9bf323d698d40f1d79f54f966698995cbd05ebbe8b4af193c488","target_id":"CLM-016"} -->
##### Purpose

Produce and verify the provider-boundary implementation for Anthropic key resolution, base URL validation, network policy bridging, provider error classification, and redacted SDK environment handoff.

Sources: `_CONTEXT.md` "Deliverable Scope" and "Anticipated Artifacts"; `docs/SPEC.md` Sections 12 and 16; `docs/PRD.md` Section 8.5.

<!-- sow-source-end -->

### CLM-017 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":21,"line_start":11,"source_sha256":"4c4d9a6b943b9bf323d698d40f1d79f54f966698995cbd05ebbe8b4af193c488","target_id":"CLM-017"} -->
##### Prerequisites

| Prerequisite | Status / Notes |
|---|---|
| Accepted decomposition reference | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` row `DEL-04-05`. |
| Source documents | `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/PLAN.md`, and `docs/PRD.md` are locally accessible. |
| PRD source warning | `docs/PRD.md` is `MATCH`; treat PRD-specific implementation detail as needing revalidation before final acceptance. — reconciled under D-APP-38 |
| Upstream dependency edges | TBD - `_DEPENDENCIES.md` has no accepted upstream/downstream edges yet. |
| first-adapter probe/version decision | TBD - required for exact SDK error object shapes and packaged SDK behavior. |
| Final implementation paths | TBD - provider wrapper, tests, and fixtures paths are not fixed by accessible source text. |

<!-- sow-source-end -->

### CLM-018 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":84,"line_start":22,"source_sha256":"4c4d9a6b943b9bf323d698d40f1d79f54f966698995cbd05ebbe8b4af193c488","target_id":"CLM-018"} -->
##### Steps

1. Confirm source and scope.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the decomposition row for `DEL-04-05`.
   - Confirm this deliverable remains limited to API key precedence, current shipped Anthropic network policy, provider error classification, and redacted SDK environment handoff.

2. Define the provider-boundary API.
   - Select the implementation path for the provider wrapper or equivalent SDK adapter boundary.
   - Keep provider-specific and SDK-specific details inside adapter metadata.
   - Do not move provider integration into the HTTP route.
   - Mark final path in implementation notes when selected.

3. Implement API key resolution.
   - Resolve UI safeStorage key first.
   - Resolve `ANTHROPIC_API_KEY` second.
   - Resolve `CHIRALITY_ANTHROPIC_API_KEY` third.
   - Return safe status metadata only: `ui`, `env`, or `none`.
   - Do not write key material to working root, docs, logs, runtime events, SDK transcripts if avoidable, or tool artifacts.

4. Implement SDK environment handoff.
   - Supply key material to SDK environment only for the active turn.
   - Keep shipped SDK settings isolated with `settingSources: []`.
   - Route SDK stderr/debug/error text through redaction before durable recording.
   - Record only safe SDK metadata such as version, permission posture, settings-source posture, and session linkage where applicable.

5. Implement base URL validation.
   - Parse candidate URLs with a structured URL parser.
   - Accept only `https://api.anthropic.com` with no username/password and empty or 443 port.
   - Reject malformed URLs, non-HTTPS schemes, non-Anthropic hosts, embedded credentials, and non-443 ports.
   - Ensure rejected base URLs do not initiate provider execution.

6. Implement renderer network policy.
   - Preserve allowlisting for loopback and Anthropic API path.
   - Cancel non-allowlisted outbound renderer requests.
   - Log only policy metadata without secrets.
   - Keep remote MCP, plugins, and non-Anthropic network tools out of current scope.

7. Implement Node/SDK network bridge.
   - Ensure Node/SDK provider calls do not silently broaden current shipped network policy.
   - ASSUMPTION: If SDK internals cannot expose all network calls directly, rely on a product-owned wrapper, environment restriction, and tests/probes to demonstrate policy behavior; record any residual risk for human review.

8. Implement provider error classification.
   - Classify at least auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation.
   - Emit typed `SDK_FAILURE` details with redaction.
   - Preserve retry/debug context without cleartext keys or raw provider payloads.

9. Add tests and fixtures.
   - Add key handoff tests for precedence and no project writes.
   - Add base URL validation tests for accepted and rejected URL shapes.
   - Add renderer/network policy tests for allowlisted and canceled requests.
   - Add provider classification tests for each required class.
   - Add redaction fixtures for key material, SDK/provider errors, stderr/debug output, and policy-denial metadata.

10. Run focused validation.
   - Run the selected unit/API test command for the touched implementation paths.
   - Run typecheck if provider-boundary types, runtime event details, or SDK option shapes changed.
   - If available for this slice, run the harness/security validation covering network/key behavior.

11. Record residuals.
   - Document exact implementation paths.
   - Record any first-adapter probe dependency, PRD hash revalidation need, or Node/SDK network-enforcement residual risk.
   - Keep unresolved values as `TBD` rather than inferring final acceptance.

<!-- sow-source-end -->

### CLM-019 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":98,"line_start":85,"source_sha256":"4c4d9a6b943b9bf323d698d40f1d79f54f966698995cbd05ebbe8b4af193c488","target_id":"CLM-019"} -->
##### Verification

| Check | Expected Result | Source |
|---|---|---|
| Key precedence | UI safeStorage key wins over `ANTHROPIC_API_KEY`, which wins over `CHIRALITY_ANTHROPIC_API_KEY`. | `docs/SPEC.md` Section 12.3 |
| Key non-persistence | No key material appears in project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` Section 16.2 |
| SDK handoff | Key is supplied only for active turns and redacted from emitted records. | `docs/SPEC.md` Section 12.3 |
| Base URL | Only `https://api.anthropic.com` with no credentials and empty/443 port is accepted. | `docs/PRD.md` Section 8.5 FR-032 |
| Renderer network | Non-loopback/non-Anthropic renderer outbound requests are canceled and logged without secrets. | `docs/PRD.md` Section 8.5 FR-033 |
| Node/SDK network | Provider calls do not broaden explicit product network scope. | `docs/SPEC.md` Section 16.3 |
| Error classification | Auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation produce typed redacted `SDK_FAILURE` details. | `docs/PRD.md` Section 8.5 FR-034 |
| Adapter boundary | Provider-specific semantics stay behind `TurnEngine`, `sdk-options-builder`, `sdk-message-mapper`, or equivalent adapter boundary and do not define public API/event contracts. | `docs/PRD.md` FR-035; `docs/CONTRACT.md` K-ENGINE-4 |
| Settings isolation | Shipped SDK options use `settingSources: []`. | `docs/SPEC.md` Section 12.2 |

<!-- sow-source-end -->

### CLM-020 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":111,"line_start":99,"source_sha256":"4c4d9a6b943b9bf323d698d40f1d79f54f966698995cbd05ebbe8b4af193c488","target_id":"CLM-020"} -->
##### Records

The implementation owner should produce or update these records:

- Provider wrapper or equivalent adapter-boundary code.
- Key resolution and SDK environment handoff tests.
- Base URL validation tests.
- Renderer and Node/SDK network policy tests.
- Provider error classification tests.
- Redaction fixture set.
- Validation command output or CI artifact references.
- Residual risk notes for SDK behavior that cannot be directly enforced or observed.

<!-- sow-source-end -->

### CLM-021 — Pass 3 Evidence Closure

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":121,"line_start":112,"source_sha256":"4c4d9a6b943b9bf323d698d40f1d79f54f966698995cbd05ebbe8b4af193c488","target_id":"CLM-021"} -->
##### Pass 3 Evidence Closure

| ItemID | Disposition | Procedure Impact | Source Reread Evidence |
|---|---|---|---|
| D-001 | already covered | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.5; `Procedure.md` "Human Rulings Needed". — reconciled under D-APP-38 |
| D-002 | converted to TBD | Node/SDK network enforcement remains an implementation-specific decision. The procedure requires the implementation owner to record the selected mechanism and residual risk instead of assuming SDK internals expose direct hooks. | `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1; `Procedure.md` Steps 7 and 11. |
| X-001 | converted to TBD | Validation record references for redaction fixture output, SDK stderr/debug redaction, and policy-denial metadata remain TBD until tests run and artifacts exist. | `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1; `docs/PLAN.md` Section 6.3; `Procedure.md` "Verification" and "Records". |
| X-002 | converted to TBD | Evidence that Node/SDK provider calls do not broaden network scope must be produced by the selected wrapper, environment restriction, tests, or probes; no completed evidence exists in this deliverable folder. | `docs/SPEC.md` Section 16.3; `docs/PRD.md` Section 12.2 required checks; `Procedure.md` Steps 7 and 10. |
| E-001 | converted to TBD | Audit evidence for absence of cleartext key material across logs, events, SDK errors, stderr/debug output, and tool artifacts remains required but unproduced. | `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1; `docs/PRD.md` FR-075 and NFR-002; `Procedure.md` "Verification" and "Records". |

<!-- sow-source-end -->

### CLM-022 — Human Rulings Needed

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":128,"line_start":122,"source_sha256":"4c4d9a6b943b9bf323d698d40f1d79f54f966698995cbd05ebbe8b4af193c488","target_id":"CLM-022"} -->
##### Human Rulings Needed

| ID | Ruling | Why |
|---|---|---|
| HR-DEL-04-05-001 | Confirm accepted PRD source snapshot or update `_REFERENCES.md` after source-state reconciliation. | `docs/PRD.md` is `MATCH`, but this deliverable depends on PRD Section 8.5 details. — reconciled under D-APP-38 |
| HR-DEL-04-05-002 | Confirm final implementation path for the provider wrapper and tests. | Accessible sources define behavior and anticipated artifacts, not file layout. |
| HR-DEL-04-05-003 | Confirm how Node/SDK network policy is enforced if SDK internals do not expose direct network hooks. | `docs/SPEC.md` requires no silent broadening, but mechanism is implementation-specific. |
<!-- sow-source-end -->

- **VER-001** — Verify the provider wrapper, key handoff tests, base URL/network tests, provider-expansion guard tests, and redaction fixtures against SOW-019, SOW-020, SOW-021 and OBJ-004, OBJ-008 for key precedence, current Anthropic network policy, provider error classification, no unauthorized provider/network expansion, and redacted adapter environment handoff.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":4,"line_start":1,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-023"} -->
#### Guidance: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-024 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":10,"line_start":5,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-024"} -->
##### Purpose

This deliverable keeps Anthropic provider access inside Chirality-owned runtime governance while adopting the Claude Agent SDK as the preferred engine substrate. It protects API keys, constrains network access, keeps provider/SDK details behind adapter boundaries, and gives downstream validation clear evidence for key precedence, base URL policy, network policy, and redacted failure handling.

Sources: `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` Sections 1.4 and 1.9; `docs/SPEC.md` Sections 12 and 16; decomposition row `DEL-04-05`.

<!-- sow-source-end -->

### CLM-025 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":12,"line_start":11,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-025"} -->
##### Principles

<!-- sow-source-end -->

### CLM-026 — Preserve Chirality Ownership

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":18,"line_start":13,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-026"} -->
###### Preserve Chirality Ownership

The SDK may host generic runtime mechanics, but Chirality owns the product contract. Provider key handling, network policy, event semantics, redaction, and public APIs must remain Chirality-defined rather than SDK-shaped.

Sources: `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-5.

<!-- sow-source-end -->

### CLM-027 — Treat Keys as Convenience State, Not Project Truth

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":24,"line_start":19,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-027"} -->
###### Treat Keys as Convenience State, Not Project Truth

API keys are runtime convenience state. They must not be written into the working root, document kit, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. Tests should prove both positive behavior, such as correct source precedence, and negative behavior, such as absence from project files and emitted records.

Sources: `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` Sections 12.3 and 16.2.

<!-- sow-source-end -->

### CLM-028 — Fail Closed on Provider Boundary Violations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":30,"line_start":25,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-028"} -->
###### Fail Closed on Provider Boundary Violations

Invalid base URLs, non-allowlisted renderer requests, policy violations, and provider failures should become typed failures that preserve retry/debug context without exposing secrets. Invalid base URL and policy-violation cases should stop execution before provider calls proceed.

Sources: `docs/PRD.md` Section 8.5 FR-032 through FR-034; `docs/CONTRACT.md` K-NET-1.

<!-- sow-source-end -->

### CLM-029 — Keep Network Scope Narrow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":36,"line_start":31,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-029"} -->
###### Keep Network Scope Narrow

Current shipped network scope is loopback plus the Anthropic API path. Remote MCP, plugins, and non-Anthropic network tools are future-governed scope and should not be introduced as part of this deliverable.

Sources: `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1.

<!-- sow-source-end -->

### CLM-030 — Redact at Every Boundary

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":42,"line_start":37,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-030"} -->
###### Redact at Every Boundary

Redaction should apply before details cross from provider/SDK internals into `HarnessEvent`, `UIEvent`, run logs, fixtures, or diagnostics. A provider wrapper should be suspicious of SDK errors and stderr/debug text because upstream message shapes can drift.

Sources: `docs/CONTRACT.md` K-EVENT-6; `docs/PLAN.md` Section 6.3; `docs/PRD.md` FR-075 and KG-021.

<!-- sow-source-end -->

### CLM-031 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":55,"line_start":43,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-031"} -->
##### Considerations

| Topic | Guidance | Source |
|---|---|---|
| UI key precedence | Prefer a simple resolver contract that returns `{ source, env }` or equivalent safe metadata, never raw values in status objects. | `docs/SPEC.md` Sections 12.3 and 16.2 |
| Environment variable names | Support both `ANTHROPIC_API_KEY` and `CHIRALITY_ANTHROPIC_API_KEY` in the documented order. | `docs/SPEC.md` Section 12.3 |
| Base URL parsing | Use a URL parser rather than string prefix checks so credentials, scheme, host, and port are validated explicitly. | `docs/PRD.md` Section 8.5 FR-032 |
| Renderer guard | Renderer guard logging should capture safe policy metadata only, such as category and redacted URL classification, not headers or credentials. | `docs/PRD.md` Section 8.5 FR-033 |
| Node/SDK bridge | Treat Node/SDK provider network calls as in-scope only when they remain within Anthropic provider policy. The exact enforcement mechanism is TBD. | `docs/SPEC.md` Section 16.3 |
| Error mapping | Normalize provider/SDK failures to typed application details without leaking upstream SDK object shape into public contracts. | `docs/CONTRACT.md` K-ENGINE-4; `docs/PRD.md` FR-034 |
| SDK drift | Keep classification logic version-aware and covered by tests because SDK API and error shapes may change. | `docs/PRD.md` KG-021; `docs/CONTRACT.md` K-SDK-2 |
| Settings isolation | Do not allow ambient Claude settings to alter key, base URL, or network policy behavior in shipped builds. | `docs/SPEC.md` Section 12.2 |

<!-- sow-source-end -->

### CLM-032 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":65,"line_start":56,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-032"} -->
##### Trade-offs

| Choice | Benefit | Cost / Risk | Recommended Posture |
|---|---|---|---|
| Single provider wrapper | Centralizes redaction, key handoff, base URL validation, and provider error mapping. | May become too broad if it absorbs turn lifecycle or Provider/SDK message mapping. | Keep wrapper provider-boundary focused and delegate turn lifecycle to `TurnEngine`. |
| Separate helpers for key, URL, network, and error classification | Easier unit testing and clearer ownership. | Requires careful integration tests to prove boundary behavior as a whole. | Prefer small helpers plus provider-boundary integration tests. |
| Rely on SDK defaults for network/key behavior | Lower initial code volume. | Violates product-owned governance and may be opaque or version-sensitive. | Do not rely on opaque SDK defaults for product-critical behavior. |
| Allow configurable base URL | Useful for mocks and future providers. | Current product requirement accepts only Anthropic production API for shipped policy. | Keep shipped validation strict; test or dev-only escape hatches require explicit governance if introduced. |
| Log rich provider errors | Improves diagnosis. | High secret-leak risk and SDK-shape leakage. | Log typed/redacted metadata and keep raw provider payloads out of durable records unless redaction is proven. |

<!-- sow-source-end -->

### CLM-033 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":74,"line_start":66,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-033"} -->
##### Examples

Supported examples from available sources:

- Key precedence example: if a UI safeStorage key exists, it is used before `ANTHROPIC_API_KEY`; if no UI key exists, `ANTHROPIC_API_KEY` is used before `CHIRALITY_ANTHROPIC_API_KEY`. Source: `docs/SPEC.md` Section 12.3.
- Safe status example: API key status may report `ui`, `env`, or `none`; it must not report the key. Source: `docs/SPEC.md` Section 16.2.
- Base URL example: `https://api.anthropic.com` with empty or 443 port and no credentials is accepted; non-Anthropic hosts, embedded credentials, or non-443 ports are rejected. Source: `docs/PRD.md` Section 8.5 FR-032.
- Network example: renderer outbound requests are restricted to loopback and Anthropic API path; broader remote MCP/plugin/network access is future scope. Source: `docs/SPEC.md` Section 16.3.

<!-- sow-source-end -->

### CLM-034 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":80,"line_start":75,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-034"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No source conflict identified during P1/P2 drafting. | TBD | TBD | TBD | TBD | TBD |

<!-- sow-source-end -->

### CLM-035 — Open Items

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":88,"line_start":81,"source_sha256":"dcf3a80594a070a59bb72025c28b38699e1d6c6a074876428e24bb7eacfd7fb8","target_id":"CLM-035"} -->
##### Open Items

| ID | Item | Reason |
|---|---|---|
| OI-DEL-04-05-001 | Exact provider wrapper module path is TBD. | Decomposition names the artifact, but source corpus does not prescribe file layout. |
| OI-DEL-04-05-002 | Exact Node/SDK network enforcement mechanism is TBD. | `docs/SPEC.md` requires Node/SDK calls not to broaden policy, but implementation mechanism is not fixed in the accessible sources. |
| OI-DEL-04-05-003 | Exact SDK error object taxonomy is TBD. | SDK version/probe results belong to adjacent R0/R1 work and may affect classifier details. |
| OI-DEL-04-05-004 | PRD-derived claims require revalidation before final acceptance. | `_REFERENCES.md` reports `docs/PRD.md` `MATCH`. — reconciled under D-APP-38 |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-019 SOW-020 SOW-021 OBJ-004 OBJ-008 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
