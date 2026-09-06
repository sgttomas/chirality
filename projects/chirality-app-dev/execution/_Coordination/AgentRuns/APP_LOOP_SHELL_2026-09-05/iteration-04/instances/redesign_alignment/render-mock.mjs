import { chromium } from '/Users/ryan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';
const out=path.dirname(fileURLToPath(import.meta.url));
const root=process.cwd();
const browser=await chromium.launch({headless:true, executablePath:'/Users/ryan/Library/Caches/ms-playwright/chromium-1223/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'});
const requests=[];const errors=[];
try {
const ctx=await browser.newContext({viewport:{width:1440,height:1100}});
await ctx.route('**/*',r=>{requests.push(r.request().url());return r.request().url().startsWith('file:') ? r.continue() : r.abort();});
const p=await ctx.newPage(); p.on('pageerror',e=>errors.push(String(e)));
await p.goto(pathToFileURL(path.join(root,'projects/chirality-app-dev/plans/shell-redesign_2026-09-04/mock/chirality-shell-mocks.html')).href);
await p.locator('[data-tab="shell"]').click();
for(const theme of ['light','dark']) { await p.locator(`[data-theme-of="shell"][data-val="${theme}"]`).click();await p.locator('#mock-shell').screenshot({path:path.join(out,`mock-shell-${theme}.png`)}); }
await p.locator('[data-tab="walk"]').click();
const states=[];
for(let i=1;i<=26;i++) {await p.locator(`#steps li[data-n="${i}"]`).click();states.push({step:i,title:await p.locator(`#steps li[data-n="${i}"]`).innerText()});await p.locator('#mock-walk').screenshot({path:path.join(out,`mock-walk-${String(i).padStart(2,'0')}.png`)});}
await fs.writeFile(path.join(out,'MOCK_RENDER_RESULT.json'),JSON.stringify({status:'COMPLETE',requests,errors,states,productRuntimeProof:false},null,2));
} finally { await browser.close(); }
