import { PassThrough } from "node:stream";
import { createControlledCodexSupervisorForTests } from "../packages/daemon/src/codex-supervisor.js";
import { mkdtemp, mkdir, realpath, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { RuntimeError, validateHarnessEventV2, type WorkerHandle, type WorkerResult } from "@chirality/runtime-contracts";
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
  const login = { async startLogin() { starts++; return { loginId: "fixture-login", authUrl: "https://example.com/authorize?state=fixture" }; }, async status() { return { schema: "chirality-hosted-login-status/v2" as const, state: "pending" as const, loginId: "fixture-login", evidenceClass: "controlled-fixture" as const, binding: { schema: "chirality-hosted-account-binding/v1" as const, state: "unavailable" as const, reason: "canonical-identity-producer-unavailable" as const }, hostedReady: false as const }; }, async cancel() { cancels++; } };
  const f = await fixture(false, login, true);
  await expect(f.client.startHostedLogin("project", compatibility)).rejects.toMatchObject({ code: "FORBIDDEN" });
  expect(starts).toBe(0);
  const result = await f.operator.startHostedLogin("project", compatibility);
  expect(result.loginId).toBe("fixture-login");
  expect(starts).toBe(1);
  expect(await f.operator.hostedLoginStatus("project")).toEqual({ schema: "chirality-hosted-login-status/v2", state: "pending", loginId: "fixture-login", evidenceClass: "controlled-fixture", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" }, hostedReady: false });
  await expect(f.client.hostedLoginStatus("project")).rejects.toMatchObject({ code: "FORBIDDEN" });
  const loginPreflight = await f.delegated.preflight("project", "login:start");
  await expect(f.delegated.turn("project", { turnId: "not-login", prompt: "x", compatibility, preflight: loginPreflight })).rejects.toMatchObject({ code: "RUNTIME_COMPATIBILITY_MISMATCH" });
  await expect(f.delegated.preflight("project", "turn:blocked")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  expect(await f.operator.cancelHostedLogin("project", compatibility)).toEqual({ cancelled: true });
  expect(cancels).toBe(1);
  expect(await f.worker.inventory()).toEqual([]);
});
it("rejects secret-bearing internal login status without exposing it or admitting work", async () => {
  const status = { schema: "chirality-hosted-login-status/v2" as const, state: "pending" as const, loginId: "fixture-login", evidenceClass: "controlled-fixture" as const, binding: { schema: "chirality-hosted-account-binding/v1" as const, state: "unavailable" as const, reason: "canonical-identity-producer-unavailable" as const }, hostedReady: false as const, providerSecret: "must-not-project" };
  const f = await fixture(false, { async startLogin() { throw new Error("Unexpected login start"); }, async status() { return status; }, async cancel() {} }, true);
  const rejected = await f.operator.hostedLoginStatus("project").then(value => ({ value }), error => ({ error }));
  expect(rejected).toMatchObject({ error: { code: "INTERNAL_FAILURE", status: 500 } });
  expect(JSON.stringify(rejected)).not.toContain("must-not-project");
  expect(String("error" in rejected ? rejected.error : rejected.value)).not.toContain("must-not-project");
  await expect(f.client.hostedLoginStatus("project")).rejects.toMatchObject({ code: "FORBIDDEN" });
  await expect(f.delegated.preflight("project", "turn:blocked")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
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

it("leaves retirement unresolved when cleanup reports unresolved descendants", async () => {
  const f = await fixture();
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const retire = f.binding.supervisor.retire.bind(f.binding.supervisor);
  let cleaned = false;
  f.binding.supervisor.retire = async (workerId, generation) => {
    if (!cleaned) { await retire(workerId, generation); cleaned = true; }
    throw new Error("controlled unresolved descendant observation");
  };
  await expect(f.client.runDelegatedTurn("project", compatibility, { turnId: "retirement-fails", prompt: "hello" })).rejects.toBeDefined();
  expect((await f.retirement.read("retirement-fails"))?.state).toBe("prepared");
  expect((await f.retirement.read("retirement-fails"))?.terminal).toBeUndefined();
  await expect(f.retirement.restart("retirement-fails", f.identity)).rejects.toMatchObject({ code: "DELEGATION_POLICY_VIOLATION" });
});

it("reports the worker's own failure with a failed retirement attached as its cause", async () => {
  const f = await fixture();
  await f.client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
  const retire = f.binding.supervisor.retire.bind(f.binding.supervisor);
  f.binding.supervisor.wait = async () => { throw new RuntimeError("ENGINE_UNAVAILABLE", "controlled primary worker failure", 503, { reason: "CODEX_PROTOCOL_FAILURE" }); };
  f.binding.supervisor.retire = async (workerId, generation) => { await retire(workerId, generation); throw new RuntimeError("ENGINE_UNAVAILABLE", "controlled unresolved descendant observation", 503, { reason: "DESCENDANT_RECONCILIATION_REQUIRED" }); };
  const preflight = await f.delegated.preflight("project", "turn:primary-kept");
  const failure = await f.delegated.turn("project", { compatibility, preflight, turnId: "primary-kept", prompt: "hello" }).then(() => undefined, error => error as RuntimeError);
  expect(failure).toMatchObject({ code: "ENGINE_UNAVAILABLE", message: "controlled primary worker failure", details: { reason: "CODEX_PROTOCOL_FAILURE" } });
  expect(failure?.cause).toMatchObject({ message: "controlled unresolved descendant observation", details: { reason: "DESCENDANT_RECONCILIATION_REQUIRED" } });
  expect((await f.retirement.read("primary-kept"))?.state).toBe("prepared");
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
          notify({ id: request.id, result: request.method === "account/read" ? { requiresOpenaiAuth: true, account: { type: "apiKey" } } : request.method === "thread/start" ? { thread: { id: "private-thread" } } : request.method === "turn/start" ? { turn: { id: "private-turn" } } : {} });
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
  void turn.catch(() => {}); // Observe early failure; the original promise must still satisfy the final await below.
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

function retirementGate<T>() {
  let resolve!: (value: T) => void, reject!: (error: unknown) => void;
  const promise = new Promise<T>((yes, no) => { resolve = yes; reject = no; });
  void promise.catch(() => {});
  return { promise, resolve, reject };
}

/** No supplier, process or network: control retirement independently of wait. */
async function controlledRetirementFixture(lateApproval = false) {
  const root = await realpath(await mkdtemp(join(tmpdir(), "retirement-barrier-")));
  cleanups.push(() => rm(root, { recursive: true, force: true }));
  const identity = { canonicalRoot: root, cwd: root, accountId: "controlled-no-account", accountEpoch: 1, policyDigest: "fixture-policy" };
  const retirement = new WorkerRetirementCoordinator({ directory: join(root, "journal") });
  const waited = retirementGate<void>(), finished = retirementGate<WorkerResult>();
  const retiring = retirementGate<void>(), cleanup = retirementGate<void>();
  const pollingStarted = retirementGate<void>(), polling = retirementGate<never[]>();
  const calls: { workerId: string; generation: string }[] = [];
  let live: WorkerHandle | undefined;
  const supervisor = {
    async acquire(workerId: string) { live = { workerId, generation: "controlled-generation", pid: 0, state: "running" }; return { ...live }; },
    async inventory() { return live ? [{ ...live }] : []; },
    async reconnect() { if (!live) throw new Error("No controlled worker"); return { ...live }; },
    async wait() { waited.resolve(); return finished.promise; },
    async retire(workerId: string, generation: string) { calls.push({ workerId, generation }); retiring.resolve(); await cleanup.promise; live = undefined; },
    async pendingNetworkApprovals() { pollingStarted.resolve(); return polling.promise; },
    async replyNetworkApproval() { return { sent: true as const }; }
  };
  const consent = {
    async read() { return { identity, posture: "off" as const, approvedBy: "controlled-test", approvedAt: "2026-09-06T00:00:00.000Z" }; },
    async grant() {}, async authorizeDestination() {}
  };
  const runtime = new DelegatedRuntime({ daemonId: "retirement-test", projects: new Map([["p", { identity, compatibility, supervisor, retirement, consent, evidenceClass: "controlled-worker", ...(lateApproval ? { approvalForwardingEnabled: true, approvals: new ApprovalStore({ canonicalRoot: root, storageRoot: join(root, "approvals"), consent, isLive: async () => true }) } : {}) }]]) });
  return {
    runtime, retirement, identity, retiring, cleanup, calls, pollingStarted, polling,
    finish() { finished.resolve({ worker: { ...live! }, exitCode: 0, signal: null, threadId: "controlled-thread", stdout: "controlled", stderr: "" }); },
    fail(error: unknown) { finished.reject(error); },
    async start() {
      const preflight = await runtime.preflight("p", "turn:t");
      const turn = runtime.turn("p", { turnId: "t", prompt: "no execution", compatibility, preflight });
      void turn.catch(() => {});
      await waited.promise;
      return { turn };
    },
    async assertUnresolved() {
      expect((await retirement.read("t"))?.state).toBe("prepared");
      expect((await retirement.read("t"))?.terminal).toBeUndefined();
      await expect(retirement.restart("t", identity)).rejects.toMatchObject({ code: "DELEGATION_POLICY_VIOLATION" });
      const preflight = await runtime.preflight("p", "turn:next");
      await expect(runtime.turn("p", { turnId: "next", previousTurnId: "t", prompt: "no replay", compatibility, preflight })).rejects.toMatchObject({ code: "DELEGATION_POLICY_VIOLATION" });
      expect(await retirement.read("next")).toBeUndefined();
      const replay = await runtime.preflight("p", "turn:t");
      await expect(runtime.turn("p", { turnId: "t", prompt: "no replay", compatibility, preflight: replay })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    }
  };
}
const unresolvedRetirement = () => new RuntimeError("ENGINE_UNAVAILABLE", "Controlled unresolved descendant", 503, { reason: "DESCENDANT_RECONCILIATION_REQUIRED" });

it("joins successful wait to retirement failure without terminal, restart, or unrelated reconciliation", async () => {
  const f = await controlledRetirementFixture();
  await f.retirement.prepare({ turnId: "unrelated", identity: f.identity, state: "prepared" });
  const { turn } = await f.start();
  const error = unresolvedRetirement();
  f.finish(); await f.retiring.promise;
  expect((await f.retirement.read("t"))?.terminal).toBeUndefined();
  f.cleanup.reject(error);
  await expect(turn).rejects.toBe(error);
  await f.assertUnresolved();
  expect(f.calls).toEqual([{ workerId: "t", generation: "controlled-generation" }]);
  expect((await f.retirement.read("unrelated"))?.state).toBe("prepared");
});

it.each([true, false])("wait failure requires confirmed retirement before failed commitment (cleanup succeeds: %s)", async succeeds => {
  const f = await controlledRetirementFixture(), waitError = new Error("controlled transport failure"), cleanupError = unresolvedRetirement();
  const { turn } = await f.start();
  f.fail(waitError); await f.retiring.promise;
  expect((await f.retirement.read("t"))?.terminal).toBeUndefined();
  if (succeeds) f.cleanup.resolve(); else f.cleanup.reject(cleanupError);
  // The transport failure stays the reported error; an unconfirmed retirement travels with it as the cause.
  await expect(turn).rejects.toBe(waitError);
  expect(waitError.cause).toBe(succeeds ? undefined : cleanupError);
  if (succeeds) expect(await f.retirement.read("t")).toMatchObject({ state: "committed", terminal: { outcome: "failed" } });
  else await f.assertUnresolved();
  expect(f.calls).toEqual([{ workerId: "t", generation: "controlled-generation" }]);
});

it.each([
  { first: "completion", succeeds: true }, { first: "completion", succeeds: false },
  { first: "interrupt", succeeds: true }, { first: "interrupt", succeeds: false }
])("shares the retirement barrier when $first starts first (cleanup succeeds: $succeeds)", async ({ first, succeeds }) => {
  const f = await controlledRetirementFixture(), error = unresolvedRetirement();
  const { turn } = await f.start();
  const preflight = await f.runtime.preflight("p", "interrupt:t");
  if (first === "completion") { f.finish(); await f.retiring.promise; }
  const interrupted = f.runtime.interruptTurn("p", { turnId: "t", compatibility, preflight });
  void interrupted.catch(() => {});
  if (first === "interrupt") { await f.retiring.promise; f.finish(); }
  // Drain the already-started admissions; cleanup is held by an explicit gate.
  await new Promise<void>(resolve => setImmediate(resolve));
  expect(f.calls).toEqual([{ workerId: "t", generation: "controlled-generation" }]);
  expect((await f.retirement.read("t"))?.terminal).toBeUndefined();
  if (succeeds) f.cleanup.resolve(); else f.cleanup.reject(error);
  if (succeeds) {
    await expect(interrupted).resolves.toMatchObject({ interrupted: true });
    await expect(turn).resolves.toMatchObject({ terminal: { outcome: "interrupted" }, event: { type: "turn.interrupted" } });
    expect(await f.retirement.read("t")).toMatchObject({ state: "committed", terminal: { outcome: "interrupted" } });
  } else {
    await expect(interrupted).rejects.toBe(error); await expect(turn).rejects.toBe(error);
    await f.assertUnresolved();
  }
  expect(f.calls).toEqual([{ workerId: "t", generation: "controlled-generation" }]);
});


it.each([true, false])("late approval failure joins settled retirement after turn cleanup (retirement succeeds: %s)", async succeeds => {
  const f = await controlledRetirementFixture(true), waitError = new Error("controlled wait failure"), cleanupError = unresolvedRetirement();
  const { turn } = await f.start();
  await f.pollingStarted.promise;
  f.fail(waitError); await f.retiring.promise;
  if (succeeds) f.cleanup.resolve(); else f.cleanup.reject(cleanupError);
  await expect(turn).rejects.toBe(waitError);
  expect(waitError.cause).toBe(succeeds ? undefined : cleanupError);
  const record = await f.retirement.read("t");
  expect(record?.state).toBe(succeeds ? "committed" : "prepared");
  if (succeeds) expect(record?.terminal?.outcome).toBe("failed");
  else await f.assertUnresolved();
  expect(f.calls).toEqual([{ workerId: "t", generation: "controlled-generation" }]);
  f.polling.reject(new Error("controlled late approval snapshot failure"));
  await new Promise<void>(resolve => setImmediate(resolve));
  expect(f.calls).toEqual([{ workerId: "t", generation: "controlled-generation" }]);
  expect((f.runtime as unknown as { turnRetirements: Map<string, Promise<void>> }).turnRetirements.size).toBe(0);
  expect(await f.retirement.read("t")).toEqual(record);
});

describe("per-turn catalog choice through the delegated hosted envelope", () => {
  const catalog = {
    models: [
      { model: "gpt-default", isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["medium", "high"] },
      { model: "gpt-alt", isDefault: false, defaultReasoningEffort: "low", supportedReasoningEfforts: ["low", "medium"] }
    ],
    default: { model: "gpt-default", isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["medium", "high"] }
  };
  async function catalogFixture(withCatalog = true) {
    const root = await realpath(await mkdtemp(join(tmpdir(), "dr-catalog-")));
    cleanups.push(() => rm(root, { recursive: true, force: true }));
    const project = join(root, "project"); await mkdir(project);
    const identity = { canonicalRoot: project, cwd: project, accountId: "controlled-account", accountEpoch: 1, policyDigest: "fixture-policy" };
    const acquired: string[] = [];
    const supervisor = {
      async acquire(workerId: string, input: string): Promise<WorkerHandle> { acquired.push(input); return { workerId, generation: "g1", pid: 4242, state: "running" }; },
      async inventory() { return []; },
      async reconnect(workerId: string, generation: string): Promise<WorkerHandle> { return { workerId, generation, pid: 4242, state: "running" }; },
      async wait(workerId: string, generation: string): Promise<WorkerResult> { return { worker: { workerId, generation, pid: 4242, state: "exited" }, exitCode: 0, signal: null, threadId: "thread-catalog", stdout: "done", stderr: "" }; },
      async retire() {}
    };
    const consent = new HostedConsentStore({ canonicalRoot: project, codexHome: join(root, "home") });
    await consent.grant({ identity, posture: "off", approvedBy: "fixture-owner", approvedAt: new Date(0).toISOString() });
    const retirement = new WorkerRetirementCoordinator({ directory: join(root, "journal") });
    const delegated = new DelegatedRuntime({ daemonId: "catalog-daemon", projects: new Map([["project", {
      identity, compatibility, supervisor, consent, retirement, commandNetworkPosture: "off" as const, evidenceClass: "controlled-worker" as const,
      actual: { adapterId: "codex-app-server", providerId: "openai", model: "gpt-default", reasoningEffort: "high" }, ...(withCatalog ? { catalog } : {})
    }]]) });
    const turn = async (turnId: string, choice: { model?: string; reasoningEffort?: string }) => delegated.turn("project", { compatibility, preflight: await delegated.preflight("project", `turn:${turnId}`), turnId, prompt: "hello", ...choice });
    return { delegated, acquired, retirement, turn, supervisor };
  }
  it("latches cancellation before acquisition publication and awaits genuine terminal settlement", async () => {
    const f = await catalogFixture();
    let publish!: () => void, began!: () => void, finish!: (result: WorkerResult) => void;
    const entered = new Promise<void>(resolve => { began = resolve; });
    const gate = new Promise<void>(resolve => { publish = resolve; });
    const terminal = new Promise<WorkerResult>(resolve => { finish = resolve; });
    const acquire = f.supervisor.acquire;
    f.supervisor.acquire = async (id, input) => { began(); await gate; return acquire(id, input); };
    f.supervisor.wait = async () => terminal;
    let interrupts = 0;
    Object.assign(f.supervisor, { async drainTurnProgress() { return []; }, async interrupt(id: string, generation: string) {
      expect([id, generation]).toEqual(["early", "g1"]); interrupts++;
    } });
    const controller = new AbortController();
    const request = { compatibility, preflight: await f.delegated.preflight("project", "turn:early"), turnId: "early", prompt: "bootstrap" };
    let settled = false;
    const running = f.delegated.turn("project", request, [], { signal: controller.signal, onProgress() {} }).finally(() => { settled = true; });
    await entered; controller.abort(); expect(interrupts).toBe(0); publish();
    await expect.poll(() => interrupts).toBe(1); expect(settled).toBe(false);
    finish({ worker: { workerId: "early", generation: "g1", pid: 4242, state: "exited" }, exitCode: null, signal: "SIGTERM", stdout: "", stderr: "" });
    await expect(running).resolves.toMatchObject({ terminal: { outcome: "interrupted" } });
  });

  it("carries the chosen model and effort in the envelope and stamps them on the terminal attribution", async () => {
    const f = await catalogFixture();
    const chosen = await f.turn("chosen", { model: "gpt-alt", reasoningEffort: "medium" });
    expect(JSON.parse(f.acquired[0]!)).toMatchObject({ prompt: "hello", model: "gpt-alt", reasoningEffort: "medium" });
    expect(chosen.event.attribution).toEqual({ adapterId: "codex-app-server", providerId: "openai", model: "gpt-alt", reasoningEffort: "medium" });
    expect(chosen.roleEvidence.actual).toEqual(chosen.event.attribution);
    expect(validateHarnessEventV2(chosen.event)).toBe(true);
    const admitted = await f.turn("admitted", {});
    expect(f.acquired[1]).toBe("hello");
    expect(admitted.event.attribution).toEqual({ adapterId: "codex-app-server", providerId: "openai", model: "gpt-default", reasoningEffort: "high" });
    const modelOnly = await f.turn("model-only", { model: "gpt-alt" });
    expect(JSON.parse(f.acquired[2]!)).toMatchObject({ model: "gpt-alt" });
    expect(JSON.parse(f.acquired[2]!)).not.toHaveProperty("reasoningEffort");
    expect(modelOnly.event.attribution).toEqual({ adapterId: "codex-app-server", providerId: "openai", model: "gpt-alt", reasoningEffort: "low" });
  });
  it("refuses an unknown model or unsupported effort before any envelope is sent", async () => {
    const f = await catalogFixture();
    await expect(f.turn("unknown", { model: "gpt-unknown", reasoningEffort: "low" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", status: 503, details: { reason: "MODEL_NOT_IN_CATALOG", model: "gpt-unknown", available: ["gpt-default", "gpt-alt"] } });
    await expect(f.turn("effort", { model: "gpt-alt", reasoningEffort: "high" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", status: 503, details: { reason: "REASONING_EFFORT_UNSUPPORTED", model: "gpt-alt", supported: ["low", "medium"] } });
    await expect(f.turn("shape", { model: "gpt alt" })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    expect(f.acquired).toEqual([]);
    expect(await f.retirement.read("unknown")).toBeUndefined();
    const uncatalogued = await catalogFixture(false);
    await expect(uncatalogued.turn("other", { model: "gpt-alt" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", status: 503, details: { reason: "MODEL_NOT_IN_CATALOG", model: "gpt-alt", available: ["gpt-default"] } });
    await expect(uncatalogued.turn("other-effort", { reasoningEffort: "low" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", status: 503, details: { reason: "REASONING_EFFORT_UNSUPPORTED" } });
    expect(uncatalogued.acquired).toEqual([]);
    const same = await uncatalogued.turn("same", { model: "gpt-default", reasoningEffort: "high" });
    expect(JSON.parse(uncatalogued.acquired[0]!)).toMatchObject({ model: "gpt-default", reasoningEffort: "high" });
    expect(same.event.attribution).toEqual({ adapterId: "codex-app-server", providerId: "openai", model: "gpt-default", reasoningEffort: "high" });
  });
});
