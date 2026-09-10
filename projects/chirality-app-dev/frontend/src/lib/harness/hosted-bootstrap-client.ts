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
  const params = new URLSearchParams({ projectRoot });
  return requestJson(`/api/harness/hosted-bootstrap/status?${params}`, { signal });
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
  return requestJson(
    '/api/harness/hosted-bootstrap/provider-network-consent',
    post(projectRoot, signal, { consent: true })
  );
}

export function startHostedBootstrapLogin(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedBootstrapLoginStartResponse> {
  return requestJson(
    '/api/harness/hosted-bootstrap/login/start',
    post(projectRoot, signal)
  );
}

export function cancelHostedBootstrapLogin(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedBootstrapStatus> {
  return requestJson(
    '/api/harness/hosted-bootstrap/login/cancel',
    post(projectRoot, signal)
  );
}

export function signOutHostedBootstrapProject(
  projectRoot: string,
  signal?: AbortSignal
): Promise<HostedBootstrapStatus> {
  return requestJson(
    '/api/harness/hosted-bootstrap/logout',
    post(projectRoot, signal)
  );
}
