import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import readline from 'node:readline';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.join(here, process.env.T3_ATTEMPT || 'attempt-1');
const setup = JSON.parse(await fs.readFile(path.join(here, 'SETUP_RESULT.json'), 'utf8'));
const fixture = JSON.parse(await fs.readFile(path.join(here, '../browser/fixture.json'), 'utf8'));
const origin = process.env.T3_BASE_URL;
assert(origin && new URL(origin).hostname === '127.0.0.1', 'owned loopback URL required');
assert(process.env.T3_FRONTEND && process.env.T3_REPO_ROOT);
const { _electron } = await import(pathToFileURL(process.env.PLAYWRIGHT_MODULE).href);
await fs.mkdir(out, { recursive: true });
await fs.copyFile(fileURLToPath(import.meta.url), path.join(out, 'input-script.mjs'));
await fs.copyFile(path.join(here, '../author', process.env.T3_SOURCE_MANIFEST || 'SOURCE_MANIFEST_v4.json'), path.join(out, 'source-manifest.json'));
await fs.copyFile(path.join(here, 'SETUP_RESULT.json'), path.join(out, 'setup-result.json'));
await fs.copyFile(path.join(here, 'FIXTURE_MANIFEST.json'), path.join(out, 'fixture-manifest.json'));
await fs.copyFile(path.join(here, 'ADDITIONAL_FIXTURE_MANIFEST.json'), path.join(out, 'additional-fixture-manifest.json'));
const env = Object.fromEntries(['PATH', 'HOME', 'TMPDIR', 'LANG', 'LC_CTYPE', '__CF_USER_TEXT_ENCODING']
  .filter(key => process.env[key] !== undefined).map(key => [key, process.env[key]]));
Object.assign(env, { CHIRALITY_USER_DATA: path.join(setup.scratch, 'user-data'),
  CHIRALITY_INSTRUCTION_ROOT: process.env.T3_REPO_ROOT, ELECTRON_RENDERER_URL: origin,
  CHIRALITY_RUNTIME_SOCKET_PATH: path.join(setup.scratch, 'user-data/runtime/control.sock'),
  CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE: path.join(setup.scratch, 'user-data/runtime/auth/tokens/operator.token'),
  CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: 'com.chirality.t3-proof-ac3dexfs', CHIRALITY_DAEMON_GUI_SPAWN: '0' });
const ownedPlist = path.join(env.HOME, 'Library/LaunchAgents', env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL + '.plist');
for (const absent of [ownedPlist, env.CHIRALITY_RUNTIME_SOCKET_PATH, env.CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE]) {
  assert.equal(await fs.lstat(absent).then(() => true, error => { if (error.code === 'ENOENT') return false; throw error; }), false, 'isolated runtime/LaunchAgent target must be absent');
}
await fs.writeFile(path.join(out, 'effective-isolation.json'), JSON.stringify({ environment: env, ownedPlist,
  daemonMode: false, forbiddenActions: ['install', 'start', 'stop', 'uninstall', 'activate-model', 'login', 'send'],
  claim: 'No inherited runtime/credential/provider configuration. HOME is preserved unchanged, not redirected; unique LaunchAgent label status-only. GUI app.isPackaged=false prevents CLI install and no --runtime-daemon enters runtimeHost.' }, null, 2) + '\n');
const application = await _electron.launch({ executablePath: setup.executable.path,
  args: [path.join(process.env.T3_FRONTEND, 'dist-electron/main.js')], cwd: process.env.T3_FRONTEND, env });
const commands = [], pageErrors = [], consoleMessages = [], resourceRequests = [];
let identity;
const write = async (status, extra = {}) => fs.writeFile(path.join(out, 'result.json'), JSON.stringify({ status, identity,
  commands, pageErrors, consoleMessages, resourceRequests, claim: 'Actual isolated macOS Electron development-host UI and native IPC. Native display requires separately captured visual inspection. No packaged-artifact, inline-PDF or live-runtime claim.', ...extra }, null, 2) + '\n');
try {
  identity = await application.evaluate(({ app }) => ({ pid: process.pid, electron: process.versions.electron,
    chrome: process.versions.chrome, node: process.versions.node, packaged: app.isPackaged, userData: app.getPath('userData'), argv: process.argv, socketPath: process.env.CHIRALITY_RUNTIME_SOCKET_PATH, operatorTokenFile: process.env.CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE, launchAgentLabel: process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL }));
  assert.equal(identity.packaged, false); assert.equal(identity.userData, env.CHIRALITY_USER_DATA);
  assert.equal(identity.socketPath, env.CHIRALITY_RUNTIME_SOCKET_PATH); assert.equal(identity.operatorTokenFile, env.CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE);
  assert.equal(identity.launchAgentLabel, env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL); assert(!identity.argv.includes('--runtime-daemon'));
  const page = await application.firstWindow();
  page.on('console', m => consoleMessages.push({ type: m.type(), text: m.text() }));
  page.on('pageerror', e => pageErrors.push({timestamp:new Date().toISOString(),message:String(e),stack:e.stack,url:page.url()}));
  page.on('request', request => resourceRequests.push({ url: request.url(), resourceType: request.resourceType() }));
  await page.context().route('**/api/harness/**', async route => {
    const u = new URL(route.request().url()); let body;
    if (u.pathname === '/api/harness/session/list') body = { sessions: [fixture.session, fixture.parentSession] };
    else if (u.pathname === '/api/harness/agents') body = { agents: fixture.agents };
    else if (u.pathname === `/api/harness/session/${fixture.parentSession.sessionId}/events`) body = { session: fixture.parentSession, events: [fixture.parentEvent], malformedLineCount: 0, summary: { eventCount: 1, firstTimestamp: fixture.parentEvent.timestamp, lastTimestamp: fixture.parentEvent.timestamp } };
    else if (u.pathname === `/api/harness/session/${fixture.session.sessionId}/events`) body = { session: fixture.session, events: [fixture.event], malformedLineCount: 0,
      summary: { eventCount: 1, firstTimestamp: fixture.event.timestamp, lastTimestamp: fixture.event.timestamp } };
    if (body) await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(body) });
    else await route.continue();
  });
  await page.evaluate(projectRoot => {
    localStorage.setItem('chirality.projectRoot', projectRoot);
    localStorage.setItem('chirality.wovenWorkspace.v1', JSON.stringify({ schema: 'chirality.woven-workspace/v1', theme: 'light', navigatorWidth: 240,
      coordinationWidth: 400, activityHeight: 100, activityCollapsed: true, coordinationCollapsed: false, rightPanelView: 'files' }));
  }, fixture.projectRoot);
  await page.reload({ waitUntil: 'networkidle' });
  await page.locator('[data-chat-input="primary"]').waitFor({ state: 'visible' });
  assert.equal(await page.evaluate(() => window.chirality.document.inlinePdfPreview), false);
  assert.equal(pageErrors.length, 0, 'Native startup must hydrate without page errors');
  await write('RUNNING');
  process.stdout.write(JSON.stringify({ event: 'READY', identity, output: out }) + '\n');
  const input = readline.createInterface({ input: process.stdin, terminal: false });
  for await (const line of input) {
    if (!line.trim()) continue;
    const command = JSON.parse(line); const result = { command, timestamp: new Date().toISOString() };
    try {
      if (command.action === 'file') {
        await application.evaluate(({ BrowserWindow }) => { for (const w of BrowserWindow.getAllWindows()) w.closeFilePreview(); });
        const crumb = page.getByRole('navigation', { name: 'Document breadcrumb' });
        if (await crumb.count()) await crumb.getByRole('button', { name: 'Files', exact: true }).click();
        await page.getByRole('button', { name: command.name, exact: true }).click();
        await page.getByRole('region', { name: 'Document preview' }).getByRole('button', { name: 'Open in default app', exact: true }).waitFor();
        result.text = await page.getByRole('region', { name: 'Document preview' }).innerText();
        if (command.name.endsWith('.pdf')) {
          assert.equal(await page.locator('iframe').count(), 0);
          assert.match(result.text, /PDF preview is unavailable here/);
        }
      } else if (command.action === 'image-safety') {
        const img = page.getByRole('region', { name: 'Document preview' }).getByRole('img');
        result.image = await img.evaluate(async el => { await el.decode(); return { complete: el.complete, width: el.naturalWidth, height: el.naturalHeight, src: el.currentSrc }; });
        assert.equal(result.image.complete, true); assert.equal(result.image.width, 900);
        assert.equal(await page.evaluate(() => Boolean(window.__t3SvgExecuted)), false);
        assert.equal(resourceRequests.filter(request => request.url.includes('t3-external-probe')).length, 0);
        result.note = 'Actual image decoding in Electron renderer with unchanged product policy; SVG script marker absent and nested external probe not requested. No OS opening of the adversarial SVG.';
      } else if (command.action === 'quick-look') {
        await application.evaluate(({app,BrowserWindow}) => { const w=BrowserWindow.getAllWindows().find(w=>w.isVisible()); if(w) {w.focus(); app.focus({steal:true});} });
        await page.getByRole('region', { name: 'Document preview' }).getByRole('button', { name: 'Quick Look', exact: true }).click();
        result.note = 'Actual renderer button invoked; native display inspection pending.';
      } else if (command.action === 'reveal-root') {
        const crumb = page.getByRole('navigation', { name: 'Document breadcrumb' });
        if (await crumb.count()) await crumb.getByRole('button', { name: 'Files', exact: true }).click();
        await page.getByLabel('Panel menu', { exact: true }).click();
        await page.getByRole('button', { name: 'Reveal root in Finder', exact: true }).click();
        result.note = 'Actual root Reveal menu invoked; Finder selection inspection pending.';
      } else if (command.action === 'reveal') {
        await page.getByLabel('Panel menu', { exact: true }).click();
        await page.getByRole('button', { name: 'Reveal file in Finder', exact: true }).click();
        result.note = 'Actual renderer Document-menu Reveal invoked; Finder fixture selection inspection pending.';
      } else if (command.action === 'default-app') {
        await page.getByRole('region', { name: 'Document preview' }).getByRole('button', { name: 'Open in default app', exact: true }).click();
        result.note = 'Actual renderer button invoked; default-app display inspection pending.';
      } else if (command.action === 'negative-sender') {
        result.probe = await application.evaluate(async ({ BrowserWindow }, options) => {
          const probe = new BrowserWindow({ show: false, webPreferences: { preload: options.preload,
            contextIsolation: true, sandbox: true, nodeIntegration: false } });
          const id = probe.id;
          try {
            await probe.loadURL('data:text/html,<title>T3 inert unauthorized sender fixture</title>');
            const input = { projectRoot: options.root, target: 'Preview.docx', action: 'open' };
            const response = await probe.webContents.executeJavaScript('window.chirality.document.handoff(' + JSON.stringify(input) + ')');
            return { id, url: probe.webContents.getURL(), response, config: { show: false, contextIsolation: true, sandbox: true, nodeIntegration: false } };
          } finally { probe.destroy(); }
        }, { preload: path.join(process.env.T3_FRONTEND, 'dist-electron/preload.js'), root: fixture.projectRoot });
        assert.equal(result.probe.response.ok, false); assert.equal(result.probe.response.error.code, 'UNAUTHORIZED_SENDER');
        result.note = 'Actual main IPC refused hidden inert foreign sender; owned probe window destroyed.';
      } else if (command.action === 'negative-paths') {
        result.responses = await page.evaluate(async root => {
          const results = [];
          for (const target of ['../outside', '/etc/passwd', 'missing.docx']) results.push({ target,
            result: await window.chirality.document.handoff({ projectRoot: root, target, action: 'open' }) });
          return results;
        }, fixture.projectRoot);
        assert(result.responses.every(r => r.result.ok === false));
      } else if (command.action === 'screenshot') {
        assert(/^[a-z0-9-]+$/.test(command.name));
        await page.screenshot({ path: path.join(out, command.name + '.png'), fullPage: true });
        result.note = 'Renderer screenshot only; native panel requires native UI capture.';
      } else if (command.action === 'close-preview') {
        await application.evaluate(({ BrowserWindow }) => { for (const w of BrowserWindow.getAllWindows()) w.closeFilePreview(); });
      } else if (command.action === 'finish') {
        result.status = 'PASS'; commands.push(result); input.close(); break;
      } else throw new Error('Unknown bounded proof command');
      result.status = 'PASS';
    } catch (error) { result.status = 'FAIL'; result.error = String(error); }
    commands.push(result); await write('RUNNING'); process.stdout.write(JSON.stringify(result) + '\n');
  }
  await application.close();
  await write(commands.some(c => c.status === 'FAIL') || pageErrors.length ? 'FAIL' : 'COMMANDS_COMPLETE_PENDING_VISUAL_FANIN', { cleanup: 'Owned Electron app closed through Playwright; independently verify process exit and native fixture windows.' });
} catch (error) { await write('FAIL', { error: String(error) }); await application.close().catch(() => {}); throw error; }
