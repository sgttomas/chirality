# D-APP-88 R2 standalone-helper drill report

## Result

`BLOCKED`. The separately built Electron helper package was structurally valid and the retained log proves that a fresh helper stopped gracefully. After GUI coexistence, retained logs prove helper PID `40416` start, GUI PID `40427` contact, no post-GUI shutdown entry, and later GUI transport loss. The operator observed first-signal survival and socket retention, followed by termination on a second signal, but no contemporaneous command, process, or socket snapshot was preserved to bind that observation independently. The mandatory post-GUI first-signal graceful-stop proof therefore failed; the candidate was not retained in product state.

## Final candidate package

- Separate builder config: `electron-builder.runtime-helper.json`.
- Standalone target: `dist-runtime-helper/mac-arm64/Chirality Runtime Service.app`.
- Embedded whole-bundle target: `Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app`.
- GUI bundle identifier: `com.chirality.app`.
- Helper bundle identifier: `com.chirality.app.runtime-helper`.
- Helper UI posture: `LSUIElement=true`.
- Product/executable name: `Chirality Runtime Service`. The terminal word `Helper` was avoided because electron-builder reserves that suffix and removes it from the main executable name.
- Four builder-generated Chromium child applications used the `com.chirality.app.runtime-helper.helper*` identifier family.
- Standalone and embedded helper main-executable SHA-256: `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.
- Standalone and embedded helper `app.asar` SHA-256: `ca938dfc9c6886c1c9b682f05000e73684a79b27b16a37bb52333d094f89dc80`.
- Symlink census: 14 relative links, zero absolute links.
- Exactly one top-level helper was embedded.

## Drill sequence on exact final bits

1. Helper PID `40377` started in isolated user-data/home state and bound the Unix control socket. First `SIGTERM` logged `desktop.shutdown.started`, then `desktop.shutdown.completed`, exited zero, and removed the socket. This is directly preserved in `raw/desktop-daemon.log` lines 1–4.
2. Helper PID `40416` restarted against the same isolated store. GUI PID `40427` then started against the same user-data and socket. The GUI reached the helper sufficiently to receive `Unknown project: chirality-app-dev`; the helper remained the distinct socket owner and logged no activate/open/fork event. This does not prove shared project/session persistence because the project-registration probe produced no usable result.
3. The operator observed that first `SIGTERM` to helper PID `40416` after GUI coexistence did not enter the App shutdown log path, left the process alive, and retained the socket; the operator then observed termination after a second `SIGTERM` without teardown. The preserved evidence independently proves only the absence of a later daemon shutdown entry and the GUI's subsequent transport loss. Because the signal command, process-survival check, and socket-retention check were not preserved, the stronger failure observation is unauditable. The conservative terminal blocker is failure to produce the required auditable post-GUI first-signal graceful-stop proof.
4. The GUI subsequently recorded inability to reach the socket and then completed its own ordinary shutdown; see `raw/desktop-main.log`.

No TCP listener was observed. No token or credential content was copied or printed. No launchd job was installed; the helper executable was used as the direct job-equivalent launch target.

## Claim-calibrated causal lead

The available evidence does **not** prove a root cause or independently prove post-GUI signal survival/socket retention. It supports a Root-side investigation hypothesis: an active GUI connection may prevent the Root daemon's awaited Node server close from completing. Root `runtime/packages/daemon/src/runtime-daemon.ts` SHA-256 `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46` lines 90–101 await `server.close(...)` before unlinking the socket and owner record. The App shutdown path in frozen candidate `electron/main.ts` SHA-256 `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491` lines 710–744 awaits `runtimeHost.stop()` before it can log `desktop.shutdown.completed`. The retained evidence proves a fresh graceful shutdown, then helper restart, GUI contact, absence of a post-GUI daemon shutdown entry, and subsequent GUI transport loss. That contrast is consistent with, but does not establish, a connection-lifetime shutdown defect.

Requested follow-up: the Root runtime owner should test `RuntimeDaemon.stop()` with a live Unix-socket client/SSE or other long-lived response and determine whether explicit connection draining is required. No Root source change is authorized or proposed by this return.

## Validation completed before the terminal blocker

- Focused Vitest: PASS, four files / 30 tests.
- Typecheck: PASS.
- Electron build: PASS.
- Separate helper builder: PASS after an authorized network retry for an initial `github.com ENOTFOUND`.
- Clean `desktop:pack`: PASS.
- Dependency boundary: PASS.
- Instruction-root integrity: PASS, 43 checks, with the standing source-completeness residual unchanged.
- Package identity, child topology, relocatability, exact embedding hashes, and top-level helper census: PASS.

The full frontend suite, registered premerge/release-quality sequence, safeStorage rerun, and later recovery scenarios were not run after the decisive preservation failure. Prior accepted safeStorage continuity evidence remains hash `ac48762937a047b83c63324861cd22482f74f8fa16955b0452bd18cee2c71abd`; the owner login keychain was not touched.

## Containment

All R2 product/config/test changes were removed after evidence freeze. D-APP-89 concurrent bytes, Root runtime source, lifecycle state, Checking Approval SHA, and the six D-APP-81 UNKNOWN relations were preserved.
