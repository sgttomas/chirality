// Contrast findings: reads tokens.json and reports the WCAG 2.x ratio of every text and mark
// pairing in both themes. The pair list is exported so that gen.mjs embeds the same list in the
// specimen and agree.mjs checks both against it. Up to V1.3 the table was findings only. V1.4 holds
// two groups of rows to a rule (`rules` below) and leaves every other row a finding: a row whose role
// begins with "control" is what identifies a control or shows its state and reads 3:1 or better in
// both themes; a "text (disabled)" row reads 2.5:1 or better in light and 3:1 or better in dark, and
// the disabled ink stays 1.2:1 or more short of the muted ink. The run exits 1 when a rule fails.
// Correction 1 to V1.4 changes no pair and no ratio: the sweep's disabled row is named for the table row that cannot be chosen as well.
// `sweep` is the control rule's table for the document (section 5): one row per component part,
// every pair of it a row of `pairs`.
//   node contrast.mjs <tokens.json> <out.md>
import fs from "node:fs";

const hex2rgb = (h) => { h = h.replace("#", ""); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)); };
const parseColor = (s) => {
  if (s.startsWith("#")) return { rgb: hex2rgb(s), a: 1 };
  const m = s.match(/rgba?\(([^)]+)\)/);
  const p = m[1].split(",").map(Number);
  return { rgb: p.slice(0, 3), a: p.length > 3 ? p[3] : 1 };
};
const over = (c, b) => c.rgb.map((v, i) => Math.round(c.a * v + (1 - c.a) * b.rgb[i]));
const lum = (rgb) => { const [r, g, b] = rgb.map(v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const ratio = (fg, bg) => { const [hi, lo] = [lum(fg), lum(bg)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05); };

// name may be "a" or "a/b": a composited over b (and b over white if translucent)
function resolve(C, name, theme) {
  let acc = { rgb: [255, 255, 255], a: 1 };
  for (const p of name.split("/").reverse()) {
    const v = C[p]?.[theme];
    if (!v) throw new Error("unknown token " + p);
    acc = { rgb: over(parseColor(v), acc), a: 1 };
  }
  return acc.rgb;
}

// [fg, bg, role]. The order is the document's. V1.2 adds five rows for canvas.edgeAlt (R-6).
export const pairs = [
  ["text.primary", "surface.panel", "text"], ["text.primary", "surface.base", "text"], ["text.primary", "surface.sunken", "text"],
  ["text.primary", "surface.header", "text"], ["text.primary", "surface.rowAlt", "text"], ["text.primary", "surface.raised", "text"],
  ["text.primary", "selection.band", "text"], ["text.primary", "proposal.band", "text"], ["text.primary", "hover.wash/surface.panel", "text"],
  ["text.primary", "issue.blockingTint", "text"], ["text.primary", "issue.warningTint", "text"], ["text.primary", "issue.infoTint", "text"],
  ["text.primary", "historical.tint", "text"], ["text.primary", "stale.band", "text"], ["text.primary", "disabled.fill", "text"],
  ["text.secondary", "surface.panel", "text"], ["text.secondary", "surface.base", "text"], ["text.secondary", "surface.header", "text"],
  ["text.secondary", "surface.sunken", "text"], ["text.secondary", "selection.band", "text"], ["text.secondary", "proposal.band", "text"],
  ["text.secondary", "canvas.hint/canvas.bg", "canvas hint text"],
  ["text.muted", "surface.panel", "text"], ["text.muted", "surface.base", "text"], ["text.muted", "surface.header", "text"], ["text.muted", "surface.sunken", "text"],
  ["text.disabled", "surface.panel", "text (disabled)"], ["text.disabled", "surface.base", "text (disabled)"], ["text.disabled", "surface.sunken", "text (disabled)"],
  // V1.4: the disabled ink on everything else it is drawn on, and how far it stays from the inks beside it
  ["text.disabled", "surface.header", "text (disabled)"], ["text.disabled", "surface.raised", "text (disabled)"], ["text.disabled", "surface.rowAlt", "text (disabled)"],
  ["text.disabled", "disabled.fill", "text (disabled)"],
  ["text.disabled", "text.muted", "disabled ink beside muted ink"], ["text.disabled", "text.secondary", "disabled ink beside an enabled glyph's ink"],
  ["text.link", "surface.panel", "text"], ["text.link", "surface.base", "text"],
  ["accent.text", "surface.panel", "text"], ["accent.text", "selection.band", "text"],
  ["text.inverse", "accent.fill", "text on button"], ["text.inverse", "accent.fillHover", "text on button"],
  ["pressed.ink", "pressed.fill", "latched toggle"], ["pressed.fill", "surface.base", "latched toggle fill"],
  ["proposal.new", "surface.panel", "text"], ["proposal.new", "proposal.band", "text"], ["proposal.new", "surface.base", "text"],
  ["proposal.old", "surface.panel", "text (struck)"], ["proposal.old", "proposal.band", "text (struck)"],
  ["mark.checked", "surface.panel", "mark"], ["mark.checkedStale", "surface.panel", "mark"], ["mark.checkedStale", "surface.base", "mark"],
  ["mark.origin", "surface.panel", "mark"], ["mark.origin", "surface.rowAlt", "mark"], ["mark.origin", "surface.header", "mark"],
  ["mark.attachment", "surface.panel", "mark"], ["mark.required", "surface.panel", "mark"], ["mark.required", "surface.sunken", "mark"],
  ["draft.bar", "surface.panel", "draft row bar"], ["draft.bar", "selection.band", "draft row bar"],
  ["issue.blocking", "surface.panel", "text"], ["issue.blocking", "issue.blockingTint", "text"], ["issue.blocking", "surface.base", "text"],
  ["issue.warning", "surface.panel", "text"], ["issue.warning", "issue.warningTint", "text"], ["issue.warning", "surface.base", "text"],
  ["issue.info", "surface.panel", "text"], ["issue.info", "issue.infoTint", "text"],
  ["status.incompleteInk", "status.incompleteFill", "chip text"], ["status.solvedInk", "status.solvedFill", "chip text"],
  ["status.failedInk", "status.failedFill", "chip text"], ["status.reviewInk", "status.reviewFill", "chip text"],
  ["status.incompleteInk", "surface.panel", "chip text"], ["status.failedInk", "surface.panel", "chip text"], ["status.reviewInk", "surface.panel", "chip text"],
  ["rail.captionFailed", "surface.base", "rail caption"], ["rail.captionStale", "surface.base", "rail caption"], ["rail.captionHistorical", "surface.base", "rail caption"],
  ["historical.ink", "historical.tint", "text"], ["historical.ink", "surface.panel", "text"],
  ["stale.ink", "stale.band", "band text"], ["stale.ink", "surface.panel", "band text"],
  ["border.hairline", "surface.panel", "hairline"], ["border.hairline", "surface.base", "hairline"],
  ["border.strong", "surface.panel", "frame"], ["border.strong", "surface.base", "frame"],
  // V1.4, the control rule. The boundary that identifies a control: on every surface a control sits on, on the bands a control
  // can sit on, on the canvas, and on the control's own fill at rest and under the hover and pressed washes.
  ["border.control", "surface.panel", "control boundary"], ["border.control", "surface.base", "control boundary"], ["border.control", "surface.sunken", "control boundary"],
  ["border.control", "surface.header", "control boundary"], ["border.control", "surface.raised", "control boundary"], ["border.control", "surface.rowAlt", "control boundary"],
  ["border.control", "selection.band", "control boundary"], ["border.control", "proposal.band", "control boundary"], ["border.control", "stale.band", "control boundary"],
  ["border.control", "canvas.bg", "control boundary"],
  ["border.control", "hover.wash/surface.panel", "control boundary"], ["border.control", "hover.wash/surface.sunken", "control boundary"], ["border.control", "hover.wash/surface.raised", "control boundary"],
  ["border.control", "pressed.wash/surface.panel", "control boundary"], ["border.control", "pressed.wash/surface.sunken", "control boundary"], ["border.control", "pressed.wash/surface.raised", "control boundary"],
  // what shows a control's state: the latched boundary, the switch's tracks and thumb, the primary fill, the selection bar off its band
  ["pressed.ink", "surface.base", "control state"], ["pressed.ink", "surface.panel", "control state"], ["pressed.ink", "surface.header", "control state"], ["pressed.ink", "surface.raised", "control state"],
  ["accent.fill", "surface.panel", "control state"], ["accent.fill", "surface.base", "control state"], ["accent.fill", "surface.header", "control state"], ["accent.fill", "surface.raised", "control state"],
  ["accent.fill", "surface.rowAlt", "control state"], ["accent.fill", "selection.band", "control state"], ["accent.fill", "proposal.band", "control state"],
  ["accent.fillHover", "surface.panel", "control state"], ["accent.fillHover", "surface.base", "control state"], ["accent.fillHover", "surface.raised", "control state"],
  ["surface.panel", "border.control", "control state"], ["surface.panel", "accent.fill", "control state"],
  ["selection.bar", "surface.base", "control state"], ["selection.bar", "surface.panel", "control state"],
  // the glyphs that identify a control with no boundary, and the offered check and plus
  ["text.secondary", "surface.raised", "control glyph"], ["text.secondary", "surface.rowAlt", "control glyph"], ["text.secondary", "historical.tint", "control glyph"],
  ["text.secondary", "hover.wash/surface.panel", "control glyph"], ["text.secondary", "hover.wash/surface.rowAlt", "control glyph"],
  ["text.muted", "hover.wash/surface.panel", "control glyph"], ["text.muted", "hover.wash/surface.rowAlt", "control glyph"], ["text.muted", "selection.band", "control glyph"], ["text.muted", "proposal.band", "control glyph"],
  ["mark.origin", "selection.band", "control glyph"], ["mark.origin", "proposal.band", "control glyph"], ["mark.origin", "hover.wash/surface.panel", "control glyph"], ["mark.origin", "hover.wash/surface.rowAlt", "control glyph"],
  ["text.link", "surface.raised", "text"],
  // fills that are not the carrier of a state: measured so that the table says what carries it instead
  ["surface.panel", "surface.sunken", "segment fill on the trough"], ["selection.band", "surface.panel", "band on the panel"],
  ["focus.ring", "surface.panel", "focus ring"], ["focus.ring", "surface.base", "focus ring"], ["focus.ring", "selection.band", "focus ring"],
  ["focus.ring", "surface.sunken", "focus ring"], ["focus.ring", "surface.header", "focus ring"], ["focus.ring", "surface.raised", "focus ring"], ["focus.ring", "surface.rowAlt", "focus ring"],
  ["focus.ring", "proposal.band", "focus ring"], ["focus.ring", "canvas.bg", "focus ring"],
  ["selection.bar", "selection.band", "mark"], ["proposal.bar", "proposal.band", "mark"], ["displayOnly.border", "surface.sunken", "border"], ["stale.stripe", "surface.panel", "mark"],
  ["bar.track", "surface.panel", "bar track"], ["bar.track", "selection.band", "bar track"],
  ["canvas.label", "canvas.labelBg/canvas.bg", "canvas text"], ["canvas.label", "canvas.bg", "canvas text"],
  ["canvas.gridMajor", "canvas.bg", "hairline"], ["canvas.gridMinor", "canvas.bg", "hairline"],
  ["canvas.pipe", "canvas.bg", "canvas mark"], ["canvas.pipeShade", "canvas.bg", "canvas mark"], ["canvas.edge", "canvas.pipe", "canvas mark"], ["canvas.edge", "canvas.bg", "canvas mark"],
  ["canvas.glyph", "canvas.bg", "canvas mark"], ["canvas.glyph", "canvas.glyphFill", "canvas mark"], ["canvas.glyphFill", "canvas.bg", "canvas mark"],
  ["canvas.vector", "canvas.bg", "canvas mark"], ["canvas.selection", "canvas.bg", "canvas mark"], ["canvas.selection", "canvas.pipe", "canvas mark"],
  ["canvas.hover", "canvas.bg", "canvas mark"], ["canvas.draft", "canvas.bg", "canvas mark"], ["canvas.proposalGhost", "canvas.bg", "canvas mark"],
  ["canvas.deformGhost", "canvas.bg", "canvas mark"], ["canvas.unsolved", "canvas.bg", "canvas mark"],
  ["canvas.axisX", "canvas.bg", "canvas mark"], ["canvas.axisY", "canvas.bg", "canvas mark"], ["canvas.axisZ", "canvas.bg", "canvas mark"],
  ...[1,2,3,4,5,6,7].map(i => [`result.scale.${i}`, "canvas.bg", "result scale on canvas"]),
  ["result.scale.1", "canvas.unsolved", "result scale beside unsolved"], ["result.scale.7", "canvas.unsolved", "result scale beside unsolved"],
  ["canvas.edge", "result.scale.1", "edge line on the near-zero step"], ["canvas.edge", "result.scale.7", "edge line on the brightest step"],
  ["canvas.edge", "result.scale.6", "edge line on the step nearest its own lightness in light"], ["canvas.edge", "result.scale.2", "edge line on the last step it keeps"], ["canvas.edgeAlt", "result.scale.2", "alternate edge on the last step it leaves"],
  ["canvas.edgeAlt", "result.scale.3", "alternate edge on the first step it takes"], ["canvas.edgeAlt", "result.scale.7", "alternate edge on the far step"],
  ["canvas.edgeAlt", "canvas.bg", "alternate edge against the ground"],
  ...[1,2,3,4,5,6,7].map(i => [`result.scale.${i}`, "surface.raised", "legend swatch"]),
  ["result.scale.1", "bar.track", "data bar on its track"], ["result.scale.7", "bar.track", "data bar on its track"],
  ...[1,2,3,4,5,6,7,8].map(i => [`cat.${i}`, "canvas.bg", "load vector on canvas"]),
  ...[1,2,3,4,5,6,7,8].map(i => [`cat.${i}`, "surface.panel", "case dot in table"]),
];

export function computeRows(T) {
  const C = T.color;
  return pairs.map(([fg, bg, role]) => ({ fg, bg, role, l: ratio(resolve(C, fg, "light"), resolve(C, bg, "light")), d: ratio(resolve(C, fg, "dark"), resolve(C, bg, "dark")) }));
}
export function toMarkdown(rows) {
  return ["| Foreground | Background | Role | Light | Dark |", "|---|---|---|---|---|",
    ...rows.map(r => `| \`${r.fg}\` | \`${r.bg}\` | ${r.role} | ${r.l.toFixed(2)}:1 | ${r.d.toFixed(2)}:1 |`)].join("\n");
}

// ---- V1.4: the two rules, and the control rule's sweep ----
// control: what identifies a control or shows its state, in both themes. disabledLight / disabledDark: a "text (disabled)" row.
// disabledApart: the disabled ink beside the muted ink. The disabled-ink values are this pass's recommendation and ROOT's to decide;
// if the 1.2 ink is kept, set disabledLight and disabledDark to 0 and the table is findings again for those rows.
export const rules = { control: 3, disabledLight: 2.5, disabledDark: 3, disabledApart: 1.2 };

// One row per component part: c the component and where section 5 specifies it, w what identifies it or shows its state, t the token that
// draws it, p every [foreground, background] the part meets (each one a row of pairs). A row with "outside" is outside the rule and says why;
// its readings are still shown. Section 5 of the document carries the table this generates.
const on = (fg, bgs) => bgs.map(bg => [fg, bg]);
const SURFACES = ["surface.panel", "surface.base", "surface.header", "surface.raised"];
export const sweep = [
  { c: "Text field, combobox, menu button, stepper, the palette field, the agent's input row, the paste band's mapping selects (§5.1 to §5.6)", w: "the 1 px boundary, against the surface around it and against its own fill at rest, hovered and pressed", t: "border.control",
    p: on("border.control", [...SURFACES, "surface.sunken", "hover.wash/surface.sunken", "pressed.wash/surface.sunken"]) },
  { c: "Bordered button, the Run again button on the stale band included (§5.1 to §5.6)", w: "the 1 px boundary, against the surface around it and against its own fill at rest, hovered and pressed", t: "border.control",
    p: on("border.control", [...SURFACES, "stale.band", "hover.wash/surface.panel", "pressed.wash/surface.panel"]) },
  { c: "Primary button: Run, a card's Accept all rows, a dialog's primary (§5.2, §5.4, §5.6)", w: "its fill, at rest and hovered, and its label", t: "accent.fill, accent.fillHover, text.inverse",
    p: [...on("accent.fill", ["surface.base", "surface.panel", "surface.raised"]), ...on("accent.fillHover", ["surface.base", "surface.panel", "surface.raised"]), ["text.inverse", "accent.fill"], ["text.inverse", "accent.fillHover"]] },
  { c: "Text button, link, a toast's action, the run text button, the hidden count (§5.1, §5.4, §5.6)", w: "its label; there is no boundary", t: "text.secondary, text.link",
    p: [...on("text.secondary", SURFACES), ...on("text.link", ["surface.panel", "surface.base", "surface.raised"])] },
  { c: "Latched toggle: the toolbar's Agent and Inspector toggles, a HUD tool, the drawer's Filter button while a filter is set, a chip that is on (§1.3, §5.2, §5.3, §5.6)", w: "the 1 px boundary against the surface, and the boundary, glyph and label against the fill", t: "pressed.ink",
    p: on("pressed.ink", ["surface.base", "surface.panel", "surface.header", "surface.raised", "pressed.fill"]) },
  { c: "Latched toggle", w: "its fill", t: "pressed.fill", p: [["pressed.fill", "surface.base"]], outside: "a wash, not the carrier: the boundary and the ink carry the state" },
  { c: "Segmented control: the view switch, a table's coordinate switch (§1.3, §5.2)", w: "the trough's boundary and the active segment's boundary", t: "border.control",
    p: on("border.control", ["surface.base", "surface.panel", "surface.sunken"]) },
  { c: "Segmented control", w: "the active segment's fill on the trough", t: "surface.panel", p: [["surface.panel", "surface.sunken"]], outside: "a fill one step from the trough, not the carrier: the segment's boundary carries the state" },
  { c: "Switch: Envelope, Show edits (§5.1, §5.5)", w: "the off track, the on track, and the thumb on each", t: "border.control, accent.fill, surface.panel",
    p: [...on("border.control", ["surface.panel", "surface.header", "surface.raised"]), ...on("accent.fill", ["surface.panel", "surface.header", "surface.raised"]), ["surface.panel", "border.control"], ["surface.panel", "accent.fill"]] },
  { c: "Check box and radio button: a check-box cell, a column menu's option, a dialog's option (§5.1, §5.6)", w: "empty, the 1 px outline; checked or chosen, the fill, and the check or the dot on it", t: "border.control, accent.fill, text.inverse",
    p: [...on("border.control", ["surface.panel", "surface.rowAlt", "surface.raised", "selection.band", "proposal.band"]), ...on("accent.fill", ["surface.panel", "surface.rowAlt", "surface.raised", "selection.band", "proposal.band"]), ["text.inverse", "accent.fill"]] },
  { c: "Tab: the stage's strip, the table drawer's strip, the agent column's tab row (§5.1, §5.3, §5.4)", w: "the active tab's boundary, against the strip and against its own fill; a tab's label", t: "border.control, text.secondary, text.primary",
    p: [...on("border.control", ["surface.panel", "surface.header"]), ["text.secondary", "surface.panel"], ["text.primary", "surface.header"]] },
  { c: "Chip that is a control: a filter chip, the footer's Read-through and Origins switches, the Changed since… control, a term of the combination editor, the legend's range control (§5.1, §5.3, §5.5, §5.6)", w: "its label; on or chosen, the latched form above", t: "text.secondary",
    p: on("text.secondary", ["surface.header", "surface.panel", "surface.raised"]) },
  { c: "Icon-only button and a control's glyph: the footer's selection group, a card's Accept and Reject, the close, collapse and information controls, Undo and Redo, Send, a HUD tool, the expansion chevron, the sort indicator, a menu's check (§3.2, §5.1 to §5.6)", w: "the glyph, on every surface and band it is drawn on and on a hovered row", t: "text.secondary",
    p: on("text.secondary", [...SURFACES, "surface.sunken", "surface.rowAlt", "selection.band", "proposal.band", "historical.tint", "hover.wash/surface.panel", "hover.wash/surface.rowAlt"]) },
  { c: "Raised icon button on the canvas: the compass's Reverse, Place and Cancel (§5.6)", w: "the boundary, against the canvas and against its own fill at rest, hovered and pressed", t: "border.control",
    p: on("border.control", ["canvas.bg", "surface.raised", "hover.wash/surface.raised", "pressed.wash/surface.raised"]) },
  { c: "The compass's axis handles and length field (§5.6)", w: "the handle and its letter; the field's boundary under the focus ring", t: "canvas.axisX, canvas.axisY, canvas.axisZ, border.control",
    p: [["canvas.axisX", "canvas.bg"], ["canvas.axisY", "canvas.bg"], ["canvas.axisZ", "canvas.bg"], ["border.control", "canvas.bg"], ["border.control", "surface.raised"]] },
  { c: "Selection: a table row, a selected cell, an issue row, the rail's stage, the Review outline's row (§1.3, §5.1 to §5.5)", w: "the 3 px bar, and a selected cell's 1 px outline", t: "selection.bar",
    p: on("selection.bar", ["selection.band", "surface.base", "surface.panel"]) },
  { c: "Selection", w: "the band", t: "selection.band", p: [["selection.band", "surface.panel"]], outside: "a fill, not the carrier: the bar carries the selection" },
  { c: "Focus: every control and cell (§1.3)", w: "the 2 px ring", t: "focus.ring",
    p: on("focus.ring", ["surface.panel", "surface.base", "surface.sunken", "surface.header", "surface.raised", "surface.rowAlt", "selection.band", "proposal.band", "canvas.bg"]) },
  { c: "Gutter and marks-column glyphs, which a click opens (§4, §5.1)", w: "the quietest of them, the origin glyph, on a row at rest, hovered, selected and proposed", t: "mark.origin",
    p: on("mark.origin", ["surface.panel", "surface.rowAlt", "surface.header", "selection.band", "proposal.band", "hover.wash/surface.panel", "hover.wash/surface.rowAlt"]) },
  { c: "The offered check and the offered plus in an empty slot (§4, §5.1)", w: "the glyph, on a hovered row and on a band", t: "text.muted",
    p: on("text.muted", ["hover.wash/surface.panel", "hover.wash/surface.rowAlt", "selection.band", "proposal.band"]) },
  { c: "Drag handle on a Review outline row (§5.5)", w: "the glyph", t: "text.secondary", p: [["text.secondary", "surface.panel"]] },
  { c: "Splitter: the split between table and canvas, a drawer's top edge, a docked column's edge (§0, §5.3)", w: "the grip on the regions' hairline", t: "border.control",
    p: on("border.control", ["surface.base", "surface.panel", "surface.header", "canvas.bg"]) },
  { c: "Rail item and the agent strip (§5.2, §5.4)", w: "the icon and its label; the strip's working dot", t: "text.secondary, accent.fill",
    p: [["text.secondary", "surface.base"], ["accent.fill", "surface.base"]] },
  { c: "Status chip with its popover, the Issues count (§2.3, §5.2)", w: "the label on the chip's fill; the count's glyph", t: "status.*Ink, issue.blocking, issue.warning",
    p: [["status.incompleteInk", "status.incompleteFill"], ["status.solvedInk", "status.solvedFill"], ["status.failedInk", "status.failedFill"], ["status.reviewInk", "status.reviewFill"], ["issue.blocking", "surface.base"], ["issue.warning", "surface.base"]] },
  { c: "Select-all control: the gutter's header cell (§5.1)", w: "nothing is drawn; the cell is the target", t: "", p: [], outside: "nothing to measure; whether it needs a drawn form is the pointer rule's question, not this rule's" },
  { c: "Disabled control of any kind, and a table row that cannot be chosen (§1.3, §5.1)", w: "its label, its glyph, the row's text", t: "text.disabled",
    p: on("text.disabled", ["disabled.fill", "surface.panel", "surface.base", "surface.sunken", "surface.header", "surface.raised", "surface.rowAlt"]), outside: "inactive, which the criterion exempts; the disabled ink has its own rule (§2.9)" },
  { c: "Hairlines: between regions and rows, around a card, a popover, an informing chip and an icon-only button", w: "the 1 px line", t: "border.hairline",
    p: on("border.hairline", ["surface.panel", "surface.base"]), outside: "separates and identifies nothing: a chip is identified by its label and an icon-only button by its glyph" },
  { c: "Frames: the table, a drawer, the expansion edge (§1.2, §5.1)", w: "the 1 px frame, the 2 px edge", t: "border.strong",
    p: on("border.strong", ["surface.panel", "surface.base"]), outside: "frames a region and identifies no component" },
  { c: "Display-only expression (§4, §5.1)", w: "the dashed frame", t: "displayOnly.border", p: [["displayOnly.border", "surface.sunken"]], outside: "not a control; the caption and the glyph say what the frame says" },
];

export function sweepRows(T) {
  const C = T.color; const listed = new Set(pairs.map(([fg, bg]) => fg + " | " + bg));
  return sweep.map((s) => {
    for (const [fg, bg] of s.p) if (!listed.has(fg + " | " + bg)) throw new Error("sweep pair is not a row of pairs: " + fg + " on " + bg);
    const at = (theme) => s.p.map(([fg, bg]) => ({ fg, bg, r: ratio(resolve(C, fg, theme), resolve(C, bg, theme)) })).sort((a, b) => a.r - b.r)[0] || null;
    const light = at("light"), dark = at("dark");
    const pass = !!light && light.r >= rules.control && dark.r >= rules.control;
    return { ...s, light, dark, pass, verdict: s.outside ? "outside the rule: " + s.outside : pass ? "pass" : "FAIL" };
  });
}
export function toSweepMarkdown(T) {
  const cell = (m) => m ? `${m.r.toFixed(2)}:1, \`${m.fg}\` on \`${m.bg}\`` : "—";
  const tokens = (t) => t ? t.split(", ").map(t => "\`" + t + "\`").join(", ") : "—";
  return ["| Component | What identifies it or shows its state | Drawn in | Lowest reading, light | Lowest reading, dark | Against 3:1 |", "|---|---|---|---|---|---|",
    ...sweepRows(T).map(r => `| ${r.c} | ${r.w} | ${tokens(r.t)} | ${cell(r.light)} | ${cell(r.dark)} | ${r.verdict} |`)].join("\n");
}
// The rows that fail a rule; empty when the token file meets both.
export function ruleFailures(T) {
  const out = []; const rows = computeRows(T);
  for (const r of sweepRows(T)) if (!r.outside && !r.pass) out.push(`control rule: ${r.c} · ${r.w}: light ${r.light.r.toFixed(2)} on ${r.light.bg}, dark ${r.dark.r.toFixed(2)} on ${r.dark.bg}`);
  const swept = new Set(sweep.flatMap(s => s.p.map(([fg, bg]) => fg + " | " + bg)));
  for (const r of rows) if ((r.role.startsWith("control") || r.role === "focus ring") && !swept.has(r.fg + " | " + r.bg)) out.push(`a ${r.role} row is in no row of the sweep: ${r.fg} on ${r.bg}`);
  for (const r of rows) {
    if (r.role === "text (disabled)" && (r.l < rules.disabledLight || r.d < rules.disabledDark)) out.push(`disabled ink: ${r.fg} on ${r.bg}: light ${r.l.toFixed(2)}, dark ${r.d.toFixed(2)}`);
    if (r.role === "disabled ink beside muted ink" && (r.l < rules.disabledApart || r.d < rules.disabledApart)) out.push(`disabled ink is too near the muted ink: light ${r.l.toFixed(2)}, dark ${r.d.toFixed(2)}`);
  }
  return out;
}

if (process.argv[1] && /contrast\.mjs$/.test(process.argv[1])) {
  const T = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
  const rows = computeRows(T);
  fs.writeFileSync(process.argv[3], toMarkdown(rows) + "\n");
  const lowest = [...rows].sort((a, b) => Math.min(a.l, a.d) - Math.min(b.l, b.d)).slice(0, 16);
  console.log("pairs:", rows.length);
  console.log("lowest (min of the two themes):");
  for (const r of lowest) console.log(`  ${r.fg} on ${r.bg} [${r.role}]  light ${r.l.toFixed(2)}  dark ${r.d.toFixed(2)}`);
  const textRows = rows.filter(r => r.role.startsWith("text") || r.role.includes("chip") || r.role.includes("canvas text") || r.role.includes("button") || r.role.includes("caption") || r.role.includes("band text") || r.role.includes("toggle") && !r.role.includes("fill"));
  console.log("text pairings:", textRows.length, "| lowest text light:", Math.min(...textRows.map(r => r.l)).toFixed(2), "dark:", Math.min(...textRows.map(r => r.d)).toFixed(2));
  const sw = sweepRows(T); const held = sw.filter(r => !r.outside);
  console.log("control rule (" + rules.control + ":1): sweep rows", sw.length, "| held to the rule", held.length, "| outside it", sw.length - held.length, "| lowest held light:", Math.min(...held.map(r => r.light.r)).toFixed(2), "dark:", Math.min(...held.map(r => r.dark.r)).toFixed(2));
  const dis = rows.filter(r => r.role === "text (disabled)");
  console.log("disabled ink (" + rules.disabledLight + ":1 light, " + rules.disabledDark + ":1 dark): rows", dis.length, "| lowest light:", Math.min(...dis.map(r => r.l)).toFixed(2), "dark:", Math.min(...dis.map(r => r.d)).toFixed(2));
  const failures = ruleFailures(T);
  console.log("rule failures:", failures.length); for (const f of failures) console.log("  " + f);
  process.exitCode = failures.length ? 1 : 0;
}
