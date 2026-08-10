# TM-PEC-013 revision 02 validation

## Successors and regenerated checklists

| Deliverable | Reviewed preimage SHA-256 | Repaired successor SHA-256 | SOW validation | Checklist rows | Checklist SHA-256 |
|---|---|---|---|---:|---|
| DEL-02-07 | `d2f898c1bc5b9b3798fe9c5b4961019c9f88366fc36e44c25c51bc878947391f` | `d044499ab5ace12305434ab3c7b5e17e21f730f8d77b45ff64c055d1edce2559` | `PASS / SOW_V1 / zero issues` | 8 | `1ea90c3c4d95d5eaa9e176280b9dba56be68b597babfa0685a7e1fa6b00a4474` |
| DEL-03-01 | `b2569e56927459f93865cbe4642bddbfbee96814aa79ed6b39cb3b3721246f64` | `564955235aeab60f169e6377dd9d5bb5fbe2a88a8cc66094e17f6f83987792d2` | `PASS / SOW_V1 / zero issues` | 17 | `fdca0465f29bc8a5da49fa3c0fec2bb10892105d55378745af097637fdbf4033` |
| DEL-04-01 | `21e696ce8ccaad88f852f6a91a4bc575c1e46601b5d3e026978a49164f2c9d89` | `6f4e8c66a5712ba73e5000f1eafbfd5dd821bb4c339a23d77aa46b5b558830ae` | `PASS / SOW_V1 / zero issues` | 16 | `e15dfaf989b574b408f7a89a4d262592071dd31a2911b90995fec7c436cd05e4` |

Every checklist item has one `source_identity.sha256`, and that value equals
its repaired successor hash. Any successor-byte change requires SOW validation
and checklist derivation to rerun.

## Exact-diff and preservation checks

- Exact repair inspection is recorded in `EXACT_REPAIR.md`; all six ruled
  findings and only their cited SOW claim locations were repaired.
- Stale-claim scan finds none of the reviewed false statements: DEL-02-07's
  old E-N16 evidence text; lifecycle `OPEN` in the cited DEL-02-07/DEL-03-01
  claims; a shared historical-exhibit `EvidenceFile`; the all-INITIALIZED
  DEL-04-01 predecessor assertion; or the no-baseline-report assertion.
- The three `Dependencies.csv` hashes remain, respectively,
  `00b5a872ca0a62c9246591d513af11637e3e15dc764824fd28b7d8219f3c3ee3`,
  `5f68759d07cc001e139fc351e33748ef7f03ba5ba9cd7ed77a6182ad8161bd65`,
  and `2daee4e76382186657c52b01caf5c4435c8d6a501c6d2b305c9b1c9703a916e4`.
- The three `_STATUS.md` hashes remain, respectively,
  `c26d6861c1f07ee33c8fec6c74d126270d619955da1068c853a4b0132c2a8792`,
  `f8816dcaa48f3ca980f1b6db51129efb5d3a5095d0120fbf4698878e9b9121b5`,
  and `7c9902184deeb30b80728979fd76c710a23396ba549c144bc713134e51a94dd1`.
- DEL-10-01 evidence reproduces: `_STATUS.md`
  `3309a68a1180b7fdf40722e5e63cc468a4f76fcf484b98799f700743a63ab5f2`,
  baseline report `0aa5dd22d397026d88dfd8af1613163dd2de01ef3264024438034e54a1f5d02d`,
  and method `5756d6cf1b7293a7db8dcf1ce968d443dcb7214867216f5013ee018a493a0c59`.
- Original producer checklists remain byte-identical at SHA-256
  `1b3a798ea90ff053c69b9c0d7b1a50eb59d22c660c99b01a91e1c1be2b424820`,
  `b32d9c92c22cbbd992793bb4abd91ae648f4cf311e59b319ad21677bda38a424`,
  and `d605eefb1e6b9089a9b0a9f935c203b4540b9845792480d330469e0523030348`.
- Review controls, findings registers, immutable review snapshots, and the
  review pointer were read only and not edited by this repair.
- Targeted `git diff --check` passes. No lifecycle, dependency, source,
  decomposition, SCA, PRD, Task Management, receipt, standing-plan, or
  foreign-loop byte was written by this repair.
- PEC reliance preflight returned `ALLOW` for both
  `dispatch-for-production` and `candidate-validation` on all three targets.

## Rerun boundary

The repaired candidates and checklists are ready for the separately owned
PEER_REVIEW rerun. This validation does not close or modify RF rows, enter a
REVIEW gate, update a review pointer, accept an artifact, or change lifecycle.
