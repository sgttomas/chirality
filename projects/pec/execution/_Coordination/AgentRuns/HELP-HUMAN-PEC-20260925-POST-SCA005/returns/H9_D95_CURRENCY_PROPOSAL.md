# H9 return: D-PEC-95 draft, transcribed

- **Executor:** `pec-task` (TASK, `claude-opus-5-5`, high). It was read-only, so HELP_HUMAN transcribed its final report verbatim from the host subagent transcript.
- **Brief:** `../briefs/H9_D95_CURRENCY_PROPOSAL.md`, SHA-256 `02fb7370e835a165a3c36f4f044447b598828050c6e2a069a66f0fa8a84945a1`.
- **SHA-256 of the report text below (UTF-8):** `78a55321a8fc640686fa6855cf432f5e182f2cf9e7ef20b72d7f9f75b61751a4`.

## Publication (HELP_HUMAN)

- **The draft** is published unchanged as `_DECISIONS/D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md`, SHA-256 `9137d3872329cea5093f61fb6c4150121e4ffcc2abe900ca88e7339049064b22`. That is the same hash as `D-PEC-95_DRAFT.md` in the preparer's `SHA256SUMS`.
- **The rest of the `h9/` folder** is published unchanged as `../../../PEC_CURRENCY_D95_PREP_2026-09-25/`. Every file listed in its `SHA256SUMS` verifies there, except the draft, which lives at the `_DECISIONS/` path above.
- **Currency re-check on current main.** HELP_HUMAN ran `gen_d95.py --option A --retired-covers --check-only --act-date 2026-09-25` on a `git archive` export of `origin/main` at `bec8bdd65`, which is after PR #919 and PR #920.
  - It exited 0 with aggregate `AGGREGATE option=A+R files=121`.
  - None of the 124 pinned preimages changed after `13df8b795`. The later `projects/pec` changes touch only STATUS, the work graph, decision records and run records, none of which are targets.

- **One file added at publication:** HELP_HUMAN added `.gitattributes` (`evidence/** -whitespace`) to the published folder. The unified diffs and TSV reports carry format-mandated trailing spaces, and this keeps their exact bytes past `git diff --check`, following the App and Piping evidence-folder practice. The file is not in `SHA256SUMS`.

## Report (verbatim)

## H9 return: D-PEC-95 draft (TASK under HELP_HUMAN, read-only)

The D-PEC-95 draft is finished and marked `PROPOSAL / AWAITING_RULING`. Every prototype run passed its checks, and nothing in the repository was changed.

**Draft:** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/h9/D-PEC-95_DRAFT.md`
- SHA-256 `9137d3872329cea5093f61fb6c4150121e4ffcc2abe900ca88e7339049064b22`, 522 lines.
- It records the brief hash `02fb7370…a945a1`.
- Everything is in the same `h9/` folder and listed in `h9/SHA256SUMS` (41 files; `shasum -c` reports all OK).

**Bound generator:** `h9/gen_d95.py`, SHA-256 `0e9ede5044b34cc4594836aab73a0a8df02cd4d1de8ae5e1e5625ebb232ebe78`.
- It pins 124 preimages at `13df8b795`: 121 target files and 3 basis files.
- It stops and writes nothing if any check fails.

Other files in `h9/`:
- `verify_d95.py`: checks the written files after the act.
- `t1_tm_pec_023.py` (`0e0cd6f9…7bec`): the draft TM-PEC-023 row, for WORKING_ITEMS to apply.
- Preparation aids: `build_gen_d95.py`, `gen_d95.template.py`, `run_prototypes.sh`.
- `evidence/`: diffs, generator reports, validator outputs, reliance-hold results, aggregates, and `T1_RERUN.txt`.

### Recommended option
**A + R.** A is N1 + N2 + N3, with dated append-only notes added to the SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md`.
- A touches 121 paths, all of them modified; none is created or deleted.
- Add-on R also rewrites the "covers" bullet in the four retired deliverables' `_REFERENCES.md`, for example "covers none — retired under SCA-005, formerly SOW-029". This adds no paths; it changes the postimage of 4 files already in A.
- R goes beyond the brief's rule that semantic fields stay untouched. Without it, those four files would name revision 1.5 next to a coverage claim that revision 1.5 contradicts. Present A alone if you want to stay strictly inside the brief.

The other options:
- **P (narrower, 119 paths):** leaves the two SCA-005 snapshot files byte-identical. `_COORDINATION.md` then records them as superseded, by hash, as the SCA-004 practice did.
- **Amend** and **Defer** are also written up.
- **Re-audit:** not recommended now, so the audit pointer does not move. SCA-006's pre-change baseline audit will observe this state. If the owner wants one now, it is an amend.

### Counts per item
- **N1: 5 files.**
  - Fenced: `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md` (4 rows and the boundary paragraph), and the two SCA-005 appends.
  - Not fenced: `_COORDINATION.md`, which is default-writable. It gets the revision-1.5 basis bullet, a new dated item 14, and one line in its "Notes (human-owned)" section.
- **N2: 106 files.** 42 contexts and 64 references, across 64 deliverables.
  - Lifecycle states: 28 OPEN, 26 INITIALIZED, 4 CHECKING, 2 IN_PROGRESS, 4 RETIRED.
  - Every path is in the grant table. Edits are confined to the anchor lines. Afterwards all 66 contexts and all 66 references name revision 1.5, and the references also name PRD v2.3.
- **N3: 19 rows in 10 registers.**
  - Only `EvidenceQuote`, `LastSeen` and `Notes` change. `LastSeen` goes from 2026-07-25 to the act date.
  - `Notes` is prefixed "Evidence refreshed under D-PEC-95 (<cause>); ". The cause is an SCA-005 action ID for 16 rows, and PRD v2.2 or SCA-003 for 3 rows.
  - Each new quote comes from the same cited cell or requirement row. Before and after text for every row is in the draft.
  - Active execution quotes that are verbatim go from 92/111 to 111/111.
- **T1:** one row closed as `RESOLVED_BY_DECISION`, then archived.

### Prototype results
All runs were on scratch copies of `13df8b795` (git export plus copy-on-write clones). One shared git clone in the temp directory supplied history for the git-based checks. Local date 2026-09-25; Python 3.13.7.

| Run | Exit | Result |
|---|---|---|
| Option A | 0 | 124 read, 121 written |
| Option A, second fresh clone | 0 | byte-identical tree and report |
| Option P | 0 | 119 written |
| Option A + R | 0 | 121 written |
| Option A at 2026-09-26 (reproduction mode) | 0 | differs only in the date slots and the one derived hash |
| Rerun on the applied tree | 1 | nothing written |
| Wrong date without reproduction mode | 1 | nothing written |
| `--check-only` | 0 | nothing written |
| Strict register validator (A, P, A + R) | 0 | 66 registers, 263 rows, 0 errors / 0 warnings; output byte-identical to before |
| Dependency closure (A, P, A + R) | 0 | `closure_summary.json` identical to D-PEC-93's `bd73806c…187a`: 111 edges, 66 nodes, 0 SCCs |
| Schema validator on the 10 registers | 0 ×10 | valid |
| `verify_d95.py` (A, P, A + R) | 0 | all checks pass; its self-check on the unchanged tree fails as designed |
| Containment (git clone) | — | changed paths equal the write set exactly |
| `git diff --check` | 0 | clean |
| Receipts validator | 0 / 0 | output identical before and after |
| Harness self-check | 0 / 0 | output identical before and after |
| Instruction entrypoints | 0 | pass |
| T1 close, then `taskmgmt validate` on both registers, archive, validate again | 0 | 9 live rows, 16 archived |
| `pec_reliance_hold.py`, exact-correction-preparation, on 123 targets | 0 ×123 | ALLOW |

### T1 answer
The work is already decided by owner acts: the amendment-1 selections, the checkpoint-2-accepted plan §B8, which names this exact closure, and checkpoint 3. But:
- the task-management contract makes disposition a human act that WORKING_ITEMS only applies;
- Root `docs/CONTRACT.md` K-TM-3 names the owner triage session as "the sole disposition authority";
- no owner statement disposes of the register row itself.

So the packet asks one owner question (question 2) rather than treating the disposition as already recorded. The register is default-writable, so no D-PEC-95 grant is needed. A TASK must not write the row.

### Owner questions (in the draft)
1. A, A + R, P, amend or defer. Recommended: A + R.
2. Confirm that TM-PEC-023 closes as `RESOLVED_BY_DECISION` on the existing record, then archive it. Recommended: confirm.
3. Re-audit: none now (recommended), or add one as an amend.
4. The one-line edit in `_COORDINATION.md`'s "Notes (human-owned)" section: include it (recommended). Leaving it out is an amend.
5. Model steer: keep the defaults or state others.

### Unresolved and carried forward
- **Precondition:** PR #919 must merge first, because the N1 texts cite the work-graph path.
- **Ordering:** if SCA-006's baseline audit runs before this act merges, it will report the INFO findings again.
- **DEP-10-05-004** has a weaker warrant after the refresh. Its cited cell no longer names orientation reads. Moving its evidence to SOW-085 would change `EvidenceFile` and `SourceRef`, so that is an amend and was not prepared.
- **Quotes that cite Scope of Work files:** 11 active rows cite a deliverable `ScopeOfWork.md`. SOW currency work may make them stale again. I recommend the SOW packets reuse this generator's quote-currency check.
- **Harness check in the real PR:** the new run-root files may change the harness self-check output, so the draft requires only "no new finding on a target path" rather than identical output.
- **Corrections to earlier records:** D-PEC-93 finding 5 called `_COORDINATION.md` a D-PEC-88 surface; D-PEC-88 covers only `docs/STATUS.md` and `README.md`. `COV-072` means different findings in the checkpoint-3 audit and the post-setup audit, so every N1 text names which audit it means.

### Boundary disclosures
- Nothing was written outside `h9/` and my temp directories, apart from the brief rename noted below.
- The checkout is clean. Its HEAD moved to `87f6bfe30` during preparation through other agents' commits, not mine. Those commits touch none of the target paths.
- Git actions: `git archive` exports; one `git fetch --dry-run`, which changes no refs; and a `git clone --shared` into my temp directory, which reads the repository's objects and writes nothing to it.
- I briefly renamed the first export into a sibling folder under `$TMPDIR` that was not created by `mktemp`. I then moved it into a fresh `mktemp -d` directory and removed the sibling.
- The large exports and clones are deleted. What remains is about 1.2 MB at `/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T/tmp.ubyCyPjneu`.
- The T1 steps in `run_prototypes.sh`'s `RESULTS.tsv` came from an earlier wording of the T1 script. The rerun with the final script is recorded in `evidence/T1_RERUN.txt`.

The serving model is Opus 5.5, as the host reports. The TASK role and high effort are instruction-asserted. There was no delegation.
