import { PassThrough } from "node:stream";
import { mkdir, mkdtemp, readdir, readFile, realpath, rm, stat, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { hostedModelCatalog, type UIEvent, type WorkerContinuity } from "@chirality/runtime-contracts";
import { AuthRegistry, DelegatedRuntime, HostedConsentStore, ProjectRegistry, SessionStore, WorkerRetirementCoordinator, type DelegatedNativePlanSink } from "@chirality/runtime-core";
import {
  createControlledCodexSupervisorForTests,
  resolveHostedProjectTokenFile,
  startControlledHostedBootstrapRuntimeHostForTests,
  startControlledHostedRuntimeHostForTests,
  startSupervisorServer,
  SupervisorClient,
  type TrustedHostedLoginCeremony
} from "@chirality/runtime-daemon";
import { RuntimeClient } from "@chirality/runtime-client";
import { settledHostedBootstrapStatus } from "./helpers.js";

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

function controlledProvider(onSecretReply: () => void) {
  let launch = 0;
  return async () => {
    const currentLaunch = ++launch;
    const mode = currentLaunch === 3 ? "native-plan" : "chat";
    const stdin = new PassThrough(), stdout = new PassThrough();
    let buffer = "", providerThread = "provider-thread", providerTurn = "", toolRequested = false;
    const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
    stdin.on("data", chunk => {
      buffer += chunk.toString();
      for (let newline = buffer.indexOf("\n"); newline >= 0; newline = buffer.indexOf("\n")) {
        const line = buffer.slice(0, newline); buffer = buffer.slice(newline + 1);
        const request = JSON.parse(line);
        if (request.method === "initialize") send({ id: request.id, result: {} });
        else if (request.method === "initialized") continue;
        else if (request.method === "account/read") send({ id: request.id, result: { requiresOpenaiAuth: false, account: null } });
        else if (request.method === "thread/start" || request.method === "thread/resume") {
          if (request.method === "thread/resume") expect(request.params.threadId).toBe(providerThread);
          if (request.method === "thread/start") expect(request.params.dynamicTools.map((tool: { name: string }) => tool.name)).toContain("chirality_load_method");
          send({ method: "thread/started", params: { thread: { id: providerThread } } });
          send({ id: request.id, result: { thread: { id: providerThread }, approvalsReviewer: "auto_review", approvalPolicy: "never" } });
        } else if (request.method === "turn/start") {
          providerTurn = mode === "native-plan" ? "provider-plan-turn" : currentLaunch === 1 ? "provider-chat-turn" : "provider-cancel-turn";
          expect(request.params.collaborationMode.mode).toBe(mode === "chat" ? "default" : "plan");
          send({ id: request.id, result: { turn: { id: providerTurn, status: "inProgress" } } });
          send({ method: "turn/started", params: { threadId: providerThread, turn: { id: providerTurn, status: "inProgress" } } });
          if (currentLaunch === 1) {
            expect(request.params.input).toHaveLength(4);
            expect(request.params.input[0]).toMatchObject({ type: "text", text_elements: [] });
            expect(request.params.input[1]).toMatchObject({ type: "text", text: expect.stringContaining("large.txt") });
            expect(request.params.input[1].text).toContain("is staged at");
            expect(request.params.input[2]).toMatchObject({ type: "text", text: expect.stringContaining('attached PDF "brief.pdf"') });
            expect(request.params.input[3]).toMatchObject({ type: "localImage", path: expect.stringContaining("/.chirality/attachments/") });
            expect(JSON.stringify(request.params.input)).not.toContain("/selected/");
            toolRequested = true;
            send({ id: "load-request", method: "item/tool/call", params: { threadId: providerThread, turnId: providerTurn, callId: "load-call", tool: "chirality_load_method", arguments: { methods: [{ kind: "workflow", name: "authored-workflow" }] } } });
          } else if (mode === "chat") {
            send({ method: "item/agentMessage/delta", params: { threadId: providerThread, turnId: providerTurn, itemId: "unfinished", delta: "unfinished" } });
          } else {
            send({ method: "turn/plan/updated", params: { threadId: providerThread, turnId: providerTurn, plan: [{ step: "checklist is not a completed plan" }] } });
            send({ method: "item/plan/delta", params: { threadId: providerThread, turnId: providerTurn, itemId: "plan-item", delta: "non-authoritative delta" } });
            send({ method: "item/completed", params: { threadId: providerThread, turnId: providerTurn, item: { id: "plan-item", type: "plan", text: "authoritative completed plan" } } });
            send({ id: "string-request", method: "item/tool/requestUserInput", params: { threadId: providerThread, turnId: providerTurn, itemId: "questions-string", questions: [{ id: "scope", header: "Scope", question: "Which scope?", options: [{ label: "A", description: "First" }], isOther: true, isSecret: false }], isBlocking: true, autoResolutionMs: null } });
            send({ id: 9, method: "item/tool/requestUserInput", params: { threadId: providerThread, turnId: providerTurn, itemId: "questions-number", questions: [{ id: "mode", header: "Mode", question: "Which mode?", options: [], isOther: true, isSecret: false }, { id: "token", header: "Token", question: "Provide token", options: [], isOther: true, isSecret: true }], isBlocking: true, autoResolutionMs: null } });
          }
        } else if (request.id === "load-request" && request.result) {
          expect(toolRequested).toBe(true);
          expect(JSON.stringify(request.result)).toContain("AUTHORED_WORKFLOW_BODY");
          send({ method: "item/agentMessage/delta", params: { threadId: providerThread, turnId: "provider-chat-turn", itemId: "answer", delta: "chat " } });
          send({ method: "item/completed", params: { threadId: providerThread, turnId: "provider-chat-turn", item: { id: "answer", type: "agentMessage", text: "chat completed" } } });
          send({ method: "turn/completed", params: { threadId: providerThread, turn: { id: "provider-chat-turn", status: "completed" } } });
        } else if (request.id === "string-request" && request.result) {
          expect(request.result).toEqual({ answers: { scope: { answers: ["A"] } } });
          send({ method: "serverRequest/resolved", params: { threadId: providerThread, requestId: "string-request" } });
        } else if (request.id === 9 && request.result) {
          expect(request.result).toEqual({ answers: { mode: { answers: ["careful"] }, token: { answers: ["fixture-secret-never-persist"] } } });
          onSecretReply();
          send({ method: "serverRequest/resolved", params: { threadId: providerThread, requestId: 9 } });
          send({ method: "turn/completed", params: { threadId: providerThread, turn: { id: "provider-plan-turn", status: "completed" } } });
        } else if (request.method === "turn/interrupt") {
          expect(request.params).toEqual({ threadId: providerThread, turnId: providerTurn });
          send({ id: request.id, result: {} });
          send({ method: "turn/completed", params: { threadId: providerThread, turn: { id: providerTurn, status: "interrupted" } } });
        }
      }
    });
    return { pid: 12000 + launch, transport: { stdin, stdout, async close() { stdin.destroy(); stdout.destroy(); } } };
  };
}

describe("controlled Codex primary connecting path", () => {
  it("connects an ordinary client session through delegated transport, dynamic methods, and native Plan clarification", async () => {
    const directory = await realpath(await mkdtemp("/tmp/chirality-primary-"));
    cleanup.push(() => rm(directory, { recursive: true, force: true }));
    const projectRoot = join(directory, "project"), runtime = join(directory, "runtime");
    await mkdir(join(projectRoot, ".chirality", "workflows", "loader-only"), { recursive: true });
    await mkdir(join(projectRoot, ".chirality", "workflows", "authored-workflow"), { recursive: true });
    await writeFile(join(projectRoot, "AGENTS.md"), "# Controlled fixture project\n", "utf8");
    await writeFile(join(projectRoot, ".chirality", "workflows", "loader-only", "WORKFLOW.md"), "---\nname: loader-only\ndescription: Admit only the dynamic method loader.\n---\n", "utf8");
    await writeFile(join(projectRoot, ".chirality", "workflows", "loader-only", "execution.json"), `${JSON.stringify({ schema_version: 1, compatible_roles: ["HELP_HUMAN"], tools: { capabilities: ["chirality_load_method"] } })}\n`, "utf8");
    await writeFile(join(projectRoot, ".chirality", "workflows", "authored-workflow", "WORKFLOW.md"), "---\nname: authored-workflow\ndescription: Pre-existing workflow used by the controlled callback fixture.\n---\n\nAUTHORED_WORKFLOW_BODY\n", "utf8");
    const manifestPath = join(projectRoot, "chirality.project.json");
    const selection = { adapterId: "codex-app-server", providerId: "openai", model: "fixture-model" };
    await writeFile(manifestPath, `${JSON.stringify({ schemaVersion: "chirality.project/v2", projectId: "primary", displayName: "Controlled primary", workingRoot: ".", instructionRoot: { mode: "runtime" }, defaultExecutionRoot: ".", profiles: { domain: [], capability: [], dataBoundary: [] }, enabledAdapterIds: [selection.adapterId], embeddedUi: { declared: false } })}\n`, "utf8");
    await mkdir(runtime, { mode: 0o700 });
    const projects = new ProjectRegistry(runtime, { CHIRALITY_INSTRUCTION_ROOT: resolve(process.cwd(), "../..") });
    await projects.register(manifestPath, "controlled-test", "fixture-only");
    const tokenFile = (await new AuthRegistry(runtime).issueClient("fixture-only", ["runtime:read", "sessions:read", "sessions:write"], "primary")).tokenFile;
    const qualification = { adapterId: selection.adapterId, providerId: selection.providerId, qualificationId: "controlled-test-only", evidenceClass: "native-adapter-qualified" as const, admissionSha256: "a".repeat(64) };
    const identity: WorkerContinuity = { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "controlled-fixture", accountEpoch: 1, policyDigest: "controlled-policy" };
    const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "b".repeat(64) };
    const workerDirectory = join(runtime, "worker"), codexHome = join(workerDirectory, "codex-home"), executablePath = join(workerDirectory, "fixture-codex");
    await mkdir(codexHome, { recursive: true, mode: 0o700 });
    await writeFile(executablePath, "#!/bin/sh\nexit 1\n", { mode: 0o700 });
    await new HostedConsentStore({ canonicalRoot: projectRoot, codexHome }).grant({ identity, posture: "off", approvedBy: "controlled-test", approvedAt: new Date(0).toISOString() });
    const configPath = join(runtime, "hosted.json");
    await writeFile(configPath, `${JSON.stringify({
      schema: "chirality-standalone-hosted/v2", mode: "hosted-validation", runtimeDirectory: runtime,
      daemonSocket: "runtime.sock", supervisorSocket: "supervisor.sock", supervisorCredential: "supervisor-credential.json",
      project: { projectId: "primary", identity, compatibility, codexHome: "worker/codex-home", retirementDirectory: "retirements" },
      supplierAuthority: { enabled: false },
      worker: { executablePath, privateDirectory: "worker", model: selection.model, commandNetworkPosture: "off", managedAuth: { backend: "keyring", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } }, providerNetworkConsent: { approvedBy: "controlled-test", approvalReference: "fixture-only" }, maxRunMs: 5000 }
    })}\n`, { mode: 0o600 });
    const bootInput = { enabled: true as const, configPath, nativeAddonPath: join(runtime, "packaged-native-addon.node"), instructionRoot: resolve(process.cwd(), "../.."), selectedProject: { projectId: "primary", canonicalRoot: projectRoot, identity, compatibility }, nativePlanQualification: qualification };
    const provider = controlledProvider(() => { secretReplyObserved = true; });
    let secretReplyObserved = false;
    const newSupervisor = () => createControlledCodexSupervisorForTests({ identity, model: selection.model, allowUnauthenticatedModel: true, requestTimeoutMs: 2000, turnTimeoutMs: 5000, launch: provider });
    let supervisor = newSupervisor();
    let host = await startControlledHostedRuntimeHostForTests(bootInput, supervisor);
    cleanup.push(() => host.stop());
    const sessions = new SessionStore(runtime, projects);
    let client = new RuntimeClient({ socketPath: host.socketPath, tokenFile });
    const session = await client.createSession("primary", { projectId: "primary", roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", selectedMethods: [{ kind: "workflow", name: "loader-only" }] });
    const selected = join(directory, "selected");
    await mkdir(selected);
    const largeText = join(selected, "large.txt"), pdf = join(selected, "brief.pdf"), image = join(selected, "photo.png");
    await writeFile(largeText, "x".repeat(200 * 1024)); await writeFile(pdf, "%PDF-1.7\nfixture\n"); await writeFile(image, Buffer.from([0x89, 0x50, 0x4e, 0x47]));
    const chatEvents = await drain(await client.turnSession("primary", session.sessionId, { message: "Load the authored workflow through the controlled callback.", attachments: [largeText, pdf, image] }));
    expect(chatEvents.find(event => event.type === "chat:complete")).toMatchObject({ data: { text: "chat completed" } });
    expect(chatEvents.map(event => event.type)).toEqual(expect.arrayContaining(["session:init", "chat:delta", "chat:complete", "process:exit"]));
    expect(chatEvents.findIndex(event => event.type === "session:init")).toBeLessThan(chatEvents.findIndex(event => event.type === "chat:delta"));
    expect(chatEvents.findIndex(event => event.type === "chat:delta")).toBeLessThan(chatEvents.findIndex(event => event.type === "chat:complete"));
    expect((await sessions.get("primary", session.sessionId)).selectedMethods).toContainEqual(expect.objectContaining({ name: "authored-workflow", source: "project" }));
    expect(await supervisor.inventory()).toEqual([]);

    const cancelled = (await client.turnSession("primary", session.sessionId, { message: "Begin a turn that the consumer will cancel." }))[Symbol.asyncIterator]();
    const liveEvents: UIEvent[] = [];
    while (!liveEvents.some(event => event.type === "chat:delta")) {
      const next = await cancelled.next();
      expect(next.done, JSON.stringify(liveEvents)).toBe(false);
      liveEvents.push(next.value!);
    }
    expect(liveEvents[0]).toMatchObject({ type: "harness:event", data: { type: "turn.accepted" } });
    expect(liveEvents.findIndex(event => event.type === "session:init")).toBeGreaterThan(0);
    expect(liveEvents.findIndex(event => event.type === "session:init")).toBeLessThan(liveEvents.findIndex(event => event.type === "chat:delta"));
    expect(liveEvents.find(event => event.type === "chat:delta")).toMatchObject({ data: { text: "unfinished" } });
    await cancelled.return?.();
    await expect.poll(async () => (await supervisor.inventory()).length).toBe(0);
    // Worker retirement precedes the TurnCoordinator's authoritative session
    // persistence. Wait for that persisted state rather than treating an empty
    // supervisor inventory as a completion acknowledgement.
    await expect.poll(async () => (await sessions.get("primary", session.sessionId)).status).toBe("interrupted");

    await host.stop();
    supervisor = newSupervisor();
    host = await startControlledHostedRuntimeHostForTests(bootInput, supervisor);
    client = new RuntimeClient({ socketPath: host.socketPath, tokenFile });
    const planTurnId = "client-plan-turn";
    const planPromise = drain(await client.turnSession("primary", session.sessionId, { turnId: planTurnId, message: "Produce a completed plan.", interactionMode: "native-plan" }));
    await expect.poll(async () => (await client.listNativePlanClarifications("primary", session.sessionId)).clarifications.length).toBe(2);
    const pending = await client.listNativePlanClarifications("primary", session.sessionId);
    expect(pending.clarifications.map(value => value.requestId)).toEqual(["string-request", 9]);
    await client.replyNativePlanClarification("primary", session.sessionId, { requestId: "string-request", answers: { scope: { answers: ["A"] } } });
    await client.replyNativePlanClarification("primary", session.sessionId, { requestId: 9, answers: { mode: { answers: ["careful"] }, token: { answers: ["fixture-secret-never-persist"] } } });
    await planPromise;
    expect(secretReplyObserved).toBe(true);
    const revisions = await client.listNativePlanRevisions("primary", session.sessionId);
    expect(revisions.revisions).toHaveLength(1);
    expect(revisions.revisions[0]?.sourceEvent).toMatchObject({
      binding: { projectId: "primary", sessionId: session.sessionId, clientTurnId: planTurnId, providerThreadId: "provider-thread", providerTurnId: "provider-plan-turn" },
      plan: { id: "plan-item", type: "plan", text: "authoritative completed plan" }
    });
    expect(JSON.stringify(revisions)).not.toContain("non-authoritative delta");
    expect(JSON.stringify(await sessions.instructionBases.history("primary", session.sessionId))).not.toContain("fixture-secret-never-persist");
    expect(await persistedText(runtime)).not.toContain("fixture-secret-never-persist");
    expect(await readFile(join(projectRoot, ".chirality", "workflows", "authored-workflow", "WORKFLOW.md"), "utf8")).toContain("AUTHORED_WORKFLOW_BODY");
    expect(await supervisor.inventory()).toEqual([]);
  }, 20_000);
});

describe("controlled Codex primary connecting path with a catalog choice", () => {
  it("carries the session's chosen model and reasoning effort from the client to the provider's thread/start and turn/start", async () => {
    const directory = await realpath(await mkdtemp("/tmp/chirality-primary-catalog-"));
    cleanup.push(() => rm(directory, { recursive: true, force: true }));
    const projectRoot = join(directory, "project"), runtime = join(directory, "runtime");
    await mkdir(projectRoot); await mkdir(runtime, { mode: 0o700 });
    const brokerRoot = join(runtime, "broker"), workerPrivate = join(brokerRoot, "worker"), codexHome = join(workerPrivate, "codex-home");
    await mkdir(codexHome, { recursive: true, mode: 0o700 });
    const entries = [
      { model: "gpt-default", isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["medium", "high"] },
      { model: "gpt-alt", isDefault: false, defaultReasoningEffort: "low", supportedReasoningEfforts: ["low", "medium"] }
    ];
    const catalog = hostedModelCatalog(entries);
    const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "b".repeat(64) };
    const identity: WorkerContinuity = { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "controlled-catalog", accountEpoch: 1, policyDigest: "controlled-policy" };
    const observed: { method: string; params: any }[] = [];
    let launches = 0;
    const controlled = createControlledCodexSupervisorForTests({ identity, model: "gpt-default", reasoningEffort: "high", modelCatalog: entries, allowUnauthenticatedModel: true, requestTimeoutMs: 2000, turnTimeoutMs: 5000, launch: async () => {
      const launch = ++launches, threadId = `catalog-thread-${launch}`, turnId = `catalog-turn-${launch}`;
      const stdin = new PassThrough(), stdout = new PassThrough(); let buffered = "";
      const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
      stdin.on("data", chunk => {
        buffered += String(chunk);
        for (let newline = buffered.indexOf("\n"); newline >= 0; newline = buffered.indexOf("\n")) {
          const request = JSON.parse(buffered.slice(0, newline)); buffered = buffered.slice(newline + 1);
          if (request.method) observed.push({ method: request.method, params: request.params });
          if (request.method === "initialize") send({ id: request.id, result: {} });
          else if (request.method === "account/read") send({ id: request.id, result: { requiresOpenaiAuth: false, account: null } });
          else if (request.method === "thread/start") { send({ method: "thread/started", params: { thread: { id: threadId } } }); send({ id: request.id, result: { thread: { id: threadId }, approvalPolicy: "never", approvalsReviewer: "auto_review" } }); }
          else if (request.method === "turn/start") {
            send({ id: request.id, result: { turn: { id: turnId, status: "inProgress" } } });
            send({ method: "turn/started", params: { threadId, turn: { id: turnId, status: "inProgress" } } });
            send({ method: "item/completed", params: { threadId, turnId, item: { id: "answer", type: "agentMessage", text: `provider used ${request.params.model} at ${request.params.collaborationMode.settings.reasoning_effort}` } } });
            send({ method: "turn/completed", params: { threadId, turn: { id: turnId, status: "completed" } } });
          }
        }
      });
      return { pid: 15000 + launch, transport: { stdin, stdout, async close() { stdin.destroy(); stdout.destroy(); } } };
    } });
    cleanup.push(() => controlled.close());
    const supervisorSocket = join(runtime, "controlled-supervisor.sock");
    const supervisorServer = await startSupervisorServer({ socketPath: supervisorSocket, supervisor: controlled });
    cleanup.push(() => supervisorServer.close());
    const supervisor = new SupervisorClient({ socketPath: supervisorSocket, credential: supervisorServer.credential });
    let delegated: DelegatedRuntime | undefined;
    const ceremony: TrustedHostedLoginCeremony = { async start() { return { loginId: "login", authUrl: "https://auth.example.test/login" }; }, async status() { return { state: "completed", hasAccount: true }; }, async cancel() {}, async close() {} };
    const bindings = {
      async createCeremony() { return ceremony; },
      async establishAdmission() { return { continuity: identity, authority: { supplierGeneration: "supplier", identityGeneration: "identity", snapshotDigest: "c".repeat(64) }, async retire() { await delegated?.close(); } }; },
      async materializeAdmission(input: { projectId: string; runtime: { nativePlanSink: DelegatedNativePlanSink } }) {
        const consent = new HostedConsentStore({ canonicalRoot: projectRoot, codexHome: join(runtime, "consent-home") });
        await consent.grant({ identity, posture: "off", approvedBy: "controlled-test", approvedAt: new Date(0).toISOString() });
        delegated = new DelegatedRuntime({ daemonId: "bootstrap-catalog", projects: new Map([[input.projectId, {
          identity, compatibility, supervisor, consent, retirement: new WorkerRetirementCoordinator({ directory: join(runtime, "retirements") }),
          nativePlanSink: input.runtime.nativePlanSink, commandNetworkPosture: "off" as const, evidenceClass: "controlled-worker" as const,
          actual: { adapterId: "codex-app-server", providerId: "openai", model: catalog.default.model, reasoningEffort: catalog.default.defaultReasoningEffort }, catalog
        }]]) });
        return { delegated, selection: { adapterId: "codex-app-server", providerId: "openai", model: catalog.default.model }, compatibility, evidenceClass: "controlled-worker" as const, catalog };
      }
    };
    const host = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory: runtime, daemonSocket: "runtime.sock", instructionRoot: resolve(process.cwd(), "../..") }, bindings);
    cleanup.push(() => host.stop());
    const bootstrap = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
    const registered = await bootstrap.initializeHostedBootstrapProject({ projectRoot });
    const projectId = registered.projectId;
    await bootstrap.grantHostedProviderNetworkConsent(projectId); await bootstrap.startHostedBootstrapLogin(projectId);
    expect(await settledHostedBootstrapStatus(bootstrap, projectId)).toMatchObject({ admission: "ready", models: entries, selection: { model: "gpt-default", reasoningEffort: "high" } });
    const client = new RuntimeClient({ socketPath: host.socketPath, tokenFile: resolveHostedProjectTokenFile(runtime, projectId) });
    await expect(client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", modelSelection: { model: "gpt-elsewhere", reasoningEffort: "low" } })).rejects.toMatchObject({ code: "INVALID_REQUEST", status: 400, details: { reason: "MODEL_NOT_IN_CATALOG", model: "gpt-elsewhere", available: ["gpt-default", "gpt-alt"] } });
    const chosen = await client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", modelSelection: { model: "gpt-alt", reasoningEffort: "low" } });
    expect(chosen).toMatchObject({ engineSelection: { model: "gpt-alt" }, reasoningEffort: "low" });
    const chosenEvents = await drain(await client.turnSession(projectId, chosen.sessionId, { message: "Answer with the chosen pair." }));
    expect(chosenEvents.find(event => event.type === "chat:complete")).toMatchObject({ data: { text: "provider used gpt-alt at low" } });
    expect(chosenEvents.find(event => event.type === "session:init")).toMatchObject({ data: { model: "gpt-alt" } });
    expect(observed.find(entry => entry.method === "thread/start")?.params).toMatchObject({ model: "gpt-alt", cwd: projectRoot });
    expect(observed.find(entry => entry.method === "turn/start")?.params).toMatchObject({ model: "gpt-alt", collaborationMode: { mode: "default", settings: { model: "gpt-alt", reasoning_effort: "low" } } });
    observed.length = 0;
    const defaulted = await client.createSession(projectId, { projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite" });
    expect(defaulted).toMatchObject({ engineSelection: { model: "gpt-default" }, reasoningEffort: "high" });
    expect((await drain(await client.turnSession(projectId, defaulted.sessionId, { message: "Answer with the admitted default." }))).find(event => event.type === "chat:complete")).toMatchObject({ data: { text: "provider used gpt-default at high" } });
    expect(observed.find(entry => entry.method === "thread/start")?.params).toMatchObject({ model: "gpt-default" });
    expect(observed.find(entry => entry.method === "turn/start")?.params).toMatchObject({ model: "gpt-default", collaborationMode: { settings: { model: "gpt-default", reasoning_effort: "high" } } });
    expect(launches).toBe(2);
    await expect.poll(async () => (await controlled.inventory()).length).toBe(0);
    const sessions = new SessionStore(runtime, new ProjectRegistry(runtime, { CHIRALITY_INSTRUCTION_ROOT: resolve(process.cwd(), "../..") }));
    expect(await sessions.get(projectId, chosen.sessionId)).toMatchObject({ engineSelection: { model: "gpt-alt" }, reasoningEffort: "low" });
    const replay = await client.replaySession(projectId, chosen.sessionId);
    expect(JSON.stringify(replay)).toContain("gpt-alt");
  }, 20_000);
});
