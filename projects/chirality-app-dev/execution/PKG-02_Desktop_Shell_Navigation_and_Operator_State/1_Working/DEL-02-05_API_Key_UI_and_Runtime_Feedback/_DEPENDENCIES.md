# Dependencies: DEL-02-05 API Key UI and Runtime Feedback

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been declared by a human.

## Declared Downstream

TBD - no accepted dependency edges have been declared by a human.

## Extracted Dependency Register

| DependencyID | Class | Type | Direction | TargetType | Target | Status | Evidence |
|---|---|---|---|---|---|---|---|
| DEP-02-05-001 | ANCHOR | OTHER | UPSTREAM | PACKAGE | PKG-02 Desktop Shell, Navigation, and Operator State | ACTIVE | `_CONTEXT.md` Identity; decomposition PKG-02 |
| DEP-02-05-002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-013 Typed runtime errors | ACTIVE | `_CONTEXT.md` Traceability; decomposition SOW ledger |
| DEP-02-05-003 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-019 API key storage and resolution | ACTIVE | `_CONTEXT.md` Traceability; decomposition SOW ledger |
| DEP-02-05-004 | EXECUTION | PREREQUISITE | UPSTREAM | UNKNOWN | Runtime/API key-status and secure-storage contracts | ACTIVE | `Procedure.md` Prerequisites |
| DEP-02-05-005 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN | Typed runtime/provider error taxonomy | ACTIVE | `Specification.md` Requirements |
| DEP-02-05-006 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN | Browser-facing SSE event contract | ACTIVE | `Procedure.md` Steps |

Counts:

- ACTIVE rows: 6
- ANCHOR rows: 3
- EXECUTION rows: 3
- UNKNOWN/TBD execution targets: 3

## Run Notes

- Run timestamp: 2026-05-20T19:30:46-0600.
- Runtime overrides: `SCOPE=DEL-02-05`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`.
- Decomposition path: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source policy: semantic lensing and P3 enrichment skipped by human ruling; `_SEMANTIC.md` was not read or consumed.
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Anchor doc choice: `Datasheet.md` plus `_CONTEXT.md` identity/traceability fields; decomposition used to validate `PKG-02`, `DEL-02-05`, `SOW-013`, and `SOW-019`.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- `[WARNING] TARGET_UNRESOLVED: Execution targets for key-status/secure-storage contracts, typed runtime/provider error taxonomy, and SSE event contract remain UNKNOWN/TBD because permitted source evidence does not assign accepted owning deliverable IDs.`
- `[WARNING] ID_FORMAT_VALIDATOR_MISMATCH: validate_id_format.sh rejects current decomposition IDs such as DEL-02-05, PKG-02, and SOW-013 because the script expects three-digit package/deliverable and four-digit SOW formats. Decomposition v3.2 IDs were preserved as authoritative.`
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- `[WARNING] TRACEABILITY_DELTA: decomposition SOW ledger also maps SOW-023 to DEL-02-05, but the DEL-02-05 decomposition row and _CONTEXT.md Traceability list only SOW-013 and SOW-019. No SOW-023 anchor row was emitted under conservative strictness.`
- Parent anchor check: PASS - exactly one ACTIVE `IMPLEMENTS_NODE` anchor.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:30:46-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` present | TARGET_UNRESOLVED; ID_FORMAT_VALIDATOR_MISMATCH; SOURCE_WARNING; TRACEABILITY_DELTA | ANCHOR=3; EXECUTION=3; TOTAL=6 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 6 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 6 |

Closure state:

- Required derivative package regenerated: `Dependencies.csv` v3.1.
- Required dependency index refreshed: `_DEPENDENCIES.md`.
- Remaining blockers: execution target ownership for three runtime/API contract dependencies is unresolved in permitted evidence and remains `UNKNOWN/TBD`.

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.
