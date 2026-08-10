# D-APP-88 R3 exact-bit drill report

## Result

`BLOCKED / SOURCE ROLLED BACK AFTER EVIDENCE FREEZE`.

The separately built helper package passed source, package, identity, topology, CLI routing, stale-state recovery, explicit SIGKILL recovery, fresh no-GUI graceful stop, no-TCP, dependency, and instruction-root checks. It failed the mandatory first post-GUI `SIGTERM` conjunct.

## Decisive sequence

1. Exact frozen candidate bytes were reconciled hunk-wise, built, and packaged with distinct GUI/helper identities.
2. The final helper recovered an absent-PID stale socket/owner and started against an isolated store without login or owner runtime state.
3. The packaged GUI installed a CLI launcher whose `daemon_executable` named the embedded standalone helper. GUI authenticated contact reached the daemon and truthfully returned `Unknown project: chirality-app-dev` because the isolated store had no registration.
4. Pre-signal evidence showed helper PID `64825`, GUI PID `64872`, three helper Unix-domain socket descriptors, and zero TCP descriptors.
5. Exact first command `/bin/kill -TERM 64825` at `2026-08-04T11:33:54-06:00` left the helper alive after 8 seconds with unchanged socket and owner inodes and no App shutdown log entry.
6. A separate diagnostic reproduced first-signal survival and showed a second `SIGTERM` terminates immediately without cleanup, leaving socket/owner state.
7. An explicit SIGKILL/restart drill proved authenticated stale-state recovery. A fresh no-GUI first `SIGTERM` then logged both shutdown entries and removed socket/owner in one poll.

The contrast is precise: the accepted Root stop code succeeds when App teardown calls it, but post-GUI helper `SIGTERM` never reaches `desktop.shutdown.started`. No further generic Root semantic is evidenced by this run. A separate diagnosis node should investigate the App/Electron signal seam.

## Preservation

- No token value, credential value, secret, or API key was read or printed.
- Owner login keychain, owner HOME, owner runtime state, and owner LaunchAgent were untouched.
- No launchd job was installed; job-equivalent direct launch was used.
- No Root source, D-APP-89/D-APP-91 source, decision/TM/receipt, Git, signing, notarization, publication, DMG, or distribution surface was changed.
- Product source/config/test was restored to exact pre-R3 bytes after evidence freeze.
