# TM candidate — permission-guard fixture modes and non-macOS umask pre-staging gate

- Harvested: `2026-08-23`.
- Source: owner direction for PR #632 fixture-mode portability repair.
- Candidate only: no Task Management register row is created, accepted, triggered, or dispositioned by this record.
- Product-policy effect: none.

## Candidate

Permission-guard test fixtures must pin runtime-data directory and file modes explicitly at creation, matching the product's `0700` directory and `0600` file contract. Before any future login-proof staging, the affected suite must also run once under a non-macOS-style permissive umask such as `umask 0002` so fixture assumptions cannot be masked by the macOS default umask.

## Evidence basis

- The exact pre-fix `umask 0002` focused run reproduced 15 unsafe-permission failures / 57 passes / 72 total.
- Product inspection found explicit `0700` directory and `0600` file creation already present; no product change was required.
- The test-only fixture-mode repair passed both the ordinary focused run and a post-fix `umask 0002` run at 72/72.
- Exact test candidate revision: `b33858d33220538ce292f276a442792ecf8050b1`; test SHA-256 `7af5c15a48fea5c6f5255a57fc9a35fb7fee32a49badd44f1495f6d82c1eff4e`.

Task Management may later normalize, reject, merge, or adopt this candidate under owner disposition. This harvest does not alter proof, runtime, package, or release policy.
