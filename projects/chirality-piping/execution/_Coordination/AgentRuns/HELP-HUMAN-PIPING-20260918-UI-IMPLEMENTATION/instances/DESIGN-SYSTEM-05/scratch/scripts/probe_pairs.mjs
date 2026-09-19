// The contrast tool's own arithmetic (8-bit rounded compositing), for pairs the tool does not list.
import fs from "node:fs";
const T = JSON.parse(fs.readFileSync(process.argv[2], "utf8")).color;
const hex2rgb = (h) => { h = h.replace("#", ""); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)); };
const parseColor = (s) => { if (s.startsWith("#")) return { rgb: hex2rgb(s), a: 1 }; const p = s.match(/rgba?\(([^)]+)\)/)[1].split(",").map(Number); return { rgb: p.slice(0, 3), a: p.length > 3 ? p[3] : 1 }; };
const over = (c, b) => c.rgb.map((v, i) => Math.round(c.a * v + (1 - c.a) * b.rgb[i]));
const lum = (rgb) => { const [r, g, b] = rgb.map(v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const ratio = (fg, bg) => { const [hi, lo] = [lum(fg), lum(bg)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05); };
const resolve = (name, theme) => { let acc = { rgb: [255, 255, 255], a: 1 }; for (const p of name.split("/").reverse()) { const v = T[p]?.[theme]; if (!v) throw new Error("unknown " + p); acc = { rgb: over(parseColor(v), acc), a: 1 }; } return acc.rgb; };
const r = (fg, bg) => ["light", "dark"].map(t => ratio(resolve(fg, t), resolve(bg, t)).toFixed(2)).join(" / ");
const groups = JSON.parse(process.argv[3]);
for (const [fg, bgs] of groups) for (const bg of bgs) console.log((fg + " on " + bg).padEnd(62), r(fg, bg));
