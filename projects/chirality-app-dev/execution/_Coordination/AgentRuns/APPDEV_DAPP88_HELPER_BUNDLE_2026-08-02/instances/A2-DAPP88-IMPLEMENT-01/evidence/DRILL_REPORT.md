# Isolated packaged-bit drill report

No live owner credential or login-keychain operation was performed. All runs used exact temporary homes, unique LaunchAgent labels, isolated userData, and `stub` provider posture.

## Passed observations

The observations below are bounded to the sanitized logs and recovered terminal
excerpts indexed in `raw-salvage/RAW_EVIDENCE_INDEX.md`. Later final-run raw
terminal streams were not independently retained; the recovered excerpts do
not establish facts beyond the quoted process, socket, CLI, and shutdown
observations.

- Relocatable-link candidate started as helper PID `31453`; helper-local GPU/network child processes resolved without ICU failure after relative symlinks were preserved.
- A fresh helper-only SIGTERM routed through `before-quit`, logged shutdown start/completion, exited 0, and removed its control socket.
- Final conventional-name candidate PID `32164` remained stable, and packaged CLI `daemon status` returned `status=ok` with the same PID and full registered engine inventory.
- GUI PID `32218` launched concurrently against the same isolated userData while the helper owner record remained PID `32164`; no helper TCP listener was present.
- SIGKILL recovery was independently demonstrated earlier in the run: killed PID `22313` restarted against the same stale state as PID `29500`, reclaimed the socket, and remained stable.

## Blocking observation

After GUI coexistence and GUI exit, helper PID `32164` did not honor the first SIGTERM. A second SIGTERM terminated it without graceful logs and left the socket present. A fresh no-GUI control PID `32383` again handled one SIGTERM gracefully and removed its socket, isolating the anomaly to the coexistence sequence.

A helper-only SIGUSR2 diagnostic was then packaged. After GUI coexistence, PID `35524` ignored SIGUSR2 as well and retained the socket. Therefore a wrapper that merely translates LaunchAgent SIGTERM into a JS-handled alternate signal is not a demonstrated solution.

Two fully distinct executable/name experiments were also rejected by Electron before JavaScript (`electron_main_delegate_mac.mm:66`, `Unable to find helper app`), both with renamed and conventional child-helper naming. Electron 43.2's pre-JavaScript child lookup therefore constrains this copied-main technique to the product executable/name.

## SafeStorage boundary

The accepted predecessor F1 return (SHA-256 `ac48762937a047b83c63324861cd22482f74f8fa16955b0452bd18cee2c71abd`) proved cross-bundle-identifier decrypt continuity with byte-identical ciphertext and no new service name. That run also established that repeating the probe against the owner's ad-hoc login-keychain identity can prompt. This run correctly did not repeat it.

## Cleanup

- Exact diagnostic PIDs were stopped or force-cleaned; no process from this worktree's packaged app remained.
- Unique label `com.chirality.runtime.dapp88.usr2` was absent from `gui/501`; no LaunchAgent was installed.
- All 19 exact temporary trees (566 files; 578,359,296 allocated bytes) had zero open holders and were removed; the post-delete match count was zero. See `CLEANUP_ADDENDUM.md`.
- `runtime/node_modules` was restored to inode `22189023`, mode `drwxr-xr-x`, uid `501`, gid `20`, size `96`, directory mtime `1785698126`; backup absent; Root runtime tracked diff clean.
- No token bytes are retained in evidence.
