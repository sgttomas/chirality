---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-01
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-009, SOW-043, SOW-046]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-01` in service of project scope [SOW-009, SOW-043, SOW-046] and package objectives [OBJ-003].

- **OUT-001** — A canonical folder-backed Chirality session store and first-touch legacy flat-record migration that preserve stable session identity and the product-owned audit boundary.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-05-01 Canonical Session Folder and Legacy Session Migration

> #### Datasheet: DEL-05-01 Canonical Session Folder and Legacy Session Migration
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-05-01 |
> | DeliverableName | Canonical Session Folder and Legacy Session Migration |
> | PackageID | PKG-05 |
> | PackageName | Session Audit, Replay, and Tool Result Records |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ResponsibleParty | TBD |
> | Type | DATA_MODEL_CHANGE |
> | ContextEnvelope | M |
> | Scope Items | SOW-009, SOW-043, SOW-046 |
> | Objective | OBJ-003 |
>
> Source: `_CONTEXT.md` `Identity`, `Traceability`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-05`.
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Canonical session root | `.chirality/sessions/<sessionId>/` unless `CHIRALITY_SESSION_ROOT` overrides the root | `docs/SPEC.md` Section 8.2; `docs/PRD.md` session storage section |
> | Canonical metadata file | `session.json` | `docs/SPEC.md` Section 8.2 |
> | Canonical event log | `events.jsonl` | `docs/SPEC.md` Section 8.2; `docs/CONTRACT.md` K-EVENT-4 |
> | Canonical per-turn folder | `turns/<turnId>.json` | `docs/SPEC.md` Section 8.2 |
> | Canonical artifact folder | `artifacts/` | `docs/SPEC.md` Section 8.2; `docs/TYPES.md` Section 7.2 |
> | Canonical SDK metadata/transcript folder | `sdk/` | `docs/SPEC.md` Section 8.2 |
> | Legacy record shape | `{sessionRoot}/{sessionId}.json` | `docs/SPEC.md` Section 8.1 |
> | Legacy conversion requirement | Legacy records must remain readable by converting to canonical folders on first touch | `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077; D-APP-41 |
> | Supported session operations in scope | create, list, resume, retrieve, save, delete | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 |
> | Legacy migration behavior in scope | Existing `.chirality/sessions/*.json` records are canonicalized during list/resume/retrieve/save/delete and removed after conversion | `docs/PRD.md` FR-077; D-APP-41 |
> | SDK transcript authority | SDK transcripts are secondary runtime state unless imported into `HarnessEvent` form | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Chirality audit mirror canonicality | `.chirality/sessions/<sessionId>/events.jsonl` remains the product-owned runtime audit mirror | `docs/SPEC.md` Section 8.4; `docs/TYPES.md` Section 1.8 |
> | Project truth boundary | Runtime transcripts, SDK transcripts, UI state, and caches are not project truth unless imported into governed files | `docs/TYPES.md` Section 1.7; `docs/CONTRACT.md` K-FS-1 |
> | Stable identity | Session, turn, and runtime event identifiers are stable IDs assigned once | `docs/TYPES.md` Section 2 |
> | SDK linkage | `sdkSessionId`, transcript path/store key, config dir, settings sources, SDK package version, Claude Code version, and resume mode are future metadata candidates | `docs/SPEC.md` Section 8.3 |
> | Transcript placement | TBD: R1 must empirically decide the least surprising SDK transcript/storage pattern | `docs/SPEC.md` Section 8.4; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-046/OI-002 |
> | Authority corpus state | D-APP-38 corpus v2 is applied for this deliverable; `_REFERENCES.md` reports MATCH for PRD/SPEC/TYPES/CONTRACT/PLAN | `_REFERENCES.md`; D-APP-38 |
>

### CLM-005 — Pass 3 Lensing Status

> ##### Pass 3 Lensing Status
>
> | ItemID | Status | Datasheet impact |
> |---|---|---|
> | X-001 | unresolved TBD | Transcript placement remains an R1/OI-002 decision; this datasheet does not treat SDK transcript storage as stable review closure. |
> | E-001 | satisfied | PRD-derived behavior was rechecked against the D-APP-38 corpus v2 MATCH state before ADQ-08 closure. |
>

### CLM-006 — Construction

> ##### Construction
>
> Canonical vNext session folder:
>
> ```text
> .chirality/sessions/<sessionId>/
> |-- session.json
> |-- events.jsonl
> |-- turns/
> |   `-- <turnId>.json
> |-- artifacts/
> `-- sdk/
> ```
>
> Source: `docs/SPEC.md` Section 8.2.
>
> Legacy session record:
>
> ```text
> {sessionRoot}/{sessionId}.json
> ```
>
> Legacy flat records are migration inputs only. On first read, list, resume, save,
> or delete access, the runtime writes `{sessionRoot}/{sessionId}/session.json`
> and removes the flat record. If both shapes exist, defined canonical values win,
> legacy-only fields are preserved, and the merged canonical record replaces the
> duplicate pair.
>
> Known legacy fields:
>
> - `sessionId`
> - `projectRoot`
> - `persona`
> - `mode`
> - `createdAt`
> - `updatedAt`
> - `claudeSessionId`
> - `bootFingerprint`
> - `bootedAt`
> - `model`
> - `engineSessionId`
> - `sdkSessionId`
> - `sdkTranscriptPath`
> - `sdkSessionStoreKey`
> - `sdkConfigDir`
> - `sdkSettingSources`
> - `sdkPackageVersion`
> - `sdkClaudeCodeVersion`
> - `runtimeFingerprint`
>
> Source: `docs/SPEC.md` Section 8.1.
>
> Future `session.json` fields should include:
>
> - `sessionId`
> - `projectRoot`
> - `persona`
> - `mode`
> - `createdAt`
> - `updatedAt`
> - `model`
> - `bootFingerprint`
> - `sdkSessionId`
> - `sdkProjectKey`
> - `sdkTranscriptPath` or `sdkSessionStoreKey`
> - `sdkConfigDir`
> - `sdkSettingSources`
> - `sdkPackageVersion`
> - `sdkClaudeCodeVersion`
> - `sdkResumeMode`
>
> Source: `docs/SPEC.md` Section 8.3.
>

### CLM-007 — References

> ##### References
>
> - `_CONTEXT.md` `Identity`, `Package Scope`, `Deliverable Scope`, `Traceability`
> - `_REFERENCES.md` `Authoritative Source Corpus`
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-05`, SOW-009, SOW-043, SOW-046, OBJ-003
> - `docs/SPEC.md` Sections 8-10 and 19.3
> - `docs/TYPES.md` Sections 1.7, 1.8, 2, and 7
> - `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-FS-1, K-SDK-3, K-EVENT-4, K-EVENT-5, K-EVENT-6
> - `docs/PLAN.md` R1/R2 implementation notes
> - `docs/PRD.md` session storage, FR-014, FR-077, FR-118, FR-121, FR-122, FR-123
> - D-APP-38 authority corpus v2
> - D-APP-41 canonical session storage ruling

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-05-01 Canonical Session Folder and Legacy Session Migration

> #### Specification: DEL-05-01 Canonical Session Folder and Legacy Session Migration
>

### CLM-009 — Scope

> ##### Scope
>
> DEL-05-01 specifies the session data-model change that makes folder-backed harness sessions canonical and converts legacy flat `.json` session records into that shape on first touch.
>
> In scope:
>
> - Canonical `.chirality/sessions/<sessionId>/` folder layout.
> - `session.json` metadata expectations.
> - Legacy `.chirality/sessions/<sessionId>.json` conversion during read, list, resume, save, and delete surfaces.
> - SDK session linkage metadata needed for resume without making SDK transcripts authoritative.
> - Tests for session folder layout, migration helpers, duplicate folder/flat behavior, and legacy conversion behavior.
>
> Out of scope:
>
> - `HarnessEvent` schema and append-only JSONL writer details owned by DEL-05-02.
> - Runtime redaction owned by DEL-05-03.
> - Replay UI/diagnostics owned by DEL-05-04.
> - Tool permission semantics, excluded by PKG-05 package scope.
> - Final SDK transcript placement decision where source authority marks it as an R1/OI-002 decision.
>
> Sources: `_CONTEXT.md` `Deliverable Scope`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-05`; `docs/SPEC.md` Sections 8-10; D-APP-41 ruling on canonical session storage.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-05-01-R001 | New canonical sessions MUST be represented as folders under `.chirality/sessions/<sessionId>/` or the configured `CHIRALITY_SESSION_ROOT` equivalent. | `docs/SPEC.md` Section 8.2 |
> | DEL-05-01-R002 | A canonical session folder MUST support `session.json`, `events.jsonl`, `turns/`, `artifacts/`, and `sdk/` as the physical layout. | `docs/SPEC.md` Section 8.2 |
> | DEL-05-01-R003 | Legacy flat records at `{sessionRoot}/{sessionId}.json` MUST be converted to `{sessionRoot}/{sessionId}/session.json` on first read/list/resume/save/delete access. | `docs/SPEC.md` Section 8.1; D-APP-41 |
> | DEL-05-01-R004 | Existing `.chirality/sessions/*.json` records MUST list and resume by way of eager canonical conversion; runtime code MUST NOT keep flat records as a standing parallel storage shape. | `docs/PRD.md` FR-077; `docs/SPEC.md` Section 8.1; D-APP-41 |
> | DEL-05-01-R005 | Session CRUD behavior MUST remain bound to normalized project root. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 |
> | DEL-05-01-R006 | `session.json` SHOULD include stable Chirality session metadata and SDK linkage metadata listed in SPEC Section 8.3. | `docs/SPEC.md` Section 8.3 |
> | DEL-05-01-R007 | SDK session identifiers and transcript/store references MUST remain adapter metadata and MUST NOT redefine Chirality session identity. | `docs/SPEC.md` Section 10.3; `docs/TYPES.md` Section 7.2; `docs/CONTRACT.md` K-ENGINE-4 |
> | DEL-05-01-R008 | `events.jsonl` MUST remain the canonical Chirality audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4 |
> | DEL-05-01-R009 | If SDK transcript storage remains outside the working root, Chirality MUST cross-reference the transcript path or store key from `session.json` and record residual reliance-boundary risk. | `docs/SPEC.md` Section 8.4 |
> | DEL-05-01-R010 | If both canonical folder and legacy flat records exist for the same `sessionId`, resolution MUST prefer defined canonical values, preserve legacy-only fields, write the merged canonical `session.json`, and remove the flat record. | D-APP-41; `docs/SPEC.md` Section 8.1 |
> | DEL-05-01-R011 | Session identifiers MUST remain stable across renames, path changes, and UI labels. | `docs/TYPES.md` Section 2; `docs/CONTRACT.md` K-ID-1 |
> | DEL-05-01-R012 | Runtime records and project files MUST preserve stable IDs when paths change. | `docs/CONTRACT.md` K-PATH-1 |
> | DEL-05-01-R013 | Secrets and API keys MUST NOT be stored in session metadata, runtime events, logs, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; K-EVENT-6 |
> | DEL-05-01-R014 | `CHIRALITY_SESSION_ROOT` override behavior MUST remain supported for session storage root resolution. | `docs/SPEC.md` Section 8.2; `docs/PRD.md` session storage section |
> | DEL-05-01-R015 | Implementation evidence MUST name the active session storage module, canonicalization helper behavior, and focused validation commands used for closure. | D-APP-41; implementation evidence |
> | DEL-05-01-R016 | New sessions MUST NOT write legacy flat `{sessionId}.json` files. | D-APP-41; `docs/SPEC.md` Section 8.2 |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | SPEC Harness Session Store | Defines legacy record shape, canonical folder layout, future metadata, and canonicalization rules. | `docs/SPEC.md` Section 8 |
> | SPEC Runtime Event Schema | Constrains `events.jsonl` canonicality and replay tolerance where the session folder contains event logs. | `docs/SPEC.md` Section 9 |
> | SPEC Engine Adapter Rules | Requires SDK names, IDs, transcript paths, and external message names to remain adapter metadata. | `docs/SPEC.md` Section 10.3 |
> | TYPES Runtime and Session Vocabulary | Defines `SessionRecord`, `sessionId`, `sdkSessionId`, `events.jsonl`, `session.json`, and `artifacts/`. | `docs/TYPES.md` Section 7 |
> | CONTRACT Invariants | Governs stable identity, project truth, SDK transcript secondary status, event mirror canonicality, replay tolerance, and redaction. | `docs/CONTRACT.md` K-ID-1, K-FS-1, K-SDK-3, K-EVENT-4 through K-EVENT-6 |
> | PRD Runtime Requirements | Product requirements for session CRUD, legacy readability, SDK linkage, and audit mirror canonicality. | `docs/PRD.md` FR-014, FR-077, FR-118, FR-121; D-APP-38 corpus v2 reports MATCH |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach |
> |---|---|
> | R001, R002, R006, R014 | Unit tests for session root resolution and canonical folder creation, including `CHIRALITY_SESSION_ROOT`. |
> | R003, R004, R005, R010, R016 | Legacy fixture tests proving flat `.json` records are converted through list, retrieve, resume, save, and delete surfaces; duplicate fixture tests proving merge precedence, legacy-only field preservation, and flat-file removal. |
> | R007, R008, R009 | Metadata tests proving SDK identifiers/transcript references are stored as adapter metadata and `events.jsonl` remains canonical. |
> | R011, R012 | Tests or scanner checks proving `sessionId` is the persisted identity and not inferred from path labels alone. |
> | R013 | Redaction/security tests proving secret-like values are not written to session metadata or referenced artifacts; detailed redaction implementation belongs to DEL-05-03. |
> | R015 | Review check that implementation-specific file paths, helper behavior, and command names are recorded in ADQ-08 evidence. |
> | A-001 | Review check that save/update behavior remains an internal session-manager persistence operation unless a separate public API is accepted. |
> | B-001 | Review check that legacy `claudeSessionId` remains readable without being silently redefined as `sdkSessionId`. |
> | F-001 | Review check that duplicate folder-versus-flat behavior follows D-APP-41 and is fixture-tested. |
> | E-002 | Review check that any external SDK transcript path/store-key use has an explicit residual reliance-boundary note; no final transcript placement claim is made in DEL-05-01. |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required artifacts:
>
> - Session folder layout specification or implementation note.
> - Migration helper description covering eager legacy flat `.json` conversion.
> - Legacy-read/list/resume/save/delete conversion test fixtures.
> - Duplicate folder/flat merge and cleanup test fixture.
> - `session.json` metadata field documentation.
> - SDK transcript/linkage residual-risk note where placement remains unresolved.
> - Test evidence for session root override behavior.
> - Implementation evidence for save/update behavior, duplicate folder-versus-flat behavior, and `claudeSessionId` preservation.
> - Source-state recheck confirming the D-APP-38 authority corpus is current for this deliverable.
>
> Source: `_CONTEXT.md` `Anticipated Artifacts`; `docs/SPEC.md` Section 8; `docs/PLAN.md` R1/R2 notes.
>

### CLM-014 — D-APP-56 guard amendment (2026-07-12)

> ##### D-APP-56 guard amendment (2026-07-12)
>
> R4-P31 adopts both session-manager guards into DEL-05-01: `assertSafeSessionId` prevents unsafe/path-traversing session identifiers, and `assertProjectRootAccessible` enforces accessible contained project roots. A dedicated session-ID guard test remains an explicit verification obligation; this text does not assert it exists.

- **AC-001** — Review and focused tests confirm that new sessions use the canonical folder layout and list, retrieve, resume, save, and delete operations convert legacy flat records while preserving stable session identity and defined duplicate-record precedence.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-05-01 Canonical Session Folder and Legacy Session Migration

> #### Procedure: DEL-05-01 Canonical Session Folder and Legacy Session Migration
>

### CLM-016 — Purpose

> ##### Purpose
>
> Provide an operational procedure for producing and verifying the DEL-05-01 implementation slice: canonical session folder layout plus eager legacy flat `.json` conversion for list, resume, retrieve, save, and delete behavior.
>
> Source: `_CONTEXT.md` `Deliverable Scope`; `docs/SPEC.md` Section 8; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-05-01.
>

### CLM-017 — Prerequisites

> ##### Prerequisites
>
> - Accepted DEL-05-01 scope and four-document kit.
> - Access to `docs/SPEC.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/PLAN.md`, and `docs/PRD.md`.
> - Awareness that the D-APP-38 authority corpus is current for this deliverable; `_REFERENCES.md` reports matching hashes for PRD/SPEC/TYPES/CONTRACT/PLAN.
> - Current session storage implementation is `frontend/src/lib/harness/session-manager.ts`; focused storage tests are `frontend/src/__tests__/lib/session-manager.test.ts`.
> - Upstream dependency edges are not yet accepted; `_DEPENDENCIES.md` declares upstream/downstream as TBD.
> - R1/OI-002 transcript placement remains unresolved; do not hard-code final SDK transcript storage policy beyond metadata support.
>

### CLM-018 — Steps

> ##### Steps
>
> 1. Locate current session storage code and fixtures.
>    - Identify where legacy `.chirality/sessions/<sessionId>.json` records are created, listed, read, resumed, and deleted.
>    - Keep the public session API contract stable while changing the on-disk storage shape.
>    - Source basis: `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-014 and FR-077.
>
> 2. Define or update the session root resolver.
>    - Resolve default `.chirality/sessions`.
>    - Preserve `CHIRALITY_SESSION_ROOT` override behavior.
>    - Normalize project-root filtering where session list behavior depends on project root.
>    - Source basis: `docs/SPEC.md` Section 8.2; `docs/PRD.md` FR-014.
>
> 3. Introduce canonical folder creation for new sessions.
>    - Create `.chirality/sessions/<sessionId>/`.
>    - Write `session.json` for new session metadata.
>    - Do not write a legacy flat `{sessionId}.json` file for new sessions.
>    - Ensure `events.jsonl`, `turns/`, `artifacts/`, and `sdk/` remain compatible with the canonical folder layout according to implementation needs.
>    - Do not make SDK transcript files canonical.
>    - Source basis: `docs/SPEC.md` Sections 8.2 and 8.4.
>
> 4. Populate `session.json` with supported metadata.
>    - Include stable Chirality metadata such as `sessionId`, `projectRoot`, `persona`, `mode`, timestamps, model, and boot fingerprint when available.
>    - Include SDK linkage metadata such as `sdkSessionId`, transcript path/store key, config dir, settings sources, SDK package version, Claude Code version, and resume mode when available.
>    - Leave unavailable fields absent or `TBD` per implementation convention; do not invent values.
>    - Source basis: `docs/SPEC.md` Section 8.3.
>
> 5. Add canonicalizing read/list logic.
>    - Folder sessions read from `<sessionId>/session.json`.
>    - Legacy sessions are read from `<sessionId>.json`, immediately written to `<sessionId>/session.json`, and then removed as flat records.
>    - Listing should discover both shapes, canonicalize legacy records, and avoid duplicate records for the same stable `sessionId`.
>    - If both shapes exist, defined canonical values take precedence, legacy-only fields are preserved, the merged canonical file is written, and the flat record is removed.
>    - Source basis: `docs/SPEC.md` Section 8.1; `docs/TYPES.md` Section 2; D-APP-41.
>
> 6. Preserve resume compatibility.
>    - Legacy `claudeSessionId` remains readable.
>    - New SDK linkage should use `sdkSessionId` and explicit resume metadata when available.
>    - Do not silently map `claudeSessionId` to `sdkSessionId`; preserve legacy linkage fields and record new SDK linkage separately when available.
>    - Source basis: `docs/SPEC.md` Sections 8.1 and 8.3; `docs/PRD.md` FR-118.
>
> 7. Preserve retrieve and delete compatibility.
>    - Retrieve should work for folder and flat legacy inputs by canonicalizing first.
>    - Delete should resolve the session shape, then remove the canonical session folder and any stray flat duplicate for the same `sessionId`.
>    - Source basis: `docs/SPEC.md` endpoint table; `docs/PRD.md` FR-014 and FR-077; D-APP-41.
>
> 8. Keep event/audit canonicality intact.
>    - Do not replace `.chirality/sessions/<sessionId>/events.jsonl` with SDK transcript data.
>    - Cross-reference SDK transcript path/store key in metadata if needed.
>    - Record residual reliance-boundary risk if SDK transcript storage remains outside a project-controlled folder.
>    - Source basis: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.
>
> 9. Add migration helper tests.
>    - Test canonical folder creation.
>    - Test legacy flat record listing and canonical conversion.
>    - Test legacy resume metadata remains available after conversion.
>    - Test legacy retrieve/save/delete behavior.
>    - Test root override behavior.
>    - Test duplicate-shape behavior under D-APP-41 canonical-precedence merge and flat-file cleanup.
>    - Source basis: `_CONTEXT.md` `Anticipated Artifacts`; `docs/SPEC.md` Section 19.3.
>
> 10. Re-run relevant local validation.
>    - Run focused unit/API tests for session CRUD and migration helpers.
>    - Run broader harness validation because this implementation changes runtime storage behavior.
>    - Confirm TypeScript and authority-corpus status before closeout.
>     - Source basis: `docs/SPEC.md` Section 19.3; `docs/PRD.md` FR-064 through FR-069.
>

### CLM-019 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | Canonical layout creation | New sessions have the folder shape required by `docs/SPEC.md` Section 8.2. |
> | Legacy list conversion | Existing `.chirality/sessions/*.json` records appear in session list output and are converted to canonical folders. |
> | Legacy resume conversion | Legacy records retain metadata and are converted without crashing. |
> | Legacy retrieve/save/delete conversion | Existing flat records can be retrieved, saved, and deleted through supported session surfaces after canonicalization. |
> | Duplicate-shape cleanup | Duplicate folder/flat records merge with canonical precedence, preserve legacy-only fields, and remove the flat record. |
> | SDK linkage metadata | SDK IDs/transcript references are adapter metadata and do not redefine Chirality `sessionId`. |
> | Audit mirror canonicality | `events.jsonl` remains the product-owned audit mirror. |
> | Redaction posture | Session metadata and artifacts do not store API keys or known secrets. |
> | Source-state recheck | PRD-derived behavior is checked against the D-APP-38 corpus v2 MATCH state before implementation closure. |
>

### CLM-020 — Pass 3 Evidence Checks

> ##### Pass 3 Evidence Checks
>
> | ItemID | Check | Expected handling |
> |---|---|---|
> | C-001 | Implementation worker identifies current session storage source files and focused test commands. | SATISFIED by ADQ-08 evidence: `session-manager.ts`, `session-manager.test.ts`, focused route/event/turn tests, typecheck. |
> | D-001 | Duplicate-shape test exists after duplicate policy is accepted. | SATISFIED by D-APP-41 and `session-manager.test.ts` duplicate fixture. |
> | E-001 | PRD-derived behavior is rechecked against REF-006 source state before closure. | SATISFIED by D-APP-38 corpus v2 / `_REFERENCES.md` MATCH state and ADQ-08 status check. |
> | F-001 | Delete behavior is verified when both folder and flat records exist for the same `sessionId`. | SATISFIED by `session-manager.test.ts` delete fixture. |
>

### CLM-021 — Records

> ##### Records
>
> - Updated source files for session root resolution, canonical folder layout, and migration helpers: `frontend/src/lib/harness/session-manager.ts`.
> - Legacy flat-session fixtures: `frontend/src/__tests__/lib/session-manager.test.ts`.
> - Canonical folder-session fixtures: `frontend/src/__tests__/lib/session-manager.test.ts`.
> - Test results for list/resume/retrieve/save/delete migration behavior: `Evidence_ADQ-08_Canonical_Session_Migration.md`.
> - Residual-risk note for SDK transcript placement if not project-controlled: remains carried by R1/OI-002 and DEL-05-04; DEL-05-01 stores only metadata.
> - Human ruling for duplicate folder/flat record delete semantics: D-APP-41.
> - Source-state recheck record for REF-006 PRD-derived behavior: D-APP-38 corpus v2 MATCH state and ADQ-08 evidence.

- **VER-001** — Run focused session-manager tests for canonical creation, legacy conversion across supported operations, duplicate merge and cleanup, root override, stable identity, SDK metadata separation, and unsafe session-ID traversal guards; review the resulting evidence against SOW-009, SOW-043, SOW-046, and OBJ-003.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-05-01 Canonical Session Folder and Legacy Session Migration

> #### Guidance: DEL-05-01 Canonical Session Folder and Legacy Session Migration
>

### CLM-023 — Purpose

> ##### Purpose
>
> This deliverable gives Chirality one canonical session storage shape while still absorbing existing harness sessions. The main design pressure is to convert legacy flat `.json` records into folder-backed sessions and keep runtime audit authority with Chirality-owned `events.jsonl`, not SDK transcripts or hidden state.
>
> Sources: `_CONTEXT.md` `Deliverable Scope`; `docs/SPEC.md` Section 8; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.
>

### CLM-024 — Principles

> ##### Principles
>
> 1. Preserve session identity.
>    `sessionId` is a stable identifier. Do not make folder names, UI labels, SDK session IDs, or transcript paths the authoritative identity. Source: `docs/TYPES.md` Section 2; `docs/CONTRACT.md` K-ID-1.
>
> 2. Prefer one durable storage shape.
>    Canonical folder sessions are the target shape. Legacy flat records are inputs to eager conversion on list, read, resume, save, and delete, not a permanent parallel format. Source: `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077; D-APP-41.
>
> 3. Keep Chirality audit canonical.
>    `events.jsonl` is the product-owned audit mirror. SDK transcripts can assist resume/debugging but are secondary unless imported into `HarnessEvent` form. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.
>
> 4. Separate metadata from provider state.
>    `sdkSessionId`, transcript paths, store keys, SDK config directories, settings sources, and SDK versions are adapter metadata. They should help resume and diagnosis without shaping public APIs or canonical event semantics. Source: `docs/SPEC.md` Sections 8.3 and 10.3; `docs/TYPES.md` Section 7.2.
>
> 5. Preserve legacy metadata without redefining it.
>    Legacy `claudeSessionId` remains readable as legacy adapter linkage. New SDK linkage fields are recorded separately when available; migration must not silently rewrite one identity into another without accepted evidence.
>

### CLM-025 — Considerations

> ##### Considerations
>
> - The layout should serve later PKG-05 deliverables: `events.jsonl` for DEL-05-02, replay support for DEL-05-04, and artifacts for DEL-05-05. Do not overload DEL-05-01 with those implementations.
> - Legacy records include `claudeSessionId`; vNext metadata uses `sdkSessionId` and related SDK linkage fields. Preserve both when present unless an accepted transform is later defined.
> - `CHIRALITY_SESSION_ROOT` changes the storage root. Tests should cover both default and override roots.
> - Session CRUD is source-supported. In the current implementation, `FileSessionManager.save` is an internal persistence operation used by boot/session update flows; no separate public save route is created by this deliverable.
> - Transcript placement remains an R1/OI-002 decision. A migration implementation should be able to record transcript path/store-key metadata without assuming the final storage mechanism.
> - Redaction requirements apply to metadata and artifacts, but detailed redaction behavior belongs to DEL-05-03.
>

### CLM-026 — Pass 3 Rulings Needed

> ##### Pass 3 Rulings Needed
>
> | ItemID | Ruling needed | Interim guidance |
> |---|---|---|
> | A-001 | Whether session save/update is a distinct behavior or covered by create/boot/retrieve/delete surfaces. | Resolved for ADQ-08 by implementation evidence: keep `FileSessionManager.save` internal and do not add a public save route. |
> | B-001 | Whether legacy `claudeSessionId` maps directly to `sdkSessionId`. | Keep the legacy field readable and record new SDK linkage separately unless implementation evidence accepts a transform. |
> | F-001 | Duplicate folder-versus-flat behavior for the same stable `sessionId`. | Resolved by D-APP-41: canonical values win, legacy-only fields are preserved, and the flat record is removed after merge. |
> | X-001 | Final SDK transcript placement and review closure standard. | Keep SDK transcript path/store key as non-authoritative metadata while R1/OI-002 remains open. |
>

### CLM-027 — Trade-offs

> ##### Trade-offs
>
> | Option | Benefit | Cost / Risk | Guidance |
> |---|---|---|---|
> | Lazy legacy read support | Minimal migration risk; existing sessions remain usable | Code must handle two storage shapes indefinitely unless later cleanup occurs | Not selected after D-APP-41 |
> | Eager conversion to folders | Simplifies later reader code and eliminates the flat-record parallel format | Requires explicit duplicate merge and field-preservation tests | Selected by D-APP-41 |
> | Store SDK transcript under working-root-controlled folder | Better locality and governance review | SDK behavior must be empirically verified | Preferred direction when reliable; source marks it as R1 decision |
> | Cross-reference SDK transcript in user home | Preserves resume if SDK cannot be redirected | Adds reliance-boundary risk and non-project state dependency | Accept only with explicit `session.json` metadata and residual-risk record |
> | Keep `events.jsonl` as canonical audit mirror | Preserves Chirality-owned runtime evidence | Requires event writer/replay discipline | Required by SPEC and CONTRACT |
>
> E-002 disposition: when SDK transcripts remain outside project-controlled storage, the trade-off is acceptable only with `session.json` cross-reference metadata and a residual reliance-boundary record. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.
>

### CLM-028 — Examples

> ##### Examples
>
> Canonical folder example:
>
> ```text
> .chirality/sessions/sess_example/
> |-- session.json
> |-- events.jsonl
> |-- turns/
> |   `-- turn_example.json
> |-- artifacts/
> `-- sdk/
> ```
>
> Legacy flat record example:
>
> ```text
> .chirality/sessions/sess_example.json
> ```
>
> `session.json` should keep SDK linkage separate from Chirality identity:
>
> ```json
> {
>   "sessionId": "sess_example",
>   "projectRoot": "/path/to/working-root",
>   "persona": "HELP_HUMAN",
>   "mode": "WORKBENCH",
>   "sdkSessionId": "TBD",
>   "sdkTranscriptPath": "TBD",
>   "sdkSessionStoreKey": "TBD"
> }
> ```
>
> Example is illustrative only; exact field optionality remains implementation-owned. Source: `docs/SPEC.md` Section 8.3.
>

### CLM-029 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | DEL-05-01-C001 | Session "save" is listed in SOW/PRD session operations, while SPEC endpoint list explicitly names create, boot, list, get/delete, turn, and interrupt but not a separate save endpoint. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 | `docs/SPEC.md` API endpoint table | `Specification.md` Verification; `Procedure.md` Steps | Treat save/update as the implementation's internal `FileSessionManager.save` persistence operation unless a separate public save route is later accepted. | ADQ-08 implementation evidence |
>

### CLM-030 — Source-State Notes

> ##### Source-State Notes
>
> - `_REFERENCES.md` reports MATCH for the active authority corpus after the D-APP-38 corpus v2 refresh.
> - ADQ-08 code inspection identifies `frontend/src/lib/harness/session-manager.ts` as the storage implementation path and `frontend/src/__tests__/lib/session-manager.test.ts` as the focused migration fixture path.

### CLM-031 — D-APP-68 managed-delegation SessionRecord ownership (2026-07-19)

> ##### D-APP-68 managed-delegation SessionRecord ownership (2026-07-19)
>
> D-APP-68 ruling 3 assigns the optional managed-delegation fields persisted in
> `SessionRecord` to DEL-05-01. The owned optional metadata fields are:
> `orchestrationRunId`, `executionRoot`, `agentInstanceId`, `parentSessionId`,
> `parentInstanceId`, `parentAgentType`, `agentType`, `childKind`, `planVersion`,
> `approvalRef`, `instructionPath`, `instructionHash`, `briefHash`,
> `declaredContext`, `declaredTools`, `allowedWriteTargets`, `outputArtifact`,
> and `childRunStatus`.
>
> These fields record product-owned orchestration linkage alongside the existing
> session metadata. They are optional and do not redefine `sessionId`, canonical
> `.chirality/sessions/<sessionId>/session.json` placement, the Chirality audit
> mirror, legacy-flat-record conversion, or canonical-over-legacy merge
> precedence. Managed-child lifecycle and replayable child-run-record semantics
> remain owned by DEL-08-05; path enforcement remains owned by DEL-06-04.
>
> Source: D-APP-68 ruling 3; live contract evidence at
> `frontend/packages/harness-contract/src/types.ts` (`SessionRecord`).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-009 SOW-043 SOW-046 OBJ-003 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
