# Datasheet: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Identification

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

## Attributes

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

## Conditions

| Condition | Value | Source |
|---|---|---|
| Chirality audit mirror canonicality | `.chirality/sessions/<sessionId>/events.jsonl` remains the product-owned runtime audit mirror | `docs/SPEC.md` Section 8.4; `docs/TYPES.md` Section 1.8 |
| Project truth boundary | Runtime transcripts, SDK transcripts, UI state, and caches are not project truth unless imported into governed files | `docs/TYPES.md` Section 1.7; `docs/CONTRACT.md` K-FS-1 |
| Stable identity | Session, turn, and runtime event identifiers are stable IDs assigned once | `docs/TYPES.md` Section 2 |
| SDK linkage | `sdkSessionId`, transcript path/store key, config dir, settings sources, SDK package version, Claude Code version, and resume mode are future metadata candidates | `docs/SPEC.md` Section 8.3 |
| Transcript placement | TBD: R1 must empirically decide the least surprising SDK transcript/storage pattern | `docs/SPEC.md` Section 8.4; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-046/OI-002 |
| Source-state warning | `docs/PRD.md` is locally accessible but has a hash mismatch in `_REFERENCES.md`; PRD-only implementation detail remains provisional unless corroborated | `_REFERENCES.md` REF-006 |

## Pass 3 Lensing Status

| ItemID | Status | Datasheet impact |
|---|---|---|
| X-001 | unresolved TBD | Transcript placement remains an R1/OI-002 decision; this datasheet does not treat SDK transcript storage as stable review closure. |
| E-001 | closure warning | PRD-derived behavior must be rechecked against REF-006 source state before implementation closure. |

## Construction

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

## References

- `_CONTEXT.md` `Identity`, `Package Scope`, `Deliverable Scope`, `Traceability`
- `_REFERENCES.md` `Authoritative Source Corpus`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-05`, SOW-009, SOW-043, SOW-046, OBJ-003
- `docs/SPEC.md` Sections 8-10 and 19.3
- `docs/TYPES.md` Sections 1.7, 1.8, 2, and 7
- `docs/CONTRACT.md` K-ID-1, K-PATH-1, K-FS-1, K-SDK-3, K-EVENT-4, K-EVENT-5, K-EVENT-6
- `docs/PLAN.md` R1/R2 implementation notes
- `docs/PRD.md` session storage, FR-014, FR-077, FR-118, FR-121, FR-122, FR-123; source-state warning applies because REF-006 has `HASH_MISMATCH`
