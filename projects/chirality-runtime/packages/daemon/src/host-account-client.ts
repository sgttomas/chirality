import { randomBytes, randomUUID } from "node:crypto";
import { request as httpRequest } from "node:http";
import {
  RuntimeError,
  validateHostedBootstrapStatus,
  type HostedBootstrapLoginStartResponse,
  type HostedBootstrapStatus
} from "@chirality/runtime-contracts";
import {
  HOST_ACCOUNT_NONCE_BYTES,
  HOST_ACCOUNT_SCOPES,
  createHostAccountCeremonyProof,
  createHostAccountRequestProof,
  hostAccountBodyDigest,
  hostAccountRequest,
  parseHostAccountSigningPredicate,
  type HostAccountOperation,
  type HostAccountProofHeaders,
  type HostAccountSigningPredicate
} from "./host-account-protocol.js";

export interface HostAccountXpcClientPort {
  provision(input: {
    requestId: string;
    onChallenge(input: { requestId: string; challenge: Buffer; generation: string }): Promise<{ requestId: string; hostNonce: Buffer; proof: Buffer }>;
  }): Promise<{ requestId: string; bearer: Buffer; generation: string; scopes: typeof HOST_ACCOUNT_SCOPES }>;
  close(): Promise<void>;
}

export interface HostAccountClientNativeAdmission {
  createHostXpcClient(input: {
    peerRequirement: string;
    expectedEuid: number;
    onPing(input: { requestId: string; sequence: bigint }): Promise<{ requestId: string; sequence: bigint }>;
    onInvalidated(input: { reason: "invalidated" | "peer-rejected" | "closed" }): void;
  }): HostAccountXpcClientPort;
}

export interface HostAccountClientOptions {
  socketPath: string;
  signingPredicate: HostAccountSigningPredicate;
  /** Derived from the running Electron main process; never read from the packaged carrier. */
  expectedEuid: number;
  /** Production supplies only the capability returned by the accepted native loader. */
  nativeAdmission: HostAccountClientNativeAdmission;
}

interface ClientAuthority {
  bearer: Buffer;
  hostNonce: Buffer;
  generation: string;
  counter: number;
}

export interface HostAccountClient {
  start(): Promise<void>;
  close(): Promise<void>;
  status(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus>;
  grantProviderNetworkConsent(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus>;
  startLogin(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapLoginStartResponse>;
  cancelLogin(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus>;
  signOut(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus>;
}

export class MainHostAccountClient implements HostAccountClient {
  private readonly predicate: HostAccountSigningPredicate;
  private port?: HostAccountXpcClientPort;
  private authority?: ClientAuthority;
  private startAttempted = false;
  private closed = false;
  private invalidated = false;
  private operationQueue: Promise<void> = Promise.resolve();
  private readonly activeRequests = new Set<AbortController>();

  constructor(private readonly options: HostAccountClientOptions) {
    this.predicate = parseHostAccountSigningPredicate(options.signingPredicate);
    if (!options.socketPath.startsWith("/")) throw new RuntimeError("ENGINE_UNAVAILABLE", "Runtime socket path is unavailable", 503);
    if (!Number.isSafeInteger(options.expectedEuid) || options.expectedEuid < 0) throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account EUID is unavailable", 503);
  }

  async start(): Promise<void> {
    if (this.startAttempted) throw new RuntimeError("ENGINE_UNAVAILABLE", "A fresh account host client is required", 503);
    this.startAttempted = true;
    const port = this.options.nativeAdmission.createHostXpcClient({
      peerRequirement: this.predicate.peerRequirement,
      expectedEuid: this.options.expectedEuid,
      onPing: async (input) => {
        if (this.closed || this.authority === undefined) throw new RuntimeError("ENGINE_UNAVAILABLE", "Account host lease is unavailable", 503);
        return { requestId: input.requestId, sequence: input.sequence };
      },
      onInvalidated: () => { this.invalidated = true; this.retire(); }
    });
    this.port = port;
    let pendingNonce: Buffer | undefined;
    let pendingGeneration: string | undefined;
    let returnedBearer: Buffer | undefined;
    const requestId = `provision:${randomUUID()}`;
    try {
      const grant = await port.provision({
        requestId,
        onChallenge: async (challenge) => {
          if (this.invalidated || this.closed || this.port !== port || challenge.requestId !== requestId || challenge.challenge.length !== 32) throw new RuntimeError("UNAUTHORIZED", "Invalid account host challenge", 401);
          pendingNonce = randomBytes(HOST_ACCOUNT_NONCE_BYTES);
          pendingGeneration = challenge.generation;
          return {
            requestId,
            hostNonce: Buffer.from(pendingNonce),
            proof: createHostAccountCeremonyProof(pendingNonce, challenge.challenge, challenge.generation)
          };
        }
      });
      returnedBearer = grant.bearer;
      if (this.invalidated || this.closed || this.port !== port || grant.requestId !== requestId || grant.bearer.length !== 32 || pendingNonce === undefined
        || pendingGeneration === undefined || grant.generation !== pendingGeneration
        || grant.scopes.length !== 2 || grant.scopes[0] !== "account:read" || grant.scopes[1] !== "account:control") {
        throw new RuntimeError("UNAUTHORIZED", "Invalid account host grant", 401);
      }
      this.authority = { bearer: Buffer.from(grant.bearer), hostNonce: pendingNonce, generation: grant.generation, counter: 0 };
      grant.bearer.fill(0);
      returnedBearer = undefined;
      pendingNonce = undefined;
    } catch (error) {
      pendingNonce?.fill(0);
      returnedBearer?.fill(0);
      await port.close().catch(() => undefined);
      this.port = undefined;
      throw error;
    }
  }

  status(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus> {
    return this.request("status", projectId, signal).then(validateHostedBootstrapStatus);
  }

  grantProviderNetworkConsent(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus> {
    return this.request("grant-provider-network-consent", projectId, signal).then(validateHostedBootstrapStatus);
  }

  async startLogin(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapLoginStartResponse> {
    const value = await this.request("start-login", projectId, signal);
    if (value === null || typeof value !== "object" || Array.isArray(value)
      || Object.keys(value).sort().join(",") !== "authUrl,loginId"
      || typeof (value as Record<string, unknown>).loginId !== "string"
      || typeof (value as Record<string, unknown>).authUrl !== "string") {
      throw new RuntimeError("INTERNAL_FAILURE", "Invalid hosted login response", 500);
    }
    return value as HostedBootstrapLoginStartResponse;
  }

  cancelLogin(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus> {
    return this.request("cancel-login", projectId, signal).then(validateHostedBootstrapStatus);
  }

  signOut(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus> {
    return this.request("sign-out", projectId, signal).then(validateHostedBootstrapStatus);
  }

  async close(): Promise<void> {
    if (this.closed) return;
    this.closed = true;
    this.retire();
    await this.port?.close();
    this.port = undefined;
  }

  private signAccountRequest(operation: HostAccountOperation, projectId: string): {
    descriptor: ReturnType<typeof hostAccountRequest>;
    headers: HostAccountProofHeaders;
    authority: ClientAuthority;
  } {
    const authority = this.authority;
    if (this.closed || authority === undefined) throw new RuntimeError("ENGINE_UNAVAILABLE", "Account host client is unavailable", 503);
    const descriptor = hostAccountRequest(operation, projectId);
    const counter = ++authority.counter;
    const proof = createHostAccountRequestProof(authority.hostNonce, {
      method: descriptor.method,
      route: descriptor.route,
      canonicalBodyDigest: hostAccountBodyDigest(descriptor.canonicalBody),
      counter,
      generation: authority.generation
    });
    return {
      descriptor,
      authority,
      headers: {
        authorization: `Bearer ${authority.bearer.toString("base64url")}`,
        ...(descriptor.method === "POST" ? { "content-type": "application/json" as const } : {}),
        "x-chirality-account-counter": String(counter),
        "x-chirality-account-generation": authority.generation,
        "x-chirality-account-proof": proof
      }
    };
  }

  private request(operation: HostAccountOperation, projectId: string, signal?: AbortSignal): Promise<unknown> {
    const pending = this.operationQueue.then(() => this.performRequest(operation, projectId, signal));
    this.operationQueue = pending.then(() => undefined, () => undefined);
    return pending;
  }

  private performRequest(operation: HostAccountOperation, projectId: string, signal?: AbortSignal): Promise<unknown> {
    const signed = this.signAccountRequest(operation, projectId);
    const controller = new AbortController();
    this.activeRequests.add(controller);
    const abort = () => controller.abort(signal?.reason);
    if (signal?.aborted) abort(); else signal?.addEventListener("abort", abort, { once: true });
    return new Promise((resolve, reject) => {
      const request = httpRequest({
        socketPath: this.options.socketPath,
        path: signed.descriptor.route,
        method: signed.descriptor.method,
        headers: { ...signed.headers },
        signal: controller.signal
      }, (response) => {
        const chunks: Buffer[] = [];
        let size = 0;
        response.on("data", (chunk: Buffer) => {
          size += chunk.length;
          if (size > 1024 * 1024) response.destroy(new Error("Account response exceeds limit"));
          else chunks.push(chunk);
        });
        response.on("end", () => {
          try {
            const value = JSON.parse(Buffer.concat(chunks).toString("utf8")) as unknown;
            if ((response.statusCode ?? 500) >= 400) throw new RuntimeError("ENGINE_UNAVAILABLE", "Account operation was rejected", response.statusCode ?? 503);
            if (controller.signal.aborted || this.closed || this.invalidated || this.authority !== signed.authority) throw new RuntimeError("ENGINE_UNAVAILABLE", "Account host authority was revoked during request", 503);
            resolve(value);
          } catch (error) { reject(error); }
        });
        response.on("error", reject);
      });
      request.on("error", reject);
      if (signed.descriptor.canonicalBody !== "") request.write(signed.descriptor.canonicalBody, "utf8");
      request.end();
    }).finally(() => { signal?.removeEventListener("abort", abort); this.activeRequests.delete(controller); });
  }

  private retire(): void {
    for (const request of this.activeRequests) request.abort();
    this.activeRequests.clear();
    const authority = this.authority;
    this.authority = undefined;
    authority?.bearer.fill(0);
    authority?.hostNonce.fill(0);
  }
}

export function createHostAccountClient(options: HostAccountClientOptions): HostAccountClient {
  return new MainHostAccountClient(options);
}
