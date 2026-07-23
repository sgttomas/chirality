import { lstat, realpath } from 'node:fs/promises';
import path from 'node:path';
import { RuntimeClient } from '@chirality/runtime-client';
import type { ProjectStatus } from '@chirality/runtime-contracts';

export const DESKTOP_PROJECT_ID = 'chirality-app-dev';

type ProjectStatusClient = {
  projectStatus(projectId: string): Promise<ProjectStatus>;
};

export type DesktopProjectBinding = {
  projectId: typeof DESKTOP_PROJECT_ID;
  projectRoot: string;
  tokenFile: string;
};

export interface DesktopHarnessEnvironment {
  [name: string]: string | undefined;
  CHIRALITY_RUNTIME_SOCKET_PATH?: string;
  CHIRALITY_RUNTIME_TOKEN_FILE?: string;
  CHIRALITY_RUNTIME_PROJECT_ID?: string;
  CHIRALITY_RUNTIME_PROJECT_ROOT?: string;
}

export type DesktopProjectBindingOptions = {
  operatorClient: ProjectStatusClient;
  runtimeDirectory: string;
  socketPath: string;
  createScopedClient?: (input: {
    socketPath: string;
    tokenFile: string;
  }) => ProjectStatusClient;
};

function assertAuthorizedStatus(status: ProjectStatus): void {
  if (
    status.project.projectId !== DESKTOP_PROJECT_ID ||
    status.manifestDrift ||
    !status.adaptersEnabled
  ) {
    throw new Error('The app-dev project is unregistered, disabled, or has manifest drift');
  }
}

function isContained(root: string, candidate: string): boolean {
  const child = path.relative(root, candidate);
  return child === '' || (!child.startsWith('..') && !path.isAbsolute(child));
}

export function prepareDesktopHarnessEnvironment(
  environment: DesktopHarnessEnvironment,
  socketPath: string
): void {
  environment.CHIRALITY_RUNTIME_SOCKET_PATH = socketPath;
  environment.CHIRALITY_RUNTIME_PROJECT_ID = DESKTOP_PROJECT_ID;
  delete environment.CHIRALITY_RUNTIME_TOKEN_FILE;
  delete environment.CHIRALITY_RUNTIME_PROJECT_ROOT;
}

export function applyDesktopProjectBinding(
  environment: DesktopHarnessEnvironment,
  binding: DesktopProjectBinding
): void {
  if (binding.projectId !== DESKTOP_PROJECT_ID) {
    throw new Error('Chirality Desktop cannot bind a different project');
  }
  environment.CHIRALITY_RUNTIME_PROJECT_ID = DESKTOP_PROJECT_ID;
  environment.CHIRALITY_RUNTIME_PROJECT_ROOT = binding.projectRoot;
  environment.CHIRALITY_RUNTIME_TOKEN_FILE = binding.tokenFile;
}

/**
 * Resolve the renderer's project-scoped daemon credential through the
 * authenticated operator client. The token itself is never read here or
 * exposed to the renderer; RuntimeClient revalidates its ownership and mode
 * when a Next route makes a request.
 */
export async function resolveDesktopProjectBinding(
  options: DesktopProjectBindingOptions
): Promise<DesktopProjectBinding> {
  const status = await options.operatorClient.projectStatus(DESKTOP_PROJECT_ID);
  assertAuthorizedStatus(status);

  const { project } = status;
  if (!/^project-[A-Za-z0-9_-]+$/u.test(project.clientId)) {
    throw new Error('The app-dev project client identifier is malformed');
  }

  const canonicalRoot = await realpath(project.canonicalRoot);
  const canonicalManifest = await realpath(project.manifestPath);
  if (
    canonicalRoot !== path.resolve(project.canonicalRoot) ||
    path.dirname(canonicalManifest) !== canonicalRoot ||
    path.basename(canonicalManifest) !== 'chirality.project.json'
  ) {
    throw new Error('The app-dev project registration does not match its canonical manifest');
  }

  const tokensDirectory = path.resolve(options.runtimeDirectory, 'auth', 'tokens');
  const tokenFile = path.join(tokensDirectory, `${project.clientId}.token`);
  const tokenMetadata = await lstat(tokenFile);
  if (
    !tokenMetadata.isFile() ||
    tokenMetadata.isSymbolicLink() ||
    (tokenMetadata.mode & 0o077) !== 0 ||
    (process.getuid !== undefined && tokenMetadata.uid !== process.getuid())
  ) {
    throw new Error('The app-dev project token file is not private and user-owned');
  }
  const canonicalToken = await realpath(tokenFile);
  if (!isContained(tokensDirectory, canonicalToken)) {
    throw new Error('The app-dev project token escapes the runtime token directory');
  }

  const createScopedClient =
    options.createScopedClient ??
    ((input: { socketPath: string; tokenFile: string }) => new RuntimeClient(input));
  const scopedStatus = await createScopedClient({
    socketPath: options.socketPath,
    tokenFile: canonicalToken
  }).projectStatus(DESKTOP_PROJECT_ID);
  assertAuthorizedStatus(scopedStatus);
  if (
    scopedStatus.project.clientId !== project.clientId ||
    scopedStatus.project.manifestHash !== project.manifestHash ||
    path.resolve(scopedStatus.project.canonicalRoot) !== canonicalRoot
  ) {
    throw new Error('The app-dev project token resolved to a different registration');
  }

  return {
    projectId: DESKTOP_PROJECT_ID,
    projectRoot: canonicalRoot,
    tokenFile: canonicalToken
  };
}
