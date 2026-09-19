# RETURN — DESIGN-SYSTEM-03 and DESIGN-SYSTEM-04 · Design system V1.2, then V1.3

Instance: DESIGN-SYSTEM (HELPS_HUMANS design manager, child of ROOT). Brief:
`../../briefs/DESIGN-SYSTEM-03_revision.md`, sealed. Date: 2026-09-18. For ROOT's
acceptance. This file replaces the DESIGN-SYSTEM-02 return. Sections 1 to 7 are the
DESIGN-SYSTEM-03 return with ROOT's two corrections; §8 is the DESIGN-SYSTEM-04 return
(V1.3), and the hash table below carries the current values first. §11 is the
DESIGN-SYSTEM-05 addendum (V1.4): it carries the current hashes, and the table in §2
stands as it was at V1.3.

## 1 What was read

The sealed brief; ROOT's preparation record (`../ROOT/REVISION_PASS_PREPARATION_2026-09-18.md`);
`../MOCKS/MOCKS_V2.md` with its frames and tools; decision packet D-71; `../UX-SPEC/UX_SPEC_V1.md`
(§2.6, §3.7, §5.4 to §5.5, §6.3, §7.5 to §7.7, §8, §10.3 to §10.9); the claims registry's
entries for the acceptance boundary, the content boundary and the evidence labels; the head of
the product's historical-run context component, for the rendered historical wording; the
rendering brief; the implementation-handoff preparation; the brief index; and this
instance's own V1.1 files. Wider consultation: none of another role's instructions.

After the brief was sealed, ROOT sent one message relaying two later directions of the owner.
I applied both on ROOT's word, under the same rules, each with its own change-log row:

- the maturity sentence is removed from the product entirely (supersedes ruling 2);
- the Checked mark is ruled, D-71 item 7 option A, with its exact words (supersedes ruling 7).

## 2 What changed

All in place under this directory; nothing outside it was written.

| File | Change | sha256 |
|---|---|---|
| `DESIGN_SYSTEM_V1.md` | **Now V1.3 with row 111, `20b100bd9c979a9341b96431387bbf8ca45b01f10debfe0964b7a4f2d5c02e7e` (§8, §9; V1.3 as accepted `f4769893…`).** At V1.2: Every change is a numbered row of §9, rows 50 to 87, and rows 88 and 89 for correction 1; rows 1 to 49 are byte-identical to V1.1 and rows 1 to 87 to V1.2 as first returned (both checked by hash). The §9 heading now covers V1 to V1.1 and V1.1 to V1.2. Ends with the fence line. | `efa22d497772e717b4cc19bc2a703ed765d0ac158fa177efbf39f373e0acfc1f` (after correction 2; after correction 1 `1a7ffe40…`; as first returned `2e0db6bc…`) |
| `tokens.json` | 1.2. Adds `canvas.edgeAlt`, the toast, HUD and run log values, the `labels` table (eight rows) and `agentCardClasses` (five words); the name is the product's name alone. Every colour value of 1.1 is unchanged (diffed). | `00c1afe97365973e6c05a2a5d938a25c46022a55c3cbc8d04ff3a9d2d68cf1e9` |
| `specimen.html` | **Now V1.3, `f9ce15a26331177bdf78cf6dfb3e5ff568ef0756c02b17333ebc5b6807273a99` (§8).** At V1.2: one self-contained file, inline styles and script, no network reference, light and dark. | `219fa8ee78c44507fcfc0b6a199298c8f4a4026abe798f4166eeda2eb607941b` (after correction 1; as first returned `c390e7e6…`) |
| `tools/palette.mjs` | the new tokens and groups; `--write` reproduces `tokens.json` byte for byte (checked) | `de73ecb9…` |
| `tools/contrast.mjs` | six pairings for the edge lines on the result scale: 152 pairings | `7a3f2653…` |
| `tools/gen.mjs`, `tools/splice.mjs` | generate the label table and splice it into §2.3 between markers | `f936d18a…`, `34e986a1…` |
| `tools/agree.mjs` | **Now `ef312774a7050a0a5bab3508de8698612f1ab338559442c767cc01f61877b54f` (§9; at V1.3's acceptance `0df98d6b…`).** V1.2 checks, §3 below; after correction 1 also rows 88 and 89 present, rows 1 to 87 unchanged by hash, and the stale band's removed clause absent; after correction 2 also row 90 present, rows 1 to 89 unchanged by hash, and the two removed framings absent | `e02a7180…` |
| `tools/render.mjs` | **Now `0fb28c40cbf9293cb4d43331b4edcc9abc1840a1820917fe240e7192a392d14c` (§8).** V1.2 checks; takes a relative specimen path; takes the Playwright location at run time (`--playwright-from <dir>` or `PLAYWRIGHT_FROM`), default the relative path to the piping project as before | `b886e708…` |

No file in the instance carries an absolute machine path; `agree.mjs` now walks the
instance and fails if one appears. The retired strings are built by concatenation inside
the two check scripts, so the tools directory does not carry them either.

Trace of the brief to §9 rows: ruling 1 → 50; ruling 2 (as superseded) → 51; ruling 3 → 52,
77; ruling 4 → 53, 54; ruling 5 → 55; ruling 6 → 56, 57; ruling 7 (as superseded) → 58;
ruling 8 → 59; ruling 9 → 60; Q-20 and the pointer rule → 61 to 67; Q-15 → 68; Q-16 → 69;
Q-17 → 70; Q-18 → 71; Q-19 → 72; Q-21 → 73; Q-22 → 74; G-7 → 75; G-8 → 76; G-9 (closed
unused) → 77; G-10 → 78; G-11 → 79; G-12 → 80; R-4 → 81; R-5 → 82; R-6 → 83; the
consequence line (MOCKS_V2 D2-1) → 84; §8 → 85; tokens and tools → 86; specimen → 87.

What the status bar's information popover now holds: nothing, and it goes. In V1.1 it
held two lines, the About link and the maturity sentence. With the sentence removed a
popover with one link is not worth a click, so the control (an information glyph,
tooltip "About SWBPIPE…") opens About directly. About carries the name, version and build,
then its tabs; the line the sentence held is closed. The M-01 and M-02 homes are removed
from §7.4.

## 3 What was verified, and how

Model: Claude Fable 5.1 (`claude-fable-5-1`), one agent, no delegation. One context
compaction occurred mid-run; work resumed from the files on disk and a transcript summary,
and every check below was run after the last edit. Edits to the document and specimen were
anchored replacements, each anchor required to occur exactly once.

**Agreement check** — `node tools/gen.mjs tokens.json <out>`, `node tools/splice.mjs <out>
specimen.html DESIGN_SYSTEM_V1.md`, `node tools/agree.mjs DESIGN_SYSTEM_V1.md tokens.json
specimen.html`: `problems: []`. 99 colour tokens, 98 plain tokens, 99 document colour rows,
152 contrast rows and pairs, 8 labels, 25 label chips in the specimen, 5 card classes, 87
change-log rows. The check covers: the colour tables, CSS blocks, embedded token JSON and
pair list against `tokens.json`; the §2.3 label table against a fresh generation; every
specimen label chip (class, token, domain, label) against the table, no label drawn
outside the chip markup, and the two unhyphenated forms nowhere; agent cards carrying one
of the five class words, every class shown, and agent text free of the five barred words;
the retired strings absent, case-insensitively, from the document, the token file and the
specimen (the longer name, the old name, the other vendor's product name, both halves of
the maturity sentence, three fragments of the acceptance sentence); change-log rows
contiguous, rows 1 to 49 unchanged by hash, and rows 50 on citing rulings 1 to 9, Q-15 to
Q-22, G-7 to G-12 and R-4 to R-6; every sprite reference resolving; no external reference;
the document ending with the fence line; no machine path in any instance file. I ran the
check once against a copy with sixteen faults injected and it reported each.

**Separate searches** (Python, case-insensitive, over the three deliverables): the same
retired strings and "user rules checked" / "user rule failed": no match. US spellings in
prose: none (the font licence's proper name aside).

**Render** — `node tools/render.mjs specimen.html <out> --playwright-from <dir>` with
Playwright 1.60 and its Chromium taken from the main checkout's piping project at run time,
because this worktree has no `node_modules`: 1440 and 720 wide, light and dark by system
preference and by the manual switch. In all four: no blocked request (none attempted), no
console error or warning, no horizontal overflow, smallest font 11 px, 99 token rows, 152
contrast rows, 8 label-table rows, the 25 chips redrawn from the table and equal to it,
wrapped HUD 154 by 64 with ten tools and Fit first, toast 320 px, the three Review header
buttons with icons and none accent, no retired string in the rendered text. I read the
screenshots of sections 5, 8, 9, 10 and 11 and fixed what they showed (a clipped button, a
wrapped toolbar, the wrapped HUD's size, which I had stated as 156 by 62 and is 154 by 64).

**Not run:** the dataviz palette validator was not found locally; the result ramp and the
categorical set are byte-identical to 1.1, where it was run, and the built-in ordinal check
passes in both themes. No product build or test was run, by instruction. `git status`
(read-only) shows changes in this instance directory only.

## 4 The key-only actions of V1.1 and their pointer controls

The rule is stated at the head of §5 and, for copy, in §7.6. The owner's words were about Q-20 only; the general rule is ROOT's reading of them, open to the owner's correction (correction 2, §7 below). The audit table is in §5; in
summary ("found" means the control existed in V1.1 and is now named):

| Action (V1.1 key) | Primary control in V1.2 |
|---|---|
| Open / close the Both-view inspector (⌘I, double-click; Escape) | the toolbar's Inspector toggle; the close control in the inspector's header |
| Open / collapse the agent column (⌘⇧G) | the Agent toggle (found); a click on the strip; the column header's collapse control |
| Fit (F) | the Fit tool (found), now first in the HUD at every canvas width |
| The other HUD tools (I H L D P R S) | the HUD tools (found) |
| Show what is hidden (none stated) | the HUD's count button, "3 hidden · Show all" |
| Routing: axis (⇥, arrows) | a click on an axis handle |
| Routing: reverse (−) | the Reverse control beside the length field; a click on the opposite stub |
| Routing: place (↩) | the Place control; "Place node 50" in the routing block |
| Routing: cancel (⎋) | the Cancel control beside the length field; the routing block's Cancel (found) |
| Routing: bend (B) | the routing block's "Bend at 40…" (found) |
| Unpin the probe (Escape) | the pinned card's close control |
| Start / commit / cancel a cell edit (↩, ⇥, ⎋) | a click on the focused cell; a click on another cell or the footer edit chip's Commit; the edit chip's Cancel |
| Open a row expansion (⌘↩; Space) | the expansion chevron in the owning cell |
| Open a joined row (⌘↩) | the marks slot and the faint plus (found) |
| Close an expansion (⎋, ⌘↩) | the caption line's chevron; its close control |
| Insert a row (⌥↩) | the footer's Insert row below; the "Add row" line |
| Delete, copy, paste rows (⌫, ⌘C, ⌘V) | the footer's selection group |
| Select all rows (⌘A) | the gutter's header cell |
| Clear the selection (⎋) | the clear control on the footer's selected count |
| Check rows, clear the check (⌘⇧K) | the faint check in an empty state slot; the footer's Check rows; the Checked popover's buttons; the inspector's control (found) |
| Reveal a mark (Space, ⌥I) | a click on the glyph; "All marks on this row" in its popover |
| Undo, redo (⌘Z, ⇧⌘Z) | the toolbar's Undo and Redo |
| Send to the agent (⌘↩) | the Send control |
| Close the issues drawer; collapse the table drawer (⎋) | the drawer's close control; the collapse chevron on the tab strip |
| Close a dialog (Escape) | every dialog's Cancel or Close button |
| Close a popover, the run log, a menu (⎋) | a click outside (found) |
| Dismiss a toast (none stated) | the toast's close control |
| View switch, palette, Issues, sort, Accept and Reject, paste band, combination editor, Run and Stop | all found, unchanged |

## 5 Uncertainties, and what in the rulings did not apply cleanly

1. **The domain word for the two evidence labels.** Ruling 4 requires the authority domain
   with every label; the governed domains are the statuses'. I used "Evidence"; it is one
   field in `tokens.json` and is the owner's to confirm (§8 item 14).
2. **Stale is treated on Historical terms.** Ruling 6 and R-9 bar a Historical record from
   a current-model overlay. After a model change the run is no longer current, so V1.2
   gives a Stale run no overlay, chip or evidence chip either. UX_SPEC_V1 §2.6 and §10.4
   say otherwise; the conservative reading is taken and flagged for UX-SPEC-02 (§8 item 16).
3. **Settled by ROOT (correction 1, §6 below).** As first returned: two sentences about the same run disagree across documents: the stale band keeps
   decision 4's "stays the solve basis", the specification's consequence line says the
   run stops being it. V1.2's consequence line avoids the phrase (§8 item 17).
4. **Q-16's words are geometrically inconsistent** at 1440 ("right-aligned under the Run
   button" and "over the canvas"); I specified by the stated purpose (§8 item 18).
5. **Q-22 applied as written:** the Kind menu has no entry for the engineer's notes; Mine
   reaches them (§8 item 15).
6. **The fitted camera** (Q-20) is one new bit of interface state, a semantic addition and
   not a restyling (§8 item 12). **`canvas.edgeAlt`** asks the engine for a per-element
   edge colour; feasibility is for the rendering observation (§8 item 13).
7. **Ruling 8 and the product's own strings.** "draft until accepted" and "accepted 16:31 ·
   Undo" remain on proposal cards as product text, not agent text; I reworded two sample
   agent sentences in the specimen that used a barred word. If the owner means the barred
   words to leave the card's product strings as well, that is a further change.
8. **"Acceptance not recorded in this session"** (§5.4, reopened records; C-68) is kept: it
   is about proposal acceptance, not the removed sentence.
9. **Toast message length.** Beside an action and the close control a 320 px toast leaves
   about 190 px for the message, so I allowed three lines, not two.
10. **Settled: ROOT named the owner records, now cited in §9 row 89.** As first returned: the two later rulings were applied on ROOT's relayed word; I did not see an owner
    record for them beyond ROOT's message and ROOT's scratch copy of the ruling.
11. The validator was not re-run (§3). The 1440 and 720 renders are Chromium only.

Nothing in the brief was left unapplied. Rulings 2 and 7 are applied in their superseding
form, as ROOT directed.

## 6 Correction 1, after ROOT's review of this return

ROOT accepted the return's checks and decided the uncertainties: 1, 2, 4, 5, 7, 8 and 9
stand as written; 10 is answered by the two owner records; 3 is settled as follows. After
a model change the run stops being the current solve basis (the product clears the solve
proof and the model hash when a model commit lands), so the stale band's closing clause,
which said the run remained the basis until the next run, was wrong.

- Removed from the stale band in §5.1, its row in the §4 placements table, the vocabulary
  of §7.1 and the specimen's band. The band reads "Model changed since Run 03: *the change,
  with its time*. The values below are from the model as solved." with "Run again"; the
  compact form reads "Model changed since Run 03 · *change* · Run again".
- §8 item 17 is closed by ROOT with that wording; item 16 says ROOT confirmed the Stale
  column.
- §9 row 88 records the correction; row 89 cites the owner records for rows 51 and 58
  (`_DECISIONS/D-71_RULING_ADDENDUM_2_2026-09-18.md` for the maturity sentence,
  `_DECISIONS/D-71_RULING_ADDENDUM_2026-09-18.md` for the Checked mark).
- `tools/agree.mjs` now requires rows 88 and 89, checks rows 1 to 87 by hash against V1.2
  as first returned, and fails if the removed clause appears in the document, the token
  file or the specimen (tested with an injected copy; it fails).
- Re-run after the correction: gen, splice, agree (`problems: []`, 89 change-log rows) and
  the render check (1440 and 720, light and dark: no request, no console issue, no
  overflow, chips equal to the table). `tokens.json` is unchanged.

One thing did not apply cleanly: ROOT asked for the owner records to be cited in rows 51
and 58, and also for rows 1 to 87 to stay byte-identical. Both cannot hold, so rows 51 and
58 are untouched and row 89 carries the citations for them.

## 7 Correction 2, from the independent review (REVIEW-03)

Two wording fixes in `DESIGN_SYSTEM_V1.md`, recorded as §9 row 90; rows 1 to 89 are
unchanged by hash. `tokens.json` and `specimen.html` are unchanged.

1. The pointer rule's heading at the head of §5, and the sentence in §0 that called the
   general rule the owner's amendment, now attribute the owner's words to Q-20 and the
   generalization to ROOT's reading, as the D-71 ruling record states it, open to the
   owner's correction. §7.6 refers to "the pointer rule of §5" without attribution and
   needed no change. Rows 61 to 67 give "Q-20 as amended by the owner" as their source and
   are frozen; the §9 sources paragraph now says how to read that.
2. §7.3 no longer says the Checked mark's words are "exactly these and no others". The
   ruled words are used exactly where they apply; "Check rows", "Check again" and "Clear
   check" are shown to derive from the ruling's "set on one row or many" and its stale
   text "Check again or Clear".

`tools/agree.mjs` requires row 90, checks rows 1 to 89 by hash, and fails if either removed
framing returns. Re-run: gen, splice, agree: `problems: []`, 90 change-log rows. The render
check was not re-run for this correction because the specimen did not change (same hash).

## 8 DESIGN-SYSTEM-04 · V1.3 · the owner's direction on the contradictions

Brief `../../briefs/DESIGN-SYSTEM-04_contradictions.md`, sealed; its SHA-256 was verified
before starting (`90506b29…3a55c`, as ROOT gave it). Read first: ROOT's record
`../ROOT/OWNER_DIRECTION_2026-09-18_CONTRADICTIONS.md`; then `../UX-SPEC/RETURN.md` §6,
`../MOCKS/MOCKS_V3.md` §6, Q-26 and D3-1, and the specification's text for the six
functions (§2.6, §2.7, §3.6, §4.2, §4.5, §5.2, §5.3, §7.5, §7.6). While I worked, ROOT sent
a supplement: the owner ruled the three items the brief's item 8 had left open (15 A,
C-20 A, C-23 B); they are applied in this pass and §8 of the document lists none of them
as open. I did not touch the UX-SPEC instance.

| Brief item | §9 row |
|---|---|
| 1. Additions: units selector's third choice (9) · View tool's menu (10) · Stress cell as fourth expansion owner (11) · "All kinds" (12) · run menu and the wrapped header (C-17, Q-26) · drawer's Filter menu (C-24) | 91 · 92 · 93 · 94 · 95 · 96 |
| 2. Readings as the rule: Review rail item (1) · report readiness (2) · Run button and run log (4) · "current" (13) | 97 · 98 · 99 · 100 |
| 3. The split's drag limit (16) | 101 |
| 4. "Apply" (5) | 102 |
| 5. Run 03 (C-25) | 103 |
| 6. G-22 sentence at the column and the glyphs (8) | 104 |
| 7. §8 item 17's cross-reference (14): wrong for the specification's V1, moot from its V1.1 on; the item says so | 105 |
| Supplement: tooltip form (15 A) · paste band's faces (C-20 A) · three chips on Review (C-23 B) | 106 · 107 · 108 |
| §8 of the document · specimen and tools | 109 · 110 |

Files changed: `DESIGN_SYSTEM_V1.md` (V1.3), `specimen.html` (V1.3), `tools/agree.mjs`,
`tools/render.mjs`, this file. `tokens.json` is unchanged at 1.2
(`00c1afe9…`): no addition needed a value; the menus' widths (240, 220, 280), the 80 px
units button and the header's wrap are stated in the prose, as the component sizes of
V1.2 that are not tokens are.

Checks, all after the last edit: gen, splice, agree: `problems: []`, 110 change-log rows,
28 label chips. `agree.mjs` now also checks rows 1 to 90 by hash, that rows 91 on cite
every contradiction the brief and the supplement name, that "Commit" is no button's face,
tooltip or label in the specimen, that no specimen tooltip writes a key outside
parentheses and no button face carries a key, and that no Historical example reads Run 02;
I ran it against a copy with those faults injected and it reported each. The retired
strings are still absent. Render at 1440 and 720, light and dark: no request, no console
issue, no overflow, chips equal to the table, six menus at their stated widths, the 737 px
header on two lines, the drawer's header on one line (28 px), the edit chip reading Apply
and Cancel, the paste band reading names only. I read the screenshots of what I added
(sections 5, 8, 9 and 10) and fixed what they showed: the stress components were hatched
under a row that was not; the View menu at 220 px truncated its longest entry and is
240 px; the units button at 72 px crowded "Entered" and is 80 px.

What did not apply cleanly, and uncertainties:

1. The brief's item 8 said to list 15, C-20 and C-23 as open; ROOT's supplement reversed
   that, and the supplement is followed.
2. ROOT's supplement names "§5.5's status bar text" for C-23. The status bar is specified
   in §5.2, which is fixed; §5.5 had no such text, so one sentence was added to its header
   paragraph.
3. Tooltip form: I also moved the joined row's caption key ("⎋ closes") into the close
   control's tooltip, because a caption that shows a bare key is the same fault. The hint
   strip keeps its list of accelerators: it is not a tooltip and §7.6 gives it that job.
   The Checked tooltips and other tooltips that name no act are unchanged.
4. Copy I chose, for the owner or ROOT to replace: "As entered" (menu) and "Entered"
   (button); "Box selects" for the box selection's filter group; "Filter" and "Filter · 2";
   "Clear filters"; "Runs" as the run menu's tooltip; the run menu's words Current, Stale,
   Historical, Failed; "Run log · Run 03" as the Run button's tooltip while the click opens
   the log; "Stress components". The specification names the functions and not these
   strings.
5. "As entered" with a column whose rows were entered in different units: I specified
   that the header drops its unit and the cells carry theirs. The specification says only
   that the choice exists; this is my addition of the least that makes the header honest.
6. Settled (§9 below): the owner confirmed the six additions. As first returned: the six additions rest on ROOT's reading (the document's §8 item 19); "Apply" is ROOT's
   word (item 20).
7. The report-readiness row was added to the run-standing table, which is not a change-log
   row, so rows 1 to 90 are untouched.

## 9 Follow-up to V1.3: the owner's confirmation of the six additions

ROOT accepted V1.3 and relayed the owner's confirmation ("Keep the six functions; the
design system additions are fine."). I verified it in the last section of
`../ROOT/OWNER_DIRECTION_2026-09-18_CONTRADICTIONS.md`. The document's §8 item 19 is
closed accordingly and §9 row 111 records it; rows 1 to 110 are unchanged by hash, and
`tools/agree.mjs` now requires row 111 and pins rows 1 to 110. Nothing else was touched:
`specimen.html` and `tokens.json` keep their hashes. Re-run: gen, splice, agree:
`problems: []`, 111 change-log rows. The render check was not re-run because the specimen
did not change.

## 10 Correction after REVIEW-04: finding T-3

Verified in `../REVIEW/REVIEW-04_RETURN.md` (T-3, accepted by ROOT). The owner's
confirmation predates V1.3's text, so it covers the six functions and their addition to
this system, not the copy I chose for them. The document's §8 item 19 now says so where
the closure is asserted, and §9 row 112 records it; row 111 is not rewritten, and
`tools/agree.mjs` pins rows 1 to 111 by hash and requires row 112. The copy stays mine and
open to replacement, as §8 item 4 of this return lists. Agreement check: `problems: []`,
112 rows. Not changed: `specimen.html`, `tokens.json`, the other tools; gen and splice
were not needed and the render check was not re-run. Current hashes: `DESIGN_SYSTEM_V1.md`
`5aef3bdf5746b0f93f9419b4c7ad459eb634a71db28a846f19133b225f277c81`, `tools/agree.mjs`
`84bb30448eb68f510b218602d52175f3dd0fbb7ccad602d694f7a049303d5a27`; the table in §2 carries
the values as of §9.

## 11 DESIGN-SYSTEM-05 · V1.4 · the control boundary and the disabled ink

Brief `../../../HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/lanes/DESIGN-SYSTEM-05/briefs/DESIGN-SYSTEM-05_control_contrast.md`,
sealed; its SHA-256 was verified before starting (`322ca33b…5e7c11`, as ROOT gave it).
Model: Claude Fable 5.1 (`claude-fable-5-1`), one agent, no delegation. Three context
compactions occurred; each time work resumed from the files on disk and a transcript
summary, and every check below was run after the last edit to the file it checks. Edits to the document, the specimen and the
tools were anchored replacements, each anchor required to occur exactly once; nothing
generated was edited by hand.

Read first, all read-only: the brief; the first slice's return
(`../../../HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/B1-TOKENS/RETURN.md`,
"Where the design could not be followed") and its review's observations; the owner's
ruling D-68 (`../../../../_DECISIONS/D-68_RULING_2026-09-15.md`); the product's resolved-style
check and the two values its stylesheet keeps without a token, to see what the product
measures and against what; and the frames' stylesheet and the nineteen frame files
(`../MOCKS/frames/`), for the list below. I wrote in this directory and in
`../../../HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/DESIGN-SYSTEM-05/` only.

| Brief item | §9 row |
|---|---|
| 1. The control-boundary token · every boundary that identifies a control moved to it, each listed | 113 · 114 |
| 2. The sweep of the same criterion: the other failures, fixed with no further token · the wash rule · what is outside the rule, each with its reason | 115 · 116 · 117 |
| 3. `text.disabled`: measured on everything it is drawn on, the pairs in §2.9, the recommendation | 118 |
| 4. Records: §2.2, §2.9, §8 item 6, §9, the specimen, the generated tables, the tools | 119 · 120 |
| 5. Not in this pass, and the frames that draw a control boundary in `border.strong` | 119 (§8's last paragraph) and the list below |

**What changed in `tokens.json` (1.2 to 1.3).** `border.control` added, `#777e85` light and
`#90969c` dark (OKLCH lightness 0.59 and 0.67 at the neutral hue); `text.disabled` from
`#a6abb1` / `#5f6469` to `#8f949a` / `#767b80`; the plain width `border.control` 1; the
version and one sentence of the note. 340 of 347 leaves are equal to 1.2 and the seven that
differ are these; `palette.mjs --write` reproduces the file byte for byte.

**The boundary's value.** It is set by the pressed moment: the lowest readings are 3.17:1 in
light (a pressed field, `pressed.wash` over `surface.sunken`) and 3.14:1 in dark (a pressed
raised button). One step lighter (0.01 in lightness) still passes, at 3.04:1 and 3.02:1; I
kept one step of margin. Holding the rule at rest and under hover only would buy 0.03 in
lightness in light and 0.04 in dark, which is not worth a second rule. The product's kept
`--ui-border` (`#71838d` / `#70828c`) was not adopted: measured on this system's surfaces it
reads 3.24:1 or better at rest and 2.91:1 and 2.35:1 on a pressed sunken and a pressed raised
fill in dark.

**What the sweep decided, beyond moving boundaries.** Each is a row of the table in the
document's §5 and of §9; each is the least that gives the state a carrier.

1. What identifies a control is its boundary where it has one, and otherwise its label or
   its glyph. An icon-only button and a chip are identified by the glyph and the label; the
   hairline around them is ornament and outside the rule. This is my reading of the
   criterion, stated in the rule so that it can be challenged in one place.
2. The latched toggle keeps a boundary, in `pressed.ink`; V1.3 made it transparent and left
   a fill of 1.11:1 to 1.82:1 as the edge. The segmented control's active segment gains a
   `border.control` boundary; its fill is 1.07:1 on the trough.
3. A chip that is a control and is on or chosen takes the latched form. The specimen drew
   the chosen filter chip on a status fill (1.02:1 on the drawer's header in light) and the
   frames draw it on the selection band (1.05:1).
4. The check box and the tab were drawn by the frames and not specified here. The frames'
   forms are adopted: the empty box's outline moves to `border.control` and the checked box
   keeps `accent.fill` with the check in `text.inverse`; the active tab is `text.primary` on
   `surface.header` inside `border.control`, in every strip, the agent column's included.
5. The wash is never drawn over a band or a state fill. With it, the origin glyph on a
   selected row measured 2.89:1 and 2.71:1; without it, 3.23:1 and 3.24:1. No token moved.
6. The two offers under the pointer were "faint" with no token and are `text.muted`; the
   drag handle is `text.secondary`; the splitter, which had no drawn form, is the regions'
   hairline with a grip 3 px by 24 px in `border.control`.
7. Outside the rule, each with its reason in the table: hairlines, frames, a fill that is
   not the carrier of its state, the display-only expression's frame, a disabled control,
   and the select-all control, which draws nothing.

**The disabled ink: the recommendation, for ROOT to decide.** Lift to `#8f949a` / `#767b80`.
Measured, light then dark: on `disabled.fill` 2.56:1 and 3.19:1; on the surfaces 2.68:1 to
3.06:1 and 3.02:1 to 3.92:1; beside `text.muted` 1.24:1 and 1.27:1; beside `text.secondary`
2.05:1 and 2.00:1. The stated ratio, which the tools hold: 2.5:1 or better in light and 3:1
or better in dark on everything the ink is drawn on, and 1.2:1 or more short of
`text.muted`.

| Option | Light | on `disabled.fill` | on the surfaces | beside `text.muted` | Dark | on `disabled.fill` | on the surfaces | beside `text.muted` |
|---|---|---|---|---|---|---|---|---|
| keep 1.2 | `#a6abb1` | 1.94:1 | 2.03:1 to 2.31:1 | 1.64:1 | `#5f6469` | 2.28:1 | 2.16:1 to 2.80:1 | 1.78:1 |
| lift (recommended, 1.3) | `#8f949a` | 2.56:1 | 2.68:1 to 3.06:1 | 1.24:1 | `#767b80` | 3.19:1 | 3.02:1 to 3.92:1 | 1.27:1 |
| 3:1 everywhere in light | `#82878c` | 3.03:1 | 3.17:1 to 3.62:1 | 1.04:1 | as the lift | | | |
| the product's kept ink | `#667680` | 3.94:1 | 4.12:1 to 4.70:1 | stronger than muted | `#9baab2` | 5.71:1 | 5.40:1 to 7.00:1 | stronger than muted |

Why the lift stops at 2.5:1 in light: `text.muted` is itself 3.17:1 on `disabled.fill`, so
an ink at 3:1 there is the muted ink to within 1.04:1, and the product's kept ink is
stronger than muted text, so it reads as enabled. 3:1 everywhere in light needs
`text.muted` to move first, which belongs with the text target (§8 item 6 of the
document). What carries the state besides ink is in the document's §1.3: `disabled.fill`,
the boundary dropping from `border.control` to `border.hairline`, no wash, the reason in the
tooltip; the cursor carries nothing, because it is the default arrow over every control.
To decide otherwise: restore or change the two values in `tools/palette.mjs` (the 1.2
values are in the comment above the line) and the note's sentence there, set
`rules.disabledLight` and `rules.disabledDark` in `tools/contrast.mjs` to the ratio
decided, change the sentences that quote the values (the status line, §2.2's note, §2.9's
`text.disabled` finding, §8 item 6, §9 rows 118 and 120), and rerun the chain below; the
specimen needs no edit by hand.

**Files changed**, all in this directory:

| File | Change | sha256 |
|---|---|---|
| `DESIGN_SYSTEM_V1.md` | V1.4: status, §1.2, §1.3, §2.2's note, §2.9 (method, findings, 214 generated rows), §4, §5 (the control rule and its generated table), §5.2, §5.5, §5.6, §8 (item 6 restated; what a frames pass must follow), §9 rows 113 to 120; rows 1 to 112 unchanged by hash | `8940ce589947536e18be2d11dd9818c98848a841783e125dbdc5efee9548a9c0` |
| `tokens.json` | 1.3, as above | `0e01828c4e7739313a47b5f71ac3c9fa3cf21aae3d07648eadc805fd82d18c00` |
| `specimen.html` | V1.4: the control rules moved to `border.control`; the latched boundary (button, icon button, HUD tool, chip); the active segment's boundary; the tab strip in the tab's form; chips that are on in the latched form; the outline's bar; the compass's buttons and its length field's boundary under the ring; the wash over a button's own fill and over no band or state fill; a disabled icon-only button in `text.disabled` with no wash, which V1.3's specimen left in the enabled ink; a strip of the controls on every surface they sit on, the disabled forms, the splitter and the glyphs | `434a3fff6945afc3a45d7d97f3430d44e3449b895eaeba6c20e17920f23fec3f` |
| `tools/palette.mjs` | builds 1.3; the 1.2 values of `text.disabled` kept in a comment | `4f9b74e7d63c390341c3b61e735390d5aeb65052840c4c45c0c8160661c89009` |
| `tools/contrast.mjs` | 214 pairs (62 added); the sweep (29 rows, 21 held to the rule, 8 outside it); `rules`; `sweepRows`, `toSweepMarkdown`, `ruleFailures`; exits 1 when a rule fails | `ca38b109504f831f71c791327d05792d580df9575478a67e8e5a0f3392bb5563` |
| `tools/gen.mjs`, `tools/splice.mjs` | generate `control_sweep.md` and splice it between the `GENERATED:CONTROL_SWEEP` markers of §5 | `af708b626a9a5a6c5b74ac96852bbdc6a1bae85db9760958cc28f6fc09796e21`, `56538c093d75c582b3870cc26187db795dee352777e3c80dbdb9013a85ceb1a6` |
| `tools/agree.mjs` | checks V1.4, 1.3 and "specimen V1.4"; rows 1 to 112 by hash, 120 rows, rows 113 on citing the brief's items 1 to 5 and D-68; no rule failure; §5's table equal to a fresh generation; in the specimen's stylesheet every control boundary in `border.control`, every latched form with a `pressed.ink` boundary, none in `border.strong`; no chosen filter chip on a status fill; no figure stroke in `border.strong` | `a7ca5882507c647183fbf0428c14b547f860c8f7ffa5a533564e5db6cc9e30b0` |
| `tools/render.mjs` | measures, as the browser resolves them, what identifies every control sample against its own fill and the surface around it (boundaries, the primary and the checked fills, switch tracks and thumbs, the splitter's grips, the compass's strokes) and the ink of every disabled sample against its fill; exits 1 when a reading is under 3:1, a boundary resolves to `border.strong`, or a disabled ink is under the stated ratio | `f43ba4d27f1b61ac06da82697a5e674443d2ff5c02d1a052aafb53fa8dd69661` |
| `RETURN.md` | this section; the table in §2 stands as it was at V1.3 | |

**What I ran**, from this directory, all after the last edit (`<out>` is a scratch directory
outside the repository):

1. `node tools/palette.mjs --write <out>/tokens.json` and `cmp` with `tokens.json`: equal
   byte for byte. The categorical validator is not supplied, as before; the result ramp and
   the categorical set are unchanged.
2. `node tools/contrast.mjs tokens.json <out>/contrast_table.md`: 214 pairs; control rule
   29 sweep rows, 21 held, lowest 3.17:1 light and 3.14:1 dark; disabled ink 7 rows, lowest
   2.56:1 light and 3.02:1 dark; rule failures 0; exit 0.
3. `node tools/gen.mjs tokens.json <out>/gen`, then
   `node tools/splice.mjs <out>/gen specimen.html DESIGN_SYSTEM_V1.md`; a second splice
   leaves both files byte-identical.
4. `node tools/agree.mjs DESIGN_SYSTEM_V1.md tokens.json specimen.html`: `problems: []`; 100
   colour tokens, 99 plain tokens, 214 contrast rows and pairs, 28 label chips, 120
   change-log rows. I ran it against copies with fourteen faults injected, one at a time (a
   boundary token at `border.strong`'s value, the disabled ink at 1.2's value and then onto
   the muted ink, a button and a switch track in `border.strong`, a latched toggle with no
   boundary, a compass button stroked in `border.strong`, a chosen chip on a status fill,
   the outline's row without its bar, a V1.3 heading, a word changed in row 100, a reading
   changed in §5's table, row 118 without its citation, a value changed in §2.9's table):
   it named each, and the unmodified files pass.
5. `node tools/render.mjs specimen.html <shots>`, where `<shots>` is
   `../../../HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/DESIGN-SYSTEM-05/shots`:
   Chromium, every request that is not the file blocked, no server and no port; 1440 and
   720 wide, light and dark by system preference and by the manual switch; exit 0. In all
   four: no request attempted, no console error or warning, no horizontal overflow,
   smallest font 11 px, 100 token rows, 214 contrast rows, and every V1.1 to V1.3 fact as
   it was. The V1.4 facts: 317 readings of what identifies a control, the lowest 3.16:1 in
   both themes (a pressed combobox in light, a pressed raised button in dark), none under
   3:1, no boundary resolving to `border.strong`; 24 disabled samples, the lowest 2.56:1 in
   light and 3.02:1 in dark, none under the stated ratio. The browser's 3.16:1 against the
   tool's 3.17:1 and 3.14:1 is rounding: the tool rounds a composited wash to whole channel
   values, as V1.3 did, and the render check does not. The same tool run on V1.3's specimen
   reports 128 of 160 readings under 3:1, 120 of them boundaries in `border.strong`, and
   disabled ink at 1.94:1 and 2.16:1. I read the screenshots of sections 1, 5, 9, 10 and 11
   in both themes and fixed what they showed: a cell of the new strip took the data bar's
   width because it shared the class name `bar`; the Borders sample's third line wrapped
   away from its name; the render check read a checked box's boundary against its own
   fill.
6. `git status` and `git diff --stat`, read-only: changes in this directory and the
   instance folder only. I ran no state-changing git command, started no server, and ran no
   product build or test.

Scratch output is under the instance folder's `scratch/`: the V1.3 and V1.4 readings of the
same pairs and the options table, the token diff, the injected-fault run, the render tool's
readings of V1.3's specimen, the frames scan, and the three scripts that produced them.

**The frames that draw a control boundary in `border.strong`**, for a later frames pass.
In `../MOCKS/frames/mocks.css` nineteen rules use `border.strong`. Thirteen selectors, twelve
rules counting the switch's two as one, draw a control's boundary and move: `.seg`, `.btn`,
`.input`, `.combo`, `.switch i` with `.tblhead .switch.off i`, `.search`, `.lenfield`,
`.tabs .tab.on`, `.maprow .m .sel`, `.pop .row .k`, `.iconbtn.raised`, `.sendrow`. Six frame a
region and stay: `.stage`, `.lights i`, `.bar b`, `.expand .block`, `.card .asked`,
`.content .live`. By frame (counts are occurrences in the markup; `index.html` draws none):

- Every one of the eighteen stage frames: `.seg` twice, bordered `.btn` (5 to 12), `.combo`
  (1 to 4), `.search` once.
- `.tabs .tab.on`: every stage frame except `s9_table_dark` and `s9_table_light`.
- The off switch's track: `s7_both_dark`, `s7_both_light`, `s7_both_light_historical`.
- `.input`: `s7_table_light`. `.pop .row .k`, three empty boxes that move and two checked
  that keep their form: `s7_table_light`.
- `.lenfield` and three `.iconbtn.raised`: `s2_model_dark`, `s2_model_light`.
- `.maprow .m .sel` (11): `s3_table_light`. `.sendrow`: `s4_both_light_slideover`,
  `s8_table_light`.

The other forms V1.4 changes, which the same pass would follow: the view switch's active
segment gains its boundary (`.seg [aria-pressed="true"]` and the mock bar's, every stage
frame); `.btn.latched` gains the `pressed.ink` boundary (`s4_both_light`,
`s4_both_light_column`, `s4_both_light_slideover` twice, `s8_table_light`), as do the latched
HUD tool (`s2_model_dark`, `s2_model_light`, `s7_both_dark`, `s7_both_light`) and `.iconbtn.on`
(`s7_both_light_historical`); `.chip.outline.on` takes the latched form in place of the
selection band (`s6_both_light`, `s9_table_dark`, `s9_table_light`); the agent column's active
tab takes the tab's form (`s4_both_light_slideover`, `s8_table_light`); `.outline div.on` gains
the bar (`s9_table_dark`, `s9_table_light`); and the disabled ink comes with 1.3. The frames
have no hover rule, and draw no splitter grip and no drag handle.

**What did not apply cleanly, uncertainties, and what I saw and did not change:**

1. The criterion is about what is needed to identify a control. Where a control has a
   visible label, a strict reading could put its boundary outside the criterion too. I held
   every boundary of a field and of a bordered button to the rule: a field has nothing else
   that says where it is, and the first slice's check measures a button's boundary.
2. The anatomy added here is the least the sweep needed and is mine, open to replacement:
   the splitter's grip and its size, the tab's form in the agent column, the latched
   boundary, the active segment's boundary, the latched form for a chip that is on, the
   offers' ink. "Changed since: Run 03" is drawn latched in the specimen on my reading that
   a set comparison is on. The specimen draws the drag handle as six dots; §3.2 has no
   drag-handle glyph and no lock glyph, and I did not add to §3.2.
3. The latched and unlatched forms differ mainly by hue; the open panel, and for a tool the
   hint strip, also say which is on. That is success criterion 1.4.1's question and outside
   this pass.
4. Text is outside this pass: the labels in `text.muted` that belong to controls read
   3.53:1 and 4.70:1 (the palette field's placeholder, on `surface.sunken`) and 3.79:1 and
   4.41:1 ("Add row", on the panel), and wait for the text target.
   §12 of the specimen keeps the product's sentence "Findings only. No conformance is
   claimed; the target is set by the project authority."; the page's own footer now says
   that two rules are held.
5. Target size is outside this pass: the 22 px icon buttons and the 16 px check box are
   under the 24 px the product's check asks of a target unless the cell or the row is the
   target.
6. The select-all control draws nothing; whether it needs a drawn form is the pointer
   rule's question. Column resize handles have no drawn form in this system. The Run
   button's progress fill is not a token; the stop glyph and the run log carry that state.
7. The review of the first slice found (its F2) that one variable of the product draws both
   the hairlines and three frames that §1.2 assigns to `border.strong`; splitting it is the
   product's work, and V1.4 keeps `border.strong` for exactly such frames.
   `status.solvedFill` equals `surface.base` in light, which is why a chip on it has no
   edge there; it informs and is outside the rule.
8. The specimen's text button takes no wash, as at V1.3, because its transparent fill
   follows the hover rule in the stylesheet; I left it, since it is not a boundary or a
   state carrier.
9. `tools/render.mjs` now imports `rules` from `tools/contrast.mjs`, so the two hold the
   same ratios; its readings cover the specimen's samples, not the product.

Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
