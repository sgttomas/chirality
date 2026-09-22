### CLM-005 — Construction

> ##### Construction
>
> | Construct | Target / Shape | Source / Status |
> |---|---|---|
> | Runtime contract module | `agent-engine-port.ts` or equivalent product-owned runtime contract. | `execution/_Decomposition/...v3_2.md` DEL-03-01; `docs/PLAN.md` R1; `docs/PRD.md` R1 |
> | TypeScript interface | `AgentEnginePort` with `startTurn(input: AgentEngineRunInput)` and optional `interrupt`. | `docs/SPEC.md` section 10.2; D-APP-40 |
> | Turn input type | Must include active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable. | `docs/SPEC.md` section 10.2 |
> | Conformance suite | `engine-conformance.ts` or equivalent tests for stub and SDK-backed adapters. | `docs/PLAN.md` R1; `docs/PRD.md` section 12.5 |
> | Stub adapter | Deterministic adapter retained for tests. | `docs/SPEC.md` section 10.3 |
> | SDK-backed adapter | Provider implementation behind the product-owned contract. | `docs/SPEC.md` section 10.3 |
> | Exact final source path | ACCEPTED PLACEMENT (2026-07-03): D-APP-46 extraction accepted `frontend/packages/harness-contract/src/agent-engine-port.ts` as the package-owned source. The original app-dev path `frontend/src/lib/harness/agent-engine-port.ts` remains as a back-compat shim that re-exports `@chirality/harness-contract/agent-engine-port`. | D-APP-46 ruling; `frontend/packages/harness-contract/src/agent-engine-port.ts`; `frontend/src/lib/harness/agent-engine-port.ts` |
>

