# P2 host XPC probe

This fixture exercises the public `@chirality/native-admission` host-XPC wrapper with isolated, synthetically signed driver hosts. It does not exercise or qualify the packaged Chirality App, its ASAR/fuses, a provider account, credentials, the supplier, a model, or a release artifact.

The executor supplies and hashes all compiled or signed inputs. The correct server and client hosts must satisfy one exact synthetic code requirement. The wrong client host must have a valid different identity, satisfy its own supplied requirement, and fail the correct requirement. The probe never signs or modifies them.

The server runs as the fixed Mach service `com.chirality.app.runtime.account-host` through a unique LaunchAgent label. Before bootstrap, the probe inspects the entire current per-user launchd domain and fails if that service name is present under any job. It never unloads an occupant. After successful bootstrap, cleanup targets only the unique label and only after `launchctl print` still names the exact expiring launcher and server host installed by this run. A mismatch fails cleanup without unloading the job.

`p2-host-xpc-expiring-exec.c` arms a 45-second `SIGALRM` before `execve` of the server driver host. POSIX alarm state survives a successful `execve`, bounding a server that hangs before JavaScript initializes. The existing reviewed `native-probe-watchdog` must wrap the probe process as the outer deadline and process-group owner. The probe does not retain or signal numeric PIDs or process groups; watchdog cleanup remains responsible for exact leader observation/reap and post-reap group absence, with no post-reap signal.

The source sequence is:

1. compile the expiring launcher into a new fail-if-present stage and inspect its architecture, minimum OS, symbols, and dependencies;
2. prepare three isolated Electron driver hosts: one server and one client satisfying the exact correct synthetic requirement, and one client satisfying only the exact wrong requirement;
3. bind the exact wrapper entry, native addon, JS driver, launcher, and driver-host file identities and code requirements;
4. invoke the existing watchdog over the exact Electron-as-Node probe host and `p2-host-xpc-probe.cjs`, passing all required `--*-sha256`, requirement, and fresh canonical `--run-root` arguments;
5. require a correct-client control, bounded wrong-client nonadmission observation, and another correct-client control, followed by the existing pending-close and bounded 65-connection terminal-delivery cases, successful owned-job cleanup, and watchdog retirement.

Each child has exclusive mode-0600 raw stdout, stderr, diagnostic JSONL, and process metadata under the fresh run root. Metadata records the exact command, argv, closed environment, spawn error, exit and signal, stream-close observation, elapsed time, byte counts, bounded retained-byte hashes, and overflow. The controller drains through child `close` before interpreting the one-result stdout contract. A parsed child FAIL is retained as the primary failure, and any cleanup failure is reported separately.

The wrong-client case passes only after the driver records successful binding load, client creation, and provision invocation; observes no client challenge or grant and no server admission/open/finish for that request; and completes an awaited local close. Its result distinguishes a supported typed remote terminal from a three-second observation expiry followed by that local close. The latter proves only bounded non-delivery against the functioning listener. Generic process exit, load/create failure, malformed evidence, delivery failure, or a missing before/after correct control is FAIL, never a peer-rejection result.

Any fixed-service occupancy, code-requirement mismatch, input-identity mismatch, timeout, cleanup uncertainty, malformed frame, unexpected pressure rejection, or missing terminal settlement makes the probe fail. Ordinary delivery or a public-wrapper terminal unavailable/closed result may satisfy the pressure observation; it is not exhaustive queue-capacity qualification.

## Driver preparation and one-shot execution recipe

The executor must start from one already accepted Electron.app extraction and a fresh mode-0700 stage. It copies that bundle three times with `/usr/bin/ditto`; the accepted source is never modified. Give the copies distinct synthetic bundle identifiers (`com.chirality.probe.server`, `com.chirality.probe.client`, and `com.chirality.probe.wrong`) using `/usr/libexec/PlistBuddy`, then sign each complete copy with the explicitly selected local signing identity and the same reviewed Electron entitlements. Do not use `--deep`; sign nested code in Electron's normal inside-out order, then the outer bundle, and verify each finished copy with `/usr/bin/codesign --verify --deep --strict --verbose=4`. These are disposable probe identities, never the production Chirality identity.

Derive each driver's actual 40-hex CDHash from `/usr/bin/codesign -d --verbose=4 <copy>/Contents/MacOS/Electron`. The correct requirement is the fixed disjunction of the server and correct-client CDHashes: `(cdhash H\"<SERVER_CDHASH>\") or (cdhash H\"<CLIENT_CDHASH>\")`; the wrong requirement is `cdhash H\"<WRONG_CDHASH>\"`. Verify both correct executables satisfy the correct requirement, the wrong executable satisfies its own, and the wrong executable fails the correct requirement. Hash the three final executable files and every other probe input only after signing; pass those exact paths and hashes to the probe. The probe repeats the executable requirement checks and never signs or mutates a host.

Compile only the expiring launcher in the fresh stage with the reviewed arm64/macOS-15 clang boundary, inspect it as an arm64-only Mach-O depending only on libSystem, and hash it. Run the already accepted watchdog once with a fresh absent run root and a closed environment:

```text
/usr/bin/env -i HOME=<fresh-home> TMPDIR=<fresh-tmp> PATH=/usr/bin:/bin:/usr/sbin:/sbin LANG=en_US.UTF-8 ELECTRON_RUN_AS_NODE=1 \
  <accepted-native-probe-watchdog> --timeout-seconds 60 --term-grace-seconds 2 --fixture-fallback-seconds 14 -- \
  <accepted-electron>/Contents/MacOS/Electron p2-host-xpc-probe.cjs \
  --addon <exact-addon> --addon-sha256 <sha256> \
  --wrapper <built-public-wrapper-entry> --wrapper-sha256 <sha256> \
  --driver p2-host-xpc-driver.mjs --driver-sha256 <sha256> \
  --expiring-exec <compiled-launcher> --expiring-exec-sha256 <sha256> \
  --server-host <server-copy>/Contents/MacOS/Electron --server-host-sha256 <sha256> \
  --correct-client-host <client-copy>/Contents/MacOS/Electron --correct-client-host-sha256 <sha256> \
  --wrong-client-host <wrong-copy>/Contents/MacOS/Electron --wrong-client-host-sha256 <sha256> \
  --correct-requirement '<correct requirement>' --wrong-requirement '<wrong requirement>' \
  --run-root <fresh-absent-run-root>
```

The executor must first inspect the fixed Mach-service namespace and stop if any owner exists. It must not unload or stop an existing job or App. The only permitted cleanup target is the unique label bootstrapped by this exact run after its Program path and server-host argument still match. Preserve raw stdout/stderr, plist, server JSONL, exact argv/environment, code-signing verification output, input hashes, and watchdog retirement evidence. Any required failure stops without retry.

For the repaired continuation after the preserved first-run failure, reuse the existing three signed hosts, expiring launcher, watchdog, Electron extraction and parity evidence only after exact rehash and requirement revalidation. Do not copy, re-sign, recompile, or re-extract those unchanged inputs. Runtime's separately reviewed ownership and wrapper-order repairs require one newly built and privately signed add-on and one freshly emitted public wrapper. Bind their new hashes together with the changed controller and driver hashes into a fresh mode-0700 run root, then run the same single `60/2/14` watchdog invocation. Preserve the failed stage unchanged. The new result is evidence only for the new frozen input set; it cannot recover or reinterpret the lost first-run diagnostic.
