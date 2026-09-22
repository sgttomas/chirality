# Context: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-01 |
| DeliverableName | Canonical Session Folder and Legacy Session Migration |
| ResponsibleParty | TBD |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence.

**InclusionCriteria:** Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence.

**Exclusions:** Generic session/event/tool-result persistence and daemon operational-state ownership.

## Deliverable Scope

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-009, SOW-043, SOW-046 |
| SupportsObjectives | OBJ-003 |
| ContextEnvelopeNotes | App compatibility and migration-participation slice; daemon sessions remain Root-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## Current interface applicability — 2026-09-22

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
