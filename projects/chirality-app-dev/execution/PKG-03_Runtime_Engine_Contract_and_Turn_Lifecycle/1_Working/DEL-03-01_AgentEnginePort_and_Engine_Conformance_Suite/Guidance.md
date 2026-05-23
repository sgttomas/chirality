# Guidance: DEL-03-01 AgentEnginePort and Engine Conformance Suite

## Purpose

DEL-03-01 exists to make the runtime engine replaceable by construction while allowing the Claude Agent SDK to serve as the preferred implementation substrate when it satisfies Chirality-owned governance, audit, permission, session, and route-compatibility requirements.

The decomposition assigns this deliverable to SOW-037 and OBJ-002: define the product-owned `AgentEnginePort` / `RuntimeEngineContract` and conformance tests before SDK behavior becomes production default.

Sources: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-03-01; `docs/DIRECTIVE.md` sections 2.8-2.10; `docs/PLAN.md` sections 2-4.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Chirality terms at the core | Contract names, public APIs, browser events, persisted events, permission decisions, and session records should use Chirality vocabulary. SDK details belong behind `EngineAdapter`. | `docs/CONTRACT.md` K-CORE-1 and K-ENGINE-4; `docs/TYPES.md` section 7 |
| Conformance before default | Treat SDK adoption as conditional. The SDK-backed adapter is not default until it passes conformance tests. | `docs/CONTRACT.md` K-ENGINE-2; `docs/SPEC.md` section 10.3 |
| Route stability | Keep `/api/harness/turn` as transport and compatibility surface. Runtime policy should be owned by `TurnEngine` and the engine boundary. | `docs/SPEC.md` section 10.4; `docs/PRD.md` section 9.1 |
| Event separation | Keep compact browser `UIEvent`s distinct from richer persisted `HarnessEvent`s. | `docs/CONTRACT.md` K-EVENT-1; `docs/SPEC.md` sections 9 and 11 |
| Adapter metadata quarantine | SDK session IDs, transcript paths, tool names, permission modes, message categories, and hook names may be retained only as explicit adapter metadata. | `docs/DIRECTIVE.md` section 2.10; `docs/SPEC.md` section 10.3 |
| Reliance boundaries are test subjects | Product-critical boundaries must be testable in Chirality terms, not only described in prompts or assumed from SDK defaults. | `docs/DIRECTIVE.md` section 2.9; `docs/CONTRACT.md` K-RELIANCE-2 |

## Considerations

- Keep the initial `AgentEnginePort` narrow. A small boundary makes stub and SDK-backed adapters easier to compare and keeps SDK-specific behavior from leaking into the product contract.
- Make the conformance suite adapter-agnostic. Tests should assert Chirality outcomes: accepted-turn persistence, stable UI events, canonical event records, terminal outcomes, permission denial, redaction, and absence of SDK-shaped leakage.
- Expect some tests to be staged. SDK message categories, resume behavior, `SessionStore`, `CLAUDE_CONFIG_DIR`, and interrupt behavior depend on DEL-04-01 probe findings, so mark unsupported cases as `TBD` rather than hard-coding assumptions.
- Preserve the stub adapter. It is the deterministic baseline for contract tests and fallback analysis.
- Keep PRD-derived details visible but caveated. `_REFERENCES.md` reports a HASH_MISMATCH for `docs/PRD.md`; human acceptance should confirm that the accessible PRD state is the intended one.

## Trade-offs

| Trade-off | Preferred Direction | Rationale |
|---|---|---|
| Thin contract vs broad SDK wrapper | Prefer thin product-owned contract. | Reduces SDK lock-in and supports provider-neutral conformance. |
| Full SDK parity vs governed subset | Prefer governed subset. | PLAN states Chirality does not chase Claude Code feature parity; it adopts SDK mechanics where they accelerate the product-owned contract. |
| Unit-only tests vs mixed conformance | Use both type/unit tests and route/SSE compatibility checks. | Contract correctness must cover adapter behavior and user-visible stream compatibility. |
| Early implementation specificity vs `TBD` | Use `TBD` until SDK probe results exist. | Prevents inaccessible or unstable SDK behavior from becoming accepted project truth. |

## Examples

Illustrative interface shape from `docs/SPEC.md` section 10.2:

```ts
interface AgentEnginePort {
  runTurn(input: TurnInput): AsyncIterable<UIEvent>;
  interrupt?(sessionId: string): Promise<void>;
}
```

Example conformance assertions:

- A stub adapter yields only stable browser `UIEvent` names and does not expose provider-specific fields in public stream payloads.
- An SDK-backed adapter persists `turn.accepted` before invoking SDK/model execution.
- An SDK-backed adapter maps SDK result/failure/interruption outcomes into product-owned terminal `HarnessEvent` records.
- A leakage test fails if public APIs or canonical `HarnessEvent` fields expose SDK message names, permission modes, transcript paths, tool names, or session IDs outside explicit adapter metadata.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | `docs/PRD.md` is accessible and used, but `_REFERENCES.md` reports REF-006 HASH_MISMATCH. | `_REFERENCES.md` REF-006 | `docs/PRD.md` sections 8.16, 9, 12, 13 | Datasheet Conditions/References; Specification Requirements/Verification; Procedure Prerequisites | Treat as a source-state warning, not a semantic conflict; require human confirmation before acceptance closure. | TBD |
