# Source Pack: SRC-DEL-DEL-05-01-CANONICAL-SESSION-FOLDER-AND-LEGACY-SESSION-MIGRATION

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/Datasheet.md

### Datasheet: DEL-05-01 Canonical Session Folder and Legacy Session Migration

#### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-05-01 |
| DeliverableName | Canonical Session Folder and Legacy Session Migration |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ResponsibleParty | TBD |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | M |
| Scope Items | SOW-009, SOW-043, SOW-046 |
| Objective | OBJ-003 |

Source: `_CONTEXT.md` `Identity`, `Traceability`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-05`.

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Canonical session root | `.chirality/sessions/<sessionId>/` unless `CHIRALITY_SESSION_ROOT` overrides the root | `docs/SPEC.md` Section 8.2; `docs/PRD.md` session storage section |
| Canonical metadata file | `session.json` | `docs/SPEC.md` Section 8.2 |
| Canonical event log | `events.jsonl` | `docs/SPEC.md` Section 8.2; `docs/CONTRACT.md` K-EVENT-4 |
| Canonical per-turn folder | `turns/<turnId>.json` | `docs/SPEC.md` Section 8.2 |
| Canonical artifact folder | `artifacts/` | `docs/SPEC.md` Section 8.2; `docs/TYPES.md` Section 7.2 |
| Canonical SDK metadata/transcript folder | `sdk/` | `docs/SPEC.md` Section 8.2 |
| Legacy record shape | `{sessionRoot}/{sessionId}.json` | `docs/SPEC.md` Section 8.1 |
| Legacy readability requirement | Legacy records must remain readable during migration | `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077 |
| Supported session operations in scope | create, list, resume, retrieve, save, delete | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 |
| Legacy migration behavior in scope | Existing `.chirality/sessions/*.json` records list/resume while folder layout is introduced | `docs/PRD.md` FR-077 |
| SDK transcript authority | SDK transcripts are secondary runtime state unless imported into `HarnessEvent` form | `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 |

#### Conditions

| Condition | Value | Source |
|---|---|---|
| Chirality audit mirror canonicality | `.chirality/sessions/<sessionId>/events.jsonl` remains the product-owned runtime audit mirror | `docs/SPEC.md` Section 8.4; `docs/TYPES.md` Section 1.8 |
| Project truth boundary | Runtime transcripts, SDK transcripts, UI state, and caches are not project truth unless imported into governed files | `docs/TYPES.md` Section 1.7; `docs/CONTRACT.md` K-FS-1 |
| Stable identity | Session, turn, and runtime event identifiers are stable IDs assigned once | `docs/TYPES.md` Section 2 |
| SDK linkage | `sdkSessionId`, transcript path/store key, config dir, settings sources, SDK package version, Claude Code version, and resume mode are future metadata candidates | `docs/SPEC.md` Section 8.3 |
| Transcript placement | TBD: R1 must empirically decide the least surprising SDK transcript/storage pattern | `docs/SPEC.md` Section 8.4; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-046/OI-002 |
| Source-state warning | `docs/PRD.md` is locally accessible but has a hash mismatch in `_REFERENCES.md`; PRD-only implementation detail remains provisional unless corroborated | `_REFERENCES.md` REF-006 |

#### Pass 3 Lensing Status

| ItemID | Status | Datasheet impact |
|---|---|---|
| X-001 | unresolved TBD | Transcript placement remains an R1/OI-002 decision; this datasheet does not treat SDK transcript storage as stable review closure. |
| E-001 | closure warning | PRD-derived behavior must be rechecked against REF-006 source state before implementation closure. |

#### Construction

Canonical vNext session folder:

```text
.chirality/sessions/<sessionId>/
|-- session.json
|-- events.jsonl
|-- turns/
|   `-- <turnId>.json
|-- artifacts/
`-- sdk/
```

Source: `docs/SPEC.md` Section 8.2.

Legacy session record:

```text
{sessionRoot}/{sessionId}.json
```

Known legacy fields:

- `sessionId`
- `projectRoot`
- `persona`
- `mode`
- `createdAt`
- `updatedAt`
- `claudeSessionId`
- `bootFingerprint`
- `bootedAt`
- `model`

Source: `docs/SPEC.md` Section 8.1.

Future `session.json` fields should include:

- `sessionId`
- `projectRoot`
- `persona`
- `mode`
- `createdAt`
- `updatedAt`
- `model`
- `bootFingerprint`
- `sdkSessionId`
- `sdkProjectKey`
- `sdkTranscriptPath` or `sdkSessionStoreKey`
- `sdkConfigDir`
- `sdkSettingSources`
- `sdkPackageVersion`
- `sdkClaudeCodeVersion`
- `sdkResumeMode`

Source: `docs/SPEC.md` Section 8.3.

#### References

- `_CONTEXT.md` `Identity`, `Package Scope`, `Deliverable Scope`, `Traceability`
- `_REFERENCES.md` `Authoritative Source Corpus`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-05`, SOW-009, SOW-043, SOW-046, OBJ-003
- `docs/SPEC.md` Sections 8-10 and 19.3
- `docs/TYPES.md` Sections 1.7, 1.8, 2, and 7
- `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-FS-1, K-SDK-3, K-EVENT-4, K-EVENT-5, K-EVENT-6
- `docs/PLAN.md` R1/R2 implementation notes
- `docs/PRD.md` session storage, FR-014, FR-077, FR-118, FR-121, FR-122, FR-123; source-state warning applies because REF-006 has `HASH_MISMATCH`

## Component: execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/Guidance.md

### Guidance: DEL-05-01 Canonical Session Folder and Legacy Session Migration

#### Purpose

This deliverable gives Chirality a forward-compatible session storage shape without breaking existing harness sessions. The main design pressure is to move from legacy flat `.json` records to folder-backed sessions while keeping runtime audit authority with Chirality-owned `events.jsonl`, not SDK transcripts or hidden state.

Sources: `_CONTEXT.md` `Deliverable Scope`; `docs/SPEC.md` Section 8; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

#### Principles

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

#### Considerations

- The layout should serve later PKG-05 deliverables: `events.jsonl` for DEL-05-02, replay support for DEL-05-04, and artifacts for DEL-05-05. Do not overload DEL-05-01 with those implementations.
- Legacy records include `claudeSessionId`; vNext metadata uses `sdkSessionId` and related SDK linkage fields. Exact field mapping is TBD because the source set does not specify a migration transform.
- `CHIRALITY_SESSION_ROOT` changes the storage root. Tests should cover both default and override roots.
- Session CRUD is source-supported, but route-level save/update semantics are less explicit than create/list/get/delete. Treat "save" behavior as TBD unless current code or a later accepted spec defines it.
- Transcript placement remains an R1/OI-002 decision. A migration implementation should be able to record transcript path/store-key metadata without assuming the final storage mechanism.
- Redaction requirements apply to metadata and artifacts, but detailed redaction behavior belongs to DEL-05-03.

#### Pass 3 Rulings Needed

| ItemID | Ruling needed | Interim guidance |
|---|---|---|
| A-001 | Whether session save/update is a distinct behavior or covered by create/boot/retrieve/delete surfaces. | Treat save/update semantics as `TBD`; do not infer a route or persistence rule from SOW/PRD wording alone. |
| B-001 | Whether legacy `claudeSessionId` maps directly to `sdkSessionId`. | Keep the legacy field readable and record new SDK linkage separately unless implementation evidence accepts a transform. |
| F-001 | Duplicate folder-versus-flat behavior for the same stable `sessionId`. | Do not implement destructive delete or overwrite behavior until duplicate precedence and deletion semantics are ruled. |
| X-001 | Final SDK transcript placement and review closure standard. | Keep SDK transcript path/store key as non-authoritative metadata while R1/OI-002 remains open. |

#### Trade-offs

| Option | Benefit | Cost / Risk | Guidance |
|---|---|---|---|
| Lazy legacy read support | Minimal migration risk; existing sessions remain usable | Code must handle two storage shapes during transition | Prefer unless a human-approved migration plan requires eager conversion |
| Eager conversion to folders | Simplifies later reader code | Risks destructive migration and field-loss without accepted mapping | Do not require in this deliverable without additional source authority |
| Store SDK transcript under working-root-controlled folder | Better locality and governance review | SDK behavior must be empirically verified | Preferred direction when reliable; source marks it as R1 decision |
| Cross-reference SDK transcript in user home | Preserves resume if SDK cannot be redirected | Adds reliance-boundary risk and non-project state dependency | Accept only with explicit `session.json` metadata and residual-risk record |
| Keep `events.jsonl` as canonical audit mirror | Preserves Chirality-owned runtime evidence | Requires event writer/replay discipline | Required by SPEC and CONTRACT |

E-002 disposition: when SDK transcripts remain outside project-controlled storage, the trade-off is acceptable only with `session.json` cross-reference metadata and a residual reliance-boundary record. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3 and K-EVENT-4.

#### Examples

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

#### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| DEL-05-01-C001 | Session "save" is listed in SOW/PRD session operations, while SPEC endpoint list explicitly names create, boot, list, get/delete, turn, and interrupt but not a separate save endpoint. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-009; `docs/PRD.md` FR-014 | `docs/SPEC.md` API endpoint table | `Specification.md` Verification; `Procedure.md` Steps | Treat save/update semantics as TBD and verify against implementation or later accepted spec before coding. | TBD |

#### Source-State Notes

- `docs/PRD.md` is marked `HASH_MISMATCH` in `_REFERENCES.md`; PRD-derived requirements are cited but should be revalidated before implementation lock-in.
- `docs/PLAN.md` names likely implementation artifacts such as `session-events.ts` and `sdk-session-link.ts`, but this deliverable does not yet have accepted implementation paths. Keep exact paths as `TBD` unless code inspection in an implementation task confirms them.

## Component: execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/Procedure.md

### Procedure: DEL-05-01 Canonical Session Folder and Legacy Session Migration

#### Purpose

Provide an operational procedure for producing and verifying the DEL-05-01 implementation slice: canonical session folder layout plus legacy flat `.json` compatibility for list, resume, retrieve, and delete behavior.

Source: `_CONTEXT.md` `Deliverable Scope`; `docs/SPEC.md` Section 8; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-05-01.

#### Prerequisites

- Accepted DEL-05-01 scope and four-document kit.
- Access to `docs/SPEC.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/PLAN.md`, and `docs/PRD.md`.
- Awareness that `docs/PRD.md` has a `HASH_MISMATCH` in `_REFERENCES.md`; PRD-only implementation details require caution.
- Current session storage implementation and tests located by the implementation worker. Exact paths are TBD.
- Upstream dependency edges are not yet accepted; `_DEPENDENCIES.md` declares upstream/downstream as TBD.
- R1/OI-002 transcript placement remains unresolved; do not hard-code final SDK transcript storage policy beyond metadata support.

#### Steps

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

#### Verification

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

#### Pass 3 Evidence Checks

| ItemID | Check | Expected handling |
|---|---|---|
| C-001 | Implementation worker identifies current session storage source files and focused test commands. | Keep paths and commands `TBD` until code inspection confirms them. |
| D-001 | Duplicate-shape test exists after duplicate policy is accepted. | Do not close this branch without an accepted duplicate folder/flat policy and evidence. |
| E-001 | PRD-derived behavior is rechecked against REF-006 source state before closure. | Record the recheck result in implementation evidence; keep PRD-only details provisional until corroborated. |
| F-001 | Delete behavior is verified when both folder and flat records exist for the same `sessionId`. | Require human or design ruling before destructive behavior. |

#### Records

- Updated source files for session root resolution, canonical folder layout, and migration helpers: TBD.
- Legacy flat-session fixtures: TBD.
- Canonical folder-session fixtures: TBD.
- Test results for list/resume/retrieve/delete migration behavior: TBD.
- Residual-risk note for SDK transcript placement if not project-controlled: TBD.
- Human ruling for duplicate folder/flat record delete semantics: TBD.
- Source-state recheck record for REF-006 PRD-derived behavior: TBD.

## Component: execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/Specification.md

### Specification: DEL-05-01 Canonical Session Folder and Legacy Session Migration

#### Scope

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

#### Requirements

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

#### Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| SPEC Harness Session Store | Defines legacy record shape, canonical folder layout, future metadata, and canonicalization rules. | `docs/SPEC.md` Section 8 |
| SPEC Runtime Event Schema | Constrains `events.jsonl` canonicality and replay tolerance where the session folder contains event logs. | `docs/SPEC.md` Section 9 |
| SPEC Engine Adapter Rules | Requires SDK names, IDs, transcript paths, and external message names to remain adapter metadata. | `docs/SPEC.md` Section 10.3 |
| TYPES Runtime and Session Vocabulary | Defines `SessionRecord`, `sessionId`, `sdkSessionId`, `events.jsonl`, `session.json`, and `artifacts/`. | `docs/TYPES.md` Section 7 |
| CONTRACT Invariants | Governs stable identity, project truth, SDK transcript secondary status, event mirror canonicality, replay tolerance, and redaction. | `docs/CONTRACT.md` K-ID-1, K-FS-1, K-SDK-3, K-EVENT-4 through K-EVENT-6 |
| PRD Runtime Requirements | Product requirements for session CRUD, legacy readability, SDK linkage, and audit mirror canonicality. | `docs/PRD.md` FR-014, FR-077, FR-118, FR-121; source-state warning applies |

#### Verification

| Requirement IDs | Verification Approach |
|---|---|
| R001, R002, R006, R014 | Unit tests for session root resolution and canonical folder creation, including `CHIRALITY_SESSION_ROOT`. |
| R003, R004, R005, R010 | Legacy fixture tests proving flat `.json` records remain listable, retrievable, resumable, and deletable through the session surfaces. |
| R007, R008, R009 | Metadata tests proving SDK identifiers/transcript references are stored as adapter metadata and `events.jsonl` remains canonical. |
| R011, R012 | Tests or scanner checks proving `sessionId` is the persisted identity and not inferred from path labels alone. |
| R013 | Redaction/security tests proving secret-like values are not written to session metadata or referenced artifacts; detailed redaction implementation belongs to DEL-05-03. |
| R015 | Review check that implementation-specific file paths and helper names are either present in code or left as `TBD`/proposal until accepted. |
| A-001 | Review check that save/update behavior is not implemented from the conflict table alone; coding must wait for implementation evidence or a human ruling. |
| B-001, F-001 | Review check that legacy `claudeSessionId` mapping and duplicate folder-versus-flat behavior remain `TBD` until accepted by implementation evidence or human ruling. |
| E-002 | Review check that any external SDK transcript path/store-key use has an explicit residual reliance-boundary note. |

#### Documentation

Required artifacts:

- Session folder layout specification or implementation note.
- Migration helper description covering legacy flat `.json` handling.
- Legacy-read/list/resume/delete test fixtures.
- `session.json` metadata field documentation.
- SDK transcript/linkage residual-risk note where placement remains unresolved.
- Test evidence for session root override behavior.
- Human or implementation rulings for save/update behavior, duplicate folder-versus-flat behavior, and `claudeSessionId` to `sdkSessionId` mapping.
- Source-state recheck for PRD-derived behavior affected by REF-006 `HASH_MISMATCH`.

Source: `_CONTEXT.md` `Anticipated Artifacts`; `docs/SPEC.md` Section 8; `docs/PLAN.md` R1/R2 notes.
