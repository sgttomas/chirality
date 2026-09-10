import { createHash } from "node:crypto";
import { chmod, mkdir, mkdtemp, readFile, readdir, realpath, rm, stat, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { PassThrough } from "node:stream";
import { afterEach, describe, expect, it, vi } from "vitest";

const state = vi.hoisted(() => ({ methods: [] as string[], invalidReadback: false, retired: 0, cleaned: 0,
  spawnedArguments: [] as string[], addonPath: "", proof: undefined as undefined | ((secret: Buffer, value: any) => string), contract: "", supplySha: "" }));

vi.mock("@chirality/native-admission", async importOriginal => {
  const actual = await importOriginal<typeof import("@chirality/native-admission")>();
  return { ...actual, loadNativeAdmissionBinding: (_required: boolean, addonPath: string) => { state.addonPath = addonPath; return ({ state: "available", value: { spawnGroupedSupplier(_program: string, args: readonly string[], secret: Buffer) {
    state.spawnedArguments = [...args];
    const stdin = new PassThrough(), stdout = new PassThrough(); let buffered = "";
    stdin.on("data", chunk => { buffered += String(chunk); for (;;) { const newline = buffered.indexOf("\n"); if (newline < 0) break; const raw = buffered.slice(0, newline); buffered = buffered.slice(newline + 1); const request = JSON.parse(raw); if (request.method) state.methods.push(request.method);
      if (request.method === "initialize") {
        const descriptor = { capability: "chirality.local-admission-authority", contract: state.contract, major: 1, minor: 0 }, v4Descriptor = { capability: "account.identity-snapshot", contract: "chirality-supplier-account-identity/1", major: 1, minor: 0, method: "account/identitySnapshot" };
        const input = { ...request.params.chiralityAdmissionAuthority, exactSupplyDigest: state.supplySha, authoritySecret: secret, descriptor, v4Descriptor };
        const result = { contract: state.contract, runtimeProcessIncarnationId: input.runtimeProcessIncarnationId, supplierGeneration: input.supplierGeneration, supplierChallenge: Buffer.alloc(32, 7).toString("base64url"), descriptor, v4Descriptor, proof: "" };
        result.proof = state.proof!(secret, { ...input, ...result }); stdout.write(`${JSON.stringify({ id: request.id, result: { chiralityAdmissionAuthority: result } })}\n`);
      } else if (request.method === "config/read") {
        const config = { sandbox_mode: "workspace-write", sandbox_workspace_write: { writable_roots: [stateRoot], network_access: false, exclude_slash_tmp: true, exclude_tmpdir_env_var: true }, approval_policy: "never", features: { plugins: false, shell_snapshot: false }, allow_login_shell: false,
          cli_auth_credentials_store: state.invalidReadback ? "file" : "keyring", check_for_update_on_startup: false, web_search: "disabled", analytics: { enabled: false }, feedback: { enabled: false }, chirality_runtime: { nativeSkills: "disabled" },
          hooks: null, mcp_servers: {}, notify: null, plugins: {}, profiles: {}, projects: null, profile: null };
        stdout.write(`${JSON.stringify({ id: request.id, result: { config } })}\n`);
      }
    } });
    return { state: "available", value: { pid: 9001, stdin, stdout, closeInput() {}, terminate() {}, kill() {}, async observeLeader() { return { exitCode: 0, signal: null }; }, async reapLeader() { return { exitCode: 0, signal: null }; }, groupRetired() { return true; } } };
  } } }); } };
});

let stateRoot = "";
vi.mock("../packages/daemon/src/codex-containment.js", async importOriginal => {
  const actual = await importOriginal<typeof import("../packages/daemon/src/codex-containment.js")>();
  return { ...actual, assertCodexKeyringHomeHasNoPlaintextCredentials: vi.fn(async () => {}), prepareCodexContainmentV2: vi.fn(async (input: any) => {
    stateRoot = input.canonicalRoot;
    const config = { sandbox_mode: "workspace-write", sandbox_workspace_write: { writable_roots: [input.canonicalRoot], network_access: false, exclude_slash_tmp: true, exclude_tmpdir_env_var: true }, approval_policy: "never", features: { plugins: false, shell_snapshot: false }, allow_login_shell: false,
      cli_auth_credentials_store: "keyring", check_for_update_on_startup: false, web_search: "disabled", analytics: { enabled: false }, feedback: { enabled: false } };
    return { config, outerPolicyDigest: "d".repeat(64), providerNetworkEnabled: true, commandNetworkBoundary: "configuration-only", environment: { HOME: input.privateDirectory, CODEX_HOME: input.codexHome, TMPDIR: join(input.privateDirectory, "scratch"), PATH: "/usr/bin:/bin:/usr/sbin:/sbin", LANG: "en_US.UTF-8" },
      sandboxProfilePath: join(input.privateDirectory, "launch.sb"), async launchArguments(path: string) { return ["-f", join(input.privateDirectory, "launch.sb"), path]; }, async cleanup() { state.cleaned++; } };
  }) };
});

vi.mock("../packages/daemon/src/codex-authenticated-transport.js", async importOriginal => {
  const actual = await importOriginal<typeof import("../packages/daemon/src/codex-authenticated-transport.js")>();
  return { ...actual, retireAuthenticatedSupplierGroup: vi.fn(async () => { state.retired++; return { leader: { exitCode: 0, signal: null }, groupRetired: true, signalFailures: [] }; }) };
});

import { initializationProof, AUTHORITY_CONTRACT } from "../packages/daemon/src/supplier-authority-controller.js";
import { observeCodexAccountFreeLoginPurposeV2, type AccountFreeLoginObservationInputV2 } from "../packages/daemon/src/account-free-login-observation.js";

const roots: string[] = [];
afterEach(async () => { state.methods = []; state.invalidReadback = false; state.retired = 0; state.cleaned = 0; state.spawnedArguments = []; state.addonPath = "";
  await Promise.all(roots.splice(0).map(path => rm(path, { recursive: true, force: true }))); });

async function fixture(): Promise<AccountFreeLoginObservationInputV2> {
  state.proof = initializationProof; state.contract = AUTHORITY_CONTRACT;
  const root = await mkdtemp(join(await realpath(tmpdir()), "account-free-observe-")); roots.push(root);
  const runtimeDirectory = join(root, "runtime"), resourcesPath = join(root, "candidate", "Resources"), evidenceDirectory = join(root, "evidence-inputs"),
    supplier = join(resourcesPath, "supplier"), executablePath = join(supplier, "codex"), nativeDirectory = join(resourcesPath, "native"), addonPath = join(nativeDirectory, "chirality_native_admission.node");
  for (const path of [runtimeDirectory, supplier, nativeDirectory, evidenceDirectory]) await mkdir(path, { recursive: true, mode: 0o700 });
  await writeFile(executablePath, "supplier", { mode: 0o700 }); await chmod(executablePath, 0o700); await writeFile(addonPath, "addon", { mode: 0o600 });
  const hash = (value: string) => createHash("sha256").update(value).digest("hex"), supplierHash = hash("supplier"), addonHash = hash("addon"); state.supplySha = supplierHash;
  const evidencePaths = { signatureEvidenceSha256: join(evidenceDirectory, "signature.md"), sourceCorrespondenceEvidenceSha256: join(evidenceDirectory, "source.md"), xpcRecordSha256: join(evidenceDirectory, "xpc.md"), groupedRecordSha256: join(evidenceDirectory, "grouped.md") };
  const evidenceBytes = { signatureEvidenceSha256: "signature evidence", sourceCorrespondenceEvidenceSha256: "source correspondence", xpcRecordSha256: "xpc record", groupedRecordSha256: "grouped record" };
  for (const field of Object.keys(evidencePaths) as Array<keyof typeof evidencePaths>) { await writeFile(evidencePaths[field], evidenceBytes[field], { mode: 0o600 }); await chmod(evidencePaths[field], 0o600); }
  return { runtimeDirectory, resourcesPath, evidencePaths, recipe: {
    schema: "chirality-account-free-login-observation-recipe/v1", runId: "11111111-1111-4111-8111-111111111111",
    supplyProfile: { schema: "chirality-custom-supplier-exact-profile/v1", executable: { relativePath: "supplier/codex", version: "1.0.0", sha256: supplierHash, size: 8 } },
    supplyClosure: [{ relativePath: "supplier", type: "directory" }, { relativePath: "supplier/codex", type: "file", sha256: supplierHash, size: 8, mode: "executable" }],
    nativeAddon: { sha256: addonHash, size: 5, ...Object.fromEntries(Object.entries(evidenceBytes).map(([field, value]) => [field, hash(value)])) } as any,
    providerNetworkConsent: { approvedBy: "owner", approvalReference: "trial" }, supportProfileDigest: "5".repeat(64), nativePolicyIdentityVersion: 11 } };
}

describe("account-free final-Supplier observation", () => {
  it("uses private initialization and one readback, emits eight distinct facts, and retires without account or model calls", async () => {
    const input = await fixture(), result = await observeCodexAccountFreeLoginPurposeV2(input);
    expect(state.methods).toEqual(["initialize", "initialized", "config/read"]); expect(state.retired).toBe(1); expect(state.cleaned).toBe(1);
    expect(Object.keys(result.limbs).sort()).toEqual(["bounded-protocol-purpose", "exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "provider-network", "retirement", "storage-isolation"]);
    expect(new Set(Object.values(result.limbs).map(value => value.evidenceSha256)).size).toBe(8);
    const outputDirectory = result.outputDirectory;
    expect((await readdir(outputDirectory)).sort()).toHaveLength(9); expect((await stat(join(outputDirectory, "observation.json"))).mode & 0o777).toBe(0o600);
    expect(state.addonPath).toBe(join(input.resourcesPath, "native", "chirality_native_admission.node"));
    expect(state.spawnedArguments).toContain(join(input.runtimeDirectory, "account-free-observations", input.recipe.runId, "private", "supplier", "codex"));
    const protocol = JSON.parse(await readFile(join(outputDirectory, "bounded-protocol-purpose.json"), "utf8"));
    expect(protocol.facts).toMatchObject({ privateInitialization: true, methods: ["initialize", "initialized", "config/read"], modelExecution: false });
    expect(JSON.stringify(protocol)).not.toContain("account/identitySnapshot");
  });

  it("rejects changed effective backend and still retires without publishing passing evidence", async () => {
    const input = await fixture(); state.invalidReadback = true;
    await expect(observeCodexAccountFreeLoginPurposeV2(input)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(state.methods).toEqual(["initialize", "initialized", "config/read"]); expect(state.retired).toBe(1); expect(state.cleaned).toBe(1);
    await expect(stat(join(input.runtimeDirectory, "account-free-observations", input.recipe.runId))).rejects.toMatchObject({ code: "ENOENT" });
  });

  it("rejects caller-selected paths hidden in the recipe before static inspection or native load", async () => {
    const input = await fixture(), hostile = { ...input, recipe: { ...input.recipe, nativeAddon: { ...input.recipe.nativeAddon, path: "/tmp/attacker.node" } } } as unknown as AccountFreeLoginObservationInputV2;
    await expect(observeCodexAccountFreeLoginPurposeV2(hostile)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", details: { reason: "OBSERVATION_INPUT_INVALID" } });
    expect(state.addonPath).toBe(""); expect(state.methods).toEqual([]);
  });

  it("rejects evidence bytes that differ from their recorded digest before native load", async () => {
    const input = await fixture(); await writeFile(input.evidencePaths.xpcRecordSha256, "changed evidence", { mode: 0o600 });
    await expect(observeCodexAccountFreeLoginPurposeV2(input)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(state.addonPath).toBe(""); expect(state.methods).toEqual([]);
  });
});
