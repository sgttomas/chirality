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
| Declared upstream dependencies | Available as extracted dependency records in `_DEPENDENCIES.md` and `Dependencies.csv`; human-declared upstream lists remain TBD pending closure ruling |
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
   - Use the product-owned `HarnessEvent` JSONL surface for persisted permission evidence when the owning PKG-05/PKG-03 writer contract is available; exact call path remains TBD and is a tracked blocker rather than an accepted implementation fact.

6. Integrate MCP and SDK tool evaluation points.
   - Ensure SDK built-ins and in-process `mcp__chirality__*` tools are evaluated by equivalent overlay policy.
   - Keep detailed MCP wrapper implementation in DEL-06-03 unless this deliverable owns a shared permission hook point.

7. Add tests.
   - Verify `readOnly` denies write/edit/bash/network-capable and unexpected tools.
   - Verify `dontAsk` denies unknown or unapproved tools without prompting.
   - Verify `ask` persists the UI/human decision before returning SDK allow or deny.
   - Verify deny-overrides-allow when `allowedTools` or SDK posture conflicts with Chirality deny policy.
   - Verify `tool.permission` event records include decision source and reason.
   - Verify in-process Chirality MCP tool attempts pass through the same overlay decision path as SDK built-ins, with detailed wrapper fixtures owned by DEL-06-03 unless this deliverable defines a shared hook point.

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
- WorkspaceWrite hook-pass gating evidence: TBD, dependent on DEL-06-04 hook result interface.
- MCP parity evidence: TBD, dependent on DEL-06-03 wrapper points or a shared overlay hook point.
- Dependency closure ruling: TBD for human-declared upstream status; extracted rows are present in `_DEPENDENCIES.md` and `Dependencies.csv`.
- Review note for PRD HASH_MISMATCH: required until REF-006 source state is reconciled.

## Pass 3 Semantic Lensing Disposition

| ItemID | Disposition | Evidence and source reread |
|---|---|---|
| D-001 | Converted to explicit Records blockers rather than invented paths. | Records now name required implementation, fixture, hook-gating, MCP parity, and decision-schema evidence as TBD. Reread: `_CONTEXT.md` anticipated artifacts; `docs/SPEC.md` Sections 14 and 15; decomposition PKG-06 rows. |
| D-002 | Incorporated as a dependency closure distinction. | Prerequisites now distinguish extracted dependency records from still-TBD human-declared upstream closure. Reread: `_DEPENDENCIES.md` Dependency Tracking and Extracted Dependency Register; `Dependencies.csv` v3.1. |
| E-001 | Converted from ASSUMPTION to tracked blocker. | Step 5 no longer states the event writer/session JSONL API as accepted fact; it depends on the owning writer contract and keeps exact call path TBD. Reread: `docs/SPEC.md` Section 9.2 and Section 9.4; `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `_DEPENDENCIES.md` DEP-06-01-E009 warning. |
| E-002 | Incorporated as explicit MCP parity procedure and record evidence. | Step 7 and Records require MCP parity evidence while leaving wrapper points to DEL-06-03 or a shared overlay hook point. Reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2; decomposition PKG-06 rows for DEL-06-03. |
