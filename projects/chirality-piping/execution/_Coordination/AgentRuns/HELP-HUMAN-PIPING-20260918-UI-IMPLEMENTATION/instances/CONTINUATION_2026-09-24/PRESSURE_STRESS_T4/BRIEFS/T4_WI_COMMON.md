# Common terms for TASKs dispatched by T4's WORKING_ITEMS

**Role.** TASK (Type 2). Engaged by T4's WORKING_ITEMS (Agent 1), which is your return path. You do not delegate. You make no Git writes.

**Undertaking.** T4 (pressure, stress and section mechanics) of `HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION`. The approved plan is `R4/PLAN_01/PLAN.md` (revision 2). The owner approved D-1 to D-4 as recommended; HELP_HUMAN's rulings H-1 to H-4 and T3's conditions are in `R4/T4_RULINGS.md`. Read the parts of the plan your brief names; read the research returns `R4/T4-I1…I5/RETURN.md` and `R4/T4-RV1/REVIEW.md` on demand.

**Placeholders.** Expand them yourself; write only placeholders into records.
- `WT` = the shared T3/T4 host directory; `NUM4` = `WT/t4` (T4's checkout, branch `codex/piping-t4-pressure-stress-20261009`).
- `P` = `projects/chirality-piping`; `PP` = `P/core/product_physics`; `FK` = `P/core/solver/frame_kernel`; `CB` = `P/core/solver/curved_bend`; `NI` = `P/core/solver/nonlinear_integration`; `SA` = `NI/src/structural_adapter.rs`.
- `I` = `NUM4/P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24`; `R4` = `I/PRESSURE_STRESS_T4`; T3's rulings `RR` = `I/NUMERICAL_INTEGRITY_T3/ROOT_RULINGS_V1.md` as read from T3's branch with `git -C NUM4 show origin/codex/piping-numerical-integrity-20260926:<path>` (fetch is already done).
- Never write a home-relative or absolute user path, a temporary-directory path or a machine name into a record.

**Code basis.** T3's U3 PR (#1168) head `ed012c7ccf` (main `ba500defa4` plus T3's pressure retirement). It is not yet merged; T4's code starts from main after it merges. Read code with `git -C NUM4 show ed012c7ccf:<path>`, `git -C NUM4 grep -n <pattern> ed012c7ccf -- <path>`. Cite `path:line@ed012c7ccf`. Do not modify NUM4's tracked files or any other worktree.

**Host (shared with T3).** Prefer reading and standard-library Python (`WT/venv/bin/python -I`; no numpy, sympy or mpmath; use `fractions` and `decimal`). If a probe truly needs cargo, it goes through `WT/tools/t3_cargo.sh` (`--locked --offline`) with its target under `WT/targets/t4-<your id>`. No DEC-025, exclusive or native jobs; never signal another process; no installs. Scratch goes in `WT/scratch/t4_<your id>/`.

**Output.** Write under `R4/<your id>/` only. Keep records terse: the facts and values someone needs, not narrative. Separate fact (read from cited bytes) from inference. Scripts you rely on go in `R4/<your id>/_run_records/` with their stdout, and a `SHA256SUMS` covers every file you write. Do not commit. If the host refuses a write, return the content as text with its intended path.

**Final message to your caller:** the paths written, the SHA256SUMS digest, and a summary of at most 25 lines, leading with anything that changes the plan, a stop rule (SP-1 to SP-4, plan §2) or a T3 condition.
