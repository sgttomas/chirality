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
| Dependency edges | TBD; no declared upstream/downstream dependencies have been extracted yet | `_DEPENDENCIES.md` |

## Steps

1. Confirm source and package scope.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the DEL-04-02 decomposition row.
   - Confirm SOW coverage: SOW-016, SOW-045, SOW-047, SOW-052.
   - Record the `docs/PRD.md` `HASH_MISMATCH` warning if using PRD-backed details.

2. Define the builder input shape.
   - Include session/runtime state needed for model, tools, max turns, mode, persona, hooks, MCP servers, subagents, resume/session linkage, and settings policy.
   - Mark exact TypeScript API names as TBD until SDK probe/version evidence is accepted.

3. Implement deterministic fallback resolution.
   - Resolve model, tools, and max turns using `docs/SPEC.md` Section 13.1.
   - Resolve mode and persona from request/session values before runtime defaults.
   - Emit warnings for unknown option keys and ensure unknown keys do not mutate behavior.

4. Implement settings isolation posture.
   - For shipped posture, set SDK settings source behavior to `settingSources: []`.
   - Permit `['project']` only under explicit development configuration.
   - Reject or prevent `user` and `local` settings sources in shipped builds.
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
   - Add unknown-option warning tests.
   - Add shipped settings isolation tests.
   - Add development-only project-setting opt-in tests.
   - Add tool mapping, ordering, and unknown-tool tests.
   - Add `allowedTools` misconception guard test.
   - Add max-turn propagation test.
   - Add safe metadata redaction/exclusion test.

10. Run validation.
    - Run targeted unit tests for `sdk-options-builder.ts`.
    - Run typecheck after SDK version/API is pinned.
    - Run broader harness validation when the feature is wired into `TurnEngine`.
    - Record any remaining TBD fields or SDK-probe dependencies.

## Verification

| Check | Expected Result |
|---|---|
| Fallback determinism | Same inputs produce same resolved options, warnings, tool ordering, and metadata. |
| Unknown option handling | Unknown option keys warn and do not affect behavior. |
| Shipped settings isolation | Shipped posture produces `settingSources: []` and no `user`/`local` setting sources. |
| Development settings gate | `['project']` requires explicit development configuration. |
| Tool mapping | Registered SDK built-ins and Chirality MCP tools resolve; unknown names produce structured validation errors. |
| Permission posture | Restricted modes do not rely on `allowedTools` alone. |
| Max-turn guard | Resolved max-turn value reaches SDK options. |
| Metadata safety | Visible metadata contains only safe runtime details and no secrets. |
| Adapter boundary | SDK-specific details do not become public Chirality API or canonical event semantics except as adapter metadata. |

## Records

Expected implementation records:

- `sdk-options-builder.ts` or equivalent module selected by implementation owner.
- Settings isolation tests.
- Tool mapping and visible metadata tests.
- Max-turn propagation tests.
- Unknown option warning tests.
- SDK probe/version evidence from DEL-04-01 before exact SDK option fields are treated as final.
- Any unresolved `TBD`, `ASSUMPTION`, or conflict entries carried forward for human or upstream-agent ruling.
