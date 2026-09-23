# Dependencies: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

> **Current-source note (2026-09-23):** References below to the former App `Remaining` section and its Depends text record dated extraction evidence. The live status section was retired in the finite App Task Management account. For current work and dependency gating, read `Dependencies.csv`, governing Scope of Work, accepted decisions and the selected work graph. The historical Depends text adds no prerequisite; this note does not change the accepted register rows.


## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-04-05-001, DEP-04-05-002, DEP-04-05-003, DEP-04-05-004, DEP-04-05-005, DEP-04-05-006, DEP-04-05-007, DEP-04-05-008, DEP-04-05-010, DEP-04-05-011, DEP-04-05-012, DEP-04-05-013

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-04-05-009

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract UPDATE run used `Datasheet.md` as the anchor document and `Specification.md`, `Guidance.md`, and `Procedure.md` as execution documents.
- Decomposition authority used: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; anchor label resolution succeeded.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed.
- Strictness: CONSERVATIVE. Unknown implementation paths, SDK error shapes, and Node/SDK network enforcement mechanisms remain `TBD`.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- 2026-07-18 WI-PKG04-01 handover-evidence pass (annotate-only): `DEP-04-05-007` stays `TBD` — partial upstream delivery is evidenced (`anthropic-agent-sdk-manager.ts` error classification and bounded base-URL posture with tests; ADQ-15/ADQ-16 scripted no-live packaged and network proofs), while live-confirmed exact SDK error object shapes and packaged live behavior remain owner-gated (D-APP-52; this deliverable's RQ-011 four-class assertion gap). Citation note: the row's `Procedure.md#Prerequisites` source now lives at `ScopeOfWork.md` CLM-017 Prerequisites per owner commit `036e0769c` (2026-07-13 ScopeOfWork-v1 migration). See DEL-04-01 `Evidence_HANDOVER_CONSUMPTION_2026-07-18.md` section D.
- 2026-07-18 WI-PKG04-01 stale-table correction: the per-row table below listed `DEP-04-05-011` as `ACTIVE` and the counts line claimed "12 ACTIVE rows", but `Dependencies.csv` records `DEP-04-05-011` as `RETIRED / NOT_APPLICABLE` (the Lifecycle Summary ACTIVE 10 / RETIRED 2 was already correct). Table row and counts line corrected in this pass; this note records the prior stale values.
- 2026-07-18 D-APP-52 live-demonstration closure (owner's in-session act 2026-07-18; mechanical conformance by run `DAPP52_LIVE_DEMONSTRATION_2026-07-18`): `DEP-04-05-007` closed `SATISFIED` — live-confirmed SDK error object shapes and packaged live behavior are now recorded in DEL-04-01 `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md` (PACK1 SHA-256 `be155013371f51c1a52a364d19d9f164f9f2509bd921ca4d1af7b00b25a11686`) and `Evidence_DAPP52_PACKAGED_LIVE_PROOF_2026-07-18_summary.json` (PACK3 SHA-256 `ac3507b043e5470a7ec16afebdf205e59f6b631b6ada552e44941fd603945e78`); RATE_LIMITED not live-triggered and this deliverable's RQ-011 four-class assertion gap remains its own gated Remaining item; producer row `DEP-04-01-013` closed in the same pass. Lifecycle Summary synced (SATISFIED 7 / TBD 3).

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-04-05-001 | ANCHOR | OTHER | UPSTREAM | PKG-04 | ACTIVE | SATISFIED |
| DEP-04-05-002 | ANCHOR | OTHER | UPSTREAM | SOW-019 | ACTIVE | SATISFIED |
| DEP-04-05-003 | ANCHOR | OTHER | UPSTREAM | SOW-020 | ACTIVE | SATISFIED |
| DEP-04-05-004 | ANCHOR | OTHER | UPSTREAM | SOW-021 | ACTIVE | SATISFIED |
| DEP-04-05-005 | ANCHOR | OTHER | UPSTREAM | OBJ-004 | ACTIVE | SATISFIED |
| DEP-04-05-006 | ANCHOR | OTHER | UPSTREAM | OBJ-008 | ACTIVE | SATISFIED |
| DEP-04-05-007 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 | RETIRED | SATISFIED |
| DEP-04-05-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-02 | RETIRED | TBD |
| DEP-04-05-009 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-04-03 | ACTIVE | TBD |
| DEP-04-05-010 | EXECUTION | INTERFACE | UPSTREAM | DEL-02-05-KEY_STATUS_CONTRACT | ACTIVE | TBD |
| DEP-04-05-011 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-03 | RETIRED | NOT_APPLICABLE |
| DEP-04-05-012 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | RETIRED | NOT_APPLICABLE |
| DEP-04-05-013 | EXECUTION | CONSTRAINT | UPSTREAM | REF-002 | ACTIVE | PENDING |

Counts: ACTIVE=11, RETIRED=2; satisfaction NOT_APPLICABLE=2, PENDING=1, SATISFIED=7, TBD=3.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 2 |

| SatisfactionStatus | Count |
|---|---:|
| PENDING | 1 |
| SATISFIED | 7 |
| TBD | 3 |

## Run Notes - 2026-09-03 v3 pathway seating (additive UPDATE)

- `TASK + dependency-extract` method applied in-line by the A12 seating tranche (ephemeral Agent 2 generalist; no TASK run record under `_run_records/` because that path is outside the tranche write set); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; `ScopeOfWork.md` re-pinned to that commit in the same tranche.
- Scope of this pass: exactly one new row, `DEP-04-05-013`, making the v3 gate/interface edge consumed by the seated `Remaining` item explicit. Existing rows are preserved byte-identically (no `LastSeen` refresh, no retirement); the full two-pass re-extraction is not claimed for them.
- Evidence: `ScopeOfWork.md` at `ScopeOfWork.md#CLM-009-Requirements`; quote: "Remote MCP, plugins, and non-Anthropic network tools must remain out of current scope unless separately governed.".
- Target resolution: Root-owned targets keep `TargetLocation=TBD` (no Root path is invented); deliverable targets resolve against the applied decomposition.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities; accepted decomposition IDs are preserved (same finding as the Gate-5 refresh).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- A2-B / SCC posture: no objective-relative feedback edge was added or linearized; the post-application audit's nine-node SCC remains a warning-bearing derivative finding.
- Schema validation: `python3 tools/validation/validate_dependencies_schema.py Dependencies.csv` PASS after the append; see `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/DEPENDENCY_REFRESH.md`.

## Run Notes - 2026-09-05 D-APP-110 SCC decompose (UPDATE, one row re-targeted)

- `TASK + dependency-extract` apply run by instance `N14-TASK-DEL-04-05` of `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` (sealed brief; parent HELP_HUMAN); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; run record `_run_records/TASK_RUN_2026-09-05_1013.md`.
- Authority: owner ruling D-APP-110 (`_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md`), amendment v1.3, workbook `SCC_DECOMPOSE_RULINGS.csv`; move basis `docs/CYCLE_DRIVEN_RESOLUTION.md` section 2.3 `decompose` in the `SCC-SAFE-MOVES-001` form.
- DECOMPOSE under D-APP-110 (SD-001): DEP-04-05-010 now targets `DEL-02-05-KEY_STATUS_CONTRACT` (`TargetType=DOCUMENT`; `TargetLocation` at DEL-02-05 `ScopeOfWork.md#CLM-003`; anchor verified present, with CLM-010 DEL-02-05-R03). The coarse deliverable edge `DEL-04-05->DEL-02-05` (cycle 39) is replaced by the document-scoped contract; the deliverable relation is preserved in the row's `Notes`; `LastSeen` refreshed to 2026-09-05; `DependencyType`, `Direction`, evidence, maturity, `SatisfactionStatus` (`TBD`), and `Status` (`ACTIVE`) unchanged.
- Task B (resolution notes on other D-APP-109 rows held here): none — this carrier holds no other D-APP-109 rows, so no `RESOLVED 2026-09-05` note was appended.
- Every other row is byte-identical; no row added, retired, or reordered. This file keeps no per-target-type tally, so ACTIVE, RETIRED, class, and SatisfactionStatus counts are unchanged (ACTIVE 11 / RETIRED 2; ANCHOR 6 / EXECUTION 7; PENDING 1 / SATISFIED 7 / TBD 3).
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present. `DependencyID` values unique.
- Function 5: `validate_dependencies_schema.py Dependencies.csv` PASS; `validate_enum.py TARGET_TYPE DOCUMENT` PASS; `TargetDeliverableID` empty for the DOCUMENT target per schema rule; `git diff --check` clean.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:35:58-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_STATE REF-006 HASH_MISMATCH | ANCHOR=6; EXECUTION=6 |
| 2026-09-03T00:00:00-06:00 | UPDATE (additive, one row) | CONSERVATIVE | applied `d6f6cadb2` SHA-256 `932b890e…168716f` | PROJECT_ID_FORMAT_PROFILE; existing rows preserved without LastSeen refresh | ANCHOR=6; EXECUTION=5; ACTIVE=11; RETIRED=2 |
| 2026-09-05T10:13-0600 (D-APP-110 decompose) | UPDATE | CONSERVATIVE | found at the pinned identity SHA-256 `c7c05169…771e61` | none; one row (DEP-04-05-010) re-targeted to a DOCUMENT contract node, all other rows byte-identical | ANCHOR=6; EXECUTION=5; ACTIVE=11; RETIRED=2 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## Downstream Handoff Notes

- As of 2026-09-05 (D-APP-110 decompose, SD-001) this carrier no longer holds any cycle-participating row: `DEP-04-05-010` is a document-scoped `DOCUMENT` edge to `DEL-02-05-KEY_STATUS_CONTRACT`, and every remaining EXECUTION row is a strict edge of the acyclic approved deliverable graph.
- Every row gates per its `SatisfactionStatus`; no row in this register is held non-gating pending SCC resolution.
- The resulting acyclic strict graph is recorded by the fresh `AUDIT_DEP_CLOSURE` snapshot produced under the same run (node N16); acceptance of that snapshot as the loop's DepClosure pointer remains a separate owner act.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=2; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=9, RETIRED=4. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_PREVIEW_THREE_INTERFACES.csv`; current rows: ACTIVE=9, RETIRED=4. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
