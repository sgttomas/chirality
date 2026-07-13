# Procedure: DEL-05-03 Redacted RunLogger and Secret Hygiene

## Purpose

Define the operational steps for producing and verifying the DEL-05-03 implementation artifacts: a redaction helper, redacted run logger behavior, run logger tests, and provider error fixtures that prevent key material and configured secrets from entering runtime records.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted source requirements from `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/PRD.md`, `docs/PLAN.md`, and the v3.2 SOFTWARE_DECOMP entry. | Available; `docs/PRD.md` has HASH_MISMATCH warning. |
| Human assignment of responsible party. | TBD |
| Final module locations for redaction helper and run logger. | TBD |
| Final configured-secret variant schema. | TBD |
| Declared dependency edges for this deliverable. | TBD: `_DEPENDENCIES.md` has no accepted upstream/downstream edges yet. |

## Steps

1. Confirm scope.
   - Verify the implementation remains limited to redaction and secret hygiene for provider, SDK, tool, run-log, event, and artifact surfaces.
   - Do not take ownership of tool permission semantics, session layout, or JSONL append/replay beyond redaction hooks.

2. Inventory persistence and display boundaries.
   - Identify every code path that can persist or display provider errors, SDK errors, SDK stderr/debug logs, run logs, `HarnessEvent.data`, and tool result payloads.
   - Mark each boundary as `must redact before write`, `must redact before display`, `artifact policy required`, or `TBD`.
   - Record the discovered module path, function or class name, payload shape, and owning deliverable when known; retain `TBD` for unknown paths rather than inferring them from adjacent scopes.

3. Define the redaction helper contract.
   - Include configured API key values and configured secret variants.
   - Include raw key material and encoded variants where supported by tests.
   - Include raw, URL-encoded, lowercase URL-encoded, double-encoded, and overlapping configured key cases once supported by the shared helper.
   - Preserve non-secret metadata needed for typed errors, audit replay, and debugging.
   - TBD: replacement token and configuration schema.

4. Implement or adapt the redacted run logger.
   - Ensure provider, SDK, tool, and run-log payloads pass through the helper before being written to logs, runtime events, or artifacts.
   - Route SDK stderr/debug capture through this layer.
   - Keep `HarnessEvent` and `UIEvent` contracts product-owned and provider-neutral.

5. Add provider error fixtures.
   - Cover auth, rate limit, timeout, API error, network error, invalid base URL, and policy violation.
   - Assert typed `SDK_FAILURE` details remain useful and contain no configured key material or secret variants.

6. Add event and artifact hygiene tests.
   - Serialize representative `HarnessEvent` payloads and assert secrets are absent.
   - Test small inline, medium preview, large artifact, and sensitive-tool-result paths.
   - Assert sensitive raw values are redacted or withheld before persistence.
   - Cover inline, preview, artifact, explicit redacted payload, and withheld-payload outcomes for tool results.

7. Add regression tests for key variants.
   - Cover raw configured key values.
   - Cover URL-encoded variants when the implementation supports URL-derived payloads.
   - Cover overlapping key values so shorter keys do not leave suffixes from longer keys.
   - ASSUMPTION: current provider tests for encoded and overlapping keys should be migrated or reused against the shared helper.

8. Run verification.
   - Run the focused unit tests for the redaction helper, run logger, provider error classification, event serialization, and tool result hygiene.
   - Run the relevant Section 8/Section 9 validation checks once the runtime-event surfaces exist.
   - Record unresolved source or implementation decisions as TBD rather than silently accepting gaps.

## Verification

| Check | Expected Result |
|---|---|
| API key storage/path check | No key material is written to working root, docs, runtime events, logs, SDK transcripts if avoidable, or tool artifacts. |
| Provider error fixtures | All required provider error classes produce typed `SDK_FAILURE` details with no key material. |
| SDK stderr/debug fixture | Captured SDK diagnostic text passes through redaction before logging or persistence. |
| Runtime event serialization | Representative `HarnessEvent.data` payloads contain no configured secret values. |
| Tool result policy | Sensitive tool output is redacted, withheld, or stored only after an approved redaction pass. |
| Audit usability | Non-secret metadata required for replay, diagnosis, and artifact references remains present. |
| Cross-surface redaction assertion | Provider errors, SDK stderr/debug logs, SDK errors, run logs, `HarnessEvent.data`, and tool artifacts all pass through redaction before persistence and sensitive display. |
| SDK transcript boundary | Record whether this deliverable can guarantee transcript redaction or only avoid/cross-reference transcripts; current source state keeps this decision TBD. |

## Records

Produce or update:

- Redaction helper source file.
- Redacted run logger source file.
- Provider error fixtures.
- Run logger and redaction helper tests.
- Event serialization and tool result hygiene tests.
- Test output or validation notes showing no configured secrets appear in runtime records.

TBD:

- Exact test command set.
- Exact Section 9 validation IDs to run for this deliverable after the runtime event schema lands.
- Exact discovered code path inventory for provider, SDK, event, run-log, and tool-result surfaces.
- Whether SDK transcript redaction is guaranteed by DEL-05-03 or only avoided and cross-referenced where feasible.
