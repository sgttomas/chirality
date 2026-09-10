import { PassThrough } from "node:stream";
import { chmod, mkdir, mkdtemp, readdir, realpath, rm, stat, symlink, writeFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it, vi } from "vitest";
import {
  launchControlledAuthenticatedCodexCandidateForTests,
  launchAuthenticatedCodexCandidate,
  codexEffectiveConfigDigestV2,
  authenticatedSupplierRetirementOutcome,
  assertOwnedCompiledPathV2,
  retireAuthenticatedSupplierGroup,
  type AuthenticatedCodexCandidateInput,
  type ControlledAuthenticatedCodexCandidateAdapters
} from "../packages/daemon/src/codex-authenticated-transport.js";
import { createCustomSupplyVerifier } from "../packages/core/src/exact-supply.js";
import { stageExactSupplierExecutable, stageExactSupplierExecutableControlledForTests } from "../packages/daemon/src/hosted-private-composition.js";
import { CodexLogin } from "../packages/daemon/src/codex-login.js";

const DIGEST = "a".repeat(64);

function fixture() {
  const events: string[] = [];
  const kernelLease = { held: true, device: 1n, inode: 2n, created: false, close: vi.fn() };
  const child = {
    pid: 4312,
    stdin: new PassThrough(), stdout: new PassThrough(),
    closeInput: vi.fn(), terminate: vi.fn(), kill: vi.fn(),
    observeLeader: vi.fn(async () => ({ exitCode: 0, signal: null })),
    reapLeader: vi.fn(async () => ({ exitCode: 0, signal: null })),
    groupRetired: vi.fn(() => true)
  };
  const input: AuthenticatedCodexCandidateInput = {
    canonicalRoot: "/project", privateDirectory: "/private/supplier", codexHome: "/private/supplier/home",
    executablePath: "/private/supplier/codex", nativeAddonPath: "/resources/native/chirality_native_admission.node",
    providerNetworkConsent: { approvedBy: "owner", approvalReference: "consent-1" }, commandNetworkPosture: "off",
    protectedPaths: ["/private/broker"], readOnlyProjectPaths: ["/project/.chirality/attachments"], immutableReadRoots: ["/usr"], trustedRuntimeReadRoots: [{ path: "/runtime/instruction-root", readPaths:["/runtime/instruction-root"], contentDigest: "e".repeat(64), artifactInventory: { kind: "packaged-resources" as const, resourcesRoot: "/runtime", manifestPath:"/runtime/runtime-artifact-inventory.json" } }],
    policyDigest: DIGEST, nativeRoleConfiguration: { digest: "d".repeat(64), configOverrides: ["agents.enabled=true"] }, toolRuntime: { codexSelfExecutablePath: "/private/supplier/codex" }, kernelLease
  };
  const outer = { cleanup: vi.fn(async () => { events.push("outer-cleanup"); }), sandboxProfilePath: "/private/supplier/outer.sb", launchArguments: vi.fn(async () => ["-f", "/private/supplier/outer.sb", "/private/supplier/codex"]), environment: { HOME: "/private/supplier", CODEX_HOME: "/private/supplier/home", TMPDIR: "/private/supplier/tmp", PATH: "/usr/bin:/bin:/usr/sbin:/sbin", LANG: "en_US.UTF-8" } };
  const toolPolicy = { cleanup: vi.fn(async () => { events.push("tool-cleanup"); }), scratchDirectory: "/project/.chirality-native-policy-fixture", policyDigest: DIGEST, permissionProfile: "chirality_policy", expectedPermissions: { filesystem: { "/project": "write" }, network: { enabled: false } }, nativeRoleConfiguration: input.nativeRoleConfiguration, configOverrides: ["cli_auth_credentials_store=\"keyring\""], args: ["-c", "cli_auth_credentials_store=\"keyring\""] };
  const spawnSupplier = vi.fn(() => ({ state: "available" as const, value: child }));
  const adapters: ControlledAuthenticatedCodexCandidateAdapters = {
    verifySupply: vi.fn(async () => ({ executablePath: input.executablePath, canonicalPath: input.executablePath, version: "0.149.0", sha256: "b".repeat(64), size: 42, signatureStatus: "accepted", evidenceClass: "accepted-supply" }) as never),
    revalidateSupply: vi.fn(async () => { events.push("revalidate"); }),
    prepareOuter: vi.fn(async () => outer as never), prepareToolPolicy: vi.fn(async () => toolPolicy as never), assertCompiledPathV2: vi.fn(async () => {}),
    assertNoPlaintext: vi.fn(async () => { events.push("plaintext-check"); }),
    openBindingStore: vi.fn(async () => ({}) as never),
    loadNative: vi.fn(() => ({ state: "available", value: { acquire: vi.fn(), spawnGroupedSupplier: spawnSupplier } }) as never),
    randomBytes: vi.fn(() => Buffer.alloc(32, 7)), randomUUID: vi.fn().mockReturnValueOnce("runtime-1").mockReturnValueOnce("supplier-1"),
    retire: vi.fn(async () => { events.push("retire"); }), createTracker: vi.fn(() => ({}) as never)
  };
  return { input, kernelLease, child, outer, toolPolicy, spawnSupplier, adapters, events };
}

describe("authenticated Codex candidate transport", () => {
  it("carries a complete custom exact closure through controlled staging and the real candidate verifier path without granting production acceptance", async () => {
    const root = await realpath(await mkdtemp(join(tmpdir(), "custom-supply-flow-")));
    try {
      const sourceRoot = join(root, "source", "supplier"), privateRoot = join(root, "private"), nested = join(sourceRoot, "nested");
      await mkdir(nested, { recursive: true }); await mkdir(privateRoot, { mode: 0o700 });
      const source = join(sourceRoot, "codex"), helper = join(sourceRoot, "runtime.dat"), data = join(nested, "config.dat");
      const executableBytes = Buffer.from("custom-supplier"), helperBytes = Buffer.from("closure-data"), dataBytes = Buffer.from("config-data");
      await writeFile(source, executableBytes, { mode: 0o700 }); await writeFile(helper, helperBytes, { mode: 0o700 }); await writeFile(data, dataBytes, { mode: 0o600 });
      const digest = (value: Buffer) => createHash("sha256").update(value).digest("hex");
      const verifier = createCustomSupplyVerifier({ schema: "chirality-custom-supplier-exact-profile/v1", executable: {
        relativePath: "supplier/codex", version: "custom-fixture", sha256: digest(executableBytes), size: executableBytes.length
      } }, [
        { relativePath: "supplier", type: "directory" },
        { relativePath: "supplier/codex", type: "file", sha256: digest(executableBytes), size: executableBytes.length, mode: "executable" },
        { relativePath: "supplier/nested", type: "directory" },
        { relativePath: "supplier/nested/config.dat", type: "file", sha256: digest(dataBytes), size: dataBytes.length, mode: "data" },
        { relativePath: "supplier/runtime.dat", type: "file", sha256: digest(helperBytes), size: helperBytes.length, mode: "executable" }
      ]);
      await expect(stageExactSupplierExecutable(source, privateRoot, verifier)).rejects.toMatchObject({ details: { reason: "PACKAGED_SUPPLY_VERIFIER_UNISSUED" } });
      expect(await readdir(privateRoot)).toEqual([]);
      const boundedRoot = join(root, "bounded"); await mkdir(boundedRoot, { mode: 0o700 });
      const undersizedVerifier = Object.freeze({ ...verifier, closureEntries: verifier.closureEntries.map(entry => entry.relativePath === "supplier/runtime.dat" && entry.type === "file" ? { ...entry, size: entry.size - 1 } : entry) });
      await expect(stageExactSupplierExecutableControlledForTests(source, boundedRoot, undersizedVerifier)).rejects.toMatchObject({ details: { reason: "PACKAGED_SUPPLIER_CHANGED" } });
      expect(await readdir(boundedRoot)).toEqual([]);
      const staged = await stageExactSupplierExecutableControlledForTests(source, privateRoot, verifier);
      expect((await stat(join(privateRoot, "supplier", "runtime.dat"))).mode & 0o777).toBe(0o700);
      expect((await stat(join(privateRoot, "supplier", "nested", "config.dat"))).mode & 0o777).toBe(0o600);
      const f = fixture();
      f.input = { ...f.input, executablePath: staged, toolRuntime: { codexSelfExecutablePath: staged }, supplyVerifier: verifier };
      expect(() => new CodexLogin({ executablePath: staged, canonicalRoot: root, privateDirectory: privateRoot, codexHome: join(privateRoot, "home"),
        providerNetworkConsent: { approvedBy: "fixture", approvalReference: "fixture" }, supplyVerifier: verifier })).toThrow();
      await expect(launchAuthenticatedCodexCandidate(f.input)).rejects.toMatchObject({ details: { reason: "PACKAGED_SUPPLY_VERIFIER_UNISSUED" } });
      f.adapters.assertSupplyVerifier = candidate => { if (candidate !== verifier) throw new Error("unexpected controlled verifier"); };
      const candidate = await launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters);
      expect(f.adapters.verifySupply).not.toHaveBeenCalled(); expect(f.adapters.revalidateSupply).not.toHaveBeenCalled(); expect(f.spawnSupplier).toHaveBeenCalledOnce();
      await candidate.cleanup();

      await writeFile(join(privateRoot, "supplier", "unlisted.dat"), "extra", { mode: 0o600 });
      await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      expect(f.spawnSupplier).toHaveBeenCalledOnce(); await rm(join(privateRoot, "supplier", "unlisted.dat"));
      await writeFile(join(privateRoot, "supplier", "runtime.dat"), Buffer.from("changed-data!"), { mode: 0o700 });
      await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      expect(f.spawnSupplier).toHaveBeenCalledOnce();
      await writeFile(join(privateRoot, "supplier", "runtime.dat"), helperBytes, { mode: 0o700 }); await chmod(join(privateRoot, "supplier", "runtime.dat"), 0o744);
      await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      expect(f.spawnSupplier).toHaveBeenCalledOnce();
      await chmod(join(privateRoot, "supplier", "runtime.dat"), 0o700); await chmod(join(privateRoot, "supplier", "nested", "config.dat"), 0o400);
      await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      expect(f.spawnSupplier).toHaveBeenCalledOnce();
      await chmod(join(privateRoot, "supplier", "nested", "config.dat"), 0o600); await chmod(join(privateRoot, "supplier"), 0o755);
      await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      expect(f.spawnSupplier).toHaveBeenCalledOnce();
    } finally { await rm(root, { recursive: true, force: true }); }
  });

  it("keeps semantic invocation identity stable while enforcing each fresh compiled path topology", async () => {
    const root = await realpath(await mkdtemp(join(await realpath(tmpdir()), "chirality-compiled-paths-")));
    try {
      const privateRoot = join(root, "private"), first = join(privateRoot, "containment-a"), second = join(privateRoot, "containment-b");
      await mkdir(privateRoot, { mode: 0o700 }); await mkdir(first, { mode: 0o700 }); await mkdir(second, { mode: 0o700 });
      const firstProfile = join(first, "launch.sb"), secondProfile = join(second, "launch.sb");
      await writeFile(firstProfile, "profile", { mode: 0o600 }); await writeFile(secondProfile, "profile", { mode: 0o600 });
      await assertOwnedCompiledPathV2(privateRoot, first, "directory"); await assertOwnedCompiledPathV2(first, firstProfile, "file");
      await assertOwnedCompiledPathV2(privateRoot, second, "directory"); await assertOwnedCompiledPathV2(second, secondProfile, "file");
      const semantic = { executablePath: join(privateRoot, "codex"), cwd: root, environment: { HOME: privateRoot, CODEX_HOME: join(privateRoot, "home"), PATH: "/usr/bin:/bin", LANG: "en_US.UTF-8" }, configOverrides: ["features.plugins=false"] };
      expect(codexEffectiveConfigDigestV2(semantic)).toBe(codexEffectiveConfigDigestV2({ ...semantic }));
      const alias = join(privateRoot, "profile-alias"); await symlink(firstProfile, alias);
      await expect(assertOwnedCompiledPathV2(privateRoot, alias, "file")).rejects.toThrow();
      await expect(assertOwnedCompiledPathV2(first, secondProfile, "file")).rejects.toThrow();
    } finally { await rm(root, { recursive: true, force: true }); }
  });

  it("spawns one nonexecuting raw candidate with exact outer argv, cwd, environment and fd3 bootstrap", async () => {
    const f = fixture();
    const candidate = await launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters);
    expect(candidate.pid).toBe(4312);
    expect(candidate.kernelLease).toBe(f.kernelLease);
    expect(candidate.expectedToolRuntime).toEqual({ codexSelfExecutablePath: f.input.executablePath, requiresSandboxedFileSystem: true, requiresSandboxedFileStreaming: true });
    expect(candidate.expectedPolicy.nativeRoleConfiguration).toEqual(f.input.nativeRoleConfiguration);
    expect(f.adapters.prepareToolPolicy).toHaveBeenCalledWith(expect.objectContaining({ nativeRoleConfiguration: f.input.nativeRoleConfiguration }));
    expect(f.adapters.prepareOuter).toHaveBeenCalledWith(expect.objectContaining({ trustedRuntimeReadRoots: f.input.trustedRuntimeReadRoots }));
    expect(f.adapters.prepareToolPolicy).toHaveBeenCalledWith(expect.objectContaining({ trustedRuntimeReadRoots: f.input.trustedRuntimeReadRoots }));
    expect(f.spawnSupplier).toHaveBeenCalledOnce();
    const [executable, args, secret, options] = f.spawnSupplier.mock.calls[0]!;
    expect(executable).toBe("/usr/bin/sandbox-exec");
    expect(args).toEqual(["-f", "/private/supplier/outer.sb", "/private/supplier/codex", "app-server", "-c", "cli_auth_credentials_store=\"keyring\""]);
    expect(secret).toEqual(Buffer.alloc(32, 7));
    expect(options).toEqual({ cwd: "/project", environment: f.outer.environment, processGroup: true });
    expect(f.events).toEqual(["plaintext-check", "revalidate", "plaintext-check", "plaintext-check"]);
    await candidate.cleanup();
    expect(f.events.slice(-3)).toEqual(["retire", "tool-cleanup", "outer-cleanup"]);
    expect(f.kernelLease.close).not.toHaveBeenCalled();
  });

  it("spawns native-11 with the compiler-owned skill selector before every config override", async () => {
    const f = fixture();
    f.input.nativePolicyIdentityVersion = 11;
    Object.assign(f.toolPolicy, { nativeSkills: "disabled", appServerArguments: ["app-server", "--chirality-disable-native-skills", ...f.toolPolicy.args] });
    const candidate = await launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters);
    expect(f.spawnSupplier.mock.calls[0]?.[1]).toEqual(["-f", "/private/supplier/outer.sb", "/private/supplier/codex", "app-server", "--chirality-disable-native-skills", "-c", "cli_auth_credentials_store=\"keyring\""]);
    expect(candidate.expectedPolicy.nativeSkills).toBe("disabled");
    await candidate.cleanup();
  });

  it("rejects a structural v2 candidate before compilation when existing instance admission is absent", async () => {
    const f = fixture(), outerPolicyDigest = "c".repeat(64);
    const runtimeReadRoot = { path: "/runtime/instruction-root", readPaths: ["/runtime/instruction-root"], contentDigest: "e".repeat(64), artifactInventory: {
      schema: "chirality-runtime-packaged-basis/v2" as const, resourcesRoot: "/runtime", inventoryPath: "/runtime/runtime-artifact-inventory-v2.json",
      payloadManifestPath: "/runtime/runtime-payload-manifest.json", outerInventorySha256: "f".repeat(64), payloadDigest: "1".repeat(64)
    } };
    const policyInstanceV2 = { schema: "chirality-codex-policy-instance/v2" as const, outerPurpose: "trusted-supplier" as const, nativePurpose: "worker" as const,
      canonicalRoot: f.input.canonicalRoot, privateDirectory: f.input.privateDirectory, codexHome: f.input.codexHome, executablePath: f.input.executablePath, nativeAddonPath: f.input.nativeAddonPath,
      providerNetworkConsent: f.input.providerNetworkConsent, commandNetworkPosture: f.input.commandNetworkPosture,
      immutableReadRoots: f.input.immutableReadRoots, protectedPaths: f.input.protectedPaths, readOnlyProjectPaths: f.input.readOnlyProjectPaths!, trustedRuntimeReadRoots: [runtimeReadRoot],
      toolRuntime: { codexSelfExecutablePath: f.input.executablePath, requiresSandboxedFileSystem: true as const, requiresSandboxedFileStreaming: true as const }, nativeRoleConfiguration: f.input.nativeRoleConfiguration! };
    const expectedEffectiveConfigDigestV2 = codexEffectiveConfigDigestV2({ executablePath: f.input.executablePath, cwd: f.input.canonicalRoot,
      environment: { HOME: f.outer.environment.HOME, CODEX_HOME: f.outer.environment.CODEX_HOME, PATH: f.outer.environment.PATH, LANG: f.outer.environment.LANG }, configOverrides: f.toolPolicy.configOverrides });
    f.input = { ...f.input, trustedRuntimeReadRoots: [runtimeReadRoot], policyInstanceV2, expectedEffectiveConfigDigestV2 };
    f.adapters.prepareOuterV2 = vi.fn(async () => ({ ...f.outer, outerPolicyDigest }) as never);
    f.adapters.prepareToolPolicyV2 = vi.fn(async () => ({ ...f.toolPolicy, policyInstance: policyInstanceV2, policyInstanceDigest: "2".repeat(64) }) as never);
    await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ details: { reason: "INSTANCE_ADMISSION_INVALID" } });
    f.input = { ...f.input, instanceInputV2: {} as never };
    await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ details: { reason: "INSTANCE_ADMISSION_INVALID" } });
    f.input = { ...f.input, instanceAdmissionV2: {} as never, instancePreparationV2: {} as never };
    await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ details: { reason: "INSTANCE_ADMISSION_INVALID" } });
    expect(f.spawnSupplier).not.toHaveBeenCalled();
    expect(f.adapters.prepareOuterV2).not.toHaveBeenCalled();
  });

  it("cleans prepared resources in reverse order when revalidation or post-spawn plaintext checks fail", async () => {
    const stale = fixture(); vi.mocked(stale.adapters.revalidateSupply).mockRejectedValue(new Error("stale"));
    await expect(launchControlledAuthenticatedCodexCandidateForTests(stale.input, stale.adapters)).rejects.toMatchObject({ details: { reason: "CANDIDATE_PREPARATION_FAILED" }, cause: expect.objectContaining({ message: "stale" }) });
    expect(stale.events.slice(-2)).toEqual(["tool-cleanup", "outer-cleanup"]); expect(stale.spawnSupplier).not.toHaveBeenCalled();

    const plaintext = fixture(); vi.mocked(plaintext.adapters.assertNoPlaintext).mockResolvedValueOnce(undefined).mockResolvedValueOnce(undefined).mockRejectedValueOnce(new Error("fallback"));
    await expect(launchControlledAuthenticatedCodexCandidateForTests(plaintext.input, plaintext.adapters)).rejects.toMatchObject({ details: { reason: "CANDIDATE_PREPARATION_FAILED" }, cause: expect.objectContaining({ message: "fallback" }) });
    expect(plaintext.events.slice(-3)).toEqual(["retire", "tool-cleanup", "outer-cleanup"]); expect(plaintext.kernelLease.close).not.toHaveBeenCalled();
  });

  it("rejects a development supplier before preparing any launch resources", async () => {
    const f = fixture(); vi.mocked(f.adapters.verifySupply).mockResolvedValue({ version: "0.0.0" } as never);
    await expect(launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters)).rejects.toMatchObject({ details: { reason: "DEVELOPMENT_SUPPLIER_BUILD" } });
    expect(f.adapters.prepareOuter).not.toHaveBeenCalled(); expect(f.adapters.loadNative).not.toHaveBeenCalled();
  });

  it("retains terminal signal diagnostics through the actual candidate cleanup owner", async () => {
    const f = fixture(), term = new Error("term EPERM"), kill = new Error("kill EPERM");
    const outcome = Object.freeze({ leader: Object.freeze({ exitCode: 0, signal: null }), groupRetired: true as const, signalFailures: Object.freeze([{ phase: "term" as const, cause: term }, { phase: "kill" as const, cause: kill }]) });
    vi.mocked(f.adapters.retire).mockResolvedValue(outcome);
    const candidate = await launchControlledAuthenticatedCodexCandidateForTests(f.input, f.adapters);
    expect(authenticatedSupplierRetirementOutcome(candidate)).toBeUndefined();
    await candidate.cleanup();
    expect(authenticatedSupplierRetirementOutcome(candidate)).toBe(outcome);
  });
});

describe("authenticated supplier group retirement", () => {
  it("signals the anchored group before reaping and then verifies group absence", async () => {
    const events: string[] = [];
    const child = { pid: 4312, stdin: new PassThrough(), stdout: new PassThrough(), closeInput: () => events.push("eof"), terminate: () => events.push("term"), kill: () => events.push("kill"), observeLeader: async () => { events.push("observe"); return { exitCode: 0, signal: null }; }, reapLeader: async () => { events.push("reap"); return { exitCode: 0, signal: null }; }, groupRetired: () => { events.push("group"); return true; } };
    const outcome = await retireAuthenticatedSupplierGroup(child, async phase => { events.push(`deadline:${phase}`); });
    expect(outcome).toEqual({ leader: { exitCode: 0, signal: null }, groupRetired: true, signalFailures: [] });
    expect(events).toEqual(["observe", "eof", "deadline:eof", "term", "deadline:term", "kill", "deadline:kill", "reap", "group"]);
  });

  it("reaps and verifies absence after failed pre-reap signals while retaining both diagnostics", async () => {
    const events: string[] = [], term = new Error("term EPERM"), kill = new Error("kill EPERM");
    const child = { pid: 4312, stdin: new PassThrough(), stdout: new PassThrough(), closeInput: () => events.push("eof"), terminate: () => { events.push("term"); throw term; }, kill: () => { events.push("kill"); throw kill; }, observeLeader: async () => { events.push("observe"); return { exitCode: 0, signal: null }; }, reapLeader: async () => { events.push("reap"); return { exitCode: 0, signal: null }; }, groupRetired: () => { events.push("group"); return true; } };
    const outcome = await retireAuthenticatedSupplierGroup(child, async phase => { events.push(`deadline:${phase}`); });
    expect(outcome.signalFailures).toEqual([{ phase: "term", cause: term }, { phase: "kill", cause: kill }]);
    expect(events).toEqual(["observe", "eof", "deadline:eof", "term", "deadline:term", "kill", "deadline:kill", "reap", "group"]);
  });

  it("does not inspect the group or signal again when exact reap fails", async () => {
    const events: string[] = [];
    const child = { pid: 4312, stdin: new PassThrough(), stdout: new PassThrough(), closeInput() {}, terminate: () => events.push("term"), kill: () => events.push("kill"), observeLeader: async () => ({ exitCode: 0, signal: null }), reapLeader: async () => { events.push("reap"); throw new Error("ECHILD"); }, groupRetired: () => { events.push("group"); return true; } };
    await expect(retireAuthenticatedSupplierGroup(child, async () => {})).rejects.toMatchObject({ details: { reason: "SUPPLIER_LEADER_REAP_FAILED" } });
    expect(events).toEqual(["term", "kill", "reap"]);
  });

  it("does not reap, inspect the group, or signal again after leader observation fails", async () => {
    const events: string[] = [], term = new Error("term EPERM"), kill = new Error("kill EPERM"), observe = new Error("waitid failed");
    const child = { pid: 4312, stdin: new PassThrough(), stdout: new PassThrough(), closeInput() {}, terminate: () => { events.push("term"); throw term; }, kill: () => { events.push("kill"); throw kill; }, observeLeader: async () => { throw observe; }, reapLeader: async () => { events.push("reap"); return { exitCode: 0, signal: null }; }, groupRetired: () => { events.push("group"); return true; } };
    const failure = await retireAuthenticatedSupplierGroup(child, async () => {}).catch(error => error);
    expect(failure).toMatchObject({ details: { reason: "SUPPLIER_LEADER_OBSERVATION_FAILED", signalFailures: ["term", "kill"] }, cause: expect.any(AggregateError) });
    expect((failure.cause as AggregateError).errors).toEqual([term, kill, observe]);
    expect(events).toEqual(["term", "kill"]);
  });

  it("fails closed without signaling after reap when a resistant group remains", async () => {
    const events: string[] = [], denied = new Error("EPERM");
    const child = { pid: 4312, stdin: new PassThrough(), stdout: new PassThrough(), closeInput() {}, terminate: () => events.push("term"), kill: () => { events.push("kill"); throw denied; }, observeLeader: async () => ({ exitCode: null, signal: 15 }), reapLeader: async () => { events.push("reap"); return { exitCode: null, signal: 15 }; }, groupRetired: () => false };
    const failure = await retireAuthenticatedSupplierGroup(child, async () => {}).catch(error => error);
    expect(failure).toMatchObject({ details: { reason: "SUPPLIER_GROUP_RETIREMENT_UNVERIFIED", signalFailures: ["kill"] }, cause: expect.any(AggregateError) });
    expect((failure.cause as AggregateError).errors).toEqual([denied]);
    expect(events).toEqual(["term", "kill", "reap"]);
  });
});
