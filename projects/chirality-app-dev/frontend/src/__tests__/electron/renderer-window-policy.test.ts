import { describe, expect, it, vi } from 'vitest';
import {
  CONTENT_SECURITY_POLICY_HEADER,
  applyContentSecurityPolicyHeader,
  assertRendererWebPreferences,
  buildRendererContentSecurityPolicy,
  evaluateRendererNavigation,
  evaluateWindowOpen,
  installRendererWindowPolicy,
  rendererWebPreferences,
  runRendererSecurityProbe,
  summarizeDestination,
  type RendererWindowLike
} from '../../../electron/renderer-window-policy';

/**
 * DEL-09-06-V3-01 (G-CSP): renderer window hardening — explicit context
 * isolation / sandbox, window-open denial, navigation containment to the
 * renderer origin, and the renderer Content-Security-Policy — proved on the
 * pure policy and on a fake window that records the installed handlers.
 */

const RENDERER_ORIGIN = 'http://127.0.0.1:41234';

describe('renderer web preferences', () => {
  it('produces exactly the hardened preferences', () => {
    expect(rendererWebPreferences({ preload: '/app/preload.js' })).toEqual({
      preload: '/app/preload.js',
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true
    });
  });

  it.each([
    ['contextIsolation off', { contextIsolation: false, nodeIntegration: false, sandbox: true }],
    ['nodeIntegration on', { contextIsolation: true, nodeIntegration: true, sandbox: true }],
    ['sandbox off', { contextIsolation: true, nodeIntegration: false, sandbox: false }],
    ['missing flags', {}],
    ['webSecurity disabled', { contextIsolation: true, nodeIntegration: false, sandbox: true, webSecurity: false }],
    ['webviewTag enabled', { contextIsolation: true, nodeIntegration: false, sandbox: true, webviewTag: true }],
    ['nodeIntegrationInWorker', { contextIsolation: true, nodeIntegration: false, sandbox: true, nodeIntegrationInWorker: true }],
    ['insecure content', { contextIsolation: true, nodeIntegration: false, sandbox: true, allowRunningInsecureContent: true }]
  ])('fails closed on %s', (_name, preferences) => {
    expect(() => assertRendererWebPreferences(preferences)).toThrow(/hardening policy/);
  });
});

describe('window-open policy', () => {
  it('denies every request', () => {
    expect(evaluateWindowOpen({ url: 'https://example.com/' })).toEqual({ action: 'deny' });
    expect(evaluateWindowOpen({ url: `${RENDERER_ORIGIN}/settings` })).toEqual({ action: 'deny' });
    expect(evaluateWindowOpen({ url: 'about:blank' })).toEqual({ action: 'deny' });
  });
});

describe('navigation policy', () => {
  it.each([
    [`${RENDERER_ORIGIN}/`],
    [`${RENDERER_ORIGIN}/chat?session=abc#top`],
    [`${RENDERER_ORIGIN}/settings/keys`]
  ])('allows the renderer origin: %s', (url) => {
    expect(evaluateRendererNavigation(url, RENDERER_ORIGIN)).toEqual({ allowed: true });
  });

  it.each([
    ['javascript:', 'javascript:alert(1)', 'SCHEME_NOT_HTTP'],
    ['file:', 'file:///Users/someone/.ssh/id_rsa', 'SCHEME_NOT_HTTP'],
    ['data:', 'data:text/html,<script>1</script>', 'SCHEME_NOT_HTTP'],
    ['about:blank', 'about:blank', 'SCHEME_NOT_HTTP'],
    // A blob: URL carries its creator's origin, so origin equality alone would
    // let a renderer-created blob document through; the scheme check stops it.
    ['blob: of the renderer origin', `blob:${RENDERER_ORIGIN}/0000`, 'SCHEME_NOT_HTTP'],
    ['ws: on the renderer host', 'ws://127.0.0.1:41234/', 'SCHEME_NOT_HTTP'],
    ['foreign https', 'https://evil.example/', 'ORIGIN_NOT_RENDERER'],
    ['foreign http', 'http://evil.example/', 'ORIGIN_NOT_RENDERER'],
    ['same host, other port', 'http://127.0.0.1:41235/', 'ORIGIN_NOT_RENDERER'],
    ['same host, other scheme', 'https://127.0.0.1:41234/', 'ORIGIN_NOT_RENDERER'],
    ['localhost alias of the same server', 'http://localhost:41234/', 'ORIGIN_NOT_RENDERER'],
    ['origin embedded in path', `https://evil.example/${RENDERER_ORIGIN}/`, 'ORIGIN_NOT_RENDERER'],
    ['origin as userinfo', 'http://127.0.0.1:41234@evil.example/', 'ORIGIN_NOT_RENDERER'],
    ['unparseable', 'not a url', 'INVALID_URL'],
    ['empty', '', 'INVALID_URL']
  ])('denies %s', (_name, url, reason) => {
    expect(evaluateRendererNavigation(url, RENDERER_ORIGIN)).toEqual({ allowed: false, reason });
  });

  it('denies everything when the renderer origin is empty', () => {
    expect(evaluateRendererNavigation(`${RENDERER_ORIGIN}/`, '')).toEqual({
      allowed: false,
      reason: 'ORIGIN_NOT_RENDERER'
    });
  });
});

describe('content security policy', () => {
  it('builds the packaged policy without eval and closed to frames, objects, and embedding', () => {
    const csp = buildRendererContentSecurityPolicy({ mode: 'packaged' });
    expect(csp).toContain("default-src 'self'");
    expect(csp).toContain("script-src 'self' 'unsafe-inline'");
    expect(csp).not.toContain("'unsafe-eval'");
    expect(csp).toContain("style-src 'self' 'unsafe-inline'");
    expect(csp).toContain("connect-src 'self' https://api.anthropic.com:*");
    expect(csp).not.toContain('ws://');
    expect(csp).toContain("frame-src 'none'");
    expect(csp).toContain("object-src 'none'");
    expect(csp).toContain("base-uri 'self'");
    expect(csp).toContain("form-action 'self'");
    expect(csp).toContain("frame-ancestors 'none'");
    expect(csp).toContain("worker-src 'self'");
    expect(csp.split('; ').every((directive) => /^[a-z-]+ /.test(directive))).toBe(true);
  });

  it('adds eval and the HMR websocket only in development', () => {
    const csp = buildRendererContentSecurityPolicy({
      mode: 'development',
      rendererOrigin: 'http://localhost:3000'
    });
    expect(csp).toContain("script-src 'self' 'unsafe-inline' 'unsafe-eval'");
    expect(csp).toContain(
      "connect-src 'self' https://api.anthropic.com:* ws://localhost:3000 wss://localhost:3000"
    );
    expect(csp).toContain("frame-src 'none'");
  });

  it('never widens connect-src beyond self, the Anthropic host, and the dev websocket', () => {
    for (const csp of [
      buildRendererContentSecurityPolicy({ mode: 'packaged' }),
      buildRendererContentSecurityPolicy({ mode: 'development', rendererOrigin: 'http://localhost:3000' }),
      buildRendererContentSecurityPolicy({ mode: 'development', rendererOrigin: 'garbage' })
    ]) {
      const connect = csp.split('; ').find((directive) => directive.startsWith('connect-src '))!;
      const sources = connect.replace('connect-src ', '').split(' ');
      for (const source of sources) {
        expect(source).toMatch(/^('self'|https:\/\/api\.anthropic\.com:\*|wss?:\/\/localhost:3000)$/);
      }
    }
  });

  it('adds the header to renderer-origin responses that lack one and leaves others alone', () => {
    const csp = buildRendererContentSecurityPolicy({ mode: 'packaged' });

    expect(
      applyContentSecurityPolicyHeader(
        { url: `${RENDERER_ORIGIN}/chat`, responseHeaders: { 'content-type': ['text/html'] } },
        RENDERER_ORIGIN,
        csp
      )
    ).toEqual({ 'content-type': ['text/html'], [CONTENT_SECURITY_POLICY_HEADER]: [csp] });

    const existing = { 'content-security-policy': ["default-src 'none'"] };
    expect(
      applyContentSecurityPolicyHeader({ url: `${RENDERER_ORIGIN}/`, responseHeaders: existing }, RENDERER_ORIGIN, csp)
    ).toBe(existing);

    const foreign = { 'content-type': ['application/json'] };
    expect(
      applyContentSecurityPolicyHeader({ url: 'https://api.anthropic.com/v1/x', responseHeaders: foreign }, RENDERER_ORIGIN, csp)
    ).toBe(foreign);

    expect(applyContentSecurityPolicyHeader({ url: 'not a url' }, RENDERER_ORIGIN, csp)).toEqual({});
    expect(applyContentSecurityPolicyHeader({ url: `${RENDERER_ORIGIN}/x` }, RENDERER_ORIGIN, csp)).toEqual({
      [CONTENT_SECURITY_POLICY_HEADER]: [csp]
    });
  });
});

describe('diagnostics', () => {
  it('summarizes a destination without path, query, or userinfo', () => {
    expect(summarizeDestination('https://user:pw@evil.example/steal?key=sk-secret#x')).toEqual({
      protocol: 'https:',
      hostname: 'evil.example'
    });
    expect(summarizeDestination('javascript:alert(1)')).toEqual({ protocol: 'javascript:', hostname: '' });
    expect(summarizeDestination('nope')).toBeNull();
  });
});

type FakeWindow = RendererWindowLike & {
  handlers: {
    windowOpen?: (details: { url: string }) => { action: 'deny' };
    navigation: Map<string, (event: { preventDefault(): void }, url: string) => void>;
    headers?: (
      details: { url: string; responseHeaders?: Record<string, string[]> },
      callback: (response: { responseHeaders?: Record<string, string[]> }) => void
    ) => void;
    headerFilter?: { urls: string[] };
  };
};

function fakeWindow(): FakeWindow {
  const handlers: FakeWindow['handlers'] = { navigation: new Map() };
  return {
    handlers,
    webContents: {
      setWindowOpenHandler: (handler) => {
        handlers.windowOpen = handler;
      },
      on: (event, listener) => {
        handlers.navigation.set(event, listener);
      },
      session: {
        webRequest: {
          onHeadersReceived: (filter, listener) => {
            handlers.headerFilter = filter;
            handlers.headers = listener;
          }
        }
      }
    }
  };
}

describe('installRendererWindowPolicy', () => {
  const csp = buildRendererContentSecurityPolicy({ mode: 'packaged' });

  it('installs a deny-all window-open handler that logs a redacted destination', () => {
    const window = fakeWindow();
    const log = vi.fn();
    installRendererWindowPolicy(window, { rendererOrigin: RENDERER_ORIGIN, contentSecurityPolicy: csp, log });

    expect(window.handlers.windowOpen!({ url: 'https://evil.example/steal?key=sk-secret' })).toEqual({
      action: 'deny'
    });
    expect(window.handlers.windowOpen!({ url: `${RENDERER_ORIGIN}/settings` })).toEqual({ action: 'deny' });
    expect(log).toHaveBeenCalledWith('warn', 'renderer.window_open.denied', {
      destination: { protocol: 'https:', hostname: 'evil.example' }
    });
    expect(JSON.stringify(log.mock.calls)).not.toContain('sk-secret');
  });

  it.each(['will-navigate', 'will-redirect'] as const)(
    '%s allows only the renderer origin and prevents everything else',
    (eventName) => {
      const window = fakeWindow();
      const log = vi.fn();
      installRendererWindowPolicy(window, { rendererOrigin: RENDERER_ORIGIN, contentSecurityPolicy: csp, log });
      const listener = window.handlers.navigation.get(eventName)!;

      const allowed = { preventDefault: vi.fn() };
      listener(allowed, `${RENDERER_ORIGIN}/chat?x=1`);
      expect(allowed.preventDefault).not.toHaveBeenCalled();

      for (const url of [
        'https://evil.example/',
        'javascript:alert(1)',
        'file:///etc/passwd',
        'http://127.0.0.1:41235/',
        'not a url'
      ]) {
        const denied = { preventDefault: vi.fn() };
        listener(denied, url);
        expect(denied.preventDefault).toHaveBeenCalledTimes(1);
      }
      expect(log).toHaveBeenCalledTimes(5);
      expect(log).toHaveBeenCalledWith('warn', 'renderer.navigation.denied', {
        event: eventName,
        reason: 'ORIGIN_NOT_RENDERER',
        destination: { protocol: 'https:', hostname: 'evil.example' }
      });
      expect(log).toHaveBeenCalledWith('warn', 'renderer.navigation.denied', {
        event: eventName,
        reason: 'SCHEME_NOT_HTTP',
        destination: { protocol: 'javascript:', hostname: '' }
      });
      expect(log).toHaveBeenCalledWith('warn', 'renderer.navigation.denied', {
        event: eventName,
        reason: 'INVALID_URL',
        destination: null
      });
    }
  );

  it('registers both navigation events', () => {
    const window = fakeWindow();
    installRendererWindowPolicy(window, { rendererOrigin: RENDERER_ORIGIN, contentSecurityPolicy: csp });
    expect([...window.handlers.navigation.keys()].sort()).toEqual(['will-navigate', 'will-redirect']);
  });

  it('attaches the CSP through onHeadersReceived for renderer-origin responses only', () => {
    const window = fakeWindow();
    installRendererWindowPolicy(window, { rendererOrigin: RENDERER_ORIGIN, contentSecurityPolicy: csp });
    expect(window.handlers.headerFilter).toEqual({ urls: ['http://*/*', 'https://*/*'] });

    const callback = vi.fn();
    window.handlers.headers!({ url: `${RENDERER_ORIGIN}/`, responseHeaders: { a: ['1'] } }, callback);
    expect(callback).toHaveBeenCalledWith({
      responseHeaders: { a: ['1'], [CONTENT_SECURITY_POLICY_HEADER]: [csp] }
    });

    const preset = { 'Content-Security-Policy': ["default-src 'none'"] };
    window.handlers.headers!({ url: `${RENDERER_ORIGIN}/`, responseHeaders: preset }, callback);
    expect(callback).toHaveBeenLastCalledWith({ responseHeaders: preset });

    const foreign = { b: ['2'] };
    window.handlers.headers!({ url: 'https://api.anthropic.com/v1/messages', responseHeaders: foreign }, callback);
    expect(callback).toHaveBeenLastCalledWith({ responseHeaders: foreign });
  });

  it('works without a log sink', () => {
    const window = fakeWindow();
    installRendererWindowPolicy(window, { rendererOrigin: RENDERER_ORIGIN, contentSecurityPolicy: csp });
    const denied = { preventDefault: vi.fn() };
    window.handlers.navigation.get('will-navigate')!(denied, 'https://evil.example/');
    expect(denied.preventDefault).toHaveBeenCalled();
    expect(window.handlers.windowOpen!({ url: 'https://evil.example/' })).toEqual({ action: 'deny' });
  });
});

describe('runRendererSecurityProbe', () => {
  function probeWindow(loading: boolean) {
    return {
      isLoadingMainFrame: vi.fn(() => loading),
      once: vi.fn<(event: 'did-finish-load', listener: () => void) => unknown>(),
      executeJavaScript: vi.fn<(code: string, userGesture?: boolean) => Promise<unknown>>()
    };
  }

  it('does nothing unless the environment asks for it', () => {
    const webContents = probeWindow(false);
    runRendererSecurityProbe({ webContents }, { env: {} });
    runRendererSecurityProbe({ webContents }, { env: { CHIRALITY_RENDERER_SECURITY_PROBE: '0' } });
    expect(webContents.isLoadingMainFrame).not.toHaveBeenCalled();
    expect(webContents.executeJavaScript).not.toHaveBeenCalled();
  });

  it('runs the probe after load and reports it under the marker', async () => {
    vi.useFakeTimers();
    const info = vi.spyOn(console, 'info').mockImplementation(() => undefined);
    try {
      const webContents = probeWindow(true);
      webContents.executeJavaScript.mockResolvedValue({ policy: 'G-CSP', windowOpen: { returned: 'null' } });
      runRendererSecurityProbe(
        { webContents },
        { env: { CHIRALITY_RENDERER_SECURITY_PROBE: '1', CHIRALITY_RENDERER_SECURITY_PROBE_DELAY_MS: '10' } }
      );
      expect(webContents.once).toHaveBeenCalledWith('did-finish-load', expect.any(Function));
      webContents.once.mock.calls[0][1]();
      await vi.advanceTimersByTimeAsync(20);
      expect(webContents.executeJavaScript).toHaveBeenCalledTimes(1);
      const [code, userGesture] = webContents.executeJavaScript.mock.calls[0];
      expect(userGesture).toBe(true);
      expect(code).toContain("securitypolicyviolation");
      expect(code).toContain("window.open('https://example.com/chirality-renderer-security-window-open'");
      expect(code).toContain("location.assign(navigationTarget)");
      expect(code).toContain("headers.get('content-security-policy')");
      expect(info).toHaveBeenCalledWith(
        '[renderer-security-probe]',
        JSON.stringify({ policy: 'G-CSP', windowOpen: { returned: 'null' } })
      );
    } finally {
      info.mockRestore();
      vi.useRealTimers();
    }
  });
});
