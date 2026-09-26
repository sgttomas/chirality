# Brief G2 — D-PEC-96 option-A registry act (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node G1 (the act). Role: WORKING_ITEMS (Type 1). Model steer: `claude-opus-5-5`, high reasoning, for you, any runner TASK and the verifier. The owner said "defaults".

## Authority and specification

- **Ruling.** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-96_RULING_2026-09-26.md`. The owner's words: "D-PEC-96: A; migrated; confirm; reject v1; create MEMORY; defaults".
- **Proposal.** `D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`, revision 4, SHA-256 `4506597b1bfd6cafd8fc561c688bcb9e803d9c2b04c3abdec9dc05edf155180e`. It is your specification: exact change, product grant, finite verification, independent verifier, administrative grant, rollback and limits. Do not enlarge it.
- **Bound scripts** in `projects/pec/execution/_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/`:
  - `apply_d96.py`, SHA-256 `80725b4ff0180e858e6a0ecf0cf50fc8bcf19d861fcf53278f115567e6d6bbf3`;
  - `mutate_d96.py`, SHA-256 `57c2f03107aec5056f03847c43b9443a6986fbfd522017971c3cab72c3c826f0`.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and the register row `RULED A` (PR #946).
- Every preimage and must-remain hash the proposal tables still holds. The script checks this itself.
- `pec_reliance_hold.py` returns ALLOW for every target, with operation `dispatch-for-production`, and with `rely-for-production` before fan-in.
- You work in an isolated worktree on branch `claude/pec-d96-registry-act`, cut from fresh `origin/main`. On any script or check failure, discard the worktree and return. Do not repair.

## Act

1. Create the run root `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/`. Copy `apply_d96.py` and `mutate_d96.py` into it byte for byte, and check their hashes.
2. From the repository root, run:
   `PYTHONDONTWRITEBYTECODE=1 python3 <run root>/apply_d96.py --repo "$(git rev-parse --show-toplevel)"`
   Save its report in the run root.
3. Run the proposal's whole "Finite verification" table, and save each command, exit code and output in the run root. That includes:
   - the five registered checks (`v2-loop-registry`, which should report 19 OK, `v2-store-guard`, `v2-api-contract`, `v2-core-posture` and `harness-self-check`);
   - the enforcement suite;
   - the mutation evidence (`mutate_d96.py`: 19/19 CAUGHT, none `NOT_APPLIED`, `RESULT PASS`);
   - byte identity against the proposal's postimages;
   - the containment check.

   **Basis note.** Root D-GOV-48 (PR #942) makes `validate_decomposition_registers.py --strict` report 26 pre-existing `XRG-013` warnings on PEC (exit 1 under `--strict`). This act does not touch the registers. Where any check involves that validator, the requirement is output identical before and after, with no new finding.
4. Create DEL-01-06 `MEMORY.md` from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4…6a5a`), following the proposal and the ruling. It is created from the template only; the undertaking's closeout writes the run row.
5. Write `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` in the run root. The D-PEC-95 run root `CURRENCY_REV15_D95_2026-09-25/` is the precedent for form.
6. Dispatch one fresh read-only verifier (`pec-reviewer`, opus). It applies the proposal's "Independent verifier" section. It must include a same-day reproduction on a fresh export, and it checks containment. Save its verdicts in the run root. Defects come back to you; repair only within the proposal and ruling.

## Write boundary

You may write only:
- the 11 granted `projects/pec/v2/**` paths;
- the run root;
- DEL-01-06 `MEMORY.md`;
- `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/G2_D96_REGISTRY_ACT.md`, which is your return.

Do NOT write:
- any other `v2/**` path, `software-workflow.json` or `service_core_posture.json`;
- any `_STATUS.md`, SOW, `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, decomposition or register file;
- `docs/**`, `README.md`, `projects/pec/AGENTS.md`, `_DECISIONS/**` or the work graph;
- any foreign path.

Commit your return to your branch before you hand back. Commit work in progress at each step, and push early.

## Publication

- Commit, ending each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Push, and open a PR against `main`, ending the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- Do not merge.
- If CI reports "Update the PR base", report it; do not repair it.

## Return

- The PR URL and head SHA.
- The act report.
- The written paths, with their hashes.
- The check results, including the mutation evidence.
- The verifier verdicts.
- Containment.
- Anything unresolved.

## Limits

- No lifecycle change, no DEL-01-06 Gate 5 act and no `_STATUS.md` write.
- No SOW, PRD, decomposition, register or instruction change.
- No CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
