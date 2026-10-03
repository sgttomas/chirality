# Native verification return and slot release

All planned serial Cargo commands finished; the native Cargo slot is released. No app bundle, desktop launch, real live endpoint, browser, CUA, old PID9925 interaction or Git mutation occurred. Only controlled process-owned test sockets were opened. Instruction origins and initial source ACK remain in ACK.md; exact commands, versions, pre-run identities, repair identities, final source/binary identities and raw logs are retained alongside this return.

## Actual results

| Command lane | Result |
|---|---|
| Library live_control filter | PASS: 8 tests; 102 unrelated tests filtered |
| Owned transport, initial sandbox run | Availability failure: 4 pass, 2 UnixListener::bind EPERM |
| Owned transport, approved escalation retry | PASS: 6 tests |
| Feature-gated CLI unit + integration | PASS: 3 + 3 tests |
| Explicit feature-gated CLI build | PASS |

Every command used locked/offline resolution, two build jobs and the manager-designated isolated target directory. RUNS.json contains exact command strings, exit codes, permission modes and raw-log hashes. PRE_RUN.json records cargo/rustc versions and initial source. The default sandbox denied temporary Unix listener binding; the exact controlled transport and CLI commands were then approved through the supported require_escalated mechanism. This was not an app/live-endpoint grant. The two initially created empty fixture directories were identified by unique generated names and common failed-run timestamp and removed with exact nonrecursive rmdir; details are in FIXTURE_CLEANUP_REPAIR.json.

One owned test reliability defect was repaired: descriptor fixture construction now installs its RAII directory guard before bind so early failures clean up. No product compile failure occurred. Between commands, manager corrected describe/docs to retire the obsolete inspection-basis1024 claim; preview256/key1024 remain. Final hashes are authoritative in FINAL_SOURCE.json. The manager-owned canonical fixture and maintained test copy remain byte-identical at revision2 SHA-256 6a35f885b5175ab9ee5c8ae9ea2290cfe118512b6476b59ff986f0aace1af8dc.

Build warnings are two dead-code warnings for descriptor limit/read_attachment in the desktop library variant (the same module is consumed by the CLI). They did not fail checks. No protected tests/oracles/limits were changed.

## Evidence scope and remaining gates

Passed coverage includes inert disabled registry, authentication/method refusal, exact envelope/frame limits, old-workspace opaque transport, main registration bookkeeping, independent dispatch IDs, stale/duplicate replies, registration replacement, original-registration disconnect cancellation, pending admission, descriptor permissions/symlinks/non-socket refusal, capability-free diagnostics, offline CLI descriptions and actual CLI/socket-fixture correlation/nonzero errors.

This is controlled carrier evidence, not complete N1–N3 or I1/I2 qualification. Actual Tauri invoking-webview identity and event delivery, optional normal desktop startup, packaging/default target selection, preserved packaged saved/edited-load self-test, connected real controller/engine publication, 30-second live timeout/concurrent connection behavior and unsupported-host cross-compilation remain unwitnessed here. Runtime retirement/recovery, native integration and actual-human single/batch H1/H2 remain pending. Agent test actions do not establish human review/Apply, engineering acceptance or release. Fresh independent candidate review remains manager/ROOT-owned.
