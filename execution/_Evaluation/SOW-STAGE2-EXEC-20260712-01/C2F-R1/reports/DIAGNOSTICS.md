# C2F-R1 Read-Only Diagnostics

Frozen canon basis: `main@e150c972889d05a8fc270239451a35c7512dc9a9`

## Inventory, hash, and containment results

- P0 exact caller rows: `64`; aggregate rows excluded from the exact set: `8`.
- Current P2_ROOT caller rows: `64`; exact surface-set delta from P0: `0`.
- Dispositions remain `58 ACTIVATE`, `5 RETAIN_LEGACY`, and
  `1 DERIVATIVE_REGENERATE`.
- Frozen App callers: `9`; App rows absent from P0: `0`.
- Root-owned manifest rows: `55`; current post-hash mismatches: `0`.
- App rows: `9`; current final-hash mismatches after applying C2A-R1's two
  repair hashes: `0`.
- Current subject diff: `52` paths = `48` root + `4` App; root/App
  intersection: `0`; set gap against the two changed-path manifests: `0`.
- Forbidden deliverable/control/status/lifecycle/receipt/release paths in the
  subject diff: `0`.
- Live canon SHA-256 values exactly match P1_CANON:
  standard `7f742901...a6f`, SPEC `915c3b59...e27`, TYPES
  `5094610a...2ae`.
- `.claude-worktrees/` was excluded from diagnostics and was not touched.

## Remediation hashes

Root live hashes match C2R-R2 exactly:

- `common.py` — `c996955374833be390d8a9c0fdbb8ed0acef629204b38de8e312a963d6ea3214`;
- converter — `8ddef1b65f337f7091156c579558bbe8adb245a8afa43295f9d041724f203ec9`;
- root test — `586646790dfe21efb7ad47cca5a77fa7561e0be014d8d7fa0adf5360e2af876c`;
- reporting fixture — `9d7263c359c9d38b7ef1918b8ef01915e21c5bb2048491902c0fb4b2003065ce`.

App live hashes match C2A-R1 exactly:

- `filesystem.ts` — `3f3a45c6dd09c35e51f22f651399f70fbae33a17021ebdf531e192ee11b2dc3f`;
- scanner test — `295fbb0369b448534de6c1bb56fbecd35df6fc2f595b96677ed2e96ed1b0ebaf`.

## Recorded checks accepted at matching identities

- Root C2R-R2: 18 focused and 791 full tool tests PASS; compile, diff hygiene,
  and containment PASS. Unchanged initial agent/skill/export/practitioner
  evidence remains bound in P2_ROOT TEST_RESULTS.
- App C2A-R1: 7 focused files / 76 tests including 15 scanner cases; full
  frontend 713 passed / 4 skipped; typecheck, build, self-check, practitioner
  pytest 264, owned-server premerge, containment, and diff hygiene PASS.
- Every C2A-R1 `*RESULTS.json` status inspected was `PASS`; source hashes match
  the terminal return and review.

No expensive suite was rerun because current identities and terminal evidence
were neither missing nor disputed.

## Direct padded-authority reproduction

The repaired common resolver compares raw equality, but the active checklist
CLI performs this normalization first:

```python
migration_authority = args.migration_authority.strip()
```

The reproduction generated a valid dual-format candidate bound to the exact
ruled marker, then invoked `derive_review_checklist.py` with a supplied value
containing one leading and one trailing space around the ruled token.

Observed result:

- exact-authority conversion return code: `0`;
- padded-authority checklist return code: `0` (expected non-zero);
- checklist output exists: `true` (expected false);
- output format: `MIGRATION_DUAL`;
- reported authority: normalized exact ruled token.

The emitted output is
`reproduction/padded-checklist/padded-authority-output.json`, SHA-256
`9375ef877e724d435d6ca60fbf584e6b44c8665fa9a1feac85b8f10c6932b4f6`.
Its source candidate SHA-256 is
`e287ee48331475fb84b17f1b4d0a180a0864174914e15153d092a831e95efa78`.

The existing padded regression covers converter and validator seams, while the
checklist negative test covers unruled authority but not padded ruled authority.
The full-suite PASS therefore does not exercise this mandatory state.
