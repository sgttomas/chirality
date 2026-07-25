import { app, BrowserWindow, dialog, ipcMain } from 'electron';
import { existsSync, mkdirSync } from 'node:fs';
import { stat } from 'node:fs/promises';
import { createServer, type IncomingMessage, type ServerResponse } from 'node:http';
import type { AddressInfo } from 'node:net';
import path from 'node:path';
import { RuntimeClient } from '@chirality/runtime-client';
import { registerApiKeyHandlers, unregisterApiKeyHandlers } from './api-key-ipc';
import { installBundledCliLauncher } from './cli-launcher';
import {
  createDesktopLogger,
  createNoopDesktopLogger,
  type DesktopLogger
} from './desktop-log';
import {
  resolveDaemonActivationPolicy,
  resolveUserDataOverride
} from './desktop-process-policy';
import {
  applyDesktopProjectBinding,
  prepareDesktopHarnessEnvironment,
  resolveDesktopProjectBinding
} from './desktop-project-client';
import { startRuntimeHost, type RuntimeHost } from './runtime-host';
import {
  createRuntimeBindingSupervisor,
  RUNTIME_CONNECTIVITY_CHANGED_CHANNEL,
  RUNTIME_CONNECTIVITY_QUERY_CHANNEL,
  type RuntimeBindingSupervisor,
  type RuntimeConnectivitySnapshot
} from './runtime-connectivity';
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
/**
 * Whether an exit has been authorized by a path we control (a signal from
 * launchd, or our own failure handling). Used to veto externally requested
 * quits in daemon mode; see the `before-quit` handler.
 */
let shutdownAuthorized = false;
let bindingSupervisor: RuntimeBindingSupervisor | undefined;
let desktopLogger: DesktopLogger = createNoopDesktopLogger();
const runtimeDaemonMode = process.argv.includes('--runtime-daemon');

/**
 * Honor `CHIRALITY_USER_DATA` for the app itself.
 *
 * The bundled `chirality` CLI and `@chirality/runtime-cli` already resolve their
 * runtime directory from `CHIRALITY_USER_DATA`, but the app hard-coded
 * Electron's default (`<appData>/chirality-frontend`). The two therefore
 * disagreed by default, and documented CLI commands pointed at a runtime
 * directory the app never used. Honoring the same variable here makes one
 * variable pin *both* sides to one runtime directory, and lets a verification
 * run drive a fully isolated app + daemon + LaunchAgent triple without touching
 * an operator's real userData.
 *
 * Must run before anything reads `app.getPath('userData')` and before `ready`,
 * because the value also selects the Chromium profile directory. Relative values
 * are rejected rather than resolved against an unpredictable cwd (launchd starts
 * jobs in `/`). `app.setPath` throws when the directory is absent, so create it
 * first. Applies to packaged and unpackaged runs alike — an env override that
 * silently only worked in one of them would be worse than none.
 */
function applyUserDataOverride(): void {
  const override = resolveUserDataOverride(process.env);
  if (override.kind === 'absent') {
    return;
  }
  if (override.kind === 'rejected') {
    console.warn(
      'Ignoring CHIRALITY_USER_DATA because it is not an absolute path',
      JSON.stringify({ requested: override.requested })
    );
    return;
  }
  try {
    mkdirSync(override.directory, { recursive: true, mode: 0o700 });
    app.setPath('userData', override.directory);
  } catch (error) {
    console.error(
      'Failed to apply CHIRALITY_USER_DATA override',
      error instanceof Error ? error.message : String(error)
    );
  }
}

/**
 * Shed the daemon's *app* identity while keeping it an Electron process.
 *
 * The daemon is the same bundle relaunched with `--runtime-daemon`, so without
 * this it comes up as an ordinary macOS application: Dock tile, menu bar, and —
 * decisively — a LaunchServices-visible, activatable instance of
 * `Chirality.app`. Opening the app from Finder/Dock then resolves against that
 * headless instance instead of starting the GUI, and the operator-visible effect
 * is "launching the GUI killed the daemon".
 *
 * `'prohibited'` is the strongest available posture ("doesn't appear in the Dock
 * and may not create windows or be activated") and is safe here precisely
 * because the daemon never creates a BrowserWindow. `'accessory'` remains
 * selectable through `CHIRALITY_DAEMON_ACTIVATION_POLICY` for comparison drills.
 *
 * safeStorage is unaffected: on macOS `safeStorage.isEncryptionAvailable()`
 * "returns true if Keychain is available" — it is gated on Keychain access, not
 * on NSApplication activation, a Dock tile, or a window. (Unlike Linux/Windows
 * it is not even gated on `ready`.) Keychain prompts are drawn by the system
 * security agent, not by this process's NSApplication.
 *
 * Called both at module scope and again after `ready`: the early call avoids a
 * visible Dock flash during launch, the later one is the belt-and-braces value
 * in case activation policy is reset while NSApplication finishes coming up.
 */
function applyDaemonActivationPolicy(): void {
  if (process.platform !== 'darwin') {
    return;
  }
  const policy = resolveDaemonActivationPolicy(process.env);
  try {
    app.setActivationPolicy(policy);
  } catch (error) {
    console.warn(
      'Failed to set the runtime daemon activation policy',
      JSON.stringify({ policy, error: error instanceof Error ? error.message : String(error) })
    );
  }
  if (policy === 'regular') {
    return;
  }
  try {
    app.dock?.hide();
  } catch {
    // A hidden or absent Dock tile is already the desired end state.
  }
}

applyUserDataOverride();
if (runtimeDaemonMode) {
  applyDaemonActivationPolicy();
}

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

/** Push a connectivity transition to every live renderer. */
function broadcastRuntimeConnectivity(snapshot: RuntimeConnectivitySnapshot): void {
  for (const window of BrowserWindow.getAllWindows()) {
    if (window.isDestroyed()) {
      continue;
    }
    window.webContents.send(RUNTIME_CONNECTIVITY_CHANGED_CHANNEL, snapshot);
  }
}

async function registerRuntimeConnectivityHandler(): Promise<void> {
  ipcMain.removeHandler(RUNTIME_CONNECTIVITY_QUERY_CHANNEL);
  ipcMain.handle(
    RUNTIME_CONNECTIVITY_QUERY_CHANNEL,
    async (): Promise<RuntimeConnectivitySnapshot | null> =>
      bindingSupervisor?.snapshot() ?? null
  );
}

async function initializeGui(): Promise<void> {
  const control = runtimeControlPaths();
  desktopLogger = createDesktopLogger({
    directory: path.join(app.getPath('userData'), 'logs')
  });
  const runtimeClient = new RuntimeClient({
    socketPath: control.socketPath,
    tokenFile: control.operatorTokenFile
  });
  registerApiKeyHandlers(runtimeClient);
  await registerDirectorySelectionHandler();
  await registerRuntimeConnectivityHandler();
  process.env.CHIRALITY_INSTRUCTION_ROOT = resolveInstructionRootForProcess();
  desktopLogger.info('desktop.gui.starting', {
    packaged: app.isPackaged,
    userData: app.getPath('userData'),
    socketPath: control.socketPath
  });

  if (app.isPackaged) {
    await installBundledCliLauncher().catch((error) => {
      desktopLogger.error('desktop.cli_launcher.install_failed', error);
    });
  }

  // Binding is a supervised main-process concern, not a one-shot startup step:
  // a daemon that is down at this instant, or that dies later, must not leave the
  // window permanently unable to reach the runtime. `start()` still awaits the
  // first attempt so a healthy daemon is fully bound before the window appears.
  bindingSupervisor = createRuntimeBindingSupervisor({
    bind: () => configureDesktopHarnessClient(runtimeClient, control),
    probe: async () => {
      try {
        await runtimeClient.daemonStatus();
        return true;
      } catch {
        return false;
      }
    },
    onStateChange: (snapshot) => {
      desktopLogger.info('runtime.connectivity.state', snapshot);
      broadcastRuntimeConnectivity(snapshot);
    },
    log: (level, event, detail) => desktopLogger.log(level, event, detail)
  });
  await bindingSupervisor.start();

  const rendererUrl = app.isPackaged
    ? (rendererServer = await startPackagedRendererServer()).url
    : process.env.ELECTRON_RENDERER_URL ?? 'http://localhost:3000';

  registerRuntimeControlHandlers({
    client: runtimeClient,
    lifecycle: createDesktopDaemonLifecycle(),
    desktopExecutable: app.getPath('exe'),
    packaged: app.isPackaged,
    rendererOrigin: new URL(rendererUrl).origin,
    // An operator action that makes the daemon reachable should not have to wait
    // out the backoff ladder.
    onDaemonAvailable: async () => {
      await bindingSupervisor?.refreshNow();
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
  // Re-assert the headless posture now that NSApplication is fully up.
  applyDaemonActivationPolicy();
  desktopLogger = createDesktopLogger({
    directory: path.join(app.getPath('userData'), 'logs'),
    fileName: 'desktop-daemon.log'
  });
  process.env.CHIRALITY_INSTRUCTION_ROOT = resolveInstructionRootForProcess();
  desktopLogger.info('runtime.daemon.starting', {
    activationPolicy: resolveDaemonActivationPolicy(process.env),
    packaged: app.isPackaged,
    userData: app.getPath('userData'),
    pid: process.pid
  });
  runtimeHost = await startRuntimeHost();
  desktopLogger.info('runtime.daemon.started', {
    socketPath: runtimeHost.socketPath,
    runtimeDirectory: runtimeHost.runtimeDirectory
  });
}

async function shutdown(exitCode = 0, reason = 'unspecified'): Promise<void> {
  if (shutdownStarted) {
    return;
  }
  shutdownStarted = true;
  // Logged first: the reason a daemon exited is exactly the evidence that was
  // missing when a clean `exit(0)` at GUI-launch time had to be diagnosed from
  // launchd bookkeeping alone.
  desktopLogger.info('desktop.shutdown.started', {
    reason,
    exitCode,
    daemonMode: runtimeDaemonMode,
    pid: process.pid
  });
  bindingSupervisor?.stop();
  bindingSupervisor = undefined;
  ipcMain.removeHandler(SELECT_DIRECTORY_CHANNEL);
  ipcMain.removeHandler(RUNTIME_CONNECTIVITY_QUERY_CHANNEL);
  unregisterApiKeyHandlers();
  unregisterRuntimeControlHandlers();

  if (runtimeHost) {
    try {
      await runtimeHost.stop();
    } catch (error) {
      exitCode = 1;
      desktopLogger.error('runtime.daemon.stop_failed', error);
    }
    runtimeHost = undefined;
  }

  if (rendererServer) {
    try {
      await rendererServer.close();
    } catch (error) {
      exitCode = 1;
      desktopLogger.error('desktop.renderer_server.close_failed', error);
    }
    rendererServer = undefined;
  }
  desktopLogger.info('desktop.shutdown.exiting', { reason, exitCode });
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
    desktopLogger.error(
      runtimeDaemonMode ? 'runtime.daemon.initialize_failed' : 'desktop.gui.initialize_failed',
      error instanceof Error ? error.message : String(error)
    );
    shutdownAuthorized = true;
    void shutdown(1, 'initialize-failed');
  });

app.on('window-all-closed', () => {
  if (!runtimeDaemonMode && process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', (event) => {
  // A service must not be quittable by the window server. The daemon shares its
  // bundle with the GUI, so anything macOS aims at "Chirality.app" — a Dock
  // Quit, a Cmd-Q, an AppleEvent quit accompanying a LaunchServices launch —
  // arrives here and would previously end the daemon with a clean `exit(0)`,
  // silently and unrecoverably. Only a signal-driven or self-initiated shutdown
  // is honored; launchd retains full control because `bootout`/`kickstart -k`
  // work by signal (and SIGKILL remains uncatchable either way).
  if (runtimeDaemonMode && !shutdownAuthorized) {
    event.preventDefault();
    desktopLogger.warn('runtime.daemon.quit_request_vetoed', {
      pid: process.pid,
      hint: 'use launchctl bootout/kickstart, or SIGTERM, to stop the runtime daemon'
    });
    return;
  }
  if (!shutdownStarted && (runtimeHost !== undefined || rendererServer !== undefined)) {
    event.preventDefault();
    void shutdown(0, 'before-quit');
  }
});

if (runtimeDaemonMode) {
  // Diagnostics only. `activate` firing in the daemon is the direct signature of
  // macOS resolving a launch of the app bundle against this headless instance
  // instead of starting the GUI, which is the mechanism the activation policy
  // above is meant to remove. Recording it makes the hypothesis falsifiable in
  // an isolated verification run.
  app.on('activate', () => {
    desktopLogger.warn('runtime.daemon.activate_received', { pid: process.pid });
  });
  app.on('open-file', (_event, filePath) => {
    desktopLogger.warn('runtime.daemon.open_file_received', { filePath });
  });
  app.on('open-url', () => {
    desktopLogger.warn('runtime.daemon.open_url_received', { pid: process.pid });
  });
  app.on('second-instance', () => {
    desktopLogger.warn('runtime.daemon.second_instance_received', { pid: process.pid });
  });
}

for (const signal of ['SIGINT', 'SIGTERM'] as const) {
  process.once(signal, () => {
    shutdownAuthorized = true;
    void shutdown(signal === 'SIGINT' ? 130 : 0, `signal:${signal}`);
  });
}
