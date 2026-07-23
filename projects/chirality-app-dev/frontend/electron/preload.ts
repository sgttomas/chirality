import { contextBridge, ipcRenderer } from 'electron';

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
