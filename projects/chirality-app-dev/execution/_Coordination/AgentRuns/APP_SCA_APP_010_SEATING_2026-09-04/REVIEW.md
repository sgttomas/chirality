# REVIEW — APP_SCA_APP_010_SEATING_2026-09-04 (independent, read-only)

**RunID:** `APP_SCA_APP_010_SEATING_2026-09-04` · **Node:** N3 (independent review) · **Date:** 2026-09-04

**Basis reviewed:** branch `claude/sca-app-010-seating` at `787a551e70d9fb33f6f9a9fe228443d890a8d02d` (= `origin/main`), uncommitted working tree.

**Frozen diff hash, recomputed live:**

```
git diff -U3 -- . ':(exclude)projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04' | shasum -a 256
a4cfc7f04715eea96a95100a655fa21ec5c22fe31fb7341734826334d2d5a9ef
```

Matches `Evidence/frozen_diff.patch` (SHA-256 `a4cfc7f04715eea96a95100a655fa21ec5c22fe31fb7341734826334d2d5a9ef`). The live tree is the frozen diff.

## Verdict

**PASS** — zero BLOCKER findings. The verdict follows the brief's definition (FAIL only on a BLOCKER).

Counts: **BLOCKER 0 · MAJOR 2 · MINOR 4.** The two MAJOR findings are one-line repairs in five carriers (DEL-03-02 and the four outside carriers) and should be applied and re-frozen before push; they do not touch any item text, gate, lifecycle field, or authority surface. Per-carrier verdicts below mark a carrier FAIL when it carries a MAJOR finding, so that N3's "review PASS per carrier" gate is not read as satisfied for those five rows until repaired.

## Findings

| # | Severity | File | Line | Defect | Suggested fix |
|---|---|---|---|---|---|
| F1 | MAJOR | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-02_Thin_TurnEngine_and_Session_Locking/_STATUS.md` | 10 (item at 12) | The pre-existing `None.` line remains directly under `## Remaining` while the new item `DEL-03-02-V3-01` is listed below it, so the section reads "None." and one open item at once; a reader or mechanical discovery over `## Remaining` gets a contradictory work surface. | Delete line 10 (`None.`) in the same tranche; it is a structural placeholder, not an item, so removing it does not breach the "no existing item edited or removed" rule; disclose the edit in `MAPPING.md` §D and refreeze the diff. |
| F2 | MAJOR | `execution/PKG-02_…/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/MEMORY.md` L10; `execution/PKG-05_…/DEL-05-04_Runtime_Replay_and_Transcript_View/MEMORY.md` L39; `execution/PKG-09_…/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/MEMORY.md` L89; `execution/PKG-01_…/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/MEMORY.md` L15 | as listed | Each outside-carrier MEMORY line says "the applied decomposition row and the SCA-APP-010 Gate-5 Current Contract section in `ScopeOfWork.md` state the current responsibility", but none of the four `ScopeOfWork.md` files has that section (they remain pinned to `7b0be4d8…` / `d6f6cadb…`; `grep -c 'SCA-APP-010 Gate-5 Current Contract'` = 0 in all four), and the paired `_STATUS.md` history line correctly says "seating only, no Scope of Work, context, or reference change"; the paired read contradicts itself and points at a nonexistent section. | Reword the four MEMORY lines to name only the applied decomposition row (e.g. "the applied decomposition row L309/L339/L381/L300 states the current responsibility; this carrier is outside the thirteen and its `ScopeOfWork.md` was not aligned in this pass"); refreeze. |
| F3 | MINOR | `execution/PKG-02_…/DEL-02-04_Toolkit_Options_and_Local_UI_State/ScopeOfWork.md` L108; `execution/PKG-08_…/DEL-08-01_…/ScopeOfWork.md` L55; `execution/PKG-06_…/DEL-06-03_…/ScopeOfWork.md` L58; `execution/PKG-05_…/DEL-05-02_…/_STATUS.md` L22; `execution/PKG-09_…/DEL-09-04_…/_STATUS.md` L113; run `MAPPING.md` §A rows L17, L21, L31 and §E L70 | as listed | The "rulings cited" record is inconsistent across surfaces: DEL-02-04's Gate-5 section says "Ruled questions applied here: Q3 (retired routes), Q14 (organisation layer)" although MAPPING §A records "none" for DEL-02-04-V3-01, the item cites no Q, and neither Q bears on row L310; DEL-08-01's section names Q14 and DEL-06-03's adds Q13 where MAPPING §A records none / Q11, Q12; conversely MAPPING §A/§E record Q13 for DEL-05-02-V3-02 and Q5 for DEL-09-04-V3-02 but neither item's Plan line names the question. No gate or obligation is affected. | Make MAPPING §A/§E, each Gate-5 "Ruled questions applied here" line, and each item's Plan line agree (recommended: DEL-02-04 → "none"; DEL-05-02-V3-02 Plan → add "Q13 ruled 2026-09-04 (SR-24)"; DEL-09-04-V3-02 Plan → add "Q5 ruled D-APP-108 (icon only)"). |
| F4 | MINOR | `execution/PKG-02_…/DEL-02-03_…/_STATUS.md` L29; `PKG-04_…/DEL-04-04_…/_STATUS.md` L21; `PKG-05_…/DEL-05-02_…/_STATUS.md` L30; `PKG-05_…/DEL-05-04_…/_STATUS.md` L34; `PKG-07_…/DEL-07-01_…/_STATUS.md` L21; `PKG-07_…/DEL-07-03_…/_STATUS.md` L21; `PKG-08_…/DEL-08-01_…/_STATUS.md` L21; `PKG-01_…/DEL-01-03_…/_STATUS.md` L12; run `build_seating.py` L729; run `MAPPING.md` §D.11 L65 | as listed | MAPPING §D.11 discloses newest-first insertion only where a History section is newest-first, "else appended at the section end (detected from the first two dated bullets)"; the builder's tie-break (`dates[0] >= dates[1]`) treats the equal first dates `2026-05-20, 2026-05-20` as newest-first, so in these eight oldest-first History sections (which run 05-20 … 07-12 or … 09-03, with the A12 lines of 2026-09-03 appended at the end in DEL-05-02 and DEL-05-04) the 2026-09-04 line was inserted at the top, out of chronological order and unlike the A12 precedent in the same files. Content is unaffected. | Either move the eight lines to the end of their History sections (refreeze), or amend MAPPING §D.11 to disclose the equal-date tie-break and the resulting placement. |
| F5 | MINOR | `execution/_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md` L50 (Q4 "Ruling as applied"); `execution/PKG-02_…/DEL-02-03_…/_STATUS.md` L13 | as listed | "PDF and Quick Look previews uncapped" is not in either selected option's text (Q4a: "Chromium renders PDF inside the right panel"; Q4b: "10 MB in-panel text cap … Larger files show size and an Open in default app action"); it is the agent's inference, carried into DEL-02-03-V3-01's Plan and Return lines. The record's Attribution section does label the column as the agent's reading, so this is not a misattribution; it is a reading the owner has not explicitly confirmed. | Ask the owner to confirm "uncapped" for PDF and Quick Look by reply, or soften the two lines to "cap applies to the in-panel text path; PDF and Quick Look preview limits not ruled". |
| F6 | MINOR | run `ORCHESTRATION_PLAN.md` (header, "Supervisor and applicator"); ruling record Attribution section | — | The WORKING_ITEMS alignment (DOWNSTREAM_HANDOFFS row 2 / OAM step 18: "under sealed briefs … reviewed exact post-images") was performed by HELP_HUMAN through the deterministic `build_seating.py` rather than by WORKING_ITEMS-dispatched sealed briefs; APP-HOLD preflight (17 × ALLOW), paired pre-image freezing, and this post-image review were performed, and the ruling record and plan disclose the substitution truthfully ("acting … as WORKING_ITEMS' applicator … role not mechanically enforced"). Recorded for the owner's byte review; not an attribution defect. | None required; the owner may confirm the mechanism at merge. |

No sentence in any history line, MEMORY line, the ruling record, the register row, or the Root notice attributes to the owner an act beyond those the ruling record quotes (adoption of the list as presented; outside items in the same pass; alignment in the same PR; the eleven question selections; the Q8 routing authorization; the G1-CONFIRM Root write grant and G2-CONFIRM SOW-007 retirement, both verified verbatim in the SCA-APP-010 `Decision_Log.md`). No line claims implementation, lifecycle, dependency acceptance, release, or Root acceptance.

## Per-carrier verdicts

Rule used: PASS = no BLOCKER or MAJOR finding in that carrier's touched files; FAIL = at least one. MINOR findings are noted but do not fail a row.

| Carrier / surface | Verdict | Note |
|---|---|---|
| DEL-02-01 (13) | PASS | 4 items (V3-01..04), gates = seeded, 7 fields each, Trace L307, Q9/Q1/Q6/Q5 consistent with ruling; SOW re-pinned `@dbd812a5…`, refs `[SOW-001, SOW-005]`/`[OBJ-001]`, Gate-5 section verbatim, matrix basis cell names SCA-APP-010, SCA-APP-004 section retitled and kept; `_CONTEXT`/`_REFERENCES` (REF-010..013, WI-001..005, DEP-001/002) exact; validator PASS. |
| DEL-02-02 (13) | PASS | V3-03 `SELECTABLE`, V3-04 gate = seeded; Q3/Q15/Q16 consistent; existing V3-01/V3-02 untouched; display name renamed to row name; refs `[SOW-006, SOW-081, SOW-082]`; OUT-001 label renamed with dated history; REF-010..013, WI-006..010, DEP-003/004; validator PASS. |
| DEL-02-04 (13) | PASS | V3-01 gate = seeded; Depends names DEL-02-03-V3-01 (§C); alignment exact (WI-011..015, DEP-005/006); validator PASS. MINOR F3 (Gate-5 "Q3, Q14" line). |
| DEL-02-05 (13) | PASS | V3-05 gate = seeded; Q7 (local model status only, no OpenAI/API indicator) and Q8 (ships no notice; routed notice named) consistent; Depends names DEL-02-03-V3-01 (§C); Trace OUT-002/AC-002/VER-002 exist; alignment exact (WI-016..020, DEP-007/008); validator PASS. |
| DEL-03-02 (13) | **FAIL** | Item and alignment correct (gate = seeded; WI-021..025, DEP-009/010; validator PASS) but MAJOR F1: `None.` left under `## Remaining` above the new item. |
| DEL-04-04 (13) | PASS | V3-01 gate = seeded; Q14 (G2-CONFIRM) cited; live file `persona-manager.ts` named with the row label (§D.3); alignment exact (WI-026..030, DEP-011/012); validator PASS. MINOR F4 (history placement). |
| DEL-05-02 (13) | PASS | V3-02 gate = Root acceptance routed to App (Root DEL-02-10), matches §A; alignment exact (WI-031..035, DEP-013/014); validator PASS. MINOR F3 (Q13 not named in item), F4. |
| DEL-06-03 (13) | PASS | V3-01 gate = seeded; Q11/Q12 tuple consistent with plan §6; alignment exact (WI-036..040, DEP-015/016); validator PASS. MINOR F3 (Q13 added in Gate-5 line). |
| DEL-07-01 (13) | PASS | V3-01 `SELECTABLE`; Q14 cited; alignment exact (WI-041..045, DEP-017/018); validator PASS. MINOR F4. |
| DEL-07-03 (13) | PASS | V3-01 `SELECTABLE`; Q10/Q16 consistent; alignment exact (WI-046..050, DEP-019/020); validator PASS. MINOR F4. |
| DEL-08-01 (13) | PASS | V3-01 gate = seeded; Depends discloses that the 2026-09-04 session Root grant does not carry forward to `agents/**`/`skills/**`; alignment exact (WI-051..055, DEP-021/022); validator PASS. MINOR F3, F4. |
| DEL-08-03 (13, record-only) | PASS | No item seated; one history line (G2-CONFIRM SOW-007 retirement verified verbatim); `## Remaining` empty; Gate-5 section and `_CONTEXT` prose verbatim from row L370; WI-056..060, DEP-023/024; validator PASS. |
| DEL-08-04 (13) | PASS | V3-02 gate = seeded; existing V3-01 untouched; Trace OUT-001/002, AC-001/002, VER-001/002 exist; alignment exact (WI-061..065, DEP-025/026); validator PASS. |
| DEL-02-03 (outside) | **FAIL** | V3-01/V3-02 gates = seeded; Q4a/Q4b/Q2 consistent; `_STATUS`/`MEMORY` only, no SOW/context/reference write (§D.7 honoured). MAJOR F2 (MEMORY L10 cites a Gate-5 section that does not exist here). MINOR F4, F5. |
| DEL-05-04 (outside) | **FAIL** | V3-02 (collision with existing V3-01 handled per §B) gate = seeded; seating-only. MAJOR F2 (MEMORY L39). MINOR F4. |
| DEL-09-04 (outside) | **FAIL** | V3-02 (collision handled per §B) gate = seeded; F-APP-2 named; seating-only. MAJOR F2 (MEMORY L89). MINOR F3 (Q5 not named in item). |
| DEL-01-03 (outside, record-only) | **FAIL** | No item; history line records the §10 copy table as offered, not adopted (consistent with plan §7 and the ruling's "copy-table note"); `## Remaining` empty. MAJOR F2 (MEMORY L15). MINOR F4. |
| Ruling record D-APP-108 | PASS | Owner text quoted verbatim with option descriptions; "Ruling as applied" column matches every item and Gate-5 section for Q1, Q2, Q3, Q4a, Q4b, Q5, Q6, Q7, Q8, Q9, Q15, Q16; Q10–Q14 correctly deferred to SR-24 / G2-CONFIRM; scope exclusions stated; attribution labelled. MINOR F5 (Q4 "uncapped" is an inference). |
| Register `_REGISTER.md` | PASS | Exactly one added row (D-APP-108), 6 columns like D-APP-106/107, status `RULED (owner direction in chat and option selections 2026-09-04)`, eleven questions named, no other row touched. |
| Root notice (repo root) | PASS | Only write outside `projects/chirality-app-dev/`; draft SHA-256 `f197b31e…` recomputed and matches (live and `origin/main`); three dependencies preserved from the draft with seated item ids added; applied identities correct (decomposition `c7c05169…` at `dbd812a5…`, PR #708 merge `7795b0972…`; companion `63383f04…`; pointer `b297f43e…`, PR #711 merge `311a2f0b8…`; ledger 84 rows SOW-001..084; 10 packages / 52 deliverables; corpus v20 no drift); claims no Root authority; Q8 authorization and G1-CONFIRM grant quoted accurately. |
| Run packet | PASS | `pre_images.json` (74 entries incl. the read-only decomposition) all equal `origin/main`; `post_images.json` (73 entries) all equal the live tree; `seeded_items.json` = live gates; 17 × APP-HOLD `ALLOW` at `repo_head 787a551e…`; validation evidence consistent with my reruns; `build_seating.py` writes only the seventeen carriers' files plus its own Evidence. MINOR F3/F4 in `MAPPING.md`. Note: `VALIDATION_EVIDENCE.md` was absent from the packet when this review began and appeared during it (written by the applicator, not by this reviewer); it is outside the frozen diff and was not reviewed here. |

## Checks performed (results)

1. **Write-set containment — PASS.** `git status --porcelain`: 76 tracked changes = 17 × (`_STATUS.md`, `MEMORY.md`) + 13 × (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`) + ruling record (A) + `_REGISTER.md` (M) + root `NOTICE_2026-09-04_APP_SCA-APP-010_SHELL_REDESIGN_ROOT_DEPENDENCIES.md` (A); untracked = the run packet only. Nothing under `frontend/`, `docs/`, `_Decomposition/`, `_ScopeChange/`, `Dependencies.csv`, `_DEPENDENCIES.md`, `loop/`, or `_TaskManagement/`.
2. **No forbidden state change — PASS.** `git diff -U0` over all touched `_STATUS.md`: no `-`/`+` line for `Current State`, `Checking Approval SHA`, `Authorization Basis`, `Directive`, or `P06 Record`; the only removed lines are `Last Updated` values (updated to 2026-09-04, as A12 did); no removed line in any `MEMORY.md`; no dependency register changed.
3. **Seating fidelity — PASS (F3 minor).** Script over all 20 items: each present exactly once in `## Remaining`; ID absent from `origin/main`; gate string equals `seeded_items.json` and MAPPING §A; field lines exactly `Trace, Plan, Depends, Write locus, Checks, Return, Removed when` in A12 order; Trace row number equals the carrier's row line (L300/307/308/309/310/311/318/329/337/339/348/357/359/368/370/371/381 verified by `sed -n`); cited SOW/OI/DEC anchors (L171, 172, 174, 176, 177, 178, 180, 251–254, 602, 634) verified; every cited OUT-/AC-/VER- id exists in the carrier's `ScopeOfWork.md`; every Q citation consistent with the ruling record. DEL-08-03 and DEL-01-03: history line only, `## Remaining` empty.
4. **Alignment fidelity — PASS.** Thirteen carriers: `decomposition_basis` ends `@dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (the last commit touching the decomposition on `origin/main`; live SHA-256 `c7c05169…` confirmed); `project_scope_refs`/`package_objective_refs` equal the row's SOW/OBJ columns; Gate-5 section quotes Description, Notes, Outputs verbatim (whitespace-normalised); H2 order intact; `validate_scope_of_work.py` PASS ×13; `_CONTEXT.md` DeliverableName = row name (DEL-02-02 renamed), Deliverable Scope = Description + "Applied decomposition row L… notes:" paragraph, PKG-02 ScopeDescription = row L280 description; `_REFERENCES.md` Authoritative Source Corpus table byte-identical to `origin/main`, new "SCA-APP-010 Gate-5 Authority" section with REF-010..013 (or the carrier's next four numbers) and WI/DEP ids equal to `FUTURE_WRITE_SET.csv` targets for that folder.
5. **Truthful attribution — PASS.** See Findings paragraph; F6 recorded as an observation.
6. **Ruling record consistency — PASS (F5 minor).**
7. **Root notice — PASS.**
8. **Selectability — PASS.** Exactly three `` (`SELECTABLE`) `` heads in the tree (DEL-02-02-V3-03, DEL-07-01-V3-01, DEL-07-03-V3-01); every other gate is "`<item> landed`", "`<item> selected`", or the Root DEL-02-10 routed acceptance; no gate names a question (`grep -E 'NOT_SELECTABLE_UNTIL: .*\bQ[0-9]'` empty).
9. **Whitespace and encoding — PASS.** `git diff --check` exit 0; Python scan of 1,495 added lines: 0 CR, 0 trailing whitespace; run packet, notice, and ruling record: 0 CR, 0 trailing whitespace; diff is valid UTF-8. (An earlier `grep $'\r'` count of 1571 was a BSD-grep pattern artefact, disproven byte-wise.)
10. **MAPPING §C/§D disclosures — PASS (F4 minor).** DEL-02-04-V3-01 and DEL-02-05-V3-05 name DEL-02-03-V3-01 in Depends; DEL-02-01-V3-02 names DEL-02-04-V3-01; DEL-02-02-V3-04 names DEL-02-03-V3-01; DEL-02-05-V3-05 "ships no notice"; DEL-04-04 names `persona-manager.ts` with the row label; DEL-02-01-V3-04 keeps the `icon.svg` convention; matrix basis cells in DEL-02-01/02-02/02-04 name SCA-APP-010 and the SCA-APP-004 heading reads "Controlling until SCA-APP-010"; outside carriers received `_STATUS`/`MEMORY` only; TM-001 vacuous (REGISTER.csv: 1 row names DEL-02-02 by id only, 0 by either label); `Dependencies.csv`/`_DEPENDENCIES.md` untouched; §D.11 placement rule mis-detects equal dates (F4).

## Commands run (all from the worktree root; read-only)

```
git branch --show-current; git rev-parse HEAD origin/main
git diff -U3 -- . ':(exclude)…/APP_SCA_APP_010_SEATING_2026-09-04' | shasum -a 256
shasum -a 256 …/Evidence/frozen_diff.patch
git status --porcelain; git status --porcelain --untracked-files=all; git diff --stat -- . ':(exclude)…'
git diff -- <each carrier _STATUS.md MEMORY.md ScopeOfWork.md _CONTEXT.md _REFERENCES.md>; git diff -- …/_DECISIONS/_REGISTER.md
git diff --check -- . ':(exclude)…'; git diff -U0 … | python3 (CR / trailing-whitespace / UTF-8 scan)
git diff -U0 -- 'projects/…/PKG-*/1_Working/*/_STATUS.md' | grep -E '^[-+]\*\*(Current State|Checking Approval SHA|…)'
git show origin/main:<each touched _STATUS.md, _REFERENCES.md, DRAFT_NOTICE_TO_ROOT.md>
shasum -a 256 <decomposition, companion register, _LATEST.md, 04_IMPLEMENTATION_PLAN.md, 03_TARGET_SPEC.md, 05_LOGO_AND_BRAND.md, DRAFT_NOTICE_TO_ROOT.md, NOTICE_…>
git log -1 --format='%H %s' origin/main -- <decomposition>; git log -1 7795b0972…; git log -1 311a2f0b8…; git log -1 dbd812a5…
sed -n '<row lines>p' <decomposition>  (L171,172,174,176,177,178,180,251-254,280,300,307-311,318,329,337,339,348,357,359,368,370,371,381,602,634)
python3 tools/scope_of_work/validate_scope_of_work.py <each of the 13 carrier dirs>
python3 <scratchpad verify.py>  (item form, gates vs seeded_items.json, Trace rows, ID collisions vs origin/main, front matter, verbatim row quotes, WI/DEP ids vs FUTURE_WRITE_SET.csv, corpus table parity, REF numbering, _CONTEXT prose, PKG-02 scope)
python3 (pre_images.json vs origin/main; post_images.json vs live tree; set difference)
grep -rn '(`SELECTABLE`)' …/_STATUS.md; grep -rhoE 'NOT_SELECTABLE_UNTIL: …' | grep -E '\bQ[0-9]'
grep -c 'DEL-02-02' …/_TaskManagement/REGISTER.csv; grep -c '<old label>\|<new label>' …
cat ORCHESTRATION_PLAN.md MAPPING.md seeded_items.json Evidence/app_hold/DEL-02-02.json Evidence/validation/*.txt; sed -n / grep -n over build_seating.py
awk/grep over Propagation_Plan.md §6, DOWNSTREAM_HANDOFFS.csv, OWNER_ACTION_MATRIX.csv rows 17/18/21/22, FUTURE_WRITE_SET.csv (WI/DEP/N/TM rows), Decision_Log.md (G1-CONFIRM, G2-CONFIRM), LOOP_INIT.md Step 1 and §6, 04_IMPLEMENTATION_PLAN.md §6–§8
```

## Attribution

Prepared by a bounded, read-only Claude Code subagent (Claude Fable 5.1, `claude-fable-5-1`) acting as an independent reviewer dispatched by HELP_HUMAN under a sealed brief; Agent 2 ephemeral-generalist form; role not mechanically enforced. This file is the reviewer's only write. The verdicts and findings are the reviewer's own reading of the frozen diff against the cited sources; the owner may amend by reply.

## Second pass (2026-09-05)

**Scope:** re-verification of the repaired tranche on branch `claude/sca-app-010-seating` at basis `787a551e70d9fb33f6f9a9fe228443d890a8d02d` (= `origin/main`), uncommitted working tree, after the applicator's repairs to F1–F5. Read-only except this section. The first-pass text above is unchanged.

**Frozen diff hash, recomputed live:**

```
git diff -U0 -- . ':(exclude)projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04' | shasum -a 256
66c0163c5b2f531674d130d5b9a2c4390d41046411e3f4679e06302f88e887b2
```

Equals `Evidence/frozen_diff.patch` (SHA-256 `66c0163c5b2f531674d130d5b9a2c4390d41046411e3f4679e06302f88e887b2`; 76 `diff --git` headers, 145 hunks, every hunk zero-context). The live tree is the re-frozen diff. Check 1: PASS.

### Verdict (second pass)

**PASS** — BLOCKER 0 · MAJOR 0 · MINOR 1 (new, N1, run-packet wording only). F1 and F2 (the two first-pass MAJORs) and F3, F4, F5 are resolved on the live bytes; F6 required no action. No first-pass PASS surface regressed.

### Per-finding resolution

| # | First-pass severity | Status | Evidence (live files) |
|---|---|---|---|
| F1 | MAJOR | **RESOLVED** | `…/DEL-03-02_Thin_TurnEngine_and_Session_Locking/_STATUS.md` L9 `## Remaining`, L10 blank, L11 `- **DEL-03-02-V3-01** (…)`; `None.` absent. Across all seventeen `_STATUS.md` diffs the only removed non-header line is `-None.` (the other 17 removals are `**Last Updated:**` values). Disclosed in `MAPPING.md` §D.13 L67. |
| F2 | MAJOR | **RESOLVED** | `DEL-01-03/MEMORY.md` L15, `DEL-02-03/MEMORY.md` L10, `DEL-05-04/MEMORY.md` L39, `DEL-09-04/MEMORY.md` L89 now read "…the applied decomposition row L300/L309/L339/L381 (unchanged by SCA-APP-010) states the responsibility; this carrier was seated only and not aligned in this pass, so `ScopeOfWork.md` keeps its earlier pin and carries no SCA-APP-010 section…"; `grep -c 'SCA-APP-010 Gate-5 Current Contract'` = 0 in each sibling `ScopeOfWork.md`, so the sentence is now true. Disclosed in `MAPPING.md` §D.14 L68. |
| F3 | MINOR | **RESOLVED** | DEL-02-04 `ScopeOfWork.md` L107–108: "Ruled questions applied here: none (Q3 and Q14 are applied by sibling carriers)"; `MAPPING.md` §A L17 = none. DEL-05-02 `_STATUS.md` L22 Plan: "Q13 ruled 2026-09-04 (proposals are additive harness event types in the session record)"; §A L21 = Q13. DEL-06-03 `_STATUS.md` L13 Plan: "Q11 and Q12 ruled 2026-09-04 (…); Q13 ruled 2026-09-04 (`proposal.offered` is an additive harness event type)"; §A L22 = Q11, Q12, Q13; SOW L57–58 = Q11, Q12, Q13. DEL-08-01 `_STATUS.md` L13 Plan: "Q14 ruled 2026-09-04 (G2-CONFIRM: the organisation layer the packaging checks verify)"; §A L25 = Q14; SOW L54–55 = Q14. DEL-09-04 `_STATUS.md` L113 Plan: "Q5 ruled D-APP-108 (icon only; no pop-out window)"; §A L31 = Q5. §E L73 states the equality rule. Full consistency result below. |
| F4 | MINOR | **RESOLVED** | The eight lines are at the end of their oldest-first sections: DEL-02-03 L40, DEL-04-04 L32, DEL-05-02 L44, DEL-05-04 L89, DEL-07-01 L32, DEL-07-03 L33, DEL-08-01 L30, DEL-01-03 L28 (each is the last dated bullet of `## History`). Builder `build_seating.py` L733–737 now decides from the first and last dated bullets (`newest_first = len(dates) >= 2 and dates[0] > dates[-1]`), appending otherwise; `MAPPING.md` §D.11 L65 discloses the rule and the earlier mis-placement. Seventeen-carrier table below. |
| F5 | MINOR | **RESOLVED** (with observation O2) | Ruling record `D-APP-108_…_2026-09-04.md` L50 now reproduces the re-asked question texts: Q4a "how do PDF, DOCX, XLSX, and PPTX open from the file tree?" and Q4b "what size cap applies to text, markdown, code, and CSV shown inside the panel? PDF and Quick Look previews are uncapped either way." The "Ruling as applied" clause "PDF and Quick Look previews uncapped" is therefore sourced to the premise of the presented Q4b question under which the owner selected the 10 MB option, not to the option text; the Attribution section (L84–90) still labels the column as the agent's reading. The two carrier lines (DEL-02-03 `_STATUS.md` L13 Plan and its Return) are unchanged and consistent with L50. |
| F6 | observation | **NO ACTION REQUIRED** (unchanged) | `ORCHESTRATION_PLAN.md` L6 and the ruling record Attribution L84–90 still disclose HELP_HUMAN acting as WORKING_ITEMS' applicator, role not mechanically enforced. |

### Seventeen-carrier history placement (check 2, F4)

Order on `origin/main` was read from the first and last dated bullets of each `## History` section (`git show origin/main:<path>`); live placement from the live file. Rule under test (`MAPPING.md` §D.11): insert at top only where the section is newest-first, else append at the end.

| Carrier | `origin/main` order (first … last dated bullet) | 2026-09-04 line, live | Placement | Correct |
|---|---|---|---|---|
| DEL-01-03 | oldest-first (2026-05-20 … 2026-07-19) | `_STATUS.md` L28 | end of section (first L12 = 05-20, last L28 = 09-04) | yes (F4 repaired) |
| DEL-02-01 | newest-first (2026-08-15 … 2026-07-12) | L61 | top (first L61 = 09-04, last L80 = 07-12) | yes |
| DEL-02-02 | newest-first (2026-09-03 … 2026-07-19) | L60 | top (last L100 = 07-19) | yes |
| DEL-02-03 | oldest-first (2026-05-20 … 2026-07-12) | L40 | end (first L29 = 05-20) | yes (F4 repaired) |
| DEL-02-04 | newest-first (2026-07-24 … 2026-07-12) | L37 | top (last L52 = 07-12) | yes |
| DEL-02-05 | newest-first (2026-09-03 … 2026-07-12) | L31 | top (last L52 = 07-12) | yes |
| DEL-03-02 | newest-first (2026-09-03 … 2026-07-12) | L21 | top (last L36 = 07-12) | yes |
| DEL-04-04 | oldest-first (2026-05-20 … 2026-07-12) | L32 | end (first L21 = 05-20) | yes (F4 repaired) |
| DEL-05-02 | oldest-first (2026-05-20 … 2026-09-03) | L44 | end (first L30 = 05-20; follows the A12 line) | yes (F4 repaired) |
| DEL-05-04 | oldest-first (2026-05-20 … 2026-09-03) | L89 | end (first L34 = 05-20; follows the A12 line) | yes (F4 repaired) |
| DEL-06-03 | newest-first (2026-07-22 … 2026-07-19) | L21 | top (last L35 = 07-19) | yes |
| DEL-07-01 | oldest-first (2026-05-20 … 2026-07-12) | L32 | end (first L21 = 05-20) | yes (F4 repaired) |
| DEL-07-03 | oldest-first (2026-05-20 … 2026-07-12) | L33 | end (first L21 = 05-20) | yes (F4 repaired) |
| DEL-08-01 | oldest-first (2026-05-20 … 2026-07-12) | L30 | end (first L21 = 05-20) | yes (F4 repaired) |
| DEL-08-03 | oldest-first by the rule (first 2026-07-12 … last 2026-07-24; the second bullet is 2026-05-20, so the section is not strictly monotone) | L34 | end (first L12 = 07-12, last L34 = 09-04) | yes |
| DEL-08-04 | newest-first (2026-09-03 … 2026-07-19) | L33 | top (last L75 = 07-19) | yes |
| DEL-09-04 | newest-first (2026-09-03 … 2026-07-12) | L121 | top (last L312 = 07-12) | yes |

Nine appended, eight inserted at top; every placement follows the disclosed rule. Note for the owner: DEL-08-03's section was already non-monotone on `main`; the rule appends there, which matches its A12 precedent.

### F3 consistency result (check 3, all 20 items and 13 paragraphs)

Test: the set of questions named in each item's `Plan:` line (regex over `Q\d+[ab]?` and `Qm to Qn` ranges) equals `MAPPING.md` §A "Rulings cited" for that item.

| Item | Plan line | Plan Q set | §A "Rulings cited" | Equal |
|---|---|---|---|---|
| DEL-02-01-V3-01 | `_STATUS.md` L29 | Q9 | Q9 (L13) | yes |
| DEL-02-01-V3-02 | L37 | Q1, Q6 | Q1, Q6 (L14) | yes |
| DEL-02-01-V3-03 | L45 | none | none (L15) | yes |
| DEL-02-01-V3-04 | L53 | Q5 | Q5 (L16) | yes |
| DEL-02-02-V3-03 | L44 | Q3 | Q3 (L11) | yes |
| DEL-02-02-V3-04 | L52 | Q10 to Q14, Q15, Q16 | Q10 to Q16 (L12) | yes |
| DEL-02-04-V3-01 | L29 | none | none (L17) | yes |
| DEL-02-05-V3-05 | L23 | Q7, Q8 | Q7, Q8 (L18) | yes |
| DEL-03-02-V3-01 | L13 | none | none (L19) | yes |
| DEL-04-04-V3-01 | L13 | Q14 | Q14 (L20) | yes |
| DEL-05-02-V3-02 | L22 | Q13 | Q13 (L21) | yes |
| DEL-06-03-V3-01 | L13 | Q11, Q12, Q13 | Q11, Q12, Q13 (L22) | yes |
| DEL-07-01-V3-01 | L13 | Q14 | Q14 (L23) | yes |
| DEL-07-03-V3-01 | L13 | Q10, Q16 | Q10, Q16 (L24) | yes |
| DEL-08-01-V3-01 | L13 | Q14 | Q14 (L25) | yes |
| DEL-08-04-V3-02 | L25 | none | none (L27) | yes |
| DEL-02-03-V3-01 | L13 | Q4a, Q4b | Q4a, Q4b (L28) | yes |
| DEL-02-03-V3-02 | L21 | Q2 | Q2 (L29) | yes |
| DEL-05-04-V3-02 | L26 | none | none (L30) | yes |
| DEL-09-04-V3-02 | L113 | Q5 | Q5 (L31) | yes |

20 of 20 equal. Existing items (DEL-02-02-V3-01/02, DEL-02-05-V3-03, DEL-05-02-V3-01, DEL-05-04-V3-01, DEL-08-04-V3-01, DEL-09-04-V3-01) cite no question and are untouched.

Thirteen "Seating and rulings" paragraphs versus the union of item citations and Gate-5 obligation citations in the same file: DEL-02-01 L113–115 names Q1, Q3, Q5, Q6, Q9 = items {Q1, Q5, Q6, Q9} ∪ contract obligation 5 at L108 "(Q3)"; DEL-02-02 L118–119 Q3, Q10 to Q14, Q15, Q16 = items, with obligations L109/L111 citing Q3, Q15, Q16; DEL-02-04 L107–108 none (see O1); DEL-02-05 L79–80 Q7, Q8 = item and obligations L72/L74; DEL-03-02 L52–53 none beyond SR-24; DEL-04-04 L54–55 Q14 = item and obligation; DEL-05-02 L52–53 Q13 = item; DEL-06-03 L57–58 Q11, Q12, Q13 = item; DEL-07-01 L56–57 Q14 = item; DEL-07-03 L52–53 Q10, Q16 = item and obligation; DEL-08-01 L54–55 Q14 = item; DEL-08-03 L53–54 SOW-007 (G2-CONFIRM), no Q, no item; DEL-08-04 L65–66 none beyond SR-24. No paragraph names a question that its items or obligations do not apply. Check 3: PASS.

### Regression sweep (check 4)

| Check | Result |
|---|---|
| `git status --porcelain` write set | 76 tracked changes: 17 × `_STATUS.md` + 17 × `MEMORY.md` + 13 × (`ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`) + ruling record (intent-to-add) + `_REGISTER.md` (M) + root `NOTICE_2026-09-04_APP_SCA-APP-010_SHELL_REDESIGN_ROOT_DEPENDENCIES.md` (intent-to-add); untracked = the run folder only (37 files). Same set as the first pass. PASS |
| Forbidden lifecycle fields | `git diff -U0` over the seventeen `_STATUS.md`: no `-`/`+` line for `Current State`, `Checking Approval SHA`, `Authorization Basis`, `Directive`, `P06 Record`; removed lines = 17 × `**Last Updated:**` + `None.`; no removed line in any `MEMORY.md`. PASS |
| `git diff --check` (excluding the run folder) | exit 0. PASS |
| `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main` | `PASS: candidate whitespace is clean`. PASS |
| `python3 tools/scope_of_work/validate_scope_of_work.py <dir>` × 13 | PASS, `format=SOW_V1`, for DEL-02-01, 02-02, 02-04, 02-05, 03-02, 04-04, 05-02, 06-03, 07-01, 07-03, 08-01, 08-03, 08-04. PASS |
| `build_seating.py --check` | `post-images verified for 73 files` (the function at L837–842 fails on any target whose live SHA-256 differs from `Evidence/post_images.json`). PASS |
| `Evidence/pre_images.json` vs `origin/main` | 74 entries, 0 mismatches (re-run of the first-pass script). PASS |
| Selectability | exactly three `` (`SELECTABLE`) `` heads (DEL-02-02-V3-03 L42, DEL-07-01-V3-01 L11, DEL-07-03-V3-01 L11); no `NOT_SELECTABLE_UNTIL` clause names a question. PASS |
| Root notice identity | live SHA-256 `299a3b138825b31218ad40e1c90aa61a702bc7462bc3fce09958f718ff34ec49`; cited draft `DRAFT_NOTICE_TO_ROOT.md` SHA-256 `f197b31e80ec71e46858bc84bb5d00941c01882e66e16c18115bffc14eaa5c5d` recomputed on the live tree and on `origin/main`, matches the notice's own citation (L6). File mtime 23:41:34, before the first-pass report was written (23:57:19); `_REGISTER.md` mtime 23:41:34 likewise. Neither was rewritten by the repair. PASS |

### Spot-check of first-pass PASS surfaces (check 5)

Limitation: the first-pass frozen patch (`-U3`, `a4cfc7f0…`) was overwritten by the re-freeze, so a byte diff between passes is not possible; the comparison below is against the first-pass notes above and their cited line numbers, which still resolve to the same content.

- **DEL-02-02** (`_STATUS.md` L42 V3-03 `SELECTABLE`; L50 V3-04 gate `DEL-02-02-V3-03 landed; DEL-07-03-V3-01 landed` = `seeded_items.json`; L44 Q3, L52 Q10–Q14/Q15/Q16 consistent with the ruling record L60–61 and Q15/Q16 rows; V3-01 L25 and V3-02 L33 untouched, no removed line in the file except `Last Updated`). `ScopeOfWork.md` front matter `@dbd812a5…`, refs `[SOW-006, SOW-081, SOW-082]` / `[OBJ-001, OBJ-007]`; Gate-5 section L69–125 with obligations L109–114; OUT-001 L16 renamed with the earlier label retained as dated history; matrix row L505 names the SCA-APP-010 section. `_CONTEXT.md` L13 `DeliverableName | Right-Panel Coordination, Workflows, and Proposal UX`. `_REFERENCES.md` REF-010..013 and the display-name note. History line at top of a newest-first section (L60). Matches the first-pass row; no change beyond the reported repairs (none reported for this carrier). PASS.
- **DEL-02-05** (`_STATUS.md` L21 V3-05 gate `DEL-02-01-V3-01 landed` = seeded; L23 Q7/Q8 consistent with the ruling record and the routed notice path; Depends L24 names DEL-02-03-V3-01 for the Settings view; V3-03 L11 untouched). `ScopeOfWork.md` refs `[SOW-013, SOW-019, SOW-023]` / `[OBJ-001, OBJ-008]`; Gate-5 section L25–85 with obligations L71–75 (Q7 at L72, Q8 at L74); OUT-002 L17, AC-002 L295, VER-002 L407 exist. `_REFERENCES.md` REF-008..011 (this carrier's next four numbers) with WI-016..020. `_CONTEXT.md` scope = row L311 description + "Applied decomposition row L311 … notes" paragraph. History line at top of a newest-first section (L31). Matches the first-pass row. PASS.
- **Root notice**: content re-read in full (105 lines); the three dependencies with seated ids (DEL-02-05-V3-05 L56–57, DEL-05-02-V3-02 L65, DEL-03-02-V3-01 and DEL-08-04-V3-02 L71–73), the applied identities (L34–43), the Q8 quotation (L11–19), the G1-CONFIRM grant (L20–22), and the "not Root authority" clauses (L83–91, L93–97) are as the first pass recorded; file untouched since 23:41:34. PASS.
- **Line-number anchors from the first pass** still resolve: F2 MEMORY lines at L10/L39/L89/L15; F3 SOW lines at DEL-02-04 L107–108, DEL-08-01 L54–55, DEL-06-03 L57–58; DEL-05-02 `_STATUS.md` L22 and DEL-09-04 L113 are still the V3-02 Plan lines; ruling record Q4 row still L50; the DEL-03-02 item moved from L12 to L11 by exactly the one removed line. No unreported shift observed.

### New findings

| # | Severity | File | Line | Defect | Suggested fix |
|---|---|---|---|---|---|
| N1 | MINOR | run `VALIDATION_EVIDENCE.md` L16 and L41–42; run `MAPPING.md` §D.15 L69 | as listed | Both say "the same reviewer re-verified the re-frozen diff" (VALIDATION_EVIDENCE.md also "The final tree is the fourth apply; the same reviewer re-verified"). This second pass was performed by a fresh bounded subagent instance under a new sealed brief, not by the first-pass instance; the two share model and role only. The sentences were also written (file mtimes 23:59 / 00:01) before this pass returned, so they record a re-verification as completed ahead of its result. Neither file is in the frozen diff; no carrier, gate, or authority surface is affected. | Reword to "a second independent review pass (fresh bounded subagent, same model and role) re-verified the re-frozen diff; see `REVIEW.md` § Second pass" and, in VALIDATION_EVIDENCE.md, state the verdict and counts recorded here rather than asserting them in advance. |

Observations (no severity):

- **O1** — DEL-02-04 `ScopeOfWork.md` L108 reads "none (Q3 and Q14 are applied by sibling carriers)". The parenthetical names two questions only to disclaim them; a plain-text search for `Q14` will hit this carrier. Truthful and unambiguous; recorded so the owner's byte review can decide whether the disclaimer is worth keeping.
- **O2** — The F5 repair sources "uncapped" to the presented Q4b question text. That text is the applicator's transcription of the chat; the plan's own Q4 row (`plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` L150: "Is a 2MB in-app file cap acceptable, and should PDFs open in-app or hand off?") predates the re-ask and does not contain the clause, and the chat is not in the repo, so this reviewer cannot independently verify the wording. The record's Attribution section labels the column as the agent's reading, which is the right posture; the owner confirms or amends at byte review.
- **O3** — `VALIDATION_EVIDENCE.md` L43 refers to `HANDOFF_STATE.md`, which does not yet exist in the run folder (N4 not yet run at the time of this pass). Forward reference only.

### Per-carrier verdicts (second pass)

Rule unchanged: PASS = no BLOCKER or MAJOR finding in that carrier's touched files.

| Carrier / surface | First pass | Second pass | Note |
|---|---|---|---|
| DEL-02-01 (13) | PASS | PASS | unchanged content; history at top of a newest-first section (L61); paragraph Q3 sourced from obligation L108 |
| DEL-02-02 (13) | PASS | PASS | spot-checked above; no change |
| DEL-02-04 (13) | PASS | PASS | F3 repaired (SOW L107–108 = none); O1 |
| DEL-02-05 (13) | PASS | PASS | spot-checked above; no change |
| DEL-03-02 (13) | FAIL | **PASS** | F1 repaired (`None.` removed; item at L11) |
| DEL-04-04 (13) | PASS | PASS | F4 repaired (L32, end of section) |
| DEL-05-02 (13) | PASS | PASS | F3 (Q13 at L22) and F4 (L44) repaired |
| DEL-06-03 (13) | PASS | PASS | F3 repaired (Plan L13 Q11, Q12, Q13 = §A L22 = SOW L57–58) |
| DEL-07-01 (13) | PASS | PASS | F4 repaired (L32) |
| DEL-07-03 (13) | PASS | PASS | F4 repaired (L33) |
| DEL-08-01 (13) | PASS | PASS | F3 (Plan L13 Q14 = §A L25 = SOW L54–55) and F4 (L30) repaired |
| DEL-08-03 (13, record-only) | PASS | PASS | unchanged; history appended at L34 per rule |
| DEL-08-04 (13) | PASS | PASS | unchanged; history at top of a newest-first section (L33) |
| DEL-02-03 (outside) | FAIL | **PASS** | F2 repaired (MEMORY L10); F4 repaired (L40); F5 resolved at the ruling record |
| DEL-05-04 (outside) | FAIL | **PASS** | F2 repaired (MEMORY L39); F4 repaired (L89) |
| DEL-09-04 (outside) | FAIL | **PASS** | F2 repaired (MEMORY L89); F3 repaired (Plan L113 Q5) |
| DEL-01-03 (outside, record-only) | FAIL | **PASS** | F2 repaired (MEMORY L15); F4 repaired (L28) |
| Ruling record D-APP-108 | PASS | PASS | F5 resolved (L50 reproduces the Q4a/Q4b question texts); O2 |
| Register `_REGISTER.md` | PASS | PASS | untouched since 23:41:34; one added row L123 |
| Root notice (repo root) | PASS | PASS | untouched since 23:41:34; identities re-verified |
| Run packet | PASS | PASS | `frozen_diff.patch` = live tree; `post_images.json` = live tree (73); `pre_images.json` = `origin/main` (74); `seeded_items.json` = live gates; MAPPING §A/§D/§E consistent with every item. MINOR N1 (wording in `VALIDATION_EVIDENCE.md` and MAPPING §D.15). |

### Commands run (all from the worktree root; read-only)

```
git rev-parse --abbrev-ref HEAD; git rev-parse HEAD origin/main
git diff -U0 -- . ':(exclude)…/APP_SCA_APP_010_SEATING_2026-09-04' | shasum -a 256
shasum -a 256 …/Evidence/frozen_diff.patch; grep -c '^diff --git' …/frozen_diff.patch; grep -E '^@@' … (hunk form)
git status --porcelain; git status --porcelain --untracked-files=all
git diff --check -- . ':(exclude)…'
python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main
python3 …/APP_SCA_APP_010_SEATING_2026-09-04/build_seating.py --check
python3 tools/scope_of_work/validate_scope_of_work.py <each of the 13 carrier dirs>
git diff -U0 -- 'projects/…/PKG-*/1_Working/*/_STATUS.md' | grep -E '^[-+]\*\*(Current State|Checking Approval SHA|Authorization Basis|Directive|P06 Record)'
git diff -U0 -- '…/_STATUS.md' | grep -E '^-[^-]'; git diff -U0 -- '…/MEMORY.md' | grep -E '^-[^-]'
git diff -U0 -- …/_DECISIONS/_REGISTER.md; git diff -U0 -- <DEL-02-02, DEL-02-05 _REFERENCES.md _CONTEXT.md>; git diff --stat -- <those dirs>
awk over every touched _STATUS.md (## Remaining and ## History with line numbers); python3 (first/last dated bullet, position of the 2026-09-04 line)
git show origin/main:<each touched _STATUS.md> | awk (first/second/last dated History bullets → order)
awk/grep over the 13 ScopeOfWork.md (### Seating and rulings paragraphs; Q mentions inside the SCA-APP-010 Gate-5 section)
grep -n over the 17 _STATUS.md (item heads and Plan lines) | python3 (Q-set extraction and comparison with MAPPING §A)
grep -n '2026-09-04' <4 outside MEMORY.md>; grep -c 'SCA-APP-010 Gate-5 Current Contract' <4 sibling ScopeOfWork.md>
sed -n / grep -n over the ruling record (L40–60 Q4 row, L60–72, Attribution); git diff -U0 | grep -i uncapped
cat -n MAPPING.md VALIDATION_EVIDENCE.md; cat seeded_items.json; sed -n '1,25p' ORCHESTRATION_PLAN.md; ls -la Evidence/ Evidence/validation/
grep -n / awk over build_seating.py (--check function L837–842; history placement L728–737)
shasum -a 256 <Root notice> <DRAFT_NOTICE_TO_ROOT.md>; git show origin/main:<DRAFT_NOTICE_TO_ROOT.md> | shasum -a 256; sed -n over the notice; grep -n identities
grep -n -i 'uncapped|Q4' projects/chirality-app-dev/plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md
stat -f '%Sm %N' <notice, ruling record, register, DEL-02-02/DEL-02-05 files, DEL-03-02 _STATUS.md, REVIEW.md, pre_images.json>
grep -rn '(`SELECTABLE`)' …/_STATUS.md; grep -rhoE 'NOT_SELECTABLE_UNTIL: …' | grep -E '\bQ[0-9]'
python3 (pre_images.json entries vs `git show origin/main:<path>` SHA-256)
```

### Attribution (second pass)

Prepared by a bounded, read-only Claude Code subagent (Claude Fable 5.1, `claude-fable-5-1`) acting as independent reviewer, second pass, dispatched by HELP_HUMAN under a sealed brief; Agent 2 ephemeral-generalist form; a fresh instance distinct from the first-pass instance; role not mechanically enforced. This appended section is the reviewer's only write; the first-pass text above was not edited. The verdicts and findings are the reviewer's own reading of the re-frozen diff against the cited sources; the owner may amend by reply.
