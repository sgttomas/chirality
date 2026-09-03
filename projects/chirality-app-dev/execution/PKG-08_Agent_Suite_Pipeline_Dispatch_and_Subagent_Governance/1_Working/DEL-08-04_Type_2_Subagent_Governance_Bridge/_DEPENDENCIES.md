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
| Total rows | 11 |
| ACTIVE rows | 10 |
| RETIRED rows | 1 |
| ANCHOR rows | 3 |
| EXECUTION rows | 8 |

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

## Run History

- 2026-09-03T00:00:00-06:00: `TASK + dependency-extract` method in-line (A12 seating), `MODE=UPDATE` additive, `STRICTNESS=CONSERVATIVE`, applied decomposition `d6f6cadb2` verified; one row `DEP-08-04-011` added; existing rows preserved without LastSeen refresh; warnings: PROJECT_ID_FORMAT_PROFILE; ACTIVE=10; RETIRED=1.
- 2026-08-24T00:53:16-06:00: `TASK + dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, applied decomposition verified, current v19 references preserved, E-020 retained non-gating without a source-invented edge. ACTIVE counts: ANCHOR=3, EXECUTION=6; RETIRED=1.
- 2026-06-21T05:00: ADQ-12 recorded child-output artifact evidence closure for the DEL-08-04 downstream handoff; remaining warnings: TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.
- 2026-06-21T03:00: ADQ-05 applied D-APP-38 source-state reconciliation and D-APP-40 child-run handoff naming; remaining warnings: TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.
- 2026-05-20T20:54: `TASK + dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, decomposition located, warnings: superseded source-state warning, TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 5 |
| PENDING | 3 |
| TBD | 3 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor, two objective trace anchors, four retained ACTIVE prerequisite/handover rows, one retired inferred SDK-probe edge, and the two distinct class-interface rows.
- Preserve the non-gating E-020 posture outside this local register unless a future accepted DEL-08-04 source names a concrete reverse information artifact.

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
