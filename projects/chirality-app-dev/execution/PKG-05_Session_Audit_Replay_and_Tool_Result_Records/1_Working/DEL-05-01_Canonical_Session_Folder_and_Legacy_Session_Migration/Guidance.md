# Guidance: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Purpose

This deliverable gives Chirality a forward-compatible session storage shape without breaking existing harness sessions. The main design pressure is to move from legacy flat `.json` records to folder-backed sessions while keeping runtime audit authority with Chirality-owned `events.jsonl`, not SDK transcripts or hidden state.

Sources: `_CONTEXT.md` `Deliverable Scope`; `docs/SPEC.md` Section 8; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

## Principles

1. Preserve session identity.
   `sessionId` is a stable identifier. Do not make folder names, UI labels, SDK session IDs, or transcript paths the authoritative identity. Source: `docs/TYPES.md` Section 2; `docs/CONTRACT.md` K-ID-1.

2. Prefer additive migration.
   Canonical folder sessions can be introduced while legacy flat records remain readable. Conversion should not delete or rewrite legacy records until list/resume/retrieve/delete behavior and validation scripts are explicitly migrated. Source: `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077. The non-destructive migration posture is an ASSUMPTION.

3. Keep Chirality audit canonical.
   `events.jsonl` is the product-owned audit mirror. SDK transcripts can assist resume/debugging but are secondary unless imported into `HarnessEvent` form. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

4. Separate metadata from provider state.
   `sdkSessionId`, transcript paths, store keys, SDK config directories, settings sources, and SDK versions are adapter metadata. They should help resume and diagnosis without shaping public APIs or canonical event semantics. Source: `docs/SPEC.md` Sections 8.3 and 10.3; `docs/TYPES.md` Section 7.2.

5. Treat PRD-only details cautiously for this run.
   `_REFERENCES.md` reports a `HASH_MISMATCH` for `docs/PRD.md`. PRD requirements are still useful local context, but unsupported implementation details from PRD should remain `TBD`, `ASSUMPTION`, or `PROPOSAL` until corroborated.

## Considerations

- The layout should serve later PKG-05 deliverables: `events.jsonl` for DEL-05-02, replay support for DEL-05-04, and artifacts for DEL-05-05. Do not overload DEL-05-01 with those implementations.
- Legacy records include `claudeSessionId`; vNext metadata uses `sdkSessionId` and related SDK linkage fields. Exact field mapping is TBD because the source set does not specify a migration transform.
- `CHIRALITY_SESSION_ROOT` changes the storage root. Tests should cover both default and override roots.
- Session CRUD is source-supported, but route-level save/update semantics are less explicit than create/list/get/delete. Treat "save" behavior as TBD unless current code or a later accepted spec defines it.
- Transcript placement remains an R1/OI-002 decision. A migration implementation should be able to record transcript path/store-key metadata without assuming the final storage mechanism.
- Redaction requirements apply to metadata and artifacts, but detailed redaction behavior belongs to DEL-05-03.

## Trade-offs

| Option | Benefit | Cost / Risk | Guidance |
|---|---|---|---|
| Lazy legacy read support | Minimal migration risk; existing sessions remain usable | Code must handle two storage shapes during transition | Prefer unless a human-approved migration plan requires eager conversion |
| Eager conversion to folders | Simplifies later reader code | Risks destructive migration and field-loss without accepted mapping | Do not require in this deliverable without additional source authority |
| Store SDK transcript under working-root-controlled folder | Better locality and governance review | SDK behavior must be empirically verified | Preferred direction when reliable; source marks it as R1 decision |
| Cross-reference SDK transcript in user home | Preserves resume if SDK cannot be redirected | Adds reliance-boundary risk and non-project state dependency | Accept only with explicit `session.json` metadata and residual-risk record |
| Keep `events.jsonl` as canonical audit mirror | Preserves Chirality-owned runtime evidence | Requires event writer/replay discipline | Required by SPEC and CONTRACT |

## Examples

Canonical folder example:

```text
.chirality/sessions/sess_example/
|-- session.json
|-- events.jsonl
|-- turns/
|   `-- turn_example.json
|-- artifacts/
`-- sdk/
```

Legacy flat record example:

```text
.chirality/sessions/sess_example.json
```

`session.json` should keep SDK linkage separate from Chirality identity:

```json
{
  "sessionId": "sess_example",
  "projectRoot": "/path/to/working-root",
  "persona": "HELP_HUMAN",
  "mode": "WORKBENCH",
  "sdkSessionId": "TBD",
  "sdkTranscriptPath": "TBD",
  "sdkSessionStoreKey": "TBD"
}
```

Example is illustrative only; exact field optionality and migration helper names are TBD. Source: `docs/SPEC.md` Section 8.3.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| DEL-05-01-C001 | Session "save" is listed in SOW/PRD session operations, while SPEC endpoint list explicitly names create, boot, list, get/delete, turn, and interrupt but not a separate save endpoint. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 | `docs/SPEC.md` API endpoint table | `Specification.md` Verification; `Procedure.md` Steps | Treat save/update semantics as TBD and verify against implementation or later accepted spec before coding. | TBD |

## Source-State Notes

- `docs/PRD.md` is marked `HASH_MISMATCH` in `_REFERENCES.md`; PRD-derived requirements are cited but should be revalidated before implementation lock-in.
- `docs/PLAN.md` names likely implementation artifacts such as `session-events.ts` and `sdk-session-link.ts`, but this deliverable does not yet have accepted implementation paths. Keep exact paths as `TBD` unless code inspection in an implementation task confirms them.
