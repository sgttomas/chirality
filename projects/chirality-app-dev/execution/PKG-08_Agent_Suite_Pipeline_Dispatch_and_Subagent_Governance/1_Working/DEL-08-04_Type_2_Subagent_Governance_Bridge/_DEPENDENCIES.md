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
| Total rows | 6 |
| ACTIVE rows | 6 |
| RETIRED rows | 0 |
| ANCHOR rows | 1 |
| EXECUTION rows | 5 |

| DependencyID | Class | Direction | Type | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-08-04-001 | ANCHOR | UPSTREAM | OTHER | WBS_NODE | SOW-063 Governed subagent runtime | ACTIVE |
| DEP-08-04-002 | EXECUTION | UPSTREAM | PREREQUISITE | DOCUMENT | Accepted source corpus for DEL-08-04 | ACTIVE |
| DEP-08-04-003 | EXECUTION | UPSTREAM | PREREQUISITE | UNKNOWN | Existing `evaluateSubagentGovernance` behavior or target contract | ACTIVE |
| DEP-08-04-004 | EXECUTION | UPSTREAM | PREREQUISITE | UNKNOWN | Permission overlay and hook infrastructure | ACTIVE |
| DEP-08-04-005 | EXECUTION | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-04-01 SDK Probe and Version-Pinned Adoption Decision | ACTIVE |
| DEP-08-04-006 | EXECUTION | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-08-05 Subagent Child Run Records and Artifacts | ACTIVE |

## Run Notes

- Runtime overrides: `SCOPE=DEL-08-04`; `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`.
- Source selection: `SOURCE_DOCS=AUTO`; `DOC_ROLE_MAP=DEFAULT`; `ANCHOR_DOC=Datasheet.md` with `_CONTEXT.md` traceability cross-check; `EXECUTION_DOC_ORDER=Procedure.md, Specification.md, Guidance.md, Datasheet.md, _REFERENCES.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Decomposition authority located and used for DEL-08-04, SOW-063, DEL-04-01, and DEL-08-05 resolution.
- [RESOLVED] SOURCE_STATE: D-APP-38 current authority-corpus reconciliation supersedes the prior REF-006 source-state warning for this tranche.
- [RESOLVED] CHILD_OUTPUT_ARTIFACT_EVIDENCE: ADQ-12 closes the package-level DEL-08-05 child-output artifact proof residual without changing the Type 2 governance gate or exposing new child capabilities.
- [WARNING] TARGET_UNRESOLVED: `evaluateSubagentGovernance` implementation/target contract remains `TBD` in the source.
- [WARNING] TARGET_UNRESOLVED: permission overlay and hook infrastructure are explicit prerequisites, but no single stable target deliverable is named in the local source; the row preserves `TargetType=UNKNOWN`.
- [WARNING] TARGET_INFERRED: SDK probe prerequisite was resolved to DEL-04-01 from decomposition because the local source names SDK/R0/R1 probes rather than a deliverable ID.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.

## Run History

- 2026-06-21T05:00: ADQ-12 recorded child-output artifact evidence closure for the DEL-08-04 downstream handoff; remaining warnings: TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.
- 2026-06-21T03:00: ADQ-05 applied D-APP-38 source-state reconciliation and D-APP-40 child-run handoff naming; remaining warnings: TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.
- 2026-05-20T20:54: `TASK + dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, decomposition located, warnings: superseded source-state warning, TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 6 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 1 |
| PENDING | 1 |
| TBD | 4 |

## Downstream Handoff Notes

Not applicable; `CONSUMER_CONTEXT=NONE`.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-137
- **Current counts:** ACTIVE 6; RETIRED 0; PENDING=1; SATISFIED=2; TBD=3.
- **Correction:** DEP-08-04-003 resolves to evaluateSubagentGovernance and is SATISFIED.
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
