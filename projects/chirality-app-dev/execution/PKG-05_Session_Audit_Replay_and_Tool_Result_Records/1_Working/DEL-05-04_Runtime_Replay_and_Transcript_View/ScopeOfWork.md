---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-04
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-006, SOW-042, SOW-046]
package_objective_refs: [OBJ-001, OBJ-003]
---

# Scope of Work — DEL-05-04

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-04` in service of project scope [SOW-006, SOW-042, SOW-046] and package objectives [OBJ-001, OBJ-003].

- **OUT-001** — Labelled read-only replay and transcript projections from canonical Runtime records with exact attribution/parentage, malformed-tail diagnostics, artifact links and primary-dialogue isolation; explicit native continuation remains distinct and verified.

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
> | Deliverable name | Runtime Replay, Dialogue, and Agent Transcript Projection |
> | Package | PKG-05 Session Audit, Replay, and Tool Result Records |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | Responsible party | TBD |
> | Context envelope | M |
> | Scope items | SOW-006, SOW-042, SOW-046 |
> | Objective | OBJ-001, OBJ-003 |
> | Anticipated artifacts | Replay parser; transcript model; selected-session read-only replay lens; bounded/stale projection; exact-parentage and transcript reconstruction tests; malformed-tail tests |
>

### CLM-003 — Attributes

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

Named verification: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

### CLM-004 — Conditions

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

Named verification: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

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

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.

Unfinished delivery: Complete live malformed-tail/redaction witnesses and replay-versus-explicit-continuation isolation checks; verify account/policy compatibility, fresh fallback, no in-flight reattachment and right-panel presentation against the current candidate.

### CLM-007 — References

> ##### References
>
> | RefID | Source | Use | Source state |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Runtime audit canonicality, professional boundaries, provider-neutrality | HISTORICAL_MATCH |
> | REF-002 | `docs/CONTRACT.md` | Binding invariants for event replay, transcript status, redaction, and SDK boundaries | HISTORICAL_MATCH |
> | REF-003 | `docs/SPEC.md` | Session layout, event schema, replay rules, SDK metadata, validation IDs | HISTORICAL_MATCH |
> | REF-004 | `docs/TYPES.md` | Vocabulary and type targets for runtime audit mirror, session metadata, and `HarnessEvent` | HISTORICAL_MATCH |
> | REF-005 | `docs/PLAN.md` | R1 sequencing context and runtime validation direction | HISTORICAL_MATCH |
> | REF-006 | `docs/PRD.md` | Product requirements for replay and SDK transcript linkage | HISTORICAL_MATCH |
> | REF-007 | `workflows/software-decomp/WORKFLOW.md` | Decomposition method context only | HISTORICAL_MATCH |


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-04 Runtime Replay and Transcript View

> #### Specification: DEL-05-04 Runtime Replay and Transcript View
>

### CLM-009 — Scope

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

Verification: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.

### CLM-010 — Requirements

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-05-04-REQ-001 | Reconstruct replay from Runtime-owned central events.jsonl records. |
| DEL-05-04-REQ-002 | The replay reader MUST process newline-delimited `HarnessEvent` records in write sequence. |
| DEL-05-04-REQ-003 | Replay MUST ignore a malformed trailing JSONL line, preserve valid prior events, and surface a diagnostic. |
| DEL-05-04-REQ-004 | Replay MUST NOT treat SDK transcripts as canonical project or runtime audit truth unless their content has been explicitly imported into `HarnessEvent` form. |
| DEL-05-04-REQ-005 | Transcript reconstruction MUST include accepted user turns and terminal outcomes when the corresponding `HarnessEvent`s are present. |
| DEL-05-04-REQ-006 | Transcript reconstruction SHOULD include assistant deltas/completions, tool summaries, artifact links, and SDK transcript links when supported by available events or session metadata. |
| DEL-05-04-REQ-007 | Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. |
| DEL-05-04-REQ-008 | Replay output MUST redact or omit secrets and MUST NOT expose API keys from event data, runtime logs, tool artifacts, provider errors, or SDK metadata. |
| DEL-05-04-REQ-009 | Preserve accessible historical records; declared legacy roots use lazy non-destructive Runtime migration. Import or v2 continuation is not a release prerequisite. |
| DEL-05-04-REQ-010 | Replay fixtures MUST cover event append/replay, malformed trailing JSONL behavior, and SDK session linkage/resume metadata. |
| DEL-05-04-REQ-011 | ASSUMPTION: the transcript view model should represent large tool results by summary and artifact reference rather than raw inline payload. |
| DEL-05-04-REQ-012 | Record current Runtime parser/model/client and App replay-view/fixture paths with actual source identity. |
| DEL-05-04-REQ-013 | Name Runtime packages/core/src/session-store.ts and packages/contracts/src/harness/transcript-replay.ts, App selected-session-replay-lens.tsx and current session-event API/client fixtures. |
| DEL-05-04-REQ-014 | Viewing history is labelled read-only and cannot silently resume or mutate the primary dialogue. Explicit native continuation is separately allowed under D-GOV-43 item 5. |
| DEL-05-04-REQ-015 | Viewing replay preserves primary draft/attachments/context/permissions/identity; any explicit continuation action must clearly identify its transition and verify isolation. |
| DEL-05-04-REQ-016 | Replay and Agent projections MUST be rebuildable from admitted canonical project/runtime records, MUST identify provenance and currency where available, and MUST render missing, stale, bounded, malformed, conflicting, or unrecorded evidence explicitly. |
| DEL-05-04-REQ-017 | Parentage and return cross-links MUST use exact canonical identifiers supplied by DEL-08-05/session evidence and MUST NOT be inferred from conversational similarity or UI grouping. |
| DEL-05-04-REQ-018 | Runtime completion or terminal state MUST remain distinct from project-plan completion, deliverable lifecycle acceptance, approval, or professional reliance. |
| DEL-05-04-REQ-019 | Read-only history controls cannot silently mutate a session. Explicit continuation remains a separate native action with truthful compatibility/fresh fallback and no in-flight reattachment. |

Verification: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.

Evidence locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

Named verification: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

### CLM-012 — Verification

Required current checks: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.

Named evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Complete live malformed-tail/redaction witnesses and replay-versus-explicit-continuation isolation checks; verify account/policy compatibility, fresh fallback, no in-flight reattachment and right-panel presentation against the current candidate.

### CLM-013 — Documentation

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.

Unfinished delivery: Complete live malformed-tail/redaction witnesses and replay-versus-explicit-continuation isolation checks; verify account/policy compatibility, fresh fallback, no in-flight reattachment and right-panel presentation against the current candidate.

- **AC-001** — The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

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

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

Current implementation/adoption evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-017 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.
4. Verify verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.
5. Retain inputs, source/candidate identity, commands, output and limitations; update governing scope and any selected work graph only for backchecked outcomes.

Locus and checks: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-018 — Verification

Required current checks: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.

Named evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Complete live malformed-tail/redaction witnesses and replay-versus-explicit-continuation isolation checks; verify account/policy compatibility, fresh fallback, no in-flight reattachment and right-panel presentation against the current candidate.

### CLM-019 — Records

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.

Unfinished delivery: Complete live malformed-tail/redaction witnesses and replay-versus-explicit-continuation isolation checks; verify account/policy compatibility, fresh fallback, no in-flight reattachment and right-panel presentation against the current candidate.

- **VER-001** — Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification.

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

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

Named verification: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

### CLM-023 — Considerations

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

Named verification: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

### CLM-024 — Trade-offs

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

Named verification: Verify malformed-tail diagnostics, synthetic-secret exclusion, parent links, read-only projection, primary state isolation and explicit continuation/fresh-otherwise outcomes. Retain source/candidate identity for G5/native continuity; legacy fixture passes are not live qualification. Evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

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

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Complete live malformed-tail/redaction witnesses and replay-versus-explicit-continuation isolation checks; verify account/policy compatibility, fresh fallback, no in-flight reattachment and right-panel presentation against the current candidate.

### CLM-027 — Conflict Table (for human ruling)

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Complete live malformed-tail/redaction witnesses and replay-versus-explicit-continuation isolation checks; verify account/policy compatibility, fresh fallback, no in-flight reattachment and right-panel presentation against the current candidate.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-006 SOW-042 SOW-046 OBJ-001 OBJ-003 | CLM-010  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
