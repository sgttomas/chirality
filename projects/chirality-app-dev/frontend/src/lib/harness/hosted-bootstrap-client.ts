import type {
  HostedBootstrapLoginStartResponse,
  HostedBootstrapStatus
} from '@chirality/runtime-contracts';

export type HostedBootstrapStatusResponse =
  | { registration: 'required' }
  | {
      registration: 'registered';
      projectId: string;
      status: HostedBootstrapStatus;
    };

export class HostedBootstrapClientError extends Error {
  constructor(readonly status: number, message: string) {
    super(message);
    this.name = 'HostedBootstrapClientError';
  }
}

function desktopHostedAccount() {
  const client = window.chirality?.runtime?.hostedAccount;
  if (!client) {
    throw new HostedBootstrapClientError(503, 'The hosted runtime bootstrap service is unavailable.');
  }
  return client;
}

function preflightSignal(signal?: AbortSignal): void {
  if (signal?.aborted) {
    throw signal.reason ?? new DOMException('The operation was aborted.', 'AbortError');
  }
}

function withLocalAbort<T>(operation: Promise<T>, signal?: AbortSignal): Promise<T> {
  if (!signal) return operation;
  return new Promise<T>((resolve, reject) => {
    const abort = (): void => reject(
      signal.reason ?? new DOMException('The operation was aborted.', 'AbortError')
    );
    signal.addEventListener('abort', abort, { once: true });
    operation.then(resolve, reject).finally(() => signal.removeEventListener('abort', abort));
  });
}

async function requestJson<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, init);
  let payload: unknown;
  try {
    payload = await response.json();
  } catch {
    payload = undefined;
  }
  if (!response.ok) {
    const message = payload && typeof payload === 'object' && 'error' in payload &&
      typeof (payload as { error?: { message?: unknown } }).error?.message === 'string'
      ? (payload as { error: { message: string } }).error.message
      : 'The hosted runtime bootstrap service is unavailable.';
    throw new HostedBootstrapClientError(response.status, message);
  }
  return payload as T;
}

function post(projectRoot: string, signal?: AbortSignal, extra: object = {}): RequestInit {
  return {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ projectRoot, ...extra }),
    signal
  };
}

export function getHostedBootstrapStatus(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedBootstrapStatusResponse> {
  preflightSignal(signal);
  return withLocalAbort(desktopHostedAccount().status(projectRoot), signal);
}

export function initializeHostedBootstrapProject(
  projectRoot: string,
  signal?: AbortSignal
): Promise<Extract<HostedBootstrapStatusResponse, { registration: 'registered' }>> {
  return requestJson(
    '/api/harness/hosted-bootstrap/project/initialize',
    post(projectRoot, signal)
  );
}

export function grantHostedProviderNetworkConsent(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedBootstrapStatus> {
  preflightSignal(signal);
  return withLocalAbort(desktopHostedAccount()
    .grantProviderNetworkConsent(projectRoot)
    .then((result) => {
      if (result.registration !== 'registered') throw new HostedBootstrapClientError(503, 'The hosted runtime bootstrap service is unavailable.');
      return result.status;
    }), signal);
}

export function startHostedBootstrapLogin(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedBootstrapLoginStartResponse> {
  preflightSignal(signal);
  return withLocalAbort(desktopHostedAccount().startLogin(projectRoot), signal);
}

export function cancelHostedBootstrapLogin(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedBootstrapStatus> {
  preflightSignal(signal);
  return withLocalAbort(desktopHostedAccount().cancelLogin(projectRoot).then((result) => {
    if (result.registration !== 'registered') throw new HostedBootstrapClientError(503, 'The hosted runtime bootstrap service is unavailable.');
    return result.status;
  }), signal);
}

export function signOutHostedBootstrapProject(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedBootstrapStatus> {
  preflightSignal(signal);
  return withLocalAbort(desktopHostedAccount().signOut(projectRoot).then((result) => {
    if (result.registration !== 'registered') throw new HostedBootstrapClientError(503, 'The hosted runtime bootstrap service is unavailable.');
    return result.status;
  }), signal);
}
