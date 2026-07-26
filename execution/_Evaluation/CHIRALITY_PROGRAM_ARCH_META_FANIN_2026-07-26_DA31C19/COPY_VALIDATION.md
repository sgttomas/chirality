# Copy Validation

## Verdict

`PASS`

## Basis

- Worktree:
  `/Users/ryan/dev/chirality-meta-fanin-worktree`
- Accepted and observed `HEAD`:
  `da31c19b5656dd74615e308c4215688971d33dc9`
- Initial worktree state: clean
- Post-copy tracked state: unchanged
- Authorized untracked state: this package only

## Source Preflight

- Six of six declared source directories were present.
- No source symlinks were found.
- No source special files were found.
- The package root did not exist before the administrative run-record
  directories were created.
- No declared destination existed before its copy began.

## Identity Results

| Measure | Result |
|---|---:|
| Source packages | 6 |
| Relied source packages | 5 |
| Excluded supplemental packages | 1 |
| Source regular files | 83 |
| Destination regular files | 83 |
| Source bytes | 1,882,678 |
| Destination bytes | 1,882,678 |
| Per-file SHA-256 matches | 83 |
| Per-file size matches | 83 |
| Mismatches | 0 |

`SOURCE_IDENTITY_MANIFEST.csv` contains one identity row per source regular
file. `SOURCE_PACKAGE_SUMMARY.csv` contains one aggregate row per source
package.

## Method

Each source tree was copied recursively to its declared destination without
renaming or content normalization. For every regular source file, validation
reconstructed the destination from the declared destination root and original
relative path, then compared:

- file existence;
- SHA-256;
- byte count.

Package-level validation independently compared regular-file count and total
bytes. The copy was accepted only after every file and package comparison
returned `PASS`.

## Limitations

- This validation establishes byte identity and path preservation. It does not
  validate the semantic findings inside the copied review artifacts.
- The excluded fourth pass is preserved for completeness but remains
  non-relied supplemental material because it did not complete reciprocal
  challenge and fan-in.
- No census or supervisory synthesis was performed in this assembly run.

