# Dependencies: DEL-08-04 Type 2 Subagent Governance Bridge

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no declared upstream dependency edges have been accepted outside the extracted register.

## Declared Downstream

TBD - no declared downstream dependency edges have been accepted outside the extracted register.

## Extracted Dependency Register

| Metric | Count |
|---|---:|
| Total rows | 13 |
| ACTIVE rows | 12 |
| RETIRED rows | 1 |
| ANCHOR rows | 4 |
| EXECUTION rows | 9 |

| DependencyID | Class | Direction | Type | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-08-04-001 | ANCHOR | UPSTREAM | OTHER | WBS_NODE | SOW-063 Project delegation authority, daemon-client dispatch, and checkout AgentRuns | ACTIVE |
| DEP-08-04-002 | EXECUTION | UPSTREAM | PREREQUISITE | DOCUMENT | Accepted source corpus for DEL-08-04 | ACTIVE |
| DEP-08-04-003 | EXECUTION | UPSTREAM | PREREQUISITE | UNKNOWN | Existing `evaluateSubagentGovernance` behavior or target contract | ACTIVE |
| DEP-08-04-004 | EXECUTION | UPSTREAM | PREREQUISITE | UNKNOWN | Permission overlay and hook infrastructure | ACTIVE |
| DEP-08-04-005 | EXECUTION | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-04-01 SDK Probe and Version-Pinned Adoption Decision | RETIRED |
| DEP-08-04-006 | EXECUTION | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-08-05 Subagent Child Run Records and Artifacts | ACTIVE |
| DEP-08-04-007 | ANCHOR | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 Project capability policy and conformance | ACTIVE |
| DEP-08-04-008 | ANCHOR | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 Agent-suite integrity and project delegation authority | ACTIVE |
| DEP-08-04-009 | EXECUTION | UPSTREAM | INTERFACE | EXTERNAL | Chirality-managed delegation class | ACTIVE |
| DEP-08-04-010 | EXECUTION | UPSTREAM | INTERFACE | EXTERNAL | delegated-harness-native descent class | ACTIVE |
| DEP-08-04-011 | EXECUTION | UPSTREAM | CONSTRAINT | EXTERNAL | Root WP-03/WP-05 fixtures: accepted DEL-02-07 process-supervisor and DEL-02-10 API v2 returns | ACTIVE |
| DEP-08-04-012 | ANCHOR | UPSTREAM | OTHER | REQUIREMENT | SOW-083 Per-chat delegation policy carried with the session and honoured by the managed delegation bridge | ACTIVE |
| DEP-08-04-014 | EXECUTION | UPSTREAM | INTERFACE | EXTERNAL | Root DEL-02-11 daemon session-record delegation-policy field | ACTIVE |

## Run Notes

- Runtime overrides: `SCOPE=DEL-08-04_Type_2_Subagent_Governance_Bridge`; `DECOMPOSITION_PATH=/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Instruction root: initial shell environment did not expose `CHIRALITY_INSTRUCTION_ROOT`; the supervising runtime then supplied additive declaration `V2_INSTRUCTION_ROOT_RUNTIME_DECLARATION.md`. Re-preflight passed with `/Users/ryan/.codex/worktrees/ef5e/chirality` and the original sealed brief remained otherwise unchanged.
- Source selection: `SOURCE_DOCS=AUTO`; `DOC_ROLE_MAP=DEFAULT`; `ANCHOR_DOC=ScopeOfWork.md` with `_CONTEXT.md` traceability cross-check; `EXECUTION_DOC_ORDER=ScopeOfWork.md, Assessment_INSP-03_DEL-08-04.md, _REFERENCES.md, applied decomposition carrier row`.
- Source-preservation gate: `ScopeOfWork.md`, `_CONTEXT.md`, `Assessment_INSP-03_DEL-08-04.md`, and current v19 `_REFERENCES.md` were read-only. `_SEMANTIC.md` was not used as dependency evidence.
- Decomposition authority was present at exact SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` and used to resolve SOW-063, OBJ-005, OBJ-007, DEL-08-04, DEL-08-05, and the two descendant classes.
- Pass 1 — ANCHOR: stable parent anchor DEP-08-04-001 was refreshed; explicit OBJ-005 and OBJ-007 trace anchors were added as DEP-08-04-007 and DEP-08-04-008.
- Pass 2 — EXECUTION: stable IDs DEP-08-04-002 through DEP-08-04-006 were preserved. DEP-08-04-005 was retained non-destructively as RETIRED because the refreshed local source no longer states SDK-probe or DEL-04-01 information flow.
- Descendant-class gate: DEP-08-04-009 is the one ACTIVE row for the Chirality-managed class; DEP-08-04-010 is the one ACTIVE row for the delegated-harness-native class. They remain distinct. The native row explicitly does not infer Agent 2 or any Agent role from native descent.
- A2-B posture: existing DEL-08-04 → DEL-08-05 handoff remains DEP-08-04-006 and corresponds to E-019. E-020 (DEL-08-05 feedback to DEL-08-04) remains non-gating; it is not emitted as a register row because the allowed local source does not state a reverse information/artifact transfer. No SCC schedule gate or silent linearization was introduced.
- [RESOLVED] SOURCE_STATE: current v19 `_REFERENCES.md` reports all seven source identities MATCH.
- [RESOLVED] CHILD_OUTPUT_ARTIFACT_EVIDENCE: ADQ-12 closes the package-level DEL-08-05 child-output artifact proof residual without changing either descendant-class boundary.
- [WARNING] TARGET_UNRESOLVED: permission overlay and hook infrastructure remain an explicit prerequisite without one stable target deliverable in the local source.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the repository's generic `validate_id_format.sh` expects `PKG-NNN`, `DEL-NNN-NN`, `DEP-NNN-NN-NNN`, and `SOW-NNNN`; this accepted App decomposition uses `PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, and `SOW-NNN`. Validation therefore reports the project IDs invalid by its generic profile. No accepted project ID was rewritten or invented.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.

## Run Notes - 2026-09-03 v3 pathway seating (additive UPDATE)

- `TASK + dependency-extract` method applied in-line by the A12 seating tranche (ephemeral Agent 2 generalist; no TASK run record under `_run_records/` because that path is outside the tranche write set); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; `ScopeOfWork.md` re-pinned to that commit in the same tranche.
- Scope of this pass: exactly one new row, `DEP-08-04-011`, making the v3 gate/interface edge consumed by the seated `Remaining` item explicit. Existing rows are preserved byte-identically (no `LastSeen` refresh, no retirement); the full two-pass re-extraction is not claimed for them.
- Evidence: `ScopeOfWork.md` at `ScopeOfWork.md#REQ-005`; quote: "D-GOV-35 is necessary, but App carrier acceptance and WP-03/05 fixtures remain required before v3 delegation work".
- Target resolution: Root-owned targets keep `TargetLocation=TBD` (no Root path is invented); deliverable targets resolve against the applied decomposition.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities; accepted decomposition IDs are preserved (same finding as the Gate-5 refresh).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- A2-B / SCC posture: no objective-relative feedback edge was added or linearized; the post-application audit's nine-node SCC remains a warning-bearing derivative finding.
- Schema validation: `python3 tools/validation/validate_dependencies_schema.py Dependencies.csv` PASS after the append; see `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/DEPENDENCY_REFRESH.md`.

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (report-only preview; UPDATE)

- Dispatch: `TASK + dependency-extract` as managed child `N1-TASK-DEL-08-04` of run `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` (parent HELP_HUMAN; authorization SCA-APP-010 `FUTURE_WRITE_SET.csv` rows DEP-025 and DEP-026). This pass is a report-only preview: the post-images were written under the instance folder only; no carrier byte changed. The reviewed write is a separate act. Rerun under brief amendment v1.1 (`AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md`, section A/D): the fan-in simulation of all thirteen previews showed the DEL-03-02 binding edge lies on a collective cycle with fourteen other newly proposed edges, so it is held as a non-emitted proposal for the owner's separate transaction and removed from this post-image; nothing else changed.
- Runtime overrides: `SCOPE=DEL-08-04_Type_2_Subagent_Governance_Bridge`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ApplyEdits=false`. `_STATUS.md` was read only for its `## Remaining` section; `_REFERENCES.md` resolved pointers; `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, and `_run_records/**` were excluded.
- Decomposition: found at the pinned identity, SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); carrier row L371 (scope refs SOW-063, SOW-083; objectives OBJ-005, OBJ-007); amended Scope Ledger row SOW-083 L253; reverse view L486; OI-008 L602; DEC-025 L634. Companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`.
- Pass 1 (ANCHOR): DEP-08-04-001 (`IMPLEMENTS_NODE` SOW-063) preserved and re-validated; DEP-08-04-007/008 (OBJ-005/OBJ-007) re-evidenced to the live traceability line; DEP-08-04-012 added for SOW-083, which SCA-APP-010 placed on this carrier's applied row. No anchor points to a scope ref that left the row, so no anchor was retired. SOW-081, SOW-082, and SOW-084 are not on this carrier's row and receive no anchor here.
- Pass 2 (EXECUTION): DEP-08-04-002/003/004/006/009/010/011 remain stated in the live sources and were refreshed (`LastSeen=2026-09-05`). One row was added for the relation SOW-083 introduces: DEP-08-04-014 (UPSTREAM INTERFACE, `EXTERNAL`, Root DEL-02-11 session-record delegation-policy field; `TargetLocation=TBD`, `SatisfactionStatus=PENDING`). The second SOW-083 relation, the DEL-03-02 per-chat delegation-policy binding, was extracted in the v1 preview as DEP-08-04-013 and is held under amendment v1.1 (next bullet).
- HELD (non-emitted proposal, pending owner ruling): DEP-08-04-013 reserved — DEL-08-04 -> DEL-03-02 UPSTREAM INTERFACE (the managed delegation bridge consumes the per-chat delegation policy that DEL-03-02 binds into the App session boot request; SOW-010, SOW-083; evidence `_STATUS.md#Remaining` DEL-08-04-V3-02 Depends line, decomposition L371/L253/L318/L413) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-019. The ID is not reused; the row is not in this register until the owner rules on the held set (`docs/CYCLE_DRIVEN_RESOLUTION.md`: cut and merge are human-gated; cycle-participating edges stay non-gating until resolved).
- Legacy four-document kit: no row cites `Datasheet.md`, `Specification.md`, `Guidance.md`, or `Procedure.md`; no re-evidencing on that ground was needed. DEP-08-04-005 (RETIRED 2026-08-24) is preserved byte-identically.
- Considered and not emitted (no named artifact, contract, tool, event, or policy transfer stated for this carrier): the SOW-006 / DEL-02-02 ownership boundary ("DEL-08-04 retains role/delegation semantics"; the view presents accepted state); the SOW-081 workflow-file delegation-policy declaration (DEL-07-03 owns the file contract; no consumption by this bridge is stated); the `NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected` gate on DEL-08-04-V3-02 (selection ordering, not information flow); the root `AGENTS.md` graph reference (unchanged since Gate 5; not re-derived). E-020 (DEL-08-05 feedback) remains non-gating and is not emitted, as at Gate 5.
- Fence F1 (SCC-001 membership): NONE. After amendment v1.1 no row in this post-image targets an SCC-001 member; the nine SCC-001 registers hold no ACTIVE row to DEL-08-04 and the baseline closure graph has no path from any SCC-001 member to DEL-08-04 (only DEL-08-05 and DEL-09-02 depend on DEL-08-04), so this carrier stays outside SCC-001 and no SCC-internal edge or retirement is proposed. The held DEL-03-02 edge passed F1 in isolation (v1 preview) and is held only because of the collective fan-in cycle. `FENCE_F1_CANDIDATES`: none.
- Fence F2 (Root path): NONE. Root DEL-02-11 is represented as `EXTERNAL` with `TargetLocation=TBD`. `FENCE_F2_CANDIDATES`: none. Observation: pre-existing DEP-08-04-003 keeps its Gate-5 `TargetLocation=frontend/src/lib/harness/subagent-governance.ts` (App-owned code, not a Root path; also the seated items' write locus); preserved as prior state.
- Fence F3 (permitted effect): NONE. The two new rows derive from the amended SOW-083 row and the applied-row prose ("Honour the per-chat delegation policy carried with the session"); none derives from SCC ordering, schedule, or coordination statements.
- `NEEDS_HUMAN_GRAPH_DECISION`: none.
- [WARNING] TARGET_UNRESOLVED: permission overlay and hook infrastructure (DEP-08-04-004) remain an explicit prerequisite without one stable target deliverable in the local source.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` three-digit profile rejects the accepted App two-digit IDs (`PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, `SOW-NNN`); no accepted ID was rewritten (same finding as Gate 5 and A12).
- [NOTE] CONTEXT_TRACEABILITY_LAG: `_CONTEXT.md#Traceability` and `ScopeOfWork.md` CLM-002 still list `CoversScopeItems: SOW-063` only; the `ScopeOfWork.md` front matter (`project_scope_refs: [SOW-063, SOW-083]`) and the applied row control. No source document was edited.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- Function 5 (re-run on the amended post-image): `validate_dependencies_schema.py` VALID (29 columns, 13 data rows); every emitted enum value VALID (29 distinct values); `DependencyID` unique (DEP-08-04-013 reserved, absent); `FromDeliverableID=DEL-08-04` on every row; every ACTIVE row carries `EvidenceFile` and `SourceRef` that resolve to live bytes; `Status=CANDIDATE` absent.

## Run History

- 2026-09-05T00:59:00-06:00: `TASK + dependency-extract` (managed child `N1-TASK-DEL-08-04`, report-only preview; v1 pass 00:40, rerun under brief amendment v1.1), `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, applied decomposition found at the pinned identity `c7c05169…1e61` (commit `dbd812a52`); two rows added (DEP-08-04-012, DEP-08-04-014), one proposal held non-emitted with its ID reserved (DEP-08-04-013, HELD_EDGE_PROPOSALS.csv H-019), ten ACTIVE rows refreshed, DEP-08-04-005 preserved RETIRED; warnings: TARGET_UNRESOLVED x1, PROJECT_ID_FORMAT_PROFILE; fences F1/F2/F3 NONE; ACTIVE=12 (ANCHOR=4, EXECUTION=8); RETIRED=1.
- 2026-09-03T00:00:00-06:00: `TASK + dependency-extract` method in-line (A12 seating), `MODE=UPDATE` additive, `STRICTNESS=CONSERVATIVE`, applied decomposition `d6f6cadb2` verified; one row `DEP-08-04-011` added; existing rows preserved without LastSeen refresh; warnings: PROJECT_ID_FORMAT_PROFILE; ACTIVE=10; RETIRED=1.
- 2026-08-24T00:53:16-06:00: `TASK + dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, applied decomposition verified, current v19 references preserved, E-020 retained non-gating without a source-invented edge. ACTIVE counts: ANCHOR=3, EXECUTION=6; RETIRED=1.
- 2026-06-21T05:00: ADQ-12 recorded child-output artifact evidence closure for the DEL-08-04 downstream handoff; remaining warnings: TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.
- 2026-06-21T03:00: ADQ-05 applied D-APP-38 source-state reconciliation and D-APP-40 child-run handoff naming; remaining warnings: TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.
- 2026-05-20T20:54: `TASK + dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, decomposition located, warnings: superseded source-state warning, TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 12 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 6 |
| PENDING | 4 |
| TBD | 3 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor (SOW-063), three trace anchors (OBJ-005, OBJ-007, SOW-083), four retained ACTIVE prerequisite/handover rows, one retired inferred SDK-probe edge, the two distinct class-interface rows, the Root WP-03/05 fixture constraint, and the one emitted SOW-083 delegation-policy interface row (Root DEL-02-11 session-record field, `EXTERNAL`/`TBD`/`PENDING`).
- The DEL-03-02 delegation-policy binding edge (reserved DEP-08-04-013) is a held, non-emitted proposal (HELD_EDGE_PROPOSALS.csv H-019); do not reconcile it as a register row until the owner rules on the held set. Any reverse DEL-03-02 -> DEL-08-04 relation would need its own source statement and an owner ruling before emission.
- DEP-08-04-014 and DEP-08-04-011 close only after the OI-008 Root returns are routed to App; do not treat either as satisfied on App-side evidence alone.
- Preserve the non-gating E-020 posture outside this local register unless a future accepted DEL-08-04 source names a concrete reverse information artifact.
- This pass is a report-only preview; the carrier register changes only after the reviewed write (SCA-APP-010 DEP-025/DEP-026).

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-137
- **Historical counts at that update:** ACTIVE 6; RETIRED 0; PENDING=1; SATISFIED=2; TBD=3.
- **Correction recorded at that update:** DEP-08-04-003 resolves to evaluateSubagentGovernance and is SATISFIED.
- Later extraction history above supersedes these counts while preserving this dated record.

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion in the earlier run history
that `_SEMANTIC.md` was invalid dependency-extraction evidence is scoped to
dependency rows. Its recorded consumption as the primary input to
`_SEMANTIC_LENSING.md` is a different act, outside that scope and consistent
with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.
