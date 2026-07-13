# Procedure: DEL-05-04 Runtime Replay and Transcript View

## Purpose

Define an operational path for producing and verifying the Runtime Replay and Transcript View deliverable. ADQ-09 assigned the implementation ownership paths for the replay parser, transcript model, replay API, sidebar component, and focused fixtures.

## Prerequisites

| Prerequisite | Status / note | Source |
|---|---|---|
| Canonical session folder layout is available through the D-APP-41/ADQ-08 eager conversion path. | Satisfied for replay discovery. | `docs/SPEC.md` Section 8.2; `D-APP-41`; ADQ-08 evidence |
| Legacy session records remain readable through conversion. | Satisfied: flat records convert to canonical folders on read/list/resume/save. | `docs/SPEC.md` Section 8.1; `D-APP-41`; ADQ-08 evidence |
| `HarnessEvent` schema and event writer behavior are available. | Satisfied for ADQ-09 replay and transcript projection. | `docs/SPEC.md` Section 9; `frontend/src/lib/harness/event-schema.ts`; `frontend/src/lib/harness/session-events.ts` |
| SDK session linkage metadata is available in session metadata or fixtures. | Satisfied by `SessionRecord` linkage fields and transcript projection fixtures. | `docs/SPEC.md` Section 8.3; `frontend/src/lib/harness/transcript-replay.ts`; `frontend/src/__tests__/lib/transcript-replay.test.ts` |
| Declared dependency edges are accepted for ADQ-09 replay closure. | Satisfied for DEL-05-04 ADQ-09 scope; ADQ-10 remains for DEL-05-05 checksum/retention policy outside this transcript slice. | `_DEPENDENCIES.md`; `D-APP-42` |
| Redaction helper or policy is available. | Satisfied: replay applies read-time redaction to imported/manual logs as well as append-time redaction. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6; `frontend/src/lib/harness/session-events.ts` |

Dependency closure disposition: F-001 is resolved for the ADQ-09 transcript/replay scope. DEL-05-01 is satisfied by ADQ-08/D-APP-41, DEL-05-02 replay-facing schema/writer behavior is available, SDK linkage is fixture-covered, read-time redaction is implemented, and DEL-05-05 artifact-link projection is covered without claiming ADQ-10 checksum/retention closure. Source reread: `_DEPENDENCIES.md` extracted dependency register; decomposition rows for DEL-05-01, DEL-05-02, DEL-05-04, and DEL-05-05; `docs/CONTRACT.md` K-EVENT-6 and K-EVENT-7.

## Steps

1. **Confirm source contracts.**
   - Re-read the accepted session layout, event schema, replay rules, SDK linkage fields, and browser/runtime contract separation.
   - Use D-APP-38 authority corpus v2 as the current source-state check.

2. **Define replay input handling.**
   - Read `.chirality/sessions/<sessionId>/session.json` and `.chirality/sessions/<sessionId>/events.jsonl` for canonical vNext sessions.
   - Preserve compatibility for legacy `{sessionRoot}/{sessionId}.json` records through D-APP-41 eager conversion to canonical folders.
   - Keep exact path override behavior for `CHIRALITY_SESSION_ROOT` aligned with the session store contract.

3. **Parse `events.jsonl`.**
   - Process newline-delimited `HarnessEvent` records in write sequence.
   - Validate the required event fields defined by the type target.
   - Ignore a malformed trailing line while retaining prior valid events.
   - Return or record a diagnostic for malformed-tail replay.

4. **Build the transcript projection.**
   - Group events by `turnId` where available.
   - Project accepted user input, assistant deltas/completions, tool summaries, terminal outcomes, and artifact references.
   - Treat missing optional event categories as absent data, not parser failure, unless a required accepted-turn/terminal invariant is violated.
   - ASSUMPTION: expose compact tool summaries and artifact links rather than raw large payloads.

5. **Attach SDK transcript linkage.**
   - Read `engineSessionId`, `claudeSessionId`, `sdkSessionId`, `sdkTranscriptPath`, `sdkSessionStoreKey`, `sdkConfigDir`, SDK setting sources, SDK package versions, and model metadata when present in `session.json`.
   - Mark SDK transcript/store linkage as adapter metadata and secondary runtime state.
   - Do not let SDK message names, transcript paths, or session IDs become canonical Chirality identifiers.

6. **Apply redaction and safety filtering.**
   - Ensure replay output and diagnostics do not expose API keys or configured secret variants.
   - For large or sensitive tool result data, show summary and artifact reference only.
   - Surface redaction limitations as diagnostics rather than silently leaking raw content.

7. **Create verification fixtures.**
   - Valid transcript reconstruction fixture.
   - Malformed-tail JSONL fixture.
   - Terminal outcome fixture for success, failure, cancellation, or interruption where source events exist.
   - SDK linkage fixture confirming `events.jsonl` remains canonical.
   - Legacy session fixture.
   - Redaction fixture for secret-like event, tool, provider, or SDK metadata.
   - Tool-result artifact-link fixture for compact summaries and stored payload references.
   - Record exact fixture filenames in the evidence file.

8. **Run verification.**
   - Execute unit tests and Section 9 validation coverage for `section9.session_event_replay` and `section9.sdk_session_link_resume`.

9. **Record accepted implementation locations.**
   - Record the replay parser module path, transcript view model/interface name, route or component placement, transcript reconstruction fixture path, malformed-tail fixture path, SDK-linkage fixture path, redaction fixture path, and tool-result artifact fixture path.
   - Source reread: `docs/SPEC.md` Sections 8.2, 8.4, 9.2, and 19.3; decomposition DEL-05-04 row. Disposition: D-001 incorporated and filled by ADQ-09 code discovery/implementation.

## Verification

| Check | Expected result |
|---|---|
| Canonical replay | Valid events reconstruct accepted turns, assistant output, tool summaries, terminal outcomes, and artifact links where present. |
| Malformed tail | Invalid final JSONL line is ignored; valid prior events survive; diagnostic is visible. |
| SDK linkage | SDK session/transcript/store metadata appears as secondary adapter metadata only. |
| Legacy read | Legacy flat session record remains readable through D-APP-41 eager conversion and then replay uses canonical folder state. |
| Redaction | Secret-like values do not appear in replay output, diagnostics, or summaries. |
| Contract separation | Browser `UIEvent` and persisted `HarnessEvent` concepts remain distinct in naming and tests. |
| Closure slots | Parser API, transcript model, route/component placement, fixture paths, dependency edges, and redaction/tool-result artifact coverage are recorded in ADQ-09 evidence. |

## Records

Expected records for closure:

- Replay parser implementation path: `frontend/src/lib/harness/session-events.ts`.
- Transcript reconstruction model path: `frontend/packages/harness-contract/src/transcript-replay.ts`.
- Replay API path: `frontend/src/app/api/harness/session/[id]/events/route.ts`.
- Transcript UI path: `frontend/src/components/shell/transcript-stream-view.tsx`.
- Transcript reconstruction, malformed-tail, SDK transcript linkage, redaction, API replay, and sidebar render test results.
- Source-state note for D-APP-38 authority corpus v2 `MATCH`.
- Dependency register update for the ADQ-09 replay/transcript scope.
