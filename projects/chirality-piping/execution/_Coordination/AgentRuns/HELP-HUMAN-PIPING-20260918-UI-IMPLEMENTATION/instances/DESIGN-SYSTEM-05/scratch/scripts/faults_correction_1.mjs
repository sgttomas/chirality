// Injected-fault test of agree.mjs for correction 1 to V1.4: each fault is applied to a fresh copy of the three files; agree.mjs must name it.
//   node faults_correction_1.mjs <DESIGN-SYSTEM dir> <work dir outside the repository>
import fs from "node:fs"; import path from "node:path"; import { execFileSync } from "node:child_process";
const [ds, work] = process.argv.slice(2);
const files = { doc: "DESIGN_SYSTEM_V1.md", tok: "tokens.json", spec: "specimen.html" };
const faults = [
  ["none (the files as they are)", null, null, null, /^$/],
  ["specimen: the row demo's disabled row back on disabled.fill", "spec", `.rowdemo .dis { color: var(--text-disabled); }`, `.rowdemo .dis { color: var(--text-disabled); background: var(--disabled-fill); }`, /row demo draws the disabled row with a fill/],
  ["specimen: the disabled-row rule given a fill", "spec", `table.ds tr.offrow td, table.ds tr.offrow td.sec { color: var(--text-disabled); }`, `table.ds tr.offrow td, table.ds tr.offrow td.sec { color: var(--text-disabled); background: var(--disabled-fill); }`, /disabled-row rule, or the rule draws a fill/],
  ["specimen: a disabled cell drawn by an inline style again", "spec", `<tr class="offrow"><td>A-05</td><td class="n">105.0</td>`, `<tr class="offrow"><td style="color:var(--text-disabled)">A-05</td><td class="n">105.0</td>`, /disabled cell by an inline style/],
  ["specimen: a disabled row that is also selected", "spec", `<tr class="offrow"><td>A-04</td>`, `<tr class="offrow sel"><td>A-04</td>`, /disabled row on a band/],
  ["specimen: the stepper loses its fill", "spec", `overflow: hidden; background: var(--surface-sunken); }`, `overflow: hidden; }`, /no fill of its own among the three: \.stepper/],
  ["specimen: a bordered button on the bare base", "spec", `border: 1px solid var(--border-control); background: var(--surface-panel); color: var(--text-primary); font: inherit; font-weight: 500;`, `border: 1px solid var(--border-control); background: var(--surface-base); color: var(--text-primary); font: inherit; font-weight: 500;`, /no fill of its own among the three: \.btn/],
  ["document: the Disabled cell state without what it sits on", "doc", "| Disabled | `text.disabled` on the row surface and nothing else;", "| Disabled | `text.disabled`;", /Disabled cell state does not say what the row sits on/],
  ["document: a word changed in row 115", "doc", `| 115 | `, `| 115 | Changed. `, /rows 1 to 120 differ/],
  ["document: row 121 no longer cites finding 1", "doc", `| correction 1 to brief DESIGN-SYSTEM-05, finding 1 (DS5-REVIEW) |`, `| correction 1 to brief DESIGN-SYSTEM-05 (DS5-REVIEW) |`, /do not cite finding 1 as a row.s source/],
  ["document: row 123 removed", "doc", /\n\| 123 \|[^\n]*/, ``, /lacks correction 1's rows/],
];
let failed = 0;
for (const [name, which, find, repl, expect] of faults) {
  fs.rmSync(work, { recursive: true, force: true }); fs.mkdirSync(work, { recursive: true });
  for (const f of Object.values(files)) fs.copyFileSync(path.join(ds, f), path.join(work, f));
  if (which) { const p = path.join(work, files[which]); const s = fs.readFileSync(p, "utf8"); const n = find instanceof RegExp ? (s.match(new RegExp(find.source, "g")) || []).length : s.split(find).length - 1; if (n !== 1) { console.log("FAULT NOT APPLIED (anchor count " + n + "): " + name); failed++; continue; } fs.writeFileSync(p, s.replace(find, () => repl)); }
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
