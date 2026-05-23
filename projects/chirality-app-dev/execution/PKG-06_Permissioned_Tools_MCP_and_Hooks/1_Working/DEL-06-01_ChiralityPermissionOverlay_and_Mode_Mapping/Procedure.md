# Procedure: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

## Purpose

This procedure describes how to produce and verify the DEL-06-01 permission overlay implementation and mode mapping evidence. It is written for the deliverable artifact, not as an end-user operation runbook.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted DEL-06-01 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
| Authoritative permission vocabulary | Available in `docs/TYPES.md` Section 8 |
| Binding permission invariants | Available in `docs/CONTRACT.md` Section 1.6 |
| Tool surface and mode mapping specification | Available in `docs/SPEC.md` Sections 14 and 15 |
| Roadmap sequencing for R2/R3 | Available in `docs/PLAN.md`; `docs/PRD.md` is warning-qualified due to HASH_MISMATCH |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` lists no accepted upstream edges yet |
| Exact implementation file paths | TBD |
| Exact test fixture paths | TBD |

## Steps

1. Establish the source-controlled mode vocabulary.
   - Use `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, and developer-local `bypass` from `docs/TYPES.md` Section 8.1.
   - Do not introduce new modes without a governed source update.

2. Define or locate the structured permission decision record.
   - Align with `HarnessPermissionDecision` from `docs/TYPES.md` Section 8.2.
   - Include safe SDK metadata only when it does not leak secrets or SDK-shaped public contract fields.

3. Implement the deny-first overlay.
   - Evaluate explicit denies from Chirality policy, path containment, hooks, governance, SDK deny rules, and human gates.
   - If any explicit deny is present, return or persist `deny` even when an SDK or tool option would otherwise allow.

4. Implement the mode mapping.
   - Map `readOnly` to read-tool posture with write/edit/bash/network-capable and unexpected tools denied.
   - Map `dontAsk` to exact safe-tool pre-approval with all other actions denied without prompting.
   - Map `ask` to `canUseTool` or equivalent application mediation, with decision persistence before SDK callback return.
   - Map `workspaceWrite` only after write hooks can prove project-root containment, instruction-root protection, symlink policy, and provenance behavior.
   - Keep `bypass` developer-local and still subject to Chirality deny rules.

5. Integrate permission-event persistence.
   - Persist `tool.permission` evidence for governed attempts with source, reason, and safe SDK metadata when available.
   - ASSUMPTION: the event writer and session JSONL append API are provided by PKG-05/PKG-03 surfaces; exact call path is TBD.

6. Integrate MCP and SDK tool evaluation points.
   - Ensure SDK built-ins and in-process `mcp__chirality__*` tools are evaluated by equivalent overlay policy.
   - Keep detailed MCP wrapper implementation in DEL-06-03 unless this deliverable owns a shared permission hook point.

7. Add tests.
   - Verify `readOnly` denies write/edit/bash/network-capable and unexpected tools.
   - Verify `dontAsk` denies unknown or unapproved tools without prompting.
   - Verify `ask` persists the UI/human decision before returning SDK allow or deny.
   - Verify deny-overrides-allow when `allowedTools` or SDK posture conflicts with Chirality deny policy.
   - Verify `tool.permission` event records include decision source and reason.

8. Record residual gaps.
   - Keep exact file paths, fixture names, and implementation ownership as `TBD` until assigned.
   - Record the `docs/PRD.md` HASH_MISMATCH as a source-state warning in implementation notes or review evidence.

## Verification

| Check | Expected result |
|---|---|
| Decision schema | Permission decisions conform to `docs/TYPES.md` Section 8.2. |
| Deny precedence | Any explicit deny produces final `deny`. |
| `allowedTools` misconception | Tests show `allowedTools` does not restrict by itself and cannot bypass deny policy. |
| `readOnly` behavior | Write/edit/bash/network-capable and unexpected tools do not execute. |
| `dontAsk` behavior | Unapproved and unknown tools deny without prompting. |
| `ask` behavior | Approval mediation persists the decision before SDK callback return. |
| Event persistence | Governed attempts produce `tool.permission` evidence. |
| MCP parity | Chirality MCP tool attempts pass through the same permission overlay as SDK built-ins. |
| PRD warning | PRD-derived details remain traceable to `_REFERENCES.md` HASH_MISMATCH until reconciled. |

## Records

- Permission overlay module or equivalent implementation path: TBD.
- Mode mapping fixture or table: TBD.
- `HarnessPermissionDecision` schema/type evidence: TBD.
- Permission event tests: TBD.
- readOnly/dontAsk/ask behavior tests: TBD.
- Review note for PRD HASH_MISMATCH: required until REF-006 source state is reconciled.

