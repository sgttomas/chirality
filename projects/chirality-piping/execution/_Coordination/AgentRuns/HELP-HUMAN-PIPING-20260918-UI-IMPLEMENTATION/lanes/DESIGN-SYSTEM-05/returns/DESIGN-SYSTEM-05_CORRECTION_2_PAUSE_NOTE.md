# DESIGN-SYSTEM-05, correction 2: the child's pause note (a status, not a return)

Retained by ROOT. What follows is the child's final message as the host stored it, with the machine's repository path replaced by `{REPO_ROOT}`; nothing else is changed.

---

# DESIGN-SYSTEM-05 · correction 2 · pause note

I have paused at a clean point. I have changed no file since `ff4c71689`. `git status` is empty at `d651c1f6b` and `tokens.json` is still `0e01828c…d18c00`. The only things I wrote are read-only probe scripts and their output, in a temporary directory outside the repository.

## Do both tools pass right now?

Yes, because the files are correction 1's as committed.

- **`tools/contrast.mjs`:** 214 pairs, 29 sweep rows of which 21 are held to the rule. The lowest held readings are 3.17 light and 3.14 dark, and rule failures are 0.
- **`tools/agree.mjs`:** exit 0, `problems: []`, 123 change-log rows.

Nothing is knowingly inconsistent in any file.

## What of correction 2 is done

This is analysis only.

**The sealed file** is verified (`f08cdbea…0815d`) and read whole.

**What I read:**
- the document's §1.3, §2.9, §5, §5.1, §5.5, §5.6 and §8;
- the three tools;
- the specimen's Controls strips and menus;
- the frames' column menu.

### The pairs I will list, and how I decided them

A check box sits in one of three places:

| Where | Washed? | Why |
|---|---|---|
| A check-box cell of a table row | Hover and pressed, over `surface.panel` or the zebra `surface.rowAlt` | §1.3 gives the wash to "the row or control", for both states. A selected or proposed row keeps its band and is never washed. |
| A column menu's option | Hover and pressed, over `surface.raised` | It is a menu row. |
| A dialog's option | No | It is a box with its label in a form, not a washed row. |

That gives eight new pairs:

- `border.control` on `hover.wash/surface.rowAlt` and on `pressed.wash/surface.rowAlt`;
- `accent.fill` on the hover and the pressed wash over each of `surface.panel`, `surface.rowAlt` and `surface.raised`.

The four `border.control` pairs on washed `surface.panel` and `surface.raised` are already listed, so the check box's sweep row gains twelve entries in all.

**The switch gets no new pairs.**
- The design has two switches, Envelope and Show edits. Both sit in header bands, which take no wash.
- The View menu's "switches" are checked items drawn with the check glyph.
- The footer's "switches" are chips.
- The switch's sweep row therefore stays as it is, and my correction-1 sentence that implies a switch can sit in a washed row will be reworded.

By the tool's arithmetic every pair I will list passes, so the stop condition is not met. The lowest are:

- `accent.fill` on `pressed.wash/surface.raised`: 4.22:1 light, 3.02:1 dark (3.0170 unrounded);
- `border.control` on `pressed.wash/surface.rowAlt`: 3.26:1 light, 3.53:1 dark.

## One finding ROOT should have while taking stock

The same row interaction makes two neighbouring sweep rows fail, by a hair. These are not pairs correction 2 asks me to list.

- The gutter's origin glyph (`mark.origin`) and the two offers (`text.muted`) are listed on a hovered row only.
- On a pressed `surface.rowAlt` row they read 2.9985:1 in light by the tool's arithmetic, which is under 3:1. With an unrounded composite the figure is 2.9905. In dark they read 3.15:1.
- On a pressed `surface.panel` row they read 3.12:1 light and 3.21:1 dark.
- No other ink that identifies a control, under either wash on a surface it is drawn on, falls under 3:1.

I did not choose a fix, because tokens and interactions are reserved. The ways out I can see are these:

- a token change: `pressed.wash`, `text.muted` with `mark.origin`, or `surface.rowAlt`;
- a statement about rows and the pressed wash.

Unless ROOT directs otherwise, I will complete correction 2 as sealed and return this as an observation. In the document I will word the "lowest reading" sentences as what the rule's table holds, so that nothing I write claims more than the tools check.

## Not started

- The edits to `tools/contrast.mjs`, then the contrast, gen and splice run.
- The §2.9 and §5 prose. Figures: the boundary's lowest stays 3.17:1 light and 3.14:1 dark. The table's lowest in dark becomes 3.02:1. The checked box's "3.50:1 or better" becomes 3.02:1. The "sixty-two pairs" sentence gains the eight.
- The stale-hatch clause in §5.1.
- The specimen's samples: a box, empty and checked, in a hovered and a pressed row on both row surfaces, and in a hovered and a pressed menu item.
- `tools/render.mjs` counting those readings apart.
- `tools/agree.mjs` pinning rows 1 to 123, requiring rows from 124 to cite correction 2, and checking the stated lowest figures against the tool.
- Change-log rows from 124.
- The render run, the padded pixel comparison, and the retained screenshots with `report.json`. Section 12 returns to `shots/`, and I expect section 1 to change as well.
- §13 of `RETURN.md`, and the return itself.

## Exact next step

1. Add the eight pairs to `pairs` and the twelve entries to the check box's sweep row in `tools/contrast.mjs`.
2. Run the tool to a temporary file outside the repository.
3. Confirm that no listed pair is under 3:1 and that rule failures are 0.
4. Run `gen.mjs` and `splice.mjs`.

I am Claude Fable 5.1 (`claude-fable-5-1`). I work alone, I delegated nothing, and I ran no state-changing git command.

Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
