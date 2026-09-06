import { PassThrough } from "node:stream";
import { spawn } from "node:child_process";
import { mkdtemp, mkdir, realpath, rm, writeFile, symlink } from "node:fs/promises";
import { join } from "node:path";
import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { prepareCodexNativePolicy } from "../packages/daemon/src/codex-containment.js";
import { DescendantTracker } from "../packages/core/src/descendant-tracker.js";
import { CodexSupervisor, createControlledCodexSupervisorForTests } from "../packages/daemon/src/codex-supervisor.js";
import type { WorkerContinuity } from "@chirality/runtime-contracts";

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
 if(r.method==='config/read'){const table=JSON.parse(process.argv[3]);if(process.argv[4]==='broaden')table.filesystem['/']='write';return send({id:r.id,result:{config:{permissions:{[process.argv[2]]:table},approvals_reviewer:'user',approval_policy:'never',allow_login_shell:false,features:{plugins:false,remote_plugin:false,network_proxy:table.network.enabled},hooks:null,mcp_servers:{},notify:null,plugins:{},profiles:{},profile:null}}});}
 if(r.method==='initialize')return send({id:r.id,result:{userAgent:'controlled-fixture'}});
 if(r.method==='account/read')return send({id:r.id,result:{requiresOpenaiAuth:true,account:process.argv[1]==='no-account'?null:{type:'fixture'}}});
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
  it.runIf(process.platform === "darwin")("rejects production continuity policy mismatch before account or executable use", async () => {
    const project = join(root, "project"), broker = join(root, "broker"), worker = join(broker, "worker"), home = join(worker, "codex");
    await mkdir(project, { mode: 0o700 }); await mkdir(home, { recursive: true, mode: 0o700 });
    const declared = { ...identity, canonicalRoot: project, cwd: project };
    const consent = { approvedBy: "fixture", approvalReference: "no-account-no-execution" };
    const policy = await prepareCodexNativePolicy({ canonicalRoot: project, codexHome: home, privateDirectory: worker,
      immutableReadRoots: ["/bin", "/usr/lib", "/usr/bin/curl", "/private/etc/ssl/openssl.cnf", "/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld"], protectedPaths: [broker], providerNetworkConsent: consent });
    try {
      const options = { executablePath: join(worker, "missing-pinned-binary"), identity: declared, model: "explicit-model", codexHome: home, privateDirectory: worker, protectedPaths: [broker], authBindingSha256: "a".repeat(64), providerNetworkConsent: consent };
      const mismatch = new CodexSupervisor(options); supervisors.push(mismatch);
      await expect(mismatch.verifyHostedBoundary(declared)).rejects.toThrow("differs from the compiled native action policy");
      const correct = { ...declared, policyDigest: policy.policyDigest };
      const accountAbsent = new CodexSupervisor({ ...options, identity: correct }); supervisors.push(accountAbsent);
      await expect(accountAbsent.verifyHostedBoundary(correct)).rejects.toThrow("account binding is unavailable");
      const changedPosture = new CodexSupervisor({ ...options, identity: correct, commandNetworkPosture: "on" }); supervisors.push(changedPosture);
      await expect(changedPosture.verifyHostedBoundary(correct)).rejects.toThrow("differs from the compiled native action policy");
      expect(await mismatch.inventory()).toEqual([]); expect(await accountAbsent.inventory()).toEqual([]);
    } finally { await policy.cleanup(); }
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
  it("checks account-file digest and symlink exclusion before any real executable launch", async () => {
    const privateRoot = join(root, "private"), codexHome = join(privateRoot, "home");
    await mkdir(codexHome, { recursive: true, mode: 0o700 });
    const auth = join(codexHome, "auth.json"); await writeFile(auth, '{"fixture":"not-an-account"}', { mode: 0o600 });
    const s = new CodexSupervisor({ executablePath: join(privateRoot, "missing-pinned-binary"), identity, model: "explicit-model", codexHome, privateDirectory: privateRoot, authBindingSha256: "a".repeat(64), providerNetworkConsent: { approvedBy: "fixture", approvalReference: "fixture-no-launch" } });
    supervisors.push(s);
    await expect(s.verifyHostedBoundary({ ...identity, accountEpoch: 2 })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(s.verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    const target = join(privateRoot, "fixture-auth.json"); await writeFile(target, '{"fixture":"not-an-account"}', { mode: 0o600 }); await rm(auth); await symlink(target, auth);
    await expect(s.verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(await s.inventory()).toEqual([]);
  });
  it("real adapter refuses unbound account and missing exact supply without launching", async () => {
    const s = new CodexSupervisor({ executablePath: join(root, "missing"), identity, model: "explicit-model", codexHome: join(root, "home"), privateDirectory: join(root, "private"), authBindingSha256: "a".repeat(64), providerNetworkConsent: { approvedBy: "fixture", approvalReference: "fixture-no-launch" } });
    supervisors.push(s);
    await expect(s.verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(await s.inventory()).toEqual([]);
  });
});

it("blocks production regular and manager admission without conformance before account reads or worker launch", async () => {
  const s = new CodexSupervisor({ identity, model: "fixture-not-production", executablePath: join(root, "absent-vendor"), codexHome: join(root, "absent-account"), privateDirectory: root, authBindingSha256: "a".repeat(64), providerNetworkConsent: { approvedBy: "fixture", approvalReference: "no-owner-act" } }); supervisors.push(s);
  await expect(s.acquire("missing-conformance", JSON.stringify({ prompt: "must not launch" }))).rejects.toThrow(/conformance/);
  await expect(s.startManager("missing-manager-conformance", JSON.stringify({ prompt: "must not launch", canonicalRoot: root, model: "fixture-not-production" }))).rejects.toThrow(/conformance/);
  expect(await s.inventory()).toEqual([]);
});
