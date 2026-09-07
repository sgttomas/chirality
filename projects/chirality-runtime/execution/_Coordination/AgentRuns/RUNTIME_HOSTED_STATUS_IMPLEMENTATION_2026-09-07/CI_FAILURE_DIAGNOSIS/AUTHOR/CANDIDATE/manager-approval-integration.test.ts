import { PassThrough } from "node:stream";
import { chmod, mkdtemp, realpath, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, expect, it } from "vitest";
import { ApprovalStore, AuthRegistry, DelegatedRuntime, EngineRegistry, HostedConsentStore, ProjectRegistry, ResidencyCoordinator, RuntimeService, SessionStore, TurnCoordinator } from "@chirality/runtime-core";
import { RuntimeClient } from "@chirality/runtime-client";
import { RuntimeDaemon } from "../packages/daemon/src/runtime-daemon.js";
import { CodexAgent1ManagerPort } from "../packages/daemon/src/codex-manager.js";
import { createControlledCodexSupervisorForTests } from "../packages/daemon/src/codex-supervisor.js";
import { startSupervisorServer, SupervisorClient } from "../packages/daemon/src/supervisor-server.js";
import { createProjectFixture } from "./helpers.js";
const cleanup: (() => Promise<void>)[] = [];
afterEach(async () => { for (const close of cleanup.splice(0).reverse()) await close(); });
const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "a".repeat(64) };
async function fixture() {
  const directory = await realpath(await mkdtemp(join(tmpdir(), "ma-"))); cleanup.push(() => rm(directory, { recursive: true, force: true }));
  const project = join(directory, "project"); const { manifestPath } = await createProjectFixture(project, "project");
  await chmod(project, 0o700);
  const identity = { canonicalRoot: project, cwd: project, accountId: "fixture", accountEpoch: 1, policyDigest: "fixture-policy" };
  const consent = new HostedConsentStore({ canonicalRoot: project, codexHome: project });
  await consent.grant({ identity, posture: "ask-per-destination", approvedBy: "fixture-owner", approvedAt: "2026-09-06T00:00:00Z" });
  let notify: (value: unknown) => void = () => {}; let providerReplies = 0;
  const supervisor = createControlledCodexSupervisorForTests({ identity, model: "fixture", commandNetworkPosture: "ask-per-destination", turnTimeoutMs: 3000,
    async launch() {
      const stdin = new PassThrough(), stdout = new PassThrough(); notify = value => { stdout.write(JSON.stringify(value) + "\n"); };
      stdin.on("data", chunk => {
        for (const line of String(chunk).trim().split("\n")) {
          const request = JSON.parse(line);
          if (request.method === "initialized") continue;
          if (!request.method) {
            providerReplies++;
            notify({ method: "item/completed", params: { threadId: "manager-thread", turnId: "manager-turn", item: { id: "answer", type: "agentMessage", text: `manager:${request.result.decision}` } } });
            notify({ method: "turn/completed", params: { threadId: "manager-thread", turn: { id: "manager-turn", status: "completed" } } }); continue;
          }
          if (request.method === "thread/start") expect(request.params.dynamicTools.map((tool: any) => tool.name)).toEqual(["delegate_agent", "review"]);
          notify({ id: request.id, result: request.method === "account/read" ? { requiresOpenaiAuth: true, account: { type: "apiKey" } } : request.method === "thread/start" ? { thread: { id: "manager-thread" } } : request.method === "turn/start" ? { turn: { id: "manager-turn" } } : {} });
          if (request.method === "turn/start") setImmediate(() => notify({ id: "network-prompt", method: "item/commandExecution/requestApproval", params: { threadId: "manager-thread", turnId: "manager-turn", itemId: "network", startedAtMs: 1, networkApprovalContext: { host: "example.com", protocol: "https" }, availableDecisions: ["accept", "decline", "acceptForSession"] } }));
        }
      });
      return { pid: 12345, transport: { stdin, stdout, async close() {} } };
    }
  }); cleanup.push(() => supervisor.close());
  const server = await startSupervisorServer({ socketPath: join(directory, "private", "supervisor.sock"), supervisor, approvalCompatibility: compatibility }); cleanup.push(() => server.close());
  const channel = new SupervisorClient({ socketPath: join(directory, "private", "supervisor.sock"), credential: server.credential });
  const description = await channel.describeApprovalScope(); expect(description).toMatchObject({ identity, compatibility, model: "fixture", commandNetworkPosture: "ask-per-destination" }); expect(JSON.stringify(description)).not.toContain("token");
  let approvals!: DelegatedRuntime;
  const store = new ApprovalStore({ canonicalRoot: project, storageRoot: join(directory, "approval-control"), consent, isLive: binding => approvals.isApprovalLive(binding) });
  approvals = new DelegatedRuntime({ daemonId: "manager", approvalOnly: true, projects: new Map([["project", { identity, compatibility, supervisor: channel, consent, approvals: store, approvalForwardingEnabled: true, commandNetworkPosture: "ask-per-destination", evidenceClass: "controlled-worker" }]]) });
  const runtime = join(directory, "runtime"), projects = new ProjectRegistry(runtime), sessions = new SessionStore(runtime, projects), engines = new EngineRegistry();
  const residency = new ResidencyCoordinator({ async listStatus() { return []; }, async load() {}, async unload() {} }, runtime);
  const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency), new AuthRegistry(runtime), { async get() { return undefined; }, async status() { return { configured: false }; }, async set() {}, async remove() {} });
  const registered = await service.registerProject(manifestPath, "fixture-owner", "fixture-only");
  const daemon = new RuntimeDaemon({ socketPath: join(directory, "daemon.sock"), runtimeDirectory: runtime, service, approvals }); await daemon.start(); cleanup.push(() => daemon.stop());
  const client = new RuntimeClient({ socketPath: join(directory, "daemon.sock"), tokenFile: registered.tokenFile });
  const port = new CodexAgent1ManagerPort({ channel, async loadInstructions() { return "Controlled manager instructions"; }, approvals: { register: (session, worker, digest) => approvals.registerExternalApprovalWorker(session.projectId, worker, digest) } });
  const controller = new AbortController();
  const session = { sessionId: "runtime-manager-session", projectId: "project", projectRoot: project, role: "agent1", engineSelection: { adapterId: "codex-app-server", providerId: "openai", model: "fixture" } } as any;
  const events: any[] = []; const run = (async () => { for await (const event of port.execute(session, { brief: "approved controlled manager scope" } as any, { async delegate() { throw new Error("Unexpected delegation"); }, async review() { throw new Error("Unexpected review"); } }, controller.signal)) events.push(event); return events; })();
  void run.catch(() => {});
  let prompt: any;
  for (let i = 0; i < 100 && !prompt; i++) { prompt = (await client.pendingRuntimeApprovals("project") as any[])[0]; if (!prompt) await new Promise(resolve => setTimeout(resolve, 5)); }
  expect(prompt).toBeDefined();
  return { client, approvals, prompt, run, store, consent, identity, channel, controller, supervisor, replies: () => providerReplies, cancel: () => notify({ method: "serverRequest/resolved", params: { threadId: "manager-thread", requestId: "network-prompt" } }) };
}
it.each(["allow", "deny", "acceptForSession"] as const)("routes an actual manager prompt through approval-only public controls for %s", async decision => {
  const f = await fixture();
  expect(f.prompt.binding).toMatchObject({ sessionId: "runtime-manager-session", turnId: "runtime-manager-session", ...f.identity });
  expect(f.prompt.binding.scopeDigest).toMatch(/^[a-f0-9]{64}$/); expect(f.prompt.caveat).toContain("queued requests"); expect(f.replies()).toBe(0);
  await expect(f.client.runDelegatedTurn("project", compatibility, { turnId: "unauthorized-work", prompt: "not admitted" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  await expect(f.client.decideRuntimeApproval("project", f.prompt.requestId, { ...compatibility, contractBasisSha256: "b".repeat(64) }, { turnId: f.prompt.binding.turnId, workerGeneration: f.prompt.binding.workerGeneration, decision, approvedBy: "fixture-human", explicitUserAct: true })).rejects.toMatchObject({ code: "RUNTIME_COMPATIBILITY_MISMATCH" });
  await expect(f.client.decideRuntimeApproval("project", f.prompt.requestId, compatibility, { turnId: f.prompt.binding.turnId, workerGeneration: f.prompt.binding.workerGeneration, decision, approvedBy: "fixture-human", explicitUserAct: false as never })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  const response = await f.client.decideRuntimeApproval("project", f.prompt.requestId, compatibility, { turnId: f.prompt.binding.turnId, workerGeneration: f.prompt.binding.workerGeneration, decision, approvedBy: "fixture-human", explicitUserAct: true });
  expect(response.applied).toBe(true); expect(response.reason).toContain("not an execution acknowledgement");
  expect(await f.run).toContainEqual({ type: "chat:complete", data: { text: `manager:${decision === "allow" ? "accept" : decision === "deny" ? "decline" : decision}` } });
  expect(f.replies()).toBe(1); expect(await f.client.pendingRuntimeApprovals("project")).toEqual([]); expect(await f.supervisor.inventory()).toEqual([]);
});
it("does not carry cancelled or changed-consent manager approval authority", async () => {
  const f = await fixture();
  const changed = { ...f.prompt.binding, scopeDigest: "b".repeat(64) }; await expect(f.store.read(f.prompt.requestId, changed)).rejects.toMatchObject({ code: "FORBIDDEN" });
  await f.consent.grant({ identity: f.identity, posture: "off", approvedBy: "fixture-owner", approvedAt: "2026-09-06T00:00:01Z" });
  await expect(f.client.decideRuntimeApproval("project", f.prompt.requestId, compatibility, { turnId: f.prompt.binding.turnId, workerGeneration: f.prompt.binding.workerGeneration, decision: "allow", approvedBy: "fixture-human", explicitUserAct: true })).rejects.toMatchObject({ code: "FORBIDDEN" });
  f.cancel(); expect(await f.client.pendingRuntimeApprovals("project")).toEqual([]); expect(f.replies()).toBe(0);
  f.controller.abort(); await expect(f.run).rejects.toThrow(); expect(await f.supervisor.inventory()).toEqual([]);
});
