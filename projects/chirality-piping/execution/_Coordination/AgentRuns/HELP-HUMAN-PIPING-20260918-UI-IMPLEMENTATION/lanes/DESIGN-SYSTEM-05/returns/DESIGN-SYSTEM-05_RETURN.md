# Retained return — DESIGN-SYSTEM-05 (model that ran: Claude Fable 5.1, by its own statement)

Retained by ROOT. What follows is the child's final message as the host stored it, with the machine's repository path replaced by `{REPO_ROOT}`; nothing else is changed.

---

# RETURN — DESIGN-SYSTEM-05 · design system V1.3 → V1.4 · `tokens.json` 1.2 → 1.3

The pass is complete and every check is clean. One decision is ROOT's: whether to lift `text.disabled` to `#8f949a` / `#767b80`, as I recommend in section 5.

Model: Claude Fable 5.1 (`claude-fable-5-1`). I worked alone and delegated nothing. I verified the brief's SHA-256 (`322ca33b…5e7c11`) before starting.

Three context compactions occurred. Each time I resumed from the files on disk and a transcript summary. Every check below was run after the last edit to the file it checks.

I wrote only in `{DESIGN}/instances/DESIGN-SYSTEM/**` and `{RUN}/instances/DESIGN-SYSTEM-05/**`.

## 1 Files changed

All tracked changes are in `{DESIGN}/instances/DESIGN-SYSTEM/`:

| File | Change | sha256 |
|---|---|---|
| `DESIGN_SYSTEM_V1.md` | V1.4: status, §1.2, §1.3, §2.2 note, §2.9 (method, findings, 214 generated rows), §4, §5 (the control rule and its generated table), §5.2, §5.5, §5.6, §8 (item 6 restated; what a frames pass must follow), §9 rows 113–120. Rows 1–112 are unchanged by hash. | `8940ce589947536e18be2d11dd9818c98848a841783e125dbdc5efee9548a9c0` |
| `tokens.json` | 1.3 | `0e01828c4e7739313a47b5f71ac3c9fa3cf21aae3d07648eadc805fd82d18c00` |
| `specimen.html` | V1.4: control boundaries moved to `border.control`. Also the latched boundary, the active segment's boundary, the tab form, chips that are on, the outline's bar, the compass, and the wash rule. A new "Controls" panel shows each control on every surface, the disabled forms, the splitter and the glyphs. | `434a3fff6945afc3a45d7d97f3430d44e3449b895eaeba6c20e17920f23fec3f` |
| `tools/palette.mjs` | Builds 1.3. The 1.2 values of `text.disabled` are kept in a comment. | `4f9b74e7d63c390341c3b61e735390d5aeb65052840c4c45c0c8160661c89009` |
| `tools/contrast.mjs` | 214 pairs (62 added). The sweep has 29 rows: 21 held to the rule, 8 outside it. Adds `rules`, `sweepRows`, `toSweepMarkdown`, `ruleFailures`. Exits 1 on a rule failure. | `ca38b109504f831f71c791327d05792d580df9575478a67e8e5a0f3392bb5563` |
| `tools/gen.mjs` | Generates the §5 sweep table. | `af708b626a9a5a6c5b74ac96852bbdc6a1bae85db9760958cc28f6fc09796e21` |
| `tools/splice.mjs` | Splices the table between the `GENERATED:CONTROL_SWEEP` markers. | `56538c093d75c582b3870cc26187db795dee352777e3c80dbdb9013a85ceb1a6` |
| `tools/agree.mjs` | Checks V1.4 and 1.3. Pins rows 1–112 by hash and requires rows 113 on to cite brief items 1–5 and D-68. Fails on any rule failure or if §5's table differs from a fresh generation. In the specimen it requires every control boundary in `border.control`, every latched form with a `pressed.ink` boundary, none in `border.strong`, and no chosen chip on a status fill. | `a7ca5882507c647183fbf0428c14b547f860c8f7ffa5a533564e5db6cc9e30b0` |
| `tools/render.mjs` | Measures, as Chromium resolves them, what identifies each control sample against its own fill and its surround. Measures each disabled sample's ink against its fill. Exits 1 if a reading is under 3:1, a boundary resolves to `border.strong`, or a disabled ink is under the stated ratio. | `f43ba4d27f1b61ac06da82697a5e674443d2ff5c02d1a052aafb53fa8dd69661` |
| `RETURN.md` | §11 addendum, plus one sentence in the head. | `7dcd40ad2d4d798fda729966c1d14f7169c0b4a6a136d2fb473a0ac7232e5bd4` |

New and untracked, under `{RUN}/instances/DESIGN-SYSTEM-05/`:
- `shots/` holds 52 PNGs and `report.json`.
- `scratch/` holds `measurements_v13_v14.md`, `frames_scan.md`, `tokens_1.2_to_1.3.diff`, `agree_injected_faults.txt`, `render_on_v13_specimen.txt`, and the three scripts under `scripts/`.

## 2 Token diff (1.2 sha `00c1afe9…` → 1.3)

```
-  "version": "1.2",
+  "version": "1.3",
   "note": … + " 1.3 (design system V1.4): border.control is the boundary that identifies a control, 3:1 or better on every surface and fill a control sits on, and border.strong stays for framing that identifies no component; text.disabled is lifted so that a disabled label is 2.5:1 or better on everything it is drawn on in light and 3:1 or better in dark, short of text.muted in both; every other colour value is that of 1.2."
     "text.disabled": {
-      "light": "#a6abb1",
-      "dark": "#5f6469"
+      "light": "#8f949a",
+      "dark": "#767b80"
     "border.strong": { "light": "#b3b8be", "dark": "#53595f" },
+    "border.control": { "light": "#777e85", "dark": "#90969c" },
   "border": { "hairline": 1, "strong": 1,
+    "control": 1,
```

- 340 of 347 leaves are equal to 1.2; the seven that differ are the ones above.
- Colour tokens go from 99 to 100. Plain tokens stay at 99.
- `palette.mjs --write` reproduces the file byte for byte.
- `border.control` is OKLCH lightness 0.59 (light) and 0.67 (dark) at the neutral hue.
- The pressed moment sets the value: 3.17:1 on `pressed.wash/surface.sunken` in light and 3.14:1 on `pressed.wash/surface.raised` in dark.
- One lightness step lighter still passes, at 3.04:1 and 3.02:1. I kept that one step of margin.
- I did not adopt the product's kept `--ui-border`. It reads 3.24:1 or better at rest on these surfaces. On a pressed sunken fill in dark it reads 2.91:1, and on a pressed raised fill 2.35:1.

## 3 Moves from `border.strong` to `border.control` (brief item 1; §9 row 114)

- The text field.
- The combobox and the menu button.
- The stepper and the line between its halves.
- The palette field.
- The agent's input row.
- The paste band's mapping selects.
- The bordered button, including "Run again" on the stale band.
- The segmented control's trough.
- The compass's three raised icon buttons.
- The compass's length field, under the focus ring.
- The check box and the radio button. Only the empty outline moves. Checked, they keep the frames' form: `accent.fill` with the check or dot in `text.inverse`.
- The active tab.

V1.3 did not specify the last two; the frames drew them in `border.strong`. `border.strong` stays for the table frame, the drawers and the expansion edge.

## 4 Component sweep (brief item 2)

This table is condensed; the verbatim generated table is in §5 of the document. Every row passed or is outside the criterion. `contrast.mjs` reports 0 rule failures.

| Component | Identified or state shown by | Token(s) | Lowest, light | Lowest, dark | 3:1 |
|---|---|---|---|---|---|
| Fields: text field, combobox, menu button, stepper, palette field, agent input row, mapping selects | 1 px boundary against the surround and its own fill at rest, hovered and pressed | `border.control` | 3.17 on `pressed.wash/surface.sunken` | 3.88 on the same | pass |
| Bordered button, including Run again | the same | `border.control` | 3.39 on `pressed.wash/surface.panel` | 3.60 | pass |
| Primary button | fill and label | `accent.fill`, `accent.fillHover`, `text.inverse` | 4.49 on `surface.base` | 4.15 on `surface.raised` | pass |
| Text button, link, toast action | label | `text.secondary`, `text.link` | 5.32 | 6.03 | pass |
| Latched toggle, HUD tool, chip that is on | 1 px boundary; boundary, glyph and label on the fill | `pressed.ink` | 5.97 on `pressed.fill` | 5.66 | pass |
| Latched toggle | its fill | `pressed.fill` | 1.11 | 1.82 | outside: a wash; the boundary and ink carry the state |
| Segmented control | trough boundary and active segment's boundary | `border.control` | 3.60 on `surface.base` | 4.95 | pass |
| Segmented control | active segment's fill | `surface.panel` | 1.07 | 1.07 | outside: the segment's boundary carries the state |
| Switch | off track, on track, thumb | `border.control`, `accent.fill`, `surface.panel` | 3.69 on `surface.header` | 4.15 | pass |
| Check box, radio | empty: outline. Checked: fill, and the check or dot on it | `border.control`, `accent.fill`, `text.inverse` | 3.50 on `selection.band` | 3.50 | pass |
| Tab (stage, drawer, agent column) | active tab's boundary; labels | `border.control`, `text.secondary`, `text.primary` | 3.69 on `surface.header` | 4.64 | pass |
| Chip that is a control | label; when on, the latched form | `text.secondary` | 5.62 | 6.03 | pass |
| Icon-only button and control glyphs | the glyph, on every surface, band and hovered row | `text.secondary` | 5.33 on `selection.band` | 5.08 | pass |
| Raised icon button on the canvas | boundary at rest, hovered and pressed | `border.control` | 3.39 | 3.14 on `pressed.wash/surface.raised` | pass |
| Compass handles and length field | handle and letter; the field's boundary under the ring | `canvas.axisX/Y/Z`, `border.control` | 3.50 on `canvas.bg` | 4.32 | pass |
| Selection | 3 px bar; a selected cell's outline | `selection.bar` | 4.36 on `selection.band` | 4.38 | pass |
| Selection | the band | `selection.band` | 1.17 | 1.36 | outside: the bar carries it |
| Focus | 2 px ring | `focus.ring` | 4.01 on `canvas.bg` | 4.69 | pass |
| Gutter and marks glyphs | the quietest of them, the origin glyph | `mark.origin` | 3.23 on `selection.band` | 3.24 | pass |
| Offered check and plus | glyph | `text.muted` | 3.23 | 3.24 | pass |
| Drag handle | glyph | `text.secondary` | 6.26 | 6.91 | pass |
| Splitter | a grip (3 px × 24 px) on the hairline | `border.control` | 3.50 on `canvas.bg` | 4.64 | pass |
| Rail item, agent strip | icon and label; working dot | `text.secondary`, `accent.fill` | 4.49 | 5.38 | pass |
| Status chip with popover, Issues count | label on the fill; the count's glyph | `status.*Ink`, `issue.blocking`, `issue.warning` | 3.82 | 6.79 | pass |
| Select-all control | nothing is drawn | — | — | — | outside: nothing to measure; a pointer-rule question |
| Disabled control | label and glyph | `text.disabled` | 2.56 on `disabled.fill` | 3.02 on `surface.raised` | outside: inactive, exempt; it has its own rule (§2.9) |
| Hairlines | 1 px line | `border.hairline` | 1.25 | 1.37 | outside: separates and identifies nothing |
| Frames (table, drawer, expansion edge) | frame or edge | `border.strong` | 1.75 | 2.09 | outside: frames a region |
| Display-only expression | dashed frame | `displayOnly.border` | 1.86 | 2.23 | outside: not a control |

The sweep's other failures were fixed with no further token (§9 rows 115–116):
- **Off switch track:** it was 2.00:1 and 2.09:1, and is now `border.control`.
- **Active segment:** its fill was 1.07:1 on the trough. It gains a `border.control` boundary.
- **Latched toggle:** V1.3 left a fill of 1.11:1 to 1.82:1 as its edge. It keeps a `pressed.ink` boundary.
- **Chip that is on or chosen:** it sat at 1.02:1 on a status fill in the specimen and 1.05:1 on the selection band in the frames. It takes the latched form.
- **Review outline's selected row:** it gains the `selection.bar`.
- **Wash:** it is never drawn over a band or a state fill. With it the origin glyph on a selected row would read 2.89:1 and 2.71:1; without it, 3.23:1 and 3.24:1.
- **Tokens for untokened parts:** the splitter grip, the drag handle and the two offers now have tokens, as in the table above.

## 5 `text.disabled` — recommendation, for ROOT to decide (brief item 3)

I recommend lifting `text.disabled` to `#8f949a` / `#767b80`. The stated ratio is 2.5:1 or better in light and 3:1 or better in dark on everything the ink is drawn on. It must also stay 1.2:1 or more short of `text.muted`. The tools hold all three.

| Option | Light value | on `disabled.fill` | on the surfaces | beside `text.muted` | Dark value | on `disabled.fill` | on the surfaces | beside `text.muted` |
|---|---|---|---|---|---|---|---|---|
| keep 1.2 | `#a6abb1` | 1.94:1 | 2.03–2.31:1 | 1.64:1 | `#5f6469` | 2.28:1 | 2.16–2.80:1 | 1.78:1 |
| **lift (in 1.3)** | `#8f949a` | 2.56:1 | 2.68–3.06:1 | 1.24:1 | `#767b80` | 3.19:1 | 3.02–3.92:1 | 1.27:1 |
| 3:1 everywhere in light | `#82878c` | 3.03:1 | 3.17–3.62:1 | 1.04:1 | as the lift | | | |
| the product's kept ink | `#667680` | 3.94:1 | 4.12–4.70:1 | stronger than muted | `#9baab2` | 5.71:1 | 5.40–7.00:1 | stronger than muted |

- Beside `text.secondary` the lifted ink reads 2.05:1 in light and 2.00:1 in dark.
- The lift stops at 2.5:1 in light because `text.muted` is itself 3.17:1 on `disabled.fill`. An ink at 3:1 there would be within 1.04:1 of the muted ink.
- The product's kept ink is stronger than muted text, so it reads as enabled.
- Reaching 3:1 everywhere in light needs `text.muted` to move first. That belongs with the text target (§8 item 6, restated).
- Besides ink, the disabled state is carried by `disabled.fill`, the boundary dropping to `border.hairline`, no wash, and the reason tooltip (§1.3). The cursor carries nothing, because it is the default arrow over every control.
- The seven disabled pairs are in §2.9. V1.3's finding that the disabled selector sits on a sunken field is corrected: it sits on `disabled.fill`.
- To decide otherwise:
  1. Change the two values in `tools/palette.mjs` (the 1.2 values are in the comment).
  2. Set `rules.disabledLight` and `rules.disabledDark` in `tools/contrast.mjs`.
  3. Change the sentences that quote the values (status line, §2.2 note, §2.9 finding, §8 item 6, §9 rows 118 and 120).
  4. Rerun the chain. The specimen needs no hand edit.

## 6 Frames that draw a control boundary in `border.strong`, for a later frames pass (brief item 5)

In `{DESIGN}/instances/MOCKS/frames/mocks.css`, 19 rules use `border.strong`.

- **Move (13 selectors, 12 rules counting the switch pair as one):** `.seg`, `.btn`, `.input`, `.combo`, `.switch i` with `.tblhead .switch.off i`, `.search`, `.lenfield`, `.tabs .tab.on`, `.maprow .m .sel`, `.pop .row .k` (empty boxes only), `.iconbtn.raised`, `.sendrow`.
- **Stay (6):** `.stage`, `.lights i`, `.bar b`, `.expand .block`, `.card .asked`, `.content .live`.

By frame:
- All 18 stage frames draw `.seg` twice, bordered `.btn` (5–12 times), `.combo` (1–4 times) and `.search` once.
- `.tabs .tab.on` is in every stage frame except `s9_table_dark` and `s9_table_light`.
- The off switch track is in `s7_both_dark`, `s7_both_light` and `s7_both_light_historical`.
- `.input` is in `s7_table_light`.
- `.pop .row .k` is in `s7_table_light`: three empty boxes move and two checked boxes keep their form.
- `.lenfield` and three `.iconbtn.raised` are in `s2_model_dark` and `s2_model_light`.
- `.maprow .m .sel` (11 occurrences) is in `s3_table_light`.
- `.sendrow` is in `s4_both_light_slideover` and `s8_table_light`.
- `index.html` draws none.

Other V1.4 forms the same pass would follow:
- The active segment's boundary, in every stage frame.
- The `pressed.ink` boundary on `.btn.latched`, in `s4_both_light`, `s4_both_light_column`, `s4_both_light_slideover` (twice) and `s8_table_light`.
- The `pressed.ink` boundary on the latched HUD tool, in `s2_model_*` and `s7_both_dark` / `s7_both_light`.
- The `pressed.ink` boundary on `.iconbtn.on`, in `s7_both_light_historical`.
- `.chip.outline.on` in the latched form, in `s6_both_light` and `s9_table_*`.
- The agent column's active tab, in `s4_both_light_slideover` and `s8_table_light`.
- `.outline div.on` with the bar, in `s9_table_*`.
- The disabled ink.

The frames have no hover rule, no splitter grip and no drag handle.

## 7 What I ran

All commands ran from `{DESIGN}/instances/DESIGN-SYSTEM/`. `<out>` is scratch outside the repository.

1. `node tools/palette.mjs --write <out>/tokens.json`, then `cmp` with `tokens.json`: equal byte for byte.
2. `node tools/contrast.mjs tokens.json <out>/contrast_table.md`: exit 0.
   - 214 pairs.
   - Control rule: 29 sweep rows, 21 held, lowest 3.17:1 light and 3.14:1 dark.
   - Disabled ink: 7 rows, lowest 2.56:1 light and 3.02:1 dark.
   - Rule failures: 0.
3. `node tools/gen.mjs tokens.json <out>/gen`, then `node tools/splice.mjs <out>/gen specimen.html DESIGN_SYSTEM_V1.md`. A second splice leaves both files byte-identical.
4. `node tools/agree.mjs DESIGN_SYSTEM_V1.md tokens.json specimen.html`: exit 0, `problems: []`.
   - It counts 100 colour tokens, 99 plain tokens, 214 contrast rows and pairs, 28 label chips and 120 change-log rows.
   - I ran it again after `RETURN.md` was finished, since its machine-path walk covers that file.
   - I also ran it against copies with 14 faults injected one at a time. It named every fault, and the unmodified files pass.
   - I re-ran that fault test against the final files, and its output is identical to the record in `scratch/agree_injected_faults.txt`.
5. `node tools/render.mjs specimen.html {RUN}/instances/DESIGN-SYSTEM-05/shots`: exit 0. Chromium, every non-file request blocked, no server and no port. Rendered at 1440 and 720 wide, light and dark.
   - In all four renderings there were no blocked requests, no console issues and no horizontal overflow. The smallest font is 11 px. There are 100 token rows and 214 contrast rows. Every V1.1–V1.3 fact is unchanged.
   - 317 control readings. The lowest is 3.16:1: a pressed combobox in light and a pressed raised icon button in dark. None is under 3:1, and none resolves to `border.strong`.
   - 24 disabled samples. The lowest is 2.56:1 in light and 3.02:1 in dark. None is under the stated ratio.
   - The 3.16:1 reading differs from the tool's 3.17:1 and 3.14:1 only by rounding: `contrast.mjs` rounds a composited wash to whole channel values and the render check does not.
   - The same tool on V1.3's specimen reports 128 of 160 readings under 3:1, 120 of them boundaries in `border.strong`, and disabled ink at 1.94:1 and 2.16:1.
   - I read the screenshots of sections 1, 5, 9, 10 and 11 in both themes. They showed three defects, and I fixed each: a class-name collision, a wrapped sample, and the check reading a checked box's boundary against its own fill.
6. `git status` and `git diff --stat`, both read-only. Ten files are modified under `{DESIGN}/instances/DESIGN-SYSTEM/`. `{RUN}/instances/DESIGN-SYSTEM-05/` is untracked.
7. A grep for machine paths in both folders found none.

## 8 What I did not do

- I did not touch the specification, the frames, or the product. Nothing under `apps/desktop/**` changed, and the product still holds its copy of 1.2.
- I ran no state-changing git command, started no server, and ran no product build or whole-suite test.
- I hand-edited nothing generated and delegated nothing.
- Nothing the owner ruled changed: names, labels, copy rules, the six functions and the tooltip form all stand.
- `palette.mjs`'s categorical validator is not supplied, as before. The result ramp and the categorical set are unchanged.

## 9 Uncertainties and observations, not acted on

1. A strict reading of the criterion could put a labelled control's boundary outside it. I held every field and bordered-button boundary to the rule anyway. A field has nothing else that says where it is, and the first slice's check measures a button's boundary.
2. The anatomy I added is the least the sweep needed. It is mine and open to replacement:
   - the grip and its size;
   - the tab form in the agent column;
   - the latched boundary;
   - the segment boundary;
   - the latched chips;
   - the offers' ink;
   - "Changed since: Run 03" drawn latched;
   - the drag handle drawn as six dots (§3.2 has no drag-handle glyph; I added none there).
3. Latched and unlatched forms differ mainly by hue. That is a 1.4.1 question and outside this pass.
4. Some `text.muted` control labels are under a text target of 4.5:1. The palette placeholder reads 3.53:1 light and 4.70:1 dark. "Add row" reads 3.79:1 and 4.41:1. They wait for the text target.
5. The 22 px icon buttons and the 16 px check box are under a 24 px target unless the cell or row is the target.
6. The select-all control and the column resize handles have no drawn form. The Run button's progress fill is not a token.
7. B1-REVIEW's F2 is product scope: one product variable draws both the hairlines and three frames that §1.2 assigns to `border.strong`. V1.4 keeps `border.strong` for exactly such frames.
8. `status.solvedFill` equals `surface.base` in light. It informs and is outside the rule.
9. The specimen's text button takes no wash, as at V1.3.
10. `render.mjs` now imports `rules` from `contrast.mjs`, so both hold the same ratios. Its readings cover the specimen's samples, not the product.

Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
