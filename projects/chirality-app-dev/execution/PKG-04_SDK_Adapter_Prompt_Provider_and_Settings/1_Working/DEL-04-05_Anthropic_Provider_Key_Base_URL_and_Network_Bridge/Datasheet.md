# Datasheet: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

## Identification

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

## Attributes

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

## Conditions

| Condition | Value | Source |
|---|---|---|
| Shipped SDK settings isolation | Shipped builds use `settingSources: []`. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| SDK adapter promotion gate | SDK-backed adapter must pass engine conformance tests before becoming the default production path. | `docs/CONTRACT.md` K-ENGINE-2; `docs/SPEC.md` Section 12.1 |
| Product boundary | Public APIs, UI events, harness events, session storage, permission decisions, and governance records remain Chirality-owned, not SDK-shaped. | `docs/CONTRACT.md` K-ENGINE-4 |
| Broader network tools | Remote MCP, plugins, and non-Anthropic network tools require governed future scope. | `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1 |
| Packaging condition | Packaged app must prove SDK execution and API key handoff without leaking secrets. | `docs/PLAN.md` Section 6.4 |
| Source-state warning | `docs/PRD.md` is locally accessible but has `HASH_MISMATCH` in `_REFERENCES.md`; claims from it are used as scoped source guidance and should be reverified before final acceptance. | `_REFERENCES.md` REF-006 |

## Construction

| Construct | Expected Content |
|---|---|
| Provider wrapper | A provider boundary that resolves API key source, validates Anthropic base URL, supplies SDK environment only for the active turn, normalizes provider/SDK failures, and emits redacted details. Exact module name: TBD. |
| Key handoff tests | Tests proving UI key precedence, environment fallback order, absence of working-root writes, and redacted SDK environment/log/event handoff. Exact test paths: TBD. |
| Base URL/network tests | Tests proving only `https://api.anthropic.com` with no credentials and empty/443 port is accepted, renderer outbound requests are loopback or current shipped Anthropic path only, and Node/SDK calls do not broaden policy. Exact test paths: TBD. |
| Redaction fixtures | Fixtures covering key material, provider error messages, SDK stderr/debug output, and policy-denial metadata. Exact fixture shape: TBD. |
| Status metadata | Safe status source values are `ui`, `env`, or `none`; no key value is recorded. |

ASSUMPTION: "Provider wrapper" may be implemented as an SDK adapter helper, a `TurnEngine` collaborator, or a dedicated provider module. The decomposition names the artifact but the source corpus does not prescribe the exact file path.

## References

| RefID | Source | SectionRef | Status |
|---|---|---|---|
| REF-002 | `docs/CONTRACT.md` | Sections 1.4, 1.9; K-ENGINE-2, K-ENGINE-4, K-EVENT-6, K-NET-1, K-KEY-1 | MATCH |
| REF-003 | `docs/SPEC.md` | Sections 12.1-12.4, 16.2-16.3 | MATCH |
| REF-005 | `docs/PLAN.md` | Sections 6.3-6.4; R1 implementation targets | MATCH |
| REF-006 | `docs/PRD.md` | Section 8.5 FR-030 through FR-035; FR-075; NFR-002 through NFR-003; NFR-028 through NFR-030 | HASH_MISMATCH warning |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOW-019 through SOW-021; OBJ-004, OBJ-008; row `DEL-04-05` | accepted decomposition reference |
