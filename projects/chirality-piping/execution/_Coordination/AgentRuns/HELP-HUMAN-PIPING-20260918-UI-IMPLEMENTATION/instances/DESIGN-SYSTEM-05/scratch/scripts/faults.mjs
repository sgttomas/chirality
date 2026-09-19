// Injected-fault test of agree.mjs: each fault is applied to a fresh copy of the three files; agree.mjs must name it.
//   node faults.mjs <DESIGN-SYSTEM dir> <work dir>
import fs from "node:fs"; import path from "node:path"; import { execFileSync } from "node:child_process";
const [ds, work] = process.argv.slice(2);
const files = { doc: "DESIGN_SYSTEM_V1.md", tok: "tokens.json", spec: "specimen.html" };
const faults = [
  ["none (the files as they are)", null, null, null, /^$/],
  ["tokens: border.control light set to border.strong's value", "tok", `"border.control": {\n      "light": "#777e85"`, `"border.control": {\n      "light": "#b3b8be"`, /rule failure: control rule/],
  ["tokens: text.disabled light back to the 1.2 value", "tok", `"light": "#8f949a"`, `"light": "#a6abb1"`, /rule failure: disabled ink/],
  ["tokens: text.disabled light raised onto text.muted", "tok", `"light": "#8f949a"`, `"light": "#7f868d"`, /too near the muted ink/],
  ["specimen: .btn boundary drawn in border.strong", "spec", `.btn { height: 26px; padding: 0 10px; border-radius: var(--radius-control); border: 1px solid var(--border-control);`, `.btn { height: 26px; padding: 0 10px; border-radius: var(--radius-control); border: 1px solid var(--border-strong);`, /draws a control in border\.strong: \.btn/],
  ["specimen: the off track drawn in border.strong", "spec", `border-radius: 8px; background: var(--border-control);`, `border-radius: 8px; background: var(--border-strong);`, /draws a control in border\.strong: \.switch i/],
  ["specimen: the latched toggle loses its boundary", "spec", `.btn.latched { background: var(--pressed-fill); color: var(--pressed-ink); border-color: var(--pressed-ink); }`, `.btn.latched { background: var(--pressed-fill); color: var(--pressed-ink); border-color: transparent; }`, /latched form has no pressed\.ink boundary: \.btn\.latched/],
  ["specimen: a compass button stroked in border.strong", "spec", `<rect x="1141" y="119" width="22" height="22" rx="3" fill="var(--surface-raised)" stroke="var(--border-control)"/>`, `<rect x="1141" y="119" width="22" height="22" rx="3" fill="var(--surface-raised)" stroke="var(--border-strong)"/>`, /figure strokes a control in border\.strong/],
  ["specimen: a chosen filter chip back on a status fill", "spec", `<span class="chip on">All 4</span><span class="chip outline">Open 3</span><span class="chip outline">Resolved 1</span>`, `<span class="chip solved">All 4</span><span class="chip outline">Open 3</span><span class="chip outline">Resolved 1</span>`, /chosen sits on a status fill/],
  ["specimen: the outline's selected row loses its bar", "spec", `.outline div.on { background: var(--selection-band); box-shadow: inset 3px 0 0 var(--selection-bar); }`, `.outline div.on { background: var(--selection-band); }`, /outline's selected row has no selection bar/],
  ["specimen: the heading still V1.3", "spec", `specimen V1.4</h1>`, `specimen V1.3</h1>`, /still names V1\.3/],
  ["document: a word changed in row 100", "doc", `| 100 | `, `| 100 | Changed. `, /rows 1 to 112 differ/],
  ["document: a reading changed in the control rule's table", "doc", `| 3.17:1, \`border.control\` on \`pressed.wash/surface.sunken\` |`, `| 3.71:1, \`border.control\` on \`pressed.wash/surface.sunken\` |`, /control rule table differs/],
  ["document: row 118 no longer cites the brief's item 3", "doc", `| brief item 3 |`, `| the brief |`, /do not cite brief item 3/],
  ["document: a contrast row's value changed", "doc", `| \`border.control\` | \`surface.panel\` | control boundary | 4.11:1 |`, `| \`border.control\` | \`surface.panel\` | control boundary | 4.12:1 |`, /contrast table differs/],
];
let failed = 0;
for (const [name, which, find, repl, expect] of faults) {
  fs.rmSync(work, { recursive: true, force: true }); fs.mkdirSync(work, { recursive: true });
  for (const f of Object.values(files)) fs.copyFileSync(path.join(ds, f), path.join(work, f));
  if (which) { const p = path.join(work, files[which]); const s = fs.readFileSync(p, "utf8"); if (s.split(find).length !== 2) { console.log("FAULT NOT APPLIED (anchor count " + (s.split(find).length - 1) + "): " + name); failed++; continue; } fs.writeFileSync(p, s.replace(find, () => repl)); }
  let out = ""; let code = 0;
  try { out = execFileSync("node", [path.join(ds, "tools/agree.mjs"), path.join(work, files.doc), path.join(work, files.tok), path.join(work, files.spec)], { encoding: "utf8" }); } catch (e) { out = e.stdout || ""; code = e.status; }
  const problems = JSON.parse(out).problems;
  const ok = which ? (code === 1 && problems.some(p => expect.test(p))) : (code === 0 && problems.length === 0);
  if (!ok) failed++;
  console.log((ok ? "caught   " : "MISSED   ") + name + " -> exit " + code + ", " + problems.length + " problem(s)" + (problems.length ? ": " + problems.slice(0, 3).map(p => p.slice(0, 110)).join(" || ") : ""));
}
fs.rmSync(work, { recursive: true, force: true });
console.log(failed ? failed + " fault(s) not caught" : "every fault caught; the unmodified files pass");
process.exitCode = failed ? 1 : 0;
