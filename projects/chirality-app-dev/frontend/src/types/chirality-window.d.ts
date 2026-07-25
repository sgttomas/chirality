type DirectorySelectionResult = {
  cancelled: boolean;
  path?: string;
  error?: string;
};

type RuntimeConnectivitySnapshotPayload = {
  state: 'connecting' | 'connected' | 'disconnected';
  failedAttempts: number;
  lastError: string | null;
  changedAt: string;
};

type ChiralityBridge = {
  platform?: string;
  versions?: {
    chrome: string;
    electron: string;
    node: string;
  };
  selectDirectory?: () => Promise<DirectorySelectionResult>;
  /**
   * Partial by design. `apiKey`/`providerApiKey`/`runtime.daemon`/`runtime.models`
   * are still narrowed locally by their own consumers; only the connectivity
   * surface is declared here, because the shell reads it directly.
   */
  runtime?: {
    connectivity?: {
      get: () => Promise<RuntimeConnectivitySnapshotPayload | null>;
      subscribe: (
        listener: (snapshot: RuntimeConnectivitySnapshotPayload) => void
      ) => () => void;
    };
  };
};

declare global {
  interface Window {
    chirality?: ChiralityBridge;
  }
}

export {};
