# Procedure: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Purpose

Provide an operational procedure for producing and verifying the DEL-05-01 implementation slice: canonical session folder layout plus eager legacy flat `.json` conversion for list, resume, retrieve, save, and delete behavior.

Source: `_CONTEXT.md` `Deliverable Scope`; `docs/SPEC.md` Section 8; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-05-01.

## Prerequisites

- Accepted DEL-05-01 scope and four-document kit.
- Access to `docs/SPEC.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/PLAN.md`, and `docs/PRD.md`.
- Awareness that the D-APP-38 authority corpus is current for this deliverable; `_REFERENCES.md` reports matching hashes for PRD/SPEC/TYPES/CONTRACT/PLAN.
- Current session storage implementation is `frontend/src/lib/harness/session-manager.ts`; focused storage tests are `frontend/src/__tests__/lib/session-manager.test.ts`.
- Upstream dependency edges are not yet accepted; `_DEPENDENCIES.md` declares upstream/downstream as TBD.
- R1/OI-002 transcript placement remains unresolved; do not hard-code final SDK transcript storage policy beyond metadata support.

## Steps

1. Locate current session storage code and fixtures.
   - Identify where legacy `.chirality/sessions/<sessionId>.json` records are created, listed, read, resumed, and deleted.
   - Keep the public session API contract stable while changing the on-disk storage shape.
   - Source basis: `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-014 and FR-077.

2. Define or update the session root resolver.
   - Resolve default `.chirality/sessions`.
   - Preserve `CHIRALITY_SESSION_ROOT` override behavior.
   - Normalize project-root filtering where session list behavior depends on project root.
   - Source basis: `docs/SPEC.md` Section 8.2; `docs/PRD.md` FR-014.

3. Introduce canonical folder creation for new sessions.
   - Create `.chirality/sessions/<sessionId>/`.
   - Write `session.json` for new session metadata.
   - Do not write a legacy flat `{sessionId}.json` file for new sessions.
   - Ensure `events.jsonl`, `turns/`, `artifacts/`, and `sdk/` remain compatible with the canonical folder layout according to implementation needs.
   - Do not make SDK transcript files canonical.
   - Source basis: `docs/SPEC.md` Sections 8.2 and 8.4.

4. Populate `session.json` with supported metadata.
   - Include stable Chirality metadata such as `sessionId`, `projectRoot`, `persona`, `mode`, timestamps, model, and boot fingerprint when available.
   - Include SDK linkage metadata such as `sdkSessionId`, transcript path/store key, config dir, settings sources, SDK package version, Claude Code version, and resume mode when available.
   - Leave unavailable fields absent or `TBD` per implementation convention; do not invent values.
   - Source basis: `docs/SPEC.md` Section 8.3.

5. Add canonicalizing read/list logic.
   - Folder sessions read from `<sessionId>/session.json`.
   - Legacy sessions are read from `<sessionId>.json`, immediately written to `<sessionId>/session.json`, and then removed as flat records.
   - Listing should discover both shapes, canonicalize legacy records, and avoid duplicate records for the same stable `sessionId`.
   - If both shapes exist, defined canonical values take precedence, legacy-only fields are preserved, the merged canonical file is written, and the flat record is removed.
   - Source basis: `docs/SPEC.md` Section 8.1; `docs/TYPES.md` Section 2; D-APP-41.

6. Preserve resume compatibility.
   - Legacy `claudeSessionId` remains readable.
   - New SDK linkage should use `sdkSessionId` and explicit resume metadata when available.
   - Do not silently map `claudeSessionId` to `sdkSessionId`; preserve legacy linkage fields and record new SDK linkage separately when available.
   - Source basis: `docs/SPEC.md` Sections 8.1 and 8.3; `docs/PRD.md` FR-118.

7. Preserve retrieve and delete compatibility.
   - Retrieve should work for folder and flat legacy inputs by canonicalizing first.
   - Delete should resolve the session shape, then remove the canonical session folder and any stray flat duplicate for the same `sessionId`.
   - Source basis: `docs/SPEC.md` endpoint table; `docs/PRD.md` FR-014 and FR-077; D-APP-41.

8. Keep event/audit canonicality intact.
   - Do not replace `.chirality/sessions/<sessionId>/events.jsonl` with SDK transcript data.
   - Cross-reference SDK transcript path/store key in metadata if needed.
   - Record residual reliance-boundary risk if SDK transcript storage remains outside a project-controlled folder.
   - Source basis: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

9. Add migration helper tests.
   - Test canonical folder creation.
   - Test legacy flat record listing and canonical conversion.
   - Test legacy resume metadata remains available after conversion.
   - Test legacy retrieve/save/delete behavior.
   - Test root override behavior.
   - Test duplicate-shape behavior under D-APP-41 canonical-precedence merge and flat-file cleanup.
   - Source basis: `_CONTEXT.md` `Anticipated Artifacts`; `docs/SPEC.md` Section 19.3.

10. Re-run relevant local validation.
   - Run focused unit/API tests for session CRUD and migration helpers.
   - Run broader harness validation because this implementation changes runtime storage behavior.
   - Confirm TypeScript and authority-corpus status before closeout.
    - Source basis: `docs/SPEC.md` Section 19.3; `docs/PRD.md` FR-064 through FR-069.

## Verification

| Check | Expected Result |
|---|---|
| Canonical layout creation | New sessions have the folder shape required by `docs/SPEC.md` Section 8.2. |
| Legacy list conversion | Existing `.chirality/sessions/*.json` records appear in session list output and are converted to canonical folders. |
| Legacy resume conversion | Legacy records retain metadata and are converted without crashing. |
| Legacy retrieve/save/delete conversion | Existing flat records can be retrieved, saved, and deleted through supported session surfaces after canonicalization. |
| Duplicate-shape cleanup | Duplicate folder/flat records merge with canonical precedence, preserve legacy-only fields, and remove the flat record. |
| SDK linkage metadata | SDK IDs/transcript references are adapter metadata and do not redefine Chirality `sessionId`. |
| Audit mirror canonicality | `events.jsonl` remains the product-owned audit mirror. |
| Redaction posture | Session metadata and artifacts do not store API keys or known secrets. |
| Source-state recheck | PRD-derived behavior is checked against the D-APP-38 corpus v2 MATCH state before implementation closure. |

## Pass 3 Evidence Checks

| ItemID | Check | Expected handling |
|---|---|---|
| C-001 | Implementation worker identifies current session storage source files and focused test commands. | SATISFIED by ADQ-08 evidence: `session-manager.ts`, `session-manager.test.ts`, focused route/event/turn tests, typecheck. |
| D-001 | Duplicate-shape test exists after duplicate policy is accepted. | SATISFIED by D-APP-41 and `session-manager.test.ts` duplicate fixture. |
| E-001 | PRD-derived behavior is rechecked against REF-006 source state before closure. | SATISFIED by D-APP-38 corpus v2 / `_REFERENCES.md` MATCH state and ADQ-08 status check. |
| F-001 | Delete behavior is verified when both folder and flat records exist for the same `sessionId`. | SATISFIED by `session-manager.test.ts` delete fixture. |

## Records

- Updated source files for session root resolution, canonical folder layout, and migration helpers: `frontend/src/lib/harness/session-manager.ts`.
- Legacy flat-session fixtures: `frontend/src/__tests__/lib/session-manager.test.ts`.
- Canonical folder-session fixtures: `frontend/src/__tests__/lib/session-manager.test.ts`.
- Test results for list/resume/retrieve/save/delete migration behavior: `Evidence_ADQ-08_Canonical_Session_Migration.md`.
- Residual-risk note for SDK transcript placement if not project-controlled: remains carried by R1/OI-002 and DEL-05-04; DEL-05-01 stores only metadata.
- Human ruling for duplicate folder/flat record delete semantics: D-APP-41.
- Source-state recheck record for REF-006 PRD-derived behavior: D-APP-38 corpus v2 MATCH state and ADQ-08 evidence.
