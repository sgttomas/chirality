# Review 01 of PR #969 (D-PEC-101 ruling), transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `def11053ee814d7323d72b5bc67bfdc4e762e5c6` (base `origin/main` `121900105`). Repairs: `7720702f7`; this file is added after that.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `21fd4c0c0aa473e2be31f7649c890068182ecde633af9f9f092940ad2a41efc7`.

## Report (verbatim)

## Review of PR #969 (head def11053ee814d7323d72b5bc67bfdc4e762e5c6, base origin/main 121900105, merge-base = origin/main)

**Verdict: PASS WITH NOTES.** I found nothing blocking. There is one NON-BLOCKING factual inaccuracy in the ruling record, and I recommend fixing it before merge. The rest are NOTEs. I modified no files, and the worktree status is clean.

### BLOCKING
None.

### NON-BLOCKING
**N1. The ruling's description of what changed on main since aca930622 is incomplete.**
- Location: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-101_RULING_2026-09-26.md:49`. The record says origin/main "changed under `projects/pec` only in work graphs and review returns".
- `git diff --name-status aca930622 origin/main -- projects/pec` shows more than that:
  - two modified work graphs (`...POST-SCA005` and `...REMAINING-RETIREMENT`);
  - review returns `REVIEW_PR961_01/02` and `REVIEW_PR962_04/05`;
  - the K14P brief and return copies, and the whole `PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/` folder added by PR #962;
  - **a modified notice**, `execution/_Coordination/NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md`. Commit `d61af6fde` appended an erratum. Its SHA-256 went from `4f06f230…6a11` at aca930622 (the hash the proposal cites in finding 5, proposal L116) to `23f95189abe5e49a4e34814874664940097fabb3b5bf5bc0aa5b2a56155aa8a8`.
- The load-bearing claim still holds (every preimage is unchanged; see item 2). The erratum only clarifies `analyze_dep_closure.py` output behaviour, and that tool is byte-unchanged. So this is a wording fix, for example "work graphs, review returns, the preparation folder and brief/return copies, and one notice erratum". Your brief expected "notices" in this list; the record leaves them out.

### NOTEs
1. **"Both parts ride one act" is HELP_HUMAN's method choice, not the owner's.** Location: ruling `:45`. The proposal leaves it open ("K4 and K1 may ride one PR or two"), and "defaults" covers only question 5 (actor and models). It sits under the "HELP_HUMAN interpretation" heading and narrows rather than enlarges, so it is acceptable. Wording it as an agent method choice would match PEC AGENTS §"Selection and decisions".
2. **The Notes (a) timing and placement are HELP_HUMAN's additions.** Location: ruling `:42`, `:49`.
   - The proposal (L437–447) authorizes the with-K1 text "if K1 is ruled". It sets no timing and gives no fallback.
   - "After the K1 writes are verified" does not say which verification: the generator, `verify_d101_k1.py`, or the independent verifier.
   - If K1 fails or is reverted, the ruling applies neither text; the proposal's without-K1 text is left unused.
   - The ruling pins no preimage for the edit. The proposal pins `_COORDINATION.md` `95ebe344…8a90c`, which is unchanged at head and at origin/main; L225–227 currently match the quoted text.
   - Putting the edit in the act PR means the proposal's act-containment row (proposal L365: "nothing else") needs to admit HELP_HUMAN's one `_COORDINATION.md` hunk, as HELP_HUMAN's STATUS/graph commits were admitted in earlier act PRs.
   - None of this enlarges the grant. Clarifying these points would help the act's verifier.
3. **The ruling does not say the verbatim string was HELP_HUMAN's own offer.** Location: ruling `:11–16`. HELP_HUMAN offered "D-PEC-101: K4 with C; K1; V; Notes a; defaults" as "take every recommendation"; the record doesn't mention that. Adding it would strengthen the option mapping. Each mapping is still correct on its own.
4. **The D-PEC-100 reservation is labelled `NOT_PREPARED` although a draft exists on a branch.** Location: `_REGISTER.md:117`. `origin/claude/pec-s2-sow-rebuild-proposal` (`fb25ce08b`) already holds `DRAFT_D-PEC-100_s2_sow_rebuild_proposal.md` with four verifier verdicts. The register defines `AWAITING_RULING` as "packet drafted", but nothing is published on main, and PEC has not added rows before publication (D-PEC-101 had none). So `NOT_PREPARED` with packet `-` is defensible and has a precedent: D-PEC-02 is also `NOT_PREPARED` with `-`. The row must move through its states when the S2 packet is published.
5. **The work graph does not track the pending Notes-line edit.** Location: `WORK_GRAPH.md:82`. The "Ready after the ruling PR merges" line names the act but not the Notes (a) replacement HELP_HUMAN owes in that PR. Only the ruling records it.

### Checks performed
1. **Proposal identity: PASS.**
   - `shasum -a 256` of `_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md` at head gives `7ad176063b10b4cb3093bc9c1d5c6efbab83fcdb5e6a059e6122c466fd095a25`.
   - `git show origin/main:.../PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/DRAFT_D-PEC-101_rev16_currency_setup_proposal.md` gives the same hash, and `cmp` reports the files identical.
   - Review 05 (`REVIEW_PR962_05.md`) records `fill_draft.py` reproducing that hash.
2. **Ruling record: PASS apart from N1.**
   - The quote at `:9` is verbatim.
   - Each resolution maps to the proposal's recommended option (proposal L416–447): Q1 K4+C, Q2 K1 as prepared, Q3 V with the pointer moved only on 0 BLOCKERs, Q4 (a) with the with-K1 text, Q5 `TASK+preparation` and Opus 5.5 high.
   - The grant, limits and run root match the proposal without enlargement.
   - Generator hashes on main: `k4/gen_d101_k4.py` is `075036f0…9e73` in full (`075036f0a8c2…0e73`), and `k1/gen_d101_k1.py` is `4892c6a3…cecb`. Both equal the proposal (L330, L338). The bound options (`--covers`; `--act-date {D}`, default actor, no `--reproduction`) match proposal L340.
   - All 161 targets in `evidence/hold_targets.txt` (161 unique) have identical blob IDs at aca930622, origin/main and HEAD; 0 changed.
   - K1's four basis files are unchanged: `Deliverables.csv` `94ee5d18…9805`, `ScopeLedger.csv` `1d24a4b8…916e`, `SOFTWARE_DECOMP.md` `9374c21f…08eb1`, `PRD.md` `ae49b806…83fbe`.
   - K1's three tools are unchanged: `write_status.sh` `1857ad59…97bc`, `scaffold_deliverable.sh` `7a04c1a9…7a23`, `check_min_viable_fileset.sh` `a6c4af3c…20f8c`.
   - The three A2 `_CONTEXT.md` mirrors and `_COORDINATION.md` are unchanged.
   - The verification tools and method files are unchanged: `analyze_dep_closure.py`, `validate_decomposition_registers.py`, `validate_dependencies_schema.py`, `pec_reliance_hold.py`, `ACTIVE_RELIANCE_HOLDS.csv`, `workflows/index.json`, `update_latest_pointer.sh`, `create_snapshot_folder.sh`. No cited workflow or skill file changed either.
   - PR #962's merge `0883c2108` is on main.
3. **Register: PASS.**
   - Rows at `_REGISTER.md:117` (D-PEC-100) and `:118` (D-PEC-101) each have exactly 7 pipes, so 6 columns.
   - The D-PEC-101 hashes (proposal full hash; generator short hashes) are correct, and its counts are correct (161 = 129 + 20 + 12; 22 rows; 16 execution edges).
   - The review summary "01 FAIL, 02 FAIL, 03 CHANGES REQUESTED, 04 PASS WITH NOTES, 05 PASS" matches the verdict files.
   - The S2 membership in the reservation row matches work graph node S2 (`WORK_GRAPH.md:62`), and the branch exists. See NOTE 4.
4. **Work graph and STATUS: PASS.**
   - `WORK_GRAPH.md:69,72,82–83,175,197` and `docs/STATUS.md:281–283` are true at head.
   - The act is described as dispatched "after the ruling PR merges". No merge of #969 or of the act is claimed; the only "merged" statement is PR #962, which is true.
   - The STATUS change is traced under D-PEC-88 (`:197`).
   - No added line prompts about CHECKING. The ruling's `:53` disclaims it.
5. **Containment: PASS.**
   - `gh pr view` and `git diff --stat origin/main...HEAD` list exactly five files: `docs/STATUS.md`, the POST-SCA005 `WORK_GRAPH.md`, `_DECISIONS/D-PEC-101_RULING_2026-09-26.md`, `_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md` and `_DECISIONS/_REGISTER.md`.
   - `git diff --check origin/main...HEAD` exits 0.

**Every-PR checks** (run from the repo root):
- `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` exits 0, with no finding on any PR file.
- `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` exits 0 (VALID).
- CI on #969: `pec`, `harness`, `Harness pre-merge`, `Desktop E2E` and the Select coverage jobs pass; the rest are skipped.

### Relevant paths
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-101_RULING_2026-09-26.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md (the changed notice behind N1)

## Disposition (HELP_HUMAN)

| Finding | Disposition |
|---|---|
| N1 (main-change description incomplete) | Repaired in `7720702f7`: the ruling lists the work graphs, review returns, preparation folder and brief/return copies, and the `NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md` erratum, and states that all pinned inputs are unchanged |
| NOTE 1 (one act as method choice) | Repaired: labelled HELP_HUMAN's method choice |
| NOTE 2 (Notes (a) timing, preimage, fallback, containment) | Repaired: after the act's independent verifier passes K1; preimage pinned; no edit and the question returns to the owner if the preimage changed or K1 fails or is reverted; the act's containment admits the one hunk |
| NOTE 3 (offered string) | Repaired: the record says HELP_HUMAN offered this exact string as taking every recommendation |
| NOTE 4 (D-PEC-100 `NOT_PREPARED`) | No change: nothing is published on main; the row moves through its states when HELP_HUMAN publishes the S2 packet |
| NOTE 5 (graph does not track the Notes edit) | Repaired: the graph's Order line names it |
