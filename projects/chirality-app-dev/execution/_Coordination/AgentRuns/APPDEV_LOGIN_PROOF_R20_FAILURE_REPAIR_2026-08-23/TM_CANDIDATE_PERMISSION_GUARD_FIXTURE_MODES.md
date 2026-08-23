# TM candidate — permission-guard fixture modes, host identity, and path portability

- Harvested: `2026-08-23`.
- Source: owner directions for PR #632 fixture-mode and UID portability repairs.
- Candidate only: no Task Management register row is created, accepted, triggered, or dispositioned by this record.
- Product-policy effect: none.

## Candidate

Permission-guard test fixtures must pin runtime-data directory and file modes explicitly at creation, matching the product's `0700` directory and `0600` file contract. Before any future login-proof staging, the affected suite must also run once under a non-macOS-style permissive umask such as `umask 0002` so fixture assumptions cannot be masked by the macOS default umask.

The pre-staging portability check should also sweep fixtures, expected diagnostics, service-domain strings, and temporary paths for hard-coded UID, GID, home/path, username, and host-layout assumptions. Real host identities should be derived from the runtime where the test contract permits it; intentionally mismatched identities must be derived distinctly and explicit root-UID rejection cases must remain literal. CI is the arbiter for portability across host-identity classes: a local macOS pass is supporting evidence, not a substitute for the CI host matrix, and this candidate does not authorize provider expansion.

## Evidence basis

- The exact pre-fix `umask 0002` focused run reproduced 15 unsafe-permission failures / 57 passes / 72 total.
- Product inspection found explicit `0700` directory and `0600` file creation already present; no product change was required.
- The test-only fixture-mode repair passed both the ordinary focused run and a post-fix `umask 0002` run at 72/72.
- A later CI host exposed the remaining hard-coded UID-501 fixture assumption. The bounded test-only repair derives the real fixture UID from `process.getuid()`, mismatch fixtures as that UID plus one, and retains root UID zero as an explicit rejection case.
- The final ordinary and `umask 0002` focused runs each passed 72/72; the local-socket full suite passed 1,282 with 4 skips. CI remains the host-identity arbiter and is not claimed complete by this candidate.
- Exact test candidate revision: `2ee96958daf997b7a156f020739bde43ca78ebf9`; test SHA-256 `77ff11055fa5c110001d37784e0a344a7f7874fcc3c69a2b62b5b7722c5e5bd7`.

Task Management may later normalize, reject, merge, or adopt this candidate under owner disposition. This harvest does not alter proof, runtime, package, or release policy.
