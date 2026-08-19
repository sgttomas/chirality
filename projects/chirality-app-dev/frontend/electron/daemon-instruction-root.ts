import path from 'node:path';

export type ProjectRoots = {
  workingRoot: string;
  instructionRoot: string;
};

export type PackagedDaemonInstructionRoot =
  | {
      instructionRoot: string;
      source: 'registered-project-manifest';
    }
  | {
      instructionRoot: string;
      source: 'packaged-resources-fallback';
      reason: string;
    };

type ResolvePackagedDaemonInstructionRootOptions = {
  projectId: string;
  packagedResourcesPath: string;
  resolveProjectRoots: (projectId: string) => Promise<ProjectRoots>;
};

function fallbackReason(error: unknown): string {
  if (typeof error === 'object' && error !== null && 'code' in error) {
    const code = (error as { code?: unknown }).code;
    if (typeof code === 'string' && /^[A-Z][A-Z0-9_]*$/u.test(code)) {
      return code;
    }
  }
  return 'MANIFEST_RESOLUTION_UNAVAILABLE';
}

/**
 * Resolve packaged daemon instructions from the already-approved project
 * registration. The registry owns manifest parsing, drift detection,
 * canonicalization, and containment, so this is the same root consumed by app
 * and CLI requests handled by the shared runtime.
 *
 * Packaged resources remain a bootstrapping fallback for an absent or
 * unavailable registration. The caller must durably log fallback results.
 */
export async function resolvePackagedDaemonInstructionRoot(
  options: ResolvePackagedDaemonInstructionRootOptions
): Promise<PackagedDaemonInstructionRoot> {
  try {
    const roots = await options.resolveProjectRoots(options.projectId);
    return {
      instructionRoot: path.resolve(roots.instructionRoot),
      source: 'registered-project-manifest'
    };
  } catch (error) {
    return {
      instructionRoot: path.resolve(options.packagedResourcesPath),
      source: 'packaged-resources-fallback',
      reason: fallbackReason(error)
    };
  }
}
