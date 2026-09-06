import { afterEach, beforeEach, expect, it } from "vitest";
import { mkdtemp, realpath, rm, symlink, readFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { ApprovalStore, validateNetworkApprovalContext, type ApprovalBinding } from "../packages/core/src/approval-store.js";
import { HostedConsentStore } from "../packages/core/src/hosted-consent.js";
let root: string, control: string, binding: ApprovalBinding, consent: HostedConsentStore, store: ApprovalStore, live: boolean;
const destination = { host: "example.com", protocol: "https" };
const allow = { decision: "allow", approvedBy: "fixture-human", explicitUserAct: true } as const;
beforeEach(async () => {
  root = await realpath(await mkdtemp(join(tmpdir(), "approval-test-")));
  binding = { canonicalRoot: root, cwd: root, accountId: "fixture-account", accountEpoch: 1, policyDigest: "fixture-policy", sessionId: "session", turnId: "turn", workerGeneration: "generation" };
  control = await realpath(await mkdtemp(join(tmpdir(), "approval-control-test-")));
  live = true;
  consent = new HostedConsentStore({ canonicalRoot: root, codexHome: join(root, "home") });
  store = new ApprovalStore({ canonicalRoot: root, storageRoot: join(control, "approvals"), consent, isLive: () => live });
});
afterEach(async () => { await rm(root, { recursive: true, force: true }); await rm(control, { recursive: true, force: true }); });
async function grant(posture: "off" | "ask-per-destination" | "on") {
  await consent.grant({ identity: binding, posture, approvedBy: "fixture-owner", approvedAt: "2026-09-06T00:00:00Z" });
}
it("defaults off and cannot mint consent through an approval", async () => {
  const request = await store.request(binding, destination, "fixture-worker");
  expect(await store.authorize(request.requestId, binding)).toBe(false);
  await expect(store.decide(request.requestId, binding, allow)).rejects.toMatchObject({ code: "FORBIDDEN" });
  await store.decide(request.requestId, binding, { ...allow, decision: "deny" });
});
it("asks for exact attributed approval, preserving durable session choice without auto-granting another request", async () => {
  await grant("ask-per-destination");
  const request = await store.request(binding, destination, "fixture-worker");
  expect(request.caveat).toContain("queued requests");
  expect(await store.authorize(request.requestId, binding)).toBe(false);
  await expect(store.decide(request.requestId, binding, { ...allow, decision: "acceptForSession", explicitUserAct: false } as never)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  const result = await store.decide(request.requestId, binding, { ...allow, decision: "acceptForSession" });
  expect(result.decision?.approvedBy).toBe("fixture-human");
  expect(await store.authorize(request.requestId, binding)).toBe(true);
  const next = await store.request(binding, destination, "fixture-worker");
  expect(await store.authorize(next.requestId, binding)).toBe(false);
  expect((await store.listPending(binding)).map(item => item.requestId)).toEqual([next.requestId]);
  const restarted = new ApprovalStore({ canonicalRoot: root, storageRoot: join(control, "approvals"), consent, isLive: () => true });
  expect(await restarted.authorize(request.requestId, binding)).toBe(true);
});
it.each(["accountId", "accountEpoch", "policyDigest", "sessionId", "turnId", "workerGeneration"] as const)("rejects cross-principal or stale %s", async field => {
  await grant("ask-per-destination");
  const request = await store.request(binding, destination, "fixture-worker");
  const different = { ...binding, [field]: field === "accountEpoch" ? 2 : "different" };
  await expect(store.decide(request.requestId, different, allow)).rejects.toMatchObject({ code: "FORBIDDEN" });
});
it("rejects a no-longer-live generation and unknown/external request paths", async () => {
  const request = await store.request(binding, destination, "fixture-worker");
  await expect(store.read("../../outside", binding)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  await expect(store.read("00000000-0000-4000-8000-000000000000", binding)).rejects.toMatchObject({ code: "FORBIDDEN" });
  live = false;
  await expect(store.read(request.requestId, binding)).rejects.toMatchObject({ code: "FORBIDDEN" });
});
it("requires standing explicit on consent and denies after consent drift or revocation", async () => {
  await grant("on");
  const request = await store.request(binding, destination, "fixture-worker");
  expect(await store.authorize(request.requestId, binding)).toBe(true);
  expect(await consent.configuration(binding)).toMatchObject({ label: "Command network on", network_access: true });
  await grant("ask-per-destination");
  expect(await store.authorize(request.requestId, binding)).toBe(false);
  await expect(store.decide(request.requestId, binding, allow)).rejects.toMatchObject({ code: "FORBIDDEN" });
  await grant("off");
  expect(await store.authorize(request.requestId, binding)).toBe(false);
});
it("publishes only one immutable decision under concurrent conflicting acts", async () => {
  await grant("ask-per-destination");
  const request = await store.request(binding, destination, "fixture-worker");
  const results = await Promise.allSettled([store.decide(request.requestId, binding, allow), store.decide(request.requestId, binding, { ...allow, decision: "deny" })]);
  expect(results.filter(result => result.status === "fulfilled")).toHaveLength(1);
  expect(results.filter(result => result.status === "rejected")).toHaveLength(1);
  const final = await store.read(request.requestId, binding);
  const before = await readFile(join(control, "approvals", `${request.requestId}.decision.json`), "utf8");
  await store.decide(request.requestId, binding, { ...allow, decision: final.decision!.decision });
  expect(await readFile(join(control, "approvals", `${request.requestId}.decision.json`), "utf8")).toBe(before);
});
it("refuses symlink records and storage inside the worker writable root", async () => {
  const request = await store.request(binding, destination, "fixture-worker");
  await symlink(join(root, "home", "chirality-root.json"), join(control, "approvals", `${request.requestId}.decision.json`));
  await expect(store.read(request.requestId, binding)).rejects.toMatchObject({ code: "INTERNAL_FAILURE" });
  const outside = new ApprovalStore({ canonicalRoot: root, storageRoot: join(root, "approvals"), consent, isLive: () => true });
  await expect(outside.request(binding, destination, "fixture-worker")).rejects.toMatchObject({ code: "FORBIDDEN" });
});
it.each(["https://example.com", "example.com/path", "user@example.com", "example.com:443", "a\nb", "-bad.test"])("rejects unsafe destination %s", host => {
  expect(() => validateNetworkApprovalContext({ host, protocol: "https" })).toThrow();
});
it("accepts DNS and IPv6 and rejects unknown provider payloads", () => {
  expect(validateNetworkApprovalContext({ host: "[::1]", protocol: "https" }).host).toBe("[::1]");
  expect(() => validateNetworkApprovalContext({ ...destination, credentials: "secret" })).toThrow();
});

it("binds external control storage to a single root and refuses symlink storage", async () => {
  await store.request(binding, destination, "fixture-worker");
  const other = await realpath(await mkdtemp(join(control, "other-root-")));
  const second = new ApprovalStore({ canonicalRoot: other, storageRoot: join(control, "approvals"), consent, isLive: () => true });
  await expect(second.request({ ...binding, canonicalRoot: other, cwd: other }, destination, "fixture-worker")).rejects.toMatchObject({ code: "FORBIDDEN" });
  await symlink(join(control, "approvals"), join(control, "alias"));
  const alias = new ApprovalStore({ canonicalRoot: root, storageRoot: join(control, "alias"), consent, isLive: () => true });
  await expect(alias.request(binding, destination, "fixture-worker")).rejects.toMatchObject({ code: "FORBIDDEN" });
});
it("preserves attributed provider resolution separately from user decision and never grants after cancellation", async () => {
  await grant("ask-per-destination");
  const request = await store.request(binding, { host: "example.com", protocol: "socks5Tcp" }, "trusted-worker");
  await store.resolve(request.requestId, binding, "trusted-supervisor");
  expect(await store.listPending(binding)).toEqual([]);
  expect(await store.authorize(request.requestId, binding)).toBe(false);
  await expect(store.decide(request.requestId, binding, allow)).rejects.toThrow("resolved");
  const record = await store.read(request.requestId, binding);
  expect(record.decision).toBeUndefined(); expect(record.resolution?.resolvedBy).toBe("trusted-supervisor");
});
