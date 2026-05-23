# Dependencies: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

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
- 2026-05-20 TASK + dependency-extract ran in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` identity/traceability fields.
- Execution doc order: `Specification.md`, `Procedure.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition path: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for anchor/target labels.
- [WARNING] REF-006 `docs/PRD.md` has `HASH_MISMATCH` in `_REFERENCES.md`; PRD-derived statements remain warning-qualified in source documents.
- [WARNING] OI-001 / DEL-04-01 probe evidence is still `TBD`; exact SDK message payload shapes were not inferred.
- [WARNING] `tools/validation/validate_id_format.sh` expects legacy `PKG-000` / `DEL-000-00` forms and rejects authoritative v3.2 IDs such as `PKG-04` and `DEL-04-03`; decomposition-authoritative IDs were preserved.

## Extracted Dependency Register

`Dependencies.csv` v3.1 was created on 2026-05-20 with conservative evidence-first rows only.

| Count | DependencyClass | Notes |
|---:|---|---|
| 6 | ANCHOR | One parent anchor and five trace anchors. |
| 5 | EXECUTION | Explicit prerequisite/interface/handoff/constraint edges only. |
| 11 | TOTAL | All rows `Status=ACTIVE`, `Origin=EXTRACTED`. |

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-DEL-04-03-001 | ANCHOR | OTHER | UPSTREAM | DEL-04-03 | ACTIVE |
| DEP-DEL-04-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-040 | ACTIVE |
| DEP-DEL-04-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-044 | ACTIVE |
| DEP-DEL-04-03-004 | ANCHOR | OTHER | UPSTREAM | SOW-051 | ACTIVE |
| DEP-DEL-04-03-005 | ANCHOR | OTHER | UPSTREAM | OBJ-002 | ACTIVE |
| DEP-DEL-04-03-006 | ANCHOR | OTHER | UPSTREAM | OBJ-004 | ACTIVE |
| DEP-DEL-04-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 | ACTIVE |
| DEP-DEL-04-03-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-01 | ACTIVE |
| DEP-DEL-04-03-009 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-03 | ACTIVE |
| DEP-DEL-04-03-010 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-05-02 | ACTIVE |
| DEP-DEL-04-03-011 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-04-02 | ACTIVE |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:35:55-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` used | REF-006 hash mismatch; OI-001 probe TBD; ID-format helper legacy mismatch | ANCHOR=6; EXECUTION=5; TOTAL=11 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 11 |
