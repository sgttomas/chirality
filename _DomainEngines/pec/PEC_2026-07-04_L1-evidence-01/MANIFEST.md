# PEC L1 evidence capture 01 — MANIFEST (immutable snapshot)

> **Epistemic status: generated evidence — not authority.** Read-only L1
> evidence per the D-T0-13 O-A staging ruling and the standing plan's
> owner-intent addendum (ladder-as-core-goal, Receipt 4). Captured outputs are
> derivative packages, not substitute authority; pec's tests and source govern.
> This folder is immutable after publication — corrections go in a new
> dated snapshot, never edits here.

## Source refs

- Tree: `origin/main` @ `090cd4efb` (PR #56 merge), checked out in an isolated
  worktree; pec subtree unmodified.
- Committed inputs only: `projects/pec/` sources, tests, and fixtures.
  Fixture SHA-256 (all 4 committed fixtures):
  - `5578f06794b08b2e9c00d570797a64d23e2cb8695f6d9378352e3b857141aa5c  fixtures/decisions-sample.csv`
  - `6f546f5a88c143c9bc8e71dc9090e170099187869a8eb1448328cc97f0b5109b  fixtures/mdl-sample.csv`
  - `db6a99131d3ed339d3a0b4dc09800bd1d792f2b844d3a286df485f6c6925073b  fixtures/rail-sample.csv`
  - `3488061d501e249364acff1f270539439f35c09bc9c18eec42559a1c141014b3  fixtures/risks-sample.csv`

## Actor / visibility basis

- Actor: PEC work loop agent at owner direction (Ryan Tufts, 2026-07-04,
  "approved to merge and proceed from there" following the ladder-as-core-goal
  direction of record in Receipt 4).
- Visibility basis: D-T0-14 residency CLOSED default — committed repo files and
  scratch databases only. **No pec instance content was read, captured, or
  egressed**; no server was started; no non-scratch database was opened.

## Commands and outputs (from `projects/pec/`, deps via `npm ci`)

| Command | Exit | Output capture | Result |
|---|---|---|---|
| `npm run typecheck` | 0 | `typecheck.log` | clean across core/server/web |
| `npm test` | 0 | `test.log` | 161 tests: core 72 pass, server 89 pass, 0 fail |
| `npm run build` | 0 | `build.log` | all workspaces build |
| `npm run drill` | 0 | `drill.log` | 17/17 rehearsal checks pass on a scratch DB under the OS temp dir |

## Warnings and limitations

- Logs are run-record evidence and carry machine-absolute paths (permitted,
  SPEC §0.2.4); they are machine-specific and non-portable.
- `drill` exit 0 means the rehearsal checks passed — **not** pilot readiness,
  go-live, or any engineering-correctness claim (F-PEC-2; professional
  boundary in `_DomainEngines/profiles/pec.yaml`).
- This capture proves the deterministic-check seam of L1 only. The remaining
  L1 seams (register exports, report renders, Explain payloads) require an
  owner-provisioned session and, for instance content, the D-T0-14/D-PEC-01
  residency case — not exercised here.
