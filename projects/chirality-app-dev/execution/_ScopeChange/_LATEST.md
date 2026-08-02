# Active SCOPE_CHANGE Snapshot

**Status:** `CLOSED_FOR_SCOPE_CHANGE_ONLY`
**Active snapshot:** `execution/_ScopeChange/SCA-APP-007_2026-08-01_DEL03_Legacy_Evidence_Ownership/`
**Amendment label:** `SCA-APP-007 DEL-03 Legacy Evidence Ownership`
**Post-change audit:** `execution/_Evaluation/DecompCoverage/COV_SCA_APP_007_POSTCHANGE_DEL03_RECON_2026-08-01_2026-08-01_1754/` — `WARNINGS`, 0 blockers, 10 unrelated pre-existing artifact-name warnings, 1 information finding

The owner confirmed the validated Gate-5 state. The retired physical
`DEL-03-06` evidence container was not adopted into the decomposition. Its 38
historical proof files were migrated byte-for-byte to accepted `DEL-09-06`,
future runner routing and labels were corrected, and provenance was recorded.
The accepted decomposition remains byte-identical and the post-change audit
confirms topology 10/51/78/10, reverse coverage 100%, and resolution of both
SCA-APP-007 topology warnings.

SCA-APP-007 is closed for scope change only. The canonical Vitest wrapper is
retained as a non-blocking rerun advisory for the next dependency-installed
test pass. The six D-APP-81 clause-6 `HISTORICAL_RELATION_UNKNOWN` relations
remain unchanged. Loop receipt, Git, lifecycle, release, dependency, estimate,
schedule, and any additional implementation work remain separately governed.
