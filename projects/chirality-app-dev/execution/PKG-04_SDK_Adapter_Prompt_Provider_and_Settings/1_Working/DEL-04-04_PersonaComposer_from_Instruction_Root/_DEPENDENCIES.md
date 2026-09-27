# Dependencies: DEL-04-04 PersonaComposer from Instruction Root

> **Current-source note (2026-09-23):** References below to the former App `Remaining` section and its Depends text record dated extraction evidence. The live status section was retired in the finite App Task Management account. For current work and dependency gating, read `Dependencies.csv`, governing Scope of Work, accepted decisions and the selected work graph. The historical Depends text adds no prerequisite; this note does not change the accepted register rows.


## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-04-04-001, DEP-04-04-002, DEP-04-04-003, DEP-04-04-004, DEP-04-04-005, DEP-04-04-006, DEP-04-04-007, DEP-04-04-009, DEP-04-04-010, DEP-04-04-011, DEP-04-04-012, DEP-04-04-013, DEP-04-04-014

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-04-04-008

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 13 |
| RETIRED rows | 1 |
| ACTIVE ANCHOR rows | 7 |
| ACTIVE EXECUTION rows | 6 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-04-04-001 | ANCHOR | UPSTREAM | OTHER | PKG-04 | ACTIVE | NOT_APPLICABLE |
| DEP-04-04-002 | ANCHOR | UPSTREAM | OTHER | SOW-017 | ACTIVE | NOT_APPLICABLE |
| DEP-04-04-003 | ANCHOR | UPSTREAM | OTHER | SOW-030 | ACTIVE | NOT_APPLICABLE |
| DEP-04-04-004 | EXECUTION | UPSTREAM | INTERFACE | DEL-04-02 | RETIRED | NOT_APPLICABLE |
| DEP-04-04-005 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-08-01 | ACTIVE | TBD |
| DEP-04-04-006 | EXECUTION | UPSTREAM | INTERFACE | DEL-08-02 | ACTIVE | TBD |
| DEP-04-04-007 | EXECUTION | UPSTREAM | CONSTRAINT | docs/PRD.md | ACTIVE | SATISFIED |
| DEP-04-04-008 | EXECUTION | DOWNSTREAM | HANDOVER | Runtime boundary boot/session fingerprint integration | ACTIVE | TBD |
| DEP-04-04-009 | ANCHOR | UPSTREAM | OTHER | SOW-081 | ACTIVE | NOT_APPLICABLE |
| DEP-04-04-010 | ANCHOR | UPSTREAM | OTHER | SOW-084 | ACTIVE | NOT_APPLICABLE |
| DEP-04-04-011 | ANCHOR | UPSTREAM | OTHER | OBJ-004 | ACTIVE | NOT_APPLICABLE |
| DEP-04-04-012 | ANCHOR | UPSTREAM | OTHER | OBJ-007 | ACTIVE | NOT_APPLICABLE |
| DEP-04-04-013 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-03 | ACTIVE | PENDING |
| DEP-04-04-014 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-01 | ACTIVE | PENDING |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract update run timestamp: 2026-05-20T19:35:58-0600.
- Runtime overrides: `SCOPE=DEL-04-04`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition path used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; existing `_SEMANTIC.md` was not read or consumed.
- Anchor document selection: `Datasheet.md` and `_CONTEXT.md` traceability, validated against decomposition PKG-04 / DEL-04-04 / SOW rows.
- Execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, then `Datasheet.md`.
- Parent anchor status: one ACTIVE `IMPLEMENTS_NODE` anchor found; no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` records `docs/PRD.md` as `HASH_MISMATCH`; PRD-only details remain constrained until accepted snapshot confirmation.
- [WARNING] UNKNOWN_TARGET: runtime boundary boot/session fingerprint integration is explicit, but the local evidence does not name a stable consuming deliverable/interface; target preserved as `UNKNOWN` / `TBD`.
- No downstream handoff section was added because `CONSUMER_CONTEXT=NONE`.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-011 MODIFY set.
- Runtime overrides: `SCOPE=DEL-04-04`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `6802477a19044ba536440fe8ecfed62623f6af73a3ea7ab72f2feee7a10a2b54`; `_CONTEXT.md` `9f401fcfeabf20892dbe02ad8cf71b2ead42b1b2800511198a3c3c3898dd3b67`; `_REFERENCES.md` `d62da0edb57cd91706f6d9c1a197bb79019328874b6042278a39e679b0bdd941`; `_STATUS.md` `312d309918a46ea4ee645d824f3999893c55b8e01281f64b9cf09f2d12310555`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `5203de4e3b3c268283c3a593aef884b4e18d50ccb3d7212220d0b74f0aa2e8ab`, `_DEPENDENCIES.md` `170ee896faa8568c7962e742bb3d70bd526447e599cd6869063f4f628e5a0a09`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 13 (`LastSeen=2026-09-27`); restated in place 0; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set.
- Runtime overrides: `SCOPE=DEL-04-04`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `6802477a19044ba536440fe8ecfed62623f6af73a3ea7ab72f2feee7a10a2b54`; `_CONTEXT.md` `9f401fcfeabf20892dbe02ad8cf71b2ead42b1b2800511198a3c3c3898dd3b67`; `_REFERENCES.md` `d62da0edb57cd91706f6d9c1a197bb79019328874b6042278a39e679b0bdd941`; `_STATUS.md` `312d309918a46ea4ee645d824f3999893c55b8e01281f64b9cf09f2d12310555`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `304c619a22a63dc38c7d0751562aca36747f664a0ececd95feb8cd90ef01c401`, `_DEPENDENCIES.md` `0fcf2ac8702b3c5cb4895f38269000bd604d78b0869d905cf195149f881a27f0`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-27, `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`; no source text changed since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 13 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (report-only preview)

- Run: `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` instance `N1-TASK-DEL-04-04`; `TASK + dependency-extract` as a Claude Code subagent dispatched by HELP_HUMAN; report-only preview under SCA-APP-010 `FUTURE_WRITE_SET.csv` rows DEP-011 and DEP-012. This file is the proposed post-image; it becomes live only when the owner accepts the preview.
- Runtime overrides: `SCOPE=DEL-04-04_PersonaComposer_from_Instruction_Root`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ApplyEdits=false`. `DOC_ROLE_MAP` default not used because the brief fixed the document roles.
- Source boundary: `_STATUS.md` was read as execution evidence only for its `## Remaining` section (seated item `DEL-04-04-V3-01` `Depends`, `Write locus`, and gate lines); `_REFERENCES.md` resolved document pointers only. `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_INSP-03_DEL-04-04.md`, and `_run_records/**` were excluded. No source document was modified.
- Decomposition authority found at the pinned identity: SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, basis `origin/main` `d66395d101143df68d956984f7ab93f5027418ec`; companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`. Applied row L329; amended ledger rows SOW-081 L251 and SOW-084 L254; reverse view L484 and L487; OI-008 L602; DEC-025 L634.
- Pass 1 (ANCHOR): parent anchor DEP-04-04-001 preserved and refreshed; SOW-017 and SOW-030 anchors (DEP-04-04-002, DEP-04-04-003) refreshed because both remain on the applied row; SOW-081 and SOW-084 anchors added as DEP-04-04-009 and DEP-04-04-010; OBJ-004 and OBJ-007 trace anchors added as DEP-04-04-011 and DEP-04-04-012 using the existing `TargetType=UNKNOWN` objective convention. No anchor was retired because no scope ref left the applied row.
- Pass 2 (EXECUTION): DEP-04-04-005, -006, -007, and -008 re-evidenced from the retired four-document kit to live `ScopeOfWork.md` bytes (PC-REQ-001, PC-REQ-005, CLM-029, CLM-018). DEP-04-04-013 (DEL-07-03 governed workflow file contract the seam reads) and DEP-04-04-014 (DEL-07-01 organisation-layer protection and pin the composer trusts) added from the seated `Remaining` item and the SOW-081/SOW-084 amended rows. DEP-04-04-004 retained byte-identical as RETIRED under RUL-SCC-001-TRANCHE-001.
- Not emitted (information-flow rule): no DEL-02-02 edge, because no local source states what the Workflows view supplies to the composer beyond ownership of the view; no DEL-03-02 or other SCC-001 edge, because no local source states a transfer; no Root-owned `EXTERNAL` row, because this carrier's applied row consumes none of the OI-008 Root semantics (login home, `proposal.*` events, delegation-policy field).
- Fence results: F1 (SCC-001 membership) NONE; F2 (Root path) NONE; F3 (permitted effect) NONE. `FENCE_F1_CANDIDATES` none; `FENCE_F2_CANDIDATES` none.
- NEEDS_HUMAN_GRAPH_DECISION: DEP-04-04-004. The DEL-04-02 resolved mode/tool-surface relation is restated in live bytes (`ScopeOfWork.md` CLM-017 and CLM-025) but the row stays RETIRED per RUL-SCC-001-TRANCHE-001; reactivating it would recreate the DEL-04-02 <-> DEL-04-04 bidirectional pair against ACTIVE DEP-04-02-007. Default proposed: keep RETIRED; no change was made.
- CONFLICT (non-blocking): `_CONTEXT.md#Traceability` still lists `CoversScopeItems | SOW-017, SOW-030` while the applied row L329 and the `ScopeOfWork.md` front matter list SOW-017, SOW-030, SOW-081, SOW-084. The applied row controls; the anchors follow it. Surfaced for the WI alignment owner.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities (`PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, `SOW-NNN`); OBJ IDs pass. No accepted ID was changed.
- [WARNING] UNKNOWN_TARGET: DEP-04-04-008 consuming deliverable/interface remains `UNKNOWN` / `TBD`; the fingerprint payload now includes the organisation-layer pin and roadmap hash per the seated item.
- [WARNING] INSTRUCTION_ROOT_ENV: `CHIRALITY_INSTRUCTION_ROOT` was not set in the dispatch shell; `INSTRUCTION_ROOT` was resolved to `REPO_ROOT` per `docs/TYPES.md` (root-product development) and the brief's repo-root-relative `agents/` and `skills/` paths. ASSUMPTION recorded in the run record.
- [RESOLVED] PRD_HASH_MISMATCH: `_REFERENCES.md` REF-006 is MATCH under D-APP-38; DEP-04-04-007 re-evidenced and marked SATISFIED (PROPOSAL; owner may prefer RETIRED).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present. Schema: `validate_dependencies_schema.py` VALID, 29 columns, 14 data rows; all emitted enum values VALID; `DependencyID` unique; `FromDeliverableID=DEL-04-04` on every row.

## Run History

| Timestamp | Mode | Strictness | Decomposition | ACTIVE Anchors | ACTIVE Execution | Warnings |
|---|---|---|---|---:|---:|---|
| 2026-05-20T19:35:58-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found | 3 | 5 | PRD_HASH_MISMATCH; UNKNOWN_TARGET |
| 2026-09-05T00:37:34-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at pinned identity `c7c05169...771e61` (commit `dbd812a5`) | 7 | 6 | PROJECT_ID_FORMAT_PROFILE; UNKNOWN_TARGET; INSTRUCTION_ROOT_ENV; NEEDS_HUMAN_GRAPH_DECISION (DEP-04-04-004) |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | ACTIVE=13 (ANCHOR=7; EXECUTION=6) | ACTIVE=13 (ANCHOR=7; EXECUTION=6) | none |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | ACTIVE=13 (ANCHOR=7; EXECUTION=6) | ACTIVE=13 (ANCHOR=7; EXECUTION=6) | none |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 13 |
| Status | RETIRED | 1 |
| SatisfactionStatus | NOT_APPLICABLE | 8 |
| SatisfactionStatus | PENDING | 2 |
| SatisfactionStatus | SATISFIED | 1 |
| SatisfactionStatus | TBD | 3 |
| RequiredMaturity | SEMANTIC_READY | 14 |
| DependencyClass | ANCHOR | 7 |
| DependencyClass | EXECUTION | 7 |
| DependencyType | CONSTRAINT | 1 |
| DependencyType | HANDOVER | 1 |
| DependencyType | INTERFACE | 4 |
| DependencyType | OTHER | 7 |
| DependencyType | PREREQUISITE | 1 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor (DEP-04-04-001), four scope-ref trace anchors (SOW-017, SOW-030, SOW-081, SOW-084), two objective trace anchors (OBJ-004, OBJ-007), four re-evidenced ACTIVE execution rows (DEP-04-04-005 to -008), two new ACTIVE upstream interface rows (DEP-04-04-013 DEL-07-03; DEP-04-04-014 DEL-07-01), and one retained RETIRED row (DEP-04-04-004).
- Cross-register observation for reconciliation only (not a source for this register): DEL-04-02 `DEP-04-02-007` self-declares consumption of PersonaComposer output, and DEL-08-02 `DEP-08-02-012` declares the shared persona-name contract downstream to DEL-04-04; DEP-04-04-008's consumer stays `UNKNOWN` until an accepted local source names it.
- Graph posture: DEL-04-04 is not a member of SCC-001; no new edge targets an SCC-001 member; DEP-04-04-004 remains the owner-ruled retired reciprocal. Resolve the DEP-04-04-004 question under `docs/CYCLE_DRIVEN_RESOLUTION.md` before any reactivation.
- Open items for the seated work: DEP-04-04-013 and -014 are PENDING until `DEL-07-03-V3-01` lands and `DEL-07-01-V3-01` is selected per the `_STATUS.md` gate line.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-123
- **Current counts:** ACTIVE 7; RETIRED 1; NOT_APPLICABLE=4; TBD=4.
- **Correction:** DEP-04-04-004 is RETIRED; range citations exclude that row.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
- 2026-09-05 note: the counts above are the dated D-APP-56 mirror; the Lifecycle Summary above supersedes them after the SCA-APP-010 dependency-closure pass.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/core/src/instruction-basis-store.ts`, `tests/instruction-basis-and-method-transition.test.ts`, `packages/daemon/src/codex-supervisor.ts`; App `frontend/electron/main.ts` instruction/service configuration; retained `frontend/src/lib/harness/persona-manager.ts` is compatibility evidence. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=13; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SEMANTIC_19_PREVIEW.csv`; current rows: ACTIVE=13, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
