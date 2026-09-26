# D-PEC-101 preparation — review 02 (in-run backcheck of b6a56559d)

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by the K14P manager; its report reached HELP_HUMAN after the manager's forced handback and is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `b6a56559d7df5031861c41d7259da6488f8ab26b` (prep folder byte-identical at `a02cff692`).
- **SHA-256 of the report text below (UTF-8, trailing newline stripped):** `c3c5a0037f2be0f42f977b734a7b964fc19c0beb2fea8f8071203a43dd834d83`.

## Report (verbatim)

## K14P review 02: fresh read-only TASK reviewer (claude-opus-5-5, high)

**Verdict: FAIL.** There is one BLOCKING finding. The repair for review-01 N1 introduced a new false verification claim. Everything else backchecks clean.

**Heads reviewed**
- **Packet:** `b6a56559d7df5031861c41d7259da6488f8ab26b`.
- **Branch movement during the review:**
  - Local HEAD advanced to `52ffa1db0`, a commit that changes only the return file.
  - The remote PR #962 head is now `a02cff6923b31dcb147d8b18e2aad8c7d2b204c4`, a merge of `origin/main` `dfb089b8a` into the branch.
- **Prep folder:** byte-identical across `b6a56559d`, `52ffa1db0` and `a02cff692` (`git diff --quiet b6a56559d a02cff692 -- <prep folder>` exit 0).
- **Tree at `a02cff692`:** equals `dfb089b8a` plus the branch files.
- **Return file:** reviewed at `52ffa1db0` (the same bytes as at `a02cff692`).

**Preflight:** `pec_reliance_hold.py --operation candidate-validation` returned ALLOW (exit 0) for the draft and for the return. The register has a header and no rows.

### BLOCKING

**B1 (new; regression from the N1 repair).** The combined-tree K4 verifier expectation is false.

- **Where:** `DRAFT_D-PEC-101_rev16_currency_setup_proposal.md:361` (`.src.md:147`), Required result cell. It says: "run the K4 verifier with the K1-applied tree as its before-state (PASS)".
- **What I ran:** on a fresh `git archive` of `origin/main` `dfb089b8a`, I applied K1 and then K4 `--covers`. I then ran `verify_d101_k4.py <K1-applied tree> <K1+K4C tree> --covers`, with and without `--allow-k1`.
- **Result:** exit 1 both times, with 2 FAILs:
  - `FAIL pre-state census  68 contexts / 68 references; std 61, d93 2, refs 66`
  - `FAIL the 64 D-PEC-62-scaffolded contexts share one provenance block  66 contexts, 3 distinct`
- **Cause:** the verifier hard-codes the pre-state population (`k4/verify_d101_k4.py:104`, `== (66, 66, 61, 2, 66)`; `:166`, `len(scaffolded) == 64`). A K1-applied before-state therefore cannot PASS.
- **Evidence gap:** no evidence file records this run. The cited `k1/evidence/verify_k4_on_both.out` is the original-export run.
- **The rest of the sentence is accurate.** Against the original export, `verify_d101_k4.py base K1+K4C --covers --allow-k1` gives exit 1 with exactly one FAIL: containment, "changed 149 (expected 129)", with the 20 extra paths being K1's modified files. `verify_d101_k1.py base K1+K4C --allow-k4` gives exit 0.
- **Why this blocks:** the owner rules on this verification table, and it is the act's acceptance criterion. For the recommended order (K1 then K4), it states a result that a correct act cannot produce. This is the same reason review 01 blocked on B1.
- **Fix:** drop the "K1-applied before-state (PASS)" instruction and keep the original-export expectation (one containment FAIL listing K1's 20 paths). Alternatively, state that with a K1 before-state the census and provenance-block checks fail by design. Then update the review-01 disposition row for N1 and the return's line 45 ("All findings repaired").

### NON-BLOCKING

**N1.** The return overstates the repair. `returns/K14P_REV16_CURRENCY_SETUP_PROPOSAL.md:45` says "All findings repaired in `b6a56559d`". N1's repair is inaccurate (B1 above). Correct this line when filling `{{VERDICT02}}`.

### NOTES

1. **The list of where K1 embeds the number is incomplete** (`.md:3`, the N5 repair). The parenthetical names "row Notes, provenance, `_DEPENDENCIES.md` Status and Run History, refresh Notes". It leaves out three places:
   - the `_REFERENCES.md` closing line (`gen_d101_k1.py:356`);
   - the Declared Upstream text (`:378`);
   - DEL-10-13 Run Notes (`:402`).

   The conclusion (rebuild K1 if the number changes) is right.

   Also, "K4's bytes carry no packet number" is true of K4's output: none of the 129 postimages contains `D-PEC-101`. The bound `gen_d101_k4.py:2` docstring does say "Provisional D-PEC-101", so a precise wording would be "K4's output bytes".
2. **The bound K1 generator's docstring still carries the Note-1 overstatement** (`gen_d101_k1.py:7-8`, "K1 reads none of K4's targets"). The draft's prose is corrected. The docstring does not affect behaviour; do not rebuild for this.

   Separately, `.md:5` calls the PKG-08/PKG-10 sibling contexts "K4 targets", but the glob (`:506`) also reads the A2 mirrors DEL-08-01 and DEL-08-03, which are not K4 targets. This is trivial.
3. **`check_short_hashes.py` is a weak check.**
   - It accepts a short hash if any file in the working tree, or any full hash quoted in the draft, matches the prefix and suffix. It does not check the file the draft names.
   - For every short hash whose full form is in the basis table, the check is circular: it tests short against full, not against the file.
   - It hashes HEAD, not `aca930622`.

   It is a preparation aid, not bound. I verified independently (below).
4. **The dispatch-preflight TSV has no metadata.** `evidence/hold_dispatch_k4_candidates.tsv` does support the `.md:20` claim: 132 rows (66 `_CONTEXT.md` and 66 `_REFERENCES.md`, i.e. the 129 targets plus the 3 A2 mirrors), all exit 0 with `dispatch-for-production` ALLOW. My own rerun of all 132 gave ALLOW, 0 bad. The TSV does not record the command, cwd, commit or register hash, and the draft does not define "132 candidate files".
5. **The return's placeholder name differs from the brief.** At `52ffa1db0` it is `{{VERDICT02}}` (line 46), not `{{VERDICTS}}`. The brief expected `{{VERDICTS}}`, which was the form at `00bee6b45`/`b6a56559d`.

### Backcheck of review-01 findings

- **B1: repaired.** All eight corrected hashes match their named files at `aca930622`: D-PEC-94 `…1e5a6b`; `projects/pec/AGENTS.md` `…eb8`; `Impact_Assessment.md` `…cb691`; project-setup `WORKFLOW.md` `…dd6d`; `contract.md` `…c218e`; `execution.json` `…ec2d`; dependency-extract `WORKFLOW.md` `…f18c3`; `_COORDINATION.md` `…8a90c` (at both `.md:118` and `.md:421`).
- **Every short hash:** I mapped each of the 45 distinct short hashes (51 occurrences) to its named file and recomputed it with `shasum -a 256` via `git show <commit>:<path>`. All 45 are OK at `aca930622`. At `dfb089b8a`, 44 are OK; the work graph `f2cdfb0e…384f6` differs there, and the draft correctly says "at `aca930622`".
- **Every full hash:** all 50 full hashes in the basis table, plus the brief copy, are OK at `aca930622`.
- **N1: not correctly repaired** (see BLOCKING B1).
- **N2: repaired and accurate.** In `gen_d101_k1.py`, `--actor` is used only in the `write_status.sh` call (line 648) and the `_STATUS.md` history rewrite (line 667). `--reproduction` changes bytes only when the local date differs from the act date.
- **N3: repaired.** The Provenance section now records the resume amendment (`.md:14`), consistent with the return's line 8.
- **N4: repaired** (see Note 4).
- **N5: repaired, with the incompleteness in Note 1.**
- **Note 1: reworded** (`.md:5`), with the residue in Note 2.
- **Note 2: disclosed as finding 7** (`.md:119`). Its supporting claims check out:
  - "gates releases, not successors" is in `DEL-10-02/_DEPENDENCIES.md`;
  - E-A18 is DEL-10-11 → DEL-03-04;
  - the plan names this edge at `Propagation_Plan.md` L275.
- **Note 4: citation fixed.** The quote is at `Propagation_Plan.md` L545.
- **Note 6: aligned.** Lines 134 and 385 now agree: a TASK runs K1, and K4 is run by the TASK or the manager.

### Bound bytes and reproduction

**Generators:** `k1/gen_d101_k1.py` is `4892c6a3…92cecb` and `k4/gen_d101_k4.py` is `075036f0…ef9f0e73`. Both are unchanged.

**No bound byte changed since `540d2ce2a`:**
- Only six files changed in the prep folder: the draft, the `.src.md`, `SHA256SUMS`, and three new files (`REVIEW_VERDICT_01.md`, `check_short_hashes.py`, `evidence/hold_dispatch_k4_candidates.tsv`).
- No file under `k1/` or `k4/` changed.
- The set of 64-hex hashes in the draft differs from `540d2ce2a` only by two added artifact rows (`017f2af1…` and `4faf5ccc…`).

**Fresh reproduction:** I exported `origin/main` `dfb089b8a` with `git archive` into `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/k14p/review02/`. The local date was 2026-09-26, so I ran without `--reproduction`.

| Run | Result |
|---|---|
| K1 | exit 0 |
| K4 `--covers` | exit 0 |
| K1 then K4 `--covers` | exit 0, exit 0 |

With my own aggregate script, every result equals the draft's tables:

| Set | pathlist | pre | post |
|---|---|---|---|
| all_A+C (129) | `bbd1374c…` | `7d6d8016…` | `01bd1f7b…` |
| references_A+C (66) | `dcde7924…` | — | `0168d726…` |
| all_K1 (32) | `c1fbca79…` | — | `483ec239…` |
| modified_K1 (20) | `8c569e60…` | `48e96f72…` | `186d9c72…` |
| created_K1 (12) | `bfca84fa…` | — | `e72fc7e9…` |

- Per-file mismatches: 0 across all 161 preimage and postimage rows.
- The combined tree gives identical K1 and K4+C postimages.
- `verify_d101_k4.py base K4C --covers`: exit 0. `verify_d101_k1.py base K1`: exit 0.

### Packet integrity

| Check | Result |
|---|---|
| `shasum -a 256 -c SHA256SUMS` (131 entries) | exit 0, all OK |
| `k4/SHA256SUMS` (62 entries) | exit 0, all OK |
| Draft's Preparation-artifacts table (17 rows) | all OK |
| `fill_draft.py` run on a `git archive HEAD` copy in scratch | exit 0; `cmp` with the committed draft: exit 0 (byte-identical, `bcaf5327…`) |
| `check_short_hashes.py <worktree>` | "45; unresolved: 0", exit 0 |

### Return accuracy (`52ffa1db0`)

The following are accurate:
- the brief hash;
- the `daa69a74…9d16` child-brief hash;
- the census, row counts and validator table;
- the rebase and CI statement ("Update the PR base"). PR checks are now green after the merge.

The one inaccuracy is "All findings repaired" (NON-BLOCKING N1).

### Containment

`git diff --name-status origin/main...<head>` shows 135 entries, all additions, at each of `b6a56559d`, `52ffa1db0` and `a02cff692`. All of them are in the prep folder, the brief copy and the return.

### Commands and exit codes (beyond those above)

| Command | Exit |
|---|---|
| `git fetch origin` | 0 |
| `harness.py self-check` | 0 |
| `validate_pec_loop_receipts.py --repo-root .` | 0 (VALID) |
| `pec_reliance_hold.py` `dispatch-for-production` ×132 | 0, all ALLOW |
| `gh pr view 962` / `gh pr checks 962` | read-only; OPEN, MERGEABLE, required checks pass |

### Disclosures

- I briefly created and then deleted a throwaway file, `/tmp/x_unused`, outside the scratchpad through a shell redirection.
- Nothing was written in the repository. The worktree status is clean.
- The scratch dir contains four APFS clones of the export (about 2.0G logical each).

Key paths:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-rev16-currency-setup/projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/DRAFT_D-PEC-101_rev16_currency_setup_proposal.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-rev16-currency-setup/projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/k4/verify_d101_k4.py`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-rev16-currency-setup/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/K14P_REV16_CURRENCY_SETUP_PROPOSAL.md`
- My verifier outputs: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/k14p/review02/v1.out` … `v6.out`

## Disposition (HELP_HUMAN)

| Finding | Disposition (HELP_HUMAN, applied after the manager's forced handback) |
|---|---|
| BLOCKING B1 (combined-tree K4 verifier expectation) | Repaired: the verification row now prescribes the original export as the K4 verifier's before-state on a combined tree (exactly one containment FAIL listing K1's 20 paths) and states that a K1-applied before-state fails the census and one-provenance-block checks by design |
| Return overstates "All findings repaired" | Repaired: the return's review-01 line is qualified and its review-02 line filled |
| Embedding list incomplete; "K4's bytes" | Repaired: the list adds the `_REFERENCES.md` closing line, Declared Upstream text and DEL-10-13 Run Notes; K4's *output* bytes carry no number |
| `git diff --check` not clean in `k1/evidence*`; act-time whitespace row | Repaired: `k1/.gitattributes` exempts `evidence/**` and `evidence_aca930622/**` like `k4/`; the draft's whitespace row is scoped to product paths, with a run-root `.gitattributes` |
| B3 "every other cell" | Repaired: except the `Notes` prefix and `LastSeen` shown |
| Packet number 101 vs unassigned 100 | Repaired: the draft says `D-PEC-100` is provisionally taken by the concurrent S2 packet; HELP_HUMAN confirms the number on publication |
| `check_short_hashes.py` weak; K1 docstring wording; TSV metadata; placeholder name; strata; method substitution; add-ons | No change: preparation aids or disclosed choices; reviewers verified independently |
| `origin/main` moved | HELP_HUMAN updates the PR base before merge |
