import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {chromium} from '/Users/ryan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
const out=path.dirname(fileURLToPath(import.meta.url));
const fixture=JSON.parse(await fs.readFile(path.join(out,'edge-fixture.json'),'utf8'));
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
const devButton=page.getByRole('button',{name:'Open Next.js Dev Tools',exact:true});if(await devButton.count()){await devButton.click();await page.getByText('Preferences',{exact:true}).click();await page.getByRole('button',{name:'Hide',exact:true}).click();await devButton.waitFor({state:'hidden'});await page.getByText('Preferences',{exact:true}).first().waitFor({state:'hidden'});}
const back=async()=>{const crumb=page.getByRole('navigation',{name:'Workflow breadcrumb'});if(await crumb.count())await crumb.getByRole('button',{name:'Workflows',exact:true}).click();};
await page.getByRole('tab',{name:'Workflows',exact:true}).click();await page.getByRole('button',{name:/Design review.md/}).waitFor();await primary.fill('Unsent workflow proof draft.');
for(const width of [1180,1440,960]){await page.setViewportSize({width,height:width===1180?720:1000});for(const theme of ['Light','Dark']){await page.getByRole('button',{name:theme,exact:true}).click();await back();await page.getByRole('button',{name:/Design review.md/}).waitFor();assert.equal(await page.getByRole('button',{name:/^(Continue|Create|Accept|Follow|Pause)/}).count(),0);const tabs=await page.getByRole('tablist',{name:'Right panel views'}).getByRole('tab').allTextContents();assert.equal(tabs.length,4);observations.push({label:'workflow tabs',width,theme,tabs,right:await page.getByRole('region',{name:'Right panel',exact:true}).boundingBox()});await page.screenshot({path:path.join(out,`final-list-${width}-${theme.toLowerCase()}.png`),fullPage:true});await page.getByRole('button',{name:/Design review.md/}).click();await page.getByRole('heading',{name:'Design review',exact:true}).waitFor();await invariant(`workflow detail ${width} ${theme}`);assert.equal(await primary.inputValue(),'Unsent workflow proof draft.');await page.screenshot({path:path.join(out,`final-detail-${width}-${theme.toLowerCase()}.png`),fullPage:true});}}
await page.setViewportSize({width:1440,height:1000});await page.getByRole('button',{name:'Expand panel',exact:true}).click();await page.getByRole('button',{name:'Return panel',exact:true}).click();await invariant('workflow expand return');await page.getByRole('button',{name:'Expand panel',exact:true}).click();await primary.press('End');await page.keyboard.type('x');assert.equal(await primary.inputValue(),'Unsent workflow proof draft.x');await page.getByRole('button',{name:'Expand panel',exact:true}).waitFor();await invariant('workflow expanded typing restores');
await back();const names=['Files','Workflows','Who is working','Activity'];await page.getByRole('tab',{name:'Files',exact:true}).click();for(const name of names){assert(await page.getByRole('tab',{name,exact:true}).evaluate(el=>el===document.activeElement));await page.keyboard.press('ArrowRight');}await page.getByRole('tab',{name:'Workflows',exact:true}).click();await page.getByRole('button',{name:/Unsafe.md/}).click();await page.getByRole('heading',{name:'Safe rendering',exact:true}).waitFor();assert.equal(await page.getByRole('article',{name:'Plan file preview'}).getByRole('link').count(),0);assert.equal(await page.getByRole('article',{name:'Plan file preview'}).getByRole('img').count(),0);assert.equal(await page.evaluate(()=>Boolean(window.__workflowScript)),false);assert.equal(requests.filter(r=>r.url.includes('workflow-probe')).length,0);await back();
await page.getByLabel('Panel menu',{exact:true}).click();await page.getByRole('button',{name:'Refresh',exact:true}).click();await page.getByRole('button',{name:/Design review.md/}).waitFor();await page.getByLabel('Panel menu',{exact:true}).click();
await page.setViewportSize({width:900,height:1000});await page.getByRole('button',{name:'Light',exact:true}).click();await page.screenshot({path:path.join(out,'final-list-900-light.png'),fullPage:true});await page.setViewportSize({width:1440,height:1000});
const changeRoot=async root=>{await page.getByLabel('Chat folder',{exact:true}).click();await page.getByRole('textbox',{name:'Folder path',exact:true}).fill(root);await page.getByRole('button',{name:'Use folder',exact:true}).click();await page.waitForFunction(root=>localStorage.getItem('chirality.projectRoot')===root,root);await page.getByLabel('Chat folder',{exact:true}).click();};
await changeRoot(fixture.missingRoot);await page.getByText('No workflow files here yet.',{exact:false}).waitFor();await page.screenshot({path:path.join(out,'missing-workflows.png'),fullPage:true});
let release;const pending=new Promise(r=>release=r);let signal;const started=new Promise(r=>signal=r);await page.route('**/api/working-root/workflow?**',async route=>{const u=new URL(route.request().url());if(u.searchParams.get('projectRoot')===fixture.projectRoot){signal();await pending;await route.fulfill({contentType:'application/json',body:JSON.stringify({projectRoot:fixture.projectRoot,files:[{name:'STALE.md',path:'.chirality/workflows/STALE.md',size:1,modifiedAt:'2026-09-06T00:00:00Z'}],directoryMissing:false})}).catch(()=>{});}else await route.continue();});
await changeRoot(fixture.projectRoot);await started;await changeRoot(fixture.emptyRoot);await page.getByText('No workflow files here yet.',{exact:false}).waitFor();release();await page.waitForLoadState('networkidle');assert.equal(await page.getByText('STALE.md',{exact:false}).count(),0);observations.push({label:'Delayed synthetic old-root list response cannot replace actual new-root empty result',pass:true});assert.equal(pageErrors.length,0);
await fs.writeFile(path.join(out,'matrix-result.json'),JSON.stringify({status:'PASS',observations,consoleMessages,pageErrors,requests,responses,claim:'Raw read-only subset only; actual route happy/empty/error evidence plus separately labelled delayed response fixture.'},null,2)+'\n');
}catch(error){if(page)await page.screenshot({path:path.join(out,'matrix-failure.png'),fullPage:true}).catch(()=>{});await fs.writeFile(path.join(out,'matrix-result.json'),JSON.stringify({status:'FAIL',error:String(error),observations,requests,responses},null,2)+'\n');throw error;}finally{if(browser)await browser.close();}
