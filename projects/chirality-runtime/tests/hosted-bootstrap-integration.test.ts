import { PassThrough } from "node:stream";
import { mkdir, mkdtemp, readdir, readFile, realpath, rm, stat, writeFile } from "node:fs/promises";
import { basename, join, resolve } from "node:path";
import { afterEach, describe, expect, it, vi } from "vitest";
import { randomUUID } from "node:crypto";
import { hostedModelCatalog, type AgentEnginePort, type AgentEngineRunInput, type DelegatedTurnRequest, type UIEvent, type WorkerContinuity } from "@chirality/runtime-contracts";
import { DelegatedRuntime, HostedConsentStore, WorkerRetirementCoordinator, type DelegatedNativePlanSink } from "@chirality/runtime-core";
import { RuntimeClient } from "@chirality/runtime-client";
import {
  resolveHostedProjectTokenFile,
  createControlledCodexSupervisorForTests,
  prepareCodexNativePolicy,
  startSupervisorServer,
  SupervisorClient,
  startControlledHostedBootstrapRuntimeHostForTests,
  type TrustedHostedLoginCeremony
} from "@chirality/runtime-daemon";

const cleanup: Array<() => Promise<void>> = [];
afterEach(async () => { for (const close of cleanup.splice(0).reverse()) await close().catch(() => undefined); });

async function drain(source: Awaited<ReturnType<RuntimeClient["turnSession"]>>): Promise<UIEvent[]> {
  const events: UIEvent[] = [];
  for await (const event of source) events.push(event);
  return events;
}

async function persistedText(root: string): Promise<string> {
  const values: string[] = [];
  for (const name of await readdir(root).catch(() => [])) {
    const path = join(root, name), info = await stat(path);
    if (info.isDirectory()) values.push(await persistedText(path));
    else if (info.isFile()) values.push(await readFile(path, "utf8").catch(() => ""));
  }
  return values.join("\n");
}

async function compileControlledNativePolicy(
  options: Parameters<typeof prepareCodexNativePolicy>[0]
): ReturnType<typeof prepareCodexNativePolicy> {
  const descriptor = Object.getOwnPropertyDescriptor(process, "platform");
  if (!descriptor) throw new Error("Controlled platform descriptor is unavailable");
  Object.defineProperty(process, "platform", { ...descriptor, value: "darwin" });
  try { return await prepareCodexNativePolicy(options); }
  finally { Object.defineProperty(process, "platform", descriptor); }
}

function engine(projectId: string, model: string, observed: AgentEngineRunInput[]): AgentEnginePort {
  const descriptor = { adapterId: "codex-app-server", providerId: "openai", capabilities: { credentials: false, tools: true, attachments: false, interruption: true, durableResume: true, compaction: false, runtimeControlTools: true } } as const;
  return {
    descriptor,
    subject: descriptor.adapterId,
    async preflight(input) { observed.push(input); },
    async *startTurn(input) {
      yield { type: "session:init", data: { engineSessionId: `${projectId}-provider`, adapterId: descriptor.adapterId, providerId: descriptor.providerId, model } };
      yield { type: "chat:complete", data: { text: `${projectId}:${input.opts.model}` } };
      yield { type: "process:exit", data: { exitCode: 0, interrupted: false } };
    },
    async interrupt() {}
  };
}

describe("hosted bootstrap public-to-private composition", () => {
  it("still fences and retires project admission when ceremony close fails during sign-out", async () => {
    const root = await realpath(await mkdtemp("/tmp/chirality-bootstrap-signout-"));
    cleanup.push(() => rm(root, { recursive: true, force: true }));
    const runtimeDirectory = join(root, "runtime"), projectRoot = join(root, "project");
    await mkdir(runtimeDirectory, { mode: 0o700 }); await mkdir(projectRoot);
    const retire = vi.fn(async () => {}), signOut = vi.fn(async () => {});
    const ceremony: TrustedHostedLoginCeremony = {
      async start() { return { loginId: "login", authUrl: "https://auth.example.test/login" }; },
      async status() { return { state: "completed" as const, hasAccount: true }; },
      async cancel() {},
      async close() { throw new Error("controlled close failure"); }
    };
    const bindings = {
      async createCeremony() { return ceremony; },
      async establishAdmission() { return { continuity: { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "private", accountEpoch: 1, policyDigest: "private" }, authority: { supplierGeneration: "supplier", identityGeneration: "identity", snapshotDigest: "d".repeat(64) }, retire }; },
      async materializeAdmission(input: { projectId: string }) { return { engine: engine(input.projectId, "fixture-model", []), selection: { adapterId: "codex-app-server", providerId: "openai", model: "fixture-model" } }; },
      signOut
    };
    const host = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory, daemonSocket: "runtime.sock", instructionRoot: resolve(process.cwd(), "../..") }, bindings);
    cleanup.push(() => host.stop());
    const bootstrap = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
    const registered = await bootstrap.initializeHostedBootstrapProject({ projectRoot });
    await bootstrap.grantHostedProviderNetworkConsent(registered.projectId);
    await bootstrap.startHostedBootstrapLogin(registered.projectId);
    expect(await bootstrap.hostedBootstrapStatus(registered.projectId)).toMatchObject({ ceremony: "signed-in", admission: "ready" });
    const retirementsBeforeSignOut = retire.mock.calls.length;
    await expect(bootstrap.signOutHostedProject(registered.projectId)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(signOut).toHaveBeenCalledTimes(1);
    expect(retire).toHaveBeenCalledTimes(retirementsBeforeSignOut + 1);
    expect(await bootstrap.hostedBootstrapStatus(registered.projectId)).toMatchObject({ ceremony: "failed", admission: "unavailable" });
  });

  it("carries native Plan through the admitted controlled supervisor and retains revisions after retirement", async () => {
    const root = await realpath(await mkdtemp("/tmp/chirality-bootstrap-plan-"));
    cleanup.push(() => rm(root, { recursive: true, force: true }));
    const runtimeDirectory = join(root, "runtime"), projectRoot = join(root, "bootstrap-plan");
    const brokerRoot = join(runtimeDirectory, "broker"), workerPrivate = join(brokerRoot, "worker"), codexHome = join(workerPrivate, "codex-home");
    await mkdir(runtimeDirectory, { mode: 0o700 }); await mkdir(projectRoot); await mkdir(codexHome, { recursive: true, mode: 0o700 });
    const selection = { adapterId: "codex-app-server", providerId: "openai", model: "fixture-model" };
    const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "b".repeat(64) };
    const identity: WorkerContinuity = { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "controlled-bootstrap", accountEpoch: 1, policyDigest: "controlled-policy" };
    let answerObserved = false; const observedMethods: string[] = [];
    const controlled = createControlledCodexSupervisorForTests({ identity, model: selection.model, allowUnauthenticatedModel: true, requestTimeoutMs: 1000, turnTimeoutMs: 5000, launch: async () => {
      const stdin = new PassThrough(), stdout = new PassThrough(); let buffered = "";
      const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
      stdin.on("data", chunk => {
        buffered += String(chunk);
        for (let newline = buffered.indexOf("\n"); newline >= 0; newline = buffered.indexOf("\n")) {
          const request = JSON.parse(buffered.slice(0, newline)); buffered = buffered.slice(newline + 1);
          observedMethods.push(String(request.method ?? request.id));
          if (request.method === "initialize") send({ id: request.id, result: {} });
          else if (request.method === "initialized") continue;
          else if (request.method === "account/read") send({ id: request.id, result: { requiresOpenaiAuth: false, account: null } });
          else if (request.method === "thread/start") {
            send({ method: "thread/started", params: { thread: { id: "bootstrap-provider-thread" } } });
            send({ id: request.id, result: { thread: { id: "bootstrap-provider-thread" }, approvalPolicy: "never", approvalsReviewer: "auto_review" } });
          } else if (request.method === "turn/start") {
            expect(request.params.collaborationMode.mode).toBe("plan");
            send({ id: request.id, result: { turn: { id: "bootstrap-provider-turn", status: "inProgress" } } });
            send({ method: "turn/started", params: { threadId: "bootstrap-provider-thread", turn: { id: "bootstrap-provider-turn", status: "inProgress" } } });
            send({ method: "turn/plan/updated", params: { threadId: "bootstrap-provider-thread", turnId: "bootstrap-provider-turn", plan: [{ step: "checklist only" }] } });
            send({ method: "item/plan/delta", params: { threadId: "bootstrap-provider-thread", turnId: "bootstrap-provider-turn", itemId: "plan", delta: "draft only" } });
            send({ method: "item/completed", params: { threadId: "bootstrap-provider-thread", turnId: "bootstrap-provider-turn", item: { id: "plan", type: "plan", text: "bootstrap authoritative plan" } } });
            send({ id: "bootstrap-question", method: "item/tool/requestUserInput", params: { threadId: "bootstrap-provider-thread", turnId: "bootstrap-provider-turn", itemId: "question", questions: [{ id: "scope", header: "Scope", question: "Which scope?", options: [{ label: "A", description: "First" }], isOther: true, isSecret: false }], isBlocking: true, autoResolutionMs: null } });
          } else if (request.id === "bootstrap-question" && request.result) {
            expect(request.result).toEqual({ answers: { scope: { answers: ["A"] } } }); answerObserved = true;
            send({ method: "serverRequest/resolved", params: { threadId: "bootstrap-provider-thread", requestId: "bootstrap-question" } });
            send({ method: "turn/completed", params: { threadId: "bootstrap-provider-thread", turn: { id: "bootstrap-provider-turn", status: "completed" } } });
          }
        }
      });
      return { pid: 14001, transport: { stdin, stdout, async close() { stdin.destroy(); stdout.destroy(); } } };
    } });
    cleanup.push(() => controlled.close());
    const supervisorSocket = join(runtimeDirectory, "controlled-supervisor.sock");
    const supervisorServer = await startSupervisorServer({ socketPath: supervisorSocket, supervisor: controlled });
    cleanup.push(() => supervisorServer.close());
    const supervisor = new SupervisorClient({ socketPath: supervisorSocket, credential: supervisorServer.credential });
    const immutableSystemRoot = await realpath("/usr/bin");
    let delegated: DelegatedRuntime | undefined; let retired = 0; let stagedPolicy: Awaited<ReturnType<typeof prepareCodexNativePolicy>> | undefined;
    let materializationFailure: unknown;
    const ceremony: TrustedHostedLoginCeremony = { async start() { return { loginId: "login", authUrl: "https://auth.example.test/login" }; }, async status() { return { state: "completed", hasAccount: true }; }, async cancel() {}, async close() {} };
    const bindings = {
      async createCeremony() { return ceremony; },
      async establishAdmission() { return { continuity: identity, authority: { supplierGeneration: "supplier", identityGeneration: "identity", snapshotDigest: "c".repeat(64) }, async retire() { retired++; await delegated?.close(); await controlled.close(); } }; },
      async materializeAdmission(input: { projectId: string; runtime: { nativePlanSink: DelegatedNativePlanSink; attachmentStagingRoot: string } }) {
        try {
          expect((await stat(input.runtime.attachmentStagingRoot)).isDirectory()).toBe(true);
          const policyInput = { canonicalRoot: projectRoot, privateDirectory: workerPrivate, codexHome, immutableReadRoots: [immutableSystemRoot], protectedPaths: [brokerRoot], readOnlyProjectPaths: [input.runtime.attachmentStagingRoot] };
          if (process.platform !== "darwin") await expect(prepareCodexNativePolicy(policyInput)).rejects.toThrow("Native policy requires macOS Seatbelt verification");
          const platformBeforeCompile = process.platform;
          stagedPolicy = await compileControlledNativePolicy(policyInput);
          expect(process.platform).toBe(platformBeforeCompile);
          cleanup.push(() => stagedPolicy?.cleanup() ?? Promise.resolve());
          expect(stagedPolicy.expectedPermissions.filesystem[projectRoot]).toBe("write");
          expect(stagedPolicy.expectedPermissions.filesystem[input.runtime.attachmentStagingRoot]).toBe("read");
          const consent = new HostedConsentStore({ canonicalRoot: projectRoot, codexHome: join(runtimeDirectory, "consent-home") });
          await consent.grant({ identity, posture: "off", approvedBy: "controlled-test", approvedAt: new Date(0).toISOString() });
          delegated = new DelegatedRuntime({ daemonId: "bootstrap-controlled", projects: new Map([[input.projectId, {
            identity, compatibility, supervisor, consent, retirement: new WorkerRetirementCoordinator({ directory: join(runtimeDirectory, "retirements") }),
            nativePlanSink: input.runtime.nativePlanSink, commandNetworkPosture: "off" as const, evidenceClass: "controlled-worker" as const,
            actual: { adapterId: selection.adapterId, providerId: selection.providerId, model: selection.model }
          }]]) });
          return { delegated, selection, compatibility, evidenceClass: "controlled-worker" as const };
        } catch (error) { materializationFailure = error; throw error; }
      }
    };
    const qualification = { adapterId: selection.adapterId, providerId: selection.providerId, qualificationId: "controlled-bootstrap-only", evidenceClass: "native-adapter-qualified" as const, admissionSha256: "a".repeat(64) };
    const host = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory, daemonSocket: "runtime.sock", instructionRoot: resolve(process.cwd(), "../..") }, bindings, qualification);
    cleanup.push(() => host.stop());
    const bootstrap = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
    const registered = await bootstrap.initializeHostedBootstrapProject({ projectRoot });
    expect(registered.projectId).toMatch(/^[0-9a-f-]{36}$/);
    await bootstrap.grantHostedProviderNetworkConsent(registered.projectId); await bootstrap.startHostedBootstrapLogin(registered.projectId);
    const admittedStatus = await bootstrap.hostedBootstrapStatus(registered.projectId);
    if (admittedStatus.admission !== "ready" && materializationFailure !== undefined) throw new Error("Controlled native Plan materialization failed", { cause: materializationFailure });
    expect(admittedStatus).toMatchObject({ ceremony: "signed-in", admission: "ready" });
    const client = new RuntimeClient({ socketPath: host.socketPath, tokenFile: resolveHostedProjectTokenFile(runtimeDirectory, registered.projectId) });
    const session = await client.createSession(registered.projectId, { projectId: registered.projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", interactionMode: "native-plan" });
    expect(await client.getNativePlanCapability(registered.projectId, session.sessionId)).toMatchObject({ status: "qualified", qualification });
    const turnId = "bootstrap-plan-turn";
    const turn = drain(await client.turnSession(registered.projectId, session.sessionId, { turnId, message: "Create a plan", interactionMode: "native-plan" }));
    await expect.poll(() => observedMethods, { timeout: 5_000 }).toContain("turn/start");
    await expect.poll(async () => (await client.listNativePlanClarifications(registered.projectId, session.sessionId)).clarifications.length, { timeout: 5_000 }).toBe(1);
    await client.replyNativePlanClarification(registered.projectId, session.sessionId, { requestId: "bootstrap-question", answers: { scope: { answers: ["A"] } } });
    await turn; expect(answerObserved).toBe(true);
    const beforeRetirement = await client.listNativePlanRevisions(registered.projectId, session.sessionId);
    expect(beforeRetirement.revisions).toHaveLength(1);
    expect(beforeRetirement.revisions[0]?.sourceEvent).toMatchObject({ binding: { projectId: registered.projectId, sessionId: session.sessionId, clientTurnId: turnId, providerThreadId: "bootstrap-provider-thread", providerTurnId: "bootstrap-provider-turn" }, plan: { text: "bootstrap authoritative plan" } });
    expect(JSON.stringify(beforeRetirement)).not.toContain("draft only");
    await bootstrap.cancelHostedBootstrapLogin(registered.projectId);
    expect(retired).toBe(1);
    expect(await client.getNativePlanCapability(registered.projectId, session.sessionId)).toMatchObject({ status: "unavailable" });
    await expect(client.replyNativePlanClarification(registered.projectId, session.sessionId, { requestId: "bootstrap-question", answers: { scope: { answers: ["A"] } } })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(await client.listNativePlanRevisions(registered.projectId, session.sessionId)).toEqual(beforeRetirement);
  }, 20_000);

  it("keeps ceremony coarse and project-isolated, then publishes the exact trusted engine on the same socket", async () => {
    const root = await realpath(await mkdtemp("/tmp/chirality-bootstrap-e2e-"));
    cleanup.push(() => rm(root, { recursive: true, force: true }));
    const runtimeDirectory = join(root, "runtime");
    await mkdir(runtimeDirectory, { mode: 0o700 });
    const observed: AgentEngineRunInput[] = [], retired: string[] = [], closed: string[] = [];
    const ceremonyManifests = new Map<string, string>();
    const ceremonies = new Map<string, TrustedHostedLoginCeremony>();
    const bindings = {
      async createCeremony(input: { projectId: string; manifestHash: string }) {
        ceremonyManifests.set(input.projectId, input.manifestHash);
        let cancelled = false;
        const ceremony: TrustedHostedLoginCeremony = {
          async start() { return { loginId: `login-${input.projectId}`, authUrl: `https://auth.example.test/${input.projectId}` }; },
          async status() { return cancelled ? { state: "failed" as const } : { state: "completed" as const, hasAccount: true }; },
          async cancel() { cancelled = true; },
          async close() { closed.push(input.projectId); }
        };
        ceremonies.set(input.projectId, ceremony);
        return ceremony;
      },
      async establishAdmission(input: { projectId: string; canonicalRoot: string }) {
        if (basename(input.canonicalRoot) === "signed-in-only") throw new Error("private producer unavailable");
        return {
          continuity: { canonicalRoot: input.canonicalRoot, cwd: input.canonicalRoot, accountId: `private-handle-${input.projectId}`, accountEpoch: 1, policyDigest: `private-policy-${input.projectId}` },
          authority: { supplierGeneration: `supplier-${input.projectId}`, identityGeneration: `identity-${input.projectId}`, snapshotDigest: "c".repeat(64) },
          async retire() { retired.push(input.projectId); }
        };
      },
      async materializeAdmission(input: { projectId: string }) {
        const model = `trusted-${input.projectId}`;
        return { engine: engine(input.projectId, model, observed), selection: { adapterId: "codex-app-server", providerId: "openai", model } };
      }
    };
    let host = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory, daemonSocket: "runtime.sock", instructionRoot: resolve(process.cwd(), "../.."), nativeAddonPath: join(runtimeDirectory, "not-loaded.node") }, bindings);
    cleanup.push(() => host.stop());
    const bootstrap = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });

    const roots = ["first", "second", "signed-in-only"].map(name => join(root, name));
    for (const projectRoot of roots) await mkdir(projectRoot);
    const registrations = [];
    for (const projectRoot of roots) registrations.push(await bootstrap.initializeHostedBootstrapProject({ projectRoot }));
    const [first, second, signedInOnly] = registrations;
    if (!first || !second || !signedInOnly) throw new Error("fixture registrations missing");

    for (const project of registrations) {
      expect(await bootstrap.hostedBootstrapStatus(project.projectId)).toMatchObject({ ceremony: "consent-required", admission: "unavailable", canStartLogin: false });
      expect(await bootstrap.grantHostedProviderNetworkConsent(project.projectId)).toMatchObject({ ceremony: "ready-to-start", admission: "unavailable", canStartLogin: true });
      expect(await bootstrap.startHostedBootstrapLogin(project.projectId)).toEqual({ loginId: `login-${project.projectId}`, authUrl: `https://auth.example.test/${project.projectId}` });
      await expect(bootstrap.startHostedBootstrapLogin(project.projectId)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    }
    for (const project of registrations) expect(ceremonyManifests.get(project.projectId)).toBe(project.manifestHash);
    expect(await bootstrap.hostedBootstrapStatus(signedInOnly.projectId)).toMatchObject({ ceremony: "signed-in", admission: "unavailable", canStartLogin: false });
    expect(await bootstrap.hostedBootstrapStatus(first.projectId)).toMatchObject({ ceremony: "signed-in", admission: "ready", canStartLogin: false });
    expect(await bootstrap.hostedBootstrapStatus(second.projectId)).toMatchObject({ ceremony: "signed-in", admission: "ready", canStartLogin: false });

    const projectClient = (projectId: string) => new RuntimeClient({ socketPath: host.socketPath, tokenFile: resolveHostedProjectTokenFile(runtimeDirectory, projectId) });
    const firstClient = projectClient(first.projectId), secondClient = projectClient(second.projectId);
    const firstSession = await firstClient.createSession(first.projectId, { projectId: first.projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite" });
    const secondSession = await secondClient.createSession(second.projectId, { projectId: second.projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite" });
    expect((await drain(await firstClient.turnSession(first.projectId, firstSession.sessionId, { message: "Use the trusted default model." }))).find(event => event.type === "chat:complete")).toMatchObject({ data: { text: `${first.projectId}:trusted-${first.projectId}` } });
    expect(observed.at(-1)).toMatchObject({ projectId: first.projectId, opts: { model: `trusted-${first.projectId}` } });

    await bootstrap.cancelHostedBootstrapLogin(first.projectId);
    expect(retired).toContain(first.projectId);
    expect(await bootstrap.hostedBootstrapStatus(second.projectId)).toMatchObject({ admission: "ready" });
    expect((await drain(await secondClient.turnSession(second.projectId, secondSession.sessionId, { message: "The other project's cancellation must not affect this turn." }))).find(event => event.type === "chat:complete")).toMatchObject({ data: { text: `${second.projectId}:trusted-${second.projectId}` } });
    expect(observed.at(-1)).toMatchObject({ projectId: second.projectId, opts: { model: `trusted-${second.projectId}` } });

    const firstFailure = await drain(await firstClient.turnSession(first.projectId, firstSession.sessionId, { message: "A retired admission must fail." }));
    expect(firstFailure).toContainEqual(expect.objectContaining({ type: "turn:error", data: expect.objectContaining({ fatal: true }) }));
    expect(await readFile(join(roots[0]!, "chirality.project.json"), "utf8")).not.toContain(`private-handle-${first.projectId}`);
    expect(JSON.stringify(await bootstrap.hostedBootstrapStatus(second.projectId))).not.toMatch(/private-handle|supplier-|identity-/u);
    const persistence = await persistedText(runtimeDirectory);
    for (const project of [first, second]) for (const secret of [`private-handle-${project.projectId}`, `supplier-${project.projectId}`, `identity-${project.projectId}`]) expect(persistence).not.toContain(secret);

    expect(await bootstrap.grantHostedProviderNetworkConsent(second.projectId)).toMatchObject({ ceremony: "ready-to-start", admission: "unavailable" });
    expect(retired).toContain(second.projectId);

    await host.stop();
    expect(closed.length).toBeGreaterThanOrEqual(3);
    host = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory, daemonSocket: "runtime.sock", instructionRoot: resolve(process.cwd(), "../..") }, bindings);
    const restarted = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
    expect(await restarted.hostedBootstrapStatus(second.projectId)).toMatchObject({ ceremony: "consent-required", admission: "unavailable" });
  }, 20_000);

  it("invalidates and retires private admission when the registered manifest drifts", async () => {
    const root = await realpath(await mkdtemp("/tmp/chirality-bootstrap-drift-"));
    cleanup.push(() => rm(root, { recursive: true, force: true }));
    const runtimeDirectory = join(root, "runtime"), projectRoot = join(root, "project");
    await mkdir(runtimeDirectory, { mode: 0o700 }); await mkdir(projectRoot);
    const retire = vi.fn(async () => {});
    const ceremony: TrustedHostedLoginCeremony = { async start() { return { loginId: "login", authUrl: "https://auth.example.test/login" }; }, async status() { return { state: "completed" as const, hasAccount: true }; }, async cancel() {}, async close() {} };
    const bindings = {
      async createCeremony() { return ceremony; },
      async establishAdmission() { return { continuity: { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "private", accountEpoch: 1, policyDigest: "private" }, authority: { supplierGeneration: "supplier", identityGeneration: "identity", snapshotDigest: "d".repeat(64) }, retire }; },
      async materializeAdmission() { return { engine: engine("drift", "trusted-drift", []), selection: { adapterId: "codex-app-server", providerId: "openai", model: "trusted-drift" } }; }
    };
    const host = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory, daemonSocket: "runtime.sock", instructionRoot: resolve(process.cwd(), "../..") }, bindings);
    cleanup.push(() => host.stop());
    const client = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
    const registered = await client.initializeHostedBootstrapProject({ projectRoot });
    await client.grantHostedProviderNetworkConsent(registered.projectId); await client.startHostedBootstrapLogin(registered.projectId);
    expect(await client.hostedBootstrapStatus(registered.projectId)).toMatchObject({ admission: "ready" });
    const manifestPath = join(projectRoot, "chirality.project.json");
    await writeFile(manifestPath, `${(await readFile(manifestPath, "utf8")).trim()} \n`, "utf8");
    await expect(client.hostedBootstrapStatus(registered.projectId)).rejects.toMatchObject({ code: "PROJECT_MANIFEST_DRIFT" });
    expect(retire).toHaveBeenCalledTimes(1);
  });

  it("exposes the authenticated catalog while admitted, fixes a validated choice per session, and refuses a model the account no longer offers", async () => {
    const root = await realpath(await mkdtemp("/tmp/chirality-bootstrap-catalog-"));
    cleanup.push(() => rm(root, { recursive: true, force: true }));
    const runtimeDirectory = join(root, "runtime"), projectRoot = join(root, "project");
    await mkdir(runtimeDirectory, { mode: 0o700 }); await mkdir(projectRoot);
    const entries = {
      full: [{ model: "gpt-default", isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["medium", "high"] }, { model: "gpt-alt", isDefault: false, defaultReasoningEffort: "low", supportedReasoningEfforts: ["low", "medium"] }],
      reduced: [{ model: "gpt-default", isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["medium", "high"] }]
    };
    const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "b".repeat(64) };
    const requests: DelegatedTurnRequest[] = [];
    const delegated = {
      async preflight(projectId: string, operationId: string) { return { ...compatibility, projectId, operationId, daemonId: "controlled-catalog", nonce: randomUUID() }; },
      async turn(_projectId: string, request: DelegatedTurnRequest, _tools: unknown[], observer: { onProgress(event: unknown): void }) {
        requests.push(structuredClone(request));
        observer.onProgress({ type: "started", providerThreadId: "thread-catalog", providerTurnId: `turn-${requests.length}` });
        return { event: {} as never, terminal: { turnId: request.turnId, workerId: request.turnId, generation: "g", outcome: "completed" as const, recordedAt: new Date().toISOString() }, output: `used:${request.model}:${request.reasoningEffort}`, providerThreadId: "thread-catalog", evidenceClass: "controlled-worker" as const };
      },
      async interruptTurn() { return { interrupted: true }; }
    } as unknown as DelegatedRuntime;
    let admissions = 0;
    const ceremony: TrustedHostedLoginCeremony = { async start() { return { loginId: "login", authUrl: "https://auth.example.test/login" }; }, async status() { return { state: "completed" as const, hasAccount: true }; }, async cancel() {}, async close() {} };
    const bindings = {
      async createCeremony() { return ceremony; },
      async establishAdmission() { return { continuity: { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "private-catalog", accountEpoch: 1, policyDigest: "private" }, authority: { supplierGeneration: "supplier", identityGeneration: "identity", snapshotDigest: "d".repeat(64) }, async retire() {} }; },
      async materializeAdmission() {
        const catalog = hostedModelCatalog(admissions++ === 0 ? entries.full : entries.reduced);
        return { delegated, selection: { adapterId: "codex-app-server", providerId: "openai", model: catalog.default.model }, compatibility, evidenceClass: "controlled-worker" as const, catalog };
      },
      async signOut() {}
    };
    const host = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory, daemonSocket: "runtime.sock", instructionRoot: resolve(process.cwd(), "../..") }, bindings);
    cleanup.push(() => host.stop());
    const bootstrap = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
    const registered = await bootstrap.initializeHostedBootstrapProject({ projectRoot });
    const projectId = registered.projectId;
    expect(await bootstrap.hostedBootstrapStatus(projectId)).toEqual({ schema: "chirality-hosted-bootstrap-status/v1", projectId, ceremony: "consent-required", admission: "unavailable", canStartLogin: false });
    await bootstrap.grantHostedProviderNetworkConsent(projectId);
    await bootstrap.startHostedBootstrapLogin(projectId);
    const ready = await bootstrap.hostedBootstrapStatus(projectId);
    expect(ready).toEqual({ schema: "chirality-hosted-bootstrap-status/v1", projectId, ceremony: "signed-in", admission: "ready", canStartLogin: false, models: entries.full, selection: { model: "gpt-default", reasoningEffort: "high" } });
    const client = new RuntimeClient({ socketPath: host.socketPath, tokenFile: resolveHostedProjectTokenFile(runtimeDirectory, projectId) });
    // A session cannot be created before admission for a model outside the catalog, nor with a partial or doubled selection.
    await expect(client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", modelSelection: { model: "gpt-unknown", reasoningEffort: "low" } })).rejects.toMatchObject({ code: "INVALID_REQUEST", status: 400, message: "Model 'gpt-unknown' is not in the authenticated Codex catalog", details: { reason: "MODEL_NOT_IN_CATALOG", model: "gpt-unknown", available: ["gpt-default", "gpt-alt"] } });
    await expect(client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", modelSelection: { model: "gpt-alt", reasoningEffort: "high" } })).rejects.toMatchObject({ code: "INVALID_REQUEST", status: 400, message: "Reasoning effort 'high' is not supported by 'gpt-alt'", details: { reason: "REASONING_EFFORT_UNSUPPORTED", model: "gpt-alt", supported: ["low", "medium"] } });
    await expect(client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", modelSelection: { model: "gpt-alt" } as never })).rejects.toMatchObject({ code: "INVALID_REQUEST", status: 400, details: { reason: "MODEL_SELECTION_INVALID" } });
    await expect(client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", modelSelection: { model: "gpt-alt", reasoningEffort: "low", extra: true } as never })).rejects.toMatchObject({ code: "INVALID_REQUEST", status: 400, details: { reason: "MODEL_SELECTION_INVALID" } });
    await expect(client.createSession(projectId, { projectId, role: "agent0", engineSelection: { adapterId: "codex-app-server", providerId: "openai", model: "gpt-alt" }, modelSelection: { model: "gpt-alt", reasoningEffort: "low" } })).rejects.toMatchObject({ code: "INVALID_REQUEST", status: 400, details: { reason: "MODEL_SELECTION_INVALID" } });
    expect(await client.listSessions(projectId)).toEqual([]);
    const chosen = await client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", modelSelection: { model: "gpt-alt", reasoningEffort: "medium" } });
    expect(chosen).toMatchObject({ engineSelection: { adapterId: "codex-app-server", providerId: "openai", model: "gpt-alt" }, reasoningEffort: "medium", schemaVersion: "chirality.session/v3" });
    expect(await client.getSession(projectId, chosen.sessionId)).toMatchObject({ engineSelection: { model: "gpt-alt" }, reasoningEffort: "medium" });
    const defaulted = await client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite" });
    expect(defaulted).toMatchObject({ engineSelection: { model: "gpt-default" }, reasoningEffort: "high" });
    const chosenEvents = await drain(await client.turnSession(projectId, chosen.sessionId, { message: "Use the chosen pair." }));
    expect(chosenEvents.find(event => event.type === "chat:complete")).toMatchObject({ data: { text: "used:gpt-alt:medium" } });
    expect(chosenEvents.find(event => event.type === "session:init")).toMatchObject({ data: { model: "gpt-alt" } });
    expect(requests.at(-1)).toMatchObject({ model: "gpt-alt", reasoningEffort: "medium", sessionId: chosen.sessionId });
    expect((await drain(await client.turnSession(projectId, defaulted.sessionId, { message: "Use the default pair." }))).find(event => event.type === "chat:complete")).toMatchObject({ data: { text: "used:gpt-default:high" } });
    expect(requests.at(-1)).toMatchObject({ model: "gpt-default", reasoningEffort: "high" });
    // The turn path never lets a client-supplied opts.model override the session's fixed model.
    const overridden = await drain(await client.turnSession(projectId, chosen.sessionId, { message: "Try to substitute.", opts: { model: "gpt-default" } }));
    expect(overridden).toContainEqual(expect.objectContaining({ type: "turn:error", data: expect.objectContaining({ fatal: true, details: { runtimeCode: "ENGINE_UNAVAILABLE", reason: "MODEL_SELECTION_MISMATCH" } }) }));
    expect(requests).toHaveLength(2);
    expect(await bootstrap.signOutHostedProject(projectId)).toEqual({ schema: "chirality-hosted-bootstrap-status/v1", projectId, ceremony: "consent-required", admission: "unavailable", canStartLogin: false });
    await bootstrap.grantHostedProviderNetworkConsent(projectId);
    await bootstrap.startHostedBootstrapLogin(projectId);
    expect(await bootstrap.hostedBootstrapStatus(projectId)).toMatchObject({ admission: "ready", models: entries.reduced, selection: { model: "gpt-default", reasoningEffort: "high" } });
    await expect(client.bootSession(projectId, chosen.sessionId)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", status: 503, details: { reason: "MODEL_NOT_IN_CATALOG", model: "gpt-alt", available: ["gpt-default"] } });
    const removed = await drain(await client.turnSession(projectId, chosen.sessionId, { message: "The model left the catalog." }));
    expect(removed).toContainEqual(expect.objectContaining({ type: "turn:error", data: expect.objectContaining({ fatal: true, details: { runtimeCode: "ENGINE_UNAVAILABLE", reason: "MODEL_NOT_IN_CATALOG" } }) }));
    expect(await client.getSession(projectId, chosen.sessionId)).toMatchObject({ engineSelection: { model: "gpt-alt" }, reasoningEffort: "medium" });
    expect((await drain(await client.turnSession(projectId, defaulted.sessionId, { message: "Still offered." }))).find(event => event.type === "chat:complete")).toMatchObject({ data: { text: "used:gpt-default:high" } });
    expect(requests).toHaveLength(3);
    const persisted = await persistedText(runtimeDirectory);
    expect(persisted).toMatch(/"reasoningEffort":\s*"medium"/);
  }, 20_000);

  it("cannot publish a late admission after cancellation", async () => {
    const root = await realpath(await mkdtemp("/tmp/chirality-bootstrap-cancel-"));
    cleanup.push(() => rm(root, { recursive: true, force: true }));
    const runtimeDirectory = join(root, "runtime"), projectRoot = join(root, "project");
    await mkdir(runtimeDirectory, { mode: 0o700 }); await mkdir(projectRoot);
    let release!: () => void, entered!: () => void, cancelEntered!: () => void;
    const gate = new Promise<void>(resolveGate => { release = resolveGate; });
    const establishmentEntered = new Promise<void>(resolveEntered => { entered = resolveEntered; });
    const cancellationEntered = new Promise<void>(resolveCancel => { cancelEntered = resolveCancel; });
    const retire = vi.fn(async () => {}), materialize = vi.fn(async () => ({ engine: engine("late", "trusted-late", []), selection: { adapterId: "codex-app-server", providerId: "openai", model: "trusted-late" } }));
    const ceremony: TrustedHostedLoginCeremony = { async start() { return { loginId: "login", authUrl: "https://auth.example.test/login" }; }, async status() { return { state: "completed" as const, hasAccount: true }; }, async cancel() { cancelEntered(); }, async close() {} };
    const host = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory, daemonSocket: "runtime.sock", instructionRoot: resolve(process.cwd(), "../..") }, {
      async createCeremony() { return ceremony; },
      async establishAdmission() { entered(); await gate; return { continuity: { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "late-private", accountEpoch: 1, policyDigest: "late-private" }, authority: { supplierGeneration: "late-supplier", identityGeneration: "late-identity", snapshotDigest: "e".repeat(64) }, retire }; },
      materializeAdmission: materialize
    });
    cleanup.push(() => host.stop());
    const client = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
    const registered = await client.initializeHostedBootstrapProject({ projectRoot });
    await client.grantHostedProviderNetworkConsent(registered.projectId); await client.startHostedBootstrapLogin(registered.projectId);
    const observing = client.hostedBootstrapStatus(registered.projectId);
    await establishmentEntered;
    const cancelled = client.cancelHostedBootstrapLogin(registered.projectId);
    await cancellationEntered;
    release();
    await observing;
    expect(await cancelled).toMatchObject({ ceremony: "cancelled", admission: "unavailable" });
    expect(await client.hostedBootstrapStatus(registered.projectId)).toMatchObject({ ceremony: "cancelled", admission: "unavailable" });
    expect(retire).toHaveBeenCalledTimes(1);
    expect(materialize).not.toHaveBeenCalled();
  });
});
