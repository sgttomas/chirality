# Dependencies: DEL-08-05 Subagent Child Run Records and Artifacts

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-08-05-001`, `DEP-08-05-002`, `DEP-08-05-003`, `DEP-08-05-004`, `DEP-08-05-005`, `DEP-08-05-006`, `DEP-08-05-007`, `DEP-08-05-008`, `DEP-08-05-009`, `DEP-08-05-010`, `DEP-08-05-011`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 11 |
| ACTIVE rows | 11 |
| RETIRED rows | 0 |
| ACTIVE ANCHOR rows | 3 |
| ACTIVE EXECUTION rows | 8 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-08-05-001 | ANCHOR | UPSTREAM | OTHER | SOW-063 | ACTIVE | SATISFIED |
| DEP-08-05-002 | ANCHOR | UPSTREAM | OTHER | OBJ-003 | ACTIVE | SATISFIED |
| DEP-08-05-003 | ANCHOR | UPSTREAM | OTHER | OBJ-007 | ACTIVE | SATISFIED |
| DEP-08-05-004 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-08-04 | ACTIVE | TBD |
| DEP-08-05-005 | EXECUTION | UPSTREAM | PREREQUISITE | Runtime event schema and HarnessEvent | ACTIVE | TBD |
| DEP-08-05-006 | EXECUTION | UPSTREAM | PREREQUISITE | Artifact storage policy | ACTIVE | SATISFIED |
| DEP-08-05-007 | EXECUTION | UPSTREAM | CONSTRAINT | Runtime redaction policy | ACTIVE | TBD |
| DEP-08-05-008 | EXECUTION | UPSTREAM | CONSTRAINT | SDK transcript metadata boundary | ACTIVE | TBD |
| DEP-08-05-009 | EXECUTION | UPSTREAM | CONSTRAINT | Retired unified pipeline run record boundary | ACTIVE | TBD |
| DEP-08-05-010 | EXECUTION | UPSTREAM | CONSTRAINT | D-APP-40 denied child-run allocation boundary | ACTIVE | SATISFIED |
| DEP-08-05-011 | EXECUTION | UPSTREAM | INTERFACE | DEL-08-04 | ACTIVE | TBD |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract run on 2026-05-20T20:55:00-0600 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling honored: `_SEMANTIC.md` was not read or consumed; semantic lensing and P3 enrichment were skipped.
- `ANCHOR_DOC=AUTO` selected `_CONTEXT.md` and `Datasheet.md` traceability fields for explicit identifiers.
- `EXECUTION_DOC_ORDER=AUTO` used `Procedure.md`, `Specification.md`, `Guidance.md`, and `Datasheet.md` for execution prerequisites and constraints.
- No `[WARNING] FLOATING_NODE`: one ACTIVE parent anchor was found.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor was found.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 current authority-corpus reconciliation supersedes the prior PRD source-state warning for this tranche.
- `[RESOLVED] HUMAN_RULING_APPLIED`: D-APP-40 resolves denied child-run allocation semantics; denied `ChildRunRecord` evidence is required only after the runtime reaches the child-run record layer.
- `[RESOLVED] CHILD_OUTPUT_ARTIFACT_EVIDENCE`: ADQ-12 persists over-inline child summaries under session child-output artifacts with parent-turn, task, child-run, tool-use, source-file, checksum, byte-count, truncation, and redaction evidence.
- Schema validation passed: 29 required columns and 10 data rows.
- TASK + dependency-extract semantic refresh on 2026-08-24T00:54:53-0600 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=RECONCILIATION`.
- Runtime declaration: `CHIRALITY_INSTRUCTION_ROOT=/Users/ryan/.codex/worktrees/ef5e/chirality`; the additive V2 declaration cured the earlier fail-closed normalization attempt without changing the sealed brief.
- Decomposition authority used: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, SHA-256 `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md` v19, `ScopeOfWork.md`, existing dependency artifacts, and the exact applied decomposition. `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` were not dependency evidence.
- `ANCHOR_DOC=AUTO` selected `_CONTEXT.md` and the applied decomposition's explicit DEL-08-05/SOW-063/OBJ-003/OBJ-007 mappings. Pass 1 retained one parent anchor and two trace anchors with stable DependencyIDs.
- `EXECUTION_DOC_ORDER=AUTO` used `ScopeOfWork.md` followed by the applied decomposition's DEL-08-04 and DEL-08-05 carrier rows. Pass 2 retained seven supported execution edges and added one distinct class-aware interface edge.
- Descendant-class evidence is deliberately non-conflated: DEP-08-05-004 covers the Chirality-managed class exactly once; DEP-08-05-011 covers the delegated-harness-native class exactly once. Native descent assigns no Agent 0/1/2 role; managed sealed-brief evidence remains distinct.
- E-020 (`DEL-08-05` feedback to `DEL-08-04`) was not present in the allowed source documents or applied decomposition, so this conservative extraction did not surface or invent it. No schedule gate was created and no SCC was silently linearized.
- No `[WARNING] FLOATING_NODE`: one ACTIVE parent anchor was found.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor was found.
- `[WARNING] ID_FORMAT_VALIDATOR_PROJECT_CONVENTION`: `validate_id_format.sh` requires `DEL-[0-9]{3}-[0-9]{2}` and `PKG-[0-9]{3}`, so it rejects the accepted live project identifiers `DEL-08-05`, `DEL-08-04`, and `PKG-08`. The extraction preserves those decomposition-authoritative identifiers; no alternative IDs were invented.
- Schema validation passed: 29 required columns and 11 data rows.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-011 MODIFY set.
- Runtime overrides: `SCOPE=DEL-08-05`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `e6fc2662e5b8f3e08a8b602828283f31025574e979d521dbe4aac21f333c4cb3`; `_CONTEXT.md` `337a22d959dd6974434cd6ab6b6ba7be7aa4d9560938ee6b3851a42d8b676d1f`; `_REFERENCES.md` `08f14e6b91d8b44280958a7701286e7529b71d58b841e127388dcc0deeb5bd26`; `_STATUS.md` `aaa583ef134d721a29aa518e03212f0379f19d851b4a149889d3bac689dca627`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `7261ccd9edd95c789f23dd6f0d6eb869309e28ab16808aa296cb5f977c1e281a`, `_DEPENDENCIES.md` `3f232964125c4cb7daaa9af76be5c23f65a6782c8fd3dc8c67748c1fe0462fb1`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 11 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-08-24T00:54:53-0600 | UPDATE | CONSERVATIVE | Exact post-application SHA-256 `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f` | 11 | ID validator/project convention mismatch |
| 2026-06-21T05:00:00-0600 | ADQ-12 | CONSERVATIVE | D-APP-38 current authority corpus, D-APP-40 child-run taxonomy, and child-output artifact evidence applied | 10 | none |
| 2026-06-21T03:00:20-0600 | ADQ-05 | CONSERVATIVE | D-APP-38 current authority corpus and D-APP-40 child-run taxonomy applied | 10 | none |
| 2026-05-20T20:55:00-0600 | UPDATE | CONSERVATIVE | Found and used explicit path | 10 | superseded source-state warning; superseded denied-allocation ruling request |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | ACTIVE=11 (ANCHOR=3; EXECUTION=8) | none |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 11 |
| SatisfactionStatus | SATISFIED | 5 |
| SatisfactionStatus | TBD | 6 |
| RequiredMaturity | SEMANTIC_READY | 11 |
| DependencyClass | ANCHOR | 3 |
| DependencyClass | EXECUTION | 8 |
| DependencyType | CONSTRAINT | 4 |
| DependencyType | INTERFACE | 1 |
| DependencyType | OTHER | 3 |
| DependencyType | PREREQUISITE | 3 |

## Downstream Handoff Notes

- Consumer context: `RECONCILIATION`.
- Consume DEP-08-05-004 and DEP-08-05-011 as distinct class-aware evidence flows; do not merge managed sealed-brief evidence with native-origin lineage evidence.
- The absent E-020 source signal remains non-gating and is not represented in this local register. A downstream graph consumer may preserve an independently governed E-020 edge only from its accepted source, without turning it into schedule authority.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-139
- **Current counts:** ACTIVE 10; RETIRED 0; SATISFIED=5; TBD=5.
- **Correction:** DEP-08-05-006 alone is newly SATISFIED; other documentary rows remain unchanged.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
