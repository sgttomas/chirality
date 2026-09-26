# TASK brief T-K4 — build and prototype the K4 re-pin generator (provisional D-PEC-101, part K4)

Parent: WORKING_ITEMS (K14P manager) under HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node K4.
Role: TASK (Type 2). Do not delegate. Model steer: `claude-opus-5-5`, high reasoning.
Manager brief: `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K14P_REV16_CURRENCY_SETUP_PROPOSAL.md` (SHA-256 `3c16bb93710b63429cd04b3ccb8d41bc5620584965dcb5228218c3dfaf1f38b1`).

## Paths

- `REPO` = `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-rev16-currency-setup` (branch `claude/pec-rev16-currency-setup-proposal`, based on `origin/main` `aca930622ba167689881416044ba0feaee3ef003`). Read `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md` first. If your session cannot write into REPO because of a worktree guard, enter it with the EnterWorktree tool (`path` = REPO); the manager created it for this task.
- `BASE` = `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/k14p/base` — a `git archive` export of `aca930622`. **Never write into BASE.** Make APFS clones (`cp -Rc BASE <scratch>/protoX`) for every prototype, under `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/k14p/k4work/`.
- Your only write location in REPO: `projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/k4/` (create it). Do not git add, commit or push; the manager does. Write nothing else anywhere in REPO.

## Method basis to reuse (read, do not copy blindly)

`projects/pec/execution/_Coordination/PEC_CURRENCY_D95_PREP_2026-09-25/` (`gen_d95.template.py`, `build_gen_d95.py`, `verify_d95.py`, `run_prototypes.sh`) and `_DECISIONS/D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md` §N2 and §"Generation method". Re-derive against current bytes; reuse the structure (template + builder that fills a pinned block from BASE; fail-closed; nothing written unless all checks pass; exit 1 on a second run; `--check-only`; stdout TSV report with `READ|RENDER|WRITE|CHECK` rows).

## The act (exact)

Census observed at `aca930622` (re-verify; stop and report if different):
- 66 deliverable folders `projects/pec/execution/PKG-*/1_Working/DEL-*`.
- `_CONTEXT.md`: 61 end their provenance with the line ``then by revision 1.5 (`current_basis`, SCA-005 successor).`` (CTX_STD); DEL-02-08 and DEL-02-09 carry the D-PEC-93 form (lines ``SCA-005 successor; deliverable added by A-19). Fields templated`` / ``...A-20). Fields templated``) (CTX_D93); DEL-04-03, DEL-08-01, DEL-08-03 already carry ``then by revision 1.6 (`current_basis`, SCA-006 successor).`` (the three SCA-006 A2 mirrors; read-only; pin their hashes as basis).
- `_REFERENCES.md`: all 66 carry ``- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5, accepted `current_basis`; SCA-005 successor)`` and ``- `docs/PRD.md` v2.3 (accepted source corpus; see SourceRef column of the ledger)``.

Replacements (anchor lines only; each anchor must occur exactly once in its file):
1. CTX_STD (61): ``then by revision 1.5 (`current_basis`, SCA-005 successor).\n`` → ``then by revision 1.5 (`current_basis`, SCA-005 successor),\nthen by revision 1.6 (`current_basis`, SCA-006 successor).\n``. After the act, the `## Provenance` block of these 61 files must be byte-identical to the block of the three A2 mirrors (check it: all 64 D-PEC-62-scaffolded contexts share one provenance block).
2. CTX_D93 (2): ``SCA-005 successor; deliverable added by A-19). Fields templated\n`` → ``SCA-005 successor; deliverable added by A-19),\nthen by revision 1.6 (`current_basis`, SCA-006 successor). Fields templated\n`` (A-20 for DEL-02-09).
3. References (66): ``(revision 1.5, accepted `current_basis`; SCA-005 successor)`` → ``(revision 1.6, accepted `current_basis`; SCA-006 successor)`` and `` `docs/PRD.md` v2.3 `` → `` `docs/PRD.md` v2.4 `` (full-line replacements as in gen_d95).
4. Add-on C (flag `--covers`; same files, different postimages): revision 1.6 added SOW-097 to DEL-04-03 and SOW-098 to DEL-08-03 (`Deliverables.csv` `CoversScopeItems` = `SOW-006;SOW-007;SOW-097` and `SOW-043;SOW-098`). Rewrite only the ScopeLedger bullet of those two `_REFERENCES.md`: ``covers SOW-006;SOW-007)`` → ``covers SOW-006;SOW-007;SOW-097)``; ``covers SOW-043)`` → ``covers SOW-043;SOW-098)``. The generator must assert the new value equals the `Deliverables.csv` cell. Also check (report only) that every other `_REFERENCES.md` covers list equals its register cell (the 4 retired ones carry the D-PEC-95 add-on R form "none — retired under SCA-005, formerly SOW-0NN" against a blank cell; treat that as agreeing).

No other byte changes. The act is **slot-free**: no date appears in any postimage, so there is no `--act-date`; do not add a local-date check.

## Fail-closed checks (before any write)

- every pinned preimage hash (129 targets) and every read-only basis hash: `projects/pec/docs/PRD.md`, `_Decomposition/SOFTWARE_DECOMP.md`, `Deliverables.csv`, `ScopeLedger.csv`, the three A2-mirror `_CONTEXT.md`. Also assert that the PRD names version 2.4 and `SOFTWARE_DECOMP.md` names revision 1.6 as current (choose exact literal anchors from the files and pin them);
- population: glob all deliverable folders at run time. Every `_CONTEXT.md`/`_REFERENCES.md` either is a pinned target, or is one of the three pinned A2 mirrors (contexts), or **already names revision 1.6** (and PRD v2.4 for references) and does not name revision 1.5 as the final `current_basis` clause / references bullet. This tolerance exists so K4 can run before or after the separately rulable K1 part, which creates DEL-08-06 and DEL-10-13 folders born at revision 1.6 / PRD v2.4. Anything else → fail;
- anchor occurs exactly once per file; render all postimages; check post-state: every context in the corpus names revision 1.6 as its final provenance clause, every reference names revision 1.6 and PRD v2.4;
- the write set equals the grant for the chosen flags.

## Deliverables in `k4/`

- `gen_d101_k4.template.py`, `build_gen_d101_k4.py`, and the pinned `gen_d101_k4.py` (built from BASE);
- `verify_d101_k4.py <pre_root> <post_root> [--covers]`: independent postimage checks (edits confined to the anchors, counts 63 + 66, provenance-block identity, covers check, nothing else under `projects/` changed except the write set — compare whole trees; tolerate the K1 part's new folders/files if present in post but not pre only when given `--allow-k1` — optional, document it);
- `run_k4_prototypes.sh`: prototypes on clones: A; A on a second fresh clone (determinism: reports and trees identical); A+C; rerun on the applied tree (expect exit 1, nothing written); `--check-only` on a clone (tree unchanged); verify A and A+C (PASS) and verify base vs base (expect exit 1); strict validator `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` and `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <dir>` on base, A and A+C (expect output identical to base: strict exit 1 with exactly 0 ERROR / 26 XRG-013 / 2 DRB-008; `closure_summary.json` byte-identical); a whitespace check on the written files; and in a `git clone --shared --no-checkout` of REPO's repository placed in your scratch dir, checked out detached at `aca930622`: run the generator via `--repo "$(git rev-parse --show-toplevel)"`, then `git diff --name-only` equals the write set, `git diff --check` clean, and `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` and `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` before and after with identical output. Record exit codes in `k4/evidence/RESULTS.tsv` and outputs in `k4/evidence/`;
- `k4/evidence/`: generator reports (`genA.tsv`, `genAC.tsv`), `optionA_vs_base.diff` (unified diff, `projects/pec` only), `addonC_vs_optionA.diff`, strict/closure outputs, `grant_table.md` (one row per target: path relative to `projects/pec/execution/`, preimage SHA-256, postimage SHA-256 under A, and under A+C where it differs), `aggregates.txt` (bytewise-sorted `projects/pec/…` path order; SHA-256 of the concatenated bytes pre and post for: all 129; contexts 63; references 66; A+C; plus SHA-256 of the newline-joined path lists), `census.md` (with lifecycle states from each `_STATUS.md` `**Current State:**` line: count per state for the 63 contexts, the 66 references, and their union of folders);
- `k4/SHA256SUMS` over everything in `k4/`.

Use `PYTHONDONTWRITEBYTECODE=1`. Record the interpreter (`python3 --version`). Stdlib only. CSV files are not touched by K4.

## Return

Via SubagentHandback: census numbers (and any deviation from the census above), generator hash and flags, the RESULTS.tsv table, aggregate hashes, anything surprising, and the exact paths you wrote. Do not repair anything in the repository; report.
