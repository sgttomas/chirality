# Validation — Root Semantic Returns Closeout

RunID: `ROOT_SEMANTIC_RETURNS_2026-08-03`

Verdict: `PASS / TM112 IMPLEMENTATION CANDIDATE REQUIRES HUMAN ACCEPTANCE`

## Authority and prerequisite checks

- The preserved owner transcript hashes to
  `6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566`.
- It contains the three unambiguous signed returns, signer `Ryan Tufts`, date
  `2026-08-03`, and all three owner additions.
- Repair commit `2b6d53027ea10374dd515a4a5a203f8ed4cf2f04` precedes every acceptance
  carrier. Root Receipt 94 and the Task Management return record failed run
  `30876341235` / job `91888465477` and passing rerun `30877532946` / job
  `91891904563`.
- `sha256sum -c` over `BASIS_MANIFEST.sha256` passes for all 25 entries.

## Snapshot and candidate checks

- TM109 exact accepted design package is bound to
  `2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489`;
  its non-selections and implementation/reliance holds remain explicit.
- TM112 semantic acceptance validates at authority-binding SHA-256
  `27052f9667896c726bcd1329686747a2f370aff521e4d9ce4556551b150c5a3d`
  and normalized carrier-manifest SHA-256 `1f623f6d…ce84`. The executed sealed
  brief's historical hash `b8163531…e6a218` and normalized publication hash
  `61751227…2e9d` are explicitly bridged without semantic drift.
- DEL-02-06's accepted semantic snapshot manifest hashes to
  `183e987585023f22c3fe0e6de36dbbd7cf63ce03c002475f90cf4d98304da300`;
  epoch, complete binding, and implementation remain held.
- TM112 product hashes equal `FINAL_PRODUCT_HASHES.sha256` and the
  implementation manager's terminal return: SPEC `647eee2d…d6a7f`, daemon
  `22440300…ddf2`, and tests `c853f207…b352`.
- The implementation validation is `PASS_WITH_NONBLOCKING_FINDINGS`; I4 has
  no material finding. Node 22.19 remains unexecuted.
- TM105 Phase-1 evidence carrier manifest hashes to `ad52a2f7…c3773` and
  verifies its bounded 21-TBD census: 8 partial, 13 blocked, 0 resolved. No
  no-TBD successor or byte gate exists.

## Register, receipt, whitespace, and containment checks

- Root live-register validation passes at 24 rows: 13 OPEN and 11 DEFERRED.
- Root closed-register validation passes at 98 rows.
- The register hashes match the Task Management terminal return and manifest.
- Receipt headings are continuous through Receipt 95, with exactly one
  Receipt 94 and one Receipt 95 heading.
- Full candidate-whitespace validation against `origin/main` passes, including
  all tracked and untracked candidate text. `git diff --check` passes.
- This manager wrote only this RunID's five closeout files and appended Receipt
  95. It did not edit registers, product files, the DEL snapshot, prior
  carriers, App/Piping, lifecycle state, the global handoff, or Git.

Structural validation and technical test evidence do not accept the TM112
product bytes. App routing and merge remain held.
