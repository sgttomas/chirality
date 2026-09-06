# P1 startup source diagnosis

RUN_STATUS: SUCCESS (read-only diagnosis; empirical cause pending controlled comparison)
ControlSurface: FILE; TaskProfile: NONE; TaskSkill: NONE.
ToolsUsed: bash/rg/sed/git read-only source inspection; Python3 evidence files.
ToolPolicyCompliance: PASS. WriteAuthorization: FOLLOWON_DIAGNOSIS only.
Attribution: OpenAI GPT-6, exact serving ID unavailable; Agent2 role/nondelegation instruction-asserted; no descendants, supplier execution, builds or production edits.

## Finding and evidence calibration

Actual parent p1-candidate1-01 failed exactly `startup-marker-absent` after 36 preceding successful assertions. Both probes ran, both foreign/broker/literal/config/alias read denials held, terminal completion marker was present, and the host startup marker was a regular 11-byte file equal to the synthetic expected bytes. All host sentinels unchanged, sourceStable/supplyRevalidated true, cleanup0, elapsed3051ms. This establishes the marker side effect, not its process/timing provenance. Original actual evidence is unchanged.

The retained supplier has a separate default-enabled shell snapshot creation path that bypasses the action-shell `allow_login_shell` choice. It is the narrow leading explanation for the side effect, not an instrumented causal verdict. Source HEAD is 758ef40f50c1a458425c7cfbf1eb12cbc07af0b0. Current retained source includes Candidate2 network changes: session.rs diff lies after the cited snapshot initialization, while other cited shell/snapshot files are unmodified. Candidate1 manifest matches observed b1ba73f…b2 /241191088. Current source read hashes and numbered excerpts are frozen in SOURCE_PINS.json and SOURCE_EXCERPTS.md; this does not relabel current tree as Candidate1 or prove binary/source correspondence beyond retained build records.

## Source chain

All supplier paths below are relative to `/private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/`.

- `codex-rs/features/src/lib.rs:869-874`: Feature::ShellSnapshot uses key `shell_snapshot`, stable, default_enabled true. `codex-rs/core/config.schema.json:5651` admits boolean feature configuration.
- `codex-rs/core/src/session/session.rs:1147-1164`: chooses default user shell, creates ShellSnapshot solely on the feature flag, and passes it into ThreadEnvironments. It does not condition creation on allow_login_shell.
- `codex-rs/core/src/environment_selection.rs:564-571`: independently spawns the snapshot build during environment resolution. `core/src/shell_snapshot.rs:65-83` returns before work when disabled.
- `core/src/shell_snapshot.rs:201-233,269-307`: capture calls run_shell_script with use_login_shell=true; run_script_with_timeout creates a direct tokio Command, scrubs a short named non-inheritable environment list, selects cwd, and executes. It does not construct an action SandboxAttempt or consume the native filesystem policy. Validation additionally starts a non-login shell at254-266. Snapshot timeout/kill-on-drop limits duration but does not undo startup-file writes.
- `core/src/shell.rs:22-30`: Zsh/Bash/Sh login selection changes `-lc` to `-c`, without `-f`/startup suppression. `core/src/tools/handlers/unified_exec.rs:97-123` enforces allow_login_shell only for the actual exec request. `core/src/tools/runtimes/mod.rs:234-262` wraps snapshots only for `-lc`; a login:false action therefore need not consume the snapshot for snapshot creation to have already run.
- `core/src/tools/runtimes/unified_exec.rs:477-509`: direct actual actions follow sandbox-command and attempt preparation, unlike the snapshot Command path. Primary/child protected broker read denials are consistent with that difference but do not individually identify the marker writer.
- `shell-command/src/shell_detect.rs:61-109,266-288`: Unix default shell is selected through user database shell lookup. Setting SHELL=/bin/bash is not a grounded fix for this selection path.
- Runtime `packages/daemon/src/codex-containment.ts:226,242-258,263`: policy digest records loginShell:false; config disables login shells/plugins/remote plugins but leaves shell_snapshot default, and launches the supplied executable directly with HOME=privateDirectory. The staged `.zshenv` is in that HOME. `packages/daemon/src/codex-session.ts:393-408` verifies login/network/plugin settings but not shell_snapshot.

## Minimal recommendation

First run a separately frozen parent-owned controlled comparison against the same Candidate1 bytes with the sole effective config difference `features.shell_snapshot=false`. Keep all P1 assertions, protected roots, environment values and budgets unchanged. Capture explicit `config/read` value, source/policy/supplier identity, and marker observations before thread start, after thread start, after turn and after cleanup where practical. An enabled/disabled pair isolates the feature better than replacing shells or changing startup expectations. Each profile remains <=60s and each actual command <=10s. A negative result remains a failure to investigate.

The feature/config spelling is source-known, so no supplier build is required to test this hypothesis. For actual implementation after comparison, propose exact Runtime paths:

1. `packages/daemon/src/codex-containment.ts`: hard-pin features.shell_snapshot=false in native config, include shellSnapshot:false plus policy identity version bump so the new behavior cannot share old policy identity. Consider the legacy containment config too within this same file, without changing its filesystem grants.
2. `packages/daemon/src/codex-session.ts`: fail closed unless effective config features.shell_snapshot is exactly false wherever existing native policy checks run, including operation-time drift.
3. `tests/codex-containment.test.ts`: verify emitted false, changed identity and retained grants; `tests/codex-session.test.ts`: explicit false controlled baseline plus missing/null/true/drift rejections.
4. `tests/exact-boundary-conformance.test.ts` only if stage observations/effective-feature evidence are needed; preserve startup-marker-absent and all existing assertions. Other controlled tests with synthetic native config replies may require exact manager-scoped updates after discovery; no blanket path grant is requested.

These paths are proposed, not edited or yet authorized to this child. The current diagnostic fixture hash remains e7a94692fd3b88a5f73da7171b22f020d956acc2ce5def7f15d5e6e7db836383.

## Alternatives and limits

Changing only tool login:false is already in force and does not control snapshot creation. Merely choosing another action shell, removing the planted file, ignoring its marker, widening broker read permissions, or relocating HOME to hide it would not establish the requested startup boundary. A zsh -f change to only tool command derivation would leave the separate login snapshot path. If explicit snapshot disable fails, parent should capture marker timing and investigate other shell initialization paths before any supplier change.

A supplier follow-on, if needed independently of Runtime's feature pin, can propose conditioning snapshot creation on a policy that expressly forbids shell startup or placing snapshot work under an appropriate hard envelope. Changing only allow_login_shell semantics globally requires review because its existing scope is login mode, not a universal startup prohibition. Exact prospective supplier surfaces: `codex-rs/core/src/session/session.rs`, `codex-rs/core/src/shell_snapshot.rs`, corresponding `codex-rs/core/src/session/tests.rs` and `codex-rs/core/src/shell_snapshot_tests.rs`; shell derivation changes additionally require `codex-rs/core/src/shell.rs` and `shell_tests.rs`. Do not mutate the currently building Candidate2 tree; use a separate reviewed source/build tranche if this route becomes necessary.

Closure: derivative diagnosis complete, parent controlled comparison and reviewed implementation remain. Accepted basis remains original P1 BRIEF/BASIS and FOLLOWON_DIAGNOSIS/BRIEF; no supplier acceptance, conformance acceptance, policy release, lifecycle change or merge. MISSING: causal enabled/disabled comparison. NEEDS_HUMAN_RULING: none for narrow config investigation. DEPENDENCY_NOTES: coordinate session/containment source ownership before repair; active supplier lane owns retained source/build.
