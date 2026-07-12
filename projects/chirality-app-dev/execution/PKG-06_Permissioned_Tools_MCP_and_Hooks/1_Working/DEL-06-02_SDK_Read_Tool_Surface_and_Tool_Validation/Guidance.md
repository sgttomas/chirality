# Guidance: DEL-06-02 SDK Read Tool Surface and Tool Validation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

DEL-06-02 exists to make `opts.tools` meaningful without letting SDK defaults or tool implementation availability define Chirality's runtime authority. It is the read-first tool-surface slice of PKG-06: it validates requested names, normalizes deterministic exposure, and hands the resulting surface to permission policy before model execution.

Sources: `_CONTEXT.md`; decomposition PKG-06; `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Section 14; `docs/PRD.md` Section 8.13 with MATCH status. (reconciled under D-APP-38).

## Principles

1. Resolve before request construction. Tool names should be validated and normalized before SDK options or model context are built. Sources: decomposition SOW-047; `docs/PRD.md` FR-078, MATCH status. (reconciled under D-APP-38).
2. Unknown is an error, not a fallback. Unknown tool names should produce structured validation errors rather than being silently passed through. Source: `docs/SPEC.md` Section 14.3.
3. Determinism is part of the contract. Stable inputs should produce stable tool ordering, names, MCP server IDs, and allow/deny lists. Sources: decomposition SOW-049; `docs/CONTRACT.md` Section 1.6 K-TOOL-1.
4. Read tools come first. Initial exposure should be SDK read tools plus Chirality read MCP tools; write/edit/bash wait for later governance phases. Sources: decomposition SOW-050; `docs/PRD.md` FR-082, MATCH status. (reconciled under D-APP-38).
5. Exposure is separate from implementation. A tool being implemented or available in the SDK does not mean it belongs in model context. Source: `docs/CONTRACT.md` Section 1.6 K-TOOL-2.
6. `allowedTools` is not a safety boundary. Treat it as SDK posture/auto-approval input only; restriction still requires deny rules, mode policy, hooks, `canUseTool`, and/or `dontAsk`. Sources: `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3.
7. MCP is not a bypass. Chirality MCP names are transport exposure for deterministic operations, not a path around policy. Source: `docs/CONTRACT.md` Section 1.6 K-MCP-1.

## Considerations

### Resolver Shape

The resolver should be small and auditable:

| Concern | Guidance |
|---|---|
| Registry ownership | Keep SDK built-in names and Chirality MCP names in an explicit registry or catalog. Exact path: TBD. |
| Alias policy | Avoid implicit aliases unless a source file defines them. Current sources name SDK candidates and `mcp__chirality__*` names directly. |
| Error shape | Return structured validation errors for unknown names. Exact error type: TBD. |
| Ordering | Sort or otherwise normalize deterministically after validation and policy filtering. |
| Output | Emit SDK-facing names and MCP server/tool identifiers as adapter metadata, not public product semantics. |

### Read-First Surface

Initial read candidates are `Read`, `LS`, `Glob`, and `Grep` where available, plus Chirality read MCP tools such as status read, dependency read, scope scan, and scaffold preview/dry-run. Do not use this deliverable to expose `Write`, `Edit`, or `Bash`; those require later hooks, path policy, output storage, and audit behavior.

### Relationship to Adjacent Deliverables

| Adjacent deliverable | Interface point |
|---|---|
| DEL-06-01 | Provides capability policy with explicit hard-deny precedence and mode policy that this resolver must consume or preserve. |
| DEL-06-03 | Provides Chirality MCP read tool definitions that this resolver registers or references. |
| DEL-06-04 | Provides write/edit hooks and path policy needed before powerful write tools can be exposed. |
| DEL-06-05 | Provides bash governance needed before `Bash` can be exposed. |
| DEL-05-05 | Provides tool result budget/artifact policy referenced by later tool-result handling. |

### PRD Hash Status

`docs/PRD.md` is listed as MATCH in `_REFERENCES.md`. Its R2/Section 8.13 content aligns with matching SPEC, CONTRACT, TYPES, PLAN, and decomposition slices used here, but PRD-only implementation details should be reviewed after source-state reconciliation. (reconciled under D-APP-38).

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

### Terminology Normalization

Use the following terms distinctly:

| Term | Use |
|---|---|
| read-first | Sequencing posture: read tools are enabled before write/edit/bash capability. |
| read-only | Capability class: tools that do not write, shell out, or perform network-capable side effects. |
| `readOnly` | Runtime mode token from the permission vocabulary. |

This normalization preserves the difference between staged rollout, tool capability, and runtime mode policy. (P3: B-002)

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Omit denied tools vs include and deny at call time | Prefer omission where possible to reduce context and accidental attempts, but never rely on omission alone; runtime denial must still hold. |
| Strict registry vs permissive passthrough | Use strict registry behavior. Passthrough conflicts with SOW-047 and makes unknown tool names hard to audit. |
| Resolver owns permission vs resolver consumes permission | Keep the resolver focused on validation and deterministic exposure. Capability-forward policy with explicit hard-deny precedence semantics belong to permission policy, but resolver output must not bypass it. |
| SDK-specific names vs Chirality contracts | SDK names are adapter metadata. Public runtime contracts and event schemas should stay Chirality-owned. |
| Read convenience vs staged governance | Exposing read tools first is useful, but it must not become a back door to write/bash or remote tool expansion. |

## Examples

| Scenario | Expected result |
|---|---|
| `opts.tools` contains `Read`, `Grep`, and `mcp__chirality__status_read` in read-first mode | Resolver accepts registered names and emits deterministic SDK/MCP surface order, subject to permission filtering. |
| `opts.tools` contains `Read` and `UnknownSearch` | Resolver returns a structured validation error for `UnknownSearch`; unknown name is not sent to the SDK. |
| SDK supports `Write`, but current mode is read-first/read-only | Resolver excludes or marks `Write` denied according to policy; implementation availability does not imply exposure. |
| `allowedTools` includes a tool that Chirality policy denies | Final exposed/executable surface respects deny policy; `allowedTools` does not bypass restriction. |
| A new `mcp__chirality__domain_*` name appears before governed domain amendment | Treat as unsupported/TBD unless accepted source updates authorize future domain tools. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No direct source conflict identified during P1/P2. PRD has a MATCH source state. | `_REFERENCES.md` REF-006 | `docs/PRD.md` sections used above | All PRD-cited requirements and guidance | Treat PRD as a current MATCH source under the reconciled D-APP-38 source state. | TBD — reconciled under D-APP-38 |

## D-APP-56 roster clarification (2026-07-12)

R4-P27 reconciles the former unsupported/TBD domain-tool roster wording: PKG-10 owns the ruled domain-profile registry and proposal-tool roster. DEL-06-02 remains the SDK read-tool and validation owner and does not duplicate that ownership.
