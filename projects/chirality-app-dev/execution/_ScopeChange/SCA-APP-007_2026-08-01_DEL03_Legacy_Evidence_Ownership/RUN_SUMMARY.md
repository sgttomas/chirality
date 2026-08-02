# Run Summary — SCA-APP-007

## Outcome

The evidence supports **migration to existing `DEL-09-06`, not addition of a
new `DEL-03-06`**. The old path is a stale output-routing defect from the
retired topology. Current `DEL-03-01` through `DEL-03-04` are present under the
accepted vNext PKG-03 and all remain `IN_PROGRESS`. `DEL-03-05` did exist in
the retired topology and was deleted during the May vNext replacement; it has
not existed in current topology.

## Work completed

- reconstructed the retired and current topology from Git and accepted files;
- read current PKG-03/PKG-09 decomposition, Scope Ledger, status/memory pairs,
  SCA-APP-002/005/006, proof runner, evidence bundles, and coverage findings;
- completed a fresh scoped AUDIT_DECOMP baseline (`WARNINGS`: 0 blockers, 12
  warnings, 1 info); the duplicate PKG-03 root and undeclared reverse-only
  `DEL-03-06` are the two topology-relevant warnings;
- prepared Gate 1 validation, Gate 2 impact, exact Gate 3 no-op preview, and
  exact Gate 4 operational plan; and
- executed the approved 38-file evidence migration and four exact proof-runner
  routing/label substitutions through WORKING_ITEMS;
- independently verified 38/38 per-file parity, 97,817 bytes, aggregate
  canonical SHA-256 `e27ca076ec3fdaeb4f6ba6cba6e716aa50497e130e5b0e3feab5dbc800aca4ff`,
  absence of the old live root, preserved CONF-002 text, and preserved
  DEL-09-06 lifecycle/Remaining/approval fields;
- verified accepted decomposition SHA-256
  `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`
  and six-UNKNOWN SHA-256
  `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`;
- verified authority corpus v18 with all eight sources `MATCH`, Receipt-52
  validation, and staged/unstaged whitespace checks; and
- completed post-change AUDIT_DECOMP snapshot
  `COV_SCA_APP_007_POSTCHANGE_DEL03_RECON_2026-08-01_2026-08-01_1754`
  (`WARNINGS`: 0 blockers, 10 unrelated pre-existing warnings, 1 info), with
  both SCA topology warnings gone and topology 10/51/78/10 unchanged.

## Gate state

Gates 1–4 were explicitly confirmed/accepted/approved on 2026-08-01. Gate 5 was
executed, independently validated, and confirmed by the owner. SCA-APP-007 is
`CLOSED_FOR_SCOPE_CHANGE_ONLY`. The
canonical Vitest wrapper was unavailable because frontend dependencies are not
installed; the exact manifest target passed 6/6 and routing assertions passed
14/14 through a deterministic Node TypeScript loader. This is sufficient for
the routing-only SCA acceptance and leaves a non-blocking canonical-wrapper
rerun advisory.

Final human token:

`CONFIRM SCA-APP-007 GATE 5: ACCEPT THE VALIDATED POST-CHANGE STATE AND CLOSE FOR SCOPE CHANGE ONLY; RETAIN THE CANONICAL VITEST WRAPPER AS A NON-BLOCKING RERUN ADVISORY.`

TM-CANDIDATE: investigate the May 2026 old-to-vNext DEL-03 stable-ID reuse as a provenance-only question; do not change current accepted identities absent a separate human-ruled scope request | `7bee9ae41` old topology, `92a25d270` deletion, `26fc253b5` vNext scaffold

## State fields

| Field | State |
|---|---|
| DecompositionTruthState | COMPLETE |
| DerivativePackageState | COMPLETE |
| ContentRemediationState | NOT_REQUIRED |
| DownstreamRerunState | COMPLETE_WITH_NON_BLOCKING_ADVISORY |
| MetadataAlignmentState | COMPLETE |
| AuditState | WARNINGS_NON_BLOCKING_FOR_SCA_OBJECTIVE |
| ReadyForNextPhase | NO — final loop receipt and any Git action are separately owned |
