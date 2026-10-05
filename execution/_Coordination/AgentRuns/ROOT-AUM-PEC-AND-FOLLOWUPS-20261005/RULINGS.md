# HELP_HUMAN's rulings: the Agent User Manual's PEC statements, Consolidated v8, and App v4's pins (2026-10-05)

Run `ROOT-AUM-PEC-AND-FOLLOWUPS-20261005`. The owner's direction is in [OWNER_DECISIONS.md](OWNER_DECISIONS.md).

## 1. The AUM's PEC statements

**PM, a Type 2 TASK** dispatched under [BRIEF_PM.md](BRIEF_PM.md) as a Claude Code subagent (general-purpose, Claude Opus 5.5), established PEC's current state from its own records and drafted the edits in [AUM_PEC_EDITS.md](AUM_PEC_EDITS.md) (sha256 `229241ab…`).
- **PEC's current state:** PEC adopted the shared loop on 2026-09-25 (D-PEC-94; commit `11be801130`, PR #917). Its `LOOP_INIT.md` is evergreen, and the steering selects the undertaking.
  - **Remaining sections are retired** (D-PEC-99).
  - **The graph method** is `construct-local-work-graph`, with graphs at `WorkGraphs/<undertaking>/WORK_GRAPH.md`.
  - **Closeout** is one bounded closeout, then a central `RECEIPT.md` and MEMORY rows.
  - **The `LOOP_RECEIPTS.md` ledger** closed at Receipt 197, and its validator now only protects it.
  - **What PEC retains:** its D-PEC packet rule, fences F-PEC-1..4, reliance gates, and its MEMORY grant condition.
- **The edits:** 16, made of 26 before/after pairs. HELP_HUMAN applied all 26, and the result equals PM's predicted sha256, `16fb79f5…`. A first application took only the first pair of each edit and missed this hash; it was reset and redone.
- **PM's questions:**
  - **Q1, adopted:** §9's two adopter statements (lines 347 and 381) now name "App, App v4, Piping and PEC", matching `construct-local-work-graph` §3 as revised in #1093. §13's "Graph-led App/Piping closeout…" is extended the same way, and the revision note says so. HELP_HUMAN checked the other "App/Piping" mentions: lines 68, 549, 675, 700 and 765 are historical or illustrative, and stay true.
  - **Q2, kept:** E12's `v2-parsers` profile correction. It is a PEC statement that is untrue at main, and the owner asked for PEC's current state.
  - **Q3, omitted:** the D-PEC-88 trace clause. The cited PEC `AGENTS.md` carries it.
- **The AUM's headings at levels 1–3 are unchanged.** The HTML is re-rendered on basis `7ba1181d43` (2026-10-05), and the README's render command records that basis.

## 2. Consolidated v8

- **Three §4.2 sentences** told a loop to point LOOP_INIT at the graph, against the evergreen rule. They now say the graph's path is returned for continuation, the human's steering selects it, and LOOP_INIT names no undertaking.
- **The Word and PDF editions were rebuilt** with v8's own method and v8's own renderer, the Codex runtime's bundled LibreOfficeDev 26.8.0.0.alpha0. The scripts and evidence are in `plans/evidence/2026-10-05_manual_v8_loopinit/`.
- **Reproducibility, checked first:** v8's scripts on the unchanged Markdown rebuilt every Word package part byte for byte.
- **The content check equals v8's.** Only the pages holding the edited paragraphs (physical pages 83 and 87) changed, and both were inspected visually.
- **The LibreOffice 26.8.1 download** was not needed for the build. It is deleted from scratch after the run.

## 3. App v4's seven pinned hashes: no re-pinning

**The hashes are point-in-time provenance.** Tranche ROOT-LOOPINIT-AUM-ALIGNMENT-20261005 left them to App v4's loop to re-pin. On inspection:
- `policy_standing/basis.json` and `a16/basis.json` record one App v4 TASK's consultation basis: its role, model, parent and base `38bb2bc87a`.
- `instructions/SOURCE_MAP.json` records what its author read for App v4's bundled instructions.

Several other entries in the same files already differ after App v4's own later changes.

**Nothing App v4 derived is affected:**
- App v4's bundled instruction files do not contain the changed LOOP_INIT sentence.
- LOOP_INIT was read as "Execution entry only; not product defaults".
- The AUM was read to "Headings to level three only", and its headings are unchanged.
- The README was read for "Current editions", which are unchanged.

**Re-pinning would misstate what was read, so it is not done.** A follow-up notice to App v4 says this (`projects/chirality-app-v4/execution/_Coordination/NOTICE_2026-10-05_ROOT_LOOP_INIT_PINS_FOLLOW_UP.md`).

## 4. The public export

The export is regenerated at the final tree with the default staging path, as in #1094. Only `export-manifest.csv` changes.

## Gates

- an independent review (`reviews/`), with any repair confirmed by the same reviewer;
- G4;
- the entrypoint validator;
- GEN-8;
- the export-profile tests;
- the renderer check;
- the PR's automatic CI.

No product code changes.

## Addendum A: FR's review and the repairs (2026-10-05)

**FR's review** is `reviews/FR-PEC.md` (sha256 `efb8f7e1…`). Verdict: **REPAIR**, with 0 BLOCKING, 1 MAJOR, 2 MINOR and 4 NOTE.

**Confirmed by FR:**
- every edited PEC statement, against PEC's own records;
- the 26 pairs, which reproduce `16fb79f5…`, plus the adopted Q1 lines;
- the AUM's headings are unchanged, and its links resolve;
- the renderer check;
- v8: exactly three sentences; Word parts `document.xml` and `app.xml` only; PDF text differs only on pages 83 and 87; the content check equals the committed one; the evidence scripts differ only in `EXPECTED_MD`;
- the App v4 ruling;
- G4, GEN-8 and the entrypoint validator.

**The repairs:**
- **MAJOR-1, repaired. Erratum to §4.** The export was run before the manifest's final edit, so it lacked this tranche's own manifest row; #1094 did the same, and this PR's export corrects that row. The export is now regenerated last, after every other edit, with the default staging path. Both `export-manifest.csv` and `export-report.md` are committed, and the manifest declares both.
- **MINOR-1, repaired.** The App v4 follow-up notice now says this tranche changes the AUM and the README again, in parts App v4's maps did not read, so two pins trail by two revisions. The recommendation stands.
- **MINOR-2, adopted.** The README's management-manual paragraph now points to the v8 revision's production note.
- **NOTE-2, repaired. Erratum to §3.** `policy_standing/a16/basis.json` records only a consultation and its sources, not role, model and base. The notice now says so, and adds the stronger grounds FR found:
  - each `candidate.json` pins its `basis.json` by hash;
  - no App v4 code or test reads these maps.
- **NOTE-3: erratum to `OWNER_DECISIONS.md`'s list of downloads.** LibreOffice 26.8.1 was downloaded and checked against its published SHA-256, but it was **not used**. The rebuild used the bundled LibreOfficeDev 26.8.0.0.alpha0, as the production note says. The download was deleted from scratch.
- **NOTE-4, ruled.** App v4 is not added to the §1, §2 and §18 lists. None of those lists claims completeness, and the owner's direction was PEC-scoped. E10(a) stays.
- **NOTE-1** needs no change.

## Addendum B: FR's Addendum A at `d715935595`; READY (2026-10-05)

**FR's Addendum A** is appended to `reviews/FR-PEC.md` (file sha256 `d290679f…`, the newest line of `reviews/SHA256SUMS`).
- **Verdict: READY.**
- **Confirmed:** MAJOR-1 (the export is byte-identical to a fresh stage of the head, 1,879 rows, default staging path), MINOR-1, MINOR-2 and NOTE-2. G4 covers all 24 changed paths.

**A-NOTE-1, applied as FR proposed.** The App v4 follow-up notice's opening now says the seven hashes record what *two* App v4 TASKs consulted:
- `SOURCE_MAP.json` comes from `/root/group_a_execution/v4_guidance_tranche`;
- both `basis.json` files come from `/root/group_a_execution/policy_standing_production`.

The notice's bullets and §3 already describe the maps separately. The exporter skips `projects/`, so the export is unaffected.
