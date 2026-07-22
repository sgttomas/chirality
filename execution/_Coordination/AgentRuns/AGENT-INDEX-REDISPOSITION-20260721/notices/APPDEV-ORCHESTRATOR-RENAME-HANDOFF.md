# Coordination Handoff Notice — App Dev follow-on for the ORCHESTRATOR → PROJECT_SETUP rename

Issued by: HELP_HUMAN, run `AGENT-INDEX-REDISPOSITION-20260721`
Basis: D-GOV-18 Items 1 and 6 (ruled 2026-07-21); owner variance of 2026-07-21
Status: OPEN — owned by the App Dev project loop

## What already happened (no App Dev action needed)

- Root rename landed atomically in PR #305: `agents/AGENT_PROJECT_SETUP.md`
  replaces `agents/AGENT_ORCHESTRATOR.md`; every root caller, validator key,
  skill contract, and registry token carried in one revertable unit.
- Under an explicit owner variance (verbatim in this run's HANDOFF_STATE.md),
  PR #305 also updated exactly two App Dev files so the matrix guard passes:
  `frontend/src/lib/shell/persona-resolution.ts` (`ORCHESTRATE:
  'PROJECT_SETUP'`) and
  `frontend/src/__tests__/lib/persona-resolution.test.ts`. App Dev CI is
  green on the merged state.

## What remains for the App Dev loop (this notice's ask)

Live App Dev doc surfaces still name the retired role and now lag the code:

1. `projects/chirality-app-dev/docs/TYPES.md:132` — alias table row
   `| ORCHESTRATE | ORCHESTRATOR |` → `PROJECT_SETUP`.
2. `projects/chirality-app-dev/docs/PRD.md:519` — FR-026 alias enumeration
   `ORCHESTRATE -> ORCHESTRATOR` → `ORCHESTRATE -> PROJECT_SETUP`.
3. `projects/chirality-app-dev/docs/PRD.md:134` — persona narrative listing
   `ORCHESTRATOR, WORKING_ITEMS, ...` → `PROJECT_SETUP, ...`.
4. Any other live App Dev doc surface the loop's own sweep finds (historical
   receipts, run records, plans/ artifacts, and execution/ provenance stamps
   are immutable and stay as written).

These are App Dev project content; the root run does not edit them. The App
Dev loop lands them under its own instruments, receipts, and checks at its
own cadence. Until then the divergence is doc-vs-code naming only; runtime
resolution is already correct.

## Premise correction carried with this notice

D-GOV-18 Item 6 assumed the deferral caused no root-PR CI breakage. That was
falsified: `agent-matrix-cells.test.ts` resolves matrix cells to on-disk
`agents/AGENT_<persona>.md` files, so the rename hard-failed `Harness
pre-merge` until the owner's two-file variance. Recorded here and in
HANDOFF_STATE.md so the App Dev loop understands why two of its files changed
under a root-run PR.
