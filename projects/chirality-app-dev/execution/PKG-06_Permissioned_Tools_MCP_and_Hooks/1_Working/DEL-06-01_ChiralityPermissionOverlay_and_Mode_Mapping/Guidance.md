# Guidance: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

DEL-06-01 exists to make runtime tool permission decisions explicit, persisted, and governed by Chirality-owned policy rather than SDK defaults or prompt text. It is the permission-policy slice of PKG-06: hooks, write path policy, bash governance, and MCP implementation details are adjacent deliverables, but this deliverable defines the overlay semantics they must feed.

Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Sections 14 and 15.

## Principles

1. Capability-forward policy with explicit hard-deny precedence is the controlling rule. If any authoritative policy, hook, governance, SDK deny rule, path boundary, or human gate says deny, the final decision is deny. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-1.
2. Prompt text is never enough. Permission-sensitive behavior must be enforced by runtime code, policy, hooks, callback mediation, or human gates. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-2.
3. `allowedTools` is convenience, not containment. Treat it as possible auto-approval only; use disallowed tools, mode posture, hooks, `canUseTool`, and `dontAsk` to restrict execution. Sources: `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3.
4. Product-owned records are the durable truth. `HarnessPermissionDecision` and `tool.permission` events should remain Chirality-shaped even when SDK metadata is attached. Sources: `docs/TYPES.md` Section 8.2; `docs/PRD.md` Section 9.4, MATCH status. (reconciled under D-APP-38).
5. MCP is not a bypass. Chirality MCP tools and SDK built-ins must pass through equivalent permission and hook policy. Source: `docs/CONTRACT.md` Section 1.6 K-MCP-1.

## Considerations

### Mode Mapping

| Mode | Practical guidance | Source |
|---|---|---|
| `readOnly` | Prefer pre-approved read tools only; deny write/edit/bash/network-capable and unexpected tools. | `docs/SPEC.md` Section 15.1; `docs/TYPES.md` Section 8.1 |
| `workspaceWrite` | Allow governed writes only after write hooks pass and project-root/instruction-root/symlink policy is satisfied. Hook internals are not owned by this deliverable. | `docs/SPEC.md` Section 15.1 |
| `dontAsk` | Use for non-interactive denial posture. Unknown and unapproved actions should deny without prompting. | `docs/CONTRACT.md` Section 1.6 K-PERM-5 |
| `ask` | Use when the application can present an approval request and persist the answer before the SDK callback returns allow or deny. | `docs/SPEC.md` Section 15.1 |
| `bypass` | Keep developer-local only; never treat it as shipped operator behavior; Chirality denies still apply. | `docs/CONTRACT.md` Section 1.6 K-PERM-6 |

### Decision Provenance

Use the `source` field deliberately. A decision from `chirality-policy` should not be mislabeled as `human`, and SDK callback mediation should be captured distinctly from hook denials. Human approvals remain non-delegable in the broader governance model; automated permission decisions should not be described as approvals for reliance.

### PRD Hash Status

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

Current disposition: keep PRD-derived implementation direction warning-qualified and require review evidence before using PRD-only details as closure proof. CONTRACT, TYPES, SPEC, PLAN, and the accepted decomposition remain the unqualified sources for binding permission vocabulary, invariants, mode mapping, sequencing, and deliverable scope.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Omit denied tools vs expose and deny at call time | Prefer omission where possible to reduce model context and accidental attempts, but still enforce denial at runtime because exposure control alone is not a safety boundary. Source: `docs/SPEC.md` Section 14.3. |
| SDK mode vs Chirality overlay | Use SDK posture where it helps, but preserve Chirality-owned capability policy with explicit hard-deny precedence, decision records, event logs, path containment, and human-gate semantics. Sources: `docs/PLAN.md` risk table; `docs/PRD.md` KG-026, MATCH status. — reconciled under D-APP-38 |
| `ask` UX vs deterministic execution | Interactive approval can be appropriate for governed actions, but only if the persisted decision precedes SDK allow/deny return. Non-interactive contexts should use `dontAsk` denial rather than inventing approval. |
| Mode mapping now vs future SDK drift | Keep mapping centralized and tested because SDK permission behavior may change. Source: `docs/PRD.md` KG-021, MATCH status. — reconciled under D-APP-38 |

## Examples

| Scenario | Expected overlay result |
|---|---|
| `readOnly` session attempts `Read` on an allowed project file | `allow` if the tool surface and path policy permit it; persist permission evidence if governed. Exact path-policy integration: TBD. |
| `readOnly` session attempts `Write`, `Edit`, `Bash`, or a network-capable tool | `deny`; do not execute. |
| `dontAsk` session attempts an unknown tool | `deny` without prompting; unknown-tool structured validation may be owned by DEL-06-02. |
| `ask` session attempts a governed write | `ask` at application level, persist the human/UI decision, then return SDK allow or deny. |
| SDK `allowedTools` includes a tool that Chirality policy denies | Final decision is `deny`; `allowedTools` does not bypass deny policy. |
| Developer-local `bypass` is enabled | SDK bypass may be used only in developer-local mode; Chirality deny hooks and disallowed tools still apply. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No direct source conflict identified during P1/P2. PRD has a MATCH source state. | `_REFERENCES.md` REF-006 | `docs/PRD.md` sections used above | All PRD-cited requirements and guidance | Treat PRD as a current MATCH source under the reconciled D-APP-38 source state. | TBD — reconciled under D-APP-38 |

## Pass 3 Semantic Lensing Disposition

| ItemID | Disposition | Evidence and source reread |
|---|---|---|
| X-001 | Incorporated as an explicit PRD MATCH disposition. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
