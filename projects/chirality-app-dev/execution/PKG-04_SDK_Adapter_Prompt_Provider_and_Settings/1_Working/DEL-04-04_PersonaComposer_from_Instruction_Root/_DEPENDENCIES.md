# Dependencies: DEL-04-04 PersonaComposer from Instruction Root

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

## Extracted Dependency Register

Generated register: `Dependencies.csv` v3.1

| Class | Type | Status | Count |
|---|---|---:|---:|
| ANCHOR | OTHER | ACTIVE | 3 |
| EXECUTION | CONSTRAINT | ACTIVE | 1 |
| EXECUTION | HANDOVER | ACTIVE | 1 |
| EXECUTION | INTERFACE | ACTIVE | 2 |
| EXECUTION | PREREQUISITE | ACTIVE | 1 |

| DependencyID | Class | Direction | Type | Target | Status | Confidence |
|---|---|---|---|---|---|---|
| DEP-DEL-04-04-001 | ANCHOR | UPSTREAM | OTHER | PKG-04 SDK Adapter, Prompt, Provider, and Settings | ACTIVE | HIGH |
| DEP-DEL-04-04-002 | ANCHOR | UPSTREAM | OTHER | SOW-017 Persona resolution and prompt composition | ACTIVE | HIGH |
| DEP-DEL-04-04-003 | ANCHOR | UPSTREAM | OTHER | SOW-030 Instruction-root resources | ACTIVE | HIGH |
| DEP-DEL-04-04-004 | EXECUTION | UPSTREAM | INTERFACE | DEL-04-02 SdkOptionsBuilder and Settings Isolation | ACTIVE | HIGH |
| DEP-DEL-04-04-005 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-08-01 Instruction Root Packaging and Agent Conformance | ACTIVE | HIGH |
| DEP-DEL-04-04-006 | EXECUTION | UPSTREAM | INTERFACE | DEL-08-02 Persona Alias and Agent Matrix Routing Contract | ACTIVE | MEDIUM |
| DEP-DEL-04-04-007 | EXECUTION | UPSTREAM | CONSTRAINT | docs/PRD.md PRD source snapshot | ACTIVE | HIGH |
| DEP-DEL-04-04-008 | EXECUTION | DOWNSTREAM | HANDOVER | UNKNOWN Runtime boundary boot/session fingerprint integration | ACTIVE | MEDIUM |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract update run timestamp: 2026-05-20T19:35:58-0600.
- Runtime overrides: `SCOPE=DEL-04-04`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition path used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; existing `_SEMANTIC.md` was not read or consumed.
- Anchor document selection: `Datasheet.md` and `_CONTEXT.md` traceability, validated against decomposition PKG-04 / DEL-04-04 / SOW rows.
- Execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, then `Datasheet.md`.
- Parent anchor status: one ACTIVE `IMPLEMENTS_NODE` anchor found; no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` records `docs/PRD.md` as `HASH_MISMATCH`; PRD-only details remain constrained until accepted snapshot confirmation.
- [WARNING] UNKNOWN_TARGET: runtime boundary boot/session fingerprint integration is explicit, but the local evidence does not name a stable consuming deliverable/interface; target preserved as `UNKNOWN` / `TBD`.
- No downstream handoff section was added because `CONSUMER_CONTEXT=NONE`.

## Run History

| Timestamp | Mode | Strictness | Decomposition | ACTIVE Anchors | ACTIVE Execution | Warnings |
|---|---|---|---|---:|---:|---|
| 2026-05-20T19:35:58-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found | 3 | 5 | PRD_HASH_MISMATCH; UNKNOWN_TARGET |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 3 |
| TBD | 5 |
