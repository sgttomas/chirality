# RECON-C2F-R1 Run Basis

Verdict: `BLOCKED`
Observed: `2026-07-13T07:57:09Z`

This is a bounded read-only remediation fan-in under RECONCILIATION. It
preserves the original C2F BLOCKED package as immutable upstream evidence and
is itself derivative evidence, not governance, decomposition, deliverable,
lifecycle, integration, release, H1, H2, or legacy-retirement authority.

## Accepted upstreams

- D-GOV-16 ruling publication
  `7584718aa32b112e415331736d1a8e68c12ac176`;
- accepted Stage-2 plan snapshot/binding
  `27f03730c956447b9a9696422cc9c63b8f061939` /
  `b22a24fda994a8387a9bf2e04a2826dc311a36dd`;
- accepted P0 basis and P1 canon post-merge handoff;
- live canon on
  `main@e150c972889d05a8fc270239451a35c7512dc9a9`;
- immutable initial C2R, C2A, RECON-C2F, EVAL-C2F, and REVIEW-C2F packages;
- active `C2F-REMEDIATION-001`, including clarifications 001-A and 001-B;
- terminal `HELPS-C2R-R1`, `HELPS-C2R-R2`, and `WORKING-C2A-R1` returns and
  their derivative evidence.

## Observed source state

- Branch/HEAD: `main@e150c972889d05a8fc270239451a35c7512dc9a9` with the live unintegrated
  C2 consumer candidate in the working tree.
- Canon hashes remain exact: standard
  `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f`,
  TYPES `5094610af55d18982658ea589be95a60fac9c89ca611846fc57279b494c6d2ae`,
  SPEC `915c3b59d35afff5e489c9c387f09c17a6e4c307fd5e91cd81a8960d97a91e27`.
- Root repaired hashes reproduce C2R-R2: `common.py`
  `c996955374833be390d8a9c0fdbb8ed0acef629204b38de8e312a963d6ea3214`,
  converter `8ddef1b65f337f7091156c579558bbe8adb245a8afa43295f9d041724f203ec9`,
  tests `586646790dfe21efb7ad47cca5a77fa7561e0be014d8d7fa0adf5360e2af876c`,
  reporting fixture
  `9d7263c359c9d38b7ef1918b8ef01915e21c5bb2048491902c0fb4b2003065ce`.
- App repaired hashes reproduce C2A-R1: scanner
  `3f3a45c6dd09c35e51f22f651399f70fbae33a17021ebdf531e192ee11b2dc3f`
  and scanner regression
  `295fbb0369b448534de6c1bb56fbecd35df6fc2f595b96677ed2e96ed1b0ebaf`.
- The active checklist caller is
  `tools/scope_of_work/derive_review_checklist.py` at
  `bd10eab5e09226b4b2643a13ef4fd7766baad5f8c06d390481cd688732c3464f`.

Any material change to these source identities, accepted upstreams, caller
population, check evidence, or changed-path set makes this package stale and
requires a fresh fan-in.
