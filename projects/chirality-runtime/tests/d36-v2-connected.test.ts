import { createHash } from "node:crypto";
import { PassThrough } from "node:stream";
import { mkdir, mkdtemp, readFile, readdir, realpath, rename, rm, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { ProjectRegistry, REQUIRED_RUNTIME_CONFORMANCE_LIMBS, runtimePolicyParameterSchemaDigestV2 } from "@chirality/runtime-core";
import { CodexLogin, validateCodexLoginStartup } from "../packages/daemon/src/codex-login.js";
import { CodexSupervisor } from "../packages/daemon/src/codex-supervisor.js";
import { HostedIdentityBindingStore } from "../packages/daemon/src/hosted-identity-binding.js";
import { createCodexCandidateLauncherFactory } from "../packages/daemon/src/codex-admitted-launcher.js";
import { createControlledHostedBootstrapPrivateBindingsForTests, productionLogout } from "../packages/daemon/src/hosted-private-composition.js";
import { AuthorityTranscript, AUTHORITY_CONTRACT, initializationProof } from "../packages/daemon/src/supplier-authority-controller.js";
import { hostAuthoritySubjectBindingDigestV2, revalidateRuntimeInstanceAdmissionV2 } from "../packages/daemon/src/runtime-conformance-v2-admission.js";
import { codexLoginConfigOverridesV2, prepareCodexContainmentV2, prepareCodexNativePolicyV2 } from "../packages/daemon/src/codex-containment.js";

// External trust and process I/O only. The production admission registries,
// compiler bodies, launcher comparisons, sessions and Supervisor run unchanged.
const io = vi.hoisted(() => ({ verified: undefined as any, spawn: undefined as any, releaseRead: undefined as any,
  children: new Map<number, boolean>(), catalog: undefined as any, trace: [] as string[], captures: [] as any[],
  invalidate: undefined as any, requestHook: undefined as any, retireFails: false, pendingLogin: false, catalogHangs: false,
  directoryRead: undefined as any, outerHook: undefined as any, compileHook: undefined as any }));
vi.mock("../packages/daemon/src/hosted-packaged-release-state.js", async original => ({
  ...await original<any>(), revalidateIssuedPackagedReleaseBasisV2: async () => { await io.releaseRead?.(); }
}));
vi.mock("node:crypto", async original => ({ ...await original<any>(), randomBytes: (size: number) => Buffer.alloc(size, 42) }));
vi.mock("node:fs/promises", async original => {
  const actual = await original<any>();
  return { ...actual, readdir: async (path: any, ...args: any[]) => { await io.directoryRead?.(path); return actual.readdir(path, ...args); }, stat: (path: any, ...args: any[]) => path === "/usr/bin/sandbox-exec"
    ? Promise.resolve({ isFile: () => true }) : actual.stat(path, ...args) };
});
vi.mock("@chirality/native-admission", async original => ({ ...await original<any>(), loadNativeAdmissionBinding: () => ({ state: "available", value: { spawnGroupedSupplier: (...args: any[]) => io.spawn(...args) } }) }));
vi.mock("@chirality/runtime-core", async original => {
  const actual = await original<any>();
  return { ...actual,
    verifyExactSupply: async ({ executablePath }: any) => ({ executablePath, sha256: io.verified.support.supplier.sha256, version: "1.2.3", identity: { size: 8n } }),
    revalidateExactSupply: async () => {}, verifyPackagedRuntimeBasisV2: async () => io.verified,
    DescendantTracker: class extends actual.DescendantTracker {
      constructor(options: any) { super({ ...options, census: async () => io.children.get(options.leaderPid)
        ? [{ pid: options.leaderPid, ppid: 1, pgid: options.leaderPid, uid: process.getuid!(), startIdentity: `test-${options.leaderPid}` }] : [] }); }
    }
  };
});
// Capture actual compiler output for individual drift regressions. No successful
// output is invented here; the production compiler still performs every read.
vi.mock("../packages/daemon/src/codex-containment.js", async original => {
  const actual = await original<any>();
  return { ...actual, prepareCodexTrustedSupplierContainmentV2: async (input: any) => { const result = await actual.prepareCodexTrustedSupplierContainmentV2(input); return io.outerHook ? io.outerHook(result) : result; }, prepareCodexNativePolicyV2: async (input: any) => {
    const result = await actual.prepareCodexNativePolicyV2(input);
    return io.compileHook ? io.compileHook(result) : result;
  } };
});
const hash = (value: string) => createHash("sha256").update(value).digest("hex");
const roles = ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"];
const principal = { accountUserId: "account-user", providerWorkspaceId: "workspace" };
const accountDigest = hash(JSON.stringify({ schema: "chirality-hosted-account-conformance/v1", ...principal }));
const account = { accountId: `rhb_${Buffer.alloc(32, 42).toString("base64url")}`, accountEpoch: 1, accountDigest };
const nominalHosts = new Map<object, () => Promise<boolean>>();
let root: string, bindings: any, supervisor: CodexSupervisor, login: CodexLogin, sourceOptions: any, issuedInputs: any[];
let live = true, manifestHash: string, manifestPath: string, projects: ProjectRegistry;
const platform = Object.getOwnPropertyDescriptor(process, "platform")!, arch = Object.getOwnPropertyDescriptor(process, "arch")!;
const weakGet = WeakMap.prototype.get, weakHas = WeakMap.prototype.has;

function supplierModel(model = "gpt-default", changes: any = {}) {
  return { id: model, model, upgrade: null, upgradeInfo: null, availabilityNux: null, displayName: "Catalog model", description: "Supplier metadata",
    modelSpecialty: null, hidden: false, supportedReasoningEfforts: [{ reasoningEffort: "high", description: "High" }], defaultReasoningEffort: "high",
    inputModalities: ["text", "image"], supportsPersonality: true, multiAgentVersion: null, additionalSpeedTiers: [], serviceTiers: [], defaultServiceTier: null, isDefault: true, ...changes };
}
function parseTomlValue(text: string) {
  let quoted = false, escaped = false, output = "";
  for (const c of text) { if (c === '"' && !escaped) quoted = !quoted; output += c === "=" && !quoted ? ":" : c; escaped = c === "\\" && !escaped; if (c !== "\\") escaped = false; }
  return JSON.parse(output);
}
function requestedConfig(args: string[]) {
  const config: any = {};
  for (let index = 4; index < args.length; index += 2) {
    expect(args[index]).toBe("-c"); const raw = args[index + 1], split = raw.indexOf("="), keys = raw.slice(0, split).split(".");
    let at = config; for (const key of keys.slice(0, -1)) at = at[key] ??= {};
    at[keys.at(-1)!] = parseTomlValue(raw.slice(split + 1));
  }
  return config;
}
function spawnSupplier(executable: string, args: string[], secret: Buffer, options: any) {
  const index = io.captures.length, config = requestedConfig(args), pid = 8000 + index;
  const capture = { executable, args: [...args], config, options, pid, methods: [] as string[] };
  io.captures.push(capture); io.children.set(pid, true);
  const stdin = new PassThrough(), stdout = new PassThrough(); let identity: any, input: any, inbound: AuthorityTranscript, outbound: AuthorityTranscript, reaped = false;
  const send = (value: any) => stdout.write(`${JSON.stringify(value)}\n`);
  let snapshot: any;
  stdin.on("data", chunk => { for (const raw of String(chunk).trim().split("\n")) {
    const r = JSON.parse(raw); if (r.method) { capture.methods.push(r.method); io.trace.push(r.method); io.requestHook?.(r.method, capture, r); }
    if (r.method === "initialize") {
      if (!r.params.chiralityAdmissionAuthority) { send({ id: r.id, result: {} }); continue; }
      input = { ...r.params.chiralityAdmissionAuthority, exactSupplyDigest: io.verified.support.supplier.sha256, authoritySecret: secret };
      identity = { runtimeProcessIncarnationId: input.runtimeProcessIncarnationId, supplierGeneration: input.supplierGeneration };
      const descriptor = { capability: "chirality.local-admission-authority", contract: AUTHORITY_CONTRACT, major: 1, minor: 0 };
      const v4Descriptor = { capability: "account.identity-snapshot", contract: "chirality-supplier-account-identity/1", major: 1, minor: 0, method: "account/identitySnapshot" };
      input = { ...input, descriptor, v4Descriptor };
      const response = { contract: AUTHORITY_CONTRACT, ...identity, supplierChallenge: Buffer.alloc(32, 11).toString("base64url"), descriptor, v4Descriptor, proof: "" };
      response.proof = initializationProof(secret, { ...input, ...response });
      inbound = new AuthorityTranscript(secret, identity, "runtime-to-supplier"); outbound = new AuthorityTranscript(secret, identity, "supplier-to-runtime");
      snapshot = { schema: "chirality-supplier-account-identity-response/1", state: "available", supplierGeneration: identity.supplierGeneration, identityGeneration: `identity-${index}`, ...principal };
      send({ id: r.id, result: { chiralityAdmissionAuthority: response } });
    } else if (r.method === "initialized") continue;
    else if (r.method === "account/login/start") {
      send({ id: r.id, result: { type: "chatgpt", loginId: "login", authUrl: "https://auth.openai.com/login" } });
      if (!io.pendingLogin) send({ method: "account/login/completed", params: { loginId: "login", success: true } });
    } else if (r.method === "account/login/cancel" || r.method === "account/logout") send({ id: r.id, result: {} });
    else if (r.method === "account/read") send({ id: r.id, result: { requiresOpenaiAuth: true, account: { type: "chatgpt", email: null, planType: "test" } } });
    else if (r.method === "model/list") { if (!io.catalogHangs) send({ id: r.id, result: io.catalog }); }
    else if (r.method === "account/identitySnapshot") { if ((capture as any).changedAccount) snapshot = { ...snapshot, accountUserId: "different" }; send({ id: r.id, result: snapshot }); }
    else if (r.method === "config/read") send({ id: r.id, result: { config } });
    else if (r.method === "thread/start") send({ id: r.id, result: { thread: { id: "thread" }, approvalsReviewer: "user", approvalPolicy: "never" } });
    else if (r.method === "turn/start") {
      (capture as any).turn = r.params;
      send({ id: r.id, result: { turn: { id: "turn", status: "inProgress" } } });
      send({ method: "turn/started", params: { threadId: "thread", turn: { id: "turn", status: "inProgress" } } });
      send({ method: "turn/completed", params: { threadId: "thread", turn: { id: "turn", status: "completed" } } });
    } else {
      const body: any = inbound!.accept(raw); io.trace.push(body.op); io.requestHook?.(body.op, capture, body);
      if (body.op === "chirality/admissionAcquire") {
        const common = { requestId: body.requestId, operationId: body.operationId, leaseId: `lease-${index}`, supplierGeneration: identity.supplierGeneration, identityGeneration: snapshot.identityGeneration, snapshotDigest: hash(JSON.stringify(snapshot)) };
        send(outbound!.encode({ kind: "result", op: body.op, state: "acquired", ...common })); send(outbound!.encode({ kind: "notification", op: "chirality/admissionAcquired", ...common }));
      } else {
        const released = body.op === "chirality/admissionRelease", common = { requestId: body.requestId, leaseId: body.leaseId, disposition: body.disposition };
        send(outbound!.encode({ kind: "result", op: body.op, state: released ? "released" : "aborted", ...common } as any));
        send(outbound!.encode({ kind: "notification", op: released ? "chirality/admissionReleased" : "chirality/admissionAborted", ...common } as any));
      }
    }
  } });
  return { state: "available", value: { pid, stdin, stdout,
    closeInput() { io.trace.push(`eof:${pid}`); }, observeLeader: async () => ({ exitCode: 0, signal: null }),
    terminate() { expect(reaped).toBe(false); io.trace.push(`term:${pid}`); }, kill() { expect(reaped).toBe(false); io.trace.push(`kill:${pid}`); },
    reapLeader: async () => { reaped = true; io.children.set(pid, false); io.trace.push(`reap:${pid}`); return { exitCode: 0, signal: null }; },
    groupRetired() { io.trace.push(`group:${pid}`); return !io.retireFails; }
  } };
}

function supportProfile() {
  const without = {
    schema: "chirality-runtime-support-profile/v2" as const, macosProductVersion: "26.6.2", macosBuildVersion: "25G83", architecture: "arm64" as const,
    electronVersion: "43.2.0", nodeVersion: "24.13.0", nodeModuleAbi: "145", napiVersion: "10",
    osMeasurement: { executablePath: "/usr/bin/sw_vers" as const, executableSha256: hash("sw"), executableSize: 2 },
    sandboxExec: { path: "/usr/bin/sandbox-exec" as const, sha256: hash("sandbox"), size: 7 },
    nativeAdmission: { contract: "chirality-native-admission/v1" as const, sha256: hash("native"), size: 6, napiVersion: "6" },
    supplier: { version: "1.2.3", sha256: hash("supplier"), size: 8, appServerProtocolDigest: hash("protocol"), authorityContract: "chirality.local-admission-authority/1.0" as const, identityContract: "chirality-supplier-account-identity/1" as const },
    compiler: { outerPolicySchema: "chirality-codex-outer-policy/v2" as const, nativePolicyIdentityVersion: 10 as const, sourceDigest: hash("compiler"), parameterSchemaDigest: runtimePolicyParameterSchemaDigestV2() },
    immutableSystemRoots: ["/System", "/usr"], kernelHelperContractDigest: hash("kernel")
  };
  return { ...without, profileDigest: hash(`${JSON.stringify(without)}\n`) };
}
async function releaseFiles(directory: string, purpose: "login" | "worker", support: any) {
  const limbNames = purpose === "login" ? ["exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "storage-isolation", "provider-network", "bounded-protocol-purpose", "retirement"] : REQUIRED_RUNTIME_CONFORMANCE_LIMBS;
  const record = { schema: `chirality-codex-${purpose}-purpose-release/v2`, evidenceClass: purpose === "login" ? "exact-account-free-login-purpose-observed" : "exact-worker-purpose-observed",
    sourceDigest: hash("source"), payloadDigest: hash("payload"), supportProfileDigests: [support.profileDigest], policyContractDigest: runtimePolicyParameterSchemaDigestV2(), supplyProfileDigest: hash(`${JSON.stringify(support.supplier)}\n`),
    issuedAt: "2026-09-01T00:00:00.000Z", expiresAt: "2026-10-01T00:00:00.000Z", limbs: Object.fromEntries(limbNames.map(name => [name, { attempted: true, passed: true, evidenceSha256: hash(name) }])),
    ...(purpose === "login" ? { backend: { credentialStore: "keyring", plaintextFallback: false }, methods: ["account/login/start", "account/login/cancel", "account/read", "model/list"], modelExecution: false } : {}) };
  const recordBytes = JSON.stringify(record), owner = "Controlled external owner act", gateIdentity = purpose === "login" ? "D36" : "G4";
  const acceptance = JSON.stringify({ schema: "chirality-runtime-conformance-acceptance/v1", status: "accepted", recordSha256: hash(recordBytes), sourceDigest: hash("source"), activationId: "test-release", gateIdentity, ownerActSha256: hash(owner), ownerReference: "controlled-owner", expiresAt: "2026-10-01T00:00:00.000Z" });
  const recordPath = join(directory, `${purpose}.json`), acceptancePath = join(directory, `${purpose}-acceptance.json`), ownerActPath = join(directory, `${purpose}-owner.md`);
  await Promise.all([writeFile(recordPath, recordBytes, { mode: 0o600 }), writeFile(acceptancePath, acceptance, { mode: 0o600 }), writeFile(ownerActPath, owner, { mode: 0o600 })]);
  return { recordPath, recordSha256: hash(recordBytes), acceptancePath, acceptanceSha256: hash(acceptance), ownerActPath, ownerActSha256: hash(owner), activationId: "test-release", gateIdentity };
}
beforeEach(async () => {
  io.children.clear(); io.trace = []; io.captures = []; io.releaseRead = undefined; io.requestHook = undefined; io.retireFails = false; io.pendingLogin = false; io.catalogHangs = false; io.compileHook = undefined; io.outerHook = undefined; io.directoryRead = undefined;
  live = true; issuedInputs = []; nominalHosts.clear(); bindings = undefined;
  Object.defineProperty(process, "platform", { ...platform, value: "darwin" }); Object.defineProperty(process, "arch", { ...arch, value: "arm64" });
  vi.spyOn(Date, "now").mockReturnValue(Date.parse("2026-09-10T12:00:00.000Z"));
  // The missing external HOST-P2 producer is represented only for these exact
  // test objects. Neither a production nor test issuer/registry is added.
  vi.spyOn(WeakMap.prototype, "get").mockImplementation(function (key: object) { return nominalHosts.has(key) ? nominalHosts.get(key) : weakGet.call(this, key); });
  vi.spyOn(WeakMap.prototype, "has").mockImplementation(function (key: object) { return nominalHosts.has(key) || weakHas.call(this, key); });
  const timer = globalThis.setTimeout;
  vi.spyOn(globalThis, "setTimeout").mockImplementation(((fn: any, ms: any, ...args: any[]) => timer(fn, ms === 1000 ? 0 : ms, ...args)) as any);
  const open = HostedIdentityBindingStore.open.bind(HostedIdentityBindingStore);
  vi.spyOn(HostedIdentityBindingStore, "open").mockImplementation(input => open({ ...input, randomHandle: () => Buffer.alloc(32, 42) }));
  root = await realpath(await mkdtemp(join(await realpath(tmpdir()), "d36-connected-")));
  const runtimeDirectory = join(root, "runtime"), project = join(root, "project"), privateDirectory = join(runtimeDirectory, "private"), codexHome = join(privateDirectory, "home"), resourcesRoot = join(root, "Resources"), instructionRoot = join(resourcesRoot, "instruction-root");
  for (const path of [runtimeDirectory, project, privateDirectory, codexHome, resourcesRoot, instructionRoot]) await mkdir(path, { recursive: true, mode: 0o700 });
  manifestPath = join(project, "chirality.project.json");
  const manifest = JSON.stringify({ schemaVersion: "chirality.project/v2", projectId: "project", displayName: "Connected", workingRoot: ".", instructionRoot: { mode: "runtime" }, defaultExecutionRoot: ".", profiles: { domain: [], capability: [], dataBoundary: [] }, enabledAdapterIds: ["codex-app-server"], embeddedUi: { declared: false } });
  await writeFile(manifestPath, manifest); manifestHash = hash(manifest);
  projects = new ProjectRegistry(runtimeDirectory, { CHIRALITY_INSTRUCTION_ROOT: instructionRoot }); await projects.register(manifestPath, { approvedBy: "test", approvalReference: "controlled" });
  const support = supportProfile();
  io.verified = { resourcesRoot, inventoryPath: join(resourcesRoot, "inventory.json"), payloadManifestPath: join(resourcesRoot, "payload.json"), inventorySha256: hash("inventory"), payloadDigest: hash("payload"), payload: { entries: [], supportProfiles: [support] }, support };
  const basis = { schema: "chirality-hosted-packaged-release-basis/v2", basisDigest: hash("basis"), verified: io.verified, supportProfile: support, instructionRoot, nativeAddonPath: join(resourcesRoot, "native.node"), supplierExecutablePath: join(resourcesRoot, "codex"),
    login: await releaseFiles(runtimeDirectory, "login", support), worker: await releaseFiles(runtimeDirectory, "worker", support) };
  sourceOptions = { runtimeDirectory, supplierExecutablePath: basis.supplierExecutablePath, nativeAddonPath: basis.nativeAddonPath, instructionRoot,
    compatibility: { compatibilityIdentity: "root-runtime-1", contractBasisSha256: hash("compatibility") }, commandNetworkPosture: "off", protectedPaths: [runtimeDirectory, join(runtimeDirectory, "release-authority"), join(runtimeDirectory, "release-basis")], immutableReadRoots: ["/usr"], releaseV2: { basis } };
  io.catalog = { data: [supplierModel()], nextCursor: null }; io.spawn = spawnSupplier;
  const lease = { held: true, close: vi.fn() };
  const nativeRoles = { digest: hash("roles"), configOverrides: ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2", ...roles.flatMap(role => [`agents.${role}.description=${JSON.stringify(role)}`, `agents.${role}.config_file=${JSON.stringify(join(privateDirectory, `${role}.toml`))}`])] };
  bindings = await createControlledHostedBootstrapPrivateBindingsForTests(sourceOptions, {
    revalidateReleaseBasis: async () => { await io.releaseRead?.(); }, acquireLease: async () => lease as any,
    stageSupplier: async (_source, directory) => { const path = join(directory, "codex"); await writeFile(path, "supplier", { mode: 0o700 }); return path; },
    prepareNativeRoles: async () => nativeRoles, bindRuntimeReadRoot: async () => { throw new Error("v1 path forbidden"); },
    validateLoginStartup: validateCodexLoginStartup, createLogin: options => { login = new CodexLogin({ ...options, timeoutMs: 600 }); issuedInputs.push(options.instanceV2); return { start: () => login.startLogin(), status: () => login.status(), resolveDefaultModel: () => login.resolveDefaultModel(), cancel: () => login.cancel(), close: () => login.close() }; },
    preparePolicy: async () => { throw new Error("v1 path forbidden"); }, createLauncherFactory: options => { issuedInputs.push(options.bindings.instanceInputV2); return createCodexCandidateLauncherFactory(options); },
    admitHosted: async options => { const result = await CodexSupervisor.admitHosted(options); supervisor = result.supervisor; return result; },
    logout: productionLogout, openBindingStore: HostedIdentityBindingStore.open,
    hostAuthority: async input => {
      const coordinate = input.purpose === "login" ? null : input.account ?? account;
      const authority = Object.freeze({ evidence: "accepted-host-account-authority", mechanismId: "test-external", daemonGeneration: "test-daemon", authorityGeneration: "test-authority", subjectBindingDigest: hostAuthoritySubjectBindingDigestV2({ ...input, account: coordinate }), liveLeaseDigest: hash("lease") });
      nominalHosts.set(authority, async () => live); return { authority: authority as any, account: coordinate };
    }
  });
});
afterEach(async () => {
  io.releaseRead = undefined; io.requestHook = undefined; io.directoryRead = undefined; io.retireFails = false;
  await bindings?.close().catch(() => {});
  vi.restoreAllMocks(); Object.defineProperty(process, "platform", platform); Object.defineProperty(process, "arch", arch);
  await rm(root, { recursive: true, force: true });
});
async function ceremony() {
  const result = await bindings.createCeremony({ projectId: "project", manifestHash, canonicalRoot: join(root, "project"), privateDirectory: join(root, "runtime", "private"), codexHome: join(root, "runtime", "private", "home"), providerNetworkConsent: { approvedBy: "owner", approvalReference: "act", approvedAt: "2026-09-10T12:00:00.000Z" } });
  await result.start(); return result;
}
async function admission() {
  const current = await ceremony();
  return bindings.establishAdmission({ projectId: "project", canonicalRoot: join(root, "project"), ceremony: current });
}
async function turn(id = "worker") { const handle = await supervisor.acquire(id, JSON.stringify({ prompt: "hello" })); return supervisor.wait(id, handle.generation); }
async function materialize(admitted: any) { return bindings.materializeAdmission({ projectId: "project", canonicalRoot: join(root, "project"), admission: admitted,
  runtime: { projects, sessions: {}, nativePlanSink: {}, attachmentStagingRoot: join(root, "project", ".chirality", "attachments") } }); }
async function signOut() { return bindings.signOut({ projectId: "project", canonicalRoot: join(root, "project"), privateDirectory: join(root, "runtime", "private"), codexHome: join(root, "runtime", "private", "home") }); }
async function bindingRecord() { const dir = join(root, "runtime", "private"); const name = (await readdir(dir)).find(name => name.includes("identity") && name.endsWith(".json"))!; return JSON.parse(await readFile(join(dir, name), "utf8")); }

describe("controlled connected D36 v2 source path", () => {
  it("runs real login, Supplier-shaped catalog, retained worker turn and fence-first logout with actual compiled argv", async () => {
    const admitted = await admission();
    await materialize(admitted);
    expect(await turn()).toMatchObject({ exitCode: 0 });
    const establish = vi.spyOn(HostedIdentityBindingStore.prototype, "establishLive");
    await signOut(); expect(establish).not.toHaveBeenCalled();
    expect(await bindingRecord()).toMatchObject({ state: "fenced", accountEpoch: 2 });
    expect(io.captures).toHaveLength(3);
    const [loginSpawn, worker, logout] = io.captures;
    expect(loginSpawn.config).toMatchObject({ features: { shell_snapshot: false, plugins: false }, web_search: "disabled", allow_login_shell: false, cli_auth_credentials_store: "keyring" });
    for (const capture of io.captures) {
      expect(capture.executable).toBe("/usr/bin/sandbox-exec"); expect(capture.args.slice(0, 4)).toEqual(["-f", join(capture.options.environment.TMPDIR, "launch.sb"), join(root, "runtime", "private", "codex"), "app-server"]);
      expect(io.trace.indexOf(`kill:${capture.pid}`)).toBeLessThan(io.trace.indexOf(`reap:${capture.pid}`));
    }
    expect(worker.config).toEqual(logout.config); expect(worker.options.environment.TMPDIR).not.toBe(logout.options.environment.TMPDIR);
    expect(worker.methods).toContain("turn/start"); expect(worker.turn).toMatchObject({ model: "gpt-default", collaborationMode: { settings: { model: "gpt-default", reasoning_effort: "high" } } }); expect(logout.methods).toContain("account/logout"); expect(logout.methods).not.toContain("thread/start"); expect(logout.methods).not.toContain("turn/start");
    expect(issuedInputs.at(-1).account.accountEpoch).toBe(2);
  });
  it("rejects liveness invalidated during final release reads before login effect", async () => {
    io.requestHook = method => { if (method === "initialize") io.releaseRead = async () => { live = false; }; };
    await expect(ceremony()).rejects.toThrow(); expect(io.trace).not.toContain("account/login/start"); expect(io.trace.some(value => value.startsWith("reap:"))).toBe(true);
  });
  it("rejects liveness invalidated during catalog reads and retires the retained actor", async () => {
    await ceremony(); await login.status(); io.releaseRead = async () => { live = false; };
    await expect(login.resolveDefaultModel()).rejects.toThrow(); expect(io.trace).not.toContain("model/list"); expect(io.trace.some(value => value.startsWith("reap:"))).toBe(true);
  });
  it.each(["hidden", "reasoning", "duplicate", "no-default"])("retires actual v2 catalog actor on %s failure", async mode => {
    await ceremony(); await login.status();
    io.catalog = { data: mode === "duplicate" ? [supplierModel(), supplierModel()] : [supplierModel("gpt-default", mode === "hidden" ? { hidden: true } : mode === "reasoning" ? { defaultReasoningEffort: "low" } : { isDefault: false })], nextCursor: null };
    await expect(login.resolveDefaultModel()).rejects.toThrow(); expect(io.trace.some(value => value.startsWith("reap:"))).toBe(true);
  });
  it("does not cache catalog success when retirement is unproven, retaining and reporting its allocation", async () => {
    await ceremony(); await login.status(); io.retireFails = true;
    await expect(login.resolveDefaultModel()).rejects.toThrow("retirement");
    expect(await readdir(io.captures[0].options.environment.TMPDIR)).toContain("launch.sb");
    await expect(login.resolveDefaultModel()).rejects.toThrow("unavailable");
  });
  it("keeps the retained catalog bounded through timeout and cancellation", async () => {
    await ceremony(); await login.status(); io.catalogHangs = true;
    const result = login.resolveDefaultModel(); await expect(result).rejects.toThrow();
    expect(io.trace.some(value => value.startsWith("reap:"))).toBe(true);
  });
  it("retires a pending actual v2 login on cancel", async () => {
    io.pendingLogin = true; await ceremony(); await login.cancel();
    expect(io.trace).toContain("account/login/cancel"); expect(io.trace.some(value => value.startsWith("reap:"))).toBe(true);
  });
  it.each(["args", "config", "policy", "digest"])("rejects fresh compiler %s drift before worker spawn", async mode => {
    const current = await ceremony(); let compiles = 0;
    io.compileHook = (compiled: any) => { if (++compiles === 1) return compiled;
      if (mode === "args") return { ...compiled, args: [...compiled.args, "--drift"] };
      if (mode === "config") return { ...compiled, configOverrides: [...compiled.configOverrides, "features.plugins=true"] };
      if (mode === "policy") return { ...compiled, policyInstance: { ...compiled.policyInstance, commandNetworkPosture: "on" } };
      return { ...compiled, policyDigest: hash("different") };
    };
    await expect(bindings.establishAdmission({ projectId: "project", canonicalRoot: join(root, "project"), ceremony: current })).rejects.toThrow();
    expect(io.captures).toHaveLength(1);
  });
  it("rejects retained same-actor account change after acquire before model effects", async () => {
    await admission(); io.requestHook = (method, capture) => { if (method === "account/identitySnapshot") capture.changedAccount = true; };
    await expect(turn()).rejects.toThrow("account identity changed after acquire"); expect(io.trace).not.toContain("thread/start"); expect(io.trace).not.toContain("turn/start");
  });
  it("keeps logout fenced when current authority dies during final release reads", async () => {
    await admission();
    io.requestHook = (method, capture) => { if (capture === io.captures.at(-1) && io.captures.length === 3 && method === "config/read") io.releaseRead = async () => { live = false; }; };
    await expect(signOut()).rejects.toThrow(); expect(await bindingRecord()).toMatchObject({ state: "fenced", accountEpoch: 2 }); expect(io.trace).not.toContain("account/logout");
  });
  it("rejects manifest drift introduced during retirement reconciliation before materialization publication", async () => {
    const admitted = await admission();
    io.directoryRead = async (path: string) => { if (path.endsWith("/retirements")) { io.directoryRead = undefined; await writeFile(manifestPath, `${await readFile(manifestPath, "utf8")} `); } };
    await expect(materialize(admitted)).rejects.toMatchObject({ code: "PROJECT_MANIFEST_DRIFT" });
    expect(io.trace).not.toContain("thread/start");
  });
  it.each(["thread", "turn"])("rejects authority invalidation during the final internal config/read before %s", async phase => {
    await admission(); let threadStarted = false;
    io.requestHook = (method: string) => { if (method === "thread/start") threadStarted = true;
      if (method === "config/read" && (phase === "thread" || threadStarted)) io.releaseRead = async () => { live = false; }; };
    await expect(turn()).rejects.toThrow();
    expect(io.trace).not.toContain(phase === "thread" ? "thread/start" : "turn/start");
  });
  it("rejects fresh same-actor principal mismatch before any fresh model effect", async () => {
    await admission(); expect(await turn()).toMatchObject({ exitCode: 0 });
    io.requestHook = (method: string, capture: any) => { if (io.captures.length === 3 && method === "initialize") capture.changedAccount = true; };
    await expect(turn("fresh")).rejects.toThrow();
    expect(io.captures[2].methods).not.toContain("thread/start"); expect(io.captures[2].methods).not.toContain("turn/start");
  });
  it("rejects authority lost during candidate preparation before grouped spawn", async () => {
    const current = await ceremony(); let count = 0;
    io.compileHook = (compiled: any) => { if (++count === 2) io.releaseRead = async () => { live = false; }; return compiled; };
    await expect(bindings.establishAdmission({ projectId: "project", canonicalRoot: join(root, "project"), ceremony: current })).rejects.toThrow();
    expect(io.captures).toHaveLength(1);
  });
  it("rejects a same-mode native scratch replacement during the last release read", async () => {
    const current = await ceremony(); let count = 0;
    io.compileHook = (compiled: any) => { if (++count === 2) io.releaseRead = async () => { io.releaseRead = undefined; await rename(compiled.scratchDirectory, `${compiled.scratchDirectory}-old`); await mkdir(compiled.scratchDirectory, { mode: 0o700 }); }; return compiled; };
    await expect(bindings.establishAdmission({ projectId: "project", canonicalRoot: join(root, "project"), ceremony: current })).rejects.toThrow(); expect(io.captures).toHaveLength(1);
  });
  it.each(["digest", "profile", "argv"])("rejects outer compiler %s drift before candidate spawn", async mode => {
    const current = await ceremony(); let count = 0;
    io.outerHook = (outer: any) => { if (++count === 1) return outer;
      if (mode === "digest") return { ...outer, outerPolicyDigest: hash("wrong-outer") };
      if (mode === "profile") return { ...outer, sandboxProfilePath: join(root, "runtime", "wrong-profile") };
      return { ...outer, launchArguments: async (path: string) => [...await outer.launchArguments(path), "--wrong"] };
    };
    await expect(bindings.establishAdmission({ projectId: "project", canonicalRoot: join(root, "project"), ceremony: current })).rejects.toThrow(); expect(io.captures).toHaveLength(1);
  });
  it("retains worker allocations and reports retirement failure while logout stays fenced", async () => {
    await admission(); io.retireFails = true;
    await expect(signOut()).rejects.toThrow("retirement"); expect(await bindingRecord()).toMatchObject({ state: "fenced", accountEpoch: 2 });
    expect(await readdir(io.captures[1].options.environment.TMPDIR)).toContain("launch.sb"); expect(io.trace).not.toContain("account/logout");
  });

  it("rejects a same-byte outer profile replacement during the last release read", async () => {
    const current = await ceremony(); let count = 0;
    io.outerHook = (outer: any) => { if (++count === 2) io.releaseRead = async () => { io.releaseRead = undefined; const bytes = await readFile(outer.sandboxProfilePath); await rename(outer.sandboxProfilePath, `${outer.sandboxProfilePath}.old`); await writeFile(outer.sandboxProfilePath, bytes, { mode: 0o600 }); }; return outer; };
    await expect(bindings.establishAdmission({ projectId: "project", canonicalRoot: join(root, "project"), ceremony: current })).rejects.toThrow(); expect(io.captures).toHaveLength(1);
  });

});
