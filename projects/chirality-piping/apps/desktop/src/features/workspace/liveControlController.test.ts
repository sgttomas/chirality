import { beforeEach, afterEach, describe, expect, it, vi } from "vitest";
import { loadPreviewModel } from "../../services/previewService";
import * as hashes from "../../services/hashService";
import * as batches from "../../services/operationBatchService";
import { LiveControlController } from "./liveControlController";
import type { LiveAdmission, LiveRequest, LiveResponse, LiveSnapshot } from "./liveControlTypes";
const deferred = <T,>() => { let resolve!: (v: T) => void; const promise = new Promise<T>(r => { resolve = r; }); return { promise, resolve }; };
function result<T = Record<string, any>>(response: LiveResponse): T { if ("error" in response) throw new Error(JSON.stringify(response.error)); return response.result as T; }
let snapshot: LiveSnapshot;
let controller: LiveControlController;
let queued: LiveAdmission[];
let busy = false;
const call = (method: string, params: unknown, signal = new AbortController().signal) => controller.request({ controller_session_id: controller.sessionId, app_instance_id: "app-test", registration_id: "registration-test", dispatch_id: crypto.randomUUID(), request_id: "request-test", method, params } satisfies LiveRequest, signal);
async function prepared(changes?: unknown[]) {
  const workspace = result(await call("inspect", { scope: "workspace" })).workspace;
  const inspected = result(await call("inspect", { scope: "nodes", workspace, node_ids: [snapshot.model.nodes[0].id] }));
  const first = inspected.nodes[0];
  const preview = result(await call("preview", { workspace, basis: inspected.basis, changes: changes ?? [{ target: { object_type: "Node", ref: first.id }, field_path: "position.x", before: String(first.position.x), after: String(first.position.x + 0.01), unit: inspected.length_unit, dimension: "length" }] }));
  expect(preview.validation).toBe("passed");
  return { workspace, preview_ref: preview.preview_ref, idempotency_key: "key-test" };
}
beforeEach(async () => {
  const model = await loadPreviewModel();
  const hash = await hashes.computeModelHash(model);
  if (!hash) throw new Error("No canonical hash");
  snapshot = { model, generation: 1, revision: 1, internalRevision: 4, hash, selection: [] };
  queued = []; busy = false;
  controller = new LiveControlController({ snapshot: () => snapshot, enqueue: a => queued.push(a), remove: token => { queued = queued.filter(a => a.token !== token); }, busy: () => busy });
  controller.bind("app-test");
});
afterEach(() => vi.restoreAllMocks());
describe("live controller publication and same-session recovery", () => {
  it("uses the real engine for agent-attributed validate-only preview without changing the source", async () => {
    const before = structuredClone(snapshot);
    const p = await prepared();
    expect(snapshot).toEqual(before); expect(queued).toHaveLength(0);
    const submit = call("submit", p);
    expect(queued).toHaveLength(1);
    expect(queued[0].batch.operations[0]).toMatchObject({ author_type: "agent", source: { source_channel: "local_json_cli", source_role: "external_agent_proposal", source_ref: `local_json_cli:${controller.sessionId}:request-test` } });
    controller.observe(new Set([queued[0].token]), 1, 1, []);
    expect(result(await submit).state).toBe("queued");
  });
  it("reserves concurrent same-key submits before publication and recovers while a new owner is busy", async () => {
    const p = await prepared(); let settled = false;
    const first = call("submit", p).then(r => { settled = true; return r; });
    const second = call("submit", p);
    await Promise.resolve(); expect(settled).toBe(false); expect(queued).toHaveLength(1);
    busy = true;
    controller.observe(new Set([queued[0].token]), 1, 1, []);
    expect(await first).toEqual(await second);
    expect(result(await call("submit", p)).state).toBe("queued");
    expect(await call("submit", { ...p, idempotency_key: "new-key" })).toMatchObject({ error: { code: "busy" } });
    expect(await call("submit", { ...p, preview_ref: "another" })).toMatchObject({ error: { code: "idempotency_conflict" } });
  });
  it("confirms cancellation only after an absent committed queue observation", async () => {
    const p = await prepared(), abort = new AbortController(); let settled = false;
    const pending = call("submit", p, abort.signal).then(r => { settled = true; return r; });
    abort.abort(); await Promise.resolve(); expect(settled).toBe(false);
    controller.observe(new Set(), 1, 1, []);
    expect(await pending).toMatchObject({ error: { code: "cancelled_before_publication" } });
  });
  it("does not withdraw observed queue publication on disconnect", async () => {
    const p = await prepared(), abort = new AbortController(); const pending = call("submit", p, abort.signal);
    controller.observe(new Set([queued[0].token]), 1, 1, []); abort.abort();
    expect(result(await pending).state).toBe("queued"); expect(queued).toHaveLength(1);
  });
  it("expires a stale queued entry even while its old UI row remains", async () => {
    const p = await prepared(), pending = call("submit", p); const token = queued[0].token;
    controller.observe(new Set([token]), 1, 1, []); await pending;
    snapshot = { ...snapshot, revision: 2 };
    controller.observe(new Set([token]), 1, 2, []);
    expect(result(await call("submit", p))).toMatchObject({ state: "expired", reason: "stale_basis" });
    expect(await call("submit", { ...p, idempotency_key: "other" })).toMatchObject({ error: { code: "stale_basis" } });
  });
  it("retains an immutable observed commit across project replacement while its canonical hash is delayed", async () => {
    const p = await prepared(), pending = call("submit", p); const a = queued[0];
    controller.observe(new Set([a.token]), 1, 1, []); const ticket = result(await pending).ticket;
    const applied = await batches.applyOperationBatch(a.model, a.batch, a.hash);
    expect(applied.applied_model).not.toBeNull();
    const after = applied.applied_model!, expectedHash = await hashes.computeModelHash(after);
    const wait = deferred<typeof expectedHash>();
    vi.spyOn(hashes, "computeModelHash").mockReturnValueOnce(wait.promise);
    controller.observe(new Set(), 1, 2, [{ token: a.token, model: after, revision: 2, undoCheckpointId: "undo-actual", appliedReceiptId: "applied-actual", batchReceiptId: "batch-actual" }]);
    expect(await call("status", { workspace: p.workspace, ticket })).toMatchObject({ error: { code: "not_ready" } });
    snapshot = { ...snapshot, generation: 2, revision: 3, model: { ...snapshot.model, project: { ...snapshot.model.project, id: "another-project" } } };
    controller.observe(new Set(), 2, 3, []);
    after.nodes[0].position.x += 100; // independent later mutation cannot rewrite retained snapshot/hash
    wait.resolve(expectedHash); await wait.promise; await Promise.resolve();
    const recovered = result(await call("submit", p));
    expect(recovered.state).toBe("committed");
    expect(recovered.receipt.after).toEqual({ model_revision: 2, model_hash: expectedHash });
    expect(recovered.receipt.identity.project_generation).toBe(1);
    expect(recovered.receipt.publication).toMatchObject({ undo_checkpoint_id: "undo-actual", batch_receipt_id: "batch-actual", queue_entry_removed: true, computed_results_invalidated: true });
  });
  it("rejects extra caller attribution and mismatched validation outcomes", async () => {
    const workspace = result(await call("inspect", { scope: "workspace" })).workspace;
    const nodes = result(await call("inspect", { scope: "nodes", workspace, node_ids: [snapshot.model.nodes[0].id] }));
    expect(await call("preview", { workspace, basis: nodes.basis, changes: [], author_type: "user" })).toMatchObject({ error: { code: "invalid_request" } });
    const actual = batches.validateOperationBatch;
    vi.spyOn(batches, "validateOperationBatch").mockImplementation(async (...args) => ({ ...await actual(...args), batch_id: "wrong" }));
    await expect(prepared()).rejects.toThrow("internal_error");
  });
  it("does not turn partial application publication into stale-basis expiry", async () => {
    const p = await prepared(), pending = call("submit", p), a = queued[0];
    controller.observe(new Set([a.token]), 1, 1, []); await pending;
    controller.beginApply(a.token);
    controller.observe(new Set(), 1, 2, []);
    expect(result(await call("submit", p))).toMatchObject({ state: "outcome_unknown", reason: "application_publication_unconfirmed", receipt: null });
  });
  it("retains and retries the same observed snapshot after canonical hash failure", async () => {
    const p = await prepared(), pending = call("submit", p), a = queued[0];
    controller.observe(new Set([a.token]), 1, 1, []); await pending;
    const outcome = await batches.applyOperationBatch(a.model, a.batch, a.hash);
    const expectedHash = await hashes.computeModelHash(outcome.applied_model!);
    const spy = vi.spyOn(hashes, "computeModelHash").mockRejectedValueOnce(new Error("controlled unavailable hash"));
    controller.observe(new Set(), 1, 2, [{ token: a.token, model: outcome.applied_model!, revision: 2, undoCheckpointId: "u", appliedReceiptId: "a", batchReceiptId: "b" }]);
    await Promise.resolve(); await Promise.resolve();
    snapshot = { ...snapshot, generation: 2, revision: 3 };
    expect(result(await call("submit", p))).toMatchObject({ state: "outcome_unknown", reason: "observed_commit_hash_unavailable" });
    await vi.waitFor(async () => expect(result(await call("submit", p))).toMatchObject({ state: "committed", receipt: { after: { model_hash: expectedHash } } }));
    expect(spy).toHaveBeenCalledTimes(2);
    expect(spy.mock.calls[0][0]).toEqual(spy.mock.calls[1][0]);
  });
  it("rejects a preview whose frozen basis changes while engine validation waits", async () => {
    const actual = batches.validateOperationBatch;
    const wait = deferred<void>(), started = deferred<void>();
    vi.spyOn(batches, "validateOperationBatch").mockImplementation(async (...args) => { const outcome = await actual(...args); started.resolve(); await wait.promise; return outcome; });
    const preparing = prepared();
    await started.promise;
    snapshot = { ...snapshot, revision: 2 };
    wait.resolve();
    await expect(preparing).rejects.toThrow("stale_basis");
    expect(queued).toHaveLength(0);
  });
  it("keeps an invalid later atomic member out of the queue and source model", async () => {
    const before = structuredClone(snapshot.model);
    const workspace = result(await call("inspect", { scope: "workspace" })).workspace;
    const inspected = result(await call("inspect", { scope: "nodes", workspace, node_ids: [snapshot.model.nodes[0].id] }));
    const node = inspected.nodes[0];
    const change = { target: { object_type: "Node", ref: node.id }, field_path: "position.x", before: String(node.position.x), after: String(node.position.x + 0.01), unit: inspected.length_unit, dimension: "length" };
    const preview = result(await call("preview", { workspace, basis: inspected.basis, changes: [change, { ...change, before: "999999" }] }));
    expect(preview).toMatchObject({ validation: "blocked", preview_ref: null });
    expect(snapshot.model).toEqual(before); expect(queued).toHaveLength(0);
  });

  it("settles unpublished submission on retirement without replay or recursive recovery", async () => {
    const p = await prepared();
    const first = call("submit", p), joined = call("submit", p);
    expect(queued).toHaveLength(1);
    controller.retire();
    expect(result(await first)).toMatchObject({ state: "outcome_unknown", reason: "controller_retired" });
    expect(await joined).toEqual(await first);
    controller.bind("app-test");
    expect(result(await call("submit", p))).toMatchObject({ state: "outcome_unknown", reason: "controller_retired" });
    expect(queued).toHaveLength(1);
  });

});
