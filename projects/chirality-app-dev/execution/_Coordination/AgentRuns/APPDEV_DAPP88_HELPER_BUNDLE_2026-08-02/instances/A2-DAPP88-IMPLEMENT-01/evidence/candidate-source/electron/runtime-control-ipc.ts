import { app, ipcMain } from 'electron';
import path from 'node:path';
import { LaunchAgentManager, type LaunchAgentStatus } from '@chirality/runtime-cli';
import type { DaemonStatusResponse, ResidencyStatus } from '@chirality/runtime-contracts';
import {
  daemonPostureEnvironment,
  resolveDesktopDaemonPosture
} from './desktop-daemon-posture';

export const RUNTIME_DAEMON_CONTROL_CHANNEL = 'chirality:runtime-daemon-control';
export const RUNTIME_MODEL_STATUS_CHANNEL = 'chirality:runtime-model-status';
export const RUNTIME_MODEL_ACTIVATE_CHANNEL = 'chirality:runtime-model-activate';

export type RuntimeDaemonAction = 'install' | 'start' | 'stop' | 'status' | 'uninstall';

export type RuntimeDaemonControlResult =
  | {
      ok: true;
      launchAgent: Pick<LaunchAgentStatus, 'installed' | 'loaded'>;
      daemon: {
        running: boolean;
        pid?: number;
        startedAt?: string;
      };
    }
  | { ok: false; error: string };

export type RuntimeModelStatusResult =
  | { ok: true; residency: ResidencyStatus }
  | { ok: false; error: string };

export interface RuntimeControlClient {
  daemonStatus(): Promise<DaemonStatusResponse>;
  listModels(): Promise<ResidencyStatus>;
  activateModel(modelId: string, approvalReference: string): Promise<ResidencyStatus>;
}

export interface RuntimeDaemonLifecycle {
  install(executablePath: string): Promise<void>;
  start(): Promise<void>;
  stop(): Promise<void>;
  status(): Promise<LaunchAgentStatus>;
  uninstall(): Promise<void>;
}

export type RuntimeControlDependencies = {
  client: RuntimeControlClient;
  lifecycle: RuntimeDaemonLifecycle;
  daemonExecutable: string;
  packaged: boolean;
  rendererOrigin: string;
  onDaemonAvailable?: () => Promise<void>;
};

const DESKTOP_MODEL_ACTIVATION_APPROVAL = 'desktop-explicit-model-activation';
const MAX_MODEL_ID_LENGTH = 512;

function safeError(error: unknown, fallback: string): string {
  if (error instanceof Error && error.message.trim()) {
    return error.message.replaceAll(/(?:Bearer|token|credential|api[_ -]?key)\s+\S+/giu, '[redacted]');
  }
  return fallback;
}

function isRuntimeDaemonAction(value: unknown): value is RuntimeDaemonAction {
  return (
    value === 'install' ||
    value === 'start' ||
    value === 'stop' ||
    value === 'status' ||
    value === 'uninstall'
  );
}

function isSafeModelId(value: unknown): value is string {
  return (
    typeof value === 'string' &&
    value.length > 0 &&
    value.length <= MAX_MODEL_ID_LENGTH &&
    value.trim() === value &&
    !/[\u0000-\u001f\u007f]/u.test(value)
  );
}

function isAuthorizedSender(
  event: { senderFrame?: { url?: string } | null },
  rendererOrigin: string
): boolean {
  const senderUrl = event.senderFrame?.url;
  if (!senderUrl) return false;
  try {
    return new URL(senderUrl).origin === rendererOrigin;
  } catch {
    return false;
  }
}

async function daemonSnapshot(
  deps: RuntimeControlDependencies
): Promise<RuntimeDaemonControlResult> {
  try {
    const launchAgent = await deps.lifecycle.status();
    const daemonStatus = await deps.client.daemonStatus().catch(() => undefined);
    if (daemonStatus !== undefined) {
      await deps.onDaemonAvailable?.().catch(() => undefined);
    }
    return {
      ok: true,
      launchAgent: {
        installed: launchAgent.installed,
        loaded: launchAgent.loaded
      },
      daemon: daemonStatus
        ? {
            running: true,
            pid: daemonStatus.pid,
            startedAt: daemonStatus.startedAt
          }
        : { running: false }
    };
  } catch (error) {
    return {
      ok: false,
      error: safeError(error, 'Unable to read runtime daemon status')
    };
  }
}

/**
 * Install the desktop daemon's LaunchAgent with the project's posture.
 *
 * Values come from `desktop-daemon-posture.ts`, which the generated `chirality`
 * launcher also exports — so the in-app install and the documented
 * `chirality daemon install` now render the same plist. They did not before
 * (Stage V, V-D2).
 *
 * The whole posture is pinned into the job's `EnvironmentVariables`, not just the
 * runtime directory. launchd jobs inherit almost nothing, and the daemon needs to
 * know its own label: when it spawns a GUI in response to an `activate`
 * (V-D4), the child inherits the label and addresses the same job — which is what
 * keeps an isolated verification run from reaching the operator's real one.
 */
export function createDesktopDaemonLifecycle(): RuntimeDaemonLifecycle {
  const userData = app.getPath('userData');
  const posture = resolveDesktopDaemonPosture(process.env, userData);
  return new LaunchAgentManager(
    {
      launchAgentsDirectory: path.join(app.getPath('home'), 'Library', 'LaunchAgents'),
      runtimeDirectory: path.join(userData, 'runtime')
    },
    undefined,
    undefined,
    {
      label: posture.label,
      keepAlive: posture.keepAlive,
      runAtLoad: posture.runAtLoad,
      environmentVariables: daemonPostureEnvironment(posture)
    }
  );
}

export function registerRuntimeControlHandlers(deps: RuntimeControlDependencies): void {
  unregisterRuntimeControlHandlers();

  ipcMain.handle(
    RUNTIME_DAEMON_CONTROL_CHANNEL,
    async (event, action: unknown): Promise<RuntimeDaemonControlResult> => {
      if (!isAuthorizedSender(event, deps.rendererOrigin)) {
        return { ok: false, error: 'Runtime control request was denied' };
      }
      if (!isRuntimeDaemonAction(action)) {
        return { ok: false, error: 'Unsupported runtime daemon action' };
      }

      try {
        if (action === 'install') {
          if (!deps.packaged) {
            return {
              ok: false,
              error: 'Daemon installation is available only in a packaged Chirality desktop build'
            };
          }
          await deps.lifecycle.install(deps.daemonExecutable);
        } else if (action === 'start') {
          await deps.lifecycle.start();
        } else if (action === 'stop') {
          await deps.lifecycle.stop();
        } else if (action === 'uninstall') {
          await deps.lifecycle.uninstall();
        }
      } catch (error) {
        return {
          ok: false,
          error: safeError(error, `Unable to ${action} the runtime daemon`)
        };
      }

      return daemonSnapshot(deps);
    }
  );

  ipcMain.handle(
    RUNTIME_MODEL_STATUS_CHANNEL,
    async (event): Promise<RuntimeModelStatusResult> => {
      if (!isAuthorizedSender(event, deps.rendererOrigin)) {
        return { ok: false, error: 'Runtime control request was denied' };
      }
      try {
        return { ok: true, residency: await deps.client.listModels() };
      } catch (error) {
        return {
          ok: false,
          error: safeError(error, 'Unable to read oMLX model status')
        };
      }
    }
  );

  ipcMain.handle(
    RUNTIME_MODEL_ACTIVATE_CHANNEL,
    async (event, modelId: unknown): Promise<RuntimeModelStatusResult> => {
      if (!isAuthorizedSender(event, deps.rendererOrigin)) {
        return { ok: false, error: 'Runtime control request was denied' };
      }
      if (!isSafeModelId(modelId)) {
        return { ok: false, error: 'An exact valid oMLX model ID is required' };
      }

      try {
        const current = await deps.client.listModels();
        if (!current.models.some((model) => model.id === modelId)) {
          return { ok: false, error: 'The selected model is not reported by oMLX' };
        }
        return {
          ok: true,
          residency: await deps.client.activateModel(
            modelId,
            DESKTOP_MODEL_ACTIVATION_APPROVAL
          )
        };
      } catch (error) {
        return {
          ok: false,
          error: safeError(error, 'Unable to activate the selected oMLX model')
        };
      }
    }
  );
}

export function unregisterRuntimeControlHandlers(): void {
  ipcMain.removeHandler(RUNTIME_DAEMON_CONTROL_CHANNEL);
  ipcMain.removeHandler(RUNTIME_MODEL_STATUS_CHANNEL);
  ipcMain.removeHandler(RUNTIME_MODEL_ACTIVATE_CHANNEL);
}
