import { assertNoPrivateAuthoritySurface } from "./supervisor-server.js";
import type { SupplierAuthorityLifecycle } from "./supplier-authority-journal.js";
import type { RuntimeApprovalControlPort } from "@chirality/runtime-core";
import { randomUUID } from "node:crypto";
import { chmod, lstat, readFile, unlink } from "node:fs/promises";
import { createServer, type IncomingMessage, type Server, type ServerResponse } from "node:http";
import type { Socket } from "node:net";
import { dirname } from "node:path";
import { performance } from "node:perf_hooks";
import {
  HarnessError,
  RUNTIME_API_VERSION,
  RuntimeError,
  validateHostedLoginStatus,
  validateHostedBootstrapStatus,
  deriveTranscriptView,
  type Agent1RunRequest,
  type CreateSessionRequest,
  type CredentialMutationRequest,
  type DaemonStatusResponse,
  type HealthResponse,
  type HostedLoginStatus,
  type HostedBootstrapStatus,
  type HostedProviderNetworkConsentRequest,
  type HostedBootstrapProjectRegistrationRequest,
  type HostedBootstrapProjectInitializationRequest,
  type HostedBootstrapProjectRegistrationResponse,
  type PermissionDecisionRequest,
  type ProjectRegistrationRequest,
  type RuntimeErrorBody,
  type ScaffoldRequest,
  type RuntimeSessionBootRequest,
  type SessionTurnRequest,
  type ResolveSelectedContextRequest,
  type ReplaceSelectedMethodsRequest,
  type ExportNativePlanRequest,
  type ReplyNativePlanClarificationRequest,
  type UIEvent
} from "@chirality/runtime-contracts";
import {
  ensurePrivateDirectory,
  atomicWriteJson,
  type AuthRegistry,
  type RuntimeScope,
  type RuntimeService,
  type DelegatedRuntime
  , ensureHostedProjectManifest
} from "@chirality/runtime-core";
import { hostedProjectClientId } from "./hosted-paths.js";
import { hostAccountRequest, type HostAccountOperation } from "./host-account-protocol.js";
import type { HostAccountAuthority } from "./host-account-authority.js";

const JSON_LIMIT_BYTES = 1024 * 1024;
const STOP_GRACE_MS = 2_000;
const STOP_FORCE_SETTLE_MS = 500;

/** Optional host-supplied diagnostic sink; the default discards every event. Fields never carry auth URLs, bearers, proofs, counters, or other secrets. */
export interface RuntimeDaemonLogger {
  warn(event: string, fields?: Readonly<Record<string, unknown>>): void;
  error(event: string, fields?: Readonly<Record<string, unknown>>): void;
}
export const NOOP_RUNTIME_DAEMON_LOGGER: RuntimeDaemonLogger = Object.freeze({ warn() {}, error() {} });
/** Bounded, control-character-free projection of an error message for diagnostics. */
export function safeDiagnosticText(value: unknown, limit = 200): string {
  const text = value instanceof Error ? value.message : typeof value === "string" ? value : String(value ?? "");
  return text.replace(/[\x00-\x1f\x7f]/g, " ").slice(0, limit);
}
/** Code, status, reason and bounded messages only; details are never copied wholesale. */
export function describeRuntimeFailure(error: unknown): Readonly<Record<string, unknown>> {
  const fields: Record<string, unknown> = error instanceof RuntimeError
    ? { code: error.code, status: error.status, ...(typeof error.details?.reason === "string" ? { reason: safeDiagnosticText(error.details.reason, 64) } : {}), message: safeDiagnosticText(error) }
    : { code: "UNEXPECTED", status: 500, message: safeDiagnosticText(error) };
  if (error instanceof AggregateError) fields.causes = error.errors.slice(0, 5).map(cause => safeDiagnosticText(cause));
  else if (error instanceof Error && error.cause !== undefined) fields.cause = safeDiagnosticText(error.cause);
  return fields;
}

type DaemonLifecycle =
  | "INITIAL"
  | "STARTING"
  | "RUNNING"
  | "STOPPING"
  | "STOPPED"
  | "STOPPED_DEGRADED"
  | "STOP_FAILED_CLEANUP";

interface ActiveSse {
  readonly generation: DaemonGeneration;
  readonly interrupt: () => Promise<void> | undefined;
  iterator?: AsyncIterator<UIEvent>;
  cancellationRequested: boolean;
  interruptionStarted: boolean;
  interruptionSettled: boolean;
  interruptionFailure?: unknown;
  interruptionTimedOut: boolean;
  identityUnavailable: boolean;
  forceExpired: boolean;
  iteratorReturnRequested: boolean;
  iteratorReturnFailure?: unknown;
}

interface DaemonGeneration {
  readonly number: number;
  readonly ownerGenerationId: string;
  readonly server: Server;
  readonly sockets: Set<Socket>;
  readonly streams: Set<ActiveSse>;
  readonly stateWaiters: Set<() => void>;
  closeStarted: boolean;
  closeComplete: boolean;
  closeError?: unknown;
  forced: boolean;
  socketUnlinked: boolean;
  ownerRemoved: boolean;
  stopStreams?: ActiveSse[];
  interruptionProblems: boolean;
}

export interface RuntimeDaemonOptions {
  supplierAuthority?:SupplierAuthorityLifecycle;
  accountHost?: HostAccountAuthority;
  socketPath: string;
  runtimeDirectory: string;
  service: RuntimeService;
  delegated?: DelegatedRuntime;
  approvals?: RuntimeApprovalControlPort;
  loginProjectId?: string;
  login?: { startLogin(): Promise<{ loginId: string; authUrl: string }>; status(): Promise<HostedLoginStatus>; cancel(): Promise<void> };
  hostedBootstrap?: {
    /** Each operation revalidates project registration/root/drift and retires stale admission. */
    status(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus>;
    grantProviderNetworkConsent(projectId: string, provenance: { approvedBy: string; approvalReference: string; approvedAt: string }, signal?: AbortSignal): Promise<HostedBootstrapStatus>;
    startLogin(projectId: string, signal?: AbortSignal): Promise<{ loginId: string; authUrl: string }>;
    cancelLogin(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus>;
    signOut(projectId: string, signal?: AbortSignal): Promise<HostedBootstrapStatus>;
  };
  logger?: RuntimeDaemonLogger;
}

export class RuntimeDaemon {
  readonly daemonId = randomUUID();
  readonly startedAt = new Date().toISOString();
  private server?: Server;
  private lifecycle: DaemonLifecycle = "INITIAL";
  private generationNumber = 0;
  private generation?: DaemonGeneration;
  private stopPromise?: Promise<void>;
  private terminalStopError?: Error;
  private authorityStartAttempted = false;
  private terminalStartupError?: Error;
  /** Nonsecret OS-process incarnation; distinct from daemon and listener generations. */
  readonly runtimeProcessIncarnationId = randomUUID();
  private readonly ownerFile: string;
  private readonly loginOperations = new Set<Promise<unknown>>();
  private readonly hostedBootstrapProjects = new Set<string>();

  constructor(private readonly options: RuntimeDaemonOptions) {
    this.ownerFile = `${options.socketPath}.owner.json`;
  }

  async start(): Promise<{ socketPath: string; operatorTokenFile: string }> {
    if (this.authorityStartAttempted) {
      throw new Error("Supplier authority requires a fresh daemon and lifecycle instance; same-instance startup retry is unavailable", { cause: this.terminalStartupError });
    }
    if (this.stopPromise !== undefined) throw new Error("Runtime daemon cannot start before shutdown has drained");
    if (this.lifecycle !== "INITIAL" && this.lifecycle !== "STOPPED") {
      throw new Error(`Runtime daemon cannot start while ${this.lifecycle.toLowerCase()}`);
    }
    this.lifecycle = "STARTING";
    this.terminalStopError = undefined;
    const generationNumber = ++this.generationNumber;
    const ownerGenerationId = randomUUID();
    let context: DaemonGeneration | undefined;
    let controlSocketBound = false;
    let authorityStarted = false;
    let accountHostStarted = false;
    try {
      await ensurePrivateDirectory(this.options.runtimeDirectory);
      await ensurePrivateDirectory(dirname(this.options.socketPath));
      if (this.options.supplierAuthority) {
        // The owner is single-incarnation even when its own start fails partway.
        this.authorityStartAttempted = true;
        await this.options.supplierAuthority.start(this.runtimeProcessIncarnationId);
        authorityStarted = true;
      }
      if (this.options.accountHost) {
        await this.options.accountHost.start();
        accountHostStarted = true;
      }
      await this.recoverStaleSocket();
      await atomicWriteJson(this.ownerFile, {
        schemaVersion: "chirality.daemon-owner/v1",
        daemonId: this.daemonId,
        generationId: ownerGenerationId,
        pid: process.pid,
        uid: process.getuid?.() ?? -1,
        socketPath: this.options.socketPath,
        startedAt: this.startedAt
      });
      const operator = await this.options.service.auth.ensureClient("operator", [
        "runtime:read",
        "projects:write",
        "sessions:read",
        "sessions:write",
        "models:read",
        "models:write",
        "credentials:read",
        "credentials:write"
      ]);
      let generation!: DaemonGeneration;
      const server = createServer((request, response) => {
        void this.route(request, response, generation).catch((error) =>
          this.error(response, error)
        );
      });
      generation = {
        number: generationNumber,
        ownerGenerationId,
        server,
        sockets: new Set(),
        streams: new Set(),
        stateWaiters: new Set(),
        closeStarted: false,
        closeComplete: false,
        forced: false,
        socketUnlinked: false,
        ownerRemoved: false,
        interruptionProblems: false
      };
      context = generation;
      server.on("connection", (socket) => {
        generation.sockets.add(socket);
        socket.once("close", () => {
          generation.sockets.delete(socket);
          this.notifyGeneration(generation);
        });
      });
      this.generation = generation;
      this.server = server;
      await new Promise<void>((resolve, reject) => {
        const onError = (error: Error): void => reject(error);
        server.once("error", onError);
        server.listen(this.options.socketPath, () => {
          server.off("error", onError);
          controlSocketBound = true;
          resolve();
        });
      });
      await chmod(this.options.socketPath, 0o600);
      if (this.generation !== generation || this.lifecycle !== "STARTING") {
        throw new Error("Runtime daemon generation changed during start");
      }
      this.options.delegated?.startGeneration(this.daemonId);
      if (this.options.approvals !== this.options.delegated) this.options.approvals?.startGeneration(this.daemonId);
      this.lifecycle = "RUNNING";
      return { socketPath: this.options.socketPath, operatorTokenFile: operator.tokenFile };
    } catch (error) {
      const cleanupFailures: unknown[] = [];
      // Close public admission first, then fence a successfully started authority.
      // Every later startup failure passes here, including owner/credential/listen/chmod.
      if (context !== undefined) {
        for (const socket of context.sockets) socket.destroy();
        try {
          await new Promise<void>((resolve, reject) => context!.server.close(closeError => {
            if (closeError && (closeError as NodeJS.ErrnoException).code !== "ERR_SERVER_NOT_RUNNING") reject(closeError);
            else resolve();
          }));
        } catch (cleanupError) { cleanupFailures.push(cleanupError); }
      }
      if (authorityStarted) {
        try { await this.options.supplierAuthority!.close(); }
        catch (cleanupError) { cleanupFailures.push(cleanupError); }
      }
      if (accountHostStarted) {
        try { await this.options.accountHost!.close(); }
        catch (cleanupError) { cleanupFailures.push(cleanupError); }
      }
      if (controlSocketBound) {
        try { await this.unlinkControlSocket(); }
        catch (cleanupError) { cleanupFailures.push(cleanupError); }
      }
      try { await this.removeOwnedRecord(ownerGenerationId); }
      catch (cleanupError) { cleanupFailures.push(cleanupError); }
      if (this.generation === context) this.generation = undefined;
      if (this.server === context?.server) this.server = undefined;
      const failure = cleanupFailures.length
        ? new AggregateError([error, ...cleanupFailures], "Runtime daemon startup and cleanup failed")
        : error instanceof Error ? error : new Error("Runtime daemon startup failed", { cause: error });
      this.terminalStartupError = failure;
      if (cleanupFailures.length || (this.authorityStartAttempted && !authorityStarted)) {
        // An incomplete authority startup or failed cleanup cannot become an idle,
        // retryable daemon. Its held lock/custody evidence requires owner disposition.
        this.lifecycle = "STOPPED_DEGRADED";
        this.terminalStopError = failure;
      } else {
        this.lifecycle = this.authorityStartAttempted ? "STOPPED" : generationNumber === 1 ? "INITIAL" : "STOPPED";
      }
      throw failure;
    }
  }

  private async loginOperation<T>(generation: DaemonGeneration, operation: () => Promise<T>): Promise<T> {
    if (this.lifecycle !== "RUNNING" || this.generation !== generation) throw new RuntimeError("ENGINE_UNAVAILABLE", "Login admission is closed for this daemon generation", 503);
    const pending = operation();
    this.loginOperations.add(pending);
    try {
      const result = await pending;
      if (this.lifecycle !== "RUNNING" || this.generation !== generation) throw new RuntimeError("ENGINE_UNAVAILABLE", "Login was cancelled during daemon shutdown", 503);
      return result;
    } finally { this.loginOperations.delete(pending); }
  }

  private async stopLogin(deadline: number): Promise<void> {
    const login = this.options.login;
    const hosted = this.options.hostedBootstrap;
    if (!login && !hosted && this.loginOperations.size === 0) return;
    const pending = [...this.loginOperations];
    // Cancel promptly, then again after starts drain: an admitted startup must not
    // create a live actor after the first cancellation has already returned.
    const drain = (async () => {
      const cancellations = [
        ...(login ? [login.cancel()] : []),
        ...(hosted ? [...this.hostedBootstrapProjects].map(projectId => hosted.cancelLogin(projectId)) : [])
      ];
      const results = await Promise.allSettled([...cancellations, ...pending]);
      await Promise.all([
        ...(login ? [login.cancel()] : []),
        ...(hosted ? [...this.hostedBootstrapProjects].map(projectId => hosted.cancelLogin(projectId)) : [])
      ]);
      const cancellation = results.slice(0, cancellations.length).find(result => result.status === "rejected");
      if (cancellation?.status === "rejected") throw cancellation.reason;
    })();
    let timer: ReturnType<typeof setTimeout> | undefined;
    try {
      await Promise.race([drain, new Promise<never>((_, reject) => {
        timer = setTimeout(() => reject(new RuntimeError("ENGINE_UNAVAILABLE", "Login cancellation did not drain within daemon shutdown grace", 503)), Math.max(0, deadline - performance.now()));
      })]);
    } finally { clearTimeout(timer); }
  }

  stop(): Promise<void> {
    if (this.stopPromise !== undefined) return this.stopPromise;
    if (this.lifecycle === "INITIAL" || this.lifecycle === "STOPPED") {
      return Promise.resolve();
    }
    if (this.lifecycle === "STARTING") {
      return Promise.reject(new Error("Runtime daemon cannot stop while starting"));
    }
    if (this.lifecycle === "STOPPED_DEGRADED") {
      return Promise.reject(
        this.terminalStopError ?? new Error("Runtime daemon stopped with interruption failure")
      );
    }
    const generation = this.generation;
    if (generation === undefined) {
      return Promise.reject(new Error("Runtime daemon lifecycle has no active generation"));
    }
    const retry = this.lifecycle === "STOP_FAILED_CLEANUP";
    this.lifecycle = "STOPPING";
    const deadline = retry ? undefined : performance.now() + STOP_GRACE_MS;
    const promise = Promise.allSettled([this.performStop(generation, retry, deadline), this.options.delegated?.close(), this.options.approvals !== this.options.delegated ? this.options.approvals?.close() : undefined, this.stopLogin(deadline ?? performance.now() + STOP_GRACE_MS)]).then((results) => {
      const daemonResult = results[0]!;
      if (daemonResult.status === "rejected") throw daemonResult.reason;
      const delegatedResult = results.slice(1).find(result => result.status === "rejected");
      if (delegatedResult?.status === "rejected") {
        this.lifecycle = "STOPPED_DEGRADED";
        this.terminalStopError = delegatedResult.reason instanceof Error ? delegatedResult.reason : new Error(String(delegatedResult.reason));
        throw this.terminalStopError;
      }
    });
    this.stopPromise = promise;
    const clear = (): void => {
      if (this.stopPromise === promise) this.stopPromise = undefined;
    };
    void promise.then(clear, clear);
    return promise;
  }

  private async route(
    request: IncomingMessage,
    response: ServerResponse,
    generation: DaemonGeneration
  ): Promise<void> {
    try {
      const url = new URL(request.url ?? "/", "http://chirality.invalid");
      const method = request.method ?? "GET";
      const segments = url.pathname.split("/").filter(Boolean).map(decodeURIComponent);
      if (segments[0] === "v3" && segments[1] === "hosted-bootstrap" && segments[2] === "projects" && segments.length === 4 && method === "POST") {
        const principal = await this.authorize(request, "projects:write");
        const provenance = this.bootstrapProvenance(principal.clientId, generation);
        if (segments[3] === "register") {
          const body = await this.body<HostedBootstrapProjectRegistrationRequest>(request);
          this.assertExactRecord(body, ["manifestPath"]);
          if (typeof body.manifestPath !== "string" || body.manifestPath.trim() === "") throw new RuntimeError("INVALID_REQUEST", "manifestPath must be a non-empty path");
          return this.json(response, 201, await this.registerHostedProject(body.manifestPath, provenance));
        }
        if (segments[3] === "initialize") {
          const body = await this.body<HostedBootstrapProjectInitializationRequest>(request);
          this.assertExactRecord(body, ["projectRoot"]);
          if (typeof body.projectRoot !== "string" || body.projectRoot.trim() === "") throw new RuntimeError("INVALID_REQUEST", "projectRoot must be a non-empty path");
          const manifestPath = await ensureHostedProjectManifest(body.projectRoot);
          return this.json(response, 201, await this.registerHostedProject(manifestPath, provenance));
        }
        throw new RuntimeError("NOT_FOUND", "Route not found", 404);
      }
      if (segments[0] === "v3" && segments[1] === "projects" && segments.length >= 5 && segments[3] === "hosted-bootstrap") {
        const projectId = segments[2]!;
        const bootstrap = this.options.hostedBootstrap;
        if (!bootstrap) throw new RuntimeError("ENGINE_UNAVAILABLE", "Hosted bootstrap is unavailable", 503);
        if (segments.length === 5 && segments[4] === "status" && method === "GET") {
          const status = await this.runHostedAccount(request, "status", "runtime:read", projectId, (_principal, signal) => this.loginOperation(generation, () => bootstrap.status(projectId, signal)));
          return this.json(response, 200, this.safeBootstrapStatus(projectId, status));
        }
        if (segments.length === 5 && segments[4] === "provider-network-consent" && method === "POST") {
          const body = await this.body<HostedProviderNetworkConsentRequest>(request);
          this.assertExactRecord(body, ["consent"]);
          if (body.consent !== true) throw new RuntimeError("INVALID_REQUEST", "Explicit provider-network consent is required");
          const status = await this.runHostedAccount(request, "grant-provider-network-consent", "credentials:write", projectId, (principal, signal) =>
            this.loginOperation(generation, () => bootstrap.grantProviderNetworkConsent(projectId, {
              ...this.bootstrapProvenance(principal.clientId, generation),
              approvedAt: new Date().toISOString()
            }, signal)));
          return this.json(response, 200, this.safeBootstrapStatus(projectId, status));
        }
        if (segments.length === 5 && segments[4] === "logout" && method === "POST") {
          const body = await this.body<Record<string, never>>(request);
          this.assertExactRecord(body, []);
          const status = await this.runHostedAccount(request, "sign-out", "credentials:write", projectId, (_principal, signal) => this.loginOperation(generation, () => bootstrap.signOut(projectId, signal)));
          return this.json(response, 200, this.safeBootstrapStatus(projectId, status));
        }
        if (segments.length === 6 && segments[4] === "login" && method === "POST" && (segments[5] === "start" || segments[5] === "cancel")) {
          const body = await this.body<Record<string, never>>(request);
          this.assertExactRecord(body, []);
          this.hostedBootstrapProjects.add(projectId);
          if (segments[5] === "cancel") {
            const status = await this.runHostedAccount(request, "cancel-login", "credentials:write", projectId, (_principal, signal) => this.loginOperation(generation, () => bootstrap.cancelLogin(projectId, signal)));
            return this.json(response, 200, this.safeBootstrapStatus(projectId, status));
          }
          const result = await this.runHostedAccount(request, "start-login", "credentials:write", projectId, (_principal, signal) => this.loginOperation(generation, () => bootstrap.startLogin(projectId, signal)));
          this.assertExactRecord(result, ["loginId", "authUrl"], "Invalid safe login response");
          if (typeof result.loginId !== "string" || result.loginId.length === 0 || result.loginId.length > 512 || typeof result.authUrl !== "string" || result.authUrl.length > 8192) {
            throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe login response", 500);
          }
          let authUrl: URL;
          try { authUrl = new URL(result.authUrl); }
          catch { throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe login URL", 500); }
          if (authUrl.protocol !== "https:" || authUrl.username || authUrl.password) throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe login URL", 500);
          return this.json(response, 200, { loginId: result.loginId, authUrl: result.authUrl });
        }
        throw new RuntimeError("NOT_FOUND", "Route not found", 404);
      }
      if (segments[0] === "v2" && segments[1] === "projects" && segments.length === 5 && segments[3] === "login") {
        const projectId = segments[2]!;
        await this.authorize(request, "credentials:write", projectId);
        const project = await this.options.service.projects.requireAuthorized(projectId);
        const { login, delegated, loginProjectId } = this.options;
        if (!login || !delegated || loginProjectId !== projectId) throw new RuntimeError("ENGINE_UNAVAILABLE", "Login is not configured for this project", 503);
        delegated.assertProjectRoot(projectId, project.canonicalRoot);
        if (method === "GET" && segments[4] === "status") {
          const status = await this.loginOperation(generation, () => login.status());
          let safeStatus: HostedLoginStatus;
          try { safeStatus = validateHostedLoginStatus(status); }
          catch { throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe login status", 500); }
          return this.json(response, 200, safeStatus);
        }
        if (method === "POST" && (segments[4] === "start" || segments[4] === "cancel")) {
          const body = await this.body<any>(request);
          delegated.authorizeControl(projectId, segments[4] === "start" ? "login:start" : "login:cancel", body);
          if (segments[4] === "cancel") { await this.loginOperation(generation, () => login.cancel()); return this.json(response, 200, { cancelled: true }); }
          const result = await this.loginOperation(generation, () => login.startLogin());
          let url: URL;
          try { url = new URL(result.authUrl); } catch { throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe login URL", 500); }
          if (url.protocol !== "https:" || url.username || url.password || result.authUrl.length > 8192 || typeof result.loginId !== "string" || !result.loginId || result.loginId.length > 512) throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe login response", 500);
          return this.json(response, 200, { loginId: result.loginId, authUrl: result.authUrl });
        }
        throw new RuntimeError("NOT_FOUND", "Route not found", 404);
      }
      if (segments[0] === "v2" && segments[1] === "projects" && segments.length === 5 && segments[3] === "approvals") {
        const projectId = segments[2]!;
        await this.authorize(request, "sessions:write", projectId);
        const registered = await this.options.service.projects.requireAuthorized(projectId);
        const approvals = this.options.approvals ?? this.options.delegated;
        if (!approvals) throw new RuntimeError("ENGINE_UNAVAILABLE", "Runtime approval controls are unavailable", 503);
        approvals.assertProjectRoot(projectId, registered.canonicalRoot);
        if (method === "GET" && segments[4] === "pending") return this.json(response, 200, await approvals.pendingProjectApprovals(projectId, url.searchParams.get("scopeId") ?? undefined));
        if (method === "GET" && segments[4] === "capabilities") return this.json(response, 200, await approvals.capabilities(projectId));
        if (method === "POST" && ["preflight", "decision"].includes(segments[4]!)) {
          const body = await this.body<any>(request);
          if (!body || typeof body !== "object" || Array.isArray(body)) throw new RuntimeError("INVALID_REQUEST", "Object request required");
          if (segments[4] === "preflight") {
            if (typeof body.operationId !== "string" || !/^approval:[a-f0-9-]{36}$/.test(body.operationId)) throw new RuntimeError("FORBIDDEN", "Approval preflight is scoped to an existing approval identity", 403);
            return this.json(response, 200, await approvals.preflight(projectId, body.operationId));
          }
          return this.json(response, 200, await approvals.decideApproval(projectId, body.requestId, body));
        }
        throw new RuntimeError("NOT_FOUND", "Route not found", 404);
      }
      if (segments[0] === "v2" && segments[1] === "projects" && segments.length === 5 && segments[3] === "delegated" && (method === "POST" || method === "GET")) {
        const projectId = segments[2]!;
        await this.authorize(request, "sessions:write", projectId);
        const registeredProject = await this.options.service.projects.requireAuthorized(projectId);
        const delegated = this.options.delegated;
        if (delegated === undefined) throw new RuntimeError("ENGINE_UNAVAILABLE", "Delegated runtime is not configured", 503);
        delegated.assertProjectRoot(projectId, registeredProject.canonicalRoot);
        if (method === "GET" && segments[4] === "capabilities") return this.json(response, 200, await delegated.capabilities(projectId));
        if (method === "GET" && segments[4] === "approvals") return this.json(response, 200, await delegated.pendingApprovals(projectId, url.searchParams.get("turnId") ?? ""));
        if (method !== "POST") throw new RuntimeError("NOT_FOUND", "Route not found", 404);
        const body = await this.body<any>(request);
        if (!body || typeof body !== "object" || Array.isArray(body)) throw new RuntimeError("INVALID_REQUEST", "Object request required");
        if (segments[4] === "preflight") return this.json(response, 200, await delegated.preflight(projectId, body.operationId));
        if (segments[4] === "consent") return this.json(response, 200, await delegated.grantConsent(projectId, body));
        if (segments[4] === "approval-decision") return this.json(response, 200, await delegated.decideApproval(projectId, body.requestId, body));
        if (segments[4] === "interrupt") return this.json(response, 200, await delegated.interruptTurn(projectId, body));
        if (segments[4] === "turn") return this.json(response, 200, await delegated.turn(projectId, body));
      }
      if (segments[0] !== "v1") throw new RuntimeError("NOT_FOUND", "Route not found", 404);

      if (method === "GET" && url.pathname === "/v1/health") {
        await this.authorize(request, "runtime:read");
        return this.json(response, 200, this.health());
      }
      if (method === "GET" && url.pathname === "/v1/daemon/status") {
        await this.authorize(request, "runtime:read");
        const body: DaemonStatusResponse = {
          ...this.health(),
          startedAt: this.startedAt,
          socketPath: this.options.socketPath,
          engines: this.options.service.engines.descriptors()
        };
        return this.json(response, 200, body);
      }
      if (method === "GET" && url.pathname === "/v1/projects") {
        const principal = await this.authorize(request, "runtime:read");
        const projects =
          principal.projectId === undefined
            ? await this.options.service.projects.list()
            : [await this.options.service.projects.status(principal.projectId)];
        return this.json(response, 200, { projects });
      }
      if (method === "POST" && url.pathname === "/v1/projects/register") {
        await this.authorize(request, "projects:write");
        const body = await this.body<ProjectRegistrationRequest>(request);
        return this.json(
          response,
          201,
          await this.options.service.registerProject(
            body.manifestPath,
            body.approvedBy,
            body.approvalReference
          )
        );
      }
      if (segments[1] === "credentials" && typeof segments[2] === "string") {
        const providerId = segments[2];
        if (method === "GET") {
          await this.authorize(request, "credentials:read");
          return this.json(response, 200, {
            providerId,
            ...(await this.options.service.credentials.status(providerId))
          });
        }
        if (method === "PUT") {
          await this.authorize(request, "credentials:write");
          const body = await this.body<CredentialMutationRequest>(request);
          if (body.credential.trim() === "") {
            throw new RuntimeError("INVALID_REQUEST", "Credential cannot be empty");
          }
          await this.options.service.credentials.set(providerId, body.credential);
          return this.json(response, 200, { providerId, configured: true });
        }
        if (method === "DELETE") {
          await this.authorize(request, "credentials:write");
          await this.options.service.credentials.remove(providerId);
          return this.json(response, 200, { providerId, configured: false });
        }
      }
      if (segments[1] === "models") {
        if (segments.length === 2 && method === "GET") {
          await this.authorize(request, "models:read");
          return this.json(response, 200, {
            residency: await this.options.service.residency.status()
          });
        }
        if (segments.length === 4 && segments[3] === "activate" && method === "POST") {
          await this.authorize(request, "models:write");
          const body = await this.body<{ approvalReference: string }>(request);
          return this.json(response, 200, {
            residency: await this.options.service.residency.activate(
              segments[2] ?? "",
              body.approvalReference
            )
          });
        }
      }
      if (segments[1] === "projects" && typeof segments[2] === "string") {
        const projectId = segments[2];
        if (segments.length === 4 && segments[3] === "status" && method === "GET") {
          await this.authorize(request, "runtime:read", projectId);
          return this.json(response, 200, await this.options.service.projects.status(projectId));
        }
        if (segments.length === 4 && segments[3] === "agents" && method === "GET") {
          await this.authorize(request, "sessions:read", projectId);
          return this.json(response, 200, {
            agents: await this.options.service.listAgents(
              projectId,
              url.searchParams.get("directChat") === "1"
            )
          });
        }
        if (segments.length === 4 && segments[3] === "roles" && method === "GET") {
          await this.authorize(request, "sessions:read", projectId);
          return this.json(response, 200, await this.options.service.listRoles(projectId));
        }
        if (segments.length === 4 && segments[3] === "methods" && method === "GET") {
          await this.authorize(request, "sessions:read", projectId);
          return this.json(response, 200, await this.options.service.listMethods(projectId));
        }
        if (segments.length === 5 && segments[3] === "methods" && method === "GET") {
          await this.authorize(request, "sessions:read", projectId);
          return this.json(response, 200, await this.options.service.inspectMethod(projectId, segments[4]!));
        }
        if (segments.length === 4 && segments[3] === "scaffold" && method === "POST") {
          await this.authorize(request, "sessions:write", projectId);
          const body = await this.body<ScaffoldRequest>(request);
          return this.json(response, 200, {
            scaffold: await this.options.service.scaffold(projectId, body)
          });
        }
        if (segments.length === 4 && segments[3] === "runs" && method === "POST") {
          await this.authorize(request, "sessions:write", projectId);
          const body = await this.body<Agent1RunRequest>(request);
          let managerSessionId: string | undefined;
          const source = this.options.service.runAgent1(projectId, body);
          const tracked = (async function* (): AsyncIterable<UIEvent> {
            for await (const event of source) {
              if (managerSessionId === undefined && event.type === "harness:event") {
                managerSessionId = event.data.sessionId;
              }
              yield event;
            }
          })();
          return await this.sse(
            response,
            tracked,
            () => {
              if (managerSessionId !== undefined) {
                return this.options.service.interruptSession(projectId, managerSessionId);
              }
              return undefined;
            },
            generation
          );
        }
        if (segments[3] === "sessions") {
          return await this.sessionRoute(
            request,
            response,
            method,
            projectId,
            segments,
            generation
          );
        }
      }
      throw new RuntimeError("NOT_FOUND", "Route not found", 404);
    } catch (error) {
      this.error(response, error);
    }
  }

  private async sessionRoute(
    request: IncomingMessage,
    response: ServerResponse,
    method: string,
    projectId: string,
    segments: string[],
    generation: DaemonGeneration
  ): Promise<void> {
    if (segments.length === 4) {
      if (method === "GET") {
        await this.authorize(request, "sessions:read", projectId);
        return this.json(response, 200, {
          sessions: await this.options.service.sessions.list(projectId)
        });
      }
      if (method === "POST") {
        await this.authorize(request, "sessions:write", projectId);
        const body = await this.body<Omit<CreateSessionRequest, "projectId">>(request);
        return this.json(response, 201, {
          session: await this.options.service.createSession({ ...body, projectId })
        });
      }
    }
    const sessionId = segments[4];
    if (sessionId === undefined) throw new RuntimeError("NOT_FOUND", "Route not found", 404);
    if (segments.length === 5) {
      if (method === "GET") {
        await this.authorize(request, "sessions:read", projectId);
        return this.json(response, 200, {
          session: await this.options.service.sessions.get(projectId, sessionId)
        });
      }
      if (method === "DELETE") {
        await this.authorize(request, "sessions:write", projectId);
        await this.options.service.sessions.delete(projectId, sessionId);
        return this.json(response, 200, { deleted: true, sessionId });
      }
    }
    if (segments.length === 7 && segments[5] === "context" && segments[6] === "resolve" && method === "POST") {
      await this.authorize(request, "sessions:read", projectId);
      const body = await this.body<ResolveSelectedContextRequest>(request);
      return this.json(response, 200, await this.options.service.resolveSelectedContext(projectId, sessionId, body));
    }
    if (segments.length === 7 && segments[5] === "native-plan" && segments[6] === "capability" && method === "GET") {
      await this.authorize(request, "sessions:read", projectId);
      return this.json(response, 200, await this.options.service.getNativePlanCapability(projectId, sessionId));
    }
    if (segments.length === 7 && segments[5] === "native-plan" && segments[6] === "revisions" && method === "GET") {
      await this.authorize(request, "sessions:read", projectId);
      return this.json(response, 200, await this.options.service.listNativePlanRevisions(projectId, sessionId));
    }
    if (segments.length === 7 && segments[5] === "native-plan" && segments[6] === "export" && method === "POST") {
      await this.authorize(request, "sessions:write", projectId);
      const body = await this.body<ExportNativePlanRequest>(request);
      return this.json(response, 200, await this.options.service.exportNativePlan(projectId, sessionId, body));
    }
    if (segments.length === 7 && segments[5] === "native-plan" && segments[6] === "clarifications" && method === "GET") {
      await this.authorize(request, "sessions:read", projectId);
      return this.json(response, 200, await this.options.service.listNativePlanClarifications(projectId, sessionId));
    }
    if (segments.length === 8 && segments[5] === "native-plan" && segments[6] === "clarifications" && segments[7] === "reply" && method === "POST") {
      await this.authorize(request, "sessions:write", projectId);
      const body = await this.body<ReplyNativePlanClarificationRequest>(request);
      return this.json(response, 200, await this.options.service.replyNativePlanClarification(projectId, sessionId, body));
    }
    if (segments.length !== 6) throw new RuntimeError("NOT_FOUND", "Route not found", 404);
    const action = segments[5];
    if (action === "methods" && method === "PUT") {
      await this.authorize(request, "sessions:write", projectId);
      const body = await this.body<ReplaceSelectedMethodsRequest>(request);
      return this.json(response, 200, await this.options.service.replaceSelectedMethods(projectId, sessionId, body));
    }
    if (action === "boot" && method === "POST") {
      await this.authorize(request, "sessions:write", projectId);
      const body = await this.body<RuntimeSessionBootRequest>(request);
      return this.json(
        response,
        200,
        await this.options.service.bootSession(
          projectId,
          sessionId,
          body.opts,
          body.expectedSelection
        )
      );
    }
    if (action === "replay" && method === "GET") {
      await this.authorize(request, "sessions:read", projectId);
      const session = await this.options.service.sessions.get(projectId, sessionId);
      const replay = await this.options.service.sessions.replayDetailed(projectId, sessionId);
      const instructionHistory = await this.options.service.sessions.instructionBases.history(projectId, sessionId);
      const basisIds = [...new Set(instructionHistory.filter(record => record.type === "instruction-basis.resolved").map(record => record.basisId))];
      const instructionBases = await Promise.all(basisIds.map(basisId => this.options.service.sessions.instructionBases.get(projectId, sessionId, basisId)));
      return this.json(response, 200, {
        session,
        ...replay,
        transcript: deriveTranscriptView(replay.events, session),
        instructionHistory,
        instructionBases
      });
    }
    if (action === "turn" && method === "POST") {
      await this.authorize(request, "sessions:write", projectId);
      const body = await this.body<SessionTurnRequest>(request);
      return await this.sse(
        response,
        this.options.service.runSessionTurn(projectId, sessionId, body),
        () => this.options.service.interruptSession(projectId, sessionId),
        generation
      );
    }
    if (action === "interrupt" && method === "POST") {
      await this.authorize(request, "sessions:write", projectId);
      await this.options.service.interruptSession(projectId, sessionId);
      return this.json(response, 200, { interrupted: true, sessionId });
    }
    if (action === "permission" && method === "POST") {
      await this.authorize(request, "sessions:write", projectId);
      await this.options.service.sessions.get(projectId, sessionId);
      const body = await this.body<PermissionDecisionRequest>(request);
      await this.options.service.decidePermission(projectId, sessionId, body);
      return this.json(response, 200, {
        accepted: true,
        requestId: body.requestId,
        decision: body.decision
      });
    }
    throw new RuntimeError("NOT_FOUND", "Route not found", 404);
  }

  private health(): HealthResponse {
    return {
      apiVersion: RUNTIME_API_VERSION,
      status: "ok",
      daemonId: this.daemonId,
      pid: process.pid
    };
  }

  private authorize(
    request: IncomingMessage,
    scope: RuntimeScope,
    projectId?: string
  ) {
    const value = Array.isArray(request.headers.authorization)
      ? request.headers.authorization[0]
      : request.headers.authorization;
    return this.options.service.auth.authenticate(value, scope, projectId);
  }

  private async runHostedAccount<T>(
    request: IncomingMessage,
    operation: HostAccountOperation,
    legacyScope: RuntimeScope,
    projectId: string,
    effect: (principal: { clientId: string }, signal: AbortSignal) => Promise<T>
  ): Promise<T> {
    const proof = request.headers["x-chirality-account-proof"];
    const authority = this.options.accountHost;
    try {
      if (authority === undefined) return await effect(await this.authorize(request, legacyScope, projectId), new AbortController().signal);
      if (proof === undefined) throw new RuntimeError("UNAUTHORIZED", "Complete App account host proof is required", 401);
      return await authority.runAuthorizedRequest({
        authorization: request.headers.authorization,
        counter: request.headers["x-chirality-account-counter"],
        generation: request.headers["x-chirality-account-generation"],
        proof,
        descriptor: hostAccountRequest(operation, projectId)
      }, effect);
    } catch (error) {
      // Diagnostics only: operation identity plus code/status/reason/message. Never the auth URL, bearer, proof or counters.
      try { (this.options.logger ?? NOOP_RUNTIME_DAEMON_LOGGER).error("runtime.daemon.hosted_account.failed", { operation, projectId, ...describeRuntimeFailure(error) }); } catch {}
      throw error;
    }
  }

  private bootstrapProvenance(clientId: string, generation: DaemonGeneration): { approvedBy: string; approvalReference: string } {
    return {
      approvedBy: `runtime-client:${clientId}`,
      approvalReference: `hosted-bootstrap:${this.daemonId}:${generation.ownerGenerationId}`
    };
  }

  private async registerHostedProject(
    manifestPath: string,
    provenance: { approvedBy: string; approvalReference: string }
  ): Promise<HostedBootstrapProjectRegistrationResponse> {
    const project = await this.options.service.projects.register(manifestPath, provenance, hostedProjectClientId);
    await this.options.service.auth.revokeProjectClients(project.projectId);
    await this.options.service.auth.ensureClient(project.clientId, [
      "runtime:read",
      "sessions:read",
      "sessions:write",
      "models:read"
    ], project.projectId);
    return { projectId: project.projectId, manifestHash: project.manifestHash };
  }

  private safeBootstrapStatus(projectId: string, value: unknown): HostedBootstrapStatus {
    let status: HostedBootstrapStatus;
    try { status = validateHostedBootstrapStatus(value); }
    catch { throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe hosted bootstrap status", 500); }
    if (status.projectId !== projectId) throw new RuntimeError("INTERNAL_FAILURE", "Hosted bootstrap status project mismatch", 500);
    return status;
  }

  private assertExactRecord(value: unknown, keys: readonly string[], message = "Invalid request fields"): asserts value is Record<string, unknown> {
    if (!value || typeof value !== "object" || Array.isArray(value) || Object.keys(value).length !== keys.length || Object.keys(value).some(key => !keys.includes(key))) {
      throw new RuntimeError(message.startsWith("Invalid safe") ? "INTERNAL_FAILURE" : "INVALID_REQUEST", message, message.startsWith("Invalid safe") ? 500 : 400);
    }
  }

  private async body<T>(request: IncomingMessage): Promise<T> {
    const chunks: Buffer[] = [];
    let total = 0;
    for await (const chunk of request) {
      const buffer = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk);
      total += buffer.length;
      if (total > JSON_LIMIT_BYTES) {
        throw new RuntimeError("INVALID_REQUEST", "Request body is too large", 413);
      }
      chunks.push(buffer);
    }
    try {
      const value=JSON.parse(Buffer.concat(chunks).toString("utf8")) as T;assertNoPrivateAuthoritySurface(value);return value;
    } catch {
      throw new RuntimeError("INVALID_REQUEST", "Request body must be valid JSON");
    }
  }

  private async discardOptionalBody(request: IncomingMessage): Promise<void> {
    for await (const _chunk of request) {
      // Drain the stream without interpreting unused compatibility input.
    }
  }

  private json(response: ServerResponse, status: number, value: unknown): void {
    if (response.headersSent) return;
    assertNoPrivateAuthoritySurface(value);
    const body = JSON.stringify(value);
    response.writeHead(status, {
      "content-type": "application/json; charset=utf-8",
      "content-length": Buffer.byteLength(body)
    });
    response.end(body);
  }

  private async sse(
    response: ServerResponse,
    events: AsyncIterable<UIEvent>,
    onDisconnect: (() => Promise<void> | undefined) | undefined,
    generation: DaemonGeneration
  ): Promise<void> {
    const iterator = events[Symbol.asyncIterator]();
    const control: ActiveSse = {
      generation,
      interrupt: onDisconnect ?? (() => undefined),
      iterator,
      cancellationRequested: false,
      interruptionStarted: false,
      interruptionSettled: false,
      interruptionTimedOut: false,
      identityUnavailable: false,
      forceExpired: false,
      iteratorReturnRequested: false
    };
    generation.streams.add(control);
    let finished = false;
    let streamStarted = false;
    let disconnected = response.destroyed;
    const close = (): void => {
      if (finished) return;
      disconnected = true;
      this.cancelSse(control);
    };
    response.once("close", close);
    try {
      const first = await iterator.next();
      streamStarted = true;
      // The first Agent 1 event may reveal the session identity while a
      // shutdown cancellation is already latched.
      this.trySseInterrupt(control);
      if (response.destroyed && !disconnected) disconnected = true;
      if (disconnected) {
        // A run stream may not know its manager session until the first event.
        // Retry the single cancellation latch after identity has been captured.
        this.trySseInterrupt(control);
      } else {
        response.writeHead(200, {
          "content-type": "text/event-stream",
          "cache-control": "no-cache, no-transform",
          connection: "keep-alive",
          "x-accel-buffering": "no"
        });
      }
      if (!first.done && !disconnected) {
        assertNoPrivateAuthoritySurface(first.value);
        response.write(
          `event: ${first.value.type}\ndata: ${JSON.stringify(first.value.data)}\n\n`
        );
      }
      while (true) {
        const next = await iterator.next();
        // A later Agent 1 event may be the first to reveal the manager
        // session while shutdown cancellation is already latched.
        this.trySseInterrupt(control);
        if (next.done) break;
        if (!disconnected) {
          assertNoPrivateAuthoritySurface(next.value);
          response.write(
            `event: ${next.value.type}\ndata: ${JSON.stringify(next.value.data)}\n\n`
          );
        }
      }
    } finally {
      finished = true;
      response.off("close", close);
      if (control.cancellationRequested) this.requestSseIteratorReturn(control);
      generation.streams.delete(control);
      this.notifyGeneration(generation);
      if (streamStarted && !response.destroyed) response.end();
    }
  }

  private cancelSse(control: ActiveSse): void {
    if (!control.cancellationRequested) control.cancellationRequested = true;
    this.trySseInterrupt(control);
  }

  private requestSseIteratorReturn(control: ActiveSse): void {
    if (!control.iteratorReturnRequested && control.iterator?.return !== undefined) {
      control.iteratorReturnRequested = true;
      let returned: Promise<IteratorResult<UIEvent>>;
      try {
        returned = Promise.resolve(control.iterator.return());
      } catch (error) {
        control.iteratorReturnFailure = error;
        this.notifyGeneration(control.generation);
        return;
      }
      void returned.then(
        () => this.notifyGeneration(control.generation),
        (error) => {
          control.iteratorReturnFailure = error;
          this.notifyGeneration(control.generation);
        }
      );
    }
  }

  private trySseInterrupt(control: ActiveSse): void {
    if (
      !control.cancellationRequested ||
      control.interruptionStarted ||
      control.forceExpired
    ) {
      return;
    }
    let interruption: Promise<void> | undefined;
    try {
      interruption = control.interrupt();
    } catch (error) {
      control.interruptionStarted = true;
      control.interruptionSettled = true;
      control.interruptionFailure = error;
      this.notifyGeneration(control.generation);
      return;
    }
    if (interruption === undefined) return;
    control.interruptionStarted = true;
    void interruption.then(
      () => {
        control.interruptionSettled = true;
        this.notifyGeneration(control.generation);
      },
      (error) => {
        control.interruptionSettled = true;
        control.interruptionFailure = error;
        this.notifyGeneration(control.generation);
      }
    );
  }

  private async performStop(
    generation: DaemonGeneration,
    retry: boolean,
    deadline: number | undefined
  ): Promise<void> {
    const cleanupFailures: unknown[] = [];
    if (!retry) {
      generation.stopStreams = [...generation.streams];
      this.beginServerClose(generation);
      await this.options.accountHost?.close();
      await this.options.supplierAuthority?.close();
      // Admission is closed before any semantic interruption is requested.
      for (const stream of generation.stopStreams) this.cancelSse(stream);
      await this.waitUntilGeneration(
        generation,
        () =>
          generation.closeComplete &&
          generation.sockets.size === 0 &&
          (generation.stopStreams ?? []).every(
            (stream) =>
              stream.interruptionStarted &&
              stream.interruptionSettled &&
              !generation.streams.has(stream)
          ),
        Math.max(0, (deadline ?? performance.now()) - performance.now())
      );
      for (const stream of generation.stopStreams) {
        if (!stream.interruptionStarted) {
          stream.forceExpired = true;
          stream.identityUnavailable = true;
        } else if (!stream.interruptionSettled) {
          stream.forceExpired = true;
          stream.interruptionTimedOut = true;
        }
        if (generation.streams.has(stream)) this.requestSseIteratorReturn(stream);
      }
      generation.interruptionProblems = generation.stopStreams.some(
        (stream) =>
          stream.identityUnavailable ||
          stream.interruptionTimedOut ||
          stream.interruptionFailure !== undefined ||
          stream.iteratorReturnFailure !== undefined
      );
      if (!generation.closeComplete || generation.sockets.size > 0) {
        this.forceGenerationTransport(generation, cleanupFailures);
      }
    } else if (!generation.closeComplete || generation.sockets.size > 0) {
      this.beginServerClose(generation);
      await this.options.accountHost?.close();
      await this.options.supplierAuthority?.close();
      this.forceGenerationTransport(generation, cleanupFailures);
    }

    if (generation.forced) {
      const settled = await this.waitUntilGeneration(
        generation,
        () => generation.closeComplete && generation.sockets.size === 0,
        STOP_FORCE_SETTLE_MS
      );
      if (!settled) cleanupFailures.push(new Error("SERVER_CLOSE_SETTLEMENT_TIMEOUT"));
    }
    if (generation.closeError !== undefined) cleanupFailures.push(generation.closeError);
    if (generation.sockets.size > 0) cleanupFailures.push(new Error("RESIDUAL_SERVER_SOCKETS"));
    generation.interruptionProblems ||= (generation.stopStreams ?? []).some(
      (stream) =>
        stream.identityUnavailable ||
        stream.interruptionTimedOut ||
        stream.interruptionFailure !== undefined ||
        stream.iteratorReturnFailure !== undefined
    );

    if (!generation.socketUnlinked) {
      try {
        await this.unlinkControlSocket();
        generation.socketUnlinked = true;
      } catch (error) {
        cleanupFailures.push(error);
      }
    }
    if (!generation.ownerRemoved) {
      try {
        await this.removeOwnedRecord(generation.ownerGenerationId);
        generation.ownerRemoved = true;
      } catch (error) {
        cleanupFailures.push(error);
      }
    }

    if (cleanupFailures.length > 0 || !generation.closeComplete) {
      const error = this.stopError("STOP_FAILED_CLEANUP", cleanupFailures);
      if (this.generation === generation) {
        this.lifecycle = "STOP_FAILED_CLEANUP";
        this.terminalStopError = error;
      }
      throw error;
    }

    this.server = this.server === generation.server ? undefined : this.server;
    if (this.generation === generation) this.generation = undefined;
    if (generation.interruptionProblems) {
      const causes = (generation.stopStreams ?? []).flatMap((stream) => [
        ...(stream.identityUnavailable
          ? [new Error("INTERRUPTION_IDENTITY_UNAVAILABLE")]
          : []),
        ...(stream.interruptionTimedOut ? [new Error("INTERRUPTION_TIMEOUT")] : []),
        ...(stream.interruptionFailure === undefined ? [] : [stream.interruptionFailure]),
        ...(stream.iteratorReturnFailure === undefined ? [] : [stream.iteratorReturnFailure])
      ]);
      const error = this.stopError("STOPPED_DEGRADED", causes);
      this.lifecycle = "STOPPED_DEGRADED";
      this.terminalStopError = error;
      throw error;
    }
    this.lifecycle = "STOPPED";
    this.terminalStopError = undefined;
  }

  private beginServerClose(generation: DaemonGeneration): void {
    if (generation.closeStarted && generation.closeError === undefined) return;
    generation.closeStarted = true;
    generation.closeError = undefined;
    try {
      generation.server.close((error) => {
        if (error === undefined) {
          generation.closeComplete = true;
        } else {
          generation.closeError = error;
        }
        this.notifyGeneration(generation);
      });
    } catch (error) {
      generation.closeError = error;
      this.notifyGeneration(generation);
    }
  }

  private forceGenerationTransport(
    generation: DaemonGeneration,
    failures: unknown[]
  ): void {
    generation.forced = true;
    try {
      generation.server.closeAllConnections();
    } catch (error) {
      failures.push(error);
    }
    for (const socket of generation.sockets) {
      try {
        socket.destroy();
      } catch (error) {
        failures.push(error);
      }
    }
  }

  private waitUntilGeneration(
    generation: DaemonGeneration,
    predicate: () => boolean,
    timeoutMs: number
  ): Promise<boolean> {
    if (predicate()) return Promise.resolve(true);
    return new Promise((resolve) => {
      let settled = false;
      const finish = (value: boolean): void => {
        if (settled) return;
        settled = true;
        clearTimeout(timer);
        generation.stateWaiters.delete(check);
        resolve(value);
      };
      const check = (): void => {
        if (predicate()) finish(true);
      };
      const timer = setTimeout(() => finish(predicate()), timeoutMs);
      generation.stateWaiters.add(check);
      check();
    });
  }

  private notifyGeneration(generation: DaemonGeneration): void {
    for (const waiter of [...generation.stateWaiters]) waiter();
  }

  private stopError(code: "STOPPED_DEGRADED" | "STOP_FAILED_CLEANUP", causes: unknown[]): Error {
    const details = causes.map((cause) =>
      cause instanceof Error ? cause.message : String(cause)
    );
    const error = new Error(`${code}${details.length === 0 ? "" : `: ${details.join("; ")}`}`);
    error.name = code;
    Object.assign(error, { code, causes });
    return error;
  }

  private async unlinkControlSocket(): Promise<void> {
    await unlink(this.options.socketPath).catch((error: NodeJS.ErrnoException) => {
      if (error.code !== "ENOENT") throw error;
    });
  }

  private error(response: ServerResponse, error: unknown): void {
    if (response.headersSent) {
      response.end();
      return;
    }
    const normalized =
      error instanceof RuntimeError
        ? error
        : error instanceof HarnessError
          ? new RuntimeError(
              error.type === "SESSION_NOT_FOUND" ? "SESSION_NOT_FOUND" : "INTERNAL_FAILURE",
              error.message,
              error.status
            )
          : new RuntimeError("INTERNAL_FAILURE", "Unexpected runtime failure", 500);
    const body: RuntimeErrorBody = {
      error: {
        code: normalized.code,
        message: normalized.message,
        ...(normalized.details === undefined ? {} : { details: normalized.details })
      }
    };
    this.json(response, normalized.status, body);
  }

  private async recoverStaleSocket(): Promise<void> {
    const owner = await this.readOwner();
    let metadata;
    try {
      metadata = await lstat(this.options.socketPath);
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code === "ENOENT") {
        if (owner === undefined) return;
        if (this.pidIsDemonstrablyAbsent(owner.pid)) {
          await unlink(this.ownerFile);
          return;
        }
        throw new RuntimeError(
          "FORBIDDEN",
          "Daemon owner is live or ambiguous while the socket is absent",
          409
        );
      }
      throw error;
    }
    if (!metadata.isSocket()) {
      throw new RuntimeError("FORBIDDEN", "Refusing to replace a non-socket control path", 409);
    }
    if (process.getuid !== undefined && metadata.uid !== process.getuid()) {
      throw new RuntimeError("FORBIDDEN", "Refusing to replace another user's socket", 403);
    }
    if (owner === undefined) {
      throw new RuntimeError(
        "FORBIDDEN",
        "Refusing stale-socket recovery without an authenticated owner record",
        409
      );
    }
    if (
      owner.socketPath !== this.options.socketPath ||
      owner.uid !== (process.getuid?.() ?? -1)
    ) {
      throw new RuntimeError("FORBIDDEN", "Daemon owner record does not match this user/socket", 403);
    }
    if (!this.pidIsDemonstrablyAbsent(owner.pid)) {
      throw new RuntimeError(
        "RESIDENCY_TRANSITION_IN_PROGRESS",
        "Runtime daemon owner is live or ambiguous",
        409
      );
    }
    await unlink(this.options.socketPath);
    await unlink(this.ownerFile);
  }

  private async readOwner(): Promise<
    | {
        schemaVersion: "chirality.daemon-owner/v1";
        daemonId: string;
        generationId?: string;
        pid: number;
        uid: number;
        socketPath: string;
        startedAt: string;
      }
    | undefined
  > {
    let metadata;
    try {
      metadata = await lstat(this.ownerFile);
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code === "ENOENT") return undefined;
      throw error;
    }
    if (
      !metadata.isFile() ||
      (process.getuid !== undefined && metadata.uid !== process.getuid()) ||
      (metadata.mode & 0o077) !== 0
    ) {
      throw new RuntimeError("FORBIDDEN", "Unsafe daemon owner record", 403);
    }
    let value: unknown;
    try {
      value = JSON.parse(await readFile(this.ownerFile, "utf8"));
    } catch {
      throw new RuntimeError("FORBIDDEN", "Malformed daemon owner record", 409);
    }
    const owner = value as Record<string, unknown>;
    if (
      owner["schemaVersion"] !== "chirality.daemon-owner/v1" ||
      typeof owner["daemonId"] !== "string" ||
      (owner["generationId"] !== undefined && typeof owner["generationId"] !== "string") ||
      typeof owner["pid"] !== "number" ||
      !Number.isSafeInteger(owner["pid"]) ||
      typeof owner["uid"] !== "number" ||
      typeof owner["socketPath"] !== "string" ||
      typeof owner["startedAt"] !== "string"
    ) {
      throw new RuntimeError("FORBIDDEN", "Malformed daemon owner record", 409);
    }
    return owner as Awaited<ReturnType<RuntimeDaemon["readOwner"]>>;
  }

  private pidIsDemonstrablyAbsent(pid: number): boolean {
    if (pid <= 0) return false;
    try {
      process.kill(pid, 0);
      return false;
    } catch (error) {
      return (error as NodeJS.ErrnoException).code === "ESRCH";
    }
  }

  private async removeOwnedRecord(ownerGenerationId: string): Promise<void> {
    const owner = await this.readOwner();
    if (
      owner === undefined ||
      owner.daemonId !== this.daemonId ||
      owner.pid !== process.pid ||
      owner.generationId !== ownerGenerationId
    ) {
      return;
    }
    await unlink(this.ownerFile).catch((error: NodeJS.ErrnoException) => {
      if (error.code !== "ENOENT") throw error;
    });
  }
}
