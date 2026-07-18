# Assessment INSP-03: DEL-07-01 Working Root Validation and Instruction Root Protection

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-07-01 |
| Package | PKG-07 Filesystem Execution, Lifecycle, and Dependencies |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `210b5b7427471fc307ecbf6eecaab78ebf08398b` |
| Spec source | `Specification.md` lines 1-69 |

## Scope

DEL-07-01 covers working-root validation, project-root containment, instruction-root write protection, symlink-write rejection, and fail-closed hook or policy behavior for ordinary project execution.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ-07-01-001 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 163-182; `frontend/src/lib/harness/session-manager.ts` lines 20-65. | Relative/non-absolute roots are rejected before session use. |
| REQ-07-01-002 | PARTIAL | `frontend/src/lib/workspace/filesystem.ts` lines 184-207; `frontend/src/lib/harness/session-manager.ts` lines 20-65; `frontend/src/__tests__/api/harness/routes.test.ts` lines 191-249. | Missing and non-directory paths are covered broadly, and session creation checks read/write access. The `/api/working-root/validate` route itself only normalizes/stat-checks the root. |
| REQ-07-01-003 | PARTIAL | `frontend/src/lib/harness/session-manager.ts` lines 20-65; `frontend/src/__tests__/api/harness/routes.test.ts` lines 191-249. | Session creation rejects instruction-root overlap; direct working-root validate route coverage is thinner. |
| REQ-07-01-004 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 215-248; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 417-512; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-240. | Ordinary governed writes are blocked from the instruction root by path policy and hook coverage. |
| REQ-07-01-005 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 215-224 and 234-248; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-240 and 370-440. | Write/edit/Bash paths are resolved against the active project root and outside-root attempts are denied. |
| REQ-07-01-006 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 234-248; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 417-512; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-240 and 370-440. | Instruction-root hard-denial applies even in otherwise permissive modes. |
| REQ-07-01-007 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 95-160; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 417-512; `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` lines 284-309. | Symlink write targets are rejected before mutation. |
| REQ-07-01-008 | PARTIAL | `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-240 and 370-440; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 238-275. | Write and shell enforcement fail closed. Domain and subagent hook surfaces were not proven in this package wave. |
| REQ-07-01-009 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 95-160 and 215-248; `frontend/src/lib/harness/mcp/read-tools.ts` lines 238-388. | Root and path policy are implemented in runtime helpers and MCP write gating, not only prompt text. |
| REQ-07-01-010 | PARTIAL | `frontend/src/__tests__/api/harness/routes.test.ts` lines 191-249; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-240 and 370-440; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 417-512. | Required invalid-root, outside-path, instruction-root, and symlink cases have coverage, but the direct validate-route matrix is incomplete. |
| REQ-07-01-011 | PARTIAL | `frontend/src/app/api/working-root/validate/route.ts` lines 1-20; `frontend/src/app/api/working-root/tree/route.ts` lines 21-42; `frontend/src/lib/workspace/filesystem.ts` lines 399-560. | The validate route exists and downstream APIs normalize roots, but the exact validator reuse path is not a single shared full validator. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| `/api/working-root/validate` does not enforce the same full root policy as session creation. | Medium | `frontend/src/app/api/working-root/validate/route.ts` lines 1-20 vs `frontend/src/lib/harness/session-manager.ts` lines 20-65. | Extract or reuse one root-validation service that includes read/write and instruction-root checks, then add route tests. |
| Domain/subagent hook fail-closed evidence was not found in the PKG-07 inspection set. | Low | Write and Bash fixtures exist in `chirality-hooks.test.ts`; no matching domain/subagent fixture was cited. | Add targeted fixtures only where those action classes share path/instruction-root enforcement. |
| REF-006 remains warning-limited. | Low | `_REFERENCES.md` REF-006 hash mismatch. | Close or waive the PRD hash warning before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active dependency rows remain pending for lifecycle/source warning closure and cross-deliverable ownership where applicable.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Consolidate working-root validation so the validate route, session creation, tree, scaffold, and deliverable-contract APIs share one full policy path. | code/test | M | FIT | Current path-policy helper contracts. |
| Add focused validate-route tests for unreadable/unwritable roots and instruction-root-contained roots. | test | S | FIT | Shared validator extraction or explicit route policy. |
| Add missing fail-closed fixtures only for domain/subagent paths that actually participate in filesystem enforcement. | test | S | FIT | Confirm active domain/subagent write surface. |

## Issuance-Gate-Process Observations

DEL-07-01 has strong containment and hook evidence, but the issuance gate should treat the validate-route reuse assumption as unresolved until the full validator is shared or explicitly documented.

## D-APP-56 R5 P40 annotation (2026-07-12)

The source-state caveat above is preserved as historical assessment evidence. REF-006 now records `docs/PRD.md` expected and actual SHA-256 as `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` (`MATCH`) under D-APP-38; it is not a current warning or blocker. No assessment verdict or lifecycle state changes here.

---

**Correction note (2026-07-18 — identifier qualification):** The requirement
identifiers in this assessment use the reversed qualification form
`REQ-07-01-NNN`. The canonical qualified form under the Deliverable
Scope-of-Work Standard §4 is `DEL-07-01-REQ-NNN`. Each `REQ-07-01-NNN` above maps
to `DEL-07-01-REQ-NNN` with the same three-digit NNN. Recorded assessment rows
are unchanged; this appended note governs interpretation of the identifiers.
