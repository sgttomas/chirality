import { afterEach, describe, expect, it } from "vitest";
import { lstat, mkdir, mkdtemp, realpath, rm, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { startHostedRuntimeHost } from "../packages/daemon/src/hosted-boot.js";
import { createProjectFixture } from "./helpers.js";

const cleanup: string[] = [];
afterEach(async () => { for (const root of cleanup.splice(0)) await rm(root, { recursive: true, force: true }); });

describe("hosted runtime boot facade", () => {
  it("is default-off before a project is selected", async () => {
    await expect(startHostedRuntimeHost()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });

  it("rejects an unregistered selected project before creating either socket", async () => {
    const root = await realpath(await mkdtemp(join(tmpdir(), "hosted-boot-"))); cleanup.push(root);
    const runtimeDirectory = join(root, "runtime"); await mkdir(runtimeDirectory, { mode: 0o700 });
    const projectRoot = join(root, "project"); await createProjectFixture(projectRoot, "selected");
    const workerDirectory = join(runtimeDirectory, "worker"); await mkdir(workerDirectory, { mode: 0o700 });
    const executablePath = join(workerDirectory, "codex-fixture"); await writeFile(executablePath, "#!/bin/sh\nexit 1\n", { mode: 0o700 });
    const identity = { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "trusted-account", accountEpoch: 1, policyDigest: "trusted-policy" };
    const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "a".repeat(64) };
    const configPath = join(runtimeDirectory, "hosted.json");
    await writeFile(configPath, JSON.stringify({
      schema: "chirality-standalone-hosted/v2", mode: "hosted-validation", runtimeDirectory,
      daemonSocket: "daemon.sock", supervisorSocket: "supervisor.sock", supervisorCredential: "supervisor.json",
      supplierAuthority: { enabled: false },
      project: { projectId: "selected", identity, compatibility, codexHome: "worker/codex", retirementDirectory: "retirement" },
      worker: { executablePath, privateDirectory: "worker", model: "fixture", managedAuth: { backend: "keyring", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } }, providerNetworkConsent: { approvedBy: "fixture-owner", approvalReference: "explicit-test-consent" } }
    }), { mode: 0o600 });
    await expect(startHostedRuntimeHost({ enabled: true, configPath, nativeAddonPath: "/Applications/Chirality.app/Contents/Resources/native/chirality_native_admission.node", selectedProject: { projectId: "selected", canonicalRoot: projectRoot, identity, compatibility } })).rejects.toThrow();
    for (const socket of ["daemon.sock", "supervisor.sock"]) await expect(lstat(join(runtimeDirectory, socket))).rejects.toMatchObject({ code: "ENOENT" });
  });
});
