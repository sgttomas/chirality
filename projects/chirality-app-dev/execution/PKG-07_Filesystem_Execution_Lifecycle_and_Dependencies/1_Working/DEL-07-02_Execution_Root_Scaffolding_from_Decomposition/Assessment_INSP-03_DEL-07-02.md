# Assessment INSP-03: DEL-07-02 Execution Root Scaffolding from Decomposition

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-07-02 |
| Package | PKG-07 Filesystem Execution, Lifecycle, and Dependencies |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `210b5b7427471fc307ecbf6eecaab78ebf08398b` |
| Spec source | `Specification.md` lines 1-105 |

## ADQ-06 Superseding Note - 2026-06-21

ADQ-06 implements the G1 scaffold baseline seeding gap recorded below. Current evidence is
`Evidence_ADQ-06_Scaffold_Baseline_Seeding.md`: `scaffoldExecutionRoot` now seeds `_STATUS.md`,
`_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md` for scaffolded deliverables;
the generated `_STATUS.md` parses as `OPEN`; preview planning includes metadata files; and reruns
preserve existing files while reseeding missing metadata. This note does not change lifecycle state,
satisfy dependency rows, or make issuance/release/professional claims.

## Scope

DEL-07-02 covers backend scaffolding from accepted decomposition markdown into a SPEC-shaped execution root, including package and deliverable folders, coordination seed files, idempotence, diagnostics, and preparation-readiness reporting.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-07-02-REQ-001 | PASS | `frontend/src/lib/harness/scaffold.ts` lines 10-35 and 706-828; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 64-101. | Execution root, tool roots, package folders, and layout validation are implemented and tested. |
| DEL-07-02-REQ-002 | PASS | `frontend/src/lib/harness/scaffold.ts` lines 376-415; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 64-101. | Package folders are generated as flat package directories. |
| DEL-07-02-REQ-003 | PASS | `frontend/src/lib/harness/scaffold.ts` lines 376-403 and 706-828; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 64-101. | Deliverable folders are created under package `1_Working` folders. |
| DEL-07-02-REQ-004 | FAIL | `frontend/src/lib/harness/scaffold.ts` lines 37-43, 445-461, and 623-703; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 64-101 and 167-196. | The code knows the required baseline file names and checks invalid existing targets, but it does not seed missing baseline metadata files for new deliverables. This confirms G1. |
| DEL-07-02-REQ-005 | FAIL | `frontend/src/lib/harness/scaffold.ts` lines 445-461 and 706-828; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 64-101. | New deliverable status files are not written with canonical `OPEN` content. |
| DEL-07-02-REQ-006 | PASS | `frontend/src/lib/harness/scaffold.ts` lines 10-35 and 706-828; `frontend/src/__tests__/api/harness/scaffold-route.test.ts` lines 33-84. | `_Coordination/_COORDINATION.md` is created or validated under the execution root. |
| DEL-07-02-REQ-007 | PASS | `frontend/src/lib/harness/scaffold.ts` lines 445-461; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 103-140. | Existing file contents are preserved on rerun. |
| DEL-07-02-REQ-008 | PASS | `frontend/src/lib/harness/scaffold.ts` lines 177-209; `frontend/src/__tests__/api/harness/scaffold-route.test.ts` lines 108-141; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 198-221. | Fail-fast diagnostics include stage/path context and created-path inventory. |
| DEL-07-02-REQ-009 | PASS | `frontend/src/__tests__/api/harness/scaffold-route.test.ts` lines 33-84 and 86-106. | `POST /api/harness/scaffold` is exposed and request validation is tested. |
| DEL-07-02-REQ-010 | PARTIAL | `frontend/src/lib/harness/scaffold.ts` lines 623-703 and 706-828; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 64-101 and 167-196. | Preparation compatibility is reported, but missing metadata files are not treated as blockers. |
| DEL-07-02-REQ-011 | PARTIAL | `frontend/src/lib/harness/scaffold.ts` lines 211-221; `frontend/src/lib/harness/mcp/read-tools.ts` lines 390-431; `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` lines 231-257. | Absolute/scaffold-preview path checks exist; full instruction-root mutation proof for live scaffold writes was not found in this wave. |
| DEL-07-02-REQ-012 | PARTIAL | `frontend/src/lib/harness/scaffold.ts` lines 262-342; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 142-165. | Malformed/no-deliverable decomposition is rejected. Missing-value `TBD` preservation fixtures were not evident. |
| DEL-07-02-REQ-013 | PARTIAL | `frontend/src/lib/harness/scaffold.ts` lines 262-342; `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 142-165. | The accepted table shape is parsed and empty/malformed cases fail; broader unsupported table-shape diagnostics remain thin. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| G1: scaffold does not seed the minimum deliverable metadata baseline. | High | `frontend/src/lib/harness/scaffold.ts` lines 37-43 and 623-703. | Implement idempotent creation of required deliverable metadata files, including canonical `OPEN` status content, with no overwrite of existing files. |
| Preparation compatibility reports invalid existing paths but not missing baseline files. | High | `frontend/src/lib/harness/scaffold.ts` lines 623-703. | Add missing-file issues and make readiness false until required baseline files exist or are intentionally deferred. |
| Parser boundary diagnostics are present but narrow. | Medium | `frontend/src/__tests__/lib/harness-scaffold.test.ts` lines 142-165. | Add fixtures for missing values and unsupported table shapes with typed compatibility issues. |
| REF-006 remains warning-limited. | Low | `_REFERENCES.md` REF-006 hash mismatch. | Close or waive PRD hash before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. G1 remains open as a roadmap/code gap and should not be marked satisfied by the existence of layout-only scaffolding.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add idempotent baseline metadata file creation for newly scaffolded deliverables. | code/test | M | FIT | Decide exact template text and owner/date fields. |
| Extend preparation compatibility to fail on missing required baseline files. | code/test | S | FIT | Baseline file creation semantics. |
| Add unsupported-table and missing-value parser fixtures with typed diagnostics. | test | S | FIT | Current parser boundary preserved. |

## Issuance-Gate-Process Observations

DEL-07-02 should not be issued as complete. The primary scaffold layout is usable, but the preparation-file seeding requirement is materially unmet.
