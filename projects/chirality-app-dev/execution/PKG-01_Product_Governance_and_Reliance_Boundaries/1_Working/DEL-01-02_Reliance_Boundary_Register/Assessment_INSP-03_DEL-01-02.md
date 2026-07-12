# Assessment INSP-03: DEL-01-02 Reliance Boundary Register

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-01-02 |
| Package | PKG-01 Product Governance and Reliance Boundaries |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `e2e9806c3fe9d2420372af8e771f9e4d5bb7d648` |
| Spec source | `Specification.md` lines 29-89 |

## Scope

DEL-01-02 is intended to produce the reliance-boundary register for P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, human-gate, runtime-engine, tool-surface, hook, redaction, and fallback boundaries. The final package is expected to include `docs/harness/reliance_boundary_register.md`, an enforcement matrix, and a Section 9 keyed test index (`Specification.md` lines 83-89).

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| RBR-001 | PARTIAL | `Specification.md` line 29; `Datasheet.md` lines 80-92; shell check found no `docs/harness/reliance_boundary_register.md`. | The schema is specified locally, but the central generated register is absent. |
| RBR-002 | PARTIAL | `Specification.md` line 30; `docs/CONTRACT.md` lines 8 and 58-59; `Guidance.md` lines 15-21. | The no-prompt-only rule is documented, but final row-level proof is not available without the register. |
| RBR-003 | PARTIAL | `Specification.md` line 31; `docs/CONTRACT.md` lines 58-60; `Datasheet.md` lines 48-60. | The expected enforcement-owner taxonomy exists, but SDK-default-only exclusion is not proven row by row. |
| RBR-004 | PASS | `Specification.md` line 32; `docs/CONTRACT.md` lines 51-57; `frontend/docs/harness/runtime_engine_contract.md` lines 5-16; `frontend/scripts/validate-harness-section9.mjs` lines 25-29. | Runtime engine contract and conformance validation ID are present. |
| RBR-005 | PARTIAL | `Specification.md` line 33; `docs/CONTRACT.md` lines 55 and 69-75; `frontend/scripts/validate-harness-section9.mjs` lines 30-37. | Current validation IDs are `adapter_*`, while spec text still names `sdk_*`; register evidence is absent. |
| RBR-006 | PARTIAL | `Specification.md` line 34; `docs/CONTRACT.md` lines 69-73; `frontend/scripts/validate-harness-section9.mjs` lines 30-41. | Event-log and replay IDs exist under current names, but the register row is not generated. |
| RBR-007 | PARTIAL | `Specification.md` line 35; `docs/CONTRACT.md` lines 62-63; `docs/SPEC.md` lines 898-918. | SPEC still lists `section9.sdk_session_link_resume`; the current Section 9 script does not. Residual risk remains unregistered. |
| RBR-008 | PASS | `Specification.md` line 36; `docs/CONTRACT.md` line 60; `frontend/scripts/validate-harness-section9.mjs` lines 42-45. | Settings-source isolation has a current Section 9 validation ID. |
| RBR-009 | PARTIAL | `Specification.md` line 37; `docs/CONTRACT.md` lines 81-86; `frontend/src/lib/harness/permission-overlay.ts`. | Permission policy surfaces exist, but no register row ties residual risk and decision status. |
| RBR-010 | PASS | `Specification.md` line 38; `frontend/scripts/validate-harness-section9.mjs` lines 46-49. | Deny-precedence validation ID is present. |
| RBR-011 | PASS | `Specification.md` line 39; `docs/CONTRACT.md` lines 81-89; `frontend/docs/harness/adding_a_tool.md` line 66. | The restriction-boundary warning is documented outside the missing register. |
| RBR-012 | PASS | `Specification.md` line 40; `frontend/scripts/validate-harness-section9.mjs` lines 61-74. | Path containment and instruction-root protection validation IDs are present. |
| RBR-013 | PASS | `Specification.md` line 41; `docs/CONTRACT.md` lines 89-93; `frontend/scripts/validate-harness-section9.mjs` lines 61-74. | Hook failure/denial surfaces have Section 9 coverage hooks. |
| RBR-014 | PARTIAL | `Specification.md` line 42; `docs/CONTRACT.md` line 93; `frontend/scripts/validate-harness-section9.mjs` lines 75-83. | Tool-result budget coverage exists; bash default-deny row evidence is not generated. |
| RBR-015 | PASS | `Specification.md` line 43; `docs/CONTRACT.md` line 89; `frontend/scripts/validate-harness-section9.mjs` lines 50-60. | In-process MCP/status/dependency validation IDs are present. |
| RBR-016 | PASS | `Specification.md` line 44; `docs/CONTRACT.md` lines 113-118; `frontend/scripts/validate-harness-section9.mjs` lines 91-97. | Subagent governance validation ID is present. |
| RBR-017 | PASS | `Specification.md` line 45; `_STATUS.md` lines 3-7; `docs/CONTRACT.md` lines 99-101. | Lifecycle canon and approval-SHA semantics are documented. |
| RBR-018 | PASS | `Specification.md` line 46; `docs/CONTRACT.md` lines 32-36 and 135-138; `Procedure.md` lines 130-144. | Professional-boundary and no-automated-approval language is explicit. |
| RBR-019 | PARTIAL | `Specification.md` line 47; `docs/CONTRACT.md` lines 74-75 and 124-125; `Datasheet.md` lines 48-60. | Redaction is a named boundary, but final row-level evidence and validation mapping are absent. |
| RBR-020 | PARTIAL | `Specification.md` line 48; `docs/CONTRACT.md` line 56; `Guidance.md` lines 70-81. | Fallback criteria are discussed, but not captured in a final register row. |
| RBR-021 | PASS | `Specification.md` line 49; `_REFERENCES.md` line 12; `_DEPENDENCIES.md` lines 24-32. | REF-006 warning is recorded and not hidden. |
| RBR-022 | PARTIAL | `Specification.md` line 50; `_REFERENCES.md` line 12; `frontend/docs/harness/TRACEABILITY.md` line 23. | Traceability exists for current Section 9 IDs, but PRD-warning row traces are not available in a generated register. |
| RBR-023 | PARTIAL | `Specification.md` line 51; `docs/CONTRACT.md` lines 8 and 58-59; `Procedure.md` lines 137-147. | The review method exists; final register review cannot be performed because the artifact is missing. |
| RBR-024 | PASS | `Specification.md` line 52; `Guidance.md` lines 125-133; `Datasheet.md` lines 98-102. | TBDs are preserved rather than invented. |
| RBR-025 | FAIL | `Specification.md` line 53; shell check found no `docs/harness/reliance_boundary_register.md`. | The required post-generation cross-check cannot run until the register exists. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| G6: central reliance-boundary register is missing. | High | `Specification.md` lines 83-89 expect `docs/harness/reliance_boundary_register.md`; shell inspection found no `docs/harness/` directory. | Build the register as a follow-on tranche and keep it source-warning aware. |
| Section 9 ID vocabulary is partly stale. | Medium | `Specification.md` lines 33-35 cite `section9.sdk_message_mapper` and `section9.sdk_turn_engine_event_log`; current script uses `section9.adapter_message_mapper` and `section9.adapter_turn_engine_event_log` at lines 30-37. | Reconcile spec/datasheet names with the current validation ID set before final acceptance. |
| Desired SPEC IDs are not all implemented in the current Section 9 script. | Medium | `docs/SPEC.md` lines 906 and 908 list `section9.reliance_boundary_register` and `section9.sdk_session_link_resume`; `frontend/scripts/validate-harness-section9.mjs` lines 25-98 do not include them. | Decide whether these remain future IDs, get renamed, or require new checks. |
| All 24 local dependency rows remain unsatisfied. | Medium | `_DEPENDENCIES.md` lines 48-88 and `Dependencies.csv`. | Close or explicitly defer rows only in a separate dependency/evidence tranche. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. The register must preserve this warning in row-level source traces until reconciled.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. DEL-01-02 has 24 active local dependency rows, all still `TBD`/unsatisfied in the dependency summary. The accepted project-level DepClosure snapshot remains acyclic for dependency-closure discovery only.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Create `docs/harness/reliance_boundary_register.md` and its enforcement/test index from the local taxonomy. | doc/governance | M | FIT | REF-006 warning retained or reconciled; no issuance claim. |
| Reconcile Section 9 ID names and decide the fate of `section9.reliance_boundary_register` and `section9.sdk_session_link_resume`. | doc/test | S | FIT | Current validation script treated as implementation truth. |
| Backfill row-level residual-risk notes for transcript placement, SDK drift, fallback criteria, redaction, and domain future scope. | doc/governance | S | FIT | Register file exists. |

## Issuance-Gate-Process Observations

DEL-01-02 is the clearest PKG-01 blocker. The project has many runtime enforcement surfaces and validation IDs, but the deliverable's named output artifact is missing. A future issuance gate should require the register file, name reconciliation, and explicit row-level source-warning treatment before considering `ISSUED`.

## D-APP-56 R5 P43 annotation (2026-07-12)

The `PARTIAL` conclusions for RBR-002, RBR-003, RBR-005, RBR-006, RBR-009,
RBR-019, RBR-020, and RBR-023 are preserved historical evidence. ADQ-02
subsequently generated `docs/harness/reliance_boundary_register.md` with the
row-level no-prompt-only/no-SDK-default proof, enforcement owners, active
adapter validation names, audit, permission, redaction, fallback, and
cross-check records those conclusions said were absent. The eight conclusions
are therefore superseded for current-state reading. This note does not erase
the original matrix or make an issuance or lifecycle decision.
