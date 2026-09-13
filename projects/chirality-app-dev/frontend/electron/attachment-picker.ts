/**
 * Native attachment picker: validation and handler factory.
 *
 * The renderer names a project root; the main process shows a native
 * multi-file open dialog under that root and returns only explicitly selected,
 * canonical regular files with supported extensions. Sources may be outside the
 * project: Runtime validates and copies their bytes into contained conversation
 * custody on send. No broader workspace access is granted. Invalid files make
 * the whole selection fail with a reason; no partially trusted list is returned.
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
  message: string;
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
    message: 'Selected files are copied into this chat’s folder when you send.',
    defaultPath: projectRoot,
    properties: ['openFile', 'multiSelections'],
    filters: [{ name: 'Supported files', extensions: attachmentDialogExtensions() }]
  };
}

export class AttachmentPickerError extends Error {}

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
 * Validate each explicit dialog selection without following symlink aliases. Fails
 * closed on the first offending path; the returned list is deduplicated and
 * keeps the dialog's order.
 */
export async function resolveAttachmentSelections(
  selections: readonly string[]
): Promise<string[]> {
  const accepted: string[] = [];
  for (const selection of selections) {
    if (typeof selection !== 'string' || !path.isAbsolute(selection) || path.resolve(selection) !== selection || /[\x00-\x1f]/u.test(selection)) {
      throw new AttachmentPickerError('Selected path is not usable.');
    }
    let canonical: string;
    try {
      canonical = await realpath(selection);
    } catch {
      throw new AttachmentPickerError(`Selected file is not accessible: ${path.basename(selection)}`);
    }
    if (canonical !== selection) {
      throw new AttachmentPickerError(
        `Attachment paths must not contain symbolic links: ${path.basename(selection)}`
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
      const paths = await resolveAttachmentSelections(dialogResult.filePaths);
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
