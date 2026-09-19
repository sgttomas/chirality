// Scratch measurement: the V1.3 (tokens 1.2) and V1.4 (tokens 1.3) readings of the same pairs, by the contrast tool's own arithmetic.
//   node measure.mjs <DESIGN-SYSTEM dir> <tokens 1.2 file> <tokens 1.3 file>
import fs from "node:fs"; import { pathToFileURL } from "node:url"; import path from "node:path";
const [dir, f12, f13] = process.argv.slice(2);
const hex2rgb = (h) => { h = h.replace("#", ""); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)); };
const parseColor = (s) => { if (s.startsWith("#")) return { rgb: hex2rgb(s), a: 1 }; const p = s.match(/rgba?\(([^)]+)\)/)[1].split(",").map(Number); return { rgb: p.slice(0, 3), a: p.length > 3 ? p[3] : 1 }; };
const over = (c, b) => c.rgb.map((v, i) => Math.round(c.a * v + (1 - c.a) * b.rgb[i]));
const lum = (rgb) => { const [r, g, b] = rgb.map(v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const ratio = (fg, bg) => { const [hi, lo] = [lum(fg), lum(bg)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05); };
const resolve = (C, name, theme) => { let acc = { rgb: [255, 255, 255], a: 1 }; for (const p of name.split("/").reverse()) { const v = C[p]?.[theme] ?? (p.startsWith("#") ? p : null); if (!v) throw new Error("unknown " + p); acc = { rgb: over(parseColor(v), acc), a: 1 }; } return acc.rgb; };
const T12 = JSON.parse(fs.readFileSync(f12, "utf8")).color, T13 = JSON.parse(fs.readFileSync(f13, "utf8")).color;
const r = (C, fg, bg) => ["light", "dark"].map(t => ratio(resolve(C, fg, t), resolve(C, bg, t)).toFixed(2) + ":1").join(" / ");
const out = [];
const table = (title, rows) => { out.push("", "### " + title, "", "| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |", "|---|---|---|---|---|"); for (const [part, fg12, fg13, bg] of rows) out.push(`| ${part}, on \`${bg}\` | \`${fg12}\` | ${fg12 === "—" ? "—" : r(T12, fg12, bg)} | \`${fg13}\` | ${r(T13, fg13, bg)} |`); };
const surf = ["surface.panel", "surface.base", "surface.sunken", "surface.header", "surface.raised", "surface.rowAlt", "canvas.bg", "selection.band", "proposal.band", "stale.band"];
table("The control boundary on every surface and band", surf.map(b => ["boundary", "border.strong", "border.control", b]));
table("The control boundary on its own fill under the washes", ["hover.wash/surface.panel", "hover.wash/surface.sunken", "hover.wash/surface.raised", "pressed.wash/surface.panel", "pressed.wash/surface.sunken", "pressed.wash/surface.raised"].map(b => ["boundary", "border.strong", "border.control", b]));
table("Switch", [["off track", "border.strong", "border.control", "surface.panel"], ["off track", "border.strong", "border.control", "surface.header"], ["off track", "border.strong", "border.control", "surface.raised"]]);
out.push("", "Thumb on the off track: V1.3 `surface.panel` on `border.strong` " + r(T12, "surface.panel", "border.strong") + "; V1.4 `surface.panel` on `border.control` " + r(T13, "surface.panel", "border.control") + ".");
table("Segmented control, active segment", [["segment edge against the trough", "surface.panel", "border.control", "surface.sunken"]]);
table("Latched toggle: what marks its edge", ["surface.base", "surface.panel", "surface.header", "surface.raised"].map(b => ["edge", "pressed.fill", "pressed.ink", b]));
table("A chip that is on or chosen: what marks it", [["chosen filter chip (specimen)", "status.solvedFill", "pressed.ink", "surface.header"], ["chosen filter chip (specimen)", "status.solvedFill", "pressed.ink", "surface.panel"], ["chip that is on (frames)", "selection.band", "pressed.ink", "surface.header"], ["chip that is on (frames)", "selection.band", "pressed.ink", "surface.panel"]]);
table("Active tab (frames)", [["boundary", "border.strong", "border.control", "surface.panel"], ["boundary against its fill", "border.strong", "border.control", "surface.header"]]);
table("Check box (frames)", [["outline", "border.strong", "border.control", "surface.raised"], ["outline", "border.strong", "border.control", "surface.panel"]]);
table("Quiet inks on a hovered band, which V1.4 no longer draws (the wash is not added to a band)", [["origin glyph", "mark.origin", "mark.origin", "hover.wash/selection.band"], ["origin glyph", "mark.origin", "mark.origin", "hover.wash/proposal.band"]]);
out.push("", "V1.4 draws the same glyph on the band without the wash: `mark.origin` on `selection.band` " + r(T13, "mark.origin", "selection.band") + ", on `proposal.band` " + r(T13, "mark.origin", "proposal.band") + ".");
out.push("", "### The disabled ink", "", "| On | 1.2 `" + T12["text.disabled"].light + "` / `" + T12["text.disabled"].dark + "` | 1.3 `" + T13["text.disabled"].light + "` / `" + T13["text.disabled"].dark + "` | `text.muted` there | `text.secondary` there |", "|---|---|---|---|---|");
for (const b of ["disabled.fill", "surface.panel", "surface.base", "surface.sunken", "surface.header", "surface.raised", "surface.rowAlt"]) out.push(`| \`${b}\` | ${r(T12, "text.disabled", b)} | ${r(T13, "text.disabled", b)} | ${r(T13, "text.muted", b)} | ${r(T13, "text.secondary", b)} |`);
out.push(`| beside \`text.muted\` (ink to ink) | ${r(T12, "text.disabled", "text.muted")} | ${r(T13, "text.disabled", "text.muted")} | | |`, `| beside \`text.secondary\` (ink to ink) | ${r(T12, "text.disabled", "text.secondary")} | ${r(T13, "text.disabled", "text.secondary")} | | |`);
// options for ROOT: keep, the recommended lift, 3:1 everywhere in light, the product's present ink
const { H } = await import(pathToFileURL(path.join(path.resolve(dir), "tools/palette.mjs")).href);
const opts = [["keep (1.2)", T12["text.disabled"].light, T12["text.disabled"].dark], ["lift, recommended (1.3)", T13["text.disabled"].light, T13["text.disabled"].dark], ["3:1 everywhere in light", H(0.62, 0.010, 250), T13["text.disabled"].dark], ["the product's present ink (B1-TOKENS)", "#667680", "#9baab2"]];
out.push("", "### The options", "", "| Option | Light | on `disabled.fill` | lowest on a surface | highest on a surface | beside `text.muted` | Dark | on `disabled.fill` | lowest on a surface | highest on a surface | beside `text.muted` |", "|---|---|---|---|---|---|---|---|---|---|---|");
const surfs = ["surface.panel", "surface.base", "surface.sunken", "surface.header", "surface.raised", "surface.rowAlt"];
for (const [name, l, d] of opts) { const cell = (hex, theme) => { const rs = surfs.map(s => ratio(hex2rgb(hex), resolve(T13, s, theme))); return [`\`${hex}\``, ratio(hex2rgb(hex), resolve(T13, "disabled.fill", theme)).toFixed(2) + ":1", Math.min(...rs).toFixed(2) + ":1", Math.max(...rs).toFixed(2) + ":1", ratio(hex2rgb(hex), resolve(T13, "text.muted", theme)).toFixed(2) + ":1"]; }; out.push(`| ${name} | ${cell(l, "light").join(" | ")} | ${cell(d, "dark").join(" | ")} |`); }
console.log(out.join("\n"));
