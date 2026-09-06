import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.join(here, process.env.T3_ATTEMPT || 'attempt-1');
const origin = process.env.T3_BASE_URL;
assert(origin && new URL(origin).hostname === '127.0.0.1', 'owned loopback URL required');
const fixture = JSON.parse(await fs.readFile(path.join(here, 'fixture.json'), 'utf8'));
const { chromium } = await import(pathToFileURL(process.env.PLAYWRIGHT_MODULE).href);
await fs.mkdir(out, { recursive: true });
await fs.copyFile(fileURLToPath(import.meta.url), path.join(out, 'input-script.mjs'));
await fs.copyFile(path.join(here, 'fixture.json'), path.join(out, 'input-fixture.json'));
await fs.copyFile(path.join(here, '../author', process.env.T3_SOURCE_MANIFEST || 'SOURCE_MANIFEST_v4.json'), path.join(out, 'source-manifest.json'));
const browser = await chromium.launch({ headless: true, executablePath: process.env.T3_CHROMIUM_EXECUTABLE });
const observations = [], requests = [], consoleMessages = [], pageErrors = [], resourceRequests = [];
let page;
try {
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
  await context.addInitScript(({ projectRoot }) => {
    localStorage.setItem('chirality.projectRoot', projectRoot);
    localStorage.setItem('chirality.wovenWorkspace.v1', JSON.stringify({ schema: 'chirality.woven-workspace/v1', theme: 'light',
      navigatorWidth: 240, coordinationWidth: 320, activityHeight: 120, navigatorCollapsed: false,
      coordinationCollapsed: false, activityCollapsed: true, rightPanelView: 'files', rightPanelWidths: { files: 320, document: 480 } }));
  }, fixture);
  await context.route('**/api/**', async route => {
    const u = new URL(route.request().url());
    const entry = { method: route.request().method(), path: u.pathname, mocked: false };
    requests.push(entry);
    let body;
    if (u.pathname === '/api/harness/session/list') body = { sessions: [fixture.session, fixture.parentSession] };
    else if (u.pathname === `/api/harness/session/${fixture.session.sessionId}/events`) body = { session: fixture.session,
      events: [fixture.event], malformedLineCount: 0, summary: { eventCount: 1, firstTimestamp: fixture.event.timestamp, lastTimestamp: fixture.event.timestamp } };
    else if (u.pathname === '/api/harness/agents') body = { agents: fixture.agents };
    else if (u.pathname === `/api/harness/session/${fixture.parentSession.sessionId}/events`) body = { session: fixture.parentSession, events: [fixture.parentEvent], malformedLineCount: 0, summary: { eventCount: 1, firstTimestamp: fixture.parentEvent.timestamp, lastTimestamp: fixture.parentEvent.timestamp } };
    if (body) { entry.mocked = true; await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(body) }); }
    else await route.continue();
  });
  page = await context.newPage();
  page.on('console', m => consoleMessages.push({ type: m.type(), text: m.text() }));
  page.on('pageerror', e => pageErrors.push(String(e)));
  page.on('request', r => resourceRequests.push({ url: r.url(), resourceType: r.resourceType() }));
  await page.goto(origin, { waitUntil: 'networkidle' });
  const primary = page.locator('[data-chat-input="primary"]');
  await primary.waitFor({ state: 'visible' });
  await primary.evaluate(el => { window.__t3Primary = el; });
  const invariant = async label => {
    assert(await primary.isVisible(), `${label}: primary visible`);
    assert(await primary.evaluate(el => el === window.__t3Primary), `${label}: primary identity preserved`);
    observations.push({ label, primary: await primary.boundingBox(), viewport: page.viewportSize(), pass: true });
  };
  const screenshot = name => page.screenshot({ path: path.join(out, name + '.png'), fullPage: true });
  const file = async name => {
    const crumb = page.getByRole('navigation', { name: 'Document breadcrumb' });
    if (await crumb.count()) await crumb.getByRole('button', { name: 'Files', exact: true }).click();
    await page.getByRole('button', { name, exact: true }).click();
    await page.getByRole('region', { name: 'Document preview' }).waitFor();
  };
  await invariant('initial Files and primary'); await screenshot('files-1440-light');
  await file('Readable note.md');
  await page.getByRole('heading', { name: 'T3 fixture document', exact: true, level: 1 }).waitFor();
  await invariant('actual markdown response rendered'); await screenshot('document-1440-light');
  // Actual layout/action regression for attempt-1: no forced clicks or mocked hit testing.
  for (const width of [1440, 960, 900]) {
    await page.setViewportSize({ width, height: 1000 });
    for (const theme of ['Light', 'Dark']) {
      await page.getByRole('button', { name: theme, exact: true }).click();
      const collapse = page.getByRole('button', { name: 'Close Coordination', exact: true });
      const expand = page.getByRole('button', { name: 'Expand panel', exact: true });
      const closeDetail = page.getByRole('button', { name: 'Close detail', exact: true });
      await expand.scrollIntoViewIfNeeded();
      const boxes = await Promise.all([collapse, expand, closeDetail].map(control => control.boundingBox()));
      assert(boxes.every(Boolean), 'all three distinct panel actions have geometry');
      const intersect = (a, b) => Math.max(0, Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)) * Math.max(0,Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y));
      assert.equal(intersect(boxes[0], boxes[1]), 0, 'collapse does not overlap expansion');
      assert.equal(intersect(boxes[0], boxes[2]), 0, 'collapse does not overlap detail return');
      await expand.click();
      await page.getByRole('button', { name: 'Return panel', exact: true }).click();
      await closeDetail.click();
      await page.getByRole('tab', { name: 'Files', exact: true }).waitFor();
      await page.getByRole('button', { name: 'Readable note.md', exact: true }).click();
      await page.getByRole('heading', { name: 'T3 fixture document', exact: true, level: 1 }).waitFor();
      await collapse.click();
      await page.getByRole('button', { name: 'Open Coordination+', exact: true }).click();
      await page.getByRole('heading', { name: 'T3 fixture document', exact: true, level: 1 }).waitFor();
      await invariant(`pointer collapse/return/expand ${width}px ${theme}`);
      observations.push({ label: 'panel control disjoint rectangles and real pointer actions', width, theme, boxes, pass: true });
      await screenshot(`panel-controls-${width}-${theme.toLowerCase()}`);
    }
  }
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.getByRole('button', { name: 'Light', exact: true }).click();
  await page.getByRole('button', { name: 'Expand panel', exact: true }).click();
  await invariant('expanded document retains primary'); await screenshot('expanded-1440-light');
  await primary.fill('Fixture-only continuity text; not sent.');
  await page.getByRole('button', { name: 'Expand panel', exact: true }).waitFor();
  await invariant('composer input restores expanded panel');
  await page.getByRole('separator', { name: 'Resize Coordination Panel' }).press('ArrowLeft');
  await invariant('keyboard document resize');
  const dragHandle = await page.getByRole('separator', { name: 'Resize Coordination Panel' }).boundingBox();
  assert(dragHandle); await page.mouse.move(dragHandle.x + dragHandle.width / 2, dragHandle.y + 80);
  await page.mouse.down(); await page.mouse.move(dragHandle.x - 64, dragHandle.y + 80, { steps: 5 }); await page.mouse.up();
  await invariant('actual pointer resize');
  assert((await page.getByRole('main', { name: 'Primary Dialogue', exact: true }).boundingBox()).width >= 420, 'primary dialogue region minimum width after drag');
  await page.getByRole('button', { name: 'Dark', exact: true }).click(); await screenshot('document-1440-dark');
  await page.getByRole('button', { name: 'Light', exact: true }).click();
  await file('data.csv'); await page.getByText('Preview: first 500 rows, up to 200 columns.', { exact: true }).waitFor();
  assert(await page.getByRole('table').count()); await screenshot('csv-1440-light');
  await file('oversized.txt'); await page.getByText('This file exceeds the 10 MB text preview limit.', { exact: true }).waitFor();
  await screenshot('oversized-1440-light');
  await file('Preview.pdf');
  const pdf = page.getByTitle('Preview.pdf', { exact: true }); await pdf.waitFor();
  const pdfResponse = await context.request.get(await pdf.getAttribute('src').then(src => origin + src));
  assert.equal(pdfResponse.status(), 200); assert.equal(pdfResponse.headers()['content-type'], 'application/pdf');
  assert((await pdfResponse.body()).subarray(0, 5).toString() === '%PDF-');
  observations.push({ label: 'actual PDF endpoint bytes and standalone browser iframe; visual inspection pending', pass: true });
  await screenshot('pdf-browser-1440-light');
  await page.waitForLoadState('networkidle');
  await screenshot('pdf-full-chromium-final');
  await fs.writeFile(path.join(out, 'result.json'), JSON.stringify({status:'PDF_RENDER_INSPECTION_PENDING',browser:browser.version(),observations,requests,consoleMessages,pageErrors}, null, 2)+'\n');
} catch (error) {
  if (page) await page.screenshot({ path: path.join(out, 'failure.png'), fullPage: true }).catch(() => {});
  await fs.writeFile(path.join(out, 'result.json'), JSON.stringify({ status: 'FAIL', error: String(error), observations, requests, resourceRequests, consoleMessages, pageErrors }, null, 2) + '\n');
  throw error;
} finally { await browser.close(); }
