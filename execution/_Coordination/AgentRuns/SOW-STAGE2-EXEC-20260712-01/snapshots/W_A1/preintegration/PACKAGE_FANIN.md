# W-A1 Package Fan-In

Verdict: `PASS`.

## Current fan-in

- Exact current package bindings: 189/189 reproduced
  (`23 + 40 + 64 + 62`).
- Terminal members: 15/15.
- Accepted author/verifier pairs: 15/15, or 30 terminal child returns.
- Claim mappings: 456.
- Source lines dispositioned: 4,817/4,817.
- Candidates: 15 exact files at the hashes in `CANDIDATE_MANIFEST.tsv`.
- Replacement / rollback: exact 75 / 75, with rollback the row-exact inverse.
- Package/member/schema/content-authority/preservation/substrate verdicts:
  PASS with no waiver.

`detailed/CURRENT_PACKAGE_BINDINGS.tsv` is the current exact binding ledger.
`detailed/PACKAGE_BINDINGS.tsv` is retained as the sealed 186-binding
historical pre-R2 audit. The historical audit is explicitly superseded only
for current package-binding cardinality and PKG01 portability identity.

## PKG01 R2 hold and closure

Initial fan-in correctly held because two generated PKG01 check JSONs retained
unclassified checkout-root `workspace_root` values while package checks
claimed generated-prefix zero. The owning manager repaired only those two
fields under `A1-PKG01-CHECK-EVIDENCE-PORT-R2-001`.

Independent R2 reproduction proves:

- current PKG01 MANIFEST 40/40 at
  `4924de97675bf8f0ad8bba606d3d5fc171d03445259a5e96eb72c5e002871f62`;
- PROJECT_CHECKS JSON postimages parse and retain all six registered PASS
  results across the two files;
- exactly one `workspace_root` substitution per file;
- reverse substitution reconstructs the exact R1 postimage/R2 preimage hashes;
- historical R1 normalization remains the exact intermediate chain;
- unclassified generated checkout/temp prefixes: zero.

See `detailed/PKG01_R2_CHAIN.tsv`, `detailed/PKG01_PORTABILITY_HITS.tsv`, and
`detailed/CURRENT_PACKAGE_FANIN.json`.

## Carried package proof chains

- PKG00: the rejected wrong-package converter invocation and zero-test initial
  premerge attempt are preserved substrate; accepted canonical conversion and
  live-stub R1 premerge pass.
- PKG01: AUTHOR-DEL-01-02 generated run-record repair and both R1 and R2 check
  normalization chains reproduce exactly.
- PKG02: check normalization and verifier DEL-02-03 Attempt 0 / accepted R1
  chain reproduce.
- PKG03: author manifest regeneration, generated-evidence portability repair,
  author-run-record terminalization reconciliation, and planned premerge
  normalization reproduce.

No chain changes candidate meaning, source/status/control identity, authority,
or lifecycle state.
