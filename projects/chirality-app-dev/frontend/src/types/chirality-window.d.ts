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

type HostedAccountStatusPayload = import('@chirality/runtime-contracts').HostedBootstrapStatus;
type HostedAccountLoginPayload = import('@chirality/runtime-contracts').HostedBootstrapLoginStartResponse;
type HostedAccountStatusResponsePayload =
  | { registration: 'required' }
  | { registration: 'registered'; projectId: string; status: HostedAccountStatusPayload };

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
   * Partial by design. `apiKey`/`providerApiKey`/`runtime.daemon`/`runtime.models`
   * remain narrowed locally by their own consumers. Connectivity and the
   * project-root-only hosted account bridge are declared because renderer
   * clients consume them directly.
   */
  runtime?: {
    connectivity?: {
      get: () => Promise<RuntimeConnectivitySnapshotPayload | null>;
      subscribe: (
        listener: (snapshot: RuntimeConnectivitySnapshotPayload) => void
      ) => () => void;
    };
    hostedAccount?: {
      status: (projectRoot: string) => Promise<HostedAccountStatusResponsePayload>;
      grantProviderNetworkConsent: (projectRoot: string) => Promise<HostedAccountStatusResponsePayload>;
      startLogin: (projectRoot: string) => Promise<HostedAccountLoginPayload>;
      cancelLogin: (projectRoot: string) => Promise<HostedAccountStatusResponsePayload>;
      signOut: (projectRoot: string) => Promise<HostedAccountStatusResponsePayload>;
    };
  };
};

declare global {
  interface Window {
    chirality?: ChiralityBridge;
  }
}

export {};
