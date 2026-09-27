# Verifier brief 01 — D-PEC-103 act, independent `MODE=VERIFY` (fresh read-only TASK)

- **Dispatcher:** WORKING_ITEMS (Type 1) for the D-PEC-103 act, under HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node K2. Brief `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K2A_D103_SOW_ACT.md` (SHA-256 `bb0d6e3105cd9a221f9adc1572e446c096bb2af04a472a8df267356c6ba48d6b`).
- **Role and method:** TASK (Type 2), `pec-reviewer`, model opus (`claude-opus-5-5`, high). Workflow `chirality-root:bundled:workflow:scope-of-work`, `MODE=VERIFY`, read-only on production content. You authored nothing in this act or its preparation.
- **Subject:** worktree `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d103-act`, branch `claude/pec-d103-first-sows-act`, head `4d2c19c1de99deae49577c295bf16701ce906a91` (base `origin/main` `d385b6a19`, the PR #989 merge carrying the ruling).

## Authority and specification (read these)

- Ruling `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-103_RULING_2026-09-26.md` (owner: "D-PEC-103: A; S; M; C8; defaults") and register row `D-PEC-103` in `_DECISIONS/_REGISTER.md`.
- Proposal `_DECISIONS/D-PEC-103_first_sows_del_08_06_10_13_proposal_2026-09-26.md`, SHA-256 `cfc2e65d5ae91f0d62d4ef993bc22a91d2bb4716969d083ae98f0fc948eb5417`. Its sections "Exact product grant", "Add-on C8", "Generation method", "Finite verification", "Independent verifier" and "Limits" are your specification.
- Method: `workflows/scope-of-work/WORKFLOW.md`, `resources/checks.md`; standard `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`. Root `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md`.
- Prep evidence `projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/` (with `SHA256SUMS`) and the act's run root `projects/pec/execution/_Coordination/SOW_INIT_K2_2026-09-26/` (the manager's evidence is under `evidence/`; treat it as claims to check, not as proof).

## What to verify (the proposal's "Independent verifier" list)

1. **Basis.** The ruling and register row are on `origin/main` (`git merge-base --is-ancestor d385b6a19 <branch head>`; you may use `git ls-remote origin main` to see whether `origin/main` moved). The run-root copies of `apply_k2.py`, `apply_k2_c8.py`, the candidates, `addons/`, `quotes/`, `claims/` and the check aids hash as in the prep `SHA256SUMS` and the proposal; the 17 pins of `apply_k2.py` and the 3 of `apply_k2_c8.py` still hash as tabled in the worktree.
2. **Byte identity.** The two written `ScopeOfWork.md` files equal the tabled postimages (`aecc5131…0826`, `c7743ee2…6633`); DEL-10-13 `_DEPENDENCIES.md` equals `609aa807…5693` and differs from the preimage `5087e581…eb63` by exactly the one tabled line, inserted after the "- **Notes:** …" line of the human-owned "Dependency Tracking Mode" section, with no other byte changed.
3. **`MODE=VERIFY`.** The mode-applicable subset of `resources/checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21) for each contract, including the QA 21 hand resolution tabled in the proposal. Record items that are `NOT_APPLICABLE` as such.
4. **Semantics.** Every claim is true at the commit it names, or at `125cfacc1`, and every quotation is verbatim; no requirement adds scope beyond the deliverable's `ScopeLedger.csv` row, its `Deliverables.csv` row and PRD v2.4; every open item is `TBD` or `CON`, and OI-006, the K3 act, the C-08 classification (in the contract text) and the DEL-02-07 edge are not decided; objective attributions are no stronger than the sources; no `## Remaining` section is read or presented as a surface. Sample substantively; you need not re-derive all 137 quotes and 482 claims by hand, but you must independently rerun the deterministic verifiers.
5. **C8.** The line records the owner's classification selected by the ruling, sits in the human-owned section, adds no heading, and leaves the DEL-10-13 contract true (its CON-001, AX-007 and REQ-016).
6. **Containment and lifecycle.** `git diff --name-status origin/main...HEAD` (use `d385b6a19...HEAD`) shows only the two created contracts, the one modified `_DEPENDENCIES.md`, the run root and the brief copy under `AgentRuns/.../briefs/`. No `_STATUS.md`, `MEMORY.md`, register, `Dependencies.csv`, `_CONTEXT.md`, `_REFERENCES.md`, decomposition, PRD, `v2/**`, `_DomainEngines/**`, `docs/**` or foreign path changed. Both `_STATUS.md` still read `OPEN` with their pinned hashes (add-on S has **not** run yet; it runs only after your verdict passes). `git diff --check` is clean.
7. **Rerun method.** Independently run the proposal's rerun method on a clean export of the base: `TMPDIR=<your mktemp dir> zsh <run root>/run_k2_checks.sh <worktree> d385b6a19 <run root> <your mktemp dir>/rerun` (it exports the base, applies A and C8 on its own export and checks everything). Also rerun, on the worktree itself: `validate_scope_of_work.py` ×2, `derive_review_checklist.py` into your temp dir (compare to `2227dbeb…9641` and `8e07ff3e…ba30`), `check_boundary_owner_resolution.py`, `verify_k2_quotes.py --tree <worktree> --gitdir <worktree> --prep <run root> --observation 125cfacc1`, `verify_k2_state_claims.py --gitdir <worktree> --prep <run root>`.

## Rules

- **Read-only.** Do not edit, create, stage or delete any file in the worktree or in any repository checkout. No `git checkout`, `switch`, `commit`, `stash`, `reset`, `fetch`, `pull` or `push` anywhere. Run Python with `PYTHONDONTWRITEBYTECODE=1`.
- Create and delete files **only inside your own `mktemp -d` directory** under `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/` (for example `mktemp -d <that path>/k2verify.XXXXXX`). Never delete other files there.
- Run the reliance-hold preflight first, from `projects/pec`: `python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <each of the 3 written paths, project-relative> --operation candidate-validation`. Stop and report on anything but `ALLOW`.
- You review; you do not repair. Defects return to the dispatcher.
- Do not raise or prompt about `CHECKING`, and make no acceptance, readiness, release or reliance claim.

## Return

A verdict document (Markdown) that the dispatcher saves verbatim as `VERIFIER_VERDICT_01.md`:
- verdict `PASS`, `PASS WITH NOTES` or `FAIL`;
- the basis you checked (head SHA, `origin/main` SHA, hashes you recomputed);
- each numbered item above with its result and evidence (commands, exit codes, key output lines);
- findings, each labelled `BLOCKING`, `NON-BLOCKING` or `NOTE`, with location and a proposed repair;
- the path of your temp dir and what you left in it.
