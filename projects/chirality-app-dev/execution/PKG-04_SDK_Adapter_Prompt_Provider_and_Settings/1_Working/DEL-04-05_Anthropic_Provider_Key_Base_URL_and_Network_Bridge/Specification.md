# Specification: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

## Scope

This deliverable covers the security and provider-boundary behavior for Anthropic SDK execution in PKG-04:

- API key precedence and SDK environment handoff.
- Anthropic base URL validation.
- Renderer and Node/SDK network policy bridge.
- Provider and SDK error classification with redaction.
- Tests and fixtures demonstrating the above behavior.

This deliverable excludes:

- General SDK option construction and settings isolation except where required for safe provider handoff; those are primarily DEL-04-02.
- SDK message mapping except where provider errors cross into stable runtime/UI events; that is primarily DEL-04-03.
- UI API key settings behavior except for the stored-key precedence contract; that is shared with DEL-02-05.
- Redacted run logger ownership except for provider-boundary fixtures and requirements; that is shared with DEL-05-03.
- Project event-store internals beyond redacted metadata handoff, per `_CONTEXT.md`.

Sources: `_CONTEXT.md` "Deliverable Scope"; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` row `DEL-04-05`.

## Requirements

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

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Chirality runtime engine boundary | Provider integration must remain behind product-owned `AgentEnginePort` / `RuntimeEngineContract` and adapter boundaries. | `docs/CONTRACT.md` Section 1.4 |
| Chirality API key and network invariants | API keys are non-project convenience state; network is loopback plus Anthropic API path unless amended. | `docs/CONTRACT.md` Section 1.9 |
| SDK runtime configuration contract | `settingSources: []`, active-turn-only API key handoff, safe metadata recording. | `docs/SPEC.md` Section 12 |
| Attachments, API keys, and network policy | Electron safeStorage location, key logging prohibitions, renderer and Node/SDK network policy. | `docs/SPEC.md` Section 16 |
| PRD Anthropic provider policy | FR-030 through FR-035 describe key precedence, base URL, renderer network policy, provider error classes, and SDK turn boundary. | `docs/PRD.md` Section 8.5, HASH_MISMATCH warning |

## Verification

| Requirement IDs | Verification Approach | Evidence Expected |
|---|---|---|
| RQ-001, RQ-003, RQ-004, RQ-005 | Unit tests for key source resolution and SDK environment construction. | Key handoff tests prove UI key precedence, fallback to `ANTHROPIC_API_KEY`, fallback to `CHIRALITY_ANTHROPIC_API_KEY`, and `none` status with no key. |
| RQ-002, RQ-005, RQ-012, RQ-017 | Redaction tests and fixture snapshots. | No cleartext key or configured secret variant appears in logs, `HarnessEvent`, `UIEvent`, SDK error details, stderr/debug output, or tool artifacts. |
| RQ-006, RQ-007 | Base URL validation tests. | Accepted: `https://api.anthropic.com` with empty or 443 port and no credentials. Rejected: other host, scheme, credentials, non-443 port, malformed URL. |
| RQ-008, RQ-009, RQ-010 | Electron/network guard tests and SDK provider bridge tests. | Renderer non-loopback/non-Anthropic requests are canceled; provider bridge tests show Node/SDK calls do not silently broaden policy. |
| RQ-011, RQ-012 | Provider error classification tests. | Auth, rate limit, timeout, API, network, invalid base URL, and policy violation map to typed `SDK_FAILURE` details with redaction. |
| RQ-013, RQ-014, RQ-015 | Integration/conformance tests and code review. | HTTP route remains transport/lifecycle adapter; provider-specific data stays in adapter metadata; shipped SDK options use `settingSources: []`. |
| RQ-016 | Artifact existence and coverage review. | Provider wrapper, key handoff tests, base URL/network tests, and redaction fixtures exist in implementation paths selected by the owning code change. |

## Documentation

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

## Source-State Warning

`docs/PRD.md` is listed as `HASH_MISMATCH` in `_REFERENCES.md`. Requirements sourced from `docs/PRD.md` are preserved because the brief instructed this warning to be treated as source-state warning, not a blocker. Before final acceptance, the owning workflow should reverify PRD-derived FR/NFR rows against the accepted source snapshot.
