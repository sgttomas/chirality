# Assessment INSP-03: DEL-04-04 PersonaComposer from Instruction Root

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-04-04 |
| Package | PKG-04 SDK Adapter, Prompt, Provider, and Settings |
| Date | 2026-06-20 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `ce0ab70933c6cc32f9eea62a563e512fc738a575` |
| Spec source | `Specification.md` lines 5-74 |

## Scope

DEL-04-04 replaces stub prompt behavior with source-grounded prompt composition from the resolved instruction root, selected persona, working-root policy, mode policy, permitted tool surface, and professional-boundary reminders.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| PC-REQ-001 | PASS | `frontend/src/lib/harness/instruction-root.ts` lines 6-103; `frontend/src/lib/harness/persona-manager.ts` lines 210-220; `frontend/src/__tests__/lib/harness-instruction-root.test.ts` lines 47-71. Focused validation passed. | The composer validates required instruction-root resources before reading persona/governance content. |
| PC-REQ-002 | PASS | `frontend/src/lib/harness/persona-manager.ts` lines 81-112 and 210-257; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 74-155. Focused validation passed. | Composer reads from the instruction root and has no write path to it. |
| PC-REQ-003 | PASS | `frontend/src/lib/harness/persona-manager.ts` lines 115-123 and 225-241; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 74-93. Focused validation passed. | Working-root policy is included as mutable workspace context, distinct from instruction-root governance. |
| PC-REQ-004 | PASS | `frontend/src/lib/harness/agent-instruction.ts` lines 20-22 and 208-243; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 124-137. Focused validation passed. | Persona files resolve to `agents/AGENT_<persona>.md`; missing personas produce typed failures. |
| PC-REQ-005 | PARTIAL | `frontend/src/lib/shell/persona-resolution.ts` lines 12-53; `frontend/src/__tests__/lib/persona-resolution.test.ts` lines 9-53; `frontend/src/lib/harness/agent-instruction.ts` lines 20-22. Focused validation passed. | Alias mapping is implemented in the shell resolver and can feed the composer, but the composer itself reads the provided persona string. |
| PC-REQ-006 | PASS | `frontend/src/lib/harness/persona-manager.ts` lines 97-189 and 225-241; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 74-93. Focused validation passed. | Prompt includes governance preface, selected persona, working-root boundary, mode policy, and tool posture. |
| PC-REQ-007 | PASS | `frontend/src/lib/harness/persona-manager.ts` lines 106-110; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 74-93. Focused validation passed. | Professional-boundary reminder is explicit and does not imply approval, issuance, certification, sealing, or validation. |
| PC-REQ-008 | PASS | `frontend/src/lib/harness/persona-manager.ts` lines 126-189; `frontend/src/lib/harness/sdk-options-builder.ts` lines 100-157; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 139-155. Focused validation passed. | Prompt text states posture while runtime enforcement remains in options, hooks, permission overlay, and tool descriptors. |
| PC-REQ-009 | PASS | `frontend/src/lib/harness/persona-manager.ts` lines 149-189; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 202-217; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 74-155. Focused validation passed. | SDK/tool details are prompt support and adapter metadata, not public contract definitions. |
| PC-REQ-010 | PARTIAL | `frontend/src/lib/harness/persona-manager.ts` lines 18, 149-189, and 243-285; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 95-122. Focused validation passed. | Fingerprints include composer-owned prompt inputs and visible tool-surface data; optional settings/MCP/subagent version handoff remains adjacent-slice input. |
| PC-REQ-011 | PASS | `frontend/src/lib/harness/options.ts` lines 71-85; `frontend/src/__tests__/lib/harness-options.test.ts` lines 241-264 and 290-312. Focused validation passed. | Unknown composition-adjacent runtime options warn and do not mutate resolved prompt behavior. |
| PC-REQ-012 | PASS | `frontend/src/lib/harness/persona-manager.ts` lines 115-123 and 225-257; `frontend/src/app/api/harness/session/boot/route.ts` lines 23-63; `frontend/src/__tests__/lib/persona-manager.test.ts` lines 74-155. Focused validation passed. | API keys, transcripts, drafts, caches, and local presets are not imported as prompt authority. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Persona alias ownership is split between shell resolution and composer lookup. | Low | `Specification.md` line 32; `frontend/src/lib/shell/persona-resolution.ts` lines 12-53. | Document the accepted delegation point so issuance does not require duplicate alias logic inside `PersonaComposer`. |
| Boot fingerprint optional inputs are only as complete as adjacent slices expose. | Medium | `Specification.md` line 37; `frontend/src/lib/harness/persona-manager.ts` lines 149-189 and 243-285. | Treat settings-source, MCP version, and subagent-policy inputs as adjacent-slice handoff evidence. |
| Instruction-root packaging conformance remains outside this deliverable. | Low | `Specification.md` lines 20 and 74. | Carry packaging/instruction-root integrity closure into DEL-08-01/DEL-09-04. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for REF-006, adjacent options/tool/fingerprint inputs, and instruction-root packaging/integrity evidence.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add a short integration note naming shell persona resolution as the alias-owner before composer lookup. | doc | S | FIT | Preserve existing alias tests. |
| Cross-link boot fingerprint optional inputs to DEL-04-02, PKG-06, and PKG-08 handoff evidence. | reconcile | S | FIT | Complete the relevant assessment waves. |
| Keep instruction-root integrity/package verification in DEL-08-01/DEL-09-04 rather than expanding this slice. | doc | S | FIT | Future packaging wave. |

## Issuance-Gate-Process Observations

DEL-04-04 has strong implementation evidence. Issuance should require only boundary/ownership reconciliation for aliases and optional fingerprint inputs, not a composer rewrite.
