# HELPS-C1 Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `HELPS_HUMANS` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Dependency: accepted `P0_BASIS` / `B0_PASS`

## Objective

Prepare the exact D-GOV-16 successor-canon candidate and evidence only. Copy
the ruled successor standard exactly and apply only the ruled zero-context
TYPES and SPEC patches to isolated copies. Do not modify live `docs/`, any
consumer, project, deliverable, lifecycle, Git ref, branch, commit, remote, or
receipt.

## Accepted basis

- `main@c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`.
- P0 handoff:
  `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/P0_BASIS/HANDOFF_STATE.md`.
- D-GOV-16 ruling publication:
  `7584718aa32b112e415331736d1a8e68c12ac176`.
- Ruled standard source and SHA-256:
  `docs/governance_harness/_PROPOSALS/D-GOV-16/DELIVERABLE_SCOPE_OF_WORK_STANDARD.proposed.md` /
  `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f`.
- Ruled TYPES patch and SHA-256:
  `docs/governance_harness/_PROPOSALS/D-GOV-16/TYPES.proposed.patch` /
  `9614166c7db8340532d838768be2de52567862757fe0d5add3d3a90edea9d4b4`.
- Ruled SPEC patch and SHA-256:
  `docs/governance_harness/_PROPOSALS/D-GOV-16/SPEC.proposed.patch` /
  `543200af8a617e2f5673db110eef2b0a5cf742c54e70ccda8bce0cad870d4b2e`.

Read root `AGENTS.md`, `agents/AGENT_HELPS_HUMANS.md`, D-GOV-16, P0 basis,
the accepted plan C1 contract, the three live canon files, and the three ruled
proposal artifacts.

## Write scope

Writes are exclusively:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P1_CANON/docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P1_CANON/docs/TYPES.md`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P1_CANON/docs/SPEC.md`;
- candidate-local `MANIFEST.tsv`, `PATCH_APPLICATION.md`, and `HANDOFF_STATE.md`;
- this instance's `RETURN.md` and `STATUS.json`.

Use `apply_patch` for file edits. The candidate directory is an isolated
derivative staging workspace, not accepted canon and not a Git integration
lane. Do not write any other path or delegate.

## Method and checks

1. Recheck P0 basis and the three ruled artifact hashes.
2. Record live before hashes for the three canon files.
3. Create candidate copies of live TYPES and SPEC, then apply only the ruled
   patches to those copies with exact zero-context semantics. Copy the ruled
   successor-standard bytes exactly to the candidate standard target.
4. Verify the candidate standard is byte-identical to the ruled source; verify
   candidate TYPES and SPEC are exactly the results of applying their ruled
   patches to the live basis; rerun patch preflight against live sources.
5. Record candidate hashes, source/patch identities, exact changed paths, and
   a no-interpretation/no-extra-path statement.
6. Confirm live canon hashes remain equal to their recorded before hashes and
   tracked project/canon Git state is unchanged.

Return `PASS`, `PARTIAL`, `BLOCKED`, or `DECISION_REQUIRED`. A mismatch,
context failure, extra path, normative ambiguity, or need to alter ruled bytes
blocks C1V. The candidate handoff must name accepted upstreams, derivative
status, closure verdict, reruns, blockers, and next owner `EVALUATION` only if
PASS.
