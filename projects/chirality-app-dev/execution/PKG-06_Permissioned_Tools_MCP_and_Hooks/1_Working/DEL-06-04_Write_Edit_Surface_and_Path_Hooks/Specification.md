# Specification: DEL-06-04 Write/Edit Surface and Path Hooks

## Scope

DEL-06-04 specifies the write/edit execution surface and path hooks needed to permit controlled workspace writes without relying on prompt text, SDK defaults, or `allowedTools` alone. It covers project-root or working-root containment, instruction-root write blocking, symlink write rejection, exact edit preconditions, and provenance hooks for write/edit attempts.

In scope:

- Gate SDK `Write`/`Edit` and Chirality MCP write tools before mutation.
- Enforce active project or working-root containment.
- Block instruction-root writes during ordinary project execution.
- Reject symlink writes in the initial policy.
- Require exact edit preconditions before edit-style mutation.
- Record safe provenance, diff/summary, permission/runtime event evidence, and hook outcomes.
- Provide path policy fixtures and write/edit tests for allowed and denied cases.

Out of scope:

- Permission overlay mode semantics and `canUseTool` approval mediation owned by DEL-06-01, except where their decisions feed this hook.
- Read tool exposure, read MCP wrappers, unknown-tool validation, and deterministic tool ordering owned by DEL-06-02 and DEL-06-03.
- Bash governance owned by DEL-06-05.
- Hook lifecycle and compaction mirror details owned by DEL-06-06, except for write/edit hook evidence needed by this deliverable.
- Domain-engine protected-path operation semantics, except where a protected path hook implication is shared with future path policy.

Sources: `_CONTEXT.md`; decomposition PKG-06 rows; `docs/CONTRACT.md` Sections 1.3 and 1.6; `docs/SPEC.md` Sections 14 and 15; `docs/PRD.md` Section 7.9 with HASH_MISMATCH warning.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-06-04-REQ-001 | The runtime MUST run a pre-execution hook or equivalent gate before any write/edit mutation is performed. | decomposition SOW-057; `docs/SPEC.md` Section 15.2 |
| DEL-06-04-REQ-002 | The write/edit gate MUST deny filesystem operations outside the active project or working root. | decomposition SOW-027; `docs/CONTRACT.md` Section 1.6 K-PATH-2 |
| DEL-06-04-REQ-003 | The write/edit gate MUST deny ordinary project writes under the instruction root. | decomposition SOW-027; `docs/CONTRACT.md` Section 1.3 K-ROOT-2 |
| DEL-06-04-REQ-004 | The write/edit gate MUST reject symlink writes in the initial policy. | decomposition SOW-060; `docs/CONTRACT.md` Section 1.6 K-PATH-3 |
| DEL-06-04-REQ-005 | Edit-style operations MUST require exact edit preconditions before mutation. | decomposition SOW-060; `docs/PRD.md` Section 7.9, HASH_MISMATCH warning |
| DEL-06-04-REQ-006 | Hook failures MUST fail closed for write/edit actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| DEL-06-04-REQ-007 | Explicit denies from policy, path containment, hook, governance, SDK deny rule, or human gate MUST override any allow. | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
| DEL-06-04-REQ-008 | `allowedTools` MUST NOT be treated as sufficient restriction or safety boundary for write/edit capability. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| DEL-06-04-REQ-009 | `readOnly` mode MUST deny write/edit capability, and `workspaceWrite` MUST allow governed writes only after hooks and policy pass. | `docs/SPEC.md` Section 15.1; `docs/PRD.md` Section 7.9, HASH_MISMATCH warning |
| DEL-06-04-REQ-010 | In-process Chirality MCP write tools MUST pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6 K-MCP-1 |
| DEL-06-04-REQ-011 | Successful controlled writes/edits SHOULD be atomic where practical and MUST emit a diff or summary suitable for audit. | `docs/PRD.md` Section 7.9, HASH_MISMATCH warning |
| DEL-06-04-REQ-012 | Every write attempt MUST produce permission/runtime event evidence or equivalent audit records, including denials. | `docs/PLAN.md` R3 acceptance; `docs/PRD.md` Section 7.9, HASH_MISMATCH warning |
| DEL-06-04-REQ-013 | Provenance append hooks MUST record safe provenance/run evidence where policy requires it. | `docs/SPEC.md` Section 15.2 |
| DEL-06-04-REQ-014 | Path validation SHOULD include regular-file and symlink checks for attachment/write-relevant paths where applicable. | `docs/SPEC.md` attachment/path validation bullets; decomposition SOW-060 |
| DEL-06-04-REQ-015 | Tests MUST cover outside-root denial, instruction-root denial, symlink denial, stale or missing exact edit preconditions, allowed in-root write/edit behavior, and provenance/event evidence. | `_CONTEXT.md`; `docs/PLAN.md` R3 acceptance |

## Standards

| Standard or governing source | Applicability |
|---|---|
| `docs/CONTRACT.md` Sections 1.3 and 1.6 | Binding root, permission, hook, MCP, and path invariants. |
| `docs/SPEC.md` Sections 14 and 15 | Tool surface rules, mode mapping, and required hook behavior. |
| `docs/TYPES.md` Section 8 | Permission mode vocabulary, tool surface terms, and hook terms. |
| `docs/PLAN.md` R3 | Controlled write/edit sequencing and acceptance criteria. |
| `docs/PRD.md` Section 7.9 | Controlled write/edit product flow; use with HASH_MISMATCH warning from `_REFERENCES.md`. |

## Verification

| Requirement | Verification approach |
|---|---|
| DEL-06-04-REQ-001, REQ-006 | Unit or integration tests inject hook pass/fail outcomes and assert no mutation occurs when the hook fails or is unavailable. |
| DEL-06-04-REQ-002 | Path containment tests attempt outside-root absolute and traversal-equivalent targets and assert denial before mutation. |
| DEL-06-04-REQ-003 | Instruction-root fixtures assert writes under the instruction root are denied during ordinary project execution. |
| DEL-06-04-REQ-004 | Symlink fixtures assert symlink targets and symlink path segments are rejected in the initial policy. |
| DEL-06-04-REQ-005 | Edit tests assert stale, missing, or non-exact preconditions do not mutate files. |
| DEL-06-04-REQ-007, REQ-008 | Precedence tests assert SDK allows, `allowedTools`, or session allows cannot override Chirality deny policy. |
| DEL-06-04-REQ-009 | Mode tests assert `readOnly` cannot write and `workspaceWrite` writes only after permission and hook gates pass. |
| DEL-06-04-REQ-010 | MCP parity tests assert `mcp__chirality__deps_write` or future write MCP tools pass through equivalent gates. |
| DEL-06-04-REQ-011, REQ-013 | Successful-write tests assert diff/summary and provenance metadata are produced without leaking unsafe data. |
| DEL-06-04-REQ-012 | Runtime event tests assert allowed and denied write attempts produce permission/runtime evidence. |
| DEL-06-04-REQ-014 | Path fixture tests cover regular-file, symlink, extension, and validation failure cases where those checks apply. |
| DEL-06-04-REQ-015 | Test index or validation marker references this deliverable and includes the required negative and positive fixtures. |

## Documentation

Required implementation evidence:

- Write/edit hook module or equivalent gate: TBD.
- Path policy helper or fixture set: TBD.
- Instruction-root and working-root resolver integration: TBD.
- Exact edit precondition validator: TBD.
- Provenance/diff/summary recorder: TBD.
- Write/edit negative and positive tests: TBD.
- Residual-risk note for `docs/PRD.md` HASH_MISMATCH until source state is reconciled.

## Traceability

| Source item | Covered by |
|---|---|
| SOW-027 Project-root containment and instruction-root protection | DEL-06-04-REQ-002, REQ-003, REQ-007, REQ-015 |
| SOW-057 Hooks and fail-closed behavior | DEL-06-04-REQ-001, REQ-006, REQ-012, REQ-013 |
| SOW-060 Safe write/edit behavior | DEL-06-04-REQ-004, REQ-005, REQ-011, REQ-014, REQ-015 |
| OBJ-005 Deny-first permission policy, hooks, result budgets, and approvals | DEL-06-04-REQ-001, REQ-006 through REQ-013 |
| OBJ-006 Filesystem project truth through containment and change discipline | DEL-06-04-REQ-002 through REQ-005, REQ-011 through REQ-015 |
