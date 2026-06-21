# Assessment INSP-03: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-07-05 |
| Package | PKG-07 Filesystem Execution, Lifecycle, and Dependencies |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `210b5b7427471fc307ecbf6eecaab78ebf08398b` |
| Spec source | `Specification.md` lines 1-98 |

## Scope

DEL-07-05 covers reading, validating, writing, and exposing deliverable-local `Dependencies.csv` v3.1 rows, including schema normalization, provenance, lifecycle status rules, extension columns, API/MCP behavior, and path-policy safeguards.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ-DEL-07-05-001 | PASS | `frontend/src/lib/dependencies/schema.ts` lines 1-31; `frontend/src/lib/dependencies/register-reader.ts` lines 86-122; `frontend/src/__tests__/lib/dependencies-register-contract.test.ts` lines 54-68. | v3.1 register rows are recognized and legacy missing schema values are warned/normalized. |
| REQ-DEL-07-05-002 | PASS | `frontend/src/lib/dependencies/register-writer.ts` lines 54-95; `frontend/src/__tests__/lib/dependencies-register-contract.test.ts` lines 54-78. | Written rows carry canonical v3.1 schema. |
| REQ-DEL-07-05-003 | PASS | `frontend/src/lib/dependencies/schema.ts` lines 38-76 and 149-187; `frontend/src/lib/dependencies/register-writer.ts` lines 97-305. | Core columns, enums, IDs, dates, provenance, origin, and lifecycle status fields are validated. |
| REQ-DEL-07-05-004 | PASS | `frontend/src/lib/dependencies/register-writer.ts` lines 367-413; `frontend/src/__tests__/lib/dependencies-register-contract.test.ts` lines 139-147. | Duplicate dependency IDs are rejected. |
| REQ-DEL-07-05-005 | PASS | `frontend/src/lib/dependencies/register-writer.ts` lines 97-305; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` lines 384-404. | Host deliverable mismatch is rejected. |
| REQ-DEL-07-05-006 | PASS | `frontend/src/lib/dependencies/register-writer.ts` lines 97-305; `frontend/src/__tests__/lib/dependencies-register-contract.test.ts` lines 80-94. | Invalid anchor row classification is rejected. |
| REQ-DEL-07-05-007 | PASS | `frontend/src/lib/dependencies/register-writer.ts` lines 97-305. | Execution rows are validated against anchor/type rules. |
| REQ-DEL-07-05-008 | PARTIAL | `frontend/src/lib/dependencies/register-writer.ts` lines 307-340 and 367-413. | Lifecycle transitions are validated, but row deletion/retire discipline is not enforced against a previous-register diff. |
| REQ-DEL-07-05-009 | PASS | `frontend/src/lib/dependencies/register-writer.ts` lines 97-305; `frontend/src/__tests__/lib/dependencies-register-contract.test.ts` lines 96-109. | Active extracted rows require provenance or explicit `location TBD`. |
| REQ-DEL-07-05-010 | PARTIAL | `frontend/src/lib/dependencies/register-writer.ts` lines 97-305; `frontend/src/__tests__/lib/dependencies-register-contract.test.ts` lines 111-137. | Target-type rules are validated, but existence of stable target deliverable IDs is not resolved against the live deliverable set. |
| REQ-DEL-07-05-011 | PASS | `frontend/src/lib/dependencies/register-reader.ts` lines 24-122; `frontend/src/lib/dependencies/register-writer.ts` lines 97-305. | Unknown/legacy values are surfaced as warnings or `TBD`-style conditions rather than guessed. |
| REQ-DEL-07-05-012 | PARTIAL | `frontend/src/lib/dependencies/register-writer.ts` lines 307-413; `frontend/src/__tests__/lib/dependencies-register-contract.test.ts` lines 149-187. | Host, schema, warning, and satisfaction-status transitions are preserved; deleted-row protection is still not proven. |
| REQ-DEL-07-05-013 | PASS | `frontend/src/app/api/working-root/deliverable/dependencies/route.ts` lines 76-107; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` lines 330-347 and 428-448. | GET/PUT dependency API is implemented and tested. |
| REQ-DEL-07-05-014 | PASS | `frontend/src/lib/harness/mcp/read-tools.ts` lines 447-457 and 553-586; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 236-282. | Dependency read/write MCP tools share event/evidence and redaction handling. |
| REQ-DEL-07-05-015 | PARTIAL | `frontend/src/lib/workspace/deliverable-contracts.ts` lines 416-471; `frontend/src/lib/harness/mcp/read-tools.ts` lines 238-388; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 284-309. | MCP write path rejects symlink targets, but the direct dependency API writes `Dependencies.csv` without a leaf-file symlink rejection check. |
| REQ-DEL-07-05-016 | PASS | `frontend/src/lib/dependencies/schema.ts` lines 33-36; `frontend/src/lib/dependencies/register-writer.ts` lines 342-365. | Extension columns are collected and preserved as non-breaking fields. |
| REQ-DEL-07-05-017 | PARTIAL | `frontend/src/lib/dependencies/register-reader.ts` lines 24-122; `frontend/src/lib/dependencies/register-writer.ts` lines 97-305. | Dependency-row unknowns produce warnings, but runtime/tool option warning behavior was not specifically evidenced for this deliverable. |
| REQ-DEL-07-05-018 | PASS | `Specification.md` lines 17-23 and 45-46; implementation evidence is confined to dependency register read/write/lint behavior. | No project-level graph generator, lock, staleness propagation, or unified pipeline run-record feature is introduced. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Direct dependency API write path lacks explicit leaf symlink rejection. | High | `frontend/src/lib/workspace/deliverable-contracts.ts` lines 416-471. | Reuse the write path policy or explicitly reject symlinked `Dependencies.csv` before `writeFile`. |
| Rows can be omitted from an update without a retire-vs-delete check. | Medium | `frontend/src/lib/dependencies/register-writer.ts` lines 307-413. | Compare previous and next rows when previousRows are supplied, and require deletion to be represented as a retired row or explicit governed repair. |
| Target deliverable existence is not resolved against the live deliverable inventory. | Medium | `frontend/src/__tests__/lib/dependencies-register-contract.test.ts` lines 111-137. | Add an optional resolver-backed validation mode for stable target IDs. |
| Runtime option warning behavior is outside the dependency tests. | Low | Requirement REQ-DEL-07-05-017; no specific runtime option fixture cited. | Either bind this requirement to an existing tool-options owner or add a narrow warning fixture. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. The dependency register machinery is mature, but this inspection did not change project dependency truth.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add direct API symlink-leaf protection for `Dependencies.csv` writes. | code/test | S | FIT | Current tool-path policy helper or local lstat check. |
| Add previous-register diff validation for deleted rows vs retired rows. | code/test | M | FIT | Decide whether governed repair can bypass deletion checks. |
| Add optional live deliverable-ID resolver for target existence checks. | code/test | M | FIT | Stable project deliverable enumeration source. |

## Issuance-Gate-Process Observations

DEL-07-05 is substantially implemented but should not be treated as fully closed while direct API write hardening and deleted-row discipline remain partial.
