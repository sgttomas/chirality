// Renders the specimen with a headless Chromium (Playwright from the piping project's node_modules, used read-only),
// with every non-file request blocked, in light and dark (system preference emulation and the manual switch),
// at 1440 and 720 wide. Writes per-section PNGs and a JSON report of layout facts.
//   node render.mjs <path to specimen.html> [out dir, default ./shots] [--playwright-from <dir>]
// Playwright is resolved from the piping project's package.json by relative path; when this instance sits in a
// checkout whose node_modules is not installed, pass --playwright-from <dir> (or set PLAYWRIGHT_FROM) at run time
// to name a directory that has it. The location is never stored in this file.
// V1.1 adds checks for the revision's elements: the stale band, the disabled case selector, the latched toggle,
// the draft row and draft ghost, the geometry strips, the run log, the banner, the outline's registered row,
// the data bar's track, and that the page's pair list is the embedded one.
// V1.2 adds: the label chips redrawn from the label table and equal to it, the label table's eight rows, the wrapped
// HUD's size, the toast's width, the Review header's icons and plain Export, the three run standings, the five
// agent card classes, the edge steps, and that the rendered text carries none of the retired strings.
// V1.3 adds: the menus and their widths, the run text button, the wrapped 737 px header, the stress components
// block, the drawer's one-line header, the units buttons, the edit chip's and the paste band's button faces.
// V1.4 adds the control rule as the browser resolves it: for every control sample on the page, the colour of what
// identifies it (its boundary, its fill where it has no boundary, a switch's track and thumb, the splitter's grip,
// the compass's stroked buttons) against its own fill and against the surface around it, as WCAG 2.x ratios, with
// the lowest reading and every reading under 3:1; that no control's boundary resolves to border.strong; and the
// ink of every disabled sample against its fill, held to the ratio stated in contrast.mjs. Exits 1 if any fails.
// Correction 1 to V1.4 adds, counted apart from the disabled controls: the ink of every cell of a row that cannot be
// chosen (the table's Disabled state) against the fill it shows, held to the same stated ratio, and that the fill is a
// row surface (surface.panel or surface.rowAlt), never a band or a wash; and that every control which carries the
// boundary and is washed has an opaque fill of its own, one of surface.panel, surface.sunken and surface.raised.
import { pathToFileURL } from "node:url";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import { rules } from "./contrast.mjs";
const args = process.argv.slice(2); const fromAt = args.indexOf("--playwright-from");
const from = fromAt >= 0 ? args.splice(fromAt, 2)[1] : process.env.PLAYWRIGHT_FROM;
const require = createRequire(from ? pathToFileURL(path.join(path.resolve(from), "package.json")) : new URL("../../../../../../../package.json", import.meta.url));
const { chromium } = require("playwright");
const file = pathToFileURL(path.resolve(args[0])).href;
const outDir = args[1] || "shots";
fs.mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
const report = {};
const sections = ["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12"];
for (const width of [1440, 720]) {
  for (const scheme of ["light", "dark"]) {
    const ctx = await browser.newContext({ viewport: { width, height: 900 }, colorScheme: scheme, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    const net = []; const errors = [];
    await page.route("**/*", (route) => { const u = route.request().url(); if (u.startsWith("file://")) return route.continue(); net.push(u); return route.abort(); });
    page.on("console", (m) => { if (m.type() === "error" || m.type() === "warning") errors.push(m.type() + ": " + m.text()); });
    page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
    await page.goto(file, { waitUntil: "load" });
    await page.waitForTimeout(150);
    const facts = await page.evaluate((rules) => {
      const cs = getComputedStyle(document.documentElement);
      const small = [...document.querySelectorAll("body *")].filter(e => e.children.length === 0 && e.textContent.trim() && getComputedStyle(e).display !== "none").map(e => parseFloat(getComputedStyle(e).fontSize));
      const tok = JSON.parse(document.getElementById("tokens").textContent);
      const pairs = JSON.parse(document.getElementById("pairs").textContent);
      const v = (k) => cs.getPropertyValue("--" + k.replace(/\./g, "-")).trim();
      const theme = cs.colorScheme.includes("dark") ? "dark" : "light";
      const draftGhost = document.querySelector('.figure path[stroke="var(--canvas-draft)"][stroke-dasharray="6 4"]');
      return {
        scrollWidth: document.documentElement.scrollWidth, innerWidth, scrollHeight: document.documentElement.scrollHeight,
        colorScheme: cs.colorScheme, bg: getComputedStyle(document.body).backgroundColor, textPrimary: v("text.primary"),
        tokRows: document.querySelectorAll("#tokgrid tbody tr").length, tokCount: Object.keys(tok.color).length, tokVersion: tok.version,
        ctRows: document.querySelectorAll("#ctable tbody tr").length, pairsEmbedded: pairs.length,
        minFont: Math.min(...small), fontsBelow11: small.filter(s => s < 11).length,
        overflowing: [...document.querySelectorAll(".panel, .card, .probe, .legend, .shell, .tblwrap")].filter(e => e.scrollWidth > e.clientWidth + 1 && !e.classList.contains("tblwrap")).map(e => (e.id || e.className) + " " + e.scrollWidth + ">" + e.clientWidth).slice(0, 10),
        v11: {
          heading: document.querySelector("h1").textContent,
          staleband: !!document.querySelector(".staleband"), stalebandBg: document.querySelector(".staleband") && getComputedStyle(document.querySelector(".staleband")).backgroundColor,
          caseAllDisabled: !!document.querySelector(".combo.disabled"), caseAllText: document.querySelector(".combo.disabled")?.textContent.trim(),
          latched: document.querySelectorAll(".btn.latched").length, latchedBg: document.querySelector(".btn.latched") && getComputedStyle(document.querySelector(".btn.latched")).backgroundColor,
          draftRow: !!document.querySelector("table.ds tr.draft"), draftBar: document.querySelector("table.ds tr.draft td.gut") && getComputedStyle(document.querySelector("table.ds tr.draft td.gut"), "::before").borderLeftStyle,
          draftGhost: !!draftGhost, draftGhostWidth: draftGhost && draftGhost.getAttribute("stroke-width"),
          hintStrip: !!document.querySelector('.figure rect[fill="var(--canvas-hint)"]'),
          geoStrips: document.querySelectorAll(".geo").length, runlog: !!document.querySelector(".runlog"), banner: !!document.querySelector(".banner"),
          railCaptionStale: document.querySelector(".rail .cap.stale") && getComputedStyle(document.querySelector(".rail .cap.stale")).color,
          signoffRow: [...document.querySelectorAll(".outline div")].some(d => d.textContent.includes("Review/signoff block")),
          reportPreview: [...document.querySelectorAll("button")].some(b => b.textContent.trim() === "Report preview"),
          barTrack: document.querySelector(".bar") && getComputedStyle(document.querySelector(".bar")).backgroundColor,
          combinationEditor: [...document.querySelectorAll(".expand")].some(e => e.textContent.includes("Combination editor")),
          v12: (() => {
            const LAB = tok.labels; const q = (s) => document.querySelector(s); const qa = (s) => [...document.querySelectorAll(s)];
            const chips = qa(".chip.lbl[data-label]"); const text = document.body.innerText.toLowerCase();
            const retired = [["pip", "ing designer"], ["open", "pipestress"], ["cae", "pipe"], ["technical ", "preview"], ["not a released ", "product"], ["decision-support ", "information"], ["remain with the responsible ", "engineer"]].map(p => p.join(""));
            const wrap = q(".hud.wrap")?.getBoundingClientRect(); const narrowHud = q(".narrow .hud")?.getBoundingClientRect(); const narrow = q(".narrow")?.getBoundingClientRect();
            return {
              labelChips: chips.length,
              labelChipsEqualTable: chips.every(c => { const r = LAB[c.dataset.label]; return r && c.textContent === r.domain + "·" + r.label && c.title === c.dataset.label && c.classList.contains(r.chip); }),
              labelTableRows: qa("#labeltable tbody tr").length,
              wrappedHud: wrap && { w: Math.round(wrap.width), h: Math.round(wrap.height), tools: qa(".hud.wrap")[0].children.length, first: qa(".hud.wrap")[0].children[0].title },
              narrowHudInside: narrow && narrowHud && narrowHud.right <= narrow.right && narrowHud.left >= narrow.left,
              toastWidth: q(".toast") && Math.round(q(".toast").getBoundingClientRect().width), toastExpected: tok.layout["toast.width"],
              reviewHeaderIcons: ["Snapshot…", "Report preview", "Export…"].map(n => { const b = qa("#s10 ~ .panel button, button").find(x => x.textContent.trim() === n); return !!(b && b.querySelector("svg")); }),
              exportIsPlain: q("#exportbtn") && !q("#exportbtn").classList.contains("primary"),
              accentButtonsOnReviewHeader: qa("#exportbtn").length && [...q("#exportbtn").parentElement.querySelectorAll(".btn.primary")].length,
              histband: q(".histband")?.textContent.replace(/\s+/g, " ").trim(), runIdentityButtons: qa("button").filter(b => b.textContent.trim() === "Run identity").length,
              legendNoteCards: qa(".legend").filter(l => l.textContent.includes("No result colour on the current model")).length,
              agentClasses: [...new Set(qa("[data-agent-class]").map(e => e.dataset.agentClass))].sort(), agentClassChips: qa("#agentclasses .chip").map(c => c.textContent),
              edgeSteps: qa("#edgesteps div").map(d => d.title), edgeNote: q("#edgenote")?.textContent.length > 0,
              addRow: !!q("tr.addrow"), selGroupButtons: qa(".selgroup button").length, editChip: !!q(".editchip"), sendControl: !!q(".sendrow button"), issueRowTruncates: (() => { const m = q(".issuerow.sel .msg"); return m ? m.scrollWidth > m.clientWidth : null; })(),
              v13: { menus: qa(".menu").map(m => m.getAttribute("aria-label") + " " + Math.round(m.getBoundingClientRect().width)), runTextButtons: qa(".runtext").length, wrappedHeaderLines: (() => { const h = qa(".tblwrap").find(w => w.style.width === "737px")?.querySelector(".tblhead"); return h ? Math.round(h.getBoundingClientRect().height) : null; })(), stressComponents: qa(".expand").some(e => e.textContent.includes("Stress components")), drawerHeadOneLine: q(".drawerhead") && Math.round(q(".drawerhead").getBoundingClientRect().height), unitsButtons: qa(".unitsbtn").map(b => b.textContent.trim() + " " + Math.round(b.getBoundingClientRect().width)), editChipButtons: qa(".editchip button").map(b => b.textContent.trim()), pasteButtons: qa(".pasteband button").map(b => b.textContent.trim()), commitAsCopy: qa("button").filter(b => /commit/i.test(b.textContent)).length, reviewWhenChips: qa("#s10 ~ .panel .demo-row .chip.lbl").length },
              retiredFound: retired.filter(r => text.includes(r)),
            };
          })(),
          expected: { staleBand: tok.color["stale.band"][theme], pressedFill: tok.color["pressed.fill"][theme], captionStale: tok.color["rail.captionStale"][theme], barTrack: tok.color["bar.track"][theme] }
        },
        v14: (() => {
          const parse = (s) => { s = s || ""; if (s[0] === "#") return { rgb: [1, 3, 5].map(i => parseInt(s.slice(i, i + 2), 16)), a: 1 }; const m = s.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[,\s\/]+/).filter(Boolean).map(Number); return { rgb: p.slice(0, 3), a: p.length > 3 ? p[3] : 1 }; };
          const over = (c, b) => c.rgb.map((x, i) => c.a * x + (1 - c.a) * b[i]);
          const lum = (rgb) => { const [r, g, b] = rgb.map(x => { x /= 255; return x <= 0.04045 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4; }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
          const ratio = (a, b) => { const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05); };
          // the opaque colour an element shows as its fill: its own wash and background over those of its ancestors
          const fillOf = (el) => { const stack = []; for (let n = el; n; n = n.parentElement) { const s = getComputedStyle(n); const g = s.backgroundImage.startsWith("linear-gradient(") ? parse(s.backgroundImage) : null; if (g) stack.push(g); const c = parse(s.backgroundColor); if (c && c.a > 0) { stack.push(c); if (c.a === 1) break; } } let acc = [255, 255, 255]; for (const c of stack.reverse()) acc = over(c, acc); return acc; };
          const solid = (s, under) => { const c = parse(s); return c ? over(c, under) : null; };
          const shown = (el) => el.getClientRects().length > 0;
          const where = (el) => { const srf = el.closest(".srf"); const lab = srf && srf.querySelector(".lab"); const sec = (() => { let n = el; while (n && n.parentElement && n.parentElement.tagName !== "MAIN") n = n.parentElement; while (n && n.tagName !== "H2") n = n.previousElementSibling; return n ? n.id : ""; })(); return (lab ? lab.textContent.trim() + " strip" : sec) + " · " + (el.textContent || "").replace(/\s+/g, " ").trim().slice(0, 24); };
          const readings = []; const strong = solid(tok.color["border.strong"][theme], [255, 255, 255]).map(Math.round).join(",");
          const take = (kind, el, mark, fills) => { for (const [against, fill] of fills) readings.push({ kind, where: where(el), against, ratio: Math.round(ratio(mark, fill) * 100) / 100, strong: mark.map(Math.round).join(",") === strong }); };
          const bounded = ['.seg', '.seg button[aria-pressed="true"]', '.btn:not(.primary):not(.text):not([disabled]):not(.disabled)', '.input', '.combo:not(.disabled)', '.search', '.sendrow', '.stepper', '.maprow .m .sel', '.cb:not(.on)', '.rb:not(.on)', '.tab.on', '.iconbtn.raised', '.iconbtn.latched', '.lenfield', '.chip.on', '.hud button[aria-pressed="true"]'];
          for (const sel of bounded) for (const el of qa2(sel)) { if (!shown(el)) continue; const own = fillOf(el); take("boundary " + sel, el, solid(getComputedStyle(el).borderTopColor, own), [["its own fill", own], ["the surface around it", fillOf(el.parentElement)]]); }
          for (const el of qa2(".btn.primary:not([disabled])")) if (shown(el)) take("fill .btn.primary", el, fillOf(el), [["the surface around it", fillOf(el.parentElement)]]);
          for (const el of qa2(".cb.on, .rb.on")) if (shown(el)) { const own = fillOf(el); take("fill " + (el.classList.contains("cb") ? ".cb.on" : ".rb.on"), el, own, [["the surface around it", fillOf(el.parentElement)], ["the check or the dot on it", solid(getComputedStyle(el).color, own)]]); }
          for (const el of qa2(".switch i")) { if (!shown(el)) continue; const track = fillOf(el); take("track .switch" + (el.parentElement.classList.contains("on") ? ".on" : ""), el.parentElement, track, [["the surface around it", fillOf(el.parentElement)], ["its thumb", solid(getComputedStyle(el, "::after").backgroundColor, track)]]); }
          for (const el of qa2(".splitdemo .split i")) { const sp = el.parentElement; const sides = [sp.previousElementSibling, sp.nextElementSibling].flatMap(n => n.classList.contains("col") ? [...n.querySelectorAll(".rg")] : [n]); take("grip " + sp.className, el, fillOf(el), sides.map(n => [n.textContent.trim(), fillOf(n)])); }
          for (const el of qa2('.figure rect[stroke="var(--border-control)"]')) { const s = getComputedStyle(el); const around = fillOf(el.ownerSVGElement); const own = solid(s.fill, around); take("stroke compass", el.parentElement, solid(s.stroke, own), [["its own fill", own], ["the canvas", around]]); }
          const held = readings; const under = held.filter(r => r.ratio < rules.control); const lowest = [...held].sort((a, b) => a.ratio - b.ratio)[0];
          const disabled = [];
          for (const el of qa2('.btn[disabled], .btn.disabled, .combo.disabled, .iconbtn[disabled], .hud button[disabled], .menu .mi.dis, .rail .it.off')) { if (!shown(el)) continue; const fill = fillOf(el); disabled.push({ where: where(el), ratio: Math.round(ratio(solid(getComputedStyle(el).color, fill), fill) * 100) / 100 }); }
          const stated = theme === "dark" ? rules.disabledDark : rules.disabledLight;
          // correction 1: the Disabled cell state, counted apart. A cell of a row that cannot be chosen shows the row surface and nothing else.
          const tokRgb = (k) => solid(tok.color[k][theme], [255, 255, 255]).map(Math.round).join(",");
          const rowSurfaces = [tokRgb("surface.panel"), tokRgb("surface.rowAlt")];
          const cells = [];
          for (const el of qa2("table.ds tr.offrow td, .rowdemo .dis")) { if (!shown(el) || !el.textContent.trim()) continue; const fill = fillOf(el); cells.push({ where: where(el), ratio: Math.round(ratio(solid(getComputedStyle(el).color, fill), fill) * 100) / 100, onRowSurface: rowSurfaces.includes(fill.map(Math.round).join(",")) }); }
          // correction 1: a control that carries the boundary and is washed has a fill of its own, one of three
          const ownFills = [tokRgb("surface.panel"), tokRgb("surface.sunken"), tokRgb("surface.raised")];
          const washedSel = ['.seg', '.btn:not(.primary):not(.text):not(.latched):not([disabled]):not(.disabled)', '.input', '.combo:not(.disabled)', '.search', '.sendrow', '.stepper', '.maprow .m .sel', '.iconbtn.raised', '.lenfield'];
          const washed = [];
          for (const sel of washedSel) for (const el of qa2(sel)) { if (!shown(el)) continue; const c = parse(getComputedStyle(el).backgroundColor); washed.push({ sel, where: where(el), ok: !!c && c.a === 1 && ownFills.includes(c.rgb.map(Math.round).join(",")) }); }
          const byKind = {}; for (const r of held) byKind[r.kind] = (byKind[r.kind] || 0) + 1;
          return { heading: document.querySelector("h1").textContent, strip: !!document.getElementById("controls"), stripRows: qa2("#controls .ctl .srf").length, theme,
            readings: held.length, byKind, lowest, under3: under, boundariesInBorderStrong: held.filter(r => r.strong).map(r => r.where),
            disabledSamples: disabled.length, disabledStated: stated, disabledLowest: [...disabled].sort((a, b) => a.ratio - b.ratio)[0], disabledUnderStated: disabled.filter(d => d.ratio < stated),
            disabledCellSamples: cells.length, disabledCellLowest: [...cells].sort((a, b) => a.ratio - b.ratio)[0] || null, disabledCellsUnderStated: cells.filter(c => c.ratio < stated), disabledCellsOffRowSurface: cells.filter(c => !c.onRowSurface).map(c => c.where),
            washedControls: washed.length, washedWithoutOwnFill: washed.filter(w => !w.ok).map(w => w.sel + " · " + w.where),
            latchedBoundaries: qa2('.btn.latched, .iconbtn.latched, .chip.on, .hud button[aria-pressed="true"]').filter(shown).length, tabsOn: qa2(".tab.on").length, checkBoxes: qa2(".cb").length, radios: qa2(".rb").length, grips: qa2(".splitdemo .split i").length, outlineBar: getComputedStyle(document.querySelector(".outline div.on")).boxShadow !== "none" };
          function qa2(s) { return [...document.querySelectorAll(s)]; }
        })()
      };
    }, rules);
    const key = `${width}-${scheme}`;
    report[key] = { ...facts, blockedRequests: net, consoleIssues: errors };
    for (const id of sections) {
      const box = await page.evaluate((id) => { const h = document.getElementById(id); let n = h, top = h.getBoundingClientRect().top + scrollY, bottom = top; while (n && (n === h || n.tagName !== "H2")) { const r = n.getBoundingClientRect(); bottom = Math.max(bottom, r.bottom + scrollY); n = n.nextElementSibling; } return { top, bottom }; }, id);
      const h = Math.min(4000, box.bottom - box.top + 8);
      await page.screenshot({ path: path.join(outDir, `${key}-${id}.png`), clip: { x: 0, y: box.top - 4, width, height: h }, fullPage: true });
    }
    // manual switch: opposite theme via the segmented control
    const other = scheme === "light" ? "dark" : "light";
    await page.click(`.spec-head .seg button[data-theme="${other}"]`);
    await page.waitForTimeout(100);
    const sw = await page.evaluate(() => ({ attr: document.documentElement.getAttribute("data-theme"), bg: getComputedStyle(document.body).backgroundColor, cs: getComputedStyle(document.documentElement).colorScheme, pressed: [...document.querySelectorAll('.spec-head .seg button')].map(b => b.getAttribute('aria-pressed')).join(','), stepColours: [...document.querySelectorAll('#steps div')].map(d => d.style.color).join(' ') }));
    report[key].manualSwitchTo = { other, ...sw };
    await page.screenshot({ path: path.join(outDir, `${key}-switched-${other}-top.png`), clip: { x: 0, y: 0, width, height: 900 } });
    await ctx.close();
  }
}
await browser.close();
fs.writeFileSync(path.join(outDir, "report.json"), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 1));
// V1.4: the control rule and the disabled ink as the browser resolved them, one line per rendering
let bad = 0;
for (const [key, r] of Object.entries(report)) { const v = r.v14; const n = v.under3.length + v.boundariesInBorderStrong.length + v.disabledUnderStated.length + v.disabledCellsUnderStated.length + v.disabledCellsOffRowSurface.length + v.washedWithoutOwnFill.length + (v.disabledCellSamples ? 0 : 1); bad += n;
  console.log(`V1.4 ${key}: ${v.readings} readings of what identifies a control, lowest ${v.lowest.ratio}:1 (${v.lowest.kind}, against ${v.lowest.against}), under 3:1: ${v.under3.length}, in border.strong: ${v.boundariesInBorderStrong.length}; disabled samples ${v.disabledSamples}, lowest ${v.disabledLowest.ratio}:1 against the stated ${v.disabledStated}:1, under it: ${v.disabledUnderStated.length}; disabled cells, counted apart, ${v.disabledCellSamples}, lowest ${v.disabledCellLowest ? v.disabledCellLowest.ratio : "none"}:1, under the stated ratio: ${v.disabledCellsUnderStated.length}, off the row surface: ${v.disabledCellsOffRowSurface.length}; washed controls ${v.washedControls}, without a fill of their own among the three: ${v.washedWithoutOwnFill.length}; blocked requests ${r.blockedRequests.length}, console issues ${r.consoleIssues.length}`); }
process.exitCode = bad ? 1 : 0;
