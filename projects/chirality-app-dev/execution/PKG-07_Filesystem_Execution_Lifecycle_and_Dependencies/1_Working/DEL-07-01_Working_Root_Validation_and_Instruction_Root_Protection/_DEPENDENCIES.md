# Dependencies: DEL-07-01 Working Root Validation and Instruction Root Protection

> **Current-source note (2026-09-23):** References below to the former App `Remaining` section and its Depends text record dated extraction evidence. The live status section was retired in the finite App Task Management account. For current work and dependency gating, read `Dependencies.csv`, governing Scope of Work, accepted decisions and the selected work graph. The historical Depends text adds no prerequisite; this note does not change the accepted register rows.


## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-01-001`, `DEP-07-01-002`, `DEP-07-01-003`, `DEP-07-01-005`, `DEP-07-01-006`, `DEP-07-01-007`, `DEP-07-01-008`, `DEP-07-01-009`, `DEP-07-01-012`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: `DEP-07-01-010`, `DEP-07-01-011`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; status: located and used for anchor validation.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] MISSING_DECOMPOSITION`: the explicit decomposition path was available.
- Conservative exclusion: no dependency edge was emitted for `DEL-06-04`; `Guidance.md` identifies the relationship as an inferred coordination note, not an accepted dependency edge.

### 2026-09-05 run (SCA-APP-010 dependency closure, DEP-017/DEP-018 report-only preview)

- Run: `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` instance `N1-TASK-DEL-07-01`; `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`, `ANCHOR_DOC=ScopeOfWork.md`, `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `_STATUS.md` read only for its `## Remaining` section; `_REFERENCES.md` read to resolve document pointers. Excluded as sources: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, `_run_records/**`.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; applied row L357; amended Scope Ledger rows SOW-002 L172 and SOW-084 L254; reverse view L405/L430/L478/L487; OI-008 L602; DEC-025 L634). Companion register SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`.
- Pre-images verified before extraction: `Dependencies.csv` SHA-256 `0584937814e740879a05178547536c49ba9d03ef36bbbc0e6a83c15b4726224c` (5 data rows); `_DEPENDENCIES.md` SHA-256 `a40fe07268822d3247b0f8790c09f91b4a60857f8ab55c71b7e2640b7af2f5c9`.
- Legacy four-document kit (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) no longer exists in this folder. Rows DEP-07-01-001 and DEP-07-01-005 were re-evidenced to live `ScopeOfWork.md`, `_STATUS.md#Remaining`, and decomposition `#L<n>` bytes; no row was retired for lost evidence because every relation is still stated. Rows DEP-07-01-002 and DEP-07-01-003 were refreshed to the live `_CONTEXT.md` traceability line (`SOW-002, SOW-027, SOW-075`) and the amended ledger rows. DEP-07-01-004 (RETIRED) is byte-identical.
- Added anchors: DEP-07-01-006 (SOW-075; on the applied row and in `_CONTEXT.md` since D-APP-80 but never extracted), DEP-07-01-007 (SOW-084; introduced by SCA-APP-010), DEP-07-01-008 (OBJ-006), DEP-07-01-009 (OBJ-008). Objective anchors use `TargetType=UNKNOWN` per the brief's existing objective-anchor convention with the raw reference preserved.
- Added execution rows: DEP-07-01-010 (INTERFACE, DOWNSTREAM, DEL-04-04 consumes the organisation-layer pins; `_STATUS.md#Remaining` and L487), DEP-07-01-011 (INTERFACE, DOWNSTREAM, DEL-02-03 UI touchpoint consumes working-folder validation; L172/L405/L309; `Confidence=MEDIUM`, transferred artifact labelled ASSUMPTION), DEP-07-01-012 (CONSTRAINT, UPSTREAM, K-ROOT-1 applied to both instruction-root layers; L254; REF-002 resolves by pinned hash to `projects/chirality-app-dev/docs/CONTRACT.md` L42).
- Considered and not emitted (information-flow rule; reported, not suppressed): (a) DEL-08-01 — L487 and `_STATUS.md#Remaining` state only an ownership split ("DEL-08-01 owns packaging and conformance checks"); the live sources do not state that DEL-07-01 supplies or consumes a named artifact with DEL-08-01, and the owner of the pin-file contract that both boot verification (DEL-07-01) and packaging checks (DEL-08-01) read is unstated; (b) DEL-06-04 — remains a coordination note (ScopeOfWork.md CLM-026; human ruling X-002 open); (c) `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` — cited by the seated item "only for what the tranche means when complete, never as a queue", so no edge; (d) `frontend/electron/daemon-instruction-root.ts` (D-APP-98) — a conditional write locus, not an edge; (e) SOW-002's "app-scoped set of known folders" (SOW-008, DEL-02-04) — no transfer to or from DEL-07-01 is stated on the amended rows.
- Root-owned semantics: none apply to this carrier (OI-008 covers SOW-010/081/082/083, none of which is on row L357); no `TargetType=EXTERNAL` row was needed.
- Fence results: F1 NONE (DEL-07-01 is not an SCC-001 member; the two deliverable targets DEL-04-04 and DEL-02-03 are not SCC-001 members, so no reverse-edge condition can arise); F2 NONE (every `TargetLocation` is a project-relative path or a `_REFERENCES.md`-pinned document; the DEP-07-01-005 `frontend/...` locations predate the fence and are preserved unchanged); F3 NONE (every new row traces to L357, L172, or L254 prose or the seated `## Remaining` item). `FENCE_F1_CANDIDATES`: none. `FENCE_F2_CANDIDATES`: none. `NEEDS_HUMAN_GRAPH_DECISION`: none.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: `tools/validation/validate_id_format.sh` uses a generic three-digit profile that rejects the accepted App two-digit IDs (`DEL-07-01`, `PKG-07`, `DEP-07-01-NNN`, `SOW-NNN`); no ID was changed. Schema validator VALID (29 columns, 12 data rows); all 25 distinct enum values VALID; exactly one ACTIVE `IMPLEMENTS_NODE`.
- No `[WARNING] FLOATING_NODE`, no `[WARNING] AMBIGUOUS_ANCHOR`, no `[WARNING] MISSING_DECOMPOSITION` for this run.
- The D-APP-56 R5 P45 "current register summary" block below is dated history as of this run; the `## Lifecycle Summary` reflects the 2026-09-05 post-image.
- Report-only preview: this text and the matching `Dependencies.csv` are proposed post-images produced under `AllowedWriteTargets` limited to the run's instance folder; the carrier bytes were not changed by this run. They become the carrier's register only through the owner's review of `PREVIEW.md` and a separately authorized write.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-011 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-07-01`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `bd24fcf27a41fd70a4b13660bd0d7c1173b04852fda0886e55098b9ff270910c`; `_CONTEXT.md` `8a9531135bf47c4468ef3a1308a76c8269be6d946d241e59eac97aa4329e756b`; `_REFERENCES.md` `dd261438c46dea103351d1030422463e50358db9b9761b5161af2fea8902aca1`; `_STATUS.md` `3dde2589888884a19383075163a98d63bd65e0fd521b274f1f3413ad4231af1b`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `fcc4dd3d5aaecea4dc44e895030d14e006400cbb3e406a9bbf27d6b8cfbcd1be`, `_DEPENDENCIES.md` `c930356070e0dc78942022caeefdf43653301c4bd93736840d1ef960c9441b66`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 10 (`LastSeen=2026-09-27`); restated in place 1; kept with a note 0; retired 0; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
  - RE-EVIDENCED DEP-07-01-010 (EXECUTION DOWNSTREAM INTERFACE -> DEL-04-04) ESR-1 (re-evidenced); see the row `Notes`.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.
- ESR-1 re-evidence: DEP-07-01-010 cited the former `_STATUS.md` `## Remaining` section, retired on 2026-09-23. Each is re-anchored in place to a current accepted source that states the dependency: the owner ruling record D-APP-110 (its SD-003 decompose names the row) or the decomposition Scope Ledger allocation (IMPLICIT, MEDIUM). The D-APP-110 record lies outside the workflow's default read boundary and was read because it is the accepted ruling that names these rows. No edge, target, status or satisfaction changed.

### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set.
- Runtime overrides: `SCOPE=DEL-07-01`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `6ac7811824201b7abaf2fdd4b6d208cd2d3c92c56126d2a4aa34114fad29a577` (as amended by SCA-APP-012).
- Source-preservation gate: `ScopeOfWork.md` `bd24fcf27a41fd70a4b13660bd0d7c1173b04852fda0886e55098b9ff270910c`; `_CONTEXT.md` `8a9531135bf47c4468ef3a1308a76c8269be6d946d241e59eac97aa4329e756b`; `_REFERENCES.md` `dd261438c46dea103351d1030422463e50358db9b9761b5161af2fea8902aca1`; `_STATUS.md` `3dde2589888884a19383075163a98d63bd65e0fd521b274f1f3413ad4231af1b`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `a98c4a5fa9242d5e44392fea64e00ea97a6ccb50ababe8114cf67d73d4ccd0b6`, `_DEPENDENCIES.md` `a1150a6693e994f6e445ad27bec27222ef609ef848076e2f96a6cf4d0f34f7b7`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause). Previous extraction: 2026-09-27, `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`; no source text changed since; that text was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 11 (`LastSeen=2026-09-27`); restated in place 0; retired 0; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative `projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no `EvidenceFile`, so the count is unchanged and no row this run changed carries the finding; no EVQ-003, EVQ-004 or DRB-006 finding.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 12 |
| ACTIVE rows | 11 |
| RETIRED rows | 1 |
| ACTIVE ANCHOR rows | 7 |
| ACTIVE EXECUTION rows | 4 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-07-01-001 | ANCHOR | UPSTREAM | OTHER | PKG-07 | ACTIVE | NOT_APPLICABLE |
| DEP-07-01-002 | ANCHOR | UPSTREAM | OTHER | SOW-002 | ACTIVE | NOT_APPLICABLE |
| DEP-07-01-003 | ANCHOR | UPSTREAM | OTHER | SOW-027 | ACTIVE | NOT_APPLICABLE |
| DEP-07-01-004 | EXECUTION | UPSTREAM | CONSTRAINT | REF-006 | RETIRED | NOT_APPLICABLE |
| DEP-07-01-005 | EXECUTION | UPSTREAM | PREREQUISITE | Landed working-root and instruction-root implementation modu… | ACTIVE | SATISFIED |
| DEP-07-01-006 | ANCHOR | UPSTREAM | OTHER | SOW-075 | ACTIVE | NOT_APPLICABLE |
| DEP-07-01-007 | ANCHOR | UPSTREAM | OTHER | SOW-084 | ACTIVE | NOT_APPLICABLE |
| DEP-07-01-008 | ANCHOR | UPSTREAM | OTHER | OBJ-006 | ACTIVE | NOT_APPLICABLE |
| DEP-07-01-009 | ANCHOR | UPSTREAM | OTHER | OBJ-008 | ACTIVE | NOT_APPLICABLE |
| DEP-07-01-010 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-04-04 | ACTIVE | PENDING |
| DEP-07-01-011 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-02-03 | ACTIVE | PENDING |
| DEP-07-01-012 | EXECUTION | UPSTREAM | CONSTRAINT | REF-002 | ACTIVE | PENDING |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 11 |
| Status | RETIRED | 1 |
| SatisfactionStatus | NOT_APPLICABLE | 8 |
| SatisfactionStatus | PENDING | 3 |
| SatisfactionStatus | SATISFIED | 1 |
| RequiredMaturity | TBD | 12 |
| DependencyClass | ANCHOR | 7 |
| DependencyClass | EXECUTION | 5 |
| DependencyType | CONSTRAINT | 2 |
| DependencyType | INTERFACE | 2 |
| DependencyType | OTHER | 7 |
| DependencyType | PREREQUISITE | 1 |

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T19:47:21-0600 | UPDATE | CONSERVATIVE | located | 5 | SOURCE_HASH_MISMATCH |
| 2026-09-05T00:36:54-0600 | UPDATE | CONSERVATIVE | located at pinned identity `c7c05169…771e61` (L357) | 11 | PROJECT_ID_FORMAT_PROFILE |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | ACTIVE=11 (ANCHOR=7; EXECUTION=4) | none |
| 2026-09-27 (`APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `6ac781182420…` (SCA-APP-012 amended) | ACTIVE=11 (ANCHOR=7; EXECUTION=4) | none |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`. This register is deliverable-local; project-graph assembly and cycle handling stay with AGGREGATION and the closure analyzer.
- Accepted upstream: applied decomposition `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; carrier `ScopeOfWork.md` re-pinned to that identity (SCA-APP-010 Gate-5 Current Contract, D-APP-108 seating).
- Cross-deliverable edges to reconcile against the counterpart registers: DEP-07-01-010 (DEL-04-04 should carry the UPSTREAM counterpart for pin consumption under SOW-084), DEP-07-01-011 (DEL-02-03 should carry the UPSTREAM counterpart for working-folder validation under SOW-002). Neither target is an SCC-001 member.
- Open for the owner, not blocking this register: the pin-file contract shared by DEL-07-01 boot verification and DEL-08-01 packaging checks has no stated owner in the live sources (no edge emitted; see Run Notes); DEL-06-04 remains a coordination note under human ruling X-002.
- Closure lifecycle: DEP-07-01-010, -011, -012 are `PENDING` until DEL-07-01-V3-01 merges with review PASS; DEP-07-01-005 stays `SATISFIED` for the landed modules only.

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-130
- **Current counts:** ACTIVE 4; RETIRED 1; NOT_APPLICABLE=4; SATISFIED=1.
- **Correction:** DEP-07-01-005 resolves to landed implementation modules and is SATISFIED.
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

## Current residual-specific interpretation — 2026-09-22

The DEP-017/018 preview described in the dated extraction run is applied in the current register. `tool-path-policy.ts` is retired compatibility provenance, not a current live enforcement locus. Current ordinary instruction-root protection and unresolved live checks are in ScopeOfWork.md CLM-028/029 and the retired-status detail there; historical line anchors and MATCH notes are not current source verification.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

6 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SEMANTIC_19_PREVIEW.csv`; current rows: ACTIVE=11, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
