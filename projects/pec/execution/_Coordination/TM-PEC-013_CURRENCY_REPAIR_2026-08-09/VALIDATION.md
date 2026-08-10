# TM-PEC-013 successor validation

## Successor validation and checklist binding

| Deliverable | Successor SHA-256 | SOW validation | Checklist rows | Checklist SHA-256 | Source-hash binding |
|---|---|---|---:|---|---|
| DEL-02-07 | `d2f898c1bc5b9b3798fe9c5b4961019c9f88366fc36e44c25c51bc878947391f` | `PASS / SOW_V1 / zero issues` | 8 | `1b3a798ea90ff053c69b9c0d7b1a50eb59d22c660c99b01a91e1c1be2b424820` | PASS; all item `source_identity.sha256` values equal successor |
| DEL-03-01 | `b2569e56927459f93865cbe4642bddbfbee96814aa79ed6b39cb3b3721246f64` | `PASS / SOW_V1 / zero issues` | 17 | `b32d9c92c22cbbd992793bb4abd91ae648f4cf311e59b319ad21677bda38a424` | PASS; all item `source_identity.sha256` values equal successor |
| DEL-04-01 | `21e696ce8ccaad88f852f6a91a4bc575c1e46601b5d3e026978a49164f2c9d89` | `PASS / SOW_V1 / zero issues` | 16 | `d605eefb1e6b9089a9b0a9f935c203b4540b9845792480d330469e0523030348` | PASS; all item `source_identity.sha256` values equal successor |

Validation used `tools/scope_of_work/validate_scope_of_work.py --json` and
checklist derivation used `tools/scope_of_work/derive_review_checklist.py`.
Any successor-byte change invalidates its listed checklist and requires both
validation and derivation to rerun.

## Preservation checks

- Preimages and accepted authority hashes reproduced before SOW editing:
  `PREIMAGE_REPRODUCTION.md`.
- `OUT-*`, `CLM-*`, `TBD-*`, `REQ-*`, `AC-*`, `CON-*`, `VER-*`, and `AX-*`
  identifier sequences compare byte-for-byte equal to their preimage
  sequences for all three SOWs.
- Semantic diff inspection found only: revision-1.4 basis pinning; replacement
  of stale OI-003-open/undecided premises; refresh of the directly dependent
  current upstream interface quotation in DEL-02-07 and DEL-03-01; and
  directly dependent AC/AX phrasing.
- DEL-03-01 `TBD-005` is unchanged. No dependency row was added, removed, or
  reclassified.
- DEL-04-01 still has exactly its existing three `EXECUTION` upstream rows,
  explicitly has no local execution edge to DEL-01-06, and obtains loop
  identity from the record tier.
- All three `_STATUS.md` and `Dependencies.csv` files are byte-identical to
  `HEAD`; no lifecycle or dependency surface changed.
- No source, decomposition, SCA, historical artifact, Task Management row,
  receipt, standing plan, PRD, REVIEW surface, or foreign-loop surface was
  written by this run.
- Targeted `git diff --check` passes. Targeted deliverable containment shows
  exactly the three intended `ScopeOfWork.md` edits.
- Stale-premise scan finds no remaining `OI-003` open/awaiting/undecided or
  later-registry-ruling phrasing in the three successors.

## Reliance and registered profile checks

- PEC reliance preflight: `ALLOW` for `dispatch-for-production` and
  `candidate-validation` on each of DEL-02-07, DEL-03-01, and DEL-04-01.
- `v2-api-contract`: PASS, 6 tests.
- `v2-core-posture`: PASS for dependency, locality, and registration when run
  from the project-profile cwd (`projects/pec`).
- `harness-self-check`: completed successfully; inherited repository-wide
  baseline remains 4 REVIEW, 31 WARN, 14 INFO, and 1 NOT_APPLICABLE, with no
  finding caused by or pointing to these three successor SOWs or their return
  package.

An initial `v2-core-posture` invocation from repository root was rejected as
an execution-cwd error (`EVALUATION_FAILURE`, source root resolved outside the
project). It was not accepted as evidence. Detection layer: registered-profile
check; failure class: invocation error; reason code: `PROFILE_CWD_MISMATCH`;
disposition: rerun from the profile-declared project cwd, which passed with
zero findings.
