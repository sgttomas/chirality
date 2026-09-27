# Review 01 of PR #1007, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `052f84cf0c663a4beed06bcb80f4fbbce3efc4c4`. The repairs listed under Disposition, this file and a merge of `origin/main` follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `06efbda1a9bbd4cc80132f505298f8e85479bda5e6160fba722f9e237d11499e`.

## Report (verbatim)

**PR #1007 review (D-PEC-105 act, A + P) at head `052f84cf0c663a4beed06bcb80f4fbbce3efc4c4`**

**Verdict: PASS WITH NOTES.** Nothing is blocking. The product bytes, checks 1–12, premise-only discipline, reliance-hold order, run-root integrity and containment all pass. My own runs reproduced them. The findings are all about record currency.

`origin/main` moved during this review, from `0adfbc747` to `8bbd022b9` (PR #1011). That PR changes only `projects/chirality-app-v4/**` (10 paths), so no D1 pin moved. The PR is still MERGEABLE/CLEAN.

I made no repository or git writes. All reads came from `git archive` exports in my scratch directory, with TMPDIR set there and `PYTHONDONTWRITEBYTECODE=1`. I removed the large exports at the end.

## Findings

**BLOCKING:** none.

**NON-BLOCKING**

1. **Graph "Current state and recovery" lines were not refreshed by the records commit.** The D-PEC-102 act's HELP_HUMAN commit (`5b2105d5f`) did refresh all three, so this breaks the precedent.
   - `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md:159`: "Checked basis" still reads `origin/main` `16010b4ca`. It omits PR #1006 (`c5d852c4a`), PR #1009 and now PR #1011.
   - `WORK_GRAPH.md:168`: "Local or unmerged work: this ruling PR; …". The ruling PR (#1006) has merged. PR #1007 (this act, with these records) is not listed.
   - `WORK_GRAPH.md:169`: "Active operations and ownership" does not list the handed-back D1A manager or its return `returns/D1A_D105_PREMISE_ACT.md`.
2. **A STATUS sentence goes stale when this lands.** `projects/pec/docs/STATUS.md:335-337` says "Still open from Lane B: the DEL-00-03 SPEC premise, the tier-0 profile entry (K3) and the API schema fields." The D1 act closes the SPEC premise item, and STATUS:278-284 and :295-296 already call it done.

**NOTE**

1. `projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/VALIDATION.md:122` says the return's hash "is given in the PR record". The PR body and comments do not give it. The return at head hashes `db9cbfcdbb17367d5fbfbc806eed9e0fdb2c42c6b2cd495d21db61dbf812e8aa`.
2. `STATUS.md:408-411` is the dated D-PEC-72 amendment note, which says "completed SELF_CHECK and exact-hash owner acceptance". It is dated history, not a current claim. No other STATUS or README sentence calls the DEL-00-03 SPEC or the DEL-00-01 ADR "accepted" as current. README has no such sentence, and the old hashes appear only in the frozen `loop/LOOP_RECEIPTS.md`.
3. `WORK_GRAPH.md:66` (D1 row) states "`{PR}` #1007" as settled. HANDOFF_STATE labels it a reading to confirm at M1, and the proposal says the slots are "fixed at closeout". It is acceptable as HELP_HUMAN's own confirmation, but it is not labelled as one.
4. **Verdict 02 is by the same verifier instance, resumed with `SendMessage`.** It was not a fresh context. This is consistent with the grant's "One fresh read-only TASK is the verifier", and `MANIFEST.md:13` discloses it. Both verdicts are independent of the author. The commits after verdict 02 (`7c15f26ad` record repairs, `0002012eb` return, `052f84cf0` records) were checked by no in-run verifier. This review covers them.
5. **Base currency.** `HANDOFF_STATE.md:39` names `0adfbc747` as the merged base, and main is now `8bbd022b9`. I reran the base-drift procedure myself (item 7 below) and it passes. The records do not reflect it.

## Verification by check

1. **Product writes: PASS.**
   - Preimages on main equal the tabled values: `cc9f4754…1bae`, `3e4f0efc…5741`, `f63ecc27…5db5`, `43346150…1740`.
   - Head bytes equal the tabled postimages and the run-root candidates: `f84c067b…f617`, `0fed4ecb…e843`, `ad6bab7e…c49e`, `3757632b…a647`.
   - No `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `REV_*` or `MEMORY.md` path changed, and neither folder has a `MEMORY.md`. Both `_STATUS.md` read `CHECKING`.
2. **Checks 1–12 reproduced: PASS.**
   - `render_candidates.py`: fails=0. My own reverse-apply of every hunk's post→pre on the head bytes gives exactly the `origin/main` preimage for all four targets (22/15/6/3 hunks).
   - Validator: `PASS format=SOW_V1` ×2.
   - Checklists: `a3bc80a0…21b1` and `6e99f93c…8cf9`, byte-identical on rerun and equal to the run-root files.
   - Boundary owners: exit 0, status OK, JSON byte-equal to the run-root copies.
   - Quotes 74/74, state claims 126/126, quote currency 127/127, TARGET-cited rows 0.
   - Strict registers (exit 1, 0 errors, 26 warnings), harness self-check and receipts are identical at head and main, with the export path normalized.
   - `run_d1p_checks.sh` against current `origin/main` `8bbd022b9`: OVERALL PASS. Its SUMMARY equals the stored `rerun_0adfbc747/SUMMARY.out` except for the basis line.
   - Evidence whitespace 0 across all 214 run-root files. `git diff --check origin/main...HEAD` is clean.
3. **Premise-only discipline: PASS.**
   - The 4(a) rebind is exactly as ruled. The frontmatter changes to `@189f205ff02df4111b33c20be441ce06e65ada7a`. OUT-002, REQ-002, REQ-003, AC-003 and the production sequence change to v2.4, and REQ-001 now reads "as brought current to". AX-009 discloses that this goes beyond SCA-006 §B4.
   - The only new IDs are AX-009 and AX-008.
   - I spot-checked the sources:
     - PRD v2.4 has 49 requirement rows.
     - ScopeLedger at 1.6 has 100 items (74 IN, 18 OUT, 8 TBD); Deliverables.csv has 68 rows, with DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 retired.
     - The PKG-00 charter "consumed by the hooks CLI bridge, the only remaining bridge" matches verbatim.
     - PRD §7.1 carries WorkGraph/WorkNode and the Workplan historical-grammar row.
   - ADR posture 3, DEL-00-01 CLM-005 and REQ-004 carry the same elements: sessions, delegation, tools, turn locks and interruption for each App instance; credentials custodied by Codex; local-model residency retired; `D-GOV-43` A2. These match Root CONTRACT K-RUNTIME-1 and K-RESIDENCY-1 at `189f205ff`.
4. **Reliance holds: PASS.** Dispatch ALLOW ×4 at 17:36:57Z, before the check-only (17:37:42Z) and the act (17:38:17Z). Rely ALLOW ×4 at 17:38:29Z, before the act commit (17:38:30Z), then at 18:03:31Z and 18:19:42Z before each verdict fan-in.
5. **Verifiers: PASS.** Their dispositions are truthful. The diff `70c4a1bca..7c15f26ad` is confined to verdict 02, its preflight, the NB-1 and Note 1–3 repairs, and the regenerated SHA256SUMS. Verdict text hashes with the final newline dropped match MANIFEST: `d9b295c2…3ee3` and `9b008f58…b61c`.
6. **Run-root integrity: PASS.**
   - `SHA256SUMS` passes 213/213 and covers every file except itself. The 28 bound files equal their prep hashes, and the prep SHA256SUMS passes.
   - I regenerated the raw scan at `8bbd022b9`: `38095b883af8238b8aa2b55606215166bec1b7e923958efd2cca48d9c637bf29`, 48,144 lines. Its filtered form hashes `0710d293…4d68`, matching the stored files.
   - The add-on M `{PR}`/`{D}` values are labelled as a reading at `HANDOFF_STATE.md:70-75`.
   - The brief copy `fbc69cee…3895` is byte-identical to the scratchpad original `acts2/D1A.md`.
7. **Merge from main: PASS.** Merge `8d85a9b6e` brought in 312 paths, all under `projects/chirality-app-dev/**`. The newer main (`8bbd022b9`) touches only `chirality-app-v4`. The runner's check-only on its export passes, so all pins and preimages are unchanged.
8. **Records commit `052f84cf0`: PASS, apart from NB-1 and NB-2.** The STATUS D1 text (:278-285, :295-296) states the lapses, that AC-011 and AC-007 are unsatisfied, and that RR1 is carried and open. The derivative-review bullet is correct. The graph D1 row is ACTIVE in PR #1007. Order lines :89 and :93, Next work :162 and the D-PEC-88 trace bullet (:246) are correct.
9. **Containment and CI: PASS.**
   - `git diff origin/main...HEAD` touches only the 4 targets, 214 run-root files, the brief, the return, the graph and STATUS (222 paths). `git diff --check` is clean.
   - CI on `052f84cf0`: governance-harness, Harness Pre-merge, pec-tests (`pec`, Select PEC coverage) and Piping Desktop E2E (Desktop E2E source mode, Select App coverage, Select source coverage) all pass. The remaining jobs were skipped. PR state: OPEN, MERGEABLE, CLEAN.

## Paths

- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/` (MANIFEST.md, VALIDATION.md, HANDOFF_STATE.md, VERIFIER_VERDICT_01.md, VERIFIER_VERDICT_02.md, SHA256SUMS)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/D1A_D105_PREMISE_ACT.md`
- Runner output against `8bbd022b9`: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/rev1007.OOgIYy/runner_main/SUMMARY.out`

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 (graph recovery lines): repaired.**
  - The checked basis now names `origin/main` `8bbd022b9` and PR #1006.
  - The unmerged-work line lists PRs #1007, #1010 and #1008.
  - The active-operations line shows none running and names the handed-back D1A, S1A and X1A managers with their returns.
- **NB-2 (Lane B sentence): repaired.** STATUS now says the DEL-00-03 SPEC premise is done under `D-PEC-105`. It lists only K3 and the API schema fields as still open from Lane B.
- **Note 1: repaired.** The return's hash (`db9cbfcd…12e8aa`) is now in the PR record (PR body).
- **Note 2:** no change. It is dated history.
- **Note 3: repaired.** The D1 row labels `{PR}` #1007 as HELP_HUMAN's reading.
- **Notes 4 and 5:** recorded. Verdict 02 came from the same verifier instance, which `MANIFEST.md` discloses. This review covers the later commits and the base drift to `8bbd022b9`.
- **Reviewer footprint:** the reviewer's scratch directory is removed.

The repair head needs a fresh review before merge.
