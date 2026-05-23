# Procedure: DEL-05-04 Runtime Replay and Transcript View

## Purpose

Define an operational path for producing and verifying the Runtime Replay and Transcript View deliverable. The procedure is written for implementation and validation planning; exact code paths remain `TBD` until implementation ownership is assigned.

## Prerequisites

| Prerequisite | Status / note | Source |
|---|---|---|
| Canonical session folder layout is available or represented by fixtures. | Required for vNext replay. | `docs/SPEC.md` Section 8.2 |
| Legacy session records remain readable. | Required during migration. | `docs/SPEC.md` Section 8.1 |
| `HarnessEvent` schema and event writer behavior are available or represented by fixtures. | Upstream implementation likely belongs to DEL-05-02; accepted dependency edge is TBD. | `docs/SPEC.md` Section 9 |
| SDK session linkage metadata is available in session metadata or fixtures. | Needed for SOW-046 coverage. | `docs/SPEC.md` Section 8.3 |
| Declared dependency edges are accepted. | TBD - no accepted upstream/downstream edges have been extracted yet. | `_DEPENDENCIES.md` |
| Redaction helper or policy is available. | Exact dependency is TBD; replay must not expose secrets. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6 |

## Steps

1. **Confirm source contracts.**
   - Re-read the accepted session layout, event schema, replay rules, SDK linkage fields, and browser/runtime contract separation.
   - Preserve `docs/PRD.md` as a warned source if its hash remains mismatched.

2. **Define replay input handling.**
   - Read `.chirality/sessions/<sessionId>/session.json` and `.chirality/sessions/<sessionId>/events.jsonl` for canonical vNext sessions.
   - Preserve compatibility for legacy `{sessionRoot}/{sessionId}.json` records until migration closure is accepted.
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
   - Read `sdkSessionId`, `sdkProjectKey`, `sdkTranscriptPath` or `sdkSessionStoreKey`, `sdkConfigDir`, and `sdkResumeMode` when present in `session.json`.
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

8. **Run verification.**
   - Execute unit tests and any Section 9 validation coverage that exists for `section9.session_event_replay` and `section9.sdk_session_link_resume`.
   - If the validation IDs are not implemented yet, record `TBD` rather than marking them passed.

## Verification

| Check | Expected result |
|---|---|
| Canonical replay | Valid events reconstruct accepted turns, assistant output, tool summaries, terminal outcomes, and artifact links where present. |
| Malformed tail | Invalid final JSONL line is ignored; valid prior events survive; diagnostic is visible. |
| SDK linkage | SDK session/transcript/store metadata appears as secondary adapter metadata only. |
| Legacy read | Legacy flat session record remains readable until migration completion is accepted. |
| Redaction | Secret-like values do not appear in replay output, diagnostics, or summaries. |
| Contract separation | Browser `UIEvent` and persisted `HarnessEvent` concepts remain distinct in naming and tests. |

## Records

Expected records for closure:

- Replay parser implementation or design record: TBD exact path.
- Transcript reconstruction test results.
- Malformed-tail fixture and test result.
- SDK transcript linkage fixture and test result.
- Source-state note for `docs/PRD.md` HASH_MISMATCH if still present.
- Dependency extraction output after `Dependencies.csv` exists and the FULL_GRAPH register is checked.
