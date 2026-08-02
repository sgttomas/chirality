# Gate-1 Validation Report

Result: `PASS`.

- CSV parse/schema: `PASS` for the conjunct ledger, evidence index,
  preservation census, and exact manifest.
- claim population: `PASS`, C01-C18 exactly once.
- disposition population: `PASS`, 13 exact removals, 3 exact restatements,
  and 2 no-change rows.
- source identity: `PASS`, all 18 before hashes equal current canonical
  top-level claim-block bytes.
- replacement identity: `PASS`, all three JSON-string UTF-8 replacements
  decode to their recorded SHA-256.
- conjunct coverage: `PASS`, 107 unique rows cover C01-C18.
- preservation: `PASS`, all 30 noncandidate Remaining blocks and their source
  files match the recorded hashes.
- adversarial fan-in: `PASS`, no overclaim and fit to stop at Gate 2.
- write containment: `PASS`, `git status` shows only this new derivative run
  root; no tracked target-corpus difference exists.

Manifest SHA-256:
`08e896349ae3bb2ce004f1aee1dbd7eb6b272cf992cfa5cf3d67ae51e7a09efe`.
