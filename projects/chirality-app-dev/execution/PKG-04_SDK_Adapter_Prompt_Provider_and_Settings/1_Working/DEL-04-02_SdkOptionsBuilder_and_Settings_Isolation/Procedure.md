# Procedure: DEL-04-02 SdkOptionsBuilder and Settings Isolation

## Purpose

Define the operational steps to produce and verify the `SdkOptionsBuilder` feature slice without exceeding the deliverable boundary. The procedure supports creation of `sdk-options-builder.ts`, settings isolation tests, and visible tool metadata.

## Prerequisites

| Prerequisite | Status | Source |
|---|---|---|
| Accepted deliverable scope for DEL-04-02 | Available in decomposition and `_CONTEXT.md` | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-02 |
| SDK probe/version decision | TBD; required before final exact SDK TypeScript option fields are frozen | `docs/PLAN.md` R0; `docs/PRD.md` KG-021, HASH_MISMATCH |
| Runtime engine contract integration point | TBD; adjacent deliverables define `AgentEnginePort`, `TurnEngine`, and conformance suite | `docs/CONTRACT.md` K-ENGINE-1; `docs/PRD.md` Section 8.12, HASH_MISMATCH |
| Persona composer output contract | TBD; DEL-04-04 owns prompt composition | `_CONTEXT.md`; `execution/_Decomposition/...` DEL-04-04 |
| Permission overlay policy inputs | TBD; PKG-06 owns full overlay and hooks, but this builder must accept policy posture | `_CONTEXT.md` ContextEnvelopeNotes; `docs/PLAN.md` R2 |
| Implementation module path | TBD; candidate R1 path is `frontend/src/lib/harness/sdk-options-builder.ts` but accepted path/export shape must follow implementation convention | `docs/PLAN.md` R1; `docs/PRD.md` Section 13.3, HASH_MISMATCH |
| Dependency edges | TBD; no declared upstream/downstream dependencies have been extracted yet | `_DEPENDENCIES.md` |

## Steps

1. Confirm source and package scope.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the DEL-04-02 decomposition row.
   - Confirm SOW coverage: SOW-016, SOW-045, SOW-047, SOW-052.
   - Record the `docs/PRD.md` `HASH_MISMATCH` warning if using PRD-backed details.

2. Define the builder input shape.
   - Include session/runtime state needed for model, tools, max turns, mode, persona, hooks, MCP servers, subagents, resume/session linkage, and settings policy.
   - Reference or import adjacent owner contracts for persona output, session linkage, hooks, MCP server descriptors, subagent descriptors, permission policy, and settings policy when those contracts exist.
   - Mark exact TypeScript API names as TBD until SDK probe/version evidence is accepted.

3. Implement deterministic fallback resolution.
   - Resolve model, tools, and max turns using `docs/SPEC.md` Section 13.1.
   - Resolve mode and persona from request/session values before runtime defaults.
   - Emit warnings for unknown option keys and ensure unknown keys do not mutate behavior.

4. Implement settings isolation posture.
   - For shipped posture, set SDK settings source behavior to `settingSources: []`.
   - Permit `['project']` only under explicit development configuration.
   - Reject invalid shipped policy inputs before option construction or omit ambient settings by construction; do not pass `user` or `local` settings sources in shipped builds.
   - Add safe visible metadata for selected settings-source posture.

5. Implement tool-surface resolution.
   - Resolve requested tools against registered SDK built-ins and registered Chirality MCP tool names.
   - Preserve deterministic ordering.
   - Return structured validation errors for unknown names before SDK request construction.
   - Include visible tool metadata that is safe for runtime display/logging.

6. Carry permission, hook, MCP, and subagent policy posture.
   - Include `disallowedTools`, permission mode, hooks, `canUseTool`, MCP server descriptors, and subagent descriptors only as supplied by governed policy inputs.
   - Do not treat `allowedTools` alone as sufficient restriction.
   - Fail closed or return TBD/integration errors for subagent descriptors until governance bridge requirements are available.

7. Include max-turn guard option.
   - Pass resolved `maxTurns` into SDK options.
   - Ensure runtime/event layers can observe terminal max-turn errors; exact event mapping is TBD in adjacent deliverables.

8. Produce safe metadata.
   - Include SDK package version where known, permission mode, visible tool list, MCP server names, settings-source posture, SDK session ID/resume mode, and transcript/store linkage where available.
   - Exclude API keys, raw secrets, hidden user settings content, and project-truth claims.

9. Add tests.
   - Add fallback-chain tests.
   - Add unknown-option warning tests that prove resolved SDK behavior is unchanged when unknown keys are present.
   - Add shipped settings isolation tests.
   - Add development-only project-setting opt-in tests.
   - Add forbidden `user` and `local` settings-source tests for shipped posture.
   - Add tool mapping, ordering, and unknown-tool tests.
   - Add one composite deterministic-order fixture covering requested tools, visible tools, MCP server IDs, allow/deny lists, permission mode, hook/callback posture, and permission policy inputs together.
   - Add `allowedTools` misconception guard test.
   - Add max-turn propagation test.
   - Add safe metadata redaction/exclusion test proving safe fields are present and API keys/secrets are absent.

10. Run validation.
    - Run targeted unit tests for `sdk-options-builder.ts` or the selected equivalent module.
    - Run typecheck after SDK version/API is pinned.
    - Run broader harness validation when the feature is wired into `TurnEngine`.
    - Record the exact test command or validation suite once the implementation path exists; until then, keep the command as TBD.
    - Record any remaining TBD fields, terminal max-turn fixture owner, or SDK-probe dependencies.

## Verification

| Check | Expected Result |
|---|---|
| Fallback determinism | Same inputs produce same resolved options, warnings, tool ordering, and metadata. |
| Unknown option handling | Unknown option keys warn and do not affect behavior. |
| Shipped settings isolation | Shipped posture produces `settingSources: []` and no `user`/`local` setting sources. |
| Development settings gate | `['project']` requires explicit development configuration. |
| Tool mapping | Registered SDK built-ins and Chirality MCP tools resolve; unknown names produce structured validation errors. |
| Composite deterministic ordering | Tools, MCP server IDs, allow/deny lists, hook/callback posture, permission mode, and policy inputs remain stable for identical inputs. |
| Permission posture | Restricted modes do not rely on `allowedTools` alone. |
| Max-turn guard | Resolved max-turn value reaches SDK options. |
| Metadata safety | Visible metadata contains only safe runtime details and no secrets. |
| Adapter boundary | SDK-specific details do not become public Chirality API or canonical event semantics except as adapter metadata. |

## Records

Expected implementation records:

- `sdk-options-builder.ts` or equivalent module selected by implementation owner.
- Exact module path/export shape record, currently TBD pending implementation convention.
- Settings isolation tests.
- Tool mapping and visible metadata tests.
- Max-turn propagation tests.
- Unknown option warning tests.
- Targeted test command or validation suite, currently TBD until implementation path exists.
- SDK probe/version evidence from DEL-04-01 before exact SDK option fields are treated as final.
- Terminal max-turn runtime/event handoff fixture owner, currently TBD and likely adjacent to DEL-04-03 or DEL-03-02 pending accepted contract.
- Any unresolved `TBD`, `ASSUMPTION`, or conflict entries carried forward for human or upstream-agent ruling.
