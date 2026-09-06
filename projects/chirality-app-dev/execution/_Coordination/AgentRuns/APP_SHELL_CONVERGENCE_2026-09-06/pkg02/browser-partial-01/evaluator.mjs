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
for(const width of [1440,960]){
await page.setViewportSize({width,height:1000});
for(const theme of ['Light','Dark']){
await page.getByRole('button',{name:theme,exact:true}).click();await files();
const tree=page.locator('.panel--file-tree');await tree.waitFor();assert.equal(await tree.count(),1);assert.equal(await page.locator('.woven-region--navigator .panel--file-tree').count(),0);
await page.screenshot({path:path.join(out,`files-${width}-${theme.toLowerCase()}.png`),fullPage:true});
await tree.getByRole('button',{name:'Readable note.md',exact:true}).click();await page.getByRole('heading',{name:'Shell redesign checkpoint',exact:true}).waitFor();
await invariant(`document ${width} ${theme}`);
const controls=page.locator('.woven-right-panel-controls');const boxes=await controls.locator(':scope > *').evaluateAll(els=>els.map(el=>{const b=el.getBoundingClientRect();return{x:b.x,y:b.y,width:b.width,height:b.height};}));
for(let i=0;i<boxes.length;i++)for(let j=i+1;j<boxes.length;j++){const a=boxes[i],b=boxes[j];assert(Math.max(0,Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x))*Math.max(0,Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y))===0);}
await page.getByRole('button',{name:'Expand panel',exact:true}).click();await page.getByRole('button',{name:'Return panel',exact:true}).click();await invariant(`expand return ${width} ${theme}`);
observations.push({width,theme,rightControlBoxes:boxes,document:await page.getByRole('region',{name:'Document preview'}).boundingBox()});
await page.screenshot({path:path.join(out,`document-${width}-${theme.toLowerCase()}.png`),fullPage:true});
}
}
await files();await page.getByRole('tab',{name:'Who is working',exact:true}).click();await invariant('switch Who is working');await page.getByRole('tab',{name:'Files',exact:true}).click();await invariant('switch Files');
assert.equal(pageErrors.length,0);
await fs.writeFile(path.join(out,'result.json'),JSON.stringify({status:'PASS',claim:'Early partial fixture presentation only; screenshots require independent visual inspection. Legacy header/composer/activity remain visible.',node:process.version,browser:browser.version(),observations,consoleMessages,pageErrors,requests,responses},null,2)+'\n');
}catch(error){if(page)await page.screenshot({path:path.join(out,'failure.png'),fullPage:true}).catch(()=>{});await fs.writeFile(path.join(out,'result.json'),JSON.stringify({status:'FAIL',error:String(error),observations,consoleMessages,pageErrors,requests,responses},null,2)+'\n');throw error;}finally{if(browser)await browser.close();}
