# Procedure: DEL-07-01 Working Root Validation and Instruction Root Protection

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

Define the operational steps to produce and verify the DEL-07-01 implementation artifacts: root validation tests, path policy helpers, and instruction-root protection fixtures.

This procedure may be used by the implementer or reviewer to check that working-root validity, root separation, path containment, and instruction-root write protection are represented in code and tests.

## Prerequisites

| Prerequisite | Status | Source |
|---|---|---|
| Accepted deliverable scope for DEL-07-01. | Available in `_CONTEXT.md` and decomposition. | `_CONTEXT.md`; decomposition `DEL-07-01` row |
| Current lifecycle state permits P3 enrichment. | `INITIALIZED`; Phase 2.5 is `P3_ONLY` and preserves `_STATUS.md` under `NO_STATUS_TOUCH`. | `_STATUS.md`; `_SEMANTIC_LENSING.md` |
| Authoritative source corpus is accessible. | Accessible; `docs/PRD.md` has MATCH status. | `_REFERENCES.md` — reconciled under D-APP-38 |
| Declared upstream dependencies. | TBD - no accepted dependency edges extracted yet. | `_DEPENDENCIES.md` |
| Code module locations for implementation. | TBD. | Source-grounding gap |

## Steps

1. Confirm source state.
   - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

2. Identify the active instruction root.
   - Resolve the instruction root from packaged resources or `CHIRALITY_INSTRUCTION_ROOT` during development.
   - Confirm required instruction-root assets are treated as release-managed resources.
   - Source: `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1.

3. Validate candidate working roots before use.
   - Reject non-absolute paths.
   - Reject missing paths.
   - Reject non-directory paths.
   - Reject paths without app read/write access.
   - Reject paths inside the active instruction root.
   - Source: `docs/PRD.md` Section 7.1; `docs/SPEC.md` Section 1.2.

4. Normalize and bind the accepted project root.
   - Store the accepted root as the active `projectRoot` for file tree, scope scan, chat session, scaffold, and contract APIs.
   - ASSUMPTION: downstream API reuse should consume the same normalized root object or equivalent canonical string.
   - Source: `docs/PRD.md` Section 7.1.

5. Implement path containment checks for tool and write paths.
   - Resolve project-relative and absolute paths.
   - Deny paths outside the active project root.
   - Deny traversal or normalization results that escape the root.
   - Source: `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050.

6. Enforce instruction-root write protection.
   - Deny ordinary writes under the active instruction root.
   - Apply the denial even when SDK or developer-local modes would otherwise permit execution.
   - Source: `docs/CONTRACT.md` K-ROOT-2; `docs/PRD.md` FR-051; `docs/TYPES.md` Section 8.2.

7. Apply required hook behavior.
   - Ensure PreToolUse or equivalent Chirality hooks enforce path containment, instruction-root protection, symlink write rejection, and provenance policy before governed writes.
   - Ensure hook failures fail closed.
   - Source: `docs/SPEC.md` Section 15.2; `docs/CONTRACT.md` K-HOOK-1.

8. Reject symlink writes in the initial policy.
   - Add fixtures for symlink write targets.
   - Deny unless a future governed amendment and tests explicitly authorize a narrower policy.
   - Source: `docs/CONTRACT.md` K-PATH-3.

9. Build the test matrix.
   - Include valid working root.
   - Include relative, missing, non-directory, unreadable, and unwritable working-root cases.
   - Include working root inside instruction root.
   - Include absolute outside-project write path.
   - Include traversal escape path.
   - Include instruction-root write attempt.
   - Include symlink write attempt.
   - Source: `docs/PRD.md` FR-003, FR-050, FR-051, FR-095, FR-097.

10. Record verification evidence.
    - Store test output or summaries where the project test convention requires.
    - Record final test command names and evidence locations when implementation identifies them; until then they remain TBD.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
    - Preserve source citations and any unresolved `TBD` items for later semantic/dependency passes.

## Verification

| Check | Pass Condition | Records |
|---|---|---|
| Root validation | Invalid roots are rejected with typed or inspectable errors; valid absolute readable/writable directory is accepted. | Root validation test output. |
| Root separation | Working roots inside instruction root are rejected. | Instruction-root containment fixture output. |
| Path containment | Writes/tool paths outside active project root are denied after normalization. | Path helper test output. |
| Instruction-root protection | Writes beneath instruction root are denied across ordinary execution modes. | Hook or policy fixture output. |
| Symlink write policy | Symlink writes are denied under the initial policy. | Symlink fixture output. |
| Fail-closed hooks | Hook failure denies governed action and records triage. | Hook failure test output. |
| PRD hash warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | Review note or run record. — reconciled under D-APP-38 |
| Fixture evidence completeness | Relative, missing, non-directory, unreadable, unwritable, instruction-root-contained, outside-root, traversal, instruction-root write, and symlink cases have output or summary records. | Test output, fixture list, or coverage checklist. |

## Records

Expected records and artifacts:

- Root validation tests.
- Path policy helper implementation and tests.
- Instruction-root protection fixtures.
- Symlink write rejection fixtures.
- Hook failure or policy denial evidence.
- Documentation of `docs/PRD.md` hash warning.

Records still TBD:

- Final implementation file paths.
- Final test command names.
- Final evidence record locations for root validation, path policy, instruction-root protection, hook failure, symlink fixtures, and PRD source-state review.
- Responsible party.

## Pass 3 Semantic Lensing Notes

| ItemID | Procedure Disposition | Evidence |
|---|---|---|
| B-001 | converted to TBD | Step 10 and Verification require concrete fixture output or summaries; final evidence is not invented before tests exist. |
| D-001 | converted to TBD | Verification requires API test output for `/api/working-root/validate` and downstream normalized-root reuse; implementation confirmation is still pending. |
| X-001 | converted to TBD | `Records still TBD` now names final test command names and evidence locations for all fixture families. |
| E-001 | already covered | Step 8 and Verification preserve initial symlink rejection and require future amendment/test evidence before relaxation. |
| E-002 | incorporated | Step 10, Verification, and Records require preservation of the PRD hash status: MATCH status in review evidence. — reconciled under D-APP-38 |
