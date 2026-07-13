# Guidance: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

This deliverable keeps Anthropic provider access inside Chirality-owned runtime governance while adopting the Claude Agent SDK as the preferred engine substrate. It protects API keys, constrains network access, keeps provider/SDK details behind adapter boundaries, and gives downstream validation clear evidence for key precedence, base URL policy, network policy, and redacted failure handling.

Sources: `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` Sections 1.4 and 1.9; `docs/SPEC.md` Sections 12 and 16; decomposition row `DEL-04-05`.

## Principles

### Preserve Chirality Ownership

The SDK may host generic runtime mechanics, but Chirality owns the product contract. Provider key handling, network policy, event semantics, redaction, and public APIs must remain Chirality-defined rather than SDK-shaped.

Sources: `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-5.

### Treat Keys as Convenience State, Not Project Truth

API keys are runtime convenience state. They must not be written into the working root, document kit, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. Tests should prove both positive behavior, such as correct source precedence, and negative behavior, such as absence from project files and emitted records.

Sources: `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` Sections 12.3 and 16.2.

### Fail Closed on Provider Boundary Violations

Invalid base URLs, non-allowlisted renderer requests, policy violations, and provider failures should become typed failures that preserve retry/debug context without exposing secrets. Invalid base URL and policy-violation cases should stop execution before provider calls proceed.

Sources: `docs/PRD.md` Section 8.5 FR-032 through FR-034; `docs/CONTRACT.md` K-NET-1.

### Keep Network Scope Narrow

Current shipped network scope is loopback plus the Anthropic API path. Remote MCP, plugins, and non-Anthropic network tools are future-governed scope and should not be introduced as part of this deliverable.

Sources: `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1.

### Redact at Every Boundary

Redaction should apply before details cross from provider/SDK internals into `HarnessEvent`, `UIEvent`, run logs, fixtures, or diagnostics. A provider wrapper should be suspicious of SDK errors and stderr/debug text because upstream message shapes can drift.

Sources: `docs/CONTRACT.md` K-EVENT-6; `docs/PLAN.md` Section 6.3; `docs/PRD.md` FR-075 and KG-021.

## Considerations

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

## Trade-offs

| Choice | Benefit | Cost / Risk | Recommended Posture |
|---|---|---|---|
| Single provider wrapper | Centralizes redaction, key handoff, base URL validation, and provider error mapping. | May become too broad if it absorbs turn lifecycle or Provider/SDK message mapping. | Keep wrapper provider-boundary focused and delegate turn lifecycle to `TurnEngine`. |
| Separate helpers for key, URL, network, and error classification | Easier unit testing and clearer ownership. | Requires careful integration tests to prove boundary behavior as a whole. | Prefer small helpers plus provider-boundary integration tests. |
| Rely on SDK defaults for network/key behavior | Lower initial code volume. | Violates product-owned governance and may be opaque or version-sensitive. | Do not rely on opaque SDK defaults for product-critical behavior. |
| Allow configurable base URL | Useful for mocks and future providers. | Current product requirement accepts only Anthropic production API for shipped policy. | Keep shipped validation strict; test or dev-only escape hatches require explicit governance if introduced. |
| Log rich provider errors | Improves diagnosis. | High secret-leak risk and SDK-shape leakage. | Log typed/redacted metadata and keep raw provider payloads out of durable records unless redaction is proven. |

## Examples

Supported examples from available sources:

- Key precedence example: if a UI safeStorage key exists, it is used before `ANTHROPIC_API_KEY`; if no UI key exists, `ANTHROPIC_API_KEY` is used before `CHIRALITY_ANTHROPIC_API_KEY`. Source: `docs/SPEC.md` Section 12.3.
- Safe status example: API key status may report `ui`, `env`, or `none`; it must not report the key. Source: `docs/SPEC.md` Section 16.2.
- Base URL example: `https://api.anthropic.com` with empty or 443 port and no credentials is accepted; non-Anthropic hosts, embedded credentials, or non-443 ports are rejected. Source: `docs/PRD.md` Section 8.5 FR-032.
- Network example: renderer outbound requests are restricted to loopback and Anthropic API path; broader remote MCP/plugin/network access is future scope. Source: `docs/SPEC.md` Section 16.3.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No source conflict identified during P1/P2 drafting. | TBD | TBD | TBD | TBD | TBD |

## Open Items

| ID | Item | Reason |
|---|---|---|
| OI-DEL-04-05-001 | Exact provider wrapper module path is TBD. | Decomposition names the artifact, but source corpus does not prescribe file layout. |
| OI-DEL-04-05-002 | Exact Node/SDK network enforcement mechanism is TBD. | `docs/SPEC.md` requires Node/SDK calls not to broaden policy, but implementation mechanism is not fixed in the accessible sources. |
| OI-DEL-04-05-003 | Exact SDK error object taxonomy is TBD. | SDK version/probe results belong to adjacent R0/R1 work and may affect classifier details. |
| OI-DEL-04-05-004 | PRD-derived claims require revalidation before final acceptance. | `_REFERENCES.md` reports `docs/PRD.md` `MATCH`. — reconciled under D-APP-38 |
