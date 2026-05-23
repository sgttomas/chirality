# Datasheet: DEL-05-04 Runtime Replay and Transcript View

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-05-04 |
| Deliverable name | Runtime Replay and Transcript View |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Decomposition variant | SOFTWARE_DECOMP v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| Responsible party | TBD |
| Context envelope | M |
| Scope items | SOW-042, SOW-046 |
| Objective | OBJ-003 |
| Anticipated artifacts | Replay parser; transcript reconstruction tests; malformed-tail tests |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary store | `.chirality/sessions/<sessionId>/events.jsonl` as the product-owned Chirality audit mirror. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4; `docs/TYPES.md` Section 1.8 |
| Session metadata input | `.chirality/sessions/<sessionId>/session.json` with session identity, project root, persona, mode, model, SDK linkage, transcript/store linkage, and resume metadata where available. | `docs/SPEC.md` Sections 8.2-8.4 |
| Legacy metadata input | Existing `{sessionRoot}/{sessionId}.json` records remain readable during migration. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` Section 8.12 and session storage notes; source-state warning applies to `docs/PRD.md` hash mismatch |
| Event record shape | `HarnessEvent` includes `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, timestamp, type, and data payload. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| Replay tolerance | Replay must ignore malformed trailing JSONL lines while preserving valid prior events and surfacing diagnostics. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5; `docs/PRD.md` FR-073 and NFR-013, with PRD source-state warning |
| Transcript content target | Accepted user turns, assistant output, tool summaries, terminal outcomes, artifact links, and SDK transcript links. | `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` FR-076, with PRD source-state warning |
| SDK transcript status | SDK transcript paths/store keys are secondary adapter metadata unless explicitly imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3; `docs/DIRECTIVE.md` Sections 2.3 and 2.10 |
| UI/runtime contract separation | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts; replay must not make public UI/API contracts SDK-shaped. | `docs/SPEC.md` Sections 10.3 and 11; `docs/CONTRACT.md` K-EVENT-1 and K-ENGINE-4 |
| Secret handling | Secrets must not be stored in events; runtime logs, tool artifacts, and provider errors require redaction. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-6 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Upstream dependencies | TBD - no accepted dependency edges have been extracted yet. | `_DEPENDENCIES.md` |
| Downstream dependencies | TBD - no accepted dependency edges have been extracted yet. | `_DEPENDENCIES.md` |
| Canonicality constraint | `events.jsonl` remains canonical for runtime replay; SDK transcripts assist resume/debugging but do not displace Chirality events. | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3 |
| Migration constraint | Replay must account for both canonical folder sessions and legacy flat session records until migration is explicitly complete. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` session storage notes, with PRD source-state warning |
| Exact parser API | TBD - source documents define behavior and storage contracts, not the module API. | Source gap |
| Exact transcript view route/UI placement | TBD - source documents identify replay/transcript behavior, not a concrete route or component path. | Source gap |
| Tool summary detail level | ASSUMPTION: replay should expose compact summaries and artifact links rather than raw large payloads, because large payloads are stored as artifacts and referenced by path. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-7 |

## Construction

| Component | Construction expectation | Source |
|---|---|---|
| Replay parser | Read ordered newline-delimited `HarnessEvent` records, ignore malformed final records, retain valid prior records, and emit diagnostics for replay/reporting. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` FR-073 and NFR-013, with PRD source-state warning |
| Transcript reconstruction | Group accepted turns, model deltas/completions, tool lifecycle summaries, and terminal outcomes into a replayable transcript representation. | `docs/SPEC.md` Sections 9.3-9.4; `docs/PRD.md` FR-076, with PRD source-state warning |
| SDK linkage projection | Include `sdkSessionId`, `sdkTranscriptPath` or `sdkSessionStoreKey`, `sdkProjectKey`, and resume metadata from session metadata when present, while keeping these fields adapter metadata. | `docs/SPEC.md` Sections 8.3-8.4; `docs/TYPES.md` Section 7.2 |
| Artifact link projection | Represent large payloads by session artifact paths rather than inlining raw large or sensitive content. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-7 |
| Verification fixtures | Include transcript reconstruction tests and malformed-tail tests; exact fixture filenames are TBD. | `_CONTEXT.md` Anticipated Artifacts; `docs/SPEC.md` Section 19.3 validation IDs |

## References

| RefID | Source | Use | Source state |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Runtime audit canonicality, professional boundaries, provider-neutrality | MATCH |
| REF-002 | `docs/CONTRACT.md` | Binding invariants for event replay, transcript status, redaction, and SDK boundaries | MATCH |
| REF-003 | `docs/SPEC.md` | Session layout, event schema, replay rules, SDK metadata, validation IDs | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary and type targets for runtime audit mirror, session metadata, and `HarnessEvent` | MATCH |
| REF-005 | `docs/PLAN.md` | R1 sequencing context and runtime validation direction | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements for replay and SDK transcript linkage | HASH_MISMATCH - treated as source-state warning per task brief |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method context only | MATCH |
