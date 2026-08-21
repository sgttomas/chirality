# Sealed Agent 2 Launch Brief — parity executor

- RequestedBy: `WI-PKG02-DAPP86-RERUN-01`
- RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`
- ParentInstanceID: `WI-PKG02-DAPP86-RERUN-01`
- ChildInstanceID: `A2-PKG02-PARITY-EXECUTOR-01`
- AgentType: ephemeral generalist Agent 2; no delegation.
- PackageID: `PKG-02`
- DeliverableID: `DEL-02-02`
- Objective: execute D-APP-86 Option A on one frozen post-D-APP-88 source/package/helper identity and produce complete executing-case evidence for Workbench, Pipeline, guarded navigator selection, post-completion recorded-session selection, and real daemon replay.
- AcceptedBasis: clean start commit `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`, tree `fe8ece104dd281e3219bd95fa8b121437d524520`, branch `codex/app-dapp86-helper-parity-rerun-20260820`; D-APP-86 packet/ruling; accepted D-APP-88/D-APP-93 closure and PR #552 helper-stop remedy; live DEL-02-02 mandatory rerun trigger.
- Dependencies: local macOS host; existing Node/npm dependencies; isolated disposable app/daemon/user-data roots; one frozen unsigned package/helper basis.
- Exclusions: product/runtime behavior changes; provider credentials or provider calls; network expansion; dependency or lockfile changes; owner-machine LaunchAgent deployment; signing/notarization/publication/distribution; lifecycle/decision/TM/receipt/completion-log/Git effects; writes outside declared targets.
- DeclaredReads: repository-wide, especially the full prior D-APP-86 run, accepted D-APP-88/D-APP-93 evidence, current package/build/runtime/UI source, applicable validation docs, package status/memory, and computer-use skill.
- AllowedTools: deterministic shell/tests/build/package; `node_repl` + `@oai/sky` for direct packaged-app UI interaction with fresh state after every action; the prior instrument's purpose-built loopback CDP/CLI surfaces only where needed and explicitly identified. No AppleScript, `osascript`, System Events, credentials, provider calls, remote network, or destructive owner-state action.
- AllowedWriteTargets:
  1. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20/instances/A2-PKG02-PARITY-EXECUTOR-01/**`;
  2. the shared run-root outputs `RUN_MANIFEST.md`, `EVIDENCE_INDEX.csv`, `PACKAGED_UI_SMOKE.md`, `REAL_DAEMON_REPLAY.md`, `VALIDATION.md`, and `HANDOFF.md`;
  3. bounded evidence-helper code under `projects/chirality-app-dev/frontend/**` only if the existing authorized instrument cannot execute because the instrument itself is defective. Any such change must be evidence plumbing, never product/runtime behavior, and must be called out before use.
- ExpectedOutputs: the six D-APP-86 named outputs; child `RETURN.md`; immutable raw/sanitized evidence with hashes; exact source/package/helper identity comparison to the 2026-08-03 evidence basis; runtime/process/socket/temp-root telemetry; command results.
- AcceptanceCriteria: same source/package/helper for all observations; Workbench and Pipeline preserve boundaries and return cleanly; in-flight selection is guarded; post-completion recorded-session selection passes; at least one real daemon-owned transcript item renders with provenance and calibrated attribution; focused tests, typecheck, build, desktop:pack, reachable packaged premerge, release-quality with no silent provider-backed skip, secret scan, cleanup and containment pass; evidence contains no secret or private content; current helper/package materially differs from prior package basis.
- Escalation: stop and return exact blocker for any product defect, runtime/source repair need, external permission/security prompt, credential/provider need, owner-machine risk, shared write, network download need, or failed/partial observation. Do not repair product.

## Execution notes

Read the computer-use skill completely before UI interaction. Prefer the current accepted exact runbook/script surfaces over inventing a new instrument. Build/package once and reuse the exact bytes. Capture the package manifest and helper plist/executable/app.asar hashes before observation and revalidate after. Use fresh isolated HOME/CHIRALITY_USER_DATA and never load or modify the owner's installed LaunchAgent. Cleanup is part of acceptance.

The six shared outputs are derivative evidence and must not claim release readiness, lifecycle issuance, broad parity, professional reliance, or owner acceptance.
