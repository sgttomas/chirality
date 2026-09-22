# Dependencies: DEL-05-01 Canonical Session Folder and Legacy Session Migration

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-05-01-001, DEP-05-01-002, DEP-05-01-003, DEP-05-01-004, DEP-05-01-005, DEP-05-01-006, DEP-05-01-007, DEP-05-01-008, DEP-05-01-009, DEP-05-01-013

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-05-01-010, DEP-05-01-011, DEP-05-01-012

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-05-01-001 | ANCHOR | OTHER | UPSTREAM | PKG-05 | ACTIVE | NOT_APPLICABLE |
| DEP-05-01-002 | ANCHOR | OTHER | UPSTREAM | SOW-009 | ACTIVE | NOT_APPLICABLE |
| DEP-05-01-003 | ANCHOR | OTHER | UPSTREAM | SOW-043 | ACTIVE | NOT_APPLICABLE |
| DEP-05-01-004 | ANCHOR | OTHER | UPSTREAM | SOW-046 | ACTIVE | NOT_APPLICABLE |
| DEP-05-01-005 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002; REF-003; REF-004; REF-005; REF-006 | ACTIVE | SATISFIED |
| DEP-05-01-006 | EXECUTION | PREREQUISITE | UPSTREAM | projects/chirality-runtime/packages/core/src/session-store.ts; projects/chirality-runtime/tests/session-and-residency.test.ts | ACTIVE | SATISFIED |
| DEP-05-01-007 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | RETIRED | SATISFIED |
| DEP-05-01-008 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-04-01 | RETIRED | TBD |
| DEP-05-01-009 | EXECUTION | CONSTRAINT | UPSTREAM | D-APP-41 | ACTIVE | PENDING |
| DEP-05-01-010 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-05-02 | ACTIVE | TBD |
| DEP-05-01-011 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-05-04 | ACTIVE | TBD |
| DEP-05-01-012 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-05-05 | ACTIVE | TBD |
| DEP-05-01-013 | EXECUTION | INTERFACE | UPSTREAM | Runtime-owned central session store and declared legacy-root migration | ACTIVE | PENDING |

Counts: ACTIVE=12, RETIRED=1; satisfaction NOT_APPLICABLE=4, PENDING=1, SATISFIED=4, TBD=4.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- Dependency extraction used `Datasheet.md` as the primary anchor document and `Specification.md`, `Guidance.md`, and `Procedure.md` as execution documents.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read or consumed as evidence.
- No existing `Dependencies.csv` was present, so this run created the v3.1 register.
- Existing declared dependency sections remain `TBD`; no declared edges were promoted because no accepted declared upstream/downstream edges existed.
- `[SATISFIED] SOURCE_STATE`: D-APP-38 corpus v2 refreshed REF-006; `_REFERENCES.md` now reports `docs/PRD.md` as `MATCH`.
- `[SATISFIED] IMPLEMENTATION_PATHS`: ADQ-08 identified `frontend/src/lib/harness/session-manager.ts` and `frontend/src/__tests__/lib/session-manager.test.ts`.
- `[WARNING] OPEN_DECISION`: OI-002 transcript placement remains unresolved and constrains SDK transcript/linkage handling.
- `[SATISFIED] D-APP-41`: duplicate folder/flat record delete semantics use canonical precedence, preserve legacy-only fields, and remove flat records after canonicalization.
- `[WARNING] ID_FORMAT_HELPER_MISMATCH`: `tools/validation/validate_id_format.sh` rejects accepted decomposition IDs such as `PKG-05` and `DEL-05-01` because it expects `PKG-000` / `DEL-000-00` style IDs. The register preserves the accepted v3.2 decomposition IDs.
- Parent anchor check passed: exactly one ACTIVE `IMPLEMENTS_NODE` row exists.

## Run Notes - 2026-09-03 v3 pathway seating (additive UPDATE)

- `TASK + dependency-extract` method applied in-line by the A12 seating tranche (ephemeral Agent 2 generalist; no TASK run record under `_run_records/` because that path is outside the tranche write set); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; `ScopeOfWork.md` re-pinned to that commit in the same tranche.
- Scope of this pass: exactly one new row, `DEP-05-01-013`, making the v3 gate/interface edge consumed by the seated `Remaining` item explicit. Existing rows are preserved byte-identically (no `LastSeen` refresh, no retirement); the full two-pass re-extraction is not claimed for them.
- Evidence: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L322`; quote: "Maintain App-client compatibility for daemon-centralized sessions".
- Target resolution: Root-owned targets keep `TargetLocation=TBD` (no Root path is invented); deliverable targets resolve against the applied decomposition.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities; accepted decomposition IDs are preserved (same finding as the Gate-5 refresh).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- A2-B / SCC posture: no objective-relative feedback edge was added or linearized; the post-application audit's nine-node SCC remains a warning-bearing derivative finding.
- Schema validation: `python3 tools/validation/validate_dependencies_schema.py Dependencies.csv` PASS after the append; see `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/DEPENDENCY_REFRESH.md`.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:41:21-0600 | UPDATE | CONSERVATIVE | v3.2 found | SOURCE_STATE; TBD_TARGET; OPEN_DECISION; ID_FORMAT_HELPER_MISMATCH | ANCHOR=4; EXECUTION=8; TOTAL=12 |
| 2026-06-21T03:00:00-0600 | UPDATE | CONSERVATIVE | v3.2 found | OPEN_DECISION; ID_FORMAT_HELPER_MISMATCH | ANCHOR=4; EXECUTION=8; ACTIVE=11; RETIRED=1 |
| 2026-09-03T00:00:00-06:00 | UPDATE (additive, one row) | CONSERVATIVE | applied `d6f6cadb2` SHA-256 `932b890e…168716f` | PROJECT_ID_FORMAT_PROFILE; existing rows preserved without LastSeen refresh | ANCHOR=4; EXECUTION=8; ACTIVE=12; RETIRED=1 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 12 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| PENDING | 1 |
| NOT_APPLICABLE | 4 |
| SATISFIED | 4 |
| TBD | 4 |

| DependencyType | Count |
|---|---:|
| OTHER | 4 |
| PREREQUISITE | 2 |
| CONSTRAINT | 3 |
| HANDOVER | 3 |
| INTERFACE | 1 |

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/core/src/session-store.ts` and its session-store/migration tests; App session routes and clients; historical `frontend/src/lib/harness/session-manager.ts` and canonicalization fixtures. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

DEP-05-01-006 snapshot designation: its App session-manager path/test evidence and SATISFIED value describe the retained legacy implementation snapshot. They do not establish the current Runtime session-store conformance; the current locus above and live checks in ScopeOfWork/Remaining apply. No formal row or satisfaction was changed by this designation.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=12; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_PREVIEW_FORMAL.csv`; current rows: ACTIVE=12, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_PREVIEW_STORE_LOCATIONS.csv`; current rows: ACTIVE=12, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=11, RETIRED=2. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
