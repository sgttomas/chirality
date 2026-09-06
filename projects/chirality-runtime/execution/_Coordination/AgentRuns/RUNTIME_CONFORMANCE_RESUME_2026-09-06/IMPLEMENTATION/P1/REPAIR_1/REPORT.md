# P1 shell snapshot repair frozen return

RUN_STATUS: SUCCESS (bounded implementation; independent review and parent actual comparison outstanding)
ControlSurface: FILE; TaskProfile: NONE; TaskSkill: NONE.
ScopePath: P1/REPAIR_1. WriteAuthorization: exact AMENDMENT.json five source/test paths plus this evidence directory. ToolPolicyCompliance: PASS.
ToolsUsed: bash read/diff; Python3 source/evidence edits and local checks; Node Vitest/TypeScript noEmit.
Attribution: OpenAI GPT-6, exact serving ID unavailable. Agent2 role/nondelegation instruction-asserted. No supplier execution, source/build edits or descendants.

## Change and reason

Runtime now explicitly sets features.shell_snapshot=false in both native trusted launch config and legacy containment config. Native policy identity is version6 and includes shellSnapshot:false, so the setting cannot silently reuse the previous identity. CodexTurnSession requires effective config features.shell_snapshot to be exactly false on all existing native checks. Missing/null/true and operation-time drift are failures before downstream work proceeds. Filesystem/network grants and existing allow_login_shell:false are unchanged. Existing policy digests and conformance bindings require regeneration/revalidation for the new identity; no acceptance migration is inferred.

Source-known basis copied into SOURCE_PINS.json/SOURCE_EXCERPTS.md/SOURCE_STATE.json: supplier shell_snapshot boolean feature defaults true; session initialization constructs ShellSnapshot::disabled when false; build exits at config.as_ref()? before command creation. Existing snapshot creation invokes a login shell directly, independently of tool login:false. The actual Candidate1 pre-repair P1 run proves marker presence, not causal process attribution. Disabling this separate startup feature is the narrow ordinary Runtime repair; actual matched P1 run remains necessary.

## Validation

73 focused tests pass across containment/session/supervisor. New per-posture tests cover off/ask/on exact false positives, absent/null/true rejection, and false-to-true drift rejection before startTurn and resumeThread. Initial generic tsc command failed at the existing supervisor test's direct-source DescendantTracker versus package-dist private class identity, unrelated to its config string change. Evidence preserves that failure. The evidence-local noEmit config maps @chirality/runtime-core consistently to source; all three edited test files and their production imports then typecheck successfully. CHECKS.json records all commands/results, including the failed ad hoc check. No compilation artifacts emitted.

Only the five authorized files changed. Supervisor test change is solely its successful synthetic config reply field. Exact P1 fixture remains byte-identical e7a94692fd3b88a5f73da7171b22f020d956acc2ce5def7f15d5e6e7db836383. No tests weaken or remove startup absence checks. Before images are .source. FROZEN_SOURCES.json holds exact final hashes; AMENDMENT input hashes remain original. Parent should review this combined five-file freeze before actual supplier use.

## Parent actual handoff

Run the unchanged P1 fixture against the same Candidate1 hash/size with a fresh evidence directory and the repaired Runtime source. This produces a natural matched comparison to P1_CANDIDATE1_01: source difference is these trusted launch/readback changes; binary/fixture remain fixed. The actor now refuses unknown/true snapshot settings through config/read before startThread. Require original P1 startup-marker-absent, both actual primary/native commands and all denials/environment/host/source/supply/cleanup/budget checks. Capture policy digest and source hashes as a new identity, not replacement of historical evidence. If the marker remains, keep failure and investigate timing/other startup paths. Parent runs broader registered checks after coherent fan-in.

Closure: derivative repair slice frozen, awaiting independent review and parent actual comparison. Accepted basis: P1/BASIS via original brief plus REPAIR_1/AMENDMENT.json and actual parent failure. No supplier acceptance, aggregate conformance, hold release, lifecycle/operational promotion or merge. MISSING: review and actual run; NEEDS_HUMAN_RULING: none; DEPENDENCY_NOTES: policy identity changed intentionally, so old bound evidence does not satisfy new exact identity.
