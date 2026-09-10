import { chmod, mkdtemp, readFile, realpath, rm, symlink, writeFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { HostedIdentityBindingStore, type HostedIdentitySnapshot } from "../packages/daemon/src/hosted-identity-binding.js";
import { CodexTurnSession } from "../packages/daemon/src/codex-session.js";
import { SupplierAuthorityController } from "../packages/daemon/src/supplier-authority-controller.js";
import { createFakeRuntimeAdmissionNativeAdapter } from "../packages/core/src/runtime-admission-lock.js";

const cleanups: (() => Promise<void>)[] = [];
afterEach(async () => { while (cleanups.length) await cleanups.pop()!(); });
const policy = "a".repeat(64);
const snapshot = (overrides: Partial<HostedIdentitySnapshot> = {}): HostedIdentitySnapshot => ({
  accountUserId: "account-a", providerWorkspaceId: "workspace-a", supplierGeneration: "supplier-1", identityGeneration: "identity-1", snapshotDigest: "b".repeat(64), ...overrides
});
async function fixture(random = Buffer.alloc(32, 1)) {
  const base = await realpath(await mkdtemp(join(tmpdir(), "hosted-binding-"))); cleanups.push(() => rm(base, { recursive: true, force: true }));
  const privateDirectory = join(base, "private"), canonicalRoot = join(base, "project");
  await import("node:fs/promises").then(({ mkdir }) => Promise.all([mkdir(privateDirectory, { mode: 0o700 }), mkdir(canonicalRoot, { mode: 0o700 })]));
  const options = { privateDirectory, canonicalRoot, policyDigest: policy, runtimeAuthorityId: "runtime-1", randomHandle: () => random };
  return { base, privateDirectory, canonicalRoot, options, store: await HostedIdentityBindingStore.open(options) };
}
const live = (calls?: string[]) => ({ assertLive() { calls?.push("live"); } });
function authority(overrides: { supplierGeneration?: string; identityGeneration?: string; snapshotDigest?: string } = {}) {
  const lease = createFakeRuntimeAdmissionNativeAdapter().acquire("", "runtime-admission-authority.lock");
  const controller = new SupplierAuthorityController({ enabled: true, kernelLease: lease,
    transport: { subscribe: () => () => {}, send: async () => {}, close: async () => {} }, authoritySecret: Buffer.alloc(32, 3),
    runtimeProcessIncarnationId: "11111111-1111-1111-1111-111111111111", supplierGeneration: overrides.supplierGeneration ?? "supplier-1",
    identityGeneration: overrides.identityGeneration ?? "identity-1", snapshotDigest: overrides.snapshotDigest ?? "b".repeat(64) });
  return { controller, lease };
}

describe("HostedIdentityBindingStore", () => {
  it("binds projected snapshot evidence to the concrete live controller and held kernel lease", async () => {
    const { controller, lease } = authority();
    expect(() => controller.assertSnapshotBinding({ supplierGeneration: "supplier-1", identityGeneration: "identity-1", snapshotDigest: "b".repeat(64) })).not.toThrow();
    expect(() => controller.assertSnapshotBinding({ supplierGeneration: "supplier-other", identityGeneration: "identity-1", snapshotDigest: "b".repeat(64) })).toThrow("authority-unavailable");
    expect(() => controller.assertSnapshotBinding({ supplierGeneration: "supplier-1", identityGeneration: "identity-other", snapshotDigest: "b".repeat(64) })).toThrow("authority-unavailable");
    expect(() => controller.assertSnapshotBinding({ supplierGeneration: "supplier-1", identityGeneration: "identity-1", snapshotDigest: "c".repeat(64) })).toThrow("authority-unavailable");
    lease.close(); expect(() => controller.assertSnapshotBinding({ supplierGeneration: "supplier-1", identityGeneration: "identity-1", snapshotDigest: "b".repeat(64) })).toThrow("authority-unavailable");
  });

  it("persists a random local handle at epoch one without projecting the supplier tuple", async () => {
    const f = await fixture(); const continuity = await f.store.establishLive(snapshot(), live());
    expect(continuity).toEqual({ canonicalRoot: f.canonicalRoot, cwd: f.canonicalRoot, accountId: `rhb_${Buffer.alloc(32, 1).toString("base64url")}`, accountEpoch: 1, policyDigest: policy });
    expect(JSON.stringify(continuity)).not.toContain("account-a");
    const file = join(f.privateDirectory, "hosted-identity-binding.json"), stat = await import("node:fs/promises").then(fs => fs.lstat(file));
    expect(stat.mode & 0o777).toBe(0o600); expect(JSON.parse(await readFile(file, "utf8")).accountUserId).toBe("account-a");
  });

  it("reuses continuity across restart only after a fresh live exact-pair observation", async () => {
    const f = await fixture(); const first = await f.store.establishLive(snapshot(), live());
    const restarted = await HostedIdentityBindingStore.open({ ...f.options, runtimeAuthorityId: "runtime-2", randomHandle: () => Buffer.alloc(32, 2) });
    const calls: string[] = []; const second = await restarted.establishLive(snapshot({ supplierGeneration: "supplier-2", identityGeneration: "identity-2", snapshotDigest: "c".repeat(64) }), live(calls));
    expect(second).toEqual(first); expect(calls).toEqual(["live"]);
    const durable = JSON.parse(await readFile(join(f.privateDirectory, "hosted-identity-binding.json"), "utf8"));
    expect(durable.runtimeAuthorityId).toBe("runtime-2"); expect(durable.supplierGeneration).toBe("supplier-2"); expect(durable.accountEpoch).toBe(1);
  });

  it("advances the epoch for a changed verified pair and preserves the lineage handle", async () => {
    const f = await fixture(); const first = await f.store.establishLive(snapshot(), live());
    const changed = await f.store.establishLive(snapshot({ accountUserId: "account-b" }), live());
    expect(changed.accountId).toBe(first.accountId); expect(changed.accountEpoch).toBe(2);
  });

  it.each(["sign-out", "switch", "revoke"] as const)("durably fences %s before same-pair re-login", async reason => {
    const f = await fixture(); const first = await f.store.establishLive(snapshot(), live());
    const fenced = await f.store.fence(reason); expect(fenced?.accountEpoch).toBe(first.accountEpoch + 1);
    const restarted = await HostedIdentityBindingStore.open({ ...f.options, runtimeAuthorityId: "runtime-2" });
    const rebound = await restarted.establishLive(snapshot({ supplierGeneration: "supplier-2" }), live());
    expect(rebound).toEqual({ ...first, accountEpoch: first.accountEpoch + 1 });
  });

  it("allocates a distinct random handle at epoch exhaustion and never wraps", async () => {
    const f = await fixture(); await f.store.establishLive(snapshot(), live());
    const file = join(f.privateDirectory, "hosted-identity-binding.json"), record = JSON.parse(await readFile(file, "utf8"));
    const { digest: _old, ...body } = record; body.accountEpoch = Number.MAX_SAFE_INTEGER; record.accountEpoch = body.accountEpoch; record.digest = createHash("sha256").update(JSON.stringify(body)).digest("hex"); await writeFile(file, `${JSON.stringify(record)}\n`, { mode: 0o600 });
    const exhausted = await HostedIdentityBindingStore.open({ ...f.options, randomHandle: () => Buffer.alloc(32, 2) });
    const next = await exhausted.establishLive(snapshot({ accountUserId: "account-b" }), live());
    expect(next.accountId).toBe(`rhb_${Buffer.alloc(32, 2).toString("base64url")}`); expect(next.accountEpoch).toBe(1);
  });

  it("fails closed on corrupt, ambiguous, missing-unsafe, symlinked, and permissive custody", async () => {
    const corrupt = await fixture(); await writeFile(join(corrupt.privateDirectory, "hosted-identity-binding.json"), "{}\n", { mode: 0o600 });
    await expect(HostedIdentityBindingStore.open(corrupt.options)).rejects.toThrow("custody-unsafe");
    const ambiguous = await fixture(); await writeFile(join(ambiguous.privateDirectory, "hosted-identity-binding.json.crash.tmp"), "partial", { mode: 0o600 });
    await expect(HostedIdentityBindingStore.open(ambiguous.options)).rejects.toThrow("custody-unsafe");
    const missingUnsafe = await fixture(); await rm(missingUnsafe.privateDirectory, { recursive: true });
    await expect(HostedIdentityBindingStore.open(missingUnsafe.options)).rejects.toThrow("custody-unsafe");
    const permissive = await fixture(); await chmod(permissive.privateDirectory, 0o755);
    await expect(HostedIdentityBindingStore.open(permissive.options)).rejects.toThrow("custody-unsafe");
    const linked = await fixture(); const alias = join(linked.base, "alias"); await symlink(linked.privateDirectory, alias);
    await expect(HostedIdentityBindingStore.open({ ...linked.options, privateDirectory: alias })).rejects.toThrow("custody-unsafe");
    const linkedRoot = await fixture(); const rootAlias = join(linkedRoot.base, "root-alias"); await symlink(linkedRoot.canonicalRoot, rootAlias);
    await expect(HostedIdentityBindingStore.open({ ...linkedRoot.options, canonicalRoot: rootAlias })).rejects.toThrow("custody-unsafe");
  });

  it("rejects a symlink record without overwriting its target", async () => {
    const f = await fixture(); const outside = join(f.base, "outside"); await writeFile(outside, "untouched", { mode: 0o600 });
    await symlink(outside, join(f.privateDirectory, "hosted-identity-binding.json"));
    await expect(HostedIdentityBindingStore.open(f.options)).rejects.toThrow("custody-unsafe"); expect(await readFile(outside, "utf8")).toBe("untouched");
  });

  it("serializes concurrent transitions and cancels a queued transition without mutation", async () => {
    const f = await fixture(); let liveCalls = 0;
    const first = f.store.establishLive(snapshot(), { assertLive() { liveCalls++; } });
    const fenced = f.store.fence("revoke");
    const controller = new AbortController(); controller.abort();
    const cancelled = f.store.establishLive(snapshot({ accountUserId: "account-b" }), live(), controller.signal);
    await first; expect((await fenced)?.accountEpoch).toBe(2); await expect(cancelled).rejects.toMatchObject({ name: "AbortError" });
    const restarted = await HostedIdentityBindingStore.open(f.options); const unchanged = await restarted.establishLive(snapshot(), live());
    expect(unchanged.accountEpoch).toBe(2); expect(liveCalls).toBe(1);
  });

  it("requires live authority and leaves an existing record unchanged when the assertion fails", async () => {
    const f = await fixture(); const first = await f.store.establishLive(snapshot(), live());
    await expect(f.store.establishLive(snapshot({ accountUserId: "account-b" }), { assertLive() { throw new Error("authority-unavailable"); } })).rejects.toThrow("authority-unavailable");
    const reopened = await HostedIdentityBindingStore.open(f.options); expect(await reopened.establishLive(snapshot(), live())).toEqual(first);
  });

  it("keeps the raw pair inside the session/store seam and returns only continuity plus opaque authority evidence", async () => {
    const f = await fixture();
    const invoke = CodexTurnSession.prototype.establishHostedIdentityBinding as unknown as (
      this: { privateAuthoritySnapshot(): Promise<HostedIdentitySnapshot> }, store: HostedIdentityBindingStore,
      authority: SupplierAuthorityController, generation: string
    ) => Promise<Record<string, unknown>>;
    const { controller, lease } = authority();
    const result = await invoke.call({ privateAuthoritySnapshot: async () => snapshot() }, f.store, controller, "supplier-1");
    expect(result).toEqual({
      continuity: { canonicalRoot: f.canonicalRoot, cwd: f.canonicalRoot, accountId: `rhb_${Buffer.alloc(32, 1).toString("base64url")}`, accountEpoch: 1, policyDigest: policy },
      authority: { supplierGeneration: "supplier-1", identityGeneration: "identity-1", snapshotDigest: "b".repeat(64) },
      accountDigest: "e06715202245598ac296ef41edcee238ec0dd7906002b37d025958ab3ce5aa24"
    });
    expect(JSON.stringify(result)).not.toContain("account-a"); expect(JSON.stringify(result)).not.toContain("workspace-a");
    await controller.revoke(); lease.close();
  });

  it("rejects a snapshot paired with the wrong or revoked controller and rechecks after persistence", async () => {
    const f = await fixture();
    const invoke = CodexTurnSession.prototype.establishHostedIdentityBinding as unknown as (
      this: { privateAuthoritySnapshot(): Promise<HostedIdentitySnapshot> }, store: HostedIdentityBindingStore,
      authority: SupplierAuthorityController, generation: string
    ) => Promise<Record<string, unknown>>;
    const wrong = authority({ supplierGeneration: "supplier-other" });
    await expect(invoke.call({ privateAuthoritySnapshot: async () => snapshot() }, f.store, wrong.controller, "supplier-1")).rejects.toThrow("authority-unavailable");
    await wrong.controller.revoke(); wrong.lease.close();

    const current = authority(); const establish = f.store.establishLive.bind(f.store);
    f.store.establishLive = async (...args) => { const result = await establish(...args); await current.controller.revoke(); return result; };
    await expect(invoke.call({ privateAuthoritySnapshot: async () => snapshot() }, f.store, current.controller, "supplier-1")).rejects.toThrow("authority-unavailable");
    current.lease.close();
    const recovered = await HostedIdentityBindingStore.open(f.options);
    const rebound = await recovered.establishLive(snapshot(), live());
    expect(rebound.accountEpoch).toBe(2);
  });
});
