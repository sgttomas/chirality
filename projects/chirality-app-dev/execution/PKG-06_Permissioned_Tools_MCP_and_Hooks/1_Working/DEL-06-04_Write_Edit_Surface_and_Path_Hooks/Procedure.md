# Procedure: DEL-06-04 Write/Edit Surface and Path Hooks

## Purpose

This procedure describes how to produce and verify the DEL-06-04 write/edit surface and path hook implementation evidence. It is written for the deliverable artifact, not as an end-user operation runbook.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted DEL-06-04 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
| Binding root, permission, hook, path, and MCP invariants | Available in `docs/CONTRACT.md` Sections 1.3 and 1.6 |
| Tool surface and hook specification | Available in `docs/SPEC.md` Sections 14 and 15 |
| Hook and tool vocabulary | Available in `docs/TYPES.md` Section 8 |
| Roadmap sequencing for controlled writes | Available in `docs/PLAN.md` R3; `docs/PRD.md` is warning-qualified due to HASH_MISMATCH |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` lists no accepted upstream edges yet |
| Exact implementation file paths | TBD |
| Exact test fixture paths | TBD |

## Steps

1. Establish the mutation surfaces.
   - Identify SDK built-in `Write` and `Edit` surfaces, plus any Chirality MCP write tools currently exposed.
   - Confirm write/edit surfaces are not exposed in `readOnly` and are only available in governed write modes.
   - Keep unknown or future write-capable tools out of scope until registered and governed.

2. Define or locate the active root resolver.
   - Resolve the active project or working root and the instruction root from product-owned runtime state.
   - Treat the decomposition phrase "project root" and the governance phrase "working root" as the same containment boundary until implementation chooses canonical naming.
   - Record any naming or resolver ambiguity as `TBD` or a review item.

3. Implement the pre-execution path gate.
   - Reject missing, malformed, or unresolvable target paths where the write/edit operation requires a target.
   - Deny targets outside the active project or working root.
   - Deny ordinary project writes under the instruction root.
   - Reject symlink targets and symlink path segments under the initial policy.
   - Fail closed if path classification cannot be completed.

4. Implement exact edit precondition checks.
   - Require edit-style operations to specify the exact content or equivalent exact precondition needed for safe replacement.
   - Deny or fail without mutation when the current file content does not match the precondition.
   - Keep the exact matching algorithm and diff strategy as `TBD` until implementation design selects them.

5. Connect permission and hook decisions.
   - Feed DEL-06-01 permission overlay results into the write/edit gate.
   - Apply deny-overrides-allow when SDK options, mode, operator intent, or `allowedTools` conflict with Chirality policy or hook denial.
   - Do not rely on `allowedTools` alone as a restriction boundary.

6. Execute controlled mutation only after gates pass.
   - Perform the write/edit atomically where practical.
   - Preserve existing file content when any pre-execution gate fails.
   - Ensure Chirality MCP write tools and SDK built-ins follow equivalent policy.

7. Record provenance and runtime evidence.
   - Record permission/runtime evidence for allowed and denied attempts.
   - For successful writes/edits, capture safe provenance, diff or summary, and hook outcome metadata.
   - Apply redaction and result-budget policy where outputs could be large or sensitive.

8. Add tests and fixtures.
   - Add fixtures for allowed in-root regular-file writes and edits.
   - Add denial fixtures for outside-root targets, instruction-root targets, symlink targets, hook failure, mode denial, and stale edit preconditions.
   - Add parity coverage for SDK built-ins and Chirality MCP write tools where both are in scope.
   - Record exact test paths as `TBD` until assigned.

9. Record residual gaps.
   - Track unresolved root naming, exact edit algorithm, implementation file paths, fixture paths, and PRD HASH_MISMATCH state.
   - Surface any remaining source conflicts in the deliverable review notes.

## Verification

| Check | Expected result |
|---|---|
| Pre-execution hook | Write/edit mutation does not occur until the hook or equivalent gate passes. |
| Path containment | Outside-root targets are denied without mutation. |
| Instruction-root protection | Instruction-root targets are denied during ordinary project execution. |
| Symlink rejection | Symlink target or path-segment attempts are denied in the initial policy. |
| Exact edit precondition | Stale, missing, or ambiguous edit preconditions fail without mutation. |
| Deny precedence | Hook, path, policy, SDK deny, governance, or human-gate denial overrides any allow. |
| Mode behavior | `readOnly` cannot write; `workspaceWrite` writes only after permission and hooks pass. |
| MCP parity | Chirality MCP write tools pass through equivalent gates as SDK built-ins. |
| Provenance | Successful writes produce safe diff/summary/provenance evidence; denied attempts produce audit evidence. |
| PRD warning | PRD-derived controlled-write details remain traceable to `_REFERENCES.md` HASH_MISMATCH until reconciled. |

## Records

- Write/edit hook implementation path: TBD.
- Root resolver and instruction-root resolver integration: TBD.
- Path policy fixtures: TBD.
- Exact edit validator and matcher tests: TBD.
- Provenance/diff/summary evidence format: TBD.
- Runtime event evidence for allowed and denied write attempts: TBD.
- Review note for PRD HASH_MISMATCH: required until REF-006 source state is reconciled.
