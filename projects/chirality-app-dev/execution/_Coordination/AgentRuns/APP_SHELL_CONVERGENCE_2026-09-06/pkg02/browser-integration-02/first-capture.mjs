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
await page.screenshot({path:path.join(out,'files-1440-light.png'),fullPage:true});
await fs.writeFile(path.join(out,'first-ready.json'),JSON.stringify({status:'CAPTURED',browser:browser.version(),observations,consoleMessages,pageErrors},null,2)+'\n');
await fs.writeFile(path.join(out,'dev-tools-dom.json'),JSON.stringify(await page.locator('nextjs-portal').evaluateAll(els=>els.map(el=>el.shadowRoot?.innerHTML)),null,2));
await page.getByText('Settings',{exact:true}).click();await page.screenshot({path:path.join(out,'settings-1440-light.png'),fullPage:true});
const geometry=await page.locator('.woven-settings-controls').evaluate(el=>({html:el.outerHTML,children:[...el.querySelectorAll('*')].filter(e=>e.getBoundingClientRect().height>0).map(e=>{let b=e.getBoundingClientRect();return{tag:e.tagName,text:e.textContent?.slice(0,80),box:b.toJSON(),hit:b.y>=0&&b.y+b.height<=innerHeight?e.contains(document.elementFromPoint(b.x+b.width/2,b.y+b.height/2)):false};})}));
await fs.writeFile(path.join(out,'settings-geometry.json'),JSON.stringify(geometry,null,2)+'\n');
}finally{if(browser)await browser.close();}
