# Integrated validation — DEL-02-06 acceptance and D-GOV-34 tranche

Result: `PASS`

Validated head before after-the-fact Receipt 113:
`246e8fba0b0d1806cbeafc88b641ece79dc36e4c`.

## Exact identities

- branch base: `33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0` (`commit`);
- accepted candidate: `14191` bytes, SHA-256
  `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`;
- accepted compatibility snapshot SHA-256:
  `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4`;
- D-GOV-34 candidate commit:
  `8e704f2b63302c8568c48f8fee7c4681e3ec4262`;
- `agents/AGENT_CHANGE.md` pre/post SHA-256:
  `950e96f4cfff13af48b9edd93a4b47356e8b388a430d70977fd528ffbd4120fa` /
  `bb2922c5761395687caf120097276806769ec38f4fee8935d9e6c7bbb8506a06`;
- final Root live/archive SHA-256:
  `cd0f1b96c500bcf7bc0886a0d5d20459129b10a86b4f106798a560432adcb5e9` /
  `c05a15d4886ca57dba8460f85be196f239cccf5a1b2394748f1ae90ec91e686c`.

## Integrated checks

- Root G0–G4: PASS; G4 contains 42 valid manifests.
- Agent instructions: 34 files, 0 errors, 0 warnings.
- Instruction entrypoints: PASS.
- Root live/archive Task Management validation: PASS, 21 / 106 rows.
- Invocation-local federation: COMPLETE, four registers, 79 typed findings,
  zero register writes.
- DEL-02-06 `SOW_V1`, candidate validator, 6/6 negative cases, member and
  snapshot manifests, exact byte/hash gate, historical preservation, and
  candidate whitespace: PASS.
- `python3 -m pytest -q tools/taskmgmt tools/validation
  tools/practitioner_harness`: 719 passed.
- Practitioner self-check: exit 0 with standing findings only.
- Git diff hygiene and node write containment: PASS.

## Publication state

PR #607 was opened against `main` with the four owner-prescribed dependency
commits. `origin/main` advanced after branch creation through App-owned PR
#606. No sync, rebase, artifact-proof label, or merge was performed. Required
PR checks were in progress when Receipt 113 was prepared; rerun/terminal check
results belong to the final PR head after the receipt commit is pushed.
