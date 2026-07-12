# Specification: DEL-06-05 Bash Governance and Timeout Policy

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Scope

DEL-06-05 specifies the security-control policy for enabling SDK `Bash` in Chirality. It covers default denial, mode-based exposure, pre-execution governance, timeout requirement, stdout/stderr capture, output storage, interruption behavior, terminal outcome persistence, and audit evidence.

In scope:

- Keep Bash denied by default and denied in `readOnly` / `dontAsk`.
- Permit Bash only in explicitly governed modes after permission, hook, timeout, result-storage, interrupt, and audit checks pass.
- Ensure denied Bash never spawns.
- Define timeout/capture/output metadata expectations for allowed Bash.
- Provide tests for default denial, timeout/capture behavior, result artifact metadata, and denied non-execution.

Out of scope:

- General permission overlay semantics and mode mapping owned by DEL-06-01, except where they are applied to Bash.
- Read tool resolver and MCP read tools owned by DEL-06-02 and DEL-06-03.
- Write/edit path policy owned by DEL-06-04, except Bash must still obey path/hook denies when command execution could mutate the filesystem.
- Hook lifecycle and compaction mirror implementation owned by DEL-06-06, except this deliverable must emit or require Bash-relevant events.
- Remote MCP, plugin marketplace, and broad remote execution, which remain out of current scope without governed amendment.

Sources: `_CONTEXT.md`; decomposition PKG-06 row DEL-06-05 and SOW-062; `docs/CONTRACT.md` Section 1.6; `docs/SPEC.md` Sections 14 and 15; `docs/PLAN.md` R4; `docs/PRD.md` Section 8.15 with MATCH status. (reconciled under D-APP-38).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-06-05-REQ-001 | Bash MUST be denied by default even when the SDK ships or supports a `Bash` tool. | `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
| DEL-06-05-REQ-002 | Bash MUST be denied or omitted from tool exposure in `readOnly` mode. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/SPEC.md` Section 15.1 |
| DEL-06-05-REQ-003 | Bash MUST be denied without prompting in `dontAsk` unless an accepted future policy explicitly defines a safe shell subset. Current source material defines no such subset. | `docs/CONTRACT.md` Section 1.6 K-PERM-5; `docs/PLAN.md` R4 acceptance |
| DEL-06-05-REQ-004 | Bash MUST NOT be enabled by `allowedTools` alone; restriction and enablement MUST be mediated by disallowed tools, permission mode, Chirality policy, hooks, `canUseTool`, and/or human gate as applicable. | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3 |
| DEL-06-05-REQ-005 | A denied Bash request MUST NOT spawn a process. | `docs/PLAN.md` R4 acceptance; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
| DEL-06-05-REQ-006 | Enabling Bash MUST require a timeout before execution. Exact default timeout and maximum override are TBD because no Bash-specific numeric limit is present in accessible sources. | `docs/CONTRACT.md` Section 1.6 K-BASH-1; `docs/PLAN.md` R4 |
| DEL-06-05-REQ-007 | Allowed Bash execution MUST capture stdout and stderr separately. | `docs/PLAN.md` R4 implementation targets; `docs/PRD.md` FR-100, MATCH status — reconciled under D-APP-38 |
| DEL-06-05-REQ-008 | Medium or large Bash output MUST be previewed or stored under session artifacts rather than streamed unbounded into chat/model context. | `docs/PRD.md` FR-096, MATCH status; `docs/PLAN.md` R4 — reconciled under D-APP-38 |
| DEL-06-05-REQ-009 | Bash output metadata MUST include safe artifact lookup and terminal-outcome data. D-APP-42 assigns the artifact schema (`toolName`, `toolUseId`, `turnId`, byte lengths, truncation flag, SHA-256, relative artifact path, and stdout/stderr stream labels); ADQ-11/D-APP-43 establishes `interrupted` Bash results as `tool.failed` terminal evidence. | `docs/TYPES.md` `outputArtifactPath`; D-APP-42; `Evidence_ADQ-11_Permission_Tool_Residuals.md`; D-APP-43 |
| DEL-06-05-REQ-010 | Allowed Bash execution MUST support interrupt/cancel where the SDK or process runner exposes that capability; where interruption cannot be performed, Chirality MUST persist the terminal failure, cancellation, or residual-risk outcome that actually occurred rather than claiming successful interruption. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` Section 1.5 K-EVENT-3; `docs/PLAN.md` R4 acceptance |
| DEL-06-05-REQ-011 | Bash permission, start, completion, failure, timeout, and interruption behavior MUST be auditable in product-owned Chirality event records. | `docs/CONTRACT.md` Section 1.5 K-EVENT-2 through K-EVENT-4; `docs/TYPES.md` event vocabulary |
| DEL-06-05-REQ-012 | Hook failures MUST fail closed for shell actions. | `docs/CONTRACT.md` Section 1.6 K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| DEL-06-05-REQ-013 | Bash commands that can affect filesystem state MUST remain subject to working-root containment, instruction-root protection, symlink write rejection, redaction, provenance, and hook policy where applicable. | `docs/CONTRACT.md` Section 1.6 K-PERM-1, K-PATH-2, K-PATH-3; `docs/SPEC.md` Section 15.2 |
| DEL-06-05-REQ-014 | Public Chirality APIs, permission records, and audit events MUST remain product-owned; SDK Bash names and transcript fields are adapter metadata. | `docs/DIRECTIVE.md` Sections 2.8 and 2.10; `docs/SPEC.md` Sections 10.1 and 10.2 |
| DEL-06-05-REQ-015 | Tests MUST cover default deny, `readOnly` deny, `dontAsk` deny, denied-never-spawns, timeout, stdout/stderr separation, output artifact metadata, and interruption behavior where technically available. | `_CONTEXT.md`; `docs/PLAN.md` R4 acceptance |
| DEL-06-05-REQ-016 | Bash preflight MUST enforce the implemented command metadata and network posture checks: command name/length, timeout, redirection/path-token counts, network-command denial, and URL-scheme denial. | `frontend/src/lib/harness/tool-shell-policy.ts`; `frontend/src/__tests__/lib/chirality-hooks.test.ts`; `docs/CONTRACT.md` Section 1.6 K-BASH-1 |

## Standards

| Standard or governing source | Applicability |
|---|---|
| `docs/CONTRACT.md` Section 1.6 | Binding permission, tool exposure, hook, path, and Bash invariants. |
| `docs/CONTRACT.md` Section 1.5 | Runtime event and audit mirror invariants. |
| `docs/SPEC.md` Sections 14 and 15 | SDK tool naming, tool surface rules, permission mode mapping, required hooks, and fail-closed hook behavior. |
| `docs/TYPES.md` Section 8 | Permission mode vocabulary, permission decision shape, tool-surface terms, and `ToolResultStore`. |
| `docs/PLAN.md` R4 | Roadmap sequencing and acceptance criteria for Bash, result budgeting, and context mirror behavior. |
| `docs/PRD.md` Section 8.15 | Product requirements for tool output storage, Bash, context management, and audit mirror; use with MATCH status from `_REFERENCES.md`. — reconciled under D-APP-38 |

## Verification

| Requirement | Verification approach |
|---|---|
| DEL-06-05-REQ-001 through REQ-004 | Unit or integration tests assert `Bash` is absent or denied by default, in `readOnly`, and in `dontAsk`; tests prove `allowedTools` cannot bypass denial. |
| DEL-06-05-REQ-005 | Spawn-suppression test instruments the command runner and asserts denied Bash requests never create a process. |
| DEL-06-05-REQ-006 | Timeout preflight tests assert no allowed Bash request can execute without an explicit timeout policy. Numeric timeout fixtures remain TBD. |
| DEL-06-05-REQ-007 | Capture tests run a controlled command that writes separately to stdout and stderr and assert separate capture channels. |
| DEL-06-05-REQ-008, REQ-009 | Tool-result budget tests assert large output is stored as an artifact and chat/event payloads contain preview plus safe artifact metadata. |
| DEL-06-05-REQ-010 | Interrupt tests assert active Bash can be cancelled or interrupted when supported; fallback tests assert unsupported interruption persists the actual terminal failure, cancellation, or residual-risk outcome. |
| DEL-06-05-REQ-011 | Runtime event tests assert permission/start/completed/failed or interrupted evidence is written to Chirality-owned event records. |
| DEL-06-05-REQ-012, REQ-013 | Hook/path tests assert hook failure and path-policy denial block Bash execution or filesystem mutation. |
| DEL-06-05-REQ-014 | Contract tests assert public event/permission schemas do not become SDK-shaped except for safe adapter metadata. |
| DEL-06-05-REQ-015 | Traceability check verifies test names or metadata cite DEL-06-05 and SOW-062; concrete test names, fixtures, and harness paths remain TBD until implementation planning assigns them. |
| DEL-06-05-REQ-016 | Preflight-contract review verifies command metadata fields and network posture checks are either implemented from an accepted contract or explicitly deferred with cited ownership. |

## Documentation

Required implementation evidence:

- Bash governance policy or options-builder slice showing default denial and explicit enablement rules.
- Timeout/capture policy with explicit default and override constraints once human-approved or source-defined.
- Output metadata schema or fixture for stdout/stderr preview and artifact storage, including PRD-derived artifact metadata fields only while the REF-006 MATCH status remains visible. (reconciled under D-APP-38).
- Denied-never-spawns test evidence.
- Timeout/capture and interruption test evidence.
- Hook/path interface evidence showing composition with DEL-06-04 and DEL-06-06 once those interfaces are accepted.
- Residual-risk note for `docs/PRD.md` MATCH under the reconciled D-APP-38 source state. (reconciled under D-APP-38).

## Traceability

| Source item | Covered by |
|---|---|
| SOW-062 Bash denied by default and governed when enabled | DEL-06-05-REQ-001 through REQ-015 |
| OBJ-005 Runtime tool execution governance | DEL-06-05-REQ-001 through REQ-014 |
| K-BASH-1 Bash default denial and enablement prerequisites | DEL-06-05-REQ-001, REQ-006 through REQ-011, REQ-015 |
| FR-100 Bash denied by default, capture, timeout, storage, interrupt | DEL-06-05-REQ-001, REQ-005 through REQ-010 |
