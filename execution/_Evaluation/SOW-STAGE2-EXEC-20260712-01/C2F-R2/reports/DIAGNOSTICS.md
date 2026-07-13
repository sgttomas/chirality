# C2F-R2 Read-Only Diagnostics

Frozen canon basis: `main@e150c972889d05a8fc270239451a35c7512dc9a9`

## Inventory, hashes, and containment

- P0 exact caller rows after excluding eight historical/independent aggregate
  rows: `64`; current P2_ROOT rows: `64`; symmetric surface delta: `0`.
- Frozen App caller rows: `9`; App rows outside the exact P0 set: `0`.
- Current root/canon post-hash mismatches: `0`.
- Current App final-hash mismatches after the C2A-R1 two-path overlay: `0`.
- Current tracked subject diff: `52` paths = `48` root + `4` App; root and
  App exact-manifest gaps: `0`; root/App intersection: `0`.
- Live canon hashes remain standard
  `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f`,
  SPEC `915c3b59d35afff5e489c9c387f09c17a6e4c307fd5e91cd81a8960d97a91e27`,
  and TYPES `5094610af55d18982658ea589be95a60fac9c89ca611846fc57279b494c6d2ae`.
- Both root `WORKING-C2A` and `WORKING-C2A-R1` status/return pairs are present
  and terminal `PASS`.
- `.claude-worktrees/` was excluded and not touched.

The only tracked root control-plane diff is the parent-owned `WORK_GRAPH.json`;
it is not a candidate subject path. No governed deliverable, lifecycle,
receipt, release, H1, H2, or retirement path is in the subject diff.

## Direct authority and ISSUED inspection

- Root `common.py:338-348` compares the raw supplied token to the exact ruled
  authority and requires the candidate marker to bind it.
- The converter compares raw equality at lines 56-63, validates a safe
  ISSUED accepted-basis value at lines 41-53 and 68-81, and emits accepted
  basis, source commit, four source hashes, and status hash at lines 168-176.
- The checklist caller passes `args.migration_authority` unchanged at lines
  163-169. It writes output only after successful exact resolution.
- The App scanner compares the raw supplied authority to the exact ruled token
  at `filesystem.ts:652-658` and requires exact marker binding at 705-706 and
  741-746. Its current regression covers unruled, malformed, missing,
  non-isolated, wrong-path, and whitespace-padded states.

## Targeted current reproduction

One non-expensive pytest invocation ran only:

- `test_review_checklist_is_exact_source_ordered_linked_and_deterministic`;
- `test_review_checklist_rejects_padded_ruled_authority_without_output`.

Result: `2 passed in 0.30s`. The first test proves byte-stable exact-dual and
SOW-only item order/text/linkage. The second constructs an exact-marker dual
candidate and proves leading-space and trailing-tab supplied authority each
exit `1` and create no requested checklist output. Durable JUnit evidence is
`reproduction/checklist-targeted.xml`, SHA-256
`9d50527937e0e6e3f5aed90dcdd7c384958fd18e41947abb4fc4d51d6089ec75`.

## Recorded current-hash evidence

C2R-R3 records focused `19 passed`, full root tools `792 passed`, compile,
diff hygiene, and containment PASS at the current checklist/test hashes. The
unchanged C2R-R2 resolver/converter hashes remain bound to focused `18` and
full root `791` PASS evidence. C2A-R1 records focused `76`, full frontend
`713 passed / 4 skipped`, typecheck, build, self-check, practitioner `264`,
and owned-server premerge PASS at current App hashes. No expensive suite was
rerun.
