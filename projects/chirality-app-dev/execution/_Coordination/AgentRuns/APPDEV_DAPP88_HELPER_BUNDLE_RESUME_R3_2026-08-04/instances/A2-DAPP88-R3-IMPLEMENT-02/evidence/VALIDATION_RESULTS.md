# R3 validation results

Terminal result: `BLOCKED` because the mandatory exact post-GUI first `SIGTERM` did not enter App teardown.

## Passing checks

- Focused helper/IPC/CLI/posture/shared-daemon Vitest: 5/5 files, 32/32 tests.
- Full frontend Vitest: 143 passed / 1 skipped files; 1,113 passed / 4 skipped tests.
- Browser and Electron TypeScript checks: PASS.
- Next/Electron/runtime CLI build: PASS.
- Clean standalone-helper plus GUI directory package: PASS after the fully materialized, validation-only dependency projection.
- Builder missing-path census on the final package: zero `cannot find path for dependency` messages.
- Packaged dependency boundary: PASS; zero local package entries and all required production packages present.
- Instruction-root integrity: PASS, 43 files; independent source-completeness advisory remains `needs_remediation`.
- App hold registered check: PASS; 53 contracts, zero held, register match true.
- `validate:release-quality` contract-dependency lint, full test, typecheck, and all 16 Section 9 checks: PASS before the overall premerge-derived failure.

## Failed or incomplete checks

- Mandatory post-GUI first-signal proof: FAIL; see `FIRST_SIGNAL_PROOF.md`.
- Registered managed-service premerge: FAIL. Service reached READY, but emitted `EMFILE` watcher diagnostics and returned 404 for the expected routes; zero premerge tests ran.
- Release-quality final status: FAIL because premerge status was fail; `RELEASE_QUALITY_TEST_COUNT` for Section 9 was 16 and passing.
- Practitioner pytest: environment failure, `/usr/bin/python3: No module named pytest`.
- Practitioner self-check: environment failure, PyYAML unavailable to the registered interpreter.
- SafeStorage continuity was not rerun because the owner login-keychain prompt is forbidden. Prior accepted cross-bundle continuity evidence remains SHA-256 `ac48762937a047b83c63324861cd22482f74f8fa16955b0452bd18cee2c71abd`; no new acceptance credit is claimed.
- Node 22.19 was not executed; Node 24 was the active runtime.

Normalized registered-check evidence is `validation/registered-checks.json`.
