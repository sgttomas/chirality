import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { chmod, mkdir, mkdtemp, realpath, rename, rm, symlink, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createHash } from "node:crypto";
import { ACCEPTED_SUPPLY, createControlledSupplyVerifierForTests, createCustomSupplyVerifier, revalidateExactSupply, verifyExactSupply, type VerifiedSupply } from "../packages/core/src/exact-supply.js";

let directory: string;
let executablePath: string;
const bytes = Buffer.from("controlled fixture bytes, not a vendor executable\n");
const profile = { sha256: createHash("sha256").update(bytes).digest("hex"), size: bytes.length, version: "fixture-only" };
beforeEach(async () => { directory = await realpath(await mkdtemp(join(tmpdir(), "exact-supply-"))); executablePath = join(directory, "fixture"); await writeFile(executablePath, bytes); });
afterEach(async () => { await rm(directory, { recursive: true, force: true }); });

describe("exact accepted supply boundary", () => {
  it("preserves the accepted identity and unresolved invalid signature finding", () => {
    expect(ACCEPTED_SUPPLY).toMatchObject({ version: "0.149.0", sha256: "b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2", size: 179721344, signatureStatus: "OPEN_G5_FINDING_INVALID_VENDOR_SIGNATURE" });
    expect(Object.isFrozen(ACCEPTED_SUPPLY)).toBe(true);
  });
  it("does not let caller overrides admit arbitrary fixture bytes as production", async () => {
    await expect(verifyExactSupply({ executablePath, expectedSha256: profile.sha256 })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(verifyExactSupply({ executablePath, expectedVersion: "fixture-only" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(verifyExactSupply({ executablePath })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("fails explicitly when the exact accepted binary is absent", async () => {
    await expect(verifyExactSupply({ executablePath: join(directory, "missing") })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("checks actual fixture bytes and freezes descriptor identity without execution", async () => {
    const verifier = createControlledSupplyVerifierForTests(profile);
    const result = await verifier.verify(executablePath);
    expect(result).toMatchObject({ canonicalPath: executablePath, sha256: profile.sha256, evidenceClass: "controlled-fixture", versionEvidence: "controlled-fixture-not-vendor-evidence" });
    expect(Object.isFrozen(result)).toBe(true); expect(Object.isFrozen(result.identity)).toBe(true);
    expect(await verifier.revalidate(result)).toEqual(result);
    await expect(revalidateExactSupply(result as unknown as VerifiedSupply)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("rejects same-length byte tampering and size mismatch", async () => {
    const verifier = createControlledSupplyVerifierForTests(profile);
    await writeFile(executablePath, Buffer.alloc(bytes.length, 65));
    await expect(verifier.verify(executablePath)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await writeFile(executablePath, "short");
    await expect(verifier.verify(executablePath)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("detects a replaced inode even when payload bytes remain identical", async () => {
    const verifier = createControlledSupplyVerifierForTests(profile);
    const original = await verifier.verify(executablePath);
    await writeFile(join(directory, "replacement"), bytes);
    await rename(join(directory, "replacement"), executablePath);
    await expect(verifier.revalidate(original)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("rejects a forged or cross-instance descriptor", async () => {
    const verifier = createControlledSupplyVerifierForTests(profile);
    const descriptor = await verifier.verify(executablePath);
    await expect(verifier.revalidate({ ...descriptor })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(createControlledSupplyVerifierForTests(profile).revalidate(descriptor)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(revalidateExactSupply({ ...descriptor, evidenceClass: "accepted-supply" } as VerifiedSupply)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("rejects direct symlinks, parent aliases, directories and relative paths", async () => {
    const verifier = createControlledSupplyVerifierForTests(profile);
    const alias = join(directory, "alias"); await symlink(executablePath, alias);
    await expect(verifier.verify(alias)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    const parentAlias = join(directory, "parent-alias"); await symlink(directory, parentAlias);
    await expect(verifier.verify(join(parentAlias, "fixture"))).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(verifier.verify(directory)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(verifier.verify("./fixture")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("binds a truthful non-vendor custom profile to its complete exact closure without granting acceptance", async () => {
    const supplier = join(directory, "supplier"), codex = join(supplier, "codex"), helper = join(supplier, "helper.dat");
    await mkdir(supplier); await writeFile(codex, bytes); await writeFile(helper, "helper");
    const helperBytes = Buffer.from("helper"), closure = [
      { relativePath: "supplier", type: "directory" as const },
      { relativePath: "supplier/codex", type: "file" as const, sha256: profile.sha256, size: bytes.length, mode: "data" as const },
      { relativePath: "supplier/helper.dat", type: "file" as const, sha256: createHash("sha256").update(helperBytes).digest("hex"), size: helperBytes.length, mode: "data" as const }
    ];
    const exactProfile = { schema: "chirality-custom-supplier-exact-profile/v1" as const, executable: { relativePath: "supplier/codex" as const, ...profile } };
    await expect(() => createCustomSupplyVerifier(exactProfile, closure)).toThrow();
    closure[1] = { ...closure[1], mode: "executable" as const };
    const verifier = createCustomSupplyVerifier(exactProfile, closure);
    await chmod(codex, 0o700);
    let descriptor = await verifier.verify({ executablePath: codex });
    expect(descriptor).toMatchObject({ evidenceClass: "custom-supply-profile-verified", versionEvidence: "custom-build-exact-profile", signatureStatus: "custom-build-signature-not-evaluated" });
    await expect(revalidateExactSupply(descriptor as unknown as VerifiedSupply)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await chmod(codex, 0o744); await expect(verifier.revalidate(descriptor)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await chmod(codex, 0o700); descriptor = await verifier.verify({ executablePath: codex });
    await writeFile(join(supplier, "unlisted"), "extra");
    await expect(verifier.verify({ executablePath: codex })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await rm(join(supplier, "unlisted"));
    await writeFile(helper, "tamper");
    await expect(verifier.revalidate(descriptor)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(createCustomSupplyVerifier(exactProfile, closure).revalidate(descriptor)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("detects symlink substitution after verification", async () => {
    const verifier = createControlledSupplyVerifierForTests(profile);
    const original = await verifier.verify(executablePath);
    const target = join(directory, "target"); await writeFile(target, bytes); await rm(executablePath); await symlink(target, executablePath);
    await expect(verifier.revalidate(original)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
});
