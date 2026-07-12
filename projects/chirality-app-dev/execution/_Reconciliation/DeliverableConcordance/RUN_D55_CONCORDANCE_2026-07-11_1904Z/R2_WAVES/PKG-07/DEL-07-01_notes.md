# DEL-07-01 concordance notes (R2 Wave-3, RUN_D55_CONCORDANCE_2026-07-11_1904Z)

Deliverable: DEL-07-01 Working Root Validation and Instruction Root Protection (PKG-07).
Source state: `frontend/` at `fac46e33f` (byte-identical through HEAD `74150b3a8`).
Assessment of record: `Assessment_INSP-03_DEL-07-01.md`, 2026-06-21, reviewed SHA `210b5b7427`.

## Census

By ClaimType: REQUIREMENT 11, EXCLUSION 3, ACCEPTANCE 1, REGISTER_DEFECT 2, REMAINING_WORK 1 (total 18).

By Disposition: ALIGNED 14, PARTIALLY_IMPLEMENTED 1, STALE_SPECIFICATION 1, REMAINING_STATE_MISMATCH 2.

Requirement set was RE-DERIVED from `Specification.md` (REQ-07-01-001..011); the R1 `REQUIREMENT_INDEX.csv` scanned only the literal `REQ-07` prefix (parser gap, as the brief anticipated). Spec was NOT rewritten after INSP-03, so REQ IDs map 1:1 to the assessment matrix (no MR-9 old-ID remap needed).

## Dominant finding: post-implementation + post-D-APP-38 kit lag

The four-document kit is a Phase 2.2 pre-implementation draft (code locations "TBD"). Since then two things landed that the kit has not caught up to:

1. **ORN-05 working-root validation parity** (commit `40afda52c`, 2026-07-10) made the `/api/working-root/validate` route delegate to the shared `assertProjectRootAccessible` full validator (session-manager.ts lines 23-66), and added `validate-route.test.ts`. This directly OVERTAKES the INSP-03 PARTIAL ratings on REQ-002, REQ-003, REQ-010, and REQ-011 and closes the assessment's Gap 1 (validate-route parity). At `fac46e33f` the validate route, `createSession`, and session boot all share one full validator.
2. **D-APP-35/D-APP-38 corpus reconciliation (v6)** resolved the REF-006 docs/PRD.md hash: `_REFERENCES.md` REF-006 now shows MATCH and the live `shasum -a 256 docs/PRD.md` reproduces the recorded value `ac35fba4...`. The pervasive "HASH_MISMATCH / warning-limited" wording in Datasheet, Specification, Guidance, Procedure, Assessment, and the dependency registers is now stale (ACC-001 STALE_SPECIFICATION; REGISTER-1 REMAINING_STATE_MISMATCH). Same pattern as R0 exemplar DEL-02-01-ACC-001.

REQ-001, REQ-004, REQ-005, REQ-006, REQ-007, REQ-009 were INSP-03 PASS and remain ALIGNED / STILL CURRENT at `fac46e33f` with live implementation + behavioral test evidence.

## Register-defect summary (MR-5)

- **REGISTER-1** (REMAINING_STATE_MISMATCH): `Dependencies.csv` DEP-07-01-004 and `_DEPENDENCIES.md` assert REF-006 HASH_MISMATCH, contradicting the deliverable's own `_REFERENCES.md` (MATCH) and the live hash. Internal inconsistency / metadata lag.
- **REGISTER-2** (REMAINING_STATE_MISMATCH): `Dependencies.csv` DEP-07-01-005 / `_DEPENDENCIES.md` declare implementation code module locations UNKNOWN/TBD (PREREQUISITE), stale now that the modules exist at `fac46e33f`.

Not flagged: the `_DEPENDENCIES.md` "Declared Upstream/Downstream: TBD" sections are human-owned declaration sections (W3 rule; docs/SPEC.md §5.2) and are NOT register defects. The DepClosure D53A coverage row `DEL-07-01,Y,5,Y,Y` matches the 5 live rows; the register count is consistent.

## Least-confident rows (self-flagged for fan-in recheck) + flip conditions

- **REQ-008 (PARTIALLY_IMPLEMENTED).** Write/shell fail-closed (chirality-hooks), subagent fail-closed on instruction-root error (subagent-governance test lines 364-388), and domain/lifecycle symlink writes denied (mutating-mcp test) are all present, but no named test asserts a *domain hook-evaluation error* itself failing closed for path/instruction-root enforcement. **Alternative reading that flips to ALIGNED:** if domain actions are judged not to "participate in path or instruction-root enforcement" in the K-HOOK-1 sense (they route through the same mutating-MCP write gate already proven for symlink/instruction-root), the requirement's enumerated surfaces are all covered and the row is ALIGNED with NONE_OBSERVED.
- **REQ-010 (ALIGNED).** Every enumerated case now has coverage, but the INSP-03 residual (unreadable/unwritable roots at the validate route directly) persists. **Alternative reading that flips to PARTIALLY_IMPLEMENTED:** if REQ-010's "invalid working roots" is read to require the unreadable/unwritable branch tested at the route surface (not only via session tests), the row is PARTIALLY_IMPLEMENTED.
- **REQ-011 (ALIGNED).** The single-shared-validator half of the ASSUMPTION is realized and tested; the downstream-reuse half (tree/scan/scaffold/contract consuming the same normalized root object) is asserted structurally, not by a dedicated test. **Alternative reading that flips to PARTIALLY_IMPLEMENTED:** if the ASSUMPTION's downstream-reuse clause is treated as a distinct testable obligation, coverage is incomplete.
- **REQ-002 (ALIGNED).** Depends on reading the shared `assertProjectRootAccessible` access check (R_OK|W_OK) plus session-route tests as sufficient. **Alternative:** PARTIALLY_IMPLEMENTED if a direct validate-route unreadable/unwritable test is deemed required.

## Method notes / deviations

- No IMPLEMENTED_UNMAPPED rows: all material live behavior on this deliverable's surface (`assertProjectRootAccessible`, `tool-path-policy`, `instruction-root` resolver, validate route) maps to REQ-001..011. `assertInstructionRootReadable` (instruction-root.ts) leans toward DEL-08-01 packaging conformance (EXC-003) rather than unmapped DEL-07-01 behavior.
- Guidance.md open human-ruling items are noted, not converted to defects: C-001 (REF-006 disposition) is resolved by the D-APP-38 MATCH state (ACC-001); X-002 (whether DEL-06-04 becomes an accepted dependency edge) is a dependency-declaration question left to R3/human ruling, not a scope conflict (EXC-002 stays ALIGNED); E-001 (future symlink relaxation) is a hypothetical.
- Verification bound per MR-3 to `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed/4 skipped) plus named test file/case. Tests were not executed. Non-behavioral bases use the MR-10 vocabulary (`SNAPSHOT+LIVE-REVERIFY`, `RUN-INSPECTION@fac46e33f`).
- No AUTHORITY_CONFLICT, no DEFERRED_AGENT_WORKFLOW, no UNKNOWN rows for this deliverable.
