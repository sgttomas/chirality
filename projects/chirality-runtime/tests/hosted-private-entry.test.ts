import { describe, expect, it, vi } from "vitest";
import { chmod, link, mkdtemp, realpath, rm, symlink, writeFile } from "node:fs/promises";
import { join } from "node:path";
import type { HostedBootstrapPrivateBindings, HostedBootstrapRuntimeHost } from "../packages/daemon/src/hosted-bootstrap.js";
import { readHostedPrivateBootstrapConfiguration, startControlledHostedPrivateBootstrapRuntimeHostForTests, type HostedPrivateBootstrapHostInput } from "../packages/daemon/src/hosted-private-entry.js";

const inventory = { kind: "source-tree" as const, sourceRoot: "/runtime/source" };
const privateComposition = {
  runtimeDirectory: "/runtime", supplierExecutablePath: "/package/codex", nativeAddonPath: "/package/native.node", instructionRoot: "/runtime/instructions",
  model: "gpt-test", managedAuth: { backend: "keyring" as const, binding: { schema: "chirality-hosted-account-binding/v1" as const, state: "unavailable" as const, reason: "canonical-identity-producer-unavailable" as const } },
  compatibility: { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "a".repeat(64) },
  conformance: { recordPath: "/accept/record", acceptancePath: "/accept/acceptance", ownerActPath: "/accept/owner", ownerActSha256: "b".repeat(64), activationId: "activation", gateIdentity: "G4", artifactInventory: inventory },
  loginPurposeRelease: { recordPath: "/accept/login-record", acceptancePath: "/accept/login-acceptance", ownerActPath: "/accept/login-owner", ownerActSha256: "d".repeat(64), activationId: "login-activation", gateIdentity: "D36", artifactInventory: inventory },
  configDigest: "c".repeat(64), consentVersion: "consent-v1", commandNetworkPosture: "off" as const, commandNetworkConsent: { approvedBy: "owner", approvedAt: "2026-09-10T00:00:00.000Z", explicitUserAct: true as const }, protectedPaths: ["/runtime"], immutableReadRoots: ["/usr"]
};
const input: HostedPrivateBootstrapHostInput = { bootstrap: { enabled: true, runtimeDirectory: "/runtime", daemonSocket: "runtime.sock", instructionRoot: "/runtime/instructions", nativeAddonPath: "/package/native.node", artifactInventory: inventory }, privateComposition };
const host: HostedBootstrapRuntimeHost = { socketPath: "/runtime/runtime.sock", runtimeDirectory: "/runtime", bootstrapTokenFile: "/runtime/token", async stop() {} };

describe("hosted private production entry wiring", () => {
  it("starts an unbound bootstrap without creating private/native composition", async () => {
    const createBindings = vi.fn(); const startHost = vi.fn(async () => host);
    await expect(startControlledHostedPrivateBootstrapRuntimeHostForTests({ bootstrap: input.bootstrap }, { createBindings, startHost })).resolves.toBe(host);
    expect(createBindings).not.toHaveBeenCalled(); expect(startHost).toHaveBeenCalledWith(input.bootstrap);
  });

  it("constructs bindings internally after exact fieldwise host matching", async () => {
    const bindings: HostedBootstrapPrivateBindings = { async createCeremony() { throw new Error("unused"); } };
    const createBindings = vi.fn(async () => bindings), startHost = vi.fn(async () => host);
    await expect(startControlledHostedPrivateBootstrapRuntimeHostForTests(structuredClone(input), { createBindings, startHost })).resolves.toBe(host);
    expect(createBindings).toHaveBeenCalledWith(expect.objectContaining({ instructionRoot: "/runtime/instructions" }));
    expect(startHost).toHaveBeenCalledWith(expect.objectContaining({ artifactInventory: inventory }), bindings);
  });

  it("accepts reordered selector properties because equality is fieldwise", async () => {
    const bindings: HostedBootstrapPrivateBindings = { async createCeremony() { throw new Error("unused"); } };
    const reordered = { sourceRoot: "/runtime/source", kind: "source-tree" as const };
    const configured = { ...input, bootstrap: { ...input.bootstrap, artifactInventory: reordered }, privateComposition: { ...privateComposition, conformance: { ...privateComposition.conformance, artifactInventory: inventory } } };
    await expect(startControlledHostedPrivateBootstrapRuntimeHostForTests(configured, { createBindings: async () => bindings, startHost: async () => host })).resolves.toBe(host);
  });

  it("rejects mismatched inventory and closes constructed bindings on host startup failure", async () => {
    const close = vi.fn(async () => {}), bindings: HostedBootstrapPrivateBindings = { async createCeremony() { throw new Error("unused"); }, close };
    await expect(startControlledHostedPrivateBootstrapRuntimeHostForTests({ ...input, bootstrap: { ...input.bootstrap, artifactInventory: { kind: "source-tree", sourceRoot: "/other" } } }, { createBindings: async () => bindings, startHost: async () => host })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(close).not.toHaveBeenCalled();
    await expect(startControlledHostedPrivateBootstrapRuntimeHostForTests(input, { createBindings: async () => bindings, startHost: async () => { throw new Error("startup failed"); } })).rejects.toThrow("startup failed");
    expect(close).toHaveBeenCalledOnce();
  });

  it("reads only the strict owner-private carrier and binds the packaged basis", async () => {
    const directory = await mkdtemp(join(await realpath("/tmp"), "hpc-"));
    try {
      const file = join(directory, "private.json");
      await writeFile(file, JSON.stringify({ schema: "chirality.hosted-private-runtime/v1", privateComposition }), { mode: 0o600 });
      const read = await readHostedPrivateBootstrapConfiguration({ configFile: file, bootstrap: input.bootstrap,
        packaged: { supplierExecutablePath: privateComposition.supplierExecutablePath, nativeAddonPath: privateComposition.nativeAddonPath, instructionRoot: privateComposition.instructionRoot, artifactInventory: inventory } });
      expect(read.privateComposition?.model).toBe("gpt-test");
      await chmod(file, 0o644);
      await expect(readHostedPrivateBootstrapConfiguration({ configFile: file, bootstrap: input.bootstrap,
        packaged: { supplierExecutablePath: privateComposition.supplierExecutablePath, nativeAddonPath: privateComposition.nativeAddonPath, instructionRoot: privateComposition.instructionRoot, artifactInventory: inventory } })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      await chmod(file, 0o600);
      const linked = join(directory, "linked.json"); await link(file, linked);
      await expect(readHostedPrivateBootstrapConfiguration({ configFile: file, bootstrap: input.bootstrap,
        packaged: { supplierExecutablePath: privateComposition.supplierExecutablePath, nativeAddonPath: privateComposition.nativeAddonPath, instructionRoot: privateComposition.instructionRoot, artifactInventory: inventory } })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      await rm(linked);
      const alias = join(directory, "alias.json"); await symlink(file, alias);
      await expect(readHostedPrivateBootstrapConfiguration({ configFile: alias, bootstrap: input.bootstrap,
        packaged: { supplierExecutablePath: privateComposition.supplierExecutablePath, nativeAddonPath: privateComposition.nativeAddonPath, instructionRoot: privateComposition.instructionRoot, artifactInventory: inventory } })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    } finally { await rm(directory, { recursive: true, force: true }); }
  });

  it("returns unbound configuration without reading or loading private state", async () => {
    await expect(readHostedPrivateBootstrapConfiguration({ bootstrap: input.bootstrap,
      packaged: { supplierExecutablePath: "/missing", nativeAddonPath: "/missing", instructionRoot: "/missing", artifactInventory: inventory } })).resolves.toEqual({ bootstrap: input.bootstrap });
    await expect(readHostedPrivateBootstrapConfiguration({ configFile: "", bootstrap: input.bootstrap,
      packaged: { supplierExecutablePath: "/missing", nativeAddonPath: "/missing", instructionRoot: "/missing", artifactInventory: inventory } })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
});
