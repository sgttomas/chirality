# WORKING-P2-PKG05 Activation

RunID: `SOW-STAGE2-EXEC-20260712-01`
InstanceID: `WORKING-P2-PKG05`
PackageID: `PKG-05`
Accepted checkout: `main@eaad463c0d481f6f1654e6adb5ee718f566176e9`
Selection authority: sealed `LAUNCH_BRIEF.md` after `W-P2-B0_ACCEPTED`.
Posture: `SEQUENTIAL_BATCH_WITH_INDEPENDENT_FAN_IN`.

Exact selected population is `DEL-05-01..05`, five members and 1,292 frozen
physical legacy-source lines. Manager preflight reproduced 5/5 P2 manifest
rows and all 45/45 expected live bindings: every member is `IN_PROGRESS`,
non-pilot, non-ISSUED, exact `LEGACY_FOUR_DOC`, and has no live
`ScopeOfWork.md`. Source, status, context, references, dependency-document,
and dependency-CSV hashes match the accepted preflight without drift.

The single batch is within both accepted bounds (five members and 2,053
lines). Exactly one package-wide author followed by one fresh evidence-only
verifier is dispatched. Child work is serialized. Only run-local candidates
and this instance's evidence may be written. Live project paths, Git,
lifecycle, controls, dependencies, PKG-00, integration, release, reliance,
rollback execution, retirement, and H2 state are excluded.
