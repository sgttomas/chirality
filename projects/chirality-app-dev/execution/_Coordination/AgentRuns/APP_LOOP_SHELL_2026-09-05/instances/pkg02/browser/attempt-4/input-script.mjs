import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import { pathToFileURL, fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.join(here, process.env.T1_ATTEMPT || 'attempt-1');
await fs.mkdir(out, {recursive:true});
await fs.copyFile(fileURLToPath(import.meta.url),path.join(out,'input-script.mjs'));
await fs.copyFile(path.join(here,'fixture.json'),path.join(out,'input-fixture.json'));
await fs.copyFile(path.join(here,'../author/SOURCE_MANIFEST_revision2.sha256'),path.join(out,'source-manifest.sha256'));
const fixture = JSON.parse(await fs.readFile(path.join(here, 'fixture.json'), 'utf8'));
const { chromium } = await import(pathToFileURL(process.env.PLAYWRIGHT_MODULE).href);
const origin = process.env.T1_BASE_URL;
assert(origin && new URL(origin).hostname === '127.0.0.1', 'loopback URL required');
const browser = await chromium.launch({ headless: true, executablePath: process.env.T1_CHROMIUM_EXECUTABLE });
const observations = [];
const requests = [];
const consoleMessages = [];
const pageErrors = [];
try {
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
  await context.addInitScript(({projectRoot, sessionId}) => {
    localStorage.setItem('chirality.projectRoot', projectRoot);
    localStorage.setItem('chirality.wovenWorkspace.v1', JSON.stringify({
      schema: 'chirality.woven-workspace/v1', theme: 'light',
      navigatorExpandedSurfaces: ['workbench'], sessionSurfaces: {[sessionId]: 'workbench'},
      navigatorWidth: 240, coordinationWidth: 320, activityHeight: 120,
      coordinationView: 'work', navigatorCollapsed: false, coordinationCollapsed: false,
      activityCollapsed: true
    }));
  }, { projectRoot: fixture.projectRoot, sessionId: fixture.session.sessionId });
  await context.route('**/api/**', async route => {
    const url = new URL(route.request().url());
    requests.push({method: route.request().method(), path: url.pathname});
    let body;
    if (url.pathname === '/api/harness/session/list') body = {sessions: [fixture.session]};
    else if (url.pathname.endsWith('/events') && url.pathname.includes(fixture.session.sessionId)) {
      body = {session: fixture.session, events: [fixture.event], malformedLineCount: 0,
        summary: {eventCount: 1, firstTimestamp: fixture.event.timestamp, lastTimestamp: fixture.event.timestamp}};
    } else if (url.pathname === '/api/harness/agents') body = {agents:fixture.agents};
    else if (url.pathname === '/api/working-root/tree') body = {root:fixture.tree,depth:3,scannedAt:fixture.event.timestamp};
    else if (url.pathname === '/api/working-root/scope') body = {deliverables:[],knowledgeTypes:[],hasKnowledgeDecomposition:false,truncated:false,scannedAt:fixture.event.timestamp};
    else if (url.pathname === '/api/working-root/validate') body = {ok: true, projectRoot: fixture.projectRoot};
    else body = {error: {type: 'T1_FIXTURE_UNAVAILABLE', message: 'Not part of this presentation fixture.'}};
    await route.fulfill({status: body.error ? 503 : 200, contentType:'application/json', body: JSON.stringify(body)});
  });
  const page = await context.newPage();
  page.on('console', message => consoleMessages.push({type:message.type(),text:message.text()}));
  page.on('pageerror', error => pageErrors.push(String(error)));
  await page.goto(origin, {waitUntil:'networkidle'});
  const primary = page.locator('[data-chat-input="primary"]');
  await primary.waitFor({state:'visible'});
  await primary.evaluate(el => { window.__t1Primary = el; });
  const invariant = async label => {
    assert.equal(await page.locator('[data-focused-surface]').count(), 0);
    assert.equal(await page.locator('.woven-navigator').getByText('Workbench', {exact:true}).count(), 0);
    assert.equal(await page.locator('.woven-navigator').getByText('Pipeline', {exact:true}).count(), 0);
    assert(await primary.isVisible(), label + ': composer visible');
    assert(await primary.isEnabled(), label + ': composer enabled');
    assert(await primary.evaluate(el => el === window.__t1Primary), label + ': same primary node');
    await primary.focus();
    assert(await primary.evaluate(el => el === document.activeElement), label + ': composer focus');
    observations.push({label, route:page.url(), viewport:page.viewportSize(), primary:await primary.boundingBox(), pass:true});
  };
  await invariant('initial legacy state hydration');
  await page.locator('.woven-navigator-session-list button').first().click();
  await page.getByText('Recorded fixture content; presentation evidence only.', {exact:true}).waitFor();
  await invariant('replay beside primary');
  assert(await page.locator('.woven-region--coordination').getByText('Replay — read-only').isVisible());
  await page.screenshot({path:path.join(out,'replay-1440-light.png'),fullPage:true});
  await page.getByRole('button',{name:'Dark',exact:true}).click();
  await invariant('dark theme replay');
  await page.screenshot({path:path.join(out,'replay-1440-dark.png'),fullPage:true});
  await page.getByRole('button',{name:'Light',exact:true}).click();
  await page.getByRole('separator',{name:'Resize Coordination Panel'}).press('ArrowLeft');
  await invariant('keyboard resize coordination');
  const coordinationToggle = page.locator('.woven-region--coordination > .woven-region-toggle');
  assert.match(await coordinationToggle.innerText(),/Close Coordination/);
  await coordinationToggle.click();
  await invariant('coordination collapsed');
  assert.match(await coordinationToggle.innerText(),/Open Coordination/);
  await coordinationToggle.click();
  await invariant('coordination expanded');
  await page.setViewportSize({width:960,height:1000});
  await invariant('narrow viewport replay');
  await page.screenshot({path:path.join(out,'replay-960-light.png'),fullPage:true});
  await page.getByRole('button',{name:'Return to primary dialogue',exact:true}).click();
  await invariant('return primary');
  for (const route of ['/chat','/workbench','/pipeline']) {
    const response = await page.goto(origin + route,{waitUntil:'networkidle'});
    assert(response && response.status() === 200, route + ': reachable');
    if (route !== '/chat') {
      assert.equal(await page.locator('[data-legacy="true"]').count(),1, route + ': retained legacy surface');
      assert.equal(await page.locator('.woven-workspace').count(),0, route + ': outside active woven shell');
      assert(await page.getByRole('heading',{name:route === '/workbench' ? 'Workbench' : 'Pipeline',exact:true}).isVisible());
      if (route === '/workbench') assert(await page.getByRole('heading',{name:'Active Agent Context',exact:true}).isVisible());
      else assert(await page.getByRole('heading',{name:'DECOMP*',exact:true}).isVisible());
    } else assert(await page.locator('[data-chat-input="primary"]').isVisible());
    observations.push({label:'retained route',route:page.url(),viewport:page.viewportSize(),pass:true});
    await page.screenshot({path:path.join(out,route.slice(1)+'-960.png'),fullPage:true});
  }
  await context.close();
  assert.equal(pageErrors.length,0,'no browser runtime errors');
  await fs.writeFile(path.join(out,'result.json'),JSON.stringify({status:'PASS',node:process.version,browser:browser.version(),fixture:'fixture.json',observations,requests,consoleMessages,pageErrors,cleanup:'isolated browser context closed; no persistent browser profile or server fixture writes'},null,2)+'\n');
} catch (error) {
  await fs.writeFile(path.join(out,'result.json'),JSON.stringify({status:'FAIL',error:String(error),observations,requests,consoleMessages,pageErrors},null,2)+'\n');
  throw error;
} finally { await browser.close(); }
