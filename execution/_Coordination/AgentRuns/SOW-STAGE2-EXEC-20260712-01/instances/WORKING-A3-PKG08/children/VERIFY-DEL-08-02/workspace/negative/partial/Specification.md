# Specification: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Scope

This deliverable specifies the routing and persona-resolution contract needed to keep UI aliases, canonical agent names, matrix routes, and persona resolution consistent for Chirality App vNext.

In scope:

- Alias resolution from UI labels to canonical agent names.
- Canonical matrix row, column, and cell vocabulary.
- Row-based routing from the agent matrix to loop-persona intent or PIPELINE.
- Loop route-state preservation for selected agent, row, and column.
- Persona resolution to instruction-root `agents/AGENT_*.md` files.
- Tests and fixtures for alias resolution, matrix mapping, and route behavior.

Out of scope:

- General SDK adapter mechanics.
- Full prompt composition implementation owned by DEL-04-04, except for the persona-name contract shared with this deliverable.
- Pipeline category and task-scope dispatch owned by DEL-08-03, except for row-level `OPERATIVE -> PIPELINE` routing.
- Dependency extraction authoring; the existing `Dependencies.csv` and `_DEPENDENCIES.md` are consumed as current dependency evidence for this deliverable.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-08-02-REQ-001 | The UI alias resolver MUST map `HELP` to `HELP_HUMAN`. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 | Alias resolver unit test. |
| DEL-08-02-REQ-002 | The UI alias resolver MUST map `ORCHESTRATE` to `ORCHESTRATOR`. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 | Alias resolver unit test. |
| DEL-08-02-REQ-003 | The UI alias resolver MUST NOT map `AGGREGATE` to `AGGREGATION`; `AGGREGATION` is a Type 2 task agent and must not boot as a top-level loop persona. | D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` Type 2 vocabulary | Negative alias resolver unit test and matrix guard test. |
| DEL-08-02-REQ-004 | The UI alias resolver MUST NOT map `RECONCILING` to `RECONCILIATION`; the EVALUATIVE/REVIEWING matrix cell uses the Type 1 `RESEARCH` persona under the loop-first guard. | D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` matrix vocabulary | Negative alias resolver unit test and matrix guard test. |
| DEL-08-02-REQ-005 | The UI alias resolver MUST map `AGENTS` to `HELPS_HUMANS`. | `docs/TYPES.md` Section 3.4; `docs/PRD.md` FR-026 | Alias resolver unit test. |
| DEL-08-02-REQ-006 | PORTAL matrix fixtures MUST use rows `NORMATIVE`, `OPERATIVE`, and `EVALUATIVE`. | `docs/TYPES.md` Section 4.1; `docs/PRD.md` FR-007 | Matrix mapping test. |
| DEL-08-02-REQ-007 | PORTAL matrix fixtures MUST use columns `GUIDING`, `APPLYING`, `JUDGING`, and `REVIEWING`. | `docs/TYPES.md` Section 4.2; `docs/PRD.md` FR-007 | Matrix mapping test. |
| DEL-08-02-REQ-008 | NORMATIVE matrix cells MUST route to loop-persona intent for Type 0/1 personas in the mounted loop shell. | `docs/TYPES.md` Section 4.1; D-APP-28 loop-first routing; `docs/PRD.md` Section 7.2 and FR-008 | Route fixture test. |
| DEL-08-02-REQ-009 | EVALUATIVE matrix cells MUST route to loop-persona intent for Type 0/1 personas in the mounted loop shell. | `docs/TYPES.md` Section 4.1; D-APP-28 loop-first routing; `docs/PRD.md` Section 7.2 and FR-008 | Route fixture test. |
| DEL-08-02-REQ-010 | OPERATIVE matrix cells MUST route to PIPELINE. | `docs/TYPES.md` Section 4.1; `docs/PRD.md` Section 7.2 and FR-008 | Route fixture test. |
| DEL-08-02-REQ-011 | Loop-persona routing MUST preserve selected agent, row, and column context. | `docs/PRD.md` Section 7.4 and FR-009; D-APP-28 loop-first routing | Route-state test. |
| DEL-08-02-REQ-012 | Persona names MUST resolve to instruction files matching `agents/AGENT_*.md`. | `docs/PRD.md` FR-025; `docs/SPEC.md` Section 13.2 | Persona resolver test with existing and missing personas. |
| DEL-08-02-REQ-013 | Missing personas MUST return `PERSONA_NOT_FOUND`. | `docs/PRD.md` FR-025 | Negative persona resolver test. |
| DEL-08-02-REQ-014 | Request/session persona fallback MUST be deterministic: empty or missing UI persona resolves to `WORKING_ITEMS`, while unknown non-empty persona labels pass through normalized and fail later at instruction-file resolution if no matching `AGENT_*.md` exists. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-023; current loop-first shell contract | Runtime option fallback and negative persona resolver tests. |
| DEL-08-02-REQ-015 | Unknown runtime option keys MUST warn without silently mutating behavior. | `docs/SPEC.md` Section 13.1; `docs/PRD.md` FR-024 | Runtime option warning test. |
| DEL-08-02-REQ-016 | Unsupported or disabled matrix/pipeline variants MUST remain visible as coming soon rather than silently disappearing. | `docs/PRD.md` Section 7.2; `docs/PRD.md` FR-011 | UI fixture or interaction test. |
| DEL-08-02-REQ-017 | The implementation MUST NOT invent additional alias mappings, matrix rows, columns, or canonical persona names without a governed source update. | `docs/CONTRACT.md` K-INVENT-1; `docs/TYPES.md` Sections 3.4 and 4 | Fixture completeness and snapshot tests. |

## Standards

| Standard / Contract | Applicability | Status |
|---|---|---|
| `docs/TYPES.md` Sections 3.4 and 4 | Authoritative vocabulary for alias and matrix terms. | Accessible; hash match. |
| `docs/PRD.md` Sections 7.2, 7.4, 8.2, and 8.4 | Product requirements for matrix routing, workbench context, and persona resolution. | Current under the D-APP-38 authority corpus. |
| `docs/SPEC.md` Section 13 | Runtime option fallback and persona composer contract. | Accessible; hash match. |
| `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 | Governance constraints for unsupported facts and source conflicts. | Accessible; hash match. |
| `docs/DIRECTIVE.md` Sections 2.8 and 4.1 | Product-owned persona/system-prompt and matrix navigation scope. | Accessible; hash match. |

## Verification

Required verification artifacts:

- Alias resolver tests covering the active sourced aliases, removed Type-2 alias negative cases, and unknown alias pass-through behavior.
- Matrix mapping tests covering all canonical rows, columns, and row destinations.
- Route fixtures proving NORMATIVE/EVALUATIVE cells produce loop-persona intent and OPERATIVE cells open PIPELINE.
- Loop route-state tests proving selected agent, row, and column survive route-state or query-param handling.
- Persona resolver tests proving canonical `AGENT_*.md` lookup and `PERSONA_NOT_FOUND` for missing personas.
- Runtime fallback tests proving default persona behavior and warning behavior for unknown option keys where this deliverable touches shared runtime option handling.

Pass 3 evidence slots:

| ItemID | Disposition | Required evidence |
|---|---|---|
| B-001 | Resolved by current implementation contract. Unknown UI alias labels pass through normalized and then fail at instruction-file resolution if no matching persona exists. | `frontend/src/__tests__/lib/persona-resolution.test.ts`. |
| F-002 | Incorporated as audit evidence naming requirement. Verification records must identify concrete result files or command outputs for alias, matrix, route, workbench-context, persona, fallback, unknown-key, and unsupported-option checks. | Implementation-local test report paths or command output locations. |
| D-001 | Resolved by loop-first launch state. Matrix launches preserve selected agent, row, and column in the mounted shell route-state contract. | `frontend/src/__tests__/lib/agent-matrix-launch.test.ts`. |
| X-001 | Incorporated from current dependency evidence. `Dependencies.csv` and `_DEPENDENCIES.md` now provide extracted rows; declared human upstream/downstream edges remain TBD. | Dependency register validation and any later human edge ruling. |
| C-001 | Resolved by D-APP-38. PRD-backed requirements are current under authority corpus v2 and remain separate from implementation proof. | `_REFERENCES.md` REF-006 records MATCH. |

## Documentation

This deliverable should produce or update:

- Alias resolver tests.
- Route fixtures.
- Matrix mapping tests.
- Any implementation-local notes needed to explain route-state keys if they change from the current loop-first launch contract.
- Concrete verification evidence paths or command outputs for the checks listed in the Pass 3 evidence slots.

Exact implementation file paths are TBD until the owning implementation slice selects or confirms the frontend/runtime module locations.
