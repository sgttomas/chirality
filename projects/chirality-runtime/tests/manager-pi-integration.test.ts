import { createServer } from "node:http";
import { mkdir, mkdtemp, readFile, readdir, realpath, rm, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { afterEach, expect, it } from "vitest";
import { AuthRegistry, ProjectRegistry, type Agent1ManagerRuntimePort } from "@chirality/runtime-core";
import { RuntimeClient } from "@chirality/runtime-client";
import { startLocalDaemon, type LocalStandaloneConfig } from "../packages/daemon/src/standalone.js";
import { createProjectFixture } from "./helpers.js";
const cleanups: (() => Promise<unknown>)[] = [];
afterEach(async () => { for (const cleanup of cleanups.splice(0).reverse()) await cleanup(); });
async function fixture(review = true, skipRead = false, hold = false) {
  const root = await realpath(await mkdtemp(join(await realpath("/tmp"), "mp-"))); cleanups.push(() => rm(root, { recursive: true, force: true }));
  const runtimeDirectory = join(root, "r"), canonicalRoot = join(root, "p"); await mkdir(runtimeDirectory, { mode: 0o700 });
  const { manifestPath } = await createProjectFixture(canonicalRoot, "managed-pi");
  await writeFile(join(canonicalRoot, "authorized.txt"), "GOVERNED_BOUND_READ_OK", { mode: 0o600 });
  const requests: any[] = [];
  const server = createServer(async (req, res) => {
    if (req.headers.authorization !== "Bearer synthetic-manager-test") { res.writeHead(401).end(); return; }
    res.setHeader("content-type", "application/json");
    if (req.url === "/v1/models/status") { res.end(JSON.stringify({ models: [{ id: "fixture-model", kind: "llm", loaded: true }] })); return; }
    if (req.url !== "/v1/chat/completions") { res.writeHead(500).end(); return; }
    let data = ""; for await (const chunk of req) data += chunk;
    const body = JSON.parse(data); requests.push(body);
    if (hold) return;
    const toolReply = body.messages.some((message: any) => message.role === "tool");
    const done = toolReply || skipRead;
    res.end(JSON.stringify({ model: "fixture-model", choices: [{ finish_reason: done ? "stop" : "tool_calls", message: done ? { role: "assistant", content: "The bound file contains GOVERNED_BOUND_READ_OK" } : { role: "assistant", content: null, tool_calls: [{ id: "governed-read", type: "function", function: { name: "read_file", arguments: "{}" } }] } }] }));
  });
  await new Promise<void>(resolve => server.listen(0, "127.0.0.1", resolve));
  cleanups.push(() => new Promise<void>(resolve => { server.closeAllConnections(); server.close(() => resolve()); }));
  const projects = new ProjectRegistry(runtimeDirectory, {}); await projects.register(manifestPath, { approvedBy: "controlled-manager-fixture", approvalReference: "test-project-only" }, "manager-client");
  const tokenFile = (await new AuthRegistry(runtimeDirectory).issueClient("manager-client", ["runtime:read", "sessions:read", "sessions:write", "runs:write"], "managed-pi")).tokenFile;
  const manager: Agent1ManagerRuntimePort = { async *execute(session, _request, hooks) {
    yield { type: "session:init", data: { sessionId: session.sessionId, adapterId: "stub", providerId: "controlled-manager", model: "controlled-manager", resumed: false } };
    const child = await hooks.delegate({ sealedBrief: "Call the bound read_file tool with {} and report the authorized file contents." });
    if (review) await hooks.review({ childSessionId: child.childSessionId, decision: "accepted", rationale: "Controlled manager verified actual child return marker: " + child.returnText });
    yield { type: "chat:complete", data: { text: "Controlled manager reviewed actual Pi child: " + child.returnText } };
  } };
  const config: LocalStandaloneConfig = { schema: "chirality-standalone/v1", mode: "local-engine-only", runtimeDirectory, daemonSocket: "d.sock", project: { projectId: "managed-pi", canonicalRoot }, engine: { baseUrl: `http://127.0.0.1:${(server.address() as { port: number }).port}/v1`, model: { id: "fixture-model", contextWindow: 8192, maxTokens: 512 }, credentialFile: "never-written-memory-only.json", approvalReference: "controlled-resident-selection", turnTimeoutMs: 5000 } };
  const job = await startLocalDaemon(config, { async get() { return "synthetic-manager-test"; }, async status() { return { configured: true }; } }, { port: manager, selection: { adapterId: "stub", providerId: "controlled-manager", model: "controlled-manager" } }); cleanups.push(() => job.close());
  const client = new RuntimeClient({ socketPath: job.socketPath, tokenFile });
  const run = async () => { const frames = []; const stream = await client.runAgent1("managed-pi", { agentId: "WORKING_ITEMS", brief: "Delegate one authorized file read and review the return", approvalReference: "controlled-governed-run", localModel: "fixture-model", readOnlyTool: { name: "read_file", relativePath: "authorized.txt" } }); for await (const frame of stream) frames.push(frame); return frames; };
  return { client, run, requests, canonicalRoot, runtimeDirectory };
}
it("real coordinator creates, binds, executes and reviews actual SDK Pi child without seeded sessions", async () => {
  const f = await fixture(); expect(await f.client.listSessions("managed-pi")).toEqual([]);
  const frames = await f.run(); expect(JSON.stringify(frames)).toContain("Controlled manager reviewed actual Pi child");
  expect(frames.at(-1)).toMatchObject({ type: "process:exit", data: { exitCode: 0 } });
  const sessions = await f.client.listSessions("managed-pi"); expect(sessions).toHaveLength(2);
  const manager = sessions.find(session => session.role === "agent1")!, child = sessions.find(session => session.role === "agent2")!;
  expect(child.parentSessionId).toBe(manager.sessionId); expect(child.status).toBe("completed");
  const runRoot = join(f.canonicalRoot, "execution/_Coordination/AgentRuns/runtime");
  const names = await readdir(runRoot); expect(names).toHaveLength(1);
  const record = JSON.parse(await readFile(join(runRoot, names[0]!, "run.json"), "utf8"));
  expect(record).toMatchObject({ status: "completed", approvalReference: "controlled-governed-run", child: { permissions: ["read"], tool: "read_file", status: "completed", acceptance: { decision: "accepted" } } });
  const replay = await f.client.replaySession("managed-pi", child.sessionId);
  expect(JSON.stringify(replay)).toContain("tool.completed");
  expect(f.requests).toHaveLength(2);
  expect(f.requests[0].tools).toHaveLength(1);
  expect(f.requests[0].tools[0].function.parameters.properties).toEqual({});
});
it("does not close a real child run without manager review", async () => {
  const f = await fixture(false); const frames = await f.run();
  expect(frames.at(-1)).toMatchObject({ type: "process:exit", data: { exitCode: 1 } });
  expect(JSON.stringify(frames)).toContain("REQUIRED_DELEGATION_MISSING");
});
it("cannot satisfy the required bound read receipt using model text alone", async () => {
  const f = await fixture(true, true); const frames = await f.run();
  expect(frames.at(-1)).toMatchObject({ type: "process:exit", data: { exitCode: 1 } });
  expect(JSON.stringify(frames)).toContain("REQUIRED_DELEGATION_MISSING");
});

it("interrupts the actual coordinator and active Pi child through authenticated manager-session cancellation", async () => {
  const f = await fixture(true, false, true);
  const running = f.run();
  const deadline = Date.now() + 3000;
  while (f.requests.length === 0 && Date.now() < deadline) await new Promise(resolve => setTimeout(resolve, 10));
  expect(f.requests.length).toBe(1);
  const manager = (await f.client.listSessions("managed-pi")).find(session => session.role === "agent1")!;
  await f.client.interruptSession("managed-pi", manager.sessionId);
  const frames = await running;
  expect(frames.at(-1)).toMatchObject({ type: "process:exit", data: { exitCode: 1 } });
  expect(JSON.stringify(frames)).toContain("INTERRUPTED");
  const child = (await f.client.listSessions("managed-pi")).find(session => session.role === "agent2")!;
  expect(child.status).toBe("interrupted");
});
