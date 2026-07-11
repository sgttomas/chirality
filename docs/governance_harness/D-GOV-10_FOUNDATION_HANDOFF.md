# Handoff State — D-GOV-10 Foundation

Status: PAUSED_FOR_OWNER_REVIEW
ClosureVerdict: FOUNDATION_DRAFT_COMPLETE__NOT_ACCEPTED_OR_INTEGRATED
Branch: `codex/agent-governance-redesign`
AcceptedUpstreamSnapshot: `052b3c2b2b33cb0fb167106d4d4417c0bf0d4d23`
DecisionBasis: `docs/governance_harness/_DECISIONS/D-GOV-10_workflow_component_architecture_normalization.md`

## Scope completed

The foundation tranche implements the ruled architectural direction as a
candidate review package:

1. Added `docs/WORKFLOW_COMPONENT_STANDARD.md` as the separated normative
   design surface.
2. Rewrote HELPS_HUMANS as a Type 1 applying/maintenance persona.
3. Replaced the stale workflow-component DBM with an explanatory, registry-
   subordinate design basis.
4. Updated direct framework, agent, skill, and tool references to the new
   standard.
5. Replaced the obsolete agent-audit rubric.
6. Added deterministic agent-instruction validation and tests.
7. Produced a disposition for all 38 live agents.

No Type 2 agent was migrated or retired. No project, domain, or deliverable
reconciliation state was changed.

## Artifact authority and derivative status

| Artifact | Class | Current status |
|---|---|---|
| D-GOV-10 record | Human-ruling transcription; SHA pending publication | RULED direction; `Ruling SHA` remains bind-at-publish TBD |
| `WORKFLOW_COMPONENT_STANDARD.md` | Candidate governed standard | Exact text awaits owner review/publication |
| `AGENT_HELPS_HUMANS.md` rewrite | Candidate live-instruction amendment | Structurally valid; not integrated |
| `AGENT_DISPOSITION_MATRIX.md` | Derivative analysis from live agent snapshot | Complete over upstream `052b3c2b2`; proposals do not retire components |
| Revised DBM | Candidate explanatory derivative | Aligned to current proposed architecture; not a registry |
| Validator and tests | Deterministic tool/evidence surface | Implemented and passing |

## Validation evidence

- `git diff --check`: PASS after trailing-whitespace/EOF correction.
- `python3 tools/validation/test_validate_agent_instructions.py`: 4 tests PASS.
- `python3 tools/validation/validate_agent_instructions.py`: 38 files, 0
  errors, 14 expected D-GOV-10 Type 2 requalification warnings.
- `python3 tools/validation/validate_skill_metadata.py`: 38 valid, 0 invalid.
- `python3 tools/validation/validate_path_anchors.py .`: PASS over 409 live
  path-anchor surfaces.
- practitioner-harness agent-registry and claim-language fixture tests: PASS.
- practitioner-harness `self-check`: completed; D-GOV-10 produces the expected
  `RULING_SHA_TBD` REVIEW with recognized bind-at-publish caveat. Other live
  project/domain findings predate and are outside this tranche.

These checks establish structural consistency within their observation
boundaries. They are not owner acceptance of the standard or dispositions.

## Owner review requested

Review the following candidate decisions:

1. Accept the standard/persona wording and HELPS_HUMANS Type 1 contract.
2. Accept the preliminary suite topology and migration waves.
3. Confirm the proposed merge targets:
   - SKILLMAKER, TOOLMAKER, CONTEXT_TRANSPOSE → HELPS_HUMANS;
   - EVALUATION → RECONCILIATION;
   - SCHEDULING → ORCHESTRATOR;
   - DECOMP_BASE conversational role → HELPS_HUMANS after extracting a
     decomposition standard.
4. Confirm that Wave 1 may begin with PREPARATION and the non-TASK audit agents
   once this foundation is accepted.

Implementation review points that may remain open without rejecting the
foundation:

- final SOFTWARE_DECOMP specialization posture;
- post-slim requalification of PDF2MD and DRAWING_EXTRACT;
- residual semantic skill need for DOMAIN_HYPERGRAPH;
- residual semantic skill need for EVALUATION_STRUCTURE_AUDIT; and
- compatibility duration for retired profile/agent names.

## Rerun and integration requirements

Before integration:

1. Incorporate owner review and record disposition.
2. Rebase onto main after the app-dev and piping reconciliation lanes reach
   stable handoffs.
3. Re-run all validation listed above plus any changed component tests.
4. Re-run registry/reference scans after conflict resolution.
5. Backfill D-GOV-10 publication SHA through the established decision-record
   flow.
6. Do not begin removals until replacement skills/tools and caller migrations
   are present in the same migration wave.

## Remaining blockers

- Exact candidate standard and matrix wording have not yet been owner-reviewed.
- Parallel reconciliation lanes have not yet supplied their final stable
  integration handoffs.
- Wave 1 replacement skills/tools do not yet exist.

## Next lawful owner

The owner reviews the foundation. After acceptance, HELPS_HUMANS may prepare
Wave 1 migration packages in the isolated branch. CHANGE handles eventual
rebase/integration and routine validated Git closeout; Git actions do not
constitute acceptance.
