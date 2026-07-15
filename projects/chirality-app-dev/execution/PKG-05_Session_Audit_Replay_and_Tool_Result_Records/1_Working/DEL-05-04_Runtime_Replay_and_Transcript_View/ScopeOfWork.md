---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-04
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-042, SOW-046]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-04

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-04` in service of project scope [SOW-042, SOW-046] and package objectives [OBJ-003].

- **OUT-001** — A runtime replay and transcript-view contract that reconstructs accepted turns, assistant output, tool summaries, terminal outcomes, diagnostics, artifact links, and secondary SDK transcript linkage from Chirality-owned HarnessEvent records.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-05-04 Runtime Replay and Transcript View

> #### Datasheet: DEL-05-04 Runtime Replay and Transcript View
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-05-04 |
> | Deliverable name | Runtime Replay and Transcript View |
> | Package | PKG-05 Session Audit, Replay, and Tool Result Records |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | Responsible party | TBD |
> | Context envelope | M |
> | Scope items | SOW-042, SOW-046 |
> | Objective | OBJ-003 |
> | Anticipated artifacts | Replay parser; transcript model; transcript sidebar view; transcript reconstruction tests; malformed-tail tests |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary store | `.chirality/sessions/<sessionId>/events.jsonl` as the product-owned Chirality audit mirror. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4; `docs/TYPES.md` Section 1.8 |
> | Session metadata input | `.chirality/sessions/<sessionId>/session.json` with session identity, project root, persona, mode, model, SDK linkage, transcript/store linkage, and resume metadata where available. | `docs/SPEC.md` Sections 8.2-8.4 |
> | Legacy metadata input | Existing `{sessionRoot}/{sessionId}.json` records remain readable through D-APP-41 eager conversion, then canonical folder records are used. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` Section 8.12 and session storage notes; `D-APP-41` |
> | Event record shape | `HarnessEvent` includes `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, timestamp, type, and data payload. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | Replay tolerance | Replay must ignore malformed trailing JSONL lines while preserving valid prior events and surfacing diagnostics. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5; `docs/PRD.md` FR-073 and NFR-013 |
> | Transcript content target | Accepted user turns, assistant output, tool summaries, terminal outcomes, artifact links, and SDK transcript links. | `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` FR-076 |
> | SDK transcript status | SDK transcript paths/store keys are secondary adapter metadata unless explicitly imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3; `docs/DIRECTIVE.md` Sections 2.3 and 2.10 |
> | UI/runtime contract separation | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts; replay must not make public UI/API contracts SDK-shaped. | `docs/SPEC.md` Sections 10.3 and 11; `docs/CONTRACT.md` K-EVENT-1 and K-ENGINE-4 |
> | Secret handling | Secrets must not be stored in events; runtime logs, tool artifacts, and provider errors require redaction. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Upstream dependencies | ADQ-09 replay scope depends on DEL-05-01, DEL-05-02, DEL-04-01 SDK linkage metadata, redaction policy/helper, and DEL-05-05 artifact-link metadata; all are satisfied for transcript/replay projection. | `_DEPENDENCIES.md`; `Dependencies.csv`; ADQ-09 evidence |
> | Downstream dependencies | ADQ-10 remains responsible for DEL-05-05 checksum/retention residuals; ADQ-09 consumes artifact-link metadata but does not close checksum policy. | `_DEPENDENCIES.md`; `D-APP-42` |
> | Canonicality constraint | `events.jsonl` remains canonical for runtime replay; SDK transcripts assist resume/debugging but do not displace Chirality events. | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3 |
> | Migration constraint | Replay must account for legacy flat sessions through D-APP-41 eager conversion, then operate on canonical folder records. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` session storage notes; `D-APP-41` |
> | Exact parser API | `replayHarnessEvents(sessionId)` in `frontend/src/lib/harness/session-events.ts`; transcript projection via `deriveTranscriptView(events, session?)` in `frontend/packages/harness-contract/src/transcript-replay.ts`. | ADQ-09 implementation; D-APP-48 relocation |
> | Exact transcript view route/UI placement | Replay route: `frontend/src/app/api/harness/session/[id]/events/route.ts`; sidebar UI: `frontend/src/components/shell/transcript-stream-view.tsx`. | ADQ-09 implementation |
> | Tool summary detail level | ASSUMPTION: replay should expose compact summaries and artifact links rather than raw large payloads, because large payloads are stored as artifacts and referenced by path. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-7 |
>

### CLM-005 — Pass 3 Semantic Lensing Notes

> ##### Pass 3 Semantic Lensing Notes
>
> | Item ID | Datasheet disposition | Source reread |
> |---|---|---|
> | B-001 | Retired: D-APP-38 authority corpus v2 reports REF-006 and all other DEL-05-04 references as `MATCH`. | `_REFERENCES.md` authoritative source corpus; `Guidance.md` Source-State Notes |
> | C-001 | Resolved: parser API, transcript model, replay route, and sidebar placement are assigned by ADQ-09. | `docs/SPEC.md` Sections 8-11; ADQ-09 implementation |
> | D-001 | Resolved: verification fixture filenames and implementation paths are recorded in Specification, Procedure, and ADQ-09 evidence. | `_CONTEXT.md` Anticipated Artifacts; `docs/SPEC.md` Section 19.3 |
>

### CLM-006 — Construction

> ##### Construction
>
> | Component | Construction expectation | Source |
> |---|---|---|
> | Replay parser | Read ordered newline-delimited `HarnessEvent` records, ignore malformed final records, retain valid prior records, redact replay output, and emit diagnostics for replay/reporting. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` FR-073 and NFR-013; `frontend/src/lib/harness/session-events.ts` |
> | Transcript reconstruction | Group accepted turns, assistant deltas/completions, tool lifecycle summaries, terminal outcomes, and diagnostics into a replayable transcript representation. | `docs/SPEC.md` Sections 9.3-9.4; `docs/PRD.md` FR-076; `frontend/src/lib/harness/transcript-replay.ts` |
> | SDK linkage projection | Include `sdkSessionId`, `sdkTranscriptPath` or `sdkSessionStoreKey`, `sdkProjectKey`, and resume metadata from session metadata when present, while keeping these fields adapter metadata. | `docs/SPEC.md` Sections 8.3-8.4; `docs/TYPES.md` Section 7.2 |
> | Artifact link projection | Represent large payloads by session artifact paths rather than inlining raw large or sensitive content. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-7 |
> | Verification fixtures | Include transcript reconstruction, malformed-tail, redaction, API replay, SDK-linkage, and sidebar render tests in accepted fixture paths. | `_CONTEXT.md` Anticipated Artifacts; `docs/SPEC.md` Section 19.3 validation IDs; ADQ-09 tests |
>

### CLM-007 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Runtime audit canonicality, professional boundaries, provider-neutrality | MATCH |
> | REF-002 | `docs/CONTRACT.md` | Binding invariants for event replay, transcript status, redaction, and SDK boundaries | MATCH |
> | REF-003 | `docs/SPEC.md` | Session layout, event schema, replay rules, SDK metadata, validation IDs | MATCH |
> | REF-004 | `docs/TYPES.md` | Vocabulary and type targets for runtime audit mirror, session metadata, and `HarnessEvent` | MATCH |
> | REF-005 | `docs/PLAN.md` | R1 sequencing context and runtime validation direction | MATCH |
> | REF-006 | `docs/PRD.md` | Product requirements for replay and SDK transcript linkage | MATCH |
> | REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method context only | MATCH |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-04 Runtime Replay and Transcript View

> #### Specification: DEL-05-04 Runtime Replay and Transcript View
>

### CLM-009 — Scope

> ##### Scope
>
> DEL-05-04 specifies the backend feature slice that reconstructs runtime replay and transcript views from Chirality-owned session events. It covers replay parsing, transcript reconstruction tests, malformed-tail handling, terminal-state projection, and SDK transcript linkage surfaced as non-canonical adapter metadata.
>
> In scope:
>
> - Read canonical `.chirality/sessions/<sessionId>/events.jsonl` records and session metadata for replay/reporting.
> - Preserve valid prior JSONL events when the tail line is malformed and surface diagnostics.
> - Reconstruct accepted turns, assistant output, tool summaries, terminal outcomes, artifact links, and SDK transcript links.
> - Keep SDK transcripts secondary to Chirality `HarnessEvent` records unless imported into `HarnessEvent` form.
> - Maintain separation between compact browser `UIEvent`s and richer persisted `HarnessEvent`s.
>
> Out of scope:
>
> - Defining the full `HarnessEvent` schema and append-only writer. That is primarily DEL-05-02.
> - Canonical session folder migration and legacy session migration helpers. That is primarily DEL-05-01.
> - Tool result storage thresholds and raw artifact storage. That is primarily DEL-05-05.
> - Tool permission semantics, which are excluded by the package context.
>
> Sources: `_CONTEXT.md`; `docs/SPEC.md` Sections 8-11; `docs/CONTRACT.md` K-EVENT and K-SDK invariants; `docs/PRD.md` FR-073, FR-076, FR-118, FR-121. D-APP-38 authority corpus v2 reports these references as `MATCH`.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-05-04-REQ-001 | The replay reader MUST treat `.chirality/sessions/<sessionId>/events.jsonl` as the canonical runtime audit mirror for transcript reconstruction. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4 |
> | DEL-05-04-REQ-002 | The replay reader MUST process newline-delimited `HarnessEvent` records in write sequence. | `docs/SPEC.md` Section 9.2 |
> | DEL-05-04-REQ-003 | Replay MUST ignore a malformed trailing JSONL line, preserve valid prior events, and surface a diagnostic. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
> | DEL-05-04-REQ-004 | Replay MUST NOT treat SDK transcripts as canonical project or runtime audit truth unless their content has been explicitly imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3; `docs/DIRECTIVE.md` Section 2.3 |
> | DEL-05-04-REQ-005 | Transcript reconstruction MUST include accepted user turns and terminal outcomes when the corresponding `HarnessEvent`s are present. | `docs/SPEC.md` Sections 9.3-9.4; `docs/CONTRACT.md` K-EVENT-2 and K-EVENT-3 |
> | DEL-05-04-REQ-006 | Transcript reconstruction SHOULD include assistant deltas/completions, tool summaries, artifact links, and SDK transcript links when supported by available events or session metadata. | `docs/SPEC.md` Sections 8.3, 9.3, and 9.4; `docs/PRD.md` FR-076 and FR-085 |
> | DEL-05-04-REQ-007 | SDK-specific names, IDs, transcript paths, and store keys MUST remain adapter metadata and MUST NOT redefine public Chirality replay contracts. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-ENGINE-4 |
> | DEL-05-04-REQ-008 | Replay output MUST redact or omit secrets and MUST NOT expose API keys from event data, runtime logs, tool artifacts, provider errors, or SDK metadata. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6; `docs/DIRECTIVE.md` Section 2.9 |
> | DEL-05-04-REQ-009 | Legacy session records MUST remain readable for replay-related session discovery through the D-APP-41 eager conversion path, after which canonical folder records are the runtime source. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077 and session storage notes; `D-APP-41` |
> | DEL-05-04-REQ-010 | Replay fixtures MUST cover event append/replay, malformed trailing JSONL behavior, and SDK session linkage/resume metadata. | `docs/SPEC.md` Section 19.3; `docs/PRD.md` conformance bullets |
> | DEL-05-04-REQ-011 | ASSUMPTION: the transcript view model should represent large tool results by summary and artifact reference rather than raw inline payload. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-7 |
> | DEL-05-04-REQ-012 | The accepted parser, model, API, component, and fixture paths are assigned by ADQ-09 implementation and must remain recorded in evidence. | Source gap resolved by ADQ-09 |
> | DEL-05-04-REQ-013 | The implementation handoff MUST record `frontend/src/lib/harness/session-events.ts`, `frontend/packages/harness-contract/src/transcript-replay.ts`, `frontend/src/app/api/harness/session/[id]/events/route.ts`, `frontend/src/components/shell/transcript-stream-view.tsx`, and the focused replay/transcript fixtures. | `docs/SPEC.md` Sections 8-11; decomposition DEL-05-04 row; P3 items C-001 and D-001 |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / contract | Applicability | Source |
> |---|---|---|
> | Chirality session layout | Replay consumes `.chirality/sessions/<sessionId>/session.json`, `events.jsonl`, `turns/`, `artifacts/`, and `sdk/` where present. | `docs/SPEC.md` Section 8.2 |
> | `HarnessEvent` type target | Replay consumes stable versioned events with event/session/turn identity and typed data payloads. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | Runtime engine adapter rule | Replay-facing contracts remain Chirality-owned and provider-neutral. | `docs/SPEC.md` Section 10.3 |
> | Runtime event invariants | Accepted turns, terminal events, malformed-tail tolerance, redaction, and artifact budgeting govern replay behavior. | `docs/CONTRACT.md` K-EVENT-2 through K-EVENT-7 |
> | SDK transcript invariant | SDK transcript linkage is resume/debug metadata, not canonical replay truth. | `docs/CONTRACT.md` K-SDK-3 |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement | Verification approach |
> |---|---|
> | DEL-05-04-REQ-001, DEL-05-04-REQ-002 | Unit test replay ordering from valid `events.jsonl` fixtures. |
> | DEL-05-04-REQ-003 | Malformed-tail fixture: final line invalid JSON; valid earlier events still appear; diagnostic is returned. |
> | DEL-05-04-REQ-004, DEL-05-04-REQ-007 | Type/API tests or snapshot tests showing SDK transcript fields appear only as adapter metadata, not canonical event identity. |
> | DEL-05-04-REQ-005, DEL-05-04-REQ-006 | Transcript reconstruction tests for accepted turns, assistant output, tool summaries, terminal outcomes, artifact links, and SDK transcript links. |
> | DEL-05-04-REQ-008 | Redaction fixture with secret-like event/tool/provider data; replay output omits or redacts sensitive values. |
> | DEL-05-04-REQ-009 | Legacy session discovery/retrieval fixture remains readable while canonical folder layout is introduced. |
> | DEL-05-04-REQ-010 | Section 9 validation coverage includes `section9.session_event_replay` and `section9.sdk_session_link_resume`. |
> | DEL-05-04-REQ-011 | Tool-result replay fixture confirms compact summary plus artifact link behavior. |
> | DEL-05-04-REQ-013 | Handoff/review check confirms all replay parser, transcript model, route/component, and fixture path placeholders are filled with accepted ADQ-09 code/test locations. |
>
> Minimum fixture coverage before closure includes success, failure, cancellation, interruption, malformed-tail diagnostics, legacy session reads, SDK transcript linkage, redaction behavior, and compact tool-result artifact links. ADQ-09 assigns the replay/transcript fixture paths: `frontend/src/__tests__/lib/session-events.test.ts`, `frontend/src/__tests__/lib/transcript-replay.test.ts`, `frontend/src/__tests__/api/harness/routes.test.ts`, and `frontend/src/__tests__/components/harness-stream-views.test.ts`. Source reread: `docs/SPEC.md` Sections 9.2 and 19.3; `docs/PRD.md` Section 12 validation IDs. Disposition: X-001 incorporated with implementation-specific names filled by ADQ-09.
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required records or artifacts for this deliverable:
>
> - Replay parser implementation: `frontend/src/lib/harness/session-events.ts`.
> - Transcript reconstruction model and interfaces: `frontend/src/lib/harness/transcript-replay.ts`.
> - Replay API placement: `frontend/src/app/api/harness/session/[id]/events/route.ts`.
> - Transcript UI placement: `frontend/src/components/shell/transcript-stream-view.tsx` and the Workspace sidebar Transcript tab.
> - Transcript, malformed-tail, SDK-linkage, redaction, and artifact-link fixtures: `frontend/src/__tests__/lib/transcript-replay.test.ts`, `frontend/src/__tests__/lib/session-events.test.ts`, `frontend/src/__tests__/api/harness/routes.test.ts`, and `frontend/src/__tests__/components/harness-stream-views.test.ts`.
> - Source-state note: D-APP-38 authority corpus v2 reports all DEL-05-04 references as `MATCH`.

- **AC-001** — The runtime replay and transcript view preserves canonical Chirality event precedence, valid-event ordering, malformed-tail tolerance, redaction, adapter-only SDK linkage, compact artifact references, and recorded implementation and fixture paths.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-05-04 Runtime Replay and Transcript View

> #### Procedure: DEL-05-04 Runtime Replay and Transcript View
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define an operational path for producing and verifying the Runtime Replay and Transcript View deliverable. ADQ-09 assigned the implementation ownership paths for the replay parser, transcript model, replay API, sidebar component, and focused fixtures.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / note | Source |
> |---|---|---|
> | Canonical session folder layout is available through the D-APP-41/ADQ-08 eager conversion path. | Satisfied for replay discovery. | `docs/SPEC.md` Section 8.2; `D-APP-41`; ADQ-08 evidence |
> | Legacy session records remain readable through conversion. | Satisfied: flat records convert to canonical folders on read/list/resume/save. | `docs/SPEC.md` Section 8.1; `D-APP-41`; ADQ-08 evidence |
> | `HarnessEvent` schema and event writer behavior are available. | Satisfied for ADQ-09 replay and transcript projection. | `docs/SPEC.md` Section 9; `frontend/src/lib/harness/event-schema.ts`; `frontend/src/lib/harness/session-events.ts` |
> | SDK session linkage metadata is available in session metadata or fixtures. | Satisfied by `SessionRecord` linkage fields and transcript projection fixtures. | `docs/SPEC.md` Section 8.3; `frontend/src/lib/harness/transcript-replay.ts`; `frontend/src/__tests__/lib/transcript-replay.test.ts` |
> | Declared dependency edges are accepted for ADQ-09 replay closure. | Satisfied for DEL-05-04 ADQ-09 scope; ADQ-10 remains for DEL-05-05 checksum/retention policy outside this transcript slice. | `_DEPENDENCIES.md`; `D-APP-42` |
> | Redaction helper or policy is available. | Satisfied: replay applies read-time redaction to imported/manual logs as well as append-time redaction. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6; `frontend/src/lib/harness/session-events.ts` |
>
> Dependency closure disposition: F-001 is resolved for the ADQ-09 transcript/replay scope. DEL-05-01 is satisfied by ADQ-08/D-APP-41, DEL-05-02 replay-facing schema/writer behavior is available, SDK linkage is fixture-covered, read-time redaction is implemented, and DEL-05-05 artifact-link projection is covered without claiming ADQ-10 checksum/retention closure. Source reread: `_DEPENDENCIES.md` extracted dependency register; decomposition rows for DEL-05-01, DEL-05-02, DEL-05-04, and DEL-05-05; `docs/CONTRACT.md` K-EVENT-6 and K-EVENT-7.
>

### CLM-017 — Steps

> ##### Steps
>
> 1. **Confirm source contracts.**
>    - Re-read the accepted session layout, event schema, replay rules, SDK linkage fields, and browser/runtime contract separation.
>    - Use D-APP-38 authority corpus v2 as the current source-state check.
>
> 2. **Define replay input handling.**
>    - Read `.chirality/sessions/<sessionId>/session.json` and `.chirality/sessions/<sessionId>/events.jsonl` for canonical vNext sessions.
>    - Preserve compatibility for legacy `{sessionRoot}/{sessionId}.json` records through D-APP-41 eager conversion to canonical folders.
>    - Keep exact path override behavior for `CHIRALITY_SESSION_ROOT` aligned with the session store contract.
>
> 3. **Parse `events.jsonl`.**
>    - Process newline-delimited `HarnessEvent` records in write sequence.
>    - Validate the required event fields defined by the type target.
>    - Ignore a malformed trailing line while retaining prior valid events.
>    - Return or record a diagnostic for malformed-tail replay.
>
> 4. **Build the transcript projection.**
>    - Group events by `turnId` where available.
>    - Project accepted user input, assistant deltas/completions, tool summaries, terminal outcomes, and artifact references.
>    - Treat missing optional event categories as absent data, not parser failure, unless a required accepted-turn/terminal invariant is violated.
>    - ASSUMPTION: expose compact tool summaries and artifact links rather than raw large payloads.
>
> 5. **Attach SDK transcript linkage.**
>    - Read `engineSessionId`, `claudeSessionId`, `sdkSessionId`, `sdkTranscriptPath`, `sdkSessionStoreKey`, `sdkConfigDir`, SDK setting sources, SDK package versions, and model metadata when present in `session.json`.
>    - Mark SDK transcript/store linkage as adapter metadata and secondary runtime state.
>    - Do not let SDK message names, transcript paths, or session IDs become canonical Chirality identifiers.
>
> 6. **Apply redaction and safety filtering.**
>    - Ensure replay output and diagnostics do not expose API keys or configured secret variants.
>    - For large or sensitive tool result data, show summary and artifact reference only.
>    - Surface redaction limitations as diagnostics rather than silently leaking raw content.
>
> 7. **Create verification fixtures.**
>    - Valid transcript reconstruction fixture.
>    - Malformed-tail JSONL fixture.
>    - Terminal outcome fixture for success, failure, cancellation, or interruption where source events exist.
>    - SDK linkage fixture confirming `events.jsonl` remains canonical.
>    - Legacy session fixture.
>    - Redaction fixture for secret-like event, tool, provider, or SDK metadata.
>    - Tool-result artifact-link fixture for compact summaries and stored payload references.
>    - Record exact fixture filenames in the evidence file.
>
> 8. **Run verification.**
>    - Execute unit tests and Section 9 validation coverage for `section9.session_event_replay` and `section9.sdk_session_link_resume`.
>
> 9. **Record accepted implementation locations.**
>    - Record the replay parser module path, transcript view model/interface name, route or component placement, transcript reconstruction fixture path, malformed-tail fixture path, SDK-linkage fixture path, redaction fixture path, and tool-result artifact fixture path.
>    - Source reread: `docs/SPEC.md` Sections 8.2, 8.4, 9.2, and 19.3; decomposition DEL-05-04 row. Disposition: D-001 incorporated and filled by ADQ-09 code discovery/implementation.
>

### CLM-018 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Canonical replay | Valid events reconstruct accepted turns, assistant output, tool summaries, terminal outcomes, and artifact links where present. |
> | Malformed tail | Invalid final JSONL line is ignored; valid prior events survive; diagnostic is visible. |
> | SDK linkage | SDK session/transcript/store metadata appears as secondary adapter metadata only. |
> | Legacy read | Legacy flat session record remains readable through D-APP-41 eager conversion and then replay uses canonical folder state. |
> | Redaction | Secret-like values do not appear in replay output, diagnostics, or summaries. |
> | Contract separation | Browser `UIEvent` and persisted `HarnessEvent` concepts remain distinct in naming and tests. |
> | Closure slots | Parser API, transcript model, route/component placement, fixture paths, dependency edges, and redaction/tool-result artifact coverage are recorded in ADQ-09 evidence. |
>

### CLM-019 — Records

> ##### Records
>
> Expected records for closure:
>
> - Replay parser implementation path: `frontend/src/lib/harness/session-events.ts`.
> - Transcript reconstruction model path: `frontend/packages/harness-contract/src/transcript-replay.ts`.
> - Replay API path: `frontend/src/app/api/harness/session/[id]/events/route.ts`.
> - Transcript UI path: `frontend/src/components/shell/transcript-stream-view.tsx`.
> - Transcript reconstruction, malformed-tail, SDK transcript linkage, redaction, API replay, and sidebar render test results.
> - Source-state note for D-APP-38 authority corpus v2 `MATCH`.
> - Dependency register update for the ADQ-09 replay/transcript scope.

- **VER-001** — Validate schema and traceability; map and parity-check every legacy source line; derive the deterministic REVIEW checklist; render script-free HTML; and confirm source/control byte preservation.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-05-04 Runtime Replay and Transcript View

> #### Guidance: DEL-05-04 Runtime Replay and Transcript View
>

### CLM-021 — Purpose

> ##### Purpose
>
> This deliverable makes Chirality runtime work replayable from product-owned records. The replay surface should let operators and tests reconstruct accepted user turns, assistant output, tool activity summaries, terminal outcomes, diagnostics, artifact references, and SDK transcript linkage without treating SDK transcripts or UI state as canonical truth.
>
> Sources: `_CONTEXT.md`; `docs/DIRECTIVE.md` Sections 2.2-2.3; `docs/SPEC.md` Sections 8-10; `docs/CONTRACT.md` K-EVENT and K-SDK invariants.
>

### CLM-022 — Principles

> ##### Principles
>
> 1. **Replay from Chirality events first.** Use `.chirality/sessions/<sessionId>/events.jsonl` as the canonical replay input. SDK transcripts can help resume/debugging, but they do not replace the Chirality audit mirror. Sources: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4 and K-SDK-3.
> 2. **Separate UI compactness from audit richness.** Browser `UIEvent`s remain compact while persisted `HarnessEvent`s may carry richer runtime metadata. Replay should not blur those contracts. Sources: `docs/SPEC.md` Sections 10.3 and 11; `docs/CONTRACT.md` K-EVENT-1.
> 3. **Keep provider-specific details at adapter boundaries.** SDK session IDs, transcript paths, tool names, and message names are useful metadata but must not become public Chirality contract identity. Sources: `docs/SPEC.md` Section 10.3; `docs/DIRECTIVE.md` Section 2.10.
> 4. **Prefer recoverability over all-or-nothing parsing.** A malformed trailing JSONL record should not destroy access to earlier valid events. Sources: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5.
> 5. **Do not leak secrets through replay.** Replay output, diagnostics, and artifact summaries should follow redaction and artifact-reference rules. Sources: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6 and K-EVENT-7.
>

### CLM-023 — Considerations

> ##### Considerations
>
> - The replay model should preserve stable identity fields: `sessionId`, `turnId`, and event identity. Stable identifiers persist across path and label changes. Source: `docs/TYPES.md` Sections 1.7-2.
> - Terminal outcomes matter as much as streamed text. Accepted turns must end with a durable success, failure, cancellation, or interruption event for reliable replay. Source: `docs/CONTRACT.md` K-EVENT-2 and K-EVENT-3.
> - Session metadata can provide SDK linkage (`sdkSessionId`, `sdkTranscriptPath`, `sdkSessionStoreKey`, `sdkResumeMode`) but replay should present it as linkage metadata, not as the transcript authority. Source: `docs/SPEC.md` Sections 8.3-8.4.
> - Legacy session records are handled through the D-APP-41 eager conversion path; replay should consume the canonical folder state after conversion. Source: `docs/SPEC.md` Section 8.1; `D-APP-41`.
> - ADQ-09 assigns the concrete view model and API shape: `TranscriptView`/`TranscriptItem` in `frontend/packages/harness-contract/src/transcript-replay.ts`, the replay API in `frontend/src/app/api/harness/session/[id]/events/route.ts`, and the sidebar component in `frontend/src/components/shell/transcript-stream-view.tsx`.
>

### CLM-024 — Trade-offs

> ##### Trade-offs
>
> | Topic | Guidance | Rationale |
> |---|---|---|
> | Strict JSONL parsing vs. tolerant replay | Favor tolerant replay for a malformed final line, while surfacing diagnostics. | Protects audit recoverability after interruption or partial writes. |
> | Raw tool output vs. artifact links | Favor compact summaries plus artifact links for large or sensitive results. | Prevents replay views from flooding UI/model context and supports redaction policy. |
> | SDK transcript detail vs. Chirality canonicality | Show SDK transcript/store linkage as secondary metadata. | Maintains provider-neutral core and avoids SDK-shaped public contracts. |
> | Legacy compatibility vs. clean vNext layout | Use D-APP-41 eager conversion and canonical folder records for replay. | Gives deterministic long-term storage while keeping legacy reads usable through migration. |
>
> For tool results, compact summaries plus artifact references are the preferred replay shape because the audit view needs durable traceability without re-exposing large or sensitive payloads in transcript context. The artifact reference preserves where the full result was stored, while the summary supports review and redaction-aware replay. Sources reread: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6 and K-EVENT-7. Disposition: E-001 incorporated.
>

### CLM-025 — Examples

> ##### Examples
>
> | Scenario | Expected replay behavior | Source |
> |---|---|---|
> | Valid event log with accepted turn, model deltas, and completion | Transcript view shows the accepted user input, assistant output, and terminal completion. | `docs/SPEC.md` Sections 9.3-9.4 |
> | Event log with malformed final line | Replay ignores the malformed tail, returns prior valid events, and surfaces a diagnostic. | `docs/SPEC.md` Section 9.2 |
> | Session metadata includes `sdkTranscriptPath` | Transcript view may link or display the SDK transcript location as secondary metadata; it must keep `events.jsonl` canonical. | `docs/SPEC.md` Section 8.4 |
> | Tool result event references an artifact | Transcript view should summarize the tool outcome and link the artifact path rather than inlining raw large content. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-7 |
>

### CLM-026 — Source-State Notes

> ##### Source-State Notes
>
> D-APP-38 authority corpus v2 reports DEL-05-04 references as `MATCH`, including `docs/PRD.md`. PRD-derived replay requirements are no longer warning-qualified for this deliverable.
>
> Disposition: B-001 is retired for the current source corpus; the previous PRD hash mismatch is resolved by D-APP-38 corpus v2 reconciliation.
>

### CLM-027 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | None | No content conflict identified in accessible source slices during P1/P2. | N/A | N/A | N/A | N/A | N/A |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-042 SOW-046 OBJ-003 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
