# WORKING_ITEMS SCA-004 currency sweep — manifest

## Authority and boundary

- Owner-approved activation: 2026-08-03, exact TM-PEC-015/017 currency sweep.
- Durable owner-approval record:
  `projects/pec/execution/_Coordination/WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/OWNER_APPROVAL_2026-08-03.md`,
  SHA-256 `0122df48fc81a8adcb351099497ba4c0543f9fc596895a8469ab04d619a399ac`.
- Routed carrier:
  `_DomainEngines/pec/_TaskManagement/DRAFT_HANDOFF_TM-PEC-012_SCA004_METADATA_ALIGNMENT.md`.
- Accepted decomposition: revision 1.4, SHA-256
  `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`.
- PROJECT_SETUP predecessor:
  `projects/pec/execution/_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/HANDOFF_STATE.md`,
  SHA-256 `93a3337b3c1f4ebee5ccee48a191e8a67ea4b080dedf88a82b6bcc7af6b58b1f`,
  verdict `PROJECT_SETUP_METADATA_ALIGNMENT_SUBSET_COMPLETE`.
- Explicit exclusions: RF-002 and every SOW/REVIEW/lifecycle byte; Task
  Management registers; decomposition truth and `_LATEST` pointers; source;
  foreign loops; receipts; acceptance, release, and reliance.

## Exact write set

| Act | Path | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|
| CURRENT_MAP | `projects/pec/README.md` | `5f3afbdae60d749c8fd680b34a806e0edebacdac0a8b157711ada4547ab5529e` | `42fd5fd9480b899db1b864f02630fbfb8545b0d3ce1f3c9cd35d03281ad9b536` |
| CURRENT_MAP | `projects/pec/docs/STATUS.md` | `e6dcef056dad6553827dcedc777e55fce666c97e29269a8b232a80c9c70d6acf` | `27b74f5e95665ca897c244e890f4feb85ae2c0eda23683ce2298bc7c0cfd5c72` |
| CURRENT_MAP | `projects/pec/execution/_Coordination/_COORDINATION.md` | `77ee9c3508bbc14886b9c4202c1529796a6b3c5f8564a12be15c1fd0cd04cd47` | `3686360344f2927b6f8f8ea58867c2cbfe848f8c50dc7679c782e8852ebc4fbb` |
| CURRENT_MAP | `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` | `bff198a04b1bb6e96e815c83f1eced2744996dd07a1b3501d80e4674e4b7e595` | `fbf6d66bc2948f8ea53ed06eea434edd1e62891ba0920345524c512a0e925986` |
| APPEND_SUPERSESSION | `projects/pec/execution/_Coordination/AgentRuns/PEC-DPEC77-78-20260802/HANDOFF_STATE.md` | `1da297710e821c072f58a78fb9850f427b55dfb88a7fdc77f3a65083dca48dae` | `e5d875e3250b28fb75ca655021563a9b306dfbb639ec1cfc2ee461f938475926` |
| APPEND_SUPERSESSION | `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md` | `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d` | `bd93bced731d75e32b5aeae6902ecf81e558244ce47b1712ef9c6bd9ac6a2ba3` |
| APPEND_SUPERSESSION | `projects/pec/execution/_Coordination/D-PEC-77_DEL-01-05_ENFORCEMENT_2026-08-02/EXECUTION_HANDOFF.md` | `7f983befae836dac0172bdc16a72a7c340d27afab9eda6f3054d149ff435aee9` | `2955761249c9e0829f03dfeedb643f04075f11c64db67af9619183bfd3af9dfa` |
| APPEND_SUPERSESSION | `projects/pec/execution/_Coordination/OD7-G3_APPLICATIONS/D-PEC-67/HANDOFF_STATE.md` | `e161f55994573d600dcd41e59bf1faa17cb32ff26bb037ae381112ca2e77f2bc` | `99188688421a70e668953584c18c709e14f6103d2ccca8ca4690284150e74366` |
| CREATE_EVIDENCE | `projects/pec/execution/_Coordination/WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/OWNER_APPROVAL_2026-08-03.md` | absent | `0122df48fc81a8adcb351099497ba4c0543f9fc596895a8469ab04d619a399ac` |
| CREATE_EVIDENCE | `projects/pec/execution/_Coordination/WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/MANIFEST.md` | absent | self-referential; not hash-bound here |
| CREATE_EVIDENCE | `projects/pec/execution/_Coordination/WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/VALIDATION.md` | absent | recorded after validation |
| CREATE_EVIDENCE | `projects/pec/execution/_Coordination/WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/HANDOFF_STATE.md` | absent | recorded after validation |
| CREATE_EVIDENCE | `projects/pec/execution/_Coordination/WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/SCOPE_CHANGE_HANDOFF_TM-PEC-023.md` | absent | recorded after validation |

The WORKING_ITEMS package contains five evidence files. No other path is owned
by this WORKING_ITEMS write set.

## Immutable historical carriers

The following files remain byte-identical. Their current superseding pointers
are recorded in `_COORDINATION.md` rather than in the immutable files:

| Path | Required SHA-256 |
|---|---|
| `projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_SOW_V22_SCA003_RECON_2026-07-28/HANDOFF_STATE.md` | `b92f52396e0d25bf40d04c0bef26f21077064174bb02d4c24c5f23d13f0794ee` |
| `projects/pec/execution/_ScopeChange/SCA-003_2026-07-28_0824/Handoff_State.md` | `ee5624241ac383aab49d0381f9c9f3b31a439888aec39a5f1016ab9aeeae3632` |
| `projects/pec/execution/_Coordination/PROJECT_SETUP_REFERENCE_PARITY_2026-07-28/HANDOFF_STATE.md` | `604826885cd39aedb85fee1f53079123d4389496f3ec48ed3f437944877fd545` |
