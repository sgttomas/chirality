import { createServer } from "node:http";
import { mkdir, mkdtemp, realpath, rm, writeFile, readFile, readdir, chmod, symlink } from "node:fs/promises";
import { join } from "node:path";
import { afterEach, expect, it } from "vitest";
import { AuthRegistry, ProjectRegistry, type Agent1ManagerRuntimePort } from "@chirality/runtime-core";
import { RuntimeClient } from "@chirality/runtime-client";
import { readStandaloneConfig, startLocalDaemon, startStandaloneJob, type LocalStandaloneConfig } from "../packages/daemon/src/standalone.js";
import { createProjectFixture } from "./helpers.js";
const cleanups: (() => Promise<unknown>)[] = [];
afterEach(async () => { for (const cleanup of cleanups.splice(0).reverse()) await cleanup(); });
async function fixture() {
  const root = await realpath(await mkdtemp(join(await realpath("/tmp"), "pii-")));
  cleanups.push(() => rm(root, { recursive: true, force: true }));
  const runtimeDirectory = join(root, "r"), canonicalRoot = join(root, "p"); await mkdir(runtimeDirectory, { mode: 0o700 });
  const { manifestPath } = await createProjectFixture(canonicalRoot, "pi-project");
  await writeFile(join(canonicalRoot, "allowed.txt"), "bounded-read-result");
  const requests: { url: string; body: any }[] = []; let resident = true, hold = false, releaseObserved!: () => void;
  const observed = new Promise<void>(resolve => { releaseObserved = resolve; });
  const server = createServer(async (req, res) => {
    expect(req.headers.authorization).toBe("Bearer synthetic-local-secret");
    let bytes = ""; for await (const part of req) bytes += part;
    const body = bytes ? JSON.parse(bytes) : undefined; requests.push({ url: req.url!, body });
    res.setHeader("content-type", "application/json");
    if (req.url === "/v1/models/status") { res.end(JSON.stringify({ models: [{ id: "fixture-exact", kind: "llm", loaded: resident }] })); return; }
    if (req.url !== "/v1/chat/completions") { res.statusCode = 500; res.end("{}"); return; }
    releaseObserved(); if (hold) return;
    const toolReply = body.messages.some((message: any) => message.role === "tool");
    res.end(JSON.stringify({ id: "fixture-response", object: "chat.completion", model: "fixture-exact", choices: [{ index: 0, finish_reason: toolReply ? "stop" : "tool_calls", message: toolReply ? { role: "assistant", content: "Pi completed bounded read" } : { role: "assistant", content: null, tool_calls: [{ id: "read1", type: "function", function: { name: "read_file", arguments: "{}" } }] } }], usage: { prompt_tokens: 8, completion_tokens: 4, total_tokens: 12 } }));
  });
  await new Promise<void>(resolve => server.listen(0, "127.0.0.1", resolve));
  cleanups.push(() => new Promise<void>(resolve => { server.closeAllConnections(); server.close(() => resolve()); }));
  const port = (server.address() as { port: number }).port;
  const config: LocalStandaloneConfig = { schema: "chirality-standalone/v1", mode: "local-engine-only", runtimeDirectory, daemonSocket: "d.sock", project: { projectId: "pi-project", canonicalRoot }, engine: { baseUrl: `http://127.0.0.1:${port}/v1`, model: { id: "fixture-exact", contextWindow: 8192, maxTokens: 512 }, credentialFile: "omlx.json", approvalReference: "synthetic-resident-selection", turnTimeoutMs: 3000 } };
  await writeFile(join(runtimeDirectory, "omlx.json"), JSON.stringify({ providerId: "omlx", credential: "synthetic-local-secret" }), { mode: 0o600 });
  const configPath = join(runtimeDirectory, "config.json");
  const save = () => writeFile(configPath, JSON.stringify(config), { mode: 0o600 }); await save();
  const registry = new ProjectRegistry(runtimeDirectory, {}); await registry.register(manifestPath, { approvedBy: "fixture", approvalReference: "synthetic-governed-project" }, "fixture");
  const tokenFile = (await new AuthRegistry(runtimeDirectory).issueClient("fixture", ["runtime:read", "sessions:read", "sessions:write", "models:read", "runs:write"], "pi-project")).tokenFile;
  const manager: Agent1ManagerRuntimePort = { async *execute(session, _request, hooks) {
    yield { type: "session:init", data: { sessionId: session.sessionId, adapterId: "stub", providerId: "controlled-manager", model: "controlled-manager", resumed: false } };
    const child = await hooks.delegate({ sealedBrief: "Read the authorized file using read_file with {} and report its contents." });
    await hooks.review({ childSessionId: child.childSessionId, decision: "accepted", rationale: "Controlled manager reviewed actual child return" });
    yield { type: "chat:complete", data: { text: child.returnText } };
  } };
  const managerBinding = { port: manager, selection: { adapterId: "stub", providerId: "controlled-manager", model: "controlled-manager" } };
  const client = new RuntimeClient({ socketPath: join(runtimeDirectory, "d.sock"), tokenFile });
  const start = async () => { const job = await startLocalDaemon(config, undefined, managerBinding); cleanups.push(() => job.close()); return job; };
  return { config, configPath, save, client, managerBinding, start, requests, observed, setResident: (value: boolean) => { resident = value; }, setHold: () => { hold = true; } };
}
it("uses the actual Pi SDK through coordinator-created Agent 2 and one bound read tool", async () => {
  const f = await fixture(); await f.start();
  const stream = await f.client.runAgent1("pi-project", { brief: "Read allowed.txt and review", approvalReference: "synthetic-governed-run", localModel: "fixture-exact", readOnlyTool: { name: "read_file", relativePath: "allowed.txt" } });
  const frames = []; for await (const frame of stream) frames.push(frame);
  expect(JSON.stringify(frames)).toContain("Pi completed bounded read");
  expect(JSON.stringify(frames)).not.toContain("synthetic-local-secret");
  expect(f.requests.filter(request => request.url === "/v1/chat/completions")).toHaveLength(2);
  expect(f.requests.every(request => !/load|unload/.test(request.url))).toBe(true);
  expect(f.requests.find(request => request.body?.messages.some((message: any) => message.role === "tool"))?.body.messages).toEqual(expect.arrayContaining([expect.objectContaining({ role: "tool", content: expect.stringContaining("bounded-read-result") })]));
  await expect(readFile(join(f.config.runtimeDirectory, "s", "credential.json"))).rejects.toMatchObject({ code: "ENOENT" });
  await expect(f.client.createSession({ projectId: "pi-project", persona: "TASK", role: "agent2", engineSelection: { adapterId: "pi", providerId: "omlx", model: "fixture-exact" } })).rejects.toThrow();
});
it("interrupts the actual SDK pending loopback completion via authenticated client", async () => {
  const f = await fixture(); f.setHold(); await f.start();
  const stream = await f.client.runAgent1("pi-project", { brief: "Read and review", approvalReference: "synthetic-interrupt-run", localModel: "fixture-exact", readOnlyTool: { name: "read_file", relativePath: "allowed.txt" } });
  const collection = (async () => { const frames = []; for await (const frame of stream) frames.push(frame); return frames; })();
  await f.observed; const managerSession = (await f.client.listSessions("pi-project")).find(session => session.role === "agent1")!; await f.client.interruptSession("pi-project", managerSession.sessionId);
  expect(JSON.stringify(await collection)).toMatch(/interrupted|cancelled/);
});
it("rejects nonresident startup without loading or starting a supervisor", async () => {
  const f = await fixture(); f.setResident(false); await expect(f.start()).rejects.toThrow(/resident/);
  expect(f.requests.map(request => request.url)).toEqual(["/v1/models/status"]);
  await expect(startStandaloneJob("supervisor", f.configPath)).rejects.toThrow(/no supervisor/);
});
it("requires explicit private local credentials and refuses Codex fields, remote endpoint and aliases", async () => {
  const f = await fixture(); const credential = join(f.config.runtimeDirectory, f.config.engine.credentialFile);
  await chmod(credential, 0o644); await expect(readStandaloneConfig(f.configPath)).rejects.toThrow(); await chmod(credential, 0o600);
  await writeFile(f.configPath, JSON.stringify({ ...f.config, supervisorCredential: "unused.json" })); await expect(readStandaloneConfig(f.configPath)).rejects.toThrow(); await f.save();
  f.config.engine.baseUrl = "https://example.com/v1"; await f.save(); await expect(readStandaloneConfig(f.configPath)).rejects.toThrow();
  f.config.engine.baseUrl = "http://127.0.0.1:1/v1"; await f.save();
  await symlink(credential, join(f.config.runtimeDirectory, "alias.json")); f.config.engine.credentialFile = "alias.json"; await f.save(); await expect(readStandaloneConfig(f.configPath)).rejects.toThrow();
});

it("uses the same production composition with a memory-only credential port", async () => {
  const f = await fixture();
  await rm(join(f.config.runtimeDirectory, f.config.engine.credentialFile));
  const job = await startLocalDaemon(f.config, { async get(provider) { return provider === "omlx" ? "synthetic-local-secret" : undefined; }, async status() { return { configured: true }; } }, f.managerBinding);
  cleanups.push(() => job.close());
  const stream = await f.client.runAgent1("pi-project", { brief: "Read allowed.txt and review", approvalReference: "synthetic-governed-run", localModel: "fixture-exact", readOnlyTool: { name: "read_file", relativePath: "allowed.txt" } });
  const frames = []; for await (const frame of stream) frames.push(frame);
  expect(JSON.stringify(frames)).toContain("Pi completed bounded read");
  await expect(readFile(join(f.config.runtimeDirectory, f.config.engine.credentialFile))).rejects.toMatchObject({ code: "ENOENT" });
});

it.runIf(process.env["CHIRALITY_RUN_LIVE_OMLX"] === "1")("live local Pi managed integration: controlled manager, real coordinator and bounded read", async () => {
  const key = process.env["CHIRALITY_OMLX_API_KEY"];
  const evidenceDirectory = process.env["CHIRALITY_OMLX_EVIDENCE_DIR"];
  if (!key || !evidenceDirectory || !evidenceDirectory.startsWith("/")) throw new Error("Live harness requires memory credential and absolute evidence directory");
  const root = await realpath(await mkdtemp(join(await realpath("/tmp"), "pilive-")));
  cleanups.push(() => rm(root, { recursive: true, force: true }));
  const runtimeDirectory = join(root, "r"), canonicalRoot = join(root, "p");
  await mkdir(runtimeDirectory, { mode: 0o700 });
  const { manifestPath } = await createProjectFixture(canonicalRoot, "live-pi-fixture");
  const marker = "CHIRALITY_PI_BOUNDED_READ_7D3E";
  await writeFile(join(canonicalRoot, "evidence.txt"), marker, { mode: 0o600 });
  const projects = new ProjectRegistry(runtimeDirectory, {});
  await projects.register(manifestPath, { approvedBy: "parent-authorized-live-harness", approvalReference: "managed-Pi-integration-controlled-manager" }, "live-fixture");
  const tokenFile = (await new AuthRegistry(runtimeDirectory).issueClient("live-fixture", ["runtime:read", "sessions:read", "sessions:write", "runs:write"], "live-pi-fixture")).tokenFile;
  const model = "Qwen3.6-35B-A3B-8bit";
  const manager: Agent1ManagerRuntimePort = { async *execute(session, _request, hooks) {
    yield { type: "session:init", data: { sessionId: session.sessionId, adapterId: "stub", providerId: "controlled-manager", model: "controlled-manager", resumed: false } };
    const child = await hooks.delegate({ sealedBrief: "Call read_file with {} to read the one authorized file. Return exactly its contents; do not guess." });
    await hooks.review({ childSessionId: child.childSessionId, decision: child.returnText.includes(marker) ? "accepted" : "rejected", rationale: "Controlled manager compared returned marker against synthetic fixture" });
    yield { type: "chat:complete", data: { text: child.returnText } };
  } };
  const config: LocalStandaloneConfig = { schema: "chirality-standalone/v1", mode: "local-engine-only", runtimeDirectory, daemonSocket: "d.sock", project: { projectId: "live-pi-fixture", canonicalRoot }, engine: { baseUrl: "http://127.0.0.1:8000/v1", model: { id: model, contextWindow: 32768, maxTokens: 2048 }, credentialFile: "unused-memory-only.json", approvalReference: "parent-authorized-exact-resident-live-Pi-validation", turnTimeoutMs: 180000 } };
  let passed = false, boundedReadObserved = false, markerObserved = false;
  let finalStatus = "not-started";
  const diagnostics: { errorType: string; status?: number; phase: string; category: string }[] = [];
  const safeErrorTypes = new Set(["INVALID_REQUEST", "SDK_FAILURE", "PROVIDER_PROTOCOL_FAILURE", "PROVIDER_AUTH_FAILURE", "MODEL_UNAVAILABLE", "ENGINE_UNAVAILABLE", "CONTEXT_EXHAUSTED", "INTERRUPTED"]);
  const safeCategories: Record<string, string> = {
    "Unsupported local model answer": "unsupported-local-answer",
    "Local model response identity/choice mismatch": "model-identity-or-choice-mismatch",
    "Invalid local model tool calls": "invalid-local-tool-calls",
    "Missing local model tool calls": "missing-local-tool-calls",
    "Pi model request did not complete": "pi-model-request-incomplete",
    "Exact oMLX model is not resident": "model-not-resident",
    "Local model turn timed out": "local-turn-timeout"
  };
  try {
    const job = await startLocalDaemon(config, { async get(providerId) { return providerId === "omlx" ? key : undefined; }, async status(providerId) { return { configured: providerId === "omlx" }; } }, { port: manager, selection: { adapterId: "stub", providerId: "controlled-manager", model: "controlled-manager" } });
    cleanups.push(() => job.close());
    const client = new RuntimeClient({ socketPath: job.socketPath, tokenFile });
    const stream = await client.runAgent1("live-pi-fixture", { brief: "Delegate the authorized file read and review its returned marker", approvalReference: "parent-authorized-managed-live-Pi-validation", localModel: model, readOnlyTool: { name: "read_file", relativePath: "evidence.txt" } });
    for await (const frame of stream) {
      // Inspect transient canonical frames only; never persist raw frames or provider payloads.
      const serialized = JSON.stringify(frame);
      const event = frame as unknown as { type?: string; data?: Record<string, unknown> };
      if (event.type === "turn:error" && diagnostics.length < 8) {
        const data = event.data ?? {};
        diagnostics.push({ errorType: typeof data["errorType"] === "string" && safeErrorTypes.has(data["errorType"]) ? data["errorType"] : "OTHER",
          ...(typeof data["status"] === "number" && Number.isInteger(data["status"]) && data["status"] >= 100 && data["status"] <= 599 ? { status: data["status"] } : {}),
          phase: data["phase"] === "pre-stream" || data["phase"] === "mid-stream" ? data["phase"] : "unknown",
          category: typeof data["message"] === "string" ? safeCategories[data["message"]] ?? "unclassified-sanitized-error" : "unclassified-sanitized-error" });
      }
      if (serialized.includes(marker)) markerObserved = true;
      if (serialized.includes('"tool:result"') && serialized.includes('"name":"read_file"') && serialized.includes('"ok":true')) boundedReadObserved = true;
    }
    const records = await client.listSessions("live-pi-fixture");
    const parent = records.find(record => record.role === "agent1"), child = records.find(record => record.role === "agent2");
    finalStatus = parent?.status ?? "manager-session-missing";
    if (child !== undefined) {
      const replay = JSON.stringify(await client.replaySession("live-pi-fixture", child.sessionId));
      boundedReadObserved = replay.includes('"tool.completed"') && replay.includes("read_file");
    }
    const runRoot = join(canonicalRoot, "execution/_Coordination/AgentRuns/runtime");
    const runNames = await readdir(runRoot);
    const runRecord = runNames.length === 1 ? JSON.parse(await readFile(join(runRoot, runNames[0]!, "run.json"), "utf8")) : undefined;
    const reviewed = runRecord?.review?.decision === "accepted" && child?.parentSessionId === parent?.sessionId && child?.status === "completed";
    if (!reviewed) finalStatus = "governed-review-or-parentage-incomplete";
    passed = markerObserved && boundedReadObserved && finalStatus === "completed";
  } catch {
    // Avoid propagating provider errors, headers, response bodies or credential-bearing values.
    finalStatus = "sanitized-live-integration-failure";
  } finally {
    await mkdir(evidenceDirectory, { recursive: true, mode: 0o700 });
    await writeFile(join(evidenceDirectory, "PI_LIVE_MANAGED_INTEGRATION.json"), JSON.stringify({ schema: "chirality-pi-live-managed-integration/v1", model, adapter: "pi", sdkVersion: "0.82.0", provider: "omlx", endpoint: "literal-loopback-8000", passed, boundedReadObserved, markerObserved, finalStatus, diagnostics, scope: "real-client-daemon-coordinator-SDK-local-provider with coordinator-created child and bound read/review", managerEvidence: "controlled-manager-port", governedCoordinatorEntryProven: passed, hostedManagerProviderObserved: false, credentialStorage: "memory-only", rawProviderEvidencePersisted: false, tmRoot106Disposition: "unchanged" }, null, 2) + "\n", { mode: 0o600 });
  }
  expect(passed, "Live managed integration did not satisfy bounded-read, marker and terminal checks; see sanitized evidence").toBe(true);
}, 210000);
