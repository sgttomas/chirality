# Guidance: DEL-06-03 Initial Chirality MCP Read Tools

## Purpose

DEL-06-03 provides the first Chirality-owned in-process MCP read tools so the runtime can expose deterministic project-state operations without opening write, edit, shell, remote MCP, plugin, or domain-operation capability. The deliverable supports OBJ-005 by keeping tool exposure behind capability policy with explicit hard-deny precedence and MCP wrappers, and OBJ-006 by reading filesystem-native project truth.

Source basis: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 6-7 and 9; `docs/PLAN.md` R2; `docs/PRD.md` Sections 8.13-8.14.

## Principles

1. Read tools come first.

   The R2 slice enables SDK read tools and Chirality read MCP tools before write/edit/bash capability. Treat this deliverable as a read-surface and descriptor/wrapper contract, not a general tool expansion.

2. MCP is a transport, not a policy escape.

   In-process Chirality MCP tools must go through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. A tool being implemented locally does not make it safe to expose.

3. Determinism is part of the contract.

   Tool naming, ordering, server IDs, wrapper metadata, and allow/deny behavior should be table-driven or otherwise stable for a fixed runtime configuration.

4. Explicit hard-deny precedence is non-negotiable.

   `allowedTools` may auto-approve, but it is not a restriction boundary. Denies from policy, hooks, path containment, governance, SDK deny rules, or human gates must win.

5. Filesystem truth remains local and inspectable.

   Status and dependency tools should read the canonical project files, not hidden runtime state. Unknowns and malformed records should produce explicit results rather than inferred project truth.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Tool boundaries | Keep `status_transition` and `deps_write` out of this read-tool slice except as excluded adjacent tools. | `docs/SPEC.md` Section 14.2 |
| Scaffold behavior | `mcp__chirality__scaffold` is listed as gated. For this deliverable, implement only preview/dry-run behavior where applicable unless a later write-surface gate authorizes more. | `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2 |
| Dependency reads | Prefer a clear `Dependencies.csv` validation result. Behavior when the deliverable has `_DEPENDENCIES.md` but no `Dependencies.csv` is TBD and should align with DEL-07-05. | `docs/CONTRACT.md` Section 1.7 K-DEP-1; `_DEPENDENCIES.md` |
| Status reads | Read `_STATUS.md` as canonical lifecycle state. Do not infer status from folder names, chat state, runtime events, or document presence. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1 |
| Scope scan | Scope scan should stay bounded to the selected working root and stable deliverable IDs. | `docs/SPEC.md` Sections 17.2 and 14.2; `docs/CONTRACT.md` K-PATH-2 |
| Runtime events | Permission/start/completion/failure event persistence may depend on R1/R2 runtime plumbing. If not available, expose a typed integration seam and tests around the expected behavior. | `docs/PLAN.md` R2; `docs/PRD.md` Section 8.13 FR-083 |
| PRD hash warning | The current PRD text is accessible but hash-mismatched against `_REFERENCES.md`; use it with the warning recorded, and avoid treating PRD-only detail as silently final if another accepted source disagrees. | `_REFERENCES.md`; task brief |

### Source-State Posture

PRD-backed details remain usable as warning-qualified implementation direction because `_REFERENCES.md` records `docs/PRD.md` as accessible but hash-mismatched. Closure should not rely on PRD-only wrapper-policy detail until one of these happens: the reference hash is refreshed, a human accepts the current PRD text for this deliverable, or the same requirement is corroborated by `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, or `docs/PLAN.md`.

## Trade-offs

| Decision Area | Trade-off | Recommended Posture |
|---|---|---|
| Single wrapper vs per-tool wrappers | A shared wrapper improves consistent permission/event/redaction behavior; per-tool wrappers can drift. | Use a shared wrapper contract with per-tool metadata and execution handlers. |
| Scaffold included vs deferred | SPEC lists scaffold as gated; PLAN R2 calls for scaffold preview/dry-run where appropriate. | Include dry-run/preview only, with write execution denied or delegated to later gated surfaces. |
| Dependency file absence | `Dependencies.csv` may not exist early in a deliverable lifecycle. | Return an explicit "not present / not tracked yet" result; do not fabricate dependencies. |
| Event coupling | Full event persistence may not be complete when read tools are first drafted. | Keep event emission/adaptation explicit and testable; mark unavailable runtime pieces `TBD` instead of embedding hidden behavior. |
| SDK-specific APIs | PRD references SDK MCP APIs, but Chirality contracts must remain product-owned. | Use SDK APIs behind product-owned wrappers and tests; do not leak SDK-shaped public contracts. |

### Scaffold Boundary Rationale

Scaffold preview belongs in this read-tool slice only as a non-mutating planning surface. `docs/SPEC.md` Section 14.2 classifies `mcp__chirality__scaffold` as gated, while `docs/PLAN.md` R2 sequences read and preview capability before write/edit/bash expansion. The practical boundary is therefore: allow a deterministic preview of intended scaffold effects, deny or defer filesystem mutation, and move any write-capable scaffold execution to the later governed write/path-hook surface.

## Examples

Example read-tool inventory:

| Tool | Expected Result Shape |
|---|---|
| `mcp__chirality__status_read` | Parsed `_STATUS.md` snapshot plus source path, parse warnings, and raw/normalized state fields. |
| `mcp__chirality__deps_read` | `Dependencies.csv` validation summary when present; explicit missing/not-tracked status when absent; warnings sourced to files. |
| `mcp__chirality__scope_scan` | Bounded package/deliverable scan summary with stable IDs and rejected out-of-root requests. |
| `mcp__chirality__scaffold` | Preview/dry-run plan showing intended scaffold effects without applying filesystem writes. |

Example wrapper metadata fields:

- Tool name.
- MCP server ID.
- Input schema.
- Permission class.
- Read/write classification.
- Concurrency policy.
- Interruption policy.
- Execution handler reference.
- Result summarization behavior.
- Redaction/event metadata.
- Denial behavior.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| N/A | No source-content conflict identified during Pass 1/2 drafting. Source-state warning only: `docs/PRD.md` has HASH_MISMATCH in `_REFERENCES.md`. | `_REFERENCES.md` REF-006 | Task brief | References and source confidence | Treat as warning per task brief; re-check hash before implementation closure. | TBD |

## Pass 3 Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| X-001 | Incorporated as source-state posture | PRD HASH_MISMATCH handling is now explicit before PRD-only policy detail can be used for closure. Source reread: `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.13; `docs/CONTRACT.md` Section 1.6. |
| E-002 | Incorporated | Scaffold preview rationale now explains why preview/dry-run is in scope while write-capable scaffold execution remains gated. Source reread: `docs/SPEC.md` Section 14.2; `docs/PLAN.md` R2. |
