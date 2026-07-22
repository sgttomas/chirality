# Agent-Index Re-disposition Handoff State

Status: `AGENT-INDEX-REDISPOSITION_DGOV18_RULED_PR0_AWAITING_MERGE`
Run: `AGENT-INDEX-REDISPOSITION-20260721`

## Current status

D-GOV-18 is RULED. The owner ruled verbatim on 2026-07-21:
"I APPROVE D-GOV-18 items 1–8 at commit
9a900b3b76dda415cc4d41185350eb2e5a436302" (the PROPOSED-state publication
commit on `codex/agent-index-pr0-dgov18`). The decision record, register row,
and disposition-matrix annotations are updated to RULED/effective. No role
file, validator, skill, or lifecycle state has changed; implementation lands
via the Item 8 PR sequence (PR-1..PR-4), each merge separately human-approved.

## Accepted upstream state

- `main@0c066652cd527eb1559f715e914262d2bda42602` (synchronized integration
  basis at run start).
- Framing record D-GOV-11 (runtime role ownership; Agent-2 construction forms).

## Derivative-package status

This run produces the D-GOV-18 governance record (authoritative-on-ruling) plus
navigational annotations (register row, matrix annotations). The register and
matrix annotations are derivative navigational surfaces citing the D-GOV-18
record; on any disagreement the decision record governs.

## Closure verdict

The ruling gate is closed: D-GOV-18 is RULED and SHA-bound to
`9a900b3b76dda415cc4d41185350eb2e5a436302`. PR-0 closure completes when the
human approves the PR-0 merge to `main`. PR-1..PR-4 execute only after PR-0
merges, sequentially, each from the then-current `main`.

## Blockers

- **PR-0 merge approval** (human act; CHANGE executes the approved merge).
- **PR-2 additionally gated** on the App Dev held EVALUATION dispatch:
  evidence as of 2026-07-21 (App Dev Receipt 85, 2026-07-20) records "fresh V3
  EVALUATION and final publication remain held" — held-not-running is the safe
  case; PR-2 lands shell + skill in one atomic commit, leaving no
  discoverability window. Re-verify the hold immediately before PR-2 opens.

## Coordination handoff notice (to the App Dev project loop)

Per D-GOV-18 Item 6, the App Dev couplings to the ORCHESTRATOR name are
deferred to the App Dev project loop by owner consent:
`projects/chirality-app-dev/frontend/src/lib/shell/persona-resolution.ts:36`
(`ORCHESTRATE → 'ORCHESTRATOR'`), its Jest expectation at
`projects/chirality-app-dev/frontend/src/__tests__/lib/persona-resolution.test.ts:24`,
and App Dev `AGENTS.md` wording. Verified no root-PR CI breakage under the PR-3
rename: the root rename touches no app-dev source, and app-dev tests run under
the app-dev loop. The App Dev loop owns whether and when to carry the rename
through its own instruments.

## Rerun requirements

- The ruling is SHA-bound (done 2026-07-21); the Ruling SHA is recorded in the
  D-GOV-18 record, the register row, and this handoff.
- Any validator or evidence surface whose basis changes before PR-1..PR-4
  executes must be rerun.
- If `main` moves before a PR opens, that PR branches from the new `main` and
  re-verifies its cited file/line references.

## Recorded follow-on candidates (not in this run)

- AUDIT_DECOMP undeclared-caller hygiene (REVIEW / SCOPE_CHANGE frontmatter).
- `tools/decomp/propose_gate4_kty.py` old-name (`ORCHESTRATOR`) seeds.
- Optional one-line historical note in `agents/AGENT_REVIEW.md` on the
  legacy `_Reconciliation/Reviews/` piping.
