import { describe, expect, it, vi } from 'vitest';
import {
  CONTENT_SECURITY_POLICY_HEADER,
  EGRESS_LAYER_PROBE_URL,
  applyContentSecurityPolicyHeader,
  applyPackagedRendererRequestPolicy,
  assertRendererWebPreferences,
  buildRendererContentSecurityPolicy,
  createRendererCspNonce,
  evaluateRendererNavigation,
  evaluateWindowOpen,
  installRendererWindowPolicy,
  rendererWebPreferences,
  runEgressLayerProbe,
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
const PACKAGED_NONCE = 'AQIDBAUGBwgJCgsMDQ4PEA==';

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
  it('never creates a child window; hands http(s) targets to the system browser', () => {
    expect(evaluateWindowOpen({ url: 'https://example.com/docs?x=1' })).toEqual({
      action: 'deny',
      external: true
    });
    expect(evaluateWindowOpen({ url: 'http://example.com/' })).toEqual({ action: 'deny', external: true });
    expect(evaluateWindowOpen({ url: `${RENDERER_ORIGIN}/settings` })).toEqual({
      action: 'deny',
      external: true
    });
  });

  it.each([
    ['javascript:', 'javascript:alert(1)'],
    ['file:', 'file:///etc/passwd'],
    ['data:', 'data:text/html,<script>1</script>'],
    ['blob:', `blob:${RENDERER_ORIGIN}/0000`],
    ['about:', 'about:blank'],
    ['custom scheme', 'chirality://open'],
    ['ws:', 'ws://example.com/']
  ])('drops %s without any external open', (_name, url) => {
    expect(evaluateWindowOpen({ url })).toEqual({
      action: 'deny',
      external: false,
      reason: 'SCHEME_NOT_HTTP'
    });
  });

  it('drops a malformed URL', () => {
    expect(evaluateWindowOpen({ url: 'not a url' })).toEqual({
      action: 'deny',
      external: false,
      reason: 'INVALID_URL'
    });
    expect(evaluateWindowOpen({ url: '' })).toEqual({ action: 'deny', external: false, reason: 'INVALID_URL' });
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
  it('builds the packaged policy with one nonce, no inline/eval allowance, and closed directives', () => {
    const csp = buildRendererContentSecurityPolicy({ mode: 'packaged', nonce: PACKAGED_NONCE });
    const scriptDirective = csp
      .split('; ')
      .find((directive) => directive.startsWith('script-src '));
    expect(csp).toContain("default-src 'self'");
    expect(csp).toContain(`script-src 'self' 'nonce-${PACKAGED_NONCE}'`);
    expect(scriptDirective).not.toContain("'unsafe-inline'");
    expect(scriptDirective).not.toContain("'unsafe-eval'");
    expect(csp).toContain("style-src 'self' 'unsafe-inline'");
    expect(csp).toContain("connect-src 'self';");
    expect(csp).not.toContain('api.anthropic.com');
    expect(csp).not.toContain('ws://');
    expect(csp).toContain("frame-src 'none'");
    expect(csp).toContain("object-src 'none'");
    expect(csp).toContain("base-uri 'self'");
    expect(csp).toContain("form-action 'self'");
    expect(csp).toContain("frame-ancestors 'none'");
    expect(csp).toContain("worker-src 'self'");
    expect(csp.split('; ').every((directive) => /^[a-z-]+ /.test(directive))).toBe(true);
  });

  it('fails closed without a valid packaged nonce and creates fresh 128-bit nonces', () => {
    expect(() => buildRendererContentSecurityPolicy({ mode: 'packaged' })).toThrow(
      /requires a valid request nonce/
    );
    expect(() =>
      buildRendererContentSecurityPolicy({ mode: 'packaged', nonce: "bad'; script-src *" })
    ).toThrow(/requires a valid request nonce/);

    const first = createRendererCspNonce();
    const second = createRendererCspNonce();
    expect(first).toMatch(/^[A-Za-z0-9+/_-]+={0,2}$/);
    expect(Buffer.from(first, 'base64')).toHaveLength(16);
    expect(second).toMatch(/^[A-Za-z0-9+/_-]+={0,2}$/);
    expect(Buffer.from(second, 'base64')).toHaveLength(16);
    expect(second).not.toBe(first);
  });

  it('attaches one byte-identical per-request policy to Next and the response', () => {
    const request = { headers: {} as Record<string, string | string[] | undefined> };
    const response = { setHeader: vi.fn() };
    const result = applyPackagedRendererRequestPolicy(request, response, PACKAGED_NONCE);

    expect(result.nonce).toBe(PACKAGED_NONCE);
    expect(request.headers['content-security-policy']).toBe(result.contentSecurityPolicy);
    expect(response.setHeader).toHaveBeenCalledWith(
      CONTENT_SECURITY_POLICY_HEADER,
      result.contentSecurityPolicy
    );
    expect(
      result.contentSecurityPolicy
        .split('; ')
        .find((directive) => directive.startsWith('script-src '))
    ).not.toContain("'unsafe-inline'");
  });

  it('adds eval and the HMR websocket only in development', () => {
    const csp = buildRendererContentSecurityPolicy({
      mode: 'development',
      rendererOrigin: 'http://localhost:3000'
    });
    expect(csp).toBe(
      [
        "default-src 'self'",
        "script-src 'self' 'unsafe-inline' 'unsafe-eval'",
        "style-src 'self' 'unsafe-inline'",
        "img-src 'self' data:",
        "font-src 'self' data:",
        "connect-src 'self' ws://localhost:3000 wss://localhost:3000",
        "worker-src 'self'",
        "manifest-src 'self'",
        "media-src 'self'",
        "frame-src 'none'",
        "object-src 'none'",
        "base-uri 'self'",
        "form-action 'self'",
        "frame-ancestors 'none'"
      ].join('; ')
    );
    expect(csp).not.toContain('api.anthropic.com');
  });

  it('never widens connect-src beyond self and the dev websocket', () => {
    for (const csp of [
      buildRendererContentSecurityPolicy({ mode: 'packaged', nonce: PACKAGED_NONCE }),
      buildRendererContentSecurityPolicy({ mode: 'development', rendererOrigin: 'http://localhost:3000' }),
      buildRendererContentSecurityPolicy({ mode: 'development', rendererOrigin: 'garbage' })
    ]) {
      const connect = csp.split('; ').find((directive) => directive.startsWith('connect-src '))!;
      const sources = connect.replace('connect-src ', '').split(' ');
      for (const source of sources) {
        expect(source).toMatch(/^('self'|wss?:\/\/localhost:3000)$/);
      }
    }
  });

  it('adds the header to renderer-origin responses that lack one and leaves others alone', () => {
    const csp = buildRendererContentSecurityPolicy({ mode: 'packaged', nonce: PACKAGED_NONCE });

    expect(
      applyContentSecurityPolicyHeader(
        { url: `${RENDERER_ORIGIN}/chat`, responseHeaders: { 'content-type': ['text/html'] } },
        RENDERER_ORIGIN,
        csp
      )
    ).toEqual({ 'content-type': ['text/html'], [CONTENT_SECURITY_POLICY_HEADER]: [csp] });

    // Untouched responses yield null — never an echoed (possibly empty) header set.
    const existing = { 'content-security-policy': ["default-src 'none'"] };
    expect(
      applyContentSecurityPolicyHeader({ url: `${RENDERER_ORIGIN}/`, responseHeaders: existing }, RENDERER_ORIGIN, csp)
    ).toBeNull();

    const foreign = { 'content-type': ['application/json'] };
    expect(
      applyContentSecurityPolicyHeader({ url: 'https://api.anthropic.com/v1/x', responseHeaders: foreign }, RENDERER_ORIGIN, csp)
    ).toBeNull();

    expect(applyContentSecurityPolicyHeader({ url: 'not a url' }, RENDERER_ORIGIN, csp)).toBeNull();
    expect(applyContentSecurityPolicyHeader({ url: 'https://evil.example/' }, RENDERER_ORIGIN, csp)).toBeNull();
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
  const csp = buildRendererContentSecurityPolicy({ mode: 'packaged', nonce: PACKAGED_NONCE });
  // The external open is deferred to a microtask so a synchronous throw is caught
  // structurally; assertions on it wait for the task queue to drain.
  const flush = () => new Promise<void>((resolve) => setTimeout(resolve, 0));

  function install(window: FakeWindow, log = vi.fn(), openExternal = vi.fn<(url: string) => Promise<void>>()) {
    openExternal.mockResolvedValue();
    installRendererWindowPolicy(window, {
      rendererOrigin: RENDERER_ORIGIN,
      contentSecurityPolicy: csp,
      openExternal,
      log
    });
    return { log, openExternal };
  }

  it('denies the child window and opens http(s) targets externally, exactly once, with the exact URL', async () => {
    const window = fakeWindow();
    const { log, openExternal } = install(window);

    const url = 'https://docs.example/page?section=2#top';
    expect(window.handlers.windowOpen!({ url })).toEqual({ action: 'deny' });
    expect(log).toHaveBeenCalledWith('info', 'renderer.window_open.external_opened', {
      destination: { protocol: 'https:', hostname: 'docs.example' }
    });
    await flush();
    expect(openExternal).toHaveBeenCalledTimes(1);
    expect(openExternal).toHaveBeenCalledWith(url);

    expect(window.handlers.windowOpen!({ url: 'http://plain.example/' })).toEqual({ action: 'deny' });
    await flush();
    expect(openExternal).toHaveBeenCalledTimes(2);
    expect(openExternal).toHaveBeenLastCalledWith('http://plain.example/');
    expect(log).not.toHaveBeenCalledWith('warn', 'renderer.window_open.denied', expect.anything());
    expect(log).not.toHaveBeenCalledWith('warn', 'renderer.window_open.external_failed', expect.anything());
  });

  it.each([
    ['javascript:', 'javascript:alert(document.cookie)'],
    ['file:', 'file:///Users/someone/.ssh/id_rsa'],
    ['data:', 'data:text/html,<script>1</script>'],
    ['blob:', `blob:${RENDERER_ORIGIN}/0000`],
    ['about:', 'about:blank#probe'],
    ['custom scheme', 'chirality://open?key=sk-secret']
  ])('denies %s without opening anything', async (_name, url) => {
    const window = fakeWindow();
    const { log, openExternal } = install(window);

    expect(window.handlers.windowOpen!({ url })).toEqual({ action: 'deny' });
    await flush();
    expect(openExternal).not.toHaveBeenCalled();
    expect(log).toHaveBeenCalledTimes(1);
    expect(log).toHaveBeenCalledWith('warn', 'renderer.window_open.denied', {
      reason: 'SCHEME_NOT_HTTP',
      destination: summarizeDestination(url)
    });
    expect(JSON.stringify(log.mock.calls)).not.toContain('sk-secret');
  });

  it('denies a malformed URL without opening anything', async () => {
    const window = fakeWindow();
    const { log, openExternal } = install(window);

    expect(window.handlers.windowOpen!({ url: 'not a url' })).toEqual({ action: 'deny' });
    await flush();
    expect(openExternal).not.toHaveBeenCalled();
    expect(log).toHaveBeenCalledWith('warn', 'renderer.window_open.denied', {
      reason: 'INVALID_URL',
      destination: null
    });
  });

  it('catches a synchronous throw from the opener the same way as a rejection', async () => {
    const window = fakeWindow();
    const log = vi.fn();
    const openExternal = vi.fn<(url: string) => Promise<void>>(() => {
      throw new Error('sync failure for sk-secret');
    });
    installRendererWindowPolicy(window, {
      rendererOrigin: RENDERER_ORIGIN,
      contentSecurityPolicy: csp,
      openExternal,
      log
    });

    expect(() => window.handlers.windowOpen!({ url: 'https://docs.example/' })).not.toThrow();
    expect(window.handlers.windowOpen!({ url: 'https://docs.example/' })).toEqual({ action: 'deny' });
    await flush();
    expect(openExternal).toHaveBeenCalledTimes(2);
    expect(log).toHaveBeenCalledWith('warn', 'renderer.window_open.external_failed', {
      destination: { protocol: 'https:', hostname: 'docs.example' },
      error: 'sync failure for sk-secret'
    });
  });

  it('logs a redacted line when the external open fails, without throwing', async () => {
    const window = fakeWindow();
    const log = vi.fn();
    const openExternal = vi.fn<(url: string) => Promise<void>>().mockRejectedValue(new Error('no browser for sk-secret'));
    installRendererWindowPolicy(window, {
      rendererOrigin: RENDERER_ORIGIN,
      contentSecurityPolicy: csp,
      openExternal,
      log
    });

    expect(window.handlers.windowOpen!({ url: 'https://docs.example/' })).toEqual({ action: 'deny' });
    await flush();
    expect(log).toHaveBeenCalledWith('warn', 'renderer.window_open.external_failed', {
      destination: { protocol: 'https:', hostname: 'docs.example' },
      error: 'no browser for sk-secret'
    });
  });

  it.each(['will-navigate', 'will-redirect'] as const)(
    '%s allows only the renderer origin and prevents everything else',
    (eventName) => {
      const window = fakeWindow();
      const { log } = install(window);
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
    install(window);
    expect([...window.handlers.navigation.keys()].sort()).toEqual(['will-navigate', 'will-redirect']);
  });

  it('attaches the CSP through onHeadersReceived and leaves every other response untouched', () => {
    const window = fakeWindow();
    install(window);
    expect(window.handlers.headerFilter).toEqual({ urls: ['http://*/*', 'https://*/*'] });

    const callback = vi.fn();
    window.handlers.headers!({ url: `${RENDERER_ORIGIN}/`, responseHeaders: { a: ['1'] } }, callback);
    expect(callback).toHaveBeenCalledWith({
      responseHeaders: { a: ['1'], [CONTENT_SECURITY_POLICY_HEADER]: [csp] }
    });

    // Untouched responses get no override at all — `{}` — never an echoed set.
    const preset = { 'Content-Security-Policy': ["default-src 'none'"] };
    window.handlers.headers!({ url: `${RENDERER_ORIGIN}/`, responseHeaders: preset }, callback);
    expect(callback).toHaveBeenLastCalledWith({});

    window.handlers.headers!({ url: 'https://api.anthropic.com/v1/messages', responseHeaders: { b: ['2'] } }, callback);
    expect(callback).toHaveBeenLastCalledWith({});

    window.handlers.headers!({ url: 'https://evil.example/' }, callback);
    expect(callback).toHaveBeenLastCalledWith({});
  });

  it('does not synthesize a packaged fallback without the request nonce', () => {
    const window = fakeWindow();
    installRendererWindowPolicy(window, {
      rendererOrigin: RENDERER_ORIGIN,
      openExternal: vi.fn()
    });
    const callback = vi.fn();
    window.handlers.headers!(
      { url: `${RENDERER_ORIGIN}/`, responseHeaders: { a: ['1'] } },
      callback
    );
    expect(callback).toHaveBeenCalledWith({});
  });

  it('works without a log sink', async () => {
    const window = fakeWindow();
    const openExternal = vi.fn<(url: string) => Promise<void>>().mockResolvedValue();
    installRendererWindowPolicy(window, { rendererOrigin: RENDERER_ORIGIN, contentSecurityPolicy: csp, openExternal });
    const denied = { preventDefault: vi.fn() };
    window.handlers.navigation.get('will-navigate')!(denied, 'https://evil.example/');
    expect(denied.preventDefault).toHaveBeenCalled();
    expect(window.handlers.windowOpen!({ url: 'https://evil.example/' })).toEqual({ action: 'deny' });
    expect(window.handlers.windowOpen!({ url: 'javascript:1' })).toEqual({ action: 'deny' });
    await flush();
    expect(openExternal).toHaveBeenCalledWith('https://evil.example/');
    expect(openExternal).toHaveBeenCalledTimes(1);
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
      // about:blank, not an http(s) URL: the proof must never open the host's browser.
      expect(code).toContain("window.open('about:blank#chirality-renderer-security-window-open'");
      expect(code).not.toContain("window.open('http");
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

describe('runEgressLayerProbe', () => {
  /**
   * DEL-09-06-V3-05: the probe's destination is fixed in the module and cannot be
   * supplied from outside. It must be a destination the REQ-NET-001 egress policy
   * in `main.ts` denies — the allowlisted Anthropic host on a port other than 443
   * (the policy's port rule, pinned in contract-pins.manifest.ts) — so the probe
   * can never produce a request the egress layer would let through.
   */
  const EXPECTED_DESTINATION = { protocol: 'https:', hostname: 'api.anthropic.com', port: '8443' };

  // URLs the egress policy WOULD allow (Anthropic host over https on 443 / default
  // port; loopback hosts) plus one foreign host: none of them may become the probe's
  // destination, however the environment is set.
  const NOT_PROBE_DESTINATIONS = [
    'https://api.anthropic.com/v1/messages',
    'https://api.anthropic.com:443/v1/messages',
    'http://127.0.0.1:3000/api/session',
    'http://localhost:3000/',
    'http://[::1]:8080/',
    'https://example.com/chirality-egress-probe-redirect'
  ];

  function egressWindow(loading: boolean) {
    const fetch = vi.fn<(input: string, init?: unknown) => Promise<{ status: number }>>();
    return {
      webContents: {
        isLoadingMainFrame: vi.fn(() => loading),
        once: vi.fn<(event: 'did-finish-load', listener: () => void) => unknown>(),
        session: { fetch }
      },
      fetch
    };
  }

  it('fixes the destination to the allowlisted Anthropic host on a port the egress policy denies', () => {
    const parsed = new URL(EGRESS_LAYER_PROBE_URL);
    expect(parsed.protocol).toBe('https:');
    expect(parsed.hostname).toBe('api.anthropic.com');
    // The policy allows this host only with an empty or 443 port; anything else is
    // `anthropic_port_not_allowlisted:<port>` — the diagnostic the packaged proof counts.
    expect(parsed.port).not.toBe('');
    expect(parsed.port).not.toBe('443');
    expect(parsed.port).toBe('8443');
    expect(['localhost', '127.0.0.1', '[::1]']).not.toContain(parsed.hostname);
    expect(parsed.username).toBe('');
    expect(parsed.password).toBe('');
    expect(parsed.search).toBe('');
    expect(EGRESS_LAYER_PROBE_URL).toBe(
      'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked'
    );
  });

  it('does nothing without the gate, whatever else the environment says', () => {
    const environments = [
      {},
      { CHIRALITY_RENDERER_SECURITY_PROBE: '0' },
      { CHIRALITY_RENDERER_SECURITY_PROBE: 'true' },
      { CHIRALITY_EGRESS_LAYER_PROBE_URL: EGRESS_LAYER_PROBE_URL }
    ];
    for (const env of environments) {
      const window = egressWindow(false);
      runEgressLayerProbe(window, { env });
      expect(window.webContents.isLoadingMainFrame).not.toHaveBeenCalled();
      expect(window.fetch).not.toHaveBeenCalled();
    }
  });

  it('cannot be pointed at any other destination by the environment', async () => {
    vi.useFakeTimers();
    const info = vi.spyOn(console, 'info').mockImplementation(() => undefined);
    try {
      for (const url of NOT_PROBE_DESTINATIONS) {
        info.mockClear();
        const window = egressWindow(false);
        window.fetch.mockRejectedValue(new Error('net::ERR_BLOCKED_BY_CLIENT'));
        runEgressLayerProbe(window, {
          env: {
            CHIRALITY_RENDERER_SECURITY_PROBE: '1',
            CHIRALITY_RENDERER_SECURITY_PROBE_DELAY_MS: '10',
            CHIRALITY_EGRESS_LAYER_PROBE_URL: url
          }
        });
        await vi.advanceTimersByTimeAsync(600);
        expect(window.fetch).toHaveBeenCalledTimes(1);
        expect(window.fetch.mock.calls[0][0]).toBe(EGRESS_LAYER_PROBE_URL);
        expect(window.fetch.mock.calls[0][0]).not.toBe(url);
        const logged = JSON.parse(info.mock.calls[0][1] as string) as { destination: unknown };
        expect(logged.destination).toEqual(EXPECTED_DESTINATION);
        expect(JSON.stringify(info.mock.calls)).not.toContain(new URL(url).pathname);
      }
    } finally {
      info.mockRestore();
      vi.useRealTimers();
    }
  });

  it('takes no destination from its caller', () => {
    // Signature: (window, { env }) — there is no URL parameter or option.
    expect(runEgressLayerProbe.length).toBe(2);
  });

  it('issues the request through the window session and reports a rejection as the expected outcome', async () => {
    vi.useFakeTimers();
    const info = vi.spyOn(console, 'info').mockImplementation(() => undefined);
    try {
      const window = egressWindow(false);
      window.fetch.mockRejectedValue(new Error('net::ERR_BLOCKED_BY_CLIENT'));
      runEgressLayerProbe(window, {
        env: {
          CHIRALITY_RENDERER_SECURITY_PROBE: '1',
          CHIRALITY_RENDERER_SECURITY_PROBE_DELAY_MS: '10'
        }
      });
      expect(window.fetch).not.toHaveBeenCalled();
      await vi.advanceTimersByTimeAsync(600);
      expect(window.fetch).toHaveBeenCalledTimes(1);
      expect(window.fetch.mock.calls[0][0]).toBe(
        'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked'
      );
      expect(window.fetch.mock.calls[0][1]).toMatchObject({ method: 'GET', cache: 'no-store' });
      expect(info).toHaveBeenCalledWith(
        '[egress-layer-probe]',
        JSON.stringify({
          policy: 'REQ-NET-001',
          destination: EXPECTED_DESTINATION,
          outcome: 'rejected',
          error: 'net::ERR_BLOCKED_BY_CLIENT'
        })
      );
      expect(JSON.stringify(info.mock.calls)).not.toContain('chirality-packaged-security-egress-blocked');
    } finally {
      info.mockRestore();
      vi.useRealTimers();
    }
  });

  it('reports a response — the egress layer letting the request through — distinctly', async () => {
    vi.useFakeTimers();
    const info = vi.spyOn(console, 'info').mockImplementation(() => undefined);
    try {
      const window = egressWindow(true);
      window.fetch.mockResolvedValue({ status: 200 });
      runEgressLayerProbe(window, {
        env: {
          CHIRALITY_RENDERER_SECURITY_PROBE: '1',
          CHIRALITY_RENDERER_SECURITY_PROBE_DELAY_MS: '10'
        }
      });
      expect(window.webContents.once).toHaveBeenCalledWith('did-finish-load', expect.any(Function));
      window.webContents.once.mock.calls[0][1]();
      await vi.advanceTimersByTimeAsync(600);
      expect(info).toHaveBeenCalledWith(
        '[egress-layer-probe]',
        JSON.stringify({
          policy: 'REQ-NET-001',
          destination: EXPECTED_DESTINATION,
          outcome: 'response',
          status: 200
        })
      );
    } finally {
      info.mockRestore();
      vi.useRealTimers();
    }
  });
});
