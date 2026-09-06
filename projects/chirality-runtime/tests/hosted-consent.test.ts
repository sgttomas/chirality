import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { chmod, mkdtemp, readFile, realpath, rm, stat, symlink } from "node:fs/promises";
import { homedir, tmpdir } from "node:os";
import { join } from "node:path";
import { HostedConsentStore } from "../packages/core/src/hosted-consent.js";
import type { HostedConsent, WorkerContinuity } from "@chirality/runtime-contracts";

let root: string;
let identity: WorkerContinuity;
let store: HostedConsentStore;
const consent = (posture: HostedConsent["posture"]): HostedConsent => ({ identity, posture, approvedBy: "fixture-owner", approvedAt: "2026-09-06T00:00:00Z" });
beforeEach(async () => {
  root = await realpath(await mkdtemp(join(tmpdir(), "consent-test-")));
  identity = { canonicalRoot: root, cwd: root, accountId: "fixture-account", accountEpoch: 1, policyDigest: "fixture-policy" };
  store = new HostedConsentStore({ canonicalRoot: root, codexHome: join(root, "codex") });
});
afterEach(async () => { await rm(root, { recursive: true, force: true }); });

describe("root-private hosted consent", () => {
  it("defaults off and explicitly supplies app-owned CODEX_HOME", async () => {
    expect(await store.read(identity)).toBeUndefined();
    expect(await store.configuration(identity)).toEqual({ posture: "off", network_access: false, label: "Command network off (default)", env: { CODEX_HOME: join(root, "codex") } });
    expect((await stat(join(root, "codex"))).mode & 0o777).toBe(0o700);
  });
  it("persists labelled on consent across a new store instance and revokes to off", async () => {
    await store.grant(consent("on"));
    const next = new HostedConsentStore({ canonicalRoot: root, codexHome: store.codexHome });
    expect(await next.configuration(identity)).toMatchObject({ network_access: true, label: "Command network on" });
    expect((await stat(join(store.codexHome, "chirality-consent.json"))).mode & 0o777).toBe(0o600);
    await next.grant(consent("off"));
    expect((await store.configuration(identity)).network_access).toBe(false);
  });
  it.each(["accountId", "accountEpoch", "policyDigest"] as const)("does not carry consent across %s drift", async field => {
    await store.grant(consent("on"));
    const changed = { ...identity, [field]: field === "accountEpoch" ? 2 : "different" };
    expect(await store.read(changed)).toBeUndefined();
    expect((await store.configuration(changed)).network_access).toBe(false);
  });
  it("refuses noncanonical cwd and root aliases", async () => {
    await symlink(root, join(root, "alias"));
    await expect(store.read({ ...identity, cwd: join(root, "other") })).rejects.toMatchObject({ code: "FORBIDDEN" });
    const alias = join(root, "alias");
    await expect(store.read({ ...identity, canonicalRoot: alias, cwd: alias })).rejects.toMatchObject({ code: "FORBIDDEN" });
  });
  it("binds a private home to exactly one root", async () => {
    await store.grant(consent("on"));
    const other = await realpath(await mkdtemp(join(root, "other-")));
    const second = new HostedConsentStore({ canonicalRoot: other, codexHome: store.codexHome });
    await expect(second.read({ ...identity, canonicalRoot: other, cwd: other })).rejects.toMatchObject({ code: "FORBIDDEN" });
  });
  it("excludes ambient home without reading its contents", async () => {
    const ambient = new HostedConsentStore({ canonicalRoot: root, codexHome: join(homedir(), ".codex") });
    await expect(ambient.read(identity)).rejects.toMatchObject({ code: "FORBIDDEN" });
  });
  it("refuses symlink storage and unsafe permissions without modifying target", async () => {
    const target = await realpath(await mkdtemp(join(root, "target-")));
    await symlink(target, store.codexHome);
    await expect(store.read(identity)).rejects.toMatchObject({ code: "FORBIDDEN" });
    await rm(store.codexHome);
    await chmod(target, 0o755);
    const unsafe = new HostedConsentStore({ canonicalRoot: root, codexHome: target });
    await expect(unsafe.read(identity)).rejects.toMatchObject({ code: "FORBIDDEN" });
    expect((await stat(target)).mode & 0o777).toBe(0o755);
  });
  it("refuses a consent-file symlink", async () => {
    await store.read(identity);
    await symlink(join(store.codexHome, "chirality-root.json"), join(store.codexHome, "chirality-consent.json"));
    await expect(store.grant(consent("on"))).rejects.toMatchObject({ code: "INTERNAL_FAILURE" });
    expect(JSON.parse(await readFile(join(store.codexHome, "chirality-root.json"), "utf8"))).toEqual({ canonicalRoot: root });
  });
  it("requires ask posture and explicit user act and records host/protocol/grouping caveat", async () => {
    const approval = { host: "example.test", protocol: "https", acceptForSession: true, explicitUserAct: true, approvedBy: "fixture-owner" };
    await expect(store.authorizeDestination(identity, approval)).rejects.toMatchObject({ code: "FORBIDDEN" });
    await store.grant(consent("ask-per-destination"));
    expect(store.destinationPrompt(approval)).toMatchObject({ host: "example.test", protocol: "https", caveat: expect.stringContaining("queued requests") });
    await expect(store.authorizeDestination(identity, { ...approval, explicitUserAct: false })).rejects.toMatchObject({ code: "FORBIDDEN" });
    await store.authorizeDestination(identity, approval);
    expect((await store.configuration(identity)).network_access).toBe(false);
    await expect(store.authorizeDestination(identity, { ...approval, host: "https://bad/path" })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  });
});
