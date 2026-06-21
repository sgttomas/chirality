# Guidance: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Purpose

This deliverable gives Chirality one canonical session storage shape while still absorbing existing harness sessions. The main design pressure is to convert legacy flat `.json` records into folder-backed sessions and keep runtime audit authority with Chirality-owned `events.jsonl`, not SDK transcripts or hidden state.

Sources: `_CONTEXT.md` `Deliverable Scope`; `docs/SPEC.md` Section 8; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

## Principles

1. Preserve session identity.
   `sessionId` is a stable identifier. Do not make folder names, UI labels, SDK session IDs, or transcript paths the authoritative identity. Source: `docs/TYPES.md` Section 2; `docs/CONTRACT.md` K-ID-1.

2. Prefer one durable storage shape.
   Canonical folder sessions are the target shape. Legacy flat records are inputs to eager conversion on list, read, resume, save, and delete, not a permanent parallel format. Source: `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077; D-APP-41.

3. Keep Chirality audit canonical.
   `events.jsonl` is the product-owned audit mirror. SDK transcripts can assist resume/debugging but are secondary unless imported into `HarnessEvent` form. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

4. Separate metadata from provider state.
   `sdkSessionId`, transcript paths, store keys, SDK config directories, settings sources, and SDK versions are adapter metadata. They should help resume and diagnosis without shaping public APIs or canonical event semantics. Source: `docs/SPEC.md` Sections 8.3 and 10.3; `docs/TYPES.md` Section 7.2.

5. Preserve legacy metadata without redefining it.
   Legacy `claudeSessionId` remains readable as legacy adapter linkage. New SDK linkage fields are recorded separately when available; migration must not silently rewrite one identity into another without accepted evidence.

## Considerations

- The layout should serve later PKG-05 deliverables: `events.jsonl` for DEL-05-02, replay support for DEL-05-04, and artifacts for DEL-05-05. Do not overload DEL-05-01 with those implementations.
- Legacy records include `claudeSessionId`; vNext metadata uses `sdkSessionId` and related SDK linkage fields. Preserve both when present unless an accepted transform is later defined.
- `CHIRALITY_SESSION_ROOT` changes the storage root. Tests should cover both default and override roots.
- Session CRUD is source-supported. In the current implementation, `FileSessionManager.save` is an internal persistence operation used by boot/session update flows; no separate public save route is created by this deliverable.
- Transcript placement remains an R1/OI-002 decision. A migration implementation should be able to record transcript path/store-key metadata without assuming the final storage mechanism.
- Redaction requirements apply to metadata and artifacts, but detailed redaction behavior belongs to DEL-05-03.

## Pass 3 Rulings Needed

| ItemID | Ruling needed | Interim guidance |
|---|---|---|
| A-001 | Whether session save/update is a distinct behavior or covered by create/boot/retrieve/delete surfaces. | Resolved for ADQ-08 by implementation evidence: keep `FileSessionManager.save` internal and do not add a public save route. |
| B-001 | Whether legacy `claudeSessionId` maps directly to `sdkSessionId`. | Keep the legacy field readable and record new SDK linkage separately unless implementation evidence accepts a transform. |
| F-001 | Duplicate folder-versus-flat behavior for the same stable `sessionId`. | Resolved by D-APP-41: canonical values win, legacy-only fields are preserved, and the flat record is removed after merge. |
| X-001 | Final SDK transcript placement and review closure standard. | Keep SDK transcript path/store key as non-authoritative metadata while R1/OI-002 remains open. |

## Trade-offs

| Option | Benefit | Cost / Risk | Guidance |
|---|---|---|---|
| Lazy legacy read support | Minimal migration risk; existing sessions remain usable | Code must handle two storage shapes indefinitely unless later cleanup occurs | Not selected after D-APP-41 |
| Eager conversion to folders | Simplifies later reader code and eliminates the flat-record parallel format | Requires explicit duplicate merge and field-preservation tests | Selected by D-APP-41 |
| Store SDK transcript under working-root-controlled folder | Better locality and governance review | SDK behavior must be empirically verified | Preferred direction when reliable; source marks it as R1 decision |
| Cross-reference SDK transcript in user home | Preserves resume if SDK cannot be redirected | Adds reliance-boundary risk and non-project state dependency | Accept only with explicit `session.json` metadata and residual-risk record |
| Keep `events.jsonl` as canonical audit mirror | Preserves Chirality-owned runtime evidence | Requires event writer/replay discipline | Required by SPEC and CONTRACT |

E-002 disposition: when SDK transcripts remain outside project-controlled storage, the trade-off is acceptable only with `session.json` cross-reference metadata and a residual reliance-boundary record. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

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

Example is illustrative only; exact field optionality remains implementation-owned. Source: `docs/SPEC.md` Section 8.3.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| DEL-05-01-C001 | Session "save" is listed in SOW/PRD session operations, while SPEC endpoint list explicitly names create, boot, list, get/delete, turn, and interrupt but not a separate save endpoint. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 | `docs/SPEC.md` API endpoint table | `Specification.md` Verification; `Procedure.md` Steps | Treat save/update as the implementation's internal `FileSessionManager.save` persistence operation unless a separate public save route is later accepted. | ADQ-08 implementation evidence |

## Source-State Notes

- `_REFERENCES.md` reports MATCH for the active authority corpus after the D-APP-38 corpus v2 refresh.
- ADQ-08 code inspection identifies `frontend/src/lib/harness/session-manager.ts` as the storage implementation path and `frontend/src/__tests__/lib/session-manager.test.ts` as the focused migration fixture path.
