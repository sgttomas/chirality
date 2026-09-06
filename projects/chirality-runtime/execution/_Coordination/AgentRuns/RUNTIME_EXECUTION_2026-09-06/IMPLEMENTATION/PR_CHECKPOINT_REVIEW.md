# PR checkpoint review

Read-only bounded closeout review by WORKING_ITEMS, OpenAI GPT-6; exact serving model ID unavailable, role not mechanically enforced. No new child, build, test, vendor call or implementation stream was started. Parent owns final checks, documentation corrections and publication.

**Verdict: current candidate can be published as an explicitly incomplete checkpoint, subject to final parent checks and the documentation corrections below. No new production-admission bypass was identified in the inspected paths. This is not release approval or a new complete product audit.**

## Production availability

- `CodexSupervisor.acquireInternal` serves both ordinary and manager acquisitions. In the production branch it requires conformance configuration, validates hosted boundary/account/supply and actual stored posture, computes the real config/consent binding, and verifies current externally accepted conformance **before launch**. Resume enters the same acquisition path. Missing conformance is ENGINE_UNAVAILABLE.
- `RuntimeConformanceVerifier.verify` requires the complete eighteen-limb record, matching actual deployed closure, original accepted supplier identity and an external acceptance reference, and rechecks asynchronous inputs/current acceptance. Inspection alone does not mint admission. No complete accepted record has been produced by this run.
- `verifyExactSupply` remains the original pinned0.149.0 artifact. Neither the literal-only candidate nor interrupted candidate2 is silently accepted by production. Candidate2 has no established binary.
- `controlledForTests` is a separately named trusted-code factory; `verifyHostedBoundary` rejects it. Standalone JSON cannot select that factory. The separate owner-configured `controlled-worker` mode is explicitly an unsandboxed test/embedding seam, not hosted verification or release conformance. No new claim should describe it as hardened production execution.
- `local-engine-only` Pi is a separate explicit adapter path, not covered by the hosted Codex eighteen-limb gate. Its existing pilot/source acceptance limits remain; do not describe all engines as blocked behind the Codex gate or all engines as conformant. Legacy v1 likewise stays separate.
- Operator login is deliberately separate from turn acquisition; it still requires explicit private configuration/provider consent and exact supply. No actual login or imported account has been claimed.

Thus incomplete original-supply shell/ask and candidate2 paths remain unavailable as *admitted production Codex workers*. Publishing source does not install jobs, create private config, accept supply, supply a conformance record or release holds.

## Required claim corrections before PR description/docs are relied on

1. README currently says “ask uses the managed proxy and attributed destination prompts” before explaining the actual missing supplier callback later. Change the earlier sentence to describe implemented configuration/forwarding and explicitly state current actual ask is unavailable pending supplier correction/validation. The early unqualified sentence is misleading in isolation.
2. README paragraph contains the broken phrase “Approval forwarding passed controlled end-to-end transport tests; empirical the patched candidate…”. Repair it. Replace “candidate is being prepared”/“remain under test” with checkpoint facts: candidate2 source patch prepared, build interrupted with no artifact; actual checks are stopped/pending. No work is currently running.
3. Scope README/Capability Matrix “production worker acquisition” to hosted Codex ordinary/manager workers, avoiding an unintended claim that local Pi or legacy v1 is subject to this specific gate. Keep controlled mode and source/pilot limits explicit.
4. Working matrix is stale relative to SESSION_HANDOFF: P1/P2/P4 **were attempted and failed in aggregate**, with partial observations; P1 masked assertion unresolved, P2 marker/timing repairs unfinished, P4 missing daemon compatibility fixture basis before vendor launch. P3 was not started. Replace the concluding “prepared for parent execution / in progress” language and update relevant read/environment/process/role cells without turning partial checks into passes.
5. Matrix says dependency repair closed, correctly; retain final63/independent67 results. README cites earlier8.42s/3.80s sample, which is historically valid; prefer latest8.50s/3.82s and say single-run measurement if updating. No claim of negligible/constant-time latency.
6. Parent PR title/description and handoff must call this a checkpoint with unresolved supplier/canary work. Do not imply the user’s full working-runtime objective, eighteen limbs, owner-live account proof, lifecycle or source acceptance is complete merely because final ordinary tests pass.

## Tests and concrete publishing blockers

No current compile/test regression is established by this limited review. Latest existing evidence: actor/supervisor operation repair67 tests plus typecheck; independent R1 backcheck68; dependency stable63 and independent67. These are scoped historical checks, not substitutes for the final parent aggregate. The actual P1/P2/P4 failures are unfinished opt-in conformance fixture/diagnosis work, explicitly excluded from any success claim; they do not demonstrate ordinary default-suite success or failure. Parent must report final registered results and fix any actual blocking compile/default-test failures before describing the checkpoint as checked.

No reason was found to restart supplier builds or canary streams merely to open an accurately described checkpoint PR. Preserve applied supplier patch, interrupted build log/cache resume recipe and all failed evidence. Any final-check failures are concrete closeout work, not permission to relabel held paths available.

## Inspected current source pins

- `README.md`: `60d2d63383996a13442c886c9609316d7f63b4f6edba676a239dfb637c9f48c2`
- `execution/_Coordination/AgentRuns/RUNTIME_EXECUTION_2026-09-06/IMPLEMENTATION/CAPABILITY_MATRIX.md`: `c7d4b37b46e502cd5675a287aeb2f431702263f8e382fa0ea3aa15ceec2c564c`
- `packages/daemon/src/codex-supervisor.ts`: `8eb3a55df2670b7bba74cd50216a77b79ac3c83e5ac1f1dc710f2ba9be0faa6f`
- `packages/daemon/src/standalone.ts`: `de9a9f25fa3fec9106159bfd57282350fbb3c97259aeb52bcd4025347864b917`
- `packages/core/src/runtime-conformance.ts`: `689e20b61843bc4de1928e9e5dbf52a66278b85b5caa9ebaae59566f22c753ef`
- `packages/core/src/exact-supply.ts`: `579de962f095db69082f28e9212d63af59b44a1979c32598fc82c11039a2952e`
