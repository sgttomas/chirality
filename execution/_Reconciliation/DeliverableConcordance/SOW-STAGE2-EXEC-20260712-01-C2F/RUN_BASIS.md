# RECON-C2F Run Basis

Verdict: `BLOCKED`

This is a bounded R3-style read-only consumer fan-in under the accepted
D-GOV-16 Stage-2 activation. It is derivative evidence, not decomposition,
deliverable, lifecycle, integration, or release authority.

## Accepted upstreams

- D-GOV-16 ruling publication
  `7584718aa32b112e415331736d1a8e68c12ac176`;
- accepted Stage-2 plan snapshot/binding
  `27f03730c956447b9a9696422cc9c63b8f061939` /
  `b22a24fda994a8387a9bf2e04a2826dc311a36dd`;
- P0 basis and caller manifest at
  `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/`;
- P1 canon post-merge handoff and live canon on
  `main@e150c972889d05a8fc270239451a35c7512dc9a9`;
- C2R candidate/return under `candidates/P2_ROOT/` and `instances/HELPS-C2R/`;
- C2A package under
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/`.

## Observed source state

- Branch and HEAD: `main@e150c972889d05a8fc270239451a35c7512dc9a9`.
- Live canon SHA-256 values reproduce the P1 handoff exactly:
  successor standard `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f`,
  TYPES `5094610af55d18982658ea589be95a60fac9c89ca611846fc57279b494c6d2ae`,
  and SPEC `915c3b59d35afff5e489c9c387f09c17a6e4c307fd5e91cd81a8960d97a91e27`.
- The live tracked diff contains 53 paths: 48 exact C2R source paths, four
  exact C2A source paths, and the parent-owned run `WORK_GRAPH.json` update.
- No expensive suite was rerun. Current recorded check evidence was consumed
  and live identities, counts, changed-path sets, and relevant source
  semantics were independently reproduced.

Material change to any accepted upstream, caller identity, live source hash,
resolver/authority contract, check evidence, or changed-path set makes this
fan-in stale and requires rerun.
