import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { Readable } from "node:stream";
import * as fs from "node:fs/promises";
import * as childProcess from "node:child_process";
import * as os from "node:os";
import * as core from "@chirality/runtime-core";
import { RuntimeError, validateHostedLoginStatus, validateHostedManagedAuth } from "@chirality/runtime-contracts";
import { RuntimeClient } from "../packages/client/src/client.js";
import { RuntimeDaemon } from "../packages/daemon/src/runtime-daemon.js";
import { SupervisorClient } from "../packages/daemon/src/supervisor-server.js";
import { CodexLogin } from "../packages/daemon/src/codex-login.js";
import { CodexSupervisor } from "../packages/daemon/src/codex-supervisor.js";
import { prepareCodexContainment, prepareCodexContainmentV2, prepareCodexNativePolicy, prepareCodexTrustedSupplierContainmentV2 } from "../packages/daemon/src/codex-containment.js";

// Mocks guard source-level process/filesystem effects. No supplier is invoked.
vi.mock("node:child_process", async importOriginal => ({ ...await importOriginal<typeof import("node:child_process")>(), spawn: vi.fn(() => { throw new Error("Unexpected process launch"); }) }));
vi.mock("node:os", async importOriginal => { const actual = await importOriginal<typeof import("node:os")>(); return { ...actual, userInfo: vi.fn(actual.userInfo) }; });
vi.mock("node:fs/promises", async importOriginal => {
  const actual = await importOriginal<typeof import("node:fs/promises")>();
  return { ...actual, ...Object.fromEntries(["stat", "lstat", "realpath", "mkdtemp", "writeFile", "open", "rm", "mkdir", "readFile"].map(key => [key, vi.fn(() => { throw new Error(`Unexpected filesystem effect: ${key}`); })])) };
});
vi.mock("@chirality/runtime-core", async importOriginal => {
  const actual = await importOriginal<typeof import("@chirality/runtime-core")>();
  return { ...actual, ...Object.fromEntries(["privateDirectory", "verifyExactSupply", "revalidateExactSupply", "assertContinuity"].map(key => [key, vi.fn(() => { throw new Error(`Unexpected admission effect: ${key}`); })])) };
});
const binding = { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } as const;
const managedAuth = { backend: "keyring", binding } as const;
const status = { schema: "chirality-hosted-login-status/v2", state: "completed", loginId: "fixture-login-1", hasAccount: true, evidenceClass: "controlled-fixture", binding, hostedReady: false } as const;
const oldStatus = { state: "completed", loginId: "fixture-login-1", hasAccount: true, evidenceClass: "controlled-fixture", authBindingSha256: "a".repeat(64) };
const malformed: unknown[] = [oldStatus, { ...status, schema: undefined }, { ...status, schema: "chirality-hosted-login-status/v1" }, { ...status, hostedReady: true }, { ...status, authBindingSha256: "a".repeat(64) }, { ...status, token: "synthetic-secret" }, { ...status, email: "synthetic@example.test" }, { ...status, planType: "plus" }, { ...status, authUrl: "https://auth.openai.com/fixture" }, { ...status, binding: { ...binding, accountId: "caller-principal" } }, { ...status, binding: { schema: binding.schema, state: "verified" } }, { ...status, loginId: "x".repeat(513) }, { ...status, hasAccount: "true" }, { ...status, extra: null }];
const fileEffects = [fs.stat, fs.lstat, fs.realpath, fs.mkdtemp, fs.writeFile, fs.open, fs.rm, fs.mkdir, fs.readFile];
const originalPlatform = Object.getOwnPropertyDescriptor(process, "platform")!;
beforeEach(() => { vi.clearAllMocks(); });
afterEach(() => { Object.defineProperty(process, "platform", originalPlatform); vi.restoreAllMocks(); });

function clientFixture(body: unknown) {
  const client = new RuntimeClient({ socketPath: "/synthetic/runtime.sock", tokenFile: "/synthetic/token", loadToken: async () => "synthetic-control-token" });
  const request = vi.spyOn(client as any, "request").mockImplementation(async () => Object.assign(Readable.from([JSON.stringify(body)]), { statusCode: 200 }));
  return { client, request };
}
// Baseline bf204d8f client.ts SHA256 ac41f4cf3977a86660cf61d64a1ebe816666dcc8aa3ffe7b3e6f65992de01367:
// hostedLoginStatus called requestJson(GET); successful JSON was returned via unchecked `value as T`.
// This source-pinned semantic fixture is not an old packaged binary qualification.
async function oldClientStatus(client: RuntimeClient, projectId: string): Promise<unknown> {
  return client.requestJson(`/v2/projects/${encodeURIComponent(projectId)}/login/status`, { method: "GET" });
}
function daemonFixture(body: unknown, authorized = true) {
  const auth = vi.fn(async () => { if (!authorized) throw new RuntimeError("FORBIDDEN", "Synthetic authorization denied", 403); return { clientId: "fixture" }; });
  const requireAuthorized = vi.fn(async () => ({ canonicalRoot: "/synthetic/project" }));
  const assertProjectRoot = vi.fn();
  const loginStatus = vi.fn(async () => body);
  const daemon = new RuntimeDaemon({ socketPath: "/synthetic/runtime.sock", runtimeDirectory: "/synthetic", service: { auth: { authenticate: auth }, projects: { requireAuthorized } } as any, delegated: { assertProjectRoot } as any, loginProjectId: "project", login: { status: loginStatus, startLogin: vi.fn(), cancel: vi.fn() } as any });
  const generation = {};
  Object.assign(daemon, { lifecycle: "RUNNING", generation });
  const request = { method: "GET", url: "/v2/projects/project/login/status", headers: { authorization: "Bearer synthetic-control-token" } };
  let code = 0, result: unknown;
  const response = { headersSent: false, writeHead(value: number) { code = value; }, end(value: string) { result = JSON.parse(value); } };
  return { auth, requireAuthorized, assertProjectRoot, loginStatus, request, async route() { await (daemon as any).route(request, response, generation); return { code, body: result }; } };
}

describe("custody versioned unavailable status and compatibility", () => {
  it.each(["pending", "completed", "failed"] as const)("accepts %s ceremony only as unavailable", state => {
    expect(validateHostedLoginStatus({ ...status, state })).toEqual({ ...status, state });
  });
  it.each(malformed.map((body, index) => ({ body, index })))("rejects malformed, legacy, mixed or secret-bearing status $index", ({ body }) => {
    expect(() => validateHostedLoginStatus(body)).toThrowError(expect.objectContaining({ code: "INVALID_REQUEST" }));
  });
  it("preserves the public opaque login identifier bound independently of the producer", () => {
    expect(validateHostedLoginStatus({ ...status, loginId: "x".repeat(512) }).loginId).toHaveLength(512);
  });
  it("supports paired updated daemon/client with completed ceremony and no hosted readiness", async () => {
    const daemon = daemonFixture(status); const projection = await daemon.route();
    expect(projection).toEqual({ code: 200, body: status });
    const { client } = clientFixture(projection.body);
    expect(await client.hostedLoginStatus("project")).toEqual(status);
    expect(daemon.auth).toHaveBeenCalledWith("Bearer synthetic-control-token", "credentials:write", "project");
    expect(daemon.assertProjectRoot).toHaveBeenCalledWith("project", "/synthetic/project");
  });
  it("rejects old daemon status in the updated client with INVALID_REQUEST", async () => {
    const { client } = clientFixture(oldStatus);
    await expect(client.hostedLoginStatus("project")).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  });
  it("records unsupported old-client/new-daemon acceptance unchanged and symmetric GET requests", async () => {
    const projection = await daemonFixture(status).route();
    const old = clientFixture(projection.body), updated = clientFixture(projection.body);
    expect(await oldClientStatus(old.client, "project")).toEqual(status);
    expect(await updated.client.hostedLoginStatus("project")).toEqual(status);
    expect(old.request.mock.calls).toEqual(updated.request.mock.calls);
    expect(old.request.mock.calls[0]).toEqual(["/v2/projects/project/login/status", expect.objectContaining({ method: "GET", accept: "application/json", body: undefined, token: "synthetic-control-token" })]);
    expect(Object.keys(old.request.mock.calls[0]![1] as object).sort()).toEqual(["accept", "body", "method", "signal", "token"]);
  });
  it("keeps authorization rejection separate from status-version compatibility", async () => {
    const f = daemonFixture(status, false);
    expect(await f.route()).toMatchObject({ code: 403, body: { error: { code: "FORBIDDEN" } } });
    expect(f.loginStatus).not.toHaveBeenCalled(); expect(f.requireAuthorized).not.toHaveBeenCalled();
  });
  it.each(malformed.map((body, index) => ({ body, index })))("rejects unsafe internal daemon projection $index as INTERNAL_FAILURE", async ({ body }) => {
    expect(await daemonFixture(body).route()).toMatchObject({ code: 500, body: { error: { code: "INTERNAL_FAILURE" } } });
  });
  it("validates supervisor status on the existing login-status operation", async () => {
    const client = new SupervisorClient({ socketPath: "/synthetic/supervisor.sock", credential: { owner: "synthetic-owner", epoch: "synthetic-epoch", token: "a".repeat(64) } });
    const request = vi.spyOn(client as any, "request").mockResolvedValue(status);
    expect(await client.loginStatus()).toEqual(status); expect(request).toHaveBeenCalledWith("login-status");
    for (const body of malformed) { request.mockResolvedValue(body); await expect(client.loginStatus()).rejects.toMatchObject({ code: "INTERNAL_FAILURE" }); }
  });
});

describe("custody purpose configuration and admission before effects", () => {
  it("accepts only keyring with the exact unavailable binding", () => {
    expect(validateHostedManagedAuth(managedAuth)).toEqual(managedAuth);
    for (const value of [{ ...managedAuth, backend: "file" }, { ...managedAuth, backend: "auto" }, { ...managedAuth, token: "synthetic" }, { ...managedAuth, binding: { ...binding, state: "verified" } }, { ...managedAuth, binding: { ...binding, digest: "a".repeat(64) } }]) {
      expect(() => validateHostedManagedAuth(value)).toThrowError(expect.objectContaining({ code: "INVALID_REQUEST" }));
    }
  });
  it("refuses production login and every worker admission without touching filesystem or spawning", async () => {
    const identity = { canonicalRoot: "/synthetic/project", cwd: "/synthetic/project", accountId: "declared-continuity-only", accountEpoch: 1, policyDigest: "synthetic-policy" };
    const options = { canonicalRoot: identity.canonicalRoot, executablePath: "/synthetic/missing-supplier", codexHome: "/synthetic/private/home", privateDirectory: "/synthetic/private", providerNetworkConsent: { approvedBy: "fixture", approvalReference: "not-qualification" } };
    const login = new CodexLogin(options);
    const supervisor = new CodexSupervisor({ ...options, identity, model: "synthetic-model", managedAuth });
    try {
      await expect(login.startLogin()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      await expect(supervisor.verifyHostedBoundary(identity)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      await expect(supervisor.acquire("worker", JSON.stringify({ prompt: "must not launch" }))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      await expect(supervisor.startManager("manager", JSON.stringify({ prompt: "must not launch", canonicalRoot: identity.canonicalRoot, model: "synthetic-model" }))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      expect(await supervisor.inventory()).toEqual([]);
    } finally { await login.close(); await supervisor.close(); }
    for (const effect of [...fileEffects, core.privateDirectory, core.verifyExactSupply, core.revalidateExactSupply, core.assertContinuity]) expect(effect).not.toHaveBeenCalled();
    expect(childProcess.spawn).not.toHaveBeenCalled();
  });
  it("renders the trusted-login exception only for that purpose and keeps independent root homes", async () => {
    Object.defineProperty(process, "platform", { value: "darwin", configurable: true });
    vi.mocked(fs.stat).mockImplementation(async () => ({ isDirectory: () => true, isFile: () => true, mode: 0o700, uid: process.getuid?.() }) as any);
    vi.mocked(fs.realpath).mockImplementation(async path => String(path));
    vi.mocked(fs.mkdtemp).mockImplementation(async prefix => `${prefix}synthetic`);
    vi.mocked(fs.writeFile).mockResolvedValue(undefined);
    vi.mocked(fs.rm).mockResolvedValue(undefined);
    const options = { canonicalRoot: "/synthetic/project-a", privateDirectory: "/synthetic/private-a", codexHome: "/synthetic/private-a/home", providerNetworkConsent: { approvedBy: "fixture", approvalReference: "render-only" } };
    const worker = await prepareCodexContainment(options);
    const workerProfile = vi.mocked(fs.writeFile).mock.calls.at(-1)![1];
    expect(workerProfile).toContain('(deny mach-lookup (global-name "com.apple.securityd"))');
    expect(worker.config.cli_auth_credentials_store).toBe("file");
    expect(worker.environment.HOME).toBe(options.privateDirectory);
    expect(workerProfile).not.toContain("Keychains");
    expect(workerProfile).toContain('(deny file-write* (require-not (require-any (subpath "/synthetic/project-a") (subpath "/synthetic/private-a") (literal "/dev/null"))))');
    const login = await prepareCodexContainment({ ...options, purpose: "trusted-login" });
    const loginProfile = vi.mocked(fs.writeFile).mock.calls.at(-1)![1];
    expect(loginProfile).not.toContain('(deny mach-lookup (global-name "com.apple.securityd"))');
    expect(login.config.cli_auth_credentials_store).toBe("keyring");
    expect(login.environment.HOME).toBe(options.privateDirectory);
    // The keyring backend rewrites the login keychain database in-process, so the effective home's keychain directory is readable and writable.
    expect(loginProfile).toContain('(subpath "/Library/Keychains") (subpath "/synthetic/private-a/Library/Keychains")');
    expect(loginProfile).toContain('(deny file-write* (require-not (require-any (subpath "/synthetic/project-a") (subpath "/synthetic/private-a") (subpath "/synthetic/private-a/Library/Keychains") (literal "/dev/null"))))');
    vi.mocked(fs.lstat).mockImplementation(async () => ({ dev: 1n, ino: 2n, mode: 0o100600n, uid: BigInt(process.getuid!()), size: 1n, mtimeNs: 1n, ctimeNs: 1n, isDirectory: () => false, isFile: () => true, isSymbolicLink: () => false }) as any);
    vi.mocked(os.userInfo).mockReturnValue({ uid: process.getuid!(), gid: process.getgid!(), username: "fixture", homedir: "/synthetic/os-user-home", shell: "/bin/zsh" });
    const loginV2 = await prepareCodexContainmentV2({ ...options, purpose: "trusted-login", trustedRuntimeReadRoots: [] });
    expect(loginV2.environment).toEqual({ HOME: "/synthetic/os-user-home", CODEX_HOME: options.codexHome, TMPDIR: expect.stringContaining("/synthetic/private-a/containment-"), PATH: "/usr/bin:/bin:/usr/sbin:/sbin", LANG: "en_US.UTF-8" });
    const loginV2Profile = vi.mocked(fs.writeFile).mock.calls.at(-1)![1];
    expect(loginV2Profile).toContain('(subpath "/Library/Keychains") (subpath "/synthetic/os-user-home/Library/Keychains")');
    expect(loginV2Profile).toContain('(deny file-write* (require-not (require-any (subpath "/synthetic/project-a") (subpath "/synthetic/private-a") (subpath "/synthetic/os-user-home/Library/Keychains") (literal "/dev/null"))))');
    const supplierV2 = await prepareCodexTrustedSupplierContainmentV2({ ...options, trustedRuntimeReadRoots: [] });
    expect(supplierV2.config.cli_auth_credentials_store).toBe("keyring");
    expect(supplierV2.environment.HOME).toBe("/synthetic/os-user-home");
    expect(vi.mocked(fs.writeFile).mock.calls.at(-1)![1]).toContain('(subpath "/synthetic/os-user-home/Library/Keychains") (literal "/dev/null"))))');
    vi.mocked(os.userInfo).mockReturnValue({ uid: process.getuid!(), gid: process.getgid!(), username: "fixture", homedir: "/synthetic/other-os-user-home", shell: "/bin/zsh" });
    const otherLoginV2 = await prepareCodexContainmentV2({ ...options, purpose: "trusted-login", trustedRuntimeReadRoots: [] });
    expect(otherLoginV2.environment.HOME).toBe("/synthetic/other-os-user-home"); expect(otherLoginV2.outerPolicyDigest).not.toBe(loginV2.outerPolicyDigest);
    const rootB = await prepareCodexContainment({ ...options, purpose: "trusted-login", canonicalRoot: "/synthetic/project-b", privateDirectory: "/synthetic/private-b", codexHome: "/synthetic/private-b/home" });
    expect(rootB.environment.CODEX_HOME).not.toBe(login.environment.CODEX_HOME);
    await expect(prepareCodexNativePolicy({ ...options, purpose: "trusted-login", immutableReadRoots: [], protectedPaths: [] })).rejects.toThrow();
    vi.mocked(fs.stat).mockImplementation(async path => ({ isDirectory: () => true, isFile: () => false, mode: 0o700, uid: String(path) === "/usr" ? 0 : process.getuid?.() }) as any);
    vi.mocked(fs.lstat).mockImplementation(async () => ({ isDirectory: () => true, isFile: () => false, isSymbolicLink: () => false }) as any);
    const nativeOptions = { ...options, privateDirectory: "/synthetic/broker/worker", codexHome: "/synthetic/broker/worker/home", immutableReadRoots: ["/usr"], protectedPaths: ["/synthetic/broker"] };
    const native = await prepareCodexNativePolicy(nativeOptions);
    expect(native.configToml).toContain('cli_auth_credentials_store="keyring"');
    expect(native.expectedPermissions.filesystem[nativeOptions.privateDirectory]).toBe("deny");
    expect(native.expectedPermissions.filesystem["/synthetic/broker"]).toBe("deny");
    expect(native.enforcementEvidence).toBe("NOT_PROVEN_G_SBX");
    await native.cleanup(); await worker.cleanup(); await login.cleanup(); await loginV2.cleanup(); await otherLoginV2.cleanup(); await rootB.cleanup();
    expect(childProcess.spawn).not.toHaveBeenCalled(); expect(fs.open).not.toHaveBeenCalled(); expect(fs.readFile).not.toHaveBeenCalled();
  });
});
