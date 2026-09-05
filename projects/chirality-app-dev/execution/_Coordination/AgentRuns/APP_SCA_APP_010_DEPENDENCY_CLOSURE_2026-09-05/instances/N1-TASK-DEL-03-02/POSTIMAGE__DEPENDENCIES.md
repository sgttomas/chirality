# Dependencies: DEL-03-02 Thin TurnEngine and Session Locking

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
- 2026-05-20 19:30 dependency-extract run used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (available; anchors and deliverable targets resolved conservatively).
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Source docs intentionally not consumed: `_SEMANTIC.md` (invalid evidence per human ruling) and `_STATUS.md` (outside the human-authorized evidence set for this run).
- Anchor doc selected by AUTO: `Datasheet.md`.
- Execution doc order selected by AUTO: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- [RESOLVED] SOURCE_STATE: D-APP-38 current authority-corpus reconciliation supersedes the prior PRD source-state warning; PRD-derived dependency evidence is accepted for this tranche.
- [WARNING] TBD_IMPLEMENTATION_PATHS: current route/session implementation paths, lock storage mechanism, event writer API, exact test file locations, and full interrupt/cancel mapping remain TBD and were not converted into invented dependency targets.
- [WARNING] ID_FORMAT_TOOL_MISMATCH: `tools/validation/validate_id_format.sh` expects `DEL-NNN-NN` and `PKG-NNN`, but the accepted decomposition uses `DEL-03-02` and `PKG-03`; authoritative decomposition IDs were preserved.
- 2026-09-05 dependency-extract run (SCA-APP-010 post-Gate-5 pass; run `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, instance `N1-TASK-DEL-03-02`; FUTURE_WRITE_SET DEP-009/DEP-010; report-only preview, `ApplyEdits: false`) used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=RECONCILIATION.
- 2026-09-05 decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at the pinned identity (SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; applied row L318; Scope Ledger L412, L413, L414, L441, L486; SSOW L180, L253; OBJ-002 L263; PKG-03 L281; OI-008 L602; DEC-025 L634); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`.
- 2026-09-05 source docs used: `ScopeOfWork.md` (ANCHOR_DOC; explicit), `_CONTEXT.md`, `_STATUS.md` (`## Remaining` only, as owner-adopted information-flow signals), `_REFERENCES.md` (pointer resolution only), existing `Dependencies.csv` and `_DEPENDENCIES.md`. Execution doc order (explicit): `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`. Excluded: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `_run_records/**`.
- 2026-09-05 legacy four-document kit (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) no longer exists in this folder (SOW_V1 consolidation). Rows DEP-03-02-001 to DEP-03-02-006 and DEP-03-02-010 were re-evidenced to live bytes in `ScopeOfWork.md`; stale decomposition line pointers in `TargetLocation` were refreshed to the applied file. No row was retired: every existing relation is restated in the live sources.
- 2026-09-05 added anchors DEP-03-02-011 (SOW-083, new on the applied row per SCA-APP-010/DEC-025) and DEP-03-02-012 (OBJ-002; `TargetType=UNKNOWN` because the schema has no OBJECTIVE enum). Added execution rows DEP-03-02-014 (UPSTREAM CONSTRAINT, EXTERNAL: Root DEL-02-11 delegation-policy session-record field, OI-008) and DEP-03-02-015 (UPSTREAM INTERFACE, EXTERNAL: Root-owned daemon session lifecycle and one-active-turn lock). Root-owned targets carry `TargetLocation=TBD` and `SatisfactionStatus=PENDING`; no Root path is named. The execution row first proposed as DEP-03-02-013 (DOWNSTREAM INTERFACE to DEL-08-04: bound per-chat delegation policy) is held under brief amendment v1.1 section A and is not in this register (see the HELD bullet below).
- 2026-09-05 brief amendment v1.1 (HELP_HUMAN, after fan-in of the thirteen N1 previews; `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md`) applied by the rerun instance `N1-TASK-DEL-03-02`: section A removed DEP-03-02-013 from this post-image (the fan-in simulation `Evidence/fanin_simulation_v1/edge_analysis.json` shows the fifteen newly proposed deliverable edges, taken together, would merge SCC-001 into a 20-node SCC; choosing among them is a human-gated cut per `docs/CYCLE_DRIVEN_RESOLUTION.md`); section B permitted an evidence-field-only refresh of the SCC-internal rows DEP-03-02-007, DEP-03-02-008, and DEP-03-02-009.
- HELD (non-emitted proposal, pending owner ruling): DEP-03-02-013 reserved — DEL-03-02 → DEL-08-04 (DOWNSTREAM INTERFACE: bound per-chat delegation policy honoured by the Type 2 Subagent Governance Bridge) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-015
- 2026-09-05 SCC-internal rows DEP-03-02-007 (DEL-05-02), DEP-03-02-008 (DEL-03-03), and DEP-03-02-009 (DEL-03-04) had `EvidenceFile`, `SourceRef`, `EvidenceQuote`, the `TargetLocation` line pointer, and `LastSeen` refreshed to live bytes under amendment v1.1 section B: 007 `Specification.md#Requirements` → `ScopeOfWork.md#CLM-009 — Requirements (DEL-03-02-REQ-008)` (L203; `TargetLocation` `:313` → `:337`); 008 `Procedure.md#Steps` → `ScopeOfWork.md#CLM-009 — Requirements (DEL-03-02-REQ-007)` (L202; `:295` → `:319`); 009 `Guidance.md#Trade-offs` → `ScopeOfWork.md#CLM-023 — Trade-offs` (L466; `:296` → `:320`). `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, `TargetDeliverableID`, `Status`, `Statement`, `SatisfactionStatus`, `Origin`, and `FirstSeen` are frozen and unchanged; `Notes` was also left unchanged because it is outside the amendment's enumerated refresh set (this bullet carries the provenance instead). No legacy-kit pointer remains in the register.
- 2026-09-05 fence results: F1 (SCC-001 membership: DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05) — no new EXECUTION row has both endpoints inside SCC-001; SCC-internal rows DEP-03-02-007, DEP-03-02-008, and DEP-03-02-009 are evidenced by `ScopeOfWork.md` live bytes (REQ-008, REQ-007, CLM-023) with their graph-bearing fields frozen; no SCC-internal edge added or retired. F2 — no Root path in any `TargetLocation`. F3 — new rows are limited to relations introduced or revised by SOW-010 L180, SOW-083 L253, and the applied row L318 prose; the DEL-08-04 relation is held (H-015), not emitted.
- [RESOLVED 2026-09-05 under amendment v1.1 section B] NEEDS_HUMAN_GRAPH_DECISION for DEP-03-02-007, DEP-03-02-008, DEP-03-02-009: the v1 preview held these SCC-internal rows byte-identical except `LastSeen`, leaving retired legacy-kit pointers (`Specification.md#Requirements`, `Procedure.md#Steps`, `Guidance.md#Trade-offs`) that failed the live-bytes evidence check. The amendment's clarification of F1 permits the evidence-field refresh recorded above; every ACTIVE row now resolves to live bytes and no NEEDS_HUMAN_GRAPH_DECISION entry remains.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: `tools/validation/validate_id_format.sh` generic profile rejects the accepted App two-digit IDs (`DEL-03-02`, `PKG-03`, `DEP-03-02-011`, `SOW-083`); `OBJ-002` passes. No ID was changed.
- [WARNING] TBD_IMPLEMENTATION_PATHS remains open: Root locations for DEP-03-02-014 and DEP-03-02-015 are `TBD` by convention; exact App boot/session route and session-manager binding paths are the seated write locus of DEL-03-02-V3-01 and were not converted into dependency targets.
- 2026-09-05 no `[WARNING] FLOATING_NODE` or `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `ANCHOR` / `IMPLEMENTS_NODE` row (DEP-03-02-001). No `[WARNING] MISSING_DECOMPOSITION`.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 14 |
| RETIRED rows | 0 |
| ANCHOR rows | 7 |
| EXECUTION rows | 7 |
| DECLARED rows | 0 |
| EXTRACTED rows | 14 |

| DependencyID | Class | Direction | Type | Target | Status |
|---|---|---|---|---|---|
| DEP-03-02-001 | ANCHOR | UPSTREAM | OTHER | PKG-03 Runtime Engine Contract and Turn Lifecycle | ACTIVE |
| DEP-03-02-002 | ANCHOR | UPSTREAM | OTHER | SOW-009 Session CRUD | ACTIVE |
| DEP-03-02-003 | ANCHOR | UPSTREAM | OTHER | SOW-010 Session boot-request binding including per-chat delegation policy | ACTIVE |
| DEP-03-02-004 | ANCHOR | UPSTREAM | OTHER | SOW-011 SSE turn stream and session locking | ACTIVE |
| DEP-03-02-005 | ANCHOR | UPSTREAM | OTHER | SOW-038 Thin TurnEngine and route extraction | ACTIVE |
| DEP-03-02-006 | EXECUTION | UPSTREAM | INTERFACE | DEL-03-01 AgentEnginePort and Engine Conformance Suite | ACTIVE |
| DEP-03-02-007 | EXECUTION | UPSTREAM | INTERFACE | DEL-05-02 HarnessEvent Schema and Append-Only JSONL | ACTIVE |
| DEP-03-02-008 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-03-03 Harness API and SSE Compatibility Adapter | ACTIVE |
| DEP-03-02-009 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-03-04 Interrupt Cancel and Terminal Outcome Handling | ACTIVE |
| DEP-03-02-010 | EXECUTION | DOWNSTREAM | ENABLES | DEL-09-03 Unit and Integration Test Expansion | ACTIVE |
| DEP-03-02-011 | ANCHOR | UPSTREAM | OTHER | SOW-083 Per-chat delegation policy carried with the session | ACTIVE |
| DEP-03-02-012 | ANCHOR | UPSTREAM | OTHER | OBJ-002 App-client conformance to Root-owned runtime contracts (TargetType UNKNOWN) | ACTIVE |
| DEP-03-02-014 | EXECUTION | UPSTREAM | CONSTRAINT | EXTERNAL Root DEL-02-11 delegation-policy session-record field (location TBD) | ACTIVE |
| DEP-03-02-015 | EXECUTION | UPSTREAM | INTERFACE | EXTERNAL Root-owned daemon session lifecycle and one-active-turn lock (location TBD) | ACTIVE |

## Lifecycle Summary

| Field | Count |
|---|---:|
| ACTIVE | 14 |
| RETIRED | 0 |
| SatisfactionStatus=PENDING | 9 |
| SatisfactionStatus=SATISFIED | 5 |
| SatisfactionStatus=TBD | 0 |
| ProposedMaturity=TBD | 9 |

No `[WARNING] FLOATING_NODE` condition: one ACTIVE `ANCHOR` / `IMPLEMENTS_NODE` row exists.

No `[WARNING] AMBIGUOUS_ANCHOR` condition: exactly one ACTIVE `ANCHOR` / `IMPLEMENTS_NODE` row exists.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-09-05 | UPDATE | CONSERVATIVE | found at the pinned identity `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; SCA-APP-010 Gate 5 applied; report-only preview, rerun under brief amendment v1.1) | 14 | PROJECT_ID_FORMAT_PROFILE; TBD_IMPLEMENTATION_PATHS; HELD DEP-03-02-013 (H-015, pending owner ruling); NEEDS_HUMAN_GRAPH_DECISION for DEP-03-02-007/008/009 resolved by amendment v1.1 section B |
| 2026-06-21 03:00 | ADQ-05 | CONSERVATIVE | D-APP-38 current authority corpus and D-APP-40 runtime taxonomy applied | 10 | TBD_IMPLEMENTATION_PATHS; ID_FORMAT_TOOL_MISMATCH |
| 2026-05-20 19:30 | UPDATE | CONSERVATIVE | available: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | 10 | superseded source-state warning; TBD_IMPLEMENTATION_PATHS; ID_FORMAT_TOOL_MISMATCH |

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-115
- **Current counts:** ACTIVE 10; RETIRED 0; PENDING=5; SATISFIED=5.
- **Correction:** DEP-03-02-006 through DEP-03-02-010 are live-reverified SATISFIED.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
- Superseded 2026-09-05: the `## Extracted Dependency Register` and `## Lifecycle Summary` sections above are the current structured-register mirror; this block is retained as dated evidence and its counts describe the 2026-07-12 register.

## Downstream Handoff Notes

- CONSUMER_CONTEXT=RECONCILIATION (2026-09-05). Accepted upstream snapshot: applied decomposition `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (SCA-APP-010 Gate 5; pointer `_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`).
- Claim-level concordance targets: applied row L318 scope refs SOW-009, SOW-010, SOW-011, SOW-038, SOW-083 and objective OBJ-002 are each anchored (DEP-03-02-002 to 005, 011, 012); the applied row's Root-ownership notes are carried as EXTERNAL rows DEP-03-02-014 and DEP-03-02-015 with `TargetLocation=TBD` (never a Root path).
- Held proposal: the DEL-03-02 → DEL-08-04 edge for the bound per-chat delegation policy (reserved ID DEP-03-02-013) is a non-emitted proposal in `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv` H-015 pending the owner's separate cycle-resolution transaction; the reciprocal DEL-08-04 row is held likewise (H-019). DEL-03-01, DEL-09-03, DEL-03-03, DEL-03-04, and DEL-05-02 registers already carried by earlier passes are unchanged by this preview.
- SCC-001 posture: this carrier is a member; no SCC-internal edge was added or retired; DEP-03-02-007/008/009 had evidence fields refreshed to live bytes under amendment v1.1 section B with every graph-bearing field frozen. Cycle resolution (decompose / invert / merge / cut) remains the cycle-resolution workflow's, not this pass's.
- Satisfaction posture: 5 SATISFIED rows (DEP-03-02-006 to 010; D-APP-56 R5 P45 UPD-115 live re-verification preserved) and 9 PENDING rows (the seven anchors plus the two EXTERNAL execution rows); PENDING execution rows resolve through DEL-03-02-V3-01 (App side) and Root DEL-02-11 acceptance routed per OI-008 (Root side).
- This file is a derivative package; it cites the accepted upstream snapshot above and is not decomposition truth.
