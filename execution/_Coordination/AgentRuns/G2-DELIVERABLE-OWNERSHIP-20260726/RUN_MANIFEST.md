# Run Manifest — G2-DELIVERABLE-OWNERSHIP-20260726

## Identity

- Parent: `HELP_HUMAN` (Agent 0)
- Manager: `HELPS_HUMANS` (Agent 1)
- Specialist: one read-only ephemeral Agent 2 adversarial test-design reviewer
- Engine/provider/model (manager): Codex / OpenAI / GPT-5
- Engine/provider/model (specialist): Codex / OpenAI / GPT-5 (inherited)
- Accepted basis: `2db2c712825af13d6b5425c34d31ff9daf470c89`
- Worktree: `/Users/ryan/dev/chirality-g2-deliverable-validator`
- Branch: `codex/g2-deliverable-ownership-validation`

## Owner authorization

Owner direction, in-session 2026-07-26, authorizes a bounded
HELPS_HUMANS/M2 correction to G2 so `kind: deliverable` entries are validated
against their actual nested tree, owning package, and accepted deliverable
register. It requires positive and negative deterministic tests, including a
foreign-tree BLOCK and proof that package behavior is unchanged. It prohibits
all other validator, schema, ownership-policy, Project Setup, product,
decomposition, runtime, and Git changes in this implementation act.

The verbatim direction is recorded in
`docs/governance_harness/tranche_manifests/G2-DELIVERABLE-OWNERSHIP-20260726.yaml`.

## Work graph

1. Manager reads the governing and live tool surfaces.
2. Read-only specialist adversarially reviews the proposed semantics and test
   matrix; it has no write targets and does not delegate.
3. Manager implements the bounded deterministic correction in the two
   authorized G2 files.
4. Manager validates focused behavior, manifest schema, diff containment, and
   the blocked Project Setup candidate.
5. Manager emits the return, validation record, and handoff for Agent 0 Git
   closeout.

There is one writer: HELPS_HUMANS. The specialist is read-only.

## Authorized writes

- `tools/validation/validate_root_surface_ownership.py`
- `tools/validation/test_validate_root_surface_ownership.py`
- `docs/governance_harness/tranche_manifests/G2-DELIVERABLE-OWNERSHIP-20260726.yaml`
- `execution/_Coordination/AgentRuns/G2-DELIVERABLE-OWNERSHIP-20260726/**`

## Artifact classes

- Tool and tests: candidate instruction-surface change under M2.
- Tranche manifest: candidate governed record of the M2/G4 gate.
- Run records: factual execution evidence and handoff, not authority.
