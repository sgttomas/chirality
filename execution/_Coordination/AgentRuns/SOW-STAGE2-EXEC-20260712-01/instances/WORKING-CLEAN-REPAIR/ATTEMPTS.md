# WORKING-CLEAN-REPAIR Attempts

## Attempt 1 — Piping root binding

- The sealed brief initially named the nonexistent root
  `projects/chirality-piping-design/execution/**`, so discovery returned 53 App
  members and zero Piping members.
- No project write occurred before this mismatch was reported.
- Parent corrected the mechanical path binding in place to the live accepted
  root `projects/chirality-piping/execution/**`.
- Recomputed population: exactly 57 = 53 App + four Piping PKG-13 pilots.

## Attempt 2 — project checks before Piping WASM preparation

- App typecheck, 713 tests (four skipped), and production build passed in a
  disposable copy using the existing dependency cache.
- The first Piping test/build attempt did not reach test execution or a
  production bundle because the disposable copy did not yet contain the
  required generated WASM engine. Both logs retain the exact
  `WASM-ENGINE-ASSET-ABSENT` guard result.
- Project writes: none. The disposable copy was removed.
- Disposition: run the project-declared
  `npm run build:wasm --workspace apps/desktop` prerequisite in a fresh
  disposable copy, then rerun tests and build.

## Attempt 3 — rebound Piping project checks

- WASM preparation passed.
- All 476 Piping desktop tests passed.
- The Piping desktop production build passed.
- Project writes outside the bounded 57 contracts: none. All generated build
  state remained in the disposable copy and was removed.
