# Procedure: DEL-08-01 Instruction Root Packaging and Agent Conformance

## Purpose

Define the operational procedure to produce and verify the DEL-08-01 test-suite artifacts: agent conformance validator, integrity fixtures, and source-completeness checklist.

## Prerequisites

- Accepted deliverable context in `_CONTEXT.md`.
- Accessible authoritative references from `_REFERENCES.md`.
- Decomposition reference: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Current instruction-root source tree containing the candidate root assets and `agents/AGENT_*.md` files.
- Test framework, validator command, and fixture directory: TBD.
- Declared upstream/downstream lists: TBD. The extracted dependency register currently records upstream source prerequisites and no populated downstream handoff edges; do not invent deliverable edges from boundary references alone. Source: `_DEPENDENCIES.md`.

## Steps

1. Establish the accepted source basis.
   - Read `_REFERENCES.md`.
   - Record matching sources and source warnings.
   - Mark `docs/PRD.md` as `HASH_MISMATCH` warning context until reconciled.

2. Build the instruction-root asset manifest.
   - Start from `docs/SPEC.md` section 1.1 required entries.
   - Add PRD FR-058 and KG-001 entries as warning-labeled candidates because REF-006 is hash-mismatched.
   - Record each asset as present, missing, not required by active policy, or TBD.

3. Define agent-instruction conformance checks.
   - Check filename convention `AGENT_*.md`.
   - Check required header: `[[DOC:AGENT_INSTRUCTIONS]]`, title, and `AGENT_TYPE`.
   - Check Agent Type table rows: `AGENT_TYPE`, `AGENT_CLASS`, `INTERACTION_SURFACE`, `WRITE_SCOPE`, `BLOCKING`, and `PRIMARY_OUTPUTS`.
   - Check required section-marker pairs for `PROTOCOL`, `SPEC`, `STRUCTURE`, and `RATIONALE` when applicable.
   - Warn on unknown runtime metadata option keys rather than mutating behavior.

4. Define Type 2 and subagent governance fixture checks.
   - Identify Type 2 candidates by `AGENT_TYPE: 2`.
   - Prefer `AGENT_CLASS: TASK` for Type 2 candidates.
   - Deny non-Type-2 or non-allowlisted delegation fixtures.
   - Deny subagent requests without sealed context, approved pipeline state, approval reference, and restricted child tool/cwd configuration.

5. Implement or update validator and fixtures.
   - Validator path: TBD.
   - Fixture path: TBD.
   - Test framework: TBD.
   - CI or local command: TBD.
   - Pass/fail artifact directory: TBD.
   - Record the selected path, framework, command, fixture directory, and artifact directory before treating verification as executable.
   - Keep outputs under the working root; do not write to the instruction root during ordinary test execution.

6. Run verification.
   - Execute the local validator/test command when available.
   - Confirm positive fixtures pass.
   - Confirm negative fixtures fail with actionable messages.
   - Confirm PRD-only checks are warning-labeled while the PRD hash mismatch remains unresolved.
   - Capture pass/fail evidence with the command, working tree or commit identifier when available, fixture summary, warning/failure counts, and output artifact location.

7. Record results.
   - Store validator output, source-completeness checklist, and fixture summary in the appropriate test artifact location: TBD.
   - Record unresolved source warnings and human-ruling needs.

## Verification

Completion checks:

- Four governing categories are covered: root assets, agent metadata, write scopes, and section markers.
- Required SPEC section 1.1 instruction-root assets are checked.
- Agent instruction conformance covers SPEC sections 7.1, 7.2, and 7.3.
- Type 2/subagent fixture expectations reflect TYPES and CONTRACT.
- PRD-derived checks carry the `HASH_MISMATCH` warning.
- No procedure step requires ordinary project execution to mutate the instruction root.
- `TBD` remains on implementation path, fixture path, command, upstream dependencies, and other items not established by source evidence.

## Records

Required records after implementation:

- Validator implementation decision record naming the framework, validator path, fixture path, local command, CI command or omission, and pass/fail artifact directory.
- Agent conformance validator output.
- Instruction-root integrity fixture summary.
- Source-completeness checklist.
- PRD hash mismatch warning record or human ruling.
- Local test command and result log.
- Any human-approved changes to required asset policy.
