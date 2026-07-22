# Agent-Index Re-disposition Handoff State

Status: `AGENT-INDEX-REDISPOSITION_PR0_MERGED_PR1_IN_PROGRESS`
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

## Process deviation recorded (PR-2 merge, 2026-07-21)

PR #304 was merged while its `Harness pre-merge` check was red: the merge
command was chained unconditionally after the checks-watch instead of gating
on the verdict — an executor error against the green-checks condition of the
owner's self-merge grant. Post-merge diagnosis: the failure was
`managed-delegation.test.ts > atomically reserves concurrent sibling write
targets`, a concurrency-timing flake unrelated to the markdown-only PR-2 diff;
the full test file passed 5/5 local reruns on the merged tree and the CI job
was re-run for a green record. Corrective rule adopted for the remainder of
the run: check verdicts are inspected and gated explicitly before any merge
command is issued; no chained merge.

## Item 6 premise correction and owner variance (PR-3, 2026-07-21)

The D-GOV-18 Item 6 deferral premise ("no root-PR CI breakage") was falsified
in PR-3 CI: App Dev's `agent-matrix-cells.test.ts` guard resolves the
ORCHESTRATE matrix cell through the persona map to an on-disk
`agents/AGENT_<persona>.md` check, so the root rename hard-fails
`Harness pre-merge`. The delta was surfaced to the owner as a new decision
request, not absorbed. Owner variance, verbatim: "I grant the variance: PR-3
may edit persona-resolution.ts and its test to map ORCHESTRATE to
PROJECT_SETUP." Scope applied, exactly two files:
`projects/chirality-app-dev/frontend/src/lib/shell/persona-resolution.ts`
(`ORCHESTRATE: 'PROJECT_SETUP'`) and
`projects/chirality-app-dev/frontend/src/__tests__/lib/persona-resolution.test.ts`
(matching expectation). The ruled D-GOV-18 record is not rewritten; the App
Dev AGENTS.md-wording follow-on remains with the App Dev loop.

## Owner directions recorded in-session (2026-07-21)

- PR-0 merged as owner-directed: "merge PR #302" → merged to `main` as
  `36774173c7acdb3786fb63df8740f897772ad2e2`.
- Owner grant, verbatim scope: "you may self-merge subsequent PRs in this
  session only." Interpretation of record: for PR-1..PR-4 of this run, within
  this session, the executing agent may merge each PR after its checks pass
  green; every other gate (ruled scope, sealed briefs, validation, receipts)
  is unchanged. The grant expires with the session and does not amend
  LOOP_INIT or any standing doctrine.

## Blockers

- **PR-0 merge approval** — CLOSED (merged `36774173c`, 2026-07-21).
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
