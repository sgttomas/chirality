# D-APP-86 Validation Record

Overall verdict: `PASS`

All commands used the frozen source/package basis. No second package was
built. Dependency-backed commands ran only while the manager's reversible
projection was active; Cycle 01 and Cycle 02 were each restored exactly with
zero Root diff.

| Gate | Result | Evidence summary |
|---|---|---|
| Focused UI/runtime tests | PASS | Six initially resolvable suites: 48/48; with the D-APP-89 rollback probe under the reversible projection: 7 files, 58/58 |
| Typecheck | PASS | `npm run typecheck`, exit 0 |
| Production build | PASS | `npm run build`, exit 0 |
| Single package | PASS | `npm run desktop:pack`; first sandboxed invocation stopped before package creation on `ENOTFOUND`; one authorized network retry produced the sole package; dependency boundary 43 checked files PASS; instruction-root integrity PASS |
| Isolated packaged-App premerge | PASS | `npm run harness:validate:premerge`; Section 8 8/8 PASS; report-only Section 9 16/16 PASS |
| Release quality | PASS | `npm run validate:release-quality`; full Vitest 142 files pass / 1 skipped, 1111 tests pass / 4 skipped; typecheck PASS; blocking Section 9 16/16 PASS; packaged premerge 8/8 PASS and report-only Section 9 16/16 PASS; summary consistency PASS |
| Receipt contract | PASS | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .`; frozen through Receipt-52, versioned contract satisfied |
| Authority corpus | PASS | v18; eight MATCH; zero drift |
| Practitioner status | PASS | 53 deliverables, all `IN_PROGRESS`; no finding severities |
| Practitioner self-check | PASS | exit 0; existing baseline only: REVIEW=4, WARN=31, INFO=14, NOT_APPLICABLE=1 |
| Practitioner pytest | PASS | 349 passed in 15.23s |
| Source manifest | PASS | 380/380 hashes match frozen manifest |
| Package manifest | PASS | 446/446 hashes match frozen manifest |
| D-APP-89 guard | PASS | `assert-harness-contract-deps.mjs` passes; zero executable consumers outside the retained 13-probe rollback test; full release suite includes the rollback test |
| Six historical UNKNOWN | PASS | 6/6; authoritative CSV SHA-256 `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`; zero diff |
| Whitespace | PASS | `git diff --check`, exit 0 |

## Exact packaged-App validation environment

The premerge and release-quality commands used:

```text
TMPDIR=/private/tmp/chirality-dapp86-parity-r2.wfbKam
HARNESS_BASE_URL=http://127.0.0.1:52812
HARNESS_PROJECT_ROOT=/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev
CHIRALITY_RUNTIME_PROJECT_ID=chirality-app-dev
```

The standalone premerge run first used the child `tmp/` directory under that
same root and passed. The first release-quality wrapper then exposed a macOS
AF_UNIX path-length limit in one full-suite test:
`listen EINVAL .../tmp/chirality-desktop-cli-lock-.../runtime/control.sock`.
That wrapper truthfully recorded `fail` although its typecheck, Section 9,
premerge, and summary-consistency checks passed. No product byte changed. The
exact wrapper was rerun once with `TMPDIR` shortened to the already-authorized
Retry-02 root; the affected test and entire wrapper passed. This is recorded
as an environmental retry, not erased or recast as a product failure.

Final release-quality summary SHA-256:
`6718f0f5e3214f4344e1691d12d78255ad2e1f22b686f06553ba8017617b2a29`.
Final Section-8 summary SHA-256:
`264d5ecab7f9fd9bc9832814765876c94204f8fe2653dad32d9006bb4a63acb9`.
Final Section-9 summary SHA-256:
`d44d6e0e357a4dc324b7a3b299359747bc259a580c4f8c73ecdb499c79fa4f4d`.

## Skips and claim boundary

The full Vitest run reported one skipped file and four skipped tests under the
repository's declared test conditions. The release-quality wrapper itself
recorded no skipped command and used no `--skip-premerge` reason. No
provider-backed validation was invoked or silently represented as passing:
the run intentionally supplied no provider credential and all live turn proof
used the deterministic stub adapter. The wrapper's four governed commands all
ran and passed.

These checks are software evidence only. They do not publish, issue, certify,
seal, authenticate, notarize, or approve a release.
