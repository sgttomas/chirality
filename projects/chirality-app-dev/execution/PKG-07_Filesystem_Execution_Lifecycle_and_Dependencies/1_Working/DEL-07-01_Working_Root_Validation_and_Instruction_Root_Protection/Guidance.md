# Guidance: DEL-07-01 Working Root Validation and Instruction Root Protection

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

DEL-07-01 exists to make the filesystem boundary trustworthy before agents, tools, MCP wrappers, hooks, or SDK-mediated actions operate on project files. It protects two project-critical distinctions:

- The instruction root is release-managed and read-only during ordinary project execution.
- The working root is the mutable project filesystem where project truth, deliverables, sessions, and tool artifacts live.

Sources: `_CONTEXT.md` `Deliverable Scope`; `docs/DIRECTIVE.md` Sections 2.7-2.9; `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Validate before use | Treat working-root validation as a gate before file tree, scan, chat session, scaffold, and contract APIs consume the root. | `docs/PRD.md` Section 7.1 |
| Deny beats allow | A path-containment or instruction-root denial must override permissive SDK modes, user prompts, persona text, or tool availability. | `docs/PRD.md` Section 3; `docs/CONTRACT.md` K-PERM-1 |
| Code owns the boundary | Prompts may explain safety posture, but enforcement belongs in runtime code, path helpers, hooks, and policy checks. | `docs/DIRECTIVE.md` Section 2.9; `docs/PRD.md` Section 3 |
| Separate read policy from write policy | Instruction-root reads may be governed by explicit policy, but ordinary writes under the instruction root are blocked. | `docs/PRD.md` FR-051; `docs/SPEC.md` Section 1.1 |
| Use project-root containment consistently | Tool and write paths should pass through one normalized containment model rather than ad hoc string checks. | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050 |
| Fail closed | Hook failures in enforcement paths should deny the action and record triage rather than continue silently. | `docs/CONTRACT.md` K-HOOK-1; `docs/PRD.md` FR-095 |

## Considerations

- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- The decomposition assigns SOW-002 and SOW-027 to DEL-07-01. SOW-002 covers working-root selection and validation; SOW-027 covers path containment and instruction-root protection.
- `DEL-06-04` also references path hooks for write/edit execution. ASSUMPTION: DEL-07-01 should define reusable root/path policy expectations and tests, while DEL-06-04 applies them in the broader write/edit surface. This is an inferred coordination note from the decomposition, not an accepted dependency edge.
- `_DEPENDENCIES.md` currently has no accepted upstream or downstream edges. Do not treat neighboring deliverables as formal dependencies until dependency extraction accepts them.
- The relationship to `DEL-06-04` remains a coordination note, not an accepted dependency edge, until the dependency register is updated or a human ruling says otherwise.
- The instruction root may be supplied through `CHIRALITY_INSTRUCTION_ROOT` during development and packaged under app resources in builds. Tests should cover both source-tree and packaged-root resolution if implementation supports both paths.
- Initial symlink write rejection is explicit. Any future relaxation requires a governed amendment and tests.

## Trade-offs

| Choice | Benefit | Risk or Cost | Preferred Posture |
|---|---|---|---|
| Central path policy helper | Consistent containment behavior across APIs, hooks, and tools. | Requires careful normalization and test coverage. | Prefer central helper with fixture coverage. |
| Enforcement in hooks and wrappers | Catches SDK built-ins and MCP/tool actions at runtime. | Hook failure paths must be tested and observable. | Required for reliance-boundary confidence. |
| Strict instruction-root write block | Protects release-managed governance assets from ordinary project execution. | Release/governance updates need a separate controlled pathway. | Required by CONTRACT and SPEC. |
| Reject symlink writes initially | Reduces path escape risk. | Blocks some advanced local workflows. | Required until governed relaxation exists. |
| REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | Allows Phase 2.2 drafting to proceed per brief. | Requirement rows may need revalidation when source state is resolved. | Record warning and cite source locations. — reconciled under D-APP-38 |

## Examples

| Scenario | Expected Result | Source |
|---|---|---|
| User selects `../project` or another relative path as working root. | Reject as invalid because relative paths are not accepted. | `docs/PRD.md` Section 7.1 |
| User selects a missing path or a file path. | Reject because the working root must exist and be a directory. | `docs/SPEC.md` Section 1.2 |
| User selects a directory nested inside the instruction root. | Reject because the working root must not be inside instruction root. | `docs/PRD.md` Section 7.1; `docs/CONTRACT.md` K-ROOT-1 |
| Tool attempts to write outside active project root using an absolute path. | Deny through path containment. | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050 |
| Tool attempts to write under instruction root while `bypass` is active in developer-local mode. | Deny because Chirality denies still apply. | `docs/TYPES.md` Section 8.2; `docs/PRD.md` permission mapping table |
| Tool attempts to write through a symlink target. | Deny under initial symlink write policy. | `docs/CONTRACT.md` K-PATH-3; `docs/SPEC.md` Section 15.2 |

## Source-State Warnings

| Warning ID | Source | Warning | Impacted Sections | Human Ruling |
|---|---|---|---|---|
| WARN-07-01-001 | `_REFERENCES.md` REF-006 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | Datasheet, Specification, Guidance, Procedure citations to `docs/PRD.md` | TBD — reconciled under D-APP-38 |

No direct source conflict was found among the accessible slices read for this draft.

## Human Rulings Needed

| ItemID | Ruling Needed | Current Posture |
|---|---|---|
| C-001 | Accept, correct, replace, or explicitly bypass the `docs/PRD.md` REF-006 hash status: MATCH before PRD-dependent rows are treated as stable closure evidence. | Source-state warning preserved; no human ruling invented. — reconciled under D-APP-38 |
| X-002 | Decide whether `DEL-06-04` remains only a coordination note or becomes an accepted dependency edge for write/edit hook enforcement. | No dependency edge accepted in `_DEPENDENCIES.md`; guidance keeps the relationship non-authoritative. |
| E-001 | If future symlink-write relaxation is proposed, identify the amendment reference and fixture evidence required for acceptance. | Initial symlink rejection remains required. |

## Pass 3 Semantic Lensing Notes

| ItemID | Guidance Disposition | Evidence |
|---|---|---|
| C-001 | surfaced as human ruling | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| X-002 | surfaced as human ruling | `Considerations` and `Human Rulings Needed` state that `DEL-06-04` is not an accepted dependency edge unless later accepted. |
| E-001 | already covered | `Considerations`, `Trade-offs`, `Examples`, and `Human Rulings Needed` keep symlink writes rejected until governed amendment and tests exist. |
