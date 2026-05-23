# Procedure: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

## Purpose

Define and verify the deliverable implementation for `HarnessEvent` schema and append-only JSONL runtime event storage. The procedure covers producing the event schema, writer/replay API, and tests required for accepted-turn and terminal-event durability.

## Prerequisites

- Deliverable context: `_CONTEXT.md` for DEL-05-02.
- Decomposition entry: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, DEL-05-02 row.
- Authoritative sources:
  - `docs/SPEC.md` Sections 8.2-8.4, 9, 10.1.
  - `docs/TYPES.md` Section 7.3.
  - `docs/CONTRACT.md` K-EVENT, K-CORE, K-ENGINE, K-KEY invariants.
  - `docs/DIRECTIVE.md` Section 2.3.
  - `docs/PRD.md` Sections 8.12, 9.4, FR-072-FR-076, with HASH_MISMATCH warning from `_REFERENCES.md`.
- Declared upstream dependencies: TBD - no accepted dependency edges have been extracted yet.
- Declared downstream dependencies: TBD - no accepted dependency edges have been extracted yet.
- Extracted active dependency edges are recorded in `Dependencies.csv` and summarized in `_DEPENDENCIES.md`: upstream/interface or constraint edges to DEL-05-01, DEL-03-04, DEL-05-03, DEL-05-05, DEL-03-03, and DEL-04-03, plus downstream enablement of DEL-05-04. Treat these as accepted only to the maturity and satisfaction state recorded in the dependency register.

## Steps

1. Confirm the event storage location.
   - Use `.chirality/sessions/<sessionId>/events.jsonl` under the canonical vNext session layout, unless a governed Chirality-controlled session root override applies.
   - Source: `docs/SPEC.md` Sections 8.2 and 8.4.

2. Define the `HarnessEvent` schema.
   - Include `schemaVersion: 1`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`.
   - Keep provider/SDK-specific names out of canonical fields except as adapter metadata.
   - Source: `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3; `docs/CONTRACT.md` K-CORE-1 and K-ENGINE-4.

3. Define the supported initial event categories.
   - Include the initial categories listed in SPEC/TYPES: session, accepted turn, turn started, SDK system init, model request/delta/completion, and terminal turn categories.
   - Leave later tool/hook/compaction/subagent categories representable without implementing unrelated deliverable behavior.
   - Source: `docs/SPEC.md` Sections 9.3 and 9.4; `docs/TYPES.md` Section 7.3.

4. Implement or specify the append API.
   - Append one newline-delimited JSON event per write.
   - Preserve write-sequence ordering.
   - Ensure event IDs are unique.
   - Prevent secrets from being written into payloads.
   - Store large payloads as artifacts and reference them by path.
   - Source: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1.

5. Implement or specify the replay/read API.
   - Parse valid prior JSONL records.
   - Ignore malformed trailing lines.
   - Surface diagnostics for malformed tail records.
   - Source: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5.

6. Connect accepted-turn persistence to the runtime lifecycle.
   - Persist `turn.accepted` before SDK/model execution starts.
   - Treat this as a P0 audit boundary, not a UI-only event.
   - Source: `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2.

7. Connect terminal-outcome persistence to the runtime lifecycle.
   - Persist a durable terminal event for success, failure, cancellation, or interruption after an accepted turn.
   - Source: `docs/CONTRACT.md` K-EVENT-3; decomposition SOW-015.

8. Preserve UI/runtime separation.
   - Keep browser SSE event names and compact `UIEvent` payloads separate from persisted `HarnessEvent` payloads.
   - Ensure SDK messages are mapped through an adapter rather than treated as the browser or persisted event contract.
   - Source: `docs/CONTRACT.md` K-EVENT-1; `docs/PRD.md` Section 9.4 (HASH_MISMATCH source warning).

9. Document unresolved implementation choices.
   - Mark event payload schemas by type as TBD unless already supported by source or accepted implementation, including payload-specific schemas for later tool, hook, compaction, subagent, and SDK mirror categories.
   - Mark artifact threshold values as TBD unless owned and accepted by DEL-05-05.
   - Mark redaction mechanism details as TBD unless owned and accepted by DEL-05-03.

## Verification

- Schema test confirms required fields, optional fields, `schemaVersion: 1`, and event ID uniqueness.
- Writer test confirms ordered append-only newline-delimited JSON.
- Lifecycle test confirms `turn.accepted` is persisted before SDK/model execution.
- Terminal tests confirm success, failure, cancellation, and interruption outcomes are persisted.
- Replay test confirms malformed trailing JSONL does not discard prior valid events and does surface diagnostics.
- Separation test confirms browser `UIEvent`s and persisted `HarnessEvent`s remain separate contracts.
- Secret-safety test confirms API keys and configured secrets are absent from event payload fixtures.
- Later-category fixture plan confirms tool, hook, compaction, subagent, and SDK mirror event names remain serializable/replayable while category-specific payload schemas remain TBD.
- Source-state check records that `docs/PRD.md` is HASH_MISMATCH if PRD text is used for verification expectations.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` for DEL-05-02.
- Event schema file or equivalent implementation artifact.
- JSONL writer/replay implementation artifact.
- Accepted-turn test fixture/results.
- Terminal-event test fixture/results.
- Malformed-tail replay fixture/results.
- UI/runtime separation test fixture/results.
- Dependency-edge register snapshot used for implementation handoff.
- Later-category fixture coverage plan with TBD payload-schema slots.
- DEL-05-03 redaction helper or fixture contract reference, currently TBD.
- DEL-05-05 artifact threshold source, currently TBD.
- TASK run record under `_run_records/`.
