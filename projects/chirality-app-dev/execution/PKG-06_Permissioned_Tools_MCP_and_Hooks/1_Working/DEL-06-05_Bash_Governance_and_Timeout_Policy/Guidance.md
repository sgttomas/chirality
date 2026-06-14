# Guidance: DEL-06-05 Bash Governance and Timeout Policy

## Purpose

DEL-06-05 exists to prevent the SDK `Bash` surface from becoming an accidental escape hatch. Bash is powerful enough to read, write, delete, invoke networks, spawn long-running work, and produce unbounded output, so Chirality treats it as denied by default and enables it only after product-owned governance, timeout, result storage, interruption, and audit behavior are ready.

Sources: `_CONTEXT.md`; decomposition row SOW-062; `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4.

## Principles

1. Denied Bash must be a non-event at the process layer. A policy denial is only effective if no shell process starts. Sources: `docs/PLAN.md` R4 acceptance; `docs/PRD.md` FR-100, HASH_MISMATCH warning.
2. Bash exposure follows capability-forward permission semantics with explicit hard-deny precedence. Any explicit deny from policy, hook, path check, governance, SDK deny rule, or human gate blocks execution. Source: `docs/CONTRACT.md` Section 1.6 K-PERM-1.
3. `allowedTools` is not a security boundary. Bash must not become available merely because it appears in a tool list; the overlay, disallowed tools, mode policy, hooks, and approval mediation remain controlling. Sources: `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3.
4. Timeout and result storage are part of authorization, not post-processing. A Bash request without a timeout/capture/storage plan is not ready to execute. Source: `docs/CONTRACT.md` Section 1.6 K-BASH-1.
5. Auditability is product-owned. SDK transcripts may help debugging and resume, but Chirality event records remain canonical for runtime governance. Sources: `docs/CONTRACT.md` Section 1.5 K-EVENT-4; `docs/PRD.md` FR-121, HASH_MISMATCH warning.

## Considerations

### Mode Behavior

| Mode | Guidance | Source |
|---|---|---|
| `readOnly` | Bash should be unavailable or hard-denied. Treat shell as write/network-capable even when a proposed command appears read-like. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/TYPES.md` Section 8.1 |
| `dontAsk` | Bash should deny without prompting. The accessible sources do not define an approved safe-shell subset. | `docs/CONTRACT.md` Section 1.6 K-PERM-5; `docs/PLAN.md` R4 |
| `ask` | Bash may request approval only after the command has passed policy preflight and the approval decision can be persisted before SDK allow/deny return. | `docs/SPEC.md` Section 15.1 |
| `workspaceWrite` | Bash still needs explicit Bash governance; write permission does not imply shell permission. | `docs/SPEC.md` Section 15.1; `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
| `bypass` | Developer-local only, never ordinary shipped behavior, and still subject to Chirality deny hooks and disallowed tools. | `docs/CONTRACT.md` Section 1.6 K-PERM-6 |

### Timeout And Capture Policy

The accessible sources require a timeout but do not provide a Bash-specific numeric default or maximum. Keep numeric values as `TBD` until accepted source or human ruling supplies them. The implementation should nevertheless require a timeout field or resolved timeout policy before a command can start.

Stdout and stderr should be captured separately so users and replay tooling can distinguish normal command output from warnings/errors. Large output should be stored under session artifacts and represented by safe metadata, not streamed unbounded into chat or model context.

### Hooks And Path Policy

Bash-specific governance should compose with the broader hook model. If a command can write, delete, traverse outside the project, touch the instruction root, follow symlink writes, or invoke prohibited network behavior, the same capability-forward posture with explicit hard-deny precedence applies. Hook failures fail closed for shell actions.

### PRD Hash Warning

`docs/PRD.md` is listed as HASH_MISMATCH in `_REFERENCES.md`. FR-096, FR-100, FR-121, and R4 implementation targets are useful product direction for this draft, but any implementation detail that depends only on PRD wording should be rechecked after source-state reconciliation.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Omit Bash vs expose and deny | Prefer omission where possible to reduce accidental model attempts, but still enforce runtime denial because tool visibility is not enough. |
| Single global timeout vs command-class timeout | A single default is simpler, but command-class overrides may be needed. Source material does not decide this; mark numeric policy as TBD. |
| Inline output vs artifact storage | Inline small output for usability; preview/store medium or large output so chat and model context remain bounded. |
| User approval vs policy denial | Do not ask the user to approve a command that fails policy preflight. Approval should only mediate commands that are otherwise governable. |
| SDK transcript vs Chirality events | Use SDK transcript linkage for resume/debugging, but rely on Chirality events for accepted-turn, permission, tool, artifact, and terminal outcome audit. |

## Examples

| Scenario | Expected result |
|---|---|
| A new session starts with no explicit Bash enablement | `Bash` is omitted or denied. |
| `readOnly` session requests `Bash` for `ls` | Deny or omit; use read tools such as `LS`, `Glob`, or `Grep` where available instead. |
| `dontAsk` session requests `Bash` for any command | Deny without prompting under current source policy. |
| `ask` session requests a command without timeout metadata | Deny before approval because timeout is a prerequisite. |
| Governed mode requests Bash with timeout, capture, and result-storage policy | Run only if policy, hooks, path checks, and approval mediation pass; capture stdout/stderr separately and persist audit events. |
| Command output exceeds inline budget | Store raw output under session artifacts and surface preview plus safe artifact metadata. |
| Active Bash is interrupted | Persist interrupted/cancelled terminal outcome and retain available output metadata according to result policy. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No direct source conflict identified during P1/P2. PRD has a HASH_MISMATCH source-state warning. | `_REFERENCES.md` REF-006 | `docs/PRD.md` sections used above | All PRD-cited requirements and guidance | Treat PRD as warning-qualified source until hash state is reconciled. | TBD |
| DEL-06-05-TIMEOUT-001 | Bash timeout is required, but no Bash-specific numeric default or maximum is present in accessible sources. | `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4 | No numeric Bash timeout source found | `Datasheet.md` Conditions; `Specification.md` REQ-006; `Procedure.md` Steps and Verification | Keep numeric timeout values as `TBD` pending human ruling or accepted source update. | TBD |
