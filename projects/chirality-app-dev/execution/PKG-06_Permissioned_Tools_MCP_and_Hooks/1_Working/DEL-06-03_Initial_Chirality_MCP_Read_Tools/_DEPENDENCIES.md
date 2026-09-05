# Dependencies: DEL-06-03 Initial Chirality MCP Read Tools

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

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-03-005` is now
`SATISFIED` because REF-002/REF-003 remain `MATCH` and REF-006 `docs/PRD.md` is
`MATCH` under the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings
remain extraction history and no longer describe the active source-state posture.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK + dependency-extract ran in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source selection: anchor document `Datasheet.md`; execution documents `Procedure.md`, `Specification.md`, and `Guidance.md`; supporting context `_CONTEXT.md`, `_REFERENCES.md`, existing `_DEPENDENCIES.md`, and decomposition authority.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed.
- Existing `Dependencies.csv`: absent before this run; no rows were retired.
- [HISTORICAL WARNING] SOURCE_STATE: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-03-005` is now `SATISFIED`.
- [WARNING] TARGET_UNRESOLVED: status lifecycle API owner is explicit in source text but not resolved to a deliverable/API identifier in accessible evidence.
- [WARNING] TARGET_UNRESOLVED: Chirality runtime event path is explicit in source text but final active implementation owner is conditional/TBD in accessible evidence.
- 2026-09-05 TASK + dependency-extract REPORT-ONLY PREVIEW (SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-015/DEP-016; run `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, instance `N1-TASK-DEL-06-03`) ran in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=RECONCILIATION`, `ApplyEdits=false`. This file and the paired register are the proposed post-image; the carrier's live files are unchanged until the reviewed write is authorized.
- 2026-09-05 source selection (explicit in the sealed brief; no defaults applied): `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `_STATUS.md` was read only for its `## Remaining` section (seated item DEL-06-03-V3-01, lines 11-18); `_REFERENCES.md` was read to resolve pointers; `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, and `_run_records/**` were excluded.
- 2026-09-05 decomposition authority: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; applied row L348; amended Scope Ledger row SOW-082 L252; reverse view L404-487; OI-008 L602; DEC-025 L634). Companion register SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`; authority corpus v20, no drift.
- 2026-09-05 pre-image identities: `Dependencies.csv` SHA-256 `b9802d035476e9781c89e71cb49415bcb98206c0ad310420ae61b1bf8361918c` (9 data rows); `_DEPENDENCIES.md` SHA-256 `9dc38450f2525d2d59cd8356b94e4331ec789b0de41d070b3ebc451dbbc18e9c`.
- 2026-09-05 legacy kit: `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` no longer exist in this carrier. Rows DEP-06-03-001 and DEP-06-03-004 through DEP-06-03-009 were re-evidenced to live `ScopeOfWork.md` bytes (`ScopeOfWork.md#<CLM/REQ id> line(s)`); DEP-06-03-002 and DEP-06-03-003 had their `_CONTEXT.md` line pointers refreshed. Every pre-image relation is still stated, so no row was retired and every `DependencyID` is preserved. `Status=CANDIDATE` was not emitted.
- 2026-09-05 Pass 1 (ANCHOR): the existing `IMPLEMENTS_NODE` row was preserved; trace anchors were added for SOW-064 (DEP-06-03-010) and SOW-082 (DEP-06-03-011), which are on the applied row L348 but were unanchored, and for OBJ-005 and OBJ-006 (DEP-06-03-012, DEP-06-03-013) using the `TargetType=UNKNOWN` objective convention. No anchor was retired because no pre-image scope ref left the applied row.
- 2026-09-05 Pass 2 (EXECUTION): four rows were added from the amended row SOW-082 (L252/L485), the applied row prose (L348), and the seated DEL-06-03-V3-01 `Depends` line: DEP-06-03-015 (instruction-root roster and policy values, UNKNOWN owner), DEP-06-03-016 (DEL-02-02 proposal card consumes `proposal.offered`), DEP-06-03-017 (DEL-05-02 consumes the additive `proposal.*` event types after Root acceptance), and DEP-06-03-018 (Root DEL-02-10 event-type acceptance, EXTERNAL/TBD). A fifth extracted row (DEL-08-01 clauses naming the triggers) was allocated DEP-06-03-014 by the v1 preview and is held under brief amendment v1.1 (next bullet); its ID stays reserved and the remaining rows are not renumbered.
- EMITTED under D-APP-109 (H-017): DEP-06-03-014 — DEL-06-03 -> DEL-08-01 UPSTREAM INTERFACE (the propose tool offers only the few triggers named by DEL-08-01 instruction-package clauses in the Agent 0 and Agent 1 packages and resolves plan references from Agent 1 procedures; evidence `_STATUS.md#Remaining DEL-06-03-V3-01 Depends line 14`, SOW-082 L252/L485, DEL-08-01 applied row L368) — cycle-participating, non-gating until the SCC is resolved by a recorded move. The row was held under amendment v1.1 (`HELD_EDGE_PROPOSALS.csv` H-017) because, with the reciprocal DEL-08-01 row DEP-08-01-018 (H-018), it forms a new two-node SCC DEL-06-03/DEL-08-01; owner ruling D-APP-109 (2026-09-05) accepted the held edges with the SCC change recorded rather than linearized, so the row now carries the `CYCLE_PARTICIPATING` non-gating clause in `Notes` and drives no blocker queue, wave placement, dispatch readiness, or implementation-readiness claim until that SCC is resolved by a recorded decompose, invert, merge, or cut move (`docs/CYCLE_DRIVEN_RESOLUTION.md`). Emitted by instance `N9-TASK-DEL-06-03` of the same run.
- 2026-09-05 fence results: F1 NONE (DEL-06-03 is not a member of SCC-001; no SCC-001 member holds an active row back to DEL-06-03, re-checked 2026-09-05 against all 52 registers for the amendment v1.1 rerun; the v1 preview's read-only replay of the registered analyzer `tools/coordination/analyze_dep_closure.py` over all 52 registers plus the proposed rows left SCC-001 at its nine baseline nodes and DEL-06-03 outside it, and the v1.1 rerun only removes an edge, which cannot create a cycle); F2 NONE (no `TargetLocation` names a Root path; the Root-owned target is `EXTERNAL` with `TargetLocation=TBD`); F3 NONE (every new row traces to SOW-082, the applied row prose, or the owner-adopted `Depends` line; no edge was inferred from the item's `NOT_SELECTABLE_UNTIL` gate, from SCC ordering, or from a keep-aligned statement).
- 2026-09-05 NEEDS_HUMAN_GRAPH_DECISION (1) H-1 held candidate, not emitted: the seated `Depends` line names `DEL-06-02 catalog validation` and the applied row L348 says catalog validation and collision prevention remain DEL-06-02 (also SOW-082 L485 and D-APP-68 composition, ScopeOfWork.md CLM-035). Read as UPSTREAM CONSTRAINT (DEL-06-03 requires DEL-06-02 validation of the registered `propose` tool) it adds analyzer edge DEL-06-03 -> DEL-06-02, and DEL-06-02 already holds ACTIVE `DEP-06-02-006` (UPSTREAM INTERFACE: the resolver registers Chirality MCP read tool definitions from DEL-06-03), so the pair would form a new two-node SCC {DEL-06-02, DEL-06-03}. Per `docs/CYCLE_DRIVEN_RESOLUTION.md` the cycle is surfaced rather than linearized; options: decompose (split the descriptor supply from the validation gate into two non-cyclic edges), invert (hold the edge only as DEL-06-03 DOWNSTREAM HANDOVER of the `propose` descriptor into the DEL-06-02 catalog, mirroring DEP-06-02-006), merge (human-gated), cut (human-gated). The write instance allocates a `DependencyID` only after the ruling.
- 2026-09-05 NEEDS_HUMAN_GRAPH_DECISION (2) DEP-06-03-008: live `ScopeOfWork.md` CLM-020 line 326 states the status reader's final ownership should align with DEL-07-04, and decomposition SOW-028 L431 maps status lifecycle to DEL-07-04; resolving the target from UNKNOWN to `DELIVERABLE DEL-07-04` adds analyzer edge DEL-06-03 -> DEL-07-04 (replay: no SCC change) but is outside the DEP-015 permitted effect (SOW-081..084 and revised SOW-001/002/004/006/007/008/010 relations). The row keeps `TargetType=UNKNOWN` pending the owner's ruling.
- [WARNING] TARGET_UNRESOLVED: DEP-06-03-008 status lifecycle API owner preserved as UNKNOWN/TBD pending decision (2) above.
- [WARNING] TARGET_UNRESOLVED: DEP-06-03-009 Chirality runtime event path owner remains UNKNOWN/TBD in live sources (`ScopeOfWork.md` CLM-021 step 9 line 370).
- [WARNING] TARGET_UNRESOLVED: DEP-06-03-015 instruction-root roster and policy values have no deliverable owner named in this carrier's sources; PROPOSAL only (SOW-030 L433; SOW-084 L487).
- [WARNING] PROJECT_ID_FORMAT_PROFILE: `tools/validation/validate_id_format.sh` implements the generic three-digit profile (`PKG-NNN`, `DEL-NNN-NN`, `DEP-NNN-NN-NNN`, `SOW-NNNN`) and rejects the accepted App two-digit identifiers; no ID was changed.
- 2026-09-05 SCC-001 adjacency disclosure: DEP-06-03-017 targets DEL-05-02, an SCC-001 member, as a DOWNSTREAM handover (analyzer edge DEL-05-02 -> DEL-06-03). This is not an edge inside SCC-001 and does not make DEL-06-03 a member because DEL-06-03 has no path into the SCC; reviewers should confirm against the N4 closure audit.
- 2026-09-05 considered and not emitted (no explicit transfer stated in this carrier's sources): declined-trigger and chat-rung state held by DEL-02-04 under revised SOW-008 (the tool refuses a trigger already declined in the chat; the once-per-chat state is in this carrier's own write locus per `_STATUS.md` line 15); the per-chat delegation-policy session-record field (SOW-083/SOW-010, Root DEL-02-11), which the tuple proposes rather than reads; DEL-04-04 plan-reference or roadmap-injection seams (SOW-081), which this carrier's sources do not name.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-06-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-06 Permissioned Tools, MCP, and Hooks | ACTIVE |
| DEP-06-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-048 Chirality MCP descriptors | ACTIVE |
| DEP-06-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-050 Read tools before writes/bash | ACTIVE |
| DEP-06-03-004 | EXECUTION | PREREQUISITE | UPSTREAM | Decomposition v3.2 document | ACTIVE |
| DEP-06-03-005 | EXECUTION | PREREQUISITE | UPSTREAM | MCP tools and permissions source contracts | ACTIVE |
| DEP-06-03-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-01 ChiralityPermissionOverlay and Mode Mapping | ACTIVE |
| DEP-06-03-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-05 Dependencies.csv v3.1 Reader Writer and Linter | ACTIVE |
| DEP-06-03-008 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN/TBD status lifecycle API owner | ACTIVE |
| DEP-06-03-009 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN/TBD Chirality runtime event path | ACTIVE |
| DEP-06-03-010 | ANCHOR | OTHER | UPSTREAM | SOW-064 MCP extension boundaries | ACTIVE |
| DEP-06-03-011 | ANCHOR | OTHER | UPSTREAM | SOW-082 Prompted specification ladder | ACTIVE |
| DEP-06-03-012 | ANCHOR | OTHER | UPSTREAM | OBJ-005 Project capability policy and conformance | ACTIVE |
| DEP-06-03-013 | ANCHOR | OTHER | UPSTREAM | OBJ-006 Filesystem project truth | ACTIVE |
| DEP-06-03-014 | EXECUTION | INTERFACE | UPSTREAM | DEL-08-01 Instruction Root Packaging and Agent Conformance | ACTIVE |
| DEP-06-03-015 | EXECUTION | PREREQUISITE | UPSTREAM | UNKNOWN/TBD instruction-root roster and policy values | ACTIVE |
| DEP-06-03-016 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-02-02 Right-Panel Coordination, Workflows, and Proposal UX | ACTIVE |
| DEP-06-03-017 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-05-02 HarnessEvent Schema and Append-Only JSONL | ACTIVE |
| DEP-06-03-018 | EXECUTION | CONSTRAINT | UPSTREAM | EXTERNAL/TBD Root DEL-02-10 additive proposal.* event-type acceptance | ACTIVE |

Counts:

- Total rows: 18 (DEP-06-03-014 emitted under D-APP-109; cycle-participating, non-gating)
- By class: ANCHOR=7, EXECUTION=11
- By type: OTHER=7, PREREQUISITE=3, INTERFACE=5, HANDOVER=2, CONSTRAINT=1
- By status: ACTIVE=18
- By direction: UPSTREAM=16, DOWNSTREAM=2
- Parent anchor check: PASS (one ACTIVE `IMPLEMENTS_NODE` row)

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 18 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 9 |
| PENDING | 5 |
| TBD | 4 |

Open dependency closure items:

- `DEP-06-03-006`: permission overlay integration target is known (`DEL-06-01`), but satisfaction remains `TBD`.
- `DEP-06-03-007`: dependency reader behavior must align with `DEL-07-05`; satisfaction remains `TBD`.
- `DEP-06-03-008`: status lifecycle API owner remains `UNKNOWN/TBD`; resolution to `DEL-07-04` is held for owner decision (Run Notes decision 2).
- `DEP-06-03-009`: runtime event path owner/availability remains `UNKNOWN/TBD`.
- `DEP-06-03-015`: instruction-root roster and policy values are `PENDING` with an unresolved owner.
- `DEP-06-03-016`: `DEL-02-02` proposal card consumption of `proposal.offered` is `PENDING` (DEL-02-02-V3-04).
- `DEP-06-03-017`: `DEL-05-02` consumption of the additive `proposal.*` event types is `PENDING` Root acceptance.
- `DEP-06-03-018`: Root DEL-02-10 acceptance of the additive event types is `PENDING` (OI-008 routed notice).
- Held candidate H-1 (DEL-06-02 catalog validation of the `propose` tool) has no row until the owner rules on the two-node cycle with `DEP-06-02-006` (Run Notes decision 1).
- `DEP-06-03-014`: `DEL-08-01` instruction-package clauses naming the triggers are `PENDING` (DEL-08-01-V3-01); emitted under D-APP-109 (H-017), cycle-participating in the new two-node SCC DEL-06-03/DEL-08-01 with the DEL-08-01 reciprocal DEP-08-01-018 (H-018), and non-gating until that SCC is resolved by a recorded move (Run Notes EMITTED bullet).

## Run History

- 2026-05-20 19:47 - `TASK + dependency-extract`; mode `UPDATE`; strictness `CONSERVATIVE`; decomposition available; created `Dependencies.csv` with 9 ACTIVE rows. Historical warnings: PRD hash mismatch later reconciled by D-APP-38 corpus v2, unresolved status lifecycle API owner, unresolved/conditional runtime event path.
- 2026-09-05 01:00 - `TASK + dependency-extract` REPORT-ONLY PREVIEW, brief amendment v1.1 rerun (`ApplyEdits=false`; instance `N1-TASK-DEL-06-03`; SCA-APP-010 DEP-015/DEP-016; supersedes the 00:41 v1 preview of the same run, whose post-image carried 18 ACTIVE rows before DEP-06-03-014 was held); mode `UPDATE`; strictness `CONSERVATIVE`; consumer context `RECONCILIATION`; decomposition found at the pinned identity `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`; warnings: PROJECT_ID_FORMAT_PROFILE, TARGET_UNRESOLVED (DEP-06-03-008, -009, -015); NEEDS_HUMAN_GRAPH_DECISION x2 (held candidate H-1 DEL-06-02 cycle; DEP-06-03-008 resolution to DEL-07-04); held proposal x1 (DEP-06-03-014 reserved, H-017); fences F1/F2/F3 NONE; 17 ACTIVE rows (9 preserved and re-evidenced or refreshed, 8 added, 0 retired, 1 held).
- 2026-09-05T07:57-0600 (D-APP-109 emission) - `TASK + dependency-extract` apply (`ApplyEdits=true`; instance `N9-TASK-DEL-06-03`; owner ruling D-APP-109 accepting the held edges of `HELD_EDGE_PROPOSALS.csv`; the 05:15 reviewed write of the v1.1 post-image by `N3-TASK-DEL-06-03` is the pre-image); mode `UPDATE`; strictness `CONSERVATIVE`; consumer context `RECONCILIATION`; decomposition found at the pinned identity `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`; warnings: PROJECT_ID_FORMAT_PROFILE, TARGET_UNRESOLVED (DEP-06-03-008, -009, -015), CYCLE_PARTICIPATING (DEP-06-03-014 inside the new two-node SCC DEL-06-03/DEL-08-01 with DEP-08-01-018; non-gating pending a recorded move); NEEDS_HUMAN_GRAPH_DECISION x2 carried unchanged (H-1 DEL-06-02 cycle; DEP-06-03-008 resolution to DEL-07-04); 18 ACTIVE rows (17 preserved byte-identical, 1 emitted DEP-06-03-014 at its numeric position, 0 retired, 0 held).

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-128
- **Current counts:** ACTIVE 9; RETIRED 0; SATISFIED=5; TBD=4.
- **Correction:** DEP-06-03-005 is SATISFIED and removed from current open-item interpretation.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
- 2026-09-05 preview note: once the reviewed DEP-015/DEP-016 write is applied, the `## Extracted Dependency Register` and `## Lifecycle Summary` sections above become the current structured-register mirror and this block remains dated history.

## Downstream Handoff Notes

Consumer context: `RECONCILIATION`.

- Accepted upstream truth for this register: applied decomposition SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (SCA-APP-010 Gate 5, DEC-025); this register is a derivative package and never substitutes for that truth.
- Cycle-participating rows (D-APP-109, 2026-09-05): this carrier now carries DEP-06-03-014 (DEL-06-03 -> DEL-08-01 UPSTREAM INTERFACE, H-017), which with the DEL-08-01 reciprocal DEP-08-01-018 (H-018) lies inside the new two-node SCC DEL-06-03/DEL-08-01. Per `docs/CYCLE_DRIVEN_RESOLUTION.md` the row is non-gating: reconciliation, aggregation, and closure audits must report it inside its SCC and must not derive a blocker queue, wave placement, dispatch readiness, or implementation-readiness claim from it until that SCC is resolved by a recorded decompose, invert, merge, or cut move (cut and merge are human-gated). The seated item's own `Depends` line and named gate in `_STATUS.md` remain the executable ordering.
- Cross-deliverable claims to reconcile: DEP-06-03-006 (DEL-06-01 permission overlay pass-through, REQ-06-03-006); DEP-06-03-007 (DEL-07-05 dependency-read contract, REQ-06-03-015); DEP-06-03-014 (DEL-08-01 instruction-package clauses name the few triggers the propose tool offers; cycle-participating, non-gating); DEP-06-03-016 (DEL-02-02 proposal card consumes `proposal.offered`); DEP-06-03-017 (DEL-05-02 consumes the additive `proposal.*` event types after Root acceptance).
- Reciprocal-register expectations: DEL-06-02 holds ACTIVE `DEP-06-02-006` toward DEL-06-03 (resolver registers this carrier's read-tool definitions); DEL-09-02 holds ACTIVE `DEP-09-02-020` toward DEL-06-03 (Section 9 MCP status/dependency validation); DEL-06-01 holds RETIRED `DEP-06-01-013`. The DEL-02-02 and DEL-05-02 previews in the same run should carry the mirror views of DEP-06-03-016 and -017; the DEL-08-01 mirror of DEP-06-03-014 (DEP-08-01-018, H-018) is emitted under D-APP-109 by the same run's `N9-TASK-DEL-08-01` instance, and the pair is the new two-node SCC DEL-06-03/DEL-08-01.
- Root-owned semantics: DEP-06-03-018 (Root DEL-02-10 additive `proposal.*` acceptance) is `EXTERNAL/TBD/PENDING` under OI-008; reconcile only against the routed Root return, never against a Root path.
- Open graph decisions for the owner: held candidate H-1 (DEL-06-02 catalog-validation cycle with `DEP-06-02-006`; not encoded in this register), DEP-06-03-008 (resolution to DEL-07-04; row kept UNKNOWN/TBD), and the resolution move for the new two-node SCC DEL-06-03/DEL-08-01 that DEP-06-03-014 and DEP-08-01-018 form (decompose, invert, merge, or cut; D-APP-109 accepted the edges and resolved no SCC).
- Unresolved targets remain `UNKNOWN/TBD` (DEP-06-03-008, -009, -015); reconciliation should not infer owners from prose.
