import { createHash } from "node:crypto";
import { PassThrough } from "node:stream";
import { cp, mkdir, mkdtemp, readFile, readdir, realpath, rename, rm, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { tmpdir } from "node:os";
import { afterAll, afterEach, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import { AuthRegistry, HostedConsentStore, ProjectRegistry, recordKey, REQUIRED_RUNTIME_CONFORMANCE_LIMBS, runtimePolicyParameterSchemaDigestV2, runtimeStageCPolicyParameterSchemaDigest } from "@chirality/runtime-core";
import { CodexLogin, validateCodexLoginStartup } from "../packages/daemon/src/codex-login.js";
import { CodexSupervisor } from "../packages/daemon/src/codex-supervisor.js";
import { HostedIdentityBindingStore } from "../packages/daemon/src/hosted-identity-binding.js";
import { createCodexCandidateLauncherFactory } from "../packages/daemon/src/codex-admitted-launcher.js";
import { createControlledHostedBootstrapPrivateBindingsForTests, productionLogout } from "../packages/daemon/src/hosted-private-composition.js";
import { AuthorityTranscript, AUTHORITY_CONTRACT, initializationProof } from "../packages/daemon/src/supplier-authority-controller.js";
import { hostAuthoritySubjectBindingDigestV2, revalidateRuntimeInstanceAdmissionV2 } from "../packages/daemon/src/runtime-conformance-v2-admission.js";
import { codexLoginConfigOverridesV2, prepareCodexContainmentV2, prepareCodexNativePolicyV2 } from "../packages/daemon/src/codex-containment.js";
import { digestCodexNativeToolDefinitionsV1 } from "../packages/daemon/src/codex-native-tools.js";
import { HostAccountAuthority } from "../packages/daemon/src/host-account-authority.js";
import { createHostAccountCeremonyProof } from "../packages/daemon/src/host-account-protocol.js";
import { RuntimeClient } from "../packages/client/src/client.js";
import { startControlledHostedBootstrapRuntimeHostForTests } from "../packages/daemon/src/hosted-bootstrap.js";
import { resolveHostedProjectTokenFile } from "../packages/daemon/src/hosted-paths.js";

// External trust and process I/O only. The production admission registries,
// compiler bodies, launcher comparisons, sessions and Supervisor run unchanged.
const io = vi.hoisted(() => ({ verified: undefined as any, spawn: undefined as any, releaseRead: undefined as any,
  children: new Map<number, boolean>(), catalog: undefined as any, trace: [] as string[], captures: [] as any[],
  invalidate: undefined as any, requestHook: undefined as any, retireFails: false, pendingLogin: false, catalogHangs: false,
  directoryRead: undefined as any, outerHook: undefined as any, compileHook: undefined as any,
  nativeReadback: new Map<number,"disabled"|"missing"|"upstream">(), stageCChild: false,
  uniqueRandom: false, randomSequence: 0, trialPlan: false, planAnswerObserved: false }));
vi.mock("../packages/daemon/src/hosted-packaged-release-state.js", async original => ({
  ...await original<any>(), revalidateIssuedPackagedReleaseBasisV2: async () => { await io.releaseRead?.(); }
}));
vi.mock("node:crypto", async original => ({ ...await original<any>(), randomBytes: (size: number) => Buffer.alloc(size, io.uniqueRandom ? ++io.randomSequence : 42) }));
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
let root: string, bindings: any, supervisor: CodexSupervisor, login: CodexLogin, sourceOptions: any, issuedInputs: any[], compositionAdapters: any, launcherBindings: any[];
let live = true, manifestHash: string, manifestPath: string, projects: ProjectRegistry, fixtureCompilerIdentity:10|11=10;
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
  // Login argv carries the outer wrapper ("-f", profile, executable) before "app-server"; the direct worker argv starts at "app-server".
  const start = args.indexOf("app-server"); expect(start).toBeGreaterThanOrEqual(0);
  const nativeSkills = args[start + 1] === "--chirality-disable-native-skills" ? "disabled" : undefined;
  for (let index = nativeSkills ? start + 2 : start + 1; index < args.length; index += 2) {
    expect(args[index]).toBe("-c"); const raw = args[index + 1], split = raw.indexOf("="), keys = raw.slice(0, split).split(".");
    let at = config; for (const key of keys.slice(0, -1)) at = at[key] ??= {};
    at[keys.at(-1)!] = parseTomlValue(raw.slice(split + 1));
  }
  return { config, nativeSkills };
}
function spawnSupplier(executable: string, args: string[], secret: Buffer, options: any) {
  const index = io.captures.length, requested = requestedConfig(args), config = requested.config, pid = 8000 + index;
  const capture = { executable, args: [...args], config, options, pid, methods: [] as string[], events: [] as string[], readbacks: [] as any[] };
  io.captures.push(capture); io.children.set(pid, true);
  const stdin = new PassThrough(), stdout = new PassThrough(); let identity: any, input: any, inbound: AuthorityTranscript, outbound: AuthorityTranscript, reaped = false, privateInitialized = false;
  const send = (value: any) => stdout.write(`${JSON.stringify(value)}\n`);
  let snapshot: any;
  stdin.on("data", chunk => { for (const raw of String(chunk).trim().split("\n")) {
    const r = JSON.parse(raw); if (r.method) { capture.methods.push(r.method); capture.events.push(r.method); io.trace.push(r.method); io.requestHook?.(r.method, capture, r); }
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
    } else if (r.method === "initialized") { privateInitialized = Boolean(input); continue; }
    else if (r.method === "account/login/start") {
      send({ id: r.id, result: { type: "chatgpt", loginId: "login", authUrl: "https://auth.openai.com/login" } });
      if (!io.pendingLogin) send({ method: "account/login/completed", params: { loginId: "login", success: true } });
    } else if (r.method === "account/login/cancel" || r.method === "account/logout") send({ id: r.id, result: {} });
    else if (r.method === "account/read") send({ id: r.id, result: { requiresOpenaiAuth: true, account: { type: "chatgpt", email: null, planType: "test" } } });
    else if (r.method === "model/list") { if (!io.catalogHangs) send({ id: r.id, result: io.catalog }); }
    else if (r.method === "account/identitySnapshot") { if ((capture as any).changedAccount) snapshot = { ...snapshot, accountUserId: "different" }; send({ id: r.id, result: snapshot }); }
    else if (r.method === "config/read") {
      const readback=io.nativeReadback.get(index)??"disabled",effective={...config};
      if(requested.nativeSkills){expect(privateInitialized).toBe(true);if(readback!=="missing")effective.chirality_runtime={nativeSkills:readback};}
      capture.readbacks.push(structuredClone(effective));
      send({ id: r.id, result: { config: effective } });
    }
    else if (r.method === "thread/start") { (capture as any).rootCarrier = r.params.chiralityRuntime; send({ id: r.id, result: { thread: { id: "thread" }, approvalsReviewer: "user", approvalPolicy: "never" } }); }
    else if (r.method === "turn/start") {
      (capture as any).turn = r.params;
      send({ id: r.id, result: { turn: { id: "turn", status: "inProgress" } } });
      send({ method: "turn/started", params: { threadId: "thread", turn: { id: "turn", status: "inProgress" } } });
      if (io.trialPlan) {
        send({ method: "turn/plan/updated", params: { threadId: "thread", turnId: "turn", plan: [{ step: "controlled draft" }] } });
        send({ method: "item/completed", params: { threadId: "thread", turnId: "turn", item: { id: "plan", type: "plan", text: "accepted trial plan" } } });
        send({ id: "trial-question", method: "item/tool/requestUserInput", params: { threadId: "thread", turnId: "turn", itemId: "question", questions: [{ id: "scope", header: "Scope", question: "Continue?", options: [{ label: "Yes", description: "Continue" }], isOther: true, isSecret: false }], isBlocking: true, autoResolutionMs: null } });
      } else if (io.stageCChild) {
        const inherited = (capture as any).rootCarrier.inheritableTools;
        send({ method: "chirality/nativeChild/turnStarted", params: { schema: "chirality-native-child-association/v1", supplierGeneration: identity.supplierGeneration, associationId: "a".repeat(32), parentThreadId: "thread", parentTurnId: "turn", childThreadId: "child-thread", childTurnId: "child-turn", selectedRole: { kind: "configured", name: "HELP_HUMAN", basisDigest: hash("Exact HELP_HUMAN child instruction.") }, inheritedToolsDigest: digestCodexNativeToolDefinitionsV1(inherited) } });
        send({ id: "child-tool", method: "item/tool/call", params: { threadId: "child-thread", turnId: "child-turn", callId: "child-call", tool: "chirality_list_methods", arguments: {}, chiralityRuntime: { schema: "chirality-native-child-call/v1", associationId: "a".repeat(32) } } });
      } else send({ method: "turn/completed", params: { threadId: "thread", turn: { id: "turn", status: "completed" } } });
    } else if (r.id === "trial-question" && r.result) {
      io.planAnswerObserved = true;
      send({ method: "serverRequest/resolved", params: { threadId: "thread", requestId: "trial-question" } });
      send({ method: "turn/completed", params: { threadId: "thread", turn: { id: "turn", status: "completed" } } });
    } else if (r.id === "child-tool" && r.result) {
      send({ method: "chirality/nativeChild/turnFinished", params: { schema: "chirality-native-child-terminal/v1", supplierGeneration: identity.supplierGeneration, associationId: "a".repeat(32), childThreadId: "child-thread", childTurnId: "child-turn", reason: "completed" } });
      send({ method: "turn/completed", params: { threadId: "thread", turn: { id: "turn", status: "completed" } } });
      send({ method: "chirality/nativeChild/familySettled", params: { schema: "chirality-native-family-settled/v1", supplierGeneration: identity.supplierGeneration, rootThreadId: "thread", rootTurnId: "turn" } });
    } else {
      const body: any = inbound!.accept(raw); capture.events.push(body.op); io.trace.push(body.op); io.requestHook?.(body.op, capture, body);
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

function supportProfile(nativePolicyIdentityVersion:10|11=10) {
  const without = {
    schema: "chirality-runtime-support-profile/v2" as const, macosProductVersion: "26.6.2", macosBuildVersion: "25G83", architecture: "arm64" as const,
    electronVersion: "43.2.0", nodeVersion: "24.13.0", nodeModuleAbi: "145", napiVersion: "10",
    osMeasurement: { executablePath: "/usr/bin/sw_vers" as const, executableSha256: hash("sw"), executableSize: 2 },
    sandboxExec: { path: "/usr/bin/sandbox-exec" as const, sha256: hash("sandbox"), size: 7 },
    nativeAdmission: { contract: "chirality-native-admission/v1" as const, sha256: hash("native"), size: 6, napiVersion: "6" },
    supplier: { version: "1.2.3", sha256: hash("supplier"), size: 8, appServerProtocolDigest: hash("protocol"), authorityContract: "chirality.local-admission-authority/1.0" as const, identityContract: "chirality-supplier-account-identity/1" as const },
    compiler: { outerPolicySchema: "chirality-codex-outer-policy/v2" as const, nativePolicyIdentityVersion, sourceDigest: hash("compiler"), parameterSchemaDigest: nativePolicyIdentityVersion===11?runtimeStageCPolicyParameterSchemaDigest():runtimePolicyParameterSchemaDigestV2() },
    immutableSystemRoots: ["/System", "/usr"], kernelHelperContractDigest: hash("kernel")
  };
  return { ...without, profileDigest: hash(`${JSON.stringify(without)}\n`) };
}
async function releaseFiles(directory: string, purpose: "login" | "worker", support: any) {
  const limbNames = purpose === "login" ? ["exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "storage-isolation", "provider-network", "bounded-protocol-purpose", "retirement"] : REQUIRED_RUNTIME_CONFORMANCE_LIMBS;
  const record = { schema: `chirality-codex-${purpose}-purpose-release/v2`, evidenceClass: purpose === "login" ? "exact-account-free-login-purpose-observed" : "exact-worker-purpose-observed",
    sourceDigest: hash("source"), payloadDigest: hash("payload"), supportProfileDigests: [support.profileDigest], policyContractDigest: support.compiler.parameterSchemaDigest, supplyProfileDigest: hash(`${JSON.stringify(support.supplier)}\n`),
    issuedAt: "2026-09-01T00:00:00.000Z", expiresAt: "2026-10-01T00:00:00.000Z", limbs: Object.fromEntries(limbNames.map(name => [name, { attempted: true, passed: true, evidenceSha256: hash(name) }])),
    ...(purpose === "login" ? { backend: { credentialStore: "keyring", plaintextFallback: false }, methods: ["account/login/start", "account/login/cancel", "account/read", "model/list"], modelExecution: false } : {}) };
  const recordBytes = JSON.stringify(record), owner = "Controlled external owner act", gateIdentity = purpose === "login" ? "D36" : "G4";
  const acceptance = JSON.stringify({ schema: "chirality-runtime-conformance-acceptance/v1", status: "accepted", recordSha256: hash(recordBytes), sourceDigest: hash("source"), activationId: "test-release", gateIdentity, ownerActSha256: hash(owner), ownerReference: "controlled-owner", expiresAt: "2026-10-01T00:00:00.000Z" });
  const recordPath = join(directory, `${purpose}.json`), acceptancePath = join(directory, `${purpose}-acceptance.json`), ownerActPath = join(directory, `${purpose}-owner.md`);
  await Promise.all([writeFile(recordPath, recordBytes, { mode: 0o600 }), writeFile(acceptancePath, acceptance, { mode: 0o600 }), writeFile(ownerActPath, owner, { mode: 0o600 })]);
  return { recordPath, recordSha256: hash(recordBytes), acceptancePath, acceptanceSha256: hash(acceptance), ownerActPath, ownerActSha256: hash(owner), activationId: "test-release", gateIdentity };
}
beforeEach(async ({ task }) => {
  io.children.clear(); io.trace = []; io.captures = []; io.releaseRead = undefined; io.requestHook = undefined; io.retireFails = false; io.pendingLogin = false; io.catalogHangs = false; io.compileHook = undefined; io.outerHook = undefined; io.directoryRead = undefined;
  io.nativeReadback.clear(); io.stageCChild = false; io.uniqueRandom = false; io.randomSequence = 0; io.trialPlan = false; io.planAnswerObserved = false;
  live = true; issuedInputs = []; launcherBindings = []; nominalHosts.clear(); bindings = undefined;
  Object.defineProperty(process, "platform", { ...platform, value: "darwin" }); Object.defineProperty(process, "arch", { ...arch, value: "arm64" });
  vi.spyOn(Date, "now").mockReturnValue(Date.parse("2026-09-10T12:00:00.000Z"));
  // Legacy controlled-adapter cases below retain their preexisting nominal
  // host objects. The concrete P2 case bypasses this set and uses the private
  // production issuer backed by a live HostAccountAuthority.
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
  const support = supportProfile(task.name.includes("concrete P2 lease") ? 11 : fixtureCompilerIdentity);
  io.verified = { resourcesRoot, inventoryPath: join(resourcesRoot, "inventory.json"), payloadManifestPath: join(resourcesRoot, "payload.json"), inventorySha256: hash("inventory"), payloadDigest: hash("payload"), payload: { entries: [], supportProfiles: [support] }, support };
  const basis = { schema: "chirality-hosted-packaged-release-basis/v2", basisDigest: hash("basis"), verified: io.verified, supportProfile: support, instructionRoot, nativeAddonPath: join(resourcesRoot, "native.node"), supplierExecutablePath: join(resourcesRoot, "codex"),
    login: await releaseFiles(runtimeDirectory, "login", support), worker: await releaseFiles(runtimeDirectory, "worker", support) };
  sourceOptions = { runtimeDirectory, supplierExecutablePath: basis.supplierExecutablePath, nativeAddonPath: basis.nativeAddonPath, instructionRoot,
    compatibility: { compatibilityIdentity: "root-runtime-1", contractBasisSha256: hash("compatibility") }, commandNetworkPosture: "off", protectedPaths: [runtimeDirectory, join(runtimeDirectory, "release-authority"), join(runtimeDirectory, "release-basis")], immutableReadRoots: ["/usr"], releaseV2: { basis } };
  io.catalog = { data: [supplierModel()], nextCursor: null }; io.spawn = spawnSupplier;
  const lease = { held: true, close: vi.fn() };
  const nativeRoles = { digest: hash("roles"), configOverrides: ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2", ...roles.flatMap(role => [`agents.${role}.description=${JSON.stringify(role)}`, `agents.${role}.config_file=${JSON.stringify(join(privateDirectory, `${role}.toml`))}`])] };
  compositionAdapters = {
    revalidateReleaseBasis: async () => { await io.releaseRead?.(); }, acquireLease: async () => lease as any,
    stageSupplier: async (_source, directory) => { const path = join(directory, "codex"); await writeFile(path, "supplier", { mode: 0o700 }); return path; },
    prepareNativeRoles: async () => {
      for (const role of roles) await writeFile(join(privateDirectory, `${role}.toml`), `developer_instructions = ${JSON.stringify(`Exact ${role} child instruction.`)}\n`, { mode: 0o600 });
      return nativeRoles;
    }, bindRuntimeReadRoot: async () => { throw new Error("v1 path forbidden"); },
    validateLoginStartup: validateCodexLoginStartup, createLogin: options => { login = new CodexLogin({ ...options, timeoutMs: 600 }); issuedInputs.push(options.instanceV2); return { start: () => login.startLogin(), status: () => login.status(), resolveDefaultModel: () => login.resolveDefaultModel(), resolveModelCatalog: () => login.resolveModelCatalog(), cancel: () => login.cancel(), close: () => login.close() }; },
    preparePolicy: async () => { throw new Error("v1 path forbidden"); }, createLauncherFactory: options => { issuedInputs.push(options.bindings.instanceInputV2); launcherBindings.push(options.bindings); return createCodexCandidateLauncherFactory(options); },
    admitHosted: async options => { const result = await CodexSupervisor.admitHosted(options); supervisor = result.supervisor; return result; },
    logout: productionLogout, openBindingStore: HostedIdentityBindingStore.open,
    hostAuthority: async input => {
      const coordinate = input.purpose === "login" ? null : input.account ?? account;
      const authority = Object.freeze({ evidence: "accepted-host-account-authority", mechanismId: "test-external", daemonGeneration: "test-daemon", authorityGeneration: "test-authority", subjectBindingDigest: hostAuthoritySubjectBindingDigestV2({ ...input, account: coordinate }), liveLeaseDigest: hash("lease") });
      nominalHosts.set(authority, async () => live); return { authority: authority as any, account: coordinate };
    }
  };
  bindings = await createControlledHostedBootstrapPrivateBindingsForTests(sourceOptions, compositionAdapters);
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
    const materialized = await materialize(admitted);
    // The retained catalog is the same non-hidden model/list read that picked the admitted default, and the
    // v2 configDigest recipe is unchanged by it (regression guard: no catalog term, same key set and values).
    expect(materialized.catalog).toEqual({ models: [{ model: "gpt-default", isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["high"] }], default: { model: "gpt-default", isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["high"] } });
    const readRoot = launcherBindings[0].trustedRuntimeReadRoots[0];
    expect(launcherBindings[0].configDigest).toBe(recordKey({ schema: "chirality.hosted-private-config/v2", projectId: "project", manifestHash, model: "gpt-default", defaultReasoningEffort: "high",
      accountStorage: { backend: "keyring" }, compatibility: sourceOptions.compatibility, providerNetworkConsent: { approvedBy: "owner", approvalReference: "act", approvedAt: "2026-09-10T12:00:00.000Z" },
      commandNetworkPosture: "off", protectedPaths: sourceOptions.protectedPaths, immutableReadRoots: ["/usr"], instructionRoot: sourceOptions.instructionRoot, nativeRoleConfigurationDigest: hash("roles"),
      trustedRuntimeReadRoot: { contentDigest: readRoot.contentDigest, readPaths: readRoot.readPaths }, releaseV2: { basisDigest: hash("basis") }, consentVersion: issuedInputs[0].consent.version }));
    expect(await turn()).toMatchObject({ exitCode: 0 });
    const establish = vi.spyOn(HostedIdentityBindingStore.prototype, "establishLive");
    await signOut(); expect(establish).not.toHaveBeenCalled();
    expect(await bindingRecord()).toMatchObject({ state: "fenced", accountEpoch: 2 });
    expect(io.captures).toHaveLength(3);
    const [loginSpawn, worker, logout] = io.captures;
    expect(loginSpawn.config).toMatchObject({ features: { shell_snapshot: false, plugins: false }, web_search: "disabled", allow_login_shell: false, cli_auth_credentials_store: "keyring" });
    // Login keeps the outer Seatbelt profile; the worker and logout suppliers launch directly so their own native Seatbelt can apply.
    expect(loginSpawn.executable).toBe("/usr/bin/sandbox-exec"); expect(loginSpawn.args.slice(0, 4)).toEqual(["-f", join(loginSpawn.options.environment.TMPDIR, "launch.sb"), join(root, "runtime", "private", "codex"), "app-server"]);
    for (const capture of [worker, logout]) { expect(capture.executable).toBe(join(root, "runtime", "private", "codex")); expect(capture.args[0]).toBe("app-server"); }
    for (const capture of io.captures) expect(io.trace.indexOf(`kill:${capture.pid}`)).toBeLessThan(io.trace.indexOf(`reap:${capture.pid}`));
    expect(worker.config).toEqual(logout.config); expect(worker.options.environment.TMPDIR).not.toBe(logout.options.environment.TMPDIR);
    expect(worker.methods).toContain("turn/start"); expect(worker.turn).toMatchObject({ model: "gpt-default", collaborationMode: { settings: { model: "gpt-default", reasoning_effort: "high" } } }); expect(logout.methods).toContain("account/logout"); expect(logout.methods).not.toContain("thread/start"); expect(logout.methods).not.toContain("turn/start");
    expect(issuedInputs.at(-1).account.accountEpoch).toBe(2);
  });
  it("binds the same candidate's observed account through the concrete P2 lease before publication", async () => {
    let p2Callbacks: any;
    const p2 = new HostAccountAuthority({
      runtimeDirectory: join(root, "runtime"),
      auth: new AuthRegistry(join(root, "runtime")),
      expectedEuid: process.geteuid?.() ?? process.getuid?.() ?? 0,
      signingPredicate: { schema: "chirality.host-account-signing-predicate/v1", serviceName: "com.chirality.app.runtime.account-host", bundleId: "com.chirality.app",
        teamId: "TESTTEAM01", peerRequirement: 'identifier "com.chirality.app" and anchor apple generic' },
      nativeAdmission: { createHostXpcServer(input) { p2Callbacks = input; return {
        async ping(_connectionId, value) { return value; }, async closeConnection() {}, async close() {}
      }; } }
    });
    const worker = sourceOptions.releaseV2.basis.worker;
    const qualifiedRecord = JSON.parse(await readFile(worker.recordPath, "utf8"));
    const trialRecord = { ...qualifiedRecord, schema: "chirality-codex-worker-purpose-release/v3", evidenceClass: "exact-local-human-trial-authorized", trialScope: "local-human-functional-trial",
      limbs: Object.fromEntries(REQUIRED_RUNTIME_CONFORMANCE_LIMBS.map(name => [name, { status: "pending-human-trial" }])), prerequisites: Object.fromEntries(["signed-payload-and-supply", "trusted-app-and-account-host", "native-enforcement-and-retirement", "connected-source-contract"].map(name => [name, { attempted: true, passed: true, evidenceSha256: hash(name) }])) };
    await writeFile(worker.recordPath, JSON.stringify(trialRecord), { mode: 0o600 });
    const acceptance = JSON.parse(await readFile(worker.acceptancePath, "utf8"));
    const trialAcceptance = { ...acceptance, recordSha256: hash(JSON.stringify(trialRecord)), ownerReference: "same-worker-trial-basis" };
    await writeFile(worker.acceptancePath, JSON.stringify(trialAcceptance), { mode: 0o600 });
    worker.recordSha256 = trialAcceptance.recordSha256;
    worker.acceptanceSha256 = hash(JSON.stringify(trialAcceptance));
    sourceOptions.releaseV2.basis.workerDisposition = "local-human-trial";
    const { hostAuthority: _syntheticHost, ...withoutSyntheticHost } = compositionAdapters;
    let completed: any;
    const actualBindings = await createControlledHostedBootstrapPrivateBindingsForTests({
      ...sourceOptions,
      requestTimeoutMs: 10_000,
      hostAccount: { executablePath: join(root, "Chirality.app", "Contents", "MacOS", "Chirality"), resourcesPath: sourceOptions.releaseV2.basis.verified.resourcesRoot }
    }, {
      ...withoutSyntheticHost,
      createAccountHost: async () => p2,
      admitHosted: async (options: any) => {
        expect(options.runtimeV2).toBeUndefined();
        expect(options.runtimeV2Preparation?.evidence).toBe("release-live-host-policy-preparation-v2");
        const result = await CodexSupervisor.admitHosted(options);
        completed = result.runtimeV2;
        supervisor = result.supervisor;
        return result;
      }
    });
    try {
      expect(await actualBindings.createAccountHost!(new AuthRegistry(join(root, "runtime")))).toBe(p2);
      await p2.start();
      const challenge = await p2Callbacks.onCeremonyOpen({ connectionId: "actual-p2", requestId: "actual-ceremony" });
      const nonce = Buffer.alloc(32, 19);
      await p2Callbacks.onCeremonyFinish({ connectionId: "actual-p2", requestId: "actual-ceremony", hostNonce: nonce,
        proof: createHostAccountCeremonyProof(nonce, challenge.challenge, challenge.generation) });
      const current = await actualBindings.createCeremony({ projectId: "project", manifestHash, canonicalRoot: join(root, "project"),
        privateDirectory: join(root, "runtime", "private"), codexHome: join(root, "runtime", "private", "home"),
        providerNetworkConsent: { approvedBy: "owner", approvalReference: "act", approvedAt: "2026-09-10T12:00:00.000Z" } });
      await current.start();
      const admitted = await actualBindings.establishAdmission!({ projectId: "project", canonicalRoot: join(root, "project"), ceremony: current });
      expect(admitted.continuity).toMatchObject({ accountId: account.accountId, accountEpoch: account.accountEpoch });
      expect(admitted.nativePlanQualification).toEqual({ adapterId: "codex-app-server", providerId: "openai", dispositionId: "same-worker-trial-basis",
        admissionSha256: trialAcceptance.recordSha256, evidenceClass: "native-adapter-local-human-trial" });
      expect(completed?.instanceInput.account).toEqual(account);
      expect(completed?.instanceInput.hostAuthority).toMatchObject({ evidence: "accepted-host-account-authority", mechanismId: "host-p2-xpc-peer-requirement" });
      const bootstrapRuntime = join(root, "b");
      const currentInstructionRoot = resolve(process.cwd(), "../..");
      await Promise.all([
        cp(join(currentInstructionRoot, "AGENTS.md"), join(sourceOptions.instructionRoot, "AGENTS.md")),
        cp(join(currentInstructionRoot, "agents"), join(sourceOptions.instructionRoot, "agents"), { recursive: true })
      ]);
      io.uniqueRandom = true;
      let bootstrapMaterializationFailure: unknown;
      const bootstrapHost = await startControlledHostedBootstrapRuntimeHostForTests({ enabled: true, runtimeDirectory: bootstrapRuntime, daemonSocket: "s", instructionRoot: sourceOptions.instructionRoot }, {
        async createCeremony() { return { async start() { return { loginId: "same-trial", authUrl: "https://example.test/trial" }; }, async status() { return { state: "completed" as const, hasAccount: true }; }, async cancel() {}, async close() {} }; },
        async establishAdmission() { return admitted; },
        async materializeAdmission(input) { try { return await actualBindings.materializeAdmission!(input); } catch (error) { bootstrapMaterializationFailure = error; throw error; } }
      });
      try {
        const bootstrapClient = new RuntimeClient({ socketPath: bootstrapHost.socketPath, tokenFile: bootstrapHost.bootstrapTokenFile });
        const registered = await bootstrapClient.initializeHostedBootstrapProject({ projectRoot: join(root, "project") });
        await bootstrapClient.grantHostedProviderNetworkConsent(registered.projectId); await bootstrapClient.startHostedBootstrapLogin(registered.projectId);
        const bootstrapStatus = await bootstrapClient.hostedBootstrapStatus(registered.projectId);
        if (bootstrapStatus.admission !== "ready") throw new Error(`Unexpected bootstrap status: ${JSON.stringify(bootstrapStatus)}: ${String(bootstrapMaterializationFailure)} ${JSON.stringify(bootstrapMaterializationFailure)}`);
        const projectClient = new RuntimeClient({ socketPath: bootstrapHost.socketPath, tokenFile: resolveHostedProjectTokenFile(bootstrapRuntime, registered.projectId) });
        const session = await projectClient.createSession(registered.projectId, { projectId: registered.projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite", interactionMode: "native-plan" });
        await expect(projectClient.getNativePlanCapability(registered.projectId, session.sessionId)).resolves.toEqual({ schemaVersion: "chirality.native-plan-capability/v3", status: "trial", admission: admitted.nativePlanQualification });
        await new HostedConsentStore({ canonicalRoot: join(root, "project"), codexHome: join(root, "runtime", "private", "home") }).grant({ identity: admitted.continuity, posture: "off", approvedBy: "controlled-owner", approvedAt: "2026-09-10T12:00:00.000Z" });
        io.trialPlan = true;
        const stream = await projectClient.turnSession(registered.projectId, session.sessionId, { turnId: "same-trial-turn", message: "Observe the accepted trial", interactionMode: "native-plan" });
        const turnEvents: unknown[] = [];
        const drained = (async () => { for await (const event of stream) turnEvents.push(event); })();
        try { await expect.poll(async () => (await projectClient.listNativePlanClarifications(registered.projectId, session.sessionId)).clarifications.length, { timeout: 5_000 }).toBe(1); }
        catch (error) { await drained; throw new Error(`Trial clarification missing: trace=${JSON.stringify(io.trace)} events=${JSON.stringify(turnEvents)}`, { cause: error }); }
        try { await projectClient.replyNativePlanClarification(registered.projectId, session.sessionId, { requestId: "trial-question", answers: { scope: { answers: ["Yes"] } } }); }
        catch (error) { await drained; throw new Error(`Trial reply failed: trace=${JSON.stringify(io.trace)} events=${JSON.stringify(turnEvents)}`, { cause: error }); }
        expect(io.planAnswerObserved).toBe(true);
        await expect(projectClient.listNativePlanRevisions(registered.projectId, session.sessionId)).resolves.toMatchObject({ status: "trial", admission: admitted.nativePlanQualification,
          revisions: [{ revision: 1, sourceEvent: { qualificationState: "trial", admission: admitted.nativePlanQualification, plan: { text: "accepted trial plan" } } }] });
        await bootstrapClient.cancelHostedBootstrapLogin(registered.projectId);
        await Promise.race([drained, new Promise<never>((_, reject) => setTimeout(() => reject(new Error(`Trial turn did not retire: trace=${JSON.stringify(io.trace)} events=${JSON.stringify(turnEvents)}`)), 5_000))]);
        await expect(projectClient.listNativePlanRevisions(registered.projectId, session.sessionId)).resolves.toMatchObject({ status: "trial", admission: admitted.nativePlanQualification,
          revisions: [{ revision: 1 }] });
      } finally { await bootstrapHost.stop().catch(error => { if ((error as { code?: string }).code !== "STOPPED_DEGRADED") throw error; }); }
    } finally {
      await actualBindings.close?.().catch(() => undefined);
      await p2.close().catch(() => undefined);
    }
  }, 20_000);
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
    // The direct worker keeps no outer profile; its private session directory is the retained allocation.
    await expect(readdir(io.captures[1].options.environment.TMPDIR)).resolves.toEqual([]); expect(io.trace).not.toContain("account/logout");
  });

  it("rejects a same-byte outer profile replacement during the last release read", async () => {
    const current = await ceremony(); let count = 0;
    io.outerHook = (outer: any) => { if (++count === 2) io.releaseRead = async () => { io.releaseRead = undefined; const bytes = await readFile(outer.sandboxProfilePath); await rename(outer.sandboxProfilePath, `${outer.sandboxProfilePath}.old`); await writeFile(outer.sandboxProfilePath, bytes, { mode: 0o600 }); }; return outer; };
    await expect(bindings.establishAdmission({ projectId: "project", canonicalRoot: join(root, "project"), ceremony: current })).rejects.toThrow(); expect(io.captures).toHaveLength(1);
  });

  describe("native-11 full composition",()=>{
    beforeAll(()=>{fixtureCompilerIdentity=11;});
    afterAll(()=>{fixtureCompilerIdentity=10;});

    it("carries the captured compiler selector through login, worker turn, and fenced logout",async()=>{
      const admitted=await admission();await materialize(admitted);expect(await turn()).toMatchObject({exitCode:0});await signOut();
      expect(io.captures).toHaveLength(3);
      const [loginSpawn,worker,logout]=io.captures;
      expect(loginSpawn.args.slice(3,5)).toEqual(["app-server","--chirality-disable-native-skills"]);
      for(const capture of [worker,logout])expect(capture.args.slice(0,2)).toEqual(["app-server","--chirality-disable-native-skills"]);
      const loginRead=loginSpawn.events.indexOf("config/read"),loginEffect=loginSpawn.events.indexOf("account/login/start");
      expect(loginRead).toBeGreaterThanOrEqual(0);expect(loginEffect).toBeGreaterThanOrEqual(0);expect(loginRead).toBeLessThan(loginEffect);
      expect(loginSpawn.readbacks[0]).toMatchObject({chirality_runtime:{nativeSkills:"disabled"}});
      expect(loginSpawn.events).not.toContain("account/identitySnapshot");
      const workerRead=worker.events.indexOf("config/read"),acquire=worker.events.indexOf("chirality/admissionAcquire"),thread=worker.events.indexOf("thread/start");
      expect(workerRead).toBeGreaterThanOrEqual(0);expect(acquire).toBeGreaterThanOrEqual(0);expect(thread).toBeGreaterThanOrEqual(0);expect(workerRead).toBeLessThan(acquire);expect(workerRead).toBeLessThan(thread);
      expect(worker.readbacks.length).toBeGreaterThanOrEqual(3);expect(worker.readbacks).toEqual(expect.arrayContaining([expect.objectContaining({chirality_runtime:{nativeSkills:"disabled"}})]));
      expect(worker.events).toContain("turn/start");
      const logoutRead=logout.events.indexOf("config/read"),logoutEffect=logout.events.indexOf("account/logout");
      expect(logoutRead).toBeGreaterThanOrEqual(0);expect(logoutEffect).toBeGreaterThanOrEqual(0);expect(logoutRead).toBeLessThan(logoutEffect);
      expect(logout.readbacks[0]).toMatchObject({chirality_runtime:{nativeSkills:"disabled"}});
      expect(await bindingRecord()).toMatchObject({state:"fenced",accountEpoch:2});
    });

    it("connects the exact inherited subset through real D36 admission, Supervisor association, child callback, and family settlement",async()=>{
      io.stageCChild=true;
      const admitted=await admission();const materialized=await materialize(admitted);
      await new HostedConsentStore({canonicalRoot:join(root,"project"),codexHome:join(root,"runtime","private","home")}).grant({identity:admitted.continuity,posture:"off",approvedBy:"controlled-owner",approvedAt:"2026-09-10T12:00:00.000Z"});
      let observed:any;
      const schema={type:"object",additionalProperties:false} as const;
      const tools=[
        {name:"chirality_list_methods",description:"List methods",inputSchema:schema,permission:{effect:"allow" as const,operation:"read" as const},execute:async(_input:unknown,_signal:AbortSignal,context?:any)=>{observed=context;return{ok:true};}},
        {name:"chirality_inspect_method",description:"Inspect method",inputSchema:schema,permission:{effect:"allow" as const,operation:"read" as const},execute:async()=>({})},
        {name:"chirality_load_method",description:"Load method",inputSchema:schema,permission:{effect:"allow" as const,operation:"read" as const},execute:async()=>({})}
      ];
      const preflight=await materialized.delegated.preflight("project","turn:stage-c-child");
      await expect(materialized.delegated.turn("project",{turnId:"stage-c-child",prompt:"use child",compatibility:sourceOptions.compatibility,preflight},tools)).resolves.toMatchObject({terminal:{outcome:"completed"}});
      expect(observed).toMatchObject({threadId:"child-thread",turnId:"child-turn",callId:"child-call",nativeChild:{associationId:"a".repeat(32),parentThreadId:"thread",parentTurnId:"turn",selectedRole:{kind:"configured",name:"HELP_HUMAN"}}});
      const worker=io.captures[1];
      expect(worker.rootCarrier).toEqual({schema:"chirality-native-tools/v1",inheritableTools:tools.map(({name,description,inputSchema})=>({name,description,inputSchema}))});
      expect(worker.events.indexOf("chirality/admissionAcquire")).toBeLessThan(worker.events.indexOf("thread/start"));
      expect(worker.events).toEqual(expect.arrayContaining(["thread/start","turn/start"]));
    });

    it("rejects a missing login projection before any login effect",async()=>{
      io.nativeReadback.set(0,"missing");await expect(ceremony()).rejects.toThrow();
      expect(io.captures).toHaveLength(1);expect(io.captures[0].events).not.toContain("account/login/start");
    });

    it("rejects an upstream worker projection before acquire or model effects",async()=>{
      const current=await ceremony();io.nativeReadback.set(1,"upstream");
      await expect(bindings.establishAdmission({projectId:"project",canonicalRoot:join(root,"project"),ceremony:current})).rejects.toThrow();
      expect(io.captures).toHaveLength(2);expect(io.captures[1].events).not.toContain("chirality/admissionAcquire");expect(io.captures[1].events).not.toContain("thread/start");
    });
  });

});
