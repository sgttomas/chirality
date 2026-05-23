# Procedure: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

## Purpose

Produce and verify the provider-boundary implementation for Anthropic key resolution, base URL validation, network policy bridging, provider error classification, and redacted SDK environment handoff.

Sources: `_CONTEXT.md` "Deliverable Scope" and "Anticipated Artifacts"; `docs/SPEC.md` Sections 12 and 16; `docs/PRD.md` Section 8.5.

## Prerequisites

| Prerequisite | Status / Notes |
|---|---|
| Accepted decomposition reference | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` row `DEL-04-05`. |
| Source documents | `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/PLAN.md`, and `docs/PRD.md` are locally accessible. |
| PRD source warning | `docs/PRD.md` is `HASH_MISMATCH`; treat PRD-specific implementation detail as needing revalidation before final acceptance. |
| Upstream dependency edges | TBD - `_DEPENDENCIES.md` has no accepted upstream/downstream edges yet. |
| SDK probe/version decision | TBD - required for exact SDK error object shapes and packaged SDK behavior. |
| Final implementation paths | TBD - provider wrapper, tests, and fixtures paths are not fixed by accessible source text. |

## Steps

1. Confirm source and scope.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the decomposition row for `DEL-04-05`.
   - Confirm this deliverable remains limited to API key precedence, Anthropic-only network policy, provider error classification, and redacted SDK environment handoff.

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
   - Record any SDK probe dependency, PRD hash revalidation need, or Node/SDK network-enforcement residual risk.
   - Keep unresolved values as `TBD` rather than inferring final acceptance.

## Verification

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

## Records

The implementation owner should produce or update these records:

- Provider wrapper or equivalent adapter-boundary code.
- Key resolution and SDK environment handoff tests.
- Base URL validation tests.
- Renderer and Node/SDK network policy tests.
- Provider error classification tests.
- Redaction fixture set.
- Validation command output or CI artifact references.
- Residual risk notes for SDK behavior that cannot be directly enforced or observed.

## Human Rulings Needed

| ID | Ruling | Why |
|---|---|---|
| HR-DEL-04-05-001 | Confirm accepted PRD source snapshot or update `_REFERENCES.md` after source-state reconciliation. | `docs/PRD.md` is `HASH_MISMATCH`, but this deliverable depends on PRD Section 8.5 details. |
| HR-DEL-04-05-002 | Confirm final implementation path for the provider wrapper and tests. | Accessible sources define behavior and anticipated artifacts, not file layout. |
| HR-DEL-04-05-003 | Confirm how Node/SDK network policy is enforced if SDK internals do not expose direct network hooks. | `docs/SPEC.md` requires no silent broadening, but mechanism is implementation-specific. |
