# Procedure: DEL-06-06 Hook Lifecycle and Compaction Mirror

## Purpose

This procedure describes how to produce and verify the DEL-06-06 hook lifecycle and compaction mirror implementation. It is written for the deliverable artifact, not as an end-user operation runbook.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted DEL-06-06 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
| Runtime event schema and event categories | Available in `docs/SPEC.md` Section 9 and `docs/TYPES.md` Section 7.3 |
| Session audit mirror rules | Available in `docs/SPEC.md` Section 8.4 and `docs/CONTRACT.md` Section 1.5 |
| Hook vocabulary and required hook behavior | Available in `docs/TYPES.md` Section 8.5 and `docs/SPEC.md` Section 15.2 |
| Engine adapter translation rules | Available in `docs/SPEC.md` Section 10.3 |
| Compaction mirror product direction | Available in `docs/PLAN.md` R4; `docs/PRD.md` Section 8.15 is warning-qualified due to HASH_MISMATCH |
| Declared upstream dependencies | Human-declared upstream dependencies remain `TBD`; extracted ACTIVE upstream edges exist in `_DEPENDENCIES.md` and must be closure-checked before final acceptance. |
| Exact implementation file paths | TBD |
| Exact test fixture paths | TBD |

## Steps

1. Confirm the event contract boundary.
   - Use `HarnessEvent` as the persisted runtime event shape.
   - Keep SDK callback names, SDK transcript IDs, and SDK compaction metadata as adapter metadata rather than public Chirality contract fields.
   - Preserve `events.jsonl` as the canonical audit mirror.

2. Define or locate the hook lifecycle mapper.
   - Map supported hook terms from `docs/TYPES.md` Section 8.5: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PreCompact`, `Stop`, `SubagentStart`, and `SubagentStop`.
   - Keep detailed policy enforcement ownership aligned with adjacent deliverables; this mapper records lifecycle and boundary evidence.
   - Exact module path: TBD.

3. Implement hook start evidence.
   - Emit or stage `hook.started` evidence when a supported hook begins.
   - Include session and turn linkage where available.
   - Include safe hook term and target context where available.
   - Do not include secrets or large raw payloads.

4. Implement hook completion and failure evidence.
   - Emit `hook.completed` evidence for successful completion.
   - For failure outcomes, record safe diagnostics and outcome status without inventing an unregistered public event type unless the event registry is updated.
   - Ensure failed hooks preserve fail-closed behavior for write, shell, domain, and subagent actions.

5. Implement `PreCompact` mirroring.
   - When the SDK/model exposes a compaction boundary, persist `context.compacted`.
   - Record boundary metadata and replay implications when safe and available.
   - Mark unavailable SDK-specific fields as `TBD`; do not infer hidden transcript state.

6. Implement Stop/finalization mapping.
   - Record finalization evidence associated with the relevant session and turn.
   - Preserve the existing terminal event contract: accepted turns end with success, failure, cancellation, or interruption evidence.
   - Avoid duplicate or contradictory terminal outcomes.

7. Integrate with append-only session event storage.
   - Append JSONL events in write sequence with unique event IDs.
   - Keep replay tolerant of malformed trailing lines as required by the session event contract.
   - Store large or sensitive payloads as session artifacts or redact them according to policy.
   - BLOCKER: the event writer and session artifact API call paths must be cited from the owning PKG-05/PKG-03 surfaces before implementation closure; exact call path is TBD.

8. Add tests and fixtures.
   - Add hook lifecycle mapper tests for start, completion, and failure outcomes.
   - Add `context.compacted` tests for boundary persistence and replay implications.
   - Add terminal hook fixtures for Stop/finalization behavior.
   - Add redaction or payload-budget checks for hook/compaction payloads.
   - Include Section 9 validation linkage for `section9.context_compaction_boundary` where the validation runner expects it.

9. Record residual gaps and source warnings.
   - Keep exact module paths, fixture names, payload fields, and event linkage policy as `TBD` until implementation assigns them.
   - Record the `docs/PRD.md` HASH_MISMATCH warning anywhere PRD-only compaction payload details are used.

## Verification

| Check | Expected result |
|---|---|
| Event schema | Hook, compaction, and terminal mirror events conform to `HarnessEvent`. |
| Event append behavior | Events append as newline-delimited JSONL in order with unique event IDs. |
| Product-owned names | Persisted event types use Chirality names, with SDK details only in adapter metadata. |
| Hook start | Supported hook execution emits or stages `hook.started` evidence. |
| Hook completion/failure | Supported hook completion records outcome; failures preserve fail-closed semantics for write, shell, domain, and subagent actions. |
| Compaction boundary | SDK/model compaction boundary emits `context.compacted` when available. |
| Replay preservation | Full Chirality event replay remains possible after compaction without relying on SDK transcript as canonical truth. |
| Stop/finalization | Finalization evidence aligns with exactly one durable terminal outcome for the accepted turn. |
| Redaction and payload budget | Secrets are absent and large payloads are artifact-referenced or redacted. |
| PRD warning | PRD-derived payload specifics remain traceable to `_REFERENCES.md` HASH_MISMATCH until reconciled. |

## Records

- Hook lifecycle mapper implementation path: TBD.
- Event schema or mapper test path: TBD.
- `context.compacted` test path: TBD.
- Terminal hook fixture path: TBD.
- Session event replay validation evidence: TBD.
- Redaction/payload-budget validation evidence: TBD.
- Review note for PRD HASH_MISMATCH: required until REF-006 source state is reconciled.
- Dependency-closure note: human-declared upstream dependency status is TBD; extracted ACTIVE edges in `_DEPENDENCIES.md` must be reconciled before closure.

## Pass 3 Disposition

| ItemID | Disposition | Evidence reread |
|---|---|---|
| D-001 | Converted to a dependency-closure blocker: the deliverable is not asserted dependency-free; human-declared edges remain `TBD`, while extracted ACTIVE upstream edges require closure review. | `_DEPENDENCIES.md` Declared Upstream and Extracted Dependency Register |
| D-002 | Rejected as an implementation assumption and replaced with a blocker: event writer/session artifact APIs must be cited from PKG-05/PKG-03 ownership before closure. | `docs/SPEC.md` Sections 8.4 and 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-4 through K-EVENT-7 |
| E-002 | Incorporated as an explicit records and verification obligation for redaction or payload-budget validation evidence on hook and compaction payloads; evidence path remains `TBD`. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` Section 1.5 K-EVENT-6 and K-EVENT-7 |
