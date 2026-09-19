// Read-only scan of the frames (MOCKS/frames): the rules of the frames' stylesheet that use border.strong, and, frame by
// frame, how many times each control boundary drawn in border.strong occurs, with the other forms V1.4 changes.
//   node frames_scan.mjs <frames dir>
import fs from "node:fs"; import path from "node:path";
const dir = process.argv[2];
const css = fs.readFileSync(path.join(dir, "mocks.css"), "utf8").replace(/\/\*[\s\S]*?\*\//g, "");
const strongRules = [...css.matchAll(/([^{}]+)\{([^{}]*)\}/g)].filter(m => m[2].includes("--border-strong")).map(m => m[1].trim().replace(/\s+/g, " "));
const control = [".seg", ".btn", ".input", ".combo", ".switch i", ".tblhead .switch.off i", ".search", ".lenfield", ".tabs .tab.on", ".maprow .m .sel", ".pop .row .k", ".iconbtn.raised", ".sendrow"];
console.log("Rules of mocks.css that use border.strong: " + strongRules.length);
console.log("  draw a control's boundary (move to border.control): " + strongRules.filter(r => control.includes(r)).join(", "));
console.log("  frame a region and identify nothing (stay): " + strongRules.filter(r => !control.includes(r)).join(", "));
const count = (s, re) => (s.match(re) || []).length;
const inside = (s, open, re) => [...s.matchAll(open)].reduce((n, m) => n + count(m[1], re), 0);
const cols = [
  [".seg", s => count(s, /class="seg[" ]/g)],
  [".btn bordered", s => count(s, /class="btn(?![^"]*\b(?:primary|text)\b)[^"]*"/g)],
  [".input", s => count(s, /class="input[" ]/g)],
  [".combo", s => count(s, /class="combo[" ]/g)],
  ["switch off", s => count(s, /class="switch(?: off)?"/g)],
  [".search", s => count(s, /class="search[" ]/g)],
  [".lenfield", s => count(s, /class="lenfield[" ]/g)],
  [".tabs .tab.on", s => count(s, /class="tab on"/g)],
  [".maprow .m .sel", s => inside(s, /<div class="maprow[^"]*"[^>]*>([\s\S]*?)<\/div>/g, /class="sel"/g)],
  [".pop .row .k empty", s => count(s, /<span class="k"><\/span>/g)],
  [".iconbtn.raised", s => count(s, /class="iconbtn raised[" ]/g)],
  [".sendrow", s => count(s, /class="sendrow[" ]/g)],
  ["latched .btn", s => count(s, /class="btn[^"]*\blatched\b[^"]*"/g)],
  ["latched HUD tool", s => inside(s, /<div class="hud[^"]*"[^>]*>([\s\S]*?)<\/div>/g, /aria-pressed="true"/g)],
  [".iconbtn.on", s => count(s, /class="iconbtn[^"]*\bon\b[^"]*"/g)],
  [".chip.outline.on", s => count(s, /class="chip outline on"/g)],
  ["agent tab on", s => inside(s, /<div class="tabs"[^>]*>([\s\S]*?)<\/div>/g, /<span class="on"/g)],
  [".outline div.on", s => inside(s, /<div class="outline"[^>]*>([\s\S]*?)<div class="note"/g, /<div class="on">/g)],
];
console.log("\n| Frame | " + cols.map(c => c[0]).join(" | ") + " |\n|---|" + cols.map(() => "---").join("|") + "|");
for (const f of fs.readdirSync(dir).filter(f => f.endsWith(".html")).sort()) { const s = fs.readFileSync(path.join(dir, f), "utf8"); console.log("| `" + f + "` | " + cols.map(([, fn]) => fn(s) || "·").join(" | ") + " |"); }
