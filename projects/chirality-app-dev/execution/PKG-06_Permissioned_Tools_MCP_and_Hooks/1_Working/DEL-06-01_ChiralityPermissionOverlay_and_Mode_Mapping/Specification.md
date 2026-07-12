# Specification: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Scope

DEL-06-01 specifies the Chirality permission overlay and mode mapping needed to mediate governed tool use in PKG-06. It covers structured permission decisions, explicit hard-deny precedence, Chirality-to-SDK mode posture, `canUseTool` approval mediation, and permission-event persistence for governed tool attempts.

In scope:

- Produce a permission overlay module that can return structured allow, deny, or application-level ask decisions.
- Map `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, and developer-local `bypass` to SDK posture plus Chirality overlay behavior.
- Ensure explicit denies override SDK or policy allows.
- Persist permission decisions and `tool.permission` event evidence before execution continues.
- Provide tests for `readOnly`, `dontAsk`, and `ask` behavior.

Out of scope:

- Detailed path containment, instruction-root protection, symlink rejection, write provenance, and hook lifecycle implementation, which belong to DEL-06-04 and DEL-06-06.
- Tool resolver, deterministic tool ordering, read MCP implementations, and unknown-tool validation, except where their outputs feed this overlay. Those belong primarily to DEL-06-02 and DEL-06-03.
- Remote MCP, plugin marketplace, and broad tool search, which are out of current scope without governed amendment.

Sources: `_CONTEXT.md`; decomposition PKG-06 rows; `docs/SPEC.md` Sections 14 and 15; `docs/PRD.md` R2/R3 with MATCH status. (reconciled under D-APP-38).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-06-01-REQ-001 | The permission overlay MUST produce or persist a structured `HarnessPermissionDecision` with `decisionId`, `sessionId`, `toolName`, `decision`, `reason`, `source`, `decidedAt`, and optional safe metadata. | `docs/TYPES.md` Section 8.2; decomposition SOW-054 |
| DEL-06-01-REQ-002 | The decision value MUST be one of `allow`, `deny`, or application-level `ask`; `ask` MUST resolve to an SDK allow or deny before SDK callback return. | `docs/TYPES.md` Section 8.2; decomposition SOW-058 |
| DEL-06-01-REQ-003 | Deny MUST override allow when any explicit deny is produced by policy, path containment, hook, governance, SDK deny rule, or human gate. | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
| DEL-06-01-REQ-004 | The overlay MUST NOT treat `allowedTools` alone as a restriction boundary. Restriction MUST use disallowed tools, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| DEL-06-01-REQ-005 | In `readOnly`, write/edit/bash/network-capable tools and unexpected tools MUST be denied or not exposed. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/SPEC.md` Section 15.1 |
| DEL-06-01-REQ-006 | In `dontAsk`, exact safe tools may be pre-approved, and everything else MUST deny without prompting. | `docs/CONTRACT.md` Section 1.6 K-PERM-5; `docs/SPEC.md` Section 15.1 |
| DEL-06-01-REQ-007 | In `ask`, governed writes or shell requests MUST be mediated through `canUseTool` and UI approval, and the decision MUST be persisted before returning allow or deny. | `docs/SPEC.md` Section 15.1; decomposition SOW-058 |
| DEL-06-01-REQ-008 | In `workspaceWrite`, SDK edit acceptance MUST be allowed only after write hooks pass; otherwise explicit approval posture is required. | `docs/SPEC.md` Section 15.1; `docs/PRD.md` R3, MATCH status — reconciled under D-APP-38 |
| DEL-06-01-REQ-009 | `bypass` MUST be developer-local only, never shipped as ordinary operator behavior, and still subject to Chirality denies. | `docs/CONTRACT.md` Section 1.6 K-PERM-6; `docs/SPEC.md` Section 15.1 |
| DEL-06-01-REQ-010 | Governed tool attempts MUST produce `tool.permission` evidence including source, reason, and safe SDK metadata when available. | decomposition SOW-056; `docs/PRD.md` R2 implementation targets, MATCH status — reconciled under D-APP-38 |
| DEL-06-01-REQ-011 | Prompt text MUST NOT be treated as a safety boundary for filesystem writes, tool exposure, bash, subagents, or domain operations. | `docs/CONTRACT.md` Section 1.6 K-PERM-2 |
| DEL-06-01-REQ-012 | In-process Chirality MCP tools MUST pass through the same permission policy as SDK built-ins when the overlay evaluates them. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2 |
| DEL-06-01-REQ-013 | The permission overlay MUST keep public Chirality contracts product-owned rather than SDK-shaped, with SDK-specific values translated as adapter metadata where needed. | `docs/CONTRACT.md` Section 1.5 K-ENGINE-4; `docs/PRD.md` Section 9.4, MATCH status — reconciled under D-APP-38 |
| DEL-06-01-REQ-014 | Tests MUST cover `readOnly`, `dontAsk`, and `ask` mode behavior, including denied tool non-execution and permission-event persistence. | `_CONTEXT.md`; `docs/PRD.md` R2 acceptance, MATCH status — reconciled under D-APP-38 |
| DEL-06-01-REQ-015 | The overlay input contract MUST include enough product-owned context to evaluate session identity, optional turn identity, requested tool name, Chirality mode, resolved tool-surface posture, and explicit deny/approval signals without making SDK request objects the public contract. | `docs/TYPES.md` Section 8.2; `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` Section 1.5 K-ENGINE-4 |

## Standards

| Standard or governing source | Applicability |
|---|---|
| `docs/CONTRACT.md` Section 1.6 | Binding invariants for permission, tool exposure, hooks, MCP, path, and bash behavior. |
| `docs/TYPES.md` Section 8 | Vocabulary and target shape for permission modes, permission decisions, tool terms, and `canUseTool`. |
| `docs/SPEC.md` Sections 14 and 15 | Runtime tool surface, MCP tool names, tool surface rules, and Chirality-to-SDK mode mapping. |
| `docs/PLAN.md` R2/R3 | Roadmap sequencing: permission-gated read surface before controlled writes and hooks. |
| `docs/PRD.md` R2/R3 | Product implementation direction; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |

## Verification

| Requirement | Verification approach |
|---|---|
| DEL-06-01-REQ-001, REQ-002 | Unit tests assert decision record shape, allowed enum values, `ask` resolution, and safe metadata handling. |
| DEL-06-01-REQ-003 | Precedence tests inject simultaneous allow and deny sources and assert final deny. |
| DEL-06-01-REQ-004 | Tests prove `allowedTools` does not restrict by itself and that `disallowedTools`, mode policy, hooks, `canUseTool`, or `dontAsk` enforce restriction. |
| DEL-06-01-REQ-005 | `readOnly` tests assert write/edit/bash/network-capable and unexpected tools deny or remain unexposed. |
| DEL-06-01-REQ-006 | `dontAsk` tests assert only exact safe tools are allowed and unknown/unapproved actions deny without UI approval. |
| DEL-06-01-REQ-007 | `ask` tests assert UI-mediated approval path persists the decision before SDK callback return. |
| DEL-06-01-REQ-008 | Integration or contract tests assert `workspaceWrite` cannot allow edits unless hooks report pass. Hook internals remain owned by DEL-06-04. |
| DEL-06-01-REQ-009 | Release/configuration tests assert ordinary shipped modes cannot select SDK `bypassPermissions`; developer-local use still applies Chirality denies. |
| DEL-06-01-REQ-010 | Runtime event tests assert `tool.permission` records source, reason, and safe SDK metadata for governed attempts. |
| DEL-06-01-REQ-011 | Negative tests assert prompt-only permission claims cannot authorize tool exposure or execution. |
| DEL-06-01-REQ-012 | MCP wrapper tests assert Chirality MCP tool attempts pass through overlay evaluation. |
| DEL-06-01-REQ-013 | Type or conformance tests assert public `HarnessEvent`, permission decision, and API contracts do not leak SDK-shaped names except adapter metadata. |
| DEL-06-01-REQ-014 | Test suite includes readOnly/dontAsk/ask fixtures named or tagged for DEL-06-01 traceability. Exact paths: TBD. |
| DEL-06-01-REQ-015 | Type or unit tests assert the overlay accepts a product-owned input shape and translates SDK-specific values only at the adapter boundary. Exact implementation path remains TBD. |

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

## Documentation

Required implementation evidence:

- Permission overlay module or equivalent product-owned runtime component.
- Mode mapping table or tested mapping fixture for `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, and developer-local `bypass`.
- Permission decision record type or schema.
- `tool.permission` event schema/mapping evidence.
- `canUseTool` approval mediation tests.
- ReadOnly/dontAsk/ask behavioral tests.
- Residual-risk note for `docs/PRD.md` MATCH under the reconciled D-APP-38 source state. (reconciled under D-APP-38).

## Pass 3 Semantic Lensing Disposition

| ItemID | Disposition | Evidence and source reread |
|---|---|---|
| C-001 | Incorporated as bounded interface requirements while preserving exact implementation shape as TBD. | Datasheet Construction and DEL-06-01-REQ-015 now identify the minimum product-owned context. Reread: `docs/TYPES.md` Section 8.2; `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` Section 1.5. |
| F-001 | Incorporated as verification evidence for workspaceWrite hook-pass gating, with hook internals deferred to DEL-06-04. | Verification keeps hook implementation out of this deliverable but requires contract/integration proof before edits can allow. Reread: `docs/SPEC.md` Section 15.1; decomposition PKG-06 rows for DEL-06-04. |
| X-002 | Converted to explicit path-TBD verification evidence requirements rather than invented test names. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| E-002 | Incorporated as MCP parity verification with concrete source obligation and adjacent wrapper ownership. | DEL-06-01-REQ-012 and verification require parity; wrapper detail remains with DEL-06-03. Reread: `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/SPEC.md` Section 14.2; decomposition PKG-06 rows for DEL-06-03. |

## Traceability

| Source item | Covered by |
|---|---|
| SOW-054 Structured permission decisions | DEL-06-01-REQ-001, REQ-002, REQ-013, REQ-015 |
| SOW-055 Permission modes and capability policy with explicit hard-deny precedence | DEL-06-01-REQ-003 through REQ-009, REQ-011, REQ-015 |
| SOW-056 Tool permission events | DEL-06-01-REQ-010 |
| SOW-058 Interactive approval through `canUseTool` | DEL-06-01-REQ-002, REQ-007 |
