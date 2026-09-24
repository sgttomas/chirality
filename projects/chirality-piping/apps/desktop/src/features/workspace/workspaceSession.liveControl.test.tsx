import { act, renderHook, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { LiveControlController } from "./liveControlController";
const capture = vi.hoisted(() => ({ controller: null as LiveControlController | null }));
vi.mock("../../services/liveControlBridge", () => ({ startLiveControlBridge: (controller: LiveControlController) => { capture.controller = controller; controller.bind("app-hook"); return () => controller.retire(); } }));
import { useWorkspaceSession } from "./workspaceSession";
import * as hashService from "../../services/hashService";
import type { LiveResponse } from "./liveControlTypes";
function value(response: LiveResponse): Record<string, any> { if ("error" in response) throw new Error(JSON.stringify(response.error)); return response.result as Record<string, any>; }
function request(method: string, params: unknown, signal = new AbortController().signal) {
  const controller = capture.controller!;
  return controller.request({ controller_session_id: controller.sessionId, app_instance_id: "app-hook", registration_id: "reg-hook", dispatch_id: crypto.randomUUID(), request_id: crypto.randomUUID(), method, params }, signal);
}
async function ready() {
  const hook = renderHook(() => useWorkspaceSession());
  await waitFor(() => expect(hook.result.current.model.modelHash).not.toBeNull());
  return hook;
}
async function prepare(nodeIds: string[]) {
  const workspace = value(await request("inspect", { scope: "workspace" })).workspace;
  const nodes = value(await request("inspect", { scope: "nodes", workspace, node_ids: nodeIds }));
  const preview = value(await request("preview", { workspace, basis: nodes.basis, changes: nodes.nodes.map((node: any) => ({ target: { object_type: "Node", ref: node.id }, field_path: "position.x", before: String(node.position.x), after: String(node.position.x + 0.01), unit: nodes.length_unit, dimension: "length" })) }));
  expect(preview.validation).toBe("passed");
  return { workspace, preview_ref: preview.preview_ref, idempotency_key: crypto.randomUUID() };
}
afterEach(() => { vi.restoreAllMocks(); capture.controller = null; window.localStorage.clear(); });
describe("hook-owned committed live publication", () => {
  it.each([1, 2])("observes %i-member atomic Apply with one checkpoint and local receipt, then Undo expires old basis", async count => {
    const hook = await ready();
    const initial = structuredClone(hook.result.current.model.model!);
    const p = await prepare(initial.nodes.slice(0, count).map(n => n.id));
    let pending!: Promise<LiveResponse>, settled = false;
    act(() => { pending = request("submit", p).then(r => { settled = true; return r; }); expect(settled).toBe(false); });
    const queued = value(await pending); expect(queued.state).toBe("queued");
    expect(hook.result.current.operations.queuedBatches).toHaveLength(1);
    expect(hook.result.current.operations.undoStack).toHaveLength(0);
    const entry = hook.result.current.operations.queuedBatches[0];
    await act(async () => { await hook.result.current.operations.handleRunOperationBatch(entry, true); });
    let committed: Record<string, any> | undefined;
    await waitFor(async () => { const response = await request("status", { workspace: p.workspace, ticket: queued.ticket }); expect("result" in response).toBe(true); committed = value(response); expect(committed.state).toBe("committed"); });
    expect(hook.result.current.operations.undoStack).toHaveLength(1);
    expect(hook.result.current.operations.redoStack).toHaveLength(0);
    expect(hook.result.current.operations.queuedBatches).toHaveLength(0);
    expect(hook.result.current.operations.batchReceipts[0].liveReceiptId).toBe(committed!.receipt.publication.batch_receipt_id);
    expect(hook.result.current.results.result).toBeNull();
    expect(hook.result.current.results.analysisRun).toBeNull();
    expect(hook.result.current.results.inputManifest).toBeNull();
    expect(hook.result.current.results.ruleCheckAggregate).toBeNull();
    act(() => hook.result.current.operations.handleUndoSessionModelEdit());
    await waitFor(() => expect(hook.result.current.model.modelHash).not.toBeNull());
    expect(hook.result.current.model.model).toEqual(initial);
    expect(value(await request("submit", p)).state).toBe("committed");
    expect(await request("submit", { ...p, idempotency_key: "new-after-undo" })).toMatchObject({ error: { code: "stale_basis" } });
  });
  it.each(["undo", "project"] as const)("retains observed commit while its after hash waits across immediate %s", async next => {
    const hook = await ready();
    const p = await prepare([hook.result.current.model.model!.nodes[0].id]);
    let pending!: Promise<LiveResponse>;
    act(() => { pending = request("submit", p); }); const ticket = value(await pending).ticket;
    const entry = hook.result.current.operations.queuedBatches[0];
    const targetX = Number(entry.batch.operations[0].change.after);
    const actual = hashService.computeModelHash;
    let callsWithAfter = 0, release!: () => void;
    const delayed = new Promise<void>(resolve => { release = resolve; });
    let observedModel: unknown;
    vi.spyOn(hashService, "computeModelHash").mockImplementation(async model => {
      if (model.nodes[0]?.position.x === targetX && ++callsWithAfter === 2) {
        observedModel = structuredClone(model);
        await delayed;
      }
      return actual(model);
    });
    await act(async () => { await hook.result.current.operations.handleRunOperationBatch(entry, true); });
    expect(observedModel).toBeDefined();
    expect(await request("status", { workspace: p.workspace, ticket })).toMatchObject({ error: { code: "not_ready" } });
    if (next === "undo") act(() => hook.result.current.operations.handleUndoSessionModelEdit());
    else await act(async () => { await hook.result.current.project.handleCreateBlankProject(); });
    release();
    await waitFor(async () => expect(value(await request("submit", p)).state).toBe("committed"));
    const recovered = value(await request("submit", p));
    expect(recovered.receipt.after.model_hash).toEqual(await actual(observedModel as Parameters<typeof actual>[0]));
    expect(recovered.receipt.identity.project_id).toBe(entry.basisModel.project.id);
  });
  it("withdraws only an observed queue on Clear and expires pending work on project replacement", async () => {
    const hook = await ready(); const p = await prepare([hook.result.current.model.model!.nodes[0].id]);
    let pending!: Promise<LiveResponse>;
    act(() => { pending = request("submit", p); }); await pending;
    act(() => hook.result.current.operations.handleClearReviewQueue());
    expect(value(await request("submit", p)).state).toBe("withdrawn");
    const next = await prepare([hook.result.current.model.model!.nodes[0].id]);
    act(() => { pending = request("submit", next); }); await pending;
    await act(async () => { await hook.result.current.project.handleCreateBlankProject(); });
    expect(value(await request("submit", next))).toMatchObject({ state: "expired", reason: "workspace_replaced" });
    expect(hook.result.current.operations.queuedBatches).toHaveLength(0);
  });
});
