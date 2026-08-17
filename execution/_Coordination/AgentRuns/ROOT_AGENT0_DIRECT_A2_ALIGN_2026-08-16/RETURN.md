# RETURN — ROOT_AGENT0_DIRECT_A2_ALIGN_2026-08-16

Child: Claude Fable 5 ephemeral Agent 2 generalist, directly dispatched under
sealed brief (v1 + amendment v2) by HELP_HUMAN (Claude Fable 5 session
minder); no delegation; no substitution.

## Outcome

EXECUTED under brief v2 (owner Option 1): prose alignment of
`agents/AGENT_HELP_HUMAN.md` only. Frontmatter `subagents:`, root validator,
and App harness alignment parked as follow-ons. PR opened for owner merge; no
merge performed.

## Raw data

- Base: `origin/main@b67197f5b647fbf0b972eee158e94c7215db9e6c`.
- Branch: `codex/root-agent0-direct-agent2-alignment` (worktree under the
  session scratchpad; main checkout untouched).
- `agents/AGENT_HELP_HUMAN.md` blob: before
  `503f70dbc00127d844e3a0327ed47655a9142278` (verified at base) → after
  `f3901408e7d5f040cb1d52e6033152ccb2bf3ade`. Interim blob with the v1
  frontmatter edit applied (`2e4755d9258e3a8c1e594bdbca4965e962673343`) was
  never committed.
- Changed hunks (three): invariant "Managers own management" (L54-62);
  invariant "Hierarchy-mediated coordination" relay clause (L64: "direct
  Agent 1 children" → "direct children"; the only additional statement found
  by the (d) grep that contradicted direct Agent 2 dispatch); SPEC item 3
  (L189-190). Frontmatter, WRITE_SCOPE, "No project-content writes" untouched.
- Manifest: `docs/governance_harness/tranche_manifests/ROOT-AGENT0-DIRECT-A2-ALIGN-20260816.yaml`.
- Notices: `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-16_ROOT_AGENT0_DIRECT_A2_DISPATCH_ALIGNMENT.md`;
  `projects/chirality-piping/execution/_Coordination/NOTICE_2026-08-16_ROOT_AGENT0_DIRECT_A2_DISPATCH_ALIGNMENT.md`;
  `_DomainEngines/_Coordination/NOTICE_2026-08-16_ROOT_AGENT0_DIRECT_A2_DISPATCH_ALIGNMENT.md`.
- Receipt: `execution/_Coordination/LOOP_RECEIPTS.md` Receipt 108.
- Run records: `OWNER_RULING_TRANSCRIPT_2026-08-16.md` (SHA-256
  `65214c24b90727cb9bae12fb677d0d7413572bab8ebc19c06f68f2b741959507`),
  `LAUNCH_BRIEF.md`, `BLOCKER_AND_RULING.md`, `PIN_SEARCH.md`, this file.
- Commit SHA and PR URL: reported in the chat return and on the PR itself
  (this file is committed inside that commit and cannot carry its own SHA).

## Checks (final lines)

- `python3 tools/validation/validate_agent_instructions.py` →
  `Summary: 34 files, 0 errors, 0 warnings`, exit 0.
- `python3 tools/validation/validate_instruction_tranche_manifest.py` (CI
  mode) → `G4 PASS (CI mode): 31 tranche manifest(s) ... schema-valid`, exit 0.
- Same, `--base origin/main --head HEAD --tranche ROOT-AGENT0-DIRECT-A2-ALIGN-20260816`
  → `G4 PASS (diff mode)`, `INFO: diff origin/main..HEAD: 10 changed path(s),
  2 on the instruction surface, checked against 1 manifest(s)`, exit 0; and
  `--added-manifests-only` → `G4 PASS (diff mode)`, exit 0.
- `python3 tools/practitioner_harness/harness.py self-check` → exit 0
  (GEN-9 agent-registry currency passes; `agents/` file set unchanged).
- `python3 -m pytest -q tools/validation` → `311 passed`.
- `git diff --check` clean; `git status --short` empty after commit; commit
  touches exactly the ten intended paths (one instruction file, manifest,
  five AgentRuns files, three notices, receipts ledger).

## Harness type-rule finding (read-only)

`projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts`
L289-290 (`Agent 0 may delegate only to named Agent 1 roles`) and L274
(generalist requires Agent 1 parent with `allow_generalist_agent2: true`);
`subagent-governance.ts` L160-168 (Agent 0 allowlist candidates must be
TYPE 1). Verdict: BLOCKS Agent 0 → TASK/generalist at runtime regardless of
the frontmatter; recorded as the App follow-on. Root validator
`tools/validation/validate_agent_instructions.py` L270-280 (+ test L167-183)
likewise rejects `TASK` in an Agent 0 allowlist; recorded as the root
follow-on. Details in `BLOCKER_AND_RULING.md`.

## Deviations

- Brief v1 edit (a) was applied, found blocking, reverted to base bytes under
  brief v2; no other deviation from v1/v2.
- Notice count is three (App, Piping, `_DomainEngines/_Coordination/`), per
  v2 and the PEC-has-no-inbox finding in `PIN_SEARCH.md`.
