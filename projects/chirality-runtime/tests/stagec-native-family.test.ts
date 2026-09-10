import { createHash } from "node:crypto";
import { mkdtemp, mkdir, realpath, rm, writeFile } from "node:fs/promises";
import { PassThrough } from "node:stream";
import { afterEach, describe, expect, it } from "vitest";
import { CodexTurnSession, type CodexDynamicTool } from "../packages/daemon/src/codex-session.js";
import { digestCodexNativeToolDefinitionsV1 } from "../packages/daemon/src/codex-native-tools.js";

const roots: string[] = [];
const sha = (value: string) => createHash("sha256").update(value).digest("hex");
afterEach(async () => { await Promise.all(roots.splice(0).map(root => rm(root, { recursive: true, force: true }))); });

async function fixture(turnTimeoutMs = 1000) {
  const root = await realpath(await mkdtemp("/tmp/chirality-c-family-")); roots.push(root);
  const roles = ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"] as const;
  const roleDirectory = `${root}/roles`; await mkdir(roleDirectory);
  const roleFiles: Record<string, string> = {}, roleInstructions: Record<string, string> = {};
  for (const role of roles) {
    const instruction = `Exact ${role} child instruction.`; roleInstructions[role] = instruction;
    const path = `${roleDirectory}/${role}.toml`; roleFiles[role] = path;
    await writeFile(path, `developer_instructions = ${JSON.stringify(instruction)}\n`);
  }
  const expected = { filesystem: { "/usr": "read", [root]: "write", [`${root}/protected`]: "deny" }, network: { enabled: false } } as const;
  const configOverrides = ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2"];
  for (const role of roles) configOverrides.push(`agents.${role}.description=${JSON.stringify(role)}`, `agents.${role}.config_file=${JSON.stringify(roleFiles[role])}`);
  const stdin = new PassThrough(), stdout = new PassThrough(); let buffered = "";
  const requests: any[] = [], responses: any[] = [], contexts: any[] = [], aborted: string[] = [], rootOnlyCalls: unknown[] = [];
  const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
  const tool: CodexDynamicTool = { name: "chirality_list_methods", description: "List methods", inputSchema: { type: "object", additionalProperties: false }, async handler(_args, context) {
    contexts.push({ ...context, signal: undefined });
    if (context.callId === "blocked") await new Promise<void>((_resolve, reject) => context.signal.addEventListener("abort", () => { aborted.push(context.callId); reject(new Error("aborted")); }, { once: true }));
    return { success: true, contentItems: [{ type: "inputText", text: "child-result" }] };
  } };
  const rootOnly: CodexDynamicTool = { name: "chirality_request_method_change", description: "Change root methods", inputSchema: { type: "object", additionalProperties: false }, async handler(args) {
    rootOnlyCalls.push(args); return { success: true, contentItems: [] };
  } };
  stdin.on("data", chunk => {
    buffered += String(chunk); let newline: number;
    while ((newline = buffered.indexOf("\n")) >= 0) {
      const raw = buffered.slice(0, newline); buffered = buffered.slice(newline + 1); if (!raw) continue;
      const request = JSON.parse(raw); requests.push(request);
      if (request.method === "initialize") send({ id: request.id, result: {} });
      else if (request.method === "initialized") undefined;
      else if (request.method === "config/read") send({ id: request.id, result: { config: { permissions: { bound: expected }, approvals_reviewer: "user", approval_policy: "never", allow_login_shell: false, features: { shell_snapshot: false, plugins: false, remote_plugin: false, network_proxy: false, multi_agent: true, multi_agent_v2: false }, agents: { enabled: true, max_depth: 2, ...Object.fromEntries(roles.map(role => [role, { description: role, config_file: roleFiles[role] }])) }, chirality_runtime: { nativeSkills: "disabled" } } } });
      else if (request.method === "thread/start" || request.method === "thread/resume") send({ method: "thread/started", params: { thread: { id: "root-thread" } } }), send({ id: request.id, result: { thread: { id: "root-thread" }, approvalsReviewer: "user", approvalPolicy: "never" } });
      else if (request.method === "turn/start") send({ id: request.id, result: { turn: { id: "root-turn" } } }), send({ method: "turn/started", params: { threadId: "root-thread", turn: { id: "root-turn", status: "inProgress" } } });
      else if (request.method === "turn/interrupt") send({ id: request.id, result: {} }), send({ method: "turn/completed", params: { threadId: "root-thread", turn: { id: "root-turn", status: "interrupted" } } });
      else if (request.id !== undefined) responses.push(request);
    }
  });
  const session = new CodexTurnSession({ transport: { stdin, stdout, async close() { stdin.destroy(); stdout.destroy(); } }, permissionProfile: "bound", policyDigest: "b".repeat(64), nativeSkills: "disabled", dynamicTools: [tool, rootOnly], turnTimeoutMs });
  await session.initialize();
  await session.verifyNativePolicy(expected, { digest: "d".repeat(64), configOverrides });
  const declarations = [{ name: tool.name, description: tool.description, inputSchema: tool.inputSchema }];
  await session.installInheritableTools(declarations);
  (session as unknown as { supplierGeneration: string }).supplierGeneration = "supplier-1";
  return { session, requests, responses, contexts, aborted, rootOnlyCalls, send, declarations, roleInstructions, root };
}

describe("Stage C native child family", () => {
  it("carries the exact subset on start/resume and waits for child callbacks and family settlement", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      expect(f.requests.find(value => value.method === "thread/start").params.chiralityRuntime).toEqual({ schema: "chirality-native-tools/v1", inheritableTools: f.declarations });
      const turnId = await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      const waiting = f.session.waitTurn(turnId); let settled = false; void waiting.then(() => { settled = true; });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "a".repeat(32), parentThreadId: "root-thread", parentTurnId: "root-turn", childThreadId: "child-thread", childTurnId: "child-turn", selectedRole: { kind: "configured", name: "HELP_HUMAN", basisDigest: sha(f.roleInstructions.HELP_HUMAN) }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
      f.send({ id: "child-call-request", method: "item/tool/call", params: { threadId: "child-thread", turnId: "child-turn", callId: "child-call", tool: "chirality_list_methods", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId: "a".repeat(32) } } });
      await new Promise<void>(resolve => setImmediate(resolve));
      expect(f.requests.find(value => value.id === "child-call-request")?.result).toEqual({ success: true, contentItems: [{ type: "inputText", text: "child-result" }] });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "b".repeat(32), parentThreadId: "child-thread", parentTurnId: "child-turn", childThreadId: "grandchild-thread", childTurnId: "grandchild-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
      f.send({ id: "grandchild-call-request", method: "item/tool/call", params: { threadId: "grandchild-thread", turnId: "grandchild-turn", callId: "grandchild-call", tool: "chirality_list_methods", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId: "b".repeat(32) } } });
      await new Promise<void>(resolve => setImmediate(resolve));
      expect(f.requests.find(value => value.id === "grandchild-call-request")?.result).toEqual({ success: true, contentItems: [{ type: "inputText", text: "child-result" }] });
      expect(f.contexts.find(value => value.callId === "grandchild-call")?.nativeChild).toMatchObject({ associationId: "b".repeat(32), rootThreadId: "root-thread", rootTurnId: "root-turn", parentThreadId: "child-thread", parentTurnId: "child-turn" });
      f.send({ method: "chirality/nativeChild/turnFinished", params: { schema: "chirality-native-child-terminal/v1", supplierGeneration: "supplier-1", associationId: "a".repeat(32), childThreadId: "child-thread", childTurnId: "child-turn", reason: "completed" } });
      f.send({ method: "turn/completed", params: { threadId: "root-thread", turn: { id: "root-turn", status: "completed" } } });
      await new Promise<void>(resolve => setImmediate(resolve)); expect(settled).toBe(false);
      f.send({ method: "chirality/nativeChild/turnFinished", params: { schema: "chirality-native-child-terminal/v1", supplierGeneration: "supplier-1", associationId: "b".repeat(32), childThreadId: "grandchild-thread", childTurnId: "grandchild-turn", reason: "completed" } });
      f.send({ method: "chirality/nativeChild/familySettled", params: { schema: "chirality-native-family-settled/v1", supplierGeneration: "supplier-1", rootThreadId: "root-thread", rootTurnId: "root-turn" } });
      await expect(waiting).resolves.toMatchObject({ status: "completed" });
      await f.session.resumeThread({ threadId: "root-thread", model: "model", continuityChecked: true });
      expect(f.requests.find(value => value.method === "thread/resume").params.chiralityRuntime).toEqual({ schema: "chirality-native-tools/v1", inheritableTools: f.declarations });
    } finally { await f.session.close(); }
  });

  it("rejects new descendants after their immediate parent is terminal", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "a".repeat(32), parentThreadId: "root-thread", parentTurnId: "root-turn", childThreadId: "child-thread", childTurnId: "child-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
      f.send({ method: "chirality/nativeChild/turnFinished", params: { schema: "chirality-native-child-terminal/v1", supplierGeneration: "supplier-1", associationId: "a".repeat(32), childThreadId: "child-thread", childTurnId: "child-turn", reason: "completed" } });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "b".repeat(32), parentThreadId: "child-thread", parentTurnId: "child-turn", childThreadId: "late-grandchild", childTurnId: "late-grandchild-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
      await expect(f.session.waitTurn("root-turn")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    } finally { await f.session.close(); }
  });

  it("scopes equal provider call IDs to exact child tuples", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      for (const [associationId, childThreadId, childTurnId] of [["a".repeat(32), "child-one", "turn-one"], ["b".repeat(32), "child-two", "turn-two"]] as const) {
        f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId, parentThreadId: "root-thread", parentTurnId: "root-turn", childThreadId, childTurnId, selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
        f.send({ id: `request-${associationId[0]}-${childThreadId}`, method: "item/tool/call", params: { threadId: childThreadId, turnId: childTurnId, callId: "same-call", tool: "chirality_list_methods", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId } } });
      }
      await new Promise<void>(resolve => setImmediate(resolve));
      expect(f.responses.filter(value => value.result?.success === true)).toHaveLength(2);
      expect(f.contexts.filter(value => value.callId === "same-call").map(value => value.nativeChild.associationId).sort()).toEqual(["a".repeat(32), "b".repeat(32)]);
      f.send({ id: "duplicate", method: "item/tool/call", params: { threadId: "child-one", turnId: "turn-one", callId: "same-call", tool: "chirality_list_methods", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId: "a".repeat(32) } } });
      await new Promise<void>(resolve => setImmediate(resolve));
      expect(f.contexts.filter(value => value.callId === "same-call" && value.nativeChild.associationId === "a".repeat(32))).toHaveLength(1);
      expect(f.responses.find(value => value.id === "duplicate")?.result?.success).toBe(true);
      f.send({ id: "mismatched", method: "item/tool/call", params: { threadId: "child-two", turnId: "turn-two", callId: "same-call", tool: "chirality_list_methods", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId: "a".repeat(32) } } });
      await expect(f.session.waitTurn("root-turn")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    } finally { await f.session.close(); }
  });

  it("cancels an outstanding grandchild callback with its root family", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "a".repeat(32), parentThreadId: "root-thread", parentTurnId: "root-turn", childThreadId: "child", childTurnId: "child-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "b".repeat(32), parentThreadId: "child", parentTurnId: "child-turn", childThreadId: "grandchild", childTurnId: "grandchild-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
      f.send({ id: "blocked-request", method: "item/tool/call", params: { threadId: "grandchild", turnId: "grandchild-turn", callId: "blocked", tool: "chirality_list_methods", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId: "b".repeat(32) } } });
      await new Promise<void>(resolve => setImmediate(resolve));
      const foreignController = new AbortController(), internal = f.session as any;
      internal.nativeChildAssociations.set("f".repeat(32), { associationId: "f".repeat(32), supplierGeneration: "supplier-1", rootThreadId: "different-root-thread", rootTurnId: "root-turn", parentThreadId: "different-root-thread", parentTurnId: "root-turn", childThreadId: "foreign-child", childTurnId: "foreign-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations), live: true });
      internal.toolCalls.set("foreign-call", { signature: "foreign", threadId: "foreign-child", turnId: "foreign-turn", associationId: "f".repeat(32), controller: foreignController, done: Promise.resolve({ success: true, contentItems: [] }), completed: false });
      const waiting = f.session.waitTurn("root-turn"); await f.session.interrupt("root-turn");
      await new Promise<void>(resolve => setImmediate(resolve)); expect(f.aborted).toEqual(["blocked"]);
      expect(foreignController.signal.aborted).toBe(false); internal.toolCalls.delete("foreign-call"); internal.nativeChildAssociations.delete("f".repeat(32));
      f.send({ method: "chirality/nativeChild/turnFinished", params: { schema: "chirality-native-child-terminal/v1", supplierGeneration: "supplier-1", associationId: "b".repeat(32), childThreadId: "grandchild", childTurnId: "grandchild-turn", reason: "cancelled" } });
      f.send({ method: "chirality/nativeChild/turnFinished", params: { schema: "chirality-native-child-terminal/v1", supplierGeneration: "supplier-1", associationId: "a".repeat(32), childThreadId: "child", childTurnId: "child-turn", reason: "cancelled" } });
      f.send({ method: "chirality/nativeChild/familySettled", params: { schema: "chirality-native-family-settled/v1", supplierGeneration: "supplier-1", rootThreadId: "root-thread", rootTurnId: "root-turn" } });
      await expect(waiting).resolves.toMatchObject({ status: "interrupted" });
    } finally { await f.session.close(); }
  });

  it("rejects a callback before its Supplier association", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      f.send({ id: "child-call-request", method: "item/tool/call", params: { threadId: "child-thread", turnId: "child-turn", callId: "child-call", tool: "chirality_list_methods", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId: "a".repeat(32) } } });
      await expect(f.session.waitTurn("root-turn")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    } finally { await f.session.close(); }
  });

  it("rejects a valid child callback for a root-only control tool without dispatching it", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "a".repeat(32), parentThreadId: "root-thread", parentTurnId: "root-turn", childThreadId: "child-thread", childTurnId: "child-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
      f.send({ id: "root-only-request", method: "item/tool/call", params: { threadId: "child-thread", turnId: "child-turn", callId: "root-only-call", tool: "chirality_request_method_change", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId: "a".repeat(32) } } });
      await expect(f.session.waitTurn("root-turn")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      expect(f.rootOnlyCalls).toEqual([]);
      expect(f.contexts).toEqual([]);
    } finally { await f.session.close(); }
  });

  it("rejects an association whose inherited definitions do not match the root declaration", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "a".repeat(32), parentThreadId: "root-thread", parentTurnId: "root-turn", childThreadId: "child-thread", childTurnId: "child-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: "0".repeat(64) } });
      await expect(f.session.waitTurn("root-turn")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    } finally { await f.session.close(); }
  });

  it("holds zero-child completion for the barrier and permanently rejects late family work", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      const waiting = f.session.waitTurn("root-turn"); let settled = false; void waiting.then(() => { settled = true; });
      f.send({ method: "turn/completed", params: { threadId: "root-thread", turn: { id: "root-turn", status: "completed" } } });
      await new Promise<void>(resolve => setImmediate(resolve)); expect(settled).toBe(false);
      f.send({ method: "chirality/nativeChild/familySettled", params: { schema: "chirality-native-family-settled/v1", supplierGeneration: "supplier-1", rootThreadId: "root-thread", rootTurnId: "root-turn" } });
      await expect(waiting).resolves.toMatchObject({ status: "completed" });
      f.send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: "supplier-1", associationId: "c".repeat(32), parentThreadId: "root-thread", parentTurnId: "root-turn", childThreadId: "late", childTurnId: "late-turn", selectedRole: { kind: "upstream" }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(f.declarations) } });
      await expect(f.session.resumeThread({ threadId: "root-thread", model: "model", continuityChecked: true })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    } finally { await f.session.close(); }
  });

  it("keeps the original root deadline while family settlement is absent", async () => {
    const f = await fixture(30);
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      f.send({ method: "turn/completed", params: { threadId: "root-thread", turn: { id: "root-turn", status: "completed" } } });
      await expect(f.session.waitTurn("root-turn")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    } finally { await f.session.close(); }
  });

  it("holds an interrupted root until the same family's cancellation barrier", async () => {
    const f = await fixture();
    try {
      await f.session.startThread({ cwd: f.root, model: "model", continuityChecked: true });
      await f.session.startTurn({ threadId: "root-thread", text: "work", model: "model" });
      const waiting = f.session.waitTurn("root-turn"); let settled = false; void waiting.then(() => { settled = true; });
      await f.session.interrupt("root-turn"); await new Promise<void>(resolve => setImmediate(resolve)); expect(settled).toBe(false);
      f.send({ method: "chirality/nativeChild/familySettled", params: { schema: "chirality-native-family-settled/v1", supplierGeneration: "supplier-1", rootThreadId: "root-thread", rootTurnId: "root-turn" } });
      await expect(waiting).resolves.toMatchObject({ status: "interrupted" });
    } finally { await f.session.close(); }
  });
});
