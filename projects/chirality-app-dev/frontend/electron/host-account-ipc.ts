import { ipcMain, type IpcMainInvokeEvent } from 'electron';
import { realpath } from 'node:fs/promises';
import path from 'node:path';
import type { RuntimeClient } from '@chirality/runtime-client';
import type { HostAccountClient } from '@chirality/runtime-daemon';
import { isAuthorizedSender } from './ipc-sender-policy';
import {
  HOST_ACCOUNT_CHANNEL,
  type HostAccountDesktopOperation,
  type HostAccountDesktopResult
} from './host-account-ipc-contract';

type HostAccountIpcOptions = {
  runtimeClient: Pick<RuntimeClient, 'listProjects' | 'projectStatus'>;
  accountClient(): HostAccountClient | undefined;
  invalidateAccountClient?(client: HostAccountClient): void;
  rendererOrigin: string;
};

const OPERATIONS: readonly HostAccountDesktopOperation[] = [
  'status',
  'grant-provider-network-consent',
  'start-login',
  'cancel-login',
  'sign-out'
];

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
  try {
    const request = parseRequest(requestValue);
    const project = await resolveRegisteredProject(request.projectRoot, options.runtimeClient);
    if (!project) {
      return request.operation === 'status'
        ? { ok: true, value: { registration: 'required' } }
        : { ok: false, error: 'Hosted account service is unavailable.' };
    }
    selectedClient = options.accountClient();
    if (!selectedClient) {
      return { ok: false, error: 'Hosted account service is unavailable.' };
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
  } catch {
    if (selectedClient) options.invalidateAccountClient?.(selectedClient);
    return { ok: false, error: 'Hosted account service is unavailable.' };
  }
}

export function registerHostAccountHandler(options: HostAccountIpcOptions): void {
  ipcMain.removeHandler(HOST_ACCOUNT_CHANNEL);
  ipcMain.handle(HOST_ACCOUNT_CHANNEL, (event: IpcMainInvokeEvent, request: unknown) => {
    if (!isAuthorizedSender(event, options.rendererOrigin)) {
      return { ok: false, error: 'Hosted account service is unavailable.' } satisfies HostAccountDesktopResult;
    }
    return performHostAccountOperation(request, options);
  });
}

export function unregisterHostAccountHandler(): void {
  ipcMain.removeHandler(HOST_ACCOUNT_CHANNEL);
}
