import { createHash } from "node:crypto";
import { mkdir, mkdtemp, readFile, readdir, realpath, rm, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { PassThrough } from "node:stream";
import { afterEach, describe, expect, it } from "vitest";
import { CHIRALITY_ROLE_NAMES } from "@chirality/runtime-contracts";
import { createFakeRuntimeAdmissionNativeAdapter, DescendantTracker, recordKey, type ProjectRegistry, type SessionStore } from "@chirality/runtime-core";
import type { DelegatedNativePlanSink } from "@chirality/runtime-core";
import type { UIEvent, WorkerHandle } from "@chirality/runtime-contracts";
import { RuntimeClient } from "@chirality/runtime-client";
import { CodexSupervisor } from "../packages/daemon/src/codex-supervisor.js";
import { PACKAGED_REQUEST_TIMEOUT_MS, PACKAGED_TURN_TIMEOUT_MS } from "../packages/daemon/src/hosted-packaged-release.js";
import { admitHostedControlledForTests } from "../packages/daemon/src/codex-supervisor-test-support.js";
import { createControlledCodexCandidateLauncherFactoryForTests } from "../packages/daemon/src/codex-admitted-launcher.js";
import type { AuthenticatedCodexCandidate } from "../packages/daemon/src/codex-authenticated-transport.js";
import { HostedIdentityBindingStore } from "../packages/daemon/src/hosted-identity-binding.js";
import { hostAuthoritySubjectBindingDigestV2 } from "../packages/daemon/src/runtime-conformance-v2-admission.js";
import { AuthorityTranscript, AUTHORITY_CONTRACT, initializationProof } from "../packages/daemon/src/supplier-authority-controller.js";
import { resolveHostedProjectTokenFile } from "../packages/daemon/src/hosted-paths.js";
import { startControlledHostedBootstrapRuntimeHostForTests } from "../packages/daemon/src/hosted-bootstrap.js";
import { settledHostedBootstrapStatus } from "./helpers.js";
import { startControlledHostedPrivateBootstrapRuntimeHostForTests } from "../packages/daemon/src/hosted-private-entry.js";
import {
  createControlledHostedBootstrapPrivateBindingsForTests,
  validateHostedPrivateCompositionOptions,
  type ControlledHostedPrivateCompositionAdapters,
  type HostedPrivateCompositionOptions
} from "../packages/daemon/src/hosted-private-composition.js";

const roots: string[] = [];
afterEach(async () => { await Promise.all(roots.splice(0).map(root => rm(root, { recursive: true, force: true }))); });
async function drain(source: Awaited<ReturnType<RuntimeClient["turnSession"]>>): Promise<UIEvent[]> { const events: UIEvent[] = []; for await (const event of source) events.push(event); return events; }
const sha256 = (value: string | Buffer): string => createHash("sha256").update(value).digest("hex");

async function packagedInventoryFixture(root: string) {
  const resourcesRoot = join(root, "Resources");
  const files: Record<string, string> = {
    "app.asar": "controlled app",
    "native/chirality_native_admission.node": "controlled native artifact",
    "runtime-cli/chirality-cli.mjs": "controlled runtime cli",
    "runtime-cli/chirality-cli.mjs.map": "controlled runtime source identity"
  };
  for (const [name, contents] of Object.entries(files)) { await mkdir(join(resourcesRoot, name, ".."), { recursive: true }); await writeFile(join(resourcesRoot, name), contents); }
  const builder = await import(pathToFileURL(resolve(process.cwd(), "../chirality-app-dev/frontend/scripts/prepare-packaged-instruction-root.mjs")).href) as {
    preparePackagedInstructionRoot(input: { sourceRoot: string; docsRoot: string; outputRoot: string }): Promise<string[]>;
  };
  const sourceRoot = resolve(process.cwd(), "../..");
  await builder.preparePackagedInstructionRoot({ sourceRoot, docsRoot: join(sourceRoot, "docs"), outputRoot: join(resourcesRoot, "instruction-root") });
  const relativePaths: string[] = [];
  const walk = async (relativeDirectory: string): Promise<void> => {
    for (const entry of (await readdir(join(resourcesRoot, relativeDirectory), { withFileTypes: true })).sort((a, b) => a.name.localeCompare(b.name))) {
      const relativePath = join(relativeDirectory, entry.name);
      if (entry.isDirectory()) await walk(relativePath); else if (entry.isFile()) relativePaths.push(relativePath); else throw new Error("controlled package fixture contains an alias");
    }
  };
  await walk(""); relativePaths.sort();
  const entries = await Promise.all(relativePaths.map(async relativePath => {
    const bytes = await readFile(join(resourcesRoot, relativePath)); return { relativePath, sha256: sha256(bytes), size: bytes.length };
  }));
  const manifest = { schema: "chirality-runtime-artifact-inventory/v1", sourceIdentityDigest: sha256("controlled source identity"),
    dependencyResolutionDigest: sha256("controlled dependency resolution"), closureRoots: ["app.asar", "instruction-root", "native", "runtime-cli"], entries };
  const manifestPath = join(resourcesRoot, "runtime-artifact-inventory.json"); await writeFile(manifestPath, JSON.stringify(manifest));
  return { resourcesRoot, manifestPath, instructionRoot: join(resourcesRoot, "instruction-root"), selection: { kind: "packaged-resources" as const, resourcesRoot, manifestPath } };
}

async function controlledAuthenticatedCandidate(input: {
  index: number; projectRoot: string; privateDirectory: string; executablePath: string;
  lease: ReturnType<ReturnType<typeof createFakeRuntimeAdmissionNativeAdapter>["acquire"]>;
  policyDigest: string; expectedPermissions: { filesystem: Record<string, "read" | "write" | "deny">; network: { enabled: boolean } };
  nativeRoles: { digest: string; configOverrides: readonly string[] };
  trace: string[]; secrets: Buffer[];
}): Promise<AuthenticatedCodexCandidate> {
  const stdin = new PassThrough(), stdout = new PassThrough();
  const secret = Buffer.alloc(32, input.index), supplierGeneration = `supplier-${input.index}`, identityGeneration = `identity-${input.index}`;
  const runtimeProcessIncarnationId = `11111111-1111-4111-8111-${String(input.index).padStart(12, "0")}`;
  const descriptor = { capability: "chirality.local-admission-authority", contract: AUTHORITY_CONTRACT, major: 1, minor: 0 } as const;
  const v4Descriptor = { capability: "account.identity-snapshot", contract: "chirality-supplier-account-identity/1", major: 1, minor: 0, method: "account/identitySnapshot" } as const;
  const authorityInitialize = { runtimeProcessIncarnationId, supplierGeneration, runtimeChallenge: Buffer.alloc(32, input.index + 10).toString("base64url"),
    exactSupplyDigest: "a".repeat(64), authoritySecret: secret, descriptor, v4Descriptor };
  const canonicalSnapshot = { schema: "chirality-supplier-account-identity-response/1", state: "available", supplierGeneration, identityGeneration,
    accountUserId: "stable-account-user", providerWorkspaceId: "stable-provider-workspace" } as const;
  const snapshotDigest = sha256(JSON.stringify(canonicalSnapshot));
  const identity = { runtimeProcessIncarnationId, supplierGeneration };
  const inbound = new AuthorityTranscript(secret, identity, "runtime-to-supplier"), outbound = new AuthorityTranscript(secret, identity, "supplier-to-runtime");
  const send = (value: unknown): void => { stdout.write(`${JSON.stringify(value)}\n`); };
  const roles: Record<string, { description: string; config_file: string }> = {};
  for (let offset = 4, role = 0; role < CHIRALITY_ROLE_NAMES.length; role++, offset += 2) {
    const roleId = CHIRALITY_ROLE_NAMES[role]!;
    roles[roleId] = { description: JSON.parse(input.nativeRoles.configOverrides[offset]!.slice(`agents.${roleId}.description=`.length)),
      config_file: JSON.parse(input.nativeRoles.configOverrides[offset + 1]!.slice(`agents.${roleId}.config_file=`.length)) };
  }
  let buffered = "", closed = false;
  stdin.on("data", chunk => {
    buffered += String(chunk);
    for (;;) {
      const newline = buffered.indexOf("\n"); if (newline < 0) break;
      const raw = buffered.slice(0, newline); buffered = buffered.slice(newline + 1);
      const message = JSON.parse(raw) as Record<string, any>;
      if (message.method === "initialize") {
        input.trace.push(`initialize-${input.index}`);
        const result = { contract: AUTHORITY_CONTRACT, ...identity, supplierChallenge: Buffer.alloc(32, input.index + 20).toString("base64url"), descriptor, v4Descriptor, proof: "" };
        result.proof = initializationProof(secret, { ...authorityInitialize, ...result });
        send({ id: message.id, result: { chiralityAdmissionAuthority: result } }); continue;
      }
      if (message.method === "initialized") continue;
      if (message.method === "account/identitySnapshot") { input.trace.push(`snapshot-${input.index}`); send({ id: message.id, result: canonicalSnapshot }); continue; }
      if (message.method === "config/read") {
        input.trace.push(`config-${input.index}`);
        send({ id: message.id, result: { config: { permissions: { chirality_test: input.expectedPermissions }, approvals_reviewer: "user", approval_policy: "never",
          allow_login_shell: false, features: { plugins: false, remote_plugin: false, shell_snapshot: false, network_proxy: false, multi_agent: true, multi_agent_v2: false },
          agents: { enabled: true, max_depth: 2, ...roles }, hooks: null, mcp_servers: {}, notify: null, plugins: {}, profiles: {}, profile: null,
          projects: { [input.projectRoot]: { trust_level: "trusted" } } } } }); continue;
      }
      if (message.method === "account/read") { input.trace.push(`account-${input.index}`); send({ id: message.id, result: { requiresOpenaiAuth: true, account: { type: "chatgpt", email: null, planType: "fixture" } } }); continue; }
      if (message.method === "thread/start" || message.method === "thread/resume") {
        const threadId = message.params.threadId ?? "provider-thread"; input.trace.push(`${message.method}-${input.index}`);
        send({ method: "thread/started", params: { thread: { id: threadId } } });
        send({ id: message.id, result: { thread: { id: threadId }, approvalsReviewer: "user", approvalPolicy: "never" } }); continue;
      }
      if (message.method === "turn/start") {
        const threadId = message.params.threadId, turnId = `turn-${input.index}`; input.trace.push(`turn-${input.index}`);
        send({ id: message.id, result: { turn: { id: turnId, status: "inProgress" } } });
        send({ method: "turn/started", params: { threadId, turn: { id: turnId, status: "inProgress" } } });
        send({ method: "item/started", params: { threadId, turnId, item: { id: `item-${input.index}`, type: "agentMessage", text: "" } } });
        send({ method: "item/agentMessage/delta", params: { threadId, turnId, itemId: `item-${input.index}`, delta: `controlled-candidate-${input.index}` } });
        send({ method: "item/completed", params: { threadId, turnId, item: { id: `item-${input.index}`, type: "agentMessage", text: `controlled-candidate-${input.index}` } } });
        send({ method: "turn/completed", params: { threadId, turn: { id: turnId, status: "completed" } } }); continue;
      }
      const body = inbound.accept(raw);
      if (body.kind !== "request") throw new Error("controlled authority request expected");
      input.trace.push(`${body.op}-${input.index}`);
      if (body.op === "chirality/admissionAcquire") {
        const common = { requestId: body.requestId, operationId: body.operationId, leaseId: `lease-${input.index}`, supplierGeneration, identityGeneration, snapshotDigest };
        send(outbound.encode({ kind: "result", op: body.op, state: "acquired", ...common }));
        send(outbound.encode({ kind: "notification", op: "chirality/admissionAcquired", ...common }));
      } else {
        const released = body.op === "chirality/admissionRelease", common = { requestId: body.requestId, leaseId: body.leaseId, disposition: body.disposition };
        send(outbound.encode({ kind: "result", op: body.op, state: released ? "released" : "aborted", ...common } as any));
        send(outbound.encode({ kind: "notification", op: released ? "chirality/admissionReleased" : "chirality/admissionAborted", ...common } as any));
      }
    }
  });
  const privateBindingStore = await HostedIdentityBindingStore.open({ privateDirectory: input.privateDirectory, canonicalRoot: input.projectRoot,
    policyDigest: input.policyDigest, runtimeAuthorityId: `runtime-${input.index}`, randomHandle: () => Buffer.alloc(32, 42) });
  const pid = 5000 + input.index; let alive = true;
  const descendantTracker = new DescendantTracker({ leaderPid: pid, intervalMs: 10, maxDurationMs: 10_000,
    census: async () => alive ? [{ pid, ppid: 1, pgid: pid, uid: process.getuid!(), startIdentity: `candidate-${input.index}` }] : [] });
  input.secrets.push(secret);
  return { pid, transport: { stdin, stdout, close: async () => { if (closed) return; closed = true; input.trace.push(`cleanup-${input.index}`); alive = false; stdin.destroy(); stdout.destroy(); } },
    cleanup: async () => { if (closed) return; closed = true; input.trace.push(`cleanup-${input.index}`); alive = false; stdin.destroy(); stdout.destroy(); }, authorityInitialize,
    kernelLease: input.lease, supplierGeneration, privateBindingStore,
    expectedPolicy: { permissionProfile: "chirality_test", policyDigest: input.policyDigest, expectedPermissions: input.expectedPermissions, nativeRoleConfiguration: input.nativeRoles },
    expectedToolRuntime: { codexSelfExecutablePath: input.executablePath, requiresSandboxedFileSystem: true, requiresSandboxedFileStreaming: true }, descendantTracker };
}

async function fixture(input: { logoutFails?: boolean; openStoreFails?: boolean; fenceFails?: boolean; logoutLauncherFails?: boolean } = {}) {
  const root = await realpath(await mkdtemp(join(await realpath("/tmp"), "hc-"))); roots.push(root);
  const canonicalRoot = join(root, "project"), runtimeDirectory = join(root, "runtime"), instructionRoot = join(root, "instructions");
  const privateRoot = join(runtimeDirectory, "hosted-bootstrap", "project"), codexHome = join(privateRoot, "codex-home");
  await Promise.all([canonicalRoot, runtimeDirectory, instructionRoot, privateRoot, codexHome].map(path => mkdir(path, { recursive: true, mode: 0o700 })));
  const events: string[] = [];
  const lease = createFakeRuntimeAdmissionNativeAdapter().acquire(runtimeDirectory, "runtime-admission-authority.lock");
  const continuity = { canonicalRoot, cwd: canonicalRoot, accountId: "rhb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", accountEpoch: 1, policyDigest: "a".repeat(64) };
  const supervisor = CodexSupervisor.controlledForTests({ identity: continuity, model: "gpt-test", launch: async () => { throw new Error("unused"); } });
  let ceremonyState: "pending" | "completed" = "completed";
  let launcherFactoryCalls = 0;
  const adapters: ControlledHostedPrivateCompositionAdapters = {
    revalidateReleaseBasis: async () => {},
    acquireLease: async () => lease,
    stageSupplier: async (_source, directory) => join(directory, "supplier", "codex"),
    prepareNativeRoles: async () => { events.push("roles-materialized"); return { digest: "9".repeat(64), configOverrides: ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2"] }; },
    bindRuntimeReadRoot: async (path, artifactInventory) => ({ path, readPaths: [join(path, "agents")], contentDigest: "4".repeat(64), artifactInventory }),
    validateLoginStartup: async () => ({ bindingDigest: "8".repeat(64), evidence: "externally-accepted-native-login-purpose", recordSha256: "6".repeat(64), ownerReference: "owner-act" }),
    createLogin: () => ({ start: async () => ({ loginId: "login-1", authUrl: "https://auth.openai.com/login" }), status: async () => ({ state: ceremonyState, hasAccount: ceremonyState === "completed" }), resolveModelCatalog: async () => { events.push("catalog-read"); throw new Error("v1 path never reads the catalog"); }, cancel: async () => { events.push("ceremony-cancel"); }, close: async () => { events.push("ceremony-close"); } }),
    preparePolicy: async input => { events.push(`policy-roles-${input.nativeRoleConfiguration?.digest ?? "missing"}`); return { policyDigest: "a".repeat(64), cleanup: async () => { events.push("policy-cleanup"); } }; },
    createLauncherFactory: launcherInput => { launcherFactoryCalls++; events.push(`launcher-roles-${launcherInput.bindings.nativeRoleConfiguration?.digest ?? "missing"}`); events.push(`launcher-config-${launcherInput.bindings.configDigest}`); if (input.logoutLauncherFails && launcherFactoryCalls > 1) throw new Error("logout launcher failed"); return { create: () => { throw new Error("controlled logout adapter does not launch"); }, close: async () => { events.push("launcher-close"); } }; },
    admitHosted: async admitOptions => { events.push(`admit-config-${admitOptions.configDigest}`); events.push(`admit-catalog-${admitOptions.modelCatalog === undefined ? "absent" : "present"}`); return { supervisor, continuity, authority: { supplierGeneration: "supplier-1", identityGeneration: "identity-1", snapshotDigest: "b".repeat(64) }, accountDigest: "7".repeat(64), retire: async () => { events.push("admission-retire"); } }; },
    logout: async (_factory, digest) => { events.push(`logout-digest-${digest}`); events.push("supplier-logout"); if (input.logoutFails) throw new Error("logout failed"); },
    openBindingStore: async () => { if (input.openStoreFails) throw new Error("store failed"); return ({ fence: async reason => { events.push(`fence-${reason}`); if (input.fenceFails) throw new Error("fence failed"); return continuity; } }) as unknown as HostedIdentityBindingStore; }
  };
  const options: HostedPrivateCompositionOptions = {
    runtimeDirectory, supplierExecutablePath: join(root, "packaged-codex"), nativeAddonPath: join(root, "native.node"), instructionRoot, model: "gpt-test",
    managedAuth: { backend: "keyring", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } },
    compatibility: { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "c".repeat(64) },
    conformance: { recordPath: join(root, "record.json"), acceptancePath: join(root, "acceptance.json"), ownerActPath: join(root, "owner.json"), ownerActSha256: "d".repeat(64), activationId: "activation", gateIdentity: "G4", artifactInventory: { kind: "source-tree", sourceRoot: root } },
    loginPurposeRelease: { recordPath: join(root, "login-record.json"), acceptancePath: join(root, "login-acceptance.json"), ownerActPath: join(root, "login-owner.json"), ownerActSha256: "5".repeat(64), activationId: "login-activation", gateIdentity: "D36", artifactInventory: { kind: "source-tree", sourceRoot: root } },
    configDigest: "e".repeat(64), consentVersion: "consent-v1", commandNetworkPosture: "off", commandNetworkConsent: { approvedBy: "owner", approvedAt: "2026-09-10T00:00:00.000Z", explicitUserAct: true },
    protectedPaths: [runtimeDirectory], immutableReadRoots: [instructionRoot]
  };
  options.configDigest = recordKey({ schema: "chirality.hosted-private-config/v1", model: options.model, managedAuth: options.managedAuth,
    compatibility: options.compatibility, commandNetworkPosture: options.commandNetworkPosture, commandNetworkConsent: options.commandNetworkConsent, protectedPaths: options.protectedPaths,
    immutableReadRoots: options.immutableReadRoots, instructionRoot: options.instructionRoot, nativeRoleConfigurationDigest: "9".repeat(64), trustedRuntimeReadRoot: { contentDigest: "4".repeat(64), readPaths: [join(options.instructionRoot, "agents")] }, loginPurposeRelease: options.loginPurposeRelease, consentVersion: options.consentVersion });
  const bindings = await createControlledHostedBootstrapPrivateBindingsForTests(options, adapters);
  const ceremony = await bindings.createCeremony({ projectId: "project", canonicalRoot, privateDirectory: privateRoot, codexHome,
    providerNetworkConsent: { approvedBy: "owner", approvalReference: "act-1", approvedAt: new Date().toISOString() } });
  return { root, canonicalRoot, runtimeDirectory, instructionRoot, privateRoot, codexHome, events, lease, continuity, bindings, ceremony, options, adapters, setCeremonyState: (state: typeof ceremonyState) => { ceremonyState = state; } };
}

describe("hosted private production composition boundary", () => {
  it("maps registered project and consent to P2 before staging, and rejects a structural host claim", async () => {
    const f = await fixture();
    const calls: unknown[] = [], stagedBeforeAuthority: string[] = [];
    const hostAuthority = async (input: any) => { calls.push(input); return { authority: { evidence: "accepted-host-account-authority", mechanismId: "fake", daemonGeneration: "d", authorityGeneration: "a", subjectBindingDigest: hostAuthoritySubjectBindingDigestV2({ ...input, account: null }), liveLeaseDigest: "1".repeat(64) } as any, account: null }; };
    const adapters = { ...f.adapters, hostAuthority, stageSupplier: async (...args: Parameters<typeof f.adapters.stageSupplier>) => { stagedBeforeAuthority.push("staged"); return f.adapters.stageSupplier(...args); } };
    const { model: _model, managedAuth: _managedAuth, conformance: _conformance, loginPurposeRelease: _login, configDigest: _config, consentVersion: _consentVersion, commandNetworkConsent: _commandConsent, ...base } = f.options;
    const options = { ...base, protectedPaths: [f.runtimeDirectory, join(f.runtimeDirectory, "release-authority"), join(f.runtimeDirectory, "release-basis")],
      releaseV2: { basis: { schema: "chirality-hosted-packaged-release-basis/v2" as const, basisDigest: "7".repeat(64) } as any } };
    expect(() => validateHostedPrivateCompositionOptions({ ...options, commandNetworkPosture: "on" })).toThrow();
    expect(() => validateHostedPrivateCompositionOptions({ ...options, configDigest: "a".repeat(64) })).toThrow();
    expect(() => validateHostedPrivateCompositionOptions({ ...options, managedAuth: f.options.managedAuth })).toThrow();
    expect(() => validateHostedPrivateCompositionOptions({ ...options, turnTimeoutMs: 3_600_001 })).toThrow(expect.objectContaining({ code: "ENGINE_UNAVAILABLE", details: { reason: "HOST_CONFIGURATION_INVALID" } }));
    expect(() => validateHostedPrivateCompositionOptions({ ...options, requestTimeoutMs: 600_001 })).toThrow(expect.objectContaining({ code: "ENGINE_UNAVAILABLE", details: { reason: "HOST_CONFIGURATION_INVALID" } }));
    expect(validateHostedPrivateCompositionOptions({ ...options, requestTimeoutMs: 90_000, turnTimeoutMs: 1_800_000 })).toMatchObject({ requestTimeoutMs: 90_000, turnTimeoutMs: 1_800_000 });
    expect(validateHostedPrivateCompositionOptions(options)).not.toHaveProperty("managedAuth");
    const bindings = await createControlledHostedBootstrapPrivateBindingsForTests(options, adapters);
    await expect(bindings.createCeremony({ projectId: "project", manifestHash: "9".repeat(64), canonicalRoot: f.canonicalRoot, privateDirectory: f.privateRoot, codexHome: f.codexHome,
      providerNetworkConsent: { approvedBy: "owner", approvalReference: "act-v2", approvedAt: "2026-09-10T00:00:00.000Z" } })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", details: { reason: "HOST_AUTHORITY_INVALID" } });
    expect(stagedBeforeAuthority).toEqual([]);
    expect(calls).toEqual([{ purpose: "login", projectId: "project", manifestHash: "9".repeat(64), canonicalRoot: f.canonicalRoot, consentDigest: expect.stringMatching(/^[a-f0-9]{64}$/) }]);
    await bindings.close?.(); await f.bindings.close?.();
  });
  it("binds ceremony, same admitted actor and materialized runtime, then closes the one host lease", async () => {
    const f = await fixture();
    const admission = await f.bindings.establishAdmission!({ projectId: "project", canonicalRoot: f.canonicalRoot, ceremony: f.ceremony, nativeAddonPath: join(f.root, "native.node") });
    expect(admission.continuity).toEqual(f.continuity);
    expect(f.events).toContain(`policy-roles-${"9".repeat(64)}`);
    expect(f.events).toContain(`launcher-roles-${"9".repeat(64)}`);
    const projects = { requireAuthorized: async () => ({ canonicalRoot: f.canonicalRoot }), roots: async () => ({ workingRoot: f.canonicalRoot, instructionRoot: f.instructionRoot }) } as unknown as ProjectRegistry;
    const nativePlanSink = { open: async () => {}, capture: async () => {}, close: async () => {} } satisfies DelegatedNativePlanSink;
    const materialized = await f.bindings.materializeAdmission!({ projectId: "project", canonicalRoot: f.canonicalRoot, admission,
      runtime: { projects, sessions: {} as SessionStore, nativePlanSink, attachmentStagingRoot: join(f.canonicalRoot, ".chirality", "attachments") } });
    expect("delegated" in materialized && materialized.selection).toEqual({ adapterId: "codex-app-server", providerId: "openai", model: "gpt-test" });
    // The v1 managed-auth path never reads a catalog, exposes none, and its configDigest recipe is byte-identical to the accepted v1 recipe.
    expect(materialized.catalog).toBeUndefined();
    expect(f.events).not.toContain("catalog-read");
    expect(f.events).toContain("admit-catalog-absent");
    expect(f.events).toContain(`launcher-config-${f.options.configDigest}`);
    expect(f.events).toContain(`admit-config-${f.options.configDigest}`);
    expect(f.lease.held).toBe(true);
    await f.bindings.close!(); await f.bindings.close!();
    expect(f.lease.held).toBe(false);
    expect(f.events.filter(value => value === "admission-retire")).toHaveLength(1);
    expect(f.events.indexOf("admission-retire")).toBeLessThan(f.events.indexOf("launcher-close"));
  });

  it("rejects a ceremony/root mismatch before candidate admission", async () => {
    const f = await fixture();
    await expect(f.bindings.establishAdmission!({ projectId: "other", canonicalRoot: f.canonicalRoot, ceremony: f.ceremony })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(f.events).toEqual(["roles-materialized"]);
    await f.bindings.close!();
  });

  it("requires completed supplier account observation", async () => {
    const f = await fixture(); f.setCeremonyState("pending");
    await expect(f.bindings.establishAdmission!({ projectId: "project", canonicalRoot: f.canonicalRoot, ceremony: f.ceremony })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(f.events).toEqual(["roles-materialized"]);
    await f.bindings.close!();
  });

  it("retires a successfully admitted actor when later private-store setup fails", async () => {
    const f = await fixture({ openStoreFails: true });
    await expect(f.bindings.establishAdmission!({ projectId: "project", canonicalRoot: f.canonicalRoot, ceremony: f.ceremony })).rejects.toThrow("store failed");
    expect(f.events).toContain("admission-retire");
    await f.bindings.close!();
  });

  it("durably fences and retires before supplier logout", async () => {
    const f = await fixture();
    await f.bindings.establishAdmission!({ projectId: "project", canonicalRoot: f.canonicalRoot, ceremony: f.ceremony });
    await f.bindings.signOut!({ projectId: "project", canonicalRoot: f.canonicalRoot, privateDirectory: f.privateRoot, codexHome: f.codexHome });
    expect(f.events.indexOf("fence-sign-out")).toBeLessThan(f.events.indexOf("admission-retire"));
    expect(f.events.indexOf("admission-retire")).toBeLessThan(f.events.indexOf("supplier-logout"));
    expect(f.events).toContain(`logout-digest-${"7".repeat(64)}`);
    expect(f.lease.held).toBe(true);
    await expect(f.bindings.signOut!({ projectId: "project", canonicalRoot: f.canonicalRoot, privateDirectory: f.privateRoot, codexHome: f.codexHome })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(f.events.filter(value => value === "supplier-logout")).toHaveLength(1);
    await f.bindings.close!(); expect(f.lease.held).toBe(false);
  });

  it("keeps local state fenced when supplier logout fails", async () => {
    const f = await fixture({ logoutFails: true });
    await f.bindings.establishAdmission!({ projectId: "project", canonicalRoot: f.canonicalRoot, ceremony: f.ceremony });
    await expect(f.bindings.signOut!({ projectId: "project", canonicalRoot: f.canonicalRoot, privateDirectory: f.privateRoot, codexHome: f.codexHome })).rejects.toThrow("logout failed");
    expect(f.events.slice(f.events.indexOf("fence-sign-out"), f.events.indexOf("supplier-logout") + 1)).toContain("admission-retire");
    expect(f.events.filter(value => value === "fence-sign-out")).toHaveLength(1);
    await f.bindings.close!(); expect(f.lease.held).toBe(false);
  });

  it("cleans the logout policy when launcher construction fails after local fencing", async () => {
    const f = await fixture({ logoutLauncherFails: true });
    await f.bindings.establishAdmission!({ projectId: "project", canonicalRoot: f.canonicalRoot, ceremony: f.ceremony });
    const before = f.events.filter(value => value === "policy-cleanup").length;
    await expect(f.bindings.signOut!({ projectId: "project", canonicalRoot: f.canonicalRoot, privateDirectory: f.privateRoot, codexHome: f.codexHome })).rejects.toThrow("logout launcher failed");
    expect(f.events.filter(value => value === "policy-cleanup")).toHaveLength(before + 1);
    await f.bindings.close!();
  });

  it("retires local admission and skips supplier logout when durable fencing fails", async () => {
    const f = await fixture({ fenceFails: true });
    await f.bindings.establishAdmission!({ projectId: "project", canonicalRoot: f.canonicalRoot, ceremony: f.ceremony });
    await expect(f.bindings.signOut!({ projectId: "project", canonicalRoot: f.canonicalRoot, privateDirectory: f.privateRoot, codexHome: f.codexHome })).rejects.toThrow("fence failed");
    expect(f.events).toContain("admission-retire");
    expect(f.events).not.toContain("supplier-logout");
    await f.bindings.close!();
  });

  it("connects public bootstrap through real same-actor admission to retained and fresh controlled candidates", async () => {
    const root = await realpath(await mkdtemp(join(await realpath("/tmp"), "hcp-"))); roots.push(root);
    const runtimeDirectory = join(root, "runtime"), projectRoot = join(root, "project"), packaged = await packagedInventoryFixture(root);
    const instructionRoot = packaged.instructionRoot;
    await mkdir(runtimeDirectory, { mode: 0o700 }); await mkdir(projectRoot);
    const lease = createFakeRuntimeAdmissionNativeAdapter().acquire(runtimeDirectory, "runtime-admission-authority.lock");
    const roleDigest = "9".repeat(64), policyDigest = "a".repeat(64), compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "c".repeat(64) };
    const rolePaths = Object.fromEntries(CHIRALITY_ROLE_NAMES.map(role => [role, join(runtimeDirectory, "roles", `${role}.toml`)]));
    const nativeRoles = { digest: roleDigest, configOverrides: ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2",
      ...CHIRALITY_ROLE_NAMES.flatMap(role => [`agents.${role}.description=${JSON.stringify(`Controlled ${role}`)}`, `agents.${role}.config_file=${JSON.stringify(rolePaths[role])}`])] };
    const runtimeReadRoot = { path: instructionRoot, readPaths: [instructionRoot], contentDigest: "4".repeat(64), artifactInventory: packaged.selection };
    const trace: string[] = [], secrets: Buffer[] = [], generations: Array<{ supplier: string; identity: string }> = [], conformanceActuals: Record<string, unknown>[] = [];
    const privateOptions: HostedPrivateCompositionOptions = {
      runtimeDirectory, supplierExecutablePath: join(root, "supplier"), nativeAddonPath: join(root, "native.node"), instructionRoot, model: "gpt-test",
      managedAuth: { backend: "keyring", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } }, compatibility,
      conformance: { recordPath: join(root, "record"), acceptancePath: join(root, "acceptance"), ownerActPath: join(root, "owner"), ownerActSha256: "d".repeat(64), activationId: "activation", gateIdentity: "G4", artifactInventory: packaged.selection },
      loginPurposeRelease: { recordPath: join(root, "login-record"), acceptancePath: join(root, "login-acceptance"), ownerActPath: join(root, "login-owner"), ownerActSha256: "5".repeat(64), activationId: "login-activation", gateIdentity: "D36", artifactInventory: packaged.selection },
      configDigest: "0".repeat(64), consentVersion: "consent-v1", commandNetworkPosture: "off", requestTimeoutMs: PACKAGED_REQUEST_TIMEOUT_MS, turnTimeoutMs: PACKAGED_TURN_TIMEOUT_MS, commandNetworkConsent: { approvedBy: "owner", approvedAt: "2026-09-10T00:00:00.000Z", explicitUserAct: true }, protectedPaths: [runtimeDirectory], immutableReadRoots: ["/usr"]
    };
    privateOptions.configDigest = recordKey({ schema: "chirality.hosted-private-config/v1", model: privateOptions.model, managedAuth: privateOptions.managedAuth, compatibility,
      commandNetworkPosture: "off", commandNetworkConsent: privateOptions.commandNetworkConsent, protectedPaths: privateOptions.protectedPaths, immutableReadRoots: privateOptions.immutableReadRoots, instructionRoot, nativeRoleConfigurationDigest: roleDigest, trustedRuntimeReadRoot: { contentDigest: runtimeReadRoot.contentDigest, readPaths: runtimeReadRoot.readPaths }, loginPurposeRelease: privateOptions.loginPurposeRelease, consentVersion: privateOptions.consentVersion });
    const adapters: ControlledHostedPrivateCompositionAdapters = {
      acquireLease: async () => lease, stageSupplier: async (_source, directory) => join(directory, "supplier", "codex"),
      prepareNativeRoles: async () => nativeRoles,
      bindRuntimeReadRoot: async () => runtimeReadRoot,
      validateLoginStartup: async () => ({ bindingDigest: "8".repeat(64), evidence: "externally-accepted-native-login-purpose", recordSha256: "6".repeat(64), ownerReference: "owner-act" }),
      createLogin: () => ({ async start() { return { loginId: "login", authUrl: "https://auth.openai.com/login" }; }, async status() { return { state: "completed", hasAccount: true }; }, async cancel() {}, async close() {} }),
      preparePolicy: async () => ({ policyDigest, async cleanup() {} }),
      createLauncherFactory: launcherOptions => createControlledCodexCandidateLauncherFactoryForTests(launcherOptions, { launchCandidate: async candidateInput => {
        const index = generations.length + 1, identity = { supplier: `supplier-${index}`, identity: `identity-${index}` }; generations.push(identity);
        const expectedPermissions = { filesystem: { [candidateInput.canonicalRoot]: "write" as const, [candidateInput.privateDirectory]: "deny" as const,
          [candidateInput.readOnlyProjectPaths![0]!]: "read" as const, [instructionRoot]: "read" as const }, network: { enabled: false } };
        return controlledAuthenticatedCandidate({ index, projectRoot: candidateInput.canonicalRoot, privateDirectory: candidateInput.privateDirectory,
          executablePath: candidateInput.executablePath, lease: candidateInput.kernelLease, policyDigest, expectedPermissions, nativeRoles, trace, secrets });
      } }),
      admitHosted: options => admitHostedControlledForTests(options, { verifyConformance: async ({ actual }) => { conformanceActuals.push(structuredClone(actual)); } }),
      logout: async () => {}, openBindingStore: HostedIdentityBindingStore.open
    };
    const bootstrapInput = { enabled: true as const, runtimeDirectory, daemonSocket: "runtime.sock", instructionRoot, nativeAddonPath: privateOptions.nativeAddonPath, artifactInventory: privateOptions.conformance.artifactInventory };
    const host = await startControlledHostedPrivateBootstrapRuntimeHostForTests({ bootstrap: bootstrapInput, privateComposition: privateOptions }, {
      createBindings: options => createControlledHostedBootstrapPrivateBindingsForTests(options, adapters),
      startHost: (boot, admittedBindings) => startControlledHostedBootstrapRuntimeHostForTests(boot, admittedBindings!)
    });
    try {
      const bootstrap = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
      const registered = await bootstrap.initializeHostedBootstrapProject({ projectRoot });
      await bootstrap.grantHostedProviderNetworkConsent(registered.projectId); await bootstrap.startHostedBootstrapLogin(registered.projectId);
      expect(await settledHostedBootstrapStatus(bootstrap, registered.projectId)).toMatchObject({ admission: "ready" });
      expect(generations).toEqual([{ supplier: "supplier-1", identity: "identity-1" }]);
      const client = new RuntimeClient({ socketPath: host.socketPath, tokenFile: resolveHostedProjectTokenFile(runtimeDirectory, registered.projectId) });
      const session = await client.createSession(registered.projectId, { projectId: registered.projectId, roleId: "HELP_HUMAN", permissionMode: "workspaceWrite" });
      const first = await drain(await client.turnSession(registered.projectId, session.sessionId, { message: "first" }));
      expect(generations).toHaveLength(1);
      const second = await drain(await client.turnSession(registered.projectId, session.sessionId, { message: "second" }));
      expect(first).toContainEqual(expect.objectContaining({ type: "chat:complete", data: expect.objectContaining({ text: "controlled-candidate-1" }) }));
      expect(second).toContainEqual(expect.objectContaining({ type: "chat:complete", data: expect.objectContaining({ text: "controlled-candidate-2" }) }));
      expect(generations).toEqual([{ supplier: "supplier-1", identity: "identity-1" }, { supplier: "supplier-2", identity: "identity-2" }]);
      expect(conformanceActuals).toHaveLength(2);
      expect(conformanceActuals[0]).toMatchObject({ accountEpoch: 1, accountDigest: expect.stringMatching(/^[a-f0-9]{64}$/), policyDigest });
      expect(conformanceActuals[1]).toMatchObject({ accountId: conformanceActuals[0]!.accountId, accountEpoch: 1, accountDigest: conformanceActuals[0]!.accountDigest, policyDigest });
      expect(trace.filter(value => value.startsWith("initialize-"))).toEqual(["initialize-1", "initialize-2"]);
      expect(trace).toEqual(expect.arrayContaining(["snapshot-1", "snapshot-2", "chirality/admissionAcquire-1", "chirality/admissionRelease-1", "chirality/admissionAcquire-2", "chirality/admissionRelease-2", "cleanup-1", "cleanup-2"]));
      expect(secrets).toHaveLength(2); expect(secrets.every(secret => secret.every(byte => byte === 0))).toBe(true);
    } finally { await host.stop(); }
  });
});
