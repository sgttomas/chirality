import { contextBridge, ipcRenderer } from 'electron';
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
