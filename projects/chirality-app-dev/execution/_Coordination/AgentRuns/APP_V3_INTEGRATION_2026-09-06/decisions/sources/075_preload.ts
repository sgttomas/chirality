import { contextBridge, ipcRenderer, webUtils } from 'electron';
import {
  RUNTIME_CONNECTIVITY_CHANGED_CHANNEL,
  RUNTIME_CONNECTIVITY_QUERY_CHANNEL,
  type RuntimeConnectivitySnapshot
} from './runtime-connectivity';

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
  document: {
    // Both Electron modes retain the current frame-denying renderer policy.
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
    }
  }
});
