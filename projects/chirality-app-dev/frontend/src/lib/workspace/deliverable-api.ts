import type { DeliverableRecordedRegister } from '../dependencies/recorded-register';
import type { DependencyRegisterRow } from '../dependencies/schema';
import type { ParsedStatusDocument } from '../lifecycle/status-parser';

type WorkspaceErrorPayload = {
  error?: {
    type?: string;
    message?: string;
    details?: unknown;
  };
};

export class WorkspaceApiClientError extends Error {
  readonly status: number;
  readonly code: string;
  readonly details?: unknown;

  constructor(status: number, code: string, message: string, details?: unknown) {
    super(message);
    this.name = 'WorkspaceApiClientError';
    this.status = status;
    this.code = code;
    this.details = details;
  }
}

async function readJson<T>(response: Response): Promise<T | undefined> {
  try {
    return (await response.json()) as T;
  } catch {
    return undefined;
  }
}

async function requestWorkspaceApi<T>(
  input: RequestInfo | URL,
  init: RequestInit,
  fallbackMessage: string
): Promise<T> {
  const response = await fetch(input, init);
  const payload = await readJson<T & WorkspaceErrorPayload>(response);

  if (!response.ok) {
    const type = payload?.error?.type ?? 'WORKSPACE_API_ERROR';
    const message = payload?.error?.message ?? fallbackMessage;
    throw new WorkspaceApiClientError(response.status, type, message, payload?.error?.details);
  }

  if (!payload) {
    throw new WorkspaceApiClientError(
      response.status,
      'INVALID_RESPONSE',
      'Workspace API returned an empty response body'
    );
  }

  return payload as T;
}

export interface DeliverableStatusSnapshot {
  projectRoot: string;
  deliverablePath: string;
  statusFilePath: string;
  status: ParsedStatusDocument;
}

export interface DeliverableStatusTransitionResult extends DeliverableStatusSnapshot {
  transition: {
    from: string;
    to: string;
    actor: string;
  };
}

export interface DeliverableDependenciesSnapshot {
  projectRoot: string;
  deliverablePath: string;
  dependenciesFilePath: string;
  dependenciesSummaryPath?: string;
  registerPresent: boolean;
  secondarySummaryPresent: boolean;
  headers: string[];
  /** Raw Dependencies.csv rows: register evidence, not a blocker judgment. */
  rows: DependencyRegisterRow[];
  warnings: string[];
  /** The recorded register and supplier-judged blocker verdict (App SPEC §5.2). */
  recordedRegister?: DeliverableRecordedRegister;
}

export interface DeliverableStatusTransitionInput {
  projectRoot: string;
  deliverablePath: string;
  targetState: string;
  actor: string;
  date?: string;
  metadata?: Record<string, string>;
  approvalSha?: string;
  ruling?: string;
  /** Accepted scope-change amendment (ID or path) authorizing ISSUED -> IN_PROGRESS. */
  amendment?: string;
}

export async function fetchDeliverableStatus(
  projectRoot: string,
  deliverablePath: string
): Promise<DeliverableStatusSnapshot> {
  const query = new URLSearchParams({ projectRoot, deliverablePath });
  return requestWorkspaceApi<DeliverableStatusSnapshot>(
    `/api/working-root/deliverable/status?${query.toString()}`,
    { method: 'GET' },
    'Unable to read deliverable lifecycle status'
  );
}

export async function transitionDeliverableStatus(
  input: DeliverableStatusTransitionInput
): Promise<DeliverableStatusTransitionResult> {
  return requestWorkspaceApi<DeliverableStatusTransitionResult>(
    '/api/working-root/deliverable/status/transition',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    },
    'Unable to apply lifecycle transition'
  );
}

export async function fetchDeliverableDependencies(
  projectRoot: string,
  deliverablePath: string
): Promise<DeliverableDependenciesSnapshot> {
  const query = new URLSearchParams({ projectRoot, deliverablePath });
  return requestWorkspaceApi<DeliverableDependenciesSnapshot>(
    `/api/working-root/deliverable/dependencies?${query.toString()}`,
    { method: 'GET' },
    'Unable to read deliverable dependency register'
  );
}
