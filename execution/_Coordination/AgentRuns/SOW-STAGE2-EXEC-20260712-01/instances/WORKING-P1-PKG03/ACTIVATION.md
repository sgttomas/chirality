# WORKING-P1-PKG03 Activation

RunID: `SOW-STAGE2-EXEC-20260712-01`
InstanceID: `WORKING-P1-PKG03`
PackageID: `PKG-03`
Accepted checkout: `main@5f124ad80fe84357f6dc33072dc4fbdbeb05d545`
Selection authority: `SESSION-CONTINUATION-PKG03-001.md` under the accepted
Stage-2 plan and Root Receipt 12.
Posture: `SEQUENTIAL_BATCH_WITH_INDEPENDENT_FAN_IN`.

Exact selected population is `DEL-03-01` through `DEL-03-08`. All eight
members reproduce as `IN_PROGRESS`, complete `LEGACY_FOUR_DOC`, with no live
`ScopeOfWork.md`. All 72 live source/status/control/dependency bindings match
the accepted rows in `snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv` and
`EXPECTED_LIVE_BINDINGS.tsv` at the accepted checkout.

Frozen source-line counts (the four legacy production documents, using exact
physical line counts) are:

| Member | Lines | Batch |
|---|---:|---:|
| DEL-03-01 | 220 | 1 |
| DEL-03-02 | 272 | 1 |
| DEL-03-03 | 191 | 1 |
| DEL-03-04 | 349 | 1 |
| DEL-03-05 | 235 | 1 |
| DEL-03-06 | 232 | 2 |
| DEL-03-07 | 218 | 2 |
| DEL-03-08 | 249 | 2 |

Batch 1 is exactly five members and 1,267 lines. Batch 2 is exactly three
members and 699 lines. This is the minimum consecutive numeric partition
under the accepted five-member/2,053-line limits.

Exactly one package-wide author followed by one fresh evidence-only verifier
is dispatched for each batch. The batches and all child writes are serialized.
Only run-local candidates and instance evidence may be written. Project paths,
PKG-00, `DEL-01-01`, lifecycle, Git, integration, H1/H2, release, retirement,
and unrelated dirty paths are excluded.
