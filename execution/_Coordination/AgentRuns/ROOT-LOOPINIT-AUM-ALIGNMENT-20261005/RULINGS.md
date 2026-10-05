# HELP_HUMAN's rulings: App v4's reading sentence, consistency edits and the Agent User Manual (2026-10-05)

Run `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`. The owner's direction is in [OWNER_DECISIONS.md](OWNER_DECISIONS.md).

## AM's return

AM, a Type 2 TASK, was dispatched under [BRIEF_AM.md](BRIEF_AM.md) as a Claude Code subagent (general-purpose, Claude Opus 5.5). It made no Git writes. It returned [AUM_EDITS.md](AUM_EDITS.md) in two revisions; the second has sha256 `12897483…`.
- **The edits:** 17 to the Agent User Manual (AUM), E1–E17. Each "before" occurs exactly once. Applied together, they give the AUM at sha256 `1ba63acd…`, 896 lines. HELP_HUMAN applied them and got the same hash.
- **Outside the AUM:** no edits needed, apart from App v4's sentence itself.

## Rulings

1. **App v4's sentence.** "If you are unsure whether something matters, ask the human." becomes "If you are unsure whether a section matters, read it.", as the owner directed. Nothing else in App v4's LOOP_INIT changes. (AM Q3: piping's "as Root `AGENTS.md` requires" is not added to App v4.)
2. **The AUM edits E1–E15:**
   - re-point every citation of piping loop sections that no longer exist (§§0–6) to where the rule now lives: the Field Book, the bundled workflows, or piping's `AGENTS.md`;
   - correct the statements that piping's loop names a graph or says "none selected for a successor undertaking";
   - add a `[field-book]` link definition (AM Q2, accepted).
3. **App v3 statements are corrected to be true at the new basis (AM Q1).** The HTML is re-rendered with a new source basis (main `87661be164`, 2026-10-05), so every statement made "at this basis" must hold there. E2, E4, E5 and E16 do this for App's "none selected" wording and the "LOOP_INIT pointer". E5 now says "`LOOP_INIT.md` names the WorkGraphs location, not a particular graph; the human's steering selects the graph", which is true for both App and Piping.
4. **E17 is kept (AM Q5).** §14's Node note said the App build guide was stale "at this basis". The guide now records `>=22.19.0`, so the note would be false at the new basis.
5. **The PEC statements (AM L5) are not changed here (AM Q4).** They have been inaccurate since PEC adopted the shared loop on 2026-09-25, and are not caused by these changes. A PEC-scoped revision should correct them. Recorded in the manifest.
6. **Not changed:**
   - Consolidated v8's three "point LOOP_INIT" lines (AM L1). The owner named the Agent User Manual.
   - The "In doubt, ask." guidance about found relationships (AM L2), from App v4's rulings GC-7 and GC-8, which is about relationships, not reading.
7. **Piping's already-stale entry pointers are corrected here,** as routed by run `PIPING-LOOP-INIT-20261005`, RULINGS Addenda A and B, under the owner's "any other minimal consistency edits":
   - B1, `projects/chirality-piping/README.md`;
   - B2, `projects/chirality-piping/docs/README.md`;
   - B3, `_COORDINATION.md` Pointers;
   - the contributor guide's row 8, which now says "the work graph the human's steering selects".
8. **App v4's product pins.** Three App v4 product resources record the previous LOOP_INIT's sha256. They belong to App v4's loop, so they are not edited. A notice is routed to App v4 (`projects/chirality-app-v4/execution/_Coordination/NOTICE_2026-10-05_ROOT_LOOP_INIT_READING_SENTENCE.md`). No test compares those hashes.
9. **The HTML edition** is regenerated with `render_manual.py`, using the pinned renderer versions already installed (`markdown-it-py` 4.2.0, `mdurl` 0.1.2). Nothing was downloaded. The README's render commands record the new basis for the agent guide. The Field Book is not re-rendered, so its command and basis are unchanged.
10. **The construct-local-work-graph sentence** was handled separately in tranche ROOT-CONSTRUCT-LOOPINIT-WORDING-20261005 (#1093, approved by the owner and merged). No AUM passage quotes it.

## Gates

- an independent review (`reviews/`), with any repairs confirmed by the same reviewer;
- G4;
- the entrypoint validator;
- GEN-8;
- the PR's automatic CI.

No product code changes.

## Addendum A: AR's review and the repairs (2026-10-05)

**AR's review** is `reviews/AR-AUM.md` (sha256 `2437c0bf…`). Verdict: **REPAIR**, with 0 BLOCKING, 1 MAJOR, 0 MINOR and 5 NOTE.

**Confirmed by AR:**
- E1–E17 reproduce the head AUM byte for byte;
- all 32 cited quotes appear verbatim;
- no `[Piping loop §…]` citation remains, and every link resolves;
- every edited statement is true at `87661be164`;
- exactly one App v4 sentence changed;
- the renderer `--check` verifies the HTML;
- B1–B3 and row 8;
- G4, the entrypoint validator and GEN-8.

**The repairs:**
- **MAJOR-1, repaired.** App v4's product resources pin seven hashes this tranche changes, not three. Besides LOOP_INIT's three pins, `SOURCE_MAP.json` (entries `manual_index` and `user_manual`) and `policy_standing/basis.json` pin the alignment-manual README and the AUM Markdown. The App v4 notice and the manifest's rationale now list all seven. **Erratum to ruling 8,** which said three.
- **NOTE-1, accepted. Erratum to ruling 4's reason.** The App build guide has recorded `>=22.19.0` since 2026-09-22 (`a89b5ddecf`), so §14's "stale at this basis" Node note was false at every basis it was rendered with. E17 corrects it, and the decision to keep E17 stands.
- **NOTE-2, applied.** B1 and B2 now say "`AGENTS.md` holds the project constraints and fences", so they do not conflict with LOOP_INIT's own "Standing constraints" section.
- **NOTE-3, applied.** Row 8 now says "these sources do not expand scope or lift holds", since LOOP_INIT no longer holds a graph pointer.
- **NOTE-4, applied.** The public export is regenerated at this PR's final tree, as earlier manual tranches did (`exports/chirality-app/export-manifest.csv` and `export-report.md`). It is staged outside the repository, and it also brings the export up to date with #1093.
- **NOTE-5** confirms ruling 5; no change.

## Addendum B: AR's Addendum A at H2 (2026-10-05)

**AR's Addendum A** is appended to `reviews/AR-AUM.md` (file sha256 `17ef5b9a…`; the original is a byte prefix). At H2 `6049100caa`: 0 BLOCKING, 1 MAJOR, 1 MINOR and 1 NOTE.
- **AR confirms MAJOR-1's repair:** all seven pins were checked against the resources and main's bytes.
- **AR confirms NOTE-1 to NOTE-3.**
- **The export:** the manifest is byte-identical to the exporter's output for H2's tree.

**The findings:**
- **A-MAJOR-1, repaired. Erratum to Addendum A's NOTE-4.**
  - Staging the export outside the repository made `export-report.md` line 5 record a machine-absolute staging path. The same defect had been repaired once before, in `d2929fd62b`.
  - The export is re-run with the default stage, `exports/chirality-app/staging`, which `.gitignore` excludes. The staging folder is then removed.
  - Line 5 again reads `exports/chirality-app/staging`, and the manifest is unchanged.
  - NOTE-4's "staged outside the repository" was the error.
- **A-MINOR-1, repaired.** The tranche manifest now declares `exports/chirality-app/export-manifest.csv` and `export-report.md`, as earlier manual tranches did. Its `scope_limits` names the regenerated export and the Piping run's final records.
- **A-NOTE-1, noted.** Before this PR, main was behind only on construct's `WORKFLOW.md` row. It was not behind on `workflows/index.json`.
