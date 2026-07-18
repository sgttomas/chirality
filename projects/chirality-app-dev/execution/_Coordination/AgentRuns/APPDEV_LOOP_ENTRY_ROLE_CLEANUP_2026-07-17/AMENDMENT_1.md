# Verifier brief amendment 1 — BLOCK remediation

**Date:** 2026-07-17

**Predecessor:** `LAUNCH_BRIEF.md` and `RETURN_BLOCK_1.md`

**Objective and acceptance contract:** unchanged

The parent accepted the first `BLOCK` and amended the validator and tests.
Re-evaluate the original six sealed claims against the entire current diff,
with particular attention to the following remediation claims:

1. HELP_HUMAN entry is detected from the actual `Act as HELP_HUMAN for
   {WORKING_ROOT}` role-selection statement, not from the instruction-file
   path.
2. Root/project launcher byte equivalence is now part of the validator.
3. Both `LOOP_INIT.md` and the lexically newest standing `WORKPLAN_*.md` are
   checked when the local launcher selects HELP_HUMAN.
4. Case-insensitive patterns cover named Agent 0/1/2 routing, agent-layer
   routing, multi-agent/orchestration language, work-graph language,
   fan-out/fan-in language, managed-child/runtime/delegation language,
   child-session/parent/sibling mechanics, selection-authority mechanics, and
   model-assignment conventions.
5. Tests now exercise rephrased loop mechanics, current-workplan mechanics,
   model-assignment language, launcher drift, and actual-role detection.

Read-only scope and the binary `COMMIT-SAFE | BLOCK` return contract remain
unchanged. Do not write to the repository.
