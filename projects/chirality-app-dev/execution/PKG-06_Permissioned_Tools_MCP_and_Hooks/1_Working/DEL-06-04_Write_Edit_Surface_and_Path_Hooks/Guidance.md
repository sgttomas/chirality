# Guidance: DEL-06-04 Write/Edit Surface and Path Hooks

## Purpose

DEL-06-04 exists to make controlled workspace writes possible without weakening Chirality's filesystem, permission, and provenance boundaries. It is the write/edit security-control slice for PKG-06: permission overlay decisions, read tool exposure, MCP wrapper shape, bash governance, and hook lifecycle mirroring are adjacent deliverables, but this deliverable defines the path and mutation gates that must pass before files change.

Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/CONTRACT.md` Sections 1.3 and 1.6; `docs/SPEC.md` Section 15; `docs/PLAN.md` R3.

## Principles

1. Runtime code is the boundary. Prompt text, persona wording, or tool descriptions must not be relied on to protect filesystem writes. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-2.
2. Deny-first remains controlling. A denial from policy, path containment, hook, governance, SDK deny rule, or human gate overrides any allow. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-1.
3. The active project or working root bounds ordinary writes. Target paths outside that root are denied before mutation. Source: `docs/CONTRACT.md` Section 1.6 K-PATH-2.
4. Instruction-root writes are release/change operations, not ordinary project execution. Ordinary project runs must not mutate the instruction root. Source: `docs/CONTRACT.md` Section 1.3 K-ROOT-2.
5. Symlink write rejection is the initial policy. Any relaxation would need a governed amendment and tests. Source: `docs/CONTRACT.md` Section 1.6 K-PATH-3.
6. Provenance is part of the write, not an afterthought. Allowed and denied attempts need enough event, diff, summary, and provenance evidence for audit. Sources: `docs/PLAN.md` R3; `docs/SPEC.md` Section 15.2.

## Considerations

### Root Terminology

The decomposition uses "project-root containment"; `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/PRD.md` primarily use "working root." Treat these as the active runtime containment root for this deliverable until implementation selects the exact public name. Do not create two independent roots without a source update.

### Hook Placement

`PreToolUse` should be the normal enforcement point for path containment, instruction-root protection, symlink rejection, exact edit preconditions, and mode/policy denial before mutation. `PostToolUse` should record successful write provenance, diff/summary, and safe metadata. Post-failure evidence should be captured where the runtime supports it, but failure mirroring details may belong to DEL-06-06.

### Exact Edit Preconditions

Exact edit preconditions should prevent stale or ambiguous edits from mutating files. The source corpus requires exact preconditions but does not specify the matching algorithm. Keep algorithmic details as `TBD` until implementation design chooses the file matcher, diff strategy, and stale-content behavior.

### PRD Hash Warning

`docs/PRD.md` is listed as HASH_MISMATCH in `_REFERENCES.md`. Use PRD Section 7.9 as warning-qualified product direction for controlled writes and exact edit preconditions. Implementation acceptance should retain this warning until REF-006 source state is reconciled.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Omit write tools vs expose and deny | Prefer not exposing write/edit tools until mode and permission policy allow them, but still enforce hook denial because exposure control alone is not a safety boundary. Sources: `docs/SPEC.md` Section 14.3; `docs/CONTRACT.md` K-PERM-3. |
| SDK built-ins vs Chirality MCP write tools | Treat both as mutation surfaces requiring equivalent permission, hook, path, redaction, and event logging policy. Source: `docs/CONTRACT.md` K-MCP-1. |
| Atomic write/edit vs implementation simplicity | Perform atomic mutation where practical, but do not use atomicity as a substitute for pre-execution path and precondition checks. Source: `docs/PRD.md` Section 7.9, HASH_MISMATCH warning. |
| Symlink denial vs advanced workspace layouts | Reject symlink writes initially. If future workspace needs require symlink support, add a governed policy amendment and targeted tests first. Source: `docs/CONTRACT.md` K-PATH-3. |
| Provenance detail vs data exposure | Record enough diff/summary/provenance to audit the write while applying the same redaction and result-budget posture as other tools. Source: `docs/SPEC.md` Section 15.2. |

## Examples

| Scenario | Expected behavior |
|---|---|
| `readOnly` session attempts `Write` or `Edit` | Deny before mutation; record permission/runtime evidence where governed. |
| `workspaceWrite` session edits an in-root regular file with exact precondition match and passing hooks | Allow mutation, preferably atomic where practical; record diff/summary and provenance. |
| Write target resolves outside the active project or working root | Deny in `PreToolUse` or equivalent gate; no mutation occurs. |
| Write target is under the instruction root | Deny as ordinary project execution; instruction-root mutation requires governed release/change operation. |
| Write target or path segment is a symlink | Deny under initial policy; no mutation occurs. |
| Edit precondition does not match current file content | Deny or fail the edit without mutation; record failure evidence. |
| SDK `allowedTools` includes `Edit` but Chirality hook denies path containment | Final result is deny; `allowedTools` does not bypass hooks. |
| Chirality MCP dependency writer is used | It must pass through equivalent permission, hook, path, redaction, and event logging policy as SDK built-ins. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| DEL-06-04-CONFLICT-001 | Root terminology differs between "project root" in decomposition wording and "working root" in governance docs. | `_CONTEXT.md` and decomposition row DEL-06-04 | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` Section 7.9 | Datasheet Conditions; Specification Scope and REQ-002; Procedure Steps | Treat both as the active runtime containment root and settle canonical naming during implementation. | TBD |
| DEL-06-04-CONFLICT-002 | PRD is content-accessible but warning-qualified due to HASH_MISMATCH. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Sections 7.9 and R3 | PRD-cited requirements and guidance | Use PRD as warning-qualified source until reference hash state is reconciled. | TBD |
