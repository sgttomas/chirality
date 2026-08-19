# Remediation return 03 — A2-DAPP100-IMPLEMENT-03

- RunID: `APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19`
- ChildInstanceID: `A2-DAPP100-IMPLEMENT-03`
- Status: `FIXTURE REPAIRED — HOST FOCUSED RERUN REQUIRED`

## Exact diff

Modified only
`frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`:

- `createProjectFixture()` now resolves the declared manifest instruction root
  before creating `agents/`.
- `AGENT_HELP_HUMAN.md` is written beneath that resolved instruction root.
- `agentsOverlay` is rendered relative to the manifest with the same declared
  instruction-root prefix.

The agreement case still declares `workingRoot: .` and `instructionRoot: ..`,
and still asserts that the daemon resolves the canonical parent instruction
root rather than working root or packaged resources.

## Focused result

Command run:

```sh
cd projects/chirality-app-dev/frontend
npm test -- --run src/__tests__/electron/daemon-instruction-root.test.ts src/__tests__/scripts/run-packaged-daemon-instruction-root-proof.test.ts src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts
```

Result inside the session sandbox:

- resolver and proof-script files: `PASS`, 9 tests;
- shared-daemon integration file: all 3 cases blocked before fixture/session
  assertions by sandbox socket denial:
  - Unix socket `listen EPERM` for two cases;
  - loopback TCP `listen EPERM` for one case.
- aggregate: 12 discovered, 9 passed, 3 host-capability blocked.

No failing assertion implicated the repaired fixture. No integration PASS is
inferred. Manager should request host escalation for the exact command above.

## Other checks

- `git diff --check` — `PASS`.
- Attempt-03 changed-path containment — `PASS`, zero violations.

## Containment and readiness

Attempt-03 writes are limited to the one allowed integration test and this
return. No production, proof-script, runtime, manifest, dependency, lockfile,
deliverable, Git, pack, or Electron-host write/action occurred. The fixture is
ready for the host-capability focused rerun and then fresh integrated review.
