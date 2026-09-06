import { PassThrough } from "node:stream";
import { createControlledCodexSupervisorForTests } from "../packages/daemon/src/codex-supervisor.js";
import { mkdtemp, mkdir, realpath, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { validateHarnessEventV2 } from "@chirality/runtime-contracts";
import { ApprovalStore } from "../packages/core/src/approval-store.js";
import { AuthRegistry, EngineRegistry, ProjectRegistry, ResidencyCoordinator, RuntimeService, SessionStore, TurnCoordinator } from "@chirality/runtime-core";
import { RuntimeClient } from "@chirality/runtime-client";
import { RuntimeDaemon, type RuntimeDaemonOptions } from "@chirality/runtime-daemon";
import { DelegatedRuntime } from "../packages/core/src/delegated-runtime.js";
import { HostedConsentStore } from "../packages/core/src/hosted-consent.js";
import { WorkerRetirementCoordinator } from "../packages/core/src/worker-retirement.js";
import { ProcessSupervisor } from "../packages/core/src/process-supervisor.js";
import { startSupervisorServer, SupervisorClient } from "../packages/daemon/src/supervisor-server.js";
import { createProjectFixture } from "./helpers.js";

const cleanups: (() => Promise<unknown>)[] = [];
afterEach(async () => { for (const cleanup of cleanups.splice(0).reverse()) await cleanup(); });
const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "a".repeat(64) };
async function fixture(slow = false, login?: RuntimeDaemonOptions["login"], hostedBlocked = false, commandNetworkPosture: "off" | "ask-per-destination" | "on" = "off", controlledNetwork = false, holdUntilReleased = false) {
  const root = await realpath(await mkdtemp(join(tmpdir(), "dr-")));
  cleanups.push(() => rm(root, { recursive: true, force: true }));
  const project = join(root, "project");
  const { manifestPath } = await createProjectFixture(project, "project");
  const identity = { canonicalRoot: project, cwd: project, accountId: "controlled-account", accountEpoch: 1, policyDigest: "fixture-policy" };
  const releasePath = join(root, "approval-worker-release");
  // A host-owned explicit release, not elapsed time, ends this worker's turn.
  const heldWorker = "const fs=require('node:fs'),path=require('node:path');const release=process.argv[1];let finished=false;const check=()=>{if(!finished&&fs.existsSync(release)){finished=true;watcher.close();process.stdout.write('controlled:released');}};const watcher=fs.watch(path.dirname(release),check);check();";
  const worker = controlledNetwork ? controlledApprovalWorker(identity) : new ProcessSupervisor({ command: process.execPath, args: holdUntilReleased ? ["-e", heldWorker, releasePath] : slow ? ["-e", "setTimeout(() => process.stdout.write('controlled:slow'), 900)"] : [resolve("tests/fixtures/delegated-worker.mjs")], cwd: project, env: {}, maxRunMs: holdUntilReleased ? 10000 : 2000 });
  cleanups.push(() => worker.close());
  const server = await startSupervisorServer({ socketPath: join(root, "s", "s.sock"), supervisor: worker });
  cleanups.push(() => server.close());
  const supervisor = new SupervisorClient({ socketPath: join(root, "s", "s.sock"), credential: server.credential });
  if (hostedBlocked) Object.assign(supervisor, { async verifyHostedBoundary() { throw new Error("No account yet"); } });
  const consent = new HostedConsentStore({ canonicalRoot: project, codexHome: join(root, "homes", "project") });
  const retirement = new WorkerRetirementCoordinator({ directory: join(root, "journal") });
  let delegated: DelegatedRuntime;
  const approvals = new ApprovalStore({ canonicalRoot: project, storageRoot: join(root, "approval-control"), consent, isLive: identity => delegated.isApprovalLive(identity) });
  const binding = { identity, compatibility, supervisor, consent, retirement, approvals, commandNetworkPosture, approvalForwardingEnabled: controlledNetwork, ...(hostedBlocked ? { actual: { adapterId: "fixture-only", providerId: "not-applicable", model: "not-applicable" } } : {}), evidenceClass: hostedBlocked ? "provider-observed" as const : "controlled-worker" as const };
  delegated = new DelegatedRuntime({ daemonId: "fixture-daemon", projects: new Map([["project", binding]]) });
  const runtime = join(root, "runtime");
  const projects = new ProjectRegistry(runtime), sessions = new SessionStore(runtime, projects), engines = new EngineRegistry();
  const residency = new ResidencyCoordinator({ async listStatus() { return []; }, async load() {}, async unload() {} }, runtime);
  const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency), new AuthRegistry(runtime), { async get() { return undefined; }, async status() { return { configured: false }; }, async set() {}, async remove() {} });
  const registered = await service.registerProject(manifestPath, "fixture-owner", "fixture-only");
  const daemon = new RuntimeDaemon({ socketPath: join(root, "d.sock"), runtimeDirectory: runtime, service, delegated, ...(login ? { login, loginProjectId: "project" } : {}) });
  const started = await daemon.start();
  cleanups.push(() => daemon.stop());
  const client = new RuntimeClient({ socketPath: join(root, "d.sock"), tokenFile: registered.tokenFile });
  const operator = new RuntimeClient({ socketPath: join(root, "d.sock"), tokenFile: started.operatorTokenFile });
  let release: Promise<void> | undefined;
  return { client, operator, delegated, binding, worker, retirement, identity, consent, daemon, releaseWorker: () => release ??= writeFile(releasePath, "release", { flag: "wx" }) };
}

describe("opt-in delegated broker composition", () => {
  it("runs client→authenticated daemon→private supervisor→controlled process and preserves v1 reads", async () => {
    const f = await fixture();
    await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
    const result = await f.client.runDelegatedTurn("project", compatibility, { turnId: "turn-1", prompt: "hello" });
    expect(result).toMatchObject({ output: "controlled:hello", evidenceClass: "controlled-worker", terminal: { outcome: "completed" } });
    expect((await f.retirement.read("turn-1"))?.state).toBe("committed");
    expect(await f.worker.inventory()).toEqual([]);
    expect(await f.client.listSessions("project")).toEqual([]);
  });
  it("rejects client compatibility mismatch before consent or worker acquisition and preserves machine fields", async () => {
    const f = await fixture();
    await expect(f.client.runDelegatedTurn("project", { ...compatibility, compatibilityIdentity: "root-runtime-2" }, { turnId: "bad", prompt: "hello" })).rejects.toMatchObject({ code: "RUNTIME_COMPATIBILITY_MISMATCH", details: { consequential_work_started: false, retryable: false, operation_id: "turn:bad", project_id: "project" } });
    expect(await f.worker.inventory()).toEqual([]);
    expect(await f.retirement.read("bad")).toBeUndefined();
  });
  it("rejects missing consent, nonce replay and unbound requests without executing", async () => {
    const f = await fixture();
    const preflight = await f.delegated.preflight("project", "turn:t");
    const request = { preflight, compatibility, turnId: "t", prompt: "hello" };
    await expect(f.delegated.turn("project", request)).rejects.toMatchObject({ code: "FORBIDDEN" });
    await expect(f.delegated.turn("project", request)).rejects.toMatchObject({ code: "RUNTIME_COMPATIBILITY_MISMATCH" });
    expect(await f.worker.inventory()).toEqual([]);
  });
  it("terminalizes controlled crash and refuses automatic turn replay", async () => {
    const f = await fixture();
    await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
    const result = await f.client.runDelegatedTurn("project", compatibility, { turnId: "crash", prompt: "crash" });
    expect(result.terminal.outcome).toBe("failed");
    await expect(f.client.runDelegatedTurn("project", compatibility, { turnId: "crash", prompt: "again" })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    expect(await f.worker.inventory()).toEqual([]);
  });
  it("cannot upgrade fixture consent to a production containment claim", async () => {
    const f = await fixture();
    const production = new DelegatedRuntime({ daemonId: "production", projects: new Map([["project", { ...f.binding, evidenceClass: "provider-observed" }]]) });
    await expect(production.preflight("project", "turn:p")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await f.client.grantDelegatedConsent("project", compatibility, { posture: "on", approvedBy: "fixture-owner", explicitUserAct: true });
    await expect(f.client.runDelegatedTurn("project", compatibility, { turnId: "network", prompt: "hello" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(await f.worker.inventory()).toEqual([]);
  });
});

it("keeps issued operation and configured identity immutable against caller mutation", async () => {
  const f = await fixture();
  const preflight = await f.delegated.preflight("project", "consent");
  preflight.operationId = "turn:mutated";
  await expect(f.delegated.turn("project", { compatibility, preflight, turnId: "mutated", prompt: "x" })).rejects.toMatchObject({ code: "RUNTIME_COMPATIBILITY_MISMATCH" });
  f.binding.identity.accountId = "changed-after-construction";
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const result = await f.client.runDelegatedTurn("project", compatibility, { turnId: "immutable", prompt: "x" });
  expect(result.terminal.outcome).toBe("completed");
  expect((await f.retirement.read("immutable"))?.identity.accountId).toBe("controlled-account");
});

it("returns typed safe mismatch for malicious compatibility fields", async () => {
  const f = await fixture();
  const preflight = await f.delegated.preflight("project", "turn:malformed");
  await expect(f.delegated.turn("project", { compatibility: { compatibilityIdentity: { toString: 0 }, contractBasisSha256: "a".repeat(64) } as any, preflight, turnId: "malformed", prompt: "x" })).rejects.toMatchObject({ code: "RUNTIME_COMPATIBILITY_MISMATCH", details: { consequential_work_started: false, client_compatibility_identity: null } });
  expect(await f.worker.inventory()).toEqual([]);
});

it("fences worker acquisition when shutdown occurs during consent read", async () => {
  const f = await fixture();
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  let release!: () => void, entered!: () => void;
  const waiting = new Promise<void>((resolve) => { release = resolve; });
  const started = new Promise<void>((resolve) => { entered = resolve; });
  const original = f.consent.read.bind(f.consent);
  f.consent.read = async (identity) => { entered(); await waiting; return original(identity); };
  const preflight = await f.delegated.preflight("project", "turn:closing");
  const turn = f.delegated.turn("project", { preflight, compatibility, turnId: "closing", prompt: "x" });
  const failure = expect(turn).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  await started;
  const closing = f.delegated.close();
  release();
  await closing;
  await failure;
  expect(await f.worker.inventory()).toEqual([]);
});

it("starts a fresh daemon generation without reusing old admissions", async () => {
  const f = await fixture();
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const old = await f.delegated.preflight("project", "turn:old");
  await f.daemon.stop();
  await f.daemon.start();
  await expect(f.delegated.turn("project", { compatibility, preflight: old, turnId: "old", prompt: "x" })).rejects.toMatchObject({ code: "RUNTIME_COMPATIBILITY_MISMATCH" });
  expect((await f.client.runDelegatedTurn("project", compatibility, { turnId: "new", prompt: "new" })).output).toBe("controlled:new");
});

it("drains admitted consent publication before successful close", async () => {
  const f = await fixture();
  let release!: () => void, entered!: () => void;
  const wait = new Promise<void>((resolve) => { release = resolve; });
  const started = new Promise<void>((resolve) => { entered = resolve; });
  const original = f.consent.grant.bind(f.consent);
  f.consent.grant = async (consent) => { entered(); await wait; return original(consent); };
  const preflight = await f.delegated.preflight("project", "consent");
  const request = { preflight, compatibility, posture: "off" as const, approvedBy: "fixture", explicitUserAct: true };
  const grant = f.delegated.grantConsent("project", request);
  await started;
  let closed = false;
  const close = f.delegated.close().then(() => { closed = true; });
  await new Promise((resolve) => setTimeout(resolve, 10));
  expect(closed).toBe(false);
  release();
  await close;
  expect(await grant).toEqual({ posture: "off" });
});

it("rejects object and null turn requests with typed invalid request errors", async () => {
  const f = await fixture();
  await expect(f.delegated.turn("project", null as any)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  await expect(f.delegated.turn("project", { turnId: { toString: 0 } } as any)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  expect(await f.worker.inventory()).toEqual([]);
});

it("binds daemon identity and rejects a mismatched configured project root", async () => {
  const f = await fixture();
  expect((await f.client.delegatedPreflight("project", "turn:identity")).daemonId).toBe(f.daemon.daemonId);
  expect(() => f.delegated.assertProjectRoot("project", "/another/canonical/root")).toThrowError("Delegated project root differs");
  expect(await f.worker.inventory()).toEqual([]);
});


it.each(["untyped", "agent0", "agent1", "agent2", "task"] as const)("offers and executes explicit %s with canonical v2 evidence", async requestedRole => {
  const f = await fixture();
  const capabilities = await f.client.delegatedCapabilities("project");
  expect(capabilities.offeredRoles).toEqual(["untyped", "agent0", "agent1", "agent2", "task"]);
  expect(capabilities.commandNetwork.map(p => [p.posture, p.executionSupported])).toEqual([["off", true], ["ask-per-destination", false], ["on", false]]);
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const result = await f.client.runDelegatedTurn("project", compatibility, { turnId: `role-${requestedRole}`, prompt: "hello", requestedRole });
  expect(result.roleEvidence).toMatchObject({ selectedRole: requestedRole, enforcementLabel: "role not mechanically enforced", evidencePosture: "instruction-asserted", actual: { model: "not-applicable" } });
  expect(validateHarnessEventV2(result.event)).toBe(true);
  expect(result.event.type).toBe("turn.completed");
});
it("exposes configured on honestly and rejects unknown roles", async () => {
  const f = await fixture();
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "on", approvedBy: "fixture-owner", explicitUserAct: true });
  expect(await f.client.delegatedCapabilities("project")).toMatchObject({ configuredPosture: "on", approvalForwardingSupported: false });
  await expect(f.client.runDelegatedTurn("project", compatibility, { turnId: "unknown-role", prompt: "x", requestedRole: "admin" as never })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
});
it("routes existing approvals only, preserves generation binding and never claims provider application", async () => {
  const f = await fixture(false, undefined, false, "off", false, true);
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const turn = f.client.runDelegatedTurn("project", compatibility, { turnId: "approval-turn", prompt: "held" });
  let settled = false;
  void turn.then(() => { settled = true; }, () => { settled = true; });
  try {
    let request;
    for (let count = 0; count < 100; count++) {
      try { request = await f.delegated.requestApproval("project", "approval-turn", { host: "example.com", protocol: "https" }, "trusted-fixture-worker"); break; }
      catch (error) { if ((error as { code?: string }).code !== "FORBIDDEN") throw error; await new Promise(resolve => setTimeout(resolve, 5)); }
    }
    expect(request).toBeDefined();
    const pending = await f.client.pendingDelegatedApprovals("project", "approval-turn");
    expect(pending).toHaveLength(1);
    const input = { turnId: "approval-turn", workerGeneration: request!.binding.workerGeneration, decision: "deny" as const, approvedBy: "fixture-human", explicitUserAct: true as const };
    await expect(f.client.decideDelegatedApproval("project", request!.requestId, compatibility, { ...input, workerGeneration: "stale" })).rejects.toMatchObject({ code: "FORBIDDEN" });
    await expect(f.client.decideDelegatedApproval("other-project", request!.requestId, compatibility, input)).rejects.toBeDefined();
    const decided = await f.client.decideDelegatedApproval("project", request!.requestId, compatibility, input);
    expect(decided).toMatchObject({ applied: false, record: { decision: { approvedBy: "fixture-human", decision: "deny" } } });
    expect(await f.client.pendingDelegatedApprovals("project", "approval-turn")).toEqual([]);
    await expect((f.client as any).requestJson("/v2/projects/project/delegated/approval-request", { method: "POST", body: { host: "example.com", protocol: "https" } })).rejects.toMatchObject({ code: "NOT_FOUND" });
    expect(settled).toBe(false);
    await f.releaseWorker();
    expect((await turn).terminal.outcome).toBe("completed");
    await expect(f.client.pendingDelegatedApprovals("project", "approval-turn")).rejects.toMatchObject({ code: "FORBIDDEN" });
  } finally {
    // Release is idempotent; failure still retires and joins the owned process.
    try { await f.releaseWorker(); } finally {
      if (!settled) {
        try { await f.client.interruptDelegatedTurn("project", "approval-turn", compatibility); }
        catch { await f.worker.close(); }
      }
      await turn.catch(() => undefined);
    }
  }
});

it("interrupts an active exact worker once and records the closed interrupted terminal", async () => {
  const f = await fixture(true);
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const turn = f.client.runDelegatedTurn("project", compatibility, { turnId: "interrupt-turn", prompt: "slow" });
  for (let count = 0; count < 100; count++) {
    try { await f.delegated.pendingApprovals("project", "interrupt-turn"); break; } catch { await new Promise(resolve => setTimeout(resolve, 5)); }
  }
  expect(await f.client.interruptDelegatedTurn("project", "interrupt-turn", compatibility)).toMatchObject({ interrupted: true, turnId: "interrupt-turn" });
  const result = await turn;
  expect(result.terminal.outcome).toBe("interrupted");
  expect(result.event.type).toBe("turn.interrupted");
  expect(validateHarnessEventV2(result.event)).toBe(true);
  expect((await f.retirement.read("interrupt-turn"))?.terminal).toEqual(result.terminal);
  await expect(f.client.interruptDelegatedTurn("project", "interrupt-turn", compatibility)).rejects.toMatchObject({ code: "FORBIDDEN" });
  expect(await f.worker.inventory()).toEqual([]);
});

it("permits operator login without a pre-existing account and confines bypass admissions to login", async () => {
  let starts = 0, cancels = 0;
  const login = { async startLogin() { starts++; return { loginId: "fixture-login", authUrl: "https://example.com/authorize?state=fixture" }; }, async status() { return { state: "pending" as const, loginId: "fixture-login", evidenceClass: "controlled-fixture" as const, providerSecret: "must-not-project" }; }, async cancel() { cancels++; } };
  const f = await fixture(false, login, true);
  await expect(f.client.startHostedLogin("project", compatibility)).rejects.toMatchObject({ code: "FORBIDDEN" });
  expect(starts).toBe(0);
  const result = await f.operator.startHostedLogin("project", compatibility);
  expect(result.loginId).toBe("fixture-login");
  expect(starts).toBe(1);
  expect(await f.operator.hostedLoginStatus("project")).toEqual({ state: "pending", loginId: "fixture-login", evidenceClass: "controlled-fixture" });
  await expect(f.client.hostedLoginStatus("project")).rejects.toMatchObject({ code: "FORBIDDEN" });
  const loginPreflight = await f.delegated.preflight("project", "login:start");
  await expect(f.delegated.turn("project", { turnId: "not-login", prompt: "x", compatibility, preflight: loginPreflight })).rejects.toMatchObject({ code: "RUNTIME_COMPATIBILITY_MISMATCH" });
  await expect(f.delegated.preflight("project", "turn:blocked")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  expect(await f.operator.cancelHostedLogin("project", compatibility)).toEqual({ cancelled: true });
  expect(cancels).toBe(1);
  expect(await f.worker.inventory()).toEqual([]);
});
it("rejects unsafe login URL output without sending arbitrary port fields", async () => {
  const f = await fixture(false, { async startLogin() { return { loginId: "fixture-login", authUrl: "http://unsafe.example.com" }; }, async status() { return { state: "failed", evidenceClass: "controlled-fixture" }; }, async cancel() {} });
  await expect(f.operator.startHostedLogin("project", compatibility)).rejects.toMatchObject({ code: "INTERNAL_FAILURE" });
});

it("rejects malformed interruption and approval identities without coercion", async () => {
  const f = await fixture();
  await expect(f.delegated.interruptTurn("project", null as never)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  await expect(f.delegated.interruptTurn("project", { turnId: { toString: 0 } } as never)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  await expect(f.delegated.decideApproval("project", { toString: 0 } as never, {} as never)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
});

it("allows exact live-turn interruption after hosted launch verification becomes unavailable", async () => {
  const f = await fixture(true, undefined, true);
  let available = true;
  Object.assign(f.binding.supervisor, { async verifyHostedBoundary() { if (!available) throw new Error("credential rotated"); } });
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const turn = f.client.runDelegatedTurn("project", compatibility, { turnId: "drift-interrupt", prompt: "slow" });
  for (let count = 0; count < 100; count++) {
    try { await f.delegated.pendingApprovals("project", "drift-interrupt"); break; } catch { await new Promise(resolve => setTimeout(resolve, 5)); }
  }
  available = false;
  await expect(f.delegated.preflight("project", "turn:new")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  expect(await f.client.interruptDelegatedTurn("project", "drift-interrupt", compatibility)).toMatchObject({ interrupted: true });
  expect((await turn).terminal.outcome).toBe("interrupted");
  await expect(f.delegated.preflight("project", "interrupt:foreign")).rejects.toMatchObject({ code: "FORBIDDEN" });
});

it("binds selected role policy to retirement and passes it to resume selection", async () => {
  const f = await fixture();
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const first = await f.client.runDelegatedTurn("project", compatibility, { turnId: "role-prior", prompt: "hello", requestedRole: "agent2" });
  expect((await f.retirement.read("role-prior"))?.rolePolicyDigest).toBe(first.roleEvidence.policyDigest);
  const original = f.retirement.restart.bind(f.retirement);
  let observed: string | undefined;
  f.retirement.restart = async (turnId, identity, digest) => { observed = digest; return original(turnId, identity, digest); };
  const second = await f.client.runDelegatedTurn("project", compatibility, { turnId: "role-next", previousTurnId: "role-prior", prompt: "hello", requestedRole: "agent0" });
  expect(observed).toBe(second.roleEvidence.policyDigest);
  expect(observed).not.toBe(first.roleEvidence.policyDigest);
});

it("cancels and drains a login startup racing daemon stop without returning a live login", async () => {
  let entered!: () => void, release!: () => void;
  const started = new Promise<void>(resolve => { entered = resolve; });
  const blocked = new Promise<void>(resolve => { release = resolve; });
  let starts = 0, cancellations = 0, live = false;
  const f = await fixture(false, {
    async startLogin() { starts++; entered(); await blocked; live = true; return { loginId: "race-login", authUrl: "https://example.com/auth" }; },
    async status() { return { state: "pending", evidenceClass: "controlled-fixture" }; },
    async cancel() { cancellations++; live = false; release(); }
  });
  const request = f.operator.startHostedLogin("project", compatibility).then(value => ({ value }), error => ({ error }));
  await started;
  await f.daemon.stop();
  expect(await request).toMatchObject({ error: { code: "ENGINE_UNAVAILABLE" } });
  expect(starts).toBe(1);
  expect(cancellations).toBeGreaterThanOrEqual(2);
  expect(live).toBe(false);
  expect(await f.worker.inventory()).toEqual([]);
});
it("cancels a current login on shutdown and cannot admit another start", async () => {
  let starts = 0, live = false;
  const f = await fixture(false, {
    async startLogin() { starts++; live = true; return { loginId: "current-login", authUrl: "https://example.com/auth" }; },
    async status() { return { state: "pending", evidenceClass: "controlled-fixture" }; },
    async cancel() { live = false; }
  });
  await f.operator.startHostedLogin("project", compatibility);
  expect(live).toBe(true);
  await f.daemon.stop();
  expect(live).toBe(false);
  await expect(f.operator.startHostedLogin("project", compatibility)).rejects.toBeDefined();
  expect(starts).toBe(1);
});
it("reports degraded shutdown within grace when configured login cancellation cannot drain", async () => {
  let release!: () => void;
  const blocked = new Promise<void>(resolve => { release = resolve; });
  const f = await fixture(false, {
    async startLogin() { return { loginId: "stuck-login", authUrl: "https://example.com/auth" }; },
    async status() { return { state: "pending", evidenceClass: "controlled-fixture" }; },
    async cancel() { await blocked; }
  });
  // This case intentionally leaves the daemon degraded; do not demand a later
  // successful stop from the generic fixture teardown.
  cleanups.pop();
  await f.operator.startHostedLogin("project", compatibility);
  const began = performance.now();
  try {
    const stopping = f.daemon.stop();
    await expect(f.daemon.start()).rejects.toThrow("before shutdown has drained");
    await expect(stopping).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(performance.now() - began).toBeLessThan(2800);
    await expect(f.daemon.stop()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  } finally { release(); }
});

it("requires explicit on consent matching the immutable configured worker posture", async () => {
  const f = await fixture(false, undefined, false, "on");
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  await expect(f.client.runDelegatedTurn("project", compatibility, { turnId: "on-blocked", prompt: "hello" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  expect(await f.worker.inventory()).toEqual([]);
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "on", approvedBy: "fixture-owner", explicitUserAct: true });
  const capabilities = await f.client.delegatedCapabilities("project");
  expect(capabilities.commandNetwork.find(item => item.posture === "on")).toMatchObject({ configured: true, executionSupported: true });
  expect((await f.client.runDelegatedTurn("project", compatibility, { turnId: "on-controlled", prompt: "hello" })).terminal.outcome).toBe("completed");
});

it("does not commit completed when worker retirement reports unresolved descendants", async () => {
  const f = await fixture();
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const retire = f.binding.supervisor.retire.bind(f.binding.supervisor);
  let cleaned = false;
  f.binding.supervisor.retire = async (workerId, generation) => {
    if (!cleaned) { await retire(workerId, generation); cleaned = true; }
    throw new Error("controlled unresolved descendant observation");
  };
  await expect(f.client.runDelegatedTurn("project", compatibility, { turnId: "retirement-fails", prompt: "hello" })).rejects.toBeDefined();
  expect((await f.retirement.read("retirement-fails"))?.terminal?.outcome).toBe("failed");
});

function controlledApprovalWorker(identity: Parameters<typeof createControlledCodexSupervisorForTests>[0]["identity"]) {
  let notify: (message: unknown) => void = () => {};
  const worker = createControlledCodexSupervisorForTests({ identity, model: "fixture", commandNetworkPosture: "ask-per-destination", turnTimeoutMs: 3000,
    async launch() {
      const stdin = new PassThrough(), stdout = new PassThrough(); notify = message => { stdout.write(JSON.stringify(message) + "\n"); };
      stdin.on("data", chunk => {
        for (const line of String(chunk).trim().split("\n")) {
          const request = JSON.parse(line);
          if (request.method === "initialized") continue;
          if (!request.method) {
            notify({ method: "item/completed", params: { threadId: "private-thread", turnId: "private-turn", item: { id: "answer", type: "agentMessage", text: request.result.decision } } });
            notify({ method: "turn/completed", params: { threadId: "private-thread", turn: { id: "private-turn", status: "completed" } } }); continue;
          }
          notify({ id: request.id, result: request.method === "account/read" ? { requiresOpenaiAuth: true, account: { type: "fixture" } } : request.method === "thread/start" ? { thread: { id: "private-thread" } } : request.method === "turn/start" ? { turn: { id: "private-turn" } } : {} });
          if (request.method === "turn/start") setImmediate(() => notify({ id: "provider-request", method: "item/commandExecution/requestApproval", params: { threadId: "private-thread", turnId: "private-turn", itemId: "network-item", startedAtMs: 1, networkApprovalContext: { host: "example.com", protocol: "socks5Tcp" }, availableDecisions: ["accept", "decline", "acceptForSession"] } }));
        }
      });
      return { pid: 123456, transport: { stdin, stdout, async close() {} } };
    }
  });
  return { acquire: (id: string, input: string) => worker.acquire(id, JSON.stringify({ prompt: input })), inventory: worker.inventory.bind(worker), reconnect: worker.reconnect.bind(worker), wait: worker.wait.bind(worker), retire: worker.retire.bind(worker), close: worker.close.bind(worker), pendingNetworkApprovals: worker.pendingNetworkApprovals.bind(worker), replyNetworkApproval: worker.replyNetworkApproval.bind(worker),
    cancelPending() { notify({ method: "serverRequest/resolved", params: { threadId: "private-thread", requestId: "provider-request" } }); } };
}
it.each(["allow", "deny", "acceptForSession"] as const)("routes explicit %s through client, authenticated daemon, durable store, private supervisor and actual actor reply", async decision => {
  const f = await fixture(false, undefined, false, "ask-per-destination", true);
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "ask-per-destination", approvedBy: "fixture-owner", explicitUserAct: true });
  const turn = f.client.runDelegatedTurn("project", compatibility, { turnId: "wire-turn", prompt: "controlled only" });
  let prompt: any;
  for (let i = 0; i < 100 && !prompt; i++) { try { const pending = await f.client.pendingDelegatedApprovals("project", "wire-turn"); prompt = (pending as any[])[0]; } catch {} if (!prompt) await new Promise(resolve => setTimeout(resolve, 5)); }
  expect(prompt).toMatchObject({ networkApprovalContext: { host: "example.com", protocol: "socks5Tcp" }, requestedBy: "trusted-codex-supervisor", availableDecisions: ["allow", "deny", "acceptForSession"] });
  expect(prompt.caveat).toContain("queued requests");
  await expect(f.client.decideDelegatedApproval("project", prompt.requestId, compatibility, { turnId: "wire-turn", workerGeneration: "wrong-generation", decision, approvedBy: "fixture-human", explicitUserAct: true })).rejects.toMatchObject({ code: "FORBIDDEN" });
  await expect(f.client.decideDelegatedApproval("project", prompt.requestId, compatibility, { turnId: "wire-turn", workerGeneration: prompt.binding.workerGeneration, decision, approvedBy: "fixture-human", explicitUserAct: false as never })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  const result = await f.client.decideDelegatedApproval("project", prompt.requestId, compatibility, { turnId: "wire-turn", workerGeneration: prompt.binding.workerGeneration, decision, approvedBy: "fixture-human", explicitUserAct: true });
  expect(result.applied).toBe(true); expect(result.reason).toContain("not an execution acknowledgement");
  expect((await turn).output).toBe(decision === "allow" ? "accept" : decision === "deny" ? "decline" : decision);
  expect(await f.worker.inventory()).toEqual([]);
});
it("carries provider cancellation into immutable resolution and refuses a queued explicit grant", async () => {
  const f = await fixture(false, undefined, false, "ask-per-destination", true);
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "ask-per-destination", approvedBy: "fixture-owner", explicitUserAct: true });
  const running = f.client.runDelegatedTurn("project", compatibility, { turnId: "cancel-wire", prompt: "controlled only" });
  const settled = running.catch(error => error);
  let prompt: any;
  for (let i = 0; i < 100 && !prompt; i++) { try { prompt = ((await f.client.pendingDelegatedApprovals("project", "cancel-wire")) as any[])[0]; } catch {} if (!prompt) await new Promise(resolve => setTimeout(resolve, 5)); }
  expect(prompt).toBeDefined();
  await expect(f.binding.supervisor.pendingNetworkApprovals("cancel-wire", "wrong-generation")).rejects.toThrow();
  (f.worker as ReturnType<typeof controlledApprovalWorker>).cancelPending();
  expect(await f.client.pendingDelegatedApprovals("project", "cancel-wire")).toEqual([]);
  const record = await f.binding.approvals.read(prompt.requestId, prompt.binding);
  expect(record.resolution).toMatchObject({ reason: "provider-resolved", resolvedBy: "trusted-codex-supervisor" });
  expect(record.decision).toBeUndefined();
  await expect(f.client.decideDelegatedApproval("project", prompt.requestId, compatibility, { turnId: "cancel-wire", workerGeneration: prompt.binding.workerGeneration, decision: "acceptForSession", approvedBy: "fixture-human", explicitUserAct: true })).rejects.toMatchObject({ code: "FORBIDDEN" });
  await f.client.interruptDelegatedTurn("project", "cancel-wire", compatibility); await settled;
  expect(await f.worker.inventory()).toEqual([]);
});
