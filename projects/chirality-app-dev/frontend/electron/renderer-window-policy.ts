/**
 * Renderer window hardening policy (DEL-09-06-V3-01, G-CSP).
 *
 * Pure policy functions (testable without Electron) plus one installer applied
 * to every BrowserWindow the main process creates:
 *
 * - web preferences are asserted at creation: `contextIsolation: true`,
 *   `nodeIntegration: false`, `sandbox: true`; anything else fails closed;
 * - `setWindowOpenHandler` never lets the renderer create a child
 *   BrowserWindow. The renderer *does* ask for windows — every link in rendered
 *   chat markdown (`src/components/shell/chat-markdown.tsx`) and the
 *   navigator's "open legacy interface" link (`src/components/woven-dialogue/
 *   navigator.tsx`) use `target="_blank"` — so an `http:`/`https:` target is
 *   handed to the operating system's default browser (`shell.openExternal`,
 *   injected by `main.ts`) instead of a child window that would inherit this
 *   app's preload and IPC bridge; every other scheme is dropped. Before this
 *   policy such a click created a child BrowserWindow at the link's URL; now it
 *   opens the system browser (coordinator decision 2026-09-03, recorded in the
 *   run record). This is not app egress: nothing leaves this process.
 * - `will-navigate` and `will-redirect` allow only the app's own renderer
 *   origin over http(s) and deny everything else — `javascript:`, `file:`,
 *   `data:`, `about:`, `blob:`, foreign hosts, a different port or scheme;
 * - a Content-Security-Policy is attached to responses from the renderer
 *   origin through `webRequest.onHeadersReceived` when the response carries
 *   none (the packaged renderer server sets it directly; the dev server does
 *   not), so both modes render under one policy.
 *
 * The CSP is defence in depth beside the REQ-NET-001 egress allowlist in
 * `main.ts`, not a replacement for it: the egress layer is what the packaged
 * proof observes on the wire, through the main-process probe below.
 */

export type RendererWindowLog = (
  level: 'info' | 'warn' | 'error',
  event: string,
  detail?: unknown
) => void;

export const REQUIRED_RENDERER_WEB_PREFERENCES = Object.freeze({
  contextIsolation: true,
  nodeIntegration: false,
  sandbox: true
} as const);

const FORBIDDEN_RENDERER_WEB_PREFERENCES = [
  'nodeIntegrationInWorker',
  'nodeIntegrationInSubFrames',
  'webviewTag',
  'allowRunningInsecureContent',
  'enableRemoteModule',
  'experimentalFeatures'
] as const;

export type RendererWebPreferencesInput = Record<string, unknown>;

/** Throws when the preferences would weaken the renderer boundary. */
export function assertRendererWebPreferences(preferences: RendererWebPreferencesInput): void {
  const problems: string[] = [];
  if (preferences.contextIsolation !== true) problems.push('contextIsolation must be true');
  if (preferences.nodeIntegration !== false) problems.push('nodeIntegration must be false');
  if (preferences.sandbox !== true) problems.push('sandbox must be true');
  if (preferences.webSecurity === false) problems.push('webSecurity must not be disabled');
  for (const name of FORBIDDEN_RENDERER_WEB_PREFERENCES) {
    if (preferences[name] === true) problems.push(`${name} must not be enabled`);
  }
  if (problems.length > 0) {
    throw new Error(
      `Renderer window web preferences violate the hardening policy: ${problems.join('; ')}`
    );
  }
}

export type RendererWebPreferences = {
  preload: string;
  contextIsolation: true;
  nodeIntegration: false;
  sandbox: true;
};

/** The only web preferences a renderer window may be created with. */
export function rendererWebPreferences(input: { preload: string }): RendererWebPreferences {
  const preferences: RendererWebPreferences = {
    preload: input.preload,
    ...REQUIRED_RENDERER_WEB_PREFERENCES
  };
  assertRendererWebPreferences(preferences);
  return preferences;
}

export type RendererNavigationDecision =
  | { allowed: true }
  | { allowed: false; reason: 'INVALID_URL' | 'SCHEME_NOT_HTTP' | 'ORIGIN_NOT_RENDERER' };

/**
 * Renderer-initiated navigations may target only the renderer origin itself,
 * over http(s). The scheme check comes first because a `blob:` URL reports its
 * creator's origin — equal to the renderer's — while `javascript:`, `file:`,
 * `data:` and `about:` report the opaque origin `null`; none of them is a page
 * of the app. Everything at a foreign origin, port, or scheme is denied.
 */
export function evaluateRendererNavigation(
  rawUrl: string,
  rendererOrigin: string
): RendererNavigationDecision {
  let parsed: URL;
  try {
    parsed = new URL(rawUrl);
  } catch {
    return { allowed: false, reason: 'INVALID_URL' };
  }
  if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
    return { allowed: false, reason: 'SCHEME_NOT_HTTP' };
  }
  if (!rendererOrigin || parsed.origin === 'null' || parsed.origin !== rendererOrigin) {
    return { allowed: false, reason: 'ORIGIN_NOT_RENDERER' };
  }
  return { allowed: true };
}

export type WindowOpenDecision =
  | { action: 'deny'; external: true }
  | { action: 'deny'; external: false; reason: 'INVALID_URL' | 'SCHEME_NOT_HTTP' };

/**
 * A child BrowserWindow is never created (`action: 'deny'` for every request).
 * An `http:`/`https:` target is instead opened in the system browser by the
 * installer; a malformed URL or any other scheme (`javascript:`, `file:`,
 * `data:`, `blob:`, `about:`, custom) is dropped.
 */
export function evaluateWindowOpen(details: { url: string }): WindowOpenDecision {
  let parsed: URL;
  try {
    parsed = new URL(details.url);
  } catch {
    return { action: 'deny', external: false, reason: 'INVALID_URL' };
  }
  if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
    return { action: 'deny', external: false, reason: 'SCHEME_NOT_HTTP' };
  }
  return { action: 'deny', external: true };
}

export type RendererCspMode = 'packaged' | 'development';

/**
 * Renderer Content-Security-Policy.
 *
 * What the renderer actually needs, verified against the `npm run build` output
 * and the dev server (recorded in the DEL-09-06 evidence):
 * - `script-src 'unsafe-inline'`: Next.js App Router delivers the React Server
 *   Components flight payload as inline `<script>self.__next_f.push(…)</script>`
 *   tags with no nonce. A nonce pipeline needs a Next middleware or a request
 *   header set before the packaged handler, plus a decision on prerendering —
 *   outside this policy's scope — so the inline allowance stays; external
 *   scripts remain restricted to `'self'`. With it, this CSP's value against an
 *   injected inline script is limited to remote-script, eval, frame, object,
 *   base, form, and connect containment.
 * - `'unsafe-eval'` only in development: Next's dev runtime and React Refresh
 *   evaluate source; the packaged renderer never gets it.
 * - `style-src 'unsafe-inline'`: two components set React `style` props (inline
 *   style attributes) and Next injects style elements in development.
 * - `connect-src 'self'` in packaged mode: the renderer talks only to its own
 *   Next server; the Anthropic and oMLX calls are made server-side by the Next
 *   server process and the daemon, never by the page. This is stricter than the
 *   REQ-NET-001 egress allowlist, which stays as the wire-level backstop. The
 *   dev server's HMR WebSocket needs the `ws:`/`wss:` form of its own origin.
 * - everything else is closed: no frames, no plugins, no foreign forms or bases,
 *   no embedding.
 */
export function buildRendererContentSecurityPolicy(options: {
  mode: RendererCspMode;
  rendererOrigin?: string;
}): string {
  const development = options.mode === 'development';
  const connectSources = ["'self'"];
  if (development && options.rendererOrigin) {
    try {
      const origin = new URL(options.rendererOrigin);
      connectSources.push(`ws://${origin.host}`, `wss://${origin.host}`);
    } catch {
      // An unparseable origin adds nothing; 'self' still covers same-origin.
    }
  }
  const directives = [
    "default-src 'self'",
    `script-src 'self' 'unsafe-inline'${development ? " 'unsafe-eval'" : ''}`,
    "style-src 'self' 'unsafe-inline'",
    "img-src 'self' data:",
    "font-src 'self' data:",
    `connect-src ${connectSources.join(' ')}`,
    "worker-src 'self'",
    "manifest-src 'self'",
    "media-src 'self'",
    "frame-src 'none'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'"
  ];
  return directives.join('; ');
}

export const CONTENT_SECURITY_POLICY_HEADER = 'Content-Security-Policy';

type ResponseHeaders = Record<string, string[]>;

function hasContentSecurityPolicy(headers: ResponseHeaders): boolean {
  return Object.keys(headers).some(
    (name) => name.toLowerCase() === CONTENT_SECURITY_POLICY_HEADER.toLowerCase()
  );
}

/**
 * Headers to install on a response from the renderer origin that carries no
 * policy, or `null` when the response must be left exactly as received (foreign
 * origin, unparseable URL, or a policy already present). Pure.
 */
export function applyContentSecurityPolicyHeader(
  details: { url: string; responseHeaders?: ResponseHeaders },
  rendererOrigin: string,
  contentSecurityPolicy: string
): ResponseHeaders | null {
  let origin: string;
  try {
    origin = new URL(details.url).origin;
  } catch {
    return null;
  }
  const headers = details.responseHeaders ?? {};
  if (origin !== rendererOrigin || hasContentSecurityPolicy(headers)) {
    return null;
  }
  return { ...headers, [CONTENT_SECURITY_POLICY_HEADER]: [contentSecurityPolicy] };
}

/** Non-secret destination summary for diagnostics: no path, query, or userinfo. */
export function summarizeDestination(rawUrl: string): { protocol: string; hostname: string } | null {
  try {
    const parsed = new URL(rawUrl);
    return { protocol: parsed.protocol, hostname: parsed.hostname };
  } catch {
    return null;
  }
}

export type RendererWindowLike = {
  webContents: {
    setWindowOpenHandler(handler: (details: { url: string }) => { action: 'deny' }): void;
    on(
      event: 'will-navigate' | 'will-redirect',
      listener: (event: { preventDefault(): void }, url: string) => void
    ): unknown;
    session: {
      webRequest: {
        onHeadersReceived(
          filter: { urls: string[] },
          listener: (
            details: { url: string; responseHeaders?: ResponseHeaders },
            callback: (response: { responseHeaders?: ResponseHeaders }) => void
          ) => void
        ): void;
      };
    };
  };
};

export type RendererWindowPolicyOptions = {
  rendererOrigin: string;
  contentSecurityPolicy: string;
  /** Opens an `http(s)` URL in the operating system's default browser. */
  openExternal: (url: string) => Promise<void>;
  log?: RendererWindowLog;
};

const HEADER_FILTER_URLS = ['http://*/*', 'https://*/*'];

/** Install window-open handling, navigation containment, and the CSP on one window. */
export function installRendererWindowPolicy(
  window: RendererWindowLike,
  options: RendererWindowPolicyOptions
): void {
  const { rendererOrigin, contentSecurityPolicy, openExternal, log } = options;
  const { webContents } = window;

  webContents.setWindowOpenHandler((details) => {
    const decision = evaluateWindowOpen(details);
    const destination = summarizeDestination(details.url);
    if (decision.external) {
      log?.('info', 'renderer.window_open.external_opened', { destination });
      // Deferred so a synchronous throw from the injected opener is caught the
      // same way as a rejection and can never escape the handler.
      Promise.resolve()
        .then(() => openExternal(details.url))
        .catch((error: unknown) => {
          log?.('warn', 'renderer.window_open.external_failed', {
            destination,
            error: error instanceof Error ? error.message : String(error)
          });
        });
    } else {
      log?.('warn', 'renderer.window_open.denied', { reason: decision.reason, destination });
    }
    return { action: 'deny' };
  });

  for (const eventName of ['will-navigate', 'will-redirect'] as const) {
    webContents.on(eventName, (event, url) => {
      const decision = evaluateRendererNavigation(url, rendererOrigin);
      if (decision.allowed) {
        return;
      }
      event.preventDefault();
      log?.('warn', 'renderer.navigation.denied', {
        event: eventName,
        reason: decision.reason,
        destination: summarizeDestination(url)
      });
    });
  }

  webContents.session.webRequest.onHeadersReceived(
    { urls: HEADER_FILTER_URLS },
    (details, callback) => {
      const responseHeaders = applyContentSecurityPolicyHeader(
        details,
        rendererOrigin,
        contentSecurityPolicy
      );
      // No override at all when untouched: echoing an empty header set would
      // tell Chromium the server answered with no headers.
      callback(responseHeaders === null ? {} : { responseHeaders });
    }
  );
}

type ProbeEnvironment = Record<string, string | undefined>;

function probeDelayMs(env: ProbeEnvironment, fallback: number): number {
  const parsed = Number.parseInt(env.CHIRALITY_RENDERER_SECURITY_PROBE_DELAY_MS ?? '', 10);
  return Number.isSafeInteger(parsed) && parsed > 0 ? parsed : fallback;
}

function afterLoad(
  webContents: { isLoadingMainFrame(): boolean; once(event: 'did-finish-load', listener: () => void): unknown },
  delayMs: number,
  run: () => void
): void {
  const schedule = (): void => {
    setTimeout(run, delayMs);
  };
  if (webContents.isLoadingMainFrame()) {
    webContents.once('did-finish-load', schedule);
  } else {
    schedule();
  }
}

/**
 * Optional in-page probe for the packaged security proof
 * (`CHIRALITY_RENDERER_SECURITY_PROBE=1`): reports the document's CSP header
 * (same-origin fetch of the page), a denied `window.open` — deliberately of an
 * `about:blank` target so the proof never opens the host's browser; the
 * `http(s)` hand-off is unit-tested — the `securitypolicyviolation` events
 * raised by a deliberately blocked fetch, and finally attempts a foreign
 * navigation so the main process logs its denial. Nothing runs unless the
 * environment asks for it. Results are written to the console under the
 * `[renderer-security-probe]` marker the proof reads.
 */
export function runRendererSecurityProbe(
  window: {
    webContents: {
      isLoadingMainFrame(): boolean;
      once(event: 'did-finish-load', listener: () => void): unknown;
      executeJavaScript(code: string, userGesture?: boolean): Promise<unknown>;
    };
  },
  options: { env: ProbeEnvironment }
): void {
  if (options.env.CHIRALITY_RENDERER_SECURITY_PROBE !== '1') {
    return;
  }
  const script = `
(() => {
  const violations = [];
  document.addEventListener('securitypolicyviolation', (event) => {
    violations.push({
      blockedURI: event.blockedURI,
      effectiveDirective: event.effectiveDirective,
      disposition: event.disposition
    });
  });
  const run = async () => {
    let cspHeader = null;
    try {
      const response = await fetch(location.href, { cache: 'no-store' });
      cspHeader = response.headers.get('content-security-policy');
    } catch (error) {
      cspHeader = 'fetch-failed:' + (error instanceof Error ? error.message : String(error));
    }
    let windowOpen;
    try {
      const opened = window.open('about:blank#chirality-renderer-security-window-open', '_blank');
      windowOpen = { returned: opened === null ? 'null' : typeof opened };
    } catch (error) {
      windowOpen = { error: error instanceof Error ? error.message : String(error) };
    }
    try {
      await fetch('https://example.com/chirality-renderer-security-csp-blocked', {
        mode: 'no-cors',
        cache: 'no-store'
      });
    } catch {
      // A rejected fetch is the expected outcome; the violation event is the evidence.
    }
    await new Promise((resolve) => setTimeout(resolve, 250));
    const navigationTarget = 'https://example.com/chirality-renderer-security-navigation';
    setTimeout(() => {
      try {
        location.assign(navigationTarget);
      } catch {
        // Denied navigation surfaces in the main-process log.
      }
    }, 0);
    return { policy: 'G-CSP', cspHeader, windowOpen, violations, navigationAttempted: navigationTarget };
  };
  return run();
})();
`;
  afterLoad(window.webContents, probeDelayMs(options.env, 1500), () => {
    void window.webContents
      .executeJavaScript(script, true)
      .then((result) => {
        console.info('[renderer-security-probe]', JSON.stringify(result));
      })
      .catch((error: unknown) => {
        console.error(
          '[renderer-security-probe]',
          JSON.stringify({ policy: 'G-CSP', error: error instanceof Error ? error.message : String(error) })
        );
      });
  });
}

/**
 * Optional main-process probe of the REQ-NET-001 egress layer for the packaged
 * security proof (same gate, plus `CHIRALITY_EGRESS_LAYER_PROBE_URL`). The page
 * cannot reach the egress layer for a foreign host any more — the CSP stops it
 * first — so the proof issues the request from the main process through the
 * window's session: `session.fetch` goes through `webRequest`, where
 * `onBeforeRequest` cancels it and logs the denial. A rejected fetch is the
 * expected outcome; a response would mean the egress layer let it through.
 */
export function runEgressLayerProbe(
  window: {
    webContents: {
      isLoadingMainFrame(): boolean;
      once(event: 'did-finish-load', listener: () => void): unknown;
      session: {
        fetch(
          input: string,
          init?: { method?: string; cache?: 'no-store'; signal?: AbortSignal }
        ): Promise<{ status: number }>;
      };
    };
  },
  options: { env: ProbeEnvironment }
): void {
  const url = options.env.CHIRALITY_EGRESS_LAYER_PROBE_URL?.trim();
  if (options.env.CHIRALITY_RENDERER_SECURITY_PROBE !== '1' || !url) {
    return;
  }
  const destination = summarizeDestination(url);
  afterLoad(window.webContents, probeDelayMs(options.env, 1500) + 500, () => {
    void window.webContents.session
      .fetch(url, { method: 'GET', cache: 'no-store', signal: AbortSignal.timeout(3000) })
      .then((response) => {
        console.info(
          '[egress-layer-probe]',
          JSON.stringify({ policy: 'REQ-NET-001', destination, outcome: 'response', status: response.status })
        );
      })
      .catch((error: unknown) => {
        console.info(
          '[egress-layer-probe]',
          JSON.stringify({
            policy: 'REQ-NET-001',
            destination,
            outcome: 'rejected',
            error: error instanceof Error ? error.message : String(error)
          })
        );
      });
  });
}
