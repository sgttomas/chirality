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
| REQ-08-01-004 | PARTIAL | `frontend/package.json` lines 24 and 71-88; `frontend/scripts/verify-instruction-root-integrity.mjs` lines 487-528. | Packaging and source/bundle integrity checks exist. The REF-006 warning is not resolved by the tool. |
| REQ-08-01-005 | PARTIAL | `frontend/scripts/verify-instruction-root-integrity.mjs` lines 269-344. | Source manifest comparison proves bundle completeness for known root/docs/agent files, but the package-specific source-completeness checklist remains implicit. |
| REQ-08-01-006 | PASS | `frontend/src/lib/harness/agent-roster.ts` lines 24-70; `frontend/scripts/verify-instruction-root-integrity.mjs` lines 239-251; `frontend/src/__tests__/lib/agent-roster.test.ts` lines 46-86. | Agent files are discovered by the `AGENT_*.md` naming contract and non-agent files are ignored. |
| REQ-08-01-007 | PARTIAL | `frontend/src/lib/harness/agent-instruction.ts` lines 180-206; `frontend/src/__tests__/lib/agent-roster.test.ts` lines 46-75. | `AGENT_TYPE` and `AGENT_CLASS` are parsed from body/table forms, but no full header/title conformance validator was found. |
| REQ-08-01-008 | PARTIAL | `frontend/src/lib/harness/agent-roster.ts` lines 36-70; `frontend/src/__tests__/lib/agent-roster.test.ts` lines 46-86. | Roster entries carry parsed type/class, but the full Agent Type table contract is not comprehensively validated. |
| REQ-08-01-009 | FAIL | `frontend/src/lib/harness/agent-instruction.ts` lines 64-123 and 180-206. | No validator was found for the required major-section markers named by the specification. |
| REQ-08-01-010 | PARTIAL | `frontend/src/lib/harness/persona-manager.ts` lines 115-123 and 149-189; `frontend/src/lib/harness/tool-path-policy.ts` lines 215-255. | Runtime prompts and path policy enforce write boundaries, but agent-instruction write-scope declarations are not parsed as a conformance field. |
| REQ-08-01-011 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 133-170; `frontend/src/__tests__/lib/harness-subagent-governance.test.ts` lines 211-313. | Type 2 candidate checks accept only `AGENT_TYPE: 2`; non-TASK class candidates warn rather than silently escalate. |
| REQ-08-01-012 | PASS | `frontend/src/lib/harness/subagent-governance.ts` lines 187-245; `frontend/src/lib/harness/subagent-bridge.ts` lines 64-75 and 100-128; `frontend/src/__tests__/lib/subagent-bridge.test.ts` lines 32-115. | Missing governance metadata fails closed, and executable child definitions have no inherited tools. |
| REQ-08-01-013 | PARTIAL | `frontend/scripts/verify-instruction-root-integrity.mjs` lines 300-344; `frontend/src/lib/harness/agent-roster.ts` lines 36-70. | Source registries are computed from files, but mutable narrative counts can still drift in project documents. |
| REQ-08-01-014 | PASS | `frontend/src/lib/harness/options.ts` lines 17-24 and 71-85; `frontend/src/__tests__/lib/harness-options.test.ts` lines 241-264. | Unknown runtime option keys warn and are ignored. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| G6: full agent conformance fixtures are missing. | Medium | `agent-instruction.ts` parses type/class, but no section/header/table conformance suite was found. | Add a small deterministic conformance validator and fixtures for missing type, wrong class, missing required sections, and unknown metadata. |
| Agent write-scope declarations are not machine-validated. | Medium | Runtime path policy exists, but `agent-instruction.ts` does not parse or validate write-scope declarations. | Either add the field to the validator or update the spec to treat write scope as runtime policy rather than instruction-file metadata. |
| REF-006 remains warning-limited. | Low | `_REFERENCES.md` records the PRD hash mismatch. | Close or waive the PRD hash warning before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. The dependency summary still records unresolved current instruction-root source-tree target evidence and the REF-006 warning.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add a deterministic agent-conformance validator focused on instruction-file shape, type/class, required sections, and unknown metadata warnings. | code/test | M | FIT | Current parser helpers in `agent-instruction.ts`. |
| Wire the validator into the instruction-root integrity script or a companion script and add fixtures for Type 2 subagent candidates. | code/test | M | FIT | Validator exists. |
| Decide whether write-scope declarations are instruction metadata or exclusively runtime policy, then align the spec and tests. | reconcile | S | FIT | Validator design decision. |

## Issuance-Gate-Process Observations

DEL-08-01 is not issuance-ready as a pure conformance deliverable because the most important runtime protections pass, but the conformance validator promised by the spec is only partially implemented.
