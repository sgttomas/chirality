# Sealed repair brief

Authority: IMPLEMENTATION_AMENDMENT_11.json and parent follow-on dispatch. OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent 2; instruction-asserted role not mechanically enforced. No delegation, Git or provider/account invocation.

Purpose: resolve reviewed callback-timeout lifecycle defect without modifying sealed earlier evidence. Port owns only packages/daemon/src/codex-manager.ts and tests/codex-manager.test.ts plus this REPAIR_01 evidence directory. Core coordinator ownership remains parent-serialized; this agent will not edit core.

Finding: the port's Promise.race bounds callback waiting, but cannot abort coordinator-owned child work using current Agent1ManagerHooks. Proposed division: core must abort and drain outstanding hook work before final terminal/evidence on manager error or early return. Port needs a trusted configurable bounded callback timeout to produce a fast deterministic actual-timeout regression; it must preserve original timeout error across failure reply/retirement and never label failure as successful callback execution.

Acceptance: independent reviewer repro, targeted timeout/cancellation regression, workspace build, parent core integration showing no late run.json overwrite or post-terminal child work. Package remains derivative implementation evidence. Live vendor/G-SBX acceptance remains parent-owned.
