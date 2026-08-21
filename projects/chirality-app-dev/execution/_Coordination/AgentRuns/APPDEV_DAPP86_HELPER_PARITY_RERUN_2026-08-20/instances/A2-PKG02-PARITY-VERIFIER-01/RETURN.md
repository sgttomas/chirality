# A2-PKG02-PARITY-VERIFIER-01 return

Verdict: `ACCEPT_BLOCKED_FAN_IN`

Scope of acceptance: the executor return is sufficient for manager fan-in as
a truthful failed/partial instrument. This verdict does not accept parity,
the four packaged-UI observations, packaged replay rendering, full validation,
release readiness, owner-state containment, network-approval provenance, or
the parent's claimed distinct-helper trigger.

## Findings

1. **Required outputs exist.** All six D-APP-86 outputs
   (`RUN_MANIFEST.md`, `EVIDENCE_INDEX.csv`, `PACKAGED_UI_SMOKE.md`,
   `REAL_DAEMON_REPLAY.md`, `VALIDATION.md`, and `HANDOFF.md`) and the executor
   `RETURN.md` exist.
2. **Indexed evidence is complete and hash-consistent.** All 12 index rows
   resolve to files under the run root and all 12 recorded SHA-256 values
   match. The executor return hash is
   `9a85bd10197cc398b694add6ff98f01ad4f104e3769668dfec89a495dc2238c9`.
3. **Frozen source and package identities independently revalidate.** The
   509-row source manifest and 446-row package manifest both pass complete
   `shasum -a 256 -c` verification. The package has 446 regular files and 14
   symlinks. Its main executable, `app.asar`, and `Info.plist` hashes are,
   respectively,
   `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`,
   `90b3b6a8d5c63a08f5ceec86ff7cf4e86d14f2ad5b843ef3aba1e0723cdd02a9`,
   and
   `8bb6ab847fe5734d203316a73e576edb11e41787a0eaadcd3645f42bcd0d916d`.
   HEAD, tree, and branch remain
   `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`,
   `fe8ece104dd281e3219bd95fa8b121437d524520`, and
   `codex/app-dapp86-helper-parity-rerun-20260820`. There is no tracked or
   staged diff; all non-ignored untracked paths are inside this run root.
4. **The owner-state stop is evidenced without invented before-state.** The
   packaged GUI log records `desktop.cli_launcher.install` with
   `status=written` for `/Users/ryan/.local/bin/chirality` before any UI action.
   The path still has mode `-rwx------`, size `1114`, inode `45468523`, mtime
   `2026-08-20T15:26:36-0600`, and SHA-256
   `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.
   No trustworthy pre-run state exists, so this verifier does not infer
   whether the path was created, replaced, or rewritten with identical bytes.
5. **Run-owned cleanup is independently supported.** Exact PIDs `67623` and
   `67697` are absent; TCP listener `127.0.0.1:52786` is absent; and
   `/private/tmp/chirality-d86pkg02.VWKLGL` is absent, which also removes the
   recorded socket path. The owner launcher remains and was not repaired by
   this verifier.
6. **Execution claims are properly limited.** The retained logs support 6/6
   focused test files and 36/36 tests, typecheck, production build, daemon
   startup, worktree registration, and one completed two-event/one-item stub
   fixture. The evidence makes no claim that Workbench, Pipeline, guarded
   in-flight selection, post-completion selection, or packaged replay
   rendering was observed. Packaged premerge, release-quality, secret scan,
   and executor final backcheck are explicitly `NOT RUN`. The verifier's
   read-only package-manifest check now confirms the retained package still
   matches its frozen manifest; it does not retroactively convert the skipped
   executor gate to PASS.

## Required discrepancy calibration at manager fan-in

1. **Network approval provenance is not durable in this run.** The only
   retained `desktop-pack.log` ends at the sandboxed `getaddrinfo ENOTFOUND
   github.com` failure. A package exists and revalidates, but no run artifact
   records the alleged parent-routed approval or a successful retry transcript.
   The resulting package proves that a later pack completed; it cannot prove
   that the network retry was authorized. Therefore the phrases `authorized
   retry` and `successful authorized retry is established by the resulting
   frozen package` in `RUN_MANIFEST.md` / `VALIDATION.md` are unsupported as
   approval-provenance claims. Manager fan-in must preserve this as
   `authorization provenance not evidenced`, not infer either authorization
   or unauthorized execution.
2. **The claimed distinct-helper trigger did not occur as stated.** The prior
   2026-08-03 package and current package use the identical generic Electron
   main executable hash. The current daemon still executes the main
   `Chirality.app/Contents/MacOS/Chirality` binary with `--runtime-daemon`;
   source explicitly describes it as the same bundle relaunched in daemon
   mode. `app.asar` and `Info.plist` changed, and the accepted signal-shutdown
   binder is present, so there is a material payload/package difference.
   However, the package contains no daemon-specific headless helper `.app`
   implementing the D-APP-88 Option-B identity; its nested helper apps are the
   ordinary Electron GPU/Plugin/Renderer/general helpers. The 2026-08-13
   D-APP-88/D-APP-93 closure accepts the signal-binder remedy and concludes the
   failure mode; it does not evidence that the earlier R8 trigger's `later
   accepted D-APP-88 distinct-helper implementation` landed. Thus the
   parent's `bind the distinct helper identity` tasking and its assertion of a
   live distinct-helper rerun trigger are discrepant. The executor's narrower
   statement that this is a payload difference and not a distinct
   helper-bundle identity is correct.
3. **`STATUS.md` is stale parent-owned state.** It still says `EXECUTOR NOT YET
   DISPATCHED`, `Accepted child returns: none`, and holds V1, while
   `RUNTIME_EVENTS.jsonl` and the executor return show E1 finished blocked and
   V1 started. It must not be cited as current status. This staleness does not
   falsify the executor return, but manager fan-in must reconcile it.

## Fan-in boundary

Accept only these conclusions: the instrument ran partially, produced a
valid daemon-side fixture, stopped correctly on an evidenced owner-state risk,
cleaned up its run-owned runtime state, and left all UI/parity and downstream
validation claims open. The owner launcher disposition, a launcher-proof
isolation posture, correction of the trigger/identity basis, and durable
network-approval provenance remain manager/owner matters. No repair was
performed.
