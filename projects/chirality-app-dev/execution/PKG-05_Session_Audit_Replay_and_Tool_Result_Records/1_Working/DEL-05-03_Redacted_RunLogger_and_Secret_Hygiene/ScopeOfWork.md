---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-03
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-021, SOW-041]
package_objective_refs: [OBJ-003, OBJ-008]
---

# Scope of Work — DEL-05-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-03` in service of project scope [SOW-021, SOW-041] and package objectives [OBJ-003, OBJ-008].

- **OUT-001** — App/Runtime-boundary secret-hygiene requirements and conformance evidence for structural redaction before persistence, both SSE hops, replay, diagnostics, errors and artifacts, without duplicating Runtime logger ownership or reading Codex credentials.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-05-03 Redacted RunLogger and Secret Hygiene

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

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

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Named verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures.

### CLM-004 — Conditions

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Named verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures.

### CLM-005 — Construction

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

Unfinished delivery: Deliver structural secret protection at every live sink and preserve metadata; verify the complete synthetic-secret matrix and record the still-unknown external transcript/withheld behavior. Closed event schema v2 and retired daemon acceptance are not prerequisites.

Historical helper contract: `frontend/src/lib/harness/run-logger.ts` exports `readConfiguredApiKeyVariants`, `redactConfiguredApiKeys` and `redactJsonLike`; configured API-key variants are replaced with `[REDACTED_API_KEY]`. D-APP-67 Option B keeps that helper API-key-specific and introduces no non-API-key registry or `[REDACTED_SECRET]` token. This identifies retained compatibility behavior, not current Runtime sink coverage.

### CLM-006 — Pass 3 Implementation Slots

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Implementation Slots
>
> | Slot | Required Record | Current Disposition | Source |
> |---|---|---|---|
> | Shared redaction helper identity | Final module path, exported API name, accepted replacement token, and supported configured-secret schema. | TBD until implementation selects the shared helper contract. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` FR-075 |
> | RunLogger identity | Final module path and public logging surface used by provider errors, SDK diagnostics, event emission, tool-result handling, and run logs. | TBD; PRD R1 names `run-logger.ts` as an implementation target but not an accepted final path. | `docs/PLAN.md` R1; `docs/PRD.md` R1 implementation targets |
> | Boundary inventory | Discovered code paths for provider errors, SDK errors, SDK stderr/debug logs, `HarnessEvent.data`, run logs, and tool-result persistence/display. | TBD until code discovery records the implementation paths. | `docs/SPEC.md` Section 9; `docs/PRD.md` Sections 10.3.1, 10.4, 10.5 |
>


Current requirement and verification boundary: Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

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
> | REF-006 | `docs/PRD.md` | Product requirements for provider error classification, runtime redaction, session events, and R1 implementation targets. HISTORICAL_MATCH status recorded in `_REFERENCES.md`. — reconciled under D-APP-38 |
> | REF-007 | `workflows/software-decomp/WORKFLOW.md` | Decomposition method; SECURITY_CONTROL type definition. |


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-03 Redacted RunLogger and Secret Hygiene

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-009 — Scope

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

### CLM-010 — Requirements

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-05-03-R1 | Runtime events, run logs, tool artifacts, and provider errors MUST redact secrets and avoid storing API keys. |
| DEL-05-03-R2 | API keys MUST remain non-project convenience state and MUST NOT be written to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. |
| DEL-05-03-R3 | Runtime logging MUST redact API keys and configured secret variants from SDK errors, tool outputs where policy requires, and event records. |
| DEL-05-03-R4 | Preserve truthful typed provider/native failure outcomes and safe diagnostic context with secrets removed; the historical SDK_FAILURE taxonomy is compatibility evidence. |
| DEL-05-03-R5 | Redact native App Server diagnostics and SDK compatibility stderr/debug capture before persistence or display. |
| DEL-05-03-R6 | `HarnessEvent.data` payloads MUST avoid secrets; any persisted event data from provider, SDK, hook, permission, tool, or transcript metadata must be redacted first. |
| DEL-05-03-R7 | Large or sensitive tool results MUST be budgeted, previewed, stored as artifacts, or redacted according to policy; sensitive raw values MUST NOT be stored unless a redaction pass has approved the payload. |
| DEL-05-03-R8 | SDK transcripts remain secondary runtime state; this deliverable MUST NOT treat SDK transcripts as canonical project truth or allow unredacted transcript data to replace Chirality JSONL review surfaces. |
| DEL-05-03-R9 | ASSUMPTION: The redaction helper SHOULD handle raw, URL-encoded, lowercase URL-encoded, and double-encoded configured key variants, because current provider tests already exercise those cases. |
| DEL-05-03-R10 | Redaction MUST preserve enough non-secret metadata for audit and debugging, such as error class, policy category, status, source indicator, artifact metadata, and event type. |
| DEL-05-03-R11 | Every runtime record or diagnostic write/display path that can carry provider, SDK, tool, run-log, event, or artifact payload data MUST pass through redaction before persistence and before user-visible diagnostic display where the value could reveal configured secrets. |
| DEL-05-03-R12 | Use the recorded D-APP-67 API-key-only helper contract and replacement token as historical evidence; design and verify structural live-sink redaction without reading Codex credential stores or silently expanding that helper into a generic registry. |
| DEL-05-03-R13 | Tool-result hygiene verification MUST cover inline, preview, artifact, redacted, and withheld payload paths before sensitive raw values may be accepted into persisted records. |
| DEL-05-03-R14 | PEC domain-proposal transport credentials and the `pec_session` cookie MUST remain outside returned envelopes, HarnessEvents, error details, logs, artifacts, and model context by construction; the cookie remains in memory only. This documentary ownership does not broaden the API-key-specific runtime logger into a generic secret registry. |

Verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

Evidence locations: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Named verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures.

### CLM-012 — Verification

Required current checks: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

Named evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Deliver structural secret protection at every live sink and preserve metadata; verify the complete synthetic-secret matrix and record the still-unknown external transcript/withheld behavior. Closed event schema v2 and retired daemon acceptance are not prerequisites.

### CLM-013 — Documentation

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

Unfinished delivery: Deliver structural secret protection at every live sink and preserve metadata; verify the complete synthetic-secret matrix and record the still-unknown external transcript/withheld behavior. Closed event schema v2 and retired daemon acceptance are not prerequisites.

Historical helper contract: `frontend/src/lib/harness/run-logger.ts` exports `readConfiguredApiKeyVariants`, `redactConfiguredApiKeys` and `redactJsonLike`; configured API-key variants are replaced with `[REDACTED_API_KEY]`. D-APP-67 Option B keeps that helper API-key-specific and introduces no non-API-key registry or `[REDACTED_SECRET]` token. This identifies retained compatibility behavior, not current Runtime sink coverage.

### CLM-014 — D-APP-56 domain-proposal transport amendment (2026-07-12)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

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

- **AC-001** — Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

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

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Current implementation/adoption evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

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

Required current checks: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

Named evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Deliver structural secret protection at every live sink and preserve metadata; verify the complete synthetic-secret matrix and record the still-unknown external transcript/withheld behavior. Closed event schema v2 and retired daemon acceptance are not prerequisites.

### CLM-020 — Records

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

Unfinished delivery: Deliver structural secret protection at every live sink and preserve metadata; verify the complete synthetic-secret matrix and record the still-unknown external transcript/withheld behavior. Closed event schema v2 and retired daemon acceptance are not prerequisites.

- **VER-001** — Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-05-03 Redacted RunLogger and Secret Hygiene

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-022 — Purpose

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

### CLM-023 — Principles

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Named verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures.

### CLM-024 — Considerations

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Named verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures.

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

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Deliver structural secret protection at every live sink and preserve metadata; verify the complete synthetic-secret matrix and record the still-unknown external transcript/withheld behavior. Closed event schema v2 and retired daemon acceptance are not prerequisites.

### CLM-028 — D-APP-68 PEC envelope-hygiene ownership (2026-07-19)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

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


Current requirement and verification boundary: Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

Verification: Run synthetic secrets and raw/URL/lowercase/double-encoded variants, overlap cases and nested structures across JSONL, both SSE hops, diagnostics, replay and inline/preview/artifact/redacted/withheld paths. Withheld and external transcript guarantees remain unverified where no fixture exists.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-021 SOW-041 OBJ-003 OBJ-008 | CLM-010  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |

## Retired status detail (2026-09-23)

These clauses retain the operative meaning of the named App `Remaining` entries after their one-time retirement. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R045:** Verify sink-specific structural redaction with candidate-bound evidence. External transcript and withheld behavior remain unknown until observed and must not be inferred from local fixtures.
