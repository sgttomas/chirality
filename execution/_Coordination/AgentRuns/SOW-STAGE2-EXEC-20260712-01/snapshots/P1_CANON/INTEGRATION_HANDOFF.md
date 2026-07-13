# P1_CANON Integration Handoff

Status: `SOURCE_BOUND — READY_FOR_RUN_SCOPED_PR`
Branch: `codex/sow-stage2-canon`
Integration base: `main@c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`
Activation commit: `2404f4e92b79c41e295a9bf3102407a0cd8b54db`
Activation parent: `c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`

## Exact activated canon

| Live path | SHA-256 |
|---|---|
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f` |
| `docs/TYPES.md` | `5094610af55d18982658ea589be95a60fac9c89ca611846fc57279b494c6d2ae` |
| `docs/SPEC.md` | `915c3b59d35afff5e489c9c387f09c17a6e4c307fd5e91cd81a8960d97a91e27` |

The three live paths compare byte-identical to the independently validated C1
candidate. Commit `2404f4e92b79c41e295a9bf3102407a0cd8b54db` changes no other
live canon path; its remaining paths are the authorized run and C1V evidence.

## Accepted upstreams and validation evidence

- accepted `P0_BASIS` / `B0_PASS` at the integration base above;
- D-GOV-16 ruling `7584718aa32b112e415331736d1a8e68c12ac176`;
- C1 exact-canon candidate and `VALIDATION_HANDOFF.md`;
- C1V `PASS` with zero findings at
  `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/C1V/`;
- C1G preintegration checks at
  `instances/CHANGE-C1G/PREINTEGRATION_CHECKS.md`.

The candidate, reproduction, C1V package, and this handoff are derivative
evidence. They cite and bind accepted upstreams but do not replace the live
canon, the D-GOV-16 ruling, project truth, consumer state, lifecycle truth, or
later phase snapshots.

## Closure, rollback, and next dependency

C1G source preparation is closed `PASS`. C1G integration is not closed until
the exact branch head containing this record is merged through its one
run-scoped PR and local `main`, `origin/main`, and remote main are resynchronized
and verified equal with the exact three hashes above.

If the permitted merge method creates a merge commit and rollback is required,
revert that merge without rewriting history using
`git revert -m 1 <merge-commit>` and route the resulting candidate through the
normal reviewed integration path. Do not reset, force-push, or delete evidence.

Rerun C1/C1V/C1G if the source SHA, base, candidate identity, three-path canon
set, required-check result, remote changed-path set, or PR readiness changes.
Current blockers and waivers: none. Consumer fan-in, conversion authority, H1,
and H2 remain parked. Only a successful C1G merge and synchronization releases
C2R and C2A preparation.
