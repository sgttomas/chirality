# DS5-REVIEW: independent read-only review of design system V1.4 (candidate 9b0e12b0d) — retained return

Retained by ROOT. What follows is the child's final message as the host stored it, with the machine's repository path replaced by `{REPO_ROOT}`; nothing else is changed.

---

I have everything I need. Here is my return.

---

# DS5-REVIEW return

**Model: Claude Opus 5** (`claude-opus-5[1m]`). TASK, Type 2, read-only, fresh context, working alone; I delegated nothing and launched no agent.

Brief hash confirmed: `shasum -a 256` on `{RUN}/lanes/DESIGN-SYSTEM-05/briefs/DS5-REVIEW_independent_review.md` gives `d2ab26f0b484f94b086e3a9059cef6900e92d15e1bda261b4d44a536dad19fcb`, equal to the sealed value. I read the brief whole before touching the candidate.

## Verdict: FINDINGS — one minor, one trivial. Neither blocks the merge.

Every substantive check passes. All 214 published ratios and all 56 numbers in the §5 sweep reproduce under arithmetic I wrote myself; the token diff is the three changes claimed and no more; `cssFrom`'s output for the 1.2 token set is byte-identical, so the product's copy is untouched; change-log rows 1–112 are byte-identical; both tools run clean and the working tree is unchanged by my run. The two findings are about what the document *says*, not what it *measures*.

---

## ROOT's question, settled

> §2.9 lists seven disabled pairs and neither `selection.band` nor `canvas.bg`.

**Neither pair belongs, on the design as written.** My arithmetic confirms ROOT's figures exactly — `text.disabled` reads 2.60:1 (light) / 2.55:1 (dark) on `selection.band` and 2.60:1 / 4.01:1 on `canvas.bg` — but §1.3 and §5 do not draw a disabled label or glyph on either:

- **`canvas.bg`.** Nothing disabled is drawn on the canvas. §5.6 puts the HUD "on `surface.raised` at elevation 1", so the two tools the run-standing table disables (Deformation and Probe, "Needs a current run", §5.1 and §6.7) are `text.disabled` on `surface.raised` = **3.06:1 / 3.02:1**, which §2.9 lists and which is exactly the dark lowest the sweep states. The compass's raised icon buttons, the probe card and the legend are `surface.raised` too.
- **`selection.band` and the hovered row.** A disabled control that has a fill sits on `disabled.fill`, which is opaque: I measured `disabled.fill` composited over `selection.band` and the ratio is **2.56:1 / 3.19:1**, identical to `disabled.fill` alone, so a band behind it never shows through. A disabled control with no fill is, by §1.3's list, a rail item (`surface.base`), a HUD tool or menu item (`surface.raised`), or an icon-only button (`surface.panel` / `base` / `header` / `raised`) — all seven listed. And §1.3 states a disabled control "takes neither wash", which removes every hover and pressed pair.

So the stated dark rule ("3:1 or better in dark on everything it is drawn on") is **not** falsified. It does, however, rest on reading §1.3's four-item list as closed — which is what finding 1 asks the document to make explicit.

---

## Findings

### Finding 1 — minor, actionable before merge

**Where:** `{DS}/DESIGN_SYSTEM_V1.md` line 873 (§5.1 cell-state table); `{DS}/specimen.html` lines 796 and 1282.

**What is wrong.** §5.1's cell-state table gives the Disabled state as "`text.disabled`; never used in the layout table" and names no fill — where its sibling states name theirs ("Read-through … on `surface.sunken`", "Editing … on `surface.panel`", "Selected … `selection.band` across the row"). §1.3 supplies `disabled.fill` for a control that has a fill, and the bare ink for "a control with no fill of its own (a rail item, a HUD tool, a menu item, an icon-only button)" — a list that names neither a cell nor a row. The line is pre-existing (unchanged from V1.3), but V1.4 is the revision that turns it into a stated ratio, so it now carries weight it did not carry before.

**Evidence.** The specimen resolves it two ways. `.rowdemo .dis` (line 796) gives a disabled row `color: text.disabled; background: disabled.fill` — and the light screenshot shows "row · disabled" on that fill. But the Candidate sizes table inside the hanger-selection expansion (line 1282) draws row A-05's six cells in `text.disabled` inline with **no fill**, on the row surface. `render.mjs`'s disabled sampler selects `.btn[disabled], .btn.disabled, .combo.disabled, .iconbtn[disabled], .hud button[disabled], .menu .mi.dis, .rail .it.off` — 24 samples — so that row is not among them, and the "0 under the stated ratio" result does not cover it.

As actually drawn the row is an odd row, so `surface.panel`: **3.06:1 / 3.46:1**, within the stated ratio. On `surface.rowAlt` it would be 2.92:1 / 3.37:1, also within it. The rule only fails if such a row can also be selected (2.60:1 / **2.55:1**) or proposed (2.67:1 / **2.87:1**).

**Smallest correction.** One clause in the cell-state table's Disabled row saying what the cell sits on — either "on `disabled.fill`", matching §1.3 and `.rowdemo .dis`, or "the ink on the row surface, never on a band". If the second, make the specimen's A-05 row and `.rowdemo .dis` agree, and add `.ds td[style*="text-disabled"]`-equivalent samples to `render.mjs`'s disabled selector so the check covers the cell state.

### Finding 2 — trivial, not actionable before merge (an observation)

**Where:** `{DS}/DESIGN_SYSTEM_V1.md` §2.9 findings prose and the §5 control rule.

The rule's stated scope is "against everything it sits on … at rest and under the hover and pressed washes". The pair list carries the washes over `surface.panel`, `surface.sunken` and `surface.raised` only — the three fills a bordered control actually has. `border.control` under a pressed wash over `surface.base` measures **2.99:1** in light (4.13:1 dark), a hair under 3:1. I could find no control this reaches: the toolbar band and status bar are `surface.base`, but nothing on them draws a `border.control` boundary over `surface.base` itself — the view switch's segments wash over `surface.panel` / `surface.sunken`, Undo/Redo and the About control carry only an ornamental hairline, Run is `accent.fill`, and the Agent and Inspector toggles latch in `pressed.ink`. Correction, if wanted: one clause in §2.9 saying the wash pairs are the control's own fills, so a later reader need not re-derive it.

---

## My computed ratios

Written independently (`wcag.mjs` in a `mktemp -d` outside the repository), sanity-checked against published values first: black/white 21.00, `#767676` on white 4.54, `#949494` on white 3.03, `#0000ff` on white 8.59.

**The disabled ink** (the seven §2.9 lists, then what ROOT asked about):

| `text.disabled` on | Light | Dark | Listed? |
|---|---|---|---|
| `surface.panel` | 3.06 | 3.46 | yes |
| `surface.base` | 2.68 | 3.92 | yes |
| `surface.sunken` | 2.85 | 3.69 | yes |
| `surface.header` | 2.74 | 3.25 | yes |
| `surface.raised` | 3.06 | **3.02** | yes (dark lowest) |
| `surface.rowAlt` | 2.92 | 3.37 | yes |
| `disabled.fill` | **2.56** | 3.19 | yes (light lowest) |
| `disabled.fill` over `selection.band` | 2.56 | 3.19 | n/a — fill is opaque |
| `selection.band` | 2.60 | 2.55 | no — not drawn there |
| `canvas.bg` | 2.60 | 4.01 | no — HUD is `surface.raised` |
| beside `text.muted` | 1.24 | 1.27 | yes |
| beside `text.secondary` | 2.05 | 2.00 | yes |

**The control boundary** (`border.control`, every surface and fill a control sits on):

| Background | Light | Dark |
|---|---|---|
| `surface.panel` / `raised` | 4.11 | 4.95 / 4.32 |
| `surface.base` | 3.60 | 5.60 |
| `surface.sunken` | 3.83 | 5.28 |
| `surface.header` | 3.69 | 4.64 |
| `surface.rowAlt` | 3.93 | 4.82 |
| `selection.band` | **3.50** | 3.64 |
| `proposal.band` / `stale.band` | 3.59 / 3.83 | 4.11 / 4.58 |
| `canvas.bg` | 3.50 | 5.73 |
| `disabled.fill` | 3.44 | 4.57 |
| `hover.wash/*` (panel, sunken, raised) | 3.68 / 3.41 / 3.68 | 4.12 / 4.44 / 3.60 |
| `pressed.wash/*` (panel, sunken, raised) | 3.39 / **3.17** / 3.39 | 3.60 / 3.88 / **3.14** |
| `pressed.wash/surface.base` (unlisted) | *2.99* | 4.13 |

Every figure the document states for these pairs is mine to 0.00. The document's "lowest anywhere is 3.17:1 in light, on a pressed field, and 3.14:1 in dark, on a pressed raised button" is correct.

**Check 8's specific ask — the lifted ink beside the muted ink.** `text.disabled` vs `text.muted` reads **1.24:1 (light) and 1.27:1 (dark)**; against `surface.panel` the two read 3.06:1 / 3.46:1 and 3.79:1 / 4.41:1 respectively. The order disabled < muted < secondary holds in both themes, and the screenshots bear it out: in the specimen's Disabled block each disabled control reads plainly weaker than the "muted text beside it" sample and than "an enabled glyph's ink", in both themes, and nothing reads as enabled. `text.muted` is itself 3.17:1 on `disabled.fill`, which is the document's stated reason for stopping at 2.5:1 in light — I reproduce that figure.

---

## Check-by-check

1. **Scope — pass.** 31 paths. Ten under `{DS}`, seventeen under `{RUN}/instances/DESIGN-SYSTEM-05`, four under `{RUN}/lanes/DESIGN-SYSTEM-05`, three shared records (`briefs/_INDEX.md`, `WORK_GRAPH.json`, `HANDOFF_STATE.md`). Nothing under `apps/**`, `core/**`, root `docs/**` or root `tools/**`; nothing under `{DESIGN}/instances/MOCKS` or `UX-SPEC`. The work is design records and their tools only.
2. **Token diff — pass.** Version 1.2 → 1.3; `text.disabled` `#a6abb1`→`#8f949a` (light) and `#5f6469`→`#767b80` (dark); `border.control` added at `#777e85` / `#90969c`, carrying both themes and following `border.hairline` / `border.strong` / `border.focus`; the plain width `border.control: 1` added beside `strong`; the note extended. No other colour value differs — I diffed the whole file. Claims verified: 152→214 pairs (+62); colour tokens 99→100; the OKLCH apartness (0.055 light, 0.06 dark) reads straight off `palette.mjs`'s specification.
3. **Arithmetic — pass, with ROOT's question answered above.** All 214 contrast rows and all 56 numeric cells of the sweep reproduce within 0.05 under the tool's compositing convention (8-bit rounded channels). Under fractional compositing exactly one row differs, by 0.06: `canvas.label` on `canvas.labelBg/canvas.bg`, doc 13.58 vs mine 13.52 in dark. That is a rounding convention on a translucent composite, not an error — rounding to a channel is arguably the more faithful model of what is rendered — and it is a pre-existing 13:1 text row that V1.4 did not touch. No figure I could find is wrong by more than that.
4. **Sweep complete and honest — pass, with finding 2.** I re-derived it: 29 rows, 21 held, 8 outside, each of the 8 with a reason I accept (a fill that is not its state's carrier, where the table names the carrier; hairlines and frames that identify nothing; the display-only dashed frame; the select-all cell, which draws nothing; the disabled control, which 1.4.11 exempts). Crucially, no input's boundary hides behind an exemption — every field, combobox, stepper, search and send row is held to the rule, which is the right call. I also swept each sweep token against every plausible background: the only sub-3:1 results outside the listed set are `border.control` on `pressed.wash/surface.base` (finding 2), and `text.muted` / `mark.origin` / `accent.fill` on a *washed band* — which the V1.4 rule change forecloses. Change-log row 116's supporting numbers verify exactly (the origin glyph would have been 2.89:1 / 2.71:1 with the wash; it is 3.23:1 / 3.24:1 on the band alone). Every remaining `border.strong` use I inspected frames a region or is specimen illustration chrome (`.tblwrap`, `.expand .block`, `.shell`, `.geo`, `.lights i`, `.splitdemo`, `.radii div`, `.rowdemo`, `.cbox`) — none identifies a component, and `agree.mjs` now enforces that no control selector draws in it.
5. **Generated content is generated — pass.** `node tools/contrast.mjs tokens.json <temp>` exits 0: 214 pairs, 29 sweep rows, 21 held, lowest held 3.17 light / 3.14 dark, **rule failures: 0**. `node tools/agree.mjs DESIGN_SYSTEM_V1.md tokens.json specimen.html` exits 0 with `"problems": []`. Neither wrote in the repository: `git status --short` was empty before and after. The §2.9 block is **byte-identical** to the tool's output. The §5 sweep block I verified numerically cell by cell and by `agree.mjs`'s own equality test against a fresh `toSweepMarkdown`.
6. **The tools as code — pass.** `lum`, `ratio`, `over`, `hex2rgb`, `parseColor` and `resolve` are byte-identical to `origin/main`; the formula is WCAG's. **Zero pairs dropped** (152 → 214 is pure addition); running the old and new tools over the same token set, **zero existing pairs changed value**. Two role labels changed text only (`border.strong` "border" → "frame"). No threshold was lowered — `rules = {control: 3, disabledLight: 2.5, disabledDark: 3, disabledApart: 1.2}` is new, since V1.3 was findings-only. **On the product's question: `cssFrom`'s source is byte-identical and its output for the 1.2 token set is byte-identical (12 235 bytes both ways), so the product's copy at its recorded hash needs no change and re-running the new generator against 1.2 emits exactly what it emits today.** `colourTablesFrom` and `labelTableFrom` are likewise unchanged for 1.2. When the product does adopt 1.3, the delta is only the version comment, `--border-width-control: 1px`, and the two changed/added colour variables in each theme block.
7. **History and rulings preserved — pass.** Change-log rows 1–112 are byte-identical to `origin/main` (I compared them directly, not only via the tool's pinned hash); the only §9 edits are the extended heading and rows 113–120. Section-by-section, §0, §3, §6 and **§7 (the copy rules) are untouched**; §4's one edit merely names `text.muted` for the two offers. Names, labels, the six functions and the tooltip form all stand. §8 item 6 is restated exactly as required: the control rule settled on D-68, the disabled ink "ROOT's to decide and open to the owner", the text target and canvas pairs still open.
8. **The disabled ink — pass.** Measurements correct (table above). The document calls it "this revision's recommendation, which ROOT decides and the owner may reopen"; the return presents it as a recommendation with a four-option comparison table whose every figure I reproduced exactly; `{RUN}/lanes/DESIGN-SYSTEM-05/HANDOFF.md` records DS5-D1 as ROOT's decision, states its reasons, and says in terms "It is not the owner's ruling, and the owner may reopen it." Nothing anywhere presents it as the owner's ruling or as a conformance requirement — §2.9 says "the criterion exempts an inactive control, so this is a design decision and not a conformance one", and both specimen footers read "No conformance is claimed and no target is named for text."
9. **The specimen — pass.** I opened all four screenshots. Section 1 at 1440 in both themes shows the new Controls panel with one strip per surface (`panel`, `base`, `sunken`, `header`, `raised`, a band strip, `canvas.bg`): fields, comboboxes, steppers, bordered buttons, the segmented switch with its active segment boundary, tabs, check boxes, radios and switch tracks all carry a plainly visible boundary on every strip, in both themes; the splitter grip reads; the disabled block shows the ink, the fill, the dropped hairline boundary and the muted-text comparison on four surfaces, and nothing in it reads as enabled. Section 12 shows the live-computed findings at 214 pairings agreeing with the document. `report.json`: 317 control readings per rendering, **0 under 3:1, 0 boundaries still resolving to `border.strong`**, 24 disabled samples with 0 under the stated ratio, 0 blocked requests and 0 console issues, at both 1440 and 720. Its lowest reading of 3.16 vs the tool's 3.17/3.14 is the same compositing-rounding difference I found in check 3, and the return says so.
10. **Records and copy — pass.** The run index row's brief hash `322ca33b…c5e7c11` matches the file; the retained return's `0f324a14…c25b34` matches the file and `WORK_GRAPH.json`; all three JSON files parse; all ten file hashes the return lists match the files on disk. No absolute machine path in any changed file. Every governed record ends with the claim fence; the two scratch `.md` files do not, which matches the precedent for scratch material elsewhere in the repository and is not a defect. "Accept" is the control; `Approve`, `certify`, `compliant` and `sign-off` appear only inside §7.1's forbidden-words table, in the "never" column. Canadian spelling holds — the only `Analyze` is §7.1's own ruled product spelling, and the two `normalized` are pre-existing lines this candidate did not add.

---

## What I did not check

- I ran only `contrast.mjs` and `agree.mjs`, as the brief allowed. I did **not** run `gen.mjs`, `palette.mjs`, `splice.mjs` or `render.mjs`, and no build, test, Playwright or dev server. So I did not independently regenerate the §2.2 colour tables or the §5 sweep *block*; I verified §2.9 byte-for-byte against `contrast.mjs`'s own output, verified all 56 sweep numbers by my own arithmetic, and relied on `agree.mjs`'s `problems: []` for the sweep block's byte equality and for the §2.2/label-table equalities.
- I did not re-render the specimen or verify the render harness's browser measurements myself; I read the four retained screenshots and `report.json`, not the other 48 PNGs.
- I did not open `{DESIGN}/instances/MOCKS/frames/mocks.css`, so the return's frames scan (19 rules, 13 to move, 6 to stay) is unverified — it is outside the candidate and a later pass's input.
- I did not audit the three scratch scripts for correctness beyond reading their recorded output, and I did not re-run the injected-fault exercise.
- I did not look at the product's copy of `tokens.json` or its recorded hash, beyond establishing that `cssFrom` makes that copy safe.
- I ran no state-changing git command and made no edit; all my scratch arithmetic lived in a `mktemp -d` outside the repository, and the working tree is exactly as I found it.

Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
