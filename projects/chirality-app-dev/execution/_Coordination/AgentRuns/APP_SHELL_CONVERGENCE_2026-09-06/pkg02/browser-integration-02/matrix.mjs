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
const devButton=page.getByRole('button',{name:'Open Next.js Dev Tools',exact:true});if(await devButton.count()){await devButton.click();await page.getByText('Preferences',{exact:true}).click();await page.getByRole('button',{name:'Hide',exact:true}).click();await devButton.waitFor({state:'hidden'});}
observations.push({label:'Development indicator hidden using its own Preferences > Hide Dev Tools for this session UI; no product CSS or runtime state modified.'});
const strip=await page.locator('.woven-activity-strip').boundingBox();assert.equal(strip.height,32);assert.equal(await page.getByRole('separator',{name:/Activity/}).count(),0);assert.equal(await page.locator('.shell-header').count(),0);assert.equal(await primary.count(),1);
const transcript=page.locator('.chat-transcript');assert((await transcript.innerText()).trim().length>0);const measure=await transcript.boundingBox();assert(measure.width<=620);observations.push({label:'Nonempty initial transcript and fixed strip',measure,strip,placeholder:await primary.getAttribute('placeholder')});
await page.getByText('Settings',{exact:true}).click();await page.getByText('Runtime & credentials',{exact:true}).click();await page.screenshot({path:path.join(out,'settings-expanded-1440-light.png'),fullPage:true});
observations.push({label:'Expanded settings',bounds:await page.locator('.shell-root-disclosure[open]').evaluate(el=>({details:el.getBoundingClientRect().toJSON(),panels:[...el.children].map(c=>({tag:c.tagName,box:c.getBoundingClientRect().toJSON(),overflow:getComputedStyle(c).overflow}))}))});
await page.getByText('Settings',{exact:true}).click();
for(const width of [1440,960]){await page.setViewportSize({width,height:1000});for(const theme of ['Light','Dark']){await page.getByRole('button',{name:theme,exact:true}).click();await files();const tree=page.locator('.panel--file-tree');await tree.waitFor();assert.equal(await tree.count(),1);const footer=await tree.locator(':scope > footer').boundingBox(),panel=await page.getByRole('region',{name:'Right panel',exact:true}).boundingBox();assert(Math.abs(footer.y+footer.height-panel.y-panel.height)<=2);observations.push({label:'Files footer bottom alignment',width,theme,footer,panel});await page.screenshot({path:path.join(out,`matrix-files-${width}-${theme.toLowerCase()}.png`),fullPage:true});await tree.getByRole('button',{name:'Readable note.md',exact:true}).click();await page.getByRole('heading',{name:'Shell redesign checkpoint',exact:true,level:1}).waitFor();await invariant(`document ${width} ${theme}`);await page.getByRole('button',{name:'Expand panel',exact:true}).click();await page.getByRole('button',{name:'Return panel',exact:true}).click();await invariant(`expand return ${width} ${theme}`);await page.screenshot({path:path.join(out,`document-${width}-${theme.toLowerCase()}.png`),fullPage:true});}}
await page.setViewportSize({width:1440,height:1000});await page.getByRole('button',{name:'Expand panel',exact:true}).click();await primary.fill('Synthetic unsent draft for continuity verification.');await page.getByRole('button',{name:'Expand panel',exact:true}).waitFor();await invariant('typing restores expansion without replacing textarea');
await page.getByRole('button',{name:'Details ›',exact:true}).click();await page.getByRole('region',{name:'Activity details',exact:true}).waitFor();await page.getByRole('textbox',{name:'Filter activity',exact:true}).fill('synthetic');await page.getByRole('button',{name:'Clear view',exact:true}).click();await invariant('Activity filter and Clear preserve primary draft');assert.equal(await primary.inputValue(),'Synthetic unsent draft for continuity verification.');await page.screenshot({path:path.join(out,'activity-1440-dark.png'),fullPage:true});observations.push({label:'Activity controls exercised with empty observed history; populated event preservation not established by this browser fixture.'});
await page.getByRole('tab',{name:'Files',exact:true}).focus();await page.getByRole('tab',{name:'Files',exact:true}).press('End');assert.equal(await page.getByRole('tab',{name:'Activity',exact:true}).getAttribute('aria-selected'),'true');await page.getByRole('tab',{name:'Activity',exact:true}).press('Home');assert.equal(await page.getByRole('tab',{name:'Files',exact:true}).getAttribute('aria-selected'),'true');
await page.setViewportSize({width:900,height:1000});await page.getByRole('button',{name:'Light',exact:true}).click();await page.screenshot({path:path.join(out,'files-900-light.png'),fullPage:true});assert.equal(pageErrors.length,0);
await fs.writeFile(path.join(out,'matrix-result.json'),JSON.stringify({status:'PASS',claim:'Bounded visual and fixture interaction checks only; no populated live history, native connection, or complete product acceptance.',browser:browser.version(),node:process.version,observations,consoleMessages,pageErrors,requests,responses},null,2)+'\n');
}catch(error){if(page)await page.screenshot({path:path.join(out,'matrix-failure.png'),fullPage:true}).catch(()=>{});await fs.writeFile(path.join(out,'matrix-result.json'),JSON.stringify({status:'FAIL',error:String(error),observations,consoleMessages,pageErrors,requests,responses},null,2)+'\n');throw error;}finally{if(browser)await browser.close();}
