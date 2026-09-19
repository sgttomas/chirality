# DESIGN-SYSTEM-05: correction 1 to design system V1.4 (the independent review's two findings) — retained return

Retained by ROOT. What follows is the child's final message as the host stored it, with the machine's repository path replaced by `{REPO_ROOT}`; nothing else is changed.

---

# DESIGN-SYSTEM-05 · correction 1 to V1.4 · return

Both findings are corrected. Both tools and the render check run clean, and my change to `tools/contrast.mjs` renames one sweep row and changes no pair or ratio.

- **Limits.** `tokens.json` is unchanged (SHA-256 `0e01828c4e7739313a47b5f71ac3c9fa3cf21aae3d07648eadc805fd82d18c00`). Change-log rows 1 to 120 are byte-identical to HEAD (row hash `d79d46b07122251a6d455c891cc9fc00fefa1f34e821b706f051e8221e0d2bde`). The revision stays V1.4, and the correction is rows 121 to 123. I did not touch §7, the owner's rulings or §8 item 6.
- **Process.** I worked alone and delegated nothing. I ran no state-changing git command, started no server, and ran no product build or test. I verified both sealed files' hashes before acting and read the reviewer's return whole.
- **Interruptions.** ROOT paused the work once. One context compaction occurred after my last edit to the document, specimen and tools, and after the render check. After it I re-ran palette, contrast, gen, splice, agree and the render check from the files on disk. The retained `report.json` and the four retained screenshots are byte-identical to that re-run.
- **Model:** Claude Fable 5.1 (`claude-fable-5-1`).

## Finding 1, decided: the Disabled state is a whole row's, the ink on the row surface

§5.1's Disabled row now reads: "`text.disabled` on the row surface and nothing else; the state is a whole row's, for a row that cannot be chosen (a size the hanger selection cannot offer, below), which is never selected, carries no proposal and takes no wash, and gives its reason in its own text or in a tooltip (§1.3; correction 1 to V1.4); never used in the layout table".

Why, in the design's terms:

- **A cell has no fill of its own.** The Entered state is the ink on the row surface, and the sibling states that have a fill name it. By §1.3's own division a disabled cell is therefore a control with no fill, and it takes the bare ink.
- **The frames already draw it so.** The hanger selection's sizes that cannot be offered use `table.ds tr.offrow`, ink only, in `s8_table_light`. That is the one place the design uses the state.
- **A fill across a row is a band in this system.** A `disabled.fill` row would read as a third band.
- **The reason is read in the row, and it reads better there.** The ink reads 3.06:1 light / 3.46:1 dark on `surface.panel` and 2.92:1 / 3.37:1 on `surface.rowAlt`, against 2.56:1 / 3.19:1 on `disabled.fill`.
- **The design does not need such a row to be selected.** The sizes are library rows in a table with no gutter, no proposal lands on a library row, and an eligible row's one control is its "Select" text button.
- **The pair list does not change.** Both backgrounds the statement allows are already rows of §2.9's disabled pairs, and both are within the stated ratio by the tool's measurement. `tools/contrast.mjs` changed only in the name of one sweep row.
- **What the statement excludes would fall short.** On `selection.band` the ink reads 2.60:1 / 2.55:1, and on `proposal.band` 2.67:1 / 2.87:1. On a hovered panel row it reads 2.73:1 / 2.88:1, and on a hovered `surface.rowAlt` row 2.61:1 / 2.80:1.

**§1.3's list of controls with no fill is now stated as closed,** with what each kind sits on:

- a rail item, on `surface.base`;
- a HUD tool and a menu item, on `surface.raised`;
- an icon-only button, on its region's surface, or inside a field on the field's `surface.sunken`;
- a table row that cannot be chosen, on the row surface.

**§2.9 now says itself** that the disabled ink meets `disabled.fill` and the six surfaces it pairs with `text.disabled`, and never a band, a wash or the canvas.

**The specimen agrees in both places.**

- `.rowdemo .dis` loses its fill.
- The A-05 row takes one `table.ds tr.offrow` rule in place of inline styles.
- The Disabled strip gains rows that cannot be chosen, on both row surfaces.

## Finding 2, decided: a rule, and the tools hold it

A control that carries the boundary and is washed has a fill of its own, and the wash is drawn over that fill, never over the bare surface of its region. The fills are three:

| Fill | Controls |
|---|---|
| `surface.panel` | a bordered button |
| `surface.sunken` | a text field; a combobox, or a menu button in the combobox's form; a stepper; the palette field; the agent's input row; a mapping select; the segmented control's trough |
| `surface.raised` | a raised icon button on the canvas; the compass's length field |

It is a rule and not only a statement of scope. §1.3 lets a wash be drawn over a surface, and the control rule holds under the washes. On a washed `surface.base` the pressed boundary would read 2.99:1 in light, and on a washed canvas 2.91:1.

- The active tab and the active segment keep their state fill under the pointer.
- An empty check box, a radio button, a switch's track and a splitter's grip are not washed themselves. A wash around one of them is the row's or the menu item's.
- Holding the rule was cheap, so both tools now fail on its breach: `tools/agree.mjs` reads the stylesheet, and the render check reads resolved styles.
- One control of the specimen breached it. The stepper had no fill, and it now takes `surface.sunken`, as every field does.

The clause is in §2.9's control-boundary finding, and the rule is a new bullet of §5's control rule.

## Files changed

All are under `{DESIGN}/instances/DESIGN-SYSTEM/`.

| File | SHA-256 |
|---|---|
| `DESIGN_SYSTEM_V1.md` | `447031fa0db2db3967686b538f2dd62f433937c376e107d07245d7ac23af76f0` |
| `specimen.html` | `2f09f63dc39b4b4d4ed847c5cadf634c52d8320eeb92247582233fdf2628fdf1` |
| `tools/contrast.mjs` | `89ee8f98335d6161bc3707d76f6381a58c3cb268544331a92f326f0551ba4fac` |
| `tools/agree.mjs` | `e01f7c92f36e1d619f25f42fd06cd428a29ff832cb4f0f865b41cc66ec09d06b` |
| `tools/render.mjs` | `1583cda6a1632623ac45316890e8d122de68d4aa3e3a4da48e899f8aafd46ae0` |
| `RETURN.md` (new §12, plus one sentence of the head) | `a7ae690b00af3ab47818add0b2c4b9edf8d73b08d981ee7a7c8c8debc5fe8a69` |

`tokens.json`, `tools/palette.mjs`, `tools/gen.mjs` and `tools/splice.mjs` are unchanged.

What changed in the document and the tools:

- **`DESIGN_SYSTEM_V1.md`:**
  - the status line;
  - §1.3, §2.9 (two findings), §5 (the new bullet) and §5.1 (the Disabled state; the hanger selection names it);
  - §8, three sentences for a later frames pass;
  - §9, the introduction and rows 121 to 123;
  - the generated sweep row, renamed through the tools.
- **`tools/agree.mjs`:**
  - pins rows 1 to 120 by hash, requires 123 rows, and requires rows 121 on to cite correction 1 and each finding in their Source cell;
  - checks the Disabled state's wording;
  - checks the disabled-row rule: no fill, no inline-styled disabled cell, no disabled row on a band;
  - checks that each washed control has one of the three fills.
- **`tools/render.mjs`:**
  - counts disabled cells apart from disabled controls, and holds them to the stated ratio and to the row surface;
  - holds every washed control to an opaque fill of its own among the three;
  - exits 1 on a breach, or when no disabled cell is sampled.

Under `{RUN}/instances/DESIGN-SYSTEM-05/`, by SHA-256:

- `shots/report.json`: `7762ba27fe1fdace2553ab475e5c56fed0d47c777d3236fb5ecc1d36a806bfa4`
- `shots/1440-light-s1.png`: `1c9644f1c4d124f038f26b48fe5f0d4fb5ba83e5caf57a778d7f211308558900`
- `shots/1440-dark-s1.png`: `da9c9bb3758ed0727ba782fae78560bf98c0c97d57a16bd683e97bf9952543dd`
- `shots/1440-light-s8.png` (new): `c02b5572162661ccb8dd43f321a32e5a36a97e96971b8f147dbff4669fae95a9`
- `shots/1440-dark-s8.png` (new): `a4398b77319d11373557aa435b72f16373f12e9359020ce4699421de9c80beaa`
- `scratch/correction_1_checks.txt` (new): `c7f5c9879d4c2f96b61030b37c4af95bc969fb95f2c96e87bc97acb1c03b02bd`
- `scratch/scripts/faults_correction_1.mjs` (new): `223ee27301680cc9d569e7a795afe23afee45d4f89d691c53eaa9199ac6bc7bb`
- `scratch/scripts/pixdiff.py` (new): `1570d428151129cd8f157c4b9ab14457fc145fc1a9f06ad1bb9cd4703fb0946f`
- `scratch/scripts/probe_pairs.mjs` (new): `d5b55c9f139acad1171109ea1c3303d929ddc1592503d27f1477ee8a4ef078b4`

**For ROOT at commit:** `shots/1440-light-s12.png` and `shots/1440-dark-s12.png` are deleted from the working tree, because that section's pixels do not change. They show as `D` in `git status`. The committed copies remain in history if ROOT prefers to keep them.

Read-only `git status` shows nothing modified outside the two folders. A grep of both folders finds no machine path.

## The two tools' output

`node tools/contrast.mjs tokens.json <tmp>/contrast_table.md` exits 0:

```
pairs: 214
lowest (min of the two themes):
  canvas.edge on result.scale.6 [edge line on the step nearest its own lightness in light]  light 1.02  dark 1.35
  result.scale.1 on canvas.unsolved [result scale beside unsolved]  light 1.02  dark 1.83
  bar.track on selection.band [bar track]  light 1.10  dark 1.04
  canvas.edgeAlt on canvas.bg [alternate edge against the ground]  light 1.05  dark 1.25
  surface.panel on surface.sunken [segment fill on the trough]  light 1.07  dark 1.07
  canvas.edge on result.scale.7 [edge line on the brightest step]  light 1.29  dark 1.10
  pressed.fill on surface.base [latched toggle fill]  light 1.11  dark 1.82
  canvas.gridMinor on canvas.bg [hairline]  light 1.12  dark 1.12
  canvas.glyphFill on canvas.bg [canvas mark]  light 1.15  dark 1.45
  selection.band on surface.panel [band on the panel]  light 1.17  dark 1.36
  text.disabled on text.muted [disabled ink beside muted ink]  light 1.24  dark 1.27
  border.hairline on surface.base [hairline]  light 1.25  dark 1.55
  bar.track on surface.panel [bar track]  light 1.29  dark 1.42
  canvas.gridMajor on canvas.bg [hairline]  light 1.31  dark 1.31
  result.scale.1 on bar.track [data bar on its track]  light 1.84  dark 1.33
  border.hairline on surface.panel [hairline]  light 1.43  dark 1.37
text pairings: 69 | lowest text light: 2.56 dark: 3.02
control rule (3:1): sweep rows 29 | held to the rule 21 | outside it 8 | lowest held light: 3.17 dark: 3.14
disabled ink (2.5:1 light, 3:1 dark): rows 7 | lowest light: 2.56 dark: 3.02
rule failures: 0
```

`node tools/agree.mjs DESIGN_SYSTEM_V1.md tokens.json specimen.html` exits 0. I ran it after the last edit to `RETURN.md`:

```
{"colourTokens":100,"labels":8,"labelChips":28,"agentCardClasses":5,"changeLogRows":123,"plainTokens":99,"docColourRows":100,"contrastRows":214,"pairs":214,"problems":[],"sha256":{"tokens":"0e01828c…d18c00","doc":"447031fa…af76f0","specimen":"2f09f63d…28fdf1"},"bytes":{"doc":251559,"specimen":225271,"tokens":14182}}
```

The rest of the chain is also clean:

- `palette.mjs --write` reproduces `tokens.json` byte for byte.
- `gen.mjs` then `splice.mjs` leave the document and the specimen byte-identical.
- The correction-1 fault script has `agree.mjs` name all ten injected faults, and the unmodified files pass.
- V1.4's fault script still catches its fourteen faults. Two of them, in rows 100 and 118, now also trip the pin of rows 1 to 120.

## The render check's counts

`node tools/render.mjs specimen.html <tmp>` exits 0. It uses Chromium, with every non-file request blocked, no server and no port. The counts are identical in all four renderings (1440 and 720 px, light and dark):

| Count | Reading |
|---|---|
| Control readings | 317; lowest 3.16:1 (a pressed combobox on its own fill in light; a raised icon button on its own fill in dark); 0 under 3:1; 0 boundaries in `border.strong` |
| Disabled controls | 24 samples; lowest 2.56:1 against the stated 2.5:1 in light, 3.02:1 against the stated 3:1 in dark; 0 under the stated ratio |
| Disabled cells, counted apart | 13 (A-05's six cells, the strip's two rows' six cells, and the row demo); lowest 2.92:1 light and 3.37:1 dark, both on `surface.rowAlt`; 0 under the stated ratio; 0 off the row surface |
| Washed controls | 87; 0 without a fill of their own among the three |
| Blocked requests | 0 |
| Console issues | 0 |

There is no overflow, and the smallest font is 11 px. The specimen carries 100 token rows and 214 contrast rows.

Run on V1.4's specimen as committed, the corrected render check exits 1. It names the row demo's disabled row off the row surface and three steppers with no fill, and it finds one disabled cell.

**Which sections' pixels change.** Section 1 grows by 110 px, so every later section sits 110 px lower and a plain comparison shows rasterisation differences in most of them. I compared against V1.4's specimen padded by a 110 px spacer before section 2. With that spacer, sections 2 to 7 and 9 to 12 are pixel-identical in both themes. Only section 1 and section 8 differ:

- section 1: the row demo, the two steppers of the Controls strips, and the Disabled strip;
- section 8: the legend's stepper.

I read both sections in both themes at 1440 px. `report.json` and the four screenshots of those two sections are retained, in place of the screenshots retained before. Every other rendering went to a temporary directory outside the repository.

## An observation for ROOT to dispose of

**The check-box readings.** The sweep lists a check box and a switch at rest only. A check box in a table row or in a column menu's option sits on the row's or the menu item's wash when the pointer is there.

**Does the control rule as written already cover those readings?** Yes. The rule reads "at 3:1 or better against everything it sits on, in both themes, at rest and under the hover and pressed washes". What does not reach them is the generated table and the tools, which hold listed pairs only. All the unlisted readings pass by the tool's arithmetic (`scratch/scripts/probe_pairs.mjs`):

| Ink | Wash | Light | Dark |
|---|---|---|---|
| `border.control` on `surface.rowAlt` | hover | 3.51:1 | 4.00:1 |
| `border.control` on `surface.rowAlt` | pressed | 3.26:1 | 3.53:1 |
| `accent.fill` (the checked box) on `surface.panel`, `surface.rowAlt`, `surface.raised` | hover | 4.37:1 to 4.58:1 | 3.46:1 to 3.96:1 |
| `accent.fill` on the same three | pressed | 4.05:1 to 4.22:1 | 3.02:1 to 3.46:1 |

The lowest is 3.02:1 in dark, on a pressed `surface.raised` menu row (3.03:1 with an unrounded composite).

**My recommendation.** The sweep should list them. 3.02:1 is the thinnest margin the rule has, and nothing holds it if `accent.fill`, `surface.raised` or `pressed.wash` moves. Listing them would be eight pairs through `tools/contrast.mjs`, with no token change. It would change these things:

- the stated dark lowest moves from 3.14:1 to 3.02:1;
- the check box's row of §5's table changes;
- one sentence of §2.9 changes;
- the rendering of the specimen's section 12 changes.

I did not do it, because the correction limits finding 2 to the clause and the rule, and because it changes a stated number that ROOT should see first.

The other option is a design statement: a row or menu item holding a check box takes the hover wash and not the pressed one. That would leave 3.46:1 as the lowest. I did not make that statement either.

**Two smaller matters, seen and not changed.**

- **`.iconbtn.off` in the frames.** The frames give `.iconbtn.off` a `disabled.fill`, while §1.3 gives an icon-only button no fill. Both forms are within the seven disabled pairs, and §8 now names it for a later frames pass.
- **The stale hatch.** The document does not say whether a stale hatch can fall on a disabled row. The hatch is drawn over result cells, and the sizes are library rows.

## What I did not check

1. **The 720 px renderings** were held to the tool's counts only, not read by eye.
2. **The control and disabled readings** are of resolved colours composited by the tool, not of sampled pixels. I checked Chromium only, with no other engine, no assistive technology and no real device.
3. **The unlisted pairs** in the observation come from a scratch script. No tool holds them.
4. **The frames, the product and the specification** are untouched. I did not read `apps/desktop/**` for this correction. The render check reads the specimen's samples, not the product.
5. **The legend's Play button** overlaps the stepper's lower edge by a pixel, as it did before the correction. I left it.
6. **The first pass's measurement and frames scripts** were not re-run. Nothing they read has changed.

The record is §12 of `{DESIGN}/instances/DESIGN-SYSTEM/RETURN.md`. The scratch record is `{RUN}/instances/DESIGN-SYSTEM-05/scratch/correction_1_checks.txt`, with its three scripts beside it.

Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
