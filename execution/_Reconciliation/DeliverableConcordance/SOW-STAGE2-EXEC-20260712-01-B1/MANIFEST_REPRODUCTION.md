# RECON-B1 Manifest Reproduction

Verdict: `PASS`

## Independent tracked census

The member set was derived from tracked `Datasheet.md` paths under the exact
App Dev and Piping `1_Working/DEL-*` roots, then C-sorted by deliverable path.

| Check | Reproduced result |
|---|---|
| total members | 154 |
| project split | App 53; Piping 101 |
| required files | 154/154 have `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, and `_STATUS.md` |
| SOW members | 0 |
| lifecycle | 153 `IN_PROGRESS`; 1 `ISSUED`; 0 unknown |
| sole ISSUED member | `projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-01_Project governance baseline` |
| partition | ten pilots; 144 remaining |
| sorted-path SHA-256 | `b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31` |

The pilot identities independently reproduce as App PKG-07 `DEL-07-01`
through `DEL-07-06` and Piping PKG-13 `DEL-13-01` through `DEL-13-04`.

## Row and artifact equality

For every member, all twelve fields were freshly derived: project, package,
deliverable ID, path, four source hashes, status hash, lifecycle, pilot, and
issued. Results are `154/154` rows equal to P0, with zero field delta. They are
also `154/154` equal to P3. P3 `EXECUTION_MANIFEST.tsv` is byte-equal to P0
`CENSUS_MANIFEST.tsv` and hashes to
`804938634127b1c81467bc6ad2792618106b12e5093cd5d7ddafc0740ef12979`.

P3 structure and binding checks independently reproduce:

- `EXECUTION_MANIFEST.tsv`: 154 data rows, twelve fields, zero ragged row;
- `ROW_COMPARISON.tsv`: 154 data rows, fourteen fields, every result `MATCH`;
- `MANIFEST.tsv`: six bindings and 6/6 current artifact hashes exact;
- P3 manifest SHA-256:
  `71f783214dd98bcf1b11570ed2918d4a18d76ef1498f7875ddb7dec7e214a740`;
- P2 manifest SHA-256:
  `def458aad0c829b9bb000b02b2813b326d101408fab4402f7c39f89822ef0dff`;
- P2 bindings: 15/15 exact.

Schema/content verdict: `PASS`. No membership, source, status, lifecycle,
pilot, issued, row, schema, or artifact-binding delta exists.
