import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath,pathToFileURL} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)), out=path.join(here,process.env.T3_ATTEMPT||'state-proof-1');
const origin=process.env.T3_BASE_URL; assert(origin&&new URL(origin).hostname==='127.0.0.1');
const fixture=JSON.parse(await fs.readFile(path.join(here,'fixture.json'),'utf8'));
const {chromium}=await import(pathToFileURL(process.env.PLAYWRIGHT_MODULE).href);
await fs.mkdir(out,{recursive:true});
await fs.copyFile(fileURLToPath(import.meta.url),path.join(out,'input-script.mjs'));
await fs.copyFile(path.join(here,'fixture.json'),path.join(out,'input-fixture.json'));
await fs.copyFile(path.join(here,'../author',process.env.T3_SOURCE_MANIFEST||'SOURCE_MANIFEST_v8.json'),path.join(out,'source-manifest.json'));
const browser=await chromium.launch({headless:true,executablePath:process.env.T3_CHROMIUM_EXECUTABLE});
const cases=[],errors=[],requests=[];
const write=()=>fs.writeFile(path.join(out,'result.json'),JSON.stringify({status:cases.length===40&&cases.every(item=>item.status==='PASS_ACTION')&&errors.length===0?'PASS_ACTIONS_PENDING_VISUAL_REVIEW':'FAIL_OR_INCOMPLETE',cases,errors,requests,claim:'Actual fixture state matrix after source review and parent rebuild. Scripted actions/geometry require separate visual fan-in; no native, runtime-account or whole-item acceptance claim.'},null,2)+'\n');
try{
 for(const width of [1440,960,900,860,840])for(const theme of ['light','dark']){
  const context=await browser.newContext({viewport:{width,height:1000}});
  await context.addInitScript(({root,theme})=>{
   localStorage.setItem('chirality.projectRoot',root);
   localStorage.setItem('chirality.wovenWorkspace.v1',JSON.stringify({schema:'chirality.woven-workspace/v1',theme,navigatorWidth:240,coordinationWidth:320,activityHeight:120,navigatorCollapsed:false,coordinationCollapsed:false,activityCollapsed:true,rightPanelView:'files',rightPanelWidths:{files:320,document:480}}));
  },{root:fixture.projectRoot,theme});
  await context.route('**/api/**',async route=>{
   const u=new URL(route.request().url());let body;
   if(u.pathname==='/api/harness/session/list')body={sessions:[fixture.session,fixture.parentSession]};
   else if(u.pathname==='/api/harness/agents')body={agents:fixture.agents};
   else if(u.pathname===`/api/harness/session/${fixture.session.sessionId}/events`)body={session:fixture.session,events:[fixture.event],malformedLineCount:0,summary:{eventCount:1}};
   requests.push({width,theme,path:u.pathname,mocked:Boolean(body)});
   if(body)await route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(body)});else await route.continue();
  });
  const page=await context.newPage();page.setDefaultTimeout(2500);page.on('pageerror',e=>errors.push({width,theme,error:String(e)}));
  const capture=async(name,entry)=>{
   entry[name]=await page.evaluate(()=>{
    const rect=el=>{if(!el)return null;const b=el.getBoundingClientRect(),c=getComputedStyle(el);return{x:b.x,y:b.y,width:b.width,height:b.height,clientHeight:el.clientHeight,scrollHeight:el.scrollHeight,overflow:c.overflow,minHeight:c.minHeight,maxHeight:c.maxHeight};};
    const controls=Array.from(document.querySelectorAll('.woven-region-toggle,.woven-right-panel > header button')).map(el=>{const b=el.getBoundingClientRect(),hit=document.elementFromPoint(b.x+b.width/2,b.y+b.height/2);return{text:el.textContent,ariaLabel:el.getAttribute('aria-label'),rect:rect(el),hit:hit?{tag:hit.tagName,text:hit.textContent?.slice(0,90),class:hit.className}:null,centerHits:hit===el||el.contains(hit)};});
    return{viewport:{width:innerWidth,height:innerHeight},page:{scrollX,scrollY,height:document.scrollingElement.scrollHeight},navigator:rect(document.querySelector('.woven-region--navigator')),coordination:rect(document.querySelector('.woven-region--coordination')),primary:rect(document.querySelector('[data-chat-input="primary"]')),controls};
   });
  };
  for(const action of ['navigator-collapse-open','coordination-collapse-open','expand-return','detail-close']){
   const entry={width,theme,action};cases.push(entry);
   try{
    await page.goto(origin,{waitUntil:'networkidle'});
    await page.locator('.woven-region--coordination').getByRole('button',{name:'Readable note.md',exact:true}).click();
    await page.getByRole('heading',{name:'T3 fixture document',level:1,exact:true}).waitFor();
    const primary=page.locator('[data-chat-input="primary"]');await primary.evaluate(el=>window.__matrixPrimary=el);
    if(action.includes('collapse')){
     const region=action.startsWith('navigator')?'.woven-region--navigator':'.woven-region--coordination';
     const toggle=page.locator(region+' > .woven-region-toggle');
     await toggle.scrollIntoViewIfNeeded();await capture('before',entry);await toggle.click();
     await capture('collapsed',entry);
     if(width<960){
      const collapsedBox=await page.locator(region).boundingBox();
      assert(collapsedBox&&collapsedBox.height>=40&&collapsedBox.height<=80,'stacked collapse is a compact visible strip');
      const label=page.locator(region+' > .woven-collapsed-label'),labelBox=await label.boundingBox();
      assert(await label.isVisible());assert(labelBox&&labelBox.y>=collapsedBox.y-1&&labelBox.y+labelBox.height<=collapsedBox.y+collapsedBox.height+1,'collapsed label fits strip');
     }
     entry.collapsedAX=await page.locator(region).ariaSnapshot();
     await page.screenshot({path:path.join(out,`${width}-${theme}-${action}-collapsed.png`),fullPage:true});
     await toggle.click();await capture('reopened',entry);
     await page.getByRole('heading',{name:'T3 fixture document',level:1,exact:true}).waitFor();
    }else if(action==='expand-return'){
     await page.getByRole('button',{name:'Expand panel',exact:true}).click();await capture('expanded',entry);await page.screenshot({path:path.join(out,`${width}-${theme}-${action}-expanded.png`),fullPage:true});
     if(width<960)assert(entry.expanded.navigator.height>=40&&entry.expanded.navigator.height<=80,'expand leaves reachable compact Navigator strip');
     await page.getByRole('button',{name:'Return panel',exact:true}).click();await capture('returned',entry);
    }else{
     await page.getByRole('button',{name:'Close detail',exact:true}).click();await page.getByRole('tab',{name:'Files',exact:true}).waitFor();await page.locator('.woven-region--coordination').getByRole('button',{name:'Readable note.md',exact:true}).waitFor();await capture('files',entry);await page.screenshot({path:path.join(out,`${width}-${theme}-${action}-files.png`),fullPage:true});
    }
    assert(await primary.isVisible());assert(await primary.evaluate(el=>el===window.__matrixPrimary));entry.status='PASS_ACTION';
   }catch(e){entry.status='FAIL_ACTION';entry.error=String(e);await capture('failure',entry).catch(()=>{});await page.screenshot({path:path.join(out,`${width}-${theme}-${action}-failure.png`),fullPage:true}).catch(()=>{});}
   await write();
  }
  await context.close();
 }
}finally{await browser.close();await write();}
