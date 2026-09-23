---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-01
package_id: PKG-05
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-009, SOW-043, SOW-046]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-05-01` in service of project scope [SOW-009, SOW-043, SOW-046] and package objectives [OBJ-003].

- **OUT-001** — App session-client conformance to Runtime-owned central storage and lazy non-destructive declared-root migration, preserving stable identity, canonical precedence, retained-source integrity, truthful legacy availability and provider-thread linkage.

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

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Named verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence. Evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

### CLM-004 — Conditions

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Named verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence. Evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

### CLM-005 — Pass 3 Lensing Status

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Lensing Status
>
> | ItemID | Status | Datasheet impact |
> |---|---|---|
> | X-001 | unresolved TBD | Transcript placement remains an R1/OI-002 decision; this datasheet does not treat SDK transcript storage as stable review closure. |
> | E-001 | satisfied | PRD-derived behavior was rechecked against the D-APP-38 corpus v2 MATCH state before ADQ-08 closure. |
>


Current requirement and verification boundary: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

### CLM-006 — Construction

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

Unfinished delivery: Complete central-store migration conformance for declared legacy roots, duplicate/source-marker/corruption/delete cases and App discovery. Preserve inaccessible or unmapped prior records as explicit limitations; import and v2 continuation are not release prerequisites.

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

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

### CLM-010 — Requirements

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-05-01-R001 | New sessions use the Runtime central per-project/session store; project-local or CHIRALITY_SESSION_ROOT shapes are legacy sources. |
| DEL-05-01-R002 | Support canonical session metadata/event storage and applicable turn/artifact/linkage records through Runtime contracts; sdk/ is a historical adapter-specific directory, while missing live artifacts remain a delivery gap. |
| DEL-05-01-R003 | Apply lazy non-destructive migration only to declared legacy roots, preserving identity and recording inaccessible/unmapped historical sources. |
| DEL-05-01-R004 | Retain readable historical records and use the central canonical store on migration; no new flat writes and no required eager import or v2 continuation feature. |
| DEL-05-01-R005 | Session CRUD behavior MUST remain bound to normalized project root. |
| DEL-05-01-R006 | `session.json` SHOULD include stable Chirality session metadata and SDK linkage metadata listed in SPEC Section 8.3. |
| DEL-05-01-R007 | SDK session identifiers and transcript/store references MUST remain adapter metadata and MUST NOT redefine Chirality session identity. |
| DEL-05-01-R008 | `events.jsonl` MUST remain the canonical Chirality audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form. |
| DEL-05-01-R009 | Cross-reference native thread/transcript identity in session metadata and record actual transcript-access/reliance limitations without declaring provider transcripts canonical. |
| DEL-05-01-R010 | If both canonical folder and legacy flat records exist for the same `sessionId`, resolution MUST prefer defined canonical values, preserve legacy-only fields, and write the merged canonical `session.json` carrying a `legacySource` consumption marker (sha256 of the flat record bytes, `materializedAt`); the flat record MUST be retained byte-identical and MUST NOT be removed; later reads MUST use the canonical record (the flat record is not a standing read input once marked consumed, and a flat record changed after consumption is reported, not merged); a canonical record that cannot be opened MUST fail closed and MUST NOT be overwritten from the flat record. (Amended 2026-09-03 under A13; the pre-amendment text required removal of the flat record.) |
| DEL-05-01-R011 | Session identifiers MUST remain stable across renames, path changes, and UI labels. |
| DEL-05-01-R012 | Runtime records and project files MUST preserve stable IDs when paths change. |
| DEL-05-01-R013 | Secrets and API keys MUST NOT be stored in session metadata, runtime events, logs, SDK transcripts if avoidable, or tool artifacts. |
| DEL-05-01-R014 | Current storage follows the Runtime user-data/project root contract; the old CHIRALITY_SESSION_ROOT knob is compatibility history. |
| DEL-05-01-R015 | Name Runtime packages/core/src/session-store.ts, current migration/client paths and focused live validation evidence. |
| DEL-05-01-R016 | New sessions MUST NOT write legacy flat `{sessionId}.json` files. |

Verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

Evidence locations: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures. These are hooks and source locations, not newly executed results.

### CLM-011 — Standards

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Named verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence. Evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

### CLM-012 — Verification

Required current checks: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

Named evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Complete central-store migration conformance for declared legacy roots, duplicate/source-marker/corruption/delete cases and App discovery. Preserve inaccessible or unmapped prior records as explicit limitations; import and v2 continuation are not release prerequisites.

### CLM-013 — Documentation

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

Unfinished delivery: Complete central-store migration conformance for declared legacy roots, duplicate/source-marker/corruption/delete cases and App discovery. Preserve inaccessible or unmapped prior records as explicit limitations; import and v2 continuation are not release prerequisites.

### CLM-014 — D-APP-56 guard amendment (2026-07-12)

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### D-APP-56 guard amendment (2026-07-12)
>
> R4-P31 adopts both session-manager guards into DEL-05-01: `assertSafeSessionId` prevents unsafe/path-traversing session identifiers, and `assertProjectRootAccessible` enforces accessible contained project roots. A dedicated session-ID guard test remains an explicit verification obligation; this text does not assert it exists.

- **AC-001** — The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-05-01 Canonical Session Folder and Legacy Session Migration

> #### Procedure: DEL-05-01 Canonical Session Folder and Legacy Session Migration
>

### CLM-016 — Purpose

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

### CLM-017 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

Current implementation/adoption evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-018 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.
4. Verify verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.
5. Retain inputs, source/candidate identity, commands, output and limitations; update governing scope and any selected work graph only for backchecked outcomes.

Locus and checks: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-019 — Verification

Required current checks: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

Named evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Complete central-store migration conformance for declared legacy roots, duplicate/source-marker/corruption/delete cases and App discovery. Preserve inaccessible or unmapped prior records as explicit limitations; import and v2 continuation are not release prerequisites.

### CLM-020 — Pass 3 Evidence Checks

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Evidence Checks
>
> | ItemID | Check | Expected handling |
> |---|---|---|
> | C-001 | Implementation worker identifies current session storage source files and focused test commands. | SATISFIED by ADQ-08 evidence: `session-manager.ts`, `session-manager.test.ts`, focused route/event/turn tests, typecheck. |
> | D-001 | Duplicate-shape test exists after duplicate policy is accepted. | SATISFIED by D-APP-41 and `session-manager.test.ts` duplicate fixture. |
> | E-001 | PRD-derived behavior is rechecked against REF-006 source state before closure. | SATISFIED by D-APP-38 corpus v2 / `_REFERENCES.md` MATCH state and ADQ-08 status check. |
> | F-001 | Delete behavior is verified when both folder and flat records exist for the same `sessionId`. | SATISFIED by `session-manager.test.ts` delete fixture. |
>


Current requirement and verification boundary: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

### CLM-021 — Records

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

Record the current implementation/consumer and named verification locations: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

Unfinished delivery: Complete central-store migration conformance for declared legacy roots, duplicate/source-marker/corruption/delete cases and App discovery. Preserve inaccessible or unmapped prior records as explicit limitations; import and v2 continuation are not release prerequisites.

- **VER-001** — Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

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

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Named verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence. Evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

### CLM-025 — Considerations

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Named verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence. Evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

### CLM-026 — Pass 3 Rulings Needed

**Historical evidence:** the dated findings below retain their evaluated path and candidate. They do not establish current Codex qualification.

> ##### Pass 3 Rulings Needed
>
> | ItemID | Ruling needed | Interim guidance |
> |---|---|---|
> | A-001 | Whether session save/update is a distinct behavior or covered by create/boot/retrieve/delete surfaces. | Resolved for ADQ-08 by implementation evidence: keep `FileSessionManager.save` internal and do not add a public save route. |
> | B-001 | Whether legacy `claudeSessionId` maps directly to `sdkSessionId`. | Keep the legacy field readable and record new SDK linkage separately unless implementation evidence accepts a transform. |
> | F-001 | Duplicate folder-versus-flat behavior for the same stable `sessionId`. | Resolved by D-APP-41: canonical values win, legacy-only fields are preserved, and the flat record is removed after merge. |
> | X-001 | Final SDK transcript placement and review closure standard. | Keep SDK transcript path/store key as non-authoritative metadata while R1/OI-002 remains open. |
>


Current requirement and verification boundary: The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence.

### CLM-027 — Trade-offs

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Named verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence. Evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

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

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Complete central-store migration conformance for declared legacy roots, duplicate/source-marker/corruption/delete cases and App discovery. Preserve inaccessible or unmapped prior records as explicit limitations; import and v2 continuation are not release prerequisites.

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

### CLM-032 — A13 legacy-record retention amendment (2026-09-03)

App session clients conform to Runtime-owned central storage and D-APP-73 lazy, non-destructive declared-legacy-root migration. D-GOV-43 preserves accessible prior history and does not require a v2 import/continuation feature for release.

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve stable session/project identity and root binding; engineSelection, adapterSession/engineSessionId and managed-child fields retain actual attribution. New sessions never write legacy flat files. Canonical precedence, fail-closed corrupt canonical handling and byte-identical retained legacy sources remain. A13 duplicate-field preservation, exact source-byte consumption marker and changed-source diagnostics remain applicable migration requirements, with live gaps explicit. Deletion must honor central-store tombstone/retention semantics; do not reintroduce eager deletion or CHIRALITY_SESSION_ROOT.

Named verification: Verify central storage, stable IDs, list/get/update/delete and declared-root behavior, flat and directory legacy cases, duplicates, corrupt canonical records, byte-identical source retention, consumed-source change diagnostics and transcript/thread linkage. Do not count a legacy fixture as live evidence. Evidence: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-009 SOW-043 SOW-046 OBJ-003 | CLM-010  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
