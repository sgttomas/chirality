# Agent 2 Attempt 2 — Implementation-First Brief Amendment

PredecessorDisposition: attempt 1 was interrupted by HELP_HUMAN after it
reported a supportable public seam but produced no test bytes or focused run.
No semantic output was accepted.

This amendment preserves every scope, exclusion, acceptance criterion, and
write boundary in `AGENT2_BRIEF.md`. It changes only the execution order and
freezes the test target:

1. Write the smallest compileable test immediately at
   `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`.
2. Copy/adapt existing setup patterns from `runtime/tests/daemon.test.ts`,
   `runtime/tests/turn-hardening.test.ts`, and the App fake-oMLX wire test. Do
   not conduct another general seam survey.
3. Run focused Vitest as soon as the file exists.
4. Refine the test to satisfy the five frozen conjuncts.
5. If a compileable focused test cannot be produced promptly, stop with the
   exact compiler/public-seam blocker and minimal App-owned seam proposal.

Attempt2ChildID: `A2-DEL0903-ATTEMPT2`
