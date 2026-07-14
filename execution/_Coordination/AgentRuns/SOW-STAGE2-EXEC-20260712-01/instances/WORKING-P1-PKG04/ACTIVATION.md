# WORKING-P1-PKG04 Activation

RunID: `SOW-STAGE2-EXEC-20260712-01`
InstanceID: `WORKING-P1-PKG04`
PackageID: `PKG-04`
Accepted checkout: `main@2a5e3825d8d2fc4943742a53ccad3b89c4c81902`
Selection authority: sealed `LAUNCH_BRIEF.md`, after accepted PKG-03 integration.
Posture: `SEQUENTIAL_BATCH_WITH_INDEPENDENT_FAN_IN`.

Exact selected population is `DEL-04-01` through `DEL-04-06`. All six
members reproduce as `IN_PROGRESS`, complete `LEGACY_FOUR_DOC`, with no live
`ScopeOfWork.md`. The complete row-by-row hash and physical-line reproduction
is `LIVE_BINDING_REPRODUCTION.tsv` and `PREFLIGHT_SUMMARY.md`.

Batch 1 is exactly `DEL-04-01..05`, five members and 1,092 frozen physical
source lines. Batch 2 is exactly `DEL-04-06`, one member and 276 lines. This
is the minimum consecutive numeric partition under the accepted five-member
and 2,053-line limits.

Exactly one package-wide author followed by one fresh evidence-only verifier
is dispatched for each batch. Batches and child writes are serialized. Only
run-local candidates and instance evidence may be written. Project paths,
PKG-00, `DEL-01-01`, lifecycle, Git, integration, H1/H2, release, retirement,
and unrelated dirty paths are excluded.
