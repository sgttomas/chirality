# Exact packaged Electron matrix — causal result

Status: `CONFIRMED_BLOCKER`

## Frozen comparison

- Git basis: `cdc76a1d398231267f1379e7143b4de27abaa01b`.
- Runtime: Node `24.18.0`; packaged Electron `43.2.0`. Node 22.19 remains unexecuted.
- Both variants used the same frozen R2 candidate, diagnostic instrumentation, package configuration, ordinary-copy dependency projection, accepted `@chirality/*` projections, GUI bundle identity, helper identity, topology, isolated HOME/userData, and direct-launch test sequence.
- The only source difference was removal of exactly `app.commandLine.appendSwitch('single-process');` from `electron/runtime-helper-entry.ts`; `disable-gpu` remained.
- SINGLE entry SHA-256: `7e0ab20f14d634f9ce4e77fcfa55826cf4b0c022828acaee0709b8927123e2bc`.
- STANDARD entry SHA-256: `970d6d8ddf00096b9c4cb3b0e82514e11355917accafa69dae13d002612ce234`.
- Common instrumented `electron/main.ts` SHA-256: `82e9a8dad10f55730dce99489f9b8eca1c221f9497a81903ce9dd518b4632239`.
- Each helper contained 446 regular files and 14 relative symlinks. The symlink manifests were identical. Exactly two regular-file hashes differed: `Contents/Resources/app.asar` and integrity-bearing `Contents/Info.plist`; there were zero added or removed files.
- Helper `app.asar`: SINGLE `e702765c7ba0bed018cd4a751db6398d3ec0b3576f23f467ddff801ee671b985`; STANDARD `627ada9c8c4c1ce8c9f326e7cd3d2ae1f428874fad5a5f1f8d55525c37604560`.
- Native helper executable remained `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`; identifiers remained `com.chirality.app.runtime-helper` / `LSUIElement=true` and GUI `com.chirality.app`.

## Runtime matrix

| Variant | Phase | Helper PID | GUI PID | Ready/contact | First SIGTERM result | Earliest lifecycle event | Root stop | Socket/owner |
|---|---|---:|---:|---|---|---|---|---|
| SINGLE | pre-GUI control | 81306 | — | ready at poll 3 | exited poll 2, code 0 | `before-quit.entry` | before/resolved | removed |
| SINGLE | restart + post-GUI | 81840 | 81898 | helper ready poll 2; registration exit 0; authenticated GUI bound poll 2 | exited poll 2, code 0; GUI stayed alive | `before-quit.entry` | before/resolved | removed |
| STANDARD | pre-GUI control | 83291 | — | ready at poll 23 | exited poll 2, code 0 | `before-quit.entry` | before/resolved | removed |
| STANDARD | restart + post-GUI | 83398 | 83413 | helper ready poll 2; registration exit 0; authenticated GUI bound poll 2 | exited poll 2, code 0; GUI stayed alive | `before-quit.entry` | before/resolved | removed |

The post-GUI SINGLE socket/owner pair was inode `25678402` / `25678401`, mode `0600`; STANDARD was inode `25681587` / `25681586`, mode `0600`. Both helpers had three Unix-domain descriptor lines and zero TCP descriptor lines before signal. Both pairs were absent after first-signal settlement.

No helper arm reached the JS `SIGTERM` callback or `will-quit`; Electron first surfaced the native signal through `before-quit`. Both then reached `teardown.entry`, `runtimeHost.stop.before`, `runtimeHost.stop.after`, and `quit.entry` in the same order. This locates the successful instrumented path and excludes `single-process` as a cause or contributor in this exact comparison.

## Calibration and limitation

The first sandbox-contained SINGLE launch aborted with code 134 before `ready` or any main-module log. It is retained as context-only execution-substrate evidence. Re-execution in the macOS GUI session reached ready and supplied the matrix facts above.

The synchronous diagnostic logger is identical in both variants, so the relative SINGLE-versus-STANDARD inference is controlled. It nevertheless changes `electron/main.ts`, adds lifecycle listeners, and performs synchronous filesystem writes inside callbacks. The both-pass result therefore does not prove that the uninstrumented R2 package must pass, and it does not explain the earlier R3 post-GUI failure. It proves only that removing `single-process` is not supported as a remedy by the required instrumented matrix.

## Terminal classification

`CONFIRMED_BLOCKER`: neither exact arm reproduces the failure, and no causal App-native remedy is supported. The next technical boundary is an exact replay of the earlier R3 intervening launch/contact/timing sequence with non-perturbing native/Electron event capture sufficient to identify what state existed between authenticated GUI contact and the failed first signal. No wrapper, supervisor, extra singleton, weakened first-signal gate, Root change, or acceptance claim follows.
