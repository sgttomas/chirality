import { createHash } from "node:crypto";
import { appendFile, mkdtemp, realpath, rm, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { describe, expect, it, vi } from "vitest";
import { REQUIRED_RUNTIME_CONFORMANCE_LIMBS, runtimePolicyParameterSchemaDigestV2, type RuntimeSupportProfileV2 } from "../packages/core/src/index.js";
import { prepareRuntimeWorkerInstanceV2FromP2, completeRuntimeWorkerInstanceV2FromP2, revalidateRuntimeInstanceAdmissionV2, revalidateRuntimeWorkerInstancePreparationV2, digestCodexPolicyInstanceV2, inspectCodexPolicyInstanceV2, inspectRuntimePurposeAcceptanceV2, inspectRuntimePurposeReleaseV2, revalidateRuntimePurposeReleaseV2, verifyRuntimePurposeReleaseV2 } from "../packages/daemon/src/runtime-conformance-v2-admission.js";
import { compileCodexNativePolicyProjectionV2, prepareCodexNativePolicyV2 } from "../packages/daemon/src/codex-containment.js";
import { HostAccountAuthority } from "../packages/daemon/src/host-account-authority.js";
import { CodexSupervisor } from "../packages/daemon/src/codex-supervisor.js";
import { createControlledCodexCandidateLauncherFactoryForTests } from "../packages/daemon/src/codex-admitted-launcher.js";

vi.mock("../packages/daemon/src/hosted-packaged-release-state.js", async importOriginal => ({
  ...await importOriginal<typeof import("../packages/daemon/src/hosted-packaged-release-state.js")>(),
  revalidateIssuedPackagedReleaseBasisV2: async () => undefined
}));

const hash = (value: string) => createHash("sha256").update(value).digest("hex");
const limbs = (names: readonly string[]) => Object.fromEntries(names.map(name => [name, { attempted: true, passed: true, evidenceSha256: hash(name) }]));
function supportProfile(): RuntimeSupportProfileV2 {
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

describe("D36 v2 shared purpose inspection", () => {
  it("accepts only the exact account-free login record and externally anchored acceptance pair", () => {
    const profile = supportProfile(), payloadDigest = hash("payload"), sourceDigest = hash("source"), recordSha256 = hash("record"), ownerActSha256 = hash("owner");
    const record = { schema: "chirality-codex-login-purpose-release/v2", evidenceClass: "exact-account-free-login-purpose-observed", sourceDigest, payloadDigest,
      supportProfileDigests: [profile.profileDigest], policyContractDigest: runtimePolicyParameterSchemaDigestV2(), supplyProfileDigest: hash(`${JSON.stringify(profile.supplier)}\n`),
      backend: { credentialStore: "keyring", plaintextFallback: false }, methods: ["account/login/start", "account/login/cancel", "account/read", "model/list"], modelExecution: false,
      issuedAt: "2026-09-10T00:00:00.000Z", expiresAt: "2026-09-11T00:00:00.000Z",
      limbs: limbs(["exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "storage-isolation", "provider-network", "bounded-protocol-purpose", "retirement"]) };
    expect(inspectRuntimePurposeReleaseV2({ purpose: "login", record, expected: { payloadDigest, supportProfile: profile }, now: Date.parse("2026-09-10T12:00:00.000Z") })).toEqual({ sourceDigest, disposition: "qualified" });
    const acceptance = { schema: "chirality-runtime-conformance-acceptance/v1", status: "accepted", recordSha256, sourceDigest, activationId: "release-2", gateIdentity: "D36", ownerActSha256, ownerReference: "owner-act", expiresAt: "2026-09-11T00:00:00.000Z" };
    expect(inspectRuntimePurposeAcceptanceV2({ purpose: "login", acceptance, expected: { recordSha256, sourceDigest, ownerActSha256, activationId: "release-2", gateIdentity: "D36" }, now: Date.parse("2026-09-10T12:00:00.000Z") })).toEqual({ ownerReference: "owner-act" });
    expect(() => inspectRuntimePurposeAcceptanceV2({ purpose: "login", acceptance, expected: { recordSha256, sourceDigest, ownerActSha256, activationId: "other", gateIdentity: "D36" }, now: Date.parse("2026-09-10T12:00:00.000Z") })).toThrow();
  });

  it("reopens the held-size-bounded private files and rejects a changed accepted release", async () => {
    const directory = await realpath(await mkdtemp(join(await realpath(tmpdir()), "chirality-v2-release-")));
    try {
      const profile = supportProfile(), payloadDigest = hash("payload"), sourceDigest = hash("source");
      const record = { schema: "chirality-codex-login-purpose-release/v2", evidenceClass: "exact-account-free-login-purpose-observed", sourceDigest, payloadDigest,
        supportProfileDigests: [profile.profileDigest], policyContractDigest: runtimePolicyParameterSchemaDigestV2(), supplyProfileDigest: hash(`${JSON.stringify(profile.supplier)}\n`),
        backend: { credentialStore: "keyring", plaintextFallback: false }, methods: ["account/login/start", "account/login/cancel", "account/read", "model/list"], modelExecution: false,
        issuedAt: "2020-01-01T00:00:00.000Z", expiresAt: "2099-01-01T00:00:00.000Z",
        limbs: limbs(["exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "storage-isolation", "provider-network", "bounded-protocol-purpose", "retirement"]) };
      const recordBytes = `${JSON.stringify(record)}\n`, ownerBytes = "owner act\n";
      const acceptance = { schema: "chirality-runtime-conformance-acceptance/v1", status: "accepted", recordSha256: hash(recordBytes), sourceDigest,
        activationId: "release-2", gateIdentity: "D36", ownerActSha256: hash(ownerBytes), ownerReference: "owner-act", expiresAt: "2099-01-01T00:00:00.000Z" };
      const acceptanceBytes = `${JSON.stringify(acceptance)}\n`;
      const recordPath = join(directory, "record.json"), acceptancePath = join(directory, "acceptance.json"), ownerActPath = join(directory, "owner.md");
      await Promise.all([writeFile(recordPath, recordBytes, { mode: 0o600 }), writeFile(acceptancePath, acceptanceBytes, { mode: 0o600 }), writeFile(ownerActPath, ownerBytes, { mode: 0o600 })]);
      const purpose = { recordPath, recordSha256: hash(recordBytes), acceptancePath, acceptanceSha256: hash(acceptanceBytes), ownerActPath,
        ownerActSha256: hash(ownerBytes), activationId: "release-2", gateIdentity: "D36" };
      const basis = { schema: "chirality-hosted-packaged-release-basis/v2" as const, verified: { payloadDigest }, supportProfile: profile, login: purpose } as any;
      const admission = await verifyRuntimePurposeReleaseV2(basis, "login");
      await appendFile(recordPath, " ");
      await expect(revalidateRuntimePurposeReleaseV2(basis, admission)).rejects.toThrow();
    } finally { await rm(directory, { recursive: true, force: true }); }
  });

  it("rejects unsorted/duplicate profiles, incomplete worker limbs, and arbitrary login gates", () => {
    const profile = supportProfile(), payloadDigest = hash("payload"), sourceDigest = hash("source");
    const worker = { schema: "chirality-codex-worker-purpose-release/v2", evidenceClass: "exact-worker-purpose-observed", sourceDigest, payloadDigest,
      supportProfileDigests: [profile.profileDigest, profile.profileDigest], policyContractDigest: runtimePolicyParameterSchemaDigestV2(), supplyProfileDigest: hash(`${JSON.stringify(profile.supplier)}\n`),
      issuedAt: "2026-09-10T00:00:00.000Z", expiresAt: "2026-09-11T00:00:00.000Z", limbs: limbs(REQUIRED_RUNTIME_CONFORMANCE_LIMBS) };
    expect(() => inspectRuntimePurposeReleaseV2({ purpose: "worker", record: worker, expected: { payloadDigest, supportProfile: profile }, now: Date.parse("2026-09-10T12:00:00.000Z") })).toThrow();
    const missingLimb = { ...worker, supportProfileDigests: [profile.profileDigest], limbs: limbs(REQUIRED_RUNTIME_CONFORMANCE_LIMBS.slice(1)) };
    expect(() => inspectRuntimePurposeReleaseV2({ purpose: "worker", record: missingLimb, expected: { payloadDigest, supportProfile: profile }, now: Date.parse("2026-09-10T12:00:00.000Z") })).toThrow();
    const acceptance = { schema: "chirality-runtime-conformance-acceptance/v1", status: "accepted", recordSha256: hash("record"), sourceDigest, activationId: "release-2", gateIdentity: "not-d36", ownerActSha256: hash("owner"), ownerReference: "owner", expiresAt: "2026-09-11T00:00:00.000Z" };
    expect(() => inspectRuntimePurposeAcceptanceV2({ purpose: "login", acceptance, expected: { recordSha256: acceptance.recordSha256, sourceDigest, ownerActSha256: acceptance.ownerActSha256, activationId: "release-2", gateIdentity: "not-d36" }, now: Date.parse("2026-09-10T12:00:00.000Z") })).toThrow();
  });
});

describe("D36 v2 policy instance", () => {
  const compilerInput = () => ({ purpose: "worker" as const, canonicalRoot: "/project", privateDirectory: "/broker/private", codexHome: "/broker/private/home",
    executablePath: "/broker/private/supplier/codex", nativeAddonPath: "/runtime/native/addon.node", providerNetworkConsent: { approvedBy: "owner", approvalReference: "act" }, commandNetworkPosture: "off" as const,
    immutableReadRoots: ["/System", "/usr"], protectedPaths: ["/broker", "/broker/release-authority", "/broker/release-basis"], readOnlyProjectPaths: ["/project/.chirality/attachments"],
    trustedRuntimeReadRoots: [{ path: "/runtime/instruction-root", readPaths: ["/runtime/instruction-root"], contentDigest: hash("instructions"), artifactInventory: { schema: "chirality-runtime-packaged-basis/v2" as const,
      resourcesRoot: "/runtime", inventoryPath: "/runtime/runtime-artifact-inventory-v2.json", payloadManifestPath: "/runtime/runtime-payload-manifest.json", outerInventorySha256: hash("inventory"), payloadDigest: hash("payload") } }],
    nativeRoleConfiguration: null as never, toolRuntime: { codexSelfExecutablePath: "/broker/private/supplier/codex", requiresSandboxedFileSystem: true as const, requiresSandboxedFileStreaming: true as const } });

  it("rejects non-UTF-8-canonical compiler collections before filesystem effects", async () => {
    await expect(prepareCodexNativePolicyV2({ ...compilerInput(), protectedPaths: ["/broker/release-basis", "/broker"] })).rejects.toThrow("canonically ordered");
  });

  it("rejects a mismatched compiler tool capability before filesystem effects", async () => {
    const input = compilerInput();
    await expect(prepareCodexNativePolicyV2({ ...input, toolRuntime: { ...input.toolRuntime, codexSelfExecutablePath: "/other/codex" } })).rejects.toThrow("not exact");
  });

  it("projects the verified instruction root into one consistent native-10 profile", () => {
    const input = compilerInput(), roles = ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"];
    const nativeRoleConfiguration = { digest: hash("roles"), configOverrides: ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2",
      ...roles.flatMap(role => [`agents.${role}.description=${JSON.stringify(role)}`, `agents.${role}.config_file=${JSON.stringify(`/broker/private/native-roles/${role}.toml`)}`])] };
    const policy = { schema: "chirality-codex-policy-instance/v2" as const, outerPurpose: "trusted-supplier" as const, nativePurpose: "worker" as const,
      canonicalRoot: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome, executablePath: input.executablePath, nativeAddonPath: input.nativeAddonPath,
      providerNetworkConsent: input.providerNetworkConsent, commandNetworkPosture: input.commandNetworkPosture, immutableReadRoots: input.immutableReadRoots,
      protectedPaths: input.protectedPaths, readOnlyProjectPaths: input.readOnlyProjectPaths, trustedRuntimeReadRoots: input.trustedRuntimeReadRoots, toolRuntime: input.toolRuntime, nativeRoleConfiguration };
    const base = { immutableFiles: [{ path: "/usr/bin/tool", sha256: hash("tool"), size: 4 }] as never,
      expectedPermissions: { filesystem: { "/broker/private": "deny" as const, "/project": "write" as const }, network: { enabled: false } }, approvalPolicy: "never" as const,
      configOverrides: ["permissions={\"legacy\"={}}", "approval_policy=\"never\""] };
    const compiled = compileCodexNativePolicyProjectionV2(policy, base);
    expect(compiled.expectedPermissions.filesystem).toEqual({ "/broker/private": "deny", "/project": "write", "/runtime/instruction-root": "read" });
    expect(compiled.profileId).toBe(`chirality_${compiled.policyDigest.slice(0, 24)}`);
    expect(compiled.permissionProfile).toBe(compiled.profileId);
    expect(compiled.configOverrides.filter(value => value.startsWith("permissions="))).toEqual([expect.stringContaining(JSON.stringify(compiled.profileId))]);
    expect(compiled.args).toEqual(compiled.configOverrides.flatMap(value => ["-c", value]));
    expect(compiled.policyDigest).toBe(hash(`${JSON.stringify({ version: 10, policyInstance: compiled.policyInstance, immutableFiles: base.immutableFiles,
      expectedPermissions: compiled.expectedPermissions, approvalPolicy: base.approvalPolicy })}\n`));
  });

  it("accepts the closed login shape and rejects an account-like native projection", () => {
    const login = { schema: "chirality-codex-policy-instance/v2" as const, outerPurpose: "trusted-login" as const, nativePurpose: null,
      canonicalRoot: "/project", privateDirectory: "/broker/project-private", codexHome: "/broker/project-private/codex-home", executablePath: "/broker/project-private/supplier/codex", nativeAddonPath: "/resources/native/chirality_native_admission.node",
      providerNetworkConsent: { approvedBy: "owner", approvalReference: "consent" }, commandNetworkPosture: "off" as const,
      immutableReadRoots: [], protectedPaths: [], readOnlyProjectPaths: [], trustedRuntimeReadRoots: [],
      toolRuntime: { codexSelfExecutablePath: "/broker/project-private/supplier/codex", requiresSandboxedFileSystem: true as const, requiresSandboxedFileStreaming: true as const }, nativeRoleConfiguration: null };
    expect(digestCodexPolicyInstanceV2(login)).toMatch(/^[a-f0-9]{64}$/);
    expect(() => inspectCodexPolicyInstanceV2({ ...login, nativePurpose: "worker" })).toThrow();
  });

  it("binds one packaged instruction root, attachment restriction, and exact four-role order", () => {
    const root = "/project", executablePath = "/broker/project-private/supplier/codex";
    const roles = ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"];
    const configOverrides = ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2", ...roles.flatMap(role => [`agents.${role}.description=${JSON.stringify(role)}`, `agents.${role}.config_file=${JSON.stringify(`/broker/project-private/native-roles/${role}.toml`)}`])];
    const worker = { schema: "chirality-codex-policy-instance/v2" as const, outerPurpose: "trusted-supplier" as const, nativePurpose: "worker" as const,
      canonicalRoot: root, privateDirectory: "/broker/project-private", codexHome: "/broker/project-private/codex-home", executablePath, nativeAddonPath: "/resources/native/chirality_native_admission.node",
      providerNetworkConsent: { approvedBy: "owner", approvalReference: "consent" }, commandNetworkPosture: "off" as const,
      immutableReadRoots: ["/System", "/usr"], protectedPaths: ["/broker", "/broker/release-authority", "/broker/release-basis"], readOnlyProjectPaths: ["/project/.chirality/attachments"],
      trustedRuntimeReadRoots: [{ path: "/resources/instruction-root", readPaths: ["/resources/instruction-root"], contentDigest: hash("instructions"), artifactInventory: { schema: "chirality-runtime-packaged-basis/v2" as const, resourcesRoot: "/resources", inventoryPath: "/resources/runtime-artifact-inventory-v2.json", payloadManifestPath: "/resources/runtime-payload-manifest.json", outerInventorySha256: hash("inventory"), payloadDigest: hash("payload") } }],
      toolRuntime: { codexSelfExecutablePath: executablePath, requiresSandboxedFileSystem: true as const, requiresSandboxedFileStreaming: true as const }, nativeRoleConfiguration: { digest: hash("roles"), configOverrides } };
    expect(inspectCodexPolicyInstanceV2(worker)).toEqual(worker);
    expect(() => inspectCodexPolicyInstanceV2({ ...worker, protectedPaths: [...worker.protectedPaths].reverse() })).toThrow();
    expect(() => inspectCodexPolicyInstanceV2({ ...worker, nativeRoleConfiguration: { ...worker.nativeRoleConfiguration, configOverrides: [...configOverrides].reverse() } })).toThrow();
  });
});

// The release file verifier and nominal issuer are real; only the packaged
// filesystem/seal boundary is mocked above. No supplier/native execution.

// Host lease renewal after a desktop relaunch. The release file verifier, the
// P2 issuers, the launcher factory and the supervisor renewal path are real;
// the host authority is a synthetic in-memory lease carrier (no XPC, journal,
// credentials or supplier process) and the candidate launch stops before any
// supplier execution.
describe("D36 v2 host lease renewal", () => {
  const ROLES = ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"];
  async function fixture() {
    const directory = await realpath(await mkdtemp(join(await realpath(tmpdir()), "chirality-host-renewal-")));
    const profile = supportProfile(), payloadDigest = hash("payload"), sourceDigest = hash("source");
    const record = { schema: "chirality-codex-worker-purpose-release/v2", evidenceClass: "exact-worker-purpose-observed", sourceDigest, payloadDigest,
      supportProfileDigests: [profile.profileDigest], policyContractDigest: runtimePolicyParameterSchemaDigestV2(), supplyProfileDigest: hash(`${JSON.stringify(profile.supplier)}\n`),
      issuedAt: "2020-01-01T00:00:00.000Z", expiresAt: "2099-01-01T00:00:00.000Z", limbs: limbs(REQUIRED_RUNTIME_CONFORMANCE_LIMBS) };
    const recordBytes = `${JSON.stringify(record)}\n`, ownerBytes = "owner act\n";
    const acceptance = { schema: "chirality-runtime-conformance-acceptance/v1", status: "accepted", recordSha256: hash(recordBytes), sourceDigest,
      activationId: "release-2", gateIdentity: "D36", ownerActSha256: hash(ownerBytes), ownerReference: "owner-act", expiresAt: "2099-01-01T00:00:00.000Z" };
    const acceptanceBytes = `${JSON.stringify(acceptance)}\n`;
    const purpose = { recordPath: join(directory, "record.json"), recordSha256: hash(recordBytes), acceptancePath: join(directory, "acceptance.json"), acceptanceSha256: hash(acceptanceBytes),
      ownerActPath: join(directory, "owner.md"), ownerActSha256: hash(ownerBytes), activationId: "release-2", gateIdentity: "D36" };
    await Promise.all([writeFile(purpose.recordPath, recordBytes, { mode: 0o600 }), writeFile(purpose.acceptancePath, acceptanceBytes, { mode: 0o600 }), writeFile(purpose.ownerActPath, ownerBytes, { mode: 0o600 })]);
    const basis = { schema: "chirality-hosted-packaged-release-basis/v2" as const, verified: { payloadDigest }, supportProfile: profile, worker: purpose } as any;
    const purposeRelease = await verifyRuntimePurposeReleaseV2(basis, "worker");
    // Synthetic lease carrier: only the fields the admission bridge reads.
    const source = Object.create(HostAccountAuthority.prototype) as any;
    source.generation = "controlled-daemon-generation"; source.closing = false;
    const connect = (host: string) => { source.active = { clientId: `host-${host}`, connectionId: `connection-${host}`, revoked: false }; };
    const disconnect = () => { source.active.revoked = true; };
    connect("A");
    const privateDirectory = "/broker/private", codexHome = "/broker/private/home", executablePath = "/broker/private/codex";
    const roles = { digest: hash("roles"), configOverrides: ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2",
      ...ROLES.flatMap(role => [`agents.${role}.description=${JSON.stringify(role)}`, `agents.${role}.config_file=${JSON.stringify(`${privateDirectory}/native-roles/${role}.toml`)}`])] };
    const readRoot = { path: "/resources/instruction-root", readPaths: ["/resources/instruction-root"], contentDigest: hash("instructions") };
    const policy = { schema: "chirality-codex-policy-instance/v2" as const, outerPurpose: "trusted-supplier" as const, nativePurpose: "worker" as const,
      canonicalRoot: "/project", privateDirectory, codexHome, executablePath, nativeAddonPath: "/resources/native/chirality_native_admission.node",
      providerNetworkConsent: { approvedBy: "owner", approvalReference: "consent" }, commandNetworkPosture: "off" as const,
      immutableReadRoots: ["/System", "/usr"], protectedPaths: ["/broker"], readOnlyProjectPaths: ["/project/.chirality/attachments"],
      trustedRuntimeReadRoots: [{ ...readRoot, artifactInventory: { schema: "chirality-runtime-packaged-basis/v2" as const, resourcesRoot: "/resources", inventoryPath: "/resources/runtime-artifact-inventory-v2.json",
        payloadManifestPath: "/resources/runtime-payload-manifest.json", outerInventorySha256: hash("inventory"), payloadDigest } }],
      toolRuntime: { codexSelfExecutablePath: executablePath, requiresSandboxedFileSystem: true as const, requiresSandboxedFileStreaming: true as const }, nativeRoleConfiguration: roles };
    const input = { purposeRelease, projectId: "project", manifestHash: hash("manifest"), canonicalRoot: "/project", cwd: "/project", privateDirectory, codexHome, brokerRoot: "/broker",
      instructionRoot: readRoot.path, nativeAddonPath: policy.nativeAddonPath, supplierExecutablePath: executablePath, attachmentRoot: "/project/.chirality/attachments",
      consent: { version: hash("consent-version"), digest: hash("consent"), authenticatedExplicitUserAct: true as const }, policy, outerPolicyDigest: hash("outer"), nativePolicyDigest: hash("native"), effectiveConfigDigest: hash("config") } as any;
    const preparation = await prepareRuntimeWorkerInstanceV2FromP2(source, basis, input);
    const account = { accountId: "account", accountEpoch: 1, accountDigest: hash("account") };
    const initial = await completeRuntimeWorkerInstanceV2FromP2(preparation, account);
    const launches: any[] = [];
    const factory = createControlledCodexCandidateLauncherFactoryForTests({ kernelLease: { held: true, device: 1n, inode: 2n, created: false, close() {} } as any,
      bindings: { canonicalRoot: "/project", privateDirectory, codexHome, executablePath, nativeAddonPath: policy.nativeAddonPath, model: "fixture-model", providerNetworkConsent: policy.providerNetworkConsent,
        commandNetworkPosture: "off", protectedPaths: policy.protectedPaths, readOnlyProjectPaths: policy.readOnlyProjectPaths, immutableReadRoots: policy.immutableReadRoots,
        trustedRuntimeReadRoots: [{ ...readRoot, artifactInventory: { kind: "packaged-resources", resourcesRoot: "/resources", manifestPath: "/resources/runtime-artifact-inventory-v2.json" } }],
        policyDigest: input.nativePolicyDigest, configDigest: hash("config"), consentVersion: "consent", toolRuntime: { codexSelfExecutablePath: executablePath }, nativeRoleConfiguration: roles,
        policyInstanceV2: policy, expectedEffectiveConfigDigestV2: input.effectiveConfigDigest, instancePreparationV2: preparation, nativePolicyIdentityVersion: 10 } as any },
      { async launchCandidate(value) { await revalidateRuntimeWorkerInstancePreparationV2(value.instancePreparationV2!); launches.push(value); throw new Error("controlled-stop-before-supplier"); } });
    const supervisor = Object.create(CodexSupervisor.prototype) as any;
    Object.assign(supervisor, { conformance: { runtimeV2: { releaseBasis: basis, ...initial } }, candidateLauncherFactory: factory, entries: new Map(), acquiring: new Set(), closed: false });
    const cleanup = async () => { await factory.close?.(); await rm(directory, { recursive: true, force: true }); };
    return { basis, source, connect, disconnect, input, preparation, account, initial, launches, factory, supervisor, cleanup };
  }
  const notLive = { details: { reason: "HOST_AUTHORITY_NOT_LIVE" } };

  it("renews an idle supervisor and its future launcher from the fresh verified host while the replaced host's admission stays invalid", async () => {
    const f = await fixture();
    try {
      const current = f.supervisor.conformance.runtimeV2;
      await expect(f.supervisor.refreshHostAdmission()).resolves.toBe(current);
      expect(f.supervisor.conformance.runtimeV2).toBe(current);
      f.disconnect();
      await expect(revalidateRuntimeInstanceAdmissionV2(f.initial.instanceInput, f.initial.instanceAdmission)).rejects.toMatchObject(notLive);
      await expect(f.supervisor.refreshHostAdmission()).rejects.toThrow("Account host lease is unavailable");
      expect(f.supervisor.conformance.runtimeV2).toBe(current);
      const retired: string[] = [];
      f.supervisor.preadmitted = { authority: { close: async () => { retired.push("authority"); } }, session: { close: async () => { retired.push("session"); } }, candidate: { cleanup: async () => { retired.push("candidate"); } } };
      f.connect("B");
      const renewed = await f.supervisor.refreshHostAdmission();
      expect(retired).toEqual(["authority", "session", "candidate"]);
      expect(f.supervisor.preadmitted).toBeUndefined();
      expect(renewed).toBe(f.supervisor.conformance.runtimeV2);
      expect(renewed).not.toBe(current);
      expect(renewed.releaseBasis).toBe(f.basis);
      expect(renewed.instanceInput.account).toEqual(f.account);
      expect(renewed.instanceInput.hostAuthority.liveLeaseDigest).not.toBe(f.initial.instanceInput.hostAuthority.liveLeaseDigest);
      expect(renewed.instanceInput.hostAuthority.daemonGeneration).toBe(f.initial.instanceInput.hostAuthority.daemonGeneration);
      await revalidateRuntimeInstanceAdmissionV2(renewed.instanceInput, renewed.instanceAdmission);
      await expect(revalidateRuntimeInstanceAdmissionV2(f.initial.instanceInput, f.initial.instanceAdmission)).rejects.toMatchObject(notLive);
      await expect(revalidateRuntimeWorkerInstancePreparationV2(f.preparation)).rejects.toThrow();
      await expect(f.factory.create().launchCandidate()).rejects.toThrow("controlled-stop-before-supplier");
      expect(f.launches).toHaveLength(1);
      expect(f.launches[0].instancePreparationV2.lease).toEqual(f.source.snapshotAdmissionLease());
      expect(f.launches[0].instancePreparationV2.lease).not.toEqual(f.preparation.lease);
      await expect(f.supervisor.refreshHostAdmission()).resolves.toBe(renewed);
    } finally { await f.cleanup(); }
  });

  it("refuses renewal while work is active, after retirement, or with an outstanding launcher, and joins concurrent renewals", async () => {
    const f = await fixture();
    try {
      const current = f.supervisor.conformance.runtimeV2;
      f.connect("B");
      f.supervisor.entries.set("worker", {});
      await expect(f.supervisor.refreshHostAdmission()).rejects.toThrow("while work is active");
      f.supervisor.entries.clear(); f.supervisor.acquiring.add("worker");
      await expect(f.supervisor.refreshHostAdmission()).rejects.toThrow("while work is active");
      f.supervisor.acquiring.clear();
      const outstanding = f.factory.create();
      await expect(f.supervisor.refreshHostAdmission()).rejects.toMatchObject({ details: { reason: "LAUNCHER_FACTORY_NOT_IDLE" } });
      await outstanding.close?.();
      expect(f.supervisor.conformance.runtimeV2).toBe(current);
      f.supervisor.closed = true;
      await expect(f.supervisor.refreshHostAdmission()).rejects.toThrow("after retirement");
      f.supervisor.closed = false;
      const [first, second] = await Promise.all([f.supervisor.refreshHostAdmission(), f.supervisor.refreshHostAdmission()]);
      expect(first).toBe(second);
      expect(first).not.toBe(current);
      expect(f.supervisor.hostAdmissionRefresh).toBeUndefined();
      await revalidateRuntimeInstanceAdmissionV2(first.instanceInput, first.instanceAdmission);
      f.supervisor.closed = true;
      await expect(f.supervisor.refreshHostAdmission()).resolves.toBe(first);
    } finally { await f.cleanup(); }
  });

  it("rejects a renewal whose account or policy subject differs and keeps the superseded admission unrenewed", async () => {
    const f = await fixture();
    try {
      const current = f.supervisor.conformance.runtimeV2, realFactory = f.supervisor.candidateLauncherFactory;
      f.connect("B");
      const issue = (input: any, account: any) => ({ async refreshHostAdmission() { return completeRuntimeWorkerInstanceV2FromP2(await prepareRuntimeWorkerInstanceV2FromP2(f.source, f.basis, input), account); } });
      f.supervisor.candidateLauncherFactory = issue(f.input, { ...f.account, accountEpoch: 2 });
      await expect(f.supervisor.refreshHostAdmission()).rejects.toThrow("changed its subject or policy");
      f.supervisor.candidateLauncherFactory = issue({ ...f.input, consent: { ...f.input.consent, digest: hash("other-consent") } }, f.account);
      await expect(f.supervisor.refreshHostAdmission()).rejects.toThrow("changed its subject or policy");
      expect(f.supervisor.conformance.runtimeV2).toBe(current);
      await expect(revalidateRuntimeInstanceAdmissionV2(current.instanceInput, current.instanceAdmission)).rejects.toMatchObject(notLive);
      f.supervisor.candidateLauncherFactory = realFactory;
      const renewed = await f.supervisor.refreshHostAdmission();
      expect(renewed).not.toBe(current);
      await revalidateRuntimeInstanceAdmissionV2(renewed.instanceInput, renewed.instanceAdmission);
    } finally { await f.cleanup(); }
  });

  it("keeps the superseded admission unrenewed when the host disconnects during renewal, then renews on the next verified host", async () => {
    const f = await fixture();
    try {
      const current = f.supervisor.conformance.runtimeV2;
      f.connect("B");
      // The first successful lease match (preparation) revokes the host before completion rechecks it.
      let armed = true;
      f.source.matchesAdmissionLease = function (this: any, snapshot: unknown) {
        const matched = HostAccountAuthority.prototype.matchesAdmissionLease.call(this, snapshot as never);
        if (matched && armed) { armed = false; this.active.revoked = true; }
        return matched;
      };
      await expect(f.supervisor.refreshHostAdmission()).rejects.toMatchObject({ details: { reason: "WORKER_PREPARATION_INVALID" } });
      delete f.source.matchesAdmissionLease;
      expect(f.supervisor.conformance.runtimeV2).toBe(current);
      await expect(f.supervisor.refreshHostAdmission()).rejects.toThrow("Account host lease is unavailable");
      f.connect("C");
      const renewed = await f.supervisor.refreshHostAdmission();
      expect(renewed).not.toBe(current);
      await revalidateRuntimeInstanceAdmissionV2(renewed.instanceInput, renewed.instanceAdmission);
      await expect(f.factory.create().launchCandidate()).rejects.toThrow("controlled-stop-before-supplier");
      expect(f.launches[0].instancePreparationV2.lease).toEqual(f.source.snapshotAdmissionLease());
    } finally { await f.cleanup(); }
  });

  it("refuses renewal once the accepted release is no longer current", async () => {
    const f = await fixture();
    try {
      const current = f.supervisor.conformance.runtimeV2;
      f.connect("B");
      const now = vi.spyOn(Date, "now").mockReturnValue(Date.parse("2100-01-01T00:00:00.000Z"));
      try { await expect(f.supervisor.refreshHostAdmission()).rejects.toMatchObject({ details: { reason: "PURPOSE_RELEASE_STALE" } }); } finally { now.mockRestore(); }
      expect(f.supervisor.conformance.runtimeV2).toBe(current);
      await expect(revalidateRuntimeInstanceAdmissionV2(current.instanceInput, current.instanceAdmission)).rejects.toMatchObject(notLive);
    } finally { await f.cleanup(); }
  });

  it("blocks renewal while a queued-candidate retirement step fails, retries that step first, and never calls the factory before retirement completes", async () => {
    const f = await fixture();
    try {
      const current = f.supervisor.conformance.runtimeV2, realFactory = f.supervisor.candidateLauncherFactory;
      let factoryCalls = 0;
      f.supervisor.candidateLauncherFactory = { async refreshHostAdmission(account: any) { factoryCalls += 1; return realFactory.refreshHostAdmission!(account); } };
      f.connect("B");
      const retired: string[] = [];
      let authorityFailures = 1;
      f.supervisor.preadmitted = { authority: { close: async () => { retired.push("authority"); if (authorityFailures-- > 0) throw new Error("authority-close-failed"); } },
        session: { close: async () => { retired.push("session"); } }, candidate: { cleanup: async () => { retired.push("candidate"); } } };
      await expect(f.supervisor.refreshHostAdmission()).rejects.toThrow("authority-close-failed");
      expect(retired).toEqual(["authority", "session", "candidate"]);
      expect(f.supervisor.preadmitted).toBeUndefined();
      expect(f.supervisor.queuedRetirement).toHaveLength(1);
      expect(factoryCalls).toBe(0);
      expect(f.supervisor.conformance.runtimeV2).toBe(current);
      const renewed = await f.supervisor.refreshHostAdmission();
      expect(retired).toEqual(["authority", "session", "candidate", "authority"]);
      expect(f.supervisor.queuedRetirement).toBeUndefined();
      expect(factoryCalls).toBe(1);
      expect(renewed).not.toBe(current);
      await revalidateRuntimeInstanceAdmissionV2(renewed.instanceInput, renewed.instanceAdmission);
    } finally { await f.cleanup(); }
  });
});
