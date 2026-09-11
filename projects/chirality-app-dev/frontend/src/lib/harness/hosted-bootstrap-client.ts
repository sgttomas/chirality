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

export type HostedProjectBindingResponse =
  | { registration: 'required' }
  | { registration: 'registered'; projectId: string };

export class HostedBootstrapClientError extends Error {
  constructor(readonly status: number, message: string) {
    super(message);
    this.name = 'HostedBootstrapClientError';
  }
}

const HOST_ACCOUNT_RETRY_DELAYS_MS = [250, 1_000, 5_000] as const;
const HOST_ACCOUNT_UNAVAILABLE = 'Hosted account service is unavailable.';

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

function retryDelay(delayMs: number, signal?: AbortSignal): Promise<void> {
  preflightSignal(signal);
  return new Promise<void>((resolve, reject) => {
    const timer = setTimeout(() => {
      signal?.removeEventListener('abort', abort);
      resolve();
    }, delayMs);
    const abort = (): void => {
      clearTimeout(timer);
      reject(signal?.reason ?? new DOMException('The operation was aborted.', 'AbortError'));
    };
    signal?.addEventListener('abort', abort, { once: true });
  });
}

function isTransientHostAccountError(error: unknown): boolean {
  return error instanceof Error && error.message === HOST_ACCOUNT_UNAVAILABLE;
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

export function bindHostedBootstrapProject(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedProjectBindingResponse> {
  return requestJson(
    '/api/harness/hosted-bootstrap/project/bind',
    post(projectRoot, signal)
  );
}

export async function hydrateHostedBootstrapProject(
  projectRoot: string,
  onBound: (binding: Extract<HostedProjectBindingResponse, { registration: 'registered' }>) => void,
  signal?: AbortSignal
): Promise<HostedBootstrapStatusResponse> {
  const binding = await bindHostedBootstrapProject(projectRoot, signal);
  if (binding.registration === 'registered') onBound(binding);
  for (let attempt = 0; ; attempt += 1) {
    try {
      return await getHostedBootstrapStatus(projectRoot, signal);
    } catch (error) {
      const delayMs = HOST_ACCOUNT_RETRY_DELAYS_MS[attempt];
      if (!isTransientHostAccountError(error) || delayMs === undefined) throw error;
      await retryDelay(delayMs, signal);
    }
  }
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
