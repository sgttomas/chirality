# Specification: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Scope

DEL-05-01 specifies the session data-model change that introduces canonical folder-backed harness sessions while preserving legacy flat `.json` session records during migration.

In scope:

- Canonical `.chirality/sessions/<sessionId>/` folder layout.
- `session.json` metadata expectations.
- Legacy `.chirality/sessions/<sessionId>.json` read/list/resume/delete compatibility.
- SDK session linkage metadata needed for resume without making SDK transcripts authoritative.
- Tests for session folder layout, migration helpers, and legacy-read behavior.

Out of scope:

- `HarnessEvent` schema and append-only JSONL writer details owned by DEL-05-02.
- Runtime redaction owned by DEL-05-03.
- Replay UI/diagnostics owned by DEL-05-04.
- Tool permission semantics, excluded by PKG-05 package scope.
- Final SDK transcript placement decision where source authority marks it as an R1/OI-002 decision.

Sources: `_CONTEXT.md` `Deliverable Scope`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-05`; `docs/SPEC.md` Sections 8-10.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-05-01-R001 | New canonical sessions MUST be represented as folders under `.chirality/sessions/<sessionId>/` or the configured `CHIRALITY_SESSION_ROOT` equivalent. | `docs/SPEC.md` Section 8.2 |
| DEL-05-01-R002 | A canonical session folder MUST support `session.json`, `events.jsonl`, `turns/`, `artifacts/`, and `sdk/` as the physical layout. | `docs/SPEC.md` Section 8.2 |
| DEL-05-01-R003 | Legacy flat records at `{sessionRoot}/{sessionId}.json` MUST remain readable during migration. | `docs/SPEC.md` Section 8.1 |
| DEL-05-01-R004 | Existing `.chirality/sessions/*.json` records MUST list and resume while canonical folder layout is introduced. | `docs/PRD.md` FR-077; `docs/SPEC.md` Section 8.1 |
| DEL-05-01-R005 | Session CRUD behavior MUST remain bound to normalized project root. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 |
| DEL-05-01-R006 | `session.json` SHOULD include stable Chirality session metadata and SDK linkage metadata listed in SPEC Section 8.3. | `docs/SPEC.md` Section 8.3 |
| DEL-05-01-R007 | SDK session identifiers and transcript/store references MUST remain adapter metadata and MUST NOT redefine Chirality session identity. | `docs/SPEC.md` Section 10.3; `docs/TYPES.md` Section 7.2; `docs/CONTRACT.md` K-ENGINE-4 |
| DEL-05-01-R008 | `events.jsonl` MUST remain the canonical Chirality audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4 |
| DEL-05-01-R009 | If SDK transcript storage remains outside the working root, Chirality MUST cross-reference the transcript path or store key from `session.json` and record residual reliance-boundary risk. | `docs/SPEC.md` Section 8.4 |
| DEL-05-01-R010 | ASSUMPTION: Migration helpers should avoid destructive conversion of legacy records until list, resume, retrieve, and delete behavior are explicitly migrated and tested. | `docs/SPEC.md` Section 8.1 and `docs/PRD.md` migration rule |
| DEL-05-01-R011 | Session identifiers MUST remain stable across renames, path changes, and UI labels. | `docs/TYPES.md` Section 2; `docs/CONTRACT.md` K-ID-1 |
| DEL-05-01-R012 | Runtime records and project files MUST preserve stable IDs when paths change. | `docs/CONTRACT.md` K-PATH-1 |
| DEL-05-01-R013 | Secrets and API keys MUST NOT be stored in session metadata, runtime events, logs, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; K-EVENT-6 |
| DEL-05-01-R014 | `CHIRALITY_SESSION_ROOT` override behavior MUST remain supported for session storage root resolution. | `docs/SPEC.md` Section 8.2; `docs/PRD.md` session storage section |
| DEL-05-01-R015 | Exact implementation module names, migration helper names, and storage adapter APIs are TBD unless already present in implementation code or separately accepted. | `docs/PLAN.md` R1/R2 notes; `_REFERENCES.md` source-state warning |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| SPEC Harness Session Store | Defines legacy record shape, canonical folder layout, future metadata, and canonicalization rules. | `docs/SPEC.md` Section 8 |
| SPEC Runtime Event Schema | Constrains `events.jsonl` canonicality and replay tolerance where the session folder contains event logs. | `docs/SPEC.md` Section 9 |
| SPEC Engine Adapter Rules | Requires SDK names, IDs, transcript paths, and external message names to remain adapter metadata. | `docs/SPEC.md` Section 10.3 |
| TYPES Runtime and Session Vocabulary | Defines `SessionRecord`, `sessionId`, `sdkSessionId`, `events.jsonl`, `session.json`, and `artifacts/`. | `docs/TYPES.md` Section 7 |
| CONTRACT Invariants | Governs stable identity, project truth, SDK transcript secondary status, event mirror canonicality, replay tolerance, and redaction. | `docs/CONTRACT.md` K-ID-1, K-FS-1, K-SDK-3, K-EVENT-4 through K-EVENT-6 |
| PRD Runtime Requirements | Product requirements for session CRUD, legacy readability, SDK linkage, and audit mirror canonicality. | `docs/PRD.md` FR-014, FR-077, FR-118, FR-121; source-state warning applies |

## Verification

| Requirement IDs | Verification Approach |
|---|---|
| R001, R002, R006, R014 | Unit tests for session root resolution and canonical folder creation, including `CHIRALITY_SESSION_ROOT`. |
| R003, R004, R005, R010 | Legacy fixture tests proving flat `.json` records remain listable, retrievable, resumable, and deletable through the session surfaces. |
| R007, R008, R009 | Metadata tests proving SDK identifiers/transcript references are stored as adapter metadata and `events.jsonl` remains canonical. |
| R011, R012 | Tests or scanner checks proving `sessionId` is the persisted identity and not inferred from path labels alone. |
| R013 | Redaction/security tests proving secret-like values are not written to session metadata or referenced artifacts; detailed redaction implementation belongs to DEL-05-03. |
| R015 | Review check that implementation-specific file paths and helper names are either present in code or left as `TBD`/proposal until accepted. |

## Documentation

Required artifacts:

- Session folder layout specification or implementation note.
- Migration helper description covering legacy flat `.json` handling.
- Legacy-read/list/resume/delete test fixtures.
- `session.json` metadata field documentation.
- SDK transcript/linkage residual-risk note where placement remains unresolved.
- Test evidence for session root override behavior.

Source: `_CONTEXT.md` `Anticipated Artifacts`; `docs/SPEC.md` Section 8; `docs/PLAN.md` R1/R2 notes.
