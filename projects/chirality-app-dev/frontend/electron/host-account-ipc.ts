import { ipcMain, type IpcMainInvokeEvent } from 'electron';
import { realpath } from 'node:fs/promises';
import path from 'node:path';
import type { RuntimeClient } from '@chirality/runtime-client';
import type { HostAccountClient } from '@chirality/runtime-daemon';
import type { DesktopLogLevel } from './desktop-log';
import { isAuthorizedSender } from './ipc-sender-policy';
import {
  HOST_ACCOUNT_CHANNEL,
  HOST_ACCOUNT_UNAVAILABLE,
  type HostAccountDesktopOperation,
  type HostAccountDesktopResult
} from './host-account-ipc-contract';

type HostAccountIpcOptions = {
  runtimeClient: Pick<RuntimeClient, 'listProjects' | 'projectStatus'>;
  accountClient(): HostAccountClient | undefined;
  invalidateAccountClient?(client: HostAccountClient): void;
  log?(level: DesktopLogLevel, event: string, detail?: unknown): void;
  rendererOrigin: string;
};

const OPERATIONS: readonly HostAccountDesktopOperation[] = [
  'status',
  'grant-provider-network-consent',
  'start-login',
  'cancel-login',
  'sign-out'
];

/** Short operator wording per rejected operation; the reason code is appended. */
const REJECTION_MESSAGES: Readonly<Record<HostAccountDesktopOperation, string>> = {
  status: 'Account status could not be read',
  'grant-provider-network-consent': 'Provider network consent could not be recorded',
  'start-login': 'Sign-in could not start',
  'cancel-login': 'Sign-in could not be cancelled',
  'sign-out': 'Sign-out could not complete'
};

/**
 * The daemon-side rejection shape the runtime's `host-account-client` attaches
 * as `RuntimeError.details` for HTTP responses of 400 and above. Anything that
 * does not match this exactly is treated as a transport or authority failure.
 */
type OperationRejection = {
  kind: 'operation-rejected';
  operation: string;
  status: number;
  daemonCode?: string;
  reason?: string;
  daemonMessage?: string;
};

const DAEMON_CODE_PATTERN = /^[A-Z_]+$/;
const REASON_PATTERN = /^[A-Z0-9_]+$/;

function optionalString(
  value: unknown,
  maxLength: number,
  pattern?: RegExp
): string | undefined | false {
  if (value === undefined) return undefined;
  if (typeof value !== 'string' || value.length === 0 || value.length > maxLength) return false;
  if (pattern && !pattern.test(value)) return false;
  return value;
}

export function parseOperationRejection(error: unknown): OperationRejection | undefined {
  if (error === null || typeof error !== 'object') return undefined;
  const details = (error as { details?: unknown }).details;
  if (details === null || typeof details !== 'object' || Array.isArray(details)) return undefined;
  const record = details as Record<string, unknown>;
  if (
    record.kind !== 'operation-rejected' ||
    typeof record.operation !== 'string' ||
    !Number.isSafeInteger(record.status)
  ) {
    return undefined;
  }
  const daemonCode = optionalString(record.daemonCode, 64, DAEMON_CODE_PATTERN);
  const reason = optionalString(record.reason, 64, REASON_PATTERN);
  const daemonMessage = optionalString(record.daemonMessage, 200);
  if (daemonCode === false || reason === false || daemonMessage === false) return undefined;
  return {
    kind: 'operation-rejected',
    operation: record.operation,
    status: record.status as number,
    ...(daemonCode !== undefined ? { daemonCode } : {}),
    ...(reason !== undefined ? { reason } : {}),
    ...(daemonMessage !== undefined ? { daemonMessage } : {})
  };
}

/**
 * Loggable view of a failure. Only `RuntimeError` messages are fixed strings
 * the runtime composes itself; any other error's message is withheld because a
 * transport-layer error can echo request material (bearer, proof, counters).
 */
function describeFailure(error: unknown): {
  name?: string;
  code?: string;
  status?: number;
  message?: string;
} {
  if (error === null || typeof error !== 'object') return {};
  const candidate = error as { name?: unknown; code?: unknown; status?: unknown; message?: unknown };
  const name = typeof candidate.name === 'string' ? candidate.name : undefined;
  return {
    ...(name !== undefined ? { name } : {}),
    ...(typeof candidate.code === 'string' ? { code: candidate.code } : {}),
    ...(typeof candidate.status === 'number' ? { status: candidate.status } : {}),
    ...(name === 'RuntimeError' && typeof candidate.message === 'string'
      ? { message: candidate.message }
      : {})
  };
}

function parseRequest(value: unknown): {
  operation: HostAccountDesktopOperation;
  projectRoot: string;
} {
  if (
    value === null ||
    typeof value !== 'object' ||
    Array.isArray(value) ||
    Object.keys(value).sort().join(',') !== 'operation,projectRoot'
  ) {
    throw new Error('invalid-request');
  }
  const request = value as Record<string, unknown>;
  if (
    typeof request.operation !== 'string' ||
    !OPERATIONS.includes(request.operation as HostAccountDesktopOperation) ||
    typeof request.projectRoot !== 'string' ||
    !path.isAbsolute(request.projectRoot) ||
    path.resolve(request.projectRoot) !== request.projectRoot
  ) {
    throw new Error('invalid-request');
  }
  return {
    operation: request.operation as HostAccountDesktopOperation,
    projectRoot: request.projectRoot
  };
}

async function resolveRegisteredProject(
  projectRoot: string,
  runtimeClient: HostAccountIpcOptions['runtimeClient']
) {
  const canonicalRoot = await realpath(projectRoot);
  if (canonicalRoot !== projectRoot) return undefined;
  const matching = (await runtimeClient.listProjects()).filter(
    ({ project }) =>
      path.isAbsolute(project.canonicalRoot) &&
      path.resolve(project.canonicalRoot) === project.canonicalRoot &&
      project.canonicalRoot === canonicalRoot
  );
  if (matching.length !== 1) return undefined;
  const listed = matching[0];
  if (!listed || listed.manifestDrift || !listed.adaptersEnabled) {
    return undefined;
  }
  const status = await runtimeClient.projectStatus(listed.project.projectId);
  if (
    status.manifestDrift ||
    !status.adaptersEnabled ||
    status.project.projectId !== listed.project.projectId ||
    status.project.canonicalRoot !== canonicalRoot ||
    status.project.manifestHash !== listed.project.manifestHash
  ) {
    return undefined;
  }
  return status.project;
}

export async function performHostAccountOperation(
  requestValue: unknown,
  options: Omit<HostAccountIpcOptions, 'rendererOrigin'>
): Promise<HostAccountDesktopResult> {
  let selectedClient: HostAccountClient | undefined;
  let operation: HostAccountDesktopOperation | undefined;
  let projectId: string | undefined;
  try {
    const request = parseRequest(requestValue);
    operation = request.operation;
    const project = await resolveRegisteredProject(request.projectRoot, options.runtimeClient);
    if (!project) {
      return request.operation === 'status'
        ? { ok: true, value: { registration: 'required' } }
        : { ok: false, error: HOST_ACCOUNT_UNAVAILABLE };
    }
    projectId = project.projectId;
    selectedClient = options.accountClient();
    if (!selectedClient) {
      options.log?.('warn', 'runtime.account_host.client_unavailable', { operation, projectId });
      return { ok: false, error: HOST_ACCOUNT_UNAVAILABLE };
    }
    if (request.operation === 'start-login') {
      return { ok: true, value: await selectedClient.startLogin(project.projectId) };
    }
    const status =
      request.operation === 'status'
        ? await selectedClient.status(project.projectId)
        : request.operation === 'grant-provider-network-consent'
          ? await selectedClient.grantProviderNetworkConsent(project.projectId)
          : request.operation === 'cancel-login'
            ? await selectedClient.cancelLogin(project.projectId)
            : await selectedClient.signOut(project.projectId);
    return {
      ok: true,
      value: { registration: 'registered', projectId: project.projectId, status }
    };
  } catch (error) {
    const rejection = selectedClient ? parseOperationRejection(error) : undefined;
    if (rejection && operation) {
      // The daemon answered. The signed connection is intact, so tearing it
      // down would only cost the ~30 s re-establishment for nothing.
      const reason = rejection.reason ?? rejection.daemonCode;
      options.log?.('warn', 'runtime.account_host.operation_rejected', {
        operation,
        projectId,
        ...describeFailure(error),
        daemonOperation: rejection.operation,
        daemonStatus: rejection.status,
        ...(rejection.daemonCode !== undefined ? { daemonCode: rejection.daemonCode } : {}),
        ...(reason !== undefined ? { reason } : {}),
        ...(rejection.daemonMessage !== undefined ? { daemonMessage: rejection.daemonMessage } : {})
      });
      return {
        ok: false,
        error: `${REJECTION_MESSAGES[operation]}${reason ? ` (${reason})` : ''}.`,
        ...(reason !== undefined ? { reason } : {})
      };
    }
    options.log?.('error', 'runtime.account_host.operation_failed', {
      operation,
      projectId,
      clientSelected: selectedClient !== undefined,
      ...describeFailure(error)
    });
    if (selectedClient) options.invalidateAccountClient?.(selectedClient);
    return { ok: false, error: HOST_ACCOUNT_UNAVAILABLE };
  }
}

export function registerHostAccountHandler(options: HostAccountIpcOptions): void {
  ipcMain.removeHandler(HOST_ACCOUNT_CHANNEL);
  ipcMain.handle(HOST_ACCOUNT_CHANNEL, (event: IpcMainInvokeEvent, request: unknown) => {
    if (!isAuthorizedSender(event, options.rendererOrigin)) {
      return { ok: false, error: HOST_ACCOUNT_UNAVAILABLE } satisfies HostAccountDesktopResult;
    }
    return performHostAccountOperation(request, options);
  });
}

export function unregisterHostAccountHandler(): void {
  ipcMain.removeHandler(HOST_ACCOUNT_CHANNEL);
}
