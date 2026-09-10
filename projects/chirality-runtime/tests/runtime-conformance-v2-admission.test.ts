import { createHash } from "node:crypto";
import { appendFile, mkdtemp, realpath, rm, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { describe, expect, it, vi } from "vitest";
import { REQUIRED_RUNTIME_CONFORMANCE_LIMBS, runtimePolicyParameterSchemaDigestV2, type RuntimeSupportProfileV2 } from "../packages/core/src/index.js";
import { digestCodexPolicyInstanceV2, inspectCodexPolicyInstanceV2, inspectRuntimePurposeAcceptanceV2, inspectRuntimePurposeReleaseV2, revalidateRuntimePurposeReleaseV2, verifyRuntimePurposeReleaseV2 } from "../packages/daemon/src/runtime-conformance-v2-admission.js";
import { compileCodexNativePolicyProjectionV2, prepareCodexNativePolicyV2 } from "../packages/daemon/src/codex-containment.js";

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
    expect(inspectRuntimePurposeReleaseV2({ purpose: "login", record, expected: { payloadDigest, supportProfile: profile }, now: Date.parse("2026-09-10T12:00:00.000Z") })).toEqual({ sourceDigest });
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
