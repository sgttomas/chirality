# D-APP-113 — Residual of D-APP-112: gating semantics at Step 1 and the state-anchored register grep at Step 0

Status: RULED (owner direction in chat 2026-09-05)

Owner: Ryan Tufts

Date: 2026-09-05

## Owner direction (verbatim)

<!-- BEGIN OWNER DIRECTION VERBATIM -->
Now return to this matter:  Clean up the one residual from the app-dev second dry run worth a later pass: the fresh operator walked four iterations forward correctly and located the terminus where I would have, but asked which `SatisfactionStatus` values gate, and noted that the Step 0 register grep matches historical rows containing the word PROPOSAL. Both are one-line fixes;
<!-- END OWNER DIRECTION VERBATIM -->

## Effect (HELP_HUMAN's reading; the owner may amend by reply)

1. **Step 0.** The register grep is anchored on the state column:
   `grep -nE "^\| D-APP-[0-9]+ \|([^|]*\|){2} (AWAITING_RULING|NOT_PREPARED)"`.
   Verified against the pre-ruling revision of the register (it returned the
   D-APP-112 row while that row was `AWAITING_RULING`) and against the live
   register (no open row). The old pattern returned thirteen historical
   `RULED` rows whose text contains the word PROPOSAL.
2. **Step 1.** Which rows block is stated: a register row blocks an item
   only when it is `ACTIVE`, of type `PREREQUISITE`, its
   `SatisfactionStatus` is `TBD`, `PENDING`, or `IN_PROGRESS`, and the
   item's `Depends` line names its target. `INTERFACE`, `HANDOVER`,
   `CONSTRAINT`, and `ENABLES` rows order work and never block.
   `SATISFIED`, `WAIVED`, and `NOT_APPLICABLE` never block. This is the
   reading D-APP-110 applied (every `PREREQUISITE` row kept strict; the
   other four types eligible for decompose) and the reading the fresh
   operator inferred for itself in the second dry run; it is now written so
   the next operator does not have to infer it.

Candidate `loop/LOOP_INIT.md` SHA-256 `a25cb37e58a333d684c7e713f4a8c9013a870e7e14f73077c8d26283c9d68d26`. No other clause changes.
The D-APP-112 packet's "Dry run" residuals 1 and 4 of the second run are
thereby closed; the remaining second-run frictions stay recorded there.

## Attribution

Transcribed and applied by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`)
acting as HELP_HUMAN (Agent 0) in an untyped Claude Code session. Role not
mechanically enforced.
