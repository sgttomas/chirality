# Sealed Gate-5 execution brief — SCA-004 revision 1.3 application

Status: `DRAFT — REQUIRES SEPARATE OWNER AUTHORIZATION`

This brief is executable only after the owner separately (1) approves the
exact `Gate_5_Application_Append.diff` bytes and (2) authorizes Gate-5
execution against the published package identity. Its execution writes only
the seven live decomposition surfaces and the SCA-owned
`Gate_5_Application_Record.md` evidence authorized in that later act.

## Exact sequence

1. Reverify the seven live revision-1.2 SHA-256 identities:
   `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`,
   `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`,
   `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`,
   `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55`,
   `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84`,
   `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0`,
   and `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282`
   in the working-surface, deliverable, scope, objective,
   forward, reverse, and telemetry order used by
   `Gate_5_Applied_Preview.md`.
2. Reverify the seven R3-A-approved Gate-3 candidate SHA-256 identities in
   the same order:
   `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641`,
   `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`,
   `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc`,
   `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f`,
   `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f`,
   `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438`,
   and `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765`.
3. Require a fresh `validate_gate5_package.py` result of `PASS` with zero
   failures. Stop on any drift or validation failure.
4. Copy each of the seven exact files from `Gate_3_Candidate/` to its matching
   live path under `execution/_Decomposition/`.
5. From repository root, apply
   `Gate_5_Application_Append.diff` with
   `git apply --unidiff-zero`. The preceding check form must pass first.
6. Hash the seven live files and require exact equality with the applied SHA
   column in `Gate_5_Applied_Preview.md`. Stop on any mismatch.
7. Write `Gate_5_Application_Record.md` inside this SCA snapshot with every
   live before/after SHA, the owner append-approval reference, the owner
   Gate-5 authorization reference, validator result, and the Git-effect slot
   as `TBD` for later backfill. Never infer the Git effect.
8. Execute only the closure-validation lane of the owner-approved
   `Propagation_Plan.md` §6 items 1–6: reverify applied hashes; run the
   applied-state equivalent of the Gate-3 validator; run the post-application
   scoped `AUDIT_DECOMP` backcheck; prove no folder/SOW/status/dependency was
   created by the copy act; prove all ten holds remain
   `HELD_UNAVAILABLE`; record derivative currentness/staleness and downstream
   reruns.
9. Return the exact applied state to Ryan Tufts through HELP_HUMAN for Gate-5
   confirmation, as `Propagation_Plan.md` §6 item 7 requires.

## Validator reproduction boundary

`validate_gate3_candidate.py` is the protected Phase-0c validator. Its
`gate5_artifacts_absent` check is valid only in a Phase-0c layout. During this
Phase-0d package and any later Gate-5 preparation, run the original 98 checks
only in a clean scratch Phase-0c layout containing the approved candidate and
no Gate-5 draft artifacts. That clean-scratch run must return 98/98 and must
not write the protected live `Gate_3_Validation.json`.

For the applied preview or live applied state, use the applied-state
equivalent implemented by `validate_gate5_package.py`: the same 98 checks
with current-status assertions inverted and the two inventoried status-only
scope-ledger Notes cells admitted. Mapping, trace, count, basis, containment,
and other structural checks remain unchanged.

## Explicit exclusions

This brief performs no PREPARATION INIT and writes no `_LATEST.md`,
`_STATUS.md`, SOW, `_CONTEXT.md`, `_DEPENDENCIES.md`, estimate, schedule,
work graph, dependency-closure audit snapshot, Task Management register,
tool, runtime, project, export, pin, or App surface. Those remain later acts
under the approved propagation plan and their owning authority. It lifts no
hold. Pointer treatment requires its own accepted authority.

Gate 5 has not been executed by creation of this brief.
