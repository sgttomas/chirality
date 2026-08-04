# HELP_HUMAN orchestration plan — plan version 7

Run ID: `ROOT_FOUR_LANES_2026-08-02`
Selection authority: `HUMAN`
Posture: `SEQUENTIAL`

## Owner authority

Owner route ruling:
`OWNER_RULING_2026-08-03_COV_POST_001_ROUTE.md`, SHA-256
`0349897a313f1a41973d3134be3dd1addffc4e9d20ed73bb60b337143de6022b`.

The ruling authorizes an exact candidate only. Application, confirmation,
closure, packet regeneration/acceptance, N0, Git publication, and merge remain
separately gated.

## Node

| Node | Agent 1 | Objective | Stop |
|---|---|---|---|
| S4 | SCOPE_CHANGE | Prepare and validate one exact metadata-only candidate changing only the three COV-POST-001 current-facing passages in the live Root decomposition. Preserve every other byte and all named protected hashes. | Stop after exact candidate, diff, validation, and gate presentation. Do not apply. |

## Frozen inputs

- live decomposition SHA-256:
  `69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c`;
- applied PRD SHA-256:
  `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`;
- S3 applied-file evidence SHA-256:
  `f2781dd2c33f01cbaf014b2bb97fbff0bcdf1db3c46a8969f195a7d320501cc8`;
- S3 applied validation SHA-256:
  `18e00b070e7eb889043688531ed4dfcdeca2f168b4e031ba2dfe86761fd08c61`;
- S3 return SHA-256:
  `38478cd78435e771897378a241fe6b8f0a386e3d16fd3f36c18eaa61f7b1eb57`;
- post-apply audit SHA-256:
  `0c49c5e18e1d02bc9abec1b01adcf1adf5cc895b79e159259d76a470aa4630a5`;
- `_ScopeChange/_LATEST.md` SHA-256:
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`;
- scope ledger SHA-256:
  `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`;
- deliverable register SHA-256:
  `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`.

## Candidate constraints

1. Change only live decomposition lines 11, 565, and 622–623 as identified by
   COV-POST-001; line numbers are evidence locators, not permission to change
   adjacent content.
2. State completed SCA-003 candidate acceptance and application, citing the
   owner-ruling and applied-hash evidence identities.
3. Refer the human confirmation state to the SCA-003 `Decision_Log.md`; do not
   encode `pending` or `confirmed` as current-facing decomposition state.
4. Preserve immutable candidate/SCA-002 history, including historical
   candidate-era wording outside the three corrected passages.
5. Preserve scope, topology, mappings, identifiers, counts, statuses,
   substantive requirements, companion registers, PRD, and `_LATEST.md`.
6. Present an exact candidate SHA-256 and exact diff SHA-256 under an external
   owner gate. Presence or validation is not application.

## Fan-in

HELP_HUMAN accepts S4 only if live authoritative hashes remain frozen, the
candidate differs at exactly the three authorized passages, deterministic
validation proves all preservation constraints, and the return stops before
application.
