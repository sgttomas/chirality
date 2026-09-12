type DirectorySelectionResult = {
  cancelled: boolean;
  path?: string;
  error?: string;
};

type AttachmentSelectionResult =
  | { cancelled: true; error?: string }
  | { cancelled: false; paths: string[] };

type RuntimeConnectivitySnapshotPayload = {
  state: 'connecting' | 'connected' | 'disconnected';
  failedAttempts: number;
  lastError: string | null;
  changedAt: string;
};

/**
 * `runtime.service.restart()` result, as `electron/runtime-control-ipc-contract.ts`
 * defines it: the service child's state after the relaunch settled, or the
 * redacted reason the main process refused or failed.
 */
type RuntimeServiceStatePayload = {
  status: 'idle' | 'starting' | 'ready' | 'restarting' | 'stopping' | 'stopped' | 'failed';
  pid: number | null;
  socketPath: string;
  clientTokenFile: string;
  restarts: number;
  recentFailures: number;
  lastExit: { code: number | null; signal: string | null; at: string } | null;
  lastError: string | null;
  nextRestartAt: string | null;
  changedAt: string;
};

type RuntimeServiceControlResultPayload =
  | { ok: true; service: RuntimeServiceStatePayload }
  | { ok: false; error: string };

type ChiralityBridge = {
  platform?: string;
  versions?: {
    chrome: string;
    electron: string;
    node: string;
  };
  selectDirectory?: () => Promise<DirectorySelectionResult>;
  /**
   * Native attachment picker rooted at a project folder. Returns canonical
   * absolute paths inside that folder with supported extensions only.
   */
  plans?: {
    chooseExportTarget: (request: { projectRoot: string; revision: number }) => Promise<{ cancelled: true; error?: string } | { cancelled: false; targetRelativePath: string }>;
    confirmOverwrite: (request: { projectRoot: string; targetRelativePath: string }) => Promise<boolean>;
  };
  attachments?: {
    selectFiles: (request: { projectRoot: string }) => Promise<AttachmentSelectionResult>;
  };
  /**
   * Partial by design. `apiKey`/`providerApiKey` remain narrowed locally by
   * their own consumers. Connectivity is declared because renderer clients
   * consume it directly. The retired `runtime.daemon`, `runtime.models` and
   * `runtime.hostedAccount` bridges are gone (D-GOV-43, A2); the preload now
   * exposes `runtime.service.restart()` for the retry after the App-owned
   * Runtime service gave up.
   */
  runtime?: {
    connectivity?: {
      get: () => Promise<RuntimeConnectivitySnapshotPayload | null>;
      subscribe: (
        listener: (snapshot: RuntimeConnectivitySnapshotPayload) => void
      ) => () => void;
    };
    service?: {
      /** Operator retry after the main process gave up restarting the service. */
      restart: () => Promise<RuntimeServiceControlResultPayload>;
    };
  };
};

declare global {
  interface Window {
    chirality?: ChiralityBridge;
  }
}

export {};
