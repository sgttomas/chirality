import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),out=path.join(here,process.env.T3_ATTEMPT),origin=process.env.T3_BASE_URL;
const {chromium}=await import(pathToFileURL(process.env.PLAYWRIGHT_MODULE).href);
await fs.mkdir(out,{recursive:true});await fs.copyFile(fileURLToPath(import.meta.url),path.join(out,'input-script.mjs'));
const browser=await chromium.launch({headless:true,executablePath:process.env.T3_CHROMIUM_EXECUTABLE});const results=[];
try { for(const capability of [false,true]) {
const context=await browser.newContext();const page=await context.newPage();const errors=[];
page.on('pageerror',error=>errors.push({timestamp:new Date().toISOString(),message:error.message,stack:error.stack}));
await context.route('**/api/harness/**',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({agents:[],sessions:[]})}));
if(capability) await context.addInitScript(()=>{window.chirality={selectDirectory:async()=>{throw Error('Diagnostic capability must never be invoked')}};});
await page.goto(origin,{waitUntil:'networkidle',timeout:20000});
await page.locator('[data-chat-input="primary"]').waitFor({timeout:10000});
results.push({capability,errors,localStorage:await page.evaluate(()=>({...localStorage})),footer:await page.locator('footer').allTextContents()});
await page.screenshot({path:path.join(out,capability?'capability.png':'baseline.png')});await context.close();
} }finally {await browser.close();await fs.writeFile(path.join(out,'result.json'),JSON.stringify({results,claim:'Production build diagnostic only. No localStorage init; inert directory-picker capability never called. All page errors retained.'},null,2)+'\n');}
console.log(JSON.stringify(results));
