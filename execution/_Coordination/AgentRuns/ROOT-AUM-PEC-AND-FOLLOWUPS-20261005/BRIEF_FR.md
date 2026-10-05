# Brief FR: independent review of PR #1095 (AUM PEC statements; Consolidated v8; App v4 pins)

TASK (Type 2), an independent reviewer for HELP_HUMAN (ROOT), run `ROOT-AUM-PEC-AND-FOLLOWUPS-20261005`. You return to ROOT and do not delegate. **You wrote none of the reviewed text**: PM drafted the AUM PEC edits, and ROOT applied them and did the rest.

## The candidate

PR https://github.com/sgttomas/chirality/pull/1095, branch `codex/root-aum-pec-and-followups-20261005`, at the head named in your dispatch. It is cut from main `7ba1181d43`.

## Basis

- `RUN3/OWNER_DECISIONS.md`, `RUN3/RULINGS.md` and `RUN3/AUM_PEC_EDITS.md`.
- **PEC's own records:**
  - `projects/pec/AGENTS.md`;
  - `projects/pec/loop/LOOP_INIT.md` and `LOOP_RECEIPTS.md`;
  - `projects/pec/init/`;
  - the `PEC-*` tranche manifests;
  - PEC's decision records cited in the edits, such as D-PEC-94 and D-PEC-99.
- `workflows/construct-local-work-graph/WORKFLOW.md`.
- **v8's production method:** `plans/evidence/2026-10-04_manual_v8/`.
- **App v4's pinned resources** under `projects/chirality-app-v4/app/src-tauri/resources/`, and the #1094 notice they follow up.

## Review, in priority order

1. **The AUM PEC statements:**
   - every edited statement is true of PEC at main `7ba1181d43`. Verify against PEC's records, not against PM's summary;
   - no PEC statement in the AUM remains false;
   - the edits are minimal, and nothing else changed (diff against main);
   - the §9 and §13 extensions to App v4 and PEC are true;
   - the remaining "App/Piping" mentions are correctly left alone, as ruled;
   - the headings at levels 1–3 are unchanged;
   - every link resolves;
   - the HTML is the renderer's output for the head's Markdown, with basis 2026-10-05 and `7ba1181d43`. Use `render_manual.py --check`;
   - the README basis is right.
2. **Consolidated v8:**
   - exactly three sentences change in the Markdown, and each new sentence is true under the evergreen rule;
   - the Word file's package parts differ from main's only where those paragraphs, and the Contents folios or summary fields affected by them, require. Compare parts;
   - the PDF has 172 pages, and its text differs only on the pages holding the paragraphs;
   - the content check passes. Re-run `plans/evidence/2026-10-05_manual_v8_loopinit/format-content-check-v8.py` on the head's files, to a scratch output;
   - the production note is accurate;
   - the evidence copies differ from v8's scripts only in `EXPECTED_MD`.
   
   To re-run the check you can use the scratch environment at `WT/scratch/tools/docvenv/bin/python`, which has `lxml` and `pypdf`.
3. **App v4's pins:**
   - the ruling not to re-pin is sound: the seven entries are consultation records, and the read extents and unchanged parts are as stated;
   - the follow-up notice is accurate;
   - no App v4 product resource changed.
4. **The manifest:**
   - G4 passes in CI mode and in diff mode against main with `--tranche`;
   - the authorization quotes match;
   - the rationale and scope are true, and cover every changed path.
5. **The export:** regenerated at the final tree, with the default staging path in `export-report.md`.
6. **Portability:**
   - GEN-8 on the head;
   - no new machine-absolute paths in text files;
   - no credentials;
   - the entrypoint validator passes.

## Host and method

- **Your copy:** read-only, in `WT/pec-pr`. Do not modify tracked files. Logs and scratch outputs go in `WT/scratch/fr_pec_01/`.
- **What you may run:** GEN-8, the two validators, `test_public_export_profile.py`, the renderer `--check`, the v8 content-check script (to scratch output), and `pypdf` text extraction.
- No cargo, no LibreOffice runs, no Git writes, no installs, and nothing in the system temp directory.

## Output

- **The report:** `RUN3/reviews/FR-PEC.md` plus `RUN3/reviews/SHA256SUMS`, with placeholder paths only. It contains:
  - a verdict, READY or REPAIR;
  - counts of BLOCKING, MAJOR, MINOR and NOTE findings;
  - each finding with its evidence and fix.
- **Time box:** 90 minutes.
- **End your turn** with the verdict, the counts, one line per finding, the report's sha256, and anything ROOT must rule on.
