# D-APP-88 R3 exact post-GUI first-signal proof

Verdict: `FAIL — TERMINAL D-APP-88 CONJUNCT`

## Exact final-bit context

- Source candidate was byte-identical to the frozen R2 candidate on all 12 helper/config/test surfaces, including package metadata.
- Clean `desktop:pack` completed with no builder `cannot find path for dependency` observations.
- Packaged dependency-boundary and 43-file instruction-root integrity checks passed.
- Helper: `dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service`.
- GUI: `dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality`.
- Isolated store: `/private/tmp/chirality-dapp88-r3.3rVHrz/user`.
- No owner login-keychain path or owner runtime state was used.

## Recovery and coexistence

- A prior absent-PID helper (`63725`) had left socket inode `25261184` and owner-record inode `25261179`.
- Final helper PID `64825` authenticated and recovered that stale state on start. It created socket inode `25329475` and owner-record inode `25329474`, both mode `0600`, with owner schema `chirality.daemon-owner/v1`.
- Helper log start: `2026-08-04T17:31:42.925Z`; listening: `2026-08-04T17:31:42.939Z`.
- GUI PID `64872` started at `2026-08-04T17:32:11.861Z` and reached the helper. Its first binding returned `Unknown project: chirality-app-dev` at `2026-08-04T17:32:11.874Z`, proving authenticated runtime contact while truthfully recording that the isolated store had no project registration.
- Pre-signal snapshot at `2026-08-04T11:33:36-06:00` showed both PIDs alive, the same socket/owner inodes, three helper Unix-domain socket descriptors, and no helper IPv4/IPv6 descriptor.

## Exact first signal and bounded observation

```text
signal_command_time=2026-08-04T11:33:54-06:00
signal_command=/bin/kill -TERM 64825
post_signal_snapshot_time=2026-08-04T11:34:03-06:00
polls=80 (0.1 seconds each)
helper_process=ALIVE
gui_process=ALIVE
socket=PRESENT inode=25329475 mode=srw------- uid=501 gid=0
owner=PRESENT inode=25329474 mode=-rw------- uid=501 gid=0 size=321
```

The helper log contained no `desktop.shutdown.started`, no `desktop.shutdown.completed`, and no daemon-stop failure after this exact signal. Therefore the Root runtime's accepted bounded `RuntimeDaemon.stop()` path was never entered. This attempt evidences an App/Electron signal seam, not a need for another generic Root semantic.

No second signal is credited toward acceptance. The D-APP-88 Option B conjunction fails.
