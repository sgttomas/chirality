# N1 return — SCA-004 Gate-5 second attempt executed

Status: `PASS — EXECUTED_AWAITING_OWNER_GATE_5_CONFIRMATION`

Role evidence: bounded ephemeral Agent 2; role not mechanically enforced;
governed evidence instruction-asserted. Delegation was not used.

## Result

Stage A passed its exact gate after one validator-only repair: R3-A
intermediate identities 7/7, R4-A final identities 7/7, and applied validator
PASS 65/65 with zero failures. The seven governed live files remained at
revision 1.2 throughout rehearsal.

Stage B then executed once. Seven explicit `/bin/cp` commands reproduced the
R3-A candidate identities 7/7 at the live paths. The approved
`Gate_5_Application_Append.diff` passed
`git apply --unidiff-zero --check`; exactly one
`git apply --unidiff-zero` produced the R4-A applied identities 7/7. No patch
editing, editor tool, `apply_patch`, Python rewrite, or re-expression of an
approved diff wrote a live decomposition file.

The closure lane passed. The live applied validator is PASS 65/65, the scoped
post-Gate5 AUDIT_DECOMP backcheck matches the expected topology with zero
mapping/trace defects, all ten holds remain `HELD_UNAVAILABLE`, and no folder,
SOW, `_STATUS.md`, or `_DEPENDENCIES.md` was created or changed.

## Pre-write fence

- Branch and basis: `codex/root-v3-phase0f-2026-08-23` at
  `origin/main@119e08647afdb380704ff660fb32d714d7bd1dad`.
- PR #630 merge `3bb3d50550b9fbdbdea67f41fa2ed108024cb43b` is an ancestor.
- Every Phase-0f basis-gate SHA matched.
- R5 steer SHA-256:
  `3c94f224578ee8187cfd8d6dda6e005d56b711a303994d26c1fef6c56bde7089`.
- R5 ruling-record SHA-256:
  `1f0a3358602fdfb4dff70607ad631130db55dcfd62d71a6fe7a3a13e18f0f42a`.
- Fresh pre-application `validate_gate5_package.py`: PASS 64/64, zero
  failures; `Gate_5_Validation.json` remained SHA-256
  `4831fb2757bfcdeb2faa0dff51a15d4f04ec68d4c9716928a36f1ea8844df966`.
- `/bin/cp`, `shasum`, and `git apply` were available before substantive
  writes.

## Stage A — rehearsal gate

Durable record: `Gate_5_Rehearsal_Record.md` SHA-256
`ea5d90e88ebc7528f758664bf354f815deb8c50b638276ead19a5f49f9f92532`.

| Surface | R3-A intermediate SHA-256 | R4-A final SHA-256 |
|---|---|---|
| Working surface | `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641` | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| Scope ledger | `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc` | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| Coverage telemetry | `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765` | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` |

The first rehearsal validator execution found one defect in the new
Stage-A artifact: it treated intentionally empty direct objective cells as
unmapped IN rows. Unlimited Stage-A repair narrowed the check to missing
package/deliverable allocation, matching the governed meaning. No rehearsal
decomposition byte changed during the repair. The repaired validator passed
65/65 with zero failures. Repair cycle 1 added the omitted exact command
transcript: the initial 64/65 failure; the relative-path `/bin/cp` no-op and
reproduced 64/65 failure; then the absolute governed-source `/bin/cp`, second
effective validator invocation, and 65/65 PASS. The scratch worktree was
removed cleanly.

## Stage B — live before → after

Stage-B attempt count: `1` (successful; no retry).

| Surface | Revision-1.2 before SHA-256 | Applied revision-1.3 SHA-256 |
|---|---|---|
| Working surface | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` |
| Deliverable register | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| Scope ledger | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` |
| Objective register | `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55` | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| Forward trace | `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84` | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| Reverse trace | `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0` | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| Coverage telemetry | `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282` | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` |

Application record SHA-256:
`31207f122e9d64b4734a701cae364b2456df65d0605b2b1d0c6880ce5595760a`.

Git-effect slot: `TBD` for a later recorded act.

## Closure-validation lane

1. Live applied identities against R4-A: PASS 7/7.
2. `validate_gate5_applied.py`: PASS 65/65, zero failures.
   Validator SHA-256:
   `281cfa29f66cf73dc3ab28c85029386e940f3109807862fbb18ae4f86036f63b`.
   Validation JSON SHA-256:
   `f811bf1c08742833ef13ca0a503ecb8d5ac965a093b21f04767c4e8df6daa1b1`.
3. Post-Gate5 scoped AUDIT_DECOMP backcheck: PASS for the applied package.
   `coverage_summary.json` SHA-256:
   `70ed91a848c762d9afb778423220c53408e1e4d2273a4a8aa7d5d81fd25359e9`.
   Topology: 53 deliverables; PKG-02=12; PKG-04=11; packages=6; scope
   items=104; objectives=7; forward rows=85; reverse units=59; zero unmapped
   IN items; zero unsupported objectives; zero untraced reverse units.
4. Write containment: PASS. No live folder, SOW, `_STATUS.md`, or
   `_DEPENDENCIES.md` changed.
5. Holds: PASS. Accepted compatibility JSON SHA-256 remains
   `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`
   and contains exactly ten complete `HELD_UNAVAILABLE` objects with null
   identities. Exact binding citations: `Impact_Assessment.md:83-92`.
6. Derivative disposition: recorded below.

The pre-application `validate_gate5_package.py` was not run against applied
live state because it asserts revision 1.2 is untouched. The protected
Phase-0c `validate_gate3_candidate.py` was not run against live applied state
because its Gate-5-artifacts-absent check belongs to the Phase-0c layout.

## Changed paths

Owned tracked updates:

- seven exact live files under `execution/_Decomposition/`;
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Decision_Log.md`;
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Handoff_State.md`.

Owned new SCA files/folder:

- `validate_gate5_applied.py`;
- `Gate_5_Rehearsal_Record.md`;
- `Gate_5_Applied_Validation.json`;
- `Gate_5_Application_Record.md`;
- `Evidence/AUDIT_DECOMP_POST_GATE5/` with nine audit-evidence files.

Owned runtime evidence:

- this `RETURN.md`;
- sibling `STATUS.json`.

The parent-owned Phase-0f orchestration plan, graph, and sealed launch brief
were pre-existing control-plane records and were not modified by N1.

## Protected state verified

- `_LATEST.md` SHA-256 remains
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.
- Gate-1 audit baseline SHA-256 remains
  `2210e77f989f29c11e005d7fe89944e2e0f0fe265e0a514f53042aaa89de9e45`.
- Task Management register SHA-256 remains
  `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518`.
- Approved append SHA-256 remains
  `336405845dde5a3ae406b46c750c38a88c1b366f69bdaa74b4078679e04fe6a8`.
- Published Gate-5 validation JSON remains
  `4831fb2757bfcdeb2faa0dff51a15d4f04ec68d4c9716928a36f1ea8844df966`.
- All R4-A/R4-B/R4-C/R5-A verbatim blocks in the SCA Decision Log were
  byte-compared to their published sources: PASS 4/4.
- No `_STATUS.md`, `ScopeOfWork.md`, `_DEPENDENCIES.md`, live deliverable
  folder, graph, tool, runtime, project, export, pin, or App surface changed.

## Derivative disposition

| Derivative | State | Rerun / next owner |
|---|---|---|
| Live decomposition package | `CURRENT_APPLIED_R4-A` | Owner Gate-5 confirmation |
| Rehearsal/application/validation/backcheck evidence | `CURRENT` | Preserve for confirmation and Git-effect backfill |
| PREPARATION INIT ×7 | `STALE_NOT_MATERIALIZED` | PROJECT_SETUP/PREPARATION, later authority |
| DEL-02-06 `_CONTEXT.md` | `STALE` | Later approved mirror edit |
| Dependency extraction | `STALE` | After folders are live |
| Estimates and schedule | `STALE` | After accepted SOW/dependency inputs |
| `WORK_GRAPH.json` / `DAG.md` | `STALE_FOR_APPLIED_TOPOLOGY` | Re-derive after folders are live |
| `AUDIT_DEP_CLOSURE` | `STALE` | After graph re-derivation |
| `_LATEST.md` | `UNCHANGED_R4-C_DEFERRED` | Separate owner ruling after confirmation |

## Blockers and rerun requirements

1. Ryan Tufts must confirm or decline the exact Gate-5 applied state and
   closure evidence.
2. Pointer treatment remains separately owner-gated under R4-C.
3. Git-effect slots remain `TBD` until a later recorded act after merge.
4. The deferred propagation acts above remain separately owned and gated.
5. TM-ROOT-106 and TM-ROOT-122 remain G1 blockers; no pin change occurred.

Before owner confirmation, rehash the seven live files against R4-A and rerun
`validate_gate5_applied.py`. Do not infer confirmation, pointer authority,
folder/SOW/dependency/estimate/schedule/graph work, implementation, hold lift,
cutover, release, publication, reliance, or merge authority from this return.
