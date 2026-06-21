# Assessment INSP-03: DEL-08-01 Instruction Root Packaging and Agent Conformance

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-08-01 |
| Package | PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `d92ef1253b37cd29423672acb146a9e9c91087d5` |
| Spec source | `Specification.md` lines 1-80 |

## Scope

DEL-08-01 covers packaging the instruction root as a read-only governance source, keeping it separate from the mutable working root, and validating agent instruction files enough to support persona and subagent dispatch without expanding capabilities.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ-08-01-001 | PASS | `frontend/src/lib/harness/tool-path-policy.ts` lines 234-248; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 167-258. | Governed writes under the instruction root are denied by path policy and hook tests. |
| REQ-08-01-002 | PASS | `frontend/src/lib/harness/session-manager.ts` lines 20-42; `frontend/src/lib/harness/persona-manager.ts` lines 115-123. | Session creation rejects project roots inside the instruction root, and prompt policy declares the project root as the mutable boundary. |
| REQ-08-01-003 | PASS | `frontend/scripts/verify-instruction-root-integrity.mjs` lines 9-22 and 165-207; `frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts` lines 116-162. | The integrity script validates the required root/docs entries and supports source-root resolution. |
| REQ-08-01-004 | PASS | `frontend/package.json` lines 24 and 71-88; `frontend/scripts/verify-instruction-root-integrity.mjs` lines 487-528; D-APP-38 REF-006 MATCH. | Packaging and source/bundle integrity checks exist, and the former REF-006 source-state warning is resolved by D-APP-38. |
| REQ-08-01-005 | PASS | `frontend/scripts/verify-instruction-root-integrity.mjs` `sourceCompleteness`; `frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts`. | The integrity summary now includes explicit SOW-073/OI-004 source-completeness rows and KG-001 remediation status for candidate source assets. |
| REQ-08-01-006 | PASS | `frontend/src/lib/harness/agent-roster.ts` lines 24-70; `frontend/scripts/verify-instruction-root-integrity.mjs` lines 239-251; `frontend/src/__tests__/lib/agent-roster.test.ts` lines 46-86. | Agent files are discovered by the `AGENT_*.md` naming contract and non-agent files are ignored. |
| REQ-08-01-007 | PASS | `frontend/src/lib/harness/agent-instruction.ts` `validateAgentInstructionConformance`; `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts`. | Header/title and `AGENT_TYPE` conformance now have positive and negative fixtures. |
| REQ-08-01-008 | PASS | `frontend/src/lib/harness/agent-instruction.ts` `validateAgentInstructionConformance`; `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts`. | The Agent Type table rows for `AGENT_TYPE`, `AGENT_CLASS`, `INTERACTION_SURFACE`, `WRITE_SCOPE`, `BLOCKING`, and `PRIMARY_OUTPUTS` are validated. |
| REQ-08-01-009 | PASS | `frontend/src/lib/harness/agent-instruction.ts` `validateInstructionSections`; `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts`. | Required `PROTOCOL`, `SPEC`, `STRUCTURE`, and `RATIONALE` marker pairs are validated. |
| REQ-08-01-010 | PASS | `frontend/src/lib/harness/agent-instruction.ts` `validateAgentInstructionConformance`; `frontend/src/lib/harness/persona-manager.ts` lines 115-123 and 149-189; `frontend/src/lib/harness/tool-path-policy.ts` lines 215-255. | Agent `WRITE_SCOPE` declarations are parsed and checked against the canonical vocabulary while runtime path policy remains the enforcement layer. |
| REQ-08-01-011 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 133-170; `frontend/src/__tests__/lib/harness-subagent-governance.test.ts` lines 211-313. | Type 2 candidate checks accept only `AGENT_TYPE: 2`; non-TASK class candidates warn rather than silently escalate. |
| REQ-08-01-012 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 187-245; `frontend/src/lib/harness/subagent-bridge.ts` lines 64-75 and 100-128; `frontend/src/__tests__/lib/subagent-bridge.test.ts` lines 32-115. | Missing governance metadata fails closed, and executable child definitions have no inherited tools. |
| REQ-08-01-013 | PASS | `frontend/scripts/verify-instruction-root-integrity.mjs` lines 300-344; `frontend/src/lib/harness/agent-roster.ts` lines 36-70; `frontend/src/lib/harness/agent-instruction.ts` conformance validator. | Source registries and instruction-file parsing are computed from files; narrative counts remain non-authoritative. |
| REQ-08-01-014 | PASS | `frontend/src/lib/harness/options.ts` lines 17-24 and 71-85; `frontend/src/__tests__/lib/harness-options.test.ts` lines 241-264. | Unknown runtime option keys warn and are ignored. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| G6: full agent conformance fixtures were missing. | Closed by ADQ-12 | `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts`. | Deterministic conformance validator and fixtures now cover missing type, invalid/wrong class, missing required sections, write scope, and unknown metadata warnings. |
| Agent write-scope declarations were not machine-validated. | Closed by ADQ-12 | `frontend/src/lib/harness/agent-instruction.ts` `validateAgentInstructionConformance`. | `WRITE_SCOPE` is parsed from the Agent Type table and checked against canonical vocabulary; runtime path policy remains enforcement. |
| REF-006 remained warning-limited. | Closed by D-APP-38 | `_REFERENCES.md` REF-006 MATCH. | Source-state proof is current under authority corpus v2. |
| SOW-073/OI-004 source-completeness checklist was implicit. | Closed by ADQ-12 | `verify-instruction-root-integrity.mjs` summary `sourceCompleteness`; integrity script tests. | Checklist rows now surface required instruction-root asset evidence and KG-001 remediation status. |

## Source-State Caveat

`docs/PRD.md` is current under the D-APP-38 authority corpus for this deliverable; `_REFERENCES.md` records REF-006 as MATCH. No semantic files were used or produced.

## Dependency Closure Note

This ADQ-12 supersession does not advance lifecycle state. The dependency summary still records unresolved current instruction-root source-tree target evidence, while the REF-006 warning is superseded by D-APP-38.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Optional: wire the conformance validator into a package instruction-root wrapper if future package policy wants a CLI artifact in addition to unit fixtures. | validation | S | FIT | `validateAgentInstructionConformance` exists. |

## Lifecycle-Gate-Process Observations

ADQ-12 closes the inspected conformance-validator residuals. Any later lifecycle transition still requires the applicable evidence profile.
