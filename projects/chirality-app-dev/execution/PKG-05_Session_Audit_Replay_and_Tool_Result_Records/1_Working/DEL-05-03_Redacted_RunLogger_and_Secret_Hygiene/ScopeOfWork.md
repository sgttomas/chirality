---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-03
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-021, SOW-041]
package_objective_refs: [OBJ-003, OBJ-008]
---

# Scope of Work — DEL-05-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-03` in service of project scope [SOW-021, SOW-041] and package objectives [OBJ-003, OBJ-008].

- **OUT-001** — Source-preserving migration contract for DEL-05-03 Redacted RunLogger and Secret Hygiene.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-05-03 Redacted RunLogger and Secret Hygiene

> #### Datasheet: DEL-05-03 Redacted RunLogger and Secret Hygiene
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-05-03 |
> | Deliverable Name | Redacted RunLogger and Secret Hygiene |
> | Package | PKG-05 Session Audit, Replay, and Tool Result Records |
> | Decomposition Variant | SOFTWARE_DECOMP v3.2 |
> | Responsible Party | TBD |
> | Type | SECURITY_CONTROL |
> | Context Envelope | S |
> | Scope Items | SOW-021, SOW-041 |
> | Supporting Objectives | OBJ-003, OBJ-008 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary control surface | Redaction of provider, SDK, tool, and run logs before key material or secrets enter runtime records. | `_CONTEXT.md`; `docs/PRD.md` Section 8.12; `docs/PLAN.md` Section 6.3 |
> | Runtime logger target | `RunLogger` or equivalent redacted structured runtime logger. | `docs/PRD.md` R1 implementation targets |
> | Secret classes explicitly named by sources | API keys and configured secret variants. | `docs/PRD.md` FR-075; `docs/PRD.md` NFR-002 |
> | Records covered | Runtime events, run logs, tool artifacts, provider errors, SDK errors, SDK stderr/debug logs, and event records. | `docs/CONTRACT.md` K-EVENT-6; `docs/PLAN.md` Section 6.3; `docs/PRD.md` FR-075 |
> | Canonical audit record relation | `.chirality/sessions/<sessionId>/events.jsonl` remains the product-owned Chirality audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` K-EVENT-4, K-SDK-3; `docs/SPEC.md` Sections 8.4 and 9 |
> | Provider error relation | Provider errors must be classified and produce typed `SDK_FAILURE` details with key redaction. | `docs/PRD.md` Section 8.5, FR-034 |
> | Tool result relation | Large or sensitive tool results must be budgeted, previewed, stored as artifacts, or redacted according to policy. | `docs/CONTRACT.md` K-EVENT-7; `docs/PRD.md` Section 10.5 |
> | Existing code context | Current source tree contains Anthropic provider redaction helpers and tests for configured API-key redaction. | `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`; `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Requirement-Relevant Fact | Source |
> |---|---|---|
> | API key storage | API keys are non-project convenience state and must not be written to project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` FR-031; `docs/SPEC.md` Section 12.3 |
> | API key handoff | Key material is supplied to the SDK environment only as needed for active turns and redacted from logs/events. | `docs/SPEC.md` Section 12.3; `docs/PLAN.md` R1 |
> | Event payloads | `HarnessEvent.data` payloads must avoid secrets. | `docs/SPEC.md` Section 9; `docs/PRD.md` Section 10.4 |
> | SDK boundaries | SDK messages, IDs, tool names, transcript paths, and external names may appear only as adapter metadata under product-owned contracts. | `docs/SPEC.md` Section 10.3; `docs/DIRECTIVE.md` Section 4.2 |
> | Source warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md`; human runtime instruction — reconciled under D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Description | Status |
> |---|---|---|
> | Redaction helper | Shared helper that redacts configured API key material and configured secret variants before text or structured data is logged or persisted. | TBD: final module path and public API |
> | Run logger | Structured runtime logger that applies the redaction helper before emitting logs, runtime events, error details, or debug/stderr captures. | TBD: final module path; anticipated as `frontend/src/lib/harness/run-logger.ts` by PRD R1 |
> | Provider error fixtures | Fixtures covering auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation redaction. | TBD |
> | Tool result redaction gate | Policy hook ensuring sensitive tool outputs are redacted or withheld before inline event payloads or artifacts are persisted. | TBD: exact policy integration point |
> | Tests | Unit and integration tests proving configured key variants and provider/SDK/tool/run-log paths do not leak secrets. | TBD: final test names; current provider redaction tests exist |
>

### CLM-006 — Pass 3 Implementation Slots

> ##### Pass 3 Implementation Slots
>
> | Slot | Required Record | Current Disposition | Source |
> |---|---|---|---|
> | Shared redaction helper identity | Final module path, exported API name, accepted replacement token, and supported configured-secret schema. | TBD until implementation selects the shared helper contract. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` FR-075 |
> | RunLogger identity | Final module path and public logging surface used by provider errors, SDK diagnostics, event emission, tool-result handling, and run logs. | TBD; PRD R1 names `run-logger.ts` as an implementation target but not an accepted final path. | `docs/PLAN.md` R1; `docs/PRD.md` R1 implementation targets |
> | Boundary inventory | Discovered code paths for provider errors, SDK errors, SDK stderr/debug logs, `HarnessEvent.data`, run logs, and tool-result persistence/display. | TBD until code discovery records the implementation paths. | `docs/SPEC.md` Section 9; `docs/PRD.md` Sections 10.3.1, 10.4, 10.5 |
>

### CLM-007 — References

> ##### References
>
> | RefID | Source | Notes |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Runtime logs and API keys are non-authoritative unless governed import occurs; secrets stay out of project files and event payloads. |
> | REF-002 | `docs/CONTRACT.md` | K-EVENT-6 and K-KEY-1 are the primary invariants for this deliverable. |
> | REF-003 | `docs/SPEC.md` | Runtime event schema, SDK adapter rules, and API-key handling rules. |
> | REF-004 | `docs/TYPES.md` | `HarnessEvent`, Runtime Audit Mirror, Project Truth, and SDK transcript vocabulary. |
> | REF-005 | `docs/PLAN.md` | R1 sequencing and security/privacy acceptance notes. |
> | REF-006 | `docs/PRD.md` | Product requirements for provider error classification, runtime redaction, session events, and R1 implementation targets. MATCH status recorded in `_REFERENCES.md`. — reconciled under D-APP-38 |
> | REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method; SECURITY_CONTROL type definition. |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-03 Redacted RunLogger and Secret Hygiene

> #### Specification: DEL-05-03 Redacted RunLogger and Secret Hygiene
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies the security control for redacting provider, SDK, tool, and run-log data so key material and configured secrets do not enter Chirality runtime records.
>
> In scope:
>
> - Redaction helper behavior for configured API keys and configured secret variants.
> - Redacted `RunLogger` or equivalent runtime logging surface.
> - Secret hygiene for `HarnessEvent` payloads, provider errors, SDK errors, SDK stderr/debug logs, and tool result artifacts.
> - Tests and fixtures proving provider error classification and redaction behavior.
>
> Out of scope:
>
> - Tool permission semantics and allow/deny policy, except where redaction must apply after permitted tool execution.
> - Canonical session folder layout and append-only JSONL writer ownership, which belong to adjacent PKG-05 deliverables.
> - API key storage implementation, except that this deliverable must not undermine the existing safeStorage/env precedence rules.
> - `frontend/scripts/scan-secret-evidence.mjs` is an unrequired
>   defense-in-depth proof surface. PKG-09 validation may formalize that command
>   in a future governed change; D-APP-56 R4-P02 does not make it a DEL-05-03
>   product obligation.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Priority | Source |
> |---|---|---:|---|
> | DEL-05-03-R1 | Runtime events, run logs, tool artifacts, and provider errors MUST redact secrets and avoid storing API keys. | P0 | `docs/CONTRACT.md` K-EVENT-6 |
> | DEL-05-03-R2 | API keys MUST remain non-project convenience state and MUST NOT be written to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. | P0 | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` FR-031, NFR-002 |
> | DEL-05-03-R3 | Runtime logging MUST redact API keys and configured secret variants from SDK errors, tool outputs where policy requires, and event records. | P0 | `docs/PRD.md` FR-075 |
> | DEL-05-03-R4 | Provider error classification MUST produce typed `SDK_FAILURE` details for auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation, with key redaction. | P1 | `docs/PRD.md` FR-034 |
> | DEL-05-03-R5 | SDK debug logs and stderr captures MUST pass through the run logger redaction layer before persistence or display. | P0 | `docs/PRD.md` Section 10.3 notes; `docs/PLAN.md` Section 6.3 |
> | DEL-05-03-R6 | `HarnessEvent.data` payloads MUST avoid secrets; any persisted event data from provider, SDK, hook, permission, tool, or transcript metadata must be redacted first. | P0 | `docs/SPEC.md` Section 9; `docs/PRD.md` Section 10.4 |
> | DEL-05-03-R7 | Large or sensitive tool results MUST be budgeted, previewed, stored as artifacts, or redacted according to policy; sensitive raw values MUST NOT be stored unless a redaction pass has approved the payload. | P0 | `docs/CONTRACT.md` K-EVENT-7; `docs/PRD.md` Section 10.5 |
> | DEL-05-03-R8 | SDK transcripts remain secondary runtime state; this deliverable MUST NOT treat SDK transcripts as canonical project truth or allow unredacted transcript data to replace Chirality JSONL review surfaces. | P0 | `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` Section 8.4 |
> | DEL-05-03-R9 | ASSUMPTION: The redaction helper SHOULD handle raw, URL-encoded, lowercase URL-encoded, and double-encoded configured key variants, because current provider tests already exercise those cases. | P1 | Current code context: `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`; exact product-wide helper API TBD |
> | DEL-05-03-R10 | Redaction MUST preserve enough non-secret metadata for audit and debugging, such as error class, policy category, status, source indicator, artifact metadata, and event type. | P1 | `docs/PRD.md` FR-034, FR-075; `docs/SPEC.md` Sections 9 and 12.3 |
> | DEL-05-03-R11 | Every runtime record or diagnostic write/display path that can carry provider, SDK, tool, run-log, event, or artifact payload data MUST pass through redaction before persistence and before user-visible diagnostic display where the value could reveal configured secrets. | P0 | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PLAN.md` Section 6.3 |
> | DEL-05-03-R12 | The shared redaction helper contract MUST remain TBD until implementation records the final module path, public API, configured-secret schema, supported encoded variants, overlap handling, and accepted replacement token. | P0 | `docs/PRD.md` FR-075; current code context; `docs/CONTRACT.md` K-EVENT-6 |
> | DEL-05-03-R13 | Tool-result hygiene verification MUST cover inline, preview, artifact, redacted, and withheld payload paths before sensitive raw values may be accepted into persisted records. | P0 | `docs/CONTRACT.md` K-EVENT-7; `docs/PRD.md` Section 10.5 |
> | DEL-05-03-R14 | PEC domain-proposal transport credentials and the `pec_session` cookie MUST remain outside returned envelopes, HarnessEvents, error details, logs, artifacts, and model context by construction; the cookie remains in memory only. This documentary ownership does not broaden the API-key-specific runtime logger into a generic secret registry. | P0 | D-APP-52; D-APP-56 R4-P27; D-APP-67 Option B; D-APP-68 ruling 7 |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard or Contract | Applicability |
> |---|---|
> | `docs/CONTRACT.md` K-EVENT-6 | Primary redaction invariant for runtime records. |
> | `docs/CONTRACT.md` K-KEY-1 | Primary key-material hygiene invariant. |
> | `docs/SPEC.md` Section 9 Runtime Event Schema | Defines `HarnessEvent` payload rules, including no secrets. |
> | `docs/SPEC.md` Section 12.3 API Key Handling | Defines key precedence and active-turn-only SDK handoff. |
> | `docs/PRD.md` Section 8.5 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | `docs/PRD.md` Section 8.12 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement | Verification Approach |
> |---|---|
> | DEL-05-03-R1, R2, R3 | Unit tests for redaction helper and run logger using configured key material and representative provider/SDK/tool/run-log payloads. |
> | DEL-05-03-R4 | Provider error fixtures for auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation; assert typed `SDK_FAILURE` details contain no key material. |
> | DEL-05-03-R5 | Tests or harness fixtures for SDK stderr/debug capture through the redaction layer. |
> | DEL-05-03-R6 | Event-schema tests that serialize representative `HarnessEvent` payloads and assert no configured secret variants are present. |
> | DEL-05-03-R7 | Tool-result tests for inline, preview, artifact, and redacted/withheld payload paths. |
> | DEL-05-03-R8 | Replay/session tests confirming Chirality JSONL remains canonical and SDK transcript metadata is treated as secondary adapter metadata. |
> | DEL-05-03-R9 | Extend current provider redaction tests to the shared helper once the helper path is finalized. |
> | DEL-05-03-R10 | Snapshot or structured assertions that non-secret diagnostic metadata survives redaction. |
> | DEL-05-03-R11 | Cross-surface fixture asserting provider errors, SDK stderr/debug logs, SDK errors, `HarnessEvent.data`, run logs, and tool artifacts are redacted before persistence and before display when display could expose secrets. |
> | DEL-05-03-R12 | Contract tests for raw, URL-encoded, lowercase URL-encoded, double-encoded, and overlapping configured key values; final fixture ownership remains TBD until the shared helper API is accepted. |
> | DEL-05-03-R13 | Tool-result tests for small inline data, medium preview data, large artifact storage, explicit redacted payloads, and withheld sensitive payloads. |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required artifacts:
>
> - Redaction helper.
> - Redacted run logger.
> - Run logger tests.
> - Provider error fixtures.
> - Secret hygiene notes for event payloads and tool artifacts.
>
> TBD:
>
> - Final module path for the shared redaction helper.
> - Final module path for `RunLogger` if it differs from the PRD R1 target.
> - Config format for additional non-API-key secret variants.
> - Exact redaction replacement token.
> - Whether SDK transcript redaction can be guaranteed or only avoided/cross-referenced, because source text says SDK transcripts should avoid API keys "if avoidable".
> - Final ownership of provider-local encoded/overlapping key tests after migration to the shared helper.
> - Final source path inventory for provider errors, SDK diagnostics, `HarnessEvent.data`, run logs, and tool result persistence/display.
>

### CLM-014 — D-APP-56 domain-proposal transport amendment (2026-07-12)

> ##### D-APP-56 domain-proposal transport amendment (2026-07-12)
>
> R4-P27 adds domain-proposal transport credential and cookie hygiene to this deliverable's redaction scope under the D-APP-52 lane. This does not unlock the separately gated arbitrary configured-secret registry item reaffirmed by R4-P46.
>
> **D-APP-68 ruling 7 current-state clarification (2026-07-19):** DEL-05-03
> owns the documentary PEC credential/cookie envelope-hygiene boundary.
> `CHIRALITY_PEC_AGENT_EMAIL`, `CHIRALITY_PEC_AGENT_PASSWORD`, login-response
> identity, and the in-memory `pec_session` cookie stay out of tool-result and
> evidence envelopes, HarnessEvents, errors, logs, artifacts, and model context
> by the D-APP-52 allowlisted transport construction. D-APP-67 Option B remains
> binding: the runtime helper is API-key-specific, no generic configured-secret
> registry or `[REDACTED_SECRET]` token is authorized, and PEC password safety
> continues to depend on envelope construction rather than registry coverage.

- **AC-001** — Every legacy source line is preserved exactly and traceably in the migrated ScopeOfWork contract.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-05-03 Redacted RunLogger and Secret Hygiene

> #### Procedure: DEL-05-03 Redacted RunLogger and Secret Hygiene
>

### CLM-016 — Purpose

> ##### Purpose
>
> Define the operational steps for producing and verifying the DEL-05-03 implementation artifacts: a redaction helper, redacted run logger behavior, run logger tests, and provider error fixtures that prevent key material and configured secrets from entering runtime records.
>

### CLM-017 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Accepted source requirements from `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/PRD.md`, `docs/PLAN.md`, and the v3.2 SOFTWARE_DECOMP entry. | Available; `docs/PRD.md` has HASH_MISMATCH warning. |
> | Human assignment of responsible party. | TBD |
> | Final module locations for redaction helper and run logger. | TBD |
> | Final configured-secret variant schema. | TBD |
> | Declared dependency edges for this deliverable. | TBD: `_DEPENDENCIES.md` has no accepted upstream/downstream edges yet. |
>

### CLM-018 — Steps

> ##### Steps
>
> 1. Confirm scope.
>    - Verify the implementation remains limited to redaction and secret hygiene for provider, SDK, tool, run-log, event, and artifact surfaces.
>    - Do not take ownership of tool permission semantics, session layout, or JSONL append/replay beyond redaction hooks.
>
> 2. Inventory persistence and display boundaries.
>    - Identify every code path that can persist or display provider errors, SDK errors, SDK stderr/debug logs, run logs, `HarnessEvent.data`, and tool result payloads.
>    - Mark each boundary as `must redact before write`, `must redact before display`, `artifact policy required`, or `TBD`.
>    - Record the discovered module path, function or class name, payload shape, and owning deliverable when known; retain `TBD` for unknown paths rather than inferring them from adjacent scopes.
>
> 3. Define the redaction helper contract.
>    - Include configured API key values and configured secret variants.
>    - Include raw key material and encoded variants where supported by tests.
>    - Include raw, URL-encoded, lowercase URL-encoded, double-encoded, and overlapping configured key cases once supported by the shared helper.
>    - Preserve non-secret metadata needed for typed errors, audit replay, and debugging.
>    - TBD: replacement token and configuration schema.
>
> 4. Implement or adapt the redacted run logger.
>    - Ensure provider, SDK, tool, and run-log payloads pass through the helper before being written to logs, runtime events, or artifacts.
>    - Route SDK stderr/debug capture through this layer.
>    - Keep `HarnessEvent` and `UIEvent` contracts product-owned and provider-neutral.
>
> 5. Add provider error fixtures.
>    - Cover auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation.
>    - Assert typed `SDK_FAILURE` details remain useful and contain no configured key material or secret variants.
>
> 6. Add event and artifact hygiene tests.
>    - Serialize representative `HarnessEvent` payloads and assert secrets are absent.
>    - Test small inline, medium preview, large artifact, and sensitive-tool-result paths.
>    - Assert sensitive raw values are redacted or withheld before persistence.
>    - Cover inline, preview, artifact, explicit redacted payload, and withheld-payload outcomes for tool results.
>
> 7. Add regression tests for key variants.
>    - Cover raw configured key values.
>    - Cover URL-encoded variants when the implementation supports URL-derived payloads.
>    - Cover overlapping key values so shorter keys do not leave suffixes from longer keys.
>    - ASSUMPTION: current provider tests for encoded and overlapping keys should be migrated or reused against the shared helper.
>
> 8. Run verification.
>    - Run the focused unit tests for the redaction helper, run logger, provider error classification, event serialization, and tool result hygiene.
>    - Run the relevant Section 8/Section 9 validation checks once the runtime-event surfaces exist.
>    - Record unresolved source or implementation decisions as TBD rather than silently accepting gaps.
>

### CLM-019 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | API key storage/path check | No key material is written to working root, docs, runtime events, logs, SDK transcripts if avoidable, or tool artifacts. |
> | Provider error fixtures | All required provider error classes produce typed `SDK_FAILURE` details with no key material. |
> | SDK stderr/debug fixture | Captured SDK diagnostic text passes through redaction before logging or persistence. |
> | Runtime event serialization | Representative `HarnessEvent.data` payloads contain no configured secret values. |
> | Tool result policy | Sensitive tool output is redacted, withheld, or stored only after an approved redaction pass. |
> | Audit usability | Non-secret metadata required for replay, diagnosis, and artifact references remains present. |
> | Cross-surface redaction assertion | Provider errors, SDK stderr/debug logs, SDK errors, run logs, `HarnessEvent.data`, and tool artifacts all pass through redaction before persistence and sensitive display. |
> | SDK transcript boundary | Record whether this deliverable can guarantee transcript redaction or only avoid/cross-reference transcripts; current source state keeps this decision TBD. |
>

### CLM-020 — Records

> ##### Records
>
> Produce or update:
>
> - Redaction helper source file.
> - Redacted run logger source file.
> - Provider error fixtures.
> - Run logger and redaction helper tests.
> - Event serialization and tool result hygiene tests.
> - Test output or validation notes showing no configured secrets appear in runtime records.
>
> TBD:
>
> - Exact test command set.
> - Exact Section 9 validation IDs to run for this deliverable after the runtime event schema lands.
> - Exact discovered code path inventory for provider, SDK, event, run-log, and tool-result surfaces.
> - Whether SDK transcript redaction is guaranteed by DEL-05-03 or only avoided and cross-referenced where feasible.

- **VER-001** — Run deterministic validation, claim mapping, parity, checklist derivation, and script-free rendering; require every check to pass.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-05-03 Redacted RunLogger and Secret Hygiene

> #### Guidance: DEL-05-03 Redacted RunLogger and Secret Hygiene
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-022 — Purpose

> ##### Purpose
>
> DEL-05-03 exists to prevent API keys and configured secrets from becoming runtime audit content. The runtime audit mirror is intentionally rich enough for replay and diagnosis, so this deliverable supplies the redaction control that lets Chirality keep durable event, provider, SDK, tool, and run-log records without converting key material into project truth or persistent runtime leakage.
>
> Primary evidence:
>
> - `docs/CONTRACT.md` K-EVENT-6: runtime events, run logs, tool artifacts, and provider errors must redact secrets and avoid storing API keys.
> - `docs/CONTRACT.md` K-KEY-1: API keys are non-project convenience state and must not be written to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts.
> - `docs/PRD.md` FR-075: runtime logging redacts API keys and configured secret variants from SDK errors, tool outputs where policy requires, and event records.
>

### CLM-023 — Principles

> ##### Principles
>
> 1. Redact before persistence and sensitive display.
>    Any provider, SDK, tool, or run-log payload that may be written to JSONL, artifacts, logs, error details, diagnostics, or user-visible diagnostic surfaces should pass through redaction before it crosses the persistence boundary or a display boundary that could reveal configured secrets.
>
> 2. Keep the audit useful.
>    Redaction should remove secret values while preserving non-secret diagnostic structure such as error class, status, source, policy category, event type, byte counts, truncation flags, and artifact references.
>
> 3. Treat API keys as non-project convenience state.
>    API keys can be resolved from UI safeStorage or environment variables for active turns, but they must not become project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts.
>
> 4. Keep SDK artifacts secondary.
>    SDK transcripts and metadata are resume/debug artifacts. The Chirality audit mirror remains the product-owned record, and SDK-shaped values should be retained only as adapter metadata where source contracts permit it.
>
> 5. Prefer shared redaction over isolated patches.
>    Current code contains provider-local redaction behavior. ASSUMPTION: the deliverable should consolidate product-wide redaction behavior into a shared helper used by provider error handling, run logging, event emission, and tool artifact handling.
>
> 6. Keep shape-specific handling where the payload requires it.
>    A shared helper should centralize secret matching and replacement, while provider errors, SDK diagnostics, `HarnessEvent.data`, and tool artifacts may still need surface-specific adapters so non-secret metadata remains useful and payload policies remain enforceable.
>

### CLM-024 — Considerations

> ##### Considerations
>
> | Topic | Guidance | Source |
> |---|---|---|
> | Provider errors | Preserve typed `SDK_FAILURE` classification while redacting key material and configured secret variants. | `docs/PRD.md` FR-034 |
> | Event records | `HarnessEvent.data` may be rich but must not contain secrets. | `docs/SPEC.md` Section 9 |
> | SDK stderr/debug logs | Treat as potentially sensitive and route through the run logger redaction layer. | `docs/PLAN.md` Section 6.3; `docs/PRD.md` runtime notes |
> | Tool results | Do not rely on truncation alone for sensitive values. Apply redaction or withhold sensitive raw values before inline event payloads or artifact storage. | `docs/PRD.md` Section 10.5 |
> | Secret variants | The PRD names API keys and configured secret variants but does not define the configuration schema. Keep schema-specific claims as TBD until implementation is decided. | `docs/PRD.md` FR-075 |
> | PRD source state | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md`; human runtime instruction — reconciled under D-APP-38 |
>

### CLM-025 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Direction |
> |---|---|
> | Strict redaction vs diagnostic detail | Prefer strict redaction of values while retaining typed, non-secret metadata for debugging. |
> | Inline tool result convenience vs leakage risk | Prefer preview/metadata/artifact references and redaction over raw inline content when sensitivity is possible. |
> | Product-owned audit vs SDK transcript completeness | Keep Chirality JSONL canonical; use SDK transcript linkage as secondary metadata, not as a replacement. |
> | Provider-local helper vs shared helper | Prefer a shared helper once this deliverable is implemented; keep provider-specific handling only where source payload shapes require it. |
> | One helper contract vs payload-specific policy | Centralize configured-secret redaction in one helper, but let each surface decide whether to preserve metadata, redact inline content, store an artifact, or withhold a payload. |
>

### CLM-026 — Examples

> ##### Examples
>
> TBD: final examples should be generated from accepted fixtures after implementation. Candidate examples:
>
> - Provider auth error containing a configured API key is stored as typed `SDK_FAILURE` details with the key replaced by the accepted redaction token.
> - SDK stderr line containing an encoded key variant is logged with the encoded variant redacted.
> - Tool result containing a secret-like configured value is not persisted as raw inline `HarnessEvent.data`; the event stores redacted preview and metadata or withholds the payload according to policy.
>

### CLM-027 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | None | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` | Human runtime instruction | All documents using PRD evidence | Use PRD as accessible source with warning; do not derive unsupported details from it alone. | TBD — reconciled under D-APP-38 |

### CLM-028 — D-APP-68 PEC envelope-hygiene ownership (2026-07-19)

> ##### D-APP-68 PEC envelope-hygiene ownership (2026-07-19)
>
> DEL-05-03 is the sole documentary owner for PEC credential/cookie hygiene at
> the app-harness transport-envelope boundary. The accepted posture is
> construction-based exclusion, not generic runtime redaction: credentials are
> read locally only for login, the login body is discarded, the session cookie
> remains private and in memory, and none of those values is returned or
> persisted through governed envelopes.
>
> D-APP-67 Option B is a hard fence on this mapping. The committed-file taxonomy
> and verifier-quoting rule are ratified, while `readConfiguredApiKeyVariants`
> remains limited to its accepted API-key sources. This section authorizes no
> registry, helper, transport, descriptor, provider, tool, or runtime-source
> expansion.
>
> Sources: D-APP-52; D-APP-67 Option B; D-APP-68 ruling 7.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-021 SOW-041 OBJ-003 OBJ-008 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
