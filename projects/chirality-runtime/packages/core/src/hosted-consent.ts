import { constants } from "node:fs";
import { link, lstat, mkdir, open, realpath, rename, unlink } from "node:fs/promises";
import { createHash, randomUUID } from "node:crypto";
import { homedir } from "node:os";
import { dirname, isAbsolute, join, parse, relative, resolve, sep } from "node:path";
import { RuntimeError, type DestinationApproval, type HostedConsent, type HostedEngineConsentPort, type WorkerContinuity } from "@chirality/runtime-contracts";

const forbidden = (message: string) => new RuntimeError("FORBIDDEN", message, 403);
export function recordKey(value: unknown): string {
  return createHash("sha256").update(JSON.stringify(value)).digest("hex");
}
export function continuityFields(value: WorkerContinuity): readonly unknown[] {
  return [value.canonicalRoot, value.accountId, value.accountEpoch, value.policyDigest, value.cwd];
}
export function sameContinuity(a: WorkerContinuity, b: WorkerContinuity): boolean {
  return JSON.stringify(continuityFields(a)) === JSON.stringify(continuityFields(b));
}
export function validContinuity(value: WorkerContinuity): boolean {
  return Boolean(value && typeof value.canonicalRoot === "string" && isAbsolute(value.canonicalRoot)
    && resolve(value.canonicalRoot) === value.canonicalRoot && value.cwd === value.canonicalRoot
    && typeof value.accountId === "string" && value.accountId.trim()
    && Number.isSafeInteger(value.accountEpoch) && value.accountEpoch >= 0
    && typeof value.policyDigest === "string" && value.policyDigest.trim());
}
export async function assertContinuity(value: WorkerContinuity): Promise<void> {
  if (!validContinuity(value)) throw forbidden("Invalid root/account/epoch/policy/cwd continuity");
  try {
    if (await realpath(value.canonicalRoot) !== value.canonicalRoot || !(await lstat(value.canonicalRoot)).isDirectory()) {
      throw forbidden("Root must be the canonical directory and cwd must equal it");
    }
  } catch (error) {
    if (error instanceof RuntimeError) throw error;
    throw forbidden("Canonical root is unavailable");
  }
}

/** Private app-owned directories; reject aliases before writing or chmodding anything. */
export async function privateDirectory(directory: string): Promise<void> {
  if (!isAbsolute(directory) || resolve(directory) !== directory) throw forbidden("Private directory must be canonical and absolute");
  let current = parse(directory).root;
  for (const segment of directory.slice(current.length).split(sep).filter(Boolean)) {
    current = join(current, segment);
    try { await mkdir(current, { mode: 0o700 }); } catch (error) {
      if ((error as NodeJS.ErrnoException).code !== "EEXIST") throw forbidden("Cannot create private storage");
    }
    const info = await lstat(current);
    if (!info.isDirectory() || info.isSymbolicLink()) throw forbidden("Private storage cannot traverse symlinks");
  }
  const info = await lstat(directory);
  if ((info.mode & 0o077) !== 0 || (process.getuid && info.uid !== process.getuid())) throw forbidden("Storage must be owner-private (0700)");
}
export async function syncDirectory(directory: string): Promise<void> {
  const handle = await open(directory, constants.O_RDONLY | constants.O_NOFOLLOW);
  try { await handle.sync(); } finally { await handle.close(); }
}
export async function privateRead<T>(file: string): Promise<T | undefined> {
  let handle;
  try {
    handle = await open(file, constants.O_RDONLY | constants.O_NOFOLLOW);
    const info = await handle.stat();
    if (!info.isFile() || (info.mode & 0o077) !== 0 || (process.getuid && info.uid !== process.getuid())) throw forbidden("Record must be an owner-private regular file");
    return JSON.parse(await handle.readFile("utf8")) as T;
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") return undefined;
    if (error instanceof RuntimeError) throw error;
    throw new RuntimeError("INTERNAL_FAILURE", "Private record is unreadable or malformed", 500);
  } finally { await handle?.close(); }
}
/** fsync bytes before publication, then directory. Exclusive link is cross-process CAS. */
export async function publishPrivate(file: string, value: unknown, exclusive: boolean): Promise<boolean> {
  await privateDirectory(dirname(file));
  const temp = `${file}.${randomUUID()}.tmp`;
  const handle = await open(temp, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600);
  try { await handle.writeFile(`${JSON.stringify(value)}\n`); await handle.sync(); } finally { await handle.close(); }
  try {
    if (exclusive) {
      try { await link(temp, file); } catch (error) {
        if ((error as NodeJS.ErrnoException).code === "EEXIST") {
          // Another publisher may not yet have synced the directory.
          await syncDirectory(dirname(file));
          return false;
        }
        throw error;
      }
    } else {
      // Refuse a pre-existing malicious alias even though rename itself does not follow it.
      await privateRead(file);
      await rename(temp, file);
    }
    await syncDirectory(dirname(file));
    return true;
  } finally { await unlink(temp).catch(error => { if (error.code !== "ENOENT") throw error; }); }
}

export class HostedConsentStore implements HostedEngineConsentPort {
  readonly canonicalRoot: string;
  readonly codexHome: string;
  constructor(options: { canonicalRoot: string; codexHome: string }) {
    this.canonicalRoot = options.canonicalRoot;
    this.codexHome = options.codexHome;
  }
  private async ready(identity: WorkerContinuity): Promise<void> {
    await assertContinuity(identity);
    if (identity.canonicalRoot !== this.canonicalRoot) throw forbidden("Consent cannot cross canonical roots");
    const ambient = resolve(homedir(), ".codex");
    const rel = relative(ambient, this.codexHome);
    if (rel === "" || (!rel.startsWith(`..${sep}`) && rel !== ".." && !isAbsolute(rel))) throw forbidden("Ambient ~/.codex is excluded");
    await privateDirectory(this.codexHome);
    const binding = join(this.codexHome, "chirality-root.json");
    await publishPrivate(binding, { canonicalRoot: this.canonicalRoot }, true);
    if ((await privateRead<{ canonicalRoot: string }>(binding))?.canonicalRoot !== this.canonicalRoot) throw forbidden("CODEX_HOME is already bound to another root");
  }
  async read(identity: WorkerContinuity): Promise<HostedConsent | undefined> {
    await this.ready(identity);
    const consent = await privateRead<HostedConsent>(join(this.codexHome, "chirality-consent.json"));
    if (!consent) return undefined;
    this.validate(consent);
    return sameContinuity(consent.identity, identity) ? consent : undefined;
  }
  private validate(consent: HostedConsent): void {
    if (!consent || !validContinuity(consent.identity) || !["off", "ask-per-destination", "on"].includes(consent.posture)
      || typeof consent.approvedBy !== "string" || !consent.approvedBy.trim()
      || typeof consent.approvedAt !== "string" || !Number.isFinite(Date.parse(consent.approvedAt))) throw new RuntimeError("INVALID_REQUEST", "Invalid explicit consent record");
  }
  async grant(consent: HostedConsent): Promise<void> {
    this.validate(consent);
    await this.ready(consent.identity);
    await publishPrivate(join(this.codexHome, "chirality-consent.json"), consent, false);
  }
  destinationPrompt(approval: Pick<DestinationApproval, "host" | "protocol">): { host: string; protocol: string; caveat: string } {
    if (!approval || typeof approval.host !== "string" || !/^[A-Za-z0-9.:[\]-]+$/.test(approval.host)
      || typeof approval.protocol !== "string" || !/^[a-z][a-z0-9+.-]*$/.test(approval.protocol)) throw new RuntimeError("INVALID_REQUEST", "Destination requires host and protocol");
    return { host: approval.host, protocol: approval.protocol, caveat: "A grant may unblock queued requests to the same destination. acceptForSession requires an explicit user act." };
  }
  async authorizeDestination(identity: WorkerContinuity, approval: DestinationApproval): Promise<void> {
    const prompt = this.destinationPrompt(approval);
    const consent = await this.read(identity);
    if (!consent || consent.posture !== "ask-per-destination") throw forbidden("Destination approval requires ask-per-destination consent");
    if (approval.explicitUserAct !== true || typeof approval.acceptForSession !== "boolean" || typeof approval.approvedBy !== "string" || !approval.approvedBy.trim()) throw forbidden("Destination approval requires an explicit user act");
    // Evidence only, not an automatic replay or a claim of vendor prompt delivery.
    await publishPrivate(join(this.codexHome, `destination-${randomUUID()}.json`), { identity, consentDigest: recordKey(consent), approval, prompt }, true);
  }
  async configuration(identity: WorkerContinuity): Promise<{ posture: HostedConsent["posture"]; network_access: boolean; label: string; env: { CODEX_HOME: string } }> {
    const posture = (await this.read(identity))?.posture ?? "off";
    return { posture, network_access: posture === "on", label: posture === "on" ? "Command network on" : posture === "off" ? "Command network off (default)" : "Ask per destination", env: { CODEX_HOME: this.codexHome } };
  }
}
