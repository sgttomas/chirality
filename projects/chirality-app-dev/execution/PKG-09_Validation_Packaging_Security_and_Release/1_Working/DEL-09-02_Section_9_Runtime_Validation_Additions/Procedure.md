# Procedure: DEL-09-02 Section 9 Runtime Validation Additions

## Purpose

Define the operational steps to produce and verify the Section 9 runtime validation additions for DEL-09-02 while preserving source-grounding, existing Section 8 behavior, and deliverable-local boundaries.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available in the deliverable folder.
- Authoritative source slices are available from `docs/PRD.md`, `docs/SPEC.md`, `docs/CONTRACT.md`, `docs/TYPES.md`, `docs/DIRECTIVE.md`, and the v3.2 software decomposition.
- Declared upstream dependencies are currently `TBD`; do not assume dependency edges until accepted extraction creates them.
- PRD hash mismatch is recorded as a source warning only for this run.
- Responsible party remains `TBD`.

## Steps

1. Confirm the Section 8 baseline remains visible in the validation suite: server reachable, session CRUD, boot error taxonomy, smoke stream ordering, session persistence/resume, permission markers, interrupt behavior, and SDK-native stream handling. Source: `docs/PRD.md` Section 12.3; `docs/SPEC.md` Section 19.2.
2. Add or update the Section 9 validation registry with each source-defined ID from PRD Section 12.4 and SPEC Section 19.3.
3. For each Section 9 ID, attach source references and a status. If the runtime phase is not implemented, use a pending or blocked status rather than inventing a passing test. Exact status enum is TBD.
4. Implement or wire runner checks for IDs whose runtime surfaces exist:
   - `section9.runtime_engine_contract`: engine conformance and product-owned boundary checks.
   - `section9.sdk_turn_engine_event_log`, `section9.sdk_message_mapper`, `section9.session_event_replay`: event schema, mapper, append/replay, and transcript non-authority checks.
   - `section9.settingsources_isolation`: shipped settings-source posture check.
   - `section9.permission_overlay_deny_first`: deny-first and `allowedTools` non-boundary checks.
   - `section9.tool_runtime_read_file` and `section9.chirality_mcp_status_dependencies`: tool exposure and MCP wrapper checks.
   - `section9.path_containment_hook` and `section9.instruction_root_protection_hook`: hook/path checks.
   - `section9.tool_result_budget`: inline/preview/artifact/redaction check.
   - `section9.context_compaction_boundary`: compaction mirror check.
   - `section9.subagent_governance_hook`: fail-closed subagent governance check.
5. Gate `section9.domain_profile_validation` until a governed domain-profile amendment enters scope.
6. Update the harness runner so Section 9 IDs are executed or reported consistently with the existing premerge validation flow. Exact command and file path are TBD.
7. Update the summary schema or fixture so Section 9 results are distinguishable from Section 8 results and usable for release readiness review. Exact schema path is TBD.
8. Run the relevant local validation command once implementation exists. Current command is TBD; do not claim execution before a command is identified and run.
9. Record any unresolved source mismatch, pending ID, or missing implementation surface in the summary output and release notes/checklist.

## Verification

| Check | Expected Evidence |
|---|---|
| ID completeness | Every ID listed in PRD Section 12.4 / SPEC Section 19.3 appears in the Section 9 registry or summary. |
| Section 8 preservation | Existing Section 8 checks remain present and runnable. |
| Engine contract | Engine conformance test or manifest proves Chirality-owned runtime boundary remains separate from SDK APIs. |
| Event schema and replay | JSONL event test proves append order, unique IDs, redaction, artifact references, malformed-tail tolerance, and terminal outcomes. |
| Settings isolation | Test or runtime metadata proves shipped `settingSources` posture does not load ambient user/local settings. |
| Permission overlay | Denial tests prove deny overrides allow and `allowedTools` alone is not treated as a boundary. |
| MCP and hooks | MCP wrapper and hook tests prove policy, path, redaction, event logging, and fail-closed behavior. |
| Compaction and subagents | Tests prove `context.compacted` and governed child-run lifecycle events are persisted when those SDK callbacks are available. |
| Summary schema | Stable summary artifact includes Section 9 ID status and evidence references. |

## Records

- Section 9 validation ID registry or manifest.
- Harness runner update.
- Summary schema/fixture update.
- Validation output or premerge summary artifact.
- Human-ruling log for PRD hash warning and domain-profile validation gating.

