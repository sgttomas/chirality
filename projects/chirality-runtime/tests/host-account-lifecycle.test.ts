import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { AuthRegistry } from "../packages/core/src/auth-registry.js";
import {
  HostAccountAuthority,
  type HostAccountNativeAdmission,
  type HostAccountXpcServerPort
} from "../packages/daemon/src/host-account-authority.js";
import {
  HOST_ACCOUNT_SCOPES,
  createHostAccountCeremonyProof,
  createHostAccountRequestProof,
  hostAccountBodyDigest,
  hostAccountRequest,
  verifyHostAccountProof,
  type HostAccountSigningPredicate
} from "../packages/daemon/src/host-account-protocol.js";
import {
  MainHostAccountClient,
  type HostAccountClientNativeAdmission
} from "../packages/daemon/src/host-account-client.js";
import {
  issueHostedAccountAuthorityV2FromP2,
  revalidateHostedAccountAuthorityV2
} from "../packages/daemon/src/runtime-conformance-v2-admission.js";

const roots: string[] = [];
afterEach(async () => { await Promise.all(roots.splice(0).map((root) => rm(root, { recursive: true, force: true }))); });

const predicate: HostAccountSigningPredicate = {
  schema: "chirality.host-account-signing-predicate/v1",
  serviceName: "com.chirality.app.runtime.account-host",
  bundleId: "com.chirality.app",
  teamId: "TESTTEAM01",
  peerRequirement: "identifier \"com.chirality.app\" and anchor apple generic and certificate leaf[subject.OU] = TESTTEAM01"
};

function nativeFixture() {
  let callbacks!: Parameters<HostAccountNativeAdmission["createHostXpcServer"]>[0];
  const closed: string[] = [];
  const port: HostAccountXpcServerPort = {
    async ping(_connectionId, input) { return input; },
    async closeConnection(connectionId) { closed.push(connectionId); },
    async close() {}
  };
  const nativeAdmission: HostAccountNativeAdmission = {
    createHostXpcServer(input) { callbacks = input; return port; }
  };
  return { nativeAdmission, callbacks: () => callbacks, closed };
}

describe("P2 host account protocol", () => {
  it("signs the actual fixed GET status and POST control domains", () => {
    const nonce = Buffer.alloc(32, 7);
    const generation = "8c318d76-f220-4e5d-a1c2-3099bf295b7c";
    for (const descriptor of [
      hostAccountRequest("status", "project-one"),
      hostAccountRequest("grant-provider-network-consent", "project-one")
    ]) {
      const proof = createHostAccountRequestProof(nonce, {
        method: descriptor.method,
        route: descriptor.route,
        canonicalBodyDigest: hostAccountBodyDigest(descriptor.canonicalBody),
        counter: 1,
        generation
      });
      expect(verifyHostAccountProof(proof, proof)).toBe(true);
    }
    expect(hostAccountRequest("status", "project-one")).toMatchObject({ method: "GET", canonicalBody: "", requiredScope: "account:read" });
    expect(hostAccountRequest("grant-provider-network-consent", "project-one")).toMatchObject({ method: "POST", canonicalBody: "{\"consent\":true}", requiredScope: "account:control" });
  });

  it("commits generation, grants memory authority, journals only digests, and rejects replay", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-host-account-")); roots.push(root);
    const auth = new AuthRegistry(root);
    const native = nativeFixture();
    const authority = new HostAccountAuthority({ runtimeDirectory: root, auth, signingPredicate: predicate, expectedEuid: 501, nativeAdmission: native.nativeAdmission });
    await authority.start();
    const challenge = await native.callbacks().onCeremonyOpen({ connectionId: "connection-1", requestId: "ceremony-1" });
    const nonce = Buffer.alloc(32, 11);
    const grant = await native.callbacks().onCeremonyFinish({
      connectionId: "connection-1", requestId: "ceremony-1", hostNonce: nonce,
      proof: createHostAccountCeremonyProof(nonce, challenge.challenge, challenge.generation)
    });
    expect(grant.scopes).toEqual(HOST_ACCOUNT_SCOPES);
    const descriptor = hostAccountRequest("status", "project-one");
    const proof = createHostAccountRequestProof(nonce, {
      method: descriptor.method, route: descriptor.route,
      canonicalBodyDigest: hostAccountBodyDigest(descriptor.canonicalBody), counter: 1,
      generation: grant.generation
    });
    const headers = {
      authorization: `Bearer ${grant.bearer.toString("base64url")}`,
      counter: "1", generation: grant.generation, proof, descriptor
    };
    await expect(authority.authorizeRequest(headers)).resolves.toMatchObject({ scopes: HOST_ACCOUNT_SCOPES });
    await expect(authority.authorizeRequest(headers)).rejects.toMatchObject({ code: "UNAUTHORIZED" });
    const control = hostAccountRequest("grant-provider-network-consent", "project-one");
    const controlHeaders = {
      authorization: headers.authorization,
      counter: "2",
      generation: grant.generation,
      proof: createHostAccountRequestProof(nonce, {
        method: control.method, route: control.route,
        canonicalBodyDigest: hostAccountBodyDigest(control.canonicalBody), counter: 2,
        generation: grant.generation
      }),
      descriptor: control
    };
    await expect(authority.runAuthorizedRequest(controlHeaders, async (principal) => ({ clientId: principal.clientId, effected: true })))
      .resolves.toMatchObject({ clientId: expect.stringMatching(/^app-account-host:/), effected: true });
    const journal = await readFile(join(root, "auth", "account-host.json"), "utf8");
    expect(journal).not.toContain(grant.bearer.toString("base64url"));
    expect(journal).not.toContain(nonce.toString("base64url"));
    expect(JSON.parse(journal).principals[0]).toMatchObject({ lastCounter: 2, leaseState: "active" });
    const subject = { purpose: "login" as const, projectId: "project-one", manifestHash: "a".repeat(64), canonicalRoot: root, account: null, consentDigest: "b".repeat(64) };
    const admission = issueHostedAccountAuthorityV2FromP2(authority, subject);
    await expect(revalidateHostedAccountAuthorityV2(admission, subject)).resolves.toBeUndefined();
    await authority.close();
    await expect(revalidateHostedAccountAuthorityV2(admission, subject)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });

  it("keeps invalidation sticky while a ceremony finish is queued", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-host-account-")); roots.push(root);
    const auth = new AuthRegistry(root);
    const native = nativeFixture();
    const authority = new HostAccountAuthority({ runtimeDirectory: root, auth, signingPredicate: predicate, expectedEuid: 501, nativeAdmission: native.nativeAdmission });
    await authority.start();
    const challenge = await native.callbacks().onCeremonyOpen({ connectionId: "connection-late", requestId: "ceremony-late" });
    const nonce = Buffer.alloc(32, 13);
    const finish = native.callbacks().onCeremonyFinish({ connectionId: "connection-late", requestId: "ceremony-late", hostNonce: nonce, proof: createHostAccountCeremonyProof(nonce, challenge.challenge, challenge.generation) });
    native.callbacks().onInvalidated({ connectionId: "connection-late", reason: "invalidated" });
    await expect(finish).rejects.toMatchObject({ code: "UNAUTHORIZED" });
    const journal = JSON.parse(await readFile(join(root, "auth", "account-host.json"), "utf8"));
    expect(journal.principals).toEqual([]);
    await authority.close();
  });

  it("does not publish a client authority when invalidated before a late grant", async () => {
    let callbacks!: Parameters<HostAccountClientNativeAdmission["createHostXpcClient"]>[0];
    let release!: (value: { requestId: string; bearer: Buffer; generation: string; scopes: typeof HOST_ACCOUNT_SCOPES }) => void;
    let provisionRequestId = "";
    let returnedBearer: Buffer | undefined;
    const generation = "8c318d76-f220-4e5d-a1c2-3099bf295b7c";
    const nativeAdmission: HostAccountClientNativeAdmission = {
      createHostXpcClient(input) {
        callbacks = input;
        return {
          async provision(request) {
            provisionRequestId = request.requestId;
            const challenge = Buffer.alloc(32, 17);
            await request.onChallenge({ requestId: request.requestId, challenge, generation });
            return await new Promise((resolve) => { release = resolve; });
          },
          async close() {}
        };
      }
    };
    const client = new MainHostAccountClient({ socketPath: "/tmp/runtime.sock", signingPredicate: predicate, expectedEuid: 501, nativeAdmission });
    const starting = client.start();
    await new Promise((resolve) => setImmediate(resolve));
    callbacks.onInvalidated({ reason: "invalidated" });
    returnedBearer = Buffer.alloc(32, 23);
    release({ requestId: provisionRequestId, bearer: returnedBearer, generation, scopes: HOST_ACCOUNT_SCOPES });
    await expect(starting).rejects.toMatchObject({ code: "UNAUTHORIZED" });
    expect(returnedBearer.every((byte) => byte === 0)).toBe(true);
    await expect(client.status("project-one")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });

  it("aborts and rejects an account effect when the exact connection is invalidated", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-host-account-")); roots.push(root);
    const auth = new AuthRegistry(root), native = nativeFixture();
    const authority = new HostAccountAuthority({ runtimeDirectory: root, auth, signingPredicate: predicate, expectedEuid: 501, nativeAdmission: native.nativeAdmission });
    await authority.start();
    const challenge = await native.callbacks().onCeremonyOpen({ connectionId: "effect-connection", requestId: "effect-ceremony" });
    const nonce = Buffer.alloc(32, 29);
    const grant = await native.callbacks().onCeremonyFinish({ connectionId: "effect-connection", requestId: "effect-ceremony", hostNonce: nonce,
      proof: createHostAccountCeremonyProof(nonce, challenge.challenge, challenge.generation) });
    const descriptor = hostAccountRequest("grant-provider-network-consent", "project-one"), counter = 1;
    let published = false;
    const running = authority.runAuthorizedRequest({ authorization: `Bearer ${grant.bearer.toString("base64url")}`, counter: String(counter), generation: grant.generation,
      proof: createHostAccountRequestProof(nonce, { method: descriptor.method, route: descriptor.route, canonicalBodyDigest: hostAccountBodyDigest(descriptor.canonicalBody), counter, generation: grant.generation }), descriptor },
    async (_principal, signal) => {
      await new Promise<void>((resolve) => signal.addEventListener("abort", () => resolve(), { once: true }));
      if (!signal.aborted) published = true;
      return { published };
    });
    await new Promise((resolve) => setImmediate(resolve));
    await native.callbacks().onInvalidated({ connectionId: "effect-connection", reason: "invalidated" });
    await expect(running).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    expect(published).toBe(false);
    await authority.close();
  });
});
