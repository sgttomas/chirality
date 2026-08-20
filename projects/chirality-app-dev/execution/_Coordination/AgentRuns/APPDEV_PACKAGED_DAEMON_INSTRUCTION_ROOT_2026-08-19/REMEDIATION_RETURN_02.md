# Remediation return 02 — A2-DAPP100-IMPLEMENT-02

- RunID: `APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19`
- ChildInstanceID: `A2-DAPP100-IMPLEMENT-02`
- Review basis: `REVIEW_RETURN_01.md`
- Status: `REMEDIATED — READY FOR FRESH REVIEW`

## Exact diff

- Modified `frontend/scripts/run-packaged-daemon-instruction-root-proof.mjs`.
- Added `frontend/src/__tests__/scripts/run-packaged-daemon-instruction-root-proof.test.ts`.
- Added this `REMEDIATION_RETURN_02.md`.

No production resolver, Electron main, original agreement regression, runtime,
manifest, dependency, lockfile, deliverable, decision, register, receipt, or Git
surface was changed in remediation attempt 02.

## Finding dispositions

1. `P1 deadlines/cleanup` — every spawned process now requires a positive
   deadline. Pack, codesign, bundled CLI, daemon, and GUI calls declare bounded
   deadlines. All children are tracked in one active set. Normal stop and final
   cleanup send SIGTERM, escalate to SIGKILL after a bounded grace interval, and
   await confirmed process exit; unconfirmed cleanup makes the proof fail.
2. `P1 exact artifact freshness` — an in-script pack can test only the canonical
   `desktop:pack` output. The proof captures the canonical app path and SHA-256
   content identities for the packaged executable, `app.asar`, and bundled CLI,
   writes an invocation marker, and rechecks the same identity before each
   process phase and after the GUI phase. `--skip-pack` now fails closed unless
   supplied a fresh pack-invocation identity marker whose exact path and bytes
   match the selected app; stale markers are rejected.
3. `P1 stale PASS` — the canonical summary is atomically replaced with
   `PENDING` before argument/platform/proof work. The terminal summary is also
   atomic. Every caught execution, deadline, cleanup, or temporary-cleanup error
   writes `FAIL` for the current invocation, so an earlier PASS cannot survive a
   failed rerun.
4. `P2 log offsets` — restart offsets now use JavaScript string length and
   string slicing consistently. No byte count is mixed with a UTF-16 string
   offset.

## Focused evidence

- `npm test -- --run src/__tests__/scripts/run-packaged-daemon-instruction-root-proof.test.ts src/__tests__/electron/daemon-instruction-root.test.ts` — `PASS`, 2 files / 9 tests.
- The proof-specific file contributes 5 passing tests covering:
  - command deadline and confirmed cleanup;
  - SIGTERM-resistant child escalation to SIGKILL with awaited exit;
  - exact canonical-path/content identity plus fresh/stale marker handling;
  - stale PASS replacement by atomic FAIL on invalid `--skip-pack`;
  - non-ASCII log offset correctness.
- `node --check frontend/scripts/run-packaged-daemon-instruction-root-proof.mjs` — `PASS`.
- `git diff --check` — `PASS`.

The test that intentionally exercises a failed proof prints a `status: FAIL`
summary line; that is the asserted behavior, while the Vitest result is PASS.

## Containment

Attempt-02 writes are limited to the remediation brief's three allowed targets:
the proof script, its proof-specific test, and this return. No pack or Electron
host proof ran. No commit or push was performed.

## Residual risks and manager work

- Fresh read-only review over the integrated diff remains required.
- Full package checks and the macOS arm64 packaged-under-isolation proof remain
  manager-owned. The remediated proof should normally run its own pack:

```sh
cd projects/chirality-app-dev/frontend
node ./scripts/run-packaged-daemon-instruction-root-proof.mjs
```

- `--skip-pack` is intentionally no longer valid by itself; it requires
  `--expected-app-identity <fresh app-identity.json>` and exact identity match.
