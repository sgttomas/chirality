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
const context=await browser.newContext({viewport:{width:1180,height:720}});
await context.addInitScript(({projectRoot})=>{
if(window!==window.top)return;
localStorage.setItem('chirality.projectRoot',projectRoot);
localStorage.setItem('chirality.wovenWorkspace.v1',JSON.stringify({schema:'chirality.woven-workspace/v1',theme:'light',navigatorWidth:240,coordinationWidth:300,activityHeight:120,navigatorCollapsed:false,coordinationCollapsed:false,activityCollapsed:true,rightPanelView:'files',rightPanelWidths:{files:300,document:480,workflows:340}}));
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
const devButton=page.getByRole('button',{name:'Open Next.js Dev Tools',exact:true});if(await devButton.count()){await devButton.click();await page.getByText('Preferences',{exact:true}).click();await page.getByRole('button',{name:'Hide',exact:true}).click();await devButton.waitFor({state:'hidden'});}
await page.getByRole('tab',{name:'Workflows',exact:true}).click();await page.getByRole('button',{name:/Design review.md/}).waitFor();await primary.fill('Unsent synthetic draft for workflow navigation.');
await page.screenshot({path:path.join(out,'product-list-1180-light.png'),fullPage:true});await page.getByRole('region',{name:'Right panel',exact:true}).screenshot({path:path.join(out,'product-list-1180-light-rail.png')});
await page.getByRole('button',{name:/Design review.md/}).click();await page.getByRole('heading',{name:'Design review',exact:true}).waitFor();await page.screenshot({path:path.join(out,'product-detail-1180-light.png'),fullPage:true});await page.getByRole('region',{name:'Right panel',exact:true}).screenshot({path:path.join(out,'product-detail-1180-light-rail.png')});await invariant('workflow file open');assert.equal(await primary.inputValue(),'Unsent synthetic draft for workflow navigation.');
await fs.writeFile(path.join(out,'product-first-result.json'),JSON.stringify({status:'PASS',browser:browser.version(),node:process.version,observations,consoleMessages,pageErrors,requests,responses,geometry:await page.getByRole('region',{name:'Right panel',exact:true}).boundingBox(),claim:'Actual GET-only raw Markdown list/open; no validated workflow metadata, progress or effect controls. Logical1180x720; mock original displays at0.70339 scale.'},null,2)+'\n');
}catch(error){if(page)await page.screenshot({path:path.join(out,'product-first-failure.png'),fullPage:true}).catch(()=>{});await fs.writeFile(path.join(out,'product-first-result.json'),JSON.stringify({status:'FAIL',error:String(error),observations,requests,responses},null,2)+'\n');throw error;}finally{if(browser)await browser.close();}
