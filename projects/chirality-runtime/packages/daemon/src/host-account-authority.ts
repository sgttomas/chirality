import { createHash, randomBytes, randomUUID, timingSafeEqual } from "node:crypto";
import { join } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import type { AccountRuntimePrincipal, AuthRegistry } from "@chirality/runtime-core";
import { atomicWriteJson, ensurePrivateDirectory, readJsonIfExists } from "@chirality/runtime-core";
import {
  HOST_ACCOUNT_CEREMONY_TIMEOUT_MS,
  HOST_ACCOUNT_MAX_MISSED_PINGS,
  HOST_ACCOUNT_PING_INTERVAL_MS,
  HOST_ACCOUNT_SCOPES,
  HOST_ACCOUNT_SILENCE_TIMEOUT_MS,
  createHostAccountCeremonyProof,
  createHostAccountRequestProof,
  hostAccountBodyDigest,
  parseHostAccountSigningPredicate,
  validHostAccountGeneration,
  verifyHostAccountProof,
  type HostAccountRequestDescriptor,
  type HostAccountSigningPredicate
} from "./host-account-protocol.js";

export type HostAccountRevocationReason =
  | "connection-invalidated"
  | "lease-expired"
  | "explicit-revocation"
  | "daemon-stop"
  | "host-replaced"
  | "ceremony-failed";

export interface HostAccountXpcServerPort {
  ping(connectionId: string, input: { requestId: string; sequence: bigint }): Promise<{ requestId: string; sequence: bigint }>;
  closeConnection(connectionId: string, reason: HostAccountRevocationReason): Promise<void>;
  close(): Promise<void>;
}

export interface HostAccountNativeAdmission {
  createHostXpcServer(input: {
    peerRequirement: string;
    expectedEuid: number;
    onCeremonyOpen(input: { connectionId: string; requestId: string }): Promise<{ requestId: string; challenge: Buffer; generation: string }>;
    onCeremonyFinish(input: { connectionId: string; requestId: string; hostNonce: Buffer; proof: Buffer }): Promise<{ requestId: string; bearer: Buffer; generation: string; scopes: typeof HOST_ACCOUNT_SCOPES }>;
    onInvalidated(input: { connectionId: string; reason: "invalidated" | "peer-rejected" | "closed" }): void;
  }): HostAccountXpcServerPort;
}

interface PendingCeremony {
  readonly requestId: string;
  readonly challenge: Buffer;
  readonly expiresAt: number;
  readonly timer: ReturnType<typeof setTimeout>;
}

interface ActiveHost {
  readonly connectionId: string;
  readonly clientId: string;
  readonly bearer: Buffer;
  readonly hostNonce: Buffer;
  lastCounter: number;
  lastSeenAt: number;
  pingSequence: bigint;
  missedPings: number;
  revoked: boolean;
  readonly operations: Set<AbortController>;
}

export interface HostAccountAdmissionLeaseSnapshot {
  readonly mechanismId: "host-p2-xpc-peer-requirement";
  readonly daemonGeneration: string;
  readonly authorityGeneration: string;
  readonly liveLeaseDigest: string;
}

interface HostAccountJournalPrincipal {
  clientId: string;
  connectionDigest: string;
  bearerDigest: string;
  hostNonceDigest: string;
  generation: string;
  scopes: readonly ["account:read", "account:control"];
  lastCounter: number;
  peerRequirementDigest: string;
  leaseState: "active" | "revoked";
  createdAt: string;
  revokedAt?: string;
  revocationReason?: HostAccountRevocationReason | "daemon-restart";
  cleanupState: "memory-active" | "memory-retired";
}

interface HostAccountJournal {
  schemaVersion: "chirality.host-account-journal/v1";
  currentGeneration: string;
  principals: HostAccountJournalPrincipal[];
}

export interface HostAccountAuthorityOptions {
  runtimeDirectory: string;
  auth: AuthRegistry;
  signingPredicate: HostAccountSigningPredicate;
  /** Derived from the running host process; never read from the packaged carrier. */
  expectedEuid: number;
  /** Production supplies only the capability returned by the accepted native loader. */
  nativeAdmission: HostAccountNativeAdmission;
  now?: () => number;
}

function digest(value: Buffer | string): string { return createHash("sha256").update(value).digest("hex"); }

function header(value: string | readonly string[] | undefined): string | undefined {
  return typeof value === "string" ? value : value?.[0];
}

export class HostAccountAuthority {
  private readonly journalFile: string;
  private readonly signingPredicate: HostAccountSigningPredicate;
  private readonly now: () => number;
  private generation?: string;
  private port?: HostAccountXpcServerPort;
  private active?: ActiveHost;
  private readonly pending = new Map<string, PendingCeremony>();
  private readonly invalidatedConnections = new Set<string>();
  private pingTimer?: ReturnType<typeof setInterval>;
  private startAttempted = false;
  private closing = false;
  private journalQueue: Promise<void> = Promise.resolve();
  private ceremonyQueue: Promise<void> = Promise.resolve();
  private requestQueue: Promise<void> = Promise.resolve();
  private invalidationQueue: Promise<void> = Promise.resolve();
  private pingInFlight = false;

  constructor(private readonly options: HostAccountAuthorityOptions) {
    this.journalFile = join(options.runtimeDirectory, "auth", "account-host.json");
    this.signingPredicate = parseHostAccountSigningPredicate(options.signingPredicate);
    if (!Number.isSafeInteger(options.expectedEuid) || options.expectedEuid < 0) throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account EUID is unavailable", 503);
    this.now = options.now ?? Date.now;
  }

  get daemonGeneration(): string | undefined { return this.generation; }

  /** Internal admission bridge: projects opaque lease identity, never bearer/nonce/connection ID. */
  snapshotAdmissionLease(): HostAccountAdmissionLeaseSnapshot {
    const active = this.active;
    const daemonGeneration = this.generation;
    if (this.closing || !active || active.revoked || !daemonGeneration) throw new RuntimeError("ENGINE_UNAVAILABLE", "Account host lease is unavailable", 503);
    return Object.freeze({
      mechanismId: "host-p2-xpc-peer-requirement",
      daemonGeneration,
      authorityGeneration: digest(active.clientId),
      liveLeaseDigest: digest(`${daemonGeneration}\0${active.clientId}\0${active.connectionId}`)
    });
  }

  /** Rechecks the same active connection generation without accepting a structural claim. */
  matchesAdmissionLease(snapshot: HostAccountAdmissionLeaseSnapshot): boolean {
    if (this.closing) return false;
    try {
      const current = this.snapshotAdmissionLease();
      return current.mechanismId === snapshot.mechanismId && current.daemonGeneration === snapshot.daemonGeneration
        && current.authorityGeneration === snapshot.authorityGeneration && current.liveLeaseDigest === snapshot.liveLeaseDigest;
    } catch { return false; }
  }

  async start(): Promise<void> {
    if (this.startAttempted) throw new Error("Host account authority requires a fresh lifecycle instance");
    this.startAttempted = true;
    await ensurePrivateDirectory(join(this.options.runtimeDirectory, "auth"));
    const generation = randomUUID();
    const previous = await this.readJournal(generation);
    const now = new Date().toISOString();
    const journal: HostAccountJournal = {
      schemaVersion: "chirality.host-account-journal/v1",
      currentGeneration: generation,
      principals: previous.principals.map((principal) => principal.leaseState === "revoked" ? principal : {
        ...principal,
        leaseState: "revoked",
        revokedAt: now,
        revocationReason: "daemon-restart",
        cleanupState: "memory-retired"
      })
    };
    await atomicWriteJson(this.journalFile, journal);
    this.options.auth.revokeAllMemoryAccountHosts();
    this.generation = generation;
    try {
      this.port = this.options.nativeAdmission.createHostXpcServer({
        peerRequirement: this.signingPredicate.peerRequirement,
        expectedEuid: this.options.expectedEuid,
        onCeremonyOpen: (input) => this.openCeremony(input),
        onCeremonyFinish: (input) => this.finishCeremony(input),
        onInvalidated: (input) => {
          this.beginInvalidation(input.connectionId);
          const operation = this.invalidationQueue.then(() => this.onInvalidated(input.connectionId));
          this.invalidationQueue = operation.catch(() => {});
        }
      });
      this.pingTimer = setInterval(() => { void this.pingLease().catch(() => undefined); }, HOST_ACCOUNT_PING_INTERVAL_MS);
      this.pingTimer.unref?.();
    } catch (error) {
      this.generation = undefined;
      throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account XPC listener is unavailable", 503, { cause: error });
    }
  }

  authorizeRequest(input: {
    authorization: string | readonly string[] | undefined;
    counter: string | readonly string[] | undefined;
    generation: string | readonly string[] | undefined;
    proof: string | readonly string[] | undefined;
    descriptor: HostAccountRequestDescriptor;
  }): Promise<AccountRuntimePrincipal> {
    const operation = this.requestQueue.then(() => this.completeAuthorization(input));
    this.requestQueue = operation.then(() => undefined, () => undefined);
    return operation;
  }

  async runAuthorizedRequest<T>(input: Parameters<HostAccountAuthority["authorizeRequest"]>[0], effect: (principal: AccountRuntimePrincipal, signal: AbortSignal) => Promise<T>): Promise<T> {
    const operation = this.requestQueue.then(async () => {
      const principal = await this.completeAuthorization(input);
      const active = this.active;
      if (this.closing || active === undefined || active.revoked || active.clientId !== principal.clientId) {
        throw new RuntimeError("ENGINE_UNAVAILABLE", "Account host authority was revoked before effect", 503);
      }
      const controller = new AbortController();
      active.operations.add(controller);
      try {
        const result = await effect(principal, controller.signal);
        if (controller.signal.aborted || this.active !== active || active.revoked || this.closing) throw new RuntimeError("ENGINE_UNAVAILABLE", "Account host authority was revoked during effect", 503);
        return result;
      } finally { active.operations.delete(controller); }
    });
    this.requestQueue = operation.then(() => undefined, () => undefined);
    return operation;
  }

  private async completeAuthorization(input: {
    authorization: string | readonly string[] | undefined;
    counter: string | readonly string[] | undefined;
    generation: string | readonly string[] | undefined;
    proof: string | readonly string[] | undefined;
    descriptor: HostAccountRequestDescriptor;
  }): Promise<AccountRuntimePrincipal> {
    const generation = header(input.generation);
    const counterText = header(input.counter);
    const proof = header(input.proof);
    const active = this.active;
    if (this.closing || active === undefined || active.revoked || generation === undefined || generation !== this.generation
      || !validHostAccountGeneration(generation) || counterText === undefined || !/^[1-9][0-9]{0,15}$/u.test(counterText)
      || proof === undefined) throw new RuntimeError("UNAUTHORIZED", "Invalid account host request proof", 401);
    const counter = Number(counterText);
    if (!Number.isSafeInteger(counter) || counter <= active.lastCounter) throw new RuntimeError("UNAUTHORIZED", "Replayed account host request", 401);
    const principal = this.options.auth.authenticateMemoryAccountHost(header(input.authorization), input.descriptor.requiredScope, generation);
    const expected = createHostAccountRequestProof(active.hostNonce, {
      method: input.descriptor.method,
      route: input.descriptor.route,
      canonicalBodyDigest: hostAccountBodyDigest(input.descriptor.canonicalBody),
      counter,
      generation
    });
    if (!verifyHostAccountProof(expected, proof)) throw new RuntimeError("UNAUTHORIZED", "Invalid account host request proof", 401);
    active.lastCounter = counter;
    active.lastSeenAt = this.now();
    try { await this.updateJournal(active.clientId, (record) => ({ ...record, lastCounter: counter })); }
    catch (error) {
      active.revoked = true;
      this.options.auth.revokeMemoryAccountHost(active.clientId);
      active.bearer.fill(0); active.hostNonce.fill(0);
      if (this.active === active) this.active = undefined;
      await this.port?.closeConnection(active.connectionId, "lease-expired").catch(() => undefined);
      throw error;
    }
    if (this.active !== active || active.revoked || this.closing) throw new RuntimeError("ENGINE_UNAVAILABLE", "Account host authority was revoked", 503);
    return principal;
  }

  async revoke(reason: HostAccountRevocationReason = "explicit-revocation"): Promise<void> {
    const active = this.active;
    if (active !== undefined) await this.revokeActive(active, reason, true);
  }

  async close(): Promise<void> {
    if (this.closing) return;
    this.closing = true;
    if (this.pingTimer !== undefined) clearInterval(this.pingTimer);
    for (const ceremony of this.pending.values()) { clearTimeout(ceremony.timer); ceremony.challenge.fill(0); }
    this.pending.clear();
    await this.ceremonyQueue;
    await this.invalidationQueue;
    const active = this.active;
    if (active !== undefined) await this.revokeActive(active, "daemon-stop", false);
    await this.port?.close();
    this.port = undefined;
    this.generation = undefined;
  }

  private async openCeremony(input: { connectionId: string; requestId: string }): Promise<{ requestId: string; challenge: Buffer; generation: string }> {
    const generation = this.generation;
    if (this.closing || this.port === undefined || generation === undefined || this.invalidatedConnections.has(input.connectionId) || !/^[A-Za-z0-9._:-]{1,96}$/u.test(input.connectionId)
      || !/^[A-Za-z0-9._:-]{1,96}$/u.test(input.requestId) || this.pending.has(input.connectionId)) {
      throw new RuntimeError("UNAUTHORIZED", "Host account ceremony is unavailable", 401);
    }
    const challenge = randomBytes(32);
    const timer = setTimeout(() => {
      const pending = this.pending.get(input.connectionId);
      if (pending?.requestId !== input.requestId) return;
      this.pending.delete(input.connectionId);
      pending.challenge.fill(0);
      void this.port?.closeConnection(input.connectionId, "ceremony-failed").catch(() => undefined);
    }, HOST_ACCOUNT_CEREMONY_TIMEOUT_MS);
    timer.unref?.();
    this.pending.set(input.connectionId, { requestId: input.requestId, challenge, expiresAt: this.now() + HOST_ACCOUNT_CEREMONY_TIMEOUT_MS, timer });
    return { requestId: input.requestId, challenge: Buffer.from(challenge), generation };
  }

  private finishCeremony(input: { connectionId: string; requestId: string; hostNonce: Buffer; proof: Buffer }): Promise<{ requestId: string; bearer: Buffer; generation: string; scopes: typeof HOST_ACCOUNT_SCOPES }> {
    const operation = this.ceremonyQueue.then(() => this.completeCeremony(input));
    this.ceremonyQueue = operation.then(() => undefined, () => undefined);
    return operation;
  }

  private async completeCeremony(input: { connectionId: string; requestId: string; hostNonce: Buffer; proof: Buffer }): Promise<{ requestId: string; bearer: Buffer; generation: string; scopes: typeof HOST_ACCOUNT_SCOPES }> {
    const pending = this.pending.get(input.connectionId);
    const generation = this.generation;
    this.pending.delete(input.connectionId);
    if (pending !== undefined) clearTimeout(pending.timer);
    try {
      if (this.closing || this.invalidatedConnections.has(input.connectionId) || pending === undefined || pending.requestId !== input.requestId || pending.expiresAt < this.now()
        || generation === undefined || input.hostNonce.length !== 32 || input.proof.length !== 32) {
        throw new RuntimeError("UNAUTHORIZED", "Host account ceremony failed", 401);
      }
      const expected = createHostAccountCeremonyProof(input.hostNonce, pending.challenge, generation);
      if (!timingSafeEqual(expected, input.proof)) throw new RuntimeError("UNAUTHORIZED", "Host account ceremony failed", 401);
      const old = this.active;
      if (old !== undefined) await this.revokeActive(old, "host-replaced", true);
      const bearer = randomBytes(32);
      const hostNonce = Buffer.from(input.hostNonce);
      const clientId = `app-account-host:${randomUUID()}`;
      const active: ActiveHost = {
        connectionId: input.connectionId, clientId, bearer, hostNonce,
        lastCounter: 0, lastSeenAt: this.now(), pingSequence: 0n, missedPings: 0, revoked: false, operations: new Set()
      };
      this.options.auth.registerMemoryAccountHost({ clientId, bearer: bearer.toString("base64url"), generation, scopes: HOST_ACCOUNT_SCOPES });
      try {
        await this.appendPrincipal({
          clientId,
          connectionDigest: digest(input.connectionId),
          bearerDigest: digest(bearer),
          hostNonceDigest: digest(hostNonce),
          generation,
          scopes: HOST_ACCOUNT_SCOPES,
          lastCounter: 0,
          peerRequirementDigest: digest(this.signingPredicate.peerRequirement),
          leaseState: "active",
          createdAt: new Date().toISOString(),
          cleanupState: "memory-active"
        });
        if (this.closing || this.invalidatedConnections.has(input.connectionId)) {
          this.options.auth.revokeMemoryAccountHost(clientId);
          await this.updateJournal(clientId, (record) => ({ ...record, leaseState: "revoked", revokedAt: new Date().toISOString(), revocationReason: "connection-invalidated", cleanupState: "memory-retired" }));
          bearer.fill(0); hostNonce.fill(0);
          throw new RuntimeError("ENGINE_UNAVAILABLE", "Account host connection was invalidated", 503);
        }
      } catch (error) {
        this.options.auth.revokeMemoryAccountHost(clientId);
        bearer.fill(0); hostNonce.fill(0);
        throw error;
      }
      this.active = active;
      return { requestId: input.requestId, bearer: Buffer.from(bearer), generation, scopes: HOST_ACCOUNT_SCOPES };
    } finally { pending?.challenge.fill(0); }
  }

  private async onInvalidated(connectionId: string): Promise<void> {
    this.beginInvalidation(connectionId);
    const active = this.active;
    if (active?.connectionId === connectionId) await this.revokeActive(active, "connection-invalidated", false);
  }

  private beginInvalidation(connectionId: string): void {
    this.invalidatedConnections.add(connectionId);
    const pending = this.pending.get(connectionId);
    if (pending !== undefined) { clearTimeout(pending.timer); pending.challenge.fill(0); this.pending.delete(connectionId); }
    const active = this.active;
    if (active?.connectionId === connectionId) for (const operation of active.operations) operation.abort();
  }

  private async pingLease(): Promise<void> {
    const active = this.active;
    const port = this.port;
    if (this.closing || active === undefined || active.revoked || port === undefined || this.pingInFlight) return;
    this.pingInFlight = true;
    const sequence = ++active.pingSequence;
    const requestId = `ping:${sequence}`;
    try {
      let timer: ReturnType<typeof setTimeout> | undefined;
      const pong = await Promise.race([
        port.ping(active.connectionId, { requestId, sequence }),
        new Promise<never>((_, reject) => { timer = setTimeout(() => reject(new Error("ping-timeout")), HOST_ACCOUNT_PING_INTERVAL_MS); })
      ]).finally(() => clearTimeout(timer));
      if (pong.requestId !== requestId || pong.sequence !== sequence) throw new Error("invalid-pong");
      if (this.active !== active || active.revoked) return;
      active.missedPings = 0;
      active.lastSeenAt = this.now();
    } catch {
      if (this.active !== active || active.revoked) return;
      active.missedPings += 1;
      if (active.missedPings >= HOST_ACCOUNT_MAX_MISSED_PINGS || this.now() - active.lastSeenAt >= HOST_ACCOUNT_SILENCE_TIMEOUT_MS) {
        await this.revokeActive(active, "lease-expired", true);
      }
    } finally { this.pingInFlight = false; }
  }

  private async revokeActive(active: ActiveHost, reason: HostAccountRevocationReason, closeConnection: boolean): Promise<void> {
    if (active.revoked) return;
    active.revoked = true;
    for (const operation of active.operations) operation.abort();
    active.operations.clear();
    this.options.auth.revokeMemoryAccountHost(active.clientId);
    if (this.active === active) this.active = undefined;
    active.bearer.fill(0);
    active.hostNonce.fill(0);
    let failure: unknown;
    try {
      await this.updateJournal(active.clientId, (record) => ({
        ...record,
        leaseState: "revoked",
        revokedAt: new Date().toISOString(),
        revocationReason: reason,
        cleanupState: "memory-retired"
      }));
    } catch (error) { failure = error; }
    if (closeConnection) {
      try { await this.port?.closeConnection(active.connectionId, reason); }
      catch (error) { failure ??= error; }
    }
    if (failure !== undefined) throw failure;
  }

  private appendPrincipal(principal: HostAccountJournalPrincipal): Promise<void> {
    return this.mutateJournal((journal) => ({ ...journal, principals: [...journal.principals, principal].slice(-256) }));
  }

  private updateJournal(clientId: string, update: (record: HostAccountJournalPrincipal) => HostAccountJournalPrincipal): Promise<void> {
    return this.mutateJournal((journal) => ({ ...journal, principals: journal.principals.map((record) => record.clientId === clientId ? update(record) : record) }));
  }

  private mutateJournal(update: (journal: HostAccountJournal) => HostAccountJournal): Promise<void> {
    const generation = this.generation;
    if (generation === undefined) return Promise.reject(new RuntimeError("ENGINE_UNAVAILABLE", "Host account generation is unavailable", 503));
    const operation = this.journalQueue.then(async () => {
      const journal = await this.readJournal(generation);
      if (journal.currentGeneration !== generation) throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account generation changed", 503);
      await atomicWriteJson(this.journalFile, update(journal));
    });
    this.journalQueue = operation.catch(() => undefined);
    return operation;
  }

  private async readJournal(fallbackGeneration: string): Promise<HostAccountJournal> {
    const value = await readJsonIfExists<HostAccountJournal>(this.journalFile, {
      schemaVersion: "chirality.host-account-journal/v1", currentGeneration: fallbackGeneration, principals: []
    });
    if (value.schemaVersion !== "chirality.host-account-journal/v1" || !Array.isArray(value.principals)) {
      throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account journal is invalid", 503);
    }
    return value;
  }
}
