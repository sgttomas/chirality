import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const [port, action, ...args] = process.argv.slice(2);
if (!/^\d+$/u.test(port ?? '')) throw new Error('port required');

const targets = await fetch(`http://127.0.0.1:${port}/json/list`).then((response) => {
  if (!response.ok) throw new Error(`CDP target discovery failed: ${response.status}`);
  return response.json();
});
const target = targets.find((entry) => entry.type === 'page');
if (!target?.webSocketDebuggerUrl) throw new Error('No packaged renderer page target');

const socket = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {
  socket.addEventListener('open', resolve, { once: true });
  socket.addEventListener('error', reject, { once: true });
});

let nextId = 0;
const pending = new Map();
socket.addEventListener('message', (event) => {
  const message = JSON.parse(event.data);
  if (!message.id) return;
  const waiter = pending.get(message.id);
  if (!waiter) return;
  pending.delete(message.id);
  if (message.error) waiter.reject(new Error(JSON.stringify(message.error)));
  else waiter.resolve(message.result);
});

function call(method, params = {}) {
  const id = ++nextId;
  const promise = new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
  socket.send(JSON.stringify({ id, method, params }));
  return promise;
}

async function evaluate(expression) {
  const result = await call('Runtime.evaluate', {
    expression,
    awaitPromise: true,
    returnByValue: true
  });
  if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
  return result.result?.value;
}

const domExpression = `(() => {
  const compact = (value) => (value ?? '').replace(/\\s+/gu, ' ').trim();
  const buttons = [...document.querySelectorAll('button')].map((button, index) => ({
    index,
    text: compact(button.innerText || button.textContent),
    disabled: button.disabled,
    ariaPressed: button.getAttribute('aria-pressed'),
    ariaExpanded: button.getAttribute('aria-expanded'),
    ariaCurrent: button.getAttribute('aria-current'),
    sessionId: button.getAttribute('data-session-id'),
    type: button.type
  }));
  const inputs = [...document.querySelectorAll('input,select,textarea')].map((input, index) => ({
    index,
    tag: input.tagName,
    ariaLabel: input.getAttribute('aria-label'),
    dataChatInput: input.getAttribute('data-chat-input'),
    placeholder: input.getAttribute('placeholder'),
    value: input.value,
    disabled: input.disabled
  }));
  const surfaces = [...document.querySelectorAll('[data-woven-surface]')].map((element) => ({
    value: element.getAttribute('data-woven-surface'),
    text: compact(element.innerText || element.textContent).slice(0, 4000)
  }));
  return {
    capturedAt: new Date().toISOString(),
    url: location.href,
    origin: location.origin,
    pathname: location.pathname,
    title: document.title,
    readyState: document.readyState,
    bodyText: compact(document.body?.innerText || '').slice(0, 30000),
    bodyHtmlShaInputLength: document.documentElement?.outerHTML.length ?? 0,
    surfaces,
    buttons,
    inputs,
    primaryDialogueMounted: Boolean(document.querySelector('[data-chat-input="primary"]')),
    primaryDialogueDisabled: document.querySelector('[data-chat-input="primary"]')?.disabled ?? null,
    selectedSessionId: document.querySelector('button[data-session-id][aria-pressed="true"]')?.getAttribute('data-session-id') ?? null,
    sessionRows: [...document.querySelectorAll('button[data-session-id]')].map((button) => ({
      sessionId: button.getAttribute('data-session-id'),
      text: compact(button.innerText || button.textContent),
      disabled: button.disabled,
      ariaPressed: button.getAttribute('aria-pressed')
    })),
    resources: performance.getEntriesByType('resource').map((entry) => entry.name).slice(0, 500)
  };
})()`;

async function capture(label, directory) {
  await mkdir(directory, { recursive: true });
  await call('Page.enable');
  await call('Runtime.enable');
  await call('Accessibility.enable');
  const dom = await evaluate(domExpression);
  const ax = await call('Accessibility.getFullAXTree');
  const shot = await call('Page.captureScreenshot', {
    format: 'png',
    fromSurface: true,
    captureBeyondViewport: false
  });
  await writeFile(path.join(directory, `${label}.dom.json`), `${JSON.stringify(dom, null, 2)}\n`);
  await writeFile(path.join(directory, `${label}.ax.json`), `${JSON.stringify(ax, null, 2)}\n`);
  await writeFile(path.join(directory, `${label}.png`), Buffer.from(shot.data, 'base64'));
  return { label, target: { id: target.id, title: target.title, url: target.url }, dom };
}

async function clickSurface(label) {
  return evaluate(`(() => {
    const target = ${JSON.stringify(label)};
    const button = [...document.querySelectorAll('button')].find((candidate) =>
      candidate.querySelector('span')?.textContent?.trim() === target
    );
    if (!button) return { clicked: false, reason: 'not-found' };
    const before = { disabled: button.disabled, ariaCurrent: button.getAttribute('aria-current'), ariaExpanded: button.getAttribute('aria-expanded') };
    button.click();
    return { clicked: true, before };
  })()`);
}

async function clickSession(sessionId) {
  return evaluate(`(() => {
    const button = document.querySelector('button[data-session-id=${JSON.stringify(sessionId)}]');
    if (!button) return { clicked: false, reason: 'not-found' };
    const before = { disabled: button.disabled, ariaPressed: button.getAttribute('aria-pressed') };
    button.click();
    return { clicked: true, before };
  })()`);
}

async function clickButtonText(text) {
  return evaluate(`(() => {
    const expected = ${JSON.stringify(text)};
    const button = [...document.querySelectorAll('button')].find((candidate) =>
      candidate.textContent?.replace(/\\s+/gu, ' ').trim().startsWith(expected)
    );
    if (!button) return { clicked: false, reason: 'not-found' };
    const before = { disabled: button.disabled, ariaPressed: button.getAttribute('aria-pressed'), ariaExpanded: button.getAttribute('aria-expanded') };
    button.click();
    return { clicked: true, before };
  })()`);
}

async function submitChat(message) {
  return evaluate(`(async () => {
    const input = document.querySelector('[data-chat-input="primary"]');
    if (!input) return { submitted: false, reason: 'input-not-found' };
    const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
    setter.call(input, ${JSON.stringify(message)});
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
    await new Promise((resolve) => requestAnimationFrame(() => resolve()));
    const form = input.closest('form');
    const button = form?.querySelector('button[type="submit"]');
    if (!button) return { submitted: false, reason: 'submit-not-found', inputDisabled: input.disabled };
    button.click();
    return { submitted: true, inputDisabled: input.disabled, submitDisabled: button.disabled };
  })()`);
}

async function applyWorkingRoot(rootPath) {
  return evaluate(`(async () => {
    const input = [...document.querySelectorAll('input')].find((candidate) =>
      candidate.getAttribute('placeholder') === '/absolute/path/to/execution/root'
    );
    if (!input) return { applied: false, reason: 'input-not-found' };
    const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
    setter.call(input, ${JSON.stringify(rootPath)});
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
    await new Promise((resolve) => requestAnimationFrame(() => resolve()));
    const button = [...document.querySelectorAll('button')].find((candidate) =>
      candidate.textContent?.trim() === 'Apply Path'
    );
    if (!button) return { applied: false, reason: 'button-not-found', inputDisabled: input.disabled };
    const before = { inputDisabled: input.disabled, applyDisabled: button.disabled, value: input.value };
    button.click();
    return { applied: true, before };
  })()`);
}

let output;
if (action === 'targets') {
  output = targets;
} else if (action === 'capture') {
  output = await capture(args[0], path.resolve(args[1]));
} else if (action === 'surface') {
  output = await clickSurface(args[0]);
} else if (action === 'session') {
  output = await clickSession(args[0]);
} else if (action === 'button') {
  output = await clickButtonText(args[0]);
} else if (action === 'chat') {
  output = await submitChat(args[0]);
} else if (action === 'root') {
  output = await applyWorkingRoot(args[0]);
} else if (action === 'state') {
  output = await evaluate(domExpression);
} else {
  throw new Error(`Unknown action: ${action}`);
}

process.stdout.write(`${JSON.stringify(output, null, 2)}\n`);
socket.close();
