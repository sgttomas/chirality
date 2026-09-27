# Review 01 of PR #989, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `2b75f972e6e129b33c8ca2b6bde7350132dca800`. The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `0f4b7fbaa2d4278da5da976f75ebba03089fde4616b9c747babe2805919bc4e7`.

## Report (verbatim)

**Review of PR #989 at head `2b75f972e6e129b33c8ca2b6bde7350132dca800` (branch `claude/pec-d103-ruling`, base `origin/main` `4b930819c`). Verdict: PASS WITH NOTES.**

Nothing blocks. The ruling is faithful to the owner's words and to the proposal, and every hash and count I checked is correct. I found three non-blocking record gaps, all in the graph or the ruling's publication text, and five notes. I stayed read-only: no edits, no git writes, no checkout or switch. I made one `mktemp -d` export under the scratchpad and deleted it.

## What I verified

**Proposal hash and containment**
- The draft at `4b930819c`, the published `_DECISIONS/D-PEC-103_first_sows_del_08_06_10_13_proposal_2026-09-26.md` and the draft at the head all hash to `cfc2e65d5ae91f0d62d4ef993bc22a91d2bb4716969d083ae98f0fc948eb5417`, so the publication is byte-identical.
- Exactly the five expected paths change (2 added, 3 modified).
- `git diff --check 4b930819c 2b75f972e` is clean.
- CI at the head is finished: all 7 non-skipped checks pass, including `harness` (1m51s); 6 skip. The PR is MERGEABLE.

**Prep hashes**
- `shasum -a 256 -c SHA256SUMS` passes all 66 entries.
- `apply_k2.py` is `b10461fa…257a` and `apply_k2_c8.py` is `093130c8…84e9`.
- The candidates are `aecc5131…0826` and `c7743ee2…6633`.
- The S postimages are `75366b6b…a127` and `3771d526…e567`.
- The C8 postimage is `609aa807…5693`.
- DEL-10-13 `_DEPENDENCIES.md` at the head is `5087e581…eb63`. Diffing it against the C8 postimage shows exactly one inserted line (line 7), after the `- **Notes:**` line and inside `## Dependency Tracking Mode` (lines 3–9).
- All 17 `PINNED` hashes in `apply_k2.py` match at the head, and both target files are absent.

**Faithfulness (K-AUTH-1)**
- Each question's resolution (ruling lines 52–58) matches the owner's words "A; S; M; C8; defaults" and the proposal's questions 1–5 and add-on sections.
- C8 is recorded as the owner's explicit selection and own classification, writing one line in the human-owned section (line 57). It matches proposal lines 262–264 and 442.
- The order A → C8 → verifier → S (lines 60–67) is labelled as HELP_HUMAN's method choice and is admissible under the proposal's rules:
  - C8 pins A's DEL-10-13 postimage (proposal line 285), so it must follow A.
  - C8 and S never run concurrently.
  - S runs only after the validator and the verifier pass (proposal lines 236–238).
- The Limits (lines 88–95) agree with the proposal's Limits (lines 417–431), including the C8 exception for CON-001.
- The execution note (lines 80–84) is true to the script. `inventory()` walks `projects/pec` and prunes the resolved `SELF_DIR`, which is the whole run root, so output written there is admitted. This is unlike `apply_d98.py`, the reason D-PEC-98 needed its note.

**Numbers and citations**
- PR #987's in-run verdicts: 01 FAILED (one blocking finding, B-1, repaired), 02–05 PASS WITH NOTES.
- PR reviews: `REVIEW_PR987_01` PASS WITH NOTES (4 notes), `_02` PASS WITH NOTES (2 notes, draft repaired to `cfc2e65d`), `_03` PASS (no notes). The ruling, register row and graph row state these correctly.

**Register rows**
- Both new rows have 6 columns and follow the house style.
- The D-PEC-102 row copies the D-PEC-100 reservation row (PR #969, merge `f392294b5`) template for template.
- Its eight deliverables match graph row S4 (line 64), correctly leaving out DEL-00-03, which goes through D1.
- `claude/pec-s4-sow-currency-proposal` exists on origin at `7da048c83` and holds `DRAFT_D-PEC-102_s4_sow_currency_proposal.md` with those eight candidates. It has no PR yet.
- The D-PEC-103 row matches the ruling and the proposal.

**Graph and STATUS edits**
- PR #986 is open and titled "S1 Scope of Work currency — preparation packet (provisional D-PEC-104)".
- PR #982 (`ce99bc256`) is an ancestor of `4b930819c`.
- `REVIEW_PR982_02` N1 exists. The retirement graph's C1 row (line 33) still says "a supported no-change result", so the carried note is true.
- The K2P return and the S4P/S1P briefs exist where the graph says.
- `ACTIVE` has been used before in this graph for ruled nodes awaiting their act.
- The STATUS sentence (lines 298–299) is true.

## BLOCKING

None.

## NON-BLOCKING

1. **Stale Order line in the graph.** `WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md:84` still reads "Ready now: packet preparation for K2 (first SOWs for DEL-08-06 and DEL-10-13), since K1 is done". This contradicts the updated K2 row (line 70, ACTIVE, ruled) and the Next-work entry (line 154). PR #971's review 01 had the same gap, and it was repaired ("graph Order lines"). Suggested repair: mark the K2 packet done and ruled, with the act next.

2. **M1 row does not list D-PEC-103 add-on M.** `WORK_GRAPH.md:76` lists only D-PEC-98 and D-PEC-100 add-on M, although the K2 row (line 70) says "Add-on M at M1". PR #971's review 01 repaired this for D-PEC-100 ("M1 names D-PEC-100 add-on M"). Suggested repair: add "`D-PEC-103` add-on M: WORKING_ITEMS creates `MEMORY.md` for DEL-08-06 and DEL-10-13" (proposal line 252).

3. **The ruling never mentions the D-PEC-102 reservation.** `_DECISIONS/D-PEC-103_RULING_2026-09-26.md:101–102` authorizes only "this decision record, the publication of the proposal, and the D-PEC-103 register row". The PR also adds the D-PEC-102 reservation row, and the ruling mentions it nowhere. The precedent `D-PEC-101_RULING_2026-09-26.md` names its reservation twice: under Selected instrument ("The number `D-PEC-100` is reserved…") and in Publication ("… and the D-PEC-100 reservation row"). Suggested repair: add the same clause.

## NOTES

1. **Grant wording.** Ruling line 73 puts "in the run root `execution/_Coordination/SOW_INIT_K2_{D}/`" in front of all five grant items. That includes item 5, the `MEMORY.md` files, which are written in the deliverable folders at M1, not in the run root. The proposal's text governs and nothing is enlarged. Cosmetic.

2. **S4 branch missing from the unmerged-work line.** `WORK_GRAPH.md:158` ("Local or unmerged work") lists this PR and PR #986 but not the unmerged S4 branch (`claude/pec-s4-sow-currency-proposal`, no PR yet). Line 159 names that branch under active operations, so nothing is hidden.

3. **Retirement graph C1 wording.** `WORK_GRAPH.md:156` records the carried N1 wording instead of applying it. Applying it would touch the retirement graph, which is outside this PR's containment, so this is acceptable. The retirement graph (line 33) also still reads "READY FOR FINAL MERGE — PR #982" although #982 has merged. That is left for the same next touch.

4. **HELP_HUMAN's presentation cannot be checked against files.** Ruling lines 11–26 describe HELP_HUMAN's own presentation. No file records it, so I can check only that its content agrees with the proposal and the reviews, which it does. The D-PEC-98 and D-PEC-101 rulings report their presentations the same way.

5. **Execution note detail.** Ruling line 80 says the script inventories everything "except its own directory". It also prunes `.git` and `__pycache__` directories (`apply_k2.py`, `inventory()`). This does not affect the note's conclusion.

## Relevant paths

All read from the head via `git show` or an archive export:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-103_RULING_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-103_first_sows_del_08_06_10_13_proposal_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (lines 119–120)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` (lines 70, 76, 84, 152–159, 181, 194, 224)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md` (lines 298–299)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/apply_k2.py`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/apply_k2_c8.py`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/REVIEW_PR987_01.md`, `_02.md`, `_03.md`, `REVIEW_PR982_02.md`, `REVIEW_PR971_01.md`

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 (stale Order line): repaired.** The graph's Order list now records the K2 packet as done (PR #987, `4b930819c`) and ruled A + S + M + C8, with its act next. X1's "Ready now" line stands alone.
- **NB-2 (M1 row): repaired.** Row M1 now names `D-PEC-103` add-on M: WORKING_ITEMS creates `MEMORY.md` for DEL-08-06 and DEL-10-13.
- **NB-3 (reservation not in the ruling): repaired.** The ruling's Selected-instrument section now says `D-PEC-102` is reserved for the S4 packet because D-PEC-103 was ruled first. Its Publication section authorizes the D-PEC-102 reservation row, following the `D-PEC-101` precedent.
- **Note 1 (grant wording): repaired.** The grant now says the run root applies to items 1–4.
- **Note 2 (S4 branch): repaired.** The unmerged-work line now names branch `claude/pec-s4-sow-currency-proposal` (no PR yet).
- **Note 3 (retirement graph): carried.** It stays outside this PR's containment. At the next touch of the retirement graph, its C1 wording and its "READY FOR FINAL MERGE" state will both be brought current.
- **Note 4 (presentation account): no change.** The account follows the D-PEC-98 and D-PEC-101 practice.
- **Note 5 (inventory detail): repaired.** The execution note now also names the pruned `.git` and `__pycache__` directories.

The repair head needs a fresh review before merge.
