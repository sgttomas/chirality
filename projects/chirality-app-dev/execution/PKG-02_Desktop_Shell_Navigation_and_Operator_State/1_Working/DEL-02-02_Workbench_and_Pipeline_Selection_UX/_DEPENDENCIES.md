# Dependencies: DEL-02-02 Right-Panel Coordination, Workflows, and Proposal UX

> **Current-source note (2026-09-23):** References below to the former App `Remaining` section and its Depends text record dated extraction evidence. The live status section was retired in the finite App Task Management account. For current work and dependency gating, read `Dependencies.csv`, governing Scope of Work, accepted decisions and the selected work graph. The historical Depends text adds no prerequisite; this note does not change the accepted register rows.


## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

See the current formal `Dependencies.csv` rows whose Direction is UPSTREAM; satisfaction and gates are read from that register, not inferred here.

## Declared Downstream

See the current formal `Dependencies.csv` rows whose Direction is DOWNSTREAM. No new dependency or status is created by this descriptive mirror.

## Current Extracted Dependency Summary — 2026-09-22

Superseded on 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`): the current register summary is under `## Extracted Dependency Register` below. The dated table of this section is kept in git history.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK + dependency-extract ran with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition path used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (found).
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was not read or consumed per human ruling.
- Anchor doc selected: `Datasheet.md`; execution doc order selected: `Specification.md`, `Guidance.md`, `Procedure.md`.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` records a hash mismatch for `docs/PRD.md`; dependency extraction treated this as a source warning, not a blocker.
- [WARNING] SOW_007_OWNER_OVERLAP: `_CONTEXT.md` and the deliverable ledger list SOW-007 under DEL-02-02, while the scope ledger marks PKG-08 / DEL-08-03 as primary owner for Pipeline selectors. Rows preserve this as conflict/TBD rather than resolving it.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.

### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)

- Run: `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on 2026-09-27 (verbatim in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md`). Role: SCA-APP-011 MODIFY deliverable.
- Runtime overrides: `SCOPE=DEL-02-02`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.
- Decomposition authority: FOUND, SHA-256 `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` (as amended by SCA-APP-011).
- Source-preservation gate: `ScopeOfWork.md` `6cb61fe4fd0c1b6678c6f6655c2350439e9dec335cd8c3879183b4494c555582`; `_CONTEXT.md` `5cf78966a568cea0238de37ac8ec37e0ef44f01bb02eaae9d5086f66f6ee5d28`; `_REFERENCES.md` `14952d205dc7b30daf8b6cc662a3583031c5b610caa9b2f2261f222a2ae63aff`; `_STATUS.md` `b8b706625f1c8c9721b8bfc54c27821a1091549b90004cd5aeb5bae380857daa`; read-only and unchanged by this run.
- Pre-images: `Dependencies.csv` `19c2d69e37550feee87ca885b7b3dda6ca073606fa7ea530391a55026389db0b`, `_DEPENDENCIES.md` `43424bcece77c23a7c60ffb1ebaad17dc805a2ca7c17a726ac10bfb8c7b29161`.
- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows already recorded.
- Results: re-seen 13 (`LastSeen=2026-09-27`); restated in place 1; kept with a note 0; retired 5; added 0; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` 1. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted.
  - RETIRED DEP-02-02-005 (EXECUTION UPSTREAM INTERFACE -> DEL-02-01) DX-01; see the row `Notes`.
  - RETIRED DEP-02-02-006 (EXECUTION UPSTREAM INTERFACE -> DEL-02-03) DX-02; see the row `Notes`.
  - RETIRED DEP-02-02-007 (EXECUTION UPSTREAM INTERFACE -> DEL-07-04) DX-03; see the row `Notes`.
  - RETIRED DEP-02-02-008 (EXECUTION UPSTREAM INTERFACE -> DEL-07-05) DX-04; see the row `Notes`.
  - RETIRED DEP-02-02-009 (EXECUTION UPSTREAM CONSTRAINT -> DEL-08-03) DX-05; see the row `Notes`.
  - RE-EVIDENCED DEP-02-02-022 (EXECUTION UPSTREAM INTERFACE -> DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1) ESR-1 (re-evidenced); see the row `Notes`.
  - HELD DEP-02-02-021 (EXECUTION UPSTREAM PREREQUISITE -> DEL-02-03) ESR-1 (retire candidate); see the row `Notes`.
- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; entries skipped 0.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` row (1).
- Function 5 checks (`execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/FUNCTION5_CHECKS.json`): `validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID (`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` (`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts match `Dependencies.csv`.
- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves `EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, EVQ-004 or DRB-006 finding.
- ESR-1 re-evidence: DEP-02-02-022 cited the former `_STATUS.md` `## Remaining` section, retired on 2026-09-23. Each is re-anchored in place to a current accepted source that states the dependency: the owner ruling record D-APP-110 (its SD-003 decompose names the row) or the decomposition Scope Ledger allocation (IMPLICIT, MEDIUM). The D-APP-110 record lies outside the workflow's default read boundary and was read because it is the accepted ruling that names these rows. No edge, target, status or satisfaction changed.
- [WARNING] EVIDENCE_SOURCE_RETIRED: DEP-02-02-021 cites the former `_STATUS.md` `## Remaining` section, retired by the owner-directed 2026-09-23 finite Task Management account. That accepted instrument preserved the rows (FINAL_CLOSEOUT.md: 'the accepted Dependencies.csv rows and source quotes remain unchanged'; the current-source note at the top of this file directs gating to `Dependencies.csv`) and takes precedence over the workflow's own unseen-row retirement, so they stay ACTIVE with `LastSeen` unchanged. No current source states them; they are retire candidates proposed to the owner (ESR-1 in `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/DEPENDENCY_EXTRACT_RESULTS.md`).

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (UPDATE)

- Authorization: SCA-APP-010 `FUTURE_WRITE_SET.csv` rows `DEP-003` and `DEP-004`, triggered by the owner's 2026-09-05 acceptance of the WORKING_ITEMS alignment; previewed report-only by `N1-TASK-DEL-02-02` (v1 preview, then the amendment v1.1 rerun) and applied by the reviewed N3 write under run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`.
- Brief amendment v1.1 (HELP_HUMAN supervisory disposition after fan-in of the thirteen N1 previews; `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md`): the fan-in simulation showed that fifteen newly proposed deliverable edges across nine carriers lie on cycles collectively (they would merge SCC-001 into a 20-node SCC and create a new two-node SCC) while any one alone changes nothing; choosing among them would be a cut, which `docs/CYCLE_DRIVEN_RESOLUTION.md` makes human-gated. Six of this carrier's proposed rows are therefore held as non-emitted proposals for the owner's separate transaction and removed from this register; their IDs stay reserved and are not reused. This is not a register deletion (the rows were never written to the carrier) and not an owner ruling.
- Runtime overrides: `SCOPE=DEL-02-02_Workbench_and_Pipeline_Selection_UX`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`. `DOC_ROLE_MAP=DEFAULT` was not needed because every doc role was explicit.
- Decomposition found at the pinned identity: SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (matches the `ScopeOfWork.md` front matter `decomposition_basis`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` naming SCA-APP-010; basis `origin/main` `d66395d101143df68d956984f7ab93f5027418ec`.
- Sources: `ScopeOfWork.md` (front matter, Purpose and Objective Traceability, SCA-APP-010 Gate-5 Current Contract, CLM blocks as dated compatibility history), `_CONTEXT.md`, `_STATUS.md` `## Remaining` only (seated items DEL-02-02-V3-01 to V3-04; lifecycle, history, and approval fields excluded), `_REFERENCES.md` for pointer resolution, and the applied decomposition at row L308, Scope Ledger rows SOW-006 L176, SOW-081 L251, SOW-082 L252, reverse view L404 to L487, OI-008 L602, DEC-025 L634. `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, and `_run_records/**` were not used.
- Pass 1 (ANCHOR): parent anchor DEP-02-02-001 preserved and re-evidenced to `ScopeOfWork.md#CLM-002` with the canonical PKG-02 label from L280. SOW-006 (DEP-02-02-002) and OBJ-001 (DEP-02-02-004) preserved and re-evidenced to `ScopeOfWork.md#Purpose and Objective Traceability`. New trace anchors DEP-02-02-010 (SOW-081), DEP-02-02-011 (SOW-082), and DEP-02-02-012 (OBJ-007) added from the front matter and applied row L308; objectives keep the existing `TargetType=UNKNOWN` convention. DEP-02-02-003 (SOW-007) retired: SOW-007 is no longer on applied row L308 and DEC-025 L634 retired its presentation half.
- Pass 2 (EXECUTION): legacy-kit rows DEP-02-02-005 to DEP-02-02-009 re-evidenced to live `ScopeOfWork.md` bytes (`DEL-02-02-REQ-002`, `CLM-025`, `DEL-02-02-REQ-003`, and the SCA-APP-010 controlling section); they remain stated as dated compatibility history for the retained Workbench/Pipeline code, so they stay ACTIVE at `Confidence=MEDIUM` with a retirement PROPOSAL tied to a future owner act. New rows emitted: DEP-02-02-013 (DEL-07-03 workflow file contract), 014 (DEL-06-03 `propose` tool), 016 (Root DEL-02-10 acceptance, EXTERNAL/TBD), and 021 (DEL-02-03 right-panel view-switcher host). The v1 preview also proposed rows 015, 017, 018, 019, 020, and 022; those were held under amendment v1.1 (next six bullets) and were emitted on 2026-09-05 under D-APP-109 (see the D-APP-109 Run Notes section below).
- EMITTED under D-APP-109 (H-002): DEP-02-02-015 — DEL-02-02 UPSTREAM INTERFACE to DEL-05-02 (live `proposal.*` consumption through the App HarnessEvent path after Root acceptance) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-003): DEP-02-02-017 — DEL-02-02 UPSTREAM INTERFACE to DEL-08-05 (recorded managed and native descendant records presented by the Who is working view) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-004): DEP-02-02-018 — DEL-02-02 UPSTREAM INTERFACE to DEL-05-04 (replay lens and Agent projection semantics composed by selected-session presentation) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-005): DEP-02-02-019 — DEL-02-02 UPSTREAM CONSTRAINT to DEL-08-04 (role/delegation semantics behind the role-entry controls and posture labels) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-006): DEP-02-02-020 — DEL-02-02 UPSTREAM CONSTRAINT to DEL-08-02 (routing, guarded selection, and legacy compatibility semantics behind recorded selections and query tests) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- EMITTED under D-APP-109 (H-007): DEP-02-02-022 — DEL-02-02 UPSTREAM INTERFACE to DEL-02-04 (chat-rung and declined-trigger convenience fields consumed by the rung forms and the proposal card) — cycle-participating, non-gating until the SCC is resolved by a recorded move
- Cross-references reconciled to the holds: the `Notes` of DEP-02-02-011 and DEP-02-02-014 now point to held proposal H-002 (DEP-02-02-015 reserved) instead of to a register row; no other field of those rows changed.
- Not emitted (no named artifact transfer stated for this carrier): DEL-04-04 roadmap-injection seam (both DEL-02-02 and DEL-04-04 consume the DEL-07-03 file contract; no direct transfer is stated), DEL-08-01 instruction-clause conformance, Root DEL-02-11 session-record delegation-policy field (the New workflow form's delegation policy is the file's field under SOW-081), Root DEL-02-09 login home (account row is DEL-02-01), and DEL-02-01 hosting of the right-panel frame (recorded only in the DEP-02-02-021 note).
- Fence F1: NONE. DEL-02-02 is not an SCC-001 member. After amendment v1.1 no row in this register targets an SCC-001 member (the v1 candidate DEP-02-02-015 to DEL-05-02 is held as H-002), and no SCC-001 member holds an ACTIVE row targeting DEL-02-02 (the sole inbound row is DEL-02-01 `DEP-02-01-007`, DOWNSTREAM supply), so no cycle through this carrier is created.
- Fence F2: NONE. Every `TargetLocation` is under the applied decomposition or `TBD`; the Root-owned target (DEP-02-02-016) is `EXTERNAL` with `TargetLocation=TBD`.
- Fence F3: NONE. Every emitted new row traces to applied row L308 prose, amended rows SOW-081/SOW-082, OI-008, or a seated `## Remaining` Depends line; no edge was inferred from SCC ordering, schedule, or a keep-aligned statement.
- NEEDS_HUMAN_GRAPH_DECISION: none remaining. The v1 preview flagged DEP-02-02-021 (right-panel view-switcher host). Amendment v1.1 C.1 (HELP_HUMAN disposition-class, not an owner ruling) keeps the target at DEL-02-03 with `Confidence=MEDIUM` and an ASSUMPTION note: the evidence is the owner-adopted `_STATUS.md` DEL-02-02-V3-04 Depends line (DEL-02-03-V3-01, D-APP-108); the reason for MEDIUM is that applied rows L307 and L309 are silent about a right-panel view switcher (SOW-001 L404 maps the one-view-at-a-time right panel to DEL-02-01). Any re-target to DEL-02-01 is an owner act.
- [WARNING] CONTEXT_SOW_007_RESIDUE: `_CONTEXT.md#Traceability` still lists SOW-007 under CoversScopeItems and names Workbench/Pipeline views under Anticipated Artifacts, while applied row L308 carries SOW-006, SOW-081, SOW-082. The applied row governs; the residue is an alignment note for the WORKING_ITEMS loop, not a dependency decision.
- [WARNING] V3_01_ROLE_ENTRY_SEATING_CONFLICT: seated item DEL-02-02-V3-01 says the Codex role-entry offer and posture labels are unseated from DEL-02-02 (S-7; former row L294), while applied row L308 places role-entry controls and the posture labels on this carrier; `_STATUS.md` history 2026-09-04 reads V3-01/V3-02 under the applied row. The proposed DEL-08-04 row that recorded this conflict (DEP-02-02-019) is held as H-005; the conflict itself remains an alignment note for the WORKING_ITEMS loop.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` expects `PKG-NNN`, `DEL-NNN-NN`, `DEP-NNN-NN-NNN`, and `SOW-NNNN`; the accepted App decomposition uses `PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, and `SOW-NNN`, so the helper reports those IDs invalid by its generic profile. No accepted ID was changed.
- Schema: `validate_dependencies_schema.py` VALID, 29 columns, 16 data rows; every emitted enum value VALID under `validate_enum.py`; `DependencyID` unique (reserved IDs 015, 017, 018, 019, 020, and 022 are absent by design); `FromDeliverableID=DEL-02-02` on every row; every ACTIVE row's `SourceRef` heading or ID and `EvidenceQuote` resolve to live bytes; every non-`TBD` `TargetLocation` line begins with its `TargetRefID`.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present. No `[WARNING] FLOATING_NODE`; no `[WARNING] AMBIGUOUS_ANCHOR`; no `[WARNING] MISSING_DECOMPOSITION`.
- `FromDeliverableName` refreshed on every row to the applied row L308 display name; the stable ID `DEL-02-02` and the physical folder name are unchanged.

## Run Notes - 2026-09-05 D-APP-109 held-edge emission (UPDATE)

- Authorization: owner ruling D-APP-109 (`execution/_Coordination/_DECISIONS/D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md`; owner direction 2026-09-05 to incorporate the fifteen held edges), plan amendment v1.2 node N9 (`AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.2_OWNER_RULING.md`), and SCA-APP-010 `FUTURE_WRITE_SET.csv` rows `DEP-003`/`DEP-004`; instance `N9-TASK-DEL-02-02` (TASK + dependency-extract, apply mode). Pre-images verified before the write: `Dependencies.csv` `d4f6dad83cc9538186214b6ab9a116c85c6ae2a8578acfb5a65acd56e61c3cff`, `_DEPENDENCIES.md` `adeb89260b62b2a86268b99505f08a6df2ea2eb98a22185961767fbad09b1df0`.
- Runtime overrides: `SCOPE=DEL-02-02_Workbench_and_Pipeline_Selection_UX`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _STATUS.md]` (evidence re-verification only; no new extraction from prose); `ANCHOR_DOC=ScopeOfWork.md` (Pass 1 unchanged); `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _STATUS.md]`.
- Decomposition found at the pinned identity: SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed; matches); every emitted `TargetLocation` line begins with `| <TargetDeliverableID> | <TargetName> |` (L310, L337, L339, L369, L371, L372).
- Row content sources: `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv` rows H-002 to H-007 (Statement, EvidenceFile, SourceRef, EvidenceQuote, Confidence, epistemic Notes as captured from the v1 post-image) and `instances/N1-TASK-DEL-02-02/PREVIEW.md` section 3a (direction, type, target, satisfaction status). Every `EvidenceFile#SourceRef` heading and every `EvidenceQuote` was re-verified against the live `ScopeOfWork.md` (SCA-APP-010 Gate-5 Current Contract, L93 to L95 and L112) and `_STATUS.md` `## Remaining` (L53) bytes at write time.
- Pass 1 (ANCHOR): no change; the parent anchor DEP-02-02-001 and the trace anchors are untouched. Pass 2 (EXECUTION): the six reserved rows DEP-02-02-015 (DEL-05-02, INTERFACE, HIGH, PENDING), 017 (DEL-08-05, INTERFACE, HIGH, PENDING), 018 (DEL-05-04, INTERFACE, HIGH, TBD), 019 (DEL-08-04, CONSTRAINT, MEDIUM, PENDING), 020 (DEL-08-02, CONSTRAINT, MEDIUM, TBD), and 022 (DEL-02-04, INTERFACE, MEDIUM, PENDING) are emitted at their numeric positions with `Origin=EXTRACTED`, `Explicitness=EXPLICIT`, `FirstSeen=LastSeen=2026-09-05`, `Status=ACTIVE`; every pre-existing row is byte-identical; no row deleted or retired.
- Each emitted row's `Notes` carries the held proposal's epistemic note followed by the D-APP-109 clause: `EMITTED 2026-09-05 under D-APP-109 (H-nnn). CYCLE_PARTICIPATING: this edge lies inside an unresolved SCC (the enlarged SCC-001) after emission and is non-gating ... until that SCC is resolved by a recorded decompose, invert, merge, or cut move (docs/CYCLE_DRIVEN_RESOLUTION.md).`
- SCC posture (supersedes the Fence F1 statement of the SCA-APP-010 closure Run Notes above): D-APP-109 accepts the fifteen held edges across nine carriers together, which merges the live nine-node SCC-001 into a larger SCC and creates a new two-node SCC (DEL-06-03/DEL-08-01); the six rows emitted here are cycle-participating and non-gating until that SCC is resolved by a recorded move. No SCC is resolved or linearized by this write; the fresh `AUDIT_DEP_CLOSURE` run (amendment v1.2 node N11) records the post-emission SCC picture. The seated items' own `Depends` lines and named gates remain the executable ordering.
- Residual cross-references reported, not changed: the `Notes` of DEP-02-02-011 and DEP-02-02-014 still describe DEP-02-02-015 as "held as H-002 (DEP-02-02-015 reserved; amendment v1.1)", and the H-002 note preserved on DEP-02-02-015 still carries its per-edge F1 sentence ("this UPSTREAM edge does not make DEL-02-02 an SCC-001 member", true of the edge alone); the brief keeps existing rows byte-identical and the held note verbatim, so both are superseded by the clause and by this section rather than rewritten. The WARNING bullets of the closure Run Notes that name DEP-02-02-019 as "held as H-005" are likewise superseded by its emission.
- `_CONTEXT.md` was not read or written by this run: its alignment to the applied row (CONTEXT_SOW_007_RESIDUE) is the concurrent N8 write under D-APP-109 point 2, and its status is not asserted here. V3_01_ROLE_ENTRY_SEATING_CONFLICT is carried unchanged on DEP-02-02-019's note.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: unchanged (generic three-digit helper profile versus accepted App two-digit IDs); no accepted ID changed.
- Schema: `validate_dependencies_schema.py` VALID, 29 columns, 22 data rows; every emitted enum value VALID under `validate_enum.py`; `DependencyID` unique (001 to 022 all present); `FromDeliverableID=DEL-02-02` on every row; `git diff --check` clean; LF, no trailing whitespace, final newline.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present. No `[WARNING] FLOATING_NODE`; no `[WARNING] AMBIGUOUS_ANCHOR`; no `[WARNING] MISSING_DECOMPOSITION`.

## Run Notes - 2026-09-05 D-APP-110 SCC decompose (UPDATE)

- Authorization: owner ruling D-APP-110 (`execution/_Coordination/_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md`; owner direction 2026-09-05 "Decompose the SCC, record it as part of PR #714."), plan amendment v1.3 node N14 (`AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.3_SCC_DECOMPOSE.md`), and the per-row workbook `SCC_DECOMPOSE_RULINGS.csv` (row SD-005 for this carrier); instance `N14-TASK-DEL-02-02` (TASK + dependency-extract, apply mode). Pre-images verified before the write: `Dependencies.csv` `9feb11b0b1aa312eed09fa70de685c6a630f3b5fd717e2b6d774c75e336ec9a0`, `_DEPENDENCIES.md` `2b6d3b9935c857b089a80453e5b6f1c8b18162a30c15a79024ad47499610341d`.
- Move basis: `docs/CYCLE_DRIVEN_RESOLUTION.md` section 2.3 `decompose` in the `SCC-SAFE-MOVES-001` form (`execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/`): a coarse deliverable edge that records consumption of a documented contract is re-targeted to that contract as a `DOCUMENT` node; the row stays ACTIVE with its evidence, and the deliverable relation is preserved in `Notes`. No row retired, cut, merged, inverted, or marked out-of-objective; no PREREQUISITE row changed; no decomposition topology changed.
- Runtime overrides: `SCOPE=DEL-02-02_Workbench_and_Pipeline_Selection_UX`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[SCC_DECOMPOSE_RULINGS.csv]` plus the DEL-02-04 `ScopeOfWork.md` for contract-anchor verification only (no new extraction from prose); `ANCHOR_DOC=ScopeOfWork.md` (Pass 1 unchanged); `EXECUTION_DOC_ORDER=[SCC_DECOMPOSE_RULINGS.csv]`.
- Decomposition found at the pinned identity: SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed; matches); applied row L310 still names DEL-02-04 and its additive v1 workspace-state outputs.
- Contract anchor verified before the write: DEL-02-04 `ScopeOfWork.md` heading `## SCA-APP-010 Gate-5 Current Contract (Controlling)` (L68) is present, and its acceptance obligation 1 reads "Workspace-state changes are additive v1 fields under the existing schema string with rollback-safe migration that preserves prior state." (L100); applied row outputs name the workspace-state schema (additive v1 fields) (L94 to L96).
- DECOMPOSE under D-APP-110 (SD-005): DEP-02-02-022 now targets DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 (`TargetType=DOCUMENT`; `TargetPackageID` and `TargetDeliverableID` cleared; `TargetName` "Additive v1 workspace-state field contract (per-view widths, expand state, chat annotations, known folders, chat rung, declined triggers)"; `TargetLocation` `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`; `LastSeen=2026-09-05`; every other field unchanged; `Notes` appended with the decompose clause naming the replaced edge DEL-02-02->DEL-02-04 and the preserved deliverable relation).
- RESOLVED under D-APP-110 (Task B): the other five D-APP-109 rows this carrier holds, DEP-02-02-015 (DEL-05-02), 017 (DEL-08-05), 018 (DEL-05-04), 019 (DEL-08-04), and 020 (DEL-08-02), received one appended `Notes` clause each ("RESOLVED 2026-09-05: the SCC this row participated in was decomposed under D-APP-110; this row is a strict edge of the acyclic approved graph and gates per its SatisfactionStatus."); no other field of those rows changed. Their earlier CYCLE_PARTICIPATING clause is retained as dated history and is superseded by the RESOLVED clause.
- SCC posture (supersedes the D-APP-109 SCC posture bullet above): after the seven-row decompose across the affected carriers (five edges; this carrier holds SD-005), the strict active deliverable execution graph is acyclic; this carrier no longer holds a cycle-participating row, and every row gates per its `SatisfactionStatus`. The fresh `AUDIT_DEP_CLOSURE` run (amendment v1.3 node N16) records the acyclic graph and the move basis; acceptance of that snapshot as the loop's DepClosure pointer remains a separate owner act.
- Pass 1 (ANCHOR): no change. Pass 2 (EXECUTION): six rows edited as listed; the sixteen other rows are byte-identical; no row added, deleted, or retired; ID order kept; 22 rows, 21 ACTIVE, 1 RETIRED.
- Residual cross-references reported, not changed: the `Notes` of DEP-02-02-011 and DEP-02-02-014 still describe DEP-02-02-015 as held (H-002), and the D-APP-109 Run Notes and Handoff bullets above still carry their dated "cycle-participating, non-gating" wording; the brief keeps every other row byte-identical and dated statements intact, so those are superseded by this section.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: unchanged (generic three-digit helper profile versus accepted App two-digit IDs); no accepted ID changed. CONTEXT_SOW_007_RESIDUE and V3_01_ROLE_ENTRY_SEATING_CONFLICT carried unchanged (`_CONTEXT.md` not read; the DEP-02-02-019 note is unchanged apart from the appended clause).
- Schema: `validate_dependencies_schema.py` VALID, 29 columns, 22 data rows (the DOCUMENT target leaves `TargetDeliverableID` empty per the schema rule); `validate_enum.py` VALID for `TARGET_TYPE DOCUMENT` and every other distinct enum value; `DependencyID` unique (001 to 022); `FromDeliverableID=DEL-02-02` on every row; `git diff --check` clean; LF, no trailing whitespace, final newline.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present. No `[WARNING] FLOATING_NODE`; no `[WARNING] AMBIGUOUS_ANCHOR`; no `[WARNING] MISSING_DECOMPOSITION`.

## Extracted Dependency Register

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`). Dated sections elsewhere in this file keep the counts of their dates.

| Count Type | Count |
|---|---:|
| Total rows | 22 |
| ACTIVE rows | 15 |
| RETIRED rows | 7 |
| ACTIVE ANCHOR rows | 6 |
| ACTIVE EXECUTION rows | 9 |
| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | 1 |
| ACTIVE Origin=DECLARED rows | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-02-02-001 | ANCHOR | UPSTREAM | OTHER | PKG-02 | ACTIVE | TBD |
| DEP-02-02-002 | ANCHOR | UPSTREAM | OTHER | SOW-006 | ACTIVE | TBD |
| DEP-02-02-003 | ANCHOR | UPSTREAM | OTHER | SOW-007 | RETIRED | TBD |
| DEP-02-02-004 | ANCHOR | UPSTREAM | OTHER | OBJ-001 | ACTIVE | TBD |
| DEP-02-02-005 | EXECUTION | UPSTREAM | INTERFACE | DEL-02-01 | RETIRED | NOT_APPLICABLE |
| DEP-02-02-006 | EXECUTION | UPSTREAM | INTERFACE | DEL-02-03 | RETIRED | NOT_APPLICABLE |
| DEP-02-02-007 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-04 | RETIRED | NOT_APPLICABLE |
| DEP-02-02-008 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-05 | RETIRED | NOT_APPLICABLE |
| DEP-02-02-009 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-08-03 | RETIRED | NOT_APPLICABLE |
| DEP-02-02-010 | ANCHOR | UPSTREAM | OTHER | SOW-081 | ACTIVE | TBD |
| DEP-02-02-011 | ANCHOR | UPSTREAM | OTHER | SOW-082 | ACTIVE | TBD |
| DEP-02-02-012 | ANCHOR | UPSTREAM | OTHER | OBJ-007 | ACTIVE | TBD |
| DEP-02-02-013 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-03 | ACTIVE | PENDING |
| DEP-02-02-014 | EXECUTION | UPSTREAM | INTERFACE | DEL-06-03 | ACTIVE | PENDING |
| DEP-02-02-015 | EXECUTION | UPSTREAM | INTERFACE | DEL-05-02 | ACTIVE | PENDING |
| DEP-02-02-016 | EXECUTION | UPSTREAM | CONSTRAINT | ROOT-PROPOSAL-EVENT-ACCEPTANCE | RETIRED | PENDING |
| DEP-02-02-017 | EXECUTION | UPSTREAM | INTERFACE | DEL-08-05 | ACTIVE | PENDING |
| DEP-02-02-018 | EXECUTION | UPSTREAM | INTERFACE | DEL-05-04 | ACTIVE | TBD |
| DEP-02-02-019 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-08-04 | ACTIVE | PENDING |
| DEP-02-02-020 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-08-02 | ACTIVE | TBD |
| DEP-02-02-021 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-02-03 | ACTIVE | SATISFIED |
| DEP-02-02-022 | EXECUTION | UPSTREAM | INTERFACE | DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1 | ACTIVE | PENDING |

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | Active Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T19:24:27-0600 | UPDATE | CONSERVATIVE | found | 9 | PRD_HASH_MISMATCH; SOW_007_OWNER_OVERLAP |
| 2026-09-05T01:05:00-0600 | UPDATE | CONSERVATIVE | found at pinned identity `c7c05169` (commit `dbd812a5`) | 15 | CONTEXT_SOW_007_RESIDUE; V3_01_ROLE_ENTRY_SEATING_CONFLICT; PROJECT_ID_FORMAT_PROFILE; six proposals held under amendment v1.1 (H-002 to H-007) |
| 2026-09-05T07:59-0600 (D-APP-109 emission) | UPDATE | CONSERVATIVE | found at pinned identity `c7c05169` (commit `dbd812a5`) | 21 | CONTEXT_SOW_007_RESIDUE (carried; `_CONTEXT.md` not read, concurrent N8 write); V3_01_ROLE_ENTRY_SEATING_CONFLICT (carried); PROJECT_ID_FORMAT_PROFILE; CYCLE_PARTICIPATING_ROWS: six rows emitted under D-APP-109 (H-002 to H-007) inside the enlarged SCC-001, non-gating until resolved by a recorded move |
| 2026-09-05T10:15-0600 (D-APP-110 decompose) | UPDATE | CONSERVATIVE | found at pinned identity `c7c05169` (commit `dbd812a5`) | 21 | CONTEXT_SOW_007_RESIDUE (carried; `_CONTEXT.md` not read); V3_01_ROLE_ENTRY_SEATING_CONFLICT (carried); PROJECT_ID_FORMAT_PROFILE; no cycle-participating row remains (SD-005 decomposed DEP-02-02-022 to a DOCUMENT contract; five D-APP-109 rows marked RESOLVED) |
| 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`) | UPDATE | CONSERVATIVE | FOUND `cf6e56ebb147…` (SCA-APP-011 amended) | ACTIVE=15 (ANCHOR=6; EXECUTION=9) | EVIDENCE_SOURCE_RETIRED DEP-02-02-021 |

## Lifecycle Summary

Current as of 2026-09-27 (`APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.

| Dimension | Value | Count |
|---|---|---:|
| Status | ACTIVE | 15 |
| Status | RETIRED | 7 |
| SatisfactionStatus | NOT_APPLICABLE | 5 |
| SatisfactionStatus | PENDING | 7 |
| SatisfactionStatus | SATISFIED | 1 |
| SatisfactionStatus | TBD | 9 |
| RequiredMaturity | SEMANTIC_READY | 22 |
| DependencyClass | ANCHOR | 7 |
| DependencyClass | EXECUTION | 15 |
| DependencyType | CONSTRAINT | 4 |
| DependencyType | INTERFACE | 10 |
| DependencyType | OTHER | 7 |
| DependencyType | PREREQUISITE | 1 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor (PKG-02), five trace anchors (SOW-006, SOW-081, SOW-082, OBJ-001, OBJ-007), one retired SOW-007 anchor, five re-evidenced compatibility-history execution rows (DEL-02-01, DEL-02-03, DEL-07-04, DEL-07-05, DEL-08-03), four execution rows introduced by SCA-APP-010 (DEL-07-03, DEL-06-03, Root DEL-02-10 EXTERNAL, DEL-02-03 host), five deliverable execution rows emitted under D-APP-109 on 2026-09-05 (DEL-05-02, DEL-08-05, DEL-05-04, DEL-08-04, DEL-08-02; DEP-02-02-015, 017, 018, 019, 020), and one `DOCUMENT` execution row (DEP-02-02-022, emitted under D-APP-109 and re-targeted under D-APP-110 SD-005 to `DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` at DEL-02-04 `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`; the deliverable relation to DEL-02-04 is preserved in its `Notes`).
- Cycle-participating rows: none. Under D-APP-110 (2026-09-05) the SCC that the six D-APP-109 rows participated in was decomposed (`docs/CYCLE_DRIVEN_RESOLUTION.md` section 2.3, `SCC-SAFE-MOVES-001` form); this carrier no longer holds a cycle-participating row, and every row gates per its `SatisfactionStatus` (PENDING rows wait on their named seated items or the Root acceptance; TBD rows carry no named gate). Reconcile the DOCUMENT row as a contract-consumption relation: it is not a strict deliverable edge and introduces no deliverable-graph ordering.
- Cross-register checks worth running: DEL-02-01 `DEP-02-01-007` (DOWNSTREAM to DEL-02-02) against DEP-02-02-005; DEL-07-03, DEL-06-03, and DEL-02-03 registers for any reciprocal DOWNSTREAM row naming DEL-02-02 as the consumer of the workflow file contract, the `propose` tool payload, or the view switcher.
- SCC posture: under D-APP-109 the fifteen held edges across nine carriers were emitted together, enlarging the live nine-node SCC-001 and creating a new two-node SCC (DEL-06-03/DEL-08-01); under D-APP-110 both SCCs were resolved by decompose (five edges, seven rows across the affected carriers; this carrier's contribution is SD-005 on DEP-02-02-022), and the strict active deliverable execution graph is acyclic. The fresh `AUDIT_DEP_CLOSURE` run (amendment v1.3 node N16) records the acyclic graph and the move basis; acceptance of that snapshot as the DepClosure pointer is a separate owner act.
- DEP-02-02-021 host identity is carried at `Confidence=MEDIUM` under the amendment v1.1 C.1 ASSUMPTION (DEL-02-03 as seated); re-target to DEL-02-01 only by owner act.
- Root boundary: DEP-02-02-016 stays `EXTERNAL`/`TBD` until the Root DEL-02-10 return is routed to App; no Root path may be recorded in this register.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=20; RETIRED=2; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
