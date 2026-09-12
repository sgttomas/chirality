import { PLAN_EXPORT_DIALOG_CHANNEL, type PlanExportTargetResult } from './plan-export-ipc-contract';
import { contextBridge, ipcRenderer, webUtils } from 'electron';
import {
  RUNTIME_CONNECTIVITY_CHANGED_CHANNEL,
  RUNTIME_CONNECTIVITY_QUERY_CHANNEL,
  type RuntimeConnectivitySnapshot
} from './runtime-connectivity';
import {
  HOST_ACCOUNT_CHANNEL,
  type HostAccountDesktopOperation,
  type HostAccountDesktopResult,
  type HostAccountDesktopValue
} from './host-account-ipc-contract';
import {
  ATTACHMENT_SELECT_FILES_CHANNEL,
  type AttachmentSelectFilesRequest,
  type AttachmentSelectFilesResult
} from './attachment-ipc-contract';

const SELECT_DIRECTORY_CHANNEL = 'chirality:select-directory';
const API_KEY_STORE_CHANNEL = 'chirality:api-key-store';
const API_KEY_REMOVE_CHANNEL = 'chirality:api-key-remove';
const API_KEY_STATUS_CHANNEL = 'chirality:api-key-status';
const PROVIDER_API_KEY_STORE_CHANNEL = 'chirality:provider-api-key-store';
const PROVIDER_API_KEY_REMOVE_CHANNEL = 'chirality:provider-api-key-remove';
const PROVIDER_API_KEY_STATUS_CHANNEL = 'chirality:provider-api-key-status';
const RUNTIME_DAEMON_CONTROL_CHANNEL = 'chirality:runtime-daemon-control';
const RUNTIME_MODEL_STATUS_CHANNEL = 'chirality:runtime-model-status';
const RUNTIME_MODEL_ACTIVATE_CHANNEL = 'chirality:runtime-model-activate';

async function invokeHostAccount(
  operation: HostAccountDesktopOperation,
  projectRoot: string
): Promise<HostAccountDesktopValue> {
  const result = (await ipcRenderer.invoke(HOST_ACCOUNT_CHANNEL, {
    operation,
    projectRoot
  })) as HostAccountDesktopResult;
  if (!result.ok) {
    throw new Error(result.error);
  }
  return result.value;
}

contextBridge.exposeInMainWorld('chirality', {
  platform: process.platform,
  versions: {
    chrome: process.versions.chrome,
    electron: process.versions.electron,
    node: process.versions.node
  },
  selectDirectory: () => ipcRenderer.invoke(SELECT_DIRECTORY_CHANNEL),
  folders: {
    registerRecent: (path: string) => ipcRenderer.invoke('chirality:folder-register-recent', path),
    pathForFile: (file: File): string => {
      try { return webUtils.getPathForFile(file); } catch { return ''; }
    },
    subscribeOpen: (listener: (intent: { path?: string; error?: string }) => void): (() => void) => {
      let active = true;
      const handler = (_event: unknown, intent: { path?: string; error?: string }) => { if (active) listener(intent); };
      ipcRenderer.on('chirality:folder-open-intent', handler);
      void ipcRenderer.invoke('chirality:folder-open-ready').catch(() => { if (active) listener({ error: 'Folder intent delivery is unavailable.' }); });
      return () => { active = false; ipcRenderer.removeListener('chirality:folder-open-intent', handler); };
    }
  },
  plans: {
    chooseExportTarget: (request: { projectRoot: string; revision: number }): Promise<PlanExportTargetResult> =>
      ipcRenderer.invoke(PLAN_EXPORT_DIALOG_CHANNEL, { operation: 'choose', projectRoot: request.projectRoot, revision: request.revision }),
    confirmOverwrite: async (request: { projectRoot: string; targetRelativePath: string }): Promise<boolean> =>
      (await ipcRenderer.invoke(PLAN_EXPORT_DIALOG_CHANNEL, { operation: 'confirm-overwrite', projectRoot: request.projectRoot, targetRelativePath: request.targetRelativePath })) === true
  },
  attachments: {
    /**
     * Native multi-file picker rooted at the project. Only canonical absolute
     * paths inside the project folder with a supported extension come back;
     * any other selection cancels the whole request with a reason.
     */
    selectFiles: (request: AttachmentSelectFilesRequest): Promise<AttachmentSelectFilesResult> =>
      ipcRenderer.invoke(ATTACHMENT_SELECT_FILES_CHANNEL, { projectRoot: request.projectRoot })
  },
  document: {
    // Desktop retains the frame-denying renderer policy, so inline PDF preview
    // remains unavailable for the MVP fallback.
    inlinePdfPreview: false,
    handoff: (request: { projectRoot: string; target: string; action: 'quick-look' | 'open' | 'reveal' } | { projectRoot: string; action: 'reveal-root' }) =>
      ipcRenderer.invoke('chirality:document-handoff', request)
  },
  apiKey: {
    store: (key: string) => ipcRenderer.invoke(API_KEY_STORE_CHANNEL, key),
    remove: () => ipcRenderer.invoke(API_KEY_REMOVE_CHANNEL),
    status: () => ipcRenderer.invoke(API_KEY_STATUS_CHANNEL)
  },
  providerApiKey: {
    store: (providerId: 'anthropic' | 'omlx', key: string) =>
      ipcRenderer.invoke(PROVIDER_API_KEY_STORE_CHANNEL, providerId, key),
    remove: (providerId: 'anthropic' | 'omlx') =>
      ipcRenderer.invoke(PROVIDER_API_KEY_REMOVE_CHANNEL, providerId),
    status: (providerId: 'anthropic' | 'omlx') =>
      ipcRenderer.invoke(PROVIDER_API_KEY_STATUS_CHANNEL, providerId)
  },
  runtime: {
    /**
     * Runtime-daemon connectivity as the main process sees it. `get()` is for
     * mount-time hydration; `subscribe()` receives every later transition so the
     * top bar reflects a daemon that dies or returns without the renderer
     * polling. The unsubscribe function must be called on unmount — the listener
     * is held by `ipcRenderer`, which outlives any React tree.
     */
    connectivity: {
      get: (): Promise<RuntimeConnectivitySnapshot | null> =>
        ipcRenderer.invoke(RUNTIME_CONNECTIVITY_QUERY_CHANNEL),
      subscribe: (listener: (snapshot: RuntimeConnectivitySnapshot) => void): (() => void) => {
        const handler = (_event: unknown, snapshot: RuntimeConnectivitySnapshot): void => {
          listener(snapshot);
        };
        ipcRenderer.on(RUNTIME_CONNECTIVITY_CHANGED_CHANNEL, handler);
        return () => {
          ipcRenderer.removeListener(RUNTIME_CONNECTIVITY_CHANGED_CHANNEL, handler);
        };
      }
    },
    daemon: {
      install: () => ipcRenderer.invoke(RUNTIME_DAEMON_CONTROL_CHANNEL, 'install'),
      start: () => ipcRenderer.invoke(RUNTIME_DAEMON_CONTROL_CHANNEL, 'start'),
      stop: () => ipcRenderer.invoke(RUNTIME_DAEMON_CONTROL_CHANNEL, 'stop'),
      status: () => ipcRenderer.invoke(RUNTIME_DAEMON_CONTROL_CHANNEL, 'status'),
      uninstall: () => ipcRenderer.invoke(RUNTIME_DAEMON_CONTROL_CHANNEL, 'uninstall')
    },
    models: {
      status: () => ipcRenderer.invoke(RUNTIME_MODEL_STATUS_CHANNEL),
      activate: (modelId: string) =>
        ipcRenderer.invoke(RUNTIME_MODEL_ACTIVATE_CHANNEL, modelId)
    },
    hostedAccount: {
      status: (projectRoot: string) => invokeHostAccount('status', projectRoot),
      grantProviderNetworkConsent: (projectRoot: string) =>
        invokeHostAccount('grant-provider-network-consent', projectRoot),
      startLogin: (projectRoot: string) => invokeHostAccount('start-login', projectRoot),
      cancelLogin: (projectRoot: string) => invokeHostAccount('cancel-login', projectRoot),
      signOut: (projectRoot: string) => invokeHostAccount('sign-out', projectRoot)
    }
  }
});
