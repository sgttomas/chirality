# Independent Distribution Semantic Rebind Review — V10

**Verdict: PASS** as a held derivative consistency review. No actionable distribution rebind findings remain. This verdict does not accept Runtime source or qualify a package, publication, or release.

## Subject and anchors

- Subject: `distribution/subject-v10.json`
- SHA-256: `485cc778ab131e477d792fad0e06b310023398d734609cdd9ec4421f1087ea18`
- Size: 13,126 bytes
- Bound members: 19
- Root semantic successor: `8669df0d1b2ab639e0e3d1352843130aabf8d88ab8050ed9f5169b022d9afad5`
- App V7: `240a974e9e6a0c9317ea77b9588997adf2d03b613bfd78595ee1a8c3c5405a80`
- Runtime V4: `1fee69de0e1ade83cd414aed63380d1cabf0989fe070734a73c40867dd10e28c`

All three anchor files match their declared hashes and sizes.

## Rebind result

All 19 V10 member hashes and sizes match. V9 and V10 bind the same 19 paths. Only `export-manifest.csv` and `export-report.md` changed; all 17 implementation and test members remain byte-identical, including the contract pins and D121 exact-source identity files. Exact-member `git diff --check` passed.

The regenerated manifest has 1,104 unique rows. Every row exactly matches the current staging path, byte size, and SHA-256 value. The staging tree contains no symlinks or special entries. The boundary scan returns zero findings, and no excluded private root, `chirality-change` skill, or App frontend/UI source appears in the projection.

The one-file increase under `tools` is legitimate Root closure: `tools/workflow_runtime/fixtures/legacy_method_normalization_cases.json` matches the source, staged, manifest, and Root semantic-successor identity of 3,727 bytes and `bb244510229acb22e559018a7851d41c9a4d7684bdfad4e18945d3ba4ffd82cc`.

The report truthfully states 1,104 rows, zero sanitized files, and zero boundary findings. All top-level counts match the current tree, including `tools` increasing from 391 to 392. V9 predecessor and independent-review bindings also reverified exactly.

## Pending review and scope

V10 explicitly records that Runtime V4 terminal Astra review was pending when the subject was created. This derivative review does not accept Runtime source and must remain held if that review finds drift or defects.

This narrow review relies on unchanged implementation and the prior V8/V9 independent reviews. It does not establish native package, supplier, account, credential, distribution, publication, or release qualification.
