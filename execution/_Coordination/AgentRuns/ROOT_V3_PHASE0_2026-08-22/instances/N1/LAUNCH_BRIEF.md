# Launch Brief — N1 HELPS_HUMANS

- Parent: `HELP_HUMAN`, run `ROOT_V3_PHASE0_2026-08-22`
- Accepted basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Objective: produce the exact D-GOV-35 proposal packet required by the owner
  steer and G0 record, without applying or activating any proposal.
- Construction: named Agent 1 `HELPS_HUMANS` under managed HELP_HUMAN
  supervision.
- Content write target: only
  `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/`.
- Control-plane writes: `STATUS.json` and `RETURN.md` in this instance folder.
- Tools: read, bounded writes, shell checks. Do not use network or delegate
  unless necessary for a fresh read-only review inside this same contract.

## Required context

Read `AGENTS.md`, `agents/AGENT_HELPS_HUMANS.md`, the owner steer and G0
record named in `ORCHESTRATION_PLAN.md`, D-GOV-14, both normative standards,
the cited App governance/SOW/code surfaces, TM-ROOT-126, and live downstream
pin/mirror surfaces. Treat plan Revision 3.1 as non-governing input.

## Output and acceptance contract

Produce every N1 file and satisfy every N1 content clause and check from the
owner steer. The patch must be zero-context, inactive, apply cleanly to the
basis `AGENTS.md`, and leave that file byte-identical. `README.md` must hash
every other file in the proposal folder and itself according to an explicitly
documented self-hash convention that does not claim an impossible recursive
fixed point. Return exact hashes, command results, changed paths, claim status,
blockers, and rerun requirements. No semantic acceptance may be inferred.

Brief amendment: version 2 at `../../amendments/N1/2.md` controls only the
mechanically incompatible patch-format/check pair and the bounded fresh-review
repairs. Objective, semantics, authority, and write scope are unchanged.
