import { describe, expect, it, vi } from "vitest";
import { PassThrough } from "node:stream";
import {
  createControlledCodexCandidateLauncherFactoryForTests,
  createControlledCodexCandidateLauncherForTests,
  type CodexCandidateLauncherOptions
} from "../packages/daemon/src/codex-admitted-launcher.js";
import type { AuthenticatedCodexCandidate } from "../packages/daemon/src/codex-authenticated-transport.js";

const DIGEST = "a".repeat(64);

function fixture(overrides: Partial<CodexCandidateLauncherOptions> = {}) {
  const kernelLease = { held: true, device: 1n, inode: 2n, created: false, close: vi.fn() };
  const options: CodexCandidateLauncherOptions = {
    bindings: {
      canonicalRoot: "/project",
      privateDirectory: "/private/supplier",
      codexHome: "/private/supplier/home",
      executablePath: "/private/supplier/codex",
      nativeAddonPath: "/resources/native/chirality_native_admission.node",
      model: "gpt-5.6-sol",
      providerNetworkConsent: { approvedBy: "owner", approvalReference: "consent-1" },
      commandNetworkPosture: "off",
      protectedPaths: ["/private/broker"],
      readOnlyProjectPaths: ["/project/.chirality/attachments"],
      immutableReadRoots: ["/usr"],
      trustedRuntimeReadRoots: [{ path: "/runtime/instruction-root", readPaths:["/runtime/instruction-root"], contentDigest: "e".repeat(64), artifactInventory: { kind: "packaged-resources" as const, resourcesRoot: "/runtime", manifestPath:"/runtime/runtime-artifact-inventory.json" } }],
      policyDigest: DIGEST,
      configDigest: "c".repeat(64),
      consentVersion: "consent-v1",
      toolRuntime: { codexSelfExecutablePath: "/private/supplier/codex" }
    },
    kernelLease,
    ...overrides
  };
  const cleanup = vi.fn(async () => {});
  const authoritySecret = Buffer.alloc(32, 7);
  const candidate = {
    pid: 4312,
    cleanup,
    transport: { stdin: new PassThrough(), stdout: new PassThrough(), close: cleanup },
    authorityInitialize: { authoritySecret }
  } as unknown as AuthenticatedCodexCandidate;
  const launchCandidate = vi.fn(async () => candidate);
  return { options, kernelLease, candidate, cleanup, authoritySecret, launchCandidate };
}

describe("Codex supplier candidate launcher", () => {
  it("passes one immutable binding snapshot and a borrowed held lease to the candidate transport", async () => {
    const f = fixture();
    const launcher = createControlledCodexCandidateLauncherForTests(f.options, { launchCandidate: f.launchCandidate });
    await expect(launcher.launchCandidate()).resolves.toMatchObject({ pid: f.candidate.pid });
    const observed = f.launchCandidate.mock.calls[0]![0];
    expect(observed.kernelLease).toBe(f.kernelLease);
    expect(observed).toMatchObject(f.options.bindings);
    expect(Object.isFrozen(observed.toolRuntime)).toBe(true);
    expect(Object.isFrozen(observed.trustedRuntimeReadRoots?.[0])).toBe(true);
    expect(f.kernelLease.close).not.toHaveBeenCalled();
  });

  it("is single-candidate and joins candidate cleanup without closing the borrowed lease", async () => {
    const f = fixture();
    const launcher = createControlledCodexCandidateLauncherForTests(f.options, { launchCandidate: f.launchCandidate });
    await launcher.launchCandidate();
    await expect(launcher.launchCandidate()).rejects.toMatchObject({ details: { reason: "CANDIDATE_ALREADY_LAUNCHED" } });
    await launcher.close?.();
    expect(f.cleanup).toHaveBeenCalledOnce();
    expect(f.authoritySecret).toEqual(Buffer.alloc(32));
    expect(f.kernelLease.close).not.toHaveBeenCalled();
  });

  it("requires a fresh launcher after a failed candidate attempt", async () => {
    const f = fixture();
    f.launchCandidate.mockRejectedValueOnce(new Error("spawn failed"));
    const launcher = createControlledCodexCandidateLauncherForTests(f.options, { launchCandidate: f.launchCandidate });
    await expect(launcher.launchCandidate()).rejects.toThrow("spawn failed");
    await expect(launcher.launchCandidate()).rejects.toMatchObject({ details: { reason: "CANDIDATE_ALREADY_LAUNCHED" } });
    expect(f.launchCandidate).toHaveBeenCalledOnce();
  });

  it("creates a fresh single-use launcher for each process and closes every created launcher", async () => {
    const f = fixture();
    const factory = createControlledCodexCandidateLauncherFactoryForTests(f.options, { launchCandidate: f.launchCandidate });
    const first = factory.create(), second = factory.create();
    await first.launchCandidate(); await second.launchCandidate();
    expect(f.launchCandidate).toHaveBeenCalledTimes(2);
    await factory.close?.();
    expect(f.cleanup).toHaveBeenCalledTimes(2);
    expect(f.kernelLease.close).not.toHaveBeenCalled();
    expect(() => factory.create()).toThrow(expect.objectContaining({ details: { reason: "LAUNCHER_FACTORY_CLOSED" } }));
  });

  it("settles a long sequence of completed and failed candidates without retaining them for factory close", async () => {
    const f = fixture();
    const cleanups: Array<ReturnType<typeof vi.fn>> = [];
    const secrets: Buffer[] = [];
    let sequence = 0;
    const launchCandidate = vi.fn(async () => {
      sequence++;
      if (sequence % 7 === 0) throw new Error(`failed-${sequence}`);
      const cleanup = vi.fn(async () => {}), authoritySecret = Buffer.alloc(32, sequence);
      cleanups.push(cleanup); secrets.push(authoritySecret);
      return { pid: 5000 + sequence, cleanup, transport: { stdin: new PassThrough(), stdout: new PassThrough(), close: cleanup }, authorityInitialize: { authoritySecret } } as unknown as AuthenticatedCodexCandidate;
    });
    const factory = createControlledCodexCandidateLauncherFactoryForTests(f.options, { launchCandidate });
    for (let index = 1; index <= 70; index++) {
      const launched = factory.create().launchCandidate();
      if (index % 7 === 0) await expect(launched).rejects.toThrow(`failed-${index}`);
      else await (await launched).cleanup();
    }
    await factory.close?.();
    expect(launchCandidate).toHaveBeenCalledTimes(70);
    expect(cleanups).toHaveLength(60);
    for (const cleanup of cleanups) expect(cleanup).toHaveBeenCalledOnce();
    for (const secret of secrets) expect(secret).toEqual(Buffer.alloc(32));
    expect(f.kernelLease.close).not.toHaveBeenCalled();
  });

  it("factory close joins an in-flight candidate start and retires it exactly once", async () => {
    const f = fixture();
    let resolveLaunch!: (candidate: AuthenticatedCodexCandidate) => void;
    const pending = new Promise<AuthenticatedCodexCandidate>(resolve => { resolveLaunch = resolve; });
    const factory = createControlledCodexCandidateLauncherFactoryForTests(f.options, { launchCandidate: vi.fn(() => pending) });
    const launch = factory.create().launchCandidate();
    const closing = factory.close?.();
    await Promise.resolve();
    expect(f.cleanup).not.toHaveBeenCalled();
    resolveLaunch(f.candidate);
    await expect(launch).resolves.toMatchObject({ pid: f.candidate.pid });
    await closing;
    expect(f.cleanup).toHaveBeenCalledOnce();
    expect(f.authoritySecret).toEqual(Buffer.alloc(32));
    expect(f.kernelLease.close).not.toHaveBeenCalled();
  });

  it("rejects an unheld lease, tool runtime drift, and roots outside the private boundary before launch", () => {
    const unheld = fixture(); unheld.options.kernelLease = { ...unheld.kernelLease, held: false };
    expect(() => createControlledCodexCandidateLauncherForTests(unheld.options, { launchCandidate: unheld.launchCandidate })).toThrow(expect.objectContaining({ details: { reason: "LAUNCHER_CONFIGURATION_INVALID" } }));
    const runtime = fixture(); runtime.options.bindings.toolRuntime = { codexSelfExecutablePath: "/private/supplier/other" };
    expect(() => createControlledCodexCandidateLauncherForTests(runtime.options, { launchCandidate: runtime.launchCandidate })).toThrow(expect.objectContaining({ details: { reason: "TOOL_RUNTIME_BINDING_MISMATCH" } }));
    const root = fixture(); root.options.bindings.executablePath = "/other/codex"; root.options.bindings.toolRuntime = { codexSelfExecutablePath: "/other/codex" };
    expect(() => createControlledCodexCandidateLauncherForTests(root.options, { launchCandidate: root.launchCandidate })).toThrow(expect.objectContaining({ details: { reason: "PRIVATE_ROOT_BINDING_INVALID" } }));
  });
});
