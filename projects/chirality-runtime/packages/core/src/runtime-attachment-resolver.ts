import { createHash, randomUUID } from "node:crypto";
import { constants } from "node:fs";
import { lstat, link, mkdir, open, realpath, unlink } from "node:fs/promises";
import { basename, extname, isAbsolute, join, resolve } from "node:path";
import { RuntimeError, type IAttachmentResolver, type ResolvedAttachments } from "@chirality/runtime-contracts";
import { assertSafeIdentifier, isContained } from "./fs.js";

const MAX_ATTACHMENT_BYTES = 10 * 1024 * 1024;
const MAX_TOTAL_ATTACHMENT_BYTES = 18 * 1024 * 1024;
const MIME_BY_EXTENSION: Readonly<Record<string, string>> = {
  ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif", ".webp": "image/webp",
  ".pdf": "application/pdf", ".txt": "text/plain", ".md": "text/markdown", ".csv": "text/csv"
};

async function privateDirectory(path: string): Promise<void> {
  await mkdir(path, { mode: 0o700 }).catch((error: NodeJS.ErrnoException) => { if (error.code !== "EEXIST") throw error; });
  const metadata = await lstat(path);
  if (!metadata.isDirectory() || metadata.isSymbolicLink() || await realpath(path) !== path) throw new RuntimeError("FORBIDDEN", "Attachment staging directory is unsafe", 403);
}

async function hashFile(path: string): Promise<string> {
  const handle = await open(path, constants.O_RDONLY | (constants.O_NOFOLLOW ?? 0));
  try { return createHash("sha256").update(await handle.readFile()).digest("hex"); }
  finally { await handle.close(); }
}

/** Stages explicitly selected files into immutable, project-contained conversation custody. */
export class RuntimeAttachmentResolver implements IAttachmentResolver {
  async resolveAttachmentsToContentBlocks(
    message: string,
    attachmentPaths: string[],
    context?: { projectId: string; sessionId: string; projectRoot: string }
  ): Promise<ResolvedAttachments> {
    if (!context) throw new RuntimeError("INVALID_REQUEST", "Hosted attachment staging requires project and session context");
    assertSafeIdentifier(context.projectId, "projectId"); assertSafeIdentifier(context.sessionId, "sessionId");
    if (!isAbsolute(context.projectRoot) || resolve(context.projectRoot) !== context.projectRoot || await realpath(context.projectRoot) !== context.projectRoot) throw new RuntimeError("FORBIDDEN", "Attachment project root must be canonical", 403);
    if (attachmentPaths.length > 8) throw new RuntimeError("INVALID_REQUEST", "At most eight attachments are supported");
    const contentBlocks: ResolvedAttachments["contentBlocks"] = message.trim() ? [{ type: "text", text: message }] : [];
    const chiralityDirectory = join(context.projectRoot, ".chirality");
    const attachmentDirectory = join(chiralityDirectory, "attachments");
    const sessionDirectory = join(attachmentDirectory, context.sessionId);
    await privateDirectory(chiralityDirectory); await privateDirectory(attachmentDirectory); await privateDirectory(sessionDirectory);
    if (!isContained(context.projectRoot, sessionDirectory)) throw new RuntimeError("FORBIDDEN", "Attachment staging escaped the project root", 403);
    const stagingIdentity = await lstat(sessionDirectory);
    const revalidateStaging = async (): Promise<void> => {
      const current = await lstat(sessionDirectory);
      if (!current.isDirectory() || current.isSymbolicLink() || current.dev !== stagingIdentity.dev || current.ino !== stagingIdentity.ino || await realpath(sessionDirectory) !== sessionDirectory) {
        throw new RuntimeError("FORBIDDEN", "Attachment staging directory changed during resolution", 403);
      }
    };
    let total = 0;
    for (const sourcePath of attachmentPaths) {
      if (!isAbsolute(sourcePath) || resolve(sourcePath) !== sourcePath) throw new RuntimeError("INVALID_REQUEST", "Attachment path must be normalized and absolute");
      const extension = extname(sourcePath).toLowerCase();
      const mimeType = MIME_BY_EXTENSION[extension];
      if (mimeType === undefined) throw new RuntimeError("INVALID_REQUEST", `Unsupported attachment extension: ${extension || "(none)"}`);
      const sourceRealPath = await realpath(sourcePath).catch(() => undefined);
      if (sourceRealPath !== sourcePath) throw new RuntimeError("INVALID_REQUEST", "Attachment path must not contain symbolic-link aliases");
      const source = await open(sourcePath, constants.O_RDONLY | (constants.O_NOFOLLOW ?? 0)).catch(() => undefined);
      if (!source) throw new RuntimeError("INVALID_REQUEST", "Attachment file is not readable");
      let bytes: Buffer; let before;
      try {
        before = await source.stat();
        if (!before.isFile()) throw new RuntimeError("INVALID_REQUEST", "Attachment path must reference a regular file");
        if (before.size > MAX_ATTACHMENT_BYTES) throw new RuntimeError("INVALID_REQUEST", "Attachment exceeds the per-file size limit");
        total += before.size;
        if (total > MAX_TOTAL_ATTACHMENT_BYTES) throw new RuntimeError("INVALID_REQUEST", "Attachments exceed the per-turn size limit");
        bytes = await source.readFile();
        const after = await source.stat();
        if (after.dev !== before.dev || after.ino !== before.ino || after.size !== before.size || after.mtimeMs !== before.mtimeMs || bytes.byteLength !== before.size) throw new RuntimeError("INVALID_REQUEST", "Attachment changed during staging");
      } finally { await source.close(); }
      const sha256 = createHash("sha256").update(bytes).digest("hex");
      const stagedName = `${sha256}${extension}`;
      const stagedPath = join(sessionDirectory, stagedName);
      const temporaryPath = join(sessionDirectory, `.${sha256}.${randomUUID()}.tmp`);
      try {
        const temporary = await open(temporaryPath, constants.O_CREAT | constants.O_EXCL | constants.O_WRONLY | (constants.O_NOFOLLOW ?? 0), 0o600);
        try { await temporary.writeFile(bytes); await temporary.sync(); }
        finally { await temporary.close(); }
        await revalidateStaging();
        await link(temporaryPath, stagedPath).catch(async (error: NodeJS.ErrnoException) => {
          if (error.code !== "EEXIST") throw error;
          const existing = await lstat(stagedPath);
          if (!existing.isFile() || existing.isSymbolicLink() || existing.size !== bytes.byteLength || await hashFile(stagedPath) !== sha256) throw new RuntimeError("FORBIDDEN", "Existing staged attachment does not match its immutable content identity", 403);
        });
      } finally { await unlink(temporaryPath).catch(() => undefined); }
      const historyPath = join(sessionDirectory, "history.jsonl");
      await revalidateStaging();
      const history = await open(historyPath, constants.O_CREAT | constants.O_APPEND | constants.O_WRONLY | (constants.O_NOFOLLOW ?? 0), 0o600).catch(() => undefined);
      if (!history) throw new RuntimeError("FORBIDDEN", "Attachment history path is unsafe", 403);
      try {
        if (!(await history.stat()).isFile()) throw new RuntimeError("FORBIDDEN", "Attachment history path is unsafe", 403);
        await history.appendFile(`${JSON.stringify({ stagedName, name: basename(sourcePath), sha256, bytes: bytes.byteLength, mimeType, recordedAt: new Date().toISOString() })}\n`, "utf8");
        await history.sync();
      } finally { await history.close(); }
      contentBlocks.push({ type: "file", path: stagedPath, mimeType, name: basename(sourcePath), sha256, bytes: bytes.byteLength });
    }
    return { contentBlocks, errors: [] };
  }
}
