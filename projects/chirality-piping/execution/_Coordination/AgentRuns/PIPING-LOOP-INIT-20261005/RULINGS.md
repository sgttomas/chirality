# HELP_HUMAN's rulings: piping LOOP_INIT in the binding form (2026-10-05)

Run `PIPING-LOOP-INIT-20261005`. The owner's direction is in [OWNER_DECISIONS.md](OWNER_DECISIONS.md).

## LM's return

LM, a Type 2 TASK, was dispatched under [BRIEF_LM.md](BRIEF_LM.md) as a Claude Code subagent (general-purpose, Claude Opus 5.5). It made no Git writes and ran no tests. It returned three files:
- `LOOP_INIT_MAPPING.md`, with sha256 `12c34aa8…`;
- `LOOP_INIT_PROPOSED.md`, with sha256 `072f6d36…`;
- `CONSISTENCY_EDITS.md`, with sha256 `3021790…`.

**The mapping** has 92 rows:
- 77 in class (a), carried elsewhere with verbatim quotes;
- 11 in class (b), piping-specific;
- 0 in class (c);
- 4 in class (d), obsolete.

It checked 194 destination quotes with `grep -F`, every draft path with `test -e`, and the eight workflow names against `workflows/index.json`. HELP_HUMAN checked these:
- the draft against the owner's three-part test;
- the stage-gate source: `_COORDINATION.md` "Current Target Stage (ruled record)", and PRD §24 "Release Milestones";
- each "before" text in A1–A7 occurring exactly once.

## Rulings on LM's open questions

1. **The MEMORY creation grant is kept.** It is piping-specific. Construct §3 leaves MEMORY writes to the project's write fences, and App v4 carries the same grant.
2. **`coordinated-knowledge-work` is kept.** Piping's T3 runs under it by owner delegation, and it is the general coordination method App v4 binds.
3. **"If you are unsure whether something matters, ask the human." is replaced by "If you are unsure whether a section matters, read it."** The replacement keeps the reading decision with the agent, as the owner asked ("the agent decides when to visit it"). It also avoids contradicting Root `AGENTS.md`: "uncertainty alone does not require an extra prompt".
4. **A6 and A7 are applied.**
   - **A6:** DEL-11-05 is IN_PROGRESS, and `RECON_2026-09-21_WHOLE_CORPUS` last changed at its closeout (2026-09-22). An earlier instruction tranche added the banner. The independent reviewer is asked to confirm that no active concordance scope freezes it.
   - **A7:** the WORKPLAN says its navigation "follows the subsequently adopted shared loop instructions". The owner-adopted retirement text is unchanged.
5. **Section B's edits are not made.** They were stale before this change, so they are recorded and left for their own correction. Section C, the manual citations and construct's introduction sentence, is outside this tranche. The manifest's notice rationale records it.
6. **"When to read further" in two loops is accepted.** Each LOOP_INIT binds its own project, and moving the paragraph into a manual is an owner-authored manual revision.

## Adoption

- **`projects/chirality-piping/loop/LOOP_INIT.md`** is replaced by the proposed text, with ruling 3 applied (sha256 `5c20a16fef96…`).
- **A1–A7 are applied** as written in `CONSISTENCY_EDITS.md`.
- **The tranche manifest** is `docs/governance_harness/tranche_manifests/PIPING-LOOP-INIT-20261005.yaml` (G4 PASS in CI mode).
- **Checks at adoption:**
  - `tools/validation/validate_instruction_entrypoints.py` PASS;
  - `projects/chirality-piping/tests/test_ci_e2e_plan.py` 41 passed (it reads piping's LOOP_INIT).
- **The gates for the PR,** under the owner's "appropriate level of CI":
  - an independent review, LR (`reviews/`), with any repairs confirmed by the same reviewer;
  - GEN-8 on the exact head;
  - the PR's automatic CI, which includes G4.
  
  No product code changes, so DEC-025 does not apply (project `AGENTS.md`, "Software checks").
