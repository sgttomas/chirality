# Dependencies: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-04-03-001, DEP-04-03-002, DEP-04-03-003, DEP-04-03-004, DEP-04-03-005, DEP-04-03-006, DEP-04-03-007, DEP-04-03-008, DEP-04-03-009, DEP-04-03-011

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-04-03-010

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK + dependency-extract ran in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` identity/traceability fields.
- Execution doc order: `Specification.md`, `Procedure.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition path: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for anchor/target labels.
- [WARNING] REF-006 `docs/PRD.md` has `HASH_MISMATCH` in `_REFERENCES.md`; PRD-derived statements remain warning-qualified in source documents.
- [WARNING] OI-001 / DEL-04-01 probe evidence is still `TBD`; exact SDK message payload shapes were not inferred.
- [WARNING] `tools/validation/validate_id_format.sh` expects legacy `PKG-000` / `DEL-000-00` forms and rejects authoritative v3.2 IDs such as `PKG-04` and `DEL-04-03`; decomposition-authoritative IDs were preserved.
- 2026-06-16 SCC-SAFE-MOVES-001 decomposed `DEP-04-03-008`, `DEP-04-03-009`, and `DEP-04-03-010` from coarse deliverable edges into document-scoped runtime-contract, SSE/UIEvent, and mapper-handoff evidence; the rows remain active and in objective.
- 2026-07-18 WI-PKG04-01 correction of the `[WARNING] OI-001 / DEL-04-01 probe evidence is still TBD` note above: partially stale — deterministic DEL-04-01 probe evidence now exists (pinned `@anthropic-ai/claude-agent-sdk@0.3.150`; `sdk-message-mapper.ts` and `sdk-message-mapper.test.ts` deterministic fixture provenance; `Evidence_CODEV-001_SDK_Probe_Record.md` 2026-07-10 refresh). Still open: the exact observed live `query()` message sequence, which remains `BLOCKED_TBD` and owner-gated (D-APP-52); `DEP-04-03-007` therefore stays `TBD` (annotate-only). The original warning text is retained above as history. Citation note: the row's `Datasheet.md#Attributes` source now lives at `ScopeOfWork.md` CLM-003 Attributes per owner commit `603384787` (2026-07-13 ScopeOfWork-v1 migration). See DEL-04-01 `Evidence_HANDOVER_CONSUMPTION_2026-07-18.md` section B.
- 2026-07-18 D-APP-52 live-demonstration closure (owner's in-session act 2026-07-18; mechanical conformance by run `DAPP52_LIVE_DEMONSTRATION_2026-07-18`): `DEP-04-03-007` closed `SATISFIED` — the exact observed live `query()` message sequence this row depended on is now recorded in DEL-04-01 `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md` (PACK1 artifact SHA-256 `be155013371f51c1a52a364d19d9f164f9f2509bd921ca4d1af7b00b25a11686`); producer row `DEP-04-01-011` closed in the same pass. Lifecycle Summary synced (SATISFIED 1 / TBD 10).

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-04-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-04 | ACTIVE | TBD |
| DEP-04-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-040 | ACTIVE | TBD |
| DEP-04-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-044 | ACTIVE | TBD |
| DEP-04-03-004 | ANCHOR | OTHER | UPSTREAM | SOW-051 | ACTIVE | TBD |
| DEP-04-03-005 | ANCHOR | OTHER | UPSTREAM | OBJ-002 | ACTIVE | TBD |
| DEP-04-03-006 | ANCHOR | OTHER | UPSTREAM | OBJ-004 | ACTIVE | TBD |
| DEP-04-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 | RETIRED | SATISFIED |
| DEP-04-03-008 | EXECUTION | INTERFACE | UPSTREAM | RUNTIME_ENGINE_CONTRACT_AGENT_ENGINE_PORT | ACTIVE | TBD |
| DEP-04-03-009 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-03-SSE_UIEVENT_CONTRACT | ACTIVE | TBD |
| DEP-04-03-010 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-04-03-SPEC-HARNESSEVENT_HANDOFF | ACTIVE | TBD |
| DEP-04-03-011 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-04-02 | ACTIVE | TBD |

Counts: ACTIVE=11; satisfaction SATISFIED=1, TBD=10.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:35:55-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` used | REF-006 hash mismatch; OI-001 probe TBD; ID-format helper legacy mismatch | ANCHOR=6; EXECUTION=5; TOTAL=11 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 1 |
| TBD | 10 |

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: App `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `frontend/src/__tests__/components/live-session-requests.test.tsx`; Runtime `tests/codex-app-server-client.test.ts`, `tests/codex-supervisor.test.ts`; retained App `sdk-message-mapper.ts` and its tests. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=10, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_PREVIEW_THREE_INTERFACES.csv`; current rows: ACTIVE=10, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
