# Diagnosis — PR #632 fixture-mode portability

## Exact reproduction

- Workdir: `projects/chirality-app-dev/frontend`.
- Command, invoked exactly once: `umask 0002; ./node_modules/.bin/vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`.
- Exit: `1`.
- Counts: `1` failed test file; `15` failed, `57` passed, `72` total.
- First divergence/error: `Failure-log identity or auth snapshot is unsafe; retained only in private runtime data: Failure-log directory identity or permissions are unsafe`.
- Complete captured output: `focused-umask-0002.log`. The terminal output was transcribed without terminal blank-line padding; the test was not rerun.

## Confirmed mechanism

The focused fixture substitutes `deps.runCommand` for the packaged install. That fake install creates four guarded runtime directories using recursive `mkdir` without a mode and three guarded files using `writeFile` without a mode. With `umask 0002`, default directory creation becomes `0775` and default file creation becomes `0664`. The real proof harness had already created `runtime-data` as `0700`, so `validateSnapshotAncestors` accepts it and next rejects the fake install's `runtime-data/runtime` because `0775 & 0022 != 0`. Snapshot acquisition therefore returns private-only, `failureLogsCopied` becomes false, runtime data is retained, and 15 tests diverge from their intended branches.

The output and source agree: all 15 failures share the same mode error or a downstream expectation changed by `failureLogsCopied: false` / `runtimeDataRemoved: false`. This is an environment-dependent fixture defect, not a product-guard defect.

## Product conclusion

Product runtime directory creation does not rely on umask at the sites relevant to this guard. The packaged CLI and daemon use private-directory helpers that pass `0700` and then chmod `0700`; auth and state files pass `0600` and are chmodded `0600`. The proof harness itself creates its fresh session/runtime roots with `0700` and its preserved-log destination/files with `0700`/`0600`.

`daemon.stdout.log` and `daemon.stderr.log` are created by launchd from plist `StandardOutPath`/`StandardErrorPath`, not through a product JS creation API. Their containing directory is product-hardened to `0700`, and the proof guard deliberately validates the created files before any copy. This does not establish a product-created runtime-directory omission and does not authorize a product change.

## Bounded implementation recommendation

Change only `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` in the fake packaged-install block:

- give both recursive `mkdir` calls `mode: 0o700`; because the first call creates the intermediate `runtime` directory under an absent path, either create `runtime` explicitly at `0700` before its children or chmod/create each of `runtime`, `logs`, `auth`, and `tokens` so every fixture directory is deterministically `0700`;
- give the stdout, stderr, and token `writeFile` calls `mode: 0o600`;
- do not change `assertSafeSnapshotMetadata`, the proof harness, runtime/daemon code, packaging semantics, or any shared record in the implementation step.

No blocker or source ambiguity remains.
