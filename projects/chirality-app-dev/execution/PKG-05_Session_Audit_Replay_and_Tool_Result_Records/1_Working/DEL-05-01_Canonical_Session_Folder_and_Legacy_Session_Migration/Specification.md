# Specification: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Scope

DEL-05-01 specifies the session data-model change that makes folder-backed harness sessions canonical and converts legacy flat `.json` session records into that shape on first touch.

In scope:

- Canonical `.chirality/sessions/<sessionId>/` folder layout.
- `session.json` metadata expectations.
- Legacy `.chirality/sessions/<sessionId>.json` conversion during read, list, resume, save, and delete surfaces.
- SDK session linkage metadata needed for resume without making SDK transcripts authoritative.
- Tests for session folder layout, migration helpers, duplicate folder/flat behavior, and legacy conversion behavior.

Out of scope:

- `HarnessEvent` schema and append-only JSONL writer details owned by DEL-05-02.
- Runtime redaction owned by DEL-05-03.
- Replay UI/diagnostics owned by DEL-05-04.
- Tool permission semantics, excluded by PKG-05 package scope.
- Final SDK transcript placement decision where source authority marks it as an R1/OI-002 decision.

Sources: `_CONTEXT.md` `Deliverable Scope`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-05`; `docs/SPEC.md` Sections 8-10; D-APP-41 ruling on canonical session storage.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-05-01-R001 | New canonical sessions MUST be represented as folders under `.chirality/sessions/<sessionId>/` or the configured `CHIRALITY_SESSION_ROOT` equivalent. | `docs/SPEC.md` Section 8.2 |
| DEL-05-01-R002 | A canonical session folder MUST support `session.json`, `events.jsonl`, `turns/`, `artifacts/`, and `sdk/` as the physical layout. | `docs/SPEC.md` Section 8.2 |
| DEL-05-01-R003 | Legacy flat records at `{sessionRoot}/{sessionId}.json` MUST be converted to `{sessionRoot}/{sessionId}/session.json` on first read/list/resume/save/delete access. | `docs/SPEC.md` Section 8.1; D-APP-41 |
| DEL-05-01-R004 | Existing `.chirality/sessions/*.json` records MUST list and resume by way of eager canonical conversion; runtime code MUST NOT keep flat records as a standing parallel storage shape. | `docs/PRD.md` FR-077; `docs/SPEC.md` Section 8.1; D-APP-41 |
| DEL-05-01-R005 | Session CRUD behavior MUST remain bound to normalized project root. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 |
| DEL-05-01-R006 | `session.json` SHOULD include stable Chirality session metadata and SDK linkage metadata listed in SPEC Section 8.3. | `docs/SPEC.md` Section 8.3 |
| DEL-05-01-R007 | SDK session identifiers and transcript/store references MUST remain adapter metadata and MUST NOT redefine Chirality session identity. | `docs/SPEC.md` Section 10.3; `docs/TYPES.md` Section 7.2; `docs/CONTRACT.md` K-ENGINE-4 |
| DEL-05-01-R008 | `events.jsonl` MUST remain the canonical Chirality audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4 |
| DEL-05-01-R009 | If SDK transcript storage remains outside the working root, Chirality MUST cross-reference the transcript path or store key from `session.json` and record residual reliance-boundary risk. | `docs/SPEC.md` Section 8.4 |
| DEL-05-01-R010 | If both canonical folder and legacy flat records exist for the same `sessionId`, resolution MUST prefer defined canonical values, preserve legacy-only fields, write the merged canonical `session.json`, and remove the flat record. | D-APP-41; `docs/SPEC.md` Section 8.1 |
| DEL-05-01-R011 | Session identifiers MUST remain stable across renames, path changes, and UI labels. | `docs/TYPES.md` Section 2; `docs/CONTRACT.md` K-ID-1 |
| DEL-05-01-R012 | Runtime records and project files MUST preserve stable IDs when paths change. | `docs/CONTRACT.md` K-PATH-1 |
| DEL-05-01-R013 | Secrets and API keys MUST NOT be stored in session metadata, runtime events, logs, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; K-EVENT-6 |
| DEL-05-01-R014 | `CHIRALITY_SESSION_ROOT` override behavior MUST remain supported for session storage root resolution. | `docs/SPEC.md` Section 8.2; `docs/PRD.md` session storage section |
| DEL-05-01-R015 | Implementation evidence MUST name the active session storage module, canonicalization helper behavior, and focused validation commands used for closure. | D-APP-41; implementation evidence |
| DEL-05-01-R016 | New sessions MUST NOT write legacy flat `{sessionId}.json` files. | D-APP-41; `docs/SPEC.md` Section 8.2 |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| SPEC Harness Session Store | Defines legacy record shape, canonical folder layout, future metadata, and canonicalization rules. | `docs/SPEC.md` Section 8 |
| SPEC Runtime Event Schema | Constrains `events.jsonl` canonicality and replay tolerance where the session folder contains event logs. | `docs/SPEC.md` Section 9 |
| SPEC Engine Adapter Rules | Requires SDK names, IDs, transcript paths, and external message names to remain adapter metadata. | `docs/SPEC.md` Section 10.3 |
| TYPES Runtime and Session Vocabulary | Defines `SessionRecord`, `sessionId`, `sdkSessionId`, `events.jsonl`, `session.json`, and `artifacts/`. | `docs/TYPES.md` Section 7 |
| CONTRACT Invariants | Governs stable identity, project truth, SDK transcript secondary status, event mirror canonicality, replay tolerance, and redaction. | `docs/CONTRACT.md` K-ID-1, K-FS-1, K-SDK-3, K-EVENT-4 through K-EVENT-6 |
| PRD Runtime Requirements | Product requirements for session CRUD, legacy readability, SDK linkage, and audit mirror canonicality. | `docs/PRD.md` FR-014, FR-077, FR-118, FR-121; D-APP-38 corpus v2 reports MATCH |

## Verification

| Requirement IDs | Verification Approach |
|---|---|
| R001, R002, R006, R014 | Unit tests for session root resolution and canonical folder creation, including `CHIRALITY_SESSION_ROOT`. |
| R003, R004, R005, R010, R016 | Legacy fixture tests proving flat `.json` records are converted through list, retrieve, resume, save, and delete surfaces; duplicate fixture tests proving merge precedence, legacy-only field preservation, and flat-file removal. |
| R007, R008, R009 | Metadata tests proving SDK identifiers/transcript references are stored as adapter metadata and `events.jsonl` remains canonical. |
| R011, R012 | Tests or scanner checks proving `sessionId` is the persisted identity and not inferred from path labels alone. |
| R013 | Redaction/security tests proving secret-like values are not written to session metadata or referenced artifacts; detailed redaction implementation belongs to DEL-05-03. |
| R015 | Review check that implementation-specific file paths, helper behavior, and command names are recorded in ADQ-08 evidence. |
| A-001 | Review check that save/update behavior remains an internal session-manager persistence operation unless a separate public API is accepted. |
| B-001 | Review check that legacy `claudeSessionId` remains readable without being silently redefined as `sdkSessionId`. |
| F-001 | Review check that duplicate folder-versus-flat behavior follows D-APP-41 and is fixture-tested. |
| E-002 | Review check that any external SDK transcript path/store-key use has an explicit residual reliance-boundary note; no final transcript placement claim is made in DEL-05-01. |

## Documentation

Required artifacts:

- Session folder layout specification or implementation note.
- Migration helper description covering eager legacy flat `.json` conversion.
- Legacy-read/list/resume/save/delete conversion test fixtures.
- Duplicate folder/flat merge and cleanup test fixture.
- `session.json` metadata field documentation.
- SDK transcript/linkage residual-risk note where placement remains unresolved.
- Test evidence for session root override behavior.
- Implementation evidence for save/update behavior, duplicate folder-versus-flat behavior, and `claudeSessionId` preservation.
- Source-state recheck confirming the D-APP-38 authority corpus is current for this deliverable.

Source: `_CONTEXT.md` `Anticipated Artifacts`; `docs/SPEC.md` Section 8; `docs/PLAN.md` R1/R2 notes.
