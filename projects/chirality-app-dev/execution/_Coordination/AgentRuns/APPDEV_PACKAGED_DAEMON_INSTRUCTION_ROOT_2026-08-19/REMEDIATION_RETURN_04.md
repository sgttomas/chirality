# Remediation return 04 — A2-DAPP100-IMPLEMENT-04

- RunID: `APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19`
- ChildInstanceID: `A2-DAPP100-IMPLEMENT-04`
- Status: `REMEDIATED — READY FOR MANAGER HOST RERUN`

## Exact diff

- Modified `frontend/scripts/run-packaged-daemon-instruction-root-proof.mjs`.
- Updated `frontend/src/__tests__/scripts/run-packaged-daemon-instruction-root-proof.test.ts`.
- Added this `REMEDIATION_RETURN_04.md`.

No product, runtime, manifest, dependency, lockfile, deliverable, decision,
receipt, or Git surface was changed.

## Repair

The macOS proof no longer derives its runtime/userData tree from `os.tmpdir()`,
whose `/private/var/folders/...` expansion made `runtime/control.sock` exceed the
Darwin Unix-domain-socket path limit. It now:

- canonicalizes the fixed short prefix `/private/tmp`;
- allocates one collision-safe `ch-d100-*` directory with `mkdtemp`;
- uses short `u`, `c`, and `h` children for userData, isolation cwd, and HOME;
- computes the exact UTF-8 byte length of `<userData>/runtime/control.sock`;
- fails and cleans the allocation before spawning anything if the path exceeds
  the declared 103-byte maximum;
- records the exact socket path and byte length in the proof summary.

All attempt-02 deadline, tracked-child, SIGKILL cleanup, app-identity,
PENDING/FAIL atomic evidence, and non-ASCII offset protections remain in place.

## Focused evidence

- `npm test -- --run src/__tests__/scripts/run-packaged-daemon-instruction-root-proof.test.ts` — `PASS`, 6/6 tests.
- New deterministic regression verifies the selected prefix is exactly
  `/private/tmp/ch-d100-`, the derived userData and socket paths are short, the
  recorded byte count is exact, and it is at or below the platform bound.
- `node --check frontend/scripts/run-packaged-daemon-instruction-root-proof.mjs` — `PASS`.
- `git diff --check` — `PASS`.

The intentional stale-PASS invalidation test prints one `status: FAIL` summary
line; the Vitest file itself passes.

## Containment and manager rerun

Attempt-04 writes are limited to the proof script, its focused test, and this
return. No pack or host proof was run. No commit or push was performed.

Exact manager host rerun command:

```sh
cd projects/chirality-app-dev/frontend
node ./scripts/run-packaged-daemon-instruction-root-proof.mjs
```
