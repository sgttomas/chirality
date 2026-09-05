# Dependencies: DEL-08-01 Instruction Root Packaging and Agent Conformance

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used RuntimeOverrides: `SCOPE=DEL-08-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Run root: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (located and read).
- Source docs scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` and `_STATUS.md` were intentionally not read or consumed per human ruling and write restrictions.
- Anchor doc selection: `Datasheet.md` with `_CONTEXT.md` and decomposition cross-checks.
- Execution doc order: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`, `_REFERENCES.md`.
- Conservative extraction emitted no downstream deliverable edges because local evidence names DEL-08-04 and DEL-08-05 only as out-of-scope/boundary owners, not accepted handoff targets.
- Implementation details for validator path, test framework, fixture path, CI/local command, and output artifact location remain `TBD`; no dependency target was invented for those unresolved choices.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 authority corpus v2 supersedes the prior REF-006 source warning; `_REFERENCES.md` now records REF-006 as MATCH and row DEP-08-01-012 is updated accordingly.
- `[RESOLVED] CONFORMANCE_VALIDATOR`: ADQ-12 adds machine validation coverage for agent instruction filename, document marker, agent type, class vocabulary, write-scope vocabulary, protocol/spec/structure/rationale markers, and allowed frontmatter keys.
- `[RESOLVED] SOURCE_COMPLETENESS_CHECKLIST`: ADQ-12 adds `sourceCompleteness` summary rows for SOW-073/OI-004 and KG-001 candidate source assets to the instruction-root integrity script.
- `[WARNING] UNRESOLVED_TARGET`: row DEP-08-01-015 records the explicitly required current instruction-root source tree, but the stable target location is unresolved and remains `UNKNOWN`/`TBD`.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor was extracted.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor was extracted.

### 2026-09-05 — SCA-APP-010 dependency closure, report-only preview post-image

- Run: `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`, instance `N1-TASK-DEL-08-01`; `TASK + dependency-extract` (Claude Fable 5.1, `claude-fable-5-1`, as a Claude Code subagent dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched). Rerun in place under brief amendment v1.1 (`AMENDMENT_v1.1_N1_PREVIEWS.md`, HELP_HUMAN fan-in disposition, sections A, C.3, C.4, D): the held deliverable edge was removed from this post-image and its ID reserved. This text is the proposed post-image; the reviewed write (SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-021/DEP-022) is a separate act.
- Runtime overrides: `SCOPE=DEL-08-01_Instruction_Root_Packaging_and_Agent_Conformance`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ApplyEdits=false`. No defaults were left to auto-discovery.
- Source posture: `_STATUS.md` was read only for its `## Remaining` section (seated item DEL-08-01-V3-01 `Depends`, `Write locus`, and gate lines as owner-adopted information-flow signals); `_REFERENCES.md` resolved document pointers only. `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, and `_run_records/**` were not used as evidence.
- Decomposition authority found at the pinned identity: SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (the `ScopeOfWork.md` `decomposition_basis` pin); applied row L368; amended Scope Ledger rows SOW-082 L252/L485 and SOW-084 L254/L487; OI-008 L602; DEC-025 L634. Companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`.
- Pass 1 — ANCHOR: DEP-08-01-001 (`IMPLEMENTS_NODE` to PKG-08) preserved with its `DependencyID`; SOW-030/SOW-031/SOW-073 and OBJ-007/OBJ-008 trace anchors preserved and re-pointed to live lines; SOW-082 (DEP-08-01-016) and SOW-084 (DEP-08-01-017) added because they are new on the applied row. No scope ref left the applied row, so no anchor was retired. `TargetType=REQUIREMENT` for objectives is this carrier's pre-existing convention and was preserved.
- Pass 2 — EXECUTION: DEP-08-01-007 to DEP-08-01-015 re-evidenced from the retired four-document kit (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) to `ScopeOfWork.md` CLM/REQ ids; every relation is still stated, so nothing was retired. New rows: DEP-08-01-019 (UPSTREAM INTERFACE, DEL-07-01 layer protections the checks verify), DEP-08-01-020 (DOWNSTREAM CONSTRAINT, routed agent-index change notice and G4 manifest under the Root `AGENTS.md` rule; `EXTERNAL`/`TBD`), DEP-08-01-021 (UPSTREAM PREREQUISITE, owner write-scope grant for `agents/**` and `skills/**` at selection; `EXTERNAL`/`TBD`). The v1 preview also proposed DEP-08-01-018 (UPSTREAM INTERFACE, DEL-06-03 `propose` tool contract the clauses invoke); it is held under amendment v1.1 and the ID is reserved, not renumbered.
- EMITTED under D-APP-109 (H-018): DEP-08-01-018 — DEL-08-01 -> DEL-06-03 UPSTREAM INTERFACE (DEL-08-01's proposal-clause conformance checks consume the DEL-06-03 `propose` tool contract) — cycle-participating, non-gating until the SCC is resolved by a recorded move. The v1.1 hold reason (fan-in simulation `Evidence/fanin_simulation_v1/`: with DEL-06-03's reciprocal H-017, DEP-06-03-014, this edge forms a new two-node SCC DEL-06-03/DEL-08-01) is now the recorded SCC change under D-APP-109, not a reason to withhold the row.
- Fence F1 (SCC-001 membership): NONE. No new row targets an SCC-001 member (DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05); no SCC-001 member holds an active row back to DEL-08-01. DEL-05-02's `proposal.*` consumption on SOW-082 is not a relation of this carrier.
- Fence F2 (Root path): NONE emitted. Root-owned targets (the `AGENTS.md` change-notice rule and G4 manifest validator; the owner grant) are `EXTERNAL` with `TargetLocation=TBD`. Pre-existing DEP-08-01-013 keeps its `_REFERENCES.md`-pinned REF-007 absolute pointer unchanged; see the graph decision below.
- Fence F3 (permitted effect): considered and not emitted — the `NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected` gate (a selection/schedule gate, not an information flow); DEL-07-03's governed workflow file contract (SOW-081 is not on this carrier's applied row and no source names it as an input to the template-discoverability check); DEL-06-02 catalog/collision validation, DEL-05-02 event consumption, DEL-02-02 proposal card, and DEL-09-04 packaging (ownership statements with no artifact this carrier consumes or supplies).
- `NEEDS_HUMAN_GRAPH_DECISION` (1): whether DEL-08-01 should carry a reciprocal DOWNSTREAM edge to DEL-04-04. Scope Ledger L487 states "DEL-08-01 owns packaging and conformance checks; DEL-04-04 composes from both layers", and DEL-04-04's own register already holds an ACTIVE UPSTREAM PREREQUISITE row to DEL-08-01 (DEP-04-04-005), but this carrier's sources state no artifact DEL-08-01 supplies (it verifies packaging and pins). Not emitted under CONSERVATIVE strictness. HELP_HUMAN disposition (amendment v1.1 C.4, disposition-class, not a ruling): reciprocal edge not invented; no change; carried to the owner slate in `HANDOFF_STATE.md`.
- `NEEDS_HUMAN_GRAPH_DECISION` (2): DEP-08-01-013 `TargetLocation` is the pre-existing REF-007 absolute pointer `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` (a Root `agents/` surface, byte-identical to this checkout's `agents/AGENT_SOFTWARE_DECOMP.md`). The relation is still stated (CLM-006; `_REFERENCES.md` REF-007 MATCH), the row is not stale, and the permitted effect does not cover rewriting it, so it is preserved unchanged; the reviewer may rule whether a later reviewed write converts it to `EXTERNAL`/`TBD`. HELP_HUMAN disposition (amendment v1.1 C.3, disposition-class, not a ruling): preserved unchanged; outside DEP-021's permitted effect; carried to the owner slate in `HANDOFF_STATE.md`.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `tools/validation/validate_id_format.sh` three-digit profile (`PKG-NNN`, `DEL-NNN-NN`, `DEP-NNN-NN-NNN`, `SOW-NNNN`) rejects the accepted App two-digit identities; `OBJ-007`/`OBJ-008` pass. No ID was changed.
- `[WARNING] UNRESOLVED_TARGET`: DEP-08-01-015 remains `UNKNOWN`/`TBD` (unchanged).
- `[WARNING] CONTEXT_LAG`: `_CONTEXT.md` `CoversScopeItems` still lists SOW-030, SOW-031, SOW-073 (the known SCA-APP-010 Gate-5 audit warning); `ScopeOfWork.md` front matter and the applied row are the anchor authority for SOW-082 and SOW-084.
- Function 5 (rerun under amendment v1.1): `validate_dependencies_schema.py` VALID (29 columns, 20 data rows); 24 distinct enum pairs VALID; exactly one ACTIVE `IMPLEMENTS_NODE` (no `FLOATING_NODE`, no `AMBIGUOUS_ANCHOR`); every ACTIVE row's `EvidenceFile` and `SourceRef` resolve to live bytes; `FromDeliverableID=DEL-08-01` on every row; `DependencyID`s unique (DEP-08-01-018 reserved, absent); no `Status=CANDIDATE`; no register row deleted (the held row was never written to the carrier).

### 2026-09-05 — D-APP-109 held-edge emission (N9)

- Run: `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`, instance `N9-TASK-DEL-08-01`; `TASK + dependency-extract` apply (Claude Fable 5.1, `claude-fable-5-1`, as a Claude Code subagent dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched). Authority: owner ruling D-APP-109 (`_DECISIONS/D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md`) and `AMENDMENT_v1.2_OWNER_RULING.md` node N9; SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-021/DEP-022 targets.
- Runtime overrides: `SCOPE=DEL-08-01_Instruction_Root_Packaging_and_Agent_Conformance`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `ApplyEdits=true`. No new extraction from prose: the one row written is the held proposal H-018 exactly as `HELD_EDGE_PROPOSALS.csv` and `instances/N1-TASK-DEL-08-01/PREVIEW.md` recorded it, with the D-APP-109 non-gating `Notes` clause appended.
- Decomposition authority found at the pinned identity: SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); applied row L368; SOW-082 L252/L485; DEL-06-03 row L348 (`Initial Chirality MCP Read Tools`).
- Row DEP-08-01-018 inserted at its numeric position (between DEP-08-01-017 and DEP-08-01-019); every pre-existing row byte-identical; no row retired or deleted. Conventions mirror the carrier's sibling DELIVERABLE row DEP-08-01-019: fully quoted fields, `TargetRefID` empty, `TargetLocation` the plain decomposition path (this register does not use the `#L<n>` pointer form on deliverable targets; the target row is L348).
- Evidence re-verified against live bytes: `_STATUS.md` `## Remaining` seated item DEL-08-01-V3-01 `Depends` line carries the quote verbatim; `ScopeOfWork.md` `### Current acceptance obligations` obligation 2 states the proposal-clause conformance; decomposition L485 assigns the tool to DEL-06-03 and instruction-clause conformance to DEL-08-01.
- Graph posture: with DEL-06-03's reciprocal DEP-06-03-014 (H-017) this row forms the new two-node SCC DEL-06-03/DEL-08-01. Under D-APP-109 and `docs/CYCLE_DRIVEN_RESOLUTION.md` the row is `CYCLE_PARTICIPATING` and non-gating (no blocker queue, wave, dispatch-readiness, or implementation-readiness effect) until that SCC is resolved by a recorded decompose, invert, merge, or cut move; no such move is recorded by this run. The seated item's own `Depends` line and named gates remain the executable ordering.
- Carried unchanged: `NEEDS_HUMAN_GRAPH_DECISION` (1) DEL-04-04 reciprocal edge and (2) DEP-08-01-013 REF-007 pointer; `[WARNING] PROJECT_ID_FORMAT_PROFILE`; `[WARNING] UNRESOLVED_TARGET` (DEP-08-01-015). `[WARNING] CONTEXT_LAG` is being cleared by the D-APP-109 `_CONTEXT.md` alignment in the same pass (HELP_HUMAN's builder), outside this run's write set.
- Function 5: `validate_dependencies_schema.py` VALID (29 columns, 21 data rows); every emitted enum value VALID; exactly one ACTIVE `IMPLEMENTS_NODE` (no `FLOATING_NODE`, no `AMBIGUOUS_ANCHOR`); 21 unique `DependencyID`s (DEP-08-01-018 now present exactly once); `FromDeliverableID=DEL-08-01` on every row; no `Status=CANDIDATE`; `git diff --check` clean; LF, no trailing whitespace, final newline.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 21 |
| ACTIVE rows | 21 |
| RETIRED rows | 0 |
| ANCHOR rows | 8 |
| EXECUTION rows | 13 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Trace anchors (`TRACES_TO_REQUIREMENT`) | 7 |
| Upstream document prerequisites | 8 |
| Upstream unresolved prerequisites | 1 |
| Upstream deliverable interfaces | 2 |
| Upstream external prerequisites | 1 |
| Downstream external constraints | 1 |
| Held non-emitted proposals (reserved IDs, not rows) | 0 |
| Cycle-participating non-gating rows (D-APP-109) | 1 |

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-08-01-001 | ANCHOR | OTHER | UPSTREAM | PKG-08 | ACTIVE | SATISFIED |
| DEP-08-01-002 | ANCHOR | OTHER | UPSTREAM | SOW-030 | ACTIVE | SATISFIED |
| DEP-08-01-003 | ANCHOR | OTHER | UPSTREAM | SOW-031 | ACTIVE | SATISFIED |
| DEP-08-01-004 | ANCHOR | OTHER | UPSTREAM | SOW-073 | ACTIVE | SATISFIED |
| DEP-08-01-005 | ANCHOR | OTHER | UPSTREAM | OBJ-007 | ACTIVE | SATISFIED |
| DEP-08-01-006 | ANCHOR | OTHER | UPSTREAM | OBJ-008 | ACTIVE | SATISFIED |
| DEP-08-01-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 `docs/DIRECTIVE.md` | ACTIVE | PENDING |
| DEP-08-01-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE | PENDING |
| DEP-08-01-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE | PENDING |
| DEP-08-01-010 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 `docs/TYPES.md` | ACTIVE | PENDING |
| DEP-08-01-011 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 `docs/PLAN.md` | ACTIVE | PENDING |
| DEP-08-01-012 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE | PENDING |
| DEP-08-01-013 | EXECUTION | PREREQUISITE | UPSTREAM | REF-007 `AGENT_SOFTWARE_DECOMP.md` | ACTIVE | PENDING |
| DEP-08-01-014 | EXECUTION | PREREQUISITE | UPSTREAM | DEC-004 decomposition v3.2 (applied row L368, DEC-025) | ACTIVE | PENDING |
| DEP-08-01-015 | EXECUTION | PREREQUISITE | UPSTREAM | TBD current instruction-root source tree | ACTIVE | PENDING |
| DEP-08-01-016 | ANCHOR | OTHER | UPSTREAM | SOW-082 | ACTIVE | SATISFIED |
| DEP-08-01-017 | ANCHOR | OTHER | UPSTREAM | SOW-084 | ACTIVE | SATISFIED |
| DEP-08-01-018 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-03 `propose` tool contract the proposal clauses invoke (cycle-participating, non-gating; D-APP-109 H-018) | ACTIVE | PENDING |
| DEP-08-01-019 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-01 organisation-layer protections (K-ROOT-1 on both layers) | ACTIVE | PENDING |
| DEP-08-01-020 | EXECUTION | CONSTRAINT | DOWNSTREAM | EXTERNAL routed agent-index change notice and G4 manifest (Root `AGENTS.md` rule; location TBD) | ACTIVE | PENDING |
| DEP-08-01-021 | EXECUTION | PREREQUISITE | UPSTREAM | EXTERNAL owner write-scope grant for `agents/**` and `skills/**` at selection (location TBD) | ACTIVE | PENDING |

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-09-05T07:58-0600 (D-APP-109 emission) | UPDATE | CONSERVATIVE | Found at the pinned identity `c7c05169…` (content commit `dbd812a52…`, SCA-APP-010 applied row L368); held row DEP-08-01-018 (H-018) emitted under owner ruling D-APP-109 as cycle-participating and non-gating (new two-node SCC DEL-06-03/DEL-08-01 recorded, not resolved) | PROJECT_ID_FORMAT_PROFILE; UNRESOLVED_TARGET for instruction-root source tree; CYCLE_PARTICIPATING x1 (DEP-08-01-018); NEEDS_HUMAN_GRAPH_DECISION x2 (DEL-04-04 reciprocal edge; DEP-08-01-013 REF-007 pointer) | 21 |
| 2026-09-05T01:01:17-0600 | UPDATE | CONSERVATIVE | Found at the pinned identity `c7c05169…` (content commit `dbd812a52…`, SCA-APP-010 applied row L368); report-only preview post-image rerun under brief amendment v1.1 (v1 preview 2026-09-05T00:40:02-0600 superseded in place), reviewed write pending (DEP-021/DEP-022) | PROJECT_ID_FORMAT_PROFILE; UNRESOLVED_TARGET for instruction-root source tree; CONTEXT_LAG; HELD x1 (DEP-08-01-018 reserved, H-018); NEEDS_HUMAN_GRAPH_DECISION x2 (DEL-04-04 reciprocal edge; DEP-08-01-013 REF-007 pointer) | 20 |
| 2026-06-21T05:00:00-0600 | ADQ-12 | CONSERVATIVE | D-APP-38 current authority corpus, conformance-validator residuals, and source-completeness checklist applied | UNRESOLVED_TARGET for instruction-root source tree | 15 |
| 2026-05-20T19:54:20-0600 | UPDATE | CONSERVATIVE | Located and read | superseded SOURCE_HASH_MISMATCH for REF-006; UNRESOLVED_TARGET for instruction-root source tree | 15 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 21 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 8 |
| PENDING | 13 |

Closure-state breakdown: 8 anchors SATISFIED (1 parent, 7 trace); 13 EXECUTION rows PENDING (8 document prerequisites, 1 unresolved instruction-root source tree, 2 deliverable interfaces awaiting DEL-06-03-V3-01 and DEL-07-01-V3-01, 1 owner write-scope grant, 1 routed-notice/G4-manifest constraint that binds at the first instruction-file change). Of these, DEP-08-01-018 (DEL-06-03 interface, emitted under D-APP-109 from held proposal H-018) is cycle-participating and non-gating until the two-node SCC DEL-06-03/DEL-08-01 is resolved by a recorded move; no held non-emitted proposal remains.

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor (PKG-08), seven trace anchors (SOW-030, SOW-031, SOW-073, SOW-082, SOW-084, OBJ-007, OBJ-008), eight re-evidenced document prerequisites (REF-001 to REF-007, DEC-004), one unresolved instruction-root source-tree prerequisite, two deliverable interfaces (DEL-06-03, DEL-07-01), one owner-grant prerequisite, and one routed-notice/G4-manifest constraint. The DEL-06-03 interface (DEP-08-01-018) was emitted under D-APP-109 from held proposal H-018 and is reconciled as a row.
- Graph posture: DEL-08-01 is not an SCC-001 member and this register adds no edge into SCC-001. The carrier now carries one cycle-participating non-gating row: DEP-08-01-018 (DEL-06-03) together with DEL-06-03's reciprocal DEP-06-03-014 (H-017) forms the new two-node SCC DEL-06-03/DEL-08-01, recorded under D-APP-109 and pending resolution by a recorded decompose, invert, merge, or cut move (`docs/CYCLE_DRIVEN_RESOLUTION.md`); until then the row drives no blocker queue, wave, dispatch-readiness, or implementation-readiness claim. The DEL-07-01 edge points to a non-SCC node. The reciprocal DEL-04-04 question and the DEP-08-01-013 REF-007 pointer are recorded above as graph decisions, not as rows, and are carried to the owner slate.
- Root boundary: the `AGENTS.md` agent-index change-notice rule and the G4 manifest validator are Root-owned; consume them as `EXTERNAL`/`TBD` until the owner routes the notice at the first instruction-file change (Propagation_Plan §6 item 9). No `proposal.*` (OI-008) edge belongs to this carrier.
- `_CONTEXT.md` traceability is aligned to the applied row under D-APP-109 in the same pass (HELP_HUMAN's builder, outside this run's write set); `ScopeOfWork.md` front matter and decomposition L368 remain the anchor authority.

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.
