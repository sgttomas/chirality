# Specification: DEL-05-04 Runtime Replay and Transcript View

## Scope

DEL-05-04 specifies the backend feature slice that reconstructs runtime replay and transcript views from Chirality-owned session events. It covers replay parsing, transcript reconstruction tests, malformed-tail handling, terminal-state projection, and SDK transcript linkage surfaced as non-canonical adapter metadata.

In scope:

- Read canonical `.chirality/sessions/<sessionId>/events.jsonl` records and session metadata for replay/reporting.
- Preserve valid prior JSONL events when the tail line is malformed and surface diagnostics.
- Reconstruct accepted turns, assistant output, tool summaries, terminal outcomes, artifact links, and SDK transcript links.
- Keep SDK transcripts secondary to Chirality `HarnessEvent` records unless imported into `HarnessEvent` form.
- Maintain separation between compact browser `UIEvent`s and richer persisted `HarnessEvent`s.

Out of scope:

- Defining the full `HarnessEvent` schema and append-only writer. That is primarily DEL-05-02.
- Canonical session folder migration and legacy session migration helpers. That is primarily DEL-05-01.
- Tool result storage thresholds and raw artifact storage. That is primarily DEL-05-05.
- Tool permission semantics, which are excluded by the package context.

Sources: `_CONTEXT.md`; `docs/SPEC.md` Sections 8-11; `docs/CONTRACT.md` K-EVENT and K-SDK invariants; `docs/PRD.md` FR-073, FR-076, FR-118, FR-121, with PRD source-state warning.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-05-04-REQ-001 | The replay reader MUST treat `.chirality/sessions/<sessionId>/events.jsonl` as the canonical runtime audit mirror for transcript reconstruction. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4 |
| DEL-05-04-REQ-002 | The replay reader MUST process newline-delimited `HarnessEvent` records in write sequence. | `docs/SPEC.md` Section 9.2 |
| DEL-05-04-REQ-003 | Replay MUST ignore a malformed trailing JSONL line, preserve valid prior events, and surface a diagnostic. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| DEL-05-04-REQ-004 | Replay MUST NOT treat SDK transcripts as canonical project or runtime audit truth unless their content has been explicitly imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3; `docs/DIRECTIVE.md` Section 2.3 |
| DEL-05-04-REQ-005 | Transcript reconstruction MUST include accepted user turns and terminal outcomes when the corresponding `HarnessEvent`s are present. | `docs/SPEC.md` Sections 9.3-9.4; `docs/CONTRACT.md` K-EVENT-2 and K-EVENT-3 |
| DEL-05-04-REQ-006 | Transcript reconstruction SHOULD include assistant deltas/completions, tool summaries, artifact links, and SDK transcript links when supported by available events or session metadata. | `docs/SPEC.md` Sections 8.3, 9.3, and 9.4; `docs/PRD.md` FR-076 and FR-085, with PRD source-state warning |
| DEL-05-04-REQ-007 | SDK-specific names, IDs, transcript paths, and store keys MUST remain adapter metadata and MUST NOT redefine public Chirality replay contracts. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-ENGINE-4 |
| DEL-05-04-REQ-008 | Replay output MUST redact or omit secrets and MUST NOT expose API keys from event data, runtime logs, tool artifacts, provider errors, or SDK metadata. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6; `docs/DIRECTIVE.md` Section 2.9 |
| DEL-05-04-REQ-009 | Legacy session records MUST remain readable for replay-related session discovery until migration completion is explicitly accepted. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077 and session storage notes, with PRD source-state warning |
| DEL-05-04-REQ-010 | Replay fixtures MUST cover event append/replay, malformed trailing JSONL behavior, and SDK session linkage/resume metadata. | `docs/SPEC.md` Section 19.3; `docs/PRD.md` conformance bullets, with PRD source-state warning |
| DEL-05-04-REQ-011 | ASSUMPTION: the transcript view model should represent large tool results by summary and artifact reference rather than raw inline payload. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-7 |
| DEL-05-04-REQ-012 | Exact parser module names, exported TypeScript interfaces, and UI route/component paths are TBD until implementation ownership and local code integration are assigned. | Source gap |
| DEL-05-04-REQ-013 | The implementation handoff MUST record the accepted replay parser module path, transcript view model/interface name, transcript route or component placement, and fixture paths once those names are established; until then they remain `TBD` and are not requirements by guesswork. | `docs/SPEC.md` Sections 8-11; decomposition DEL-05-04 row; P3 items C-001 and D-001 |

## Standards

| Standard / contract | Applicability | Source |
|---|---|---|
| Chirality session layout | Replay consumes `.chirality/sessions/<sessionId>/session.json`, `events.jsonl`, `turns/`, `artifacts/`, and `sdk/` where present. | `docs/SPEC.md` Section 8.2 |
| `HarnessEvent` type target | Replay consumes stable versioned events with event/session/turn identity and typed data payloads. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| Runtime engine adapter rule | Replay-facing contracts remain Chirality-owned and provider-neutral. | `docs/SPEC.md` Section 10.3 |
| Runtime event invariants | Accepted turns, terminal events, malformed-tail tolerance, redaction, and artifact budgeting govern replay behavior. | `docs/CONTRACT.md` K-EVENT-2 through K-EVENT-7 |
| SDK transcript invariant | SDK transcript linkage is resume/debug metadata, not canonical replay truth. | `docs/CONTRACT.md` K-SDK-3 |

## Verification

| Requirement | Verification approach |
|---|---|
| DEL-05-04-REQ-001, DEL-05-04-REQ-002 | Unit test replay ordering from valid `events.jsonl` fixtures. |
| DEL-05-04-REQ-003 | Malformed-tail fixture: final line invalid JSON; valid earlier events still appear; diagnostic is returned. |
| DEL-05-04-REQ-004, DEL-05-04-REQ-007 | Type/API tests or snapshot tests showing SDK transcript fields appear only as adapter metadata, not canonical event identity. |
| DEL-05-04-REQ-005, DEL-05-04-REQ-006 | Transcript reconstruction tests for accepted turns, assistant output, tool summaries, terminal outcomes, artifact links, and SDK transcript links. |
| DEL-05-04-REQ-008 | Redaction fixture with secret-like event/tool/provider data; replay output omits or redacts sensitive values. |
| DEL-05-04-REQ-009 | Legacy session discovery/retrieval fixture remains readable while canonical folder layout is introduced. |
| DEL-05-04-REQ-010 | Section 9 validation coverage includes `section9.session_event_replay` and `section9.sdk_session_link_resume`. |
| DEL-05-04-REQ-011 | Tool-result replay fixture confirms compact summary plus artifact link behavior. |
| DEL-05-04-REQ-013 | Handoff/review check confirms all replay parser, transcript model, route/component, and fixture path placeholders are either filled with accepted code locations or retained as explicit `TBD` blockers. |

Minimum fixture coverage before closure includes success, failure, cancellation, interruption, malformed-tail diagnostics, legacy session reads, SDK transcript linkage, redaction behavior, and compact tool-result artifact links. Exact validation IDs and fixture filenames remain `TBD` until implementation adds them. Source reread: `docs/SPEC.md` Sections 9.2 and 19.3; `docs/PRD.md` Section 12 validation IDs with REF-006 source-state warning. Disposition: X-001 incorporated as coverage checklist with implementation-specific names left `TBD`.

## Documentation

Required records or artifacts for this deliverable:

- Replay parser implementation notes or module documentation: TBD exact location.
- Transcript reconstruction test fixtures.
- Malformed-tail JSONL fixtures and expected diagnostics.
- SDK transcript/session-link fixture showing non-canonical linkage.
- Accepted implementation slots for replay parser API, transcript view model/interface, route or component placement, and fixture paths; `TBD` until code discovery assigns them.
- Source-state note: `docs/PRD.md` was used with HASH_MISMATCH warning per task brief and must not be treated as silently verified source state.
