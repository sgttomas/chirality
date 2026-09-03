/**
 * Renderer window hardening policy (DEL-09-06-V3-01, G-CSP).
 *
 * Pure policy functions (testable without Electron) plus one installer applied
 * to every BrowserWindow the main process creates:
 *
 * - web preferences are asserted at creation: `contextIsolation: true`,
 *   `nodeIntegration: false`, `sandbox: true`; anything else fails closed;
 * - `setWindowOpenHandler` denies every request (the app never opens windows
 *   from the renderer) and logs a redacted line;
 * - `will-navigate` and `will-redirect` allow only the app's own renderer
 *   origin (the packaged loopback renderer server or the dev server) and deny
 *   everything else — `javascript:`, `file:`, `data:`, `about:`, foreign hosts,
 *   a different port or scheme;
 * - a Content-Security-Policy is attached to responses from the renderer
 *   origin through `webRequest.onHeadersReceived` when the response carries
 *   none (the packaged renderer server sets it directly; the dev server does
 *   not), so both modes render under one policy.
 *
 * The CSP is defence in depth beside the REQ-NET-001 egress allowlist in
 * `main.ts`, not a replacement for it: the egress layer is what the packaged
 * proof observes on the wire.
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

/** The renderer never opens windows: every request is denied. */
export function evaluateWindowOpen(_details: { url: string }): { action: 'deny' } {
  return { action: 'deny' };
}

export type RendererCspMode = 'packaged' | 'development';

/**
 * Renderer Content-Security-Policy.
 *
 * What the renderer actually needs, verified against the `npm run build` output
 * and the dev server (recorded in the DEL-09-06 evidence):
 * - `script-src 'unsafe-inline'`: Next.js App Router delivers the React Server
 *   Components flight payload as inline `<script>self.__next_f.push(…)</script>`
 *   tags (8 per prerendered page in the production build). A nonce pipeline
 *   would need a Next middleware, which is outside this policy's scope, so the
 *   inline allowance stays; external scripts remain restricted to `'self'`.
 * - `'unsafe-eval'` only in development: Next's dev runtime and React Refresh
 *   evaluate source; the packaged renderer never gets it.
 * - `style-src 'unsafe-inline'`: two components set React `style` props (inline
 *   style attributes) and Next injects style elements in development.
 * - `connect-src`: `'self'` plus the REQ-NET-001 egress allowlist. The Anthropic
 *   host is listed with a port wildcard on purpose: an exactly-equal CSP would
 *   make the egress layer unreachable from the page and the packaged proof could
 *   no longer observe it independently; the egress policy still enforces
 *   https:443 exactly, and the proof drives a non-443 port to watch it deny.
 *   The dev server's HMR WebSocket needs the `ws:`/`wss:` form of its own origin.
 * - everything else is closed: no frames, no plugins, no foreign forms or bases,
 *   no embedding.
 */
export function buildRendererContentSecurityPolicy(options: {
  mode: RendererCspMode;
  rendererOrigin?: string;
}): string {
  const development = options.mode === 'development';
  const connectSources = ["'self'", 'https://api.anthropic.com:*'];
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
 * Add the policy to a response from the renderer origin that carries none.
 * Pure: returns the headers to install (the same object when untouched).
 */
export function applyContentSecurityPolicyHeader(
  details: { url: string; responseHeaders?: ResponseHeaders },
  rendererOrigin: string,
  contentSecurityPolicy: string
): ResponseHeaders {
  const headers = details.responseHeaders ?? {};
  let origin: string;
  try {
    origin = new URL(details.url).origin;
  } catch {
    return headers;
  }
  if (origin !== rendererOrigin || hasContentSecurityPolicy(headers)) {
    return headers;
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
  log?: RendererWindowLog;
};

const HEADER_FILTER_URLS = ['http://*/*', 'https://*/*'];

/** Install window-open denial, navigation containment, and the CSP on one window. */
export function installRendererWindowPolicy(
  window: RendererWindowLike,
  options: RendererWindowPolicyOptions
): void {
  const { rendererOrigin, contentSecurityPolicy, log } = options;
  const { webContents } = window;

  webContents.setWindowOpenHandler((details) => {
    log?.('warn', 'renderer.window_open.denied', {
      destination: summarizeDestination(details.url)
    });
    return evaluateWindowOpen(details);
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
      callback({
        responseHeaders: applyContentSecurityPolicyHeader(
          details,
          rendererOrigin,
          contentSecurityPolicy
        )
      });
    }
  );
}

/**
 * Optional in-page probe for the packaged security proof
 * (`CHIRALITY_RENDERER_SECURITY_PROBE=1`): reports the document's CSP header
 * (same-origin fetch of the page), a denied `window.open`, the
 * `securitypolicyviolation` events raised by a deliberately blocked fetch, and
 * finally attempts a foreign navigation so the main process logs its denial.
 * Nothing runs unless the environment asks for it.
 */
export function runRendererSecurityProbe(
  window: {
    webContents: {
      isLoadingMainFrame(): boolean;
      once(event: 'did-finish-load', listener: () => void): unknown;
      executeJavaScript(code: string, userGesture?: boolean): Promise<unknown>;
    };
  },
  options: { env: Record<string, string | undefined>; log?: RendererWindowLog }
): void {
  if (options.env.CHIRALITY_RENDERER_SECURITY_PROBE !== '1') {
    return;
  }
  const delayMs = Number.parseInt(options.env.CHIRALITY_RENDERER_SECURITY_PROBE_DELAY_MS ?? '', 10);
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
      const opened = window.open('https://example.com/chirality-renderer-security-window-open', '_blank');
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
  const runProbe = async (): Promise<void> => {
    try {
      const result = await window.webContents.executeJavaScript(script, true);
      console.info('[renderer-security-probe]', JSON.stringify(result));
    } catch (error) {
      console.error(
        '[renderer-security-probe]',
        JSON.stringify({ policy: 'G-CSP', error: error instanceof Error ? error.message : String(error) })
      );
    }
  };
  const schedule = (): void => {
    setTimeout(() => {
      void runProbe();
    }, Number.isSafeInteger(delayMs) && delayMs > 0 ? delayMs : 1500);
  };
  if (window.webContents.isLoadingMainFrame()) {
    window.webContents.once('did-finish-load', schedule);
  } else {
    schedule();
  }
}
