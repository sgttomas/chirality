import { PassThrough } from "node:stream";
import { describe, expect, it, vi } from "vitest";
import {
  launchControlledAuthenticatedCodexCandidateForTests,
  authenticatedSupplierRetirementOutcome,
  retireAuthenticatedSupplierGroup,
  type AuthenticatedCodexCandidateInput,
  type ControlledAuthenticatedCodexCandidateAdapters
} from "../packages/daemon/src/codex-authenticated-transport.js";

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
  const outer = { cleanup: vi.fn(async () => { events.push("outer-cleanup"); }), launchArguments: vi.fn(async () => ["-f", "/private/supplier/outer.sb", "/private/supplier/codex"]), environment: { HOME: "/private/supplier", CODEX_HOME: "/private/supplier/home", TMPDIR: "/private/supplier/tmp", PATH: "/usr/bin:/bin:/usr/sbin:/sbin", LANG: "en_US.UTF-8" } };
  const toolPolicy = { cleanup: vi.fn(async () => { events.push("tool-cleanup"); }), policyDigest: DIGEST, permissionProfile: "chirality_policy", expectedPermissions: { filesystem: { "/project": "write" }, network: { enabled: false } }, nativeRoleConfiguration: input.nativeRoleConfiguration, args: ["-c", "cli_auth_credentials_store=\"keyring\""] };
  const spawnSupplier = vi.fn(() => ({ state: "available" as const, value: child }));
  const adapters: ControlledAuthenticatedCodexCandidateAdapters = {
    verifySupply: vi.fn(async () => ({ executablePath: input.executablePath, canonicalPath: input.executablePath, version: "0.149.0", sha256: "b".repeat(64), size: 42, signatureStatus: "accepted", evidenceClass: "accepted-supply" }) as never),
    revalidateSupply: vi.fn(async () => { events.push("revalidate"); }),
    prepareOuter: vi.fn(async () => outer as never), prepareToolPolicy: vi.fn(async () => toolPolicy as never),
    assertNoPlaintext: vi.fn(async () => { events.push("plaintext-check"); }),
    openBindingStore: vi.fn(async () => ({}) as never),
    loadNative: vi.fn(() => ({ state: "available", value: { acquire: vi.fn(), spawnGroupedSupplier: spawnSupplier } }) as never),
    randomBytes: vi.fn(() => Buffer.alloc(32, 7)), randomUUID: vi.fn().mockReturnValueOnce("runtime-1").mockReturnValueOnce("supplier-1"),
    retire: vi.fn(async () => { events.push("retire"); }), createTracker: vi.fn(() => ({}) as never)
  };
  return { input, kernelLease, child, outer, toolPolicy, spawnSupplier, adapters, events };
}

describe("authenticated Codex candidate transport", () => {
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
