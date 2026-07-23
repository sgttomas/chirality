import { app, BrowserWindow, dialog, ipcMain } from 'electron';
import { existsSync } from 'node:fs';
import { stat } from 'node:fs/promises';
import { createServer, type IncomingMessage, type ServerResponse } from 'node:http';
import type { AddressInfo } from 'node:net';
import path from 'node:path';
import { RuntimeClient } from '@chirality/runtime-client';
import { registerApiKeyHandlers, unregisterApiKeyHandlers } from './api-key-ipc';
import { installBundledCliLauncher } from './cli-launcher';
import {
  applyDesktopProjectBinding,
  prepareDesktopHarnessEnvironment,
  resolveDesktopProjectBinding
} from './desktop-project-client';
import { startRuntimeHost, type RuntimeHost } from './runtime-host';
import {
  createDesktopDaemonLifecycle,
  registerRuntimeControlHandlers,
  unregisterRuntimeControlHandlers
} from './runtime-control-ipc';

type RendererServer = {
  close: () => Promise<void>;
  url: string;
};

type RendererProbeResult = {
  url: string;
  ok: boolean;
  status: number | null;
  type: string | null;
  error: string | null;
};

const SELECT_DIRECTORY_CHANNEL = 'chirality:select-directory';
const RUNTIME_NETWORK_POLICY_ID = 'REQ-NET-001';
const DEFAULT_RENDERER_PROBE_DELAY_MS = 1500;
const DEFAULT_RENDERER_PROBE_TIMEOUT_MS = 8000;

const ALLOWED_ANTHROPIC_API_HOSTNAMES = new Set<string>(['api.anthropic.com']);
const ALLOWED_LOOPBACK_HOSTNAMES = new Set<string>(['localhost', '127.0.0.1', '[::1]']);
const RENDERER_EGRESS_FILTER_URLS = ['http://*/*', 'https://*/*', 'ws://*/*', 'wss://*/*'];

let rendererServer: RendererServer | undefined;
let runtimeHost: RuntimeHost | undefined;
let shutdownStarted = false;
const runtimeDaemonMode = process.argv.includes('--runtime-daemon');

type RendererEgressPolicyDecision =
  | { allowed: true }
  | { allowed: false; category: 'INVALID_URL' | 'NETWORK_POLICY_VIOLATION'; reason: string };

type RendererRequestDestination = {
  hostname: string;
  port: string | null;
  protocol: string;
};

function isAllowedLoopbackHostname(hostname: string): boolean {
  return ALLOWED_LOOPBACK_HOSTNAMES.has(hostname.toLowerCase());
}

function summarizeRendererRequestDestination(rawUrl: string): RendererRequestDestination | null {
  try {
    const parsed = new URL(rawUrl);
    return {
      hostname: parsed.hostname,
      port: parsed.port || null,
      protocol: parsed.protocol
    };
  } catch {
    return null;
  }
}

function parsePositiveInteger(raw: string | undefined, fallback: number): number {
  const parsed = Number.parseInt(raw ?? '', 10);
  if (!Number.isSafeInteger(parsed) || parsed <= 0) {
    return fallback;
  }
  return parsed;
}

function readRendererProbeUrls(): string[] {
  const raw = process.env.CHIRALITY_NETWORK_POLICY_PROBE_URLS?.trim();
  if (!raw) {
    return [];
  }

  return raw
    .split(',')
    .map((value) => value.trim())
    .filter((value) => value.length > 0);
}

function evaluateRendererEgressPolicy(rawUrl: string): RendererEgressPolicyDecision {
  let parsed: URL;
  try {
    parsed = new URL(rawUrl);
  } catch {
    return {
      allowed: false,
      category: 'INVALID_URL',
      reason: 'url_parse_failed'
    };
  }

  const hostname = parsed.hostname.toLowerCase();
  if (ALLOWED_ANTHROPIC_API_HOSTNAMES.has(hostname)) {
    if (parsed.protocol !== 'https:') {
      return {
        allowed: false,
        category: 'NETWORK_POLICY_VIOLATION',
        reason: `anthropic_protocol_not_allowlisted:${parsed.protocol}`
      };
    }

    if (parsed.port !== '' && parsed.port !== '443') {
      return {
        allowed: false,
        category: 'NETWORK_POLICY_VIOLATION',
        reason: `anthropic_port_not_allowlisted:${parsed.port}`
      };
    }

    return { allowed: true };
  }

  if (isAllowedLoopbackHostname(hostname)) {
    return { allowed: true };
  }

  return {
    allowed: false,
    category: 'NETWORK_POLICY_VIOLATION',
    reason: `host_not_allowlisted:${hostname}`
  };
}

function registerRendererEgressPolicy(window: BrowserWindow): void {
  window.webContents.session.webRequest.onBeforeRequest(
    { urls: RENDERER_EGRESS_FILTER_URLS },
    (details, callback) => {
      const decision = evaluateRendererEgressPolicy(details.url);
      if (decision.allowed) {
        callback({ cancel: false });
        return;
      }

      console.warn('Blocked renderer outbound request by network policy', {
        category: decision.category,
        policy: RUNTIME_NETWORK_POLICY_ID,
        reason: decision.reason,
        destination: summarizeRendererRequestDestination(details.url),
        method: details.method,
        resourceType: details.resourceType,
        webContentsId: details.webContentsId
      });

      callback({ cancel: true });
    }
  );
}

async function runRendererNetworkProbe(window: BrowserWindow): Promise<void> {
  const urls = readRendererProbeUrls();
  if (urls.length === 0) {
    return;
  }

  const delayMs = parsePositiveInteger(
    process.env.CHIRALITY_NETWORK_POLICY_PROBE_DELAY_MS,
    DEFAULT_RENDERER_PROBE_DELAY_MS
  );
  const timeoutMs = parsePositiveInteger(
    process.env.CHIRALITY_NETWORK_POLICY_PROBE_TIMEOUT_MS,
    DEFAULT_RENDERER_PROBE_TIMEOUT_MS
  );

  const runProbe = async (): Promise<void> => {
    const script = `
(() => {
  const urls = ${JSON.stringify(urls)};
  const timeoutMs = ${timeoutMs};
  const run = async () => {
    const results = [];
    for (const url of urls) {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), timeoutMs);
      try {
        const response = await fetch(url, {
          method: 'GET',
          mode: 'no-cors',
          cache: 'no-store',
          signal: controller.signal
        });
        results.push({
          url,
          ok: true,
          status: typeof response?.status === 'number' ? response.status : null,
          type: typeof response?.type === 'string' ? response.type : null,
          error: null
        });
      } catch (error) {
        const errorMessage = error instanceof Error ? error.message : String(error);
        results.push({
          url,
          ok: false,
          status: null,
          type: null,
          error: errorMessage
        });
      } finally {
        clearTimeout(timer);
      }
    }
    return results;
  };
  return run();
})();
`;

    try {
      const results = (await window.webContents.executeJavaScript(script, true)) as RendererProbeResult[];
      console.info(
        '[network-policy-probe]',
        JSON.stringify({
          policy: RUNTIME_NETWORK_POLICY_ID,
          results
        })
      );
    } catch (error) {
      console.error(
        '[network-policy-probe]',
        JSON.stringify({
          policy: RUNTIME_NETWORK_POLICY_ID,
          error: error instanceof Error ? error.message : String(error)
        })
      );
    }
  };

  const scheduleProbe = (): void => {
    setTimeout(() => {
      void runProbe();
    }, delayMs);
  };

  if (window.webContents.isLoadingMainFrame()) {
    window.webContents.once('did-finish-load', scheduleProbe);
  } else {
    scheduleProbe();
  }
}

function resolveInstructionRootForProcess(): string {
  const envOverride = process.env.CHIRALITY_INSTRUCTION_ROOT?.trim();
  if (envOverride) {
    return path.resolve(envOverride);
  }

  if (app.isPackaged) {
    return path.resolve(process.resourcesPath);
  }

  const candidates: string[] = [];
  for (const start of [process.cwd(), __dirname]) {
    let candidate = path.resolve(start);
    for (;;) {
      candidates.push(candidate);
      const parent = path.dirname(candidate);
      if (parent === candidate) break;
      candidate = parent;
    }
  }
  const resolved = candidates.find(
    (candidate) =>
      existsSync(path.join(candidate, 'agents')) &&
      existsSync(path.join(candidate, 'AGENTS.md')) &&
      existsSync(path.join(candidate, 'docs', 'DIRECTIVE.md'))
  );
  if (resolved === undefined) {
    throw new Error('Unable to resolve the Chirality instruction root');
  }
  return resolved;
}

async function registerDirectorySelectionHandler(): Promise<void> {
  ipcMain.removeHandler(SELECT_DIRECTORY_CHANNEL);
  ipcMain.handle(SELECT_DIRECTORY_CHANNEL, async () => {
    const dialogResult = await dialog.showOpenDialog({
      title: 'Select Working Root',
      properties: ['openDirectory']
    });

    if (dialogResult.canceled || dialogResult.filePaths.length === 0) {
      return { cancelled: true };
    }

    const selectedPath = path.resolve(dialogResult.filePaths[0]);

    try {
      const selectedStat = await stat(selectedPath);
      if (!selectedStat.isDirectory()) {
        return {
          cancelled: true,
          error: 'Selected path is not a directory'
        };
      }
    } catch {
      return {
        cancelled: true,
        error: 'Selected path is not accessible'
      };
    }

    return {
      cancelled: false,
      path: selectedPath
    };
  });
}

async function startPackagedRendererServer(): Promise<RendererServer> {
  const rendererRoot = path.join(process.resourcesPath, 'app.asar');
  const nextModule = await import('next');
  const nextFactory = (nextModule.default ?? nextModule) as unknown as (config: {
    dev: boolean;
    dir: string;
  }) => {
    getRequestHandler: () => (
      req: IncomingMessage,
      res: ServerResponse<IncomingMessage>
    ) => Promise<void> | void;
    prepare: () => Promise<void>;
  };

  const nextApp = nextFactory({
    dev: false,
    dir: rendererRoot
  });

  await nextApp.prepare();
  const handle = nextApp.getRequestHandler();
  const server = createServer((req, res) => {
    handle(req, res);
  });

  await new Promise<void>((resolve, reject) => {
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      server.off('error', reject);
      resolve();
    });
  });

  const address = server.address() as AddressInfo | null;
  if (!address || typeof address === 'string') {
    throw new Error('Renderer server failed to bind a TCP port');
  }

  return {
    close: async () => {
      await new Promise<void>((resolve, reject) => {
        server.close((error) => {
          if (error) {
            reject(error);
            return;
          }
          resolve();
        });
      });
    },
    url: `http://127.0.0.1:${address.port}`
  };
}

function createMainWindow(rendererUrl: string): BrowserWindow {
  const window = new BrowserWindow({
    width: 1280,
    height: 840,
    show: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true
    }
  });

  window.once('ready-to-show', () => {
    window.show();
  });

  registerRendererEgressPolicy(window);
  window.loadURL(rendererUrl);
  void runRendererNetworkProbe(window);

  return window;
}

function runtimeControlPaths(): {
  runtimeDirectory: string;
  socketPath: string;
  operatorTokenFile: string;
} {
  const runtimeDirectory = path.join(app.getPath('userData'), 'runtime');
  return {
    runtimeDirectory,
    socketPath:
      process.env.CHIRALITY_RUNTIME_SOCKET_PATH?.trim() ||
      path.join(runtimeDirectory, 'control.sock'),
    operatorTokenFile:
      process.env.CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE?.trim() ||
      path.join(runtimeDirectory, 'auth', 'tokens', 'operator.token')
  };
}

async function configureDesktopHarnessClient(
  operatorClient: RuntimeClient,
  control: ReturnType<typeof runtimeControlPaths>
): Promise<void> {
  prepareDesktopHarnessEnvironment(process.env, control.socketPath);

  const binding = await resolveDesktopProjectBinding({
    operatorClient,
    runtimeDirectory: control.runtimeDirectory,
    socketPath: control.socketPath
  });
  applyDesktopProjectBinding(process.env, binding);
}

async function initializeGui(): Promise<void> {
  const control = runtimeControlPaths();
  const runtimeClient = new RuntimeClient({
    socketPath: control.socketPath,
    tokenFile: control.operatorTokenFile
  });
  registerApiKeyHandlers(runtimeClient);
  await registerDirectorySelectionHandler();
  process.env.CHIRALITY_INSTRUCTION_ROOT = resolveInstructionRootForProcess();

  if (app.isPackaged) {
    await installBundledCliLauncher().catch((error) => {
      console.error('Failed to install bundled Chirality CLI launcher', error);
    });
  }

  await configureDesktopHarnessClient(runtimeClient, control).catch((error) => {
    console.warn(
      'Desktop harness routes remain disabled until app-dev is registered without drift',
      error instanceof Error ? error.message : 'project binding unavailable'
    );
  });

  const rendererUrl = app.isPackaged
    ? (rendererServer = await startPackagedRendererServer()).url
    : process.env.ELECTRON_RENDERER_URL ?? 'http://localhost:3000';

  registerRuntimeControlHandlers({
    client: runtimeClient,
    lifecycle: createDesktopDaemonLifecycle(),
    desktopExecutable: app.getPath('exe'),
    packaged: app.isPackaged,
    rendererOrigin: new URL(rendererUrl).origin,
    onDaemonAvailable: async () => {
      await configureDesktopHarnessClient(runtimeClient, control);
    }
  });

  createMainWindow(rendererUrl);

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createMainWindow(rendererUrl);
    }
  });
}

async function initializeDaemon(): Promise<void> {
  process.env.CHIRALITY_INSTRUCTION_ROOT = resolveInstructionRootForProcess();
  runtimeHost = await startRuntimeHost();
  console.info('[chirality-runtime-daemon]', {
    socketPath: runtimeHost.socketPath,
    runtimeDirectory: runtimeHost.runtimeDirectory
  });
}

async function shutdown(exitCode = 0): Promise<void> {
  if (shutdownStarted) {
    return;
  }
  shutdownStarted = true;
  ipcMain.removeHandler(SELECT_DIRECTORY_CHANNEL);
  unregisterApiKeyHandlers();
  unregisterRuntimeControlHandlers();

  if (runtimeHost) {
    try {
      await runtimeHost.stop();
    } catch (error) {
      exitCode = 1;
      console.error('Failed closing shared runtime daemon', error);
    }
    runtimeHost = undefined;
  }

  if (rendererServer) {
    try {
      await rendererServer.close();
    } catch (error) {
      exitCode = 1;
      console.error('Failed closing packaged renderer server', error);
    }
    rendererServer = undefined;
  }
  app.exit(exitCode);
}

app
  .whenReady()
  .then(async () => {
    if (runtimeDaemonMode) {
      await initializeDaemon();
      return;
    }
    await initializeGui();
  })
  .catch((error) => {
    console.error(
      runtimeDaemonMode
        ? 'Failed to initialize shared runtime daemon'
        : 'Failed to initialize renderer client',
      error
    );
    void shutdown(1);
  });

app.on('window-all-closed', () => {
  if (!runtimeDaemonMode && process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', (event) => {
  if (!shutdownStarted && (runtimeHost !== undefined || rendererServer !== undefined)) {
    event.preventDefault();
    void shutdown();
  }
});

for (const signal of ['SIGINT', 'SIGTERM'] as const) {
  process.once(signal, () => {
    void shutdown(signal === 'SIGINT' ? 130 : 0);
  });
}
