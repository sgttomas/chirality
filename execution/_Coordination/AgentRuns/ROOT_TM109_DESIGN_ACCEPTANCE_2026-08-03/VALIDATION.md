# TM109-A design-acceptance validation

Verdict: `PASS`

## Authority checks

- The authority source exists and hashes to
  `6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566`.
- The transcript contains one unambiguous signed TM109-A ACCEPT return naming
  package SHA-256
  `2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489`,
  signer `Ryan Tufts`, and date `2026-08-03`.
- The signed return explicitly limits acceptance to contract-design semantics,
  preserves recorded non-selections, and denies implementation, affected-client
  acceptance, lifecycle, release, publication, and reliance.

## Accepted-package identity checks

- Git commit `ba4678ca00c0cf9fb862ba36d1410d11ce1ff6ac` exists.
- At that commit, `POST_REFUTATION_MANIFEST.csv` hashes to the exact signed
  package SHA-256.
- All six manifest paths exist as regular Git blobs at that commit.
- Each blob's bytes hash to its exact manifest-listed SHA-256.
- Each Git blob OID and SHA-256 is recorded in `ACCEPTED_PACKAGE_BINDING.csv`.
- The manifest and its two unchanged members remain byte-identical after
  repair. The other four members differ only by removal of one surplus
  terminal blank line, as shown by the Git diff from `ba4678ca...` to
  `2b6d53027...`.
- The current manifest's unchanged digest does not rebind its old member hashes
  to the normalized descendant files. The accepted exact bytes remain the
  preserved blobs at `ba4678ca...`.

## Repair-sequencing checks

- Branch `HEAD` and `origin/codex/root-owner-rulings-2026-08-03` both resolve to
  repair commit `2b6d53027ea10374dd515a4a5a203f8ed4cf2f04` before this carrier's writes.
- The Root TM-ROOT-111 note records the failed PR #510 run/job, the repair
  commit, and passed rerun `30877532946` / `91891904563` as priority evidence.
- No claim is made that local validation substitutes for hosted CI authority.

## Scope and claim checks

- Only this acceptance RunID was written by this manager.
- The original candidate carrier was not mutated.
- No Root register, receipt, source, test, App, Piping, DEL-02-06, lifecycle,
  release, publication, or Git state was changed by this manager.
- No equality, mapping, normalization, tolerance, semantic comparison,
  conformance, compatibility, or cross-consumer claim is made.
- All deliberate non-selections in accepted OD109-01 through OD109-16 remain
  explicit blockers to implementation or reliance.

Structural status is `PASS`. This validation records an already-signed human
semantic decision; it is not a second acceptance and grants no implementation
authority.
