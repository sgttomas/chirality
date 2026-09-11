import { PassThrough } from "node:stream";
import { spawn } from "node:child_process";
import { mkdtemp, mkdir, realpath, rm, writeFile, symlink } from "node:fs/promises";
import { join } from "node:path";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { prepareCodexNativePolicy } from "../packages/daemon/src/codex-containment.js";
import { DescendantTracker } from "../packages/core/src/descendant-tracker.js";
import { CodexSupervisor, codexRuntimeConformanceConfigDigest, createControlledCodexSupervisorForTests } from "../packages/daemon/src/codex-supervisor.js";
import { admitHostedControlledForTests } from "../packages/daemon/src/codex-supervisor-test-support.js";
import * as daemonPublicSurface from "../packages/daemon/src/index.js";
import { recordKey } from "@chirality/runtime-core";
import type { RuntimeError, WorkerContinuity } from "@chirality/runtime-contracts";

let root: string;
let identity: WorkerContinuity;
const supervisors: CodexSupervisor[] = [];
beforeEach(async () => { root = await realpath(await mkdtemp(join(await realpath("/tmp"), "cs-"))); identity = { canonicalRoot: root, cwd: root, accountId: "fixture-account", accountEpoch: 1, policyDigest: "fixture-policy" }; });
afterEach(async () => { for (const supervisor of supervisors.splice(0)) await supervisor.close(); await rm(root, { recursive: true, force: true }); });

const source = `
const readline = require('node:readline');
let thread = 'thread-fixture';
readline.createInterface({input:process.stdin}).on('line', line => {
 const r=JSON.parse(line); const send = value => process.stdout.write(JSON.stringify(value)+'\\n');
 if (process.argv[2] && ['thread/start','thread/resume','turn/start'].includes(r.method) && (r.params.permissions !== process.argv[2] || 'sandbox' in r.params || 'sandboxPolicy' in r.params || 'policyDigest' in r.params)) return send({id:r.id,error:{message:'native profile missing or overridden'}});
 if(r.method==='initialized')return;
 if(r.method==='config/read'){const table=JSON.parse(process.argv[3]);if(process.argv[4]==='broaden')table.filesystem['/']='write';return send({id:r.id,result:{config:{permissions:{[process.argv[2]]:table},approvals_reviewer:'user',approval_policy:'never',allow_login_shell:false,features:{plugins:false,remote_plugin:false,shell_snapshot:false,network_proxy:table.network.enabled},hooks:null,mcp_servers:{},notify:null,plugins:{},profiles:{},profile:null}}});}
 if(r.method==='initialize')return send({id:r.id,result:{userAgent:'controlled-fixture'}});
 if(r.method==='account/read')return send({id:r.id,result:{requiresOpenaiAuth:true,account:process.argv[1]==='no-account'?null:{type:'apiKey'}}});
 if(r.method==='thread/start'||r.method==='thread/resume'){thread=r.params.threadId||thread;return send({id:r.id,result:{thread:{id:thread},approvalsReviewer:r.params.approvalsReviewer,approvalPolicy:r.params.approvalPolicy}});}
 if(r.method==='turn/start'){
  const text=r.params.input[0].text;
  if(text==='crash')process.exit(9);
  send({id:r.id,result:{turn:{id:'turn-fixture',status:'inProgress'}}});
  if(text==='hang')return;
  if(text==='retry-error'){send({method:'error',params:{threadId:thread,turnId:'turn-fixture',willRetry:true,error:{message:'retrying'}}});return;}
  send({method:'item/completed',params:{threadId:thread,turnId:'turn-fixture',item:{id:'item-fixture',type:'agentMessage',text:'fixture:'+thread+':'+text}}});
  send({method:'turn/completed',params:{threadId:thread,turn:{id:'turn-fixture',status:text==='fail'?'failed':text==='interrupt'?'interrupted':'completed'}}});
 }
});
`;
function fixture(noAccount = false, timeout = 1000, nativePolicy?: { permissionProfile: string; policyDigest: string; expectedPermissions?: { filesystem: Record<string, "read" | "write" | "deny">; network: { enabled: boolean } } }, broadenProfile = false, trackingOutcome?: "gone" | "detached" | "census-failure"): CodexSupervisor {
  const supervisor = createControlledCodexSupervisorForTests({ identity, model: "fixture-model", commandNetworkPosture: nativePolicy?.expectedPermissions?.network.enabled ? "on" : "off", requestTimeoutMs: timeout, turnTimeoutMs: timeout,
    async launch() {
      const child = spawn(process.execPath, ["-e", source, noAccount ? "no-account" : "account", ...(nativePolicy ? [nativePolicy.permissionProfile, JSON.stringify(nativePolicy.expectedPermissions ?? null), broadenProfile ? "broaden" : "exact"] : [])], { env: {}, detached: true, stdio: "pipe" });
      const done = new Promise<void>(resolve => child.once("close", () => resolve()));
      await new Promise<void>((resolve, reject) => { child.once("spawn", resolve); child.once("error", reject); });
      let alive = true;
      const descendantTracker = trackingOutcome ? new DescendantTracker({ leaderPid: child.pid!, census: async () => {
        if (trackingOutcome === "census-failure") throw new Error("fixture census failure");
        const leader = { pid: child.pid!, ppid: process.pid, pgid: child.pid!, uid: process.getuid!(), startIdentity: "fixture-leader" };
        const descendant = { pid: 999991, ppid: alive ? child.pid! : 1, pgid: alive ? child.pid! : 999991, uid: process.getuid!(), startIdentity: "fixture-descendant" };
        return alive ? [leader, descendant] : trackingOutcome === "detached" ? [descendant] : [];
      } }) : undefined;
      return { pid: child.pid!, ...nativePolicy, ...(descendantTracker ? { descendantTracker } : {}), transport: { stdin: child.stdin, stdout: child.stdout, async close() { try { process.kill(-child.pid!, "SIGKILL"); } catch {} await done; alive = false; } } };
    }
  });
  supervisors.push(supervisor); return supervisor;
}

describe("Codex supervisor adapter without account/network use", () => {
  it("does not expose controlled hosted conformance substitution on production surfaces", () => {
    expect(Object.hasOwn(daemonPublicSurface, "admitHostedControlledForTests")).toBe(false);
    expect(Object.hasOwn(CodexSupervisor, "admitHostedControlledForTests")).toBe(false);
  });
  it("rejects a structural v2 instance admission before creating a candidate", async () => {
    const launchCandidate = vi.fn();
    const options = { canonicalRoot: root, candidateLauncherFactory: { create: vi.fn(() => ({ launchCandidate })), close: vi.fn() },
      executablePath: "/private/supplier/codex", model: "fixture-model", codexHome: "/private/codex-home", privateDirectory: "/private",
      managedAuth: { backend: "keyring", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } },
      providerNetworkConsent: { approvedBy: "owner", approvalReference: "act" }, commandNetworkPosture: "off" as const, configDigest: "a".repeat(64), consentVersion: "b".repeat(64),
      runtimeV2: { purposeReleaseSource: {} as any, instanceInput: { purposeRelease: { purpose: "worker" }, hostAuthority: {} } as any, instanceAdmission: { purpose: "worker", evidence: "release-and-live-instance-v2" } as any } };
    await expect(admitHostedControlledForTests(options as any, { verifyConformance: async () => {} })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(options.candidateLauncherFactory.create).not.toHaveBeenCalled();
    expect(launchCandidate).not.toHaveBeenCalled();
  });
  it("drives actual JSONL child, genuine terminal and strict resumed thread selection", async () => {
    const s = fixture();
    const h = await s.acquire("worker", JSON.stringify({ prompt: "hello", resumeThreadId: "thread-recorded" }));
    expect(h.pid).toBeGreaterThan(0);
    expect(await s.reconnect(h.workerId, h.generation)).toMatchObject({ workerId: "worker", generation: h.generation });
    expect(await s.wait(h.workerId, h.generation)).toMatchObject({ exitCode: 0, stdout: "fixture:thread-recorded:hello", threadId: "thread-recorded" });
    await s.retire(h.workerId, h.generation); expect(await s.inventory()).toEqual([]);
  });
  it("binds one immutable named profile on fresh, resumed and turn requests", async () => {
    const policy = { permissionProfile: "chirality_fixture", policyDigest: "b".repeat(64), expectedPermissions: { filesystem: { [root]: "write" as const }, network: { enabled: false } } };
    const s = fixture(false, 1000, policy);
    const fresh = await s.acquire("native-fresh", JSON.stringify({ prompt: "hello" }));
    expect((await s.wait(fresh.workerId, fresh.generation)).exitCode).toBe(0);
    const resumed = await s.acquire("native-resume", JSON.stringify({ prompt: "again", resumeThreadId: "recorded-thread" }));
    expect((await s.wait(resumed.workerId, resumed.generation)).threadId).toBe("recorded-thread");
    await expect(s.verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(s.acquire("override", JSON.stringify({ prompt: "hello", permissionProfile: "forged" }))).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  });
  it.each([false, true])("checks exact effective native config before thread and turn (command network %s)", async enabled => {
    const expectedPermissions = { filesystem: { [root]: "write" as const, "/bin": "read" as const }, network: { enabled } };
    const policy = { permissionProfile: "chirality_effective", policyDigest: "c".repeat(64), expectedPermissions };
    const exact = fixture(false, 1000, policy);
    const worker = await exact.acquire("effective", JSON.stringify({ prompt: "hello" }));
    expect((await exact.wait(worker.workerId, worker.generation)).exitCode).toBe(0);
    const broad = fixture(false, 1000, policy, true);
    const rejected = await broad.acquire("broadened", JSON.stringify({ prompt: "must reject" }));
    await expect(broad.wait(rejected.workerId, rejected.generation)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("does not convert a genuine terminal into success when an observed detached survivor remains", async () => {
    const s = fixture(false, 1000, undefined, false, "detached");
    const handle = await s.acquire("detached", JSON.stringify({ prompt: "hello" }));
    await expect(s.wait(handle.workerId, handle.generation)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", details: { reason: "DESCENDANT_RECONCILIATION_REQUIRED", detachedCount: 1, detachedPids: [999991], signalAuthority: "NONE" } });
    await expect(s.retire(handle.workerId, handle.generation)).rejects.toMatchObject({ details: { reason: "DESCENDANT_RECONCILIATION_REQUIRED" } });
    await expect(s.close()).rejects.toMatchObject({ details: { detachedCount: 1 } });
    expect(() => process.kill(handle.pid, 0)).toThrow();
    supervisors.splice(supervisors.indexOf(s), 1); // Expected persistent diagnostic, no actual detached process was created.
  });
  it("reports the turn's own failure and carries the reconciliation diagnostic as its cause", async () => {
    const s = fixture(false, 300, undefined, false, "detached");
    const unhandled: unknown[] = []; const onUnhandled = (reason: unknown) => { unhandled.push(reason); };
    process.on("unhandledRejection", onUnhandled);
    try {
      const handle = await s.acquire("hung", JSON.stringify({ prompt: "hang" }));
      const failure = await s.wait(handle.workerId, handle.generation).then(() => undefined, error => error as RuntimeError);
      expect(failure).toMatchObject({ code: "ENGINE_UNAVAILABLE", message: expect.stringContaining("timed out"), details: { reason: "CODEX_PROTOCOL_FAILURE" } });
      expect(failure?.cause).toMatchObject({ code: "ENGINE_UNAVAILABLE", details: { reason: "DESCENDANT_RECONCILIATION_REQUIRED", detachedCount: 1, detachedPids: [999991] } });
      await expect(s.retire(handle.workerId, handle.generation)).rejects.toMatchObject({ details: { reason: "DESCENDANT_RECONCILIATION_REQUIRED" } });
      await new Promise(resolve => setTimeout(resolve, 20));
      expect(unhandled).toEqual([]);
    } finally { process.off("unhandledRejection", onUnhandled); }
    await expect(s.close()).rejects.toMatchObject({ details: { detachedCount: 1 } });
    supervisors.splice(supervisors.indexOf(s), 1);
  });
  it("names the census failure in the reconciliation diagnostic", async () => {
    const s = fixture(false, 1000, undefined, false, "census-failure");
    await expect(s.acquire("no-census-text", JSON.stringify({ prompt: "hello" }))).rejects.toMatchObject({ details: { censusFailed: true, censusFailure: "fixture census failure" } });
  });
  it("permits an observed clean closure while retaining the tracker's polling limitation", async () => {
    const s = fixture(false, 1000, undefined, false, "gone");
    const handle = await s.acquire("tracked", JSON.stringify({ prompt: "hello" }));
    expect((await s.wait(handle.workerId, handle.generation)).exitCode).toBe(0);
    await s.retire(handle.workerId, handle.generation);
    expect(await s.inventory()).toEqual([]);
  });
  it("fails acquisition and closes the child when initial descendant observation is unavailable", async () => {
    const s = fixture(false, 1000, undefined, false, "census-failure");
    await expect(s.acquire("no-census", JSON.stringify({ prompt: "hello" }))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", details: { reason: "DESCENDANT_RECONCILIATION_REQUIRED", censusFailed: true } });
    expect(await s.inventory()).toEqual([]);
  });
  it("cleans up a launched transport if native profile binding is malformed", async () => {
    const s = fixture(false, 1000, { permissionProfile: "chirality_fixture", policyDigest: "not-a-digest" });
    await expect(s.acquire("invalid-policy", JSON.stringify({ prompt: "hello" }))).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    expect(await s.inventory()).toEqual([]);
  });
  it("custody rejects all production continuity declarations while identity is unavailable", async () => {
    const s = new CodexSupervisor({ executablePath: join(root, "missing"), identity, model: "explicit-model", codexHome: join(root, "missing-home"), privateDirectory: root, managedAuth: { backend: "keyring" as const, binding: { schema: "chirality-hosted-account-binding/v1" as const, state: "unavailable" as const, reason: "canonical-identity-producer-unavailable" as const } }, providerNetworkConsent: { approvedBy: "fixture", approvalReference: "no-effects" } }); supervisors.push(s);
    await expect(s.verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(s.verifyHostedBoundary({ ...identity, policyDigest: "caller-claimed-policy" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(await s.inventory()).toEqual([]);
  });
  it("cannot upgrade the controlled launcher into hosted boundary admission", async () => {
    await expect(fixture().verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it.each(["fail", "interrupt"])("preserves genuine %s terminal without a completion claim", async prompt => {
    const s = fixture(); const h = await s.acquire("worker", JSON.stringify({ prompt }));
    const result = await s.wait(h.workerId, h.generation);
    expect(result.exitCode).toBe(prompt === "fail" ? 1 : null);
    expect(result.signal).toBe(prompt === "interrupt" ? "SIGTERM" : null);
  });
  it.each(["crash", "retry-error", "hang"])("never reports completion after %s", async prompt => {
    const s = fixture(false, 100); const h = await s.acquire("worker", JSON.stringify({ prompt }));
    await expect(s.wait(h.workerId, h.generation)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("requires an actual account/read account before a turn even in the fixture", async () => {
    const s = fixture(true); const h = await s.acquire("worker", JSON.stringify({ prompt: "hello" }));
    await expect(s.wait(h.workerId, h.generation)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("fences duplicate and stale generations and retires an active process", async () => {
    const s = fixture(); const h = await s.acquire("worker", JSON.stringify({ prompt: "hang" }));
    await expect(s.acquire("worker", JSON.stringify({ prompt: "new" }))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(s.wait(h.workerId, "stale")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await s.retire(h.workerId, h.generation);
    expect(() => process.kill(h.pid, 0)).toThrow();
    await s.close(); await expect(s.acquire("late", JSON.stringify({ prompt: "late" }))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("waits for an in-progress launch to be cleaned before closing", async () => {
    let release!: () => void, entered!: () => void, transportClosed = false;
    const gate = new Promise<void>(resolve => { release = resolve; });
    const started = new Promise<void>(resolve => { entered = resolve; });
    const s = createControlledCodexSupervisorForTests({ identity, model: "fixture-model", async launch() {
      entered(); await gate;
      return { pid: 1, transport: { stdin: new PassThrough(), stdout: new PassThrough(), async close() { transportClosed = true; } } };
    } }); supervisors.push(s);
    const acquisition = s.acquire("worker", JSON.stringify({ prompt: "hello" }));
    const failure = expect(acquisition).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await started; let drained = false; const closing = s.close().then(() => { drained = true; });
    await Promise.resolve(); expect(drained).toBe(false);
    release(); await failure; await closing; expect(transportClosed).toBe(true);
  });
  it("preserves the exact user prompt and adds only explicit selected-role labels", async () => {
    const s = fixture(); const prompt = "  Preserve this exact prompt.\n";
    const h = await s.acquire("role", JSON.stringify({ prompt, requestedRole: "agent0", roleEvidence: { selectedRole: "agent0", enforcementLabel: "role not mechanically enforced", evidencePosture: "instruction-asserted" } }));
    const result = await s.wait(h.workerId, h.generation);
    expect(result.stdout).toContain("explicit user selection): agent0"); expect(result.stdout).toContain("role not mechanically enforced"); expect(result.stdout.endsWith(prompt)).toBe(true);
    const untyped = await s.acquire("untyped", JSON.stringify({ prompt }));
    expect((await s.wait(untyped.workerId, untyped.generation)).stdout).toBe(`fixture:thread-fixture:${prompt}`);
    await expect(s.acquire("bad-role", JSON.stringify({ prompt, requestedRole: "owner" }))).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await expect(s.acquire("bad-label", JSON.stringify({ prompt, requestedRole: "agent2", roleEvidence: { selectedRole: "agent2", enforcementLabel: "mechanically enforced", evidencePosture: "instruction-asserted" } }))).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  });
  it("rejects raw text and unrecognized broker controls", async () => {
    const s = fixture();
    await expect(s.acquire("worker", "raw prompt")).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await expect(s.acquire("worker", JSON.stringify({ prompt: "hello", executable: "/bin/sh" }))).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  });
  it("custody unavailable identity does not become a credential-file binding", async () => {
    const s = new CodexSupervisor({ executablePath: join(root, "missing-vendor"), identity, model: "explicit-model", codexHome: join(root, "missing-account"), privateDirectory: root, managedAuth: { backend: "keyring" as const, binding: { schema: "chirality-hosted-account-binding/v1" as const, state: "unavailable" as const, reason: "canonical-identity-producer-unavailable" as const } }, providerNetworkConsent: { approvedBy: "fixture", approvalReference: "no-effects" } }); supervisors.push(s);
    await expect(s.verifyHostedBoundary({ ...identity, accountEpoch: 2 })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(s.verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(await s.inventory()).toEqual([]);
  });
  it("custody real adapter refuses unavailable identity without launching", async () => {
    const s = new CodexSupervisor({ executablePath: join(root, "missing"), identity, model: "explicit-model", codexHome: join(root, "home"), privateDirectory: join(root, "private"), managedAuth: { backend: "keyring" as const, binding: { schema: "chirality-hosted-account-binding/v1" as const, state: "unavailable" as const, reason: "canonical-identity-producer-unavailable" as const } }, providerNetworkConsent: { approvedBy: "fixture", approvalReference: "fixture-no-launch" } });
    supervisors.push(s);
    await expect(s.verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(await s.inventory()).toEqual([]);
  });
});

describe("catalog-bound per-turn model and reasoning choice", () => {
  const catalog = [
    { model: "gpt-default", isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["medium", "high"] },
    { model: "gpt-alt", isDefault: false, defaultReasoningEffort: "low", supportedReasoningEfforts: ["low", "medium"] }
  ];
  function catalogFixture(options: { modelCatalog?: typeof catalog; reasoningEffort?: string } = { modelCatalog: catalog, reasoningEffort: "high" }) {
    const requests: { method: string; params: any }[] = []; let launches = 0;
    const supervisor = createControlledCodexSupervisorForTests({ identity, model: "gpt-default", allowUnauthenticatedModel: true, requestTimeoutMs: 1000, turnTimeoutMs: 1000, ...options, async launch() {
      launches++;
      const stdin = new PassThrough(), stdout = new PassThrough(); let buffer = "";
      const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
      stdin.on("data", chunk => {
        buffer += String(chunk);
        for (let newline = buffer.indexOf("\n"); newline >= 0; newline = buffer.indexOf("\n")) {
          const request = JSON.parse(buffer.slice(0, newline)); buffer = buffer.slice(newline + 1);
          requests.push({ method: request.method, params: request.params });
          if (request.method === "initialize") send({ id: request.id, result: {} });
          else if (request.method === "account/read") send({ id: request.id, result: { requiresOpenaiAuth: false, account: null } });
          else if (request.method === "thread/start") send({ id: request.id, result: { thread: { id: "thread-catalog" }, approvalsReviewer: "auto_review", approvalPolicy: "never" } });
          else if (request.method === "turn/start") {
            send({ id: request.id, result: { turn: { id: "turn-catalog", status: "inProgress" } } });
            send({ method: "item/completed", params: { threadId: "thread-catalog", turnId: "turn-catalog", item: { id: "item", type: "agentMessage", text: `used:${request.params.model}:${request.params.collaborationMode.settings.reasoning_effort}` } } });
            send({ method: "turn/completed", params: { threadId: "thread-catalog", turn: { id: "turn-catalog", status: "completed" } } });
          }
        }
      });
      return { pid: 24680 + launches, transport: { stdin, stdout, async close() { stdin.destroy(); stdout.destroy(); } } };
    } });
    supervisors.push(supervisor);
    const run = async (workerId: string, envelope: Record<string, unknown>) => { const handle = await supervisor.acquire(workerId, JSON.stringify({ prompt: "hello", ...envelope })); return supervisor.wait(handle.workerId, handle.generation); };
    return { supervisor, requests, run, launches: () => launches };
  }
  it("carries an in-catalog envelope choice to thread/start and turn/start, defaulting to the admitted pair", async () => {
    const f = catalogFixture();
    expect((await f.run("chosen", { model: "gpt-alt", reasoningEffort: "medium" })).stdout).toBe("used:gpt-alt:medium");
    expect(f.requests.find(r => r.method === "thread/start")?.params).toMatchObject({ model: "gpt-alt" });
    expect(f.requests.find(r => r.method === "turn/start")?.params).toMatchObject({ model: "gpt-alt", collaborationMode: { mode: "default", settings: { model: "gpt-alt", reasoning_effort: "medium" } } });
    f.requests.length = 0;
    expect((await f.run("default", {})).stdout).toBe("used:gpt-default:high");
    expect(f.requests.find(r => r.method === "turn/start")?.params).toMatchObject({ model: "gpt-default", collaborationMode: { settings: { reasoning_effort: "high" } } });
    f.requests.length = 0;
    expect((await f.run("model-only", { model: "gpt-alt" })).stdout).toBe("used:gpt-alt:low");
    expect(f.launches()).toBe(3);
  });
  it("rejects out-of-catalog model or effort before any launch and keeps managers on the admitted model", async () => {
    const f = catalogFixture();
    await expect(f.run("unknown-model", { model: "gpt-unknown", reasoningEffort: "low" })).rejects.toMatchObject({ code: "INVALID_REQUEST", details: { reason: "MODEL_NOT_IN_CATALOG" } });
    await expect(f.run("bad-effort", { model: "gpt-alt", reasoningEffort: "high" })).rejects.toMatchObject({ code: "INVALID_REQUEST", details: { reason: "REASONING_EFFORT_UNSUPPORTED" } });
    await expect(f.run("bad-default-effort", { reasoningEffort: "xhigh" })).rejects.toMatchObject({ code: "INVALID_REQUEST", details: { reason: "REASONING_EFFORT_UNSUPPORTED" } });
    await expect(f.run("bad-shape", { model: "gpt alt" })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await expect(f.supervisor.startManager("manager-alt", JSON.stringify({ canonicalRoot: root, model: "gpt-alt", prompt: "manager" }))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(f.launches()).toBe(0);
    expect(await f.supervisor.inventory()).toEqual([]);
    const uncatalogued = catalogFixture({});
    await expect(uncatalogued.run("other", { model: "gpt-alt" })).rejects.toMatchObject({ code: "INVALID_REQUEST", details: { reason: "MODEL_NOT_IN_CATALOG" } });
    await expect(uncatalogued.run("other-effort", { reasoningEffort: "low" })).rejects.toMatchObject({ code: "INVALID_REQUEST", details: { reason: "REASONING_EFFORT_UNSUPPORTED" } });
    expect(uncatalogued.launches()).toBe(0);
    expect((await uncatalogued.run("same", { model: "gpt-default" })).stdout).toBe("used:gpt-default:null");
    expect(() => createControlledCodexSupervisorForTests({ identity, model: "gpt-missing", modelCatalog: catalog, launch: async () => { throw new Error("unused"); } })).toThrow("outside its catalog");
    expect(() => createControlledCodexSupervisorForTests({ identity, model: "gpt-default", reasoningEffort: "xhigh", modelCatalog: catalog, launch: async () => { throw new Error("unused"); } })).toThrow("outside its catalog");
  });
});

it("custody blocks production regular and manager admission before account reads or worker launch", async () => {
  const s = new CodexSupervisor({ identity, model: "fixture-not-production", executablePath: join(root, "absent-vendor"), codexHome: join(root, "absent-account"), privateDirectory: root, managedAuth: { backend: "keyring" as const, binding: { schema: "chirality-hosted-account-binding/v1" as const, state: "unavailable" as const, reason: "canonical-identity-producer-unavailable" as const } }, providerNetworkConsent: { approvedBy: "fixture", approvalReference: "no-owner-act" } }); supervisors.push(s);
  await expect(s.acquire("missing-conformance", JSON.stringify({ prompt: "must not launch" }))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  await expect(s.startManager("missing-manager-conformance", JSON.stringify({ prompt: "must not launch", canonicalRoot: root, model: "fixture-not-production" }))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  expect(await s.inventory()).toEqual([]);
});


it("custody changes the config digest without treating unavailable binding as an account digest", () => {
  const common = { model: "synthetic", executablePath: "/synthetic/vendor", identity, codexHome: "/synthetic/home", privateDirectory: "/synthetic/private", protectedPaths: [], providerNetworkConsent: { approvedBy: "fixture", approvalReference: "no-effects" }, commandNetworkPosture: "off" as const, requestTimeoutMs: 10000, turnTimeoutMs: 120000, maxWorkers: 16 };
  const policy = { configToml: 'cli_auth_credentials_store="keyring"\n', expectedPermissions: { filesystem: { [root]: "write" as const }, network: { enabled: false } } };
  const managedAuth = { backend: "keyring" as const, binding: { schema: "chirality-hosted-account-binding/v1" as const, state: "unavailable" as const, reason: "canonical-identity-producer-unavailable" as const } };
  const current = codexRuntimeConformanceConfigDigest({ ...common, managedAuth }, policy);
  // Baseline bf204d8f digest used this auth-file field; hold all other inputs fixed to isolate its replacement.
  const legacyFields = { model: common.model, executablePath: common.executablePath, identity: common.identity,
    codexHome: common.codexHome, privateDirectory: common.privateDirectory, protectedPaths: common.protectedPaths,
    authBindingSha256: "a".repeat(64), providerNetworkConsent: common.providerNetworkConsent,
    commandNetworkPosture: common.commandNetworkPosture, requestTimeoutMs: common.requestTimeoutMs,
    supportedPermissionMode: "workspaceWrite",
    turnTimeoutMs: common.turnTimeoutMs, maxWorkers: common.maxWorkers,
    nativeConfig: policy.configToml, expectedPermissions: policy.expectedPermissions };
  const legacy = recordKey(legacyFields);
  const replacement = Object.fromEntries(Object.entries(legacyFields).map(([key, value]) => key === "authBindingSha256" ? ["managedAuth", managedAuth] : [key, value]));
  expect(current).toBe(recordKey(replacement));
  expect(current).not.toBe(legacy);
  expect(managedAuth.binding).toEqual({ schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" });
  expect(() => codexRuntimeConformanceConfigDigest({ ...common, managedAuth: { backend: "keyring", binding: { ...managedAuth.binding, accountDigest: "a".repeat(64) } } } as any, policy)).toThrow();
});

describe("deterministic supplier admission cancellation",()=>{
  function authorityFixture(trace:string[],releaseFailure=false){let held=false;return {projection:()=>({state:"ready"}),runGuarded:async(fn:()=>Promise<unknown>)=>fn(),acquire:async()=>{trace.push("acquire");held=true;return{leaseId:"private"};},assertCommit:()=>{if(!held)throw Error("not-held");},release:async()=>{trace.push("release");held=false;if(releaseFailure)throw Error("release-response-lost");},abort:async()=>{trace.push("abort");held=false;},revoke:async()=>{trace.push("revoke");held=false;},close:async()=>{}} as any;}
  for(const kind of ["regular","manager"]){for(const phase of ["pre-acquire","post-acquire-pre-worker-publication","post-publication-pre-release"]){it(`${kind}/${phase} has exact ordered cancellation cardinalities`,async()=>{const trace:string[]=[];let reached!:()=>void,unblock!:()=>void;const at=new Promise<void>(r=>reached=r),gate=new Promise<void>(r=>unblock=r);let closed=false;const supervisor=createControlledCodexSupervisorForTests({identity,model:"fixture-model",supplierAuthority:authorityFixture(trace),barrier:async name=>{trace.push(name);if(name===`${kind}/${phase}`){reached();await gate;}},launch:async()=>{trace.push("launch");const stdin=new PassThrough(),stdout=new PassThrough();return{pid:12345,transport:{stdin,stdout,close:async()=>{if(!closed){closed=true;trace.push("retire");stdin.destroy();stdout.destroy();}}}};}});supervisors.push(supervisor);const pending=kind==="regular"?supervisor.acquire("w",JSON.stringify({prompt:"test"})):supervisor.startManager("w",JSON.stringify({canonicalRoot:root,model:"fixture-model",prompt:"test"}));void pending.catch(()=>{});await at;supervisor.cancelAdmission("w");unblock();await expect(pending).rejects.toThrow("cancelled");expect(await supervisor.inventory()).toEqual([]);const relevant=trace.filter(x=>["acquire","launch","release","abort","retire"].includes(x));expect(relevant).toEqual(phase==="pre-acquire"?[]:phase==="post-acquire-pre-worker-publication"?["acquire","launch","abort","retire"]:["acquire","launch","release","retire"]);});}}
  it("release failure removes publication and retires once without a second release or abort",async()=>{const trace:string[]=[];let closed=false;const supervisor=createControlledCodexSupervisorForTests({identity,model:"fixture-model",supplierAuthority:authorityFixture(trace,true),launch:async()=>{const stdin=new PassThrough(),stdout=new PassThrough();return{pid:12345,transport:{stdin,stdout,close:async()=>{if(!closed){closed=true;trace.push("retire");stdin.destroy();stdout.destroy();}}}};}});supervisors.push(supervisor);await expect(supervisor.acquire("w",JSON.stringify({prompt:"test"}))).rejects.toThrow("release-response-lost");expect(await supervisor.inventory()).toEqual([]);expect(trace).toEqual(["acquire","release","retire"]);});
});
