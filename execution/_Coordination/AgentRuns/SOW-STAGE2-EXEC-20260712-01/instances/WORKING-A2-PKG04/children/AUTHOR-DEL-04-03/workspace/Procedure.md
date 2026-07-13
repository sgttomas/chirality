# Procedure: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

## Purpose

Define the working procedure to implement and verify the `SdkMessageMapper` deliverable so SDK stream messages are translated into stable browser `UIEvent`s and provider-neutral `HarnessEvent`s without leaking SDK shape into Chirality core contracts.

## Prerequisites

| Prerequisite | Status / Notes |
|---|---|
| Deliverable context | Available in `_CONTEXT.md`. |
| Authoritative references | Available in `_REFERENCES.md`; REF-006 `docs/PRD.md` has HASH_MISMATCH and is used as a warning-qualified source per task brief. |
| Accepted dependency register | `Dependencies.csv` exists with ACTIVE extracted edges, but all satisfaction statuses remain `TBD`; implementation closure should verify upstream satisfaction before closing this deliverable. |
| Declared upstream dependencies | Extracted ACTIVE upstream execution dependencies include DEL-04-01, DEL-03-01, DEL-03-03, and DEL-04-02. Their satisfaction remains `TBD` in `_DEPENDENCIES.md` / `Dependencies.csv`. |
| first-adapter probe results | TBD / pending DEL-04-01 and OI-001 for exact SDK message categories and payload fields. |
| Engine contract target | Product-owned `AgentEnginePort` / `RuntimeEngineContract` is defined by PKG-03 / DEL-03-01, not by this deliverable. |
| Runtime event schema target | `HarnessEvent` target type is available in REF-004 and REF-003. |
| Browser event target | Stable browser SSE event names are available in REF-003 and REF-004. |
| Implementation path discovery | Concrete mapper module path, UI/HarnessEvent type import paths, and mapper test locations are `TBD` until code discovery confirms the accepted backend/runtime layout. |

## Steps

1. Confirm mapping boundaries.
   - Read the accepted `AgentEnginePort` / `RuntimeEngineContract` once available.
   - Confirm the mapper is an adapter component and not the owner of route policy, event persistence, SDK option construction, or permission enforcement.
   - Before implementation closure, confirm `Dependencies.csv` has no unsatisfied blocker for the upstream runtime contract, SSE compatibility adapter, SDK options/settings isolation, or first-adapter probe evidence.

2. Create the mapper module.
   - Add `sdk-message-mapper.ts` or equivalent in the accepted backend runtime location.
   - Record the accepted mapper path, UI event type import path, `HarnessEvent` type import path, mapper unit-test path, and provider-neutral leakage-test path in implementation notes or fixture documentation once code discovery is complete.
   - Define input types for SDK-side messages using probe-backed fixtures where available.
   - Define output types for browser `UIEvent` and `HarnessEvent` results using Chirality-owned types.

3. Implement browser event mapping.
   - Map assistant deltas, completions, session initialization, tool result summaries, terminal errors, and process completion into the stable SSE event names.
   - Do not emit SDK message names as browser event names.
   - Mark any unconfirmed SDK input shape as `TBD` until DEL-04-01 provides probe evidence.

4. Implement runtime event mapping.
   - Emit versioned `HarnessEvent` records for accepted categories such as `sdk.system.init`, `model.request.started`, `model.delta`, `model.completed`, `turn.completed`, `turn.failed`, and `turn.cancelled` where inputs support them.
   - Prepare explicit cases or fixture placeholders for later categories such as tool, permission, hook, compaction, subagent, and SDK mirror error events.
   - Keep SDK-specific fields under explicit adapter metadata, not top-level canonical fields unless the schema accepts them.

5. Handle unknown and probe-dependent SDK inputs.
   - For unknown categories, return a structured mapper error or safe diagnostic output according to the runtime contract.
   - Do not pass raw SDK messages through to browser events or canonical runtime events.
   - Record unconfirmed categories in a `TBD` fixture list tied to DEL-04-01 / OI-001.

6. Apply redaction-compatible handling.
   - Avoid copying API keys, configured secret variants, provider error bodies, or raw tool output blobs into mapped events.
   - Preserve enough non-secret metadata for diagnosis, replay, and terminal outcome handling.

7. Write mapper tests.
   - Cover each stable browser event name expected from supported SDK input fixtures.
   - Cover each supported `HarnessEvent` category and required schema field.
   - Cover deterministic ordering for repeated runs over the same input sequence.
   - Cover mapper-owned terminal success, failure, interruption, and cancellation translation cases.
   - Leave accepted-turn persistence, client-disconnect cleanup, cancellation-source classification, lock cleanup, and terminal durability to `TurnEngine` / engine conformance tests; reference those results rather than duplicating ownership in the mapper.

8. Write provider-neutral leakage tests.
   - Assert public event names are Chirality event names, not SDK message names.
   - Assert canonical event types are Chirality categories, not SDK raw categories.
   - Assert SDK session IDs, transcript paths, SDK tool names, and provider names appear only in approved adapter metadata locations.

9. Integrate with validation.
   - Use `section9.adapter_message_mapper` as the active Section 9 runtime validation ID for mapper coverage.
   - Ensure mapper tests are part of local premerge validation once the runtime validation suite lands.

10. Reconcile with first-adapter probe updates.
   - When DEL-04-01 provides observed SDK message fixtures, replace `TBD` cases with probe-backed tests.
   - If SDK behavior cannot support required product-owned mapping semantics, surface the issue through the reliance-boundary/fallback process rather than weakening provider neutrality.

## Verification

| Check | Expected Result |
|---|---|
| Four output categories | Mapper produces browser UI events, canonical runtime events, structured mapper errors, or explicit `TBD` probe cases; it does not raw-pass SDK messages. |
| UI compatibility | Stable SSE event names remain unchanged. |
| Runtime schema | `HarnessEvent` records validate against the target type. |
| Provider-neutral leakage | No unapproved SDK-shaped top-level fields or event names appear in public/canonical outputs. |
| Determinism | Identical SDK input fixtures produce identical ordered mapping outputs. |
| Redaction | Secret-like values do not appear in mapper outputs. |
| Probe completeness | All SDK categories named by the accepted probe have a mapping, structured rejection, or documented `TBD` requiring human/architecture action. |

## Records

Expected records and evidence from implementation:

- `sdk-message-mapper.ts` or equivalent implementation.
- Mapper unit tests.
- Provider-neutral leakage tests.
- Fixture files or inline fixtures derived from DEL-04-01 first-adapter probe outputs.
- `TBD` list for SDK message categories or payload fields not yet confirmed.
- Section 9 validation entry or follow-up for `section9.adapter_message_mapper`.
- Notes on any fallback or reliance-boundary concerns if SDK behavior cannot be mapped without weakening Chirality-owned contracts.
- Implementation path record naming the accepted mapper module, UI/HarnessEvent type import paths, mapper unit-test path, and provider-neutral leakage-test path.
- Dependency closure note confirming whether ACTIVE upstream dependencies remain `TBD`, blocked, or satisfied at implementation closeout.
