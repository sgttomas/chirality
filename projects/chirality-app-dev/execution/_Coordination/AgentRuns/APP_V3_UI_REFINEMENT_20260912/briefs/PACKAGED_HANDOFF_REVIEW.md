# TASK: independent packaged hand-off review

Parent: this session's HELP_HUMAN / Agent 0, using the session's native
`collaboration.spawn_agent` facility. Reviewer: fresh `gpt-6-astra`, medium,
Type 2, read-only, no authorship and no further delegation. No Fable model is
available in this session; the owner's prior Astra/medium direction is used.

## Assignment

Review the full record-only diff from base
`85f19f019589b798331c804c4b206e34849eeab5` to the frozen commit supplied in
the dispatch. Verify the evidence supports the DMG hand-off and honestly
distinguishes build/signature success from owner native acceptance and
notarization. Check that the owner's tasks 4 to 6 and carried risks are covered
without adding source work, new release gates or approval claims.

Checkout: `/Users/ryan/.codex/worktrees/chirality-ui-refinement-packaged-20260912/chirality`.
Read Root and App AGENTS and the TASK role. Relevant run files: the current
handoff, BUILD_EVIDENCE_20260912.md, OWNER_HANDOFF_20260912.md, final log
entries, WORK_GRAPH.md and the existing third review/update checklist.

Supporting build records are at
`/Users/ryan/.claude/chirality-build-ui-85f19f019-evidence` (filtered build
logs and three JSON summaries). The detached source is
`/Users/ryan/.claude/chirality-build-ui-85f19f019`; the candidate output is
`/Users/ryan/.claude/chirality-build-ui-85f19f019-out`.

Read-only Git inspection and contained reads of these source/evidence/artifact
paths are permitted. Reuse recorded packaging checks; do not rerun builds,
tests, signing or native probes. No write targets. Never open or launch an App,
read live identity/auth/token/binding/keychain/Codex-home/session/event files,
inspect the owner's intro-rehearsal, use `security`, change Git, or clean up any
worktree. Do not emit account email; supplied build logs already exclude lines
containing `@`.

Return PASS or FAIL for this hand-off record, any concrete actionable finding
with location and reason, and limits or residual risks. Identify the exact
reviewed commit and coverage. Do not call an agent review owner approval.
Return in the agent message; the parent records it and validates the fan-in.
