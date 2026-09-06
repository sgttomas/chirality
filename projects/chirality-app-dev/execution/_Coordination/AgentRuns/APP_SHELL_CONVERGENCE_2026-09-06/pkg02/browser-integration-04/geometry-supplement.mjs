import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {chromium} from '/Users/ryan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
const out=path.dirname(fileURLToPath(import.meta.url));
const fixture=JSON.parse(await fs.readFile(path.join(out,'fixture.json'),'utf8'));
const origin='http://127.0.0.1:3187';
let browser,page; const observations=[],consoleMessages=[],pageErrors=[],requests=[],responses=[];
try {
browser=await chromium.launch({headless:true,executablePath:'/Users/ryan/Library/Caches/ms-playwright/chromium-1223/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'});
const context=await browser.newContext({viewport:{width:1440,height:1000}});
await context.addInitScript(({projectRoot})=>{
if(window!==window.top)return;
localStorage.setItem('chirality.projectRoot',projectRoot);
localStorage.setItem('chirality.wovenWorkspace.v1',JSON.stringify({schema:'chirality.woven-workspace/v1',theme:'light',navigatorWidth:240,coordinationWidth:300,activityHeight:120,navigatorCollapsed:false,coordinationCollapsed:false,activityCollapsed:true,rightPanelView:'files',rightPanelWidths:{files:300,document:480}}));
},fixture);
await context.route('**/*',async route=>{
const u=new URL(route.request().url());
if(u.origin!==origin){requests.push({url:u.href,blocked:true});return route.abort();}
if(!u.pathname.startsWith('/api/'))return route.continue();
requests.push({url:u.href,method:route.request().method()});
let body;
if(u.pathname==='/api/harness/session/list')body={sessions:[fixture.session,fixture.parentSession]};
else if(u.pathname==='/api/harness/agents')body={agents:fixture.agents};
else if(u.pathname===`/api/harness/session/${fixture.session.sessionId}/events`)body={session:fixture.session,events:[fixture.event],malformedLineCount:0,summary:{eventCount:1,firstTimestamp:fixture.event.timestamp,lastTimestamp:fixture.event.timestamp}};
else if(u.pathname.startsWith('/api/harness/'))body={error:'Isolated presentation fixture: live runtime unavailable.'};
if(body)return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(body)});
return route.continue();
});
page=await context.newPage();page.on('console',m=>consoleMessages.push({type:m.type(),text:m.text()}));page.on('pageerror',e=>pageErrors.push(String(e)));page.on('response',r=>responses.push({url:r.url(),status:r.status()}));
await page.goto(origin,{waitUntil:'networkidle'});
const primary=page.locator('[data-chat-input="primary"]');await primary.waitFor({state:'visible'});await primary.evaluate(el=>{window.__checkpointInput=el;window.__checkpointPanel=el.closest('.chat-panel')||el.closest('section');});
await page.evaluate(()=>document.fonts.ready);
observations.push({fonts:await page.evaluate(()=>({status:document.fonts.status,body:getComputedStyle(document.body).fontFamily,faces:[...document.fonts].map(f=>({family:f.family,status:f.status,weight:f.weight}))}))});
const invariant=async label=>{assert(await primary.isVisible());assert(await primary.evaluate(el=>el===window.__checkpointInput && (el.closest('.chat-panel')||el.closest('section'))===window.__checkpointPanel));observations.push({label,inputIdentity:true,primary:await primary.boundingBox()});};
const files=async()=>{const crumb=page.getByRole('navigation',{name:'Document breadcrumb'});if(await crumb.count())await crumb.getByRole('button',{name:'Files',exact:true}).click();};
await page.getByRole('button',{name:'Readable note.md',exact:true}).click();await page.getByRole('heading',{name:'Shell redesign checkpoint',exact:true,level:1}).waitFor();
const headings=await page.getByRole('region',{name:'Document preview'}).locator('h1,h2,h3').evaluateAll(els=>els.filter(el=>el.offsetHeight>2).map(el=>({tag:el.tagName,text:el.textContent,size:getComputedStyle(el).fontSize,font:getComputedStyle(el).fontFamily})));
const controls=await page.locator('.woven-right-panel-controls').evaluateAll(els=>els.map(el=>({box:el.getBoundingClientRect().toJSON(),children:[...el.children].map(c=>c.getBoundingClientRect().toJSON())})));
await fs.writeFile(path.join(out,'geometry-supplement.json'),JSON.stringify({headings,controls},null,2)+'\n');assert.equal(headings.length,4);assert(parseFloat(headings[0].size)>parseFloat(headings[1].size));assert(parseFloat(headings[1].size)>parseFloat(headings[3].size));assert.equal(controls.length,1);assert.equal(controls[0].children.length,3);
await page.getByLabel('Panel menu',{exact:true}).click();const menu=page.getByRole('button',{name:'Copy file path',exact:true});await menu.waitFor({state:'visible'});assert(await menu.evaluate(el=>{const b=el.getBoundingClientRect();return el.contains(document.elementFromPoint(b.x+b.width/2,b.y+b.height/2));}));
}finally{if(browser)await browser.close();}
