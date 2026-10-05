# FR-PEC: independent review of PR #1095

**Reviewer.** FR, a Type 2 TASK (Claude Code subagent, Claude Opus 5.5) dispatched by HELP_HUMAN (ROOT) under `RUN3/BRIEF_FR.md` for run `ROOT-AUM-PEC-AND-FOLLOWUPS-20261005`. I wrote none of the reviewed text. I made no Git writes.

**Candidate.** PR #1095, branch `codex/root-aum-pec-and-followups-20261005`, head `bd9bbc8536e38bd39488845c062b868d9a94fc63`. Its single parent is main `7ba1181d43d063a0b11365697412df9bdbe2b2e6`, the stated basis. `gh` shows the PR open, a draft, MERGEABLE, 20 files, with every hosted check passed or skipped by coverage selection.

**Placeholders.** `WT` is the T3 worktree root. The PR checkout is `WT/pec-pr`. `RUN3` is `WT/pec-pr/execution/_Coordination/AgentRuns/ROOT-AUM-PEC-AND-FOLLOWUPS-20261005`. My logs and scratch outputs are in `WT/scratch/fr_pec_01/`. Other paths are repository-relative.

## Verdict: REPAIR

| Severity | Count |
|---|---:|
| BLOCKING | 0 |
| MAJOR | 1 |
| MINOR | 2 |
| NOTE | 4 |

The main deliverables are sound:
- The AUM's PEC statements are true of PEC at `7ba1181d43`.
- The §9 and §13 extensions are true.
- The v8 Markdown, Word and PDF changes are confined to the three sentences.
- The App v4 ruling is sound.

The one MAJOR finding is that the public export was not regenerated at the final tree, although the run records say it was. The two MINOR findings are omissions in follow-on records.

## Findings

### MAJOR-1: the export was not regenerated at the final tree

**Evidence.**
- I ran `tools/validation/test_public_export_profile.py` with pytest's base temp under `WT/scratch/fr_pec_01/pytest_export/`. It passed: 5 passed. Its `test_public_export_excludes_private_runtime_surfaces` builds a fresh stage with the exporter's own `build_stage`.
- I then listed that stage the way `write_manifest` does (sorted, path, size, sha256). It has 1,879 rows. The committed `exports/chirality-app/export-manifest.csv` has 1,878.
- The one difference is a missing row for this PR's own tranche manifest, `docs/governance_harness/tranche_manifests/ROOT-AUM-PEC-AND-FOLLOWUPS-20261005.yaml` (2,955 bytes, sha256 `f1587567ce28cdfc63a957609dc21f14b6c2e079c7a2e2489b72923c4fc2021e`). The exporter copies `docs/` recursively, and only `docs/governance_harness/briefs/` is excluded. Every other row matches byte for byte.
- `exports/chirality-app/export-report.md` is unchanged from main. It still says "Manifest rows: 1878" and `docs` 341. At the head, the true values are 1,879 and 342.
- The default staging path, `exports/chirality-app/staging`, is correct.
- The cause is the same one seen on main. Main's export row for #1094's manifest, `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005.yaml`, recorded 3,060 bytes, but the file on main is 3,282 bytes. That export was also generated before its manifest's last edit. This PR corrects that row (to 3,282 / `83c5fca1…`) but repeats the pattern for its own manifest.
- `RUN3/RULINGS.md` §4 says the export is "regenerated at the final tree" and that "Only `export-manifest.csv` changes". Neither is true at `bd9bbc8536`.
- `RUN3/RULINGS.md` also lists the regenerated export among the gates (§4).

**Fix.**
1. Finish every other edit first, including any edit to the tranche manifest. The manifest is itself an exported file, so any later edit to it makes the export stale again. Review files under `execution/` are not exported.
2. Add `exports/chirality-app/export-report.md` to the manifest's `instruction_surface_paths`, or to its `scope_limits` wording. The current scope says "the paths above … only", and the report will change.
3. Re-run `exports/chirality-app/export_public.py` from the final tree with the default stage. Commit both `export-manifest.csv` (1,879 rows) and `export-report.md` (1,879 rows; `docs` 342), with the staging path still `exports/chirality-app/staging`.
4. Correct RULINGS §4. Say that the regeneration also fixes main's stale row for `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005.yaml`.

### MINOR-1: the follow-up notice omits that this tranche changes two pinned files again

**Evidence.**
- `projects/chirality-app-v4/execution/_Coordination/NOTICE_2026-10-05_ROOT_LOOP_INIT_PINS_FOLLOW_UP.md` explains why #1094's changes need no re-pinning ("#1094 changed only the README's render-basis lines").
- It does not say that this tranche changes the same two pinned manual files again:
  - the AUM Markdown, whose PEC statements change and whose headings do not;
  - `docs/alignment-manual/README.md`, whose AUM render-basis line changes.
- As a result, the `SOURCE_MAP.json` entries `user_manual` and `manual_index`, and the AUM and README entries in `policy_standing/basis.json`, now trail by two revisions, not the one the #1094 notice stated. A receiving loop reading only the notices would not learn this.
- The recommendation itself still holds. I confirmed that the AUM's level 1–3 headings are identical between the pinned revision (`1cb9fd536e`, sha256 `08ca0e40…`) and the head. The README's "Current editions" table is unchanged by this PR.

**Fix.** Add one sentence to the notice: "This tranche also changes the Agent User Manual (PEC statements and the §§9, 13 loop lists; headings unchanged) and the README's render-basis line, so those pins now trail by two revisions; the same reasoning applies."

### MINOR-2: the README's v8 revision pointer is now incomplete

**Evidence.**
- `docs/alignment-manual/README.md`, "Maintain the management-manual formats", says "The v8 text revisions are recorded in the App v4 manual change summary".
- v8 now has a further text revision, the three LOOP_INIT sentences. Its record is `plans/evidence/2026-10-05_manual_v8_loopinit/production-note.md`, which the README does not point to.
- The v8 Markdown has no in-text revision log.

**Fix.** Append a pointer to the 2026-10-05 production note. This changes the README again, so do it before the MAJOR-1 regeneration.

**ROOT may decline.** ROOT may judge this outside the authorized correction. It is provenance navigation, not a false statement about content.

### NOTE-1: two precision nits in the PEC edits (no change required)

- **E7, line 331.** The AUM says "PEC blocks work only on an active `PREREQUISITE` row whose status is unsatisfied and whose target the work needs." PEC's rule (`projects/pec/AGENTS.md`, "Selection and decisions") names `TBD`, `PENDING` and `IN_PROGRESS`, and says `WAIVED` and `NOT_APPLICABLE` never block. AUM line 329 calls those "another permitted disposition", so "unsatisfied" is defensible. Naming the three statuses would be exact.
- **E9, line 646.** The AUM says "an unmerged branch's claim is a different condition". PEC says reliance is "never on an unmerged branch's claim of it". The AUM wording is true but softer.

### NOTE-2: the description of `a16/basis.json` is loose; the ruling is stronger than stated

- The follow-up notice and RULINGS §3 say that `policy_standing/basis.json` and `a16/basis.json` record the TASK's role, parent, mechanism, model and base `38bb2bc87a`. Only `policy_standing/basis.json` has those fields. `a16/basis.json` has only `consultation` ("Prior Root/TASK/LOOP and review context retained…") and `sources`. The A16 change record (`APP-V4-GROUP-A-20261004/changes/I3-A16-STANDING.md`) names the TASK, its parent and its model.
- **Supporting evidence the records do not cite.**
  - `policy_standing/candidate.json` and `a16/candidate.json` each pin the sha256 of their `basis.json`. Re-pinning a basis would therefore also falsify its candidate's provenance.
  - No App v4 source or test reads `SOURCE_MAP.json` or either `basis.json`. I searched `projects/chirality-app-v4/app/`.

### NOTE-3: the run records disagree on whether LibreOffice 26.8.1 was used

- `RUN3/OWNER_DECISIONS.md` says the 26.8.1 download was "used from a scratch folder, not installed system-wide".
- The production note says "Not used", and RULINGS §2 says it "was not needed for the build".
- The PDF `Producer` is `LibreOfficeDev 26.8.0.0.alpha0 (AARCH64)`, the same as v8's, which supports "not used for the build".
- **Fix (optional).** Reword OWNER_DECISIONS to say the download was kept in a scratch folder. Alternatively, state in the records what, if anything, 26.8.1 was run for.

### NOTE-4: list consistency and one addition beyond correction (ROOT's choice)

- **App v4 in the loop lists.** App v4 is now named in §9 (lines 347, 381) and §13 (line 565), but not in the parallel lists in §1 (lines 62, 74), §2 (line 104) or §18 (lines 684, 690). None of those lists claims to be exclusive, so none is false. App v4 also has its own §14 entry. The inconsistency is the one PM's Q1 anticipated.
- **E10(a).** It adds "; nor do the loop, a work graph, a Task Management outcome or a central receipt" to a sentence that was not false. The addition is true (`projects/pec/AGENTS.md`, "Write Scopes And Fences") and small. Strictly, it goes beyond correcting false statements.

## Checks by brief item

### 1. The AUM's PEC statements

- **The PEC basis.** I read `projects/pec/AGENTS.md` and `projects/pec/loop/LOOP_INIT.md` in full, plus `init/` (both files), the decision register (D-PEC-94, D-PEC-99, D-PEC-106), `loop/LOOP_RECEIPTS.md` and `software-workflow.json`. I also checked the PEC folders on disk:
  - The PR changes nothing under `projects/pec`.
  - The ledger closes at Receipt 197, dated 2026-09-25.
  - None of the 68 `PKG-*` `_STATUS.md` files has `## Remaining`.
  - The profile's six checks include `v2-parsers`.
  - The three WorkGraphs are present.
  - `taskmgmt-init-prompt.md` is now a pointer.
  - Adoption commit `11be801130` and merge `13df8b795e` are dated 2026-09-25 local time and are ancestors of the basis.
- **Each changed line is true of PEC at `7ba1181d43`.**
  - Lines 62, 74, 76, 104, 106 and 331.
  - Lines 644–667 (E8–E13). The step references hold: LOOP_INIT §§0–1, 3–6; the AGENTS sections "Write Scopes And Fences", "Selection and decisions", "Active Reliance Holds" and "Development checks and evidence"; the MEMORY grant rule; the closed ledger; and conditional Task Management.
  - Lines 682, 684 and 690.
- **No remaining false PEC statement.** I read every remaining PEC mention: lines 29, 78, 102, 146, 623, 642, 648 (rest), 650–663, and the Contents. None is false.
- **Minimal and nothing else changed.** The diff against main is 19 changed lines:
  - the 16 PM edit lines;
  - E1's revision note, extended;
  - lines 347, 381 and 565 under Q1.
  
  I re-applied PM's 26 before/after pairs, parsed from `AUM_PEC_EDITS.md` (sha256 `229241ab…`), to main's AUM. Every Before occurs exactly once, and the result is `16fb79f5e839…`, as RULINGS says. The head differs from that result only on lines 5, 347, 381 and 565.
- **The §9 and §13 extensions.** These are true:
  - `workflows/construct-local-work-graph/WORKFLOW.md` §3 reads "(currently App, App v4, Piping and PEC)".
  - App v4's LOOP_INIT adopts construct's "graph, closeout, receipt and MEMORY conventions", names `execution/_Coordination/WorkGraphs/` and selects the graph by steering. Its graphs sit at `WorkGraphs/<undertaking>/WORK_GRAPH.md`.
- **The remaining "App/Piping" mentions.** Lines 68, 549, 675, 700 and 765 are the only remaining ones. They are historical or illustrative, and true, as ruled.
- **Headings.** Levels 1–3 are identical to main's, and to App v4's pinned revision `1cb9fd536e`.
- **Links.**
  - All 415 reference uses resolve to the 102 definitions.
  - Every definition target exists.
  - Every in-page `#` link has an `<a id>` target.
  - The unused-definition set is the same as main's, so no definition lost its last use.
- **HTML.** `render_manual.py --source …v3.md --output …v3.html --basis-date 2026-10-05 --basis-revision 7ba1181d43d063a0b11365697412df9bdbe2b2e6 --check` gives exit 0, "Verified", source `2535efe5…` and HTML `a9ea63f3…`. The Field Book's `--check` also passes.
- **README.** The render command's basis is 2026-10-05 and `7ba1181d43…` (full SHA). The "Current editions" table is unchanged.

### 2. Consolidated v8

- **Markdown.** Exactly three sentences change, on lines 1678, 1782 and 1786. Each new sentence is true under the evergreen rule (construct §4; the App, PEC, Piping and App v4 LOOP_INITs name no undertaking's graph). No other v8 line tells LOOP_INIT to point at a graph.
- **Word.** The package has the same 28 parts in the same order. Only `word/document.xml` and `docProps/app.xml` differ; the ZIP timestamps also differ.
  - In `document.xml`, only paragraphs 846, 881 and 883 differ. Swapping main's three paragraphs back makes the documents XML-identical.
  - Their run structure and properties are unchanged, and their text equals the Markdown lines with the backticks removed.
  - No Contents folio changed. `toc-map-v8.json`'s entries are identical to v8's.
  - In `app.xml`, only the summary counts changed: Words +24 (I counted +18, +1 and +5 by hand), Characters +131 and CharactersWithSpaces +155. Pages stays 172.
- **PDF.** Both editions have 172 pages. Text differs only on physical pages 83 (folio 79) and 87 (folio 83), and only in the edited paragraphs. The one outline shift is "Recover the current undertaking" on page 83, by one line. The Producer is unchanged.
- **Content check.** I re-ran `plans/evidence/2026-10-05_manual_v8_loopinit/format-content-check-v8.py` on the head's three files, with output to `WT/scratch/fr_pec_01/content-check-fr.json`. It exited 0:
  - Word: 1,656 of 1,656 units, 266/266 headings, 15/15 tables, 31/31 specimens, 9 list items, no mismatches;
  - PDF: 0 missing units and 3 extras.
  
  Once pypdf's in-memory object ids are normalized, the output is identical to the committed `content-check-final.json`.
- **Production note.** It is accurate on the change, the scripts, the renderer, the files' hashes, the check results and the pagination. Its reproducibility run cannot be re-checked without LibreOffice, which the brief excludes. v8's own evidence folder is unchanged in the diff.
- **Evidence copies.** The `.py` scripts differ from `plans/evidence/2026-10-04_manual_v8/` only in `format-finalize-v8.py`'s `EXPECTED_MD`. `build-check.json` and `toc-map-v8.json` differ only where the new source and render require.

### 3. App v4's pins

- **The seven entries.** They are:
  - `SOURCE_MAP.json` `loop`, `manual_index` and `user_manual`;
  - `policy_standing/basis.json`, for LOOP_INIT, the README and the AUM;
  - `a16/basis.json`, for LOOP_INIT.
- **Read extents.** These are as stated: "Execution entry only; not product defaults", "Current editions" and "Headings to level three only".
- **Unchanged parts.** These are as stated:
  - #1094 changed one LOOP_INIT sentence, which no bundled instruction file contains;
  - #1094 changed only the README's render-basis lines;
  - the headings are unchanged since the pin.
- **Other entries already differ.** In `SOURCE_MAP.json`, `role_contract` differs. In the two `basis.json` files, `WORK_GRAPH.md`, `RECORD_SEMANTICS.md` and several `src`/`tests` files differ.
- **No App v4 product resource changed.** The only App v4 path in the diff is the notice.
- **The ruling is sound.** See NOTE-2 for the stronger grounds and MINOR-1 for the omission.

### 4. The manifest

- **G4.** CI mode, diff mode against `7ba1181d43` with `--tranche ROOT-AUM-PEC-AND-FOLLOWUPS-20261005`, and diff mode with `--added-manifests-only` all give PASS, exit 0, no BLOCK.
- **Authorization quotes.** Both match `RUN3/OWNER_DECISIONS.md` byte for byte, with the double spaces kept. The first quote starts at "I want you to", omitting the preceding "CI is green…" sentence.
- **Scope.** The 20 changed paths are 8 declared paths, 4 run records, the 7 v8 evidence files and the App v4 notice. That is complete, until MINOR-2's or MAJOR-1's repairs add `export-report.md`.
- **Rationale.** It is true.

### 5. The export

It fails. See MAJOR-1. The staging path is the default.

### 6. Portability

- **GEN-8.** `CHIRALITY_REQUIRE_LIVE_TESTS=1 … -m pytest -q -p no:cacheprovider tools/practitioner_harness/test_live_baseline.py -k gen8` on the head: 1 passed.
- **Entrypoint validator.** "PASS: root instruction entrypoints are canonical."
- **Added lines.** The diff's 12,987 added text lines contain no machine-absolute or home paths and no credential patterns. The changed Word and PDF files contain no such paths.

## Host and method disclosures

- **Commands I ran.**
  - GEN-8, G4 (three modes), the entrypoint validator, `test_public_export_profile.py`, the renderer's `--check` (AUM and Field Book), the v8 content check (output to scratch), and pypdf/lxml comparisons.
  - Read-only analysis scripts of my own for links, edit replay, package parts and the export stage listing.
  - `gh pr view` and `gh pr checks` (reads).
- **Python environments.**
  - The piping `.venv` Python for GEN-8, the validators and pytest.
  - `WT/scratch/tools/docvenv/bin/python` for the content check and the lxml/pypdf work.
  - System `python3` for the renderer.
- **Settings.** pytest ran with `TMPDIR` and `--basetemp` under `WT/scratch/fr_pec_01/` and `-p no:cacheprovider`. Git reads used `GIT_OPTIONAL_LOCKS=0`.
- **I did not run** the exporter itself, LibreOffice, cargo or installs.
- **Writes.**
  - This report and `SHA256SUMS`.
  - Scratch outputs.
  - One stray step during link-check setup created and deleted an untracked temporary copy of main's AUM in `docs/alignment-manual/` within a single command. Nothing remained.

  `git status` shows only the untracked `BRIEF_FR.md` and these review files.

## For ROOT to rule

1. **MAJOR-1.** Regenerate the export as the last content step, extend the manifest's scope to `export-report.md`, and correct RULINGS §4.
2. **MINOR-2.** Accept the README pointer, or decline it as outside the authorized correction.
3. **NOTE-4.** Leave App v4 out of the §1, §2 and §18 lists, as now, or extend them. Either is true. Extending them would widen the revision beyond the owner's PEC-scoped direction.
