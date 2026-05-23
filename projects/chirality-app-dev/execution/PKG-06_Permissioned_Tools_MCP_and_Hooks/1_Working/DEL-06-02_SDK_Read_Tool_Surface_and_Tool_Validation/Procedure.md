# Procedure: DEL-06-02 SDK Read Tool Surface and Tool Validation

## Purpose

This procedure describes how to produce and verify the DEL-06-02 SDK read tool-surface resolver and validation evidence. It is written for the deliverable artifact, not as an end-user operation runbook.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted DEL-06-02 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
| Tool-surface vocabulary | Available in `docs/TYPES.md` Section 8 |
| Binding permission/tool/MCP invariants | Available in `docs/CONTRACT.md` Section 1.6 |
| SDK and MCP tool naming specification | Available in `docs/SPEC.md` Section 14 |
| Mode and hook context | Available in `docs/SPEC.md` Section 15 |
| Roadmap sequencing for R2/R3 | Available in `docs/PLAN.md`; `docs/PRD.md` is warning-qualified due to HASH_MISMATCH |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` lists no accepted upstream edges yet |
| Exact implementation file paths | TBD |
| Exact test fixture paths | TBD |

## Steps

1. Establish the accepted tool-name registry.
   - Include SDK built-in candidates from `docs/SPEC.md` Section 14.1: `Read`, `LS`, `Glob`, `Grep`, `Write`, `Edit`, and `Bash` where available.
   - Include accepted Chirality MCP names from `docs/SPEC.md` Section 14.2 and `docs/TYPES.md` Section 8.4.
   - Do not introduce aliases or remote/plugin tool names without an accepted source update.

2. Define the resolver input and output.
   - Input should include resolved runtime options, especially `opts.tools`, plus context needed for deterministic ordering and policy filtering.
   - Keep the exact interface shape TBD until the runtime owner assigns the object or function boundary carrying `opts.tools`, session, persona, mode, SDK version, MCP server set, and permission policy. (P3: F-001)
   - Output should identify SDK built-ins and Chirality MCP tools in the form required by SDK options/MCP configuration.
   - Keep SDK-specific values as adapter metadata, not public Chirality contract terms.

3. Validate requested names.
   - For each `opts.tools` entry, resolve against the accepted registry.
   - If a name is unknown, produce a structured validation error and stop before SDK request construction.
   - Keep the exact structured validation error type and fixture assertion shape TBD until the implementation contract is named. (P3: C-002)
   - Ensure unknown names are not present in emitted SDK options or model context.

4. Apply read-first sequencing.
   - Permit initial exposure of SDK read candidates (`Read`, `LS`, `Glob`, `Grep`) where available.
   - Permit initial exposure of Chirality read MCP tools such as status read, dependency read, scope scan, and scaffold preview/dry-run where supported by registry policy.
   - Exclude or deny `Write`, `Edit`, and `Bash` until later write/bash governance phases activate them.

5. Preserve permission policy boundaries.
   - Do not treat `allowedTools` alone as restriction.
   - Hand the resolved surface to deny-first permission policy, disallowed tools, hooks, `canUseTool`, and/or `dontAsk` posture as applicable.
   - Ensure implementation availability does not override policy filtering.

6. Normalize deterministic ordering.
   - Sort or otherwise canonicalize the final visible tool surface after validation and filtering.
   - Use stable inputs: session, persona, mode, option set, SDK version, MCP server set, and permission policy.
   - Record safe metadata or fingerprints when required by the runtime contract. Exact metadata path: TBD.

7. Add unknown-tool tests.
   - Verify unknown names produce structured validation errors.
   - Verify unknown names are absent from SDK options and model context.
   - Include at least one unknown SDK-like name and one unknown `mcp__chirality__*` name.

8. Add deterministic ordering fixtures.
   - Feed the same set of tools in varied input orders.
   - Assert stable normalized output for identical context.
   - Add fixture coverage for mixed SDK built-ins and Chirality MCP names.

9. Add read-first sequencing tests.
   - Verify read candidates resolve in the initial surface.
   - Verify write/edit/bash do not appear or are hard-denied in read-first/read-only posture.
   - Verify `allowedTools` cannot cause a denied or unsupported tool to execute.

10. Record residual gaps.
   - Keep exact implementation and fixture paths as `TBD` until assigned.
   - Record the `docs/PRD.md` HASH_MISMATCH as a source-state warning in implementation or review evidence.

## Verification

| Check | Expected result |
|---|---|
| Registry validation | Only registered SDK built-ins and accepted `mcp__chirality__*` names resolve. |
| Unknown-tool behavior | Unknown names produce structured validation errors and are not passed to the SDK. |
| Determinism | Same context and tool set produce stable output ordering and identifiers. |
| Read-first sequencing | Initial surface contains read tools only; write/edit/bash are excluded or hard-denied. |
| Permission boundary | `allowedTools` does not restrict by itself and cannot bypass deny policy. |
| Implementation-vs-exposure | SDK/tool implementation availability does not imply model exposure. |
| MCP parity | Chirality MCP names pass through the same surface and permission path as SDK built-ins. |
| PRD warning | PRD-derived details remain traceable to `_REFERENCES.md` HASH_MISMATCH until reconciled. |

## Records

- Tool resolver implementation path: TBD.
- SDK built-in and Chirality MCP registry path: TBD.
- Structured validation error contract: TBD. (P3: C-002)
- Unknown-tool test path: TBD. (P3: F-002)
- Deterministic ordering fixture path: TBD. (P3: F-002)
- Read-first sequencing test path: TBD. (P3: F-002)
- Safe metadata or boot-fingerprint path for SDK names, versions, and MCP identifiers: TBD. (P3: E-001)
- Trace package tying resolver, registry, error contract, fixtures, sequencing tests, and PRD warning note to implementation evidence: TBD. (P3: X-001)
- Review note for PRD HASH_MISMATCH: required until REF-006 source state is reconciled. (P3: A-001, D-002, E-002)
