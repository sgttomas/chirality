# Procedure: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Purpose

Provide an operational procedure for producing and verifying the DEL-05-01 implementation slice: canonical session folder layout plus legacy flat `.json` compatibility for list, resume, retrieve, and delete behavior.

Source: `_CONTEXT.md` `Deliverable Scope`; `docs/SPEC.md` Section 8; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-05-01.

## Prerequisites

- Accepted DEL-05-01 scope and four-document kit.
- Access to `docs/SPEC.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/PLAN.md`, and `docs/PRD.md`.
- Awareness that `docs/PRD.md` has a `HASH_MISMATCH` in `_REFERENCES.md`; PRD-only implementation details require caution.
- Current session storage implementation and tests located by the implementation worker. Exact paths are TBD.
- Upstream dependency edges are not yet accepted; `_DEPENDENCIES.md` declares upstream/downstream as TBD.
- R1/OI-002 transcript placement remains unresolved; do not hard-code final SDK transcript storage policy beyond metadata support.

## Steps

1. Locate current session storage code and fixtures.
   - Identify where legacy `.chirality/sessions/<sessionId>.json` records are created, listed, read, resumed, and deleted.
   - Preserve current API compatibility unless an accepted runtime contract says otherwise.
   - Source basis: `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-014 and FR-077.

2. Define or update the session root resolver.
   - Resolve default `.chirality/sessions`.
   - Preserve `CHIRALITY_SESSION_ROOT` override behavior.
   - Normalize project-root filtering where session list behavior depends on project root.
   - Source basis: `docs/SPEC.md` Section 8.2; `docs/PRD.md` FR-014.

3. Introduce canonical folder creation for new sessions.
   - Create `.chirality/sessions/<sessionId>/`.
   - Write or prepare `session.json`.
   - Ensure `events.jsonl`, `turns/`, `artifacts/`, and `sdk/` are represented according to implementation needs.
   - Do not make SDK transcript files canonical.
   - Source basis: `docs/SPEC.md` Sections 8.2 and 8.4.

4. Populate `session.json` with supported metadata.
   - Include stable Chirality metadata such as `sessionId`, `projectRoot`, `persona`, `mode`, timestamps, model, and boot fingerprint when available.
   - Include SDK linkage metadata such as `sdkSessionId`, transcript path/store key, config dir, settings sources, SDK package version, Claude Code version, and resume mode when available.
   - Leave unavailable fields absent or `TBD` per implementation convention; do not invent values.
   - Source basis: `docs/SPEC.md` Section 8.3.

5. Add dual-shape read/list logic.
   - Folder sessions read from `<sessionId>/session.json`.
   - Legacy sessions read from `<sessionId>.json`.
   - Listing should include both shapes and avoid duplicate records for the same stable `sessionId`.
   - Duplicate-resolution policy is TBD if both a folder and flat record exist for the same `sessionId`.
   - Source basis: `docs/SPEC.md` Section 8.1; `docs/TYPES.md` Section 2.

6. Preserve resume compatibility.
   - Legacy `claudeSessionId` remains readable.
   - New SDK linkage should use `sdkSessionId` and explicit resume metadata when available.
   - Mapping from `claudeSessionId` to `sdkSessionId` is TBD unless accepted by implementation evidence.
   - Source basis: `docs/SPEC.md` Sections 8.1 and 8.3; `docs/PRD.md` FR-118.

7. Preserve retrieve and delete compatibility.
   - Retrieve should work for both folder and flat legacy records.
   - Delete should remove or retire the selected session shape according to current session policy.
   - If both shapes exist for the same `sessionId`, delete semantics are TBD and require human or design ruling before destructive behavior.
   - Source basis: `docs/SPEC.md` endpoint table; `docs/PRD.md` FR-014 and FR-077.

8. Keep event/audit canonicality intact.
   - Do not replace `.chirality/sessions/<sessionId>/events.jsonl` with SDK transcript data.
   - Cross-reference SDK transcript path/store key in metadata if needed.
   - Record residual reliance-boundary risk if SDK transcript storage remains outside a project-controlled folder.
   - Source basis: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

9. Add migration helper tests.
   - Test canonical folder creation.
   - Test legacy flat record listing.
   - Test legacy resume metadata remains available.
   - Test legacy retrieve/delete behavior.
   - Test root override behavior.
   - Test duplicate-shape behavior once policy is accepted. D-001 remains open until this accepted policy exists.
   - Source basis: `_CONTEXT.md` `Anticipated Artifacts`; `docs/SPEC.md` Section 19.3.

10. Re-run relevant local validation.
    - Run focused unit/API tests for session CRUD and migration helpers.
    - Run broader harness validation if this implementation changes runtime behavior.
    - Exact command names are TBD until the implementation worker confirms project scripts.
    - Source basis: `docs/SPEC.md` Section 19.3; `docs/PRD.md` FR-064 through FR-069.

## Verification

| Check | Expected Result |
|---|---|
| Canonical layout creation | New sessions have the folder shape required by `docs/SPEC.md` Section 8.2. |
| Legacy list compatibility | Existing `.chirality/sessions/*.json` records appear in session list output. |
| Legacy resume compatibility | Legacy records retain enough metadata to resume or report resume limitations without crashing. |
| Legacy retrieve/delete compatibility | Existing flat records can be retrieved and deleted through supported session surfaces. |
| SDK linkage metadata | SDK IDs/transcript references are adapter metadata and do not redefine Chirality `sessionId`. |
| Audit mirror canonicality | `events.jsonl` remains the product-owned audit mirror. |
| Redaction posture | Session metadata and artifacts do not store API keys or known secrets. |
| Source-state warning | PRD-derived behavior affected by `HASH_MISMATCH` is rechecked before implementation closure. |

## Pass 3 Evidence Checks

| ItemID | Check | Expected handling |
|---|---|---|
| C-001 | Implementation worker identifies current session storage source files and focused test commands. | Keep paths and commands `TBD` until code inspection confirms them. |
| D-001 | Duplicate-shape test exists after duplicate policy is accepted. | Do not close this branch without an accepted duplicate folder/flat policy and evidence. |
| E-001 | PRD-derived behavior is rechecked against REF-006 source state before closure. | Record the recheck result in implementation evidence; keep PRD-only details provisional until corroborated. |
| F-001 | Delete behavior is verified when both folder and flat records exist for the same `sessionId`. | Require human or design ruling before destructive behavior. |

## Records

- Updated source files for session root resolution, canonical folder layout, and migration helpers: TBD.
- Legacy flat-session fixtures: TBD.
- Canonical folder-session fixtures: TBD.
- Test results for list/resume/retrieve/delete migration behavior: TBD.
- Residual-risk note for SDK transcript placement if not project-controlled: TBD.
- Human ruling for duplicate folder/flat record delete semantics: TBD.
- Source-state recheck record for REF-006 PRD-derived behavior: TBD.
