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
  await context.addInitScript(({ projectRoot, appOrigin }) => {
    if (window !== window.top || location.origin !== appOrigin) {
      console.info('T3_FIXTURE_INIT_SKIPPED', JSON.stringify({url:location.href, origin:location.origin, mainFrame:window===window.top}));
      return;
    }
    localStorage.setItem('chirality.projectRoot', projectRoot);
    localStorage.setItem('chirality.wovenWorkspace.v1', JSON.stringify({ schema: 'chirality.woven-workspace/v1', theme: 'light',
      navigatorWidth: 240, coordinationWidth: 320, activityHeight: 120, navigatorCollapsed: false,
      coordinationCollapsed: false, activityCollapsed: true, rightPanelView: 'files', rightPanelWidths: { files: 320, document: 480 } }));
  }, { ...fixture, appOrigin: origin });
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
  for (const width of [1440, 960, 900, 860, 840]) {
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
      const navTree = page.locator('.woven-region--navigator .panel--file-tree');
      const navBody = navTree.locator(':scope > .panel-body');
      const navFooter = navTree.locator(':scope > footer');
      const navBoxes = { body: await navBody.boundingBox(), footer: await navFooter.boundingBox(), ancestor: await page.locator('.woven-region--navigator').boundingBox() };
      assert(navBoxes.ancestor && navBoxes.footer && navBoxes.footer.y + navBoxes.footer.height <= navBoxes.ancestor.y + navBoxes.ancestor.height + 1, 'Navigator footer fits its visible ancestor');
      assert(navBoxes.body && navBoxes.footer && navBoxes.body.height >= 120, 'Navigator has usable multi-row list area');
      assert(navBoxes.footer.y >= navBoxes.body.y + navBoxes.body.height - 1, 'Navigator footer follows body without overlap');
      const scrollBefore = await navBody.evaluate(el => ({ top: el.scrollTop, height: el.clientHeight, total: el.scrollHeight }));
      if (scrollBefore.total > scrollBefore.height + 1) {
        await navBody.hover(); await page.mouse.wheel(0, 500);
        await page.waitForFunction(() => { const el=document.querySelector('.woven-region--navigator .panel--file-tree > .panel-body'); return el && el.scrollTop > 0; });
      }
      const fileTree = page.locator('.woven-region--coordination .panel--file-tree');
      const fileBody = await fileTree.locator(':scope > .panel-body').boundingBox();
      const fileFooter = await fileTree.locator(':scope > footer').boundingBox();
      assert(fileBody && fileFooter && fileBody.height >= 120 && fileFooter.y >= fileBody.y + fileBody.height - 1, 'callback-enabled Files body/footer are readable and disjoint');
      await fileTree.getByRole('button', { name: 'Picture.png', exact: true }).click();
      await page.getByRole('region', { name: 'Document preview' }).getByRole('img').evaluate(async el => { await el.decode(); });
      observations.push({ label: 'Navigator readonly list scroll and callback-enabled Files ordinary click', width, theme, navBoxes, scrollBefore, fileBody, fileFooter, pass: true });
      await file('Readable note.md');
      await page.getByRole('heading', { name: 'T3 fixture document', exact: true, level: 1 }).waitFor();
      await collapse.click();
      await page.getByRole('button', { name: /^Open Coordination\+?$/ }).click();
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
  await page.waitForLoadState('networkidle');
  // Plugin raster paint can lag networkidle; keep actual screenshot review mandatory.
  await page.waitForTimeout(1500);
  await screenshot('pdf-browser-1440-light');
  await file('Preview.docx'); await page.getByText('Preview this Office document with Quick Look.', { exact: true }).waitFor();
  assert(await page.getByRole('button', { name: 'Quick Look', exact: true }).isDisabled());
  await screenshot('office-browser-1440-light');
  await file('Headings and links.md');
  await page.getByRole('heading', { name: 'Headings and links fixture', exact: true, level: 1 }).waitFor();
  await page.getByRole('region', { name: 'Document preview' }).locator('summary').filter({ hasText: /^Headings$/ }).click();
  const toc = page.getByRole('navigation', { name: 'Document headings', exact: true });
  const tocNames = await toc.getByRole('button').allTextContents();
  assert.equal(tocNames.filter(name => name === 'Repeated heading').length, 2);
  assert(!tocNames.some(name => name === 'Not a real heading'));
  await toc.getByRole('button', { name: 'Repeated heading', exact: true }).last().click();
  assert(await page.getByRole('heading', { name: 'Repeated heading', exact: true }).last().evaluate(el => el === document.activeElement));
  observations.push({ label: 'actual duplicate-heading TOC navigation focuses selected real heading', tocNames, pass: true });
  await page.getByRole('link', { name: 'Open local note', exact: true }).click();
  await page.getByRole('heading', { name: 'T3 fixture document', exact: true, level: 1 }).waitFor();
  await invariant('local markdown link stays in panel');
  await file('Folded.json');
  const jsonTree = page.getByLabel('JSON tree', { exact: true });
  for (const label of ['nested', 'items', '3']) await jsonTree.locator('summary').filter({ hasText: new RegExp('^' + label + '$') }).click();
  await jsonTree.getByText('literal key', { exact: false }).waitFor();
  await screenshot('json-1440-light');
  await file('Malformed.json'); await page.getByRole('alert').filter({ hasText: 'Invalid JSON. Showing the original text.' }).waitFor();
  await screenshot('json-malformed-1440-light');
  await file('Oversized image.png'); await page.getByText('This image exceeds the 2 MB image preview limit.', { exact: true }).waitFor();
  await screenshot('oversized-image-1440-light');
  await file('Picture.png');
  const raster = page.getByRole('region', { name: 'Document preview' }).getByRole('img'); await raster.waitFor();
  assert(await raster.evaluate(async el => { await el.decode(); return el.complete && el.naturalWidth === 900; }));
  await raster.click(); await screenshot('image-natural-1440-light');
  await file('Image-only.svg');
  const svg = page.getByRole('region', { name: 'Document preview' }).getByRole('img'); await svg.waitFor();
  assert(await svg.evaluate(async el => { await el.decode(); return el.complete && el.naturalWidth === 900; }));
  assert.equal(await page.evaluate(() => Boolean(window.__t3SvgExecuted)), false);
  assert.equal(resourceRequests.filter(r => r.url.includes('t3-external-probe')).length, 0, 'SVG image makes no external resource request');
  await screenshot('svg-image-1440-light');
  const svgUrl = origin + '/api/working-root/file?projectRoot=' + encodeURIComponent(fixture.projectRoot) + '&target=Image-only.svg&content=image';
  const svgResponse = await context.request.get(svgUrl);
  assert.equal(svgResponse.status(), 200); assert.equal(svgResponse.headers()['content-type'], 'image/svg+xml');
  assert.match(svgResponse.headers()['content-disposition'], /^attachment/);
  assert.equal(svgResponse.headers()['x-content-type-options'], 'nosniff');
  const downloadPage = await context.newPage(); const dialogs = [];
  downloadPage.on('dialog', async dialog => { dialogs.push(dialog.message()); await dialog.dismiss(); });
  downloadPage.on('request', r => resourceRequests.push({ url: r.url(), resourceType: r.resourceType() }));
  const downloadPromise = downloadPage.waitForEvent('download');
  await downloadPage.goto(svgUrl).catch(error => { assert.match(String(error), /Download|ERR_ABORTED|download/i); });
  const download = await downloadPromise; await download.saveAs(path.join(out, 'direct-image-download.svg'));
  assert.equal(dialogs.length, 0); assert.equal(resourceRequests.filter(r => r.url.includes('t3-external-probe')).length, 0);
  observations.push({ label: 'direct SVG response downloads; no execution or external resource request', pass: true });
  await downloadPage.close();
  for (const imageName of ['Picture.jpg', 'Picture.gif', 'Picture.webp']) {
    await file(imageName); const img = page.getByRole('region', { name: 'Document preview' }).getByRole('img');
    await img.waitFor(); assert(await img.evaluate(async el => { await el.decode(); return el.complete && el.naturalWidth === 900; }));
    observations.push({ label: 'actual image decoding ' + imageName, pass: true });
  }
  await file('Long filename for readable metadata and breadcrumb wrapping with all content accessible.md');
  for (const width of [960, 900]) {
    await page.setViewportSize({ width, height: 1000 });
    await invariant(`document at ${width}px`);
    const documentPanel = page.getByRole('region', { name: 'Document preview' });
    await documentPanel.scrollIntoViewIfNeeded();
    const box = await documentPanel.boundingBox(); assert(box && box.width > 200);
    if (width === 900) assert(await page.evaluate(() => document.scrollingElement.scrollHeight > innerHeight), 'stacked page has reachable scroll height');
    await screenshot(`document-${width}-light`);
  }
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.getByRole('navigation', { name: 'Document breadcrumb' }).getByRole('button', { name: 'Files', exact: true }).click();
  await page.getByRole('tab', { name: 'Agents', exact: true }).click();
  await page.locator('.woven-navigator-session-list button').first().click();
  await page.getByText('Recorded fixture content; presentation evidence only.', { exact: true }).waitFor();
  await invariant('recorded replay remains alongside primary'); await screenshot('replay-1440-light');
  await page.getByLabel('Panel menu', { exact: true }).click();
  await page.getByRole('button', { name: 'Open parent chat', exact: true }).click();
  await page.getByText('Recorded parent fixture; no live session action.', { exact: true }).waitFor();
  await invariant('recorded parent navigation retains primary'); await screenshot('parent-replay-1440-light');
  const endpoint = target => origin + '/api/working-root/file?projectRoot=' + encodeURIComponent(fixture.projectRoot) + '&target=' + encodeURIComponent(target);
  for (const target of ['../outside.txt', '/etc/passwd']) {
    const response = await context.request.get(endpoint(target)); assert.equal(response.status(), 400);
    observations.push({ label: 'actual endpoint rejects ' + target, status: response.status(), pass: true });
  }
  assert.equal(pageErrors.length, 0, 'no page runtime errors');
  assert(requests.some(r => r.path === '/api/working-root/file' && !r.mocked));
  assert(requests.some(r => r.path === '/api/working-root/tree' && !r.mocked));
  await fs.writeFile(path.join(out, 'result.json'), JSON.stringify({ status: 'PASS', node: process.version, browser: browser.version(), observations, requests, resourceRequests, consoleMessages, pageErrors, claim: 'Local fixture presentation and actual bounded file API. No live-account/runtime/native-display proof. Screenshots require independent visual inspection.' }, null, 2) + '\n');
  await context.close();
} catch (error) {
  if (page) await page.screenshot({ path: path.join(out, 'failure.png'), fullPage: true }).catch(() => {});
  await fs.writeFile(path.join(out, 'result.json'), JSON.stringify({ status: 'FAIL', error: String(error), observations, requests, resourceRequests, consoleMessages, pageErrors }, null, 2) + '\n');
  throw error;
} finally { await browser.close(); }
