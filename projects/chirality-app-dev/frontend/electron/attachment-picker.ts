/**
 * Native attachment picker: validation and handler factory.
 *
 * The renderer names a project root; the main process shows a native
 * multi-file open dialog under that root and returns only canonical absolute
 * paths that (a) resolve inside the canonical project root and (b) carry a
 * supported attachment extension. Everything else — a symlink pointing out of
 * the project, a file from another folder, an unsupported type — makes the
 * whole selection fail closed with `cancelled: true` and a reason, so the
 * renderer never receives a partially trusted list.
 *
 * Kept free of `electron` imports; the dialog and sender check are injected so
 * the validation is unit-testable against a real temporary directory.
 */

import { realpath, stat } from 'node:fs/promises';
import path from 'node:path';
import {
  SUPPORTED_ATTACHMENT_EXTENSIONS,
  isSupportedAttachmentPath
} from '../src/lib/harness/ui-attachments';
import type { IpcSenderEvent } from './ipc-sender-policy';
import type {
  AttachmentSelectFilesRequest,
  AttachmentSelectFilesResult
} from './attachment-ipc-contract';

export type AttachmentOpenDialogOptions = {
  title: string;
  buttonLabel: string;
  defaultPath: string;
  properties: Array<'openFile' | 'multiSelections'>;
  filters: Array<{ name: string; extensions: string[] }>;
};

export type AttachmentOpenDialogResult = {
  canceled: boolean;
  filePaths: string[];
};

export type AttachmentPickerDependencies = {
  authorized: (event: IpcSenderEvent) => boolean;
  showOpenDialog: (options: AttachmentOpenDialogOptions) => Promise<AttachmentOpenDialogResult>;
};

/** `SUPPORTED_ATTACHMENT_EXTENSIONS` in the dot-less form Electron filters expect. */
export function attachmentDialogExtensions(): string[] {
  return SUPPORTED_ATTACHMENT_EXTENSIONS.map((extension) => extension.replace(/^\./u, ''));
}

export function attachmentDialogOptions(projectRoot: string): AttachmentOpenDialogOptions {
  return {
    title: 'Attach files',
    buttonLabel: 'Attach',
    defaultPath: projectRoot,
    properties: ['openFile', 'multiSelections'],
    filters: [{ name: 'Supported files', extensions: attachmentDialogExtensions() }]
  };
}

export class AttachmentPickerError extends Error {}

function within(root: string, candidate: string): boolean {
  const relative = path.relative(root, candidate);
  // Only a leading `..` path segment escapes; an in-root name such as
  // `..notes.md` is a legitimate file.
  const escapes = relative === '..' || relative.startsWith(`..${path.sep}`);
  return relative !== '' && !escapes && !path.isAbsolute(relative);
}

/**
 * Validate the renderer-supplied request and resolve its project root to a
 * canonical existing directory. The supplied value must already be absolute and
 * normalized — the renderer only ever holds roots produced by the folder picker
 * or by validated project bindings, so anything else is a malformed request.
 */
export async function resolveAttachmentProjectRoot(input: unknown): Promise<string> {
  if (!input || typeof input !== 'object' || Array.isArray(input)) {
    throw new AttachmentPickerError('Attachment request requires a project root.');
  }
  const root = (input as Partial<AttachmentSelectFilesRequest>).projectRoot;
  if (
    typeof root !== 'string' ||
    !path.isAbsolute(root) ||
    /[\x00-\x1f]/u.test(root) ||
    path.resolve(root) !== root
  ) {
    throw new AttachmentPickerError('Project root must be an absolute, normalized directory path.');
  }
  let canonical: string;
  try {
    canonical = await realpath(root);
  } catch {
    throw new AttachmentPickerError('Project root is not accessible.');
  }
  let info: Awaited<ReturnType<typeof stat>>;
  try {
    info = await stat(canonical);
  } catch {
    throw new AttachmentPickerError('Project root is not accessible.');
  }
  if (!info.isDirectory()) {
    throw new AttachmentPickerError('Project root must be a directory.');
  }
  return canonical;
}

/**
 * Canonicalize each dialog selection and enforce containment and type. Fails
 * closed on the first offending path; the returned list is deduplicated and
 * keeps the dialog's order.
 */
export async function resolveAttachmentSelections(
  canonicalRoot: string,
  selections: readonly string[]
): Promise<string[]> {
  const accepted: string[] = [];
  for (const selection of selections) {
    if (typeof selection !== 'string' || selection.length === 0) {
      throw new AttachmentPickerError('Selected path is not usable.');
    }
    let canonical: string;
    try {
      canonical = await realpath(path.resolve(selection));
    } catch {
      throw new AttachmentPickerError(`Selected file is not accessible: ${path.basename(selection)}`);
    }
    if (!within(canonicalRoot, canonical)) {
      throw new AttachmentPickerError(
        `Attachments must be inside the project folder: ${path.basename(selection)}`
      );
    }
    if (!isSupportedAttachmentPath(canonical)) {
      throw new AttachmentPickerError(
        `Unsupported attachment type: ${path.basename(selection)}`
      );
    }
    let info: Awaited<ReturnType<typeof stat>>;
    try {
      info = await stat(canonical);
    } catch {
      throw new AttachmentPickerError(`Selected file is not accessible: ${path.basename(selection)}`);
    }
    if (!info.isFile()) {
      throw new AttachmentPickerError(`Only regular files can be attached: ${path.basename(selection)}`);
    }
    if (!accepted.includes(canonical)) {
      accepted.push(canonical);
    }
  }
  return accepted;
}

/** `ipcMain.handle` body for the attachment picker channel. */
export function createAttachmentSelectionHandler(deps: AttachmentPickerDependencies) {
  return async (event: IpcSenderEvent, input: unknown): Promise<AttachmentSelectFilesResult> => {
    if (!deps.authorized(event)) {
      return { cancelled: true, error: 'Unauthorized attachment request.' };
    }
    try {
      const projectRoot = await resolveAttachmentProjectRoot(input);
      const dialogResult = await deps.showOpenDialog(attachmentDialogOptions(projectRoot));
      if (dialogResult.canceled || dialogResult.filePaths.length === 0) {
        return { cancelled: true };
      }
      const paths = await resolveAttachmentSelections(projectRoot, dialogResult.filePaths);
      return { cancelled: false, paths };
    } catch (error) {
      return {
        cancelled: true,
        error:
          error instanceof AttachmentPickerError
            ? error.message
            : 'Unable to attach the selected files.'
      };
    }
  };
}
